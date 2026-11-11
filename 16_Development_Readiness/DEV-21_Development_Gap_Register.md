# DEV-21 Development Gap Register

**Document ID:** DEV-21  
**Status:** Working register derived from DEV-20 assessment (2026-11-03)  
**Parent:** [DEV-20_Comprehensive_Development_Gap_Assessment.md](./DEV-20_Comprehensive_Development_Gap_Assessment.md)  
**Roadmap:** [DEV-23](./DEV-23_Development_Completion_Roadmap.md)  
**Inventory authority (2026-11-04):** Canonical registry **`app/api/contracts/api_registry.py`**. Full reconciliation: [API_INVENTORY_RECONCILIATION_2026-11-04.md](./evidence/API_INVENTORY_RECONCILIATION_2026-11-04.md).  
**Status vocabulary:** Implemented · Tested · Integration-verified · Blocked · Deferred by product decision · Awaiting authorization  

Priority: **P0** Critical · **P1** Core product completion · **P2** Important completeness · **P3** Enhancement  

> Priority ≠ implementation status. Deferred product decisions are not ordinary defects.

---

## Summary counts (actionable + gated)

| Class | Approx. count |
| --- | ---: |
| P0 | 4 |
| P1 | 28 |
| P2 | 24 |
| P3 | 14 |
| **Total registered** | **75** |

Of which roughly: **~22 Deferred by product decision**, **~8 Awaiting authorization / Blocked (schema/provider)**, remainder **Missing Flutter / Partial E2E / verification**.

---

## P0 — Critical

| Gap ID | Module | Role | Affected | Current | Missing | Impact | Priority | Dependencies | Required work | Completion criteria | Decision / auth | DEV-19 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| GAP-INT-001 | Integrations / API-04/06 | OA/Staff | OTP register, attendance OTP | SMS abstract + memory/none + MSG91 boundary | Live SMS vendor | Cannot QA or operate OTP flows | P0 | Provider contract, secrets | **Deferred first release**; consolidated `Msg91SmsNotificationDeliveryProvider` (not activated) — evidence `GAP-INT-001-002_COMMUNICATION_CONSOLIDATION_2026-11-09.md` | OTP succeeds in authorized QA | **Deferred by product** | Vendor API + DLT |
| GAP-API05-001 | API-05 | OA | Customer membership desk | Open-by-known-ID + additive list GET | — | Desk discovery | P0 (product) | DR-020 P1-009 | — | List + open lifecycle from profile | **INTEGRATION_VERIFIED (local `digitize`)** 2026-11-09 | API-05 |
| GAP-API08-006 | API-08 | OA | Online facility payments (**catalog API-08-009**, not API-08-005 adjustments) | Mock route + `payment_transactions` | Live Razorpay + Flutter checkout | No card capture for facility invoices if required | P0 | API-08 register, Razorpay | Approve live gateway + checkout UX | Online pay succeeds sandbox | **INTEGRATION_VERIFIED (`digitize`)** — M2 PG mock online + webhook settle; production live **disabled**; manual card IV **pending** | API-08 |
| GAP-API09-002 | SaaS INV (extras) | PA/OA | Tax invoice issue | Invoice scaffold **Implemented**; **`issue` fail-closed** | Professional pack **2026-11-09** `GAP-API09-002_STATUTORY_INVOICE_PROFESSIONAL_APPROVAL_PACK_2026-11-09.md` + registry §9 | Cannot issue statutory SaaS invoices | P0–P1 | SAAS_INVOICE registry §8–§9 | Accountant/legal complete §9 + product owner sign-off | Issued tax invoice PG IV | **Blocked (product + legal)** — **AWAITING_LEGAL_OR_ACCOUNTING_APPROVAL** | SaaS invoice §9 |

---

## P1 — Core product completion

### API-01 / Platform

| Gap ID | Module | Missing | Pri | Status | Notes |
| --- | --- | --- | --- | --- | --- |
| GAP-API01-001 | API-01 | Flutter for settings/flags/maintenance/releases/health/security/report executions | P1 | **INTEGRATION_VERIFIED** (local `digitize` governance IV 2026-11-07) | Flutter `/platform/console` **TESTED**; `test_platform_admin_governance_digitize_postgres.py` — org PENDING, PA/tenant auth boundaries; full API-01 path batch still `digitize_test` |
| GAP-API01-002 | API-01 | Shared-env PA certification | P1 | **BLOCKED** / **AWAITING_AUTHORIZATION** | EQ-011 / `digitize_test` / shared QA — unchanged Phase 10 |

### API-02 / Onboarding / T&C

| Gap ID | Module | Missing | Pri | Status | Notes |
| --- | --- | --- | --- | --- | --- |
| GAP-API02-001 | ORG-TERMS | Shared-env T&C CMS + OA accept E2E | P1 | **INTEGRATION_VERIFIED (local `digitize`)** | `tests/organization/test_org_terms_digitize_postgres.py` — `DIGITIZE_ORG_TERMS_PG_TEST=1`; published `platform.terms_document` row |
| GAP-API02-003 | API-02 | DR-023 hierarchy residual cutover verification | P1–P2 | **Closed — INTEGRATION_VERIFIED 2026-11-07** | Read-only IV on local `digitize` (**4 passed**); no schema/data changes; re-run supersedes 2026-11-04 evidence. |

### API-03 Identity

| Gap ID | Module | Missing | Pri | Status | Notes |
| --- | --- | --- | --- | --- | --- |
| GAP-API03-001 | API-03 | Flutter role-assignment + access scopes + permissions | P1 | **Implemented** 2026-11-03 | Staff details IAM panel (DEV-19 Phase 1) |
| GAP-API03-002 | API-03 | Flutter activate + credential-reset | P1 | **Implemented** 2026-11-03 | Staff lifecycle actions |

### API-04 / Integrations

| Gap ID | Module | Missing | Pri | Status | Notes |
| --- | --- | --- | --- | --- | --- |
| GAP-API04-001 | API-04 | OTP against real SMS QA | P1 | Blocked (provider) | See GAP-INT-001 |
| GAP-INT-002 | Integrations | Email/FCM production credentials & QA | P1 | **App prepared — provider QA** | `CommunicationService` + `SesNotificationDeliveryProvider`; SMTP/Mailpit/HELD unchanged — evidence `GAP-INT-001-002_COMMUNICATION_CONSOLIDATION_2026-11-09.md` |

### API-05 Membership

| Gap ID | Module | Missing | Pri | Status | Notes |
| --- | --- | --- | --- | --- | --- |
| GAP-API05-002 | API-05 | Flutter renew / upgrade / downgrade | P1 | **Implemented** 2026-11-03 (Flutter + ACTIVE invoice path; focused checks) | Backend Implemented |
| GAP-API05-005 | API-05 | Live membership lifecycle E2E | P1 | **Integration-verified** (local `digitize` 2026-11-03) | EQ-011 HTTP | |

### API-06 / UI discoverability

| Gap ID | Module | Missing | Pri | Status | Notes |
| --- | --- | --- | --- | --- | --- |
| GAP-UI-001 | Flutter shell | Attendance in AppShell nav | P1 | **Implemented** 2026-11-03 | `/attendance` entry |
| GAP-JRN-006 | Journey 6 | Discoverable attendance journey | P1 | **Connected (Flutter TESTED)** | Shell nav + `/attendance` entry (single-facility redirect, multi picker) — `attendance_entry_page_test.dart`, `operational_shell_nav_test.dart`; facility **Attendance desk** CTA unchanged; OTP provider still GAP-INT-001 |
| GAP-API06-003 | API-06 | Desk reports live E2E | P1 | **INTEGRATION_VERIFIED 2026-11-07** | Re-run `test_attendance_desk_digitize_postgres.py` (eligibility → check-in/out → reports → walk-in identify) | |
| GAP-API06-004 | API-06 | Attendance OTP/QR provider QA | P1 | Blocked (provider) | |

### API-07 Training

| Gap ID | Module | Missing | Pri | Status | Notes |
| --- | --- | --- | --- | --- | --- |
| GAP-API07-001 | API-07 | List enrollments API + UI reload | P1 | **INTEGRATION_VERIFIED (local `digitize`)** 2026-11-09 | Additive GET; not in 228 |
| GAP-API07-002 | API-07 | Facility/site schedule conflict enforcement | P1 | **INTEGRATION_VERIFIED (local `digitize`)** sequential PG; **concurrency NOT VERIFIED** — `digitize_trainer_concurrency` missing | NULL-site rule documented |
| GAP-API07-004 | API-07 | Live training E2E / DB | P1 | **INTEGRATION_VERIFIED 2026-11-07** | Re-run `DIGITIZE_TRAINING_PG_TEST=1` — workflows A–F **1 passed**; site-aware customer create for DR-023 facility sites; GAP-API07-003 Flutter wiring re-verified. |

### API-08 Billing

| Gap ID | Module | Missing | Pri | Status | Notes |
| --- | --- | --- | --- | --- | --- |
| GAP-API08-001 | API-08 | Charges calculate (002) | P1 | **INTEGRATION_VERIFIED** | HTTP PG IV `test_billing_m2_http_digitize_postgres.py` (`DIGITIZE_BILLING_HTTP_INTEGRATION_PG_TEST=1`) |
| GAP-API08-002 | API-08 | Discounts (003) | P1 | **INTEGRATION_VERIFIED** | Same HTTP PG IV module (DRAFT line scope) |
| GAP-API08-003 | API-08 | Taxes (004) | P1 | **INTEGRATION_VERIFIED** | Same HTTP PG IV module (facility tax settings, DRAFT only) |
| GAP-API08-005 | API-08 | Credit notes (007) | P1 | **INTEGRATION_VERIFIED** | HTTP PG IV: `test_billing_credit_receipt_recon_http_digitize_postgres.py` (`DIGITIZE_BILLING_HTTP_INTEGRATION_PG_TEST=1`) |
| GAP-API08-009 | API-08 | Live-DB verification of Phase-1 ops | P1 | **Integration-verified** | **2026-11-04** — `test_billing_invoices_revenue_live_digitize.py` on local `digitize`: baseline/delta revenue checks (isolates TAG fixture from pre-existing Acme facility payments); TAG-only cleanup in `finally`; 2× pass. Refunds/history/outstanding/offline/cancel/report paths unchanged. |
| GAP-JRN-008 | Journey 8 | Complete facility billing journey | P1 | **SANDBOX_CONNECTED (mock + SDK)** | Outstanding panel Pay online → mock dialog **or** `CheckoutGateway` sandbox; refreshes billing surfaces; production pay **blocked** |

### API-09 / SaaS

| Gap ID | Module | Missing | Pri | Status | Notes |
| --- | --- | --- | --- | --- | --- |
| GAP-API09-003 | API-09 extras | Razorpay live + webhook QA | P1 | **SANDBOX_CONNECTED (code)** | PG + SaaS webhook **Tested**; **manual sandbox card checkout NOT executed** (2026-11-08); real order API ok |
| GAP-API09-005 | API-09 | Cheque bounce → grace → auto-suspend + PA override | P1 | **Dev deployed (2026-11-09)** | Local DB **`digitize`**: Alembic **084** applied; worker verified (0 due); no dev cron; QA/prod/`digitize_test` pending — evidence § Development deployment verification. |
| GAP-API09-006 | API-09 | Facility-addition proration | P2 | **Integration-verified** | INV-005 on local `digitize` — `test_facility_proration_postgres.py` with `DIGITIZE_PRORATION_PG_TEST=1`; unit `test_facility_addition_proration.py`. |

### API-10 Notifications

| Gap ID | Module | Missing | Pri | Status | Notes |
| --- | --- | --- | --- | --- | --- |
| GAP-API10-001 | API-10 | Real SMS provider | P1 | Blocked (provider) | Alias GAP-INT-001 |
| GAP-API10-002 | API-10 | Email/WhatsApp/FCM env QA | P1 | Provider QA | |
| GAP-API10-003 | API-10 | Flutter campaign / staff notification admin | P1 | **INTEGRATION_VERIFIED 2026-11-07** | Flutter remote wiring + unit tests retained; PG HTTP IV **8 passed** (`DIGITIZE_FLUTTER_SURFACES_PG_TEST=1`). Send/deliver/retry (016–019) still omitted by design. Provider Stages 2–3 unchanged. |

### API-11 Reports

| Gap ID | Module | Missing | Pri | Status | Notes |
| --- | --- | --- | --- | --- | --- |
| GAP-API11-001 | API-11 | Schedule delivery notifier | P1 | **Blocked (provider)** | Calculation + `run_due_schedules` **IMPLEMENTED**; default `HeldReportNotifier` records `HELD` (not SENT). **TESTED** Phase 9 — `test_report_schedule_worker.py`, worker rules in `test_reporting_decisions.py`, mig **039** SQL IV. Live SMTP/SES **AWAITING_AUTHORIZATION** (GAP-INT-002) |
| GAP-JRN-011 | Journey 11 | Scheduled report delivery | P1 | **Partial — Flutter TESTED 2026-11-08** | Schedule panel + HELD delivery notice (`schedule_delivery_held_notice`); worker/email still **GAP-API11-001** / **GAP-INT-002**; no list-recipients/delivery-runs API in 228 |

### API-12 Support

| Gap ID | Module | Missing | Pri | Status | Notes |
| --- | --- | --- | --- | --- | --- |
| GAP-API12-001 | API-12 | Escalate migration + route + Flutter | P1 | **Implemented — INTEGRATION_VERIFIED 2026-11-09** | GAP approved **history-only Phase 1**; mig **083**; `escalate.ticket` (OA + SUPPORT_AGENT); PG escalate **3** + lifecycle **1**; Flutter panel **4** + pages **11**; proposal `API-12_008_Escalate_Migration_Proposal.md` |
| GAP-JRN-012 | Journey 12 | Support lifecycle incl. escalate | P1 | **INTEGRATION_VERIFIED 2026-11-09** | Lifecycle + agent workspace + **active** escalation panel (`escalate.ticket`); PG **4** support IV on `digitize`; Flutter **15** (tickets + escalation) |

### API-13 / API-14

| Gap ID | Module | Missing | Pri | Status | Notes |
| --- | --- | --- | --- | --- | --- |
| GAP-API13-002 | API-13 | Security event store (004) | P1 | Deferred / Blocked | |
| GAP-API13-003 | API-13 | Investigations (006) | P1 | Blocked (schema) | |
| GAP-API13-005 | API-13 | Policies + violations (010/011) | P1 | Blocked (schema) | |
| GAP-API14-001 | API-14 | Countries/states GMD seeds (001/002) | P1 | Deferred by product decision | |
| GAP-API14-003 | API-14 | Activity-type ownership (007) | P1 | Deferred by product decision | |

### Roles / QA

| Gap ID | Module | Missing | Pri | Status | Notes |
| --- | --- | --- | --- | --- | --- |
| GAP-ROLE-001 | Flutter roles | Site Admin distinct nav/policy | P1 | **Implemented (Flutter TESTED)** | `_showCompanyAccountNav` hides org billing/profile for Site Admin; sidebar label **Site Admin** — `operational_shell_nav_test.dart` |
| GAP-QA-001 | QA | EQ-011 live on digitize_test | P1 | Awaiting authorization | TEST-13 |
| GAP-AUTH-001 | Auth | Documented idle-timeout / last-PA matrix verification evidence | P1 | **Verified 2026-11-08** | Idle on **refresh** via `last_activity_at`; access JWT hot path unchanged per AUTH_CONTRACT_FREEZE. Evidence: `evidence/GAP-AUTH-001_session_idle_timeout_2026-11-08.md`; unit **18** + PG **`digitize`** **6** passed |

---

## P2 — Important completeness

| Gap ID | Module | Summary | Pri | Status |
| --- | --- | --- | --- | --- |
| GAP-API02-002 | T&C | Existing-org reacceptance | P2 | Deferred by product decision |
| GAP-API02-004 | API-02 | Media operational polish | P2–P3 | Partial |
| GAP-API02-005 | API-02 | Governance timeline UX depth | P3 | **Implemented (Flutter TESTED 2026-11-08)** | Paginated `governance-timeline` section (load more, retry); refresh after lifecycle; evidence `evidence/GAP-API02-005_governance_timeline_ux_2026-11-08.md` |
| GAP-API03-003 | API-03 | Flutter staff activity | P2 | **Implemented** 2026-11-03 | `StaffActivityPanel` on details |
| GAP-API03-004 | API-03 | Dedicated staff get-by-id | P2 | **Implemented (client)** | **2026-11-03** | Paginated API-03-012 lookup + staff-code search; `staff_directory_lookup_test.dart`. No new numbered API. |
| GAP-API04-002 | API-04 | Shared-env CRM IV | P2 | **Integration-verified** | **2026-11-03** — `test_customer_crm_digitize_postgres.py` + `customer_digitize_pg_guard.py` on local `digitize`. |
| GAP-API05-003 | API-05 | Flutter transfer / expire | P2 | **Implemented** 2026-11-03 (Flutter + focused tests) | Backend Implemented |
| GAP-API05-004 | API-05 | Freeze date-range / billing coupling | P2 | Deferred by product decision |
| GAP-API06-001 | API-06 | Walk-in identify Flutter | P2 | **INTEGRATION_VERIFIED 2026-11-07** | Flutter **1** walk-in identify test + PG `POST /walkin-visits/identify` in desk IV | |
| GAP-API06-002 | API-06 | Session + PATCH remarks + audit UI | P2 | **INTEGRATION_VERIFIED 2026-11-07** | Flutter **6** remarks tests + PG PATCH API-06-006 + GET audit in desk IV | |
| GAP-API07-003 | API-07 | Capacity/rules/progress dedicated Flutter | P2 | **INTEGRATION_VERIFIED 2026-11-07** | Flutter **2** widget tests + remote wiring (production env); backend rules/progress in GAP-API07-004 PG suite — **skipped re-implementation**. |
| GAP-API07-005 | API-07 | Catalog extras vs numbered SoT clarity | P3 | Docs |
| GAP-API08-004 | API-08 | Adjustments (**catalog API-08-005**) | P2 | **Deferred** — no adjustment entity; distinct from API-08-009 online pay (see GAP-API08-006) |
| GAP-API08-007 | API-08 | Receipts (012) | P2 | **INTEGRATION_VERIFIED** | Same HTTP PG IV module; bulk historical backfill execute still **AWAITING_AUTHORIZATION** |
| GAP-API08-008 | API-08 | Reconciliations (014) | P2 | **INTEGRATION_VERIFIED** | Same HTTP PG IV module (mig **082**) |
| GAP-API09-001 | API-09 | Flutter for numbered subscription/license admin | P2 | **INTEGRATION_VERIFIED 2026-11-07** | Admin slice unchanged; PG IV covers `subscriptions/reports`, `licenses/reports`, `subscriptions/{id}/history`. Route-order fix for `licenses/reports`. Live Razorpay remains GAP-API09-003. |
| GAP-API10-005 | API-10 | Inbox ≠ staff API-10 surface | P2 | **INTEGRATION_VERIFIED 2026-11-07** | Staff HTTP paths in Phase 5 IV; inbox separation tests unchanged (**7 passed**). |
| GAP-API11-002 | API-11 | PDF export unavailable | P2 | **Implemented (UI/doc)** | API-11 exports are HTML, Excel, CSV per catalogue only; backend rejects PDF. Flutter **Reports** page: capability panel, catalogue subtitles, no PDF control, entitlement note. **Tested** (21 reporting tests). Not integration-verified. Future PDF needs approved backend renderer (out of 228). |
| GAP-API11-003 | API-11 | Live reporting certification | P2 | **Integration-verified** | Local `digitize` ASGI 2026-11-03. HTTP export **200** HTML bytes with temporary Advanced Reporting entitlement (`advanced_reporting_entitlement_helpers.py`); prior 403/422/404 harness regressions retained. Evidence: `test_reports_export_http_digitize.py` (5 passed with `DIGITIZE_REPORTS_EXPORT_HTTP_TEST=1`). |
| GAP-API12-002 | API-12 | Live org-scoped ticket suite | P2 | **Integration-verified** | **2026-11-03** + **reconfirmed 2026-11-08** — `test_support_tickets_digitize_postgres.py` **1 passed** on local `digitize`; API-12-008 not in scope. |
| GAP-API13-004 | API-13 | Compliance reports / archive | P2 | Deferred |
| GAP-API13-006 | API-13 | Phase-1 reads live DB IV | P2 | **Integration-verified** | **2026-11-03** + **reconfirmed 2026-11-08** — `test_audit_reads_digitize_postgres.py` **4 passed** on local `digitize`. |
| GAP-API14-002 | API-14 | Languages/timezones | P2 | Deferred |
| GAP-API14-004 | API-14 | Localization SoT | P2 | Deferred |
| GAP-ROLE-002 | Roles | Confirm PA ops exclusion intentional | P2 | Product confirm |
| GAP-ROLE-003 | Roles | PA audit nav absent | P2 | **INTEGRATION_VERIFIED 2026-11-08** | Flutter nav + `report.view` (11 widget tests, 2026-11-03); backend PA scoped audit PG **8 passed** (`test_audit_*_digitize_postgres.py`); governance `require_governance_organization_access`; evidence `evidence/GAP-ROLE-003_platform_admin_audit_reads_2026-11-08.md` |
| GAP-UI-002 | Flutter DI | Mixed mock/remote in development | P2 | **Closed — INTEGRATION_VERIFIED** | Facility, staff, walk-in, training-ops, **membership**, **trainer**, **push device-token**, **in-app inbox** always remote; auth mock = explicit `AppEnvironment.development()` only; tests `operational_provider_environment_test.dart` |
| GAP-INT-003 | Storage | Default disabled storage | P2 | Config |
| GAP-INT-004 | Payments | Razorpay live vs mock dual-path QA | P2 | **INTEGRATION_VERIFIED (`digitize`)** — PG M2 + SaaS webhook concurrency; mock forced in IV; manual card QA optional |
| GAP-JRN-007 | Journey 7 | Enrollment list + facility conflicts | P2 | **INTEGRATION_VERIFIED (local `digitize`)** 2026-11-09 | GAP-API07-001/002; facility concurrency PG **pending** `digitize_trainer_concurrency` |
| GAP-JRN-010 | Journey 10 | Outbound notification completeness | P2 | **Partial — Flutter TESTED 2026-11-08** | Personal inbox controller (pagination, mark-read guards); campaign admin retained (local index + lifecycle); manual WhatsApp vs launch gated; **provider QA/SMS/live send** still GAP-INT-001 / GAP-API10-001…002 |
| GAP-AUTH-002 | Auth | Continuous PA DEK/impersonation regression suite | P2 | **Implemented 2026-11-08** (+ **DR-021 hardening**) | Regression suite; customer deny; residual `require_tenant_operational_*` + facility/site deny — `evidence/DR-021_tenant_operational_hardening_2026-11-08.md` |

### Cross-cutting — transaction safety (AUDIT-TXN-2026-11-03)

| Gap ID | Module | Finding | Pri | Class | Status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| GAP-TXN-001 | API-08 | Offline payment success without invoice row lock | P1 | **GAP → Fixed** | **Implemented 2026-11-03** | `get_invoice_for_update` + outstanding validation in `OfflinePaymentService.record`. Tests: `test_offline_payment_invoice_lock.py` (8 passed with opt-in PG on local `digitize`). **Not** GAP-TXN-004 full concurrency IV. |
| GAP-TXN-002 | Test / IV | `get_session` override skips UoW commit | P2 | **Implemented** | **2026-11-03** | Shared `tests/api/asgi_session_helpers.py`; 5 unit stubs standardized; integration/cert use production `get_session`. Evidence: `docs/16_Development_Readiness/evidence/GAP-TXN-002_session_override_inventory.md`; regression `test_get_session_uow_lifecycle.py` (4 unit + opt-in IV). GAP-API11-003 harness fix retained. |
| GAP-TXN-003 | API-03 | Post-commit email vs identity txn | P2 | **Implemented** | **2026-11-03** | By design: identity + outbox commit in request txn; delivery post-commit. **Recovery:** outbox FAILED + open reset row synced to FAILED; re-issue consumes prior tokens. Prod: `email/service.py` sync. Tests: `test_credential_email_txn003.py`. **Limitation:** no background retry of failed outbox rows. |
| GAP-TXN-004 | API-08 / API-09 / API-10 | Concurrent payment/webhook IV | P2 | **Integration-verified** | **2026-11-03** | PG IV + webhook IntegrityError duplicate path; **rollback scope verified** — event insert precedes business mutations; production webhook route has no prior session writes (see matrix rollback section). |
| GAP-TXN-005 | Scaffold | `UserRepository.create` self-commits | P3 | **Resolved** | **2026-11-03** scaffold flush-only fix; **2026-11-04** entire `app/modules/users/` removed (GAP-API03-005). |

Evidence summary: `docs/16_Development_Readiness/evidence/AUDIT-TXN-2026-11-03_summary.md`. DEV-19 session log **AUDIT-TXN-2026-11-03**.

---

## P3 — Enhancement / documentation

| Gap ID | Summary | Status |
| --- | --- | --- |
| GAP-API01-003 | Catalog COLLECTION_META Flutter blurbs stale | **Closed — TESTED 2026-11-09** (re-verified; registry §10 aligned) |
| GAP-API03-005 | Retire legacy `/users` scaffold | **Closed — TESTED 2026-11-09** (re-verified; `app/modules/users/` absent; `test_legacy_users_scaffold_removed.py` **4 passed**) |
| GAP-API08-010 | Catalog FE metadata lag for billing UI | **Closed — TESTED 2026-11-09** (API-08 `frontend_status` PARTIAL; not op API-08-010 backend row) |
| GAP-API09-004 | Catalog FE + outdated API-09 gate doc | **Closed — TESTED 2026-11-09** (gate doc + PARTIAL metadata) |
| GAP-API10-004 | Catalog database_gap flag on 024 vs live preferences | **Closed — TESTED 2026-11-07** | Removed stale `DATABASE_GAP_IDS` entry; entity `customer.customer_preference` (004); route live. |
| GAP-API11-004 | Catalog FE NOT_STARTED despite reporting UI | **Closed — TESTED 2026-11-09** (INTEGRATED + reporting path) |
| GAP-API12-003 | Extra chat/FAQ beyond numbered 12 | Scope clarity |
| GAP-API13-001 | Confirm non-client capture POST stance | **Deferred (product)** — Phase 13: no client routes; reconcile in [API-13 acceptance](../07_API_Collections/API-13_Acceptance_Evidence.md); formal product sign-off still open |
| GAP-API13-007 | Optional audit.events.view alias | Enhancement |
| GAP-API14-005 | Flutter prefers extras over `/reference` | Acceptable |
| GAP-API14-006 | Do not alias facility-types via GMD | Rule |
| GAP-UI-003 | Mock checkout host when Razorpay UI absent | **Closed — IMPLEMENTED** | `MockCheckoutHost` only when `AppEnvironment.development()` mock mode (`app_shell.dart`) |
| GAP-JRN-001 | T&C reacceptance (dup of API02-002) | Deferred |
| GAP-API02-004 | Media polish | Partial |

---

## Grouping by module (quick index)

- **Auth:** GAP-AUTH-001, GAP-AUTH-002  
- **API-01:** GAP-API01-*  
- **API-02 / T&C:** GAP-API02-*, GAP-JRN-001  
- **API-03:** GAP-API03-*  
- **API-04:** GAP-API04-*, GAP-INT-001  
- **API-05:** GAP-API05-*  
- **API-06:** GAP-API06-*, GAP-UI-001, GAP-JRN-006  
- **API-07:** GAP-API07-*, GAP-JRN-007  
- **API-08:** GAP-API08-*, GAP-JRN-008  
- **API-09:** GAP-API09-*  
- **API-10:** GAP-API10-*, GAP-JRN-010  
- **API-11:** GAP-API11-*, GAP-JRN-011  
- **API-12:** GAP-API12-*, GAP-JRN-012  
- **API-13:** GAP-API13-*  
- **API-14:** GAP-API14-*  
- **Roles/UI/INT/QA:** GAP-ROLE-*, GAP-UI-*, GAP-INT-*, GAP-QA-001  
- **Cross-cutting txn:** GAP-TXN-*  

---

## Explicit non-gaps (recognize completed work)

Do not reopen without new defect evidence:

- API-04 Customer 12/12 backend + Flutter CRM + registration OTP extras (memory/none SMS); GAP-API04-002 PG IV. Live SMS QA remains GAP-API04-001 / GAP-INT-001 only.  
- API-05 freeze/resume/cancel backend + Flutter (Phase 1).  
- API-06 attendance desk + reports + walk-in charge/pay path.  
- API-07 batch enroll/remove + batch/PTR schedule-conflict UX (trainer-level).  
- API-08 offline collect, refund, invoice cancel, outstanding (Phase 1).  
- API-09 numbered 24/24 backend + SaaS checkout extras UI.  
- Auth login/refresh/logout/session-backed principal model.  
- DR-021 onboarding + ORG-TERMS-001…006 + OA acceptance + PA T&C CMS + mig 072 on local digitize.  

---

## Change log

| Date | Note |
| --- | --- |
| 2026-11-07 | Phase 7 API-07 IV: GAP-API07-004 re-run **1 passed** on `digitize`; site resolution for customer create; GAP-API07-003 Flutter wiring test. |
| 2026-11-07 | Phase 6 attendance desk IV: GAP-API06-001…003 — extended `test_attendance_desk_digitize_postgres.py` **2 passed**; billing ORM metadata + IV bootstrap site/customer alignment. |
| 2026-11-07 | Phase 5 Flutter/backend IV: GAP-API10-003, GAP-API10-005, GAP-API09-001 — `test_flutter_surfaces_digitize_postgres.py` **8 passed**; comms route fixes + `licenses/reports` ordering. |
| 2026-11-07 | GAP-API10-004: `notification_preferences_update` removed from `DATABASE_GAP_IDS`; catalog DB entity `customer.customer_preference`; regression `test_notification_preferences_update_not_marked_database_gap_api10_004`. |
| 2026-11-07 | Phase 3 engineering gaps: catalog FE metadata re-verified (API01-003, API08-010, API09-004, API11-004); users scaffold absent; DR-023 PG IV **4 passed**; registry doc inventory reconciled (0 unmounted handlers). |
| 2026-11-07 | Phase 2 contract/metadata (N-05…N-08): `DATABASE_GAP_IDS` credit-note schema fix; `billing.*` registry reconciliation; OpenAPI op IDs aligned (API-05-003, 07-002, 08-011); J5 workflow map in DEV-22. |
| 2026-11-09 | **Pre-QA release** — security gate pass (targeted tests); WhatsApp webhook implemented; Meta live **pending**; AWS QA deploy **pending** ops. Evidence: `SECURITY_HARDENING_*`, `WHATSAPP_*`, `QA_DEPLOYMENT_*`, `BASIC_QA_TESTING_HANDOVER.md`. |
| 2026-11-09 | **Master 16-skeleton implementation pass** — `MASTER_16_SKELETON_IMPLEMENTATION_REPORT_2026-11-09.md`; **0/16** promoted; GAP-API08-004 (005 adjustments), GAP-API13-*, GAP-API14-* unchanged pending product/migration gates. |
| 2026-11-09 | Master **seven-area** closure — `MASTER_SEVEN_AREAS_CLOSURE_EXECUTION_2026-11-09.md`; API-08-012 verified; statutory/providers/skeletons/cheque/extras **await decisions**. |
| 2026-11-09 | Consolidated continuation — **no new authorized implementation**; master blockers unchanged except GAP-API12-001 / catalog / users scaffold closures this date. |
| 2026-11-09 | **GAP-API03-005** — legacy users scaffold retirement re-verified; no backend/Flutter consumers; API-03 identity routes intact. |
| 2026-11-09 | **GAP-API01-003 / 08-010 / 09-004 / 11-004** — registry §10 + gate doc aligned to `COLLECTION_META`; drift tests **3**; `validate_catalog()` clean. |
| 2026-11-09 | **GAP-API12-001** — history-only escalate Phase 1; PG **4**; Flutter escalation **4**; catalog API-12-008 **BACKEND_IMPLEMENTED**. |
| 2026-11-09 | **Phase 7 closure (080–082)** — reconcile only; **10** migration/balance + **1** PG credit/recon HTTP passed on `digitize`; frozen billing rules unchanged; **no** further implementation until master-blocker approval. |
| 2026-11-09 | Payment **lifecycle verification** doc + targeted regression (PG M2, offline lock, cheque guards, Flutter flow); sandbox capture still open. |
| 2026-11-09 | Flutter **online/offline channel selection** before Razorpay; harness docs clarify bypass; sandbox payment still incomplete. |
| 2026-11-08 | Manual sandbox **result audit** — orders tied to `sbox-e2e-INV` OK; **cancelled**, Razorpay **0** captures; invoice stays **ISSUED**; no verify/webhook success. |
| 2026-11-08 | Razorpay **device verification (partial)** — Checkout Test Mode + UPI QR + method tiles; cancel + invalid webhook on live API; capture/verify/webhook/Android **not** done (iframe, no tunnel, no device). |
| 2026-11-08 | Payment method coverage review — API-08 offline/cheque/cash unchanged; Razorpay UPI display config; Flutter collection UX; evidence `PAYMENT_METHOD_COVERAGE_2026-11-08.md`. |
| 2026-11-08 | Sandbox **order + Checkout Test Mode** verified; **payment settle / Flutter / inbound webhook not completed** — see evidence verification matrix. |
| 2026-11-08 | Manual sandbox E2E **not completed** — preflight: `.env` mode≠sandbox, no Flutter/webhook URL; probe: Razorpay order ok, payment REST 401; see evidence § Manual. |
| 2026-11-08 | Razorpay PG IV on `digitize` — M2 billing HTTP + webhook settle + SaaS webhook concurrency; M2 harness `RAZORPAY_MODE=mock`; evidence updated; GAP-API08-006 / GAP-INT-004 → **INTEGRATION_VERIFIED** (no card charge). |
| 2026-11-08 | Razorpay sandbox slice — facility gateway from settings, webhook→facility settlement, Flutter SDK path; evidence `RAZORPAY_SANDBOX_INTEGRATION_2026-11-08.md`; GAP-INT-004 / GAP-API08-006 / GAP-API09-003 / GAP-JRN-008 → **SANDBOX_CONNECTED** (no card charge). |
| 2026-11-08 | API-08 M2 HTTP PG IV — `test_billing_m2_http_digitize_postgres.py` **1 passed** with `DIGITIZE_BILLING_HTTP_INTEGRATION_PG_TEST=1` (002/003/004/009 mock online); GAP-API08-001…003 **INTEGRATION_VERIFIED**; GAP-API08-006 clarified as **API-08-009** (not 005). |
| 2026-11-08 | API-12-008 — `SupportTicketEscalationService` + `test_escalation_service.py` (**3 passed**); route still skeleton (GAP-API12-001). |
| 2026-11-08 | Membership facility-details grid — `DetailsSectionGrid` top-align pairs; routing test + **79** `membership_plan/` widget tests **passed**. |
| 2026-11-09 | Final QA cutover — local `digitize` mig **088**; security-event auth PG green; Terraform plan unblocked (IAM count); **GAP-QA-001** unchanged (**digitize_test@083**, TEST-13); QA deploy **not executed** — `CONSOLIDATED_FINAL_QA_CUTOVER_REPORT.md`. |
| 2026-11-08 | API-08 M2 routes — promoted **002, 003, 004, 009** (mock online); **005** remains skeleton; pytest billing/api contract **32 passed** in focused bundle. |
| 2026-11-08 | API-13 Phase 13 — GAP-API13-006 reconfirmed (**4** PG IV); client ingest still gated; `API-13_Acceptance_Evidence.md`; no production changes. |
| 2026-11-08 | API-12 Phase 12 — GAP-API12-002 reconfirmed (**1** PG IV); GAP-API12-001 unchanged; `API-12_Acceptance_Evidence.md`; no production changes. |
| 2026-11-08 | Cross-module Flutter — facility-scoped membership billing deep link + panel `facilityId`; JRN-006/JRN-008/GAP-ROLE-001 widget tests (**39+2+3** in touched suites). |
| 2026-11-08 | GAP-JRN-011 — report schedule delivery panel (GET/POST schedules, recipients, DELETE recipient); Flutter tests **28 passed** under `test/features/reporting/`. |
| 2026-11-08 | GAP-JRN-008 — facility outstanding **Pay online (mock)** (API-08-009) + billing surface refresh; Flutter **15 passed** (`facility_outstanding` + mock dialog); PG online path covered by existing `test_billing_m2_http_digitize_postgres.py`. |
| 2026-11-08 | Second-installment OA billing tracking — invoice list metadata + obligation-derived due dates; PG `test_subscription_history_metadata_digitize_postgres.py` **3 passed** on `digitize`; Flutter **8 passed**. |
| 2026-11-08 | API-09-011 enrichment — history `metadata.subscription` + OA billing/lifecycle links; Flutter **6 passed** (`subscription_admin_controller_test.dart`); live API test not run (`digitize_test` guard). |
| 2026-11-08 | EQ-011 local green — 73 passed subscription+catalog IV on `digitize_test`; Mailpit delivery IV; `EQ011_POST_MIGRATION_RECONCILIATION_2026-11-08.md`. |
| 2026-11-08 | Master approval execution — escalation 083, Mailpit resolver, digitize_test→083, SMS deferred; `MASTER_APPROVAL_EXECUTION_REPORT_2026-11-08.md`. |
| 2026-11-08 | Master blockers — consolidated approval package; local dev scope closed; eq011 preflight head `082`. |
| 2026-11-08 | GAP-API02-005 — governance timeline pagination + retry (Flutter **2 passed**). |
| 2026-11-08 | GAP-ROLE-003 — PA scoped audit PG IV **8 passed**; governance org access helper. |
| 2026-11-08 | GAP-JRN-011 — HELD delivery notice on schedule card. |
| 2026-11-08 | GAP-JRN-012 — agent workspace Flutter + `routes_center` pagination fix; PG IV inbox/queue/GET ticket; Flutter **15 passed**; escalate still GAP-API12-001. |
| 2026-11-08 | GAP-JRN-012 — Flutter support ticket lifecycle (`getTicket` detail reload, pagination, conversation preview); **11 passed** `support_ticket_pages_test.dart`; escalate still GAP-API12-001. |
| 2026-11-08 | GAP-JRN-010 — `InAppInboxController` + inbox/campaign widget tests (**22 passed** in `in_app_notifications/`, `campaign/`, `notification_surface_separation`). |
| 2026-11-07 | API-09 Phase 11 — lifecycle regression **139+16 PG passed**; Flutter **38 passed**; GAP-API09-002/005 **BLOCKED**; GAP-API09-003 **AWAITING_AUTHORIZATION**; GAP-API09-006/001 reconfirmed. |
| 2026-11-07 | API-01 Phase 10 — governance IV on local `digitize` **2 passed**; GAP-API01-001 **INTEGRATION_VERIFIED** (governance); GAP-API01-002 **BLOCKED** (EQ-011/QA); `API-01_Acceptance_Evidence.md`. |
| 2026-11-07 | API-11 Phase 9 — schedule worker delivery semantics **TESTED**; exports/sql IV reconfirmed; GAP-API11-001 remains **BLOCKED (provider)**; evidence `docs/07_API_Collections/API-11_Acceptance_Evidence.md`. |
| 2026-11-07 | API-08 Phase 8 — API-08-018 effective outstanding **TESTED** (`test_credit_note_financial_balance.py`); receipt backfill **TESTED** (`test_receipt_backfill_service.py`); billing unit **56 passed**; GAP-API08-009 live IV **1 passed**; no skeleton promotion. |
| 2026-11-07 | API-08 WIP stabilization — billing unit **47 passed**; GAP-API08-009 IV cleanup fixed for 077+ tables; Alembic head **082** + migration metadata tests; API-08-016 Phase 2 / outstanding effective balance unchanged in product scope. |
| 2026-11-07 | API-04 module gap-closure verification — no new engineering gaps; GAP-API04-002 PG IV re-run **pass**; GAP-API04-001 / GAP-INT-001 remain provider-blocked. |
| 2026-11-04 | GAP-API08-009 billing PG IV closed — baseline/delta revenue assertions + TAG cleanup; 2× pass on local `digitize`. |
| 2026-11-03 | Initial register from DEV-20 assessment. No implementation. |
| 2026-11-03 | GAP-TXN-001 remediated — invoice FOR UPDATE + outstanding validation. |
| 2026-11-03 | Bottom-up route source inventory — 366 source declarations, 362 v1 HTTP registered; see ROUTE_SOURCE_INVENTORY evidence + `scripts/route_source_inventory.py`. |
| 2026-11-03 | GAP-API11-003 export-byte IV; GAP-API13-006, GAP-API12-002, GAP-API04-002 PG IV on local digitize. |
| 2026-11-09 | Master closure — `MASTER_DEVELOPMENT_CLOSURE_AND_DEPENDENCY_HANDOVER_2026-11-09.md`; GAP-API05/07 PG verified; facility concurrency PG blocked on DBA. |

---

## Final dependency register (master closure 2026-11-09)

Authoritative consolidated backlog for **external** work only. Completed gaps are omitted. Full table: [MASTER_DEVELOPMENT_CLOSURE_AND_DEPENDENCY_HANDOVER_2026-11-09.md](./evidence/MASTER_DEVELOPMENT_CLOSURE_AND_DEPENDENCY_HANDOVER_2026-11-09.md) §3.

| Item | Current state | Dependency | Responsible | Next execution |
| --- | --- | --- | --- | --- |
| Facility concurrency PG | Partial | `digitize_trainer_concurrency` + Alembic | DBA / infra | `DIGITIZE_FACILITY_SCHEDULE_CONCURRENCY_PG_TEST=1` pytest module |
| GAP-API09-002 issue | Fail-closed | INV pack §9 sign-off | Legal / accounting / product | Remove blockers per approved registry only |
| Live SMS / OTP | Deferred | MSG91 + DLT / de-scope | Product + provider | Provider QA or defer launch |
| Live email / WA | Adapters only | SES / Meta credentials | Infra + provider | Delivery IV with creds |
| EQ-011 `digitize_test` | Blocked | TEST-13 migration auth | Product / DBA | `eq011` preflight + suite |
| API-13/14 skeletons (15+1 adj) | Skeleton | Product + schema per op | Product owner | Per-op promotion + mig |
| Manual Razorpay card | Optional QA | Human sandbox checkout | User | Not a code gate |
| Production certification | Not done | Deploy + shared QA | Ops / QA | Env-specific IV |

**Independently executable engineering:** **none remaining** without resolving a row above.
