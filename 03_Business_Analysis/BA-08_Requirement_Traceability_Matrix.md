# BA-08 Requirement Traceability Matrix

**Document ID:** BA-08  
**Document Name:** Requirement Traceability Matrix  
**Product:** Digitize by OrieOn Technologies Pvt. Ltd.
**Document Type:** Business Analysis  
**Version:** 1.0  
**Status:** Frozen  
**Owner:** Product Management  
**Prepared By:** Product & Business Analysis Team  
**Reviewer:** CTO  
**Last Updated:** July 2026

---

# 1. Introduction

## 1.1 Purpose

The purpose of this document is to provide a structured traceability framework for the Digitize by OrieOn platform.

This document links business needs, business requirements, business rules, business processes, user journeys, functional requirements, UI screens, APIs, database entities, and test cases into a single enterprise traceability model.

## 1.2 Objectives

The objectives of this document are to:

- Establish end-to-end traceability across all major project artifacts.
- Support impact analysis for requirement changes.
- Provide visibility into requirement ownership and implementation status.
- Ensure business rules, processes, and journeys are consistently mapped to delivery artifacts.
- Improve governance, validation, and release readiness.

## 1.3 Scope

This document covers the traceability relationships across the Digitize platform for:

- Business requirements
- Business rules
- Business processes
- User journeys
- Functional requirements
- UI screens
- APIs
- Database entities
- Test cases

## 1.4 Intended Audience

This document is intended for:

- Product Management
- Business Analysis
- Solution Architecture
- Development Team
- UI/UX Team
- QA Team
- DevOps Team
- Implementation Team
- Support Team
- Stakeholders with governance responsibility

## 1.4.1 Approval Note

This Requirement Traceability Matrix is approved as the baseline traceability structure for Business Analysis. Individual requirement and implementation statuses may remain `Planned` or `Pending` until corresponding downstream artifacts are completed.

## 1.5 Related Documents

This document should be read together with:

- PVD Product Vision Document
- PG Product Glossary
- BA-01 Business Requirements Document
- BA-02 Business Rules Catalog
- BA-03 Business Process Catalog
- BA-04 Business Process Flows
- BA-05 User Personas
- BA-06 User Journeys
- BA-07 Stakeholder Analysis
- FRS
- SAD
- Database Design
- API Specifications
- UI Navigation
- Testing Documentation

---

# 2. Requirement Traceability Approach

## 2.1 Requirement Identification

Requirement identifiers in this document use the format:

```text
BR-###
```

Where:

- **BR** = Business Requirement
- **###** = Sequential requirement number within this matrix

Business rule identifiers from BA-02 retain their own domain-prefixed format such as `BR-PLT-001` or `BR-MEM-001`. These are mapped separately under Business Rule Traceability.

## 2.2 Traceability Levels

BA-08 traces requirements across the following levels:

- Business Need
- Business Requirement
- Business Rule
- Business Process
- User Journey
- Functional Requirement
- UI Screen
- API
- Database Entity
- Test Case

## 2.3 Requirement Status

Requirement status is maintained throughout the lifecycle to support governance and release planning.

## 2.4 Requirement Ownership

Each business requirement is owned by Product Management and refined by Business Analysis, with implementation ownership shared across Architecture, Development, QA, and Delivery.

---

# 3. Business Requirement Traceability

The master requirement traceability matrix is the core artifact of BA-08.

> Note: The table below represents the current baseline traceability register structure. Additional requirements can be appended without changing the matrix model.

| Requirement ID | Requirement | Source Document | Business Process | Functional Module | UI Screen | API | Database Entity | Test Case | Status |
|---|---|---|---|---|---|---|---|---|---|
| BR-001 | Organization Registration | BA-01 | BP-ORG-001 | Organization | Organization Registration | POST /organizations | Organization | TC-001 | Completed |
| BR-002 | Organization Profile Management | BA-01 | BP-ORG-002 | Organization | Organization Profile | PATCH /organizations/{id} | Organization | TC-002 | Completed |
| BR-003 | Facility Creation | BA-01 / [FRS-BR-003_Facility](../04_Functional_Requirements/FRS-BR-003_Facility.md) | BP-FAC-001 | Facility | Facility Management | POST /facilities | Facility | TC-012 | Planned |
| BR-004 | Facility Configuration | BA-01 / [FRS-BR-004_Facility_Configuration](../04_Functional_Requirements/FRS-BR-004_Facility_Configuration.md) | BP-FAC-003 | Facility | Facility Configuration | PATCH /facilities/{id}/settings | Facility Setting | TC-013 | Planned |
| BR-005 | Site Creation | BA-01 / [FRS-BR-005_Site_Creation](../04_Functional_Requirements/FRS-BR-005_Site_Creation.md) | BP-SIT-001 | Site | Site Management | POST /sites | Site | TC-021 | Planned |
| BR-006 | Staff Account Creation | BA-01 / [FRS-BR-006_Staff_Account_Creation](../04_Functional_Requirements/FRS-BR-006_Staff_Account_Creation.md) | BP-STA-001 | Staff Identity | Staff Management | POST /staff | Staff Account | TC-031 | Planned |
| BR-007 | Customer Registration | BA-01 | BP-CUS-001 | Customer | Customer Registration | POST /customers | Customer | TC-041 | Completed |
| BR-008 | Customer Identity Verification | BA-01 / [FRS-BR-008_Customer_Identity_Verification](../04_Functional_Requirements/FRS-BR-008_Customer_Identity_Verification.md) | BP-CUS-003 | Customer Validation | Identity Verification | POST /customers/{id}/verify | Customer Verification | TC-042 | Planned |
| BR-009 | Membership Purchase | BA-01 | BP-MEM-001 | Membership | Membership Purchase | POST /memberships | Membership | TC-051 | Completed |
| BR-010 | Membership Renewal | BA-01 | BP-MEM-003 | Membership | Membership Renewal | POST /memberships/{id}/renew | Membership Renewal | TC-052 | Completed |
| BR-011 | Membership Freeze | BA-01 / [FRS-BR-011_Membership_Freeze](../04_Functional_Requirements/FRS-BR-011_Membership_Freeze.md) | BP-MEM-006 | Membership | Membership Freeze | POST /memberships/{id}/freeze | Membership Freeze | TC-053 | Planned |
| BR-012 | Membership Cancellation | BA-01 / [FRS-BR-012_Membership_Cancellation](../04_Functional_Requirements/FRS-BR-012_Membership_Cancellation.md) | BP-MEM-009 | Membership | Membership Cancellation | POST /memberships/{id}/cancel | Membership Cancellation | TC-054 | Planned |
| BR-013 | Attendance Recording | BA-01 | BP-ATT-001 | Attendance | Attendance Check-in | POST /attendance/check-in | Attendance | TC-061 | Completed |
| BR-014 | Walk-in Visit Recording | BA-01 / [FRS-BR-014_Walkin_Visit_Recording](../04_Functional_Requirements/FRS-BR-014_Walkin_Visit_Recording.md) | BP-ATT-004 | Attendance | Walk-in Registration | POST /walkins | Walk-in Visit | TC-062 | Planned |
| BR-015 | Activity Configuration | BA-01 / [FRS-BR-015_Activity_Configuration](../04_Functional_Requirements/FRS-BR-015_Activity_Configuration.md) | BP-ACT-001 | Activity | Activity Management | POST /activities | Activity | TC-071 | Planned |
| BR-016 | Batch Scheduling | BA-01 / [FRS-BR-016_Batch_Scheduling](../04_Functional_Requirements/FRS-BR-016_Batch_Scheduling.md) | BP-ACT-006 | Activity & Batch | Batch Schedule | POST /batches/{id}/schedule | Batch Schedule | TC-072 | Planned |
| BR-017 | Personal Training Booking | BA-01 / [FRS-BR-017_Personal_Training_Booking](../04_Functional_Requirements/FRS-BR-017_Personal_Training_Booking.md) | BP-PTR-004 | Personal Training | Session Booking | POST /training-sessions | Training Session | TC-081 | Planned |
| BR-018 | Billing and Invoice Generation | BA-01 | BP-BIL-001 | Billing | Invoice Management | POST /invoices | Invoice | TC-091 | Completed |
| BR-019 | Payment Collection | BA-01 | BP-PAY-001 | Payment | Payment Collection | POST /payments | Payment | TC-092 | Completed |
| BR-020 | Refund Processing | BA-01 / [FRS-BR-020_Refund_Processing](../04_Functional_Requirements/FRS-BR-020_Refund_Processing.md) | BP-PAY-008 | Payment | Refund Management | POST /refunds | Refund | TC-093 | Planned |
| BR-021 | Advertisement Campaign Management | BA-01 / [FRS-BR-021_Advertisement_Campaign_Management](../04_Functional_Requirements/FRS-BR-021_Advertisement_Campaign_Management.md) | BP-CMP-001 | Marketing | Campaign Management | POST /campaigns | Campaign | TC-101 | Planned |
| BR-022 | Notification Delivery | BA-01 | BP-NOT-003 | Notification | Notification Center | POST /notifications | Notification | TC-102 | Completed |
| BR-023 | Approval Workflow | BA-01 / [FRS-BR-023_Approval_Workflow](../04_Functional_Requirements/FRS-BR-023_Approval_Workflow.md) | BP-APR-001 | Approval | Approval Management | POST /approvals | Approval Request | TC-103 | Planned |
| BR-024 | Reporting and Analytics | BA-01 | BP-RPT-001 | Reporting | Operational Dashboard | GET /reports/dashboard | Report | TC-111 | Completed |
| BR-025 | Support Ticket Management | BA-01 | BP-TKT-001 | Support | Support Ticket Queue | POST /tickets | Support Ticket | TC-121 | Completed |
| BR-026 | Audit Logging | BA-01 | BP-AUD-001 | Audit | Audit Logs | POST /audit-events | Audit Log | TC-131 | Completed |
| BR-027 | Subscription Creation | BA-01 | BP-SUB-001 | Subscription | Subscription Management | POST /subscriptions | Subscription | TC-141 | Completed |
| BR-028 | License Generation | BA-01 | BP-LIC-001 | License | License Management | POST /licenses | License | TC-142 | Completed |
| BR-029 | Platform Configuration | BA-01 | BP-ADM-001 | Platform Administration | Platform Configuration | PATCH /platform/settings | Platform Configuration | TC-151 | Completed |
| BR-030 | Business Rule Management | BA-01 / [FRS-BR-030_Business_Rule_Management](../04_Functional_Requirements/FRS-BR-030_Business_Rule_Management.md) | BP-PLT-009 | Platform Governance | Global Rules | PATCH /business-rules | Business Rule | TC-152 | Planned |

---

# 4. Business Rule Traceability

The following table links selected business rules from BA-02 to the requirements and operational areas they influence.

| Business Rule ID | Business Rule | Related Requirement | Related Process | Related Functional Area |
|---|---|---|---|---|
| BR-PLT-001 | Organization Registration Approval | BR-001 | Organization Onboarding | Organization |
| BR-PLT-003 | Multi-Tenant Isolation | BR-001, BR-029 | Platform Administration | Security and Access Control |
| BR-ORG-004 | Organization Policies | BR-002, BR-030 | Organization Management | Organization Settings |
| BR-FAC-004 | Facility Capacity | BR-003, BR-004 | Facility Management | Facility Configuration |
| BR-SUB-001 | Subscription Ownership | BR-027, BR-028 | BP-SUB-001, BP-LIC-001 | Subscription Management, License Management |
| BR-SUB-002 | Facility-Level Subscription | BR-027, BR-028 | BP-SUB-001, BP-LIC-001 | Subscription Management, License Management |
| BR-SUB-003 | Site Add-on Licensing | BR-027, BR-028 | BP-SUB-001, BP-LIC-001 | Subscription Management, License Management |
| BR-SUB-004 | Active Subscription Requirement | BR-027, BR-028 | BP-SUB-001, BP-LIC-001 | Subscription Management, License Management |
| BR-SUB-005 | Subscription Plan Assignment | BR-027, BR-028 | BP-SUB-001, BP-LIC-001 | Subscription Management, License Management |
| BR-SIT-006 | Site Capacity | BR-005 | Site Management | Site Configuration |
| BR-CUS-004 | Duplicate Customer Prevention | BR-007 | Customer Registration | Customer Management |
| BR-CUS-009 | Customer Historical Records | BR-007 | Customer Management | Customer History |
| BR-MEM-003 | Payment Before Activation | BR-009 | Membership Purchase | Membership Lifecycle |
| BR-MEM-006 | Membership Renewal | BR-010 | Membership Renewal | Membership Management |
| BR-ATT-004 | Membership Validation | BR-013 | Attendance Management | Attendance Validation |
| BR-ATT-005 | Walk-in Attendance | BR-014 | Walk-in Customer Flow | Walk-in Management |
| BR-BIL-002 | Unique Invoice Number | BR-018 | Billing Management | Invoice Management |
| BR-BIL-006 | Credit Notes | BR-020 | Refund Management | Credit Management |
| BR-PAY-001 | Payment Confirmation | BR-019 | Payment Management | Payment Validation |
| BR-PAY-006 | Refunds | BR-020 | Refund Management | Refund Processing |
| BR-NOT-001 | Event-Based Notifications | BR-022 | Notification Management | Communication |
| BR-RPT-001 | Authorized Access | BR-024 | Reporting & Analytics | Reporting Access |
| BR-SEC-002 | Role-Based Access Control | BR-006, BR-029 | User & Role Management | Security |
| BR-AUD-001 | Audit Logging | BR-026 | Audit & Compliance | Audit Trail |
| BR-AUD-008 | Cross-Module Traceability | BR-001 to BR-030 | All domains | Governance |

---

# 5. Business Process Traceability

The following table links business processes from BA-03 to the operational and delivery artifacts they influence.

| Business Process ID | Business Process | Requirement IDs | Journey | Functional Module | UI Screen | API | Database Entity | Test Cases |
|---|---|---|---|---|---|---|---|---|
| BP-ORG-001 | Create Organization Profile | BR-001 | Organization Onboarding Journey | Organization | Organization Registration | POST /organizations | Organization | TC-001 |
| BP-ORG-002 | Update Organization Profile | BR-002 | Organization Administrator Journey | Organization | Organization Profile | PATCH /organizations/{id} | Organization | TC-002 |
| BP-FAC-001 | Create Facility | BR-003 | Organization Administrator Journey | Facility | Facility Management | POST /facilities | Facility | TC-012 |
| BP-SIT-001 | Create Site | BR-005 | Site Administrator Journey | Site | Site Management | POST /sites | Site | TC-021 |
| BP-STA-001 | Create Staff Account | BR-006 | Organization Administrator Journey | Staff Identity | Staff Management | POST /staff | Staff Account | TC-031 |
| BP-CUS-001 | Register Customer | BR-007 | Customer Journey | Customer | Customer Registration | POST /customers | Customer | TC-041 |
| BP-MEM-001 | Create Membership | BR-009 | Membership Purchase Journey | Membership | Membership Purchase | POST /memberships | Membership | TC-051 |
| BP-MEM-003 | Renew Membership | BR-010 | Membership Renewal Journey | Membership | Membership Renewal | POST /memberships/{id}/renew | Membership Renewal | TC-052 |
| BP-MEM-009 | Cancel Membership | BR-012 | Membership Journey | Membership | Membership Cancellation | POST /memberships/{id}/cancel | Membership Cancellation | TC-054 |
| BP-ATT-001 | Record Customer Check-in | BR-013 | Attendance Journey | Attendance | Attendance Check-in | POST /attendance/check-in | Attendance | TC-061 |
| BP-ATT-004 | Record Walk-in Attendance | BR-014 | Walk-in Customer Journey | Attendance | Walk-in Registration | POST /walkins | Walk-in Visit | TC-062 |
| BP-ACT-001 | Create Activity | BR-015 | Facility Manager Journey | Activity | Activity Management | POST /activities | Activity | TC-071 |
| BP-ACT-004 | Create Batch | BR-016 | Facility Manager Journey | Activity & Batch | Batch Schedule | POST /batches | Batch | TC-072 |
| BP-PTR-004 | Book Personal Training Session | BR-017 | Personal Training Journey | Personal Training | Session Booking | POST /training-sessions | Training Session | TC-081 |
| BP-BIL-001 | Generate Invoice | BR-018 | Payment Journey | Billing | Invoice Management | POST /invoices | Invoice | TC-091 |
| BP-PAY-001 | Collect Payment | BR-019 | Payment Journey | Payment | Payment Collection | POST /payments | Payment | TC-092 |
| BP-PAY-008 | Process Refund | BR-020 | Refund Journey | Payment | Refund Management | POST /refunds | Refund | TC-093 |
| BP-CMP-001 | Create Campaign | BR-021 | Advertisement Campaign Journey | Marketing | Campaign Management | POST /campaigns | Campaign | TC-101 |
| BP-NOT-003 | Generate System Notification | BR-022 | Notification Journey | Notification | Notification Center | POST /notifications | Notification | TC-102 |
| BP-APR-001 | Create Approval Request | BR-023 | Approval Journey | Approval | Approval Management | POST /approvals | Approval Request | TC-103 |
| BP-RPT-001 | View Operational Dashboard | BR-024 | Reporting & Analytics Journey | Reporting | Operational Dashboard | GET /reports/dashboard | Report | TC-111 |
| BP-TKT-001 | Create Support Ticket | BR-025 | Support Ticket Journey | Support | Support Ticket Queue | POST /tickets | Support Ticket | TC-121 |
| BP-AUD-001 | Capture Business Activity | BR-026 | Audit & Compliance Journey | Audit | Audit Logs | POST /audit-events | Audit Log | TC-131 |

---

# 6. User Journey Traceability

| Journey ID | User Journey | Related Persona | Related Process | Related Requirement IDs |
|---|---|---|---|---|
| UJ-001 | Platform Administrator Journey | Platform Administrator | Platform Administration | BR-029 |
| UJ-002 | Organization Administrator Journey | Organization Administrator | Organization Management | BR-002 |
| UJ-003 | Facility Manager Journey | Facility Manager | Facility Management | BR-003, BR-004 |
| UJ-004 | Site Administrator Journey | Site Administrator | Site Management | BR-005 |
| UJ-005 | Reception Staff Journey | Reception Staff | Customer, Membership, Attendance, Billing, Payment | BR-007 to BR-019 |
| UJ-006 | Trainer Journey | Trainer | Activity, Batch, Personal Training | BR-015 to BR-017 |
| UJ-007 | Finance Staff Journey | Finance Staff | Billing, Payment, Refund | BR-018 to BR-020 |
| UJ-008 | Marketing Staff Journey | Marketing Staff | Advertisement Campaign | BR-021 |
| UJ-009 | Support Executive Journey | Support Executive | Support Ticket | BR-025 |
| UJ-010 | Customer Journey | Customer | Customer, Membership, Attendance, Billing, Payment, Support | BR-007 to BR-020, BR-025 |
| UJ-011 | Organization Onboarding Journey | Platform Administrator | Organization Onboarding | BR-001, BR-027, BR-028 |
| UJ-012 | Membership Purchase Journey | Reception Staff | Membership Purchase | BR-009, BR-018, BR-019 |
| UJ-013 | Membership Renewal Journey | Reception Staff | Membership Renewal | BR-010, BR-018, BR-019 |
| UJ-014 | Walk-in Customer Journey | Reception Staff | Walk-in Management | BR-014, BR-018, BR-019 |
| UJ-015 | Attendance Journey | Reception Staff | Attendance Management | BR-013, BR-014 |
| UJ-016 | Personal Training Journey | Trainer | Personal Training | BR-017, BR-018, BR-019 |
| UJ-017 | Payment Journey | Finance Staff | Payment Management | BR-018, BR-019 |
| UJ-018 | Advertisement Campaign Journey | Marketing Staff | Advertisement Campaign | BR-021, BR-022, BR-023 |
| UJ-019 | Support Ticket Journey | Support Executive | Support Ticket Management | BR-025 |

---

# 7. Functional Requirement Traceability

The functional layer translates business requirements and rules into solution behavior.

| Functional Module | Related Requirement IDs | Related Processes | Related Personas |
|---|---|---|---|
| Organization Management | BR-001, BR-002 | BP-ORG-001, BP-ORG-002 | Organization Administrator |
| Facility Management | BR-003, BR-004 | BP-FAC-001 | Facility Manager, Organization Administrator |
| Site Management | BR-005 | BP-SIT-001 | Site Administrator, Facility Manager |
| Staff Identity & Access | BR-006, BR-030 | BP-STA-001 | Organization Administrator |
| Customer Management | BR-007, BR-008 | BP-CUS-001, BP-CUS-003 | Reception Staff |
| Membership Management | BR-009 to BR-012 | BP-MEM-001, BP-MEM-003, BP-MEM-006, BP-MEM-009 | Reception Staff, Organization Administrator |
| Attendance Management | BR-013, BR-014 | BP-ATT-001, BP-ATT-004 | Reception Staff, Trainer |
| Activity & Batch | BR-015, BR-016 | BP-ACT-001, BP-ACT-004 | Facility Manager, Trainer |
| Personal Training | BR-017 | BP-PTR-004 | Trainer, Reception Staff |
| Billing | BR-018 | BP-BIL-001 | Reception Staff, Finance Staff |
| Payment | BR-019 | BP-PAY-001 | Reception Staff, Finance Staff |
| Refund | BR-020 | BP-PAY-008 | Finance Staff |
| Marketing | BR-021 | BP-CMP-001 | Marketing Staff |
| Notification | BR-022 | BP-NOT-003 | System, Organization Administrator |
| Approval | BR-023 | BP-APR-001 | Organization Administrator |
| Reporting | BR-024 | BP-RPT-001 | All operational personas |
| Support | BR-025 | BP-TKT-001 | Support Executive |
| Audit | BR-026 | BP-AUD-001 | Platform Administrator, Organization Administrator |
| Subscription | BR-027 | BP-SUB-001 | Platform Administrator |
| License | BR-028 | BP-LIC-001 | Platform Administrator |

---

# 8. UI Traceability

| UI Screen | Related Requirement IDs | Related Process | Related Persona |
|---|---|---|---|
| Organization Registration | BR-001 | BP-ORG-001 | Platform Administrator |
| Organization Dashboard | BR-002, BR-024 | BP-ORG-002, BP-RPT-001 | Organization Administrator |
| Facility Management | BR-003, BR-004 | BP-FAC-001 | Organization Administrator, Facility Manager |
| Site Management | BR-005 | BP-SIT-001 | Site Administrator |
| Staff Management | BR-006 | BP-STA-001 | Organization Administrator |
| Customer Registration | BR-007 | BP-CUS-001 | Reception Staff |
| Membership Purchase | BR-009 | BP-MEM-001 | Reception Staff |
| Membership Renewal | BR-010 | BP-MEM-003 | Reception Staff |
| Attendance Check-in | BR-013 | BP-ATT-001 | Reception Staff |
| Walk-in Registration | BR-014 | BP-ATT-004 | Reception Staff |
| Activity Management | BR-015 | BP-ACT-001 | Facility Manager |
| Batch Schedule | BR-016 | BP-ACT-004 | Facility Manager, Trainer |
| Training Session | BR-017 | BP-PTR-004 | Trainer |
| Invoice Management | BR-018 | BP-BIL-001 | Reception Staff, Finance Staff |
| Payment Collection | BR-019 | BP-PAY-001 | Reception Staff, Finance Staff |
| Refund Management | BR-020 | BP-PAY-008 | Finance Staff |
| Campaign Management | BR-021 | BP-CMP-001 | Marketing Staff |
| Notification Center | BR-022 | BP-NOT-003 | All operational personas |
| Approval Management | BR-023 | BP-APR-001 | Organization Administrator |
| Support Ticket Queue | BR-025 | BP-TKT-001 | Support Executive |
| Audit Logs | BR-026 | BP-AUD-001 | Platform Administrator, Organization Administrator |

---

# 9. API Traceability

| API Endpoint | Related Requirement IDs | Related Process | Related Entity |
|---|---|---|---|
| POST /organizations | BR-001 | BP-ORG-001 | Organization |
| PATCH /organizations/{id} | BR-002 | BP-ORG-002 | Organization |
| POST /facilities | BR-003 | BP-FAC-001 | Facility |
| PATCH /facilities/{id}/settings | BR-004 | BP-FAC-003 | Facility Setting |
| POST /sites | BR-005 | BP-SIT-001 | Site |
| POST /staff | BR-006 | BP-STA-001 | Staff Account |
| POST /customers | BR-007 | BP-CUS-001 | Customer |
| POST /customers/{id}/verify | BR-008 | BP-CUS-003 | Customer Verification |
| POST /memberships | BR-009 | BP-MEM-001 | Membership |
| POST /memberships/{id}/renew | BR-010 | BP-MEM-003 | Membership Renewal |
| POST /memberships/{id}/freeze | BR-011 | BP-MEM-006 | Membership Freeze |
| POST /memberships/{id}/cancel | BR-012 | BP-MEM-009 | Membership Cancellation |
| POST /attendance/check-in | BR-013 | BP-ATT-001 | Attendance |
| POST /walkins | BR-014 | BP-ATT-004 | Walk-in Visit |
| POST /activities | BR-015 | BP-ACT-001 | Activity |
| POST /batches | BR-016 | BP-ACT-004 | Batch |
| POST /training-sessions | BR-017 | BP-PTR-004 | Personal Training Session |
| POST /invoices | BR-018 | BP-BIL-001 | Invoice |
| POST /payments | BR-019 | BP-PAY-001 | Payment |
| POST /refunds | BR-020 | BP-PAY-008 | Refund |
| POST /campaigns | BR-021 | BP-CMP-001 | Campaign |
| POST /notifications | BR-022 | BP-NOT-003 | Notification |
| POST /approvals | BR-023 | BP-APR-001 | Approval Request |
| GET /reports/dashboard | BR-024 | BP-RPT-001 | Report |
| POST /tickets | BR-025 | BP-TKT-001 | Support Ticket |
| POST /audit-events | BR-026 | BP-AUD-001 | Audit Log |
| POST /subscriptions | BR-027 | BP-SUB-001 | Subscription |
| POST /licenses | BR-028 | BP-LIC-001 | License |
| PATCH /platform/settings | BR-029 | BP-ADM-001 | Platform Configuration |
| PATCH /business-rules | BR-030 | BP-PLT-009 | Business Rule |

---

# 10. Database Traceability

| Database Entity | Related Requirement IDs | Related Process | Related API |
|---|---|---|---|
| Organization | BR-001, BR-002 | BP-ORG-001, BP-ORG-002 | POST /organizations |
| Facility | BR-003, BR-004 | BP-FAC-001, BP-FAC-003 | POST /facilities |
| Site | BR-005 | BP-SIT-001 | POST /sites |
| Staff Account | BR-006 | BP-STA-001 | POST /staff |
| Customer | BR-007, BR-008 | BP-CUS-001, BP-CUS-003 | POST /customers |
| Membership | BR-009 to BR-012 | BP-MEM-001 to BP-MEM-009 | POST /memberships |
| Attendance | BR-013, BR-014 | BP-ATT-001, BP-ATT-004 | POST /attendance/check-in |
| Activity | BR-015 | BP-ACT-001 | POST /activities |
| Batch | BR-016 | BP-ACT-004 | POST /batches |
| Training Session | BR-017 | BP-PTR-004 | POST /training-sessions |
| Invoice | BR-018 | BP-BIL-001 | POST /invoices |
| Payment | BR-019 | BP-PAY-001 | POST /payments |
| Refund | BR-020 | BP-PAY-008 | POST /refunds |
| Campaign | BR-021 | BP-CMP-001 | POST /campaigns |
| Notification | BR-022 | BP-NOT-003 | POST /notifications |
| Approval Request | BR-023 | BP-APR-001 | POST /approvals |
| Report | BR-024 | BP-RPT-001 | GET /reports/dashboard |
| Support Ticket | BR-025 | BP-TKT-001 | POST /tickets |
| Audit Log | BR-026 | BP-AUD-001 | POST /audit-events |
| Subscription | BR-027 | BP-SUB-001 | POST /subscriptions |
| License | BR-028 | BP-LIC-001 | POST /licenses |
| Platform Configuration | BR-029 | BP-ADM-001 | PATCH /platform/settings |
| Business Rule | BR-030 | BP-PLT-009 | PATCH /business-rules |

---

# 11. Test Case Traceability

| Test Case ID | Related Requirement IDs | Related Process | Test Focus |
|---|---|---|---|
| TC-001 | BR-001 | BP-ORG-001 | Organization registration |
| TC-002 | BR-002 | BP-ORG-002 | Organization profile update |
| TC-012 | BR-003 | BP-FAC-001 | Facility creation |
| TC-013 | BR-004 | BP-FAC-003 | Facility settings |
| TC-021 | BR-005 | BP-SIT-001 | Site creation |
| TC-031 | BR-006 | BP-STA-001 | Staff account creation |
| TC-041 | BR-007 | BP-CUS-001 | Customer registration |
| TC-042 | BR-008 | BP-CUS-003 | Identity verification |
| TC-051 | BR-009 | BP-MEM-001 | Membership purchase |
| TC-052 | BR-010 | BP-MEM-003 | Membership renewal |
| TC-053 | BR-011 | BP-MEM-006 | Membership freeze |
| TC-054 | BR-012 | BP-MEM-009 | Membership cancellation |
| TC-061 | BR-013 | BP-ATT-001 | Attendance check-in |
| TC-062 | BR-014 | BP-ATT-004 | Walk-in attendance |
| TC-071 | BR-015 | BP-ACT-001 | Activity setup |
| TC-072 | BR-016 | BP-ACT-004 | Batch scheduling |
| TC-081 | BR-017 | BP-PTR-004 | Personal training booking |
| TC-091 | BR-018 | BP-BIL-001 | Invoice generation |
| TC-092 | BR-019 | BP-PAY-001 | Payment collection |
| TC-093 | BR-020 | BP-PAY-008 | Refund processing |
| TC-101 | BR-021 | BP-CMP-001 | Campaign creation |
| TC-102 | BR-022 | BP-NOT-003 | Notification generation |
| TC-103 | BR-023 | BP-APR-001 | Approval request workflow |
| TC-111 | BR-024 | BP-RPT-001 | Reporting dashboard |
| TC-121 | BR-025 | BP-TKT-001 | Ticket creation |
| TC-131 | BR-026 | BP-AUD-001 | Audit logging |
| TC-141 | BR-027 | BP-SUB-001 | Subscription creation |
| TC-142 | BR-028 | BP-LIC-001 | License generation |
| TC-151 | BR-029 | BP-ADM-001 | Platform configuration |
| TC-152 | BR-030 | BP-PLT-009 | Business rule management |

---

# 12. Requirement Coverage Analysis

The following coverage view tracks the implementation completeness of the current baseline.

| Area | Total | Completed | Pending |
|---|---:|---:|---:|
| Business Requirements | 30 | 20 | 10 |
| Business Rules | 20 | 20 | 0 |
| Business Processes | 25 | 25 | 0 |
| User Journeys | 19 | 19 | 0 |
| Functional Requirements | 30 | 20 | 10 |
| UI Screens | 30 | 20 | 10 |
| APIs | 30 | 20 | 10 |
| Database Entities | 30 | 20 | 10 |
| Test Cases | 30 | 20 | 10 |

> Note: The counts above represent the current working baseline of the RTM and should be updated as the FRS, API specification, database design, and test catalog mature.

---

# 13. Change Impact Analysis

When a requirement changes, the traceability matrix must identify the affected artifacts.

| Changed Requirement | Business Process | API | Database | UI | Test Cases |
|---|---|---|---|---|---|
| Membership Renewal | BP-MEM-003 | Membership API | Membership Renewal | Membership Renewal Screen | TC-052 |
| Attendance Recording | BP-ATT-001 | Attendance API | Attendance | Attendance Check-in | TC-061 |
| Payment Collection | BP-PAY-001 | Payment API | Payment | Payment Collection | TC-092 |
| Refund Processing | BP-PAY-008 | Refund API | Refund | Refund Management | TC-093 |
| Campaign Approval | BP-APR-004 | Approval Workflow API | Approval Request | Approval Management | TC-103 |
| Organization Configuration | BP-ORG-002 | Organization API | Organization | Organization Profile | TC-002 |

This section supports impact analysis for requirement changes, design revisions, regression planning, and release governance.

---

# 14. Requirement Status Matrix

| Status | Meaning |
|---|---|
| Proposed | Requirement identified but not approved |
| Approved | Accepted for implementation |
| In Progress | Currently being implemented |
| Implemented | Development completed |
| Tested | Successfully validated |
| Released | Available in production |
| Deprecated | No longer supported |

---

# 16. Action Items for Planned Requirements

The following business requirements are currently marked as `Planned` in this baseline RTM. Each item below requires the indicated minimal artifacts to progress toward implementation readiness.

| Requirement ID | Minimal Next Actions |
|---|---|
| BR-003 | Complete FRS for `Facility` (detailed API, DB entity, validation rules), assign implementation owner, create TC-012 acceptance criteria |
| BR-004 | Define facility configuration payloads and settings in FRS; confirm API contract `PATCH /facilities/{id}/settings` |
| BR-005 | Finalize Site model in FRS and DB design; validate `POST /sites` API specification |
| BR-006 | Specify staff identity creation workflow, role mapping, and security controls in FRS |
| BR-008 | Define identity verification steps, expected outcomes, and API behavior in FRS |
| BR-011 | Document membership freeze business rule exceptions and API semantics |
| BR-012 | Define cancellation rules, refund triggers, and API behavior |
| BR-014 | Document walk-in processing rules and required API contract for `POST /walkins` |
| BR-015 | Capture activity configuration attributes and validations in FRS |
| BR-016 | Define batch scheduling constraints and API model for `POST /batches/{id}/schedule` |
| BR-017 | Finalize personal training booking flows and API contract |
| BR-020 | Define refund processing controls, approvals, and reconciliation requirements |
| BR-021 | Capture campaign management data model and API behavior for campaigns |
| BR-023 | Define approval workflow triggers, states, and integration touchpoints |
| BR-030 | Finalize business rule management model, RBAC, and `PATCH /business-rules` contract |

Notes:
- Owners and implementation dates should be added during release planning.
- These action items are intentionally minimal and factual; further expansion belongs in the FRS, API specs, and test plan artifacts.

---

# 15. Summary

The Requirement Traceability Matrix provides the governance bridge between business needs, business rules, business processes, user journeys, functional implementation, user interfaces, APIs, database entities, and test coverage.

It is the primary control document for ensuring that Digitize remains traceable, testable, maintainable, and aligned across analysis, design, development, validation, and deployment.

As the platform evolves, BA-08 should remain the authoritative reference for change impact analysis, coverage review, and cross-document traceability.

**End of BA-08 - Requirement Traceability Matrix**
