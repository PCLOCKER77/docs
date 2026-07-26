# DEV-16 Feature Traceability Matrix

> Feature and user-story traceability matrix for development tracking.

---

# Document Control

| Field | Value |
|---|---|
| Document ID | DEV-16 |
| Document Name | Feature Traceability Matrix |
| Folder | 16_Development_Readiness |
| Product | Digitize by OreeOn Technologies Pvt. Ltd. |
| Status | Design Draft |
| Owner | Product / QA / Engineering |
| Reviewers | Business Analysis, Functional Requirements, API, Database, UI/UX, Backend, Testing, Release Management |
| Version | 1.0 |
| Last Updated | 2026-07-24 |

---

# 1. Purpose

This matrix maps development features and user stories to documentation, implementation, test, and release-readiness artifacts.

It is used to avoid missing functionality while development proceeds without an external agile tool.

---

# 2. Traceability Status Values

| Status | Meaning |
|---|---|
| Ready | Required source links are available for development |
| Partial | Some links are available and missing links are tracked |
| Blocked | Missing source prevents development |
| Done | Feature and story are implemented and tested |
| Deferred | Feature is intentionally postponed |

---

# 3. Feature Traceability Matrix

| Feature ID | Primary Story IDs | FR Source | API Source | DB Source | UI Source | Backend Source | Test Source | Release Input | Trace Status |
|---|---|---|---|---|---|---|---|---|---|
| FEAT-PLT-001 | US-PLT-001 | FR-02 | API-01 | DB-09, DB-16 | Operations/Admin | BE-08, DEP-08 | TEST-06, TEST-11 | DEP-10 | Ready |
| FEAT-PLT-002 | US-PLT-002 | FR-02 | API-01 | DB-05 | Platform Admin | BE-01, BE-07 | TEST-05, TEST-06 | RELM-10 | Partial |
| FEAT-PLT-003 | US-PLT-003 | FR-02 | API-01 | DB-05 | Platform Admin | BE-02, BE-07 | TEST-05, TEST-06 | RELM-10 | Partial |
| FEAT-PLT-004 | Draft | FR-02 | API-01 | DB-05 | Platform Admin | BE-07 | TEST-05, TEST-06 | RELM-10 | Partial |
| FEAT-ORG-001 | US-ORG-001 | FR-03 | API-02 | DB-05, DB-11 | UI-ORG-003 | BE-01, BE-04, BE-07 | TEST-05, TEST-06 | DEV-09 | Ready |
| FEAT-ORG-002 | US-ORG-002 | FR-03 | API-02 | DB-05 | UI-ORG-001 | BE-04, BE-07 | TEST-05, TEST-06 | DEV-09 | Ready |
| FEAT-ORG-003 | US-ORG-003 | FR-03 | API-02 | DB-05 | UI-ORG-002 | BE-04, BE-07 | TEST-05, TEST-06 | DEV-09 | Ready |
| FEAT-ORG-004 | US-ORG-004 | FR-03 | API-02 | DB-05, DB-11 | UI-ORG-003 | BE-04, BE-07 | TEST-05, TEST-06 | DEV-09 | Ready |
| FEAT-ORG-005 | US-ORG-005 | FR-03 | API-02 | DB-05, DB-11 | Organization Detail | BE-04, BE-07 | TEST-05, TEST-06 | RELM-10 | Partial |
| FEAT-FAC-001 | US-FAC-001 | FR-04 | API-02 | DB-05, DB-11 | UI-FAC-002 | BE-04, BE-06, BE-07 | TEST-05, TEST-06 | DEV-09 | Ready |
| FEAT-FAC-002 | US-FAC-002 | FR-04 | API-02 | DB-05 | UI-FAC-001 | BE-04, BE-06, BE-07 | TEST-05, TEST-06 | DEV-09 | Ready |
| FEAT-FAC-003 | US-FAC-003 | FR-04 | API-02 | DB-05 | Facility Form | BE-04, BE-06, BE-07 | TEST-05, TEST-06 | RELM-10 | Partial |
| FEAT-FAC-004 | US-FAC-004 | FR-04 | API-02 | DB-05, DB-11 | Facility Detail | BE-04, BE-07 | TEST-05, TEST-06 | RELM-10 | Partial |
| FEAT-SITE-001 | US-SITE-001 | FR-05 | API-02 | DB-05, DB-11 | UI-SITE-002 | BE-04, BE-06, BE-07 | TEST-05, TEST-06 | DEV-09 | Ready |
| FEAT-SITE-002 | US-SITE-002 | FR-05 | API-02 | DB-05 | UI-SITE-001 | BE-04, BE-06, BE-07 | TEST-05, TEST-06 | DEV-09 | Ready |
| FEAT-SITE-003 | US-SITE-003 | FR-05 | API-02 | DB-05 | Site Form | BE-04, BE-06, BE-07 | TEST-05, TEST-06 | RELM-10 | Partial |
| FEAT-SITE-004 | US-SITE-004 | FR-05 | API-02 | DB-06 | Site Detail | BE-04, BE-07 | TEST-05, TEST-06 | RELM-10 | Partial |
| FEAT-IAM-001 | US-IAM-001 | FR-06 | API-03 | DB-05 | UI-AUTH-001 | BE-05 | TEST-06, TEST-09 | RELM-10 | Partial |
| FEAT-IAM-002 | US-IAM-002 | FR-06 | API-03 | DB-05 | App Shell | BE-05 | TEST-06, TEST-09 | RELM-10 | Partial |
| FEAT-IAM-003 | US-IAM-003 | FR-06 | API-03 | DB-05 | App Shell | BE-05 | TEST-06, TEST-09 | RELM-10 | Partial |
| FEAT-IAM-004 | US-IAM-004 | FR-06 | API-03 | DB-05 | User Admin | BE-05, BE-06 | TEST-05, TEST-06, TEST-09 | RELM-10 | Partial |
| FEAT-IAM-005 | US-IAM-005 | FR-06 | API-03 | DB-05 | Role Admin | BE-05 | TEST-05, TEST-06, TEST-09 | RELM-10 | Partial |
| FEAT-IAM-006 | US-IAM-006 | FR-06 | API-23 | DB-05 | UI-HOME-001 | BE-05 | TEST-05, TEST-09 | DEV-09 | Ready |
| FEAT-IAM-007 | US-IAM-007 | FR-06 | API-03 | DB-05 | UI-CTX-001 | BE-06 | TEST-05, TEST-09 | DEV-09 | Ready |
| FEAT-CUS-001 | US-CUS-001 | FR-07 | API-04 | DB-06 | Customer Form | BE-04, BE-07 | TEST-05, TEST-06 | RELM-10 | Partial |
| FEAT-CUS-002 | US-CUS-002 | FR-07 | API-04 | DB-06 | Customer List | BE-04, BE-07 | TEST-05, TEST-06 | RELM-10 | Partial |
| FEAT-CUS-003 | US-CUS-003 | FR-07 | API-04 | DB-06 | Customer Detail | BE-04, BE-07 | TEST-05, TEST-06 | RELM-10 | Partial |
| FEAT-CUS-004 | US-CUS-004 | FR-07 | API-04 | DB-06, DR-014 | Customer Documents | BE-07 | TEST-05, TEST-06, TEST-09 | RELM-10 | Partial |
| FEAT-CUS-005 | US-CUS-005 | FR-07 | API-04 | DB-06 | Customer Detail | BE-04, BE-07 | TEST-05, TEST-06 | RELM-10 | Partial |
| FEAT-MEM-001 | US-MEM-001 | FR-08 | API-05 | DB-06 | Membership Plans | BE-07 | TEST-05, TEST-06 | RELM-10 | Partial |
| FEAT-MEM-002 | US-MEM-002 | FR-08 | API-05 | DB-06, DB-07 | Membership Form | BE-04, BE-07 | TEST-05, TEST-06 | RELM-10 | Partial |
| FEAT-MEM-003 | US-MEM-003 | FR-08 | API-05 | DB-06, DB-07 | Membership Detail | BE-04, BE-07 | TEST-05, TEST-06 | RELM-10 | Partial |
| FEAT-MEM-004 | US-MEM-004 | FR-08 | API-05 | DB-06, DB-07 | Renewal Flow | BE-04, BE-07 | TEST-05, TEST-06 | RELM-10 | Partial |
| FEAT-MEM-005 | US-MEM-005 | FR-08 | API-05 | DB-06 | Freeze Flow | BE-04, BE-07 | TEST-05, TEST-06 | RELM-10 | Partial |
| FEAT-MEM-006 | US-MEM-006 | FR-08 | API-05 | DB-06, DB-07 | Cancel Flow | BE-04, BE-07 | TEST-05, TEST-06 | RELM-10 | Partial |
| FEAT-ATT-001 | US-ATT-001 | FR-09 | API-06 | DB-06 | Attendance | BE-07 | TEST-05, TEST-06 | RELM-10 | Partial |
| FEAT-ATT-002 | US-ATT-002 | FR-09 | API-06 | DB-06 | Attendance | BE-07 | TEST-05, TEST-06 | RELM-10 | Partial |
| FEAT-ATT-003 | US-ATT-003 | FR-09 | API-06 | DB-06 | Attendance Correction | BE-07 | TEST-05, TEST-06 | RELM-10 | Partial |
| FEAT-ATT-004 | US-ATT-004 | FR-09 | API-06 | DB-06 | Attendance List | BE-07 | TEST-05, TEST-06 | RELM-10 | Partial |
| FEAT-WLK-001 | US-WLK-001 | FR-10 | API-06 | DB-06 | Walk-in Form | BE-07 | TEST-05, TEST-06 | RELM-10 | Partial |
| FEAT-WLK-002 | US-WLK-002 | FR-10, FR-14 | API-06, API-08 | DB-06, DB-07 | Walk-in Payment | BE-07 | TEST-05, TEST-06 | RELM-10 | Partial |
| FEAT-WLK-003 | US-WLK-003 | FR-10 | API-06 | DB-06 | Walk-in History | BE-07 | TEST-05, TEST-06 | RELM-10 | Partial |
| FEAT-TRN-001 | US-TRN-001 | FR-11 | API-07 | DB-06 | Trainer Admin | BE-07 | TEST-05, TEST-06 | RELM-10 | Partial |
| FEAT-TRN-002 | US-TRN-002 | FR-11 | API-07 | DB-06 | Trainer Assignment | BE-07 | TEST-05, TEST-06 | RELM-10 | Partial |
| FEAT-PT-001 | US-PT-001 | FR-12 | API-07 | DB-06, DB-07 | PT Package | BE-07 | TEST-05, TEST-06 | RELM-10 | Partial |
| FEAT-PT-002 | US-PT-002 | FR-12 | API-07 | DB-06 | PT Booking | BE-07 | TEST-05, TEST-06 | RELM-10 | Partial |
| FEAT-BAT-001 | US-BAT-001 | FR-13 | API-07 | DB-06 | Batch Form | BE-07 | TEST-05, TEST-06 | RELM-10 | Partial |
| FEAT-BAT-002 | US-BAT-002 | FR-13 | API-07 | DB-06 | Schedule | BE-07 | TEST-05, TEST-06 | RELM-10 | Partial |
| FEAT-BAT-003 | US-BAT-003 | FR-13 | API-07 | DB-06 | Enrollment | BE-07 | TEST-05, TEST-06 | RELM-10 | Partial |
| FEAT-BIL-001 | US-BIL-001 | FR-14 | API-08 | DB-07 | Invoice | BE-07 | TEST-05, TEST-06 | RELM-10 | Partial |
| FEAT-BIL-002 | US-BIL-002 | FR-14 | API-08 | DB-07 | Payment | BE-07 | TEST-05, TEST-06 | RELM-10 | Partial |
| FEAT-BIL-003 | US-BIL-003 | FR-14 | API-08 | DB-07 | Payment Status | BE-07, IC-04 | TEST-05, TEST-06, TEST-07 | RELM-10 | Partial |
| FEAT-BIL-004 | US-BIL-004 | FR-14 | API-08 | DB-07 | Refund | BE-07, IC-04 | TEST-05, TEST-06, TEST-07 | RELM-10 | Partial |
| FEAT-BIL-005 | US-BIL-005 | FR-14 | API-08 | DB-07 | Reconciliation | BE-07, IC-04 | TEST-05, TEST-06, TEST-07 | RELM-10 | Partial |
| FEAT-SUB-001 | US-SUB-001 | FR-15 | API-09 | DB-07 | Subscription Admin | BE-07 | TEST-05, TEST-06 | RELM-10 | Partial |
| FEAT-SUB-002 | US-SUB-002 | FR-15 | API-09 | DB-07 | Subscription | BE-07 | TEST-05, TEST-06 | RELM-10 | Partial |
| FEAT-LIC-001 | US-LIC-001 | FR-16 | API-09 | DB-07 | License Admin | BE-07 | TEST-05, TEST-06 | RELM-10 | Partial |
| FEAT-LIC-002 | US-LIC-002 | FR-16 | API-09 | DB-07 | Cross-module | BE-05, BE-07 | TEST-05, TEST-06 | RELM-10 | Partial |
| FEAT-CAM-001 | US-CAM-001 | FR-17 | API-10 | DB-08 | Campaign | BE-07 | TEST-05, TEST-06 | RELM-10 | Partial |
| FEAT-CAM-002 | US-CAM-002 | FR-17 | API-10 | DB-08 | Campaign Approval | BE-07 | TEST-05, TEST-06 | RELM-10 | Partial |
| FEAT-NOT-001 | US-NOT-001 | FR-18 | API-10 | DB-08 | Templates | BE-07 | TEST-05, TEST-06 | RELM-10 | Partial |
| FEAT-NOT-002 | US-NOT-002 | FR-18 | API-10 | DB-08, DB-11 | Notification | BE-09, IC-05 | TEST-05, TEST-06, TEST-07 | RELM-10 | Partial |
| FEAT-NOT-003 | US-NOT-003 | FR-18 | API-10 | DB-08 | Delivery Tracking | BE-09, IC-05 | TEST-05, TEST-06, TEST-07 | RELM-10 | Partial |
| FEAT-REP-001 | US-REP-001 | FR-19 | API-11 | DB-21 | Dashboard | BE-07 | TEST-05, TEST-06, TEST-08 | RELM-10 | Partial |
| FEAT-REP-002 | US-REP-002 | FR-19 | API-11 | DB-21, DR-014 | Report Export | BE-09, IC-07 | TEST-05, TEST-06, TEST-07 | RELM-10 | Partial |
| FEAT-REP-003 | US-REP-003 | FR-19 | API-11 | DB-21 | Reports | BE-07 | TEST-05, TEST-06 | RELM-10 | Partial |
| FEAT-SUP-001 | US-SUP-001 | FR-20 | API-12 | DB-08 | Support Ticket | BE-07 | TEST-05, TEST-06 | RELM-10 | Partial |
| FEAT-SUP-002 | US-SUP-002 | FR-20 | API-12 | DB-08 | Ticket Detail | BE-07 | TEST-05, TEST-06 | RELM-10 | Partial |
| FEAT-SUP-003 | US-SUP-003 | FR-20 | API-12 | DB-08 | Ticket Detail | BE-07 | TEST-05, TEST-06 | RELM-10 | Partial |
| FEAT-AUD-001 | US-AUD-001 | FR-21 | API-13 | DB-08, DB-11 | Audit | BE-08 | TEST-05, TEST-06, TEST-09 | RELM-10 | Partial |
| FEAT-AUD-002 | US-AUD-002 | FR-21 | API-13 | DB-08 | Audit Search | BE-07, BE-08 | TEST-05, TEST-06, TEST-09 | RELM-10 | Partial |
| FEAT-AUD-003 | US-AUD-003 | FR-21 | API-13 | DB-08 | Compliance Export | BE-09, IC-07 | TEST-05, TEST-06, TEST-09 | RELM-10 | Deferred |

---

# 4. Traceability Rules

- Ready features may enter sprint planning.
- Partial features may enter analysis or design refinement but should not start development unless missing links are non-blocking.
- Blocked features require gap-register entry.
- Done features require story, code, tests, and release-readiness evidence.

