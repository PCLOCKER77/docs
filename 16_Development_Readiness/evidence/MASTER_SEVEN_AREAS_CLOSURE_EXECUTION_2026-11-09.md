# Master — seven remaining development areas (execution + consolidated approvals)

**Date:** 2026-11-09  
**Authority:** Repository code, `var/api_audit_matrix.csv`, DEV-19/21/22/23, decision registers, frozen 228 inventory.  
**Session result:** No unauthorized schema, route, provider, or statutory changes. Engineering already delivered where authorized; outstanding items require explicit decisions below.

---

## Summary status (seven areas)

| # | Area | Gap / scope | Status label |
|---|------|-------------|----------------|
| A | Statutory SaaS invoices | GAP-API09-002 | **AWAITING_LEGAL_OR_ACCOUNTING_APPROVAL** |
| B | Cheque-bounce automation | GAP-API09-005 | **IMPLEMENTED** (mig 084 — see GAP-API09-005 evidence) |
| C | Production email / SMS | GAP-INT-001, GAP-INT-002, GAP-API11-001 | **BOUNDARY IMPLEMENTED** — live SES/MSG91/Meta still **AWAITING_PROVIDER_CONFIGURATION** |
| D | Membership / training deferrals | GAP-API05-001, GAP-API07-001/002 | **DEFERRED_BY_APPROVED_DECISION** |
| E | Audit / reference data | API-13, API-14 skeletons | **AWAITING_USER_DECISION** |
| F | 16 numbered skeletons | See §F table | **DEFERRED_BY_APPROVED_DECISION** (15) · **AWAITING_USER_DECISION** (adjustments) |
| G | Payment receipts API-08-012 | Route + service + PG IV | **IMPLEMENTED_AND_VERIFIED** (backend); Flutter **IMPLEMENTED_NOT_FULLY_VERIFIED** |

**Live inventory:** `NUMBERED_COUNT` = **228** · `BACKEND_IMPLEMENTED` = **212** · `SKELETON_CREATED` = **16** (`contract_numbered_audit.py` 2026-11-09).

---

## A. Statutory SaaS invoices — GAP-API09-002

### Current implementation (preserved)

- Extra-catalog: `saas_invoices_*`, PDF routes, preview/issue, 60/40 installment model, immutable issued snapshots (mig 034).
- **Fail-closed issuance:** `ISSUANCE_BLOCKERS` in `invoice_service.py` (`GAP_SUPPLIER_MISSING`, customer legal/GSTIN, tax components, place of supply, installment document policy).
- Razorpay SaaS checkout **separate** from facility billing; not statutory issuance.

### Technical work already done (not repeated)

- Quote calculator, webhook settlement, Flutter `saas_subscription_admin` + invoice detail with gap display.

### Outstanding (cannot implement without approval)

| Decision ID | Question | Recommended option | Consequence if deferred |
|-------------|----------|-------------------|------------------------|
| INV-001 | Place of supply → CGST/SGST vs IGST | Sign §9.1 in `SAAS_INVOICE_READINESS_DECISION_REGISTRY.md` | Issuance remains blocked |
| INV-002 | Customer GSTIN plaintext policy | Sign §9.3 privacy/storage pack | Issuance remains blocked |
| INV-003 | One statutory doc vs per-installment | Sign §9.2 document policy | Installment issue blocked |
| INV-004…009 | Credit note GST, proration, paid-through, PDF/e-invoice | Per registry §2 table | Launch-only gaps |

**Acceptance criteria (post-approval):** `POST /saas/invoices` succeeds only when configured gaps cleared; PG on `digitize` with real org legal data; no invented tax rates.

**External need:** Complete [GAP-API09-002 statutory invoice professional approval pack](./GAP-API09-002_STATUTORY_INVOICE_PROFESSIONAL_APPROVAL_PACK_2026-11-09.md) §9 signatures → map to registry §9.

---

## B. Cheque-bounce automation — GAP-API09-005

### Current implementation (preserved)

- Cheque offline → `PENDING`; `PaymentTransactionService.clear_cheque_payment` / `bounce_cheque_payment` (internal, **no HTTP routes**).
- Success only via clear/settlement path; bounce does not mark SUCCESS.
- Subscription grace messaging partial (`routes.py` copy only); **no** auto-suspend job.

### Product decision proposal (single sign-off)

| Topic | Existing behavior | Decision required |
|-------|-------------------|-----------------|
| Bounce source | Operator marks bounce via service (HTTP deferred) | Authorize HTTP op vs admin-only internal tool |
| Grace start | Not automated | Calendar: clear date vs bounce date vs custom |
| Grace duration | Not defined | N days (product) |
| Suspension trigger | Manual `subscriptions_suspend` only | Auto-suspend after grace? PA override API? |
| Notifications | None automated | GAP-INT-001/002 dependency |
| Recovery | Replacement payment via existing billing | Reuse offline/online; no new model |

**Status:** **AWAITING_USER_DECISION** — do not implement grace/suspend automation until state machine signed.

**Tests (existing):** offline/cheque paths in `test_offline_payment_invoice_lock.py` (PG opt-in).

---

## C. Production email and SMS — GAP-INT-001 / GAP-INT-002

### Current implementation (preserved)

- **Reports:** `HeldReportNotifier` when SMTP not configured; Mailpit path in dev (`report_email_delivery.py`).
- **SMS:** `SMS_PROVIDER` empty → failures/held; memory provider in tests.
- **OTP:** Flows exist; vendor not configured.

### Provider decision package (one charter per channel)

| Channel | Options | Implementation boundary |
|---------|---------|-------------------------|
| Transactional email | Mailpit dev / SES / SMTP relay | Replace HELD only after tier approved |
| Report schedules | Same as email | GAP-API11-001 |
| SMS OTP | De-scope first release vs Twilio/etc. | GAP-INT-001 user decision 2026-11-08: **deferred first release** |

**Status:** **AWAITING_PROVIDER_CONFIGURATION** — adapters exist; production credentials and FROM domain verification required.

**Do not:** Invent SES/SMS credentials in repo.

---

## D. Membership and training — GAP-API05-001, GAP-API07-001/002

### Proposals (from DR-020 / API-05 brief)

| Gap | Proposal | Recommendation |
|-----|----------|----------------|
| GAP-API05-001 | Extra `GET` list memberships by customer | **Defer** unless desk P0 — keep open-by-ID UX |
| GAP-API07-001 | Extra enrollment list API | **Defer** — batch enroll/remove live |
| GAP-API07-002 | Facility/site schedule conflict enforcement | **Defer** — document trainer-level conflicts only |

**Status:** **DEFERRED_BY_APPROVED_DECISION** — no new numbered/extra APIs without inventory approval.

---

## E. Audit and platform reference data — API-13 / API-14

**Stance (frozen):** Server-side audit append only; **no** client `POST /audit-events` ingestion without product pack.

| Collection | Live reads | Skeleton writes (blocked) |
|------------|------------|---------------------------|
| API-13 | 005, 009, 012 **IMPLEMENTED** | 001–004, 006–008, 010–011 client capture / investigations / archive |
| API-14 | 003, 006, 008, 009, 010, 011 **IMPLEMENTED** | 001–002, 004–005, 007, 012 country/region/language/TZ/activity/localization seeds |

**Decisions required:** Schema ownership for investigations/compliance; GMD seed data sets and update policy (GAP-API14-001…004).

**Status:** **AWAITING_USER_DECISION** — no DDL until packs signed.

---

## F. Sixteen numbered skeletons (exact list)

| API ID | Operation | Backend status | Authorization | Blocker |
|--------|-----------|----------------|---------------|---------|
| API-08-005 | `invoices_adjustments` | SKELETON | Deferred product | No adjustment entity |
| API-13-001 | `audit_events_create` | SKELETON | Blocked | Non-client ingest stance |
| API-13-002 | `authentication_events_create` | SKELETON | Blocked | Same |
| API-13-003 | `audit_events_configuration_changes_create` | SKELETON | Blocked | Same |
| API-13-004 | `security_events_create` | SKELETON | Blocked | Same |
| API-13-006 | `investigations_create` | SKELETON | Blocked | Schema/product |
| API-13-007 | `compliance_records_reports_create` | SKELETON | Blocked | API-11 overlap |
| API-13-008 | `audit_events_archive_create` | SKELETON | Blocked | Retention policy |
| API-13-010 | `audit_policies_update` | SKELETON | Blocked | Policy entity |
| API-13-011 | `compliance_violations_list` | SKELETON | Blocked | Compliance store |
| API-14-001 | `reference_countries_list` | SKELETON | Deferred | Seed pack |
| API-14-002 | `reference_states_regions_list` | SKELETON | Deferred | Seed pack |
| API-14-004 | `reference_languages_list` | SKELETON | Deferred | Seed pack |
| API-14-005 | `reference_timezones_list` | SKELETON | Deferred | Seed pack |
| API-14-007 | `reference_activity_types_list` | SKELETON | Deferred | Ownership vs training |
| API-14-012 | `reference_localization_list` | SKELETON | Deferred | Localization SoT |

**None** of the above are authorized for promotion in this session.

**Follow-up execution (same day):** Dedicated master implementation pass — [MASTER_16_SKELETON_IMPLEMENTATION_REPORT_2026-11-09.md](./MASTER_16_SKELETON_IMPLEMENTATION_REPORT_2026-11-09.md) — confirms **0/16** promotions; inventory still **212/228** implemented.

---

## G. Payment receipts — API-08-012

### Implemented and verified (backend)

- Mig **079** `billing.receipts`; org-wide numbering; `ReceiptService.issue_for_payment_id` (SUCCESS only, idempotent).
- **Route live:** `POST /api/v1/payments/{payment_id}/receipts` (`payments_receipts`, `BACKEND_IMPLEMENTED`).
- Auto-receipt on offline SUCCESS; backfill script `backfill_historical_payment_receipts.py` (assess/dry-run/execute).
- **PG IV:** `test_billing_credit_receipt_recon_http_digitize_postgres.py` — **1 passed** (2026-11-09); pending payment → receipt rejected.

### Flutter

- Facility billing history exposes `receipt_id` on financial events (`facility_billing_history.dart`); **no** dedicated facility receipt PDF/download screen (distinct from SaaS invoice PDF).

### Gaps (not authorization to invent)

| Item | Status |
|------|--------|
| Facility receipt PDF/print | **AWAITING_USER_DECISION** if required beyond ID in history |
| Bulk backfill **execute** on shared `digitize` | **AWAITING_QA_AUTHORIZATION** per backfill script policy |
| Acceptance doc matrix rows | Updated 2026-11-09 to match live backend |

**Status:** **IMPLEMENTED_AND_VERIFIED** (HTTP + PG); Flutter presentation **IMPLEMENTED_NOT_FULLY_VERIFIED** for PDF.

### Tests run (2026-11-09)

```text
pytest tests/billing/test_receipt_backfill_service.py -q  → 3 passed
pytest tests/billing/test_billing_credit_receipt_recon_http_digitize_postgres.py
  (DIGITIZE_BILLING_HTTP_INTEGRATION_PG_TEST=1) → 1 passed
```

---

## Consolidated approval actions (user)

Sign or reply with gap ID + choice:

1. **INV-001…003** — statutory SaaS issue (legal/accountant).  
2. **GAP-API09-005** — cheque grace/suspend state machine.  
3. **GAP-INT-002** — email delivery tier (+ optional SES).  
4. **GAP-INT-001** — SMS in/out of first release.  
5. **GAP-API05-001 / GAP-API07-001/002** — approve extra APIs or confirm deferral.  
6. **API-13 / API-14** — schema + seed packs per operation group.  
7. **API-08-005** — billing adjustments entity or permanent deferral.  
8. **Facility receipt PDF UI** — product scope for Flutter.  
9. **TEST-13** — `digitize_test` EQ-011 (unchanged from master blockers).

---

## Tracker cross-reference

- DEV-19 session log 2026-11-09 (this file).  
- DEV-21 — gap rows unchanged except evidence dates; seven-area scan logged in changelog.  
- `MASTER_REMAINING_BLOCKERS_APPROVAL_PACKAGE_2026-11-08.md` — still authoritative; this document **extends** with seven-area detail only.
