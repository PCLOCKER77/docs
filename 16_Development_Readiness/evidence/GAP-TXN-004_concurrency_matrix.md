# GAP-TXN-004 — Database concurrency integration matrix (2026-11-03, updated)

**Database identity (execution):** `host=localhost`, `port=5434` (from `DB_PORT` / settings), `database=digitize`, `ENVIRONMENT=development`, loopback only.

Opt-in flag: **`DIGITIZE_TXN004_PG_TEST=1`** (refund + webhook IV). Payment concurrency retains **`DIGITIZE_OFFLINE_PAYMENT_CONCURRENCY_PG_TEST=1`**.

**`digitize_test` is prohibited** (EQ-011). No full-database truncate was required for this pass — tests insert tagged rows and delete in teardown.

| Scenario | Risk | Evidence file | Sessions | Result |
|----------|------|---------------|----------|--------|
| Two sessions collect same invoice | Double SUCCESS payment | `test_offline_payment_invoice_lock.py` | 2 | **IV pass** (opt-in) |
| Concurrent full refund same payment | Double refund | `test_refund_concurrency_postgres.py::test_pg_concurrent_full_refunds_single_success` | 2 | **IV pass** — 1× SUCCESS refund ₹500, 1× `InvalidStateError`, audit count 1 |
| Same refund idempotency key concurrent | Duplicate refund row | `test_refund_concurrency_postgres.py::test_pg_concurrent_refund_same_idempotency_key` | 2 | **IV pass** — one refund row, same `refund_id` replay |
| Different refund keys, partial amounts | Over-refund | `test_refund_concurrency_postgres.py::test_pg_concurrent_partial_refunds_cap_total` | 2 | **IV pass** — total SUCCESS refunds ₹300 |
| Same webhook event concurrent | Double verify | `test_saas_webhook_concurrency_postgres.py::test_pg_concurrent_same_webhook_event_applied_once` | 2 | **IV pass** — 1× `applied`, 1× `duplicate`, one event row, attempt `VERIFIED` |
| Webhook replay after success | Repeat mutation | `test_saas_webhook_concurrency_postgres.py::test_pg_duplicate_webhook_after_success_is_noop` | 2 sequential | **IV pass** — `duplicate`, single event |
| Webhook retry after rollback | Lost or double apply | `test_saas_webhook_concurrency_postgres.py::test_pg_webhook_retry_after_rollback_processes_once` | 2 sequential | **IV pass** — rollback then single `applied` |
| Duplicate SaaS webhook (unit) | Double apply | `test_saas_commerce_service.py::test_duplicate_webhook_is_idempotent` | mocked | **Tested** |
| Notification worker claim | Double delivery | `test_notification_worker_claim.py` | unit SQL | **Tested** (`SKIP LOCKED`) |
| Trainer schedule | Double booking | `test_trainer_schedule_concurrency_postgres.py` | 2 | **IV** (dedicated `digitize_trainer_concurrency`) |

## Production fix (concurrency)

Concurrent webhook insert race: `SaasCommerceService.handle_webhook` catches unique violation on `saas_provider_event` and returns **`duplicate`** (same as sequential replay).

## Rollback scope verification (2026-11-03)

**Route:** `POST /api/v1/.../webhooks/razorpay` → `get_session` → `handle_webhook` only (no earlier DB writes in that request).

**Order inside `handle_webhook`:** read `event_by_provider_id` → (optional) insert `saas_provider_event` → **only then** attempt/obligation/`_mark_verified` mutations.

**`session.rollback()` on unique violation:** rolls back the **current request session** transaction. On the production webhook route that transaction contains only the failed event insert attempt at that point—no subscription, obligation, or audit writes have run yet in the losing session. The winning session is a separate connection and is unaffected.

**Unrelated pending work:** Not applicable on the registered route. Scenario B (duplicate handling with unrelated pending work in the same transaction) is **N/A** for production HTTP webhooks.

**After duplicate return:** `get_session` still runs `UnitOfWork.commit()` on success, persisting the loser's `processing_status = DUPLICATE` marker on the existing event row (separate commit from winner).

**Tests:** `test_saas_webhook_rollback_scope_postgres.py` (PG on `digitize`); route isolation unit check `test_webhook_route_has_no_pre_session_database_work`.

## How to run

```bash
cd digitize-services
export ENVIRONMENT=development
export DB_NAME=digitize
export DB_HOST=localhost
export DIGITIZE_TXN004_PG_TEST=1
poetry run pytest tests/billing/test_refund_concurrency_postgres.py \
  tests/subscription/test_saas_webhook_concurrency_postgres.py -v

export DIGITIZE_OFFLINE_PAYMENT_CONCURRENCY_PG_TEST=1
poetry run pytest tests/billing/test_offline_payment_invoice_lock.py -k pg_ -v
```

## Remaining limitation

Multi-**process** notification worker duplicate-claim IV is not run on `digitize` (SQL-level `SKIP LOCKED` covered in unit test).
