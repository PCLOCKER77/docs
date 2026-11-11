# GAP-API09-002 — SaaS statutory invoice professional approval pack

**Decision groups:** INV-001, INV-002, INV-003  
**Audience:** Accountant · Tax professional · Legal reviewer · Digitize product owner  
**Scope:** Statutory **tax invoices** Digitize issues to **Organization** customers for SaaS subscriptions (extra-catalog `saas_invoices_*`).  
**Authority (technical, unchanged by this pack):** [SAAS_INVOICE_READINESS_DECISION_REGISTRY.md](../../architecture/SAAS_INVOICE_READINESS_DECISION_REGISTRY.md) §9; `app/modules/subscription/commerce/invoice_service.py` (`ISSUANCE_BLOCKERS`).

**Instructions for reviewers:** Answer each item below. Mark each answer:

| Tag | Meaning |
| --- | --- |
| **M** | Legally or statutorily mandatory |
| **A** | Required by accounting practice / internal control |
| **R** | Recommended business practice |
| **O** | Optional preference |

Do **not** assume India-specific GST outcomes unless your firm confirms them. Engineering will **not** clear issuance blockers from advisor text in this document until product owner records formal approval in DEV-19.

---

## 1. Purpose

Digitize implements preview, issuance, history, PDF generation and payment allocation for SaaS invoices. **Statutory issuance remains fail-closed** until configuration and the decisions in INV-001…003 are approved and mapped to code.

---

## 2. Existing commercial design — confirm, do not redesign

Please confirm whether this established model is **acceptable** for statutory/tax treatment, or state **required changes** (with legal basis):

1. Digitize sells SaaS subscriptions to Organizations.  
2. The **Digitize legal entity** is the invoice issuer.  
3. Invoices cover the **approved subscription commitment** (not ad-hoc facility line items as separate tax documents unless you require otherwise).  
4. Payment schedule **60%** initially, **40%** due **three calendar months** after subscription start (same calendar day rule).  
5. **Facility** is the billable unit.  
6. New facilities billable **immediately** with proration (proration policy: **INV-005**, separate from this pack).  
7. Annual discounts are **configurable** (server-side quote).  
8. Advertisements are a **separate** commercial product — **excluded** from SaaS subscription price.  
9. **Invoice issuance** and **payment collection** are separate events.  
10. **Partial payments** must trace to invoice and installment obligations.

| # | Advisor confirmation (acceptable / change required) | Tag | Legal / accounting basis | Effective date |
| --- | --- | --- | --- | --- |
| 1–10 | | | | |

**Issues identified (free text):**

---

## 3. INV-001 — Seller identity and tax treatment

### 3.A Seller identity

| # | Question | Advisor answer | Tag | Basis | Evidence required |
| --- | --- | --- | --- | --- | --- |
| S1 | Exact **legal name** of Digitize invoice issuer | | | | |
| S2 | **Registered business address** on invoice | | | | |
| S3 | **GSTIN** / other tax registration number(s) | | | | |
| S4 | Other **business registration** particulars on invoice | | | | |
| S5 | **Contact** particulars mandatory on invoice | | | | |
| S6 | **Establishment / place of business** identification required? | | | | |

**Software mapping:** Blocker `SUPPLIER_IDENTITY_UNCONFIGURED` until active supplier row configured (registry §9.1.2 S1–S3).

### 3.B Tax treatment

| # | Question | Advisor answer | Tag | Basis |
| --- | --- | --- | --- | --- |
| T1 | Tax **classification** of Digitize SaaS supply (e.g. service category / SAC) | | | |
| T2 | Applicable **rate** and **components** (CGST/SGST/IGST or other) | | | |
| T3 | **IGST vs CGST+SGST** test (state comparison rule) | | | |
| T4 | **Place of supply** determination rule (cite statute/practice) | | | |
| T5 | Effect of customer **GST registered** vs **unregistered** | | | |
| T6 | Treatment when customer has **no GSTIN** | | | |
| T7 | **Interstate** transaction rules for this supply | | | |
| T8 | **Rounding** per component and on taxable value | | | |

**Software mapping:** `GST_COMPONENTS_UNCONFIGURED`, `PLACE_OF_SUPPLY_RULE_UNAPPROVED`, `TAX_COMPONENT_ROUNDING_UNAPPROVED`.

### 3.C Tax identity data

| # | Question | Advisor answer | Tag |
| --- | --- | --- | --- |
| D1 | Seller identifiers to **collect / store / display** | | |
| D2 | Customer identifiers to **collect / store / display** | | |
| D3 | **Masking, encryption, access, retention** for GSTIN and related IDs | | |

Cross-reference: registry **§9.1.8** (legal questions P1–P4).

---

## 4. INV-002 — Customer details and commercial invoice policy

### 4.A Customer particulars

| Field | Mandatory on invoice? | Source of truth | Tag | Notes |
| --- | --- | --- | --- | --- |
| Legal name | | Org legal identity | | → `CUSTOMER_LEGAL_NAME_MISSING` |
| Billing address | | Org address today | | → `CUSTOMER_BILLING_ADDRESS_INCOMPLETE` |
| State / **state code** | | **Must define** (registry R1) | | |
| GSTIN | | Encrypted org field | | → `CUSTOMER_GSTIN_PLAINTEXT_UNAVAILABLE` |
| Contact details | | | | |
| Other | | | | |

### 4.B Policy questions

| # | Question | Advisor answer | Tag |
| --- | --- | --- | --- |
| C1 | Registered vs **billing** address may differ? | | |
| C2 | Separate **billing profile** required? | | |
| C3 | Customer data **changes after issue** — re-print / snapshot rule | | |
| C4 | **Facility add + proration** on invoice presentation | | |
| C5 | **Annual discount** line presentation | | |
| C6 | 60/40 schedule affects **invoice timing** or **payments only**? | | |
| C7 | **One invoice** for full commitment vs per-installment tax documents | | |

For C7, select **one** model (registry §9.2 Options 1–4):

- [ ] **Option 1** — Single tax invoice (full value; payments as receipts)  
- [ ] **Option 2** — Tax invoice per installment  
- [ ] **Option 3** — Tax invoice only when 100% paid  
- [ ] **Option 4** — Proforma + final tax invoice  
- [ ] **Other (describe):**

**Software mapping:** `INSTALLMENT_INVOICE_DOCUMENT_POLICY_UNAPPROVED` until C6/C7 resolved.

Cross-reference: registry **§9.2.3**, **§9.3** (GSTIN Policy A vs B).

---

## 5. INV-003 — Invoice operations and statutory document controls

### 5.A Invoice timing

| # | Question | Advisor answer | Tag |
| --- | --- | --- | --- |
| I1 | **When** must statutory invoice be issued? | | |
| I2 | Trigger: acceptance / service start / payment / other | | |
| I3 | **Advance payment** documentation before tax invoice? | | |
| I4 | Statutory **deadlines** | | |

### 5.B Invoice numbering

| # | Question | Advisor answer | Tag |
| --- | --- | --- | --- |
| N1 | **Format** and financial-year rules | | |
| N2 | Separate **series** per establishment / type? | | |
| N3 | **Cancelled / void / unused** number handling | | |
| N4 | **Reuse** of numbers permitted? | | |

### 5.C Invoice contents

List **all mandatory** fields, declarations and disclosures (attach schedule if needed):

| Field / declaration | Required? | Tag |
| --- | --- | --- |
| Seller / customer identity | | |
| Number, issue date | | |
| Service description, period | | |
| Billable unit / quantity | | |
| Taxable value, discounts | | |
| Tax components, totals | | |
| Other statutory text | | |

### 5.D Format and retention

| # | Question | Advisor answer | Tag |
| --- | --- | --- | --- |
| F1 | **PDF** acceptable for customer delivery? | | |
| F2 | **E-invoice / government reporting** required (now or later)? | | |
| F3 | **Retention** period and archival controls | | |
| F4 | **Digital signature / QR** required? | | |

### 5.E Corrections and cancellations

| # | Question | Advisor answer | Tag |
| --- | --- | --- | --- |
| E1 | Permitted **correction** process | | |
| E2 | **Credit / debit note** requirements | | → `CREDIT_NOTE_GST_RULES_UNAPPROVED` (INV-004, follow-on) |
| E3 | **Cancel** issued invoice vs CN-only | | |
| E4 | Audit / supporting records | | |

---

## 6. Payment confirmation and receipts (facility + SaaS)

**Product behavior (existing):** Payment initiated → server-confirmed success → payment record → **separate receipt per SUCCESS payment** (API-08-012; mig 079); invoice balance updated; receipt **not** proof of pay before confirm.

| # | Question | Advisor answer | Tag |
| --- | --- | --- | --- |
| R1 | Separate receipt **per successful payment** required? | | |
| R2 | Mandatory **receipt particulars** | | |
| R3 | Receipt = acknowledgement only vs statutory document | | |
| R4 | Separate receipt **numbering series**? | | |
| R5 | **Partial payments** — separate receipts? | | |
| R6 | **Failed / reversed / refunded** treatment | | |
| R7 | **Cheque** — wording while PENDING / after bounce | | |

**Note:** SaaS Razorpay receipts are payment-provider artefacts; **tax invoice** timing remains INV-003.

---

## 7. Issuance blocker resolution map

| Blocker code (application) | INV group | Approved resolution (advisor) | Clears blocker when |
| --- | --- | --- | --- |
| `SUPPLIER_IDENTITY_UNCONFIGURED` | INV-001 | | Supplier row + policy configured |
| `CUSTOMER_LEGAL_NAME_MISSING` | INV-002 | | Org legal name present |
| `CUSTOMER_BILLING_ADDRESS_INCOMPLETE` | INV-002 | | Address rule satisfied |
| `CUSTOMER_GSTIN_PLAINTEXT_UNAVAILABLE` | INV-002 | Policy **A** or **B** (§9.3) | Decrypt/store rule implemented **per policy** |
| `GST_COMPONENTS_UNCONFIGURED` | INV-001 | | Rates/components configured |
| `TAX_COMPONENT_ROUNDING_UNAPPROVED` | INV-001 | | Rounding rule coded |
| `PLACE_OF_SUPPLY_RULE_UNAPPROVED` | INV-001 | P1/P2 written rule | Rule id + logic implemented |
| `INSTALLMENT_INVOICE_DOCUMENT_POLICY_UNAPPROVED` | INV-003 | Option 1–4 selected | Timing + schema authorized |

**GSTIN policy:** System **must not** reconstruct full GSTIN from hash or last-four alone.

| Related (not in `ISSUANCE_BLOCKERS` for issue) | Follow-on |
| --- | --- |
| `PRORATION_POLICY_UNAPPROVED` | INV-005 |
| `CREDIT_NOTE_GST_RULES_UNAPPROVED` | INV-004 |

---

## 8. Advisor response checklist

For each answered section, confirm: **answer · tag (M/A/R/O) · basis · effective date · evidence · separate legal review needed (Y/N).**

**Unresolved items (explicit list):**

1.  
2.  

---

## 9. Approval record

### Accountant / tax professional

| Field | Value |
| --- | --- |
| Name | |
| Firm | |
| Date | |
| Approval / comments | |

### Legal reviewer (if required)

| Field | Value |
| --- | --- |
| Name | |
| Date | |
| Approval / comments | |

### Digitize product decision owner

| Field | Value |
| --- | --- |
| Name | |
| Date | |
| Decision references approved | [ ] INV-001 [ ] INV-002 [ ] INV-003 |

---

## 10. Post-approval engineering sequence (no work before §9 signatures)

1. Map answers to [SAAS_INVOICE_READINESS_DECISION_REGISTRY.md](../../architecture/SAAS_INVOICE_READINESS_DECISION_REGISTRY.md) §9.  
2. Clear only blockers with **written** approved resolution (§7).  
3. Implement approved technical controls (API-02 state code, POS/GSTIN policy, installment timing per selected option).  
4. Run: `test_saas_invoice_service.py`, calculator tests, opt-in PG issue on local `digitize` only.  
5. Verify preview, issue, PDF, payment allocation, receipt separation.  
6. **Fail-closed** for any remaining **M**-tag item without configuration.

**GAP-API09-002** status until §9 complete: **AWAITING_LEGAL_OR_ACCOUNTING_APPROVAL**.
