# DEV-22 End-to-End Journey Matrix

**Document ID:** DEV-22  
**Assessment date:** 2026-11-03  
**Parent:** [DEV-20](./DEV-20_Comprehensive_Development_Gap_Assessment.md)  
**Gaps:** [DEV-21](./DEV-21_Development_Gap_Register.md)  

Status key: **Connected** · **Partial** · **Missing** · **Blocked** · **Deferred**

---

## J1 — Platform Admin onboarding (DR-021 + T&C)

| Field | Content |
| --- | --- |
| Starting point | PA login |
| Role | Platform Admin |
| Prerequisites | Seeded PA account; platform permissions; DB with org + terms tables |
| Screens | Login; Companies list/create; `/platform/terms*`; org governance/activate |
| Backend APIs | Auth; API-02 org create/list/activate; ORG-TERMS-001…006; ORG-ONBOARDING-ACCEPT-001 (OA side) |
| Business rules | PENDING → credential setup → T&C → PA review when required → ACTIVE; T&C alone does not activate if other gates fail |
| Completion outcome | ACTIVE organization with accepted current T&C version/hash |
| Missing links | Shared-env IV (GAP-API01-002 / EQ-011); existing-org reacceptance **Deferred** (GAP-API02-002) |
| Current status | **Connected** — local `digitize` governance IV **2026-11-07**; shared QA **Blocked** |
| Dependencies | Identity provisioning, email for credentials, mig 072 on env |

---

## J2 — Organization Admin setup

| Field | Content |
| --- | --- |
| Starting point | OA login / credential setup |
| Role | Organization Admin |
| Prerequisites | Org PENDING/ACTIVE per lifecycle; often SaaS subscription for operational nav |
| Screens | Org profile; branches/sites; facilities; staff; plans; checkout/billing |
| Backend APIs | API-02 facility/site; API-03 staff subset; API-09 extras SaaS checkout; membership plans extras |
| Business rules | Operational modules gated by lifecycle snapshot; PA review path when OA changes pending details |
| Completion outcome | Configured site/facility + staff + optional subscription |
| Missing links | Full IAM Flutter (roles/scopes); media polish |
| Current status | **Connected** (lifecycle-gated) |
| Dependencies | J1; API-09 SaaS; GAP-API03-001/002 |

---

## J3 — Membership product configuration

| Field | Content |
| --- | --- |
| Starting point | OA Plans nav |
| Role | Organization Admin |
| Prerequisites | Active org + permissions |
| Screens | `/plans*` create/edit |
| Backend APIs | Membership plan catalog extras (not the 12 numbered membership lifecycle ops) |
| Business rules | Plan pricing/eligibility as implemented in plan module; advanced product variants may still need product clarity |
| Completion outcome | Sellable plans available for customer membership create |
| Missing links | Product-variant depth (family/camp/happy-hour) — treat unclear rules as product decision if not in frozen docs |
| Current status | **Connected** for plan CRUD |
| Dependencies | Facility association rules |

---

## J4 — Customer management

| Field | Content |
| --- | --- |
| Starting point | Customers nav |
| Role | OA / staff with customer permissions |
| Prerequisites | Facility/site scope |
| Screens | Customer list/create/profile/history/docs/contacts |
| Backend APIs | API-04 + CUST-REG-OTP extras |
| Business rules | Duplicate detection / transfer / suspend per CRM implementation |
| Completion outcome | Verified customer profile usable for membership/attendance |
| Missing links | Real SMS OTP QA (GAP-INT-001 / GAP-API04-001) |
| Current status | **Partial** |
| Dependencies | SMS provider; PII encryption |

---

## J5 — Membership lifecycle

| Field | Content |
| --- | --- |
| Starting point | Customer profile membership section |
| Role | OA |
| Prerequisites | Customer + plan; invoice/offline pay for activate path |
| Screens | Create/activate; freeze/resume/cancel; open-by-id |
| Backend APIs | API-05-001/002/006/007/009/011/012; API-08 invoice/offline |
| Business rules | Phase-1 freeze without date-range billing coupling; cancel ≠ auto-refund; list-by-customer Deferred |
| Completion outcome | Membership in intended status with history |
| Missing links | List-by-customer (GAP-API05-001); renew/upgrade UI (GAP-API05-002) |
| Current status | **Partial** |
| Dependencies | J3, J4, API-08 Phase-1 |

### J5 workflow map (as implemented — 2026-11-07, N-08)

Approved **quotation → acceptance → issued invoice → payment → activation** is product-approved for a future slice (migrations **073** / quotation entities **not** in repo). **Phase-1 live path** below is what the code exercises today.

| Step | Requirement (logical) | Implemented operation(s) | Status |
| ---: | --- | --- | --- |
| 1 | Select customer + plan | API-04-005; membership plan list/get (API-05 plan module / extras) | **IMPLEMENTED** |
| 2 | Create membership sale | API-05-001 `memberships_create` | **IMPLEMENTED** / **TESTED** |
| 3 | Quotation / commercial offer | *(product F0 — not in 228)* | **DEFERRED** — no `membership_quotation` persistence |
| 4 | Customer/staff acceptance + schedule snapshot | *(product F0)* | **DEFERRED** |
| 5 | Issue membership invoice | API-08-001 `invoices_create` (membership plan snapshot, numbering mig **074**) | **IMPLEMENTED** / **INTEGRATION_VERIFIED** |
| 6 | Record payment (full outstanding Phase-1) | API-08-010 `payments_offline_create`; optional API-08-008 alias | **IMPLEMENTED** / **INTEGRATION_VERIFIED** |
| 6b | Verify payment before activate | API-08-011 `payments_status_list` | **IMPLEMENTED** — Flutter `verifyPaymentStatus` |
| 7 | Activate membership | API-05-002 `memberships_activate` (paid invoice validation) | **IMPLEMENTED** / **TESTED** |
| 8 | Lifecycle: freeze / resume / cancel / transfer / expire | API-05-006…009, 011, 012 | **IMPLEMENTED** — Flutter known-ID panel |
| 9 | Renew / upgrade / downgrade | API-05-003, 004, 005 | **IMPLEMENTED** backend; Flutter **PARTIAL** (GAP-API05-002) |
| 10 | Installment partial pay | Allocations / obligations (mig **077**); U12 full-pay unless accepted schedule | **PARTIAL** — schema + services; quotation acceptance **missing** |
| 11 | Credit note / wallet apply | `CreditNoteService` + mig **080**–**081**; API-08-007 `invoices_credit_notes` **BACKEND_IMPLEMENTED**; PG HTTP IV (credit + mig **082** recon in same module) | **INTEGRATION_VERIFIED** (local `digitize`); **Flutter / U7 formal** deferred; no new routes |

**Genuine functional gaps (not documentation):** quotation/acceptance entities (F0); list memberships by customer (DR-020 P1-009 **DEFERRED**); renew/upgrade/downgrade Flutter parity (GAP-API05-002).

---

## J6 — Attendance and walk-in

| Field | Content |
| --- | --- |
| Starting point | Facility details CTA → attendance desk (not shell) |
| Role | Facility staff / OA |
| Prerequisites | Eligible membership or walk-in admission config |
| Screens | Desk check-in/out; walk-in; reports panel |
| Backend APIs | API-06 check-in/eligibility/history/reports/walk-in; payments extras |
| Business rules | Duplicate check-in handling in service; frozen membership eligibility rules |
| Completion outcome | Recorded attendance or paid walk-in visit |
| Missing links | OTP provider (GAP-INT-001); walk-in identify polish |
| Current status | **Connected** (shell + entry + facility desk CTA; Flutter TESTED 2026-11-08) |
| Dependencies | J5; walk-in pricing; GAP-INT-001 |

---

## J7 — Trainer and activity management

| Field | Content |
| --- | --- |
| Starting point | Training operations / trainers nav |
| Role | OA / trainers per permissions |
| Prerequisites | Facility/site; trainer profiles |
| Screens | Trainers; activities; batches; PTR; conflict dialogs |
| Backend APIs | API-07 numbered ops + conflict enforcement |
| Business rules | Availability non-overridable; schedule conflict override permission-gated; facility/site conflicts Deferred |
| Completion outcome | Scheduled batch/PTR with enrollments and sessions |
| Missing links | List enrollments API (Deferred); facility/site conflicts (Deferred) |
| Current status | **Connected** / **Partial** |
| Dependencies | J2; API-06 for class attendance linkage |

---

## J8 — Billing and payments (facility)

| Field | Content |
| --- | --- |
| Starting point | Organization billing panels / membership pay |
| Role | OA |
| Prerequisites | Invoices from membership/walk-in |
| Screens | Outstanding; history; **Collect payment → Online (Razorpay) or Offline at facility**; refund; cancel |
| Backend APIs | API-08 Implemented subset |
| Business rules | Offline SUCCESS → refund path; PENDING cancel; no invented SUCCESS cancel |
| Completion outcome | Settled or refunded facility receivable (offline or verified online) |
| Missing links | Production Razorpay; API-08-005 adjustments deferred |
| Current status | **Lifecycle verified (mock/PG + Flutter channel flow)** — 2026-11-09 evidence; **live Razorpay capture, webhook tunnel, Android UPI Intent** pending |
| Dependencies | Product decisions for remaining 8 ops |

---

## J9 — Subscription and licensing (SaaS)

| Field | Content |
| --- | --- |
| Starting point | Org billing / checkout; PA SaaS plans |
| Role | OA + PA |
| Prerequisites | Plans catalog; Razorpay mock/live |
| Screens | Checkout; SaaS invoices; PA plan CMS |
| Backend APIs | API-09 numbered lifecycle (backend); SaaS extras for Flutter |
| Business rules | Facility-based SaaS billing frozen commercial rules; INV statutory blockers separate |
| Completion outcome | Active SaaS subscription / paid invoice |
| Missing links | Statutory invoice (GAP-API09-002); live Razorpay (GAP-API09-003); cheque automation (GAP-API09-005) |
| Current status | **Connected** — billing list shows second-installment due/amount/status from obligations; lifecycle admin + API-09-011 snapshot; PG **3 passed** + Flutter **8 passed** **2026-11-08** |
| Dependencies | GAP-API09-002/003/005 |

---

## J10 — Notifications and campaigns

| Field | Content |
| --- | --- |
| Starting point | In-app bell / inbox |
| Role | End user / staff |
| Prerequisites | Provider config |
| Screens | Inbox; push token registration |
| Backend APIs | `/me/notifications*` extras; API-10 numbered staff/campaign APIs |
| Business rules | Delivery retries per communication module |
| Completion outcome | User sees in-app notification; outbound email/SMS/push when providers configured |
| Missing links | Live SMS/email/push provider QA (GAP-INT-001/002); Digitize/org WhatsApp automated delivery; API-10 send/deliver/retry (016–019) omitted by design |
| Current status | **Partial** — inbox + campaign admin **TESTED** 2026-11-08; manual WhatsApp share only for external distribution |
| Dependencies | GAP-API10-001…003 |

---

## J11 — Reports and analytics

| Field | Content |
| --- | --- |
| Starting point | Company reports / PA governance reports |
| Role | OA / PA |
| Prerequisites | `report.view` / entitlements |
| Screens | Domain report pages; schedules UI |
| Backend APIs | API-11 |
| Business rules | Entitlement gates in reporting rules |
| Completion outcome | On-screen/export report; scheduled delivery when notifier live |
| Missing links | Live SMTP/SES notifier (GAP-API11-001, GAP-INT-002); worker HELD default; no list-recipients API for historical recipients |
| Current status | **Partial** — export **verified**; schedule UI **TESTED** 2026-11-08 (`report_schedule_delivery_*`); email delivery **blocked** |
| Dependencies | Email provider (GAP-INT-002) |

---

## J12 — Support and audit

| Field | Content |
| --- | --- |
| Starting point | Support tickets / help / agent; Audit events (OA) |
| Role | OA / agents / PA (limited) |
| Prerequisites | Support permissions; audit view permission |
| Screens | Tickets lifecycle; chat; agent; audit list/analytics/export |
| Backend APIs | API-12 (except escalate); API-13-005/009/012 |
| Business rules | Org-scoped tickets; audit append via server side-effects |
| Completion outcome | Resolved ticket; auditable event trail readable |
| Missing links | API-13 capture/schema ops; escalation Phase 2 (priority/assignee) **not authorized** |
| Current status | **INTEGRATION_VERIFIED** — API-12 lifecycle + **history-only escalate** (mig **083**); agent inbox/queue; Flutter panel behind `escalate.ticket` (2026-11-09 PG **4** + Flutter **15**) |
| Dependencies | GAP-API13-* product/schema gates |

---

## Cross-journey dependency sketch

```text
J1 (PA org + T&C)
 └─► J2 (OA setup + SaaS J9)
      ├─► J3 plans ─► J4 customers ─► J5 membership ─► J6 attendance
      ├─► J7 training
      ├─► J8 facility billing ◄── J5 / J6 walk-in
      └─► J11 reports / J12 support
J10 notifications overlays many journeys (provider-dependent)
```
