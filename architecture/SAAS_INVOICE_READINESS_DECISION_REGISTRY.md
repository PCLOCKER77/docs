# SaaS invoice readiness — decision registry

**Status:** Authoritative registry for unresolved commercial and statutory decisions affecting Digitize SaaS tax invoices, subscription quotes, and Razorpay-backed payment reconciliation.  
**Date:** 2026-10-20 (Phase 8 reconciliation); **GAP-API09-002 assessment:** 2026-11-03; **Decision-resolution package:** 2026-11-03  
**Sandbox plan:** `SAAS_RAZORPAY_SANDBOX_TEST_PLAN.md`  
**Scope:** Organization → Digitize SaaS commerce (`commercial.saas_*`), extra-catalog invoice APIs, Flutter billing UI.  
**Does not supersede:** DR-019 (SaaS vs facility commerce); DR-021 (Platform Admin ≠ tenant checkout); approved billing options `ANNUAL_UPFRONT` and `INSTALLMENT_60_40`; 228 numbered product API inventory; backend-authoritative quote arithmetic in `invoice_calculator.py` / `calculator.py`.

Implementation gap codes referenced below are defined in `digitize-services/app/modules/subscription/commerce/invoice_calculator.py` and `commerce/calculator.py` unless noted.

---

## 1. Frozen approved decisions (not reopened here)

| Topic | Approved behavior | Evidence |
| --- | --- | --- |
| SaaS commercial unit | Organization → Digitize; facility-scoped subscription; no staff-mobile SaaS purchase | DR-019 |
| Billing options | `ANNUAL_UPFRONT` and `INSTALLMENT_60_40` (60% upfront / 40% second installment) | `calculator.py`, migration 033 |
| Quote money | Server-side from active discount/tax/quote policies; client amounts rejected | `SaasCommerceService`, `CLIENT_AMOUNT_FIELDS` |
| Installment split math | 60/40 of payable total when installment quote is allowed | `calculator.SIXTY` / `FORTY` |
| Tax mode | `EXCLUSIVE` only for quotes | `BLOCK_TAX_MODE` |
| Invoice preview | In-memory; `PREVIEW` status; no invoice number; `not_a_tax_invoice: true` | `SaasInvoiceService.preview` |
| Issued snapshot immutability | DB trigger on legal/monetary fields; payment fields mutable | Migration 034 `trg_saas_invoice_guard_issued_rewrite` |
| One issued invoice per accepted terms | Unique partial index `uq_saas_invoice_terms_issued` | Migration 034 |
| Platform Admin | Cannot create quotes, verify checkout, preview/issue tenant invoices | `_deny_platform_impersonation` |
| Paid-through | Not computed; status `PAID_THROUGH_RULE_UNAPPROVED` | `commerce/service.py` |

---

## 2. Unresolved decisions — implementation reconciliation

Legend for **Gate impact:**  
- **Sandbox pay** = Razorpay test checkout / verify / webhook  
- **Activate** = facility subscription activation after verified payment  
- **Issue** = statutory tax invoice `POST /saas/invoices`  
- **Launch** = production statutory invoice + compliance rollout  

| ID | Gap / blocker code | Gate impact |
| --- | --- | --- |
| INV-001 | `PLACE_OF_SUPPLY_RULE_UNAPPROVED` | Issue, Launch |
| INV-002 | `CUSTOMER_GSTIN_PLAINTEXT_UNAVAILABLE` | Issue, Launch |
| INV-003 | `INSTALLMENT_INVOICE_DOCUMENT_POLICY_UNAPPROVED` | Issue (installment), Launch |
| INV-004 | `CREDIT_NOTE_GST_RULES_UNAPPROVED` | Launch (corrections) |
| INV-005 | `PRORATION_POLICY_UNAPPROVED` | Launch (mid-cycle) |
| INV-006 | `PAID_THROUGH_RULE_UNAPPROVED` | Launch (UX); not Sandbox pay |
| INV-007 | (feature absent) | Launch (PDF/e-invoice) |
| INV-008 | `MONTH_END_INSTALLMENT_UNAPPROVED` | Quote/Verify for edge dates |
| INV-009 | `DISCOUNT_ON_INSTALLMENTS_UNAPPROVED` | Quote when discount &gt; 0 on installment |

### INV-001 — Place of supply and CGST/SGST vs IGST

| Field | Value |
| --- | --- |
| **Gap code** | `PLACE_OF_SUPPLY_RULE_UNAPPROVED` — in `ISSUANCE_BLOCKERS` (`invoice_service.py`) |
| **Current code behavior** | `invoice_calculator.split_configured_tax` always appends this gap when CGST/SGST/IGST percents are used. Tax snapshot: `place_of_supply: null`, `place_of_supply_rule: PLACE_OF_SUPPLY_RULE_UNAPPROVED`. No rule selects IGST vs CGST+SGST from customer/supplier state. |
| **Business decision required** | Approved place-of-supply determination and component set per B2B supply. |
| **Services** | `invoice_calculator.py`, `invoice_service._compose`, `SaasInvoiceService.issue` |
| **APIs (extra catalog)** | `saas_invoices_preview_create`, `saas_invoices_create` |
| **UI** | `saas_invoice_detail_page.dart` — shows backend `tax` / gaps; no client-side GST split |
| **Tests when approved** | `test_invoice_calculator.py` (intrastate/interstate snapshots); issuance integration; preview gap cleared |
| **Gate impact** | Sandbox pay: **no** · Activate: **no** · Issue: **yes** · Launch: **yes** |
| **Approver** | Commercial + statutory tax advisor (TBD in org) |
| **Acceptance criteria** | Rule inputs documented; gap removed only when rule implemented; no default state pairing invented |
| **Resolution package** | **§9.1** (pending product + legal approval) |

### INV-002 — Customer GSTIN storage and invoice snapshot

| Field | Value |
| --- | --- |
| **Gap code** | `CUSTOMER_GSTIN_PLAINTEXT_UNAVAILABLE` — in `ISSUANCE_BLOCKERS`; `_customer_snapshot()` always adds gap (with or without `gstin_last4`) |
| **Current code behavior** | Org model: hash/mask only on APIs. Invoice snapshot: `gstin: null`, optional `gstin_masked`. Issuance raises `ValidationFailed` with code in `details`. |
| **Business decision required** | Storage, encryption, RBAC, retention, and invoice field content for customer GSTIN. |
| **Services** | `invoice_service._customer_snapshot`, `SaasInvoiceService.issue` |
| **APIs** | `saas_invoices_create`; org legal identity APIs (separate module) |
| **UI** | Invoice detail shows gaps; billing does not collect GSTIN for invoice bypass |
| **Tests when approved** | `test_saas_invoice_service.py` (issuance success path); privacy/authz tests; cold DB issue path currently blocked |
| **Gate impact** | Sandbox pay: **no** · Activate: **no** · Issue: **yes** · Launch: **yes** |
| **Approver** | Legal / privacy + commercial (TBD) |
| **Acceptance criteria** | Plaintext available only under policy; snapshot on issue; no test bypass of gap |
| **Resolution package** | **§9.3** (pending product + legal approval) |

### INV-003 — Annual contract invoice vs 60/40 installment tax documents

| Field | Value |
| --- | --- |
| **Gap code** | `INSTALLMENT_INVOICE_DOCUMENT_POLICY_UNAPPROVED` — in `ISSUANCE_BLOCKERS` when `billing_option == INSTALLMENT_60_40` |
| **Current code behavior** | Quote/checkout/verify **allowed** for installment (obligations `UPFRONT`/`INSTALLMENT_1`/`INSTALLMENT_2`). Tax invoice issue **blocked** for installment terms. |
| **Business decision required** | One annual tax invoice vs per-installment tax documents; timing vs obligation `PAID`. |
| **Services** | `invoice_service._compose`, `SaasCommerceService` obligation creation |
| **APIs** | `saas_quotes_create`, `saas_payment_orders_create`, `saas_invoices_create` |
| **UI** | `organization_billing_page.dart`, checkout flow; invoice list when issued |
| **Tests when approved** | `test_installment_terms_cannot_issue_tax_invoice` replaced/extended per policy; multi-invoice uniqueness tests |
| **Gate impact** | Sandbox pay: **no** (installment pay testable) · Activate: **no** · Issue: **yes (installment)** · Launch: **yes** |
| **Approver** | Commercial + finance (TBD) |
| **Acceptance criteria** | Written policy; schema if multiple issued invoices per terms cycle |
| **Resolution package** | **§9.2** (pending product + legal approval) |

### INV-004 — Credit notes, cancellations, and GST corrections

| Field | Value |
| --- | --- |
| **Gap code** | `CREDIT_NOTE_GST_RULES_UNAPPROVED` — metadata on invoice JSON (`credit_note_status`); **not** an issuance blocker |
| **Current code behavior** | No credit-note tables; issued invoice immutable; refunds not wired from Razorpay to invoice reversal. |
| **Business decision required** | Credit note workflow, GST reversal, link to `saas_payment_attempt` / refunds. |
| **Services** | Future module; today `invoice_service._invoice_out` only surfaces gap |
| **APIs** | None implemented (facility API-08 credit note is separate product surface) |
| **UI** | Invoice detail may list gap in `configuration_gaps` / metadata |
| **Tests when approved** | New migration + service tests; immutability interaction with credit notes |
| **Gate impact** | Sandbox pay: **no** · Activate: **no** · Issue: **no** (initial issue) · Launch: **yes** (post-issue ops) |
| **Approver** | Finance + statutory tax advisor |
| **Acceptance criteria** | End-to-end correction path approved before implementation |

### INV-005 — Proration

| Field | Value |
| --- | --- |
| **Gap code** | ~~`PRORATION_POLICY_UNAPPROVED`~~ **Approved 2026-11-03** — implemented in `commerce/proration.py`, `quote_pricing.py`, quote/checkout path |
| **Approved policy** | Organization common renewal date; calendar-day proration; facility `created_at` effective date; co-terminate new facilities; late-addition installment → annual upfront only; no mid-period credits (INV-004 unchanged) |
| **Current code behavior** | `SaasCommerceService` uses `compute_authoritative_quote_amounts`; invoice `_compose` uses terms `calculation_inputs` period; `GAP_PRORATION` only when proration metadata absent |
| **Business decision required** | **Closed** — product owner sign-off recorded in GAP-API09-006 implementation |
| **Services** | `proration.py`, `quote_pricing.py`, `calculator.py` (installment anchor), `invoice_service._compose`, `SubscriptionService.activate_from_verified_payment` |
| **Tests** | `test_facility_addition_proration.py`; opt-in `DIGITIZE_PRORATION_PG_TEST=1` on local `digitize` |
| **Gate impact** | Sandbox pay: **no** · Activate: **no** · Issue: **no** (other INV blockers remain) · Launch: **partial** (proration closed; GST/installment docs still open) |

### INV-006 — Paid-through calculation

| Field | Value |
| --- | --- |
| **Gap code** | `PAID_THROUGH_RULE_UNAPPROVED` (`PAID_THROUGH_PENDING` in `commerce/service.py`) |
| **Current code behavior** | `_terms_out` / payment status: `paid_through: null`, `paid_through_status: PAID_THROUGH_RULE_UNAPPROVED`. |
| **Business decision required** | Paid-through date definition (anniversary vs payment date vs installment schedule). |
| **Services** | `SaasCommerceService` response builders |
| **APIs** | `saas_quotes_accept`, `saas_payments_get`, terms payloads |
| **UI** | Billing/checkout may show null paid-through (no invented date) |
| **Tests when approved** | Commerce service tests for computed `paid_through` |
| **Gate impact** | Sandbox pay: **no** · Activate: **no** · Issue: **no** · Launch: **yes** (entitlement UX) |
| **Approver** | Commercial product owner |
| **Acceptance criteria** | Single rule; tests for annual vs installment |

### INV-007 — Statutory PDF / legal format

| Field | Value |
| --- | --- |
| **Gap code** | None (feature absent) |
| **Current code behavior** | Flutter printable dialog renders backend strings; no PDF service, IRN, or IRP. |
| **Business decision required** | Layout, HSN/SAC, signatures, e-invoice compliance. |
| **Services** | None server-side for PDF |
| **APIs** | None |
| **UI** | `saas_invoice_detail_page.dart` print dialog |
| **Tests when approved** | PDF generation service tests; snapshot fixture parity |
| **Gate impact** | Sandbox pay: **no** · Activate: **no** · Issue: **no** (digital issue separate) · Launch: **yes** |
| **Approver** | Legal + finance |
| **Acceptance criteria** | Signed template; retention policy |

### INV-008 — Month-three installment due date (invalid calendar day)

| Field | Value |
| --- | --- |
| **Gap code** | `MONTH_END_INSTALLMENT_UNAPPROVED` (`calculator.BLOCK_MONTH_END`) |
| **Current code behavior** | `add_calendar_months` + 3 months for installment 2 due; `QuoteCalculationBlocked` if day invalid. |
| **Business decision required** | Month-end rule (last day vs shift). |
| **Services** | `commerce/calculator.py` |
| **APIs** | `saas_quotes_create` with `INSTALLMENT_60_40` |
| **UI** | Checkout quote step error surfaced via API |
| **Tests when approved** | `test` for Jan 31 + 3 months etc. |
| **Gate impact** | Sandbox pay: **edge dates only** · Activate: **no** · Issue: indirect · Launch: **yes** |
| **Approver** | Commercial product owner |
| **Acceptance criteria** | One convention in `add_calendar_months` |

### INV-009 — Annual discount on installment billing

| Field | Value |
| --- | --- |
| **Gap code** | `DISCOUNT_ON_INSTALLMENTS_UNAPPROVED` (`calculator.BLOCK_DISCOUNT_INSTALLMENT`) |
| **Current code behavior** | Non-zero discount + installment requires `applies_to_installments is True` on active discount policy; else quote blocked or discount zeroed. |
| **Business decision required** | Whether annual discount applies to installment payable total. |
| **Services** | `calculate_quote`, `SaasDiscountPolicy.applies_to_installments` |
| **APIs** | `saas_quotes_create`; platform policy admin (supplier/commerce policies) |
| **UI** | Quote/checkout error with actionable code |
| **Tests when approved** | Calculator tests for True/False flag; installment quote amounts |
| **Gate impact** | Sandbox pay: **when discount &gt; 0** · Activate: **no** · Issue: **no** · Launch: **yes** |
| **Approver** | Commercial product owner |
| **Acceptance criteria** | Flag semantics frozen in policy model |

---

## 3. Razorpay and payment verification boundary

| Step | Backend authority | Client cannot alone |
| --- | --- | --- |
| Order creation | `SaasCommerceService` creates `saas_payment_attempt` + provider order | Mark paid |
| Checkout callback | `verify_checkout` requires valid HMAC (`gateway.verify_checkout`) | Verify without secret |
| Webhook | `handle_webhook` requires valid webhook signature; idempotent on `provider_event_id` | Forge events |
| Verification | `_mark_verified` sets attempt `VERIFIED`, obligation `PAID`, calls `apply_verified_attempt` | Set status in payload |
| Invoice reconciliation | Only `VERIFIED` attempts in `apply_verified_attempt`; duplicate attempt rows idempotent via `uq_saas_invoice_payment_attempt` | Apply failed/created attempts |
| Subscription activation | `_activate_after_payment` only after verified upfront/installment_1 | Activate on client claim |

Failed signature, amount/currency mismatch, duplicate obligation payment, and failed provider events do not mark invoices paid. Tests: `tests/subscription/test_saas_commerce_service.py`, `test_saas_mock_checkout_lifecycle.py`, `test_razorpay_hmac.py`.

**Not in scope:** live Razorpay credentials, real money movement, or production webhook endpoints.

### 3.1 Razorpay sandbox

Full checklist (automated vs manual, S1–S17, logging, Flutter targets): **`SAAS_RAZORPAY_SANDBOX_TEST_PLAN.md`**.

**No sandbox payment has been executed** in the repository authoring process. Mock automated tests remain the only exercised payment path.

---

## 4. Issuance gate summary (implementation)

Tax invoice **issuance** is blocked when any code in `ISSUANCE_BLOCKERS` (`invoice_service.py`) appears in composed gaps, including supplier/customer legal data, GST components, tax rounding, place of supply, installment document policy, and customer GSTIN plaintext.

**Preview** may return gaps but does not persist rows or consume invoice numbers.

---

## 5. Technical verification notes

| Item | Status |
| --- | --- |
| Cold DB migration 034 | `digitize_mig_cold` only; see `tests/migrations/test_034_saas_invoices.py` |
| Immutability trigger exercised | Yes — transactional probes in cold tests |
| Two-connection duplicate issued insert | `tests/migrations/test_saas_invoice_issue_concurrency_cold.py` |
| Subscription → payment → invoice lifecycle (services) | `tests/subscription/test_saas_subscription_invoice_lifecycle.py` |
| Concurrent `SaasInvoiceService.issue` (in-memory) | Blocked path + idempotent return when invoice already exists |
| Concurrent `SaasInvoiceService.issue` (cold DB, 2 sessions) | `tests/migrations/test_saas_invoice_issue_service_cold.py` — both `ValidationFailed`, zero `ISSUED` rows (INV-002 blockers) |
| Concurrent create race to INSERT | `tests/migrations/test_saas_invoice_issue_concurrency_cold.py` — DB unique index |
| End-to-end concurrent issue **reaching numbering** | **Not exercised** — `ISSUANCE_BLOCKERS` require approved statutory config (INV-001/002/003); bypass would invalidate the test |
| Numbered API count 228 | `tests/api/test_contract_registry.py` |

---

## 6. Related documents

- `docs/architecture/SAAS_RAZORPAY_SANDBOX_TEST_PLAN.md`
- `docs/architecture/ACCESS_MOBILE_COMMERCE_ARCHITECTURE_FREEZE.md`
- `docs/architecture/API_09_SUBSCRIPTION_LICENSE_IMPLEMENTATION_GATE.md`
- `docs/99_Decision_Records/DR-019_Access_Mobile_Commerce_Architecture.md`
- `digitize-services/migrations/sql/034_saas_invoices.sql`

---

## 7. Additional issuance blockers (configured policy — not separate INV IDs)

These are enforced via `ISSUANCE_BLOCKERS` without a dedicated commercial decision record; operators must configure data, not approve new rules:

| Code | Source |
| --- | --- |
| `SUPPLIER_IDENTITY_UNCONFIGURED` | No active `saas_supplier_identity` |
| `CUSTOMER_LEGAL_NAME_MISSING` | Org `legal_name` empty |
| `CUSTOMER_BILLING_ADDRESS_INCOMPLETE` | Org address fields incomplete |
| `GST_COMPONENTS_UNCONFIGURED` | Tax policy without CGST/SGST/IGST split when required |
| `TAX_COMPONENT_ROUNDING_UNAPPROVED` | Component sum ≠ tax on terms |

---

## 8. GAP-API09-002 — statutory SaaS invoice readiness assessment (2026-11-03)

**Gap code:** GAP-API09-002  
**Assignment:** Policy, schema, dependency, and implementation-readiness only — **no GST implementation started**.  
**Gap status after assessment:** **Blocked** (product + legal/accounting decisions required). Assessment complete ≠ implemented ≠ integration-verified.

### 8.1 Current implementation inventory

| Layer | Implemented (verified in code/tests) | Preview / non-statutory | Not implemented |
| --- | --- | --- | --- |
| Quote → terms → obligations | `SaasCommerceService`; server `calculate_quote` / proration (`INV-005`); `ANNUAL_UPFRONT` + `INSTALLMENT_60_40` obligations | — | Paid-through date (`INV-006`) |
| Payment verify → activation | Mock + webhook paths; obligation `PAID`; subscription activation | Payment receipt ≠ tax invoice | Live Razorpay (`GAP-API09-003`) |
| Invoice preview | `SaasInvoiceService.preview` — **in-memory**; `status=PREVIEW`, `not_a_tax_invoice: true`, no DB row, no number | PDF preview (`preview/pdf`) with banner | — |
| Invoice issue | `SaasInvoiceService.issue` — persists `commercial.saas_invoice*` when blockers cleared | — | **No successful statutory issue in CI** (blockers always present in cold/real paths) |
| Amounts on invoice | From **accepted terms** (`amounts_from_terms`); line mirrors quote totals; proration period from `terms.calculation_inputs` | Preview shows same math + `configuration_gaps` | Per-installment tax split |
| GST components | Policy columns `cgst_percent` / `sgst_percent` / `igst_percent` (migration 034); split math in `invoice_calculator.split_configured_tax` | `EXCLUSIVE_TAX` placeholder when split missing | **Place-of-supply rule** (always adds `PLACE_OF_SUPPLY_RULE_UNAPPROVED`) |
| Supplier identity | `commercial.saas_supplier_identity` + platform policy admin; snapshot on compose | — | FY-specific numbering series; HSN/SAC on lines |
| Customer identity | Org `legal_name`, `address_payload`, encrypted GSTIN (`gstin_ciphertext`, mask on API) | Invoice API never returns full GSTIN | B2C / unregistered recipient policy |
| Numbering | Row lock on supplier; `{prefix}-{next:06d}`; global unique index | — | Financial-year reset; cancellation of sequence gaps |
| Immutability | Trigger `trg_saas_invoice_guard_issued_rewrite`; one `ISSUED` row per `terms_id` | — | Credit notes (`INV-004`) |
| Payment reconciliation | `saas_invoice_payment` + `apply_verified_attempt` updates `amount_received` / `payment_status` on **issued** invoice only | Verify without issued invoice does not create tax doc | Refund → credit note |
| PDF | `invoice_document.py` + ReportLab; disclaimer: not e-invoice / not compliance by itself | Preview PDF | IRN/IRP, signed statutory template (`INV-007`) |
| Audit | `SAAS_INVOICE_ISSUED` via subscription helper | — | Credit-note audit trail |
| API surface (extras) | `saas_invoices_preview_create`, `saas_invoices_create`, list/get/pdf; platform read-only list/get/pdf | — | Credit note APIs |
| UI | Flutter `saas_invoice_*`, platform masterdata invoice pages | Print dialog from backend strings | — |
| API-08 facility billing | Separate `billing.invoices` / membership path | — | Must not merge with SaaS commerce |

**Explicit:** Invoice **preview** and preview PDF are **not** statutory tax invoices. Issued rows are intended as `TAX_INVOICE` but **`issue` raises `ValidationFailed`** while any `ISSUANCE_BLOCKERS` gap remains (today: always for realistic configs until INV decisions land).

### 8.2 Statutory invoice requirements matrix

Legend: **Existing** = in codebase today · **Missing** = required for statutory compliance, not done · **Decision** = product owner · **Legal** = statutory tax advisor / finance · **Deps** = cross-module · **Schema** = migration only after policy approved.

| Area | Existing implementation | Missing implementation | Required business/product decision | Required legal/accounting validation | API/module dependencies | Schema / migration (proposed scope) |
| --- | --- | --- | --- | --- | --- | --- |
| **A. Supplier legal identity & GSTIN** | Active `saas_supplier_identity`: legal name, registered address, **plaintext supplier GSTIN**, state name/code, invoice prefix | Production supplier row seeding; rotation/expiry ops; statutory fields (PAN, CIN, logo) if required on face of invoice | Which Digitize legal entity supplies SaaS; single vs multi-GSTIN | Confirm registered address and GSTIN on tax invoice face | API-09 platform supplier policy admin; API-13 audit on policy change | None if current table sufficient; optional columns after legal field list approved |
| **B. Customer/recipient identity, address, GSTIN** | Org `legal_name`; `primary_address` → `address_payload`; GSTIN encrypted at rest; APIs expose mask only | **Billing address** is org primary only (no separate billing profile); GSTIN **not** in persisted invoice JSON plaintext (`_customer_snapshot_for_storage` strips `gstin`); optional `state_code` on org address not in `OrganizationAddressIn` schema | B2B-only vs B2C; whether GSTIN mandatory for issue; separate billing address vs registered office | Valid tax invoice fields for B2B recipient; GSTIN display rules | **API-02** org update + identifier encryption; invoice compose reads org only | Possible `state_code` on org address JSON or column; optional billing address entity — **decision first** |
| **C. Supplier & recipient state** | Supplier `state_code` (2-digit) in supplier identity | Customer `state_code` often **null** (only `state_province` text collected) | Map states to GST state codes at onboarding | Code list aligns with GST law | API-02 address capture; invoice `_customer_snapshot` | Validate/enforce `state_code` on org address when GST issue required |
| **D. Place of supply** | `tax_snapshot.place_of_supply: null`, `place_of_supply_rule: PLACE_OF_SUPPLY_RULE_UNAPPROVED`; gap always appended when CGST/SGST/IGST configured | Rule engine comparing supplier state vs recipient state (or POS override for B2B) | **INV-001:** approved POS rule for Digitize SaaS (likely 12(2)(b) B2B default — **not assumed**) | Statutory POS for software/SaaS supply | API-09 invoice compose + calculator | Store resolved POS + rule id on `tax_snapshot` (JSON OK) |
| **E. CGST / SGST / IGST** | Tax policy allows CGST+SGST **or** IGST split; amounts computed from **terms** taxable value; `saas_invoice_tax_component` rows | **No selection** of IGST vs CGST+SGST from POS; both configs can exist in DB but POS gap blocks issue | Tie component set to INV-001 outcome | Rate correctness (18% etc.) from finance; not hard-coded in app | API-09 policies + invoice issue | None if rule-only; else snapshot fields for component rationale |
| **F. Invoice numbering** | Monotonic `invoice_number_next` per supplier row; format `{prefix}-{6d}`; unique index | Financial-year series reset; gap handling on cancel; e-invoice IRN linkage | Series per FY vs continuous; prefix convention | GST invoice serial number rules (Sec 31) | API-09 issue path | Possible FY column or separate series table — **after legal** |
| **G. Issue date & tax point** | `issue_date = utc_now().date()` at issue; `issued_at` timestamp; period from terms/proration snapshot | Tax point vs payment date vs service period for SaaS; back-dated issue prohibition | When OA may issue (on accept, on first payment, on activation) | Time of supply rules for continuous service / advance | API-09 terms + payment timestamps | Optional explicit `tax_point_date` on invoice — decision |
| **H. Annual upfront billing** | Single obligation `UPFRONT`; invoice totals = full terms payable; issue blocked by INV-001/002 + config gaps only | End-to-end **issued** annual invoice on real DB with configured supplier/tax/POS | Confirm one tax invoice per annual terms cycle (matches `uq_saas_invoice_terms_issued`) | Full invoice content checklist | API-09 checkout + issue | None beyond POS/GSTIN decisions |
| **I. 60/40 installment billing** | Quote + 60% / 40% obligations; installment 2 due +3 calendar months (`installment_due_at` in quote inputs); checkout/verify **allowed**; **`INSTALLMENT_INVOICE_DOCUMENT_POLICY_UNAPPROVED` blocks issue** | Tax document per installment vs single annual; partial `amount_received` on one invoice; second payment after issue | **INV-003** (see §8.3) | GST treatment of split payments / advances | API-09 obligations + invoice payment apply | Likely **schema** if multiple issued docs per terms (relax unique index, link `obligation_id`) |
| **J. Credit notes & corrections** | Metadata gap `CREDIT_NOTE_GST_RULES_UNAPPROVED`; issued invoice immutable | Credit note entity, reversal, link to payment/refund | **INV-004** workflow | CN numbering and GST reversal | API-09 + future Razorpay refund | New tables — **not authorized** |
| **K. Immutable snapshots** | Supplier/customer/tax JSON on issue; trigger blocks legal field updates; quote inputs embedded in `tax_snapshot.quote_inputs` | Plaintext GSTIN on stored snapshot (by design ciphertext key); line description generic | Whether ciphertext + decrypt-at-PDF satisfies “invoice copy” retention | Record-keeping duration and fields | API-02 encryption; API-09 PDF | Optional encrypted GSTIN in snapshot already partially there |
| **L. Audit & access control** | `SAAS_INVOICE_ISSUED`; tenant facility scope; platform read-only governance; PA cannot issue tenant invoice | Credit note / reissue audit | Who may issue (role — today subscription perms) | SOX/statutory access | **API-03** permissions; **API-13** | None |

### 8.3 60/40 installment tax-document analysis (frozen commercial rule)

**Frozen (unchanged):** 60% first installment (`INSTALLMENT_1`), 40% second (`INSTALLMENT_2`); second due = effective/start date + **3 calendar months** same day, subject to `BLOCK_MONTH_END` / proration forcing `ANNUAL_UPFRONT` when second due ≥ renewal.

**Current technical shape:**

- One `saas_commercial_terms` row carries **full-year** list/discount/tax/payable totals (same as annual).
- Two payment obligations; verify marks each `PAID` independently; activation typically after first verified payment (commerce service).
- Invoice model assumes **one issued tax invoice per terms** (`uq_saas_invoice_terms_issued`), with `invoice_total` = **full** payable and `amount_received` updated via `apply_verified_attempt` (PARTIALLY_PAID → PAID).
- Issuance is **hard-blocked** for `INSTALLMENT_60_40` via `GAP_INSTALLMENT_INVOICE_POLICY`.

**Tax-document lifecycle options (product must choose — not implemented):**

| Option | Description | Implications for current schema |
| --- | --- | --- |
| **1. Single tax invoice at contract acceptance** | One invoice for full taxable value; payments are receipts against it | Aligns with current totals + `apply_verified_attempt`; still need INV-001/002; clarify issue timing vs first payment |
| **2. Tax invoice on each installment** | Two invoices (60% and 40% taxable/tax amounts) | Requires **INV-003**; split tax proportionally; **multiple** issued rows per terms; unique index + `obligation_id` semantics must change |
| **3. Tax invoice only when fully paid** | Issue once at 100% received | Conflicts with common GST practice for advances; needs legal validation |
| **4. Proforma / payment voucher + final tax invoice** | Non-statutory docs on partial pay | New document kinds; not in schema today |

**Not interchangeable:** Razorpay payment confirmation, checkout success UI, invoice **preview**, and **issued** `TAX_INVOICE` serve different purposes — only the latter is gated by `ISSUANCE_BLOCKERS`.

### 8.4 Cross-module dependency findings

| Module | Finding | Blocks statutory SaaS issue? |
| --- | --- | --- |
| **API-02** | Org address lacks enforced GST **state code** in create/update schema; invoice uses org primary address only | **Yes** for POS/component selection unless rule uses name-only mapping (not implemented) |
| **API-02** | GSTIN capture + encryption works; invoice issue clears GSTIN blocker when decrypt succeeds but **does not persist plaintext** on invoice row | **Policy/legal** — may block if statutory copy requires plaintext field on document |
| **API-03** | Issue attributed to `issued_by` principal; facility scope enforced; PA blocked from tenant issue | No defect for initial issue |
| **API-08** | Separate billing domain; no shared invoice numbers | No merge required (frozen) |
| **API-09** | Commerce + invoice services complete **scaffold**; fail-closed gates correct | No code defect — **policy** gaps |
| **API-13** | Audit on issue event | No defect; credit notes would need new actions |

No unrelated module expansion required before decisions; **API-02 address/state_code** is the only concrete **data-model dependency defect** for POS implementation.

### 8.5 Required product decisions (registry IDs)

| ID | Decision | Status |
| --- | --- | --- |
| INV-001 | Place of supply + IGST vs CGST/SGST rule | Open |
| INV-002 | Customer GSTIN on issued document (plaintext vs decrypt-at-render + ciphertext snapshot) | Open |
| INV-003 | Installment tax-document model (§8.3) | Open |
| INV-004 | Credit notes / cancellations | Open (launch) |
| INV-006 | Paid-through (UX) | Open (launch) |
| INV-007 | PDF / e-invoice format | Open (launch) |
| INV-008 | Month-end installment calendar | Open (quote edge cases) |
| INV-009 | Discount on installments | Open when discount &gt; 0 |
| INV-005 | Proration | **Closed** — do not reopen |

### 8.6 Required legal/accounting validations

- Confirm **time of supply** and **invoice issue timing** for annual SaaS and for **partial payments** under chosen INV-003 model.
- Validate **invoice serial number** and **financial year** rules for the supplier GSTIN.
- Validate **face-of-invoice mandatory fields** (HSN/SAC for SaaS, recipient GSTIN, signature, reverse charge if any).
- Confirm **POS** rule for B2B SaaS subscriptions billed per facility.
- Confirm whether **encrypted GSTIN snapshot** satisfies record-keeping if API redacts plaintext.

### 8.7 Proposed schema / migration scope (not authorized)

**Do not migrate until INV-001, INV-002, INV-003 decided.**

| Change | Trigger |
| --- | --- |
| Relax `uq_saas_invoice_terms_issued` / use `obligation_id` | INV-003 option 2 (multi-invoice) |
| `saas_credit_note*` tables | INV-004 |
| Org `state_code` validation or billing address table | API-02 + POS rule |
| FY numbering columns on supplier identity | Legal FY series rule |
| Line-item HSN/SAC, service description codes | Legal field list |
| E-invoice IRN storage | INV-007 |

### 8.8 Implementation sequence (after authorization only)

1. **Product + legal sign-off:** INV-001, INV-002, INV-003 (minimum to start).
2. **API-02:** Enforce/collect recipient state code (and billing address if decided).
3. **API-09:** Implement POS rule; remove `PLACE_OF_SUPPLY` from blockers when satisfied; implement INV-003 invoice lifecycle (single or multi-doc).
4. **Configure** supplier identity + tax policy in platform masterdata (non-code).
5. **Tests:** Extend `test_invoice_calculator.py`, `test_saas_invoice_service.py`; add opt-in PG issue test (mirror proration guard) on local `digitize` — **no** `digitize_test` mutation.
6. **INV-004 / INV-007** in later phase.

### 8.9 Tests and integration-verification plan

| Test | Today | After authorized implementation |
| --- | --- | --- |
| Preview never persists / no number | **PASS** | Keep |
| Installment cannot issue | **PASS** (`test_installment_terms_cannot_issue_tax_invoice`) | Replace/extend per INV-003 |
| GSTIN decrypt clears blocker | **PASS** (`test_saas_invoice_gstin_retrieval.py`) | Add issuance success path |
| Cold DB immutability / concurrency | **PASS** (migration 034) | Keep |
| End-to-end issue reaching numbering | **Not exercised** (blockers) | Opt-in `DIGITIZE_SAAS_INVOICE_PG_TEST=1` (proposed) on `digitize` only |
| PG read-after-write issued invoice | **Not claimed** | Required for integration-verified GAP-API09-002 |

### 8.10 Blockers and deferred items

**Blockers (GAP-API09-002 remains blocked):** INV-001, INV-002, INV-003; configured supplier/tax data; API-02 state code; legal validations in §8.6.

**Deferred (do not block sandbox pay / activation):** INV-004, INV-006, INV-007, live Razorpay (`GAP-API09-003`), EQ-011.

**Verified unchanged:** INV-005 proration; 60/40 math; API-08 separation; transaction idempotency on issue (`issued_invoice_for_terms` idempotent return).

### 8.11 Smallest decision set to **begin** implementation

1. **INV-001** — Approved place-of-supply rule and resulting **CGST+SGST vs IGST** selection inputs (supplier state + recipient state code source).
2. **INV-003** — Choose one installment tax-document model (§8.3); if not single full-value invoice, authorize schema change scope.
3. **INV-002** — Whether issued invoice snapshot/PDF may use **decrypt-at-render** with ciphertext stored, or requires **plaintext GSTIN** on persisted snapshot (privacy trade-off).

Until those three are approved in writing, **implementation is not authorized** and GAP-API09-002 stays **Blocked**.

---

## 9. Decision-resolution package — INV-001, INV-003, INV-002 (2026-11-03)

**Purpose:** Prepare sign-off-ready decision records for the three minimum blockers. **No option is selected here.** **No GST logic, migrations, commerce changes, or statutory records** were created for this package.

**Status vocabulary:**

| Label | Meaning |
| --- | --- |
| **Product decision** | Commercial product owner must approve in writing |
| **Legal/accounting validation** | External statutory tax advisor / finance must confirm |
| **Technical recommendation** | Engineering proposal only — **not** business approval |
| **Can implement without decision?** | **No** for all three INV items below |

### 9.0 Decision ownership summary

| ID | Product / business owner decision | Legal / accounting validation | Technical consequence (after approval) | Dependencies | Implement without decision? |
| --- | --- | --- | --- | --- | --- |
| **INV-001** | POS rule; recipient state source; billing address scope; invalid-state handling | POS for B2B SaaS; IGST vs CGST+SGST for chosen POS | `invoice_calculator` + `_compose` POS engine; clear `PLACE_OF_SUPPLY` gap when inputs valid | API-02 state code; API-09 policies; configured supplier | **No** |
| **INV-003** | Select one tax-document model (Options 1–4 in §9.2) | Time of supply & tax on advances/part payments for chosen model | Issue timing; possibly multi-row invoices; remove installment policy gap per model | INV-001/002 for any issued tax invoice; may need migration | **No** |
| **INV-002** | Policy A (plaintext snapshot) vs B (ciphertext snapshot + controlled decrypt) | Record-keeping & invoice copy requirements for recipient GSTIN | `_customer_snapshot_for_storage`; issuance blocker; PDF path | API-02 encryption; API-03/13 access | **No** |

---

### 9.1 INV-001 — Place of supply and CGST/SGST versus IGST

#### 9.1.1 Current system facts (not decisions)

- **Supplier:** Active row in `commercial.saas_supplier_identity` supplies legal name, registered address, **plaintext supplier GSTIN**, `state_name`, **`state_code` (2-digit GST state code)**, invoice prefix. Platform masterdata admin configures this (API-09 extras).
- **Recipient:** Invoice `_customer_snapshot()` reads **organization** `legal_name` and **`address_payload`** (API-02 `primary_address`). It copies `state_province` into `state_name` and reads optional `address_payload.state_code` — **not validated** on org create/update (`OrganizationAddressIn` has **no** `state_code` field).
- **Facility:** SaaS subscription and invoice rows are **facility-scoped** (`facility_id` on terms/invoice), but **no facility site address** is used for invoice customer snapshot today.
- **Tax policy:** Platform `saas_tax_policy` may define **either** CGST+SGST **or** IGST percents (migration 034 constraint). Invoice arithmetic uses **accepted terms** totals; components are derived in `split_configured_tax`, but **`GAP_PLACE_OF_SUPPLY` is always appended** when split is configured — issuance blocked.

#### 9.1.2 Decisions required — supplier

| # | Decision question | Product / business owner | Legal / accounting validation | Software note (implementation choice after approval) |
| --- | --- | --- | --- | --- |
| S1 | Which **legal entity** is supplier for Digitize SaaS (single GSTIN)? | **Required** | Confirm registration covers SaaS/software supply | Configure one active `saas_supplier_identity` |
| S2 | Is supplier **`state_code`** always taken from configured supplier identity (not inferred from GSTIN prefix alone)? | **Required** | Confirm state on registration matches code used on invoice | Snapshot uses row fields as today |
| S3 | Supplier address on invoice = **registered address** from supplier identity only? | **Required** | Face-of-invoice address rules | No facility/org override unless product adds one |

#### 9.1.3 Decisions required — recipient state and address

| # | Decision question | Product / business owner | Legal / accounting validation | Software note |
| --- | --- | --- | --- | --- |
| R1 | **Authoritative recipient state code** for POS: mandatory **`state_code` on org billing address**, not free-text `state_province`? | **Required** — **do not rely on province text alone** | Confirm code list (01–37 + UT codes) | API-02 must collect/validate; invoice reads stored code |
| R2 | **Billing address source:** organization **`primary_address` only**, or separate **billing address** entity/field? | **Required** | Whether POS follows billing address vs principal place of business | Today: org primary only; facility address **not** used |
| R3 | If org operates facilities in **multiple states**, is SaaS POS always **org billing state** (not facility state)? | **Required** | Multi-state B2B POS for SaaS billed per facility | DR-019: billable unit = facility; **POS may still be org-level** — product must confirm |
| R4 | **B2B scope:** Is SaaS tax invoice issue **limited to registered GST customers** (GSTIN on file), or also B2C/unregistered? | **Required** | B2C invoice rules if allowed | Today: GSTIN gap blocks issue without decryptable GSTIN |
| R5 | **Missing `state_code`:** block issue, or allow issue with gap (fail-closed today)? | **Required** | N/A | **Technical recommendation:** remain **fail-closed** until R1 satisfied |

#### 9.1.4 Decisions required — place of supply and component selection

| # | Decision question | Product / business owner | Legal / accounting validation | Software note |
| --- | --- | --- | --- | --- |
| P1 | **Approved POS rule** for B2B SaaS (e.g. recipient location vs supplier location — **statute section and narrative must be written by advisor, not engineering**) | **Required** | **Primary external validation** for INV-001 | Implement as `place_of_supply_rule` id + resolved POS in `tax_snapshot` |
| P2 | Given approved POS, **when to apply IGST** vs **CGST+SGST** (typically interstate vs intrastate — **exact test is legal, not assumed here**) | **Required** | Confirm for software/SaaS supply type | Select component set at issue; do not use both IGST and CGST+SGST rows |
| P3 | **Invalid or unknown state code** (wrong length, not in approved list, supplier code missing): hard block issue? | **Required** | N/A | **Technical recommendation:** block with validation error + audit-safe message |
| P4 | **Export / SEZ / reverse charge** scenarios in scope for v1? | **Required** | If yes, separate rules | **Technical recommendation:** v1 **out of scope** unless product explicitly includes |

#### 9.1.5 Required API-02 changes (after INV-001 product + legal approval)

These are **implementation consequences**, not substitutes for P1/P2:

| Change | Trigger | Authorization |
| --- | --- | --- |
| Add **`state_code`** to `OrganizationAddressIn` / org address JSON with **GST state code validation** | R1 | After R1 approved |
| Reject org save or invoice issue when `state_code` missing for orgs required to receive B2B tax invoices | R4, R5 | After R4/R5 approved |
| Optional separate **billing address** if R2 ≠ primary only | R2 | Product schema decision first |
| **No** mapping table from `state_province` free text to code without product-approved dictionary | — | **Not recommended** as authoritative POS input |

#### 9.1.6 Technical recommendation only (INV-001)

> **Recommendation (not approved):** For v1 B2B SaaS, use **supplier `state_code` from `saas_supplier_identity`** and **recipient `state_code` from org billing address**; compute **intrastate vs interstate** per **written rule P1/P2** from tax advisor; persist `place_of_supply`, `place_of_supply_rule`, and selected components on issue; remain **fail-closed** when either code missing or POS rule undefined.

#### 9.1.7 Exact sign-off required from product / business owner (INV-001)

1. Written POS rule reference (P1) and component selection rule (P2).  
2. Recipient state source: org billing `state_code` mandatory (R1) and billing address scope (R2, R3).  
3. B2B-only vs B2C (R4) and behavior when state code missing (R5).  
4. Supplier entity and registered address source (S1–S3).

#### 9.1.8 Exact questions for legal / accounting (INV-001)

1. Statutory **place of supply** for B2B SaaS subscription supplied to a company with facilities in one or more states — which address/state code applies given **facility-scoped** billing?  
2. Confirm **IGST vs CGST+SGST** test outputs for: (a) supplier state = recipient state code, (b) different states.  
3. Are **HSN/SAC** and service description mandatory on the same invoice pass (may touch INV-007)?  
4. Confirm supplier GSTIN/state on invoice matches **Digitize** entity actually liable to pay GST on this supply.

---

### 9.2 INV-003 — Installment tax-document model (frozen 60% / 40%, +3 calendar months)

**Frozen commercial terms (not reopened):** obligation amounts remain **60%** and **40%** of quote `payable_total`; installment 2 **`due_at`** from quote `installment_due_at` (+3 months); proration and renewal gates unchanged (`INV-005`).

**Frozen system facts:** one `saas_commercial_terms` row holds **full annual** list/discount/tax/total; obligations `INSTALLMENT_1` / `INSTALLMENT_2`; payment verify does **not** auto-issue tax invoice; installment issue blocked by `INSTALLMENT_INVOICE_DOCUMENT_POLICY_UNAPPROVED`.

**Product must select exactly one option below.** Tables describe consequences — **not a selection**.

#### Option 1 — Single tax invoice for full contract value (payments as receipts)

| Dimension | At 60% payment | At 40% payment | Notes |
| --- | --- | --- | --- |
| Tax invoice issued? | Product decides **issue timing** (e.g. on accept, on first payment, on activation) — **must align with legal time of supply** | Same single invoice if already issued | One `ISSUED` row per `terms_id` matches `uq_saas_invoice_terms_issued` |
| Full annual value on invoice | **Yes** — `invoice_total` = terms `payable_total` (full tax on full taxable value) | Unchanged | Line reflects full subscription period from terms/proration snapshot |
| Tax calculation | Full tax from terms on issue date | N/A second invoice | Reporting: full liability at issue (subject to legal validation) |
| Payment receipt relationship | `saas_invoice_payment` links verify to invoice; `amount_received` 60% → `PARTIALLY_PAID` | 100% → `PAID` | Razorpay receipt ≠ tax invoice |
| Outstanding balance | `outstanding_amount` on same invoice | Updated via `apply_verified_attempt` | Compatible with **current** schema |
| Cancel / refund / credit note | Adjust via **INV-004** (not defined) | Same | Immutable invoice — CN required for corrections |
| Schema | **Minimal** — likely no migration | | Remove installment **policy** gap when model approved + timing rule set |
| Obligations / verify | **Compatible** — no obligation math change | | |

#### Option 2 — Tax invoice per installment (60% doc, then 40% doc)

| Dimension | At 60% payment | At 40% payment | Notes |
| --- | --- | --- | --- |
| Tax invoice issued? | **First** issued invoice (~60% taxable + proportional tax) | **Second** issued invoice (~40% + tax) | Two serial numbers |
| Full annual value | **Split** across two documents | Second completes contract value | Terms row still stores full totals for quote integrity |
| Tax calculation | ~60% of taxable value & tax (rounded per approved rule) | ~40% remainder; rounding policy **required** | Product + finance must approve split rounding |
| Payment receipt relationship | Each `saas_invoice_payment` tied to obligation-specific invoice | Second payment on second invoice | `obligation_id` on invoice row becomes meaningful |
| Outstanding balance | Per-invoice outstanding, not single contract balance | | **Breaking change** vs current single-invoice model |
| Cancel / refund / CN | Per-invoice CN likely | | **INV-004** must cover partial contract cancel |
| Schema | **Required:** relax `uq_saas_invoice_terms_issued`; unique per `(terms_id, obligation_id)` or sequence; possibly `document_sequence` | | Migration **not authorized** until Option 2 selected |
| Obligations / verify | Issue first invoice on `INSTALLMENT_1` verify; second on `INSTALLMENT_2` verify (typical — **product must confirm**) | | Compatible if issue gated on verify |

#### Option 3 — Tax invoice only when 100% paid

| Dimension | At 60% payment | At 40% payment | Notes |
| --- | --- | --- | --- |
| Tax invoice issued? | **No** statutory invoice (may show preview only) | **Yes** — full value at second payment | |
| Full annual value | Deferred until paid in full | Full `payable_total` on one invoice | |
| Tax calculation | Deferred | Full tax at issue | **Legal validation critical** — advance/ TOS rules |
| Payment receipt relationship | Payments without tax invoice until complete | Final invoice links both payments | May need non-statutory payment acknowledgment (product) |
| Outstanding balance | N/A until issue | Zero after issue | `apply_verified_attempt` runs only after issue exists today |
| Cancel / refund / CN | Complex if first payment without invoice | | |
| Schema | Near Option 1 single invoice | | Issue gate = all obligations `PAID` |
| Obligations / verify | **Compatible** with obligation model | | **Conflict risk** with GST advance invoice practice — **legal must rule** |

#### Option 4 — Proforma / payment voucher + final tax invoice

| Dimension | At 60% payment | At 40% payment | Notes |
| --- | --- | --- | --- |
| Tax invoice issued? | **Non-statutory** document kind (new) | Final **TAX_INVOICE** for full or remaining value — **product must define** | Not in `document_kind` enum today |
| Full annual value | On proforma (non-GST or non-deductible?) | On final tax invoice | |
| Tax calculation | **Product + legal** define whether tax shown on proforma | Final tax per advisor | |
| Payment receipt relationship | Three document types in play | | Highest UI/ops complexity |
| Outstanding balance | Product-defined | | |
| Cancel / refund / CN | Multiple doc types | | |
| Schema | **New** `document_kind` values + workflows | | Largest scope |
| Obligations / verify | Compatible if vouchers are non-blocking | | |

#### 9.2.1 Technical recommendation only (INV-003)

> **Recommendation (not approved):** If legal confirms **single tax invoice for full subscription value** is acceptable with **partial payments** as receipts (Option 1), prefer Option 1 for **schema compatibility** with migration 034 and existing `apply_verified_attempt`. If advisor requires **tax invoice per collection**, Option 2 with explicit rounding rules — authorize migration only after written selection.

#### 9.2.2 Exact sign-off required from product / business owner (INV-003)

1. **Select Option 1, 2, 3, or 4** (one only).  
2. For chosen option: **when** OA/system may issue (relative to terms accept, first verify, second verify, 100% paid).  
3. For Option 2 or 4: authorize **schema/document_kind** scope.  
4. Confirm **no change** to 60/40 amounts or +3-month due rule.

#### 9.2.3 Exact questions for legal / accounting (INV-003)

1. For **60/40 B2B SaaS**, is one tax invoice for the **full annual taxable value** permitted while payments are collected in two parts? If yes, **time of supply** and tax reporting dates?  
2. If not, must each installment payment trigger a **separate tax invoice** with proportional tax? Rounding rules?  
3. Treatment of **first payment before tax invoice** under Option 3 — compliant or not?  
4. Are **payment receipts** from Razorpay sufficient for any period without a tax invoice?  
5. How do **credit notes** interact with partial installment billing (**INV-004** dependency)?

---

### 9.3 INV-002 — GSTIN persistence on statutory invoice snapshot

**Current behavior:**

- Org GSTIN: encrypted (`gstin_ciphertext`), API returns **mask** only.  
- On compose: decrypt can **clear** `CUSTOMER_GSTIN_PLAINTEXT_UNAVAILABLE` for issuance check; `_customer_snapshot_for_storage` **strips plaintext `gstin`** before persist; snapshot may store **`gstin_ciphertext` + DEK version** keys.  
- PDF: `_enrich_customer_gstin_for_tax_document` decrypts for **render** only; tenant GET invoice API still redacts via `_customer_for_api`.  
- **Fail-closed:** without decryptable GSTIN, issuance blocker remains.

#### Policy A — Plaintext recipient GSTIN in immutable invoice snapshot (restricted storage)

| Topic | Assessment |
| --- | --- |
| Reproducibility | **High** — re-render PDF/historical view from snapshot alone; no live org decrypt |
| Key rotation | Snapshot independent of org DEK rotation **if GSTIN copied at issue** |
| Access control | Must **not** expose via general org/list APIs; restrict GET invoice + PDF to authorized roles; platform governance read policy |
| Logging / audit | Risk of GSTIN in logs if payloads logged — require redaction in API-13/log pipelines |
| PDF / re-render | Trivial from snapshot |
| Retention / privacy | GSTIN duplicated on invoice row; retention follows invoice retention policy; DPA/privacy sign-off **required** |

#### Policy B — Encrypted GSTIN in snapshot; plaintext only on authorized render (status quo direction)

| Topic | Assessment |
| --- | --- |
| Reproducibility | **Depends on org DEK** + ciphertext in snapshot; historical re-render needs decrypt path |
| Key rotation | Must store **`gstin_dek_version`** on snapshot (partially done); rotation strategy for **old invoices** must be defined |
| Access control | Decrypt only in invoice PDF/issue-detail path with same RBAC as A |
| Logging / audit | Lower risk of plaintext in persisted JSON; audit events must not dump decrypted GSTIN |
| PDF / re-render | Requires `_enrich_customer_gstin_for_tax_document` (or successor) on every render |
| Retention / privacy | Fewer plaintext copies; **legal must confirm** encrypted copy satisfies “invoice copy” rules |

#### 9.3.1 Comparison summary

| Criterion | Policy A (plaintext on snapshot) | Policy B (ciphertext on snapshot) |
| --- | --- | --- |
| Statutory reproducibility without live org | Stronger | Weaker unless legal accepts decrypt-from-snapshot |
| Privacy / minimization | Weaker (extra plaintext copy) | Stronger |
| Implementation delta from today | Persist `gstin` at issue (restricted column/json); tighten API redaction | Formalize B as approved path; document rotation; possibly remove misleading issuance gap when ciphertext present |
| General API exposure | **Forbidden** for both — no change to org APIs | Same |

#### 9.3.2 Technical recommendation only (INV-002)

> **Recommendation (not approved):** Prefer **Policy B** if legal/accounting confirms that **encrypted recipient GSTIN in immutable snapshot + controlled decrypt for PDF/authorized export** meets record-keeping; adjust issuance blocker to require **ciphertext + successful decrypt at issue** rather than plaintext in JSON. If legal requires **literal GSTIN field on stored invoice copy**, adopt **Policy A** with **strict RBAC** and **no plaintext in tenant list endpoints or audit payloads**.

#### 9.3.3 Exact sign-off required from product / business owner (INV-002)

1. Choose **Policy A or B**.  
2. Approve **who** may view full GSTIN on issued invoice (roles/scopes — API-03, no new roles without authorization).  
3. Approve retention period and whether invoice snapshot GSTIN survives org GSTIN update/delete.

#### 9.3.4 Exact questions for legal / accounting / privacy (INV-002)

1. Must a **stored tax invoice copy** include recipient GSTIN in **human-readable** form, or is **encrypted-at-rest with controlled display** sufficient?  
2. If org **changes GSTIN** after issue, which GSTIN appears on **re-print** of historical invoice — snapshot only?  
3. Data protection: is duplicate plaintext GSTIN on `saas_invoice.customer_snapshot` acceptable under your DPA?  
4. E-invoice / IRP future (**INV-007**): does IRP submission require plaintext at submission time regardless of storage policy?

---

### 9.4 Dependency implementation sequence (after all three decisions + validations)

**Order is sequential; no step starts without prior approvals.**

| Step | Work | Gated by |
| --- | --- | --- |
| 1 | Written approval: INV-001, INV-002, INV-003 + legal answers in §9.1.8, §9.2.3, §9.3.4 | Product + advisor |
| 2 | API-02: `state_code` (+ optional billing address) per INV-001 R1/R2 | INV-001 |
| 3 | API-09: POS + component selection; GSTIN snapshot policy; installment issue lifecycle | INV-001, INV-002, INV-003 |
| 4 | Platform configure supplier + tax policy (non-code) | Ops |
| 5 | Tests + opt-in PG issue IV on local `digitize` | Engineering |
| 6 | INV-004 / INV-007 follow-on | Separate authorization |

**GAP-API09-002** remains **Blocked — product decisions and legal/accounting validation required** until step 1 is complete.

### 9.5 Package completion attestation (2026-11-03)

| Assertion | Status |
| --- | --- |
| GST logic implemented | **No** |
| Migrations created/applied | **No** |
| Statutory / production financial records | **No** |
| Commerce, proration (INV-005), 60/40 math changed | **No** |
| Invoice issue fail-closed behavior changed | **No** |
| `digitize_test`, QA, RDS, production touched | **No** |
| Live payment providers | **No** |
