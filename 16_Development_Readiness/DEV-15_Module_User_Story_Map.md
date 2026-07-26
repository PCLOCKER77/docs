# DEV-15 Module User Story Map

> Actual module-level user story map for Digitize development.

---

# Document Control

| Field | Value |
|---|---|
| Document ID | DEV-15 |
| Document Name | Module User Story Map |
| Folder | 16_Development_Readiness |
| Product | Digitize by OreeOn Technologies Pvt. Ltd. |
| Status | Design Draft |
| Owner | Product / Engineering |
| Reviewers | Business Analysis, Functional Requirements, UI/UX, API, Backend, QA |
| Version | 1.0 |
| Last Updated | 2026-07-24 |

---

# 1. Purpose

This document defines the actual user stories grouped by module.

It is used for development planning because no external agile tool is currently being used.

---

# 2. Story Status Values

| Status | Meaning |
|---|---|
| Draft | Story is identified but not ready |
| Ready | Story has enough detail to build |
| In Development | Story is being implemented |
| In Review | Story is under review |
| QA Ready | Story is ready for QA |
| Done | Story is completed |
| Blocked | Story has an unresolved blocker |
| Deferred | Story is intentionally postponed |

---

# 3. Story Map

| Story ID | Feature ID | Module | Actor | User Story | Acceptance Summary | Priority | Status |
|---|---|---|---|---|---|---|---|
| US-PLT-001 | FEAT-PLT-001 | Platform | DevOps | As DevOps, I want health and readiness endpoints so that I can verify the backend process and dependencies. | Health works without dependencies; readiness reports PostgreSQL and Redis status. | P0 | Ready |
| US-PLT-002 | FEAT-PLT-002 | Platform | Platform Admin | As Platform Admin, I want to manage global settings so that platform behavior can be configured centrally. | Create/update/read settings with audit and permission controls. | P2 | Draft |
| US-PLT-003 | FEAT-PLT-003 | Platform | Platform Admin | As Platform Admin, I want to manage feature flags so that capabilities can be enabled safely. | Flags have owner, safe default, tenant awareness, and audit history. | P2 | Draft |
| US-ORG-001 | FEAT-ORG-001 | Organization | Platform Admin | As Platform Admin, I want to create an Organization so that a customer business can be onboarded. | Required fields validated; duplicate code rejected; organization persisted. | P0 | Ready |
| US-ORG-002 | FEAT-ORG-002 | Organization | Platform Admin | As Platform Admin, I want to view Organizations so that I can manage customer businesses. | List supports loading, empty, error, success, and restricted states. | P0 | Ready |
| US-ORG-003 | FEAT-ORG-003 | Organization | Platform Admin | As Platform Admin, I want to view Organization details so that I can inspect customer business data. | Detail loads by ID, handles not found and unauthorized states. | P0 | Ready |
| US-ORG-004 | FEAT-ORG-004 | Organization | Platform Admin | As Platform Admin, I want to update Organization profile fields so that business records remain accurate. | Editable fields update; restricted fields protected; audit metadata preserved. | P0 | Ready |
| US-ORG-005 | FEAT-ORG-005 | Organization | Platform Admin | As Platform Admin, I want to suspend or reactivate Organizations so that access can be controlled. | Lifecycle transition is validated, audited, and reflected in downstream access. | P2 | Draft |
| US-FAC-001 | FEAT-FAC-001 | Facility | Organization Admin | As Organization Admin, I want to create a Facility so that a business type can be configured under my Organization. | Facility is scoped to Organization; type is validated; unauthorized context rejected. | P0 | Ready |
| US-FAC-002 | FEAT-FAC-002 | Facility | Organization Admin | As Organization Admin, I want to view Facilities so that I can manage business units. | Facility list filters by Organization context and supports empty/error states. | P0 | Ready |
| US-FAC-003 | FEAT-FAC-003 | Facility | Organization Admin | As Organization Admin, I want to update Facility profile information so that facility records remain correct. | Update respects tenant scope and read-only fields. | P1 | Draft |
| US-FAC-004 | FEAT-FAC-004 | Facility | Organization Admin | As Organization Admin, I want to activate or suspend a Facility so that commercial and operational access can be controlled. | Lifecycle transition is validated and audited. | P2 | Draft |
| US-SITE-001 | FEAT-SITE-001 | Site | Organization Admin | As Organization Admin, I want to create a Site so that operations can be managed by location. | Site is scoped to Facility; validation and tenant checks pass. | P0 | Ready |
| US-SITE-002 | FEAT-SITE-002 | Site | Site Admin | As Site Admin, I want to view Sites so that I can manage operational locations. | Site list loads by Facility context and handles empty/error states. | P0 | Ready |
| US-SITE-003 | FEAT-SITE-003 | Site | Site Admin | As Site Admin, I want to update Site profile data so that location records remain accurate. | Editable fields update with tenant and permission checks. | P1 | Draft |
| US-SITE-004 | FEAT-SITE-004 | Site | Site Admin | As Site Admin, I want to manage operating hours so that attendance and booking rules use the correct schedule. | Operating hours are validated and visible to dependent flows. | P1 | Draft |
| US-IAM-001 | FEAT-IAM-001 | Identity | User | As a user, I want to log in so that I can access Digitize securely. | Valid credentials create session; invalid credentials show safe error. | P1 | Draft |
| US-IAM-002 | FEAT-IAM-002 | Identity | User | As a user, I want to log out so that my session ends safely. | Token/session cleared and protected routes become inaccessible. | P1 | Draft |
| US-IAM-003 | FEAT-IAM-003 | Identity | User | As a user, I want my session refreshed so that I can continue working securely. | Refresh follows approved token behavior and handles expiry. | P1 | Draft |
| US-IAM-004 | FEAT-IAM-004 | Identity | Organization Admin | As Organization Admin, I want to manage user accounts so that staff access is controlled. | Create/update/deactivate users with role and tenant scope. | P1 | Draft |
| US-IAM-005 | FEAT-IAM-005 | Identity | Organization Admin | As Organization Admin, I want to manage roles so that permissions match responsibilities. | Roles map to permissions and are audit-tracked. | P1 | Draft |
| US-IAM-006 | FEAT-IAM-006 | Identity | User | As a user, I want navigation to reflect my permissions so that unavailable actions are not shown. | UI hides unavailable actions; backend still enforces access. | P0 | Ready |
| US-IAM-007 | FEAT-IAM-007 | Identity | User | As a user, I want to select Organization, Facility, and Site context so that I work in the correct scope. | Only authorized contexts are shown and sent to APIs. | P0 | Ready |
| US-CUS-001 | FEAT-CUS-001 | Customer | Staff | As Staff, I want to create a Customer so that customer records can be managed. | Required fields validated and customer is scoped to tenant. | P1 | Draft |
| US-CUS-002 | FEAT-CUS-002 | Customer | Staff | As Staff, I want to search Customers so that I can quickly find records. | Search supports approved filters and tenant scope. | P1 | Draft |
| US-CUS-003 | FEAT-CUS-003 | Customer | Staff | As Staff, I want to update Customer profiles so that customer details remain accurate. | Updates validate restricted fields and audit changes. | P1 | Draft |
| US-CUS-004 | FEAT-CUS-004 | Customer | Staff | As Staff, I want to manage customer document metadata so that documents are associated safely. | Metadata stored in DB; files use approved storage workflow. | P2 | Draft |
| US-CUS-005 | FEAT-CUS-005 | Customer | Site Admin | As Site Admin, I want to change Customer status so that inactive or suspended customers are controlled. | Status transitions follow approved lifecycle and audit. | P2 | Draft |
| US-MEM-001 | FEAT-MEM-001 | Membership | Staff | As Staff, I want to view membership plans so that I can sell the correct plan. | Plans load by Facility context and active status. | P1 | Draft |
| US-MEM-002 | FEAT-MEM-002 | Membership | Staff | As Staff, I want to create a Membership so that a Customer can access services. | Membership validates customer, plan, dates, payment rule, and tenant. | P1 | Draft |
| US-MEM-003 | FEAT-MEM-003 | Membership | Staff | As Staff, I want to activate Membership after prerequisites so that access begins correctly. | Activation checks payment/license/eligibility and updates state. | P1 | Draft |
| US-MEM-004 | FEAT-MEM-004 | Membership | Staff | As Staff, I want to renew Membership so that customers can continue services. | Renewal validates expiry, plan, payment, and new period. | P1 | Draft |
| US-MEM-005 | FEAT-MEM-005 | Membership | Site Admin | As Site Admin, I want to freeze Membership so that temporary pauses are tracked. | Freeze validates policy and updates entitlement period. | P2 | Draft |
| US-MEM-006 | FEAT-MEM-006 | Membership | Site Admin | As Site Admin, I want to cancel Membership so that access and billing stop correctly. | Cancellation validates financial impact and audit evidence. | P2 | Draft |
| US-ATT-001 | FEAT-ATT-001 | Attendance | Staff | As Staff, I want to check in a member so that attendance is recorded. | Active entitlement is validated before check-in. | P1 | Draft |
| US-ATT-002 | FEAT-ATT-002 | Attendance | Staff | As Staff, I want to check out a member so that visit duration is captured. | Open attendance record is completed. | P2 | Draft |
| US-ATT-003 | FEAT-ATT-003 | Attendance | Site Admin | As Site Admin, I want to correct attendance so that operational records are accurate. | Correction requires reason and approval where configured. | P2 | Draft |
| US-ATT-004 | FEAT-ATT-004 | Attendance | Site Admin | As Site Admin, I want to view attendance records so that I can monitor usage. | List filters by site, date, member, and status. | P1 | Draft |
| US-WLK-001 | FEAT-WLK-001 | Walk-in | Staff | As Staff, I want to register a walk-in customer so that one-time visits can be served. | Walk-in visit is captured with required customer and visit details. | P1 | Draft |
| US-WLK-002 | FEAT-WLK-002 | Walk-in | Staff | As Staff, I want to associate payment with a walk-in visit so that access follows payment policy. | Payment required/deferred behavior follows policy. | P1 | Draft |
| US-WLK-003 | FEAT-WLK-003 | Walk-in | Site Admin | As Site Admin, I want to view walk-in history so that site usage is traceable. | History filters by date, customer, and payment status. | P2 | Draft |
| US-TRN-001 | FEAT-TRN-001 | Trainer | Site Admin | As Site Admin, I want to manage Trainer profiles so that trainer availability can be tracked. | Trainer profile create/update follows tenant scope. | P1 | Draft |
| US-TRN-002 | FEAT-TRN-002 | Trainer | Site Admin | As Site Admin, I want to assign Trainers so that classes and sessions have owners. | Assignment validates schedule and active trainer status. | P2 | Draft |
| US-PT-001 | FEAT-PT-001 | Personal Training | Site Admin | As Site Admin, I want to configure personal training packages so that paid sessions can be offered. | Package has price, session count, validity, and status. | P2 | Draft |
| US-PT-002 | FEAT-PT-002 | Personal Training | Staff / Customer | As a user, I want to book personal training so that sessions are scheduled. | Booking validates trainer, slot, entitlement, and conflicts. | P2 | Draft |
| US-BAT-001 | FEAT-BAT-001 | Batch/Class | Site Admin | As Site Admin, I want to create batches/classes so that group sessions can be managed. | Batch has capacity, schedule, trainer, and lifecycle status. | P1 | Draft |
| US-BAT-002 | FEAT-BAT-002 | Batch/Class | Site Admin | As Site Admin, I want to manage schedules so that classes happen at correct times. | Schedule validates conflicts and site hours. | P1 | Draft |
| US-BAT-003 | FEAT-BAT-003 | Batch/Class | Staff / Customer | As a user, I want to enroll in a batch so that participation is tracked. | Enrollment checks capacity and eligibility. | P1 | Draft |
| US-BIL-001 | FEAT-BIL-001 | Billing | Staff | As Staff, I want to create invoices so that charges are recorded. | Invoice creates line items, totals, taxes, and status. | P1 | Draft |
| US-BIL-002 | FEAT-BIL-002 | Billing | Staff | As Staff, I want to record payment so that invoices can be settled. | Payment updates invoice and receipt state. | P1 | Draft |
| US-BIL-003 | FEAT-BIL-003 | Billing | Staff / System | As a user, I want to verify payment status so that payment uncertainty can be resolved. | Status check supports pending, success, failed, duplicate, and timeout. | P1 | Draft |
| US-BIL-004 | FEAT-BIL-004 | Billing | Site Admin | As Site Admin, I want to process refunds so that customer financial corrections are tracked. | Refund validates policy, amount, and audit reason. | P2 | Draft |
| US-BIL-005 | FEAT-BIL-005 | Billing | Finance | As Finance, I want to reconcile payments so that records match provider outcomes. | Reconciliation identifies matched, missing, duplicate, and failed records. | P2 | Draft |
| US-SUB-001 | FEAT-SUB-001 | Subscription | Platform Admin | As Platform Admin, I want to assign subscription plans so that facilities have commercial access. | Plan assignment creates commercial entitlement. | P1 | Draft |
| US-SUB-002 | FEAT-SUB-002 | Subscription | Platform Admin / System | As Platform Admin, I want to renew subscriptions so that service access continues. | Renewal validates billing and license impact. | P2 | Draft |
| US-LIC-001 | FEAT-LIC-001 | License | Platform Admin / System | As a system user, I want licenses activated so that feature access is governed. | License status drives entitlement checks. | P1 | Draft |
| US-LIC-002 | FEAT-LIC-002 | License | System | As the system, I want to enforce license entitlements so that unavailable capabilities are blocked. | Backend blocks unauthorized feature access. | P1 | Draft |
| US-CAM-001 | FEAT-CAM-001 | Campaign | Organization Admin | As Organization Admin, I want to create campaigns so that customers can be engaged. | Campaign validates audience, content, schedule, and approval status. | P2 | Draft |
| US-CAM-002 | FEAT-CAM-002 | Campaign | Organization Admin | As Organization Admin, I want to approve campaigns so that communications are governed. | Approval records approver and prevents unauthorized dispatch. | P2 | Draft |
| US-NOT-001 | FEAT-NOT-001 | Notification | Organization Admin | As Organization Admin, I want to manage templates so that messages are consistent. | Template create/update is versioned and tenant-scoped. | P2 | Draft |
| US-NOT-002 | FEAT-NOT-002 | Notification | System | As the system, I want to dispatch notifications so that users receive events. | Dispatch uses provider adapter and outbox tracking. | P2 | Draft |
| US-NOT-003 | FEAT-NOT-003 | Notification | Staff / Admin | As Staff, I want to view delivery status so that failed communications can be handled. | Delivery status includes pending, sent, failed, retry, dead-letter. | P2 | Draft |
| US-REP-001 | FEAT-REP-001 | Reports | Admin | As Admin, I want an operational dashboard so that I can monitor performance. | Dashboard shows approved KPIs with tenant filters. | P2 | Draft |
| US-REP-002 | FEAT-REP-002 | Reports | Admin | As Admin, I want to export reports so that records can be shared or archived. | Export is async, permissioned, and downloadable after ready. | P2 | Draft |
| US-REP-003 | FEAT-REP-003 | Reports | Admin | As Admin, I want KPI filters so that I can analyze by period, site, and status. | Filters are applied consistently and safely. | P2 | Draft |
| US-SUP-001 | FEAT-SUP-001 | Support | Customer / Staff | As a user, I want to create a support ticket so that help requests are tracked. | Ticket creates with category, priority, summary, and tenant context. | P2 | Draft |
| US-SUP-002 | FEAT-SUP-002 | Support | Support Staff | As Support Staff, I want to assign and respond to tickets so that issues are handled. | Assignment and replies update ticket history. | P2 | Draft |
| US-SUP-003 | FEAT-SUP-003 | Support | Support Staff | As Support Staff, I want to manage ticket status so that support workflow is clear. | Status transitions follow approved lifecycle. | P2 | Draft |
| US-AUD-001 | FEAT-AUD-001 | Audit | System | As the system, I want to capture audit events so that sensitive actions are traceable. | Audited actions write immutable audit records. | P1 | Draft |
| US-AUD-002 | FEAT-AUD-002 | Audit | Security | As Security, I want to search audit events so that investigations can be performed. | Search is permissioned and filters by tenant, actor, event, and date. | P2 | Draft |
| US-AUD-003 | FEAT-AUD-003 | Audit | Security | As Security, I want compliance exports so that external evidence can be produced. | Export is permissioned, audited, and redacted where required. | P3 | Deferred |

---

# 4. Story Governance

- This document is the primary user-story register until an agile tool is adopted.
- Stories shall not be deleted after development begins; use Deferred or Superseded status.
- Acceptance detail may live in DEV-06 for first-slice stories and in module-specific story expansions later.
- Story status shall be updated during planning, implementation, review, QA, and release readiness.

