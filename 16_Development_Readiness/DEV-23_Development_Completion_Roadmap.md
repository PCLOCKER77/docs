# DEV-23 Development Completion Roadmap

**Document ID:** DEV-23  
**Assessment date:** 2026-11-03  
**Parent:** [DEV-20](./DEV-20_Comprehensive_Development_Gap_Assessment.md)  
**Gap IDs:** [DEV-21](./DEV-21_Development_Gap_Register.md)  
**Journeys:** [DEV-22](./DEV-22_End_to_End_Journey_Matrix.md)  

This is a **dependency-aware execution sequence**, not an authorization to change contracts, invent APIs, or apply gated migrations. Product decisions and migration authorizations remain separate gates.

**Inventory authority (2026-11-04):** Canonical **`app/api/contracts/api_registry.py`** (single approved inventory). Reconciliation: `scripts/api_inventory_reconciliation.py` and [evidence](../16_Development_Readiness/evidence/API_INVENTORY_RECONCILIATION_2026-11-04.md).

**2026-11-04 engineering pass:** P1 users scaffold removed; P2 catalog metadata aligned; P3 DR-023 read-only IV; P4 Flutter remote wiring verified; P5 PG IV re-run on local `digitize`. See DEV-19 session log **five engineering priorities**.

**Do not implement from this document until the product owner approves a phase.**

**Master reconciliation (2026-11-09):** **228/228** `BACKEND_IMPLEMENTED`. Final QA cutover: [CONSOLIDATED_FINAL_QA_CUTOVER_REPORT.md](./evidence/CONSOLIDATED_FINAL_QA_CUTOVER_REPORT.md) — **NOT COMPLETE** (deploy + TEST-13 + smoke pending). Evidence: `FINAL_SECURITY_*`, `FINAL_WHATSAPP_*`, `FINAL_QA_DEPLOYMENT_*`, [BASIC_QA_TESTING_HANDOVER.md](./evidence/BASIC_QA_TESTING_HANDOVER.md) (draft). Local dev DB head **088**; `digitize_test` **083** until TEST-13.

---

## Guiding principles

1. Preserve the frozen **228** numbered inventory.  
2. Prefer extras / decision packs over silent renumbering.  
3. Close journey blockers before polish.  
4. Do not treat Deferred items as sprint defects.  
5. Integration-verification is a phase, not a substitute for implementation.  
6. Preserve existing WIP; land commits in small reviewable PRs after approval.

---

## Phase 0 — Decision and authorization gates (parallel, non-coding or docs-only)

**Objective:** Unblock skeletons and list APIs that development cannot invent.

| Decision | Gap IDs | Outcome needed |
| --- | --- | --- |
| Membership list-by-customer (extra vs defer forever) | GAP-API05-001 | **Closed 2026-11-09** — additive GET + PG IV |
| Facility online pay / tax / credit notes scope | GAP-API08-* | Approve subset for next release |
| Support escalate semantics + migration auth | GAP-API12-001 | **Closed 2026-11-09** — history-only Phase 1 implemented (mig 083) |
| API-14 GMD seed set | GAP-API14-001…004 | Approve seeds / ownership |
| API-13 capture-POST non-client confirmation | GAP-API13-001 | Written confirmation |
| T&C reacceptance policy | GAP-API02-002 | Keep deferred or define |
| Facility/site conflict + enrollments list | GAP-API07-001/002 | **Closed 2026-11-09** — implemented + PG (concurrency DB still DBA) |
| SaaS INV statutory blockers | GAP-API09-002 | Approve INV pack or defer invoice issue |
| EQ-011 digitize_test upgrade | GAP-QA-001 | Authorize TEST-13 |
| OTP in launch scope? | GAP-INT-001 | Require SMS vendor or de-scope |

**Completion criteria:** Signed decisions recorded in decision docs / DEV-19; no silent inventory growth.

---

## Phase 1 — Journey discoverability and IAM Flutter (P1, no new numbered APIs)

**Objective:** Make already-live backends usable by real roles.

| Work | Gap IDs | APIs / Flutter | Status (2026-11-03) |
| --- | --- | --- | --- |
| Add Attendance to AppShell + role permissions | GAP-UI-001, GAP-JRN-006 | API-06 desk | **Implemented** — `/attendance` entry + shell nav; desk/reports reused |
| Staff role-assignment, scopes, activate, credential-reset UI | GAP-API03-001, GAP-API03-002 | API-03 | **Implemented** — staff details IAM panel + lifecycle actions |
| Site Admin nav/policy clarity (if product confirms distinct SA) | GAP-ROLE-001 | Shell / permissions | **Implemented** — Site Admin hides OA billing/profile; account label; permission-scoped ops |
| Membership renew/upgrade/downgrade UI (backend already live) | GAP-API05-002 | API-05 | **Implemented** 2026-11-03 — customer membership section + ACTIVE invoice commercial path |

**Dependencies:** Phase 0 only if SA role model changes permissions seeds.  
**Order:** ~~Attendance nav → IAM Flutter → membership renew/upgrade~~.  
**Completion criteria:** Widget/controller tests; permission-denied paths verified; no mock-only in release mode.  
**Phase 1 status:** **Complete** for scoped P1 items (attendance nav, IAM Flutter, Site Admin nav, membership renew/upgrade/downgrade). Transfer/expire remain P2 (GAP-API05-003).

---

## Phase 2 — Provider integrations (P0/P1)

**Objective:** Replace memory/mock providers required for launch journeys.

| Work | Gap IDs | Modules |
| --- | --- | --- |
| SMS vendor implementation + config | GAP-INT-001, GAP-API04-001, GAP-API10-001, GAP-API06-004 | communication/sms |
| SMTP/SES production path QA | GAP-INT-002, GAP-API11-001 | email + report notifier |
| FCM credentials QA | GAP-INT-002 | push |
| Razorpay live/webhook QA (SaaS + walk-in) | GAP-API09-003, GAP-INT-004 | subscription commerce / attendance |
| Storage enablement for attachments/media | GAP-INT-003 | storage provider |

**Dependencies:** Secrets management; Phase 0 OTP scope.  
**Order:** SMS (if in scope) → email schedule delivery → payment live QA.  
**Completion criteria:** Sandbox evidence without claiming Integration-verified until EQ-011/shared env.

---

## Phase 3 — Product-approved schema / skeleton completions

**Objective:** Implement only **authorized** remaining skeletons.

| Track | Gap IDs | Collections |
| --- | --- | --- |
| ~~API-12-008 escalate~~ | GAP-API12-001 | **Complete** (2026-11-09) |
| Approved API-08 subset (e.g. online and/or credit notes) | GAP-API08-005/006/… | Billing |
| Approved API-14 seeds | GAP-API14-* | Reference |
| Approved API-13 schema items (if any) | GAP-API13-002…005 | Audit |

**Dependencies:** Phase 0 authorizations. Never apply unauthorized DDL.  
**Order:** Escalate (smallest) → API-14 seeds → API-08 online/credit → API-13 if approved.  
**Completion criteria:** Catalog backend_status updates; Flutter for newly live ops; contract tests.

---

## Phase 4 — Membership discovery and training completeness

**Objective:** Close high-friction deferred extras once approved.

| Work | Gap IDs |
| --- | --- |
| Membership list-by-customer extra + Flutter | GAP-API05-001 |
| List enrollments extra + UI reload | GAP-API07-001 |
| Facility/site conflict enforcement (if approved) | GAP-API07-002 |
| Walk-in identify + session/audit Flutter polish | GAP-API06-001/002 | **Done (Flutter)**; GAP-API06-003 **Integration-verified** (PG desk IV 2026-11-03) |

**Dependencies:** Phase 0 extras approval.  
**Completion criteria:** Desk can find memberships/enrollments without memorized IDs.

---

## Phase 5 — Notifications admin, PA console, renewals polish

**Objective:** Staff-facing completeness for already-live backends.

| Work | Gap IDs |
| --- | --- |
| Campaign / notification admin Flutter | GAP-API10-003, GAP-API10-005 | **Done** — campaigns + staff ops + inbox/staff surface separation (see DEV-19 session logs) |
| PA Flutter for remaining API-01 ops | GAP-API01-001 | **Implemented** 2026-11-03 — `/platform/console` (settings, health, flags, maintenance, release publish, security policy, reports) |
| Membership transfer/expire UI | GAP-API05-003 | **Implemented** 2026-11-03 — customer membership section (known ID) |
| Numbered API-09 admin UI (optional if extras suffice) | GAP-API09-001 | **Done** — `/organization/subscription-admin` + existing `/organization/billing` checkout/invoices |
| PA audit visibility decision | GAP-ROLE-003 | **Done** 2026-11-03 — PA audit nav when `report.view`; scoped reads via company profile link |
| PDF export limitation (API-11 UI clarity) | GAP-API11-002 | **Done** 2026-11-03 — catalogue-driven HTML/Excel/CSV; PDF documented unavailable |
| API-11 live certification evidence | GAP-API11-003 | **Integration-verified 2026-11-03** — HTML export bytes on local `digitize` with opt-in entitlement fixture |

**Dependencies:** Phases 1–2 preferred.  
**Completion criteria:** Role-permissioned screens; empty/error/busy states.

---

## Phase 6 — SaaS statutory invoice track (conditional)

**Objective:** Only if product requires tax invoice issue.

| Work | Gap IDs |
| --- | --- |
| Execute INV-* decisions from SaaS invoice registry | GAP-API09-002 |

**Dependencies:** Phase 0 INV decisions; may be parallel to Phase 3.  
**Completion criteria:** Issue path against approved tax rules; still separate from API-08 facility billing.

---

## Phase 7 — Integration verification and release certification

**Objective:** Promote Implemented/Tested → Integration-verified where authorized.

| Work | Gap IDs |
| --- | --- |
| EQ-011 on digitize_test per TEST-13 | GAP-QA-001 |
| Shared QA: J1–J9 happy paths | Multiple |
| Provider sandbox evidence pack | GAP-INT-* |
| Refresh stale catalog frontend_status | **Closed 2026-11-07** — re-verified **2026-11-09** (GAP-API01-003, API08-010, API09-004, API11-004) |
| WIP commit/PR hygiene across services/ui/docs | Release risk |

**Dependencies:** Prior phases as needed for launch scope.  
**Completion criteria:** DEV-19 updated with Integration-verified labels only with evidence; EQ-011 not claimed without live pass.

---

## Recommended near-term sequence (first 6 execution slices)

1. **Product workshop** — Phase 0 decisions (list APIs, API-08 subset, escalate, OTP, EQ-011).  
2. ~~**Attendance shell nav** — GAP-UI-001.~~ **Done 2026-11-03.**  
3. ~~**Staff IAM Flutter** — GAP-API03-001/002.~~ **Done 2026-11-03** (incl. activity + Site Admin nav).  
4. ~~**Membership renew/upgrade/downgrade UI** — GAP-API05-002.~~ **Done 2026-11-03.**  
5. **SMS provider or OTP de-scope** — GAP-INT-001 (Phase 2).  
6. **Authorize + implement API-12-008** — GAP-API12-001; EQ-011 authorization parallel.

---

## Mapping phases → API collections

| Phase | Primary collections / modules |
| --- | --- |
| 0 | Decision docs (08/12/13/14/T&C/DR-020/INV/TEST-13) |
| 1 | API-03, API-05, API-06 Flutter; shell |
| 2 | API-04/06/10/11 providers; SaaS Razorpay |
| 3 | API-08/12/13/14 skeletons |
| 4 | API-05/06/07 extras |
| 5 | API-01/09/10 Flutter |
| 6 | SaaS INV extras |
| 7 | All — verification |

---

## Out of scope for this roadmap

- Expanding or renumbering the 228 inventory without a new product freeze.  
- Mandatory T&C reacceptance unless Phase 0 reverses deferral.  
- Infrastructure/Terraform/AWS execution.  
- Merging onboarding T&C with SaaS commercial terms.  
- Claiming Integration-verified without authorized live evidence.
