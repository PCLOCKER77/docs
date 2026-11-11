# Master remaining blockers — consolidated approval checkpoint

**Date:** 2026-11-08  
**Continues from:** [MASTER_DEV_EXECUTABLE_CLOSURE_2026-11-08.md](./MASTER_DEV_EXECUTABLE_CLOSURE_2026-11-08.md)  
**Authority:** DEV-19, DEV-21, DEV-22, DEV-23, frozen `api_registry.py`, gap-specific evidence.

**Purpose:** Single approval checkpoint for all blockers after local executable development closed. **No gap is marked authorized from `.env` credentials alone.**

**Seven-area expansion (2026-11-09):** [MASTER_SEVEN_AREAS_CLOSURE_EXECUTION_2026-11-09.md](./MASTER_SEVEN_AREAS_CLOSURE_EXECUTION_2026-11-09.md) — statutory, cheque, providers, membership/training, API-13/14, 16 skeletons, API-08-012 receipts.

---

## A. Implemented and verified (no further engineering without new scope)

| Gap / slice | Evidence |
| --- | --- |
| Local API-12 lifecycle + escalate (history-only Phase 1) + agent workspace | GAP-API12-001, GAP-JRN-012, GAP-API12-002; PG `digitize` (2026-11-09) |
| PA scoped audit reads | GAP-ROLE-003; PG **8 passed** |
| Mock facility online pay (API-08-009) | GAP-JRN-008 mock; PG HTTP IV |
| Report schedule UI + HELD notice | GAP-JRN-011; worker records HELD |
| Governance timeline UX | GAP-API02-005 |
| Auth / DR-021 / tenant ops deny | GAP-AUTH-001/002 |
| Transaction safety IV | GAP-TXN-001…004 where cited in DEV-19 |

---

## B. Consolidated approval matrix

| Gap ID | Current status (DEV-21) | Existing decisions | Missing dependency | Approver | Proposed scope (if approved) | Risks | Test plan (post-approval) | Recommendation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **GAP-API12-001** / **GAP-JRN-012** | **Implemented — INTEGRATION_VERIFIED 2026-11-09** | [API-12_008 proposal](../../07_API_Collections/API-12_008_Escalate_Migration_Proposal.md) — **approved history-only Phase 1**; mig **083**; PG escalate **3** + lifecycle **1**; Flutter **4** panel + **11** pages | — | — | — | — | — | **Closed** for Phase 1; Phase 2 priority/assignee requires new authorization |
| **GAP-INT-004** / **GAP-API08-006** / **GAP-API09-003** / **GAP-JRN-008** (live) | Partial / AWAITING_AUTHORIZATION | Mock checkout + webhook dedupe **Tested**; `RAZORPAY_MOCK` PG IV; `Issuance` fail-closed | **Explicit** sandbox/live Razorpay program: key custody, webhook URL, settlement, facility vs SaaS scope, no prod charges in QA | Product + finance + security | Dual-path config review; sandbox-only HTTP IV; Flutter live checkout only after sign-off | Real money, webhook spoofing, double-settlement | `test_billing_m2_http_*`, SaaS webhook PG, Flutter checkout E2E sandbox | **Reject** using local `.env` `RAZORPAY_*` as authorization; approve sandbox **program** first |
| **GAP-INT-002** / **GAP-API11-001** / **GAP-JRN-011** (send) | Blocked (provider) | `HeldReportNotifier`; schedule worker **TESTED**; SMTP localhost in dev `.env` | Approve **delivery tier**: dev Mailpit only vs SES/SMTP sandbox vs production FROM domain | Platform ops + security | Replace `HeldReportNotifier` with authorized sender **only** after tier approved; optional local Mailpit IV doc | Spam, PII in email, misdirected reports | Worker + schedule PG; opt-in SMTP integration test on loopback if tier=dev | Local SMTP **≠** production auth; group with SMS (GAP-INT-001) only for program planning |
| **GAP-INT-001** / **GAP-API04-001** / **GAP-API06-004** / **GAP-API10-001** | Blocked (provider) | SMS abstract + memory/none; OTP flows exist | SMS vendor in scope? (de-scope vs Twilio/etc.) | Product | Provider adapter + secrets + QA OTP IV **or** explicit de-scope of OTP journeys | OTP abuse, cost | API-04/06 OTP PG on authorized env | Decide in/out of launch scope before implementation |
| **GAP-API09-002** | Blocked (product + legal) | [SAAS_INVOICE registry §8–9](../../architecture/SAAS_INVOICE_READINESS_DECISION_REGISTRY.md); `ISSUANCE_BLOCKERS`; preview/issue fail-closed | **INV-001, INV-002, INV-003** sign-off (+ legal validations §8.6) | Product + legal | Remove blockers incrementally per decision; schema §8.7 **only** after INV-003 path chosen | Statutory non-compliance | Issue PG on `digitize`; Flutter issue UX | **Minimum to start build:** §9.1–9.3 signatures (DEV-19 2026-11-03) |
| **GAP-API09-005** | Blocked (product/implementation) | Offline commitment recorded; grace messaging partial | Job design: bounce detection, grace days, auto-suspend, PA override API, notifications | Product + subscription owner | Implement only after written state machine approved | Wrong suspensions; revenue ops | Subscription PG + unit state machine | **No automation** in codebase today — do not invent grace period |
| **GAP-QA-001** / **GAP-API01-002** | Awaiting authorization | [TEST-13](../../12_Testing/TEST-13_EQ011_digitize_test_Migration_Authorization.md); `eq011_digitize_test_preflight.py` | Written auth to mutate **`digitize_test`**; `alembic upgrade head` (now **`082_billing_manual_reconciliation`**, not 071); dump/restore plan | QA / platform owner | Upgrade test DB; run EQ-011; shared PA certification | Data loss on wrong DB; cost if RDS | `DIGITIZE_API_TEST=1 DB_NAME=digitize_test` suites | **Do not run upgrade** until TEST-13 authorized; preflight head target updated in repo for alignment |
| **GAP-API05-001** | Deferred (product) | DR-020 P1-009 | Approve list-by-customer extra **or** permanent deferral | Product | New extra API + Flutter **only** if approved | Inventory growth in 228 | Contract + PG + desk UI | Keep **deferred** unless desk discovery is P0 |
| **GAP-API07-001** / **GAP-API07-002** | Deferred (product) | DR-020 / training conflict docs | List enrollments extra; facility/site conflict enforcement | Product | Extras + Flutter **only** if approved | Schedule integrity | API-07 PG | Defer unless training desk requires |
| **GAP-API13-002…005** / **GAP-API13-001** | Deferred / Blocked (schema) | Phase-1 reads **verified**; no client capture POST | Schema/product for events store, investigations, policies | Product + security | Per API-13 acceptance; no invented capture routes | Compliance scope creep | API-13 acceptance checklist | **No DDL** without approved pack |
| **GAP-API14-001…004** | Deferred (product) | GMD seed proposals | Approved country/state/language/timezone seed sets | Product | Migration seeds only when approved | Wrong reference data | Migration SQL IV | Deferred |
| **GAP-ROLE-002** | Product confirm | DR-021 PA ops deny implemented | Written confirm PA governance-only is intentional | Product owner | Documentation only — **no code** unless defect | Support confusion | N/A | Confirm and close register row |
| **GAP-API02-004** | Partial (P2–P3) | No defect-led scope | Concrete defect or approved media requirement | Product | — | — | — | **Remain deferred** — no invented polish |
| **GAP-API02-002** | Deferred (product) | ORG-TERMS flow live on `digitize` | Reacceptance policy for existing orgs | Product | Policy doc only until approved | Legal | Org-terms PG | Deferred |

---

## C. Grouped approval bundles (sign once vs separate)

| Bundle | Gap IDs | Single decision? | Notes |
| --- | --- | --- | --- |
| **Support escalate** | GAP-API12-001, GAP-JRN-012 | **Signed 2026-11-09** — history-only Phase 1 implemented | Phase 2 semantics separate |
| **Razorpay program** | GAP-INT-004, GAP-API08-006, GAP-API09-003, JRN-008 live | One **sandbox program** charter | Facility + SaaS may share webhook infra but need scope table |
| **Outbound delivery** | GAP-INT-002, GAP-API11-001, GAP-JRN-011 email; optional GAP-INT-001 SMS | **Separate** email vs SMS decisions | Preserve manual WhatsApp vs managed delivery |
| **Statutory SaaS invoice** | GAP-API09-002, INV-001…003 | **Legal must sign** INV pack; independent from Razorpay | INV-004+ launch items can follow |
| **Cheque automation** | GAP-API09-005 | Independent product state machine | Not bundled with Razorpay |
| **EQ-011 QA** | GAP-QA-001, GAP-API01-002 | Independent **environment** authorization ([TEST-13](../../12_Testing/TEST-13_EQ011_digitize_test_Migration_Authorization.md)) | Never use `digitize` for EQ-011 writes |
| **Training/membership extras** | GAP-API05-001, GAP-API07-001/002 | Per-extra approval | Frozen 228 unless formal extra |
| **Audit/security schema** | GAP-API13-* | Per-slice | Client ingest remains non-client stance (GAP-API13-001) |

---

## D. Provider-independent work already complete (do not redo)

- Mock payment initiate/verify (API-08-009) and SaaS mock commerce paths.
- Webhook idempotency and rollback scope (GAP-TXN-004).
- Report calculation + `run_due_schedules` + HELD delivery records.
- ~~Support ticket lifecycle (incl. escalate Phase 1)~~ — complete on local `digitize`.
- Flutter surfaces for blocked journeys (static notices, fail-closed UI).

---

## E. What still prevents “global product complete”

| Class | Examples |
| --- | --- |
| **Legal/statutory** | SaaS tax invoice issue (INV-001…003) |
| **Real payments** | Live Razorpay sandbox/production program |
| **Real notifications** | SMS + outbound email delivery tiers |
| ~~**Support escalate**~~ | **Closed Phase 1** (2026-11-09); optional Phase 2 not authorized |
| **QA certification** | `digitize_test` migration + EQ-011 |
| **Product deferrals** | Membership list, enrollments list, GMD seeds, API-13/14 schema |
| **Automation not designed** | Cheque bounce / grace / suspend |

**Development completion (local `digitize` + Flutter wiring for authorized APIs)** — **done** per closure report.  
**Product readiness for launch** — **not complete** while rows above remain open.

---

## F. Resume implementation trigger

When a row in §B is **explicitly recorded** (DEV-19 decision log, signed proposal amendment, or user message naming GAP ID + approval):

1. Re-read approved scope only.  
2. Implement + test on authorized env (`digitize` PG IV unless gap is EQ-011/`digitize_test`).  
3. Update DEV-19/21/22 and gap evidence.  
4. Continue to next newly authorized gap **without** a new master prompt.

Until then: **no schema, route, permission, provider, or QA mutations** for blocked rows.
