# DEV-19 Feature Completion Tracker

**Document ID:** DEV-19  
**Folder:** `16_Development_Readiness`  
**Status:** Working tracker (not a product approval)  
**Last updated:** 2026-11-09 (master development closure and dependency handover)  
**Inventory:** canonical `app/api/contracts/api_registry.py`; runtime catalogue in `catalog.py`  
**Machine authority for counts:** `scripts/api_inventory_reconciliation.py`, `scripts/contract_numbered_audit.py`, `catalog.validate_catalog()` — this tracker records evidence, not inventing contracts.

Regenerate machine counts:

```bash
cd digitize-services && poetry run python scripts/api_inventory_reconciliation.py
cd digitize-services && poetry run python scripts/contract_numbered_audit.py
```

## Session log — 2026-11-09 (Master development closure)

| Deliverable | `evidence/MASTER_DEVELOPMENT_CLOSURE_AND_DEPENDENCY_HANDOVER_2026-11-09.md` |
| --- | --- |
| Audit | `contract_numbered_audit.py` → **212** implemented, **16** skeleton (228 numbered) |
| Concurrency DB | Re-checked: `digitize_trainer_concurrency` **missing**; concurrency tests **5 skipped** without opt-in DB |
| Engineering | No further authorized net-new implementation; dependency register consolidated in DEV-21 |
| Truth | Product **not** production-complete; local dev scope **maximized** per frozen decisions |

---

## Session log — 2026-11-09 (Backlog continuation — no further unblocked P0/P1)

| Scan | Result |
| --- | --- |
| DEV-21 P0/P1 | Membership/training list + facility **closed**; remainder **blocked** (statutory INV, providers, EQ-011, API-13/14 schema, skeleton promotions) or **deferred** (product) |
| Engineering delivered | Flutter compile fix `listBatchEnrollments` pagination (`envelope.metadata`); widget test enrollment list on open; DEV-21 **GAP-JRN-007** updated |
| Facility concurrency PG | Still **open** — `digitize_trainer_concurrency` missing; `digitize_app` cannot `CREATE DATABASE` |
| Tests | `batch_enrollment_test.dart` **4 passed** |

---

## Session log — 2026-11-09 (GAP-API05-001 / GAP-API07-001 / GAP-API07-002)

| Gap | Backend | Flutter | Tests | Inventory |
| --- | --- | --- | --- | --- |
| GAP-API05-001 | `GET /api/v1/customers/{customer_id}/memberships` additive | Customer profile list + reload | `test_membership_list_by_customer.py` **2**; `customer_membership_section_test.dart` **7** | **228 unchanged** |
| GAP-API07-001 | `GET /api/v1/batches/{batch_id}/enrollments` additive | `BatchDetailPage` load + refresh | Service + route wired; PG suite not re-run this session | **228 unchanged** |
| GAP-API07-002 | Facility/site overlap + xact advisory lock | N/A (backend) | Unit **16** passed; `digitize` PG suite **1** passed (list + sequential facility IV); **concurrency DB not provisioned** | Trainer BR-TRN-008 preserved |
| GAP-API05-001 PG IV | — | — | `test_membership_list_by_customer_digitize_postgres.py` **1 passed** on `digitize` @ :5434 | — |

**Evidence:** `evidence/GAP-API05-001_MEMBERSHIP_LIST_BY_CUSTOMER_2026-11-09.md`, `evidence/GAP-API07-001_002_TRAINING_LIST_FACILITY_CONFLICT_2026-11-09.md`

**Recorded scheduling decision:** `site_id` NULL matches NULL only (not interchangeable with site-specific rows).

---

## Session log — 2026-11-09 (GAP-API09-002 — statutory invoice professional approval pack)

| Item | Detail |
| --- | --- |
| Deliverable | `evidence/GAP-API09-002_STATUTORY_INVOICE_PROFESSIONAL_APPROVAL_PACK_2026-11-09.md` |
| Content | INV-001/002/003 questionnaire; commercial design confirmation; blocker map ↔ `ISSUANCE_BLOCKERS` |
| Code | **No change** — issuance remains fail-closed |
| Next | Completed §9 signatures → map to registry §9 → implement approved controls only |

---

## Session log — 2026-11-09 (Master seven-area closure execution)

| Item | Detail |
| --- | --- |
| Document | `evidence/MASTER_SEVEN_AREAS_CLOSURE_EXECUTION_2026-11-09.md` |
| Code changes | **None** (unauthorized: statutory, providers, skeletons, cheque automation, extras) |
| Area G | API-08-012 **live**; PG receipt IV **1 passed**; backfill unit **3 passed**; API-08 acceptance matrix aligned |
| Inventory | **228** numbered · **212** live · **16** skeletons |
| Conclusion | **IMPLEMENTATION BLOCKED** for net-new work; consolidated approval package for user sign-off |

---

## Session log — 2026-11-09 (Consolidated continuation — authorized work exhausted)

| Result | Detail |
| --- | --- |
| Queue scan | DEV-21 P0/P1 + master blockers (2026-11-08/09); **no** unfinished item both authorized and implementable without external approval |
| Reused (not reopened) | Phase 7 billing 080–082; GAP-API12-001 escalate; catalog metadata GAP-API01-003/08-010/09-004/11-004; GAP-API03-005 users scaffold; payment lifecycle / channel UX evidence |
| Code delivered this continuation | **None** — prior session items already merged; remaining backlog is blocked/deferred per master §B/E |
| Sanity | Targeted pytest slice (catalog + users scaffold + support escalate): **pass** (see session GAP-API12-001 / API03-005 / catalog logs) |
| Conclusion | **IMPLEMENTATION BLOCKED** for net-new engineering; local authorized dev scope **closed** per `MASTER_REMAINING_BLOCKERS_APPROVAL_PACKAGE` |

**Resume triggers:** TEST-13 (`GAP-QA-001`); Razorpay sandbox **program** + human capture (`GAP-INT-004`, `GAP-JRN-008` live); INV pack (`GAP-API09-002`); SMS/email tiers (`GAP-INT-001/002`); product deferrals (API-05/07 lists, API-13/14 DDL, cheque automation `GAP-API09-005`).

---

## Session log — 2026-11-09 (GAP-API03-005 — legacy users scaffold)

| Item | Detail |
| --- | --- |
| State | `app/modules/users/` **absent**; not in `LIVE_MODULE_ROUTERS` (`app/api/v1/routes.py`) |
| Consumers | No backend imports of `modules.users`; no Flutter `/api/v1/users` (non-identity) clients |
| Canonical | API-03 staff via `app/modules/identity/routes.py` (`/identity/staff-accounts`, `/identity/users/{id}/*`) |
| Tests | `test_legacy_users_scaffold_removed.py` **4**; `test_identity_staff.py` **6**; `test_api_inventory_reconciliation.py` **4** (inventory); **no code removal** (already retired 2026-11-04) |
| Hardening | Added `test_legacy_scaffold_paths_not_on_v1_router` |

---

## Session log — 2026-11-09 (GAP-API01-003 / API08-010 / API09-004 / API11-004 — catalog metadata drift)

| Item | Detail |
| --- | --- |
| Scope | Metadata alignment only — no routes, contracts, or `IMPLEMENTED_NUMBERED_KEYS` changes |
| Code authority | `COLLECTION_META` + `_COLLECTION_FRONTEND_STATUS` in `numbered_product_contracts.py` (unchanged blurbs; already correct) |
| Doc fix | `API_CONTRACT_REGISTRY.md` §10 — API-01/08/09/11 Flutter paths + INTEGRATED/PARTIAL (was stale NOT_STARTED/TBD) |
| GAP-API09-004 | `API_09_SUBSCRIPTION_LICENSE_IMPLEMENTATION_GATE.md` — catalog PARTIAL vs GAP-API09-003 live pay |
| Tests | `test_collection_metadata_drift.py` **3**; `test_catalog_passes_consistency_checks` ×2; inventory/reconciliation/runtime slices; `validate_catalog()` **0** issues; `NUMBERED_COUNT` **228**; audit **212** live / **16** skeleton |
| Gaps | **Re-closed** — no product behavior change |

---

## Session log — 2026-11-09 (GAP-API12-001 — API-12-008 escalate, history-only Phase 1)

| Item | Detail |
| --- | --- |
| Authorization | Product owner approval for GAP-API12-001 per `API-12_008_Escalate_Migration_Proposal.md` (history-only) |
| Migration | `083_support_ticket_escalation` + SQL twin — `support.ticket_escalation`; `escalate.ticket` → ORGANIZATION_ADMIN + SUPPORT_AGENT only |
| Backend | `SupportTicketEscalationService.escalate` — persist history; status/priority/severity unchanged; reject `to_priority_id`/`to_severity` in Phase 1; `If-Match`; audit `SUPPORT_TICKET_ESCALATED` |
| Flutter | `SupportTicketEscalationPanel` (permission-gated); conversation `refreshGeneration` on ticket version |
| Tests | Unit `test_escalation_service.py` **3**; mig `test_083_*` **1**; PG escalate **3** + lifecycle **1** (`DIGITIZE_SUPPORT_ESCALATE_PG_TEST=1`); Flutter escalation **4** + pages **11** |
| Catalog | `support_tickets_escalate` → **BACKEND_IMPLEMENTED** (`var/api_audit_matrix.csv`) |
| Limitations | No assignee/SLA/notification; no priority bump until a later authorized phase |

---

## Session log — 2026-11-09 (Phase 7 — migrations 080–082 reconciliation)

**Scope:** Confirm existing credit-note / wallet / reversal / manual-reconciliation implementation. **No** schema, route, contract, skeleton promotion, Flutter, or L5 seed changes.

| Item | Evidence |
| --- | --- |
| Mig **080** | `080_billing_credit_notes_customer_credit.py` — org-wide customer-credit wallet, cross-facility apply, corrective CNs; `CreditNoteService` + `POST /api/v1/invoices/{invoice_id}/credit-notes` (`invoices_credit_notes`, API-08-007 `BACKEND_IMPLEMENTED` in `api_audit_matrix.csv`) |
| Mig **081** | `081_billing_credit_note_reversal_idempotency.py` — reversal idempotency, partial/multi-step, ledger compensation |
| Mig **082** | `082_billing_manual_reconciliation.py` — backend-only reconciliation records/history (non-mutating) |
| Frozen rules | T1–T6 unchanged; issued CNs immutable; org numbering; no self-approval; wallet org+customer+currency; append-only ledger; txn balance+ledger; block cancel after apply; `REFUND_MANUAL_REQUIRED` for cash refunds; recon does not mutate payments/invoices/allocations |
| Tests (this session) | `test_billing_evolution_074_082.py` + `test_credit_note_financial_balance.py` → **10 passed**; `test_billing_credit_receipt_recon_http_digitize_postgres.py` (`DIGITIZE_BILLING_HTTP_INTEGRATION_PG_TEST=1`) → **1 passed** on local `digitize` (080–082 HTTP slice) |
| Reused | Prior Phase 8 billing unit IV; `MASTER_REMAINING_BLOCKERS_APPROVAL_PACKAGE_2026-11-08.md` §D — do not redo |
| Next engineering | **None authorized** without explicit gap approval (see blockers below) |

**Explicit deferrals preserved:** new HTTP/Flutter for this scope, L5 permission seeds, formal U7 testing, new product/accounting rules.

**Resume triggers (no implementation until recorded):** live Razorpay sandbox capture (GAP-INT-004 / GAP-JRN-008 live); TEST-13 / `digitize_test` EQ-011 (GAP-QA-001); statutory SaaS invoice (GAP-API09-002); SMS/email delivery tiers (GAP-INT-001/002). Cheque grace deploy: schedule worker + mig 084 on target envs (GAP-API09-005 implemented).

---

## Session log — 2026-11-08 (DR-021 residual hardening)

| Item | Evidence |
| --- | --- |
| Core | `deny_platform_tenant_operational_access`; facility/site deny; tenant org wrapper |
| Modules | billing, attendance, membership, facility, identity, subscription, communication, customer (centralized) |
| Tests | `test_dr021_tenant_operational_access.py` + security PG billing history **403** |
| Doc | `evidence/DR-021_tenant_operational_hardening_2026-11-08.md` |

---

## Session log — 2026-11-08 (GAP-AUTH-002)

| Item | Evidence |
| --- | --- |
| Regression | `tests/security/test_platform_admin_security_regression.py` — **16 passed** |
| PG IV | `DIGITIZE_PLATFORM_ADMIN_PG_TEST=1` security + governance — **7 passed** on local `digitize` |
| Flutter | `platform_admin_operational_boundary_test.dart` — **10 passed** |
| Defect | PA `GET /customers` denied via `_deny_platform_tenant_customer_access` (DR-021) |
| DEV-21 | GAP-AUTH-002 → **Implemented** |

---

## Session log — 2026-11-08 (GAP-AUTH-001)

| Item | Evidence |
| --- | --- |
| Contract | AUTH_CONTRACT_FREEZE §7–8: idle timeout on refresh; access JWT without DB session lookup |
| Code | `session_refresh_is_blocked` + `AuthenticationService.refresh` |
| Unit | `test_session_refresh_policy.py` + principal/helpers — **18 passed** |
| PG IV | `DIGITIZE_AUTH_SESSION_PG_TEST=1` `test_auth_session_digitize_postgres.py` on local `digitize` — **6 passed** |
| DEV-21 | GAP-AUTH-001 → **Verified** |

---

## Session log — 2026-11-07 (Phase 7 — GAP-API07-004)

| Item | Evidence |
| --- | --- |
| PG IV | `DIGITIZE_TRAINING_PG_TEST=1` — `test_training_programs_digitize_postgres.py` **1 passed** (workflows A–F) |
| Fix | Resolve ACTIVE `primary_site_id` for facility before customer create (DR-023 sites on `digitize`) |
| GAP-API07-003 | Skipped re-implementation; `activity_rules_and_progress_test.dart` **2 passed** + remote wiring |
| Flutter wiring | `integration_remote_repository_wiring_test.dart` training (production env override) |

---

## Session log — 2026-11-07 (Phase 6 — GAP-API06-001…003)

| Item | Evidence |
| --- | --- |
| PG IV | `DIGITIZE_ATTENDANCE_PG_TEST=1` — `test_attendance_desk_digitize_postgres.py` **2 passed** (full desk workflow + cross-org reports deny) |
| GAP-API06-002 | PATCH remarks + GET audit added to PG workflow |
| GAP-API06-001 | `POST /walkin-visits/identify` in same PG workflow |
| GAP-API06-003 | Re-verified reports + check-in/out path (supersedes 2026-11-03) |
| Flutter | `flutter test test/features/attendance/` + wiring — **94 passed** |
| Fixes | `invoice_service` ORM metadata (`DiscountDefinition`); `digitize_pg_workflows` `primary_site_id` + site teardown guard; billing teardown FK order in IV cleanup |

---

## Session log — 2026-11-07 (Phase 5 — campaign / staff notifications / subscription-admin IV)

| Gap | Backend IV | Flutter | Defects fixed |
| --- | --- | --- | --- |
| GAP-API10-003 | `DIGITIZE_FLUTTER_SURFACES_PG_TEST=1` — **8 passed** (campaign create+report, notification list/template/reports, cross-org/permission) | `flutter test` campaign + staff_notifications + wiring — **20 passed** | `pagination_metadata(total_records)` + `NotificationAnalyticsService` import; `/licenses/reports` route order |
| GAP-API10-005 | Same suite (history + reports paths) | staff_notifications **9 passed** | Inbox vs staff surface unchanged (prior **7** separation tests) |
| GAP-API09-001 | subscriptions/licenses reports + history | saas_subscription_admin **5 passed** | License reports no longer shadowed by `licenses_get` |

**Test module:** `tests/integration/test_flutter_surfaces_digitize_postgres.py`

---

## Session log — 2026-11-07 (Phase 4 — GAP-API10-004)

| Item | Result |
| --- | --- |
| Root cause | `notification_preferences_update` in `DATABASE_GAP_IDS` despite live route + `customer.customer_preference` (004) |
| Fix | Metadata only — removed from `DATABASE_GAP_IDS`; no migration/route/schema change |
| Tests | `test_notification_preferences_update_not_marked_database_gap_api10_004`, `test_api10_024_live_route_matches_frozen_contract` |
| Product note | Flutter still needs known `preference_id` (no list op in 228) — **not** part of GAP-API10-004 |

---

## Session log — 2026-11-07 (Phase 3 — catalog / scaffold / DR-023)

| Gap | Status | Evidence |
| --- | --- | --- |
| GAP-API01-003, API08-010, API09-004, API11-004 | **CLOSED** (re-verified) | `COLLECTION_META` + `_COLLECTION_FRONTEND_STATUS`; `test_collection_metadata_drift.py`; API-08 `repository` → `billing.*` |
| GAP-API03-005 | **CLOSED** (re-verified) | `app/modules/users/` absent; `test_legacy_users_scaffold_removed.py` (+ identity staff route mounted) |
| GAP-API02-003 | **INTEGRATION_VERIFIED** | `DIGITIZE_DR023_HIERARCHY_PG_TEST=1` — **4 passed** on local `digitize` (read-only) |
| Docs drift | **IMPLEMENTED** | `API_CONTRACT_REGISTRY.md` inventory counts (364 source / **0** unmounted); regenerated `var/api_inventory_reconciliation.json` |

**Tests (2026-11-07 Phase 3):** `pytest tests/api/test_collection_metadata_drift.py test_legacy_users_scaffold_removed.py test_contract_registry.py test_runtime_catalog.py test_catalog_validation.py test_api_inventory_reconciliation.py` — **56 passed**; `test_identity_staff.py` — **pass** (module).

---

## Session log — 2026-11-07 (Phase 2 — contract/metadata N-05…N-08)

| Item | Result |
| --- | --- |
| N-05 `DATABASE_GAP_IDS` | Removed `invoices_credit_notes`; catalog entities → `billing.credit_notes*`; **API-08-007 route still SKELETON** |
| N-06 naming | `API_CONTRACT_REGISTRY` API-08 DB column: `billing.*` vs SaaS `commercial.*` |
| N-07 OpenAPI | Routes: `memberships_renewals`, `trainers_facility_assignments`, `payments_status_list` |
| N-08 J5 | DEV-22 workflow table — Phase-1 vs quotation-first gaps |
| Tests | `test_contract_registry.py` (N-05/N-07), `pytest tests/api/test_runtime_catalog.py test_catalog_validation.py` |

---

## Session log — 2026-11-08 (GAP-JRN-008 — facility mock online pay)

**Flutter:** `FacilityOutstandingStatementsPanel` — **Pay online (mock)** → `POST /api/v1/payments/online` initiate (Idempotency-Key) + verify with mock dialog; reloads outstanding, billing history, SaaS invoice/installment list.

**Tests:** `facility_outstanding_statements_controller_test.dart` + `facility_mock_online_checkout_dialog_test.dart` — **15 passed**. Backend IV: existing `test_billing_m2_http_digitize_postgres.py` (API-08-009).

**Gate:** Live Razorpay remains GAP-API08-006.

---

## Session log — 2026-11-08 (Razorpay sandbox — GAP-INT-004 / API-08-006 / API-09-003)

**Backend:** `FacilityRazorpayGateway.from_settings`; API-08-009 `mock_checkout` / `gateway` / `key_id` from `RAZORPAY_MODE`; facility webhook settlement via shared `POST /webhooks/razorpay`.

**Flutter:** Facility outstanding **Pay online** uses `createCheckoutGateway()` when `mock_checkout=false`; mock dialog unchanged.

**Tests:** gateway **2**; billing/SaaS HMAC suite **28**; Flutter outstanding + checkout **18**.

**Evidence:** `evidence/RAZORPAY_SANDBOX_INTEGRATION_2026-11-08.md` — **no live/sandbox card charge executed** this session.

**Production payments:** still disabled / out of scope.

---

## Session log — 2026-11-08 (Razorpay facility pay — PG `digitize` IV)

**PG:** `DIGITIZE_BILLING_HTTP_INTEGRATION_PG_TEST=1` — `test_billing_m2_http_digitize_postgres.py` **1 passed** (mock online + webhook settle + duplicate/invalid/mismatch); credit/receipt/recon **1 passed**; SaaS webhook concurrency **3 passed**.

**Harness:** IV forces `RAZORPAY_MODE=mock` on `app.state.settings` (avoids accidental Razorpay HTTP from dev `.env`).

**Manual sandbox card checkout:** still **not** verified.

---

## Session log — 2026-11-08 (Manual Razorpay sandbox E2E — blocked)

**Preflight:** `.env` `RAZORPAY_MODE=live` (not `sandbox`); test key prefix ok; no production keys; webhook URL not confirmed; Flutter not run.

**Probe:** with session `RAZORPAY_MODE=sandbox`, real Razorpay **order create** ok; REST payment create 401 → Checkout UI required.

**Card checkout:** **NOT executed.** Evidence: `RAZORPAY_SANDBOX_INTEGRATION_2026-11-08.md` § Manual sandbox end-to-end.

---

## Session log — 2026-11-09 (Payment lifecycle verification)

- Lifecycle matrix: online (PG mock), offline methods, cheque PENDING/clear/bounce design; reconciliation rules.
- Tests: backend **23** + Flutter **25** passed; PG M2 **1** re-run; **no** live Razorpay capture.
- Evidence: `PAYMENT_LIFECYCLE_E2E_2026-11-09.md`.

---

## Session log — 2026-11-09 (Payment channel selection UX)

- Outstanding: **Collect payment** → channel dialog → online (Razorpay after initiate) or offline form.
- Harness labelled engineering-only; does not replace channel selection journey.
- Flutter tests: channel dialog + payment flow widget + cheque pending controller (**24+** related passing).
- Razorpay sandbox capture: still **not** server-verified.

---

## Session log — 2026-11-08 (Manual sandbox result audit)

- Inspected harness JSON + DB + Razorpay order/payments API: **checkout cancelled**, no capture, invoice **ISSUED**, no server verify, no inbound webhook.
- Payment journey **not** marked complete. Evidence: `RAZORPAY_SANDBOX_INTEGRATION_2026-11-08.md` § Manual checkout result inspection.

---

## Session log — 2026-11-08 (Razorpay device verification — partial)

- API `:8000` + Checkout.js harness; Test Mode modal; **UPI QR** visible after harness display blocks aligned with Flutter.
- **No** sandbox capture, server verify, invoice PAID, inbound webhook, or Android UPI Intent (iframe + no device + no tunnel).
- Live invalid webhook → **422**; harness checkout cancel verified.
- Evidence: `RAZORPAY_SANDBOX_INTEGRATION_2026-11-08.md` § Device verification run.

---

## Session log — 2026-11-08 (Payment method coverage + collection UX)

- Razorpay checkout: shared options enable card/UPI/netbanking; UPI Collect not implemented.
- Flutter outstanding: Pay online vs physical collection labels; history already shows `payment_method`.
- Evidence: `PAYMENT_METHOD_COVERAGE_2026-11-08.md`; Flutter **19** + billing **9** tests passed.
- Blocker: physical **card terminal** offline method not in frozen API-08 set.

---

## Session log — 2026-11-08 (Sandbox order + Checkout.js; payment pending)

- Dev `.env`: `RAZORPAY_MODE=sandbox` (test keys only).
- Digitize initiate → real Razorpay order; Checkout.js **Test Mode** modal opened via `scripts/razorpay_sandbox_facility_e2e.py`.
- **Payment not captured** (order payments count 0); **Flutter E2E not run**; **no webhook tunnel**.

---

## Session log — 2026-11-08 (Second-installment due tracking — billing list + PG IV)

**Backend:** `GET /api/v1/saas/invoices` — backward-compatible list fields (`billing_option`, `second_installment`) + `metadata.second_installments` from `commercial.saas_payment_obligation` (INSTALLMENT_2) and quote-derived `due_at`. Timing labels: paid / upcoming / due / overdue / suspended / unavailable (no invented grace).

**Flutter:** Org billing facility + invoice rows; subscription detail reloads tracking after lifecycle; shared `SecondInstallmentStatusLine`.

**GET invoice:** `second_installment` on `GET /api/v1/saas/invoices/{id}`; SaaS invoice detail UI.

**Checkout:** Successful payment/offline commitment navigates to facility-scoped **Subscriptions & Billing** (reloads installment metadata).

**Tests:** `test_installment_tracking.py` **3 passed**; `test_subscription_history_metadata_digitize_postgres.py` **3 passed** (`DIGITIZE_SUBSCRIPTION_HISTORY_PG_TEST=1` on `digitize`); Flutter **9 passed** (installment + subscription admin).

---

## Session log — 2026-11-08 (API-09-011 — subscription snapshot on history + OA journey wiring)

**Backend:** `GET /api/v1/subscriptions/{id}/history` returns authoritative `metadata.subscription` (`SubscriptionOut`) alongside paginated lifecycle rows — no new route.

**Flutter:** `SubscriptionDetailController.load` hydrates status from history metadata; history pagination; org billing ↔ lifecycle hub (`facilityId` query + per-facility **Lifecycle**); invoice detail → subscription detail; checkout shows second-installment due date from quote.

**Tests:** `subscription_admin_controller_test.dart` **6 passed** (incl. load snapshot). Live `DIGITIZE_API_TEST` history assertion added — not executed (guard requires `digitize_test`).

**Gates unchanged:** GAP-API09-002/003/005.

---

## Session log — 2026-11-08 (GAP-JRN-010 — notifications inbox + campaign journey tests)

**Inbox:** `InAppInboxController` — pagination, mark-read single-flight, API error messages; inbox page load/empty/retry/unread filter; bell unread invalidate on mark.

**Campaign:** Performance metrics disclaimer (manual WhatsApp not counted); list page test key; existing lifecycle/create/detail/share unchanged (manual external default; automated launch disabled).

**Tests:** `in_app_inbox_controller_test.dart` (4), `in_app_inbox_page_test.dart` (3), `campaign_list_page_test.dart` (2) + prior campaign/surface tests — **22 passed** in notification/campaign bundle.

**Gates:** GAP-API10-001–003 provider paths; no campaign list/get numbered API.

---

## Session log — 2026-11-08 (GAP-JRN-011 — scheduled report delivery UI)

**Flutter:** `ReportScheduleDeliveryPanel`, `ReportScheduleDeliveryController`, extended `RemoteReportingRepository` (`GET/POST /api/v1/report-schedules`, recipients POST/DELETE). Schedule uses selected schedulable report code (not hardcoded). Messaging distinguishes schedule vs HELD delivery vs email.

**Tests:** `test/features/reporting/` — **28 passed** (controller + company reports page).

**Gates unchanged:** GAP-API11-001 (live notifier), GAP-INT-002; no list-recipients or delivery-run read API.

---

## Session log — 2026-11-08 (Cross-module journeys — attendance discoverability, facility billing scope, Site Admin nav)

**Flutter:** Facility details **Membership billing** → `OrganizationRouteNames.billingScopedToFacility`; outstanding/history panels accept optional `facilityId`; billing page shows facility filter banner.

**Tests:** `attendance_entry_page_test.dart` **3 passed**; `operational_shell_nav_test.dart` **2 passed**; facility billing controller facility-scope **+2** tests.

**Gaps:** GAP-JRN-006 **Connected**; GAP-JRN-008 offline path deep link; GAP-ROLE-001 **TESTED**.

---

## Session log — 2026-11-08 (Operational Flutter remote DI — membership, trainer, notifications)

**Providers:** membership, trainer, device-token, in-app notification → always remote (facility pattern). Auth mock retained only for explicit `AppEnvironment.development()`; `main` defaults `DIGITIZE_REMOTE` → production/live auth.

**Tests:** `operational_provider_environment_test.dart`, `authentication_provider_environment_test.dart`, wiring tests — **26 passed** (provider regression bundle).

---

## Session log — 2026-11-08 (Facility remote DI + billing HTTP PG IV)

**Flutter:** `facility_access_providers` always remote (mock via test overrides only); `facility_provider_environment_test.dart` + wiring tests **14 passed**.

**Backend:** `test_billing_credit_receipt_recon_http_digitize_postgres.py` — HTTP IV on `digitize` (`DIGITIZE_BILLING_HTTP_INTEGRATION_PG_TEST=1`) **1 passed**; fixed credit/receipt/recon response `model_dump(mode="json")`.

---

## Session log — 2026-11-08 (Execution batch — billing routes 007/012/014, Flutter DI, ORG-TERMS IV)

**Backend:** Promoted **API-08-007**, **API-08-012**, **API-08-014** to live routes delegating to existing services (`billing/routes.py`, schemas, `ReceiptService.issue_for_payment_id`). Inventory **207/228** implemented, **21** skeletons (`contract_numbered_audit.py`).

**Flutter:** GAP-UI-002 (staff, training-ops, walk-in always remote); GAP-UI-003 (mock checkout host only in mock `AppEnvironment`).

**Tests:** `test_billing_numbered_skeleton_routes.py`, contract registry route registration, `test_org_terms_digitize_postgres.py` (opt-in `DIGITIZE_ORG_TERMS_PG_TEST=1`); Flutter `app_environment_test` + `integration_remote_repository_wiring_test` **9 passed**; backend tracking/contract subset **12+ passed**.

---

## Session log — 2026-11-08 (Master backlog reconciliation — DEV-21 + 24 skeletons)

**Requested:** Implement all 75 DEV-21 gaps and all non-deferred numbered skeletons in one pass.

**Repository evidence (2026-11-08):**
- `scripts/contract_numbered_audit.py` → **204** `BACKEND_IMPLEMENTED`, **24** `SKELETON_CREATED` (unchanged).
- Phases 1–13 + prior engineering passes closed **independently actionable** items; **no** skeleton promotions without decision-register authorization.
- **24/24 skeletons** map to explicit **Deferred**, **Blocked**, or **Awaiting authorization** in `operation_tracking.py` / decision registers (API-08×8, API-12-008, API-13×8, API-14×7).

**Outcome:** **INCOMPLETE — ACTIONABLE ENGINEERING REMAINS** only where **product/legal/provider/migration authorization** is missing; **not** because implementable Phase work was skipped. Further coding without approvals would invent contracts (billing engines, client audit POST, statutory invoice, escalation DDL, GMD seeds).

**Next authorized batch (per DEV-23 Phase 0):** await owner decisions on P0 table below; then implement **one approved skeleton family** at a time after additive migration auth.

---

## Session log — 2026-11-08 (API-13 Phase 13 — Audit evidence reconciliation)

**Scope:** Re-verify reads (005/009/012), server-side capture boundary, no client ingest routes.

| Item | Outcome |
| --- | --- |
| GAP-API13-006 | **INTEGRATION_VERIFIED** (reconfirmed) — audit PG **4 passed** |
| GAP-API13-001 | **Deferred (product)** — 001–003 remain server-side only; no routes added |
| GAP-API13-002/003/004/005/007 | **Blocked/Deferred** — unchanged |
| Production code | **None** |

**Tests:** audit unit **12 passed**; PG IV **4 passed**; Flutter audit **11 passed**.

**Status:** **COMPLETE WITH APPROVED BLOCKERS**

---

## Session log — 2026-11-08 (GAP-JRN-012 — Flutter support ticket lifecycle)

**Scope:** Wire authorized support-ticket lifecycle in Flutter; **no** API-12-008 escalation.

| Item | Outcome |
| --- | --- |
| GAP-JRN-012 | **Partial — Flutter TESTED** — detail via `GET /api/v1/support-tickets/{id}`; lifecycle refresh; reports pagination; conversation messages preview + chat link |
| GAP-API12-001 | Unchanged — **AWAITING_AUTHORIZATION**; static escalation notice only |
| Evidence | `evidence/GAP-JRN-012_support_ticket_flutter_lifecycle_2026-11-08.md` |

**Tests:** `flutter test test/features/support_tickets/support_ticket_pages_test.dart` → **11 passed**.

## Session log — 2026-11-08 (EQ-011 post-migration reconciliation)

- Root causes: stale org/subscription fixtures (legal identity + DR-021 tenant headers), `advanced_reporting` catalog addon (039), facility-type pagination on dirty `digitize_test`.
- **73 passed, 1 skipped** `test_subscription_license.py` + `test_platform_catalog.py` on `digitize_test`.
- Mailpit **UP**; `DIGITIZE_MAILPIT_REPORT_TEST=1` delivery **5 passed**.
- Evidence: `EQ011_POST_MIGRATION_RECONCILIATION_2026-11-08.md`.

## Session log — 2026-11-08 (Master approval execution)

- User master instruction applied; report: `evidence/MASTER_APPROVAL_EXECUTION_REPORT_2026-11-08.md`.
- **API-12-008:** migration 083, route, Flutter escalate panel; PG **1 passed**, unit **22 passed**, Flutter **11 passed**.
- **GAP-INT-002:** `CommunicationService` + SES adapter prepared; `SmtpReportNotifier` / `HeldReportNotifier` unchanged — evidence `GAP-INT-001-002_COMMUNICATION_CONSOLIDATION_2026-11-09.md`.
- **EQ-011:** local `digitize_test` upgraded to 083; preflight READY; API-09 suite **49 passed / 13 failed** (catalog count drift).
- **GAP-INT-001:** SMS OTP deferred first release.
- **Razorpay:** `sandbox` mode + facility/SaaS dual path — see `RAZORPAY_SANDBOX_INTEGRATION_2026-11-08.md` (no card charge in agent run).

## Session log — 2026-11-08 (Master remaining blockers — approval checkpoint)

- Inspected all closure blockers; **no new authorizations** in repo.
- Deliverable: `evidence/MASTER_REMAINING_BLOCKERS_APPROVAL_PACKAGE_2026-11-08.md` (single approval matrix + bundles).
- Aligned `eq011_digitize_test_preflight.py` expected head → `082_billing_manual_reconciliation` (read-only probe; **no** `digitize_test` migration).
- **No implementation** for blocked gaps; resume when GAP ID + approval recorded per package §F.

## Session log — 2026-11-08 (GAP-API02-005 — governance timeline UX)

- Paginated PA governance timeline section; `organization_governance_panel_test.dart` **2 passed**.

## Session log — 2026-11-08 (GAP-ROLE-003 — PA scoped audit PG IV)

| Item | Outcome |
| --- | --- |
| Governance access | `require_governance_organization_access` on audit reads |
| PG IV | `test_audit_platform_admin_digitize_postgres.py` + existing audit IV → **8 passed** |
| Regression | audit unit **11 passed**; DR-021/PA security **25 passed** |
| Evidence | `evidence/GAP-ROLE-003_platform_admin_audit_reads_2026-11-08.md` |

## Session log — 2026-11-08 (GAP-JRN-011 — HELD delivery UX)

- `schedule_delivery_held_notice` on active schedule card; live email still **GAP-API11-001**.

## Session log — 2026-11-08 (GAP-JRN-012 — agent workspace + center pagination)

**Scope:** Support agent Flutter wiring; fix broken pagination on support-center list routes.

| Item | Outcome |
| --- | --- |
| Agent workspace | Dashboard inbox/queue + `getTicket` refresh on agent ticket controls |
| Backend | `routes_center.py` — `pagination_metadata` keyword args (6 routes); PG IV extended |
| Tests | Flutter agent **4 passed**; support unit **31 passed**; PG **1 passed** |

---

## Session log — 2026-11-08 (API-12 Phase 12 — Support completion)

**Scope:** Re-verify live ticket lifecycle (GAP-API12-002); preserve API-12-008 gate (GAP-API12-001).

| Item | Outcome |
| --- | --- |
| GAP-API12-002 | **INTEGRATION_VERIFIED** (reconfirmed) — `DIGITIZE_SUPPORT_PG_TEST=1` → **1 passed** |
| GAP-API12-001 | **AWAITING_AUTHORIZATION** — no migration/route/permission changes; Alembic head **082** |
| Production code | **None** |

**Tests:** support unit **28 passed**; PG IV **1 passed**; Flutter support **18 passed**.

**Status:** **COMPLETE WITH APPROVED BLOCKERS**

---

## Session log — 2026-11-07 (API-09 Phase 11 — SaaS subscription completion)

**Scope:** Re-verify subscription/license lifecycle and commercial rules; no new formulas, statutory fields, or provider credentials.

| Gap | Phase 11 outcome |
| --- | --- |
| GAP-API09-001 | **INTEGRATION_VERIFIED** (reconfirmed) — Flutter admin + PG surfaces IV |
| GAP-API09-002 | **BLOCKED (product + legal)** — `ISSUANCE_BLOCKERS` fail-closed unchanged |
| GAP-API09-003 | **AWAITING_AUTHORIZATION** — mock/HMAC/webhook PG **3 passed**; no live Razorpay |
| GAP-API09-004 | **Closed** — not reopened |
| GAP-API09-005 | **Dev deployed (2026-11-09)** — mig **084** on local **`digitize`**; worker tick OK; schedule external (not configured); evidence `GAP-API09-005_CHEQUE_BOUNCE_GRACE_IMPLEMENTATION_2026-11-09.md` |
| GAP-API09-006 | **INTEGRATION_VERIFIED** (reconfirmed) — proration PG **5 passed** |

**Defect fixed:** `saas_checkout_controller_test.dart` — `_FakeRepository.previewQuote` missing `facilityId` / `effectiveDateIso` (INV-005 API drift).

**Tests:** subscription unit **139 passed**; proration PG **5**; webhook rollback PG **3**; flutter surfaces **8**; Flutter SaaS **38 passed**.

**Status:** **COMPLETE WITH APPROVED BLOCKERS** — no claim of full API-09 certification while 002/003/005 remain.

---

## Session log — 2026-11-07 (API-01 Phase 10 — Platform Admin completion)

**Scope:** Verify Platform Admin console, onboarding integration, governance boundaries; local `digitize` IV only.

| Gap | Outcome |
| --- | --- |
| GAP-API01-001 | **INTEGRATION_VERIFIED** — governance HTTP IV + Flutter console tests (no contract changes) |
| GAP-API01-002 | **BLOCKED** — EQ-011 / shared QA not accessed |
| GAP-API01-003 | **Closed** — not reopened |

**Tests (2026-11-07 Phase 10):**

| Suite | Result |
| --- | --- |
| `pytest tests/organization/test_onboarding_review.py` … authz/saas unit | **28 passed** |
| `DIGITIZE_PLATFORM_ADMIN_PG_TEST=1` … `test_platform_admin_governance_digitize_postgres.py` | **2 passed** |
| `flutter test` platform_administration + PA boundary + dashboard UX | **20 passed** |

**Status:** **COMPLETE WITH APPROVED BLOCKERS** (shared-env certification).

---

## Session log — 2026-11-07 (API-11 Phase 9 — reporting & scheduled delivery)

**Scope:** Verify exports and reporting IV; close evidence gaps for schedule execution without introducing email providers or new migrations.

| Workstream | Finding | Action |
| --- | --- | --- |
| A — Reports & exports | GAP-API11-003 already **INTEGRATION_VERIFIED**; routes/rules/decisions covered | Re-ran suites; no product code changes |
| B — Scheduled delivery | `worker.run_due_schedules` + mig **039** `tenant_report_schedule` chain on head **082**; `HeldReportNotifier` by design | **TESTED** — `test_report_schedule_worker.py` (HELD/FAILED/SENT-skip); GAP-API11-001 **BLOCKED (provider)** |

**Tests (2026-11-07 Phase 9):**

| Suite | Result |
| --- | --- |
| `pytest tests/reports/ -q` | **55 passed**, 19 skipped |
| `DIGITIZE_REPORTS_EXPORT_HTTP_TEST=1` … `test_reports_export_http_digitize.py` | **5 passed** |
| `DIGITIZE_REPORTING_SQL_TEST=1` … `test_reporting_sql_integration.py` | **14 passed** |
| `flutter test test/features/reporting/` | **21 passed** |

**Status:** **COMPLETE WITH APPROVED BLOCKERS** — on-screen/export reporting verified; scheduled **calculation + delivery audit** verified; external email delivery not authorized.

---

## Session log — 2026-11-07 (API-08 Phase 8 — remaining engineering gaps)

**Scope:** Close independently actionable API-08 work only (effective outstanding consistency, historical receipt backfill verification, regression IV). No skeleton promotion; no migrations 083+; excluded ops 002–005, 007 route, 009, 012, 014.

| Workstream | Gap / op | Finding | Action |
| --- | --- | --- | --- |
| A — Effective outstanding | API-08-018 | `OutstandingStatementsService` already uses `batch_invoice_effective_outstanding` (same `invoice_effective_outstanding_from_totals` core as payment/cheque lock path) | **No code change** — added `test_credit_note_financial_balance.py` (CN/customer-credit/refund/cancel scenarios) |
| B — Historical receipt backfill | M6 / offline pre-079 | `ReceiptBackfillService` + `scripts/backfill_historical_payment_receipts.py` (`assess` / `dry-run` / `execute`); digitize-only guard | **TESTED** — `test_receipt_backfill_service.py` (classify, dry-run, no commit). Bulk **execute** not run on shared `digitize` — **AWAITING_AUTHORIZATION** |
| C — Regression | GAP-API08-009 | Unchanged product paths | Re-ran billing unit + live IV + Flutter controllers |

**Tests (2026-11-07 Phase 8):**

| Suite | Result |
| --- | --- |
| `pytest tests/billing/ -q` | **56 passed**, 7 skipped |
| `DIGITIZE_BILLING_LIVE_VERIFICATION=1` … `test_billing_invoices_revenue_live_digitize.py` | **1 passed** (history + outstanding HTTP in suite) |
| `flutter test` billing history + outstanding controllers | **32 passed** |

**Status:** Phase 8 **COMPLETE WITH APPROVED BLOCKERS** — engineering evidence for 018 parity and backfill policy; product-deferred skeletons unchanged.

---

## Session log — 2026-11-07 (API-08 billing WIP stabilization)

**Scope:** November 6 assessment stabilization items (migrations 074–082, API-08-016 Phase 2, outstanding alignment, Alembic head, `DATABASE_GAP_IDS`, test/docs reconciliation). No skeleton promotion; no new product scope.

| WIP item | Finding | Action |
| --- | --- | --- |
| Migrations 074–082 | Chain + SQL twins present; head `082_billing_manual_reconciliation` | **Left as-is**; added `test_billing_evolution_074_082.py` + extended `test_sql_twin.py` |
| API-08-016 Phase 2 | `financial_events` wired in `BillingHistoryService` | **Already complete** — aligned tests (`test_billing_history_financial_events.py`) |
| Outstanding (018) | `batch_invoice_effective_outstanding` in outstanding statements | **Already complete** — unit `test_outstanding_statements.py` |
| Alembic docs vs code | Nov 6 evidence cited head `072` | **Docs updated** (DEV-21, API-08 evidence); repo head **082** |
| `DATABASE_GAP_IDS` | `invoices_credit_notes` stale schema flag | **Superseded** by Phase 2 N-05 (schema live; route still skeleton) |
| Phase-1 unit regressions | Billing evolution hooks (allocations/receipts/txn) broke mocks | **Fixed** — `billing_full_payment` getattr; `billing_phase1_mocks.py`; test updates |
| GAP-API08-009 IV teardown | FK on `payment_allocation_reversals` | **Fixed** cleanup order in live IV test |

**Tests (2026-11-07):**

| Suite | Result |
| --- | --- |
| `pytest tests/billing tests/migrations/test_billing_evolution_074_082.py -q` | **47 passed**, 7 skipped |
| `DIGITIZE_BILLING_LIVE_VERIFICATION=1` … `test_billing_invoices_revenue_live_digitize.py` | **1 passed** |
| `flutter test` billing history + outstanding controllers | **32 passed** |

**Status:** Phase-1 operational billing **TESTED** + **INTEGRATION-VERIFIED** (GAP-API08-009). Evolution migrations **IMPLEMENTED** in repo; env apply + numbered-route promotion remain **BLOCKED/DEFERRED** per decision register.

---

## Session log — 2026-11-07 (API-04 Customer — gap-closure pass)

**Scope:** DEV-21 API-04 entries only (GAP-API04-001, GAP-API04-002, GAP-INT-001 cross-ref). No new product requirements; no schema or route changes.

**Gap inventory:**

| Gap ID | Status | Action this pass |
| --- | --- | --- |
| GAP-API04-002 | Integration-verified (prior) | Re-ran PG IV on local `digitize` |
| GAP-API04-001 | Blocked (provider) | No live SMS; memory/none OTP path remains provider-ready per instructions |
| GAP-INT-001 | Blocked (provider) | Shared with API-04/06 attendance OTP — unchanged |

**Backend / extras:** 12 numbered API-04 operations **BACKEND_IMPLEMENTED** (`API_04_CUSTOMER_IMPLEMENTATION_GATE.md` PASS); registration-phone OTP extras (`customers_registration_phone_otp_create` / `verify`) wired with Flutter `RemoteRegistrationPhoneOtpRepository` + form verify/resend UX.

**Tests executed (2026-11-07):**

| Suite | Command / flag | Result |
| --- | --- | --- |
| Customer module | `poetry run pytest tests/customer tests/api/test_customer.py -q` | **43 passed**, 34 skipped (opt-in PG/PPI) |
| Registration OTP unit | `pytest tests/customer/test_registration_phone_*.py -q` | **15 passed** |
| CRM PG IV (GAP-API04-002) | `DIGITIZE_CUSTOMER_PG_TEST=1 DB_NAME=digitize … test_customer_crm_digitize_postgres.py -q` | **1 passed** |
| Flutter customer | `flutter test test/features/customer/` | **37 passed** |

**Module verdict:** **COMPLETE WITH APPROVED BLOCKERS** — engineering work for approved API-04 scope is done; remaining work is authorized live SMS vendor QA only (GAP-API04-001 / GAP-INT-001).

---

## Session log — 2026-11-04 (canonical `api_registry.py` consolidation)

**Change:** All approved operation rows (numbered + additional, incl. ORG-TERMS + onboarding) consolidated into **`app/api/contracts/api_registry.py`**. Legacy `operations.py` / `extra_operations.py` removed after migration. `numbered_product_contracts.py` retains EndpointContract enrichment only.

**Migration proof:** `tests/fixtures/pre_migration_registry_baseline.json` + `tests/api/test_api_registry_consolidation.py`.

**Validation:** `validate_catalog()` pass; `scripts/api_inventory_reconciliation.py` pass.

---

## Session log — 2026-11-04 (complete API inventory reconciliation)

**Scope:** Entire approved API surface (numbered + extras + T&C + onboarding + runtime + source).

**Evidence:** [API_INVENTORY_RECONCILIATION_2026-11-04.md](./evidence/API_INVENTORY_RECONCILIATION_2026-11-04.md), `var/api_inventory_reconciliation.json`.

**Totals (calculated, not hardcoded in validators):**

| Layer | Count |
| --- | ---: |
| Approved operation identities | **386** (228 + 158) |
| Live `/api/v1` HTTP | **362** |
| Numbered skeleton (no route) | **24** |
| ORG-TERMS extras | **6** (within 158) |
| ORG-ONBOARDING-ACCEPT-001 | **1** (within 158) |
| WebSocket | **1** |
| Docs UI | **2** |
| Unmounted source (`users/routes.py`) | **2** |

**Code:** `approved_inventory_summary()` in `catalog.py`; `scripts/api_inventory_reconciliation.py`; dynamic collection counts in `validate_numbered_product_catalog()`; tests `test_api_inventory_reconciliation.py`.

**Validation:** `validate_catalog()` → **0 issues**. `pytest tests/api/test_api_inventory_reconciliation.py tests/api/test_runtime_catalog.py tests/api/test_contract_registry.py tests/api/test_module_routes.py` → **pass**.

**Assessment:** **COMPLETE WITH APPROVED DEFERRED ITEMS** (24 skeletons + decision-register deferrals unchanged).

---

## Session log — 2026-11-04 (GAP-API08-009 billing PG IV — closed)

**Root cause:** Live suite asserted absolute January INR `10000.00` on facility A while local `digitize` already held other SUCCESS January payments for the same org/facility (prior IV tags / seed data) — aggregate correctly returned **40000.00**.

**Fix (test only):** Capture revenue baseline before TAG bootstrap; assert **delta** matches fixture (`+10000` Jan A, `-3000` Feb A with refunds, `+5000` Jan B); TAG-prefix cleanup in `finally`. No billing product or `aggregate_customer_revenue` code changes.

**Evidence:** `DIGITIZE_BILLING_LIVE_VERIFICATION=1` — **1 passed** ×2 consecutive runs on `digitize`.

---

## Session log — 2026-11-04 (five engineering priorities — implementation)

| Priority | Gap | Work | Evidence |
| --- | --- | --- | --- |
| P1 | GAP-API03-005 | Removed entire `app/modules/users/` scaffold (unmounted GET/POST `/users`) | `tests/api/test_legacy_users_scaffold_removed.py` |
| P2 | GAP-API01-003, 08-010, 09-004, 11-004 | `COLLECTION_META`, `_COLLECTION_FRONTEND_STATUS`, `_frontend_status()`; API-09 gate doc refresh | `tests/api/test_collection_metadata_drift.py`; `validate_catalog()` pass |
| P3 | GAP-API02-003 | Read-only DR-023 hierarchy IV on local `digitize` | `tests/facility/test_dr023_hierarchy_digitize_postgres.py` (opt-in `DIGITIZE_DR023_HIERARCHY_PG_TEST=1`) |
| P4 | Flutter IV | Verified campaign/staff/subscription-admin use `Remote*` repositories (no mock in provider roots) | `digitize-ui/test/features/integration_remote_repository_wiring_test.dart` |
| P5 | PG IV | Re-ran opt-in module suites on `digitize` (billing, support, audit, CRM, training, reports) | Commands + counts in session notes below |

**PostgreSQL IV (2026-11-04, `DB_NAME=digitize`, loopback):**

| Suite | Env flag | Result |
| --- | --- | --- |
| Billing live | `DIGITIZE_BILLING_LIVE_VERIFICATION=1` | **1 passed** (×2 runs 2026-11-04) — baseline/delta revenue assertions + TAG-scoped teardown; production `aggregate_customer_revenue` unchanged |
| Support | `DIGITIZE_SUPPORT_PG_TEST=1` | **1 passed** |
| Audit reads | `DIGITIZE_AUDIT_PG_TEST=1` | **4 passed** |
| CRM | `DIGITIZE_CUSTOMER_PG_TEST=1` | **1 passed** |
| Training | `DIGITIZE_TRAINING_PG_TEST=1` | **1 passed** |
| Reports export HTTP | `DIGITIZE_REPORTS_EXPORT_HTTP_TEST=1` | **5 passed** |
| DR-023 hierarchy | `DIGITIZE_DR023_HIERARCHY_PG_TEST=1` | **4 passed** |

**Unmounted source handlers:** **0** (was 2 in `users/routes.py`).

---

## Session log — 2026-11-04 (blocker resolution pass — inventory-wide)

**Scope:** Resolve outstanding blocker metadata, approval-ready requests, and executable defects across **386** approved operations (not a repeat of skeleton-24 assessment).

**GMD catalog test (GAP-QA catalog alignment):** `test_approved_global_master_data_groups_match_db11` failed because `TENANT_READABLE_MASTER_DATA_GROUPS` was expanded for API-14 reference aliases while the test still asserted DB-11-era tenant scope. **Root cause:** approved product policy in [API-14_REFERENCE_SOURCE_OF_TRUTH.md](../architecture/API-14_REFERENCE_SOURCE_OF_TRUTH.md) and `app/modules/platform/catalogs.py` — **not** a missing migration. Test updated to document DB-11 groups vs tenant-readable expansion; **no route or schema change.**

**Unmounted `users/routes.py`:** **Superseded 2026-11-04** — module removed (GAP-API03-005 **closed**); see Phase 3 re-verification above.

**Skeleton / gated ops:** **24** remain `SKELETON_CREATED`; **0** promoted (existing decision registers unchanged). See § Blocker approval pack below in session notes and [SKELETON_24_IMPLEMENTATION_ASSESSMENT_2026-11-04.md](./evidence/SKELETON_24_IMPLEMENTATION_ASSESSMENT_2026-11-04.md) for inventory only.

**Validation:** `pytest tests/api/test_catalog_validation.py tests/api/test_reference_aliases.py -q` → **pass**; full `tests/api/` → **111 passed** (1 prior GMD failure cleared).

---

## Session log — 2026-11-04 (remove obsolete compatibility modules)

**Deleted:** `app/api/contracts/operations.py`, `app/api/contracts/extra_operations.py` (thin re-exports; all consumers import `api_registry.py`).

**Retained:** `numbered_product_contracts.py` (EndpointContract enrichment), `contract_numbered_audit.py` (numbered-subset legacy audit with explicit scope).

**Verification:** inventory reconciliation + API contract tests pass.

---

## Session log — 2026-11-04 (unified implementation tracking)

**Change:** `operation_tracking.py` owns per-operation status for all **386** approved identities. `catalog.py` reconciles runtime against the full implemented set. `approved_inventory_summary()` exposes unified metrics only (no numbered/additional split). `contract_numbered_audit.py` documented as numbered-subset only.

**Tests:** `tests/api/test_unified_operation_tracking.py` + inventory suite (**pass**).

---

## Session log — 2026-11-09 (pre-QA release execution)

**Scope:** Security gate, WhatsApp webhooks, local mig **087**, QA readiness evidence (no AWS apply).

**Deliverables:** `SECURITY_HARDENING_AND_VERIFICATION_REPORT.md`, `WHATSAPP_INTEGRATION_IMPLEMENTATION_REPORT.md`, `QA_DEPLOYMENT_READINESS_REPORT.md`, `BASIC_QA_TESTING_HANDOVER.md`.

**Code:** `record_durable_security_event` wired to auth login/refresh failures; `GET/POST /webhooks/whatsapp`; settings for Meta verify/secret.

**Tests:** Auth + WhatsApp webhook + catalog regressions **pass** (targeted). AWS deploy + QA RDS migration **not executed** (TEST-13 / ops).

---

## Session log — 2026-11-09 (approved 16 skeleton implementation)

**Requested:** Implement **16** skeletons after user-approved product decisions (API-08-005, API-13, API-14).

**Outcome:** **16/16 promoted**; inventory **228/228** `BACKEND_IMPLEMENTED`. Migrations **085–087**; routes and services for billing adjustments, reference data, audit governance; trusted client audit ingest returns **403**.

**Evidence:** [MASTER_16_SKELETON_IMPLEMENTATION_REPORT_2026-11-09.md](./evidence/MASTER_16_SKELETON_IMPLEMENTATION_REPORT_2026-11-09.md).

**Tests:** `contract_numbered_audit.py` **228/228**; unit tests for adjustment balance, client-ingest block, catalog GMD groups, reference aliases — **pass** (apply migrations before PG IV).

---

## Session log — 2026-11-09 (GHA QA deploy path)

**Scope:** GHA-only deploy; Terraform ownership split; `httpx` + FastAPI 0.109.1; Alembic guard **088**.

**Evidence:** [QA_GHA_DEPLOYMENT_EXECUTION_2026-11-09.md](./evidence/QA_GHA_DEPLOYMENT_EXECUTION_2026-11-09.md) — ECS **:15**, liveness **200**, digest `sha256:911b8f7d…`.

**Repos:** `release/qa-smoke-20261016` @ `602223f` / `9a12d4b`; infrastructure `02f520c` (+ IAM ListTasks applied).

---

## Session log — 2026-11-09 (final QA cutover)

**Scope:** Security completion, mig **088**, Terraform plan unblock, final evidence; **no** QA deploy / TEST-13 migration.

**Code:** `088_security_event_schema_align`; `SecurityEvent` timestamptz mapping; auth durable-event commit order; IAM `count` fix; `test_security_event_auth_digitize_postgres.py`.

**DB:** Local `digitize` @ **088**; `digitize_test` @ **083** (EQ-011 NOT READY).

**Tests:** Auth/audit/platform-admin PG batches **pass** (47+ targeted); pip-audit **153** vulns documented.

**Deliverables:** `FINAL_*` reports + `CONSOLIDATED_FINAL_QA_CUTOVER_REPORT.md`; handover **draft** until deploy.

**Verdict:** Cutover **not complete** — awaiting consolidated authorization (TEST-13 + terraform apply + ECS).

---

## Session log — 2026-11-04 (skeleton 24 implementation assessment)

**Requested:** Implement all 24 numbered skeleton operations (API-08×8, API-12-008, API-13×9, API-14×6).

**Outcome:** **0/24 promoted.** Per mandatory inspection, each operation remains gated by an **existing** product decision register, schema gap, or **Awaiting authorization** migration proposal. Implementing live routes without those gates would require inventing schema, client audit ingest (forbidden by [API-13 recommendation](../architecture/API-13_AUDIT_PRODUCT_DECISION.md)), or fake billing success responses (forbidden by engineering standards).

**Evidence:** [SKELETON_24_IMPLEMENTATION_ASSESSMENT_2026-11-04.md](./evidence/SKELETON_24_IMPLEMENTATION_ASSESSMENT_2026-11-04.md).

**Machine check:** `contract_numbered_audit.py` still reports **204** implemented / **24** skeleton.

**Next authorized slice (when product/migration gates close):** API-12-008 (DDL **072** + permission seed) or API-14 GMD seed migration — not started here.

---

Regenerate numbered matrix only:

```bash
cd digitize-services && poetry run python scripts/contract_numbered_audit.py
```

**Related canonical docs**

| Topic | Location | Decision state |
| --- | --- | --- |
| Comprehensive gap assessment | [DEV-20](./DEV-20_Comprehensive_Development_Gap_Assessment.md) | Assessment 2026-11-03 (read-only) |
| Gap register | [DEV-21](./DEV-21_Development_Gap_Register.md) | Working IDs / priorities |
| E2E journey matrix | [DEV-22](./DEV-22_End_to_End_Journey_Matrix.md) | Journey connectivity |
| Completion roadmap | [DEV-23](./DEV-23_Development_Completion_Roadmap.md) | Phased sequence (not an implementation auth) |
| QA readiness review | [TEST-12](../12_Testing/TEST-12_Engineering_Quality_QA_Readiness_Review_2026-11-02.md) | Findings register |
| EQ-011 `digitize_test` migration | [TEST-13](../12_Testing/TEST-13_EQ011_digitize_test_Migration_Authorization.md) | **Awaiting authorization** (proposal) |
| API-08 facility billing skeletons | [architecture/API-08_FACILITY_BILLING_DECISION_REGISTER.md](../architecture/API-08_FACILITY_BILLING_DECISION_REGISTER.md) | **Deferred by product decision** |
| API-12-008 escalate | [API-12_008_Escalate_Migration_Proposal.md](../07_API_Collections/API-12_008_Escalate_Migration_Proposal.md) | **Awaiting authorization** (proposal) |
| API-13 audit | [architecture/API-13_AUDIT_PRODUCT_DECISION.md](../architecture/API-13_AUDIT_PRODUCT_DECISION.md) | **Deferred by product decision** |
| API-14 reference | [architecture/API-14_REFERENCE_SOURCE_OF_TRUTH.md](../architecture/API-14_REFERENCE_SOURCE_OF_TRUTH.md) | **Deferred by product decision** |
| Org / Platform T&C management | [architecture/ORG_TERMS_MANAGEMENT_GAP_REGISTER.md](../architecture/ORG_TERMS_MANAGEMENT_GAP_REGISTER.md) | ORG-TERMS-002…006 **Implemented**; mig **072** applied on local `digitize`; reacceptance **Deferred by product decision** |

Regenerate machine counts:

```bash
cd digitize-services && poetry run python scripts/contract_numbered_audit.py
```

**Full-surface reconciliation (2026-11-04):** [API_INVENTORY_RECONCILIATION_2026-11-04.md](./evidence/API_INVENTORY_RECONCILIATION_2026-11-04.md) — **386** approved identities, **362** live HTTP v1, ORG-TERMS + onboarding verified in extras + runtime.

## Status vocabulary (use these labels)

| Label | Meaning |
| --- | --- |
| **Implemented** | Backend route registered and catalog `BACKEND_IMPLEMENTED` for that operation ID |
| **Tested** | Automated unit/contract/module tests pass in CI or local focused suite |
| **Integration-verified** | Live suite passed against an **authorized** target database / environment |
| **Blocked** | Cannot proceed until a technical prerequisite exists (schema, provider, env) |
| **Deferred by product decision** | Contract or behavior needs product approval before implementation |
| **Awaiting authorization** | Implementation/proposal ready; migration, DB, infra, or payment action not approved |

Do **not** mark EQ-011 as **Integration-verified** until the live test passes against authorized `digitize_test`.  
Do **not** infer completion from route registration or catalog metadata alone when claiming Flutter or integration readiness.

## Summary dashboard

| Collection | Backend (live / 228) | Flutter (evidence) | Primary gap |
| --- | ---: | --- | --- |
| API-01 Platform | 11/11 | **`platform_administration` console** + `platform_masterdata`, auth | Certification / integration gates |
| API-02 Org / Facility / Site | 20/20 | `organization`, `facility`, `branch` | Operational polish, media |
| API-03 Identity | 12/12 | Staff directory + **IAM activate/role/scopes/credential-reset/activity** | Directory paging lookup for details (no GET-by-id in 228) |
| API-04 Customer | 12/12 | `customer` remote + reg OTP extras | **COMPLETE WITH APPROVED BLOCKERS** — live SMS QA (GAP-API04-001 / GAP-INT-001); CRM PG IV (GAP-API04-002) **pass** |
| API-05 Membership | 12/12 | Plans + lifecycle + Flutter | List-by-customer **Deferred**; **PG IV PASS** (GAP-API05-005) |
| API-06 Attendance | **15/15** | Desk + reports + walk-in Flutter | OTP/QR provider **Blocked**; **PG IV PASS** (GAP-API06-003) |
| API-07 Training | 32/32 | **activity rules + customer progress UI** (GAP-API07-003 closed); enroll/remove + batch/PTR conflict UX | **GAP-API07-004 closed** (PG IV on `digitize`); list-enrollments / facility-conflict APIs deferred (GAP-API07-001/002); registry INTEGRATED/CERTIFIED + optional PG concurrency audit rows still open |
| API-08 Billing | **10/18** | History cancel payment/refund/invoice; outstanding collect/cancel | **GAP-API08-009 closed** (live `digitize` IV); 8 skeletons deferred/blocked per [decision register](../architecture/API-08_FACILITY_BILLING_DECISION_REGISTER.md) |
| API-09 Subscription | **24/24** | `saas_checkout`, `saas_invoice`, subscription-admin | Live Razorpay QA **Awaiting authorization**; cheque-bounce/grace automation + facility **proration** product-blocked; EQ-011 `digitize_test` IV separate |
| API-10 Notifications | **24/24** | `in_app_notifications`, push scaffold | Provider QA only |
| API-11 Reports | 12/12 | `reporting` | External schedule delivery |
| API-12 Support | 11/12 | `support_tickets`, help center | **API-12-008** DB gap |
| API-13 Audit | **3/12** | **Audit events page** (list/analytics/export) | Capture POSTs / schema gaps deferred |
| API-14 Reference | **6/12** | Facility types via extras; numbered aliases live | Geo / i18n / activity lists |

**Extras (outside 228):** **158** catalogued `EXTRA_OPERATIONS` — **156** additional approved product routes + **2** OPS health probes; all **158** registered. Includes **ORG-TERMS-001…006** (6) and **ORG-ONBOARDING-ACCEPT-001** (1). Do **not** report **228+6=234** as total product APIs (ignores other extras). See [API_CONTRACT_REGISTRY](../architecture/API_CONTRACT_REGISTRY.md) § inventory reconciliation.

---

**Backend totals:** **204** `BACKEND_IMPLEMENTED`, **24** `SKELETON_CREATED` (recalculated 2026-11-02 finalization; **reconfirmed 2026-11-03** inventory reconciliation via `numbered_contracts()` + live route set — see session log below).

> Cross-product gap analysis and prioritized roadmap live in **DEV-20…DEV-23**. This DEV-19 file remains the chronological implementation evidence tracker; do not treat DEV-20 as overwriting session history below.

**EQ-011:** Test **Implemented** + **Tested** (skip without live flag); live run **Blocked** / **Awaiting authorization**. `digitize_test` Alembic **`036`**; head **`071`**. Plan: [TEST-13](../12_Testing/TEST-13_EQ011_digitize_test_Migration_Authorization.md). Preflight (services): `scripts/eq011_digitize_test_preflight.py`.

**API-10:** **24/24 Implemented** (provider QA remains external).

---

## Remaining skeletons (24) — status classes

Merged from former `digitize-services/docs/REMAINING_SKELETON_PRODUCT_DECISIONS.md` (that file is now a pointer).

| Group | Ops | Class | Canonical decision doc |
| --- | --- | --- | --- |
| API-08 | 002, 003, 004, 005, 007, 009, 012, 014 | Deferred / Blocked (schema) / Awaiting authorization | [API-08 facility billing register](../architecture/API-08_FACILITY_BILLING_DECISION_REGISTER.md) |
| API-12 | 008 | Awaiting authorization (migration proposal) | [API-12-008 escalate proposal](../07_API_Collections/API-12_008_Escalate_Migration_Proposal.md) |
| API-13 | 001–004, 006–008, 010–011 | Deferred by product decision / Blocked (schema) | [API-13 audit decision](../architecture/API-13_AUDIT_PRODUCT_DECISION.md) |
| API-14 | 001, 002, 004, 005, 007, 012 | Deferred by product decision (GMD seeds) | [API-14 source of truth](../architecture/API-14_REFERENCE_SOURCE_OF_TRUTH.md) |

---

## Session log — 2026-11-02 (EQ-011 preflight + API-13/08 Flutter readiness)

### Part A — EQ-011 preflight (read-only)

- Re-ran `eq011_digitize_test_preflight.py` + `alembic current` / `heads`.
- Confirmed `digitize_test` at **036**, head **071**, 36 upgrade twins present, **no** DROP/TRUNCATE/DELETE/DROP COLUMN in 037–071 SQL.
- `display_name_ciphertext` still absent; addressed by **043** within the recommended **upgrade head** chain.
- EQ-011 remains **Blocked** / **Awaiting authorization** / **not** integration-verified.
- Canonical auth plan updated: [TEST-13](../12_Testing/TEST-13_EQ011_digitize_test_Migration_Authorization.md).

### Part B — API-13 Flutter vs contract

| Finding | Action |
| --- | --- |
| Paths/ops map to API-13-005/009/012 | Confirmed |
| Export catalog success **202** vs route **201** | Backend route aligned to **202** (contract preserved) |
| Optional `occurred_from` / `occurred_to` / `entity_id` not wired in Flutter | Added to repository, controller, page + widget test |
| Org scope + `report.view` | Unchanged; correct |
| Live DB integration | **Not claimed** |

### Part C — API-08-015 Flutter cancel PENDING

- Wired `payment_id` on billing history entries + cancel action for `PENDING` only (backend already Implemented/Tested).
- Offline SUCCESS payments remain refund-path only (no invented cancel of SUCCESS).

---

## Session log — 2026-11-02 (registry sync + API-13 Flutter audit)

### Registry synchronization (`API_CONTRACT_REGISTRY.md`)

- Preserved freeze inventory **228** and historical gate snapshot **173 / 55**.
- Added dated **current** counts **204 / 24** from `contract_numbered_audit.py`.
- Refreshed per-row backend_status column only (138 were stale `SKELETON_CREATED` → `BACKEND_IMPLEMENTED`).
- Updated §5.1 runtime ownership narrative and facility-types alias note for API-14-006.
- Contracts, paths, auth rules, and semantics unchanged.

### E2E gap closed — API-13 Phase 1 reads (Flutter)

| Op | Backend | Flutter | Tests | Status labels |
| --- | --- | --- | --- | --- |
| API-13-005 list | Implemented | `AuditEventsPage` remote list | Widget + existing backend service tests | **Implemented** + **Tested** (not integration-verified) |
| API-13-009 export | Implemented | Export JSON action | Widget | **Implemented** + **Tested** |
| API-13-012 analytics | Implemented | Analytics card | Widget | **Implemented** + **Tested** |

Evidence: `digitize-ui/lib/features/audit/**`, `test/features/audit/audit_events_page_test.dart` (**3 passed**); `pytest tests/audit/test_audit_read_service.py tests/api/test_contract_registry.py` (**25 passed**). Permission: `report.view`. No schema/migration. Capture POSTs remain **Deferred by product decision**.

### Still blocked / deferred (unchanged)

- EQ-011 live: **Awaiting authorization** (`digitize_test` 036→071).
- API-08 / API-12-008 / remaining API-13 / API-14 skeletons: product or migration gates.

---

## Session log — 2026-11-02 (documentation consolidation)

- Canonical home moved to this DEV-19 document in the documentation repository.
- Decision packs relocated under `architecture/`, `07_API_Collections/`, and `12_Testing/` (see Related table).
- Inventory unchanged: **204 / 24 / 228**. No migrations, code, or infra changes in the consolidation pass.

---

## Session log — 2026-11-02 (finalization / authorization readiness)

### Safe work completed

| Item | Evidence |
| --- | --- |
| Recalculated inventory | **204 / 24 / 228** |
| Read-only `digitize_test` probe | Current rev **036**; missing `display_name_ciphertext`; catalogs present |
| EQ-011 auth plan | [TEST-13](../12_Testing/TEST-13_EQ011_digitize_test_Migration_Authorization.md) — recommend upgrade **to head 071**, not stop at 043 |
| Preflight script | `digitize-services/scripts/eq011_digitize_test_preflight.py` (read-only; refuses non-`digitize_test`) |
| API-13 / 14 / 08 / 12-008 decision docs | Canonical paths in Related table; no contract invention; no DDL applied |

### Tests

| Suite | Result |
| --- | --- |
| `DB_NAME=digitize_test PGDATABASE=digitize_test poetry run python scripts/eq011_digitize_test_preflight.py` | Exit **1** NOT READY — rev `036`, missing ciphertext; expected until migration auth |
| `pytest tests/api/test_contract_registry.py tests/api/test_module_routes.py tests/organization/test_eq011_onboarding_auth_e2e.py -q` | **36 passed, 1 skipped** |
| `poetry run python scripts/contract_numbered_audit.py` | **228** rows; **204** BACKEND / **24** SKELETON |

---

## Session log — 2026-11-02 (multi-workstream completion pass)

### Inventory delta

| Metric | Before this pass | After |
| --- | ---: | ---: |
| Implemented | 192 (recalculated; tracker had 188) | **204** |
| Skeleton | 36 | **24** |
| Total | 228 | **228** |

### Completed — API-08 (3)

| ID | Op | Notes |
| --- | --- | --- |
| API-08-008 | `POST /payments` | Alias of offline collect (`OfflinePaymentService`) |
| API-08-015 | `POST /payments/{id}/cancel` | PENDING → FAILED only; SUCCESS must use refund |
| API-08-017 | `GET /commercial/reports` | Alias of API-11 revenue (`ReportingService`) |

**Deferred (schema/product):** charges calc, discounts, taxes calc, adjustments, credit notes (DB gap), online payments, receipts, reconciliations.

### Completed — API-13 (3)

| ID | Op | Notes |
| --- | --- | --- |
| API-13-005 | `GET /audit-events` | Org-scoped read of `audit.audit_event` |
| API-13-009 | `POST /audit-events/export` | Sync JSON export (first page) |
| API-13-012 | `GET /audit-analytics` | Counts by action / entity_type |

**Permission alias:** `report.view` (no new permission migration). Capture POSTs / investigations / compliance / policies remain blocked.

### Completed — API-14 (6)

| ID | Op | Notes |
| --- | --- | --- |
| API-14-003 | currencies | GMD `CURRENCY` (+ tenant-readable expansion) |
| API-14-006 | facility-types | Alias of `GET /facility-types` |
| API-14-008 | status-values | GMD `STATUS` |
| API-14-009 | payment-methods | App constants `APPROVED_OFFLINE_PAYMENT_METHODS` |
| API-14-010 | communication-channels | App constants `APPROVED_CHANNEL_CODES` |
| API-14-011 | lookup-values/{group} | Approved GMD groups only |

### API-10

Confirmed **24/24** live (tracker “21/24” was stale). No code change this pass.

### API-12-008

Still **blocked-schema**. Proposal: [API-12_008_Escalate_Migration_Proposal.md](../07_API_Collections/API-12_008_Escalate_Migration_Proposal.md) (not applied).

### Flutter

No UI changes required: membership already uses offline payment; reporting covers revenue; reference/audit screens not required for alias completeness.

### Tests (this pass)

| Suite | Result |
| --- | --- |
| `pytest tests/billing/test_payment_collect_cancel.py tests/audit/test_audit_read_service.py tests/api/test_reference_aliases.py tests/api/test_contract_registry.py tests/api/test_module_routes.py tests/billing/test_facility_membership_billing.py tests/billing/test_refund_service.py -q` | **63 passed** |
| `poetry run python scripts/contract_numbered_audit.py` | **204 / 24 / 228** |

---

## Session log — 2026-11-02 (EQ-011 onboarding auth E2E)

### Completed — EQ-011 test implementation

| Item | Detail |
| --- | --- |
| **Test module** | `tests/organization/test_eq011_onboarding_auth_e2e.py` |
| **Flow** | Platform `POST /organizations` (+ `organization_admin`) → memory `credential_setup` email → parse setup URL token → `POST /auth/password-reset/confirm` → `POST /auth/login` → OA views PENDING org; `POST /sites` and `POST /identity/staff-accounts` rejected while org inactive |
| **Opt-in** | `DIGITIZE_API_TEST=1`, `DB_NAME=digitize_test` per `live_db_guard` (not `digitize` / `digitize_mig_cold`) |
| **Production code** | None (test-only) |

### Tests (EQ-011 batch)

| Suite | Result (this session) |
| --- | --- |
| `pytest tests/organization/test_eq011_onboarding_auth_e2e.py -q` | **1 skipped** (no `DIGITIZE_API_TEST`) |
| `DIGITIZE_API_TEST=1 DB_NAME=digitize_test pytest tests/organization/test_eq011_onboarding_auth_e2e.py -q` | **1 error** at setup — `digitize_test` missing `identity.user_account.display_name_ciphertext` (need migration **043_identity_staff_pii_encryption** and current integration catalog) |
| `pytest tests/organization/test_onboarding_review.py tests/identity/test_credential_provisioning.py tests/authentication/test_auth_api.py tests/api/test_contract_registry.py -q` | **40 passed**, **19 skipped** |
| `poetry run python scripts/contract_numbered_audit.py` | **228** ops; **188** implemented / **40** skeleton |

**Status:** Test **implemented**; live **PASS blocked** locally until `digitize_test` is migrated through ≥043 (and live guard catalog seeds).

---

## Session log — 2026-11-02 (API-06 session, update, reports, walk-in identify)

### Completed — API-06 skeleton operations (4)

| ID | Operation | Backend | Notes |
| --- | --- | --- | --- |
| API-06-003 | POST `/attendance/session` | Live | Phase 1 alias of membership `check_in` (`AttendanceCheckIn` + Idempotency-Key) |
| API-06-006 | PATCH `/attendance/{id}` | Live | Staff remarks via `AttendanceUpdate`; `If-Match`; allowed from CHECKED_IN / CHECKED_OUT |
| API-06-009 | GET `/attendance/reports` | Live | Org/facility/site scoped status counts + optional `present_checkins` in date window |
| API-06-011 | POST `/walkin-visits/identify` | Live | Resolve ACTIVE customer + optional open visit; not registration |

**Flutter:** Unchanged — existing attendance / walk-in flows already use check-in and visit create paths.

### Tests (API-06 batch)

| Suite | Result |
| --- | --- |
| `pytest tests/attendance/test_attendance_service.py tests/api/test_contract_registry.py -q` | **61 passed** |
| `pytest tests/attendance/ -q` | **117 passed** |

---

## Session log — 2026-11-02 (API-09 renewal & facility subscription)

### Completed — API-09 skeleton operations (8)

| ID | Operation | Backend | Notes |
| --- | --- | --- | --- |
| API-09-004 | POST `/subscriptions/{id}/renew` | Live | Extends `ends_at` by annual period; **ACTIVE** or **EXPIRED** only |
| API-09-005 | POST `.../upgrade` | Live | Active plan change |
| API-09-006 | POST `.../downgrade` | Live | Same validation as upgrade |
| API-09-010 | POST `.../renewal-invoices` | Live | `SaasInvoiceService.issue` |
| API-09-012 | GET `/subscriptions/reports` | Live | Status counts by org/facility |
| API-09-016 | POST `/licenses/{id}/renew` | Live | Extends license; syncs subscription `ends_at` |
| API-09-023 | GET `/licenses/{id}/history` | Live | Linked subscription lifecycle history |
| API-09-024 | GET `/licenses/reports` | Live | License status counts |

**Business rules (Phase 1):** Renew extends facility subscription window (365-day annual default). EXPIRED renew reactivates subscription, license, and facility scope. SUSPENDED must reactivate before renew. Installment/discount/cheque policies stay in SaaS commerce extras. Catalog `subscription.renew` / `license.renew` alias to seeded permissions (`subscription.activate`, `license.activate`).

**Flutter:** Unchanged — `saas_checkout` / `saas_invoice` for tenant checkout; numbered API-09 ops are backend lifecycle.

### Tests (API-09 batch)

| Suite | Result |
| --- | --- |
| `pytest tests/subscription/test_subscription_renewal_lifecycle.py tests/subscription/test_subscription_renew_service.py tests/api/test_contract_registry.py tests/subscription/test_helpers.py -q` | **31 passed** |
| Live `test_subscription_license.py` | **Not run** |

---

## Session log — 2026-11-02 (API-08-018)

### Completed — API-08-018

| Item | Evidence |
| --- | --- |
| **API-08-018** GET `/api/v1/billing/outstanding-statements` | `OutstandingStatementsService`, `invoice_balance.py`, `billing/routes.py`, catalog `billing_outstanding_statements_list` |
| **Flutter outstanding statements** | `OrganizationBillingPage` panel (`FacilityOutstandingStatementsPanel`) |
| **Contract verified** | Collection permission name `generate.outstanding.statement`; runtime alias `billing.payment.offline.record` (migration 063), same as history |

**Financial rules (Phase 1, no new ledger):**

- Per-invoice **outstanding** = `invoice_total − (SUCCESS payments − SUCCESS refunds on those payments)`, floored at zero.
- **DRAFT** and **CANCELLED** invoices excluded from the query.
- Rows included only when computed outstanding **> 0** (covers **ISSUED** unpaid invoices and **PAID** invoices with partial refunds that restore receivable).
- **Ambiguity documented:** aggregate helper `outstanding_issued()` in reporting sums full **ISSUED** invoice totals only (not payment-adjusted). This endpoint uses payment/refund-adjusted balances, aligned with SaaS commerce `outstanding_amount` pattern and Phase 1 payment/refund services—not the reporting aggregate.

**Query contract (implemented):** Same filters as API-08-016: `organization_id` (required), optional `facility_id`, `invoice_status`, `invoice_date_from`, `invoice_date_to`, API-00 pagination. Order `invoice_date DESC`, `invoice_id DESC`.

### Tests executed (API-08-018 batch)

| Suite | Result |
| --- | --- |
| `pytest tests/billing/test_invoice_balance.py tests/billing/test_outstanding_statements.py tests/billing/test_billing_history.py tests/api/test_contract_registry.py -q` | **34 passed** |
| `flutter test test/features/organization/facility_outstanding_statements_controller_test.dart` | **3 passed** |

### Files touched (API-08-018)

- `app/modules/billing/invoice_balance.py`, `outstanding_statements_service.py`, `repository.py`, `routes.py`, `schemas.py`, `constants.py`
- `tests/billing/test_invoice_balance.py`, `tests/billing/test_outstanding_statements.py`
- `app/api/contracts/catalog.py`, `var/api_audit_matrix.csv`
- `digitize-ui/lib/features/organization/domain|data|application|presentation/...` (outstanding repo, controller, panel, billing page)
- `digitize-ui/test/features/organization/facility_outstanding_statements_controller_test.dart`

**Limitations:** Live data requires migration **063**; no Postgres HTTP integration test in this batch; dedicated `generate.outstanding.statement` DB permission not seeded (aliased like history).

---

## Session log — 2026-11-02 (continued)

### Completed — API-08-016

| Item | Evidence |
| --- | --- |
| **API-08-016** GET `/api/v1/billing/history` | `BillingHistoryService`, `billing/routes.py`, catalog `billing_history_list` |
| **Flutter billing history** | Org dashboard Payments feed + `OrganizationBillingPage` panel |
| **Contract verified** | Collection: `view.billing.and.payment.history`; runtime permission `billing.payment.offline.record` (migration 063) |

**Query contract (implemented):** `organization_id` (required), optional `facility_id`, `invoice_status`, `invoice_date_from`, `invoice_date_to`, `page`, `page_size` (API-00 offset pagination). Response: list of invoice rows with latest successful payment snapshot; order `created_at DESC`, `invoice_id DESC`.

### Tests executed (API-08-016 batch)

| Suite | Result |
| --- | --- |
| `pytest tests/billing/test_billing_history.py tests/billing/test_facility_membership_billing.py tests/api/test_contract_registry.py -q` | **34 passed** |
| `flutter test test/features/organization/facility_billing_history_controller_test.dart` | **3 passed** |

### Files touched (API-08-016)

- `app/modules/billing/billing_history_service.py`, `repository.py`, `routes.py`, `schemas.py`, `constants.py`
- `tests/billing/test_billing_history.py`
- `app/api/contracts/catalog.py`
- `digitize-ui/lib/features/organization/domain|data|application|presentation/...` (history repo, controller, panel, dashboard, billing page)
- `digitize-ui/test/features/organization/facility_billing_history_controller_test.dart`

**Limitations:** Live data requires migration **063** applied; catalog permission name `view.billing.and.payment.history` is not a separate DB permission yet (aliased to `billing.payment.offline.record`). No HTTP integration test against Postgres in this batch.

---

## Session log — 2026-11-02 (earlier)

### Completed

| Item | Evidence |
| --- | --- |
| **API-08-011** GET `/api/v1/payments/{payment_id}/status` | `billing/routes.py`, `PaymentStatusService`, catalog + tests |
| **Flutter API-08-011** | `verifyPaymentStatus` in customer membership repo + activate flow |
| **EQ-009** Org create success copy | `organization_form_page.dart` setup-email toast |
| Prior review fixes | EQ-001…EQ-005 (see engineering-quality report) |

### Tests executed

| Suite | Result |
| --- | --- |
| `pytest tests/billing/test_facility_membership_billing.py tests/api/test_contract_registry.py -q` | **29 passed** |
| `pytest tests/identity/test_credential_provisioning.py -q` | **6 passed** (prior batch) |
| `flutter test test/features/authentication/auth_contract_test.dart` | **5 passed** (prior batch) |

### Files touched (this session)

- `app/modules/billing/*` (status service, route, schemas, repository, constants)
- `app/api/contracts/catalog.py`
- `tests/billing/test_facility_membership_billing.py`
- `digitize-ui/.../organization_form_page.dart`
- Formerly `digitize-services/docs/FEATURE_COMPLETION_TRACKER.md` — canonical location is this DEV-19 file

---

## Module detail (acceptance-oriented)

### API-08 Billing / Payment

| ID | Operation | Backend | Flutter | Tests | Notes |
| --- | --- | --- | --- | --- | --- |
| API-08-001 | POST `/invoices` | Live | Customer membership flow | `test_facility_membership_billing` | Requires migration 063 in target DB |
| API-08-006 | POST `/invoices/{id}/cancel` | Live | **History + outstanding Cancel invoice** | membership billing cancel tests + Flutter controller tests | `billing.invoice.generate`; ISSUED + no SUCCESS payment |
| API-08-010 | POST `/payments/offline` | Live | **Membership + outstanding Collect** | Same + outstanding controller tests | Idempotency required |
| API-08-011 | GET `/payments/{id}/status` | Live | Customer membership verify | `test_payment_status_*` | Permission aliases to `billing.payment.offline.record` |
| API-08-016 | GET `/billing/history` | **Live (2026-11-02)** / enriched **2026-11-03** | **Dashboard + billing page + status filter** | `test_billing_history.py` | Additive `refunded_amount` / `refundable_balance`; invoice_status filter in UI |
| API-08-018 | GET `/billing/outstanding-statements` | **Live (2026-11-02)** | **Billing page + Collect/Cancel** | `test_outstanding_statements.py`, `test_invoice_balance.py` | Payment/refund-adjusted receivable; pagination |
| API-08-013 | POST `/payments/{id}/refunds` | Live | **Billing history Refund** | `tests/billing/test_refund*` + Flutter controller tests | Permission `billing.refund.process`; reporting flag stays off |
| API-08-008 | POST `/payments` | **Live (2026-11-02)** | Offline path | `test_payment_collect_cancel` | Alias of offline collect |
| API-08-015 | POST `/payments/{id}/cancel` | **Live (2026-11-02)** | **Billing history** | `test_payment_collect_cancel` + Flutter | PENDING only |
| API-08-017 | GET `/commercial/reports` | **Live (2026-11-02)** | Reporting UI | contract + revenue reuse | Alias of API-11 revenue |
| API-08-002…005, 007, 009, 012, 014 | Various | Skeleton | Partial / none | Placeholder | See [API-08 facility billing register](../architecture/API-08_FACILITY_BILLING_DECISION_REGISTER.md) |

**Acceptance (Phase 1 slice):** Org staff can list facility billing history, create membership invoice, record offline payment, verify status, activate membership, collect from outstanding, refund SUCCESS payments, and cancel unpaid ISSUED invoices — backend yes; Flutter **Implemented** / **Tested** (controller unit); **not Integration-verified**.

**Blockers:** DB migration 063/069 not applied without authorization; dedicated `view.billing.and.payment.history` permission seed optional future migration. History list now exposes additive `refunded_amount` / `refundable_balance` (same computation as API-08-011); Flutter hides Refund when remaining balance is zero.

### API-06 Attendance

**Status:** **15/15 live** (2026-11-02). Former skeletons API-06-003, -006, -009, -011 implemented per Phase 1 contracts (session = check-in pipeline; reports = scoped aggregates, not API-11 engine). Flutter Attendance Desk reports panel (**API-06-009**) **Implemented** / **Tested** 2026-11-03.

### API-13 / API-14

**API-13:** 3/12 **Implemented** (`GET /audit-events`, export, analytics). Flutter **Tested** via `AuditEventsPage` (not integration-verified). Capture POSTs and compliance/schema ops **Deferred / Blocked** — [API-13 decision](../architecture/API-13_AUDIT_PRODUCT_DECISION.md).  
**API-14:** 6/12 **Implemented** (facility-types, currencies, status, payment-methods, channels, lookup-values). Geo/i18n/activity/localization **Deferred** — [API-14 SoT](../architecture/API-14_REFERENCE_SOURCE_OF_TRUTH.md).

### API-12 Support

| ID | Status |
| --- | --- |
| API-12-001…007, 009…012 | Backend live |
| API-12-008 | Skeleton — **DATABASE GAP**; proposal [API-12-008](../07_API_Collections/API-12_008_Escalate_Migration_Proposal.md) (**Awaiting authorization**) |

Flutter: support tickets, conversations, help center present; integration tests under `test/features/support_*`.

---

## Flutter integration matrix (high level)

| Feature folder | Remote API | Mock fallback |
| --- | --- | --- |
| organization | Always remote | No |
| staff | Remote when `DIGITIZE_REMOTE` | Mock in dev |
| membership_plan | Remote | Mock |
| customer + membership billing | Remote | Partial mocks |
| attendance / walk-in | Remote | Mock |
| saas_checkout / saas_invoice | Remote | Tests |
| reporting | Remote | — |
| push_notifications | FCM when configured | Disabled without Firebase |
| facility billing history | **Remote** (`/billing/history` + payment cancel/refund + invoice cancel) | N/A |
| facility outstanding statements | **Remote** (list + Collect offline + Cancel invoice) | N/A |

---

## External dependencies (not product code)

| Need | Owner action |
| --- | --- |
| RDS migrations 031–071 | DBA / authorized migration run |
| SES SMTP QA | Secrets + domain verification |
| SMS / WhatsApp / FCM QA | Provider accounts (see [TEST-12](../12_Testing/TEST-12_Engineering_Quality_QA_Readiness_Review_2026-11-02.md) §E) |
| Razorpay live webhooks | QA URL + secret in SM |

---

## Next implementation tasks (ordered)

1. ~~**API-08-016** GET `/billing/history`~~ **Done 2026-11-02**.
2. ~~**API-09** skeleton renew / facility subscription ops~~ **Done 2026-11-02** (API-09 **24/24**).
3. ~~**API-06** resolve session/report skeletons vs live attendance routes~~ **Done 2026-11-02** (API-06 **15/15**).
4. ~~**EQ-011** test file~~ **Implemented** / **Tested**; live **Blocked** / **Awaiting authorization** (`digitize_test` **036→071** per [TEST-13](../12_Testing/TEST-13_EQ011_digitize_test_Migration_Authorization.md)).
5. ~~**Safe API-08 / API-13 / API-14 aliases**~~ **Done 2026-11-02** (inventory **204/228**).
6. **Authorize** `digitize_test` `alembic upgrade head` (036→071) per [TEST-13](../12_Testing/TEST-13_EQ011_digitize_test_Migration_Authorization.md); re-run EQ-011 live.
7. **Approve** API-13 capture-POST stance + API-14 GMD seed set ([API-13](../architecture/API-13_AUDIT_PRODUCT_DECISION.md), [API-14](../architecture/API-14_REFERENCE_SOURCE_OF_TRUTH.md)).
8. **Authorize** API-12-008 escalate migration ([proposal](../07_API_Collections/API-12_008_Escalate_Migration_Proposal.md)) and/or API-08 schema slices ([billing register](../architecture/API-08_FACILITY_BILLING_DECISION_REGISTER.md)).
9. ~~**Flutter API-13 Phase 1 audit reads**~~ **Done 2026-11-02** (widget-tested; live DB integration not claimed).
10. ~~**API-13 export 202 + date/entity filters; API-08-015 Flutter cancel PENDING**~~ **Done 2026-11-02** (widget/unit tested; not integration-verified).
11. ~~**Outstanding Collect payment (API-08-018 → API-08-010)**~~ **Done 2026-11-02** (Flutter **Implemented** / **Tested**; backend unchanged; not integration-verified).
12. ~~**Flutter refunds UI (API-08-013)**~~ **Done 2026-11-02** (billing history; **Implemented** / **Tested**; not integration-verified).
13. ~~**Invoice cancel UI (API-08-006)**~~ **Done 2026-11-03** (history + outstanding; **Implemented** / **Tested**; not integration-verified).
14. ~~**Membership freeze/cancel (known membership)**~~ **Done 2026-11-03** (Flutter **Implemented** / **Tested**; list-by-customer still **Deferred by product decision**).
15. ~~**Attendance Desk reports (API-06-009)**~~ **Done 2026-11-03** (Flutter **Implemented** / **Tested**; not integration-verified).
16. ~~**Batch enroll/remove (API-07-018/019)**~~ **Done 2026-11-03** (Flutter **Implemented** / **Tested**; session-known IDs only; not integration-verified).
17. ~~**Batch schedule conflict UX (BR-TRN-005/008)**~~ **Done 2026-11-03** (Flutter **Implemented** / **Tested**; uses existing 409/422 responses; not integration-verified).
18. ~~**PTR schedule conflict UX parity**~~ **Done 2026-11-03** (book / reschedule / assign; Flutter **Implemented** / **Tested**; not integration-verified).
19. ~~**Org Admin T&C acceptance UX + integrity hash**~~ **Done 2026-11-03** (Flutter **Implemented** / **Tested**; backend content_hash additive on extras; mig **072** authored unapplied; PA CMS **Blocked**).
20. ~~**DEV-23 Phase 1 — Attendance shell + IAM Flutter + Site Admin nav**~~ **Done 2026-11-03** (Flutter **Implemented** / focused checks; not integration-verified).
21. ~~**Membership renew/upgrade/downgrade UI (GAP-API05-002)**~~ **Done 2026-11-03** (Flutter **Implemented** / focused checks; invoice create allowed for ACTIVE commercial changes; not integration-verified).
22. ~~**API-08 history refundable UX + invoice status filter**~~ **Done 2026-11-03** (API-08-016 additive fields + Flutter filter/eligibility; **Implemented** / **Tested**; not integration-verified).
23. ~~**Next slice (recommended):** Continue approved API-08 unblocked workflows (e.g. outstanding invoice_status filter parity if needed) or DEV-23 Phase 2 / GAP-API05-003.~~ **Done 2026-11-03** (outstanding `invoice_status` filter parity + GAP-API05-003 transfer/expire Flutter; **Implemented** / **Tested**; not integration-verified).
24. ~~**GAP-API01-001** Platform Admin console (API-01 settings/health/ops)~~ **Done 2026-11-03** (`/platform/console`; **Implemented** / **Tested**; not integration-verified).
25. ~~**GAP-API10-003** campaign admin Flutter (Stage 1 manual/external)~~ **Done 2026-11-03** (`/campaigns`; **Implemented** / **Tested**; Stages 2–3 architecture doc only; not integration-verified).
26. ~~**GAP-API06-002** session remarks UI~~ **Done 2026-11-03** (desk PATCH remarks + audit trail panel; **Implemented** / **Tested**; not integration-verified).
27. ~~**GAP-API10-003** staff notification admin Flutter~~ **Done 2026-11-03** (`/staff-notifications`; **Implemented** / **Tested**; send/deliver/retry not exposed; not integration-verified).
28. ~~**GAP-API10-005** inbox vs staff API-10 surface~~ **Done 2026-11-03** (route guards, labels, `/me/notifications` alias; **Implemented** / **Tested**; not integration-verified).
29. ~~**GAP-API09-001** numbered subscription/license admin Flutter~~ **Done 2026-11-03** (`/organization/subscription-admin`; **Implemented** / **Tested**; not integration-verified).
30. ~~**GAP-ROLE-003** Platform Admin audit navigation visibility~~ **Done 2026-11-03** (sidebar + PA org scope via query; **Implemented** / **Tested**; not integration-verified).
31. ~~**GAP-API11-002** Reporting PDF export limitation (Flutter clarity)~~ **Done 2026-11-03** (**Implemented** / **Tested**; not integration-verified).
32. ~~**GAP-API11-003** API-11 reporting live certification~~ **Partial 2026-11-03** (local `digitize` ASGI; HTTP export 404 was **certification harness** — fixed; see evidence + `test_reports_export_http_digitize.py`).
33. ~~**AUDIT-TXN-2026-11-03** Cross-module DB transaction safety audit (API-01…API-14)~~ **Done 2026-11-03** (read-only; evidence `docs/16_Development_Readiness/evidence/AUDIT-TXN-2026-11-03_summary.md`; gaps **GAP-TXN-001…005** in DEV-21).
34. ~~**GAP-TXN-001** API-08-010 offline payment invoice lock~~ **Done 2026-11-03** (Implemented + unit-tested + local `digitize` PG concurrency; not full GAP-TXN-004 IV).
35. ~~**GAP-TXN-002** Test harness `get_session` / UoW lifecycle standardization~~ **Done 2026-11-03** (`tests/api/asgi_session_helpers.py`, `test_get_session_uow_lifecycle.py`, override inventory evidence).
36. ~~**GAP-TXN-003** Identity post-commit email consistency~~ **Done 2026-11-03** (outbox/reset sync on delivery outcome; `test_credential_email_txn003.py`; re-provision recovery path).
37. ~~**GAP-TXN-004** Database concurrency integration matrix~~ **Done 2026-11-03** (refund + webhook PG IV on `digitize`; matrix + `DIGITIZE_TXN004_PG_TEST`; webhook unique-violation fix).
38. ~~**GAP-TXN-005** Retired scaffold self-commit~~ **Done 2026-11-03** (`UserRepository.create` flush-only; `test_gap_txn005_scaffold.py`).
39. ~~**Next slice (recommended):** Advanced Reporting export-byte IV (requires Advanced Reporting entitlement on test org), or provider QA (Phase 2), or activity rules / customer progress UI (remaining GAP-API07-003).~~ **Done 2026-11-03** — export-byte IV on local `digitize`; API-13/12/04 PG IV suites (see session log below).
40. **Next slice (recommended):** Phase 2 provider QA (SMS/Razorpay/live) or authorized gates (EQ-011 `digitize_test`, API-12-008 migrate) — no further authorized core API/Flutter slices without product decisions.

---

## Session log — 2026-11-03 (Org T&C acceptance UX + terms document prep)

### Existing implementation discovered
- Hardcoded published doc v`1.0` in `organization/terms.py`
- Extras: `GET /api/v1/terms/current`, `POST .../onboarding/accept` (outside 228)
- Acceptance in org `metadata.onboarding` + audit `ORGANIZATION_TERMS_ACCEPTED`
- Flutter OA onboarding review page already had basic checkbox/accept
- **No** PA draft/publish/history APIs or UI; **no** terms DB table before this session

### Implemented this session
| Area | Change | Label |
| --- | --- | --- |
| Backend current terms | Additive `content_hash` (SHA-256) on GET current | **Implemented** / **Tested** |
| Backend accept | Optional `content_hash` validation; store hash in metadata + audit | **Implemented** / **Tested** |
| Migration `072_platform_terms_document` | `platform.terms_document` + model | **Awaiting authorization** (unapplied at end of that slice) |
| PA management APIs / UI | Not built | **Blocked** (see gap register) |
| OA Flutter UX | Scrollable full content; required checkbox wording; Accept and Continue gating; empty/error/loading; stale-version reload + checkbox reset; submit busy guard; sends version + hash | **Implemented** / **Tested** |
| Reacceptance for existing orgs | Not invented | **Deferred by product decision** |
| Live E2E | — | **Not Integration-verified** |

### Focused checks
- `pytest tests/organization/test_onboarding_review.py` — **12 passed**
- `flutter test test/features/organization/organization_onboarding_terms_test.dart` — **4 passed**

### Proposed next (authorization required)
Approve ExtraOperations ORG-TERMS-002…006 and apply mig **072** before Platform Admin CMS and DB-backed current document retrieval.

---

## Session log — 2026-11-03 (ORG-TERMS-002…006 + mig 072 + PA CMS)

### Decisions applied
- Product approved ORG-TERMS-002…006 as **additional** management operations (228 inventory unchanged).
- Migration **072** authorized for existing **`digitize`** database only (seeded published v1.0).
- Mandatory reacceptance for existing organizations remains **Deferred by product decision**.
- Onboarding T&C stays separate from SaaS commercial terms.

### Implemented
| Area | Change | Label |
| --- | --- | --- |
| Mig 072 | Table + unique one-PUBLISHED index + seed v1.0; applied on local `digitize` @ localhost:5434 | **Implemented** (local DB) |
| ORG-TERMS-002…006 | List/create/patch/publish/get with Platform Admin perms + audit | **Implemented** |
| ORG-TERMS-001 | `GET /terms/current` reads PUBLISHED row from DB | **Implemented** |
| Accept integrity | Accept binds to DB published version + hash; idempotent reaccept for same version | **Implemented** |
| PA Flutter CMS | `/platform/terms` list/draft/preview/publish/history | **Implemented** |
| OA Flutter | Preserved prior acceptance UX | **Implemented** / **Tested** (prior suite) |
| Reacceptance | Not forced on publish | **Deferred by product decision** |
| Live shared-env E2E | — | **Not Integration-verified** |

### Focused checks (this slice)
- `pytest tests/organization/test_onboarding_review.py` + contract/extras uniqueness + OpenAPI live routes — **15 passed**
- DB smoke against local `digitize`: `GET` current + list published v1.0 — **ok**
- `flutter test test/features/organization/organization_onboarding_terms_test.dart` — **4 passed**
- `dart analyze` on new T&C pages / repository — no new errors (pre-existing unused locals in `app_shell.dart`)

### Notes
Gap-register REST IDs (002=list … 006=get) are authoritative over alternate prose numbering. Draft “preview” for unsaved edits is client-side; persisted draft preview uses ORG-TERMS-006.

---

## Session log — 2026-11-03 (API-07 PTR schedule conflict UX parity)

### Coverage
| Operation | Conflict UX | Availability UX | Override (permission-gated) | Draft preserve | Busy guard |
| --- | --- | --- | --- | --- | --- |
| Book PTR session | Yes | Yes | Yes (`override.trainer.schedule.conflicts`) | Yes | Yes |
| Reschedule PTR session | Yes | Yes | Yes | Yes | Yes |
| Assign trainer to PTR session | Yes | Yes | Yes | Yes | Yes |

### Shared utilities
Reused `schedule_conflict_support`, `schedule_conflict_flow`, override dialog; added `ScheduleConflictFeedbackCard` / `ScheduleOperationFeedback` for batch/PTR parity messaging.

### Tests
`ptr_operations_conflict_test` **7 passed**; combined with support/flow/batch conflict/enrollment suites **all passed**.

### Status
| Item | Label |
| --- | --- |
| Backend PTR conflict paths | **Implemented** / **Tested** (prior) |
| Flutter PTR conflict UX | **Implemented** / **Tested** |
| Facility/site conflicts | **Deferred by product decision** (not in enforcement) |
| Live E2E | **Not Integration-verified** |

---

## Session log — 2026-11-03 (API-07 schedule conflict UX — BatchDetailPage)

### Existing backend conflict behavior (authority)
| Question | Finding |
| --- | --- |
| What conflicts are detected? | **Trainer time overlap only** (BR-TRN-008): non-cancelled class sessions + personal training sessions for the effective trainer |
| Trainer conflicts? | **Yes** — HTTP **409** `TRAINER_SCHEDULE_CONFLICT` + catalog `TRAINER_CONFLICT_001` + structured `conflicts[]` (`conflict_type`, `session_id`, `starts_at`, `ends_at`) |
| Batch/session facility/site conflicts? | **Not implemented** — no facility/site overlap enforcement in schedule conflict module |
| Capacity restrictions on schedule write? | Enrollment capacity is separate; schedule path does not invent capacity conflict UX |
| Availability? | **BR-TRN-005** — `VALIDATION_FAILED` (422) when session not fully covered by AVAILABLE windows; **not overridable** |
| Override? | Optional `schedule_conflict_override` (`reason` 10–500, exact `acknowledged_conflicts`); permission `override.trainer.schedule.conflicts` (org admin implicit) |
| Triggering ops | Schedule batch (when trainer resolved), PTR book / reschedule / assign trainer |

### UX gaps before
Hardcoded tomorrow window; snackbar with conflict **count only**; generic `Schedule failed: $e` for availability/validation; form values discarded; weak override dialog detail.

### Flutter completed
Inline schedule form (code + start/end) preserving drafts; distinct conflict vs availability vs validation feedback + recovery guidance; conflict line summaries; improved override dialog with times; busy/duplicate submit guard; quiet schedule refresh after success.

### Files
`schedule_conflict_support.dart`, `schedule_conflict_flow.dart`, `schedule_conflict_override_dialog.dart`, `batch_detail_page.dart`, mock hook, `schedule_conflict_support_test.dart`, `batch_schedule_conflict_test.dart`, DEV-19.

### Tests
`flutter test` support + flow + batch_schedule_conflict + enrollment — **18 passed**. Analyze: no errors on touched files.

### Status
| Item | Label |
| --- | --- |
| Backend BR-TRN-005/008 | **Implemented** / **Tested** (prior) |
| Flutter BatchDetailPage conflict UX | **Implemented** / **Tested** |
| Facility/site conflict detection | **Deferred by product decision** (not in current enforcement) |
| Live E2E | **Not Integration-verified** |

---

## Session log — 2026-11-03 (API-07-018/019 batch enrollment Flutter)

### Gap analysis (API-07)
| Area | Backend | Flutter before | Decision |
| --- | --- | --- | --- |
| Trainer CRUD / assign / availability | 32/32 live | Screens + remote present | Defer polish — lower gap than enroll |
| Activity CRUD / batches | Live | List/form + create batch present | Defer |
| Batch schedule / trainer assign / session lifecycle | Live | Batch detail present | Already wired |
| Enroll / remove customer (API-07-018/019) | Live | **Missing** | **Selected** — highest unblocked vertical gap |
| List enrollments by batch | **Not in 228 inventory** | N/A | **Deferred by product decision** — session-known IDs only |
| Attendance ↔ batch/trainer | API-06 session/check-in live; desk reports done | Relates via class session / facility scope | No new attendance rules invented |

### Contract reused
- `POST /api/v1/batches/{batch_id}/enrollments` — `enroll.customer.into.batch` (201)
- `POST /api/v1/batches/{batch_id}/enrollments/{enrollment_id}/remove` — `remove.customer.from.batch`

### Flutter completed
`BatchEnrollment` model; repository + remote/mock enroll/remove; permission aliases; `BatchDetailPage` enroll/remove dialogs + session-known enrollment list (no list API).

### Tests
`flutter test test/features/training_operations/batch_enrollment_test.dart` — **4 passed**.

### Status
| Item | Label |
| --- | --- |
| API-07-018/019 backend | **Implemented** / **Tested** (prior) |
| Flutter enroll/remove on batch detail | **Implemented** / **Tested** |
| List enrollments API | **Deferred by product decision** (not in inventory) |
| Live E2E | **Not Integration-verified** |

---

## Session log — 2026-11-03 (API-06-009 Attendance reports Flutter)

### Gap analysis (ops)
| Area | Verdict |
| --- | --- |
| Customer CRM | Search/edit/history/profile remote; list-by-customer memberships deferred (P1-009) |
| Membership lifecycle | Known-membership freeze/resume/cancel done |
| Attendance core | Remote check-in / eligibility / history / walk-in path present |
| Attendance reports | Backend live; **Flutter missing** → selected |
| Walk-in identify | Backend live; optional polish (not selected) |

### Contract
`GET /api/v1/attendance/reports` — `attendance.history.view`; query org (+ optional facility/site + check-in window); `counts_by_status`, `present_checkins` (when both dates set), `total_records`.

### Flutter completed
Model + remote + `AttendanceReportController` + desk `AttendanceReportPanel` (local-day window, site-aware refresh). Tests: report controller **5** + existing desk suite still **28** (combined run with attendance_test).

### Status
| Item | Label |
| --- | --- |
| API-06-009 backend | **Implemented** / **Tested** (prior) |
| Flutter reports panel | **Implemented** / **Tested** |
| Live desk E2E | **Not Integration-verified** |

---

## Session log — 2026-11-03 (API-05 membership lifecycle Flutter)

### Gap analysis
| Capability | Backend | Flutter before | Decision |
| --- | --- | --- | --- |
| List memberships by customer | **Not in 228 inventory** | Empty profile note | **Deferred by product decision** (DR-020 P1-009 — do not implement `GET /memberships`) |
| Freeze | Live `POST .../freeze` | None | Unblocked — Phase 1 status-only (`reason` ≥3; ACTIVE→FROZEN; If-Match + Idempotency-Key) |
| Resume | Live `POST .../resume` | None | Unblocked — FROZEN→ACTIVE |
| Cancel | Live `POST .../cancel` | None | Unblocked — DRAFT/PENDING_PAYMENT/ACTIVE/FROZEN→CANCELLED; no invoice/refund side effects in service |
| Get + history | Live | Partial (get unused in UI) | Used to open known ID + show history |

Freeze Phase 1 does **not** collect freeze date ranges, extend expiry, or change billing; attendance eligibility is owned by API-06 (not invented here). Cancel does **not** auto-refund.

### Flutter completed
| Piece | Change |
| --- | --- |
| Domain | `canFreeze` / `canResume` / `canCancel` on `CreatedMembership` |
| Remote | freeze / resume / cancel posts with If-Match + Idempotency-Key |
| Controller | `CustomerMembershipLifecycleController` (open-by-id customer check, mutate, history refresh, busy guard) |
| UI | Customer profile: open by membership ID, freeze/resume/cancel dialogs, lifecycle history |
| Tests | lifecycle controller **10** + section tests updated — combined **16 passed** |

### Status labels
| Capability | Label |
| --- | --- |
| Freeze/resume/cancel backend | **Implemented** / **Tested** (prior) |
| Flutter lifecycle for known membership | **Implemented** / **Tested** |
| List-by-customer | **Deferred by product decision** |
| Live E2E | **Not Integration-verified** |

---

## Session log — 2026-11-03 (API-08-006 Flutter invoice cancel)

### Contract / backend (verified in code)
| Item | Evidence |
| --- | --- |
| Method/path | `POST /api/v1/invoices/{invoice_id}/cancel` |
| Auth | `billing.invoice.generate` + facility access + operational scope |
| Body | Required `cancellation_reason` (1–500) |
| Eligibility | Status **ISSUED** only; reject if SUCCESS payment exists; already **CANCELLED** returns current invoice (idempotent) |
| Effects | Invoice → **CANCELLED**; clears linked membership `invoice_id` when matched; receivable excluded from outstanding; payments unchanged |
| Idempotency header | Not required for cancel invoice |

### Flutter completed
| Piece | Change |
| --- | --- |
| Domain | `canCancelInvoice` on history + outstanding entries |
| Remote | `POST /invoices/{id}/cancel` on history + outstanding repos |
| Controllers | `cancelInvoice` with reason validation, busy guard, reload, actionMessage |
| UI | Cancel dialog on billing history + outstanding panels (`billing.invoice.generate`); cross-invalidate sibling providers |
| Tests | History **18** + outstanding **10** focused tests passed (2026-11-03 combined run **28**) |

### Status labels
| Capability | Label |
| --- | --- |
| API-08-006 backend | **Implemented** / **Tested** (prior) |
| Flutter invoice cancel | **Implemented** / **Tested** |
| Live cancel E2E | **Not Integration-verified** |

---

## Session log — 2026-11-02 (API-08-013 Flutter refund)

### Contract / backend (verified in code)
| Item | Evidence |
| --- | --- |
| Method/path | `POST /api/v1/payments/{payment_id}/refunds` → 200 |
| Auth | `billing.refund.process` + facility access + operational scope |
| Body | Optional `amount` (defaults to remaining refundable), optional `external_ref`, optional `refunded_at` |
| Idempotency | Required `Idempotency-Key`; replay same payload; conflict on mismatch |
| Eligibility | Payment must be **SUCCESS**; remaining balance = payment amount − SUCCESS refunds; partial or full |
| Response | `refund_id`, `payment_id`, `invoice_id`, `amount`, `currency`, `status` (**SUCCESS** recorded immediately in Phase 1), timestamps, `external_ref` |
| History after refund | Payment row stays **SUCCESS**; receivable restored via refund totals (outstanding); history snapshot fields unchanged |
| Status preview | `GET /payments/{id}/status` exposes `refunded_amount` / `refundable_balance` |

### Flutter completed
| Piece | Change |
| --- | --- |
| Domain | `canRefundSuccessfulPayment`, refund preview/result types, repo methods |
| Remote | status GET + refunds POST with idempotency |
| Controller | `loadRefundPreview`, `refundPayment` (busy guard, reload, actionMessage) |
| UI | Refund dialog on history panel (`billing.refund.process`); invalidates outstanding provider |
| Tests | `facility_billing_history_controller_test.dart` — **12 passed** |

### Status labels
| Capability | Label |
| --- | --- |
| API-08-013 backend | **Implemented** / **Tested** (prior) |
| Flutter refund workflow | **Implemented** / **Tested** |
| Live refund E2E | **Not Integration-verified** (needs 069 + SUCCESS payment with balance; no real gateway refunds) |

---

## Session log — 2026-11-02 (Outstanding Collect payment)

### Gap chosen
Highest-priority incomplete unblocked workflow: staff could **list** outstanding facility invoices (API-08-018) but could not **collect** from that panel; membership create/pay path already used API-08-010. Backend offline collect already **Implemented** / **Tested**.

### Completed — Flutter vertical slice
| Piece | Evidence |
| --- | --- |
| Domain | `canCollectPayment`, `FacilityOutstandingCollectResult`, repo `collectOfflinePayment` |
| Remote | `POST /api/v1/payments/offline` + `Idempotency-Key` (`newOutstandingCollectIdempotencyKey`) |
| Controller | `collectOfflinePayment` → reload list → `actionMessage`; errors keep rows |
| UI | `FacilityOutstandingStatementsPanel` Collect dialog (CASH/BANK_TRANSFER/UPI/CHEQUE/OTHER + reference); invalidates `facilityBillingHistoryControllerProvider` |
| Tests | `facility_outstanding_statements_controller_test.dart` — **5 passed** (2026-11-02) |
| Analyze | `dart analyze` on touched outstanding files — clean |

### Not done this slice
- No backend/schema changes; no migrations; no live HTTP against `digitize`
- No EQ-011 / `digitize_test` work
- Refunds UI, invoice cancel UI, API-08 skeletons — deferred

### Status labels
| Capability | Label |
| --- | --- |
| API-08-010 backend | **Implemented** / **Tested** (prior) |
| Outstanding Collect Flutter | **Implemented** / **Tested** |
| Live org billing collect E2E | **Not Integration-verified** (needs authorized DB with 063 + receivable rows) |

---

---

## Session log — 2026-11-03 (API-08 history refund eligibility + invoice status filter)

### Gap chosen
Billing history Refund CTA stayed visible for fully refunded SUCCESS payments because API-08-016 rows lacked refundable facts (preview via API-08-011 only after dialog open). Invoice `invoice_status` filter existed on the backend but was unused in Flutter.

### Backend
| Piece | Change |
| --- | --- |
| Schema | Additive optional `refunded_amount`, `refundable_balance` on `BillingHistoryEntryOut` (same facts as payment status) |
| Repository | `sum_successful_refunds_for_payments` batch helper |
| Service | History rows enrich SUCCESS payments with refund totals / remaining balance |
| Contract | Additive fields only — no frozen field renames/removals |

### Flutter
| Piece | Change |
| --- | --- |
| Domain | Parse refund fields; `canRefundSuccessfulPayment` requires balance > 0 when present |
| Remote / controller | Pass `invoice_status`; `setInvoiceStatusFilter` |
| UI | Invoice status dropdown on history panel; summary shows refundable/refunded |
| Reused | Existing refund dialog + status GET preview path unchanged |

### Deferred / unchanged
- API-08-002/003/004/009 — **Integration-verified** on local `digitize` (2026-11-08): `test_billing_m2_http_digitize_postgres.py`; **005** adjustments still deferred; **007/012/014** unchanged (`test_billing_credit_receipt_recon_http_digitize_postgres.py`)
- No migrations, gateway, credit notes, write-offs, real payments

### Focused verification
| Command | Result |
| --- | --- |
| `python3 -m pytest tests/billing/test_billing_history.py -q` | **6 passed** |
| `dart analyze` on touched billing history files | **No issues found** |
| `flutter test test/features/organization/facility_billing_history_controller_test.dart` | **20 passed** |

### Status labels
| Capability | Label |
| --- | --- |
| API-08-016 refundable enrichment | **Implemented** / **Tested** |
| Flutter refund CTA eligibility | **Implemented** / **Tested** |
| Flutter history invoice_status filter | **Implemented** / **Tested** |
| Live E2E | **Not Integration-verified** |

---

## Session log — 2026-11-03 (DEV-23 Phase 1 — Navigation, IAM, role experiences)

### Scope completed
- **GAP-UI-001 / GAP-JRN-006:** `/attendance` entry page + AppShell/rail/drawer nav → existing Attendance Desk + reports.
- **GAP-API03-001 / 002 (+ activity):** Staff remote/mock IAM methods; details panels for role/facility/site assign; activate + credential-reset lifecycle actions.
- **GAP-ROLE-001:** Site Admin no longer sees OA billing/company profile; account label shows Site Admin; ops remain permission + lifecycle gated. PA governance boundary unchanged (no tenant ops / no PA audit deep-link without org scope).

### Focused verification
- `dart analyze` on modified staff/attendance/shell/router/auth paths — no errors (pre-existing unused rail locals only).
- `flutter test` staff mock/permissions/details + attendance desk suite — passed.
- Integration-verified: **No**.

### Remaining in Phase 1
- None for scoped P1 Phase 1 items. GAP-API05-003 transfer/expire remains P2.

### Not done (excluded / blocked)
- PA org-wide audit browse without `org_id` (existing API contract constraint).
- EQ-011, SMS, schema, infra.

---

## Session log — 2026-11-03 (GAP-API05-002 Membership renew/upgrade/downgrade)

### Completed
- Flutter: renew / upgrade / downgrade on customer membership section via API-05-003/004/005.
- Payment retry path when backend requires `invoice_id` for paid commercial changes.
- Backend (smallest compatible fix): facility membership invoices allowed for **ACTIVE** as well as PENDING_PAYMENT so renew/upgrade can follow the activate payment pattern.

### Focused verification
- Flutter lifecycle + section tests: passed.
- `pytest tests/billing/test_facility_membership_billing.py`: **10 passed**.
- Integration-verified: **No**.

---

## Approval / deferral log

| Topic | Status |
| --- | --- |
| `BILLING_REFUNDS_REPORTING_ENABLED` | Not enabled (per policy) |
| Terraform / ECS changes | Not modified |
| Database migrations | Not applied |
| git commit / push | Not performed |

Resume future sessions from **Next implementation tasks** above; update **Session log** when work continues.

---

## Session log — 2026-11-03 (API-08 outstanding filter + API-05 transfer/expire Flutter)

### API-08 — Outstanding statements invoice_status filter parity

| Area | Change | Label |
| --- | --- | --- |
| Backend | `GET /billing/outstanding-statements` already supported `invoice_status` (unchanged) | **Implemented** (prior) |
| Flutter | `invoice_status` query on outstanding repo; controller filter + billing page dropdown (parity with billing history) | **Implemented** / **Tested** |
| Live E2E | — | **Not Integration-verified** |

**Tests:** `flutter test test/features/organization/facility_outstanding_statements_controller_test.dart` — **11 passed** (incl. new filter test).

**Files:** `facility_billing_outstanding.dart`, `remote_facility_outstanding_statements_repository.dart`, `facility_outstanding_statements_controller.dart`, `facility_outstanding_statements_panel.dart`, controller test.

### API-05 — GAP-API05-003 transfer / expire (Flutter)

| Op | Backend | Flutter | Notes |
| --- | --- | --- | --- |
| API-05-008 transfer | **Implemented** (same-facility site move only) | Site picker + reason; `membership.transfer` | Cross-facility rejected by backend |
| API-05-010 expire | **Implemented** | Optional reason dialog; `membership.expire` | Default backend reason when blank |

**Tests:** `flutter test test/features/customer/customer_membership_lifecycle_controller_test.dart test/features/customer/customer_membership_section_test.dart` — **20 passed** (combined with outstanding suite **32 passed** in one run).

**Files:** `created_membership.dart`, `customer_membership_repository.dart`, `remote_customer_membership_repository.dart`, `customer_membership_lifecycle_controller.dart`, `customer_membership_section.dart`, lifecycle + section tests.

### Remaining (unchanged)

- GAP-API05-001 list-by-customer — **Implemented** 2026-11-09 (additive GET; see session log)
- EQ-011, provider QA, schema skeletons — per Related table

### API-06 — Walk-in identify (GAP-API06-001)

| Area | Change | Label |
| --- | --- | --- |
| Backend | `POST /walkin-visits/identify` (unchanged) | **Implemented** (prior) |
| Flutter | Repository + desk **Identify customer** action with eligibility/open-visit feedback | **Implemented** / **Tested** |
| Live E2E | — | **Not Integration-verified** |

**Tests:** `flutter test test/features/attendance/walkin_identify_test.dart` — **1 passed** (with `walkin_charge_test.dart` **2 passed** in combined run).

---

## Session log — 2026-11-03 (GAP-API01-001 Platform Admin console — API-01 Flutter)

### Scope
Live API-01 operations **001–011** (excluding GMD **003–005** already on `platform_masterdata` pages).

| Op | Flutter workflow | Label |
| --- | --- | --- |
| API-01-001/002 | Settings list + JSON edit dialog (If-Match) | **Implemented** / **Tested** |
| API-01-006 | Feature flag update by code + version | **Implemented** / **Tested** (form) |
| API-01-007 | Schedule maintenance window | **Implemented** / **Tested** (form) |
| API-01-008 | Publish release by record ID + version | **Implemented** / **Tested** (form) |
| API-01-009 | Health summary panel + refresh | **Implemented** / **Tested** |
| API-01-010 | Security policy PATCH by record ID + version | **Implemented** / **Tested** (form) |
| API-01-011 | Queue platform report execution | **Implemented** / **Tested** (form) |

Route: **`/platform/console`** (`PlatformConsolePage`). App shell **Platform console** nav (Platform Admin + API-01 permission family). Remote: `RemotePlatformAdministrationRepository`.

### Limitations (not defects)
- No numbered **list** APIs for feature flags, releases, or security policies — UI uses operator-supplied codes/IDs/versions (same constraint as membership open-by-ID).
- Platform Admin JWT still uses existing presentation allow-list in `authPermissionProvider` (not expanded tenant ops).
- **Not Integration-verified** (widget/controller tests only).

### Tests
- `flutter test test/features/platform_administration/` — **5 passed**
- `dart analyze lib/features/platform_administration` — no errors (minor infos only)

### Files (new module)
- `digitize-ui/lib/features/platform_administration/**`
- `digitize-ui/test/features/platform_administration/**`
- `digitize-ui/lib/app/router.dart`, `lib/core/navigation/app_shell.dart`

---

## Session log — 2026-11-03 (GAP-API10-003 — Campaign admin Stage 1)

### Product direction applied
- Hybrid WhatsApp delivery model: manual/external **implemented**; Digitize-managed and org-owned **architecture only** (no fake sends, no OAuth/DB).

### Implemented
| Area | Change | Label |
| --- | --- | --- |
| Flutter module | `digitize-ui/lib/features/campaign/**` — Riverpod, `RemoteCampaignRepository` (API-10-001…012), local index, list/create/detail, lifecycle actions, customer audience search, consent warnings | **Implemented** |
| Manual distribution | WhatsApp share URI, copy message, report JSON export (no customer PII) | **Implemented** |
| Automated launch | Disabled for manual delivery (API-10-007 would enqueue real notifications) | **Implemented** |
| Navigation | `/campaigns` in router + app shell | **Implemented** |
| Architecture | [CAMPAIGN_HYBRID_WHATSAPP_DELIVERY.md](../architecture/CAMPAIGN_HYBRID_WHATSAPP_DELIVERY.md) Stages 2–3 dependencies | **Documented** |
| List campaigns | No frozen list/get API — device `CampaignLocalIndex` + open-by-UUID + report refresh | **Constraint documented** |
| Live E2E / WhatsApp | — | **Not Integration-verified** |

### Focused checks
- `flutter test test/features/campaign/` — **5 passed**
- `url_launcher` added to `pubspec.yaml`

### Remaining (GAP-API10-003)
- ~~Staff notification admin surfaces (templates, manual send history) — still **Missing**~~ **Done 2026-11-03** — see session log below (staff ops hub).
- Backend consent enforcement on campaign launch — **Gap** (see architecture doc)

### Next recommended
- **GAP-API11-002** (PDF export limitation doc) or next authorized P1 from DEV-19 § authorization queue

---

## Session log — 2026-11-03 (GAP-API06-002 — Session remarks UI)

### Implemented
| Area | Change | Label |
| --- | --- | --- |
| Repository | `updateRemarks` → PATCH `/api/v1/attendance/{id}` with `If-Match`; `attendanceAudit` → GET `.../audit` | **Implemented** |
| Desk UI | `AttendanceSessionRemarksPanel` on checked-in/out result; validation (500 chars); busy guard; local note list for session | **Implemented** |
| Audit | Shows `AttendanceAuditEntry` list when `attendance.audit.view` granted | **Implemented** |
| Check-in controller | `applyEntry` refreshes ETag after remark save | **Implemented** |
| Historical notes | Operational notes not returned on API-06 read — UI explains limitation | **Documented gap** |
| Live E2E | — | **Not Integration-verified** |

### Focused checks
- `flutter test test/features/attendance/attendance_session_remarks_test.dart` — **6 passed**

---

## Session log — 2026-11-03 (GAP-API10-003 — Staff notification admin UI)

### Product boundaries applied
- Separate from `features/campaign/` and user inbox (`/notifications/inbox`).
- No UI for API-10-016…019 (manual/system send, deliver, retry) — avoids unintended live delivery.
- Hybrid WhatsApp / campaign direction unchanged; no real bulk sends from this hub.

### Implemented
| Area | Change | Label |
| --- | --- | --- |
| Flutter module | `digitize-ui/lib/features/staff_notifications/**` — history, delivery detail + archive, org reports, template create, rule configure | **Implemented** |
| APIs reused | API-10-020 list, 021 delivery-status, 022 archive, 023 reports, 013 template, 014 rule | **Implemented** |
| Permissions | `StaffNotificationPermissions` + per-tab `authPermissionProvider` gates; org id from auth context | **Implemented** |
| Navigation | `/staff-notifications`, `/staff-notifications/:notificationId`; shell **Notification ops** | **Implemented** |
| Live E2E | — | **Not Integration-verified** |

### Contract limitations (documented, not defects)
- No frozen list/get for templates or rules — create-only forms; staff must retain returned IDs externally.
- API-10-024 preferences not surfaced (requires known `preference_id`; no org list in 228 inventory).
- Send/deliver/retry remain backend-only until product authorizes staff UI with delivery safeguards.

### Focused checks
- `flutter test test/features/staff_notifications/` — **9 passed**
- `dart analyze lib/features/staff_notifications` — **no issues**

### Files (new module)
- `digitize-ui/lib/features/staff_notifications/**`
- `digitize-ui/test/features/staff_notifications/**`
- `digitize-ui/lib/app/router.dart`, `lib/core/navigation/app_shell.dart` (nav wiring)

---

## Session log — 2026-11-03 (GAP-API10-005 — Inbox vs staff notification surface)

### Problem addressed
- Personal in-app inbox (INAPP-001…004, `/api/v1/me/notifications`) was easy to confuse with organization staff notification administration (`/staff-notifications`, API-10-020…024).
- Sidebar used the bell icon for staff ops; `/staff-notifications` could be mis-selected as “Staff” people nav because `_isStaffLocation` matched any path starting with `/staff`.

### Implemented
| Area | Change | Label |
| --- | --- | --- |
| Route guards | Staff admin paths require any `StaffNotificationPermissions`; personal inbox paths require tenant session (platform admin denied at router) | **Implemented** |
| Inbox routes | `/notifications/inbox` + alias `/me/notifications`; `InAppNotificationAccess` | **Implemented** |
| Inbox UX | Title **My notifications**, subtitle/empty state distinguish from staff ops; header bell tooltip **My notifications** | **Implemented** |
| Staff UX | Sidebar **Notification operations** (settings icon); hub subtitle points users to personal bell inbox | **Implemented** |
| Nav selection | `_isStaffLocation` excludes `/staff-notifications` | **Implemented** |
| Live E2E | — | **Not Integration-verified** |

### Focused checks
- `flutter test test/features/notifications/notification_surface_separation_test.dart` — **7 passed**
- `flutter test test/features/staff_notifications/` — **9 passed** (unchanged)
- `dart analyze` on touched modules — no new errors (pre-existing `app_shell` infos)

### Files
- `digitize-ui/lib/features/in_app_notifications/application/access/in_app_notification_access.dart`
- `digitize-ui/lib/features/in_app_notifications/**` (routes, inbox page, bell)
- `digitize-ui/lib/features/staff_notifications/application/access/staff_notification_permissions.dart`
- `digitize-ui/lib/app/router.dart`, `lib/core/navigation/app_shell.dart`
- `digitize-ui/test/features/notifications/notification_surface_separation_test.dart`

---

## Session log — 2026-11-03 (GAP-API09-001 — SaaS subscription/license admin Flutter)

### Reused (not duplicated)
- **Subscriptions & Billing** (`/organization/billing`) — facility `subscription_scope_status`, SaaS invoices, checkout entry, outstanding/history (API-08 extras + commerce).
- **`saas_checkout` / `saas_invoice`** — payment and invoice UX unchanged.

### Implemented (numbered API-09 in Flutter)
| Op | Use in UI | Label |
| --- | --- | --- |
| API-09-012 | Org/facility subscription status counts | **Implemented** |
| API-09-024 | Org/facility license status counts | **Implemented** |
| API-09-011 | Subscription history on detail | **Implemented** |
| API-09-003…009, 004 | Lifecycle actions (activate, suspend, cancel, expire, renew) | **Implemented** |
| API-09-005, 006 | Upgrade / downgrade (plan ID + server rules) | **Implemented** |
| API-09-010 | Renewal invoice (requires `terms_id` from billing) | **Implemented** |
| API-09-013 | Generate license from subscription | **Implemented** |
| API-09-022 | License detail GET | **Implemented** |
| API-09-023 | License history | **Implemented** |
| API-09-015…020 | License lifecycle (incl. renew) | **Implemented** |
| API-09-001, 002, 014, 017, 021 | No dedicated UI (see limitations) | **Documented** |

### Contract / product limitations
- No **list** or **GET subscription** in frozen 228 — hub uses **open-by-subscription-ID**; status snapshot from lifecycle POST responses + history.
- **API-09-001/002** create/plan-assignment without hub create form (IDs/dates from provisioning runbook).
- **API-09-017** capabilities PATCH, **API-09-014** facility assignment, **API-09-021** validate-login — not admin UI (system/login or future slice).
- Platform Admin facility suspend/activate extras — not in numbered UI (tenant org-admin scope).
- No client-side pricing, installments, grace periods, or payment capture.

### Focused checks
- `flutter test test/features/saas_subscription_admin/` — **5 passed**
- `dart analyze lib/features/saas_subscription_admin` — clean

### Files
- `digitize-ui/lib/features/saas_subscription_admin/**`
- `digitize-ui/test/features/saas_subscription_admin/**`
- `digitize-ui/lib/app/router.dart`, `lib/core/navigation/app_shell.dart` (route guard + **SaaS lifecycle** nav)

### Live E2E
- **Not Integration-verified**

---

## Session log — 2026-11-03 (GAP-ROLE-003 — Platform Admin audit navigation visibility)

### Root cause
- `app_shell.dart` hid **Audit events** when `user.isPlatformAdmin == true` even if `report.view` was granted.
- Route guard already required `AuditPermissions.view` (`report.view`) for `/organization/audit-events`.
- PA has no session tenant org; audit reads require `organization_id` (API-13-005/009/012).

### Implemented
| Area | Change | Label |
| --- | --- | --- |
| Navigation | Show audit nav for any principal with `report.view` (desktop rail + mobile `nav_audit_events`) | **Implemented** |
| PA org scope | `resolveAuditOrganizationId` — PA uses optional `?organizationId=`; tenant uses session org only | **Implemented** |
| Company profile | **View audit events** → `AuditRouteNames.eventsPath(organizationId: …)` when `report.view` | **Implemented** |
| Audit page | Permission empty state; PA “No company selected” + Companies link; subtitle shows scoped company id | **Implemented** |
| Reports hub | **Audit events** header action gated on `report.view` | **Implemented** |
| Backend / permissions | No new permission strings or API operations | **Unchanged** |
| Live E2E | — | **Not Integration-verified** |

### Behavior matrix
| Principal | `report.view` | Sidebar | Direct URL | Data scope |
| --- | --- | --- | --- | --- |
| Platform Admin | Yes | Audit events visible | Allowed; empty state until `organizationId` query or company link | Per-company query only |
| Platform Admin | No | Hidden | Access denied | — |
| Organization Admin | Yes | Visible (unchanged) | Allowed | Session organization |
| User without permission | No | Hidden | Access denied | — |

### Contract limitations (documented)
- No platform-wide audit browse without selecting a company (backend requires org scope; no impersonation).
- PA must open audit from **Companies** profile or navigate with `?organizationId=` — not a product defect.

### Focused checks
- `flutter test test/features/audit/` — **11 passed**
- `dart analyze` on touched audit/shell/org-details/reports modules — no new errors (pre-existing unused locals in `app_shell`)

### Files
- `digitize-ui/lib/features/audit/application/audit_organization_scope.dart` (new)
- `digitize-ui/lib/features/audit/routing/audit_route_names.dart`
- `digitize-ui/lib/features/audit/presentation/pages/audit_events_page.dart`
- `digitize-ui/lib/core/navigation/app_shell.dart`
- `digitize-ui/lib/features/organization/presentation/pages/organization_details_page.dart`
- `digitize-ui/lib/features/reporting/presentation/pages/company_reports_page.dart`
- `digitize-ui/test/features/audit/audit_navigation_access_test.dart` (new)
- `digitize-ui/test/features/audit/audit_events_page_test.dart`

### Next recommended (superseded by GAP-API11-002 completion — see session log below)
- ~~GAP-API11-002~~ **Done 2026-11-03**

---

## Session log — 2026-11-03 (GAP-API11-002 — Reporting PDF export limitation)

### Backend truth (unchanged)
- API-11 catalogue publishes `export_formats` per report — default core: **html, xlsx, csv**; `membership_revenue_summary`: **html, xlsx** only; unavailable training reports: **none**.
- `ReportingService.export` renders HTML, XLSX, CSV; any other format (including **pdf**) → `ValidationFailed("PDF export is not available.")`.
- Export requires **`report.export`**, Advanced Reporting entitlement, and a successful execution for the selected period.
- SaaS invoice PDFs (API-09 extras) are **separate** operations — not company report exports.

### Implemented (Flutter only)
| Area | Change | Label |
| --- | --- | --- |
| Messaging | `report_export_messaging.dart` — labels, PDF limitation copy, catalogue subtitles | **Implemented** |
| Reports UI | `ReportExportCapabilityPanel` on **Reports** when a report is selected; chips for supported formats; PDF limitation text | **Implemented** |
| Export actions | Buttons only for catalogue formats (never PDF); human-readable labels (HTML, Excel, CSV) | **Implemented** |
| Page copy | Header + list subtitles state PDF not available for API-11 | **Implemented** |
| Live E2E | — | **Not Integration-verified** |

### Future backend dependency (documented, not in scope)
- Product-approved PDF renderer + catalogue `export_formats` entry + inventory change would be required before PDF could be offered in UI.

### Focused checks
- `flutter test test/features/reporting/` — **21 passed**
- `dart analyze lib/features/reporting` — clean

### Files
- `digitize-ui/lib/features/reporting/application/report_export_messaging.dart`
- `digitize-ui/lib/features/reporting/presentation/widgets/report_export_capability_panel.dart`
- `digitize-ui/lib/features/reporting/presentation/pages/company_reports_page.dart`
- `digitize-ui/test/features/reporting/report_export_messaging_test.dart`
- `digitize-ui/test/features/reporting/company_reports_page_test.dart`

### Next recommended (superseded — GAP-API11-003 partial run complete; see below)

---

## Session log — 2026-11-03 (GAP-API11-003 — API-11 reporting live certification)

### Authorized environment assessed
| Target | Outcome |
| --- | --- |
| Local PostgreSQL **`digitize`** (development, Alembic **072**) | **Used** — read/write ASGI certification |
| Loopback HTTP API (uvicorn/QA) | **Not running** — not started per execution rules |
| **`digitize_test`** + `DIGITIZE_API_TEST=1` | **Blocked** — Alembic **036**, EQ-011 preflight NOT READY |
| Flutter → live backend | **Not executed** |

### Certification harness (new)
- `digitize-services/scripts/reports_certification_evidence.py` — opt-in `DIGITIZE_REPORTS_CERTIFICATION=1`, ASGITransport + real sessions.
- Evidence artifacts: `docs/16_Development_Readiness/evidence/GAP-API11-003_certification_run_2026-11-03.jsonl`, `…_certification_summary.md`.

### Results (honest labels)
| Layer | Result |
| --- | --- |
| Catalogue / unavailable reports | **API integration verified** (HTTP 200, ASGI + `digitize`) |
| Report generation (membership, revenue+facility) | **API integration verified** |
| Date validation | **API integration verified** (422) |
| Permission gate (`report.view`) | **API integration verified** (403) |
| PDF via service | **API integration verified** — `ValidationFailed` (not in catalogue) |
| Export entitlement (HTML) | **API integration verified** — Advanced Reporting required |
| HTTP export API-11-009 (html/xlsx/csv/pdf) | **Partial IV** — lookup + **403** entitlement / **422** PDF after harness fix; **200 byte export not verified** (Acme entitlement inactive) |
| SQL read-only integration suite | **Tested** (14 passed, `DIGITIZE_REPORTING_SQL_TEST=1`) |
| Route/decision unit tests | **Tested** (33 passed) |
| Flutter Reports UI | **Widget tested** (21 passed; not live E2E) |

### Follow-up (superseded by API-11-009 investigation — see session log below)

### Next recommended (superseded)

---

## Session log — 2026-11-03 (API-11-009 export HTTP 404 investigation)

### Root cause
- **Test-harness defect**, not backend: `reports_certification_evidence.py` overrode `get_session` without `UnitOfWork.commit()`.
- Run returned `execution_id` from flush; transaction rolled back → export lookup → **404**.

### Fix
- Removed harness `get_session` override; added `tests/reports/test_reports_export_http_digitize.py` (4 passed with `DIGITIZE_REPORTS_EXPORT_HTTP_TEST=1`).
- **No production route/service/schema changes.**

### Post-fix HTTP (Acme, Advanced Reporting inactive)
- html/xlsx/csv export: **403** entitlement (execution found).
- pdf export: **422** format validation.

### Certification rerun
- Evidence JSONL updated; D-001…D-003 **blocked** (403); fail count **0**.

### Next recommended
- Authorized Advanced Reporting on test org for export-byte IV, or DEV-19 items **6–8**.

---

## Session log — 2026-11-03 (AUDIT-TXN — cross-module transaction safety)

### Scope
Read-only audit of API-01…API-14 in `digitize-services`. No contract, schema, migration, or remediation code changes.

### Transaction architecture (authoritative)
| Layer | Behavior | Evidence |
| --- | --- | --- |
| `get_session` | Single request UoW: commit on success; rollback + discard pending channels on error; post-commit email/SMS/WhatsApp flush | Code review `app/api/deps.py`, `app/infrastructure/database/uow.py` |
| Repositories | `flush()` only; no commit | Grep `app/**` — commits only in documented exceptions |
| Audit writer | `record_audit_event` → `session.add` + `flush`; same txn as mutation | `app/modules/audit/service.py` |
| Attendance denials | Separate short txn for audit when main txn rolls back (by design) | `denial_audit.py` + unit tests |
| Workers | Caller commits (notification worker script) | `scripts/run_notification_worker.py` |

### Module results (summary)
| Module | Overall | Notes |
| --- | --- | --- |
| API-01 Platform | **PASS** | Settings/releases/flags: flush + audit in request session |
| API-02 Org / facility / site | **PASS** | Org/terms services use shared session; bulk ops use `begin_nested` savepoints |
| API-03 Identity | **PASS** / **RISK** | Provisioning + audit same txn; post-commit SMTP (TEST-12) |
| API-04 Customer | **PASS** | Registration paths use row locks where needed (repository `with_for_update`) |
| API-05 Membership | **PASS** | Lifecycle history + audit in same service txn; idempotency metadata |
| API-06 Attendance | **PASS** | Successful check-in/out audit + rows same txn; denial audit isolated |
| API-07 Training | **PASS** / **BLOCKED** | Advisory locks + opt-in PG concurrency suite |
| API-08 Billing | **GAP** | Refunds/cancel use `FOR UPDATE`; offline success record does not lock invoice (**GAP-TXN-001**) |
| API-09 Subscription | **PASS** | SaaS commerce idempotency + webhook dedupe; `FOR UPDATE` on hot rows |
| API-10 Notification | **PASS** | Queue rows in business txn when emit succeeds; worker `skip_locked` |
| API-11 Reports | **PASS** | Execution/export persist via request UoW (API-11-003 harness lesson) |
| API-12 Support | **PASS** | Savepoints for partial failure within ticket/chat flows |
| API-13 Audit | **PASS** | Immutable insert participates in caller commit |
| API-14 Reference | **PASS** | Read/write reference routes use `get_session` |

### Tests run (this session)
- `pytest tests/attendance/test_denial_audit_and_tokens.py tests/billing/test_refund_service.py tests/membership/test_membership_lifecycle.py` — **28 passed** (unit; not HTTP IV).

### Remediation (not started — await instruction)
1. **GAP-TXN-001:** Lock invoice (or equivalent) in `OfflinePaymentService.record` before creating SUCCESS payment.
2. **GAP-TXN-002:** Document/review test `get_session` overrides (pattern caused API-11-003 false 404).
3. **GAP-TXN-003:** Accept or product-review post-commit email vs identity atomicity.

### Next recommended
- Authorized fix for GAP-TXN-001, or export-byte IV, or DEV-19 items **6–8**.

---

## Session log — 2026-11-03 (GAP-TXN-001 — API-08-010 offline payment concurrency)

### Root cause (confirmed)
- `OfflinePaymentService.record` loaded invoices without row lock; concurrent SUCCESS inserts with different idempotency keys could over-settle.

### Implementation
- `BillingRepository.get_invoice_for_update` (`SELECT … FOR UPDATE`).
- After lock: recompute outstanding via payment/refund sums; **full** payment amount = invoice total (server-derived per contract); reject when outstanding ≤ 0 or when invoice total exceeds outstanding; set `PAID` when balance cleared after full pay.
- Idempotency replay unchanged (returns prior payment).

### Tests
- `tests/billing/test_offline_payment_invoice_lock.py` — 5 unit + 3 opt-in PG on local **`digitize`** (`DIGITIZE_OFFLINE_PAYMENT_CONCURRENCY_PG_TEST=1`): sequential reject, dual-session concurrent full pay, partial remainder concurrency — **8 passed**.

### Labels
- **Implemented** / **Unit-tested** / **Database integration-tested** (local `digitize`, opt-in).
- **Not** full **Concurrency integration-verified** per GAP-TXN-004 (shared-env / broader matrix).

### Next recommended
- Export-byte IV or DEV-19 items **6–8**.

---

## Session log — 2026-11-03 (GAP-TXN-002 — test harness transaction lifecycle)

### Delivered
- Shared helper `tests/api/asgi_session_helpers.py` (`clear_get_session_override`, `install_unit_test_session_stub`, teardown).
- Override inventory: `docs/16_Development_Readiness/evidence/GAP-TXN-002_session_override_inventory.md` (8 sites; 2 integration/production-path, 5 unit stubs, 1 certification).
- Regression: `tests/infrastructure/test_get_session_uow_lifecycle.py` — UoW commit/rollback unit tests + opt-in ASGI persistence (`DIGITIZE_GET_SESSION_LIFECYCLE_TEST=1`).
- Standardized unit-test fixtures to named stub helper (reporting routes, attendance OTP/token, subscription bulk, SaaS price versions).
- API-11 certification script doc + prior fix (production `get_session` only); `test_reports_export_http_digitize.py` explicit clear override.

### Labels
- **Implemented** / **Unit-tested** (4 lifecycle unit tests pass by default).
- **Integration-tested:** API-11 export suite + optional lifecycle test on local `digitize` (opt-in).
- Production `get_session` / UoW: **unchanged**.

### Next recommended
- GAP-TXN-003 (separate) or export-byte IV.

---

## Session log — 2026-11-03 (GAP-TXN-003…005 — transaction safety closure)

### GAP-TXN-003
- Traced `issue_account_credentials` / `queue_recovery_email` → `EmailOutbox` + pending queue; delivery via `flush_pending_email` after UoW commit.
- **Change:** `_sync_password_reset_delivery_from_outbox` in `app/infrastructure/email/service.py` updates open `PasswordResetRequest` rows to SENT/FAILED when outbox status is recorded post-commit.
- **Recovery:** Admin/staff credential-reset or re-provision consumes prior tokens and queues new mail (no SMTP inside open txn).
- **Tests:** `tests/identity/test_credential_email_txn003.py`.
- **Limitation:** No durable outbox retry worker — **Deferred by product decision** if background retry is required.

### GAP-TXN-004
- Evidence matrix: `docs/16_Development_Readiness/evidence/GAP-TXN-004_concurrency_matrix.md`.
- Reused GAP-TXN-001 opt-in PG on local `digitize`; added `tests/communication/test_notification_worker_claim.py` (SKIP LOCKED).
- **Blocked:** concurrent refund IV, multi-session SaaS webhook IV on shared DB.

### GAP-TXN-005
- Confirmed `app/modules/users` not on `v1_router`.
- Removed independent `session.commit()` from scaffold `UserRepository.create` (flush only).
- **Tests:** `tests/users/test_gap_txn005_scaffold.py`.

### Labels
- TXN-003: **Implemented** / **Tested**
- TXN-004: **Partial** / payment opt-in **Integration-verified** where run
- TXN-005: **Resolved** / **Tested**

---

## Session log — 2026-11-03 (GAP-TXN-004 — PostgreSQL concurrency IV completion)

### Database
- Target verified: **localhost:5434**, database **`digitize`**, `ENVIRONMENT=development`.
- No full truncate/reset; tagged fixture rows with teardown deletes.

### Tests added
- `tests/billing/test_refund_concurrency_postgres.py` — 2 sessions, barrier sync (full refund race, idempotency race, partial cap).
- `tests/subscription/test_saas_webhook_concurrency_postgres.py` — concurrent/sequential webhook (mock Razorpay).
- Helpers: `tests/concurrency/digitize_pg_guard.py`, `tests/concurrency/saas_webhook_pg_prereqs.py`.

### Production
- `SaasCommerceService.handle_webhook`: handle `IntegrityError` on concurrent `saas_provider_event` insert → **`duplicate`** response.

### Execution (this session)
- 6/6 TXN-004 PG tests passed; 3/3 TXN-001 payment PG tests passed; 39 unit regressions passed (1 skipped opt-in lifecycle).

### Labels
- **Integration-verified** on local `digitize` for refund + webhook matrix items.

---

## Session log — 2026-11-03 (GAP-TXN-004 — webhook duplicate rollback scope)

### Finding
- Production path `razorpay_webhook` → `get_session` → `handle_webhook` only; no DB work before service.
- Event insert is the **first write** in `handle_webhook`; unique-violation `session.rollback()` runs before attempt/obligation/`_mark_verified` on the **losing session** only.
- **No production code change** (savepoint not required for current route).
- Scenario “duplicate + unrelated pending work in same txn” **N/A** on registered route.

### Tests
- `tests/subscription/test_saas_webhook_rollback_scope_postgres.py` (PG + route isolation unit check).
- Evidence: `GAP-TXN-004_concurrency_matrix.md` rollback scope section.

---

## Session log — 2026-11-03 (GAP-API03-004 + GAP-API07-003 partial)

### GAP-API03-004
- Remote staff details: `staff_directory_lookup.dart` paginates `GET /identity/staff-directory` and searches by staff code when applicable (228 has no GET-by-id).
- Tests: `staff_directory_lookup_test.dart` — **2 passed**.

### GAP-API07-003 (capacity slice)
- Flutter: `configureBatchCapacity` → `POST /api/v1/batches/{id}/capacity` (API-07-017), permission `configure.batch.capacity`, batch detail **Set capacity** action.
- Tests: `batch_detail_widget_test.dart` — **passed** (mock).

### Labels
- **Implemented** / **Tested** (Flutter unit/widget); **not** integration-verified on live `digitize`.

### Next incomplete (recommended)
- GAP-API07-003 remainder: ~~activity rules UI (API-07-013), customer progress (API-07-030)~~ **Done 2026-11-03** (see session log below).

## Session log — 2026-11-03 (GAP-API07-003 completion — rules + progress Flutter)

### Delivered

| Op | Backend | Flutter | Tests |
| --- | --- | --- | --- |
| API-07-013 Configure Activity Rules | Implemented (prior) | `ActivityFormPage` rule form + `configureActivityRules` remote/mock | `activity_rules_and_progress_test.dart`; `test_activity_rules_and_progress.py` |
| API-07-030 Record Customer Progress | Implemented (prior) | PTR **Notes** tab + `recordCustomerProgress` remote/mock | Same |

### Evidence

```bash
cd digitize-services && python3 -m pytest tests/training/ -q --ignore=tests/training/test_trainer_schedule_concurrency_postgres.py
# 75 passed

cd digitize-ui && flutter test test/features/training_operations/ -r compact
# 40 passed
```

Integration-verified against live PostgreSQL: **PASS** for GAP-API07-004 (`tests/training/test_training_programs_digitize_postgres.py`, Alembic `072_platform_terms_document`, DB `digitize`). EQ-011 / `digitize_test` certification and opt-in PG concurrency module unchanged.

## Session log — 2026-11-03 (API-08 module assessment + GAP-API08-009)

- **Inspection:** 10/18 operations **Implemented**; 8 skeletons unchanged per [API-08 facility billing register](../architecture/API-08_FACILITY_BILLING_DECISION_REGISTER.md). No new financial rules or provider credentials.
- **Live IV:** Fixed stale Alembic pin in `test_billing_invoices_revenue_live_digitize.py`; added `billing_digitize_pg_guard.py`; extended HTTP coverage (016, 018, 011, 010, 015, 013, 017 aggregates).
- **Evidence:** [API-08_Acceptance_Evidence.md](../07_API_Collections/API-08_Acceptance_Evidence.md) — full 18-op matrix.
- **Regression:** `pytest tests/billing/` (38 passed, 1 skipped) + live suite **1 passed**; Flutter billing controller tests unchanged.

## Session log — 2026-11-03 (API-09 master assessment + evidence)

- **Inspection:** Registry **24/24 BACKEND_IMPLEMENTED**; Flutter `saas_checkout`, `saas_invoice`, `/organization/subscription-admin`. No new numbered APIs or migrations.
- **Commercial rules:** 60/40 + month-3 due **tested**; month-end **blocked**; proration **blocked**; facility-scoped quotes; ads excluded in calculator.
- **Gaps (not invented):** live Razorpay **GAP-API09-003**; SaaS statutory invoice **GAP-API09-002**. Cheque bounce grace **GAP-API09-005** implemented (waive HTTP pending approval).
- **Evidence:** [API-09_Acceptance_Evidence.md](../07_API_Collections/API-09_Acceptance_Evidence.md).
- **Tests:** `pytest tests/subscription/` + `test_subscription_license.py` → **123 passed**, 63 skipped; Flutter SaaS → **33 passed**.

## Session log — 2026-11-03 (GAP-API09-006 PostgreSQL IV)

- **Tests:** `tests/subscription/test_facility_proration_postgres.py` + `proration_pg_prereqs.py` (tagged `{TAG}` org rows).
- **Command:** `DIGITIZE_PRORATION_PG_TEST=1 ENVIRONMENT=development DB_NAME=digitize DB_HOST=localhost pytest tests/subscription/test_facility_proration_postgres.py -q` → **5 passed**.
- **Verified:** anchor from explicit `ends_at`, preview/create/accept/mock verify, invoice preview parity, read-after-write, idempotency, late installment reject, anchor conflict, cross-org deny.
- **Cleanup:** commercial/facility rows removed; append-only `audit.audit_event` prevents org delete when commerce wrote audit rows.

## Session log — 2026-11-03 (GAP-API09-006 INV-005 implementation)

- **Policy:** Approved INV-005 — org common renewal, calendar-day proration, facility creation effective date, co-termination, late-addition annual-only, no auto-credits.
- **Backend:** `commerce/proration.py`, `quote_pricing.py`; `calculator.py` installment anchor; `SaasCommerceService` quote/preview; `activate_from_verified_payment` sets common `ends_at`; invoice period from terms snapshot.
- **Flutter:** `SaasQuotePreview` proration fields; `FacilityCreateSubscriptionEstimate` + `FacilityCheckoutPage` server-driven billing options.
- **Tests:** `test_facility_addition_proration.py`; subscription suite **139 passed**; mock checkout lifecycle updated.
- **PG IV:** `DIGITIZE_PRORATION_PG_TEST=1` — `test_facility_proration_postgres.py` **5 passed** on local `digitize` (read-after-write quote/terms/mock verify/activation; 2026-11-03).
- **Status:** GAP-API09-006 **Integration-verified** (local `digitize`); not EQ-011 / live Razorpay.

## Session log — 2026-11-03 (GAP-API09-002 statutory invoice readiness)

- **Scope:** Policy/schema/dependency assessment only — **no GST implementation**, no migrations, no statutory records created.
- **Inspection:** `SaasInvoiceService` preview (non-persistent) vs issue (persisted `TAX_INVOICE`); `ISSUANCE_BLOCKERS`; migration 034; API-08 `billing.*` boundary; org GSTIN encryption; 60/40 obligations unchanged.
- **Deliverable:** [SAAS_INVOICE_READINESS_DECISION_REGISTRY.md](../architecture/SAAS_INVOICE_READINESS_DECISION_REGISTRY.md) **§8** (matrix A–L, installment analysis, dependencies, sequence, IV plan).
- **Status:** GAP-API09-002 **Blocked (product + legal)** — assessment complete; **not** implemented or integration-verified.
- **Minimum decisions to start build:** INV-001 (POS/components), INV-003 (installment tax docs), INV-002 (GSTIN on snapshot/PDF).

## Session log — 2026-11-03 (GAP-API09-002 decision-resolution package)

- **Deliverable:** Registry **§9** — INV-001 / INV-003 / INV-002 sign-off templates, option matrices, ownership, legal question lists, sequence §9.4.
- **No business option selected** in registry; technical recommendations only where labelled.
- **Status:** GAP-API09-002 remains **Blocked (product + legal)** until §9 sign-offs + advisor answers.
- **No code, migrations, commerce behavior, or financial records changed.**

## Session log — 2026-11-03 (API-05 / API-06 PostgreSQL IV)

- **Defect fixed:** `InvoiceItem.product_id` invalid ORM FK → membership invoice 500 on PostgreSQL (`app/modules/billing/models/invoice_items.py`).
- **PG IV:** `DIGITIZE_MEMBERSHIP_PG_TEST=1` / `DIGITIZE_ATTENDANCE_PG_TEST=1` on local `digitize` — see `test_membership_lifecycle_digitize_postgres.py`, `test_attendance_desk_digitize_postgres.py`.
- **Evidence:** [API-05_Acceptance_Evidence.md](../07_API_Collections/API-05_Acceptance_Evidence.md), [API-06_Acceptance_Evidence.md](../07_API_Collections/API-06_Acceptance_Evidence.md).

## Session log — 2026-11-03 (GAP-API09-006 facility-addition proration)

- **Scope:** Focused API-09 gap only — no general API-09 re-audit, no code changes to commerce math.
- **Pricing model (verified):** Billable unit = facility; list price from active `commercial.saas_plan_price_version` (period `ANNUAL`) per facility-type plan; `calculate_quote` applies platform discount/tax and `ANNUAL_UPFRONT` or `INSTALLMENT_60_40`; not volume-tiered; ads excluded (`advertising_included: false`).
- **Current add-facility behavior:** Facility created with `subscription_scope_status=PENDING`; checkout quote/payment is per-facility full annual contract (no proration); verified payment activates subscription + scope; operational writes gated on `ACTIVE` scope.
- **Outcome:** **Outcome B** — essential proration formula and period anchor undecided; **not implemented** (would charge wrong amounts if guessed). Product decision request captured in chat deliverable + API-09 acceptance evidence § GAP-API09-006.
- **Status:** GAP-API09-006 remains **Blocked (product)**; not integration-verified.

- GAP-API11-003 export-byte IV when Advanced Reporting entitlement available on test org.
- Phase 2 provider QA or authorized gates (EQ-011, API-12-008).

## Session log — 2026-11-03 (API inventory reconciliation)

### Machine audit (no DB, no code changes)

| Check | Result |
| --- | --- |
| `poetry run python scripts/contract_numbered_audit.py` | **228** rows; **204** `BACKEND_IMPLEMENTED`; **24** `SKELETON_CREATED` |
| Live FastAPI routes vs numbered `BACKEND_IMPLEMENTED` | **204/204** registered; **0** catalog/live mismatches |
| Live routes vs `SKELETON_CREATED` | **0/24** registered (expected) |
| `EXTRA_OPERATIONS` | **158** entries; **158/158** registered |
| `/api/v1` route pairs | **362** = 204 numbered + 158 extras (disjoint paths) |
| Per-collection numbered totals | API-01…07, 09…11 **full live**; API-08 **10/18**; API-12 **11/12**; API-13 **3/12**; API-14 **6/12** |

### ORG-TERMS-001…006 + ORG-ONBOARDING-ACCEPT-001

| ID | Registered | Catalog status | Backend tests | Flutter |
| --- | --- | --- | --- | --- |
| ORG-TERMS-001…006 | Yes (6 routes) | `BACKEND_IMPLEMENTED` in extras | `test_onboarding_review.py`, `test_module_routes.py` path asserts | OA onboarding + PA `/platform/terms` CMS |
| ORG-ONBOARDING-ACCEPT-001 | Yes | `BACKEND_IMPLEMENTED` | Same onboarding suite | OA accept flow |

All six T&C management/read routes are **implemented** and **tested** (unit/contract); **not** claimed Integration-verified on shared QA. Kept **outside** the frozen **228** inventory.

### Count correction note

Historical **204/228** and **24 skeleton** figures remain **correct** for the numbered catalogue. **228+6=234** is **not** an authoritative total product API count — **156** additional approved product extras exist beyond ORG-TERMS alone (see API_CONTRACT_REGISTRY reconciliation table).

### Documents updated

- [API_CONTRACT_REGISTRY.md](../architecture/API_CONTRACT_REGISTRY.md) — reconciliation §, exact 24 skeleton table, route arithmetic
- [ROUTE_SOURCE_INVENTORY_2026-11-03.md](../16_Development_Readiness/evidence/ROUTE_SOURCE_INVENTORY_2026-11-03.md) — **bottom-up per-file route counts** (primary engineering evidence)
- DEV-19 (this file), DEV-21/DEV-23 cross-references unchanged except where counts already matched

---

## Session log — 2026-11-03 (Bottom-up route.py / routes source inventory)

### Discovery

- **0** files named exactly `route.py`.
- **26** route source files (`routes.py`, `routes_*.py`, `*_routes.py`, `health.py`).
- **2** additional app-level GET handlers in `app/main.py` (`/docs`, `/docs/oauth2-redirect`).
- **`app/modules/users/routes.py`:** 2 source endpoints, **not** mounted on `v1_router`.

### Counts (source-first)

| Layer | Count |
| --- | ---: |
| Source declarations in route files | **366** |
| Runtime unique `/api/v1` HTTP | **362** |
| Runtime `/api/v1` WebSocket | **1** |
| Post-hoc map: numbered live + extras | **204 + 158 = 362** HTTP |
| Catalog numbered skeletons (no route) | **24** |

Regenerate: `poetry run python scripts/route_source_inventory.py`.

---

## Session log — 2026-11-03 (Integration verification closure — API-11 export bytes, API-13/12/04 PG)

### GAP-API11-003 — Advanced Reporting export-byte IV

| Item | Detail |
| --- | --- |
| Helper | `tests/reports/advanced_reporting_entitlement_helpers.py` — temporary `commercial.entitlement` row for Acme |
| Test | `test_run_then_export_html_returns_attachment_bytes` in `test_reports_export_http_digitize.py` |
| Command | `DIGITIZE_REPORTS_EXPORT_HTTP_TEST=1 ENVIRONMENT=development DB_NAME=digitize DB_HOST=localhost pytest tests/reports/test_reports_export_http_digitize.py -q` → **5 passed** (incl. prior 403/422 regressions) |
| Label | **Integration-verified** (local `digitize`; entitlement row removed after module) |

### GAP-API13-006 — API-13 Phase 1 reads PG IV

| Op | Evidence |
| --- | --- |
| API-13-005 list | `tests/audit/test_audit_reads_digitize_postgres.py` |
| API-13-009 export | Same (202 + events page) |
| API-13-012 analytics | Same (dict aggregates) |
| Command | `DIGITIZE_AUDIT_PG_TEST=1 … pytest tests/audit/test_audit_reads_digitize_postgres.py -q` → **4 passed** |

### GAP-API12-002 — Support ticket org-scoped PG IV (excludes API-12-008)

| Flow | Evidence |
| --- | --- |
| Create → accept → progress → resolve → reports | `tests/support/test_support_tickets_digitize_postgres.py` |
| Command | `DIGITIZE_SUPPORT_PG_TEST=1 … pytest tests/support/test_support_tickets_digitize_postgres.py -q` → **1 passed** |
| Escalate | **Awaiting authorization** (unchanged) |

### GAP-API04-002 — Customer CRM PG IV

| Flow | Evidence |
| --- | --- |
| Register → GET → search by phone | `tests/customer/test_customer_crm_digitize_postgres.py` |
| Command | `DIGITIZE_CUSTOMER_PG_TEST=1 … pytest tests/customer/test_customer_crm_digitize_postgres.py -q` → **1 passed** |

### Files added/changed (digitize-services)

- `tests/reports/advanced_reporting_entitlement_helpers.py`, `tests/reports/reports_export_digitize_pg_guard.py`, `tests/reports/test_reports_export_http_digitize.py`
- `tests/audit/audit_digitize_pg_guard.py`, `tests/audit/test_audit_reads_digitize_postgres.py`
- `tests/support/support_digitize_pg_guard.py`, `tests/support/test_support_tickets_digitize_postgres.py`
- `tests/customer/customer_digitize_pg_guard.py`, `tests/customer/test_customer_crm_digitize_postgres.py`

