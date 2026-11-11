# API-08 Facility Billing — Master Technical Design and Migration Authorization Assessment

**Document type:** Authoritative technical design and migration authorization assessment (consolidated)  
**Date:** 2026-11-04 (master consolidation)  
**Supersedes:** Prior sections of this same file that referenced organization-level partial-payment eligibility as the primary model; installment eligibility is **membership-plan-controlled** (approved).  
**Status:** **MASTER TECHNICAL DESIGN CONSOLIDATED — NOT AUTHORIZED FOR IMPLEMENTATION OR MIGRATION**  
**Evidence:** Repository inspection + read-only PostgreSQL `digitize` aggregates (2026-11-04); **no tests executed**; **no DDL/DML**

---

## 1. Executive summary

Digitize facility billing (**API-08**) today implements a **Phase 1 membership path**: API-05 creates `PENDING_PAYMENT` memberships; API-08-001 issues an **immediate ISSUED** invoice (single line, random `MFI-*` number); API-08-010 records **full invoice total** as **SUCCESS** in `billing.payments`; API-05 activation requires **PAID** + SUCCESS payment (`MembershipInvoiceValidation`).

Physical schema on local `digitize` (Alembic head **`072_platform_terms_document`**) has **five** `billing.*` tables. Four billing ORM models have **no physical tables**. Eight API-08 numbered operations remain **skeleton-only** on the contract catalogue.

**Approved product direction (this document):** Quotation and customer acceptance **before** invoice; **membership-plan** installment templates (max 3, org-admin configured); **one full membership invoice** with **accepted schedule snapshot**; **flexible payment allocation** (earliest outstanding installment first); org-wide **invoice/receipt numbering**; discount approval workflow; **approved tax order** (discount then tax on discounted base); cheques **PENDING** until cleared; credit notes + **customer credit liability**; manual reconciliation with **`billing.reconciliation.manage`**; extensive reporting including installment analytics.

**Gate:** Business rules in this prompt are **approved product decisions** but **do not authorize** schema, migrations, or code. All migration groups **F0–F8 remain NOT AUTHORIZED**. Further **formal API contract authorization** is required for optional offline payment `amount`. **Recommended first incremental migration review:** **F0** (quotation, acceptance, plan installment templates, accepted schedule snapshot) — **BLOCKED BY DECISION** on exact API-05/API-08 persistence boundary (U1) until closed.

---

## 2. Scope and read-only safety declaration

| Activity | This task |
|----------|-----------|
| Inspect backend, Flutter, migrations, contracts, tests (no DB writes) | Yes |
| Read-only SQL on `digitize` | Yes |
| Update **only** this evidence document | Yes |
| Modify application code, migrations, DB rows, API contracts, Flutter, RBAC seeds, DEV-19/21/23, other docs | **No** |
| Run DB-writing tests; enable `BILLING_REFUNDS_REPORTING_ENABLED`; activate payment providers | **No** |

---

## 3. Repository and database inspection evidence

### 3.1 Alembic head and billing migration chain

| Item | Verified value | Source |
|------|----------------|--------|
| Alembic head (`digitize`) | `072_platform_terms_document` | `SELECT version_num FROM alembic_version` |
| Revises | `071_support_center_foundation` | `migrations/versions/072_platform_terms_document.py` |
| Facility billing DDL | `063_facility_billing_membership` | `migrations/sql/063_facility_billing_membership.sql` |
| Refunds DDL | `069_billing_refunds` | `migrations/sql/069_billing_refunds.sql` |
| DB-11 bootstrap | `database/migrations/001–008` + `db11_foundation_baseline` | Not duplicated in 063+ |

**Proposed next revisions (planning only):** F0=`073_*` … F8=`081_*` after head `072`. Final identifiers require PO sign-off per release.

### 3.2 Aggregate data on `digitize` (no PII)

| Metric | Count | Reverified 2026-11-04 |
|--------|------:|------------------------|
| `billing.invoices` ISSUED | 4 | Yes |
| `billing.invoices` PAID | 21 | Yes |
| `billing.payments` SUCCESS | 22 | Yes |
| `billing.payments` FAILED | 4 | Yes |
| `billing.invoice_items` rows | **0** | Yes (anomaly vs 25 invoices — see §27) |
| `billing.refunds` rows | 16 | Yes |
| `billing.sellers` | (not re-counted; prior: 10) | — |

**Interpretation:** Code always inserts a line in `FacilityInvoiceService.create_membership_invoice` (`invoice_service.py`); zero line rows suggests **environment-specific cleanup or drift**. Backfill must run before NOT NULL snapshot constraints.

### 3.3 Status CHECK constraints (physical)

- **Invoices:** `DRAFT`, `ISSUED`, `PAID`, `CANCELLED`, `REFUNDED` — **no `PARTIALLY_PAID`** (`063` SQL).
- **Payments:** `PENDING`, `SUCCESS`, `FAILED`, `REFUNDED`.

---

## 4. Verified Alembic head

**`072_platform_terms_document`** on local `digitize` (read-only query 2026-11-04).

---

## 5. Existing physical billing schema

| Table | Tenant / facility | Notes |
|-------|-------------------|--------|
| `billing.sellers` | `organization_id` | `(organization_id, seller_code)` unique |
| `billing.invoices` | `organization_id`, `facility_id` | Membership FK; idempotency unique per org |
| `billing.invoice_items` | via `invoice_id` | `tax_amount`, `line_total`; no charge source |
| `billing.payments` | `organization_id`, `facility_id` | Direct `invoice_id`; attempt+success combined |
| `billing.refunds` | `organization_id` | FK `payment_id`; idempotency per org |

**Absent physically:** `receipts`, `payment_transactions`, `billing_settings`, `billing_status_history`, allocations, installments, quotations, credit notes, reconciliation (facility).

**Hierarchy codes for numbering (DB-11):** `tenant.organization.organization_code`, `tenant.site.site_code` (**Branch**), `tenant.facility.facility_code` — `database/migrations/002_create_core_platform_tenant_tables.sql`.

---

## 6. ORM versus physical schema drift

| ORM model | File | Physical table | Alembic twin |
|-----------|------|----------------|--------------|
| Invoice, InvoiceItem, Payment, Refund, Seller | `app/modules/billing/models/` | Yes | 063 / 069 |
| `PaymentTransaction` | `payment_transactions.py` | **No** | **None** |
| `Receipt` | `receipts.py` | **No** | **None** |
| `BillingSetting` | `billing_settings.py` | **No** | **None** |
| `BillingStatusHistory` | `billing_status_history.py` | **No** | **None** |

**Classification:** PaymentTransaction/Receipt/BillingSetting are **proposed technical design** targets, not deployable today.

---

## 7. Existing API-08 operation inventory

| ID | Path | Runtime | Classification |
|----|------|---------|----------------|
| API-08-001 | POST `/invoices` | Live | **Existing and verified** (unit + PG IV patterns) |
| API-08-006 | POST `/invoices/{id}/cancel` | Live | Verified |
| API-08-008 | POST `/payments` | Live | Alias offline |
| API-08-010 | POST `/payments/offline` | Live | Verified; PG lock tests |
| API-08-011 | GET `/payments/{id}/status` | Live | Verified |
| API-08-013 | POST `/payments/{id}/refunds` | Live | Verified + PG concurrency |
| API-08-015 | POST `/payments/{id}/cancel` | Live | PENDING only |
| API-08-016 | GET `/billing/history` | Live | Verified |
| API-08-017 | GET `/commercial/reports` | Live | Revenue alias |
| API-08-018 | GET `/billing/outstanding-statements` | Live | Verified |
| API-08-002,003,004,005,007,009,012,014 | Various | **Not registered** | **Blocked / deferred** skeleton (`operation_tracking.py`) |

Canonical registry: `app/api/contracts/api_registry.py`. Skeleton not on wire: `tests/api/test_runtime_catalog.py`.

---

## 8. Existing backend implementation status

| Capability | Status | Evidence |
|------------|--------|----------|
| Membership invoice from plan price | **Live** | `FacilityInvoiceService.create_membership_invoice` |
| Immediate ISSUED (no DRAFT) | **Live** | `INVOICE_STATUS_ISSUED` on create |
| Single line, tax zero | **Live** | `invoice_service.py` line item |
| Full-total offline SUCCESS | **Live** | `payment_service.py` `payment_amount = invoice.total_amount` |
| Outstanding math (pay − refund) | **Live** | `invoice_balance.py`, `repository.py` subqueries |
| Invoice row lock on pay | **Live** | `get_invoice_for_update`; `test_offline_payment_invoice_lock.py` |
| Idempotency org keys | **Live** | invoices, payments, refunds |
| Cheque as immediate SUCCESS | **Live gap vs product** | `CHEQUE` in constants; no PENDING path |
| Allocations / installments | **Missing** | No tables |
| Quotation / acceptance | **Missing** | No membership grep hits |
| Receipts | **Missing** | ORM only |
| `BILLING_REFUNDS_REPORTING_ENABLED` | **False** | `app/modules/reportsandanalytics/rules.py` ~156 |
| Revenue basis SUCCESS + `completed_at` | **Live** | `aggregate_customer_revenue` in `queries.py` |

**API-05 boundary:** `instance_service.py` creates membership **without** invoice; `lifecycle_service.py` activation uses `MembershipInvoiceValidation`; workflow in `tests/membership/digitize_pg_workflows.py` calls invoice API **directly after** create — **contradicts** approved quotation-first flow (**gap**).

---

## 9. Existing Flutter integration status

| Surface | API | Status |
|---------|-----|--------|
| Outstanding + collect | 018, 010 | **Existing and verified** (controller tests) |
| Billing history, cancel, refund | 016, 006, 013, 011 | **Existing** |
| Customer membership offline pay | 010 | **Existing** (`customer_membership_section.dart`) |
| Org billing page | SaaS + facility panels | **Partial** |
| Quotation Screen B | — | **Missing** (no quotation strings in facility/customer membership UI) |
| Plan installment admin | — | **Missing** (installment UI exists for **SaaS** checkout only: `facility_checkout_page.dart`, `saas_checkout` — **not** API-05 membership plans) |
| Receipts, reconciliation, discount approval | — | **Missing** |

Repositories: `remote_facility_outstanding_statements_repository.dart`, `remote_facility_billing_history_repository.dart`, `remote_customer_membership_repository.dart`.

---

## 10. Approved product decision traceability matrix

| Area | Approved rule (summary) | Existing | Gap |
|------|-------------------------|----------|-----|
| Quotation before invoice | Acceptance required | Direct invoice after membership | F0 + API-05/08 boundary |
| Installments | Plan-controlled, max 3, frozen on accept | None | F0 + F4 |
| Payment allocation | Earliest installment first; custom amount | Full invoice pay only | F4 + contract `amount` |
| Invoice numbering | `INV-ORG-SITE-FAC-######` org sequence | `MFI-*` random | F1 |
| Tax order | Discount → tax on discounted base | tax=0 | F3 |
| Discount approval | Separate applier/approver | None | F3 |
| Cheque PENDING | No outstanding until SUCCESS | Immediate SUCCESS | F6 + F4 |
| Credit note + customer credit | Outstanding first; liability traceable | Refunds only | F7 |
| Reconciliation | Manual + permission | `commercial.*` only | F8 |
| Reporting | Installment + discount + gross/net | Revenue/outstanding partial | Post F3/F4/F7 |
| Walk-in vs facility catalogue | Separate | walk-in in `operations.*` | F2 |

---

## 11. Membership quotation and acceptance architecture

### 11.1 Approved workflow

1. Staff selects customer + plan → **quotation** (offer, not invoice).  
2. Customer reviews (Screen B — checkout-style **offer**, not tax invoice layout).  
3. Explicit acceptance → evidence recorded.  
4. **Single full membership invoice** issued for accepted amount.  
5. Payment collection → activation per API-05 rules.

### 11.2 Module ownership (approved recommendation)

| Concern | Owner |
|---------|--------|
| Plan config, enrollment, quotation, acceptance | **API-05** |
| Invoice, snapshots, payments, allocations, receipts, CN, reconciliation | **API-08** |

**API-05 must not write `billing.*` directly.** Proposed **application orchestration** (internal service, not new numbered contract):

- Validate tenant/facility/principal on both sides.  
- **Single transaction or saga:** acceptance commit → idempotent invoice issue (keyed by `acceptance_id`).  
- On invoice failure: acceptance marked `INVOICE_PENDING` / retry — **exact recovery (U1)**.  
- Audit on both modules (`record_audit_event` pattern).

### 11.3 Persistence (proposed — F0)

- `membership.membership_quotation` (+ version rows or `quotation_version` int).  
- `membership.membership_quotation_acceptance` (method, actor, timestamp, snapshot JSON, terms ref).  
- Link invoice: `billing.invoices.quotation_acceptance_id` (nullable; NULL for historical 25 rows).

**Duplicate prevention:** unique `(acceptance_id)` → at most one invoice; idempotency on issue API unchanged.

---

## 12. Membership-plan installment configuration

### 12.1 Approved rules (**supersedes org-wide partial-payment default**)

- Per **membership plan**; org admin only; default **single payment**.  
- Optional ≤ **3** installments; amounts sum to **full membership price**; admin sets **due dates** (ordered, validated).  
- Customer selects **only** admin-defined schedules on quotation.  
- **One invoice** for full membership amount — **not** one invoice per installment.

### 12.2 Proposed schema (F0 template + F0/F4 snapshot)

**Plan template (mutable for future sales):**

- `membership.plan_payment_schedule_option` (`plan_id`, `option_code`, `installment_count`, active flag).  
- `membership.plan_payment_schedule_line` (`option_id`, `sequence`, `scheduled_amount`, `due_date_offset_days` or absolute rule — **U8**).

**Accepted snapshot (immutable per enrollment):**

- `membership.enrollment_payment_schedule` (FK `customer_membership_id`, `quotation_acceptance_id`, frozen JSON or normalized lines).  
- Lines: `sequence`, `scheduled_amount`, `due_date`, `allocated_amount` (maintained by allocations — **F4**).

Plan changes **do not** alter accepted snapshots.

---

## 13. Accepted installment schedule snapshot

Stored at acceptance with quotation version. Fields per line:

- Scheduled amount, due date, allocated amount, remaining scheduled amount.  
- **Derived:** overdue (due &lt; today ∧ remaining &gt; 0); settlement status (open/partial/closed).  
- **Not** payment transactions.

Reports must **not** count scheduled amounts as collections (§23).

---

## 14. Payment transaction and allocation architecture

### 14.1 Distinction (approved)

| Concept | Role |
|---------|------|
| Installment line | Scheduled obligation |
| `billing.payments` | Attempt + successful payment record (Phase 1 evolve: PENDING→SUCCESS) |
| `billing.payment_allocations` | Amount applied to invoice (+ optional `installment_sequence`) |
| `billing.payment_transactions` | Gateway/cheque instrument detail (F6) — **single source with payment row**, not duplicate money |

### 14.2 Allocation algorithm (approved)

1. Reject if payment &gt; **invoice outstanding**.  
2. Apply to **earliest installment with remaining &gt; 0**.  
3. Overflow to next installments.  
4. Update `allocated_amount` on schedule snapshot; **do not** change scheduled amounts/dates.  
5. Update invoice status: `PARTIALLY_PAID` / `PAID` (F1 CHECK).  
6. **Atomic** with payment SUCCESS + allocation insert(s).  
7. **One invoice per payment** (Phase 1).

### 14.3 Offline payment contract (proposed — **requires formal authorization U5**)

| `amount` | Behavior |
|----------|----------|
| Omitted | Pay **current invoice outstanding** (behavior change from today’s full `total_amount`) |
| Provided | Specified amount; membership installment allocation rules |
| &gt; outstanding | Reject |
| Non-membership invoice | **U12** — do not assume plan installments apply |

**Compatibility:** Today `OfflinePaymentCreate` has **no** `amount` (`schemas.py`); implementation uses **invoice total** (`payment_service.py` ~138–141). Document as **breaking risk** when multiple SUCCESS payments exist unless migration path defined.

### 14.4 Cheques (approved)

- Create `PENDING` payment; **no** allocation / **no** outstanding reduction.  
- Clear → `SUCCESS` + allocation + receipt (F5).  
- Bounce → failed + audit (`BillingStatusHistory` or audit payload).  
- Bounce suspension: **separate frozen grace rules** — not implemented in facility billing today.

---

## 15. Invoice lifecycle and numbering

### 15.1 Lifecycle (approved)

- Multi-line; DRAFT cancel; ISSUED immutable snapshots; overdue **derived**; historical rows unchanged.  
- Membership issue **only after acceptance** (future); legacy `MFI-*` preserved.

### 15.2 Numbering (approved)

Format: **`INV-{organization_code}-{site_code}-{facility_code}-{sequence}`**  
- **One org-wide sequence** (not per site/facility).  
- Snapshot codes on invoice at issue; counter in `billing.billing_settings` with **`SELECT … FOR UPDATE`**.  
- Cancelled numbers never reused; unique constraint on `(organization_id, invoice_number)` or global number string unique.

**Site selection:** Which site code when multiple sites per facility — **U2** technical default: primary site on invoice or enrollment context.

---

## 16. Receipt architecture

- One receipt per **SUCCESS** payment (after allocation).  
- Org sequential receipt number (`billing_settings.receipt_sequence_next`).  
- Persist JSON: invoice total, prior payments, current payment, paid-to-date, outstanding.  
- PDF async (mirror SaaS PDF pattern in `subscription` module).  
- API-08-012 skeleton until F5.  
- Extend ORM: add `facility_id`, payload JSON — **proposed**.

---

## 17. Discount configuration and approval architecture

- Org-configurable definitions; **one discount per line**, no stack.  
- Application vs approval users; **no self-approval**; audit fields on line snapshot at issue.  
- Approval **policies** configurable — **no default thresholds (U4)**.  
- Draft/declined quotations excluded from **issued** discount reports; optional separate quotation-conversion metrics.

---

## 18. Tax calculation architecture

**Approved order:**

1. Eligible discount on line.  
2. Tax on **discounted taxable base**.  
3. Persist: original line, discount type/amount, taxable base, rate, tax amount, final line (all snapshot at issue).

**Technical:** Decimal only (`money` / `Decimal` — align with `app/modules/reportsandanalytics/money.py`). **U3:** rounding per line vs invoice total — recommend **per-line half-up to 2 dp** for INR; **requires confirmation**.

No hard-coded GST; config in `billing_settings.tax_settings` or facility override — **proposed**.

---

## 19. Refund and credit-note architecture

- **Refunds:** existing `billing.refunds` + `billing.refund.process`.  
- **Credit notes (F7):** header/lines linked to invoice; partial CN supported; authorized actor.  
- **Partially paid invoice (approved):** CN reduces outstanding first; excess → **refund OR customer credit liability** (explicit authorized process); prevent double settlement.

**Allocation reversal on refund:** Must reduce `allocated_amount` on installment lines and outstanding — **U9** detail in service design.

---

## 20. Customer credit liability design

**Proposed (F7):** `billing.customer_credit_liability` (org, customer, source CN id, amount, currency, status OPEN/APPLIED/REFUNDED), application rows when applied to future invoice.

**Not** an unrestricted wallet. **U7:** ledger representation for finance — **unresolved**.

---

## 21. Reconciliation and RBAC design

**Facility tables (F8)** — not `commercial.reconciliation`:

- Event/history: outcome ∈ {MATCHED, UNMATCHED, AMOUNT_MISMATCH, DUPLICATE, PENDING_INVESTIGATION}.  
- **No auto** invoice balance change.

**Permission (approved, not seeded):** `billing.reconciliation.manage`  
- Seed like 063/069: `identity.permission` + assign via org admin (no new role).  
- View: existing billing/report permissions.  
- Refunds: still `billing.refund.process`.

---

## 22. Walk-in and facility service catalogue architecture

| Source | Storage | Line metadata |
|--------|---------|---------------|
| Walk-in | `operations.walk_in_visit_charge` | `charge_source=WALK_IN` |
| Facility service | `billing.facility_service_charge` (F2) | `charge_source=FACILITY_SERVICE` |
| Membership | plan snapshot | `charge_source=MEMBERSHIP` |

API-08-002 uses facility catalogue only; walk-in remains API-06.

---

## 23. Revenue, discount and installment reporting

### 23.1 Definitions (avoid double-count)

| Metric | Source |
|--------|--------|
| Gross invoice | Sum issued snapshot line amounts pre-discount |
| Discounts | Snapshot discount amounts |
| Tax | Snapshot tax |
| Net invoice | Gross − discount + tax per rules |
| Collections | **SUCCESS payments** `completed_at` in period only |
| Scheduled installments | **Never** collections |
| Refunds | SUCCESS refunds in period (when flag enabled) |
| Outstanding | Invoice − allocations + approved CN/adjustments − … |

### 23.2 Refund reporting enablement (approved business rule — **not enabled**)

Change **`BILLING_REFUNDS_REPORTING_ENABLED = True`** in `app/modules/reportsandanalytics/rules.py` (module constant, **not** environment variable). Logic already in `queries.py` when true. Requires regression: `test_billing_invoices_revenue_live_digitize.py`, `test_reporting_rev2a_financial.py`. **Status: NOT AUTHORIZED.**

### 23.3 New report catalogue entries

**Proposed** post-schema: installment performance, discount approval audit, gross-to-net, allocation detail — extend `reportsandanalytics/catalogue.py` (authorization separate).

---

## 24. Detailed migration F0–F8 specifications

**All groups: NOT AUTHORIZED.**

### F0 — `073_membership_quotation_acceptance_installments` — **BLOCKED BY DECISION (U1)**

| # | Content |
|---|---------|
| Purpose | Quotation, acceptance, plan schedule options, accepted schedule snapshot |
| Tables | Quotation, acceptance, plan schedule option/lines, enrollment schedule snapshot |
| FK | org, facility, site, customer, membership, terms doc |
| Backfill | NULL acceptance on existing invoices |
| API | API-05 new flows; API-08-001 gated on acceptance — **contract change: formal approval** |
| Flutter | Screen B quotation; plan installment admin |
| Tests | New PG workflow replacing direct invoice in `digitize_pg_workflows.py` |
| Out of scope | Auto-debit, late fees, suspension |

### F1 — `074_billing_settings_invoice_lifecycle_numbering` — **NOT AUTHORIZED**

| # | Content |
|---|---------|
| Purpose | `billing_settings`, org invoice/receipt counters, `PARTIALLY_PAID`, `issued_at`, code snapshot JSON |
| Extend | `invoices` CHECK, unique invoice number |
| Depends | F0 acceptance FK optional nullable |
| Rollback | Risk if PARTIALLY_PAID rows exist |

### F2 — `075_facility_service_charge_catalogue` — **NOT AUTHORIZED**

Facility-scoped service codes/prices; line `charge_source` on items (with F3).

### F3 — `076_invoice_financial_snapshots_discount_tax` — **NOT AUTHORIZED**

Line snapshot columns; discount definition + approval audit columns; backfill lines from header totals.

### F4 — `077_payment_allocations_installment_settlement` — **NOT AUTHORIZED**

`payment_allocations`; update schedule `allocated_amount`; offline amount behavior; invoice status transitions; preserve revenue on `payments.completed_at`.

### F5 — `078_receipts` — **NOT AUTHORIZED**

Create `billing.receipts`; numbering; structured payload.

### F6 — `079_payment_attempts_transactions` — **NOT AUTHORIZED**

`payment_transactions`; PENDING payment path for cheque; no Razorpay.

### F7 — `080_credit_notes_adjustments_customer_credit` — **NOT AUTHORIZED**

CN, adjustments, customer credit liability; permissions for authorize CN.

### F8 — `081_manual_reconciliation` — **NOT AUTHORIZED**

Reconciliation tables; seed `billing.reconciliation.manage`.

**Order:** F0 → F1 → F3 → F4 → F5 → (F6 parallel after F4) → F7 → F8; F2 after F1.

---

## 25. API contract impact matrix

| Operation | Change | Backward compat | Formal approval |
|-----------|--------|-----------------|-----------------|
| POST `/invoices` | Requires acceptance / idempotent from acceptance | **Breaking** for current Flutter/PG workflow | **Yes** |
| POST `/payments/offline` | Optional `amount`; outstanding default | Additive if optional; behavior change if omitted semantics change | **Yes (U5)** |
| Skeleton 002–014 | New implementations | N/A | Per operation |
| API-05 | Quotation/acceptance endpoints | New surface | **Yes** (not numbered in this doc) |

**Do not invent new API-08 numbered IDs** in implementation without registry update authorization.

---

## 26. Flutter implementation impact matrix

| Feature | Files / area | Status |
|---------|--------------|--------|
| Plan installment config | New org-admin on membership plan editor | **Proposed** |
| Screen B quotation | New customer/staff flow | **Proposed** |
| Acceptance capture | Staff + customer paths | **Proposed** |
| Payment custom amount | `facility_outstanding_statements_panel.dart`, membership section | **Proposed** |
| Installment outstanding UI | Outstanding/history models | **Proposed** |
| Receipts | New panel/route | **Proposed** |
| Discount approval | Invoice draft UI | **Proposed** |
| Reconciliation | New admin UI | **Proposed** |
| Reports | `company_reports_page.dart`, reporting repo | **Proposed** |

Existing SaaS installment UI **not reusable** for API-05 without new APIs/models.

---

## 27. Existing-data backfill strategy

1. Detect invoices without `invoice_items` (currently all 25 on sample DB).  
2. Reconstruct single membership line from `total_amount` + membership plan snapshot where possible.  
3. Leave `MFI-*` numbers; new format forward-only.  
4. Set `quotation_acceptance_id` NULL.  
5. For SUCCESS payments without allocations, backfill **one allocation row = payment.amount** (F4 migration script).  
6. Idempotent migration scripts; no DELETE of financial history.

---

## 28. Testing and PostgreSQL integration plan

| Suite | Role |
|-------|------|
| `tests/billing/test_offline_payment_invoice_lock.py` | Concurrency, idempotency — extend for partial/allocation |
| `tests/billing/test_facility_membership_billing.py` | Invoice/pay unit |
| `tests/billing/test_billing_invoices_revenue_live_digitize.py` | Revenue IV on `digitize` (TAG guard) |
| `tests/membership/digitize_pg_workflows.py` | Replace invoice-before-acceptance |
| `tests/billing/test_refund_concurrency_postgres.py` | Refund caps |
| Flutter controller tests | Extend for quotation/installment |

**Do not run** PG tests during design tasks on shared DB without TAG isolation (`billing_digitize_pg_guard.py`).

---

## 29. Rollback and recovery strategy

- Forward-only for issued invoice/receipt numbers.  
- Downgrade F4 only if no allocation rows.  
- Feature flags: quotation-first enrollment vs legacy path during transition (**U7** product flag).  
- Acceptance without invoice: retry job or manual re-issue — document in runbook (**U1**).

---

## 30. Security and tenant isolation review

- All new tables: `organization_id`; facility where applicable.  
- Continue `require_facility_access`, `require_billing_facility_operational_scope`.  
- Idempotency on all financial mutations.  
- Row locks on invoice issue numbering and payment allocation.  
- Platform admin: governance only — no new tenant superuser.

---

## 31. Unresolved decision register

| ID | Topic | Status |
|----|-------|--------|
| U1 | API-05/API-08 orchestration & failure recovery | **Requires authorization** |
| U2 | Site code on invoice when multiple sites | **Requires authorization** |
| U3 | Tax rounding precision | Recommend per-line 2dp; **confirm** |
| U4 | Discount policy storage (no default thresholds) | **Requires authorization** |
| U5 | Formal OpenAPI for payment `amount` | **Requires authorization** |
| U6 | Enable refund reporting flag in `rules.py` | Approved rule; **NOT AUTHORIZED** to enable |
| U7 | Customer credit ledger accounting | **Requires authorization** |
| U8 | Installment due date validation rules | **Requires authorization** |
| U9 | Refund/CN reversing allocation across installments | **Requires authorization** |
| U10 | Installment reminders (no provider activation) | **Requires authorization** |
| U11 | Membership cancellation vs financial workflow | **Requires authorization** |
| U12 | Non-membership partial payment policy | **Separate product approval** |

**Approved (do not reopen):** Installment plan model, allocation order, CN-on-partial-pay order, tax calculation order, receipt numbering, reconciliation permission code, branch=site, one invoice per membership.

---

## 32. Incremental migration authorization checklist

| Group | Revision (proposed) | Approval status |
|-------|---------------------|-----------------|
| F0 Quotation + acceptance + plan schedules | 073 | **NOT AUTHORIZED** — **READY FOR REVIEW** after U1 |
| F1 Settings + numbering + PARTIALLY_PAID | 074 | **NOT AUTHORIZED** |
| F2 Facility service catalogue | 075 | **NOT AUTHORIZED** |
| F3 Snapshots + discount/tax | 076 | **NOT AUTHORIZED** |
| F4 Allocations + installment settlement | 077 | **NOT AUTHORIZED** |
| F5 Receipts | 078 | **NOT AUTHORIZED** |
| F6 Payment transactions / cheque | 079 | **NOT AUTHORIZED** |
| F7 CN + adjustments + customer credit | 080 | **NOT AUTHORIZED** |
| F8 Reconciliation + permission seed | 081 | **NOT AUTHORIZED** |
| Refund reporting flag | code change | **NOT AUTHORIZED** |

---

## 33. Final gate recommendation

| Question | Answer |
|----------|--------|
| Product decisions reflected? | **Yes** in this document |
| Implementation authorized? | **No** |
| Migrations authorized? | **No** |
| First group for incremental PO review? | **F0** (after closing **U1**, **U8**) |
| Further product clarification? | **Yes** — U1, U5, U11, U12 minimum |

**MASTER TECHNICAL DESIGN CONSOLIDATED — NOT AUTHORIZED FOR IMPLEMENTATION OR MIGRATION**

---

## Appendix A — Key repository references

| Topic | Location |
|-------|----------|
| Invoice create | `app/modules/billing/invoice_service.py` — `create_membership_invoice`, `_invoice_number` |
| Full pay | `app/modules/billing/payment_service.py` — `OfflinePaymentService.record` |
| Activation check | `app/modules/billing/membership_invoice_validation.py` |
| Membership create | `app/modules/membership/instance_service.py` |
| Revenue | `app/modules/reportsandanalytics/queries.py` — `aggregate_customer_revenue` |
| Refund flag | `app/modules/reportsandanalytics/rules.py` — `BILLING_REFUNDS_REPORTING_ENABLED` |
| Skeleton gates | `app/api/contracts/operation_tracking.py` |
| PG E2E (current) | `tests/membership/digitize_pg_workflows.py` — `bootstrap_active_membership` |

## Appendix B — Tracker update recommendations (do not edit now)

After future implementation authorization: DEV-21 (API-08 gaps, quotation, installments), DEV-19 (API-08 completion, Screen B), DEV-23 (F0→F8 sequencing).

## Appendix C — Document history

| Version | Change |
|---------|--------|
| 2026-11-04 initial | Read-only assessment F0–F8, org partial pay |
| 2026-11-04 master | Consolidated approved decisions; plan installments; F0=073…F081; superseded org partial-pay as primary model |
