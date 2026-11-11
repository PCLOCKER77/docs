# GAP-API09-005 — Cheque bounce grace and facility suspension (implementation)

**Date:** 2026-11-09  
**Status:** **IMPLEMENTED** — **development database deployed and worker verified** (QA / production / `digitize_test` not claimed)

## Approved rules implemented

| Rule | Implementation |
|------|----------------|
| Default 7 calendar days | `DEFAULT_CHEQUE_BOUNCE_GRACE_DAYS = 7`; migration seeds `platform.platform_setting` key `CHEQUE_BOUNCE_GRACE_PERIOD_DAYS` |
| PA configurable (prospective) | Reuses **API-01** `platform_settings_update`; validation on `days` 1–365; existing grace rows keep snapshotted `grace_period_days` + `policy_snapshot` |
| Snapshot per obligation | `billing.cheque_bounce_grace` created on confirmed bounce (`start_on_cheque_bounce`), idempotent on `payment_id` |
| Bounce starts grace | Hooked from `PaymentTransactionService.bounce_cheque_payment` after FAILED transition |
| Facility scope from allocations | `affected_facility_ids`: distinct `invoices.facility_id` via `payment_allocations`; fallback `payments.facility_id` / invoice when no allocation rows |
| Expiry suspends facilities only | Worker + `process_expiry` → `SubscriptionService.suspend` per affected facility (SaaS subscription), not organization |
| Full settlement reactivation | `try_resolve_after_settlement` on invoice **PAID** + zero effective outstanding; reactivates only facilities this grace suspended |
| Partial settlement | No auto-reactivate (`INVOICE_STATUS_PAID` required) |
| PA override (audit) | `ChequeBounceGraceService.platform_waive_grace` — **service only**; see proposed API below |
| Payment lifecycle unchanged | PENDING / SUCCESS / FAILED paths untouched |
| Scheduler pattern | `scripts/run_cheque_bounce_grace_worker.py` → `run_cheque_bounce_grace_expiry_tick` (external scheduler, same class as reports/notifications) |

## Code and migrations

| Artifact | Path |
|----------|------|
| SQL twin | `digitize-services/migrations/sql/084_cheque_bounce_grace.sql` |
| Alembic | `digitize-services/migrations/versions/084_cheque_bounce_grace.py` |
| Models | `app/modules/billing/models/cheque_bounce_grace.py` |
| Policy (expiry math + validation) | `app/modules/billing/cheque_bounce_grace_policy.py` |
| Service | `app/modules/billing/cheque_bounce_grace_service.py` |
| Repository | `app/modules/billing/cheque_bounce_grace_repository.py` |
| Worker | `app/modules/billing/cheque_bounce_grace_worker.py` |
| Operator script | `scripts/run_cheque_bounce_grace_worker.py` |

## API operations reused

- **API-01-002** `platform_settings_update` — grace duration (`CHEQUE_BOUNCE_GRACE_PERIOD_DAYS`, JSON `{"days": N}`)
- **API-09** `platform_facility_subscription_suspend` / `platform_facility_subscription_activate` — same lifecycle + audit as manual PA ops (worker uses internal `SubscriptionService` with SYSTEM org principal)

## Proposed API (not implemented — awaiting approval)

| Proposed operation | Why |
|--------------------|-----|
| `POST /api/v1/platform/cheque-bounce-grace/{grace_id}/waive` | Expose `platform_waive_grace` with PA auth + reason; no existing numbered operation targets grace records |

Until approved, PA may waive via direct service/operator tooling in controlled environments, or reactivate subscription manually with existing platform activate + separate grace data fix (not recommended for production).

## Expiry boundary (recorded decision)

- **Convention used:** UTC **calendar** days; `grace_expires_at` = 00:00:00 **UTC** on the date `bounce_date + N` days (grace active while `now < grace_expires_at`).
- **Open product question:** Tenant-local calendar boundary (e.g. Asia/Kolkata) is **not** defined elsewhere in billing; using UTC unless product specifies a tenant timezone source of truth.

## Tests executed

```text
python3 -m pytest tests/billing/test_cheque_bounce_grace.py tests/billing/test_cheque_bounce_service.py tests/migrations/test_sql_twin.py -q
# 16 passed
```

Coverage includes: default 7 days, validation, expiry math, idempotent grace start, allocation-based facilities, partial vs paid resolve, pre-expiry no-op, platform setting key constant.

**Not run this session:** `digitize_test` Postgres integration IV; shared QA worker schedule deployment.

## Development deployment verification (2026-11-09)

### Preflight

| Check | Result |
|-------|--------|
| Target | `ENVIRONMENT=development`, database name **`digitize`** (`app.config.db_config.DEVELOPMENT_DATABASE`), host `localhost` |
| Alembic before upgrade | `083_support_ticket_escalation` |
| Head / chain | `084_cheque_bounce_grace` revises `083_support_ticket_escalation` |
| Migration artifact | `migrations/sql/084_cheque_bounce_grace.sql` present |
| Worker script | `scripts/run_cheque_bounce_grace_worker.py` (aligned with notification worker session pattern after deploy fix) |

### Migration

```text
poetry run alembic upgrade head
# Running upgrade 083_support_ticket_escalation -> 084_cheque_bounce_grace
```

| Check | Result |
|-------|--------|
| Alembic after upgrade | `084_cheque_bounce_grace` |
| `billing.cheque_bounce_grace` | present |
| `billing.cheque_bounce_grace_facility` | present |
| `CHEQUE_BOUNCE_GRACE_PERIOD_DAYS` | `{"days": 7}`, `is_active=true` |
| Existing data | `billing.payments` count **55**, `commercial.subscription` count **66** (unchanged post-migrate) |
| New grace data | **0** rows (expected pre–live-bounce) |

### Worker (development)

```text
poetry run python scripts/run_cheque_bounce_grace_worker.py
# Worker tick complete: {'due_count': 0, 'processed_count': 0, ...}
# exit code 0
```

Second immediate run: same `due_count=0`, `processed_count=0`, exit **0** (no duplicate processing).

| Check | Result |
|-------|--------|
| DB connectivity | Uses `Settings().DATABASE_URL` (same as API / Alembic) |
| Due expired ACTIVE graces | **0** — nothing suspended |
| Idempotent re-run | Confirmed (two ticks, no schema/data drift) |

**Deploy fix (script only):** initial worker entrypoint incorrectly used `UnitOfWork()` as a context manager; corrected to `init_engine(settings=settings)` + `get_async_session()` + explicit `session.commit()` (same as `scripts/run_notification_worker.py`). No change to grace business logic.

**Lifecycle on dev:** No synthetic bounce/grace rows were inserted; controlled verification is empty-queue + schema/setting proof. End-to-end bounce→grace→expiry→suspend on shared PG remains for a future IV when dev data exists.

### Recurring execution (development)

No in-repo cron, ECS task, or local scheduler configuration exists (same as `run_notification_worker.py` — external operator responsibility per API-10 Phase 9).

**Recommended when wiring ops (not configured in this task):**

- **Command:** `cd digitize-services && poetry run python scripts/run_cheque_bounce_grace_worker.py`
- **Frequency:** short interval (e.g. **5–15 minutes**) so expiry is near real time; retry = next scheduled tick (idempotent `SKIP LOCKED` selection)
- **Logging:** stdout `INFO` `cheque_bounce_grace.worker` — `due_count` / `processed_count`
- **Disable:** remove cron/task entry; API grace creation unaffected, only expiry processing stops

## Remaining / blocked

- Migration **084** on **QA**, **`digitize_test`**, and production (not executed in this task).
- Recurring worker schedule on development (no supported in-repo scheduler — manual/cron left to operator).
- Approve waive HTTP contract if PA UI needs in-product override without operator access.
- Independent suspension: reactivation only attempts facilities where `cheque_bounce_grace_facility.subscription_suspended_at` is set by this grace expiry path; other suspend reasons are not auto-cleared.
