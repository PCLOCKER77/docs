# DEV-14 Product Feature Backlog

> Actual product feature backlog for Digitize development, grouped by module and implementation priority.

---

# Document Control

| Field | Value |
|---|---|
| Document ID | DEV-14 |
| Document Name | Product Feature Backlog |
| Folder | 16_Development_Readiness |
| Product | Digitize by OreeOn Technologies Pvt. Ltd. |
| Status | Design Draft |
| Owner | Product / Engineering |
| Reviewers | Business Analysis, Functional Requirements, UI/UX, API, Backend, QA, DevOps |
| Version | 1.0 |
| Last Updated | 2026-07-24 |

---

# 1. Purpose

This document is the repo-based product feature backlog for Digitize.

Because no external agile tool is being used, this document acts as the initial source for feature planning, sprint selection, development status, and release readiness tracking.

---

# 2. Backlog Status Values

| Status | Meaning |
|---|---|
| Backlog | Feature is identified but not yet selected for development |
| Ready | Feature has enough requirement, API, UI, and DB clarity to start |
| In Development | Feature is actively being built |
| In Review | Feature is under code or documentation review |
| QA Ready | Feature is ready for QA validation |
| Done | Feature satisfies acceptance criteria and tests |
| Blocked | Feature cannot proceed due to unresolved dependency |
| Deferred | Feature is intentionally postponed |

---

# 3. Priority Values

| Priority | Meaning |
|---|---|
| P0 | Required for development foundation or first vertical slice |
| P1 | Required for MVP core operations |
| P2 | Required for full operational readiness |
| P3 | Enhancement or later-phase capability |

---

# 4. Product Feature Backlog

| Feature ID | Module | Feature | Primary Actor | Priority | Source FR | API Doc | UI Area | Status | Target Phase |
|---|---|---|---|---|---|---|---|---|---|
| FEAT-PLT-001 | Platform Administration | Platform health and readiness | Platform Admin / DevOps | P0 | FR-02 | API-01 | Admin / Ops | Ready | Foundation |
| FEAT-PLT-002 | Platform Administration | Global platform settings | Platform Admin | P2 | FR-02 | API-01 | Platform Admin | Backlog | MVP |
| FEAT-PLT-003 | Platform Administration | Feature flag management | Platform Admin | P2 | FR-02 | API-01 | Platform Admin | Backlog | MVP |
| FEAT-PLT-004 | Platform Administration | Maintenance window management | Platform Admin | P2 | FR-02 | API-01 | Platform Admin | Backlog | MVP |
| FEAT-PLT-005 | Platform Administration | Platform usage overview | Platform Admin | P3 | FR-02 | API-01 | Reports | Backlog | Later |
| FEAT-ORG-001 | Organization Management | Create Organization | Platform Admin | P0 | FR-03 | API-02 | UI-ORG-003 | Ready | First Slice |
| FEAT-ORG-002 | Organization Management | View Organization list | Platform Admin | P0 | FR-03 | API-02 | UI-ORG-001 | Ready | First Slice |
| FEAT-ORG-003 | Organization Management | View Organization detail | Platform Admin | P0 | FR-03 | API-02 | UI-ORG-002 | Ready | First Slice |
| FEAT-ORG-004 | Organization Management | Update Organization profile | Platform Admin | P0 | FR-03 | API-02 | UI-ORG-003 | Ready | First Slice |
| FEAT-ORG-005 | Organization Management | Suspend or reactivate Organization | Platform Admin | P2 | FR-03 | API-02 | Organization Detail | Backlog | MVP |
| FEAT-FAC-001 | Facility Management | Create Facility | Organization Admin | P0 | FR-04 | API-02 | UI-FAC-002 | Ready | First Slice |
| FEAT-FAC-002 | Facility Management | View Facility list | Organization Admin | P0 | FR-04 | API-02 | UI-FAC-001 | Ready | First Slice |
| FEAT-FAC-003 | Facility Management | Update Facility profile | Organization Admin | P1 | FR-04 | API-02 | Facility Form | Backlog | MVP |
| FEAT-FAC-004 | Facility Management | Activate or suspend Facility | Organization Admin | P2 | FR-04 | API-02 | Facility Detail | Backlog | MVP |
| FEAT-SITE-001 | Site Management | Create Site | Organization Admin / Site Admin | P0 | FR-05 | API-02 | UI-SITE-002 | Ready | First Slice |
| FEAT-SITE-002 | Site Management | View Site list | Organization Admin / Site Admin | P0 | FR-05 | API-02 | UI-SITE-001 | Ready | First Slice |
| FEAT-SITE-003 | Site Management | Update Site profile | Site Admin | P1 | FR-05 | API-02 | Site Form | Backlog | MVP |
| FEAT-SITE-004 | Site Management | Site operating hours | Site Admin | P1 | FR-05 | API-02 | Site Detail | Backlog | MVP |
| FEAT-IAM-001 | Identity and Access | Login | Staff / Admin / Customer | P1 | FR-06 | API-03 | UI-AUTH-001 | Backlog | MVP |
| FEAT-IAM-002 | Identity and Access | Logout | Authenticated User | P1 | FR-06 | API-03 | App Shell | Backlog | MVP |
| FEAT-IAM-003 | Identity and Access | Session refresh | Authenticated User | P1 | FR-06 | API-03 | App Shell | Backlog | MVP |
| FEAT-IAM-004 | Identity and Access | User account management | Organization Admin | P1 | FR-06 | API-03 | User Admin | Backlog | MVP |
| FEAT-IAM-005 | Identity and Access | Role management | Organization Admin | P1 | FR-06 | API-03 | Role Admin | Backlog | MVP |
| FEAT-IAM-006 | Identity and Access | Permission-aware navigation | Authenticated User | P0 | FR-06 | API-23 | App Shell | Ready | First Slice |
| FEAT-IAM-007 | Identity and Access | Tenant context selection | Authenticated User | P0 | FR-06 | API-03 | UI-CTX-001 | Ready | First Slice |
| FEAT-CUS-001 | Customer Management | Create customer | Staff / Site Admin | P1 | FR-07 | API-04 | Customer Form | Backlog | MVP |
| FEAT-CUS-002 | Customer Management | Customer list and search | Staff / Site Admin | P1 | FR-07 | API-04 | Customer List | Backlog | MVP |
| FEAT-CUS-003 | Customer Management | Customer profile update | Staff / Site Admin | P1 | FR-07 | API-04 | Customer Detail | Backlog | MVP |
| FEAT-CUS-004 | Customer Management | Customer document metadata | Staff / Site Admin | P2 | FR-07 | API-04 | Customer Documents | Backlog | MVP |
| FEAT-CUS-005 | Customer Management | Customer status lifecycle | Staff / Site Admin | P2 | FR-07 | API-04 | Customer Detail | Backlog | MVP |
| FEAT-MEM-001 | Membership Management | Membership plan list | Staff / Site Admin | P1 | FR-08 | API-05 | Membership Plans | Backlog | MVP |
| FEAT-MEM-002 | Membership Management | Create membership | Staff / Site Admin | P1 | FR-08 | API-05 | Membership Form | Backlog | MVP |
| FEAT-MEM-003 | Membership Management | Membership activation | Staff / Site Admin | P1 | FR-08 | API-05 | Membership Detail | Backlog | MVP |
| FEAT-MEM-004 | Membership Management | Membership renewal | Staff / Site Admin | P1 | FR-08 | API-05 | Renewal Flow | Backlog | MVP |
| FEAT-MEM-005 | Membership Management | Membership freeze | Site Admin | P2 | FR-08 | API-05 | Freeze Flow | Backlog | MVP |
| FEAT-MEM-006 | Membership Management | Membership cancellation | Site Admin | P2 | FR-08 | API-05 | Cancel Flow | Backlog | MVP |
| FEAT-ATT-001 | Attendance | Member check-in | Staff | P1 | FR-09 | API-06 | Attendance | Backlog | MVP |
| FEAT-ATT-002 | Attendance | Member check-out | Staff | P2 | FR-09 | API-06 | Attendance | Backlog | MVP |
| FEAT-ATT-003 | Attendance | Attendance correction | Site Admin | P2 | FR-09 | API-06 | Attendance Correction | Backlog | MVP |
| FEAT-ATT-004 | Attendance | Attendance list and filters | Staff / Site Admin | P1 | FR-09 | API-06 | Attendance List | Backlog | MVP |
| FEAT-WLK-001 | Walk-in | Register walk-in customer | Staff | P1 | FR-10 | API-06 | Walk-in Form | Backlog | MVP |
| FEAT-WLK-002 | Walk-in | Walk-in payment association | Staff | P1 | FR-10 | API-06, API-08 | Walk-in Payment | Backlog | MVP |
| FEAT-WLK-003 | Walk-in | Walk-in visit history | Staff / Site Admin | P2 | FR-10 | API-06 | Walk-in History | Backlog | MVP |
| FEAT-TRN-001 | Trainer Management | Trainer profile management | Site Admin | P1 | FR-11 | API-07 | Trainer Admin | Backlog | MVP |
| FEAT-TRN-002 | Trainer Management | Trainer assignment | Site Admin | P2 | FR-11 | API-07 | Trainer Assignment | Backlog | MVP |
| FEAT-PT-001 | Personal Training | Personal training package | Site Admin | P2 | FR-12 | API-07 | PT Package | Backlog | MVP |
| FEAT-PT-002 | Personal Training | Personal training booking | Staff / Customer | P2 | FR-12 | API-07 | PT Booking | Backlog | MVP |
| FEAT-BAT-001 | Batch/Class | Create batch/class | Site Admin | P1 | FR-13 | API-07 | Batch Form | Backlog | MVP |
| FEAT-BAT-002 | Batch/Class | Batch schedule management | Site Admin | P1 | FR-13 | API-07 | Schedule | Backlog | MVP |
| FEAT-BAT-003 | Batch/Class | Batch enrollment | Staff / Customer | P1 | FR-13 | API-07 | Enrollment | Backlog | MVP |
| FEAT-BIL-001 | Billing and Payment | Create invoice | Staff / Site Admin | P1 | FR-14 | API-08 | Invoice | Backlog | MVP |
| FEAT-BIL-002 | Billing and Payment | Record payment | Staff | P1 | FR-14 | API-08 | Payment | Backlog | MVP |
| FEAT-BIL-003 | Billing and Payment | Payment status verification | Staff / System | P1 | FR-14 | API-08 | Payment Status | Backlog | MVP |
| FEAT-BIL-004 | Billing and Payment | Refund processing | Site Admin | P2 | FR-14 | API-08 | Refund | Backlog | MVP |
| FEAT-BIL-005 | Billing and Payment | Payment reconciliation | Finance / Site Admin | P2 | FR-14 | API-08 | Reconciliation | Backlog | MVP |
| FEAT-SUB-001 | Subscription | Subscription plan assignment | Platform Admin | P1 | FR-15 | API-09 | Subscription Admin | Backlog | MVP |
| FEAT-SUB-002 | Subscription | Subscription renewal | Platform Admin / System | P2 | FR-15 | API-09 | Subscription | Backlog | MVP |
| FEAT-LIC-001 | License | License activation | Platform Admin / System | P1 | FR-16 | API-09 | License Admin | Backlog | MVP |
| FEAT-LIC-002 | License | License entitlement enforcement | System | P1 | FR-16 | API-09 | Cross-module | Backlog | MVP |
| FEAT-CAM-001 | Campaign | Create campaign | Organization Admin | P2 | FR-17 | API-10 | Campaign | Backlog | MVP |
| FEAT-CAM-002 | Campaign | Approve campaign | Organization Admin | P2 | FR-17 | API-10 | Campaign Approval | Backlog | MVP |
| FEAT-NOT-001 | Notification | Notification template management | Organization Admin | P2 | FR-18 | API-10 | Templates | Backlog | MVP |
| FEAT-NOT-002 | Notification | Dispatch notification | System / Staff | P2 | FR-18 | API-10 | Notification | Backlog | MVP |
| FEAT-NOT-003 | Notification | Notification delivery tracking | Staff / Admin | P2 | FR-18 | API-10 | Delivery Tracking | Backlog | MVP |
| FEAT-REP-001 | Reports | Operational dashboard | Organization Admin / Site Admin | P2 | FR-19 | API-11 | Dashboard | Backlog | MVP |
| FEAT-REP-002 | Reports | Report export | Admin / Staff | P2 | FR-19 | API-11 | Report Export | Backlog | MVP |
| FEAT-REP-003 | Reports | KPI filters | Admin / Staff | P2 | FR-19 | API-11 | Reports | Backlog | MVP |
| FEAT-SUP-001 | Support | Create support ticket | Customer / Staff | P2 | FR-20 | API-12 | Support Ticket | Backlog | MVP |
| FEAT-SUP-002 | Support | Assign and respond to ticket | Support / Staff | P2 | FR-20 | API-12 | Ticket Detail | Backlog | MVP |
| FEAT-SUP-003 | Support | Ticket status lifecycle | Support / Staff | P2 | FR-20 | API-12 | Ticket Detail | Backlog | MVP |
| FEAT-AUD-001 | Audit and Compliance | Audit event capture | System | P1 | FR-21 | API-13 | Audit | Backlog | MVP |
| FEAT-AUD-002 | Audit and Compliance | Audit search | Security / Platform Admin | P2 | FR-21 | API-13 | Audit Search | Backlog | MVP |
| FEAT-AUD-003 | Audit and Compliance | Compliance export | Security / Platform Admin | P3 | FR-21 | API-13 | Compliance Export | Backlog | Later |

---

# 5. MVP Feature Groups

## Foundation Group

- FEAT-PLT-001
- FEAT-ORG-001 through FEAT-ORG-004
- FEAT-FAC-001 through FEAT-FAC-002
- FEAT-SITE-001 through FEAT-SITE-002
- FEAT-IAM-006
- FEAT-IAM-007

## Core Operations Group

- FEAT-IAM-001 through FEAT-IAM-005
- FEAT-CUS-001 through FEAT-CUS-003
- FEAT-MEM-001 through FEAT-MEM-004
- FEAT-ATT-001
- FEAT-ATT-004
- FEAT-WLK-001

## Commercial Group

- FEAT-BIL-001 through FEAT-BIL-003
- FEAT-SUB-001
- FEAT-LIC-001
- FEAT-LIC-002

## Management and Visibility Group

- FEAT-TRN-001
- FEAT-BAT-001 through FEAT-BAT-003
- FEAT-REP-001
- FEAT-SUP-001
- FEAT-AUD-001

---

# 6. Backlog Governance

- Feature IDs shall remain stable.
- New features shall be added here before implementation begins.
- Features shall not be marked Done until related stories, tests, and traceability are complete.
- Deferred features shall remain visible.
- This backlog is the source for sprint planning until an external agile tool is adopted.

