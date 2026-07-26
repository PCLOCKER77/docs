# DEV-18 Complete User Story Catalog

> Complete development story catalog for Digitize, generated from approved functional requirements and implementation-readiness documentation.

---

# Document Control

| Field | Value |
|---|---|
| Document ID | DEV-18 |
| Document Name | Complete User Story Catalog |
| Folder | 16_Development_Readiness |
| Product | Digitize by OreeOn Technologies Pvt. Ltd. |
| Status | Design Draft |
| Owner | Product / Engineering / QA |
| Reviewers | Business Analysis, Functional Requirements, UI/UX, API, Database, Backend, DevOps, QA, Release Management |
| Version | 1.0 |
| Last Updated | 2026-07-24 |

---

# 1. Purpose

This document is the complete user-story source of truth before development starts.

It exists because Digitize is not currently using an external agile tool. The documentation repository therefore owns feature, story, status, traceability, and implementation planning until a tool is adopted.

This catalog includes:

- Product user stories derived from approved Functional Requirements.
- Frontend implementation stories for Flutter web, Android, and iOS.
- Backend implementation stories for FastAPI modular monolith development.
- Database implementation stories for PostgreSQL and Alembic.
- Testing, deployment, release, and operations readiness stories required to ship safely.

---

# 2. Story Count

| Story Category | Count | Source |
|---|---:|---|
| Product requirement stories | 237 | FR-02 through FR-21 |
| Technical implementation stories | 40 | DEV, BE, DB, DEP, TEST, OPS, RELM docs |
| Total tracked stories before development | 277 | DEV-18 |

---

# 3. Product Story Count by Module

| Module | Story Range | Count |
|---|---|---:|
| Platform Administration | US-PLT-001 through US-PLT-012 | 12 |
| Organization Management | US-ORG-001 through US-ORG-010 | 10 |
| Facility Management | US-FAC-001 through US-FAC-012 | 12 |
| Site Management | US-SIT-001 through US-SIT-011 | 11 |
| User and Role Management | US-USR-001 through US-USR-012 | 12 |
| Customer Management | US-CUS-001 through US-CUS-012 | 12 |
| Membership Management | US-MEM-001 through US-MEM-012 | 12 |
| Attendance Management | US-ATT-001 through US-ATT-010 | 10 |
| Walk-in Customer Management | US-WLK-001 through US-WLK-007 | 7 |
| Trainer Management | US-TRN-001 through US-TRN-010 | 10 |
| Personal Training | US-PTR-001 through US-PTR-012 | 12 |
| Batch and Class Management | US-BAT-001 through US-BAT-015 | 15 |
| Billing and Payment Management | US-BPM-001 through US-BPM-018 | 18 |
| Subscription Management | US-SUB-001 through US-SUB-012 | 12 |
| License Management | US-LIC-001 through US-LIC-012 | 12 |
| Advertisement Campaign | US-CMP-001 through US-CMP-012 | 12 |
| Notification Management | US-NOT-001 through US-NOT-012 | 12 |
| Reports and Analytics | US-RPT-001 through US-RPT-012 | 12 |
| Support Ticket Management | US-TKT-001 through US-TKT-012 | 12 |
| Audit and Compliance | US-AUD-001 through US-AUD-012 | 12 |

---

# 4. Story Readiness Standard

A story is Ready only when:

- Source FR is known.
- Actor is known.
- UI route or screen dependency is known or explicitly not applicable.
- API contract is known or mock contract is available.
- Backend service, repository, and tenant context impact are understood.
- Database table or migration impact is known.
- Acceptance criteria can be tested.
- Test type is identified.
- Deployment or operational impact is identified where relevant.

Most stories start in Backlog. They move to Ready during sprint planning after detailed acceptance criteria are confirmed from the source FR.

---

# 5. Product User Story Register

Each row below maps one approved Functional Requirement to one product user story. Detailed acceptance criteria remain in the source FR and are expanded into sprint-ready story notes when the story is selected for implementation.

| Story ID | Source FR | Module | Actor | User Story | Required Build Coverage | Priority | Status |
|---|---|---|---|---|---|---|---|
| US-PLT-001 | FR-PLT-001 | Platform Administration | Platform Admin | As Platform Admin, I want to configure platform settings so that platform administration requirements are delivered. | FE, BE, DB, API, QA | P0 | Backlog |
| US-PLT-002 | FR-PLT-002 | Platform Administration | Platform Admin | As Platform Admin, I want to manage global master data so that platform administration requirements are delivered. | FE, BE, DB, API, QA | P0 | Backlog |
| US-PLT-003 | FR-PLT-003 | Platform Administration | Platform Admin | As Platform Admin, I want to configure subscription plans so that platform administration requirements are delivered. | FE, BE, DB, API, QA | P0 | Backlog |
| US-PLT-004 | FR-PLT-004 | Platform Administration | Platform Admin | As Platform Admin, I want to configure license templates so that platform administration requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-PLT-005 | FR-PLT-005 | Platform Administration | Platform Admin | As Platform Admin, I want to manage feature flags so that platform administration requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-PLT-006 | FR-PLT-006 | Platform Administration | Platform Admin | As Platform Admin, I want to configure global business rules so that platform administration requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-PLT-007 | FR-PLT-007 | Platform Administration | Platform Admin | As Platform Admin, I want to monitor platform health so that platform administration requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-PLT-008 | FR-PLT-008 | Platform Administration | Platform Admin | As Platform Admin, I want to schedule system maintenance so that platform administration requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-PLT-009 | FR-PLT-009 | Platform Administration | Platform Admin | As Platform Admin, I want to manage platform releases so that platform administration requirements are delivered. | FE, BE, DB, API, QA | P2 | Backlog |
| US-PLT-010 | FR-PLT-010 | Platform Administration | Platform Admin | As Platform Admin, I want to review platform usage so that platform administration requirements are delivered. | FE, BE, DB, API, QA | P2 | Backlog |
| US-PLT-011 | FR-PLT-011 | Platform Administration | Platform Admin | As Platform Admin, I want to manage platform security policies so that platform administration requirements are delivered. | FE, BE, DB, API, QA | P2 | Backlog |
| US-PLT-012 | FR-PLT-012 | Platform Administration | Platform Admin | As Platform Admin, I want to generate platform reports so that platform administration requirements are delivered. | FE, BE, DB, API, QA | P2 | Backlog |
| US-ORG-001 | FR-ORG-001 | Organization Management | Platform Admin / Organization Admin | As Platform Admin / Organization Admin, I want to create organization profile so that organization management requirements are delivered. | FE, BE, DB, API, QA | P0 | Backlog |
| US-ORG-002 | FR-ORG-002 | Organization Management | Platform Admin / Organization Admin | As Platform Admin / Organization Admin, I want to update organization profile so that organization management requirements are delivered. | FE, BE, DB, API, QA | P0 | Backlog |
| US-ORG-003 | FR-ORG-003 | Organization Management | Platform Admin / Organization Admin | As Platform Admin / Organization Admin, I want to configure organization settings so that organization management requirements are delivered. | FE, BE, DB, API, QA | P0 | Backlog |
| US-ORG-004 | FR-ORG-004 | Organization Management | Platform Admin / Organization Admin | As Platform Admin / Organization Admin, I want to configure business policies so that organization management requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-ORG-005 | FR-ORG-005 | Organization Management | Platform Admin / Organization Admin | As Platform Admin / Organization Admin, I want to manage organization branding so that organization management requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-ORG-006 | FR-ORG-006 | Organization Management | Platform Admin / Organization Admin | As Platform Admin / Organization Admin, I want to manage organization documents so that organization management requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-ORG-007 | FR-ORG-007 | Organization Management | Platform Admin / Organization Admin | As Platform Admin / Organization Admin, I want to activate organization so that organization management requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-ORG-008 | FR-ORG-008 | Organization Management | Platform Admin / Organization Admin | As Platform Admin / Organization Admin, I want to suspend organization so that organization management requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-ORG-009 | FR-ORG-009 | Organization Management | Platform Admin / Organization Admin | As Platform Admin / Organization Admin, I want to archive organization so that organization management requirements are delivered. | FE, BE, DB, API, QA | P2 | Backlog |
| US-ORG-010 | FR-ORG-010 | Organization Management | Platform Admin / Organization Admin | As Platform Admin / Organization Admin, I want to view organization dashboard so that organization management requirements are delivered. | FE, BE, DB, API, QA | P2 | Backlog |
| US-FAC-001 | FR-FAC-001 | Facility Management | Organization Admin | As Organization Admin, I want to create facility so that facility management requirements are delivered. | FE, BE, DB, API, QA | P0 | Backlog |
| US-FAC-002 | FR-FAC-002 | Facility Management | Organization Admin | As Organization Admin, I want to update facility details so that facility management requirements are delivered. | FE, BE, DB, API, QA | P0 | Backlog |
| US-FAC-003 | FR-FAC-003 | Facility Management | Organization Admin | As Organization Admin, I want to configure facility settings so that facility management requirements are delivered. | FE, BE, DB, API, QA | P0 | Backlog |
| US-FAC-004 | FR-FAC-004 | Facility Management | Organization Admin | As Organization Admin, I want to assign facility type so that facility management requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-FAC-005 | FR-FAC-005 | Facility Management | Organization Admin | As Organization Admin, I want to configure operating hours so that facility management requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-FAC-006 | FR-FAC-006 | Facility Management | Organization Admin | As Organization Admin, I want to configure capacity limits so that facility management requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-FAC-007 | FR-FAC-007 | Facility Management | Organization Admin | As Organization Admin, I want to assign facility manager so that facility management requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-FAC-008 | FR-FAC-008 | Facility Management | Organization Admin | As Organization Admin, I want to activate facility so that facility management requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-FAC-009 | FR-FAC-009 | Facility Management | Organization Admin | As Organization Admin, I want to suspend facility so that facility management requirements are delivered. | FE, BE, DB, API, QA | P2 | Backlog |
| US-FAC-010 | FR-FAC-010 | Facility Management | Organization Admin | As Organization Admin, I want to archive facility so that facility management requirements are delivered. | FE, BE, DB, API, QA | P2 | Backlog |
| US-FAC-011 | FR-FAC-011 | Facility Management | Organization Admin | As Organization Admin, I want to view facility dashboard so that facility management requirements are delivered. | FE, BE, DB, API, QA | P2 | Backlog |
| US-FAC-012 | FR-FAC-012 | Facility Management | Organization Admin | As Organization Admin, I want to manage facility policies so that facility management requirements are delivered. | FE, BE, DB, API, QA | P2 | Backlog |
| US-SIT-001 | FR-SIT-001 | Site Management | Organization Admin / Site Admin | As Organization Admin / Site Admin, I want to create site so that site management requirements are delivered. | FE, BE, DB, API, QA | P0 | Backlog |
| US-SIT-002 | FR-SIT-002 | Site Management | Organization Admin / Site Admin | As Organization Admin / Site Admin, I want to update site details so that site management requirements are delivered. | FE, BE, DB, API, QA | P0 | Backlog |
| US-SIT-003 | FR-SIT-003 | Site Management | Organization Admin / Site Admin | As Organization Admin / Site Admin, I want to configure site settings so that site management requirements are delivered. | FE, BE, DB, API, QA | P0 | Backlog |
| US-SIT-004 | FR-SIT-004 | Site Management | Organization Admin / Site Admin | As Organization Admin / Site Admin, I want to configure site operating hours so that site management requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-SIT-005 | FR-SIT-005 | Site Management | Organization Admin / Site Admin | As Organization Admin / Site Admin, I want to configure site capacity limits so that site management requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-SIT-006 | FR-SIT-006 | Site Management | Organization Admin / Site Admin | As Organization Admin / Site Admin, I want to manage site documents so that site management requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-SIT-007 | FR-SIT-007 | Site Management | Organization Admin / Site Admin | As Organization Admin / Site Admin, I want to activate site so that site management requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-SIT-008 | FR-SIT-008 | Site Management | Organization Admin / Site Admin | As Organization Admin / Site Admin, I want to suspend site so that site management requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-SIT-009 | FR-SIT-009 | Site Management | Organization Admin / Site Admin | As Organization Admin / Site Admin, I want to archive site so that site management requirements are delivered. | FE, BE, DB, API, QA | P2 | Backlog |
| US-SIT-010 | FR-SIT-010 | Site Management | Organization Admin / Site Admin | As Organization Admin / Site Admin, I want to view site dashboard so that site management requirements are delivered. | FE, BE, DB, API, QA | P2 | Backlog |
| US-SIT-011 | FR-SIT-011 | Site Management | Organization Admin / Site Admin | As Organization Admin / Site Admin, I want to manage site policies so that site management requirements are delivered. | FE, BE, DB, API, QA | P2 | Backlog |
| US-USR-001 | FR-USR-001 | User and Role Management | Organization Admin / Authorized User | As Organization Admin / Authorized User, I want to create staff account so that user and role management requirements are delivered. | FE, BE, DB, API, QA | P0 | Backlog |
| US-USR-002 | FR-USR-002 | User and Role Management | Organization Admin / Authorized User | As Organization Admin / Authorized User, I want to update staff profile so that user and role management requirements are delivered. | FE, BE, DB, API, QA | P0 | Backlog |
| US-USR-003 | FR-USR-003 | User and Role Management | Organization Admin / Authorized User | As Organization Admin / Authorized User, I want to assign staff role so that user and role management requirements are delivered. | FE, BE, DB, API, QA | P0 | Backlog |
| US-USR-004 | FR-USR-004 | User and Role Management | Organization Admin / Authorized User | As Organization Admin / Authorized User, I want to assign facility access so that user and role management requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-USR-005 | FR-USR-005 | User and Role Management | Organization Admin / Authorized User | As Organization Admin / Authorized User, I want to assign site access so that user and role management requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-USR-006 | FR-USR-006 | User and Role Management | Organization Admin / Authorized User | As Organization Admin / Authorized User, I want to configure staff permissions so that user and role management requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-USR-007 | FR-USR-007 | User and Role Management | Organization Admin / Authorized User | As Organization Admin / Authorized User, I want to activate staff account so that user and role management requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-USR-008 | FR-USR-008 | User and Role Management | Organization Admin / Authorized User | As Organization Admin / Authorized User, I want to suspend staff account so that user and role management requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-USR-009 | FR-USR-009 | User and Role Management | Organization Admin / Authorized User | As Organization Admin / Authorized User, I want to reset staff credentials so that user and role management requirements are delivered. | FE, BE, DB, API, QA | P2 | Backlog |
| US-USR-010 | FR-USR-010 | User and Role Management | Organization Admin / Authorized User | As Organization Admin / Authorized User, I want to deactivate staff account so that user and role management requirements are delivered. | FE, BE, DB, API, QA | P2 | Backlog |
| US-USR-011 | FR-USR-011 | User and Role Management | Organization Admin / Authorized User | As Organization Admin / Authorized User, I want to view staff activity so that user and role management requirements are delivered. | FE, BE, DB, API, QA | P2 | Backlog |
| US-USR-012 | FR-USR-012 | User and Role Management | Organization Admin / Authorized User | As Organization Admin / Authorized User, I want to view staff directory so that user and role management requirements are delivered. | FE, BE, DB, API, QA | P2 | Backlog |
| US-CUS-001 | FR-CUS-001 | Customer Management | Staff / Site Admin | As Staff / Site Admin, I want to register customer so that customer management requirements are delivered. | FE, BE, DB, API, QA | P0 | Backlog |
| US-CUS-002 | FR-CUS-002 | Customer Management | Staff / Site Admin | As Staff / Site Admin, I want to update customer profile so that customer management requirements are delivered. | FE, BE, DB, API, QA | P0 | Backlog |
| US-CUS-003 | FR-CUS-003 | Customer Management | Staff / Site Admin | As Staff / Site Admin, I want to verify customer identity so that customer management requirements are delivered. | FE, BE, DB, API, QA | P0 | Backlog |
| US-CUS-004 | FR-CUS-004 | Customer Management | Staff / Site Admin | As Staff / Site Admin, I want to search customer so that customer management requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-CUS-005 | FR-CUS-005 | Customer Management | Staff / Site Admin | As Staff / Site Admin, I want to view customer profile so that customer management requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-CUS-006 | FR-CUS-006 | Customer Management | Staff / Site Admin | As Staff / Site Admin, I want to transfer customer between sites so that customer management requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-CUS-007 | FR-CUS-007 | Customer Management | Staff / Site Admin | As Staff / Site Admin, I want to suspend customer so that customer management requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-CUS-008 | FR-CUS-008 | Customer Management | Staff / Site Admin | As Staff / Site Admin, I want to reactivate customer so that customer management requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-CUS-009 | FR-CUS-009 | Customer Management | Staff / Site Admin | As Staff / Site Admin, I want to archive customer so that customer management requirements are delivered. | FE, BE, DB, API, QA | P2 | Backlog |
| US-CUS-010 | FR-CUS-010 | Customer Management | Staff / Site Admin | As Staff / Site Admin, I want to manage customer documents so that customer management requirements are delivered. | FE, BE, DB, API, QA | P2 | Backlog |
| US-CUS-011 | FR-CUS-011 | Customer Management | Staff / Site Admin | As Staff / Site Admin, I want to manage emergency contacts so that customer management requirements are delivered. | FE, BE, DB, API, QA | P2 | Backlog |
| US-CUS-012 | FR-CUS-012 | Customer Management | Staff / Site Admin | As Staff / Site Admin, I want to view customer history so that customer management requirements are delivered. | FE, BE, DB, API, QA | P2 | Backlog |
| US-MEM-001 | FR-MEM-001 | Membership Management | Staff / Site Admin | As Staff / Site Admin, I want to create membership so that membership management requirements are delivered. | FE, BE, DB, API, QA | P0 | Backlog |
| US-MEM-002 | FR-MEM-002 | Membership Management | Staff / Site Admin | As Staff / Site Admin, I want to activate membership so that membership management requirements are delivered. | FE, BE, DB, API, QA | P0 | Backlog |
| US-MEM-003 | FR-MEM-003 | Membership Management | Staff / Site Admin | As Staff / Site Admin, I want to renew membership so that membership management requirements are delivered. | FE, BE, DB, API, QA | P0 | Backlog |
| US-MEM-004 | FR-MEM-004 | Membership Management | Staff / Site Admin | As Staff / Site Admin, I want to upgrade membership so that membership management requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-MEM-005 | FR-MEM-005 | Membership Management | Staff / Site Admin | As Staff / Site Admin, I want to downgrade membership so that membership management requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-MEM-006 | FR-MEM-006 | Membership Management | Staff / Site Admin | As Staff / Site Admin, I want to freeze membership so that membership management requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-MEM-007 | FR-MEM-007 | Membership Management | Staff / Site Admin | As Staff / Site Admin, I want to resume membership so that membership management requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-MEM-008 | FR-MEM-008 | Membership Management | Staff / Site Admin | As Staff / Site Admin, I want to transfer membership so that membership management requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-MEM-009 | FR-MEM-009 | Membership Management | Staff / Site Admin | As Staff / Site Admin, I want to cancel membership so that membership management requirements are delivered. | FE, BE, DB, API, QA | P2 | Backlog |
| US-MEM-010 | FR-MEM-010 | Membership Management | Staff / Site Admin | As Staff / Site Admin, I want to expire membership so that membership management requirements are delivered. | FE, BE, DB, API, QA | P2 | Backlog |
| US-MEM-011 | FR-MEM-011 | Membership Management | Staff / Site Admin | As Staff / Site Admin, I want to view membership details so that membership management requirements are delivered. | FE, BE, DB, API, QA | P2 | Backlog |
| US-MEM-012 | FR-MEM-012 | Membership Management | Staff / Site Admin | As Staff / Site Admin, I want to view membership history so that membership management requirements are delivered. | FE, BE, DB, API, QA | P2 | Backlog |
| US-ATT-001 | FR-ATT-001 | Attendance Management | Staff / Site Admin | As Staff / Site Admin, I want to record customer check-in so that attendance management requirements are delivered. | FE, BE, DB, API, QA | P0 | Backlog |
| US-ATT-002 | FR-ATT-002 | Attendance Management | Staff / Site Admin | As Staff / Site Admin, I want to validate membership eligibility so that attendance management requirements are delivered. | FE, BE, DB, API, QA | P0 | Backlog |
| US-ATT-003 | FR-ATT-003 | Attendance Management | Staff / Site Admin | As Staff / Site Admin, I want to record session attendance so that attendance management requirements are delivered. | FE, BE, DB, API, QA | P0 | Backlog |
| US-ATT-004 | FR-ATT-004 | Attendance Management | Staff / Site Admin | As Staff / Site Admin, I want to record walk-in attendance so that attendance management requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-ATT-005 | FR-ATT-005 | Attendance Management | Staff / Site Admin | As Staff / Site Admin, I want to record customer check-out so that attendance management requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-ATT-006 | FR-ATT-006 | Attendance Management | Staff / Site Admin | As Staff / Site Admin, I want to update attendance record so that attendance management requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-ATT-007 | FR-ATT-007 | Attendance Management | Staff / Site Admin | As Staff / Site Admin, I want to cancel attendance record so that attendance management requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-ATT-008 | FR-ATT-008 | Attendance Management | Staff / Site Admin | As Staff / Site Admin, I want to view attendance history so that attendance management requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-ATT-009 | FR-ATT-009 | Attendance Management | Staff / Site Admin | As Staff / Site Admin, I want to generate attendance report so that attendance management requirements are delivered. | FE, BE, DB, API, QA | P2 | Backlog |
| US-ATT-010 | FR-ATT-010 | Attendance Management | Staff / Site Admin | As Staff / Site Admin, I want to audit attendance records so that attendance management requirements are delivered. | FE, BE, DB, API, QA | P2 | Backlog |
| US-WLK-001 | FR-WLK-001 | Walk-in Customer Management | Staff | As Staff, I want to identify or register walk-in customer so that walk-in customer management requirements are delivered. | FE, BE, DB, API, QA | P0 | Backlog |
| US-WLK-002 | FR-WLK-002 | Walk-in Customer Management | Staff | As Staff, I want to validate walk-in eligibility so that walk-in customer management requirements are delivered. | FE, BE, DB, API, QA | P0 | Backlog |
| US-WLK-003 | FR-WLK-003 | Walk-in Customer Management | Staff | As Staff, I want to create walk-in visit so that walk-in customer management requirements are delivered. | FE, BE, DB, API, QA | P0 | Backlog |
| US-WLK-004 | FR-WLK-004 | Walk-in Customer Management | Staff | As Staff, I want to calculate walk-in charges so that walk-in customer management requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-WLK-005 | FR-WLK-005 | Walk-in Customer Management | Staff | As Staff, I want to collect walk-in payment so that walk-in customer management requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-WLK-006 | FR-WLK-006 | Walk-in Customer Management | Staff | As Staff, I want to record walk-in attendance so that walk-in customer management requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-WLK-007 | FR-WLK-007 | Walk-in Customer Management | Staff | As Staff, I want to view walk-in history and reports so that walk-in customer management requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-TRN-001 | FR-TRN-001 | Trainer Management | Site Admin | As Site Admin, I want to register trainer profile so that trainer management requirements are delivered. | FE, BE, DB, API, QA | P0 | Backlog |
| US-TRN-002 | FR-TRN-002 | Trainer Management | Site Admin | As Site Admin, I want to assign trainer to facilities and sites so that trainer management requirements are delivered. | FE, BE, DB, API, QA | P0 | Backlog |
| US-TRN-003 | FR-TRN-003 | Trainer Management | Site Admin | As Site Admin, I want to maintain trainer availability so that trainer management requirements are delivered. | FE, BE, DB, API, QA | P0 | Backlog |
| US-TRN-004 | FR-TRN-004 | Trainer Management | Site Admin | As Site Admin, I want to validate trainer schedule conflicts so that trainer management requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-TRN-005 | FR-TRN-005 | Trainer Management | Site Admin | As Site Admin, I want to assign trainer to batch so that trainer management requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-TRN-006 | FR-TRN-006 | Trainer Management | Site Admin | As Site Admin, I want to assign trainer to personal training session so that trainer management requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-TRN-007 | FR-TRN-007 | Trainer Management | Site Admin | As Site Admin, I want to record trainer attendance so that trainer management requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-TRN-008 | FR-TRN-008 | Trainer Management | Site Admin | As Site Admin, I want to manage trainer status so that trainer management requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-TRN-009 | FR-TRN-009 | Trainer Management | Site Admin | As Site Admin, I want to view trainer history so that trainer management requirements are delivered. | FE, BE, DB, API, QA | P2 | Backlog |
| US-TRN-010 | FR-TRN-010 | Trainer Management | Site Admin | As Site Admin, I want to generate trainer performance summary so that trainer management requirements are delivered. | FE, BE, DB, API, QA | P2 | Backlog |
| US-PTR-001 | FR-PTR-001 | Personal Training | Site Admin / Staff | As Site Admin / Staff, I want to create personal training package so that personal training requirements are delivered. | FE, BE, DB, API, QA | P0 | Backlog |
| US-PTR-002 | FR-PTR-002 | Personal Training | Site Admin / Staff | As Site Admin / Staff, I want to configure training package so that personal training requirements are delivered. | FE, BE, DB, API, QA | P0 | Backlog |
| US-PTR-003 | FR-PTR-003 | Personal Training | Site Admin / Staff | As Site Admin / Staff, I want to assign trainer so that personal training requirements are delivered. | FE, BE, DB, API, QA | P0 | Backlog |
| US-PTR-004 | FR-PTR-004 | Personal Training | Site Admin / Staff | As Site Admin / Staff, I want to book personal training session so that personal training requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-PTR-005 | FR-PTR-005 | Personal Training | Site Admin / Staff | As Site Admin / Staff, I want to reschedule training session so that personal training requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-PTR-006 | FR-PTR-006 | Personal Training | Site Admin / Staff | As Site Admin / Staff, I want to cancel training session so that personal training requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-PTR-007 | FR-PTR-007 | Personal Training | Site Admin / Staff | As Site Admin / Staff, I want to start personal training session so that personal training requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-PTR-008 | FR-PTR-008 | Personal Training | Site Admin / Staff | As Site Admin / Staff, I want to complete personal training session so that personal training requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-PTR-009 | FR-PTR-009 | Personal Training | Site Admin / Staff | As Site Admin / Staff, I want to record training notes so that personal training requirements are delivered. | FE, BE, DB, API, QA | P2 | Backlog |
| US-PTR-010 | FR-PTR-010 | Personal Training | Site Admin / Staff | As Site Admin / Staff, I want to record customer progress so that personal training requirements are delivered. | FE, BE, DB, API, QA | P2 | Backlog |
| US-PTR-011 | FR-PTR-011 | Personal Training | Site Admin / Staff | As Site Admin / Staff, I want to view training history so that personal training requirements are delivered. | FE, BE, DB, API, QA | P2 | Backlog |
| US-PTR-012 | FR-PTR-012 | Personal Training | Site Admin / Staff | As Site Admin / Staff, I want to generate trainer performance report so that personal training requirements are delivered. | FE, BE, DB, API, QA | P2 | Backlog |
| US-BAT-001 | FR-BAT-001 | Batch and Class Management | Site Admin / Staff | As Site Admin / Staff, I want to create activity so that batch and class management requirements are delivered. | FE, BE, DB, API, QA | P0 | Backlog |
| US-BAT-002 | FR-BAT-002 | Batch and Class Management | Site Admin / Staff | As Site Admin / Staff, I want to update activity so that batch and class management requirements are delivered. | FE, BE, DB, API, QA | P0 | Backlog |
| US-BAT-003 | FR-BAT-003 | Batch and Class Management | Site Admin / Staff | As Site Admin / Staff, I want to configure activity rules so that batch and class management requirements are delivered. | FE, BE, DB, API, QA | P0 | Backlog |
| US-BAT-004 | FR-BAT-004 | Batch and Class Management | Site Admin / Staff | As Site Admin / Staff, I want to create batch so that batch and class management requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-BAT-005 | FR-BAT-005 | Batch and Class Management | Site Admin / Staff | As Site Admin / Staff, I want to update batch so that batch and class management requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-BAT-006 | FR-BAT-006 | Batch and Class Management | Site Admin / Staff | As Site Admin / Staff, I want to schedule batch so that batch and class management requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-BAT-007 | FR-BAT-007 | Batch and Class Management | Site Admin / Staff | As Site Admin / Staff, I want to assign trainer to batch so that batch and class management requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-BAT-008 | FR-BAT-008 | Batch and Class Management | Site Admin / Staff | As Site Admin / Staff, I want to configure batch capacity so that batch and class management requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-BAT-009 | FR-BAT-009 | Batch and Class Management | Site Admin / Staff | As Site Admin / Staff, I want to enroll customer into batch so that batch and class management requirements are delivered. | FE, BE, DB, API, QA | P2 | Backlog |
| US-BAT-010 | FR-BAT-010 | Batch and Class Management | Site Admin / Staff | As Site Admin / Staff, I want to remove customer from batch so that batch and class management requirements are delivered. | FE, BE, DB, API, QA | P2 | Backlog |
| US-BAT-011 | FR-BAT-011 | Batch and Class Management | Site Admin / Staff | As Site Admin / Staff, I want to start session so that batch and class management requirements are delivered. | FE, BE, DB, API, QA | P2 | Backlog |
| US-BAT-012 | FR-BAT-012 | Batch and Class Management | Site Admin / Staff | As Site Admin / Staff, I want to complete session so that batch and class management requirements are delivered. | FE, BE, DB, API, QA | P2 | Backlog |
| US-BAT-013 | FR-BAT-013 | Batch and Class Management | Site Admin / Staff | As Site Admin / Staff, I want to cancel session so that batch and class management requirements are delivered. | FE, BE, DB, API, QA | P3 | Backlog |
| US-BAT-014 | FR-BAT-014 | Batch and Class Management | Site Admin / Staff | As Site Admin / Staff, I want to view batch schedule so that batch and class management requirements are delivered. | FE, BE, DB, API, QA | P3 | Backlog |
| US-BAT-015 | FR-BAT-015 | Batch and Class Management | Site Admin / Staff | As Site Admin / Staff, I want to view activity performance so that batch and class management requirements are delivered. | FE, BE, DB, API, QA | P3 | Backlog |
| US-BPM-001 | FR-BPM-001 | Billing and Payment Management | Staff / Finance | As Staff / Finance, I want to generate invoice so that billing and payment management requirements are delivered. | FE, BE, DB, API, QA | P0 | Backlog |
| US-BPM-002 | FR-BPM-002 | Billing and Payment Management | Staff / Finance | As Staff / Finance, I want to calculate service charges so that billing and payment management requirements are delivered. | FE, BE, DB, API, QA | P0 | Backlog |
| US-BPM-003 | FR-BPM-003 | Billing and Payment Management | Staff / Finance | As Staff / Finance, I want to apply discounts so that billing and payment management requirements are delivered. | FE, BE, DB, API, QA | P0 | Backlog |
| US-BPM-004 | FR-BPM-004 | Billing and Payment Management | Staff / Finance | As Staff / Finance, I want to calculate taxes so that billing and payment management requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-BPM-005 | FR-BPM-005 | Billing and Payment Management | Staff / Finance | As Staff / Finance, I want to apply billing adjustments so that billing and payment management requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-BPM-006 | FR-BPM-006 | Billing and Payment Management | Staff / Finance | As Staff / Finance, I want to cancel invoice so that billing and payment management requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-BPM-007 | FR-BPM-007 | Billing and Payment Management | Staff / Finance | As Staff / Finance, I want to generate credit note so that billing and payment management requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-BPM-008 | FR-BPM-008 | Billing and Payment Management | Staff / Finance | As Staff / Finance, I want to collect payment so that billing and payment management requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-BPM-009 | FR-BPM-009 | Billing and Payment Management | Staff / Finance | As Staff / Finance, I want to process online payment so that billing and payment management requirements are delivered. | FE, BE, DB, API, QA | P2 | Backlog |
| US-BPM-010 | FR-BPM-010 | Billing and Payment Management | Staff / Finance | As Staff / Finance, I want to record offline payment so that billing and payment management requirements are delivered. | FE, BE, DB, API, QA | P2 | Backlog |
| US-BPM-011 | FR-BPM-011 | Billing and Payment Management | Staff / Finance | As Staff / Finance, I want to verify payment status so that billing and payment management requirements are delivered. | FE, BE, DB, API, QA | P2 | Backlog |
| US-BPM-012 | FR-BPM-012 | Billing and Payment Management | Staff / Finance | As Staff / Finance, I want to generate payment receipt so that billing and payment management requirements are delivered. | FE, BE, DB, API, QA | P2 | Backlog |
| US-BPM-013 | FR-BPM-013 | Billing and Payment Management | Staff / Finance | As Staff / Finance, I want to process refund so that billing and payment management requirements are delivered. | FE, BE, DB, API, QA | P3 | Backlog |
| US-BPM-014 | FR-BPM-014 | Billing and Payment Management | Staff / Finance | As Staff / Finance, I want to reconcile payment so that billing and payment management requirements are delivered. | FE, BE, DB, API, QA | P3 | Backlog |
| US-BPM-015 | FR-BPM-015 | Billing and Payment Management | Staff / Finance | As Staff / Finance, I want to cancel payment so that billing and payment management requirements are delivered. | FE, BE, DB, API, QA | P3 | Backlog |
| US-BPM-016 | FR-BPM-016 | Billing and Payment Management | Staff / Finance | As Staff / Finance, I want to view billing and payment history so that billing and payment management requirements are delivered. | FE, BE, DB, API, QA | P3 | Backlog |
| US-BPM-017 | FR-BPM-017 | Billing and Payment Management | Staff / Finance | As Staff / Finance, I want to generate commercial reports so that billing and payment management requirements are delivered. | FE, BE, DB, API, QA | P3 | Backlog |
| US-BPM-018 | FR-BPM-018 | Billing and Payment Management | Staff / Finance | As Staff / Finance, I want to generate outstanding statement so that billing and payment management requirements are delivered. | FE, BE, DB, API, QA | P3 | Backlog |
| US-SUB-001 | FR-SUB-001 | Subscription Management | Platform Admin | As Platform Admin, I want to create subscription so that subscription management requirements are delivered. | FE, BE, DB, API, QA | P0 | Backlog |
| US-SUB-002 | FR-SUB-002 | Subscription Management | Platform Admin | As Platform Admin, I want to assign subscription plan so that subscription management requirements are delivered. | FE, BE, DB, API, QA | P0 | Backlog |
| US-SUB-003 | FR-SUB-003 | Subscription Management | Platform Admin | As Platform Admin, I want to activate subscription so that subscription management requirements are delivered. | FE, BE, DB, API, QA | P0 | Backlog |
| US-SUB-004 | FR-SUB-004 | Subscription Management | Platform Admin | As Platform Admin, I want to renew subscription so that subscription management requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-SUB-005 | FR-SUB-005 | Subscription Management | Platform Admin | As Platform Admin, I want to upgrade subscription plan so that subscription management requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-SUB-006 | FR-SUB-006 | Subscription Management | Platform Admin | As Platform Admin, I want to downgrade subscription plan so that subscription management requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-SUB-007 | FR-SUB-007 | Subscription Management | Platform Admin | As Platform Admin, I want to suspend subscription so that subscription management requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-SUB-008 | FR-SUB-008 | Subscription Management | Platform Admin | As Platform Admin, I want to cancel subscription so that subscription management requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-SUB-009 | FR-SUB-009 | Subscription Management | Platform Admin | As Platform Admin, I want to expire subscription so that subscription management requirements are delivered. | FE, BE, DB, API, QA | P2 | Backlog |
| US-SUB-010 | FR-SUB-010 | Subscription Management | Platform Admin | As Platform Admin, I want to generate renewal invoice so that subscription management requirements are delivered. | FE, BE, DB, API, QA | P2 | Backlog |
| US-SUB-011 | FR-SUB-011 | Subscription Management | Platform Admin | As Platform Admin, I want to view subscription history so that subscription management requirements are delivered. | FE, BE, DB, API, QA | P2 | Backlog |
| US-SUB-012 | FR-SUB-012 | Subscription Management | Platform Admin | As Platform Admin, I want to generate subscription reports so that subscription management requirements are delivered. | FE, BE, DB, API, QA | P2 | Backlog |
| US-LIC-001 | FR-LIC-001 | License Management | Platform Admin / System | As Platform Admin / System, I want to generate license so that license management requirements are delivered. | FE, BE, DB, API, QA | P0 | Backlog |
| US-LIC-002 | FR-LIC-002 | License Management | Platform Admin / System | As Platform Admin / System, I want to assign license to facility so that license management requirements are delivered. | FE, BE, DB, API, QA | P0 | Backlog |
| US-LIC-003 | FR-LIC-003 | License Management | Platform Admin / System | As Platform Admin / System, I want to activate license so that license management requirements are delivered. | FE, BE, DB, API, QA | P0 | Backlog |
| US-LIC-004 | FR-LIC-004 | License Management | Platform Admin / System | As Platform Admin / System, I want to renew license so that license management requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-LIC-005 | FR-LIC-005 | License Management | Platform Admin / System | As Platform Admin / System, I want to modify licensed capabilities so that license management requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-LIC-006 | FR-LIC-006 | License Management | Platform Admin / System | As Platform Admin / System, I want to suspend license so that license management requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-LIC-007 | FR-LIC-007 | License Management | Platform Admin / System | As Platform Admin / System, I want to expire license so that license management requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-LIC-008 | FR-LIC-008 | License Management | Platform Admin / System | As Platform Admin / System, I want to cancel license so that license management requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-LIC-009 | FR-LIC-009 | License Management | Platform Admin / System | As Platform Admin / System, I want to validate license during login so that license management requirements are delivered. | FE, BE, DB, API, QA | P2 | Backlog |
| US-LIC-010 | FR-LIC-010 | License Management | Platform Admin / System | As Platform Admin / System, I want to view license details so that license management requirements are delivered. | FE, BE, DB, API, QA | P2 | Backlog |
| US-LIC-011 | FR-LIC-011 | License Management | Platform Admin / System | As Platform Admin / System, I want to view license history so that license management requirements are delivered. | FE, BE, DB, API, QA | P2 | Backlog |
| US-LIC-012 | FR-LIC-012 | License Management | Platform Admin / System | As Platform Admin / System, I want to generate license reports so that license management requirements are delivered. | FE, BE, DB, API, QA | P2 | Backlog |
| US-CMP-001 | FR-CMP-001 | Advertisement Campaign | Marketing Staff / Organization Admin | As Marketing Staff / Organization Admin, I want to create campaign so that advertisement campaign requirements are delivered. | FE, BE, DB, API, QA | P0 | Backlog |
| US-CMP-002 | FR-CMP-002 | Advertisement Campaign | Marketing Staff / Organization Admin | As Marketing Staff / Organization Admin, I want to configure campaign so that advertisement campaign requirements are delivered. | FE, BE, DB, API, QA | P0 | Backlog |
| US-CMP-003 | FR-CMP-003 | Advertisement Campaign | Marketing Staff / Organization Admin | As Marketing Staff / Organization Admin, I want to select target audience so that advertisement campaign requirements are delivered. | FE, BE, DB, API, QA | P0 | Backlog |
| US-CMP-004 | FR-CMP-004 | Advertisement Campaign | Marketing Staff / Organization Admin | As Marketing Staff / Organization Admin, I want to submit campaign for approval so that advertisement campaign requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-CMP-005 | FR-CMP-005 | Advertisement Campaign | Marketing Staff / Organization Admin | As Marketing Staff / Organization Admin, I want to approve campaign so that advertisement campaign requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-CMP-006 | FR-CMP-006 | Advertisement Campaign | Marketing Staff / Organization Admin | As Marketing Staff / Organization Admin, I want to schedule campaign so that advertisement campaign requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-CMP-007 | FR-CMP-007 | Advertisement Campaign | Marketing Staff / Organization Admin | As Marketing Staff / Organization Admin, I want to launch campaign so that advertisement campaign requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-CMP-008 | FR-CMP-008 | Advertisement Campaign | Marketing Staff / Organization Admin | As Marketing Staff / Organization Admin, I want to pause campaign so that advertisement campaign requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-CMP-009 | FR-CMP-009 | Advertisement Campaign | Marketing Staff / Organization Admin | As Marketing Staff / Organization Admin, I want to complete campaign so that advertisement campaign requirements are delivered. | FE, BE, DB, API, QA | P2 | Backlog |
| US-CMP-010 | FR-CMP-010 | Advertisement Campaign | Marketing Staff / Organization Admin | As Marketing Staff / Organization Admin, I want to cancel campaign so that advertisement campaign requirements are delivered. | FE, BE, DB, API, QA | P2 | Backlog |
| US-CMP-011 | FR-CMP-011 | Advertisement Campaign | Marketing Staff / Organization Admin | As Marketing Staff / Organization Admin, I want to monitor campaign performance so that advertisement campaign requirements are delivered. | FE, BE, DB, API, QA | P2 | Backlog |
| US-CMP-012 | FR-CMP-012 | Advertisement Campaign | Marketing Staff / Organization Admin | As Marketing Staff / Organization Admin, I want to generate campaign report so that advertisement campaign requirements are delivered. | FE, BE, DB, API, QA | P2 | Backlog |
| US-NOT-001 | FR-NOT-001 | Notification Management | System / Organization Admin | As System / Organization Admin, I want to create notification template so that notification management requirements are delivered. | FE, BE, DB, API, QA | P0 | Backlog |
| US-NOT-002 | FR-NOT-002 | Notification Management | System / Organization Admin | As System / Organization Admin, I want to configure notification rules so that notification management requirements are delivered. | FE, BE, DB, API, QA | P0 | Backlog |
| US-NOT-003 | FR-NOT-003 | Notification Management | System / Organization Admin | As System / Organization Admin, I want to generate system notification so that notification management requirements are delivered. | FE, BE, DB, API, QA | P0 | Backlog |
| US-NOT-004 | FR-NOT-004 | Notification Management | System / Organization Admin | As System / Organization Admin, I want to send manual notification so that notification management requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-NOT-005 | FR-NOT-005 | Notification Management | System / Organization Admin | As System / Organization Admin, I want to schedule notification so that notification management requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-NOT-006 | FR-NOT-006 | Notification Management | System / Organization Admin | As System / Organization Admin, I want to deliver notification so that notification management requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-NOT-007 | FR-NOT-007 | Notification Management | System / Organization Admin | As System / Organization Admin, I want to retry failed notification so that notification management requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-NOT-008 | FR-NOT-008 | Notification Management | System / Organization Admin | As System / Organization Admin, I want to view notification history so that notification management requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-NOT-009 | FR-NOT-009 | Notification Management | System / Organization Admin | As System / Organization Admin, I want to track delivery status so that notification management requirements are delivered. | FE, BE, DB, API, QA | P2 | Backlog |
| US-NOT-010 | FR-NOT-010 | Notification Management | System / Organization Admin | As System / Organization Admin, I want to archive notification so that notification management requirements are delivered. | FE, BE, DB, API, QA | P2 | Backlog |
| US-NOT-011 | FR-NOT-011 | Notification Management | System / Organization Admin | As System / Organization Admin, I want to generate notification reports so that notification management requirements are delivered. | FE, BE, DB, API, QA | P2 | Backlog |
| US-NOT-012 | FR-NOT-012 | Notification Management | System / Organization Admin | As System / Organization Admin, I want to manage notification preferences so that notification management requirements are delivered. | FE, BE, DB, API, QA | P2 | Backlog |
| US-RPT-001 | FR-RPT-001 | Reports and Analytics | Admin / Manager | As Admin / Manager, I want to view operational dashboard so that reports and analytics requirements are delivered. | FE, BE, DB, API, QA | P0 | Backlog |
| US-RPT-002 | FR-RPT-002 | Reports and Analytics | Admin / Manager | As Admin / Manager, I want to generate membership report so that reports and analytics requirements are delivered. | FE, BE, DB, API, QA | P0 | Backlog |
| US-RPT-003 | FR-RPT-003 | Reports and Analytics | Admin / Manager | As Admin / Manager, I want to generate attendance report so that reports and analytics requirements are delivered. | FE, BE, DB, API, QA | P0 | Backlog |
| US-RPT-004 | FR-RPT-004 | Reports and Analytics | Admin / Manager | As Admin / Manager, I want to generate revenue report so that reports and analytics requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-RPT-005 | FR-RPT-005 | Reports and Analytics | Admin / Manager | As Admin / Manager, I want to generate customer report so that reports and analytics requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-RPT-006 | FR-RPT-006 | Reports and Analytics | Admin / Manager | As Admin / Manager, I want to generate trainer performance report so that reports and analytics requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-RPT-007 | FR-RPT-007 | Reports and Analytics | Admin / Manager | As Admin / Manager, I want to generate activity performance report so that reports and analytics requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-RPT-008 | FR-RPT-008 | Reports and Analytics | Admin / Manager | As Admin / Manager, I want to generate subscription report so that reports and analytics requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-RPT-009 | FR-RPT-009 | Reports and Analytics | Admin / Manager | As Admin / Manager, I want to export report so that reports and analytics requirements are delivered. | FE, BE, DB, API, QA | P2 | Backlog |
| US-RPT-010 | FR-RPT-010 | Reports and Analytics | Admin / Manager | As Admin / Manager, I want to schedule automated report so that reports and analytics requirements are delivered. | FE, BE, DB, API, QA | P2 | Backlog |
| US-RPT-011 | FR-RPT-011 | Reports and Analytics | Admin / Manager | As Admin / Manager, I want to monitor business kpis so that reports and analytics requirements are delivered. | FE, BE, DB, API, QA | P2 | Backlog |
| US-RPT-012 | FR-RPT-012 | Reports and Analytics | Admin / Manager | As Admin / Manager, I want to view historical trends so that reports and analytics requirements are delivered. | FE, BE, DB, API, QA | P2 | Backlog |
| US-TKT-001 | FR-TKT-001 | Support Ticket Management | User / Support Staff | As User / Support Staff, I want to create support ticket so that support ticket management requirements are delivered. | FE, BE, DB, API, QA | P0 | Backlog |
| US-TKT-002 | FR-TKT-002 | Support Ticket Management | User / Support Staff | As User / Support Staff, I want to classify ticket so that support ticket management requirements are delivered. | FE, BE, DB, API, QA | P0 | Backlog |
| US-TKT-003 | FR-TKT-003 | Support Ticket Management | User / Support Staff | As User / Support Staff, I want to assign ticket so that support ticket management requirements are delivered. | FE, BE, DB, API, QA | P0 | Backlog |
| US-TKT-004 | FR-TKT-004 | Support Ticket Management | User / Support Staff | As User / Support Staff, I want to set ticket priority so that support ticket management requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-TKT-005 | FR-TKT-005 | Support Ticket Management | User / Support Staff | As User / Support Staff, I want to accept ticket so that support ticket management requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-TKT-006 | FR-TKT-006 | Support Ticket Management | User / Support Staff | As User / Support Staff, I want to update ticket progress so that support ticket management requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-TKT-007 | FR-TKT-007 | Support Ticket Management | User / Support Staff | As User / Support Staff, I want to request additional information so that support ticket management requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-TKT-008 | FR-TKT-008 | Support Ticket Management | User / Support Staff | As User / Support Staff, I want to escalate ticket so that support ticket management requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-TKT-009 | FR-TKT-009 | Support Ticket Management | User / Support Staff | As User / Support Staff, I want to resolve ticket so that support ticket management requirements are delivered. | FE, BE, DB, API, QA | P2 | Backlog |
| US-TKT-010 | FR-TKT-010 | Support Ticket Management | User / Support Staff | As User / Support Staff, I want to close ticket so that support ticket management requirements are delivered. | FE, BE, DB, API, QA | P2 | Backlog |
| US-TKT-011 | FR-TKT-011 | Support Ticket Management | User / Support Staff | As User / Support Staff, I want to reopen ticket so that support ticket management requirements are delivered. | FE, BE, DB, API, QA | P2 | Backlog |
| US-TKT-012 | FR-TKT-012 | Support Ticket Management | User / Support Staff | As User / Support Staff, I want to generate support reports so that support ticket management requirements are delivered. | FE, BE, DB, API, QA | P2 | Backlog |
| US-AUD-001 | FR-AUD-001 | Audit and Compliance | System / Security | As System / Security, I want to capture business activity so that audit and compliance requirements are delivered. | FE, BE, DB, API, QA | P0 | Backlog |
| US-AUD-002 | FR-AUD-002 | Audit and Compliance | System / Security | As System / Security, I want to capture user login activity so that audit and compliance requirements are delivered. | FE, BE, DB, API, QA | P0 | Backlog |
| US-AUD-003 | FR-AUD-003 | Audit and Compliance | System / Security | As System / Security, I want to record business configuration changes so that audit and compliance requirements are delivered. | FE, BE, DB, API, QA | P0 | Backlog |
| US-AUD-004 | FR-AUD-004 | Audit and Compliance | System / Security | As System / Security, I want to monitor security events so that audit and compliance requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-AUD-005 | FR-AUD-005 | Audit and Compliance | System / Security | As System / Security, I want to review audit logs so that audit and compliance requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-AUD-006 | FR-AUD-006 | Audit and Compliance | System / Security | As System / Security, I want to investigate audit records so that audit and compliance requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-AUD-007 | FR-AUD-007 | Audit and Compliance | System / Security | As System / Security, I want to generate compliance report so that audit and compliance requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-AUD-008 | FR-AUD-008 | Audit and Compliance | System / Security | As System / Security, I want to archive audit records so that audit and compliance requirements are delivered. | FE, BE, DB, API, QA | P1 | Backlog |
| US-AUD-009 | FR-AUD-009 | Audit and Compliance | System / Security | As System / Security, I want to export audit history so that audit and compliance requirements are delivered. | FE, BE, DB, API, QA | P2 | Backlog |
| US-AUD-010 | FR-AUD-010 | Audit and Compliance | System / Security | As System / Security, I want to configure audit policies so that audit and compliance requirements are delivered. | FE, BE, DB, API, QA | P2 | Backlog |
| US-AUD-011 | FR-AUD-011 | Audit and Compliance | System / Security | As System / Security, I want to monitor compliance violations so that audit and compliance requirements are delivered. | FE, BE, DB, API, QA | P2 | Backlog |
| US-AUD-012 | FR-AUD-012 | Audit and Compliance | System / Security | As System / Security, I want to generate audit analytics so that audit and compliance requirements are delivered. | FE, BE, DB, API, QA | P2 | Backlog |

---

# 6. Technical Implementation Story Register

Technical stories exist where implementation work is required to make product stories buildable, testable, deployable, observable, or supportable.

| Story ID | Area | Actor | User Story | Acceptance Summary | Source | Status |
|---|---|---|---|---|---|---|
| US-FE-001 | Frontend | Frontend Engineer | As Frontend Engineer, I want to scaffold the Flutter monorepo application so that Digitize can be developed and released safely. | Flutter app builds for web, Android, and iOS with approved package structure. | DEV-01, DEV-03 | Backlog |
| US-FE-002 | Frontend | Frontend Engineer | As Frontend Engineer, I want to implement the responsive app shell and navigation so that Digitize can be developed and released safely. | Navigation reflects UX-05, permissions, tenant context, and route guards. | UX-05, DEV-03, DEV-13 | Backlog |
| US-FE-003 | Frontend | Frontend Engineer | As Frontend Engineer, I want to implement authentication and session handling in Flutter so that Digitize can be developed and released safely. | Login, logout, refresh, expiry, secure storage, and restricted states work consistently. | FR-06, API-03, DEV-03 | Backlog |
| US-FE-004 | Frontend | Frontend Engineer | As Frontend Engineer, I want to implement tenant context selection in Flutter so that Digitize can be developed and released safely. | Organization, Facility, and Site context is visible and attached to scoped API calls. | IC-03, BE-06, DEV-07 | Backlog |
| US-FE-005 | Frontend | Frontend Engineer | As Frontend Engineer, I want to build reusable form, table, filter, and detail components so that Digitize can be developed and released safely. | Common components cover loading, empty, error, validation, success, and restricted states. | UX-04, DEV-13 | Backlog |
| US-FE-006 | Frontend | Frontend Engineer | As Frontend Engineer, I want to implement the generated API client baseline so that Digitize can be developed and released safely. | Flutter client supports headers, auth, tenant context, errors, retries, and typed DTOs. | API-22, DEV-08, DEV-12 | Backlog |
| US-FE-007 | Frontend | Frontend Engineer | As Frontend Engineer, I want to support mock API and fixture mode so that Digitize can be developed and released safely. | Screens can develop against approved mock responses without backend availability. | API-25, DEV-08, DEV-12 | Backlog |
| US-FE-008 | Frontend | Frontend Engineer | As Frontend Engineer, I want to add Flutter widget and integration test coverage so that Digitize can be developed and released safely. | Critical screens and flows have widget/integration coverage before release. | TEST-05, TEST-06, DEV-10 | Backlog |
| US-FE-009 | Frontend | Frontend Engineer | As Frontend Engineer, I want to package Flutter web and mobile release builds so that Digitize can be developed and released safely. | Web, Android, and iOS builds follow deployment and release-readiness requirements. | DEP-07, RELM-05 | Backlog |
| US-BE-001 | Backend | Backend Engineer | As Backend Engineer, I want to scaffold the FastAPI modular monolith so that Digitize can be developed and released safely. | Application starts with approved module boundaries and health endpoint. | BE-01, BE-02, DEV-04 | Backlog |
| US-BE-002 | Backend | Backend Engineer | As Backend Engineer, I want to implement request context, request ID, and correlation ID so that Digitize can be developed and released safely. | Every request has traceable context and structured logs. | BE-08, IC-13 | Backlog |
| US-BE-003 | Backend | Backend Engineer | As Backend Engineer, I want to implement authentication and authorization foundations so that Digitize can be developed and released safely. | JWT validation, role checks, permission checks, and restricted responses are enforced server-side. | BE-05, API-23 | Backlog |
| US-BE-004 | Backend | Backend Engineer | As Backend Engineer, I want to implement tenant context enforcement so that Digitize can be developed and released safely. | Every scoped request validates Organization, Facility, and Site context. | BE-06, IC-03 | Backlog |
| US-BE-005 | Backend | Backend Engineer | As Backend Engineer, I want to implement domain service and repository patterns so that Digitize can be developed and released safely. | Business rules live outside routes and repositories stay persistence-focused. | BE-03, BE-04 | Backlog |
| US-BE-006 | Backend | Backend Engineer | As Backend Engineer, I want to implement API error handling and response standards so that Digitize can be developed and released safely. | Errors follow API-19 and do not leak internal details. | API-19, BE-08 | Backlog |
| US-BE-007 | Backend | Backend Engineer | As Backend Engineer, I want to implement outbox and background worker foundations so that Digitize can be developed and released safely. | Transactional events, retries, dead-letter states, and workers follow IC-09. | BE-09, IC-09 | Backlog |
| US-BE-008 | Backend | Backend Engineer | As Backend Engineer, I want to implement backend unit and API test foundation so that Digitize can be developed and released safely. | Use cases, tenant checks, authorization, and API contracts have automated tests. | BE-10, TEST-06 | Backlog |
| US-DB-001 | Database | Database Engineer | As Database Engineer, I want to create PostgreSQL schema and namespace baseline so that Digitize can be developed and released safely. | Schemas, extensions, naming, and ownership follow DB-00 and DB-03. | DB-00, DB-03 | Backlog |
| US-DB-002 | Database | Database Engineer | As Database Engineer, I want to create Alembic migration baseline so that Digitize can be developed and released safely. | Migrations are ordered, reversible where feasible, and deployable through DEP-05. | DB-12, DEP-05 | Backlog |
| US-DB-003 | Database | Database Engineer | As Database Engineer, I want to implement core platform tables so that Digitize can be developed and released safely. | Organization, Facility, Site, identity, tenant, and audit tables match DB-05 and DB-11. | DB-05, DB-11 | Backlog |
| US-DB-004 | Database | Database Engineer | As Database Engineer, I want to implement operational module tables so that Digitize can be developed and released safely. | Customer, membership, attendance, walk-in, trainer, PT, and batch tables match DB-06. | DB-06, DB-11 | Backlog |
| US-DB-005 | Database | Database Engineer | As Database Engineer, I want to implement commercial module tables so that Digitize can be developed and released safely. | Billing, payment, subscription, and license tables match DB-07. | DB-07, DB-11 | Backlog |
| US-DB-006 | Database | Database Engineer | As Database Engineer, I want to implement communication, reporting, audit, and outbox tables so that Digitize can be developed and released safely. | Notification, campaign, report, support, audit, inbox, and outbox persistence matches DB-08 and DB-22. | DB-08, DB-22 | Backlog |
| US-DB-007 | Database | Database Engineer | As Database Engineer, I want to add tenant isolation constraints and indexes so that Digitize can be developed and released safely. | Queries and constraints support tenant isolation, performance, and safe reporting. | DB-04, DB-13 | Backlog |
| US-DB-008 | Database | Database Engineer | As Database Engineer, I want to prepare seed and reference data so that Digitize can be developed and released safely. | Approved master/reference data is seedable for local, test, and demo environments. | DB-10, DEV-12 | Backlog |
| US-QA-001 | Testing | QA Engineer | As QA Engineer, I want to create the release test plan and traceability baseline so that Digitize can be developed and released safely. | Stories map to test cases, evidence, defects, and release readiness. | TEST-01, TEST-04, DEV-16 | Backlog |
| US-QA-002 | Testing | QA Engineer | As QA Engineer, I want to create functional regression coverage for product stories so that Digitize can be developed and released safely. | Core product stories have positive, negative, tenant, permission, and lifecycle tests. | TEST-05 | Backlog |
| US-QA-003 | Testing | QA Engineer | As QA Engineer, I want to create API contract and Postman coverage so that Digitize can be developed and released safely. | API tests validate approved requests, responses, headers, errors, and auth behavior. | TEST-06, API_Test_Cases, Postman_Collection | Backlog |
| US-QA-004 | Testing | QA Engineer | As QA Engineer, I want to create integration and outbox testing coverage so that Digitize can be developed and released safely. | Provider, webhook, retry, idempotency, and dead-letter behavior is verified. | TEST-07, IC-14 | Backlog |
| US-QA-005 | Testing | QA Engineer | As QA Engineer, I want to create performance and security baseline tests so that Digitize can be developed and released safely. | Critical journeys have load, authorization, tenant isolation, and OWASP-aligned coverage. | TEST-08, TEST-09 | Backlog |
| US-DEP-001 | Deployment | DevOps Engineer | As DevOps Engineer, I want to create local Docker Compose runtime so that Digitize can be developed and released safely. | Local PostgreSQL, Redis, backend, worker, and Flutter web dependencies are reproducible. | DEV-02, DEP-01 | Backlog |
| US-DEP-002 | Deployment | DevOps Engineer | As DevOps Engineer, I want to create CI pipeline baseline so that Digitize can be developed and released safely. | Lint, test, build, migration check, and artifact retention run in CI. | DEP-03, DR-012 | Backlog |
| US-DEP-003 | Deployment | DevOps Engineer | As DevOps Engineer, I want to create AWS environment baseline so that Digitize can be developed and released safely. | Environment strategy, compute, storage, networking, and secrets align to AWS decision record. | DEP-01, DEP-02, DR-016 | Backlog |
| US-DEP-004 | Deployment | DevOps Engineer | As DevOps Engineer, I want to implement configuration and secrets deployment so that Digitize can be developed and released safely. | Configuration is environment-specific and secrets are not stored in code. | DEP-04, DR-011 | Backlog |
| US-DEP-005 | Deployment | DevOps Engineer | As DevOps Engineer, I want to implement database migration deployment path so that Digitize can be developed and released safely. | Migrations are gated, observable, and rollback-aware. | DEP-05, DB-12 | Backlog |
| US-DEP-006 | Deployment | DevOps Engineer | As DevOps Engineer, I want to implement backend and worker deployment runbooks so that Digitize can be developed and released safely. | FastAPI and Celery deployments have startup, health, rollback, and handover steps. | DEP-06, BE-11 | Backlog |
| US-DEP-007 | Deployment | DevOps Engineer | As DevOps Engineer, I want to implement frontend web and mobile deployment path so that Digitize can be developed and released safely. | Flutter web/mobile release artifacts follow approved DEP-07 controls. | DEP-07, DEV-03 | Backlog |
| US-DEP-008 | Deployment | DevOps Engineer | As DevOps Engineer, I want to implement observability and rollback readiness so that Digitize can be developed and released safely. | Metrics, logs, traces, alerts, rollback, and recovery are release ready. | DEP-08, DEP-09 | Backlog |
| US-REL-001 | Release Management | Release Manager | As Release Manager, I want to manage release scope and candidate governance so that Digitize can be developed and released safely. | Release candidates have scope, version, evidence, and Go/No-Go inputs. | RELM-04, RELM-05, RELM-06 | Backlog |
| US-OPS-001 | Operations | Operations Engineer | As Operations Engineer, I want to prepare production operations handover so that Digitize can be developed and released safely. | Runbooks, alerts, access, incidents, backup/restore, and support handover are ready. | OPS-05, OPS-11 | Backlog |

---

# 7. Build Coverage Legend

| Coverage | Meaning |
|---|---|
| FE | Flutter screen, route, widget, state, validation, API client, and responsive behavior |
| BE | FastAPI route, schema, application service, domain rule, repository, auth, tenant context, logging |
| DB | PostgreSQL table, index, constraint, migration, seed/reference data, retention, audit impact |
| API | Approved REST endpoint, request/response schema, error behavior, headers, idempotency where required |
| QA | Unit, API, contract, integration, widget, regression, security, tenant, and release tests |
| DEP | CI/CD, environment config, secrets, migration deployment, release artifacts, rollback, observability |

---

# 8. Governance

- DEV-18 is the complete story catalog while no external agile tool is used.
- DEV-15 remains the module-level story map and may summarize or prioritize subsets of this catalog.
- DEV-06 remains the detailed acceptance-criteria document for sprint-ready stories, starting with the first vertical slice.
- DEV-09 and future sprint documents shall select stories from DEV-18.
- DEV-16 shall trace selected stories to FR, API, DB, UI, backend, testing, and release readiness.
- Product stories shall not be marked Ready until acceptance criteria are reviewed against the source FR.
- Technical stories shall not be marked Done until the implementation is verified by code review and applicable tests.
- If an agile tool is introduced later, DEV-18 story IDs shall be preserved and mapped to the tool.

---

# 9. Summary

The current documentation baseline produces 237 product stories and 40 technical implementation stories, for a total of 277 tracked stories before development starts.

This gives Digitize a complete starting backlog without depending on Jira, Azure DevOps, or another agile tool.
