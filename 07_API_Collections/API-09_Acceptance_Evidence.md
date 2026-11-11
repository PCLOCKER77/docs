# API-09 Subscription / License — Acceptance Evidence

**Document ID:** API-09-EVIDENCE  
**Last updated:** 2026-11-07 (Phase 11 — regression re-verification)  
**Status:** IMPLEMENTATION COMPLETE / INTEGRATION VERIFICATION PARTIAL (approved blockers remain)

All **24 numbered** registry operations are **BACKEND_IMPLEMENTED**. Formal registry **INTEGRATED/CERTIFIED** remains a process gate. **`digitize_test`** live API-09 suite (EQ-011) is separate from local **`digitize`** commerce IV.

## Evidence legend

| Label | Meaning |
|-------|---------|
| **PASS** | Tests or documented live verification |
| **MOCK** | Razorpay mock mode / stub checkout — not live provider |
| **BLOCKED** | Product decision, schema, or external authorization |
| **NOT VERIFIED** | No mutating IV on approved DB for that claim |

## Operation matrix (API-09-001 … API-09-024)

| ID | Registry name | Backend | Flutter | Tests | IV |
|----|---------------|---------|---------|-------|-----|
| 001 | Create Subscription | Implemented | Hub (open-by-ID); no create form | `test_subscription_license.py` | `digitize_test` when EQ-011 |
| 002 | Assign Subscription Plan | Implemented | Detail actions | Same | Same |
| 003 | Activate Subscription | Implemented | Detail | Same + mock checkout | Mock commerce + PG webhook scope |
| 004 | Renew Subscription | Implemented | Detail | `test_subscription_renew*` | Same |
| 005 | Upgrade Subscription Plan | Implemented | Detail | Route tests | Same |
| 006 | Downgrade Subscription Plan | Implemented | Detail | Route tests | Same |
| 007 | Suspend Subscription | Implemented | Detail + platform facility suspend | Live lifecycle tests | Same |
| 008 | Cancel Subscription | Implemented | Detail | Same | Same |
| 009 | Expire Subscription | Implemented | Detail | Same | Same |
| 010 | Generate Renewal Invoice | Implemented | Detail (`terms_id`) | `test_saas_subscription_invoice_lifecycle` | Same |
| 011 | View Subscription History | Implemented | Detail | Same | Same |
| 012 | Generate Subscription Reports | Implemented | Admin hub | Flutter admin tests | Same |
| 013 | Generate License | Implemented | Detail | Same | Same |
| 014 | Assign License to Facility | Implemented | Backend only | Same | Same |
| 015 | Activate License | Implemented | License detail | Same | Same |
| 016 | Renew License | Implemented | License detail | Same | Same |
| 017 | Modify Licensed Capabilities | Implemented | Backend PATCH | Same | Same |
| 018 | Suspend License | Implemented | License detail | Same | Same |
| 019 | Expire License | Implemented | License detail | Same | Same |
| 020 | Cancel License | Implemented | License detail | Same | Same |
| 021 | Validate License During Login | Implemented | System (no admin UI) | Same | Same |
| 022 | View License Details | Implemented | License detail GET | Same | Same |
| 023 | View License History | Implemented | License detail | Same | Same |
| 024 | Generate License Reports | Implemented | Admin hub | Flutter admin tests | Same |

**SaaS commerce extras (not numbered 228):** quote, terms accept, payment orders, verify, webhook, offline commitment, invoices — `saas_checkout`, `saas_invoice`, platform masterdata policies.

## Commercial rules — verification

| Rule | Status | Evidence |
|------|--------|----------|
| Billable unit = **Facility** | **PASS** | Per-facility quotes/subscriptions (`facility_id` on `SaasQuote`); facility scope status |
| New facility billable / checkout path | **PASS** | Facility created `PENDING` scope; checkout activates scope (`test_subscription_license`, operational gates) |
| Facility addition **proration** | **PASS (integration-verified)** | `test_facility_addition_proration.py` + opt-in `test_facility_proration_postgres.py` on `digitize` |
| Installment 40% / 60–40 | **PASS** | `test_quote_calculator.py` — 40% balance, due +3 calendar months same day |
| Month-end installment date | **BLOCKED** | `BLOCK_MONTH_END` — no silent shift; product unapproved |
| Configurable annual discount | **PASS** | `SaasDiscountPolicy`; zero explicit policy in tests; non-zero installment rules in calculator |
| Ads excluded from SaaS pricing | **PASS** | `advertising_included: False` in quote inputs |
| Subscription activation gate | **PASS** | `operational_eligibility.py`, `require_active_saas_subscription`, staff gate tests |
| T&C ≠ subscription activation | **PASS** | Separate org-terms flow vs SaaS terms/checkout (onboarding docs + tests) |
| Cheque bounce → grace → auto suspend + PA override | **NOT VERIFIED / partial** | Offline commitment + message "grace ends"; **no automated bounce/grace job** found in code |
| Statutory SaaS tax invoice issue | **BLOCKED** | GAP-API09-002 — assessment 2026-11-03; registry §8; `issue` fail-closed on `ISSUANCE_BLOCKERS` |
| API-08 separation | **PASS** | `billing.*` vs `commercial.saas_*` tables; API-08 remains blocked separately |

## Razorpay / payment boundary

| Area | Status |
|------|--------|
| Mock checkout + verify + webhook | **PASS** — `test_saas_mock_checkout_lifecycle.py`, `test_razorpay_hmac.py` |
| Webhook idempotency / duplicate | **PASS** — unit + `test_saas_webhook_rollback_scope_postgres.py` on **`digitize`** (GAP-TXN-004) |
| Live Razorpay credentials / sandbox QA | **AWAITING AUTHORIZATION** — GAP-API09-003 |
| Client redirect ≠ payment success | **PASS** — checkout controller tests |

## Phase 11 — regression re-verification (2026-11-07)

| Suite | Result |
|-------|--------|
| `pytest tests/subscription/ tests/api/test_subscription_license.py -q` (PG hooks off) | **139 passed**, 68 skipped |
| `DIGITIZE_PRORATION_PG_TEST=1` … `test_facility_proration_postgres.py` | **5 passed** |
| `DIGITIZE_TXN004_PG_TEST=1` … `test_saas_webhook_rollback_scope_postgres.py` | **3 passed** |
| `DIGITIZE_FLUTTER_SURFACES_PG_TEST=1` … `test_flutter_surfaces_digitize_postgres.py` (incl. GAP-API09-001 paths) | **8 passed** |
| Flutter `saas_checkout` + `saas_invoice` + `saas_subscription_admin` | **38 passed** (checkout fake aligned to `effectiveDateIso` preview API) |

**Unchanged blockers:** GAP-API09-002 statutory issue; GAP-API09-003 live Razorpay; GAP-API09-005 cheque automation; EQ-011 `digitize_test`.

## Regression commands (2026-11-03)

```bash
cd digitize-services
python3 -m pytest tests/subscription/ tests/api/test_subscription_license.py -q \
  --ignore=tests/subscription/test_saas_webhook_concurrency_postgres.py \
  --ignore=tests/subscription/test_saas_webhook_rollback_scope_postgres.py
# 123 passed, 63 skipped (DIGITIZE_API_TEST off)

# Optional local digitize webhook rollback IV (GAP-TXN-004):
# txn004 guard + tests/subscription/test_saas_webhook_rollback_scope_postgres.py

# PostgreSQL integration (local digitize — required for integration-verified claim):
DIGITIZE_PRORATION_PG_TEST=1 ENVIRONMENT=development DB_NAME=digitize DB_HOST=localhost \
  pytest tests/subscription/test_facility_proration_postgres.py -q
# 5 passed

# EQ-011 numbered API-09 HTTP (digitize_test only — NOT modified in this pass):
# DIGITIZE_API_TEST=1 DB_NAME=digitize_test pytest tests/api/test_subscription_license.py

cd digitize-ui
flutter test test/features/saas_checkout/ test/features/saas_invoice/ \
  test/features/saas_subscription_admin/ -r compact
# 33 passed
```

## Acceptance checklist

| Criterion | Status |
|-----------|--------|
| 24/24 backend registry status | **PASS** |
| Flutter checkout + invoice + admin slice | **PASS** |
| Mock payment lifecycle | **PASS** |
| Live provider verification | **BLOCKED** |
| EQ-011 full numbered API IV | **BLOCKED** (digitize_test policy) |
| Cheque bounce automation | **BLOCKED** (product/implementation gap) |
| Facility proration on add | **PASS** (INV-005) |
| Module COMPLETE (assignment criteria) | **PARTIALLY COMPLETE — BLOCKED** |

## GAP-API09-006 — facility addition proration (2026-11-03)

**Status:** **Integration-verified** on local PostgreSQL `digitize` (2026-11-03).

**Formula:** `prorated_list = annual_list × remaining_billable_days / total_period_days` (calendar days; period start inclusive, end exclusive; effective date = facility `created_at` UTC date).

**Evidence:**
- Unit: `tests/subscription/test_facility_addition_proration.py`
- PostgreSQL (opt-in): `tests/subscription/test_facility_proration_postgres.py` — **5 passed** with `DIGITIZE_PRORATION_PG_TEST=1 ENVIRONMENT=development DB_NAME=digitize DB_HOST=localhost`
- Regression: `pytest tests/subscription/` → **144 passed**, **5 skipped** (PG module skipped without env)

**Remaining:** Statutory invoice blockers (GAP-API09-002), live Razorpay (GAP-API09-003), cheque bounce automation (GAP-API09-005), EQ-011 HTTP IV on `digitize_test`.

## GAP-API09-002 — statutory SaaS tax invoice readiness (2026-11-03)

**Status:** **Blocked (product + legal)** — readiness assessment **§8** + decision-resolution package **§9** (2026-11-03); **no option selected**; implementation **not authorized**.

**What exists (verified):**

| Capability | Status |
|------------|--------|
| Quote/terms/obligations + mock payment + activation | **PASS** (separate from tax invoice) |
| Invoice preview + preview PDF | **PASS** — explicitly **not** a tax invoice |
| Invoice issue API + DB schema (034) + immutability + numbering lock | **Implemented** — **`POST /saas/invoices` fails closed** while `ISSUANCE_BLOCKERS` present |
| Full statutory issue on real DB | **NOT VERIFIED** — blockers prevent reaching numbering in compliance tests |
| API-08 operational invoices | **Separate** — not reused for SaaS |

**Issuance blockers (today):** `PLACE_OF_SUPPLY_RULE_UNAPPROVED`, `INSTALLMENT_INVOICE_DOCUMENT_POLICY_UNAPPROVED` (installment terms), `CUSTOMER_GSTIN_PLAINTEXT_UNAVAILABLE` (when no decryptable ciphertext), plus configuration gaps (supplier, address, GST split) per registry §7.

**Authoritative detail:** [SAAS_INVOICE_READINESS_DECISION_REGISTRY.md](../architecture/SAAS_INVOICE_READINESS_DECISION_REGISTRY.md) **§8** (assessment), **§9** (decision-resolution package for INV-001, INV-003, INV-002).

**Smallest decisions to authorize implementation:** Written sign-off per registry **§9.1.7**, **§9.2.2**, **§9.3.3** plus legal answers **§9.1.8**, **§9.2.3**, **§9.3.4** (not engineering recommendations).

**Unchanged blockers:** GAP-API09-003, GAP-API09-005, EQ-011, GAP-API09-006 proration remains **integration-verified**.

## API-08 boundary (unchanged)

API-08 operational billing: **PARTIALLY COMPLETE — BLOCKED** (eight skeleton ops). Do not conflate with API-08-009 online facility payment.
