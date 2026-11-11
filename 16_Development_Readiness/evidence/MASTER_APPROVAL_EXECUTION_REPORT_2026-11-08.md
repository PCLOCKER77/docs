# Master approval execution report — 2026-11-08

**Authority:** User master instruction (eight binding decisions) + [MASTER_REMAINING_BLOCKERS_APPROVAL_PACKAGE_2026-11-08.md](./MASTER_REMAINING_BLOCKERS_APPROVAL_PACKAGE_2026-11-08.md)

## 1. Decisions applied

| # | Decision | Action |
| --- | --- | --- |
| 1 | Support escalation | Migration **083**, route **API-12-008**, Flutter panel, tests |
| 2 | Razorpay sandbox | **`RAZORPAY_MODE=sandbox`** accepted in settings; `RazorpayGateway.is_mock` excludes sandbox; facility billing remains mock-only |
| 3 | Email / schedules | `SmtpReportNotifier` + `resolve_report_notifier`; worker uses Mailpit when `SMTP_HOST` + `EMAIL_FROM` set |
| 4 | SMS / OTP | **Deferred first release** — recorded in DEV-21 |
| 5 | Statutory invoice | **No issuance** — blockers preserved; legal package unchanged |
| 6 | Cheque bounce | **No automation** — unit tests on existing `bounce_cheque_payment`; product decision doc below |
| 7 | EQ-011 local | **`digitize_test` @ localhost** upgraded to **083**; preflight **READY** |
| 8 | Product deferrals | Preserved — documented only |

## 2. Implemented gaps and primary files

| Gap | Files |
| --- | --- |
| GAP-API12-001 / API-12-008 / JRN-012 | `migrations/sql/083_*`, `escalation_service.py`, `routes.py`, `ticket_escalation.py`, Flutter `support_ticket_escalation_panel.dart` |
| GAP-INT-002 / GAP-API11-001 | `report_email_delivery.py`, `worker.py` |
| GAP-INT-004 / sandbox | `settings.py`, `commerce/razorpay.py` |
| GAP-API09-005 (partial) | `tests/billing/test_cheque_bounce_service.py` |
| GAP-QA-001 (local) | `digitize_test` migration run; preflight head `083` |

## 3. Tests executed

| Suite | Command | Result |
| --- | --- | --- |
| Escalation + routes + reports + cheque unit | `pytest tests/support/test_escalation_service.py tests/reports/test_report_email_delivery.py tests/billing/test_cheque_bounce_service.py tests/api/test_module_routes.py -q` | **22 passed** |
| Support PG IV | `DIGITIZE_SUPPORT_PG_TEST=1 DB_NAME=digitize … test_support_tickets_digitize_postgres.py` | **1 passed** (incl. escalate row) |
| Report worker | `pytest tests/reports/test_report_schedule_worker.py -q` | **3 passed** |
| Flutter support | `flutter test test/features/support_tickets/` | **11 passed** |
| EQ-011 API-09 HTTP | `DIGITIZE_API_TEST=1 DB_NAME=digitize_test … test_subscription_license.py` | **49 passed, 13 failed, 1 skipped** |

## 4. Sandbox integrations verified

- **Razorpay live/sandbox HTTP:** **Not executed** — no sandbox transaction run in this session (mock paths unchanged; `RAZORPAY_MODE` default remains `mock`).
- **Mailpit SMTP delivery:** **Not end-to-end verified** — resolver tests pass; live Mailpit send requires local Mailpit on configured host/port (typically `127.0.0.1:1025`).

## 5. Local `digitize_test`

| Check | Result |
| --- | --- |
| Host / name | `localhost` / `digitize_test` (preflight) |
| Alembic after upgrade | `083_support_ticket_escalation` |
| Preflight | **READY** |

## 6. EQ-011 — reconciled (2026-11-08)

Local `digitize_test` subscription + platform catalog suite: **73 passed, 1 skipped**. See [EQ011_POST_MIGRATION_RECONCILIATION_2026-11-08.md](./EQ011_POST_MIGRATION_RECONCILIATION_2026-11-08.md).

## 6a. EQ-011 failures (historical — pre-reconciliation)

Failures in `test_subscription_license.py` on fresh `digitize_test` head are predominantly **fixture/catalog drift** (e.g. `test_catalog_endpoints_still_work` expects **8** license capabilities, DB has **9** after migrations). Requires seed/expectation alignment or refreshed EQ-011 fixtures — **not** shared QA certification.

## 7. Still blocked

| Item | Dependency |
| --- | --- |
| GAP-API09-002 statutory issue | Legal sign-off INV-001…003 |
| Production Razorpay | Production program + credentials |
| Production email (SES) | Production SMTP authorization |
| GAP-API01-002 shared QA | Shared-environment owner |
| GAP-API09-005 automation | Grace days, suspend job, PA override HTTP — product decisions |
| API-05/07/13/14 deferrals | Unchanged |

## 8. Product deferrals (first release)

- **GAP-INT-001** SMS / SMS OTP — out of scope; manual WhatsApp unchanged.
- **GAP-API05-001, API-07-*, API-13/14, GAP-ROLE-002, GAP-API02-004** — preserved.

## 9. Cheque bounce — remaining product decision

Record for GAP-API09-005:

1. Configurable **grace period days** after bounce.
2. **Notification** schedule during grace.
3. **Auto-suspend** subscription trigger conditions.
4. **PA override** API contract (if distinct from existing suspend/activate).

Internal `PaymentTransactionService.bounce_cheque_payment` is **implemented**; HTTP/grace/suspend remain **disabled**.

## 10. Engineering vs product readiness

| Lens | Status |
| --- | --- |
| **Authorized engineering (this instruction)** | **Largely complete** — escalation, Mailpit wiring, local EQ-011 schema, deferrals recorded |
| **Product / launch readiness** | **Incomplete** — statutory invoice, production providers, shared QA, cheque automation, EQ-011 full green on `digitize_test` |
