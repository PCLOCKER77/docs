# API-07 Trainer Management — Acceptance Evidence

**Document ID:** API-07-EVIDENCE  
**Last updated:** 2026-11-09  
**Status:** PARTIALLY VERIFIED (GAP-API07-004 closed; registry certification still open)

This note records **test-backed and read-only evidence** for API-07 Trainer Management. It does not mark the collection INTEGRATED/CERTIFIED in the API registry.

## Evidence legend

| Label | Meaning |
|-------|---------|
| **PASS** | Supported by executed tests or read-only inspection cited below |
| **NOT VERIFIED** | Insufficient evidence (mocks, no rows, or no safe DB test) |
| **BLOCKED** | Verification requires a prohibited operation (mutating `digitize`, new DB, migrations, etc.) |

## Frozen rules and evidence

| Rule / area | Status | Evidence |
|-------------|--------|----------|
| BR-TRN-004 | **PASS** | `tests/training/test_class_schedule_trainer.py`, `test_batch_schedule_trainer_requirements.py`, `test_trainer_organization_ownership.py` |
| BR-TRN-005 | **PASS** | `tests/training/test_trainer_availability_enforcement.py`; enforcement in `batch_ops_service`, `ptr_ops_service` |
| BR-TRN-008 | **PASS** | `tests/training/test_trainer_schedule_conflict_enforcement.py`, `test_batch_schedule_effective_trainer.py` |
| GAP-API07-002 facility/site resource conflict | **PASS** (unit + `digitize` PG sequential) | `test_facility_schedule_conflict.py`; extended `test_training_programs_digitize_postgres.py` (null vs site + site overlap `409`); **concurrency module added, NOT RUN** — `digitize_trainer_concurrency` missing |
| GAP-API07-001 batch enrollment list | **PASS** (PG on `digitize`) | Additive `GET .../enrollments` in GAP-API07-004 suite; Flutter reload |
| Org ownership / auth | **PASS** | `test_trainer_organization_ownership.py`; route permissions unchanged per contract tests |
| Advisory locks (code + unit) | **PASS** | `trainer_schedule_lock.py`; `test_trainer_schedule_lock.py`, `test_ptr_schedule_lock_wiring.py`, batch lock-order test |
| API contracts / routes | **PASS** | `tests/api/test_contract_registry.py`, `tests/api/test_module_routes.py` in regression suite |
| Flutter scheduling UX | **PASS** | `flutter test test/features/trainer/ test/features/training_operations/` — **40+** passed (2026-11-03 training_operations suite) |
| API-07-013 / API-07-030 Flutter | **PASS** | `activity_rules_and_progress_test.dart`; repository POST wiring |
| API-07-013 / API-07-030 backend services | **PASS** | `tests/training/test_activity_rules_and_progress.py` (5 tests) |
| GAP-API07-004 live PostgreSQL (local `digitize`) | **PASS** | `tests/training/test_training_programs_digitize_postgres.py` — trainer/activity/rules, batch/capacity/schedule, enroll/remove, optional attendance check-in, progress, API-07-024 GET performance, auth denial; cleanup scoped to `digitize-iv-training-*` prefix (`tests/digitize_iv_tag.py`) |
| HTTP 201 on training create POSTs | **PASS** | `_created_response` in `routes_ops.py`; trainer register `status_code=201`; `tests/api/test_success_envelope_jsonable.py` |

## Validation order (scheduling writes)

Organization/facility/trainer eligibility → effective trainer (class) → **advisory lock(s)** → BR-TRN-005 → BR-TRN-008 → persist → audit (same request transaction).

## Advisory locks

- **Mechanism:** `SELECT pg_advisory_xact_lock(:lock_id)` on the request `AsyncSession` (transaction-scoped; released on commit/rollback).
- **Order:** Before `enforce_trainer_availability_window` and `enforce_trainer_schedule_window` on `schedule_batch`, `book_session`, `assign_trainer_to_session`, `reschedule_session`.
- **Multi-trainer:** `trainers_for_ptr_trainer_change` + sorted UUID order.
- **Key:** `(907 << 52) | (trainer_id.int & ((1<<52)-1))` — documented non-collision-free lower-52-bit truncation.
- **Real PostgreSQL concurrent overlap:** **NOT VERIFIED** — opt-in module `test_trainer_schedule_concurrency_postgres.py` is guarded; must **not** run against `digitize`. No mutating concurrency run was performed in acceptance.

## Transaction and rollback

- **Design:** `get_session` yields one session; success → `UnitOfWork.commit()`; exception → rollback (`app/api/deps.py`, `app/infrastructure/database/uow.py`).
- **Audit:** `record_audit_event` uses `session.add` + `flush` only; commit with business writes.
- **Tests:** Mocked tests assert scheduling `create` not called on validation failure (`test_trainer_availability_enforcement.py`, `test_batch_schedule_trainer_requirements.py`).
- **Database rollback on failure:** **NOT VERIFIED** on PostgreSQL (no dedicated failure-path IV on `digitize`; scheduling validation failures covered by mocked tests only).

## GAP-API07-004 — End-to-end integration (2026-11-03)

**Database:** `digitize` @ localhost (development). **Alembic:** `072_platform_terms_document`. **Guard:** `DIGITIZE_TRAINING_PG_TEST=1` (legacy `DIGITIZE_API07_PG_TEST=1`), `ENVIRONMENT=development`, loopback `DB_HOST`, no `DATABASE_URL`. Guard module: `tests/training/training_digitize_pg_guard.py`.

**Workflows exercised (real ASGI + production `get_session`):**

| Workflow | Result |
|----------|--------|
| A — Trainer, activity, API-07-013 rules, scope negatives | **PASS** |
| B — Batch, trainer assignment, schedule (after availability window), capacity 422/200, GET batch/schedule, API-07-024 performance | **PASS** |
| C — Customer create (API-04), enroll, duplicate 409, over-capacity enroll (accepted per frozen behavior), remove | **PASS** |
| D — API-06 check-in | **PASS** when membership allows **201**; otherwise recorded as skipped status in run |
| E — API-07-030 progress persist + wrong-org **404** | **PASS** |
| F — Cross-module (Acme org/facility, permissions) | **PASS** |

**Not claimed:** full Flutter app session against live backend; PostgreSQL concurrent double-book (`test_trainer_schedule_concurrency_postgres.py`); audit row persistence proof on mutating IV.

**Product-deferred (not defects):** GAP-API07-001 list enrollments; GAP-API07-002 facility/site schedule conflicts.

### API-07-024 — Activity performance UI

`API_CONTRACT_REGISTRY.md` marks Flutter for API-07-024 as **NOT_APPLICABLE** / backend **BACKEND_IMPLEMENTED**. Facility-scoped analytics are exposed via GET `/api/v1/activities/{id}/performance` (IV **200**). Advanced reporting product path uses **API-11-007** (`POST /api/v1/reports/activity-performance`). No dedicated Flutter screen required by current registry decision.

## Audit persistence

### Code (same transaction)

- `record_audit_event` docstring: *"Insert one immutable audit.audit_event row. Caller owns commit."*
- Scheduling override: `apply_schedule_enforcement_after_mutation` → `record_schedule_conflict_override_audit` with action `OVERRIDE_TRAINER_SCHEDULE_CONFLICT`.
- Validate-only: `TrainerScheduleService.validate_conflicts` → `VALIDATE_TRAINER_SCHEDULE_CONFLICTS`.

### Tests (mock only)

- `test_successful_override_emits_audit_event` asserts mocked `record_audit_event` kwargs (action `OVERRIDE_TRAINER_SCHEDULE_CONFLICT`).
- `test_validate_conflicts_detects_overlap` mocks audit on validate path.
- **Mock tests do not prove rows in PostgreSQL.**

### Read-only inspection on development database `digitize` (2026-10-30)

Read-only queries only; no writes.

| Check | Result |
|-------|--------|
| `audit.audit_event` exists | **Yes** |
| Rows for `OVERRIDE_TRAINER_SCHEDULE_CONFLICT` | **0** |
| Rows for `VALIDATE_TRAINER_SCHEDULE_CONFLICTS`, `SCHEDULE_BATCH`, `BOOK_PERSONAL_TRAINING_SESSION` | **0** (grouped count query) |
| `training.trainer`, `training.trainer_availability`, `training.class_session` | **Present** |

**Conclusion:** Transaction integration is **PASS** by code review. **Row persistence for API-07 audit actions is NOT VERIFIED** on `digitize` (no historical rows to inspect; no mutating test run to create one).

## Regression commands (executed)

```bash
cd digitize-services
python3 -m pytest tests/training/ -q --ignore=tests/training/test_trainer_schedule_concurrency_postgres.py
# 2026-11-03: exit 0 — 76 passed, 1 skipped, 66 warnings

DB_HOST=localhost DB_PORT=5434 DB_USER=digitize_app DB_PASSWORD='***' DB_NAME=digitize \\
  ENVIRONMENT=development DIGITIZE_TRAINING_PG_TEST=1 \\
  python3 -m pytest tests/training/test_training_programs_digitize_postgres.py -q
# 2026-11-07: exit 0 — 1 passed (GAP-API07-004 re-verified; customer `primary_site_id` resolved from facility ACTIVE site)
# 2026-11-03: exit 0 — 1 passed (GAP-API07-004)

cd digitize-ui
flutter test test/features/training_operations/ -r compact
# 2026-11-03: exit 0 — 40 passed

flutter test test/features/trainer/ -r compact
# 2026-11-03: exit 0 — 10 passed (50 total training_operations + trainer when run together)
```

Training pytest modules use **mocked** `AsyncSession`; they do **not** connect to `digitize` during regression.

## Optional future PostgreSQL concurrency module

`tests/training/test_trainer_schedule_concurrency_postgres.py` remains opt-in with guard `trainer_schedule_concurrency_pg_guard.py` (dedicated DB name in guard — **not** `digitize`). Creating or using that database was **out of scope** for this verification pass per instruction to use `digitize` only for read-only inspection.

## Acceptance checklist

| Criterion | Status |
|-----------|--------|
| BR-TRN-004 / 005 / 008 enforced in code | **PASS** |
| Lock protocol on all scheduling writes | **PASS** (code + unit tests) |
| Contract/route regression | **PASS** |
| Flutter regression | **PASS** |
| Audit same-transaction design | **PASS** |
| Audit rows persisted in DB | **NOT VERIFIED** |
| PG concurrent double-book prevention | **NOT VERIFIED** |
| GAP-API07-004 training workflows on `digitize` | **PASS** |
| Full API-07 certification / INTEGRATED | **BLOCKED** (registry process; EQ-011 / optional concurrency + audit-row IV) |

## Out of scope (v1)

`assign_trainer_to_batch` time-window conflicts; BR-TRN-008 second approver; ON_LEAVE; facility-scoped availability; cross-org trainers.
