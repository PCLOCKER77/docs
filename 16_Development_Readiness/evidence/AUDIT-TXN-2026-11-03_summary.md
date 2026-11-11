# Cross-module database transaction safety audit — summary

**Date:** 2026-11-03  
**Scope:** API-01 … API-14 (digitize-services)  
**Type:** Read-only audit; no schema/data/production changes  

## Authoritative transaction boundary

- HTTP/catalog routes: `app.api.deps.get_session` → yield `AsyncSession` → `UnitOfWork.commit()` on success; rollback + discard pending email/SMS/WhatsApp on exception; post-commit delivery flush.
- Repositories: `flush()` only; no commits (except documented exceptions below).
- Background ticks: caller-owned commit (e.g. `scripts/run_notification_worker.py`).

## Evidence executed (this audit)

| Suite | Result | Label |
| --- | --- | --- |
| `tests/attendance/test_denial_audit_and_tokens.py` | passed | Unit — denial txn vs request rollback |
| `tests/billing/test_refund_service.py` | passed | Unit — refund idempotency / balance rules |
| `tests/membership/test_membership_lifecycle.py` | passed | Unit — lifecycle transitions |
| Prior: `test_reports_export_http_digitize.py`, `DIGITIZE_REPORTING_SQL_TEST`, trainer concurrency (opt-in) | see DEV-19 | Mixed |

## Findings register

| ID | Class | Module | Summary |
| --- | --- | --- | --- |
| GAP-TXN-001 | **Fixed 2026-11-03** | API-08 | Invoice `FOR UPDATE` + outstanding validation in `OfflinePaymentService.record`; tests `test_offline_payment_invoice_lock.py` (opt-in PG on local `digitize`). |
| GAP-TXN-002 | **Implemented 2026-11-03** | Test harness | `asgi_session_helpers.py` + override inventory + UoW lifecycle tests |
| GAP-TXN-003 | **Implemented 2026-11-03** | API-03 / email | Outbox + `PasswordResetRequest` in request txn; post-commit SMTP; `_sync_password_reset_delivery_from_outbox` on SENT/FAILED; admin re-provision via `issue_account_credentials` / credential-reset API. Tests: `test_credential_email_txn003.py`. No durable outbox retry worker (recovery = re-issue). |
| GAP-TXN-004 | **Integration-verified 2026-11-03** | API-08 / API-09 / API-10 | Refund + webhook multi-session IV on local `digitize`; webhook unique-violation handling; rollback scope verified (no unrelated-work loss on production route). |
| GAP-TXN-005 | **Resolved 2026-11-03** | Scaffold | Routes not on `v1_router`; `UserRepository.create` no longer self-commits (flush only). Tests: `test_gap_txn005_scaffold.py`. |

Full module matrix and remediation notes: DEV-19 session log + DEV-21 gap rows.
