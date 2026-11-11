# API-08 — Facility billing remaining-skeleton decision register

**Status:** **Decision register** — API-08-005 **approved 2026-11-09** (facility adjustments); other rows may remain proposals. Does **not** supersede [SAAS_INVOICE_READINESS_DECISION_REGISTRY.md](SAAS_INVOICE_READINESS_DECISION_REGISTRY.md) (SaaS commerce).  
**Live today (10/18):** invoices create/cancel, payments collect (alias), offline, status, cancel (PENDING), refunds, billing history, outstanding statements, commercial reports.  
**Skeleton (8):** listed below. **Date:** 2026-11-02.  
**Tracker:** [DEV-19](../16_Development_Readiness/DEV-19_Feature_Completion_Tracker.md).

---

### API-08-002 `POST /billing/charges/calculate` (`billing_charges_calculate_create`)

| Field | Detail |
| --- | --- |
| Contract intent | Calculate service charges (FR-BPM-002) |
| Reusable | Walk-in charge calculate; membership invoice uses plan snapshot; SaaS quote preview is commercial |
| Missing rules | Facility “service charge” catalog undefined |
| Schema | No facility charge catalog table |
| External | None |
| Security / idempotency | Would need authz + optional Idempotency-Key if mutating |
| Safe now | Optional **read-only** membership/invoice total preview only if product confirms it is not walk-in |
| Approval needed | Product: charge model vs reuse plan price / walk-in |

### API-08-003 `POST /invoices/{id}/discounts` (`invoices_discounts`)

| Field | Detail |
| --- | --- |
| Contract intent | Apply discounts (FR-BPM-003) |
| Reusable | SaaS quote discount fields — **not** facility `billing.invoices` |
| Missing rules | When discounts allowed (DRAFT only?); stacking; audit |
| Schema | No discount history / column rewrite policy for ISSUED invoices |
| External | None |
| Security / idempotency | Facility scope; idempotency if mutating totals |
| Safe now | **Nothing mutating** without DRAFT lifecycle |
| Approval needed | Invoice lifecycle + discount persistence model |

### API-08-004 `POST /invoices/{id}/taxes/calculate` (`invoices_taxes_calculate`)

| Field | Detail |
| --- | --- |
| Contract intent | Calculate taxes (FR-BPM-004) |
| Reusable | SaaS GST policies; facility lines currently `tax_amount=0` |
| Missing rules | Facility tax policy / GST rates |
| Schema | `BillingSetting.tax_settings` ORM has **no migration** |
| External | None |
| Security / idempotency | Facility scope |
| Safe now | Read-only echo of existing zeros — weak contract fit |
| Approval needed | Tax policy source + whether recalculation may rewrite ISSUED invoices |

### API-08-005 `POST /invoices/{id}/adjustments` (`invoices_adjustments`) — **APPROVED 2026-11-09**

| Field | Detail |
| --- | --- |
| Contract intent | Apply billing adjustments (FR-BPM-005) |
| Approved model | `ADDITIONAL_CHARGE` and `CHARGE_REDUCTION`; compensating reversal; immutable posted history; distinct from credit/debit notes |
| Schema | `billing.facility_invoice_adjustments` (mig **086**) |
| Permissions | `billing.adjustment.post`, `billing.adjustment.reverse` |
| Outstanding | Net adjustments in `batch_invoice_effective_outstanding` |
| Not in scope | Statutory tax/accounting treatment |

### API-08-007 `POST /invoices/{id}/credit-notes` (`invoices_credit_notes`)

| Field | Detail |
| --- | --- |
| Contract intent | Generate credit note (FR-BPM-007) |
| Reusable | Refunds (API-08-013) are payment-side only |
| Missing rules | Credit note numbering, linkage to invoice/refund |
| Schema | Catalog **`database_gap=True`**; no credit-note tables |
| External | None |
| Safe now | **Cannot** implement without inventing tables |
| Approval needed | DDL + permission + relationship to refunds |

### API-08-009 `POST /payments/online` (`payments_online_create`)

| Field | Detail |
| --- | --- |
| Contract intent | Process online payment (FR-BPM-009) |
| Reusable | Walk-in Razorpay + SaaS payment-orders/verify patterns |
| Missing rules | Facility checkout UX; PENDING→SUCCESS; webhook ownership |
| Schema | `PaymentTransaction` ORM exists; **table not migrated** |
| External | Razorpay (no live gateway in this work) |
| Security / idempotency | Idempotency required (catalog); HMAC verify; tenant isolation |
| Safe now | Do **not** fake SUCCESS; PENDING-only without txn table is incomplete |
| Approval needed | Migrate `billing.payment_transactions` (+ secrets) and product checkout path |

### API-08-012 `POST /payments/{id}/receipts` (`payments_receipts`)

| Field | Detail |
| --- | --- |
| Contract intent | Generate payment receipt (FR-BPM-012) |
| Reusable | Payment status / history facts |
| Missing rules | Receipt number allocation; PDF vs JSON |
| Schema | `Receipt` ORM exists; **`billing.receipts` not migrated** |
| External | Optional PDF storage |
| Security / idempotency | Facility scope; unique `(organization_id, receipt_number)` |
| Safe now | Ephemeral DTO without persist is weak vs catalog DB entity |
| Approval needed | Migrate `billing.receipts` + numbering policy |

### API-08-014 `POST /reconciliations` (`reconciliations_create`)

| Field | Detail |
| --- | --- |
| Contract intent | Reconcile payment (FR-BPM-014) |
| Reusable | Catalog mentions `commercial.reconciliation` (nonexistent) |
| Missing rules | Bank file / settlement process |
| Schema | No reconciliation table; txn `reconciled` flag unmigrated |
| External | Possible bank/PSP exports |
| Safe now | None |
| Approval needed | Full ops product + schema |

---

## Summary

| Can proceed without approval | Needs product decision | Needs migration auth | Needs external provider |
| --- | --- | --- | --- |
| None of the 8 remaining as full live ops | 002–005 (rules) | 007, 009, 012, 014 (+ tax settings) | 009 (Razorpay) |
