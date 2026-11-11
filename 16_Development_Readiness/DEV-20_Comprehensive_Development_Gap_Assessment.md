# DEV-20 Comprehensive Development Gap Assessment

**Document ID:** DEV-20  
**Folder:** `16_Development_Readiness`  
**Status:** Assessment only (not a product approval; not an implementation plan authorization)  
**Assessment date:** 2026-11-03  
**Primary status authority:** [DEV-19_Feature_Completion_Tracker.md](./DEV-19_Feature_Completion_Tracker.md)  
**Companion deliverables:** [DEV-21](./DEV-21_Development_Gap_Register.md), [DEV-22](./DEV-22_End_to_End_Journey_Matrix.md), [DEV-23](./DEV-23_Development_Completion_Roadmap.md)  
**Numbered inventory:** **228** (frozen). Machine source: `digitize-services/app/api/contracts/catalog.py`.

---

## 1. Executive summary

Digitize is a **largely backend-complete SaaS core** with **204 / 228** numbered operations live (`BACKEND_IMPLEMENTED`) and **24** remaining skeletons gated by product decisions or migration authorization. Flutter covers most desk and admin happy paths for organization setup, customers, membership create/activate/freeze, attendance, training/PTR, SaaS checkout, reports, support, and audit reads.

The product is **not yet functionally complete as an operable end-to-end SaaS** because:

1. **24 numbered skeletons** remain (facility billing depth, support escalate, audit capture/compliance, reference geo/i18n).
2. Several **critical UX discovery / IAM / membership-list** gaps leave otherwise-live APIs unreachable or incomplete for real users.
3. **External providers** (SMS especially; report schedule email; facility online payments) are incomplete or mock-only.
4. Almost nothing is **Integration-verified** against an authorized shared environment (EQ-011 still Awaiting authorization).
5. Catalog `frontend_status` metadata is often **stale** versus actual Flutter remotes — do not use catalog FE fields as truth.

**Verdict:** Safe to plan remaining development systematically. Highest leverage is closing P0/P1 journey gaps and product-gated skeletons that unblock commercial and operational completeness — not expanding the 228 inventory.

---

## 2. Repository and branch information

| Repository | Path | Branch | HEAD (at assessment) |
| --- | --- | --- | --- |
| digitize-services | `/Users/premjyo/dev/Digitize-by-OrieOn/digitize-services` | `release/qa-smoke-20261016` | `07cd920` |
| digitize-ui | `/Users/premjyo/dev/Digitize-by-OrieOn/digitize-ui` | `release/20261019` | `879364f` |
| docs | `/Users/premjyo/dev/Digitize-by-OrieOn/docs` | `main` | `2f506be` |

Local Alembic head on inspected `digitize` DB: **`072_platform_terms_document`**. EQ-011 target `digitize_test` remains at **036** per DEV-19 / TEST-13 (not re-migrated in this assessment).

---

## 3. Worktree / WIP preservation

Assessment was **read-only** for product code and databases (documentation deliverables only under `docs/`).

| Repo | Approx. porcelain entries | Notes |
| --- | ---: | --- |
| digitize-services | ~494 | Large uncommitted surface: org/T&C, billing, membership, training, attendance, subscription, migrations including 072, PTR/API-07-related, etc. |
| digitize-ui | ~226 | Facility, training, membership lifecycle, T&C CMS, billing panels, attendance, auth, shell nav, etc. |
| docs | ~56 | DEV-19, architecture registers, API completion reports, T&C gap register, etc. |

**Do not treat uncommitted WIP as missing.** T&C management (ORG-TERMS-002…006), membership freeze/resume/cancel UI, API-07 conflict UX, API-08 offline/refund/cancel flows, and related work are present in the working trees and/or committed history as documented in DEV-19.

No branch switches, resets, cleans, stashes, commits, or pushes were performed for this assessment.

---

## 4. Assessment methodology

Four levels were applied:

| Level | Focus |
| --- | --- |
| A | Backend routes, services, models, migrations, authz, audit, lifecycle |
| B | Flutter screens, routing, Riverpod, remotes vs mocks, UX states |
| C | End-to-end user journeys (screen → repository → API → persistence → UI refresh) |
| D | Fit to frozen business rules / decision records; unclear items marked for product decision |

**Evidence sources:** `catalog.py` machine counts, DEV-19, API contract registry, architecture decision packs, module routes/services, Flutter remotes and `app_shell.dart`. Prefer code + DEV-19 over stale catalog `frontend_status`.

**Not performed:** broad QA, EQ-011 live run, real payments/emails/SMS, infrastructure/Terraform, penetration testing, schema changes.

---

## 5. Overall development status

| Metric | Value |
| --- | ---: |
| Numbered product APIs | **228** |
| `BACKEND_IMPLEMENTED` | **204** |
| `SKELETON_CREATED` | **24** |
| Catalog extras (`EXTRA_OPERATIONS`) | **158** (156 approved product + 2 OPS health; all registered) |
| ORG-TERMS-001…006 (subset of extras) | **6** implemented / tested (outside 228) |
| Collections fully backend-live (0 skeletons) | API-01…07, 09, 10, 11 |
| Collections with skeletons | API-08 (8), API-12 (1), API-13 (9), API-14 (6) |
| Integration-verified (DEV-19 sense) | **None claimed** for full product |

**Functional completeness estimate (product owner framing):**

- **Platform foundation + org/facility/site + CRM + training desk:** largely Implemented/Tested in code; Incomplete on IAM Flutter depth and shared-env verification.
- **Commercial facility billing depth + statutory SaaS invoice blockers + SMS OTP:** incomplete / deferred / provider-blocked.
- **Governance audit depth + geo reference:** deferred by product decision.

---

## 6. API-01 through API-14 module assessment

Statuses use DEV-19 vocabulary. Detailed gaps: DEV-21.

### API-01 Platform Admin (11/11 backend)

| Dimension | Finding |
| --- | --- |
| Backend | All live (settings, GMD, flags, maintenance, releases, health, security, report executions) |
| Flutter | GMD + extensive **extras** masterdata/T&C; numbered settings/flags/maintenance/releases/health/security/executions largely **without** Flutter screens |
| E2E | Partial PA console |
| Primary gaps | GAP-API01-001…003 |

### API-02 Organization / Facility / Site (20/20)

| Dimension | Finding |
| --- | --- |
| Backend | Live CRUD/lifecycle; DR-021 onboarding + ORG-TERMS extras DB-backed |
| Flutter | Strong org/facility/branch; PA T&C CMS; OA acceptance UI |
| E2E | Connected for core onboarding when lifecycle prerequisites met |
| Primary gaps | Reacceptance deferred; shared-env T&C E2E; DR-023 hierarchy cutover residual risk |

### API-03 Identity (12/12)

| Dimension | Finding |
| --- | --- |
| Backend | Live staff/account/role/scope/credential ops |
| Flutter | Create/list/edit/suspend/deactivate; **missing** role-assignment, scopes, activate, credential-reset, activity UIs |
| E2E | Partial IAM |
| Primary gaps | GAP-API03-001…004 (P1/P2) |

### API-04 Customer (12/12)

| Dimension | Finding |
| --- | --- |
| Backend | Live CRM |
| Flutter | Strong remote coverage + OTP extras |
| E2E | Connected code-path; SMS QA blocked |
| Primary gaps | GAP-API04-001 (provider), GAP-INT-001 |

### API-05 Membership (12/12)

| Dimension | Finding |
| --- | --- |
| Backend | Live lifecycle including freeze/resume/cancel |
| Flutter | Create/activate/freeze/resume/cancel + offline pay; **no** renew/upgrade/downgrade/transfer/expire UI |
| Product | List-by-customer **Deferred** (DR-020 P1-009) |
| Primary gaps | GAP-API05-001…005 |

### API-06 Attendance (15/15)

| Dimension | Finding |
| --- | --- |
| Backend | Live desk + walk-in + reports |
| Flutter | Desk + walk-in + reports; weak identify/session/audit wiring |
| UX | **No AppShell nav** — discoverability gap |
| Primary gaps | GAP-UI-001 / GAP-JRN-006, GAP-API06-* |

### API-07 Trainer / Activity / Batch (32/32)

| Dimension | Finding |
| --- | --- |
| Backend | Live ops + schedule conflict / availability rules |
| Flutter | Broad training_operations + PTR conflict UX **Implemented/Tested** |
| Deferred | List enrollments API; facility/site conflict enforcement |
| Primary gaps | GAP-API07-001…004 |

### API-08 Billing / Payment (10/18)

| Dimension | Finding |
| --- | --- |
| Backend | Phase-1 offline/history/refund/cancel **Implemented/Tested**; API-08-016 Phase 2 `financial_events`; outstanding uses effective balance (018); Alembic **074–082** in repo (head **082**) — apply/promotion gated by product register |
| Flutter | Outstanding + history panels **Implemented/Tested** (32 controller tests) |
| External | Facility online pay skeleton (009); Razorpay SaaS ≠ facility 009 |
| Primary gaps | GAP-API08-001…010 (skeletons/deferred); GAP-API08-009 **Integration-verified** on local `digitize` (2026-11-07 stabilization) |

### API-09 Subscription / License (24/24)

| Dimension | Finding |
| --- | --- |
| Backend | Full numbered lifecycle live |
| Flutter | Uses **SaaS extras** (checkout/invoices/plans), not numbered `/subscriptions` admin UI |
| Product | Statutory SaaS invoice issue blockers in INV registry (orthogonal to 24/24) |
| Primary gaps | GAP-API09-001…004 |

### API-10 Notifications / Campaigns (24/24)

| Dimension | Finding |
| --- | --- |
| Backend | Live communication + campaign modules |
| Flutter | In-app inbox + push scaffold; **no** campaign admin UI |
| Providers | Email SMTP/memory; SMS **memory/none only**; WhatsApp cloud_api optional; FCM optional |
| Primary gaps | GAP-API10-001…005, GAP-INT-* |

### API-11 Reports (12/12)

| Dimension | Finding |
| --- | --- |
| Backend | Live domain reports + schedules |
| Flutter | Company + governance reporting wired |
| Blocker | Schedule delivery notifier held (no real email attachment path) |
| Primary gaps | GAP-API11-001…004 |

### API-12 Support (11/12)

| Dimension | Finding |
| --- | --- |
| Backend | Ticket lifecycle live; **008 escalate** skeleton |
| Flutter | Tickets/help/chat/agent; no escalate |
| Gate | API-12-008 migration proposal Awaiting authorization |
| Primary gaps | GAP-API12-001…003 |

### API-13 Audit (3/12)

| Dimension | Finding |
| --- | --- |
| Backend | List/export/analytics live; capture/compliance skeletons |
| Flutter | Audit events page for 005/009/012 |
| Product | Capture POSTs deferred (must remain non-client) |
| Primary gaps | GAP-API13-001…007 |

### API-14 Reference (6/12)

| Dimension | Finding |
| --- | --- |
| Backend | Currencies/status/payment-methods/channels/lookup/facility-types alias live |
| Flutter | Prefers GMD + facility-types extras over `/reference/*` |
| Deferred | Countries/states/languages/timezones/activity-types/localization |
| Primary gaps | GAP-API14-001…006 |

### Additional management operations (outside 228)

| IDs | Status |
| --- | --- |
| ORG-TERMS-001…006 + ORG-ONBOARDING-ACCEPT-001 | Backend **Implemented**; PA CMS + OA accept Flutter **Implemented**; local mig 072 applied on `digitize`; reacceptance **Deferred**; not Integration-verified |
| Auth contracts | Separately documented; not part of 228 |
| Catalog extras (facility-types, SaaS commerce, media, OTP, etc.) | Substantial; keep outside numbered inventory |

---

## 7. Authentication and authorization assessment

| Area | Assessment |
| --- | --- |
| Login / RS256 access JWT / hashed rotating refresh cookie | Implemented in `authentication` module |
| Logout / session revocation / rate limits | Present in service paths |
| Password reset / credential setup | Present; env-policy for OA provisioning (DR-021) |
| Database-backed principal | `load_authorized_principal` resolves assignments/permissions from DB — JWT claims are not the sole authority |
| Permission enforcement | Route-level `require_permission`; Flutter visibility is not sufficient |
| Platform Admin governance | Operational modules hidden in shell; catalog notes and services emphasize no tenant impersonation / no unrestricted DEK access — **treat as Implemented intent**; continuous security review still recommended, not performed here |
| Last Platform Admin protection | Identity service contains system-role / platform-scope guards; **full last-admin edge-case matrix not exhaustively proven in this assessment** |
| Flutter auth state / guards | Auth controller + permission providers; mock auth when not `DIGITIZE_REMOTE`/release |

**Gaps:** GAP-AUTH-* in DEV-21 (verification depth, idle-timeout product clarity, Site Admin vs OA shell indistinction).

---

## 8. Business journey assessment

See **DEV-22** for the matrix. Summary:

| Journey | Status |
| --- | --- |
| J1 PA onboarding + T&C | Connected (code); not Integration-verified |
| J2 OA setup | Connected (lifecycle-gated) |
| J3 Membership plans | Connected |
| J4 Customers | Partial (SMS OTP) |
| J5 Membership lifecycle | Partial (list deferred; renew/upgrade UI missing) |
| J6 Attendance | Partial (desk exists; shell nav missing) |
| J7 Training/PTR | Connected / Partial (list enrollments & facility conflicts deferred) |
| J8 Facility billing | Partial (offline yes; online/tax/credit deferred) |
| J9 SaaS subscription | Connected via extras |
| J10 Notifications | Partial (inbox yes; campaigns/SMS no) |
| J11 Reports | Partial (on-screen yes; schedule delivery held) |
| J12 Support/audit | Partial (escalate + audit depth) |

---

## 9. Role-capability matrix

| Capability class | Platform Admin | Organization Admin | Site Admin |
| --- | --- | --- | --- |
| Platform masterdata / SaaS catalogs / T&C CMS | Yes (permissioned) | No | No |
| Companies list / activate | Yes | Own org only | Own scope only |
| Facilities / sites / staff / customers / plans / training | Shell **hidden** for PA | Yes when ACTIVE + subscription lifecycle allows | Same shell pattern — **no distinct SA nav**; depends on granted permissions |
| Attendance desk | No shell path | Facility details CTA only | Same |
| Company billing / SaaS invoices | PA SaaS invoices catalog | Org billing + checkout | If permitted |
| Audit events UI | **No PA nav** | Yes if `report.view` / audit permission | If permitted |
| Support | PA may use support surfaces depending on permissions; operational support nav is OA-gated in shell | Yes | If permitted |

**Key finding:** Site Admin is not a first-class Flutter navigation role (GAP-ROLE-001).

---

## 10. Flutter architecture assessment

| Topic | Finding |
| --- | --- |
| Shell / responsive | AppShell with rail + drawer; permission-driven destinations |
| State | Riverpod controllers/providers; repository abstractions generally respected |
| Mock vs remote | Mixed: some domains always remote even in development mock mode (GAP-UI-002) |
| Placeholders | Mostly design-system barrel comments; facility capacity “legacy placeholder” label; chart placeholders in analytics cards |
| Dead / incomplete | Numbered PA console ops; campaign admin; renew/upgrade membership; escalate |
| Catalog FE metadata | Stale `NOT_STARTED` for many collections despite remotes — documentation debt |

---

## 11. Database and migration assessment

| Topic | Finding |
| --- | --- |
| Alembic | Additive SQL twins; head **072** on local `digitize` |
| Skeletons needing schema | API-08 credit notes/receipts/online txn; API-12 escalate; API-13 policies/violations/investigations; API-14 GMD seeds |
| EQ-011 | `digitize_test` lagging at 036; upgrade authorization required (TEST-13) |
| Data integrity themes | Unique published T&C; membership/billing offline paths; training conflict rules at trainer level |
| Assessment limit | No schema-changing inspection queries beyond confirming local alembic current for T&C workstream context |

---

## 12. External integration assessment

| Integration | Abstraction | Production readiness |
| --- | --- | --- |
| Email | Provider interface | SMTP when configured; else memory/unconfigured |
| SMS | Provider interface | **No live vendor** — memory/none only |
| WhatsApp | Channel delivery | Optional `cloud_api` |
| Push | FCM v1 or memory | Needs credentials |
| Payments | Razorpay gateway | Mock vs live env; facility online numbered op skeleton |
| Object storage | Local / S3 / disabled | Defaults often disabled |
| Monitoring/logging | App logging setup | Ops depth not certified here |

---

## 13. Critical functional gaps (P0 / selected P1)

See DEV-21 for full IDs. Highlights:

1. SMS provider absence blocking OTP QA (GAP-INT-001) — **P0** if OTP is launch-required.
2. Membership list-by-customer deferred (GAP-API05-001) — **P0 product** if CRM desk must manage memberships without IDs.
3. Facility online payment if required for launch (GAP-API08-006) — **P0 product**.
4. Attendance undiscoverable in shell (GAP-UI-001) — **P1**.
5. Staff IAM Flutter incomplete (GAP-API03-001/002) — **P1**.
6. Support escalate awaiting auth (GAP-API12-001) — **P1**.
7. Report schedule delivery held (GAP-API11-001) — **P1**.
8. EQ-011 / shared-env verification (GAP-QA-001) — **P1** for certification.
9. SaaS INV statutory blockers if tax invoice issue is required (GAP-API09-002) — **P0–P1 product**.
10. Campaign admin Flutter missing (GAP-API10-003) — **P1** if campaigns are launch-scope.

---

## 14. Deferred product decisions

| Item | Canonical doc |
| --- | --- |
| Existing-org T&C reacceptance | ORG_TERMS_MANAGEMENT_GAP_REGISTER |
| Membership list-by-customer | DR-020 P1-009 / DEV-19 |
| Facility/site schedule conflicts; list enrollments | DEV-19 / API-07 notes |
| API-08 eight skeletons | API-08_FACILITY_BILLING_DECISION_REGISTER |
| API-13 capture POSTs / compliance depth | API-13_AUDIT_PRODUCT_DECISION |
| API-14 geo/i18n/activity/localization | API-14_REFERENCE_SOURCE_OF_TRUTH |
| SaaS INV-* tax invoice blockers | SAAS_INVOICE_READINESS_DECISION_REGISTRY |
| Freeze date-range / billing coupling Phase 1 | DEV-19 API-05 |

---

## 15. Awaiting-authorization items

| Item | Doc |
| --- | --- |
| EQ-011 live on `digitize_test` (036→head) | TEST-13 |
| API-12-008 escalate migration | API-12_008_Escalate_Migration_Proposal |
| API-08 schema migrations for online/receipts/credit notes (if approved) | API-08 register |
| Shared-env apply of mig 072 (if not already) | ORG terms register / ops |

---

## 16. Integration-verification gaps

No collection is claimed **Integration-verified**. Widget/controller/unit/contract tests exist widely. Live multi-tenant QA, provider QA, and EQ-011 remain open.

---

## 17. Risk register

| Risk | Impact | Mitigation direction |
| --- | --- | --- |
| Stale catalog FE metadata | False “missing Flutter” conclusions | Prefer remotes + DEV-19; refresh metadata as chore |
| Large WIP uncommitted | Merge/conflict and release risk | Commit/PR hygiene after assessment approval |
| SMS/memory OTP | Production registration/check-in failures | Real SMS provider or scope OTP out |
| PA cannot see ops modules | Support load on OA only | Confirm intentional; add PA support paths if needed |
| Facility online pay skeleton | Cannot take card payments at facility | Product decide scope vs SaaS/walk-in Razorpay |
| Audit client POST temptation | Integrity compromise | Keep deferred non-client stance |
| EQ-011 lag | Cannot certify release | Authorize TEST-13 upgrade |

---

## 18. Prioritized development roadmap

Authoritative phased plan: **DEV-23**. Sequence theme:

1. Product decisions that unlock skeletons / list APIs.  
2. P0/P1 journey UX (attendance nav, IAM Flutter, membership discovery).  
3. Provider integrations (SMS, email schedule, Razorpay live QA).  
4. Authorized migrations (escalate, billing schema, EQ-011).  
5. Flutter for campaigns / renew-upgrade / PA console polish.  
6. Integration-verification wave.

---

## 19. Dependencies and recommended execution sequence

See DEV-23. Critical dependency chains:

- Customer OTP → SMS provider → API-04/06 QA  
- Membership desk usability → list-by-customer product decision → Flutter  
- Facility card pay → API-08-009 product + schema + Razorpay  
- Support escalate → migration auth → Flutter  
- Certification → EQ-011 auth → shared-env suites  

---

## 20. Explicit exclusions and limitations

- No implementation, contract changes, renumbering, migrations, infra, deployments, commits, or pushes.  
- No broad QA / EQ-011 execution / real money or messages.  
- Did not exhaustively line-audit every one of 228 handlers or every Flutter widget.  
- Security assessment is code-path review only — not a penetration test.  
- Catalog `frontend_status` treated as unreliable.  
- Assessment recognizes WIP; statuses may include uncommitted local work that is not yet released.

---

## Document control

| Related | Path |
| --- | --- |
| Status tracker | DEV-19 |
| Gap IDs | DEV-21 |
| Journeys | DEV-22 |
| Roadmap | DEV-23 |
| Inventory | `architecture/API_CONTRACT_REGISTRY.md` + `catalog.py` |
