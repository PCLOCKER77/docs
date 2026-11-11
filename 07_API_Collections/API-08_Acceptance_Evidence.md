# API-08 Billing / Payment — Acceptance Evidence

**Document ID:** API-08-EVIDENCE  
**Last updated:** 2026-11-09 (seven-area closure — backend vs acceptance matrix aligned)  
**Status:** PARTIALLY VERIFIED (Phase 1 live; **1** numbered skeleton remaining: API-08-005 adjustments)

This note records test-backed evidence for **facility operational billing** (API-08). It does not mark the collection INTEGRATED/CERTIFIED in the API registry. **API-09** SaaS subscription commerce remains a separate domain.

## Evidence legend

| Label | Meaning |
|-------|---------|
| **PASS** | Executed tests or live PostgreSQL IV cited below |
| **SKELETON** | Route in catalog; handler placeholder / blocked |
| **DEFERRED** | Product decision — see [API-08 facility billing register](../architecture/API-08_FACILITY_BILLING_DECISION_REGISTER.md) |
| **NOT VERIFIED** | No safe mutating IV on `digitize` for that claim |

## API-08 operation matrix (001–018)

| ID | Approved name | Path | Backend | Flutter | Tests | Final status |
|----|---------------|------|---------|---------|-------|--------------|
| API-08-001 | Generate Invoice | POST `/invoices` | **Implemented** — membership plan snapshot | Customer membership create/pay flow | `test_facility_membership_billing.py` | **Implemented** / **Tested** |
| API-08-002 | Calculate Service Charges | POST `/billing/charges/calculate` | **SKELETON** | — | Contract placeholder | **Deferred by product decision** |
| API-08-003 | Apply Discounts | POST `/invoices/{id}/discounts` | **SKELETON** | — | — | **Deferred by product decision** |
| API-08-004 | Calculate Taxes | POST `/invoices/{id}/taxes/calculate` | **SKELETON** | — | — | **Blocked (schema)** / Deferred |
| API-08-005 | Apply Billing Adjustments | POST `/invoices/{id}/adjustments` | **SKELETON** | — | — | **Deferred by product decision** |
| API-08-006 | Cancel Invoice | POST `/invoices/{id}/cancel` | **Implemented** | History + outstanding panels | membership + Flutter controller tests | **Implemented** / **Tested** |
| API-08-007 | Generate Credit Note | POST `/invoices/{id}/credit-notes` | **Implemented** | Outstanding/history (partial) | PG HTTP IV credit module | **Implemented** / **Integration-verified** (mig **080**–**081**) |
| API-08-008 | Collect Payment | POST `/payments` | **Implemented** — alias offline | Same as offline | `test_payment_collect_cancel.py` | **Implemented** / **Tested** |
| API-08-009 | Process Online Payment | POST `/payments/online` | **Implemented** (mock/sandbox gateway) | Outstanding online channel | PG M2 HTTP + webhook IV | **Integration-verified** (`digitize` mock); live capture **pending** human sandbox |
| API-08-010 | Record Offline Payment | POST `/payments/offline` | **Implemented** | Outstanding + membership | billing tests + live IV | **Implemented** / **Integration-verified** (live suite) |
| API-08-011 | Verify Payment Status | GET `/payments/{id}/status` | **Implemented** | Membership activate verify | `test_facility_membership_billing.py` | **Implemented** / **Tested** |
| API-08-012 | Generate Payment Receipt | POST `/payments/{id}/receipts` | **Implemented** | History shows `receipt_id` | `test_billing_credit_receipt_recon_http_digitize_postgres.py` + `test_receipt_backfill_service.py` | **Implemented** / **Integration-verified** (HTTP); facility receipt PDF UI **not** in scope |
| API-08-013 | Process Refund | POST `/payments/{id}/refunds` | **Implemented** — Phase 1 immediate SUCCESS | Billing history Refund | `test_refund*` + live IV | **Implemented** / **Integration-verified** |
| API-08-014 | Reconcile Payment | POST `/reconciliations` | **Implemented** (manual recon records) | — | Same PG module as 007 (mig **082**) | **Integration-verified** — non-mutating reconciliation |
| API-08-015 | Cancel Payment | POST `/payments/{id}/cancel` | **Implemented** — PENDING only | Billing history | `test_payment_collect_cancel.py` | **Implemented** / **Tested** |
| API-08-016 | View Billing and Payment History | GET `/billing/history` | **Implemented** — Phase 2 `financial_events` | Organization billing page | `test_billing_history*.py` + live IV | **Implemented** / **Tested** |
| API-08-017 | Generate Commercial Reports | GET `/commercial/reports` | **Implemented** — API-11 revenue alias | Reporting UI | contract + live revenue checks | **Implemented** / **Tested** |
| API-08-018 | Generate Outstanding Statement | GET `/billing/outstanding-statements` | **Implemented** — `batch_invoice_effective_outstanding` | Outstanding panel | `test_outstanding_statements.py`, `test_credit_note_financial_balance.py` + live IV | **Implemented** / **Integration-verified** |

**Phase 1 refund behavior (frozen):** API-08-013 records a **Digitize refund as SUCCESS immediately**; no external payment-provider refund execution.

## Live PostgreSQL integration (GAP-API08-009)

**Guard:** `DIGITIZE_BILLING_LIVE_VERIFICATION=1`, `ENVIRONMENT=development`, `DB_NAME=digitize`, loopback `DB_HOST`, no `DATABASE_URL` (`tests/billing/billing_digitize_pg_guard.py`).

**Suite:** `tests/billing/test_billing_invoices_revenue_live_digitize.py` — synthetic tagged rows (`digitize-iv-billing-*` prefix from `billing_digitize_pg_guard.py`), HTTP refund idempotency, cross-org **404**, audit count, **revenue delta vs pre-suite baseline** (same production `aggregate_customer_revenue` / report path; excludes unrelated Acme facility-A January payments on shared `digitize`), TAG-scoped `finally` cleanup, plus HTTP **history**, **outstanding**, **payment status**, **offline collect**, **cancel PENDING**.

**Repeatability (2026-11-04):** two consecutive opt-in runs on local `digitize` — **1 passed** each.

**Database:** local `digitize`; Alembic **repository head** `082_billing_manual_reconciliation` (074–082 chain + SQL twins); IV cleanup deletes allocation/reversal/receipt/txn children before refunds (2026-11-07 stabilization).

**Stabilization (2026-11-07):** Unit billing suite **47 passed** (7 skipped); live IV **1 passed** after cleanup fix; migration metadata tests `test_billing_evolution_074_082.py`.

## Phase 8 — effective outstanding + receipt backfill (2026-11-07)

| Item | Evidence |
|------|----------|
| API-08-018 parity (payments vs statements) | Shared helper `invoice_effective_outstanding_from_totals` / `batch_invoice_effective_outstanding`; **8** unit cases in `test_credit_note_financial_balance.py` |
| Historical SUCCESS receipt backfill (pre–offline-auto-receipt) | `ReceiptBackfillService` + `scripts/backfill_historical_payment_receipts.py`; unit **3 passed** in `test_receipt_backfill_service.py`; **no** bulk `execute` on shared `digitize` |
| Regression | `pytest tests/billing/ -q` → **56 passed**, 7 skipped; live IV **1 passed**; Flutter billing controllers **32 passed** |

**Not claimed:** API-08-012 HTTP route; production/QA backfill execution.

## Transaction safety

| Area | Evidence |
|------|----------|
| GAP-TXN-001 offline invoice lock | `get_invoice_for_update` + outstanding validation — `test_offline_payment_invoice_lock.py` (unit + opt-in PG) |
| Refund concurrency | `test_refund_concurrency_postgres.py` (opt-in PG) |
| GAP-TXN-004 webhook / rollback | Documented in DEV-19; separate from facility offline path |

## Dependency closure (verified in code/tests)

| Module | API-08 use |
|--------|------------|
| API-02 | Invoice/payment `organization_id` / `facility_id`; operational scope checks |
| API-03 | Permissions `billing.*`; principal attribution on audit |
| API-04 | Customer on membership invoices |
| API-05 | Membership invoice source; activate requires paid invoice |
| API-06 | Walk-in pay uses offline path where applicable — no duplicate billing engine |
| API-07 | No training charge engine in API-08 Phase 1 |
| API-09 | SaaS invoices/checkout on same billing **page** but separate routes/domain |
| API-10 | No unapproved receipt notification sends added |

## Flutter verification

| Workflow | Evidence |
|----------|----------|
| Outstanding collect / cancel invoice | `facility_outstanding_statements_controller_test.dart`, panel widgets |
| History refund / cancel payment | `facility_billing_history_controller_test.dart` |
| Membership pay + status verify | `customer_membership_section_test.dart`, remote repo |
| Remote serialization | `organization/remote_repository_test.dart` (billing paths) |

**Not claimed:** full Flutter app session against live FastAPI for every billing action.

## Regression commands (executed 2026-11-07 Phase 8)

```bash
cd digitize-services
python3 -m pytest tests/billing/ -q
# 56 passed, 7 skipped

DB_HOST=localhost DB_PORT=5434 DB_USER=digitize_app DB_PASSWORD='***' DB_NAME=digitize \
  ENVIRONMENT=development DIGITIZE_BILLING_LIVE_VERIFICATION=1 \
  python3 -m pytest tests/billing/test_billing_invoices_revenue_live_digitize.py -q
# 1 passed

cd digitize-ui
flutter test test/features/organization/facility_billing_history_controller_test.dart \
  test/features/organization/facility_outstanding_statements_controller_test.dart -r compact
```

## Acceptance checklist

| Criterion | Status |
|-----------|--------|
| 10/18 operations implemented (Phase 1) | **PASS** |
| 8 skeletons documented with justified status | **PASS** |
| Offline pay + allocation + invoice PAID | **PASS** |
| Refund Phase 1 + idempotency | **PASS** |
| Tenant isolation (refund cross-org) | **PASS** (live IV) |
| Live DB Phase 1 workflows | **PASS** (GAP-API08-009 closed) |
| Online gateway (009) | **BLOCKED** — authorization + schema |
| Credit notes / receipts / reconciliation | **BLOCKED** — schema/product |
| Full API-08 INTEGRATED/CERTIFIED | **BLOCKED** — registry process + skeletons |

## Out of scope (unchanged)

Facility GST/discount engines, credit notes, online Razorpay checkout, bank reconciliation, provider refund execution.
