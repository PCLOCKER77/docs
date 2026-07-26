# (status banner removed to preserve metadata `Status: Design Draft`)
# API-17 API Traceability Matrix

**Document ID:** API-17  
**Document Name:** API Traceability Matrix  
**Company:** OreeOn Technologies Pvt. Ltd.  
**Product:** Digitize  
**Document Type:** API Collection Documentation  
**Backend Technology:** FastAPI  
**Database Engine:** PostgreSQL  
**Authentication:** JWT  
**API Version:** v1  
**Document Version:** 0.1  
**Status:** Design Draft  
**Owner:** API Architecture  
**Reviewer:** Solution Architecture / Business Analysis / Security Architecture / Backend Engineering / QA  
**Dependencies:** API-00 to API-26, BA-01 to BA-10, FR-01 to FR-21, DB-00 to DB-22  
**Last Updated:** 2026-07-26

---

# 1. Document Metadata

| Attribute | Value |
|---|---|
| Document ID | API-17 |
| Document Name | API Traceability Matrix |
| Output File | API-17_API_Traceability_Matrix.md |
| API Version | v1 |
| Document Version | 0.1 |
| Status | Design Draft |
| Governing Standard | API-00_API_Collection_Standards.md |

---

# 2. Purpose

This document defines the Digitize API traceability matrix standard and baseline matrix structure.

It maps API endpoints and governance documents to functional requirements, business processes, UI screens, database tables, security controls, audit events, domain events, notifications, tests, owners, status, and release change records.

---

# 3. Scope

In scope:

- Endpoint traceability for API-01 through API-14.
- Governance traceability for API-15 through API-26 and API support artifacts.
- Mapping rules for FR, BA, DB, UI, security, event, audit, notification, test, owner, and release references.
- Traceability status definitions and review workflow.
- Matrix templates and initial baseline rows.

Out of scope:

- Changing source FR or BA documents.
- Creating UI screen IDs where source UI artifacts do not define them.
- Generating OpenAPI schemas.
- Runtime telemetry implementation.

---

# 4. Traceability Principles

| Principle | Standard |
|---|---|
| Source-backed | Mappings shall come from approved source documents |
| No invention | Unknown mappings shall use `TBD — Owner: Business Analysis; Action: populate missing rows with BA/FR/API/DB/event/test IDs referencing authoritative artifacts.` |
| Bidirectional | Requirements shall map to endpoints and endpoints shall map back to requirements |
| Reviewable | Every row shall have owner, status, and review state |
| Testable | Every endpoint shall map to at least one test scenario |
| Auditable | Sensitive and lifecycle endpoints shall map to audit controls |
| Release-aware | API changes shall map to API-20 change records |

---

# 5. Traceability Status Definitions

| Status | Meaning |
|---|---|
| Draft | Initial mapping created |
| Source Pending | Source artifact or source identifier is unavailable |
| Review Pending | Mapping requires architecture or BA review |
| Verified | Mapping was checked against source artifacts |
| Changed | Mapping changed after initial review |
| Deprecated | Endpoint or mapping is deprecated |
| Retired | Endpoint or mapping is retired |

---

# 6. Required Matrix Columns

| Column | Required | Description |
|---|---|---|
| Endpoint ID | Yes | API document endpoint identifier |
| API Document | Yes | API-01 to API-26 or support artifact source document |
| Method | Conditional | HTTP method for endpoint rows |
| URL | Conditional | API URL for endpoint rows |
| Endpoint Name | Yes | Business endpoint name |
| API Classification | Yes | Public, Authentication, Tenant, Platform, Internal, Integration, Webhook |
| Data Classification | Yes | Public, Internal, Confidential, Restricted, Financial, Security, Audit |
| FR Mapping | Conditional | Functional requirement IDs |
| BA Requirement | Conditional | Business requirement or BA-08 reference |
| Business Process | Conditional | BA-03 process reference |
| Business Process Flow | Conditional | BA-04 flow reference |
| UI Screen | Conditional | UI screen ID or name |
| Database Mapping | Yes | Approved DB tables or [OWNER ACTION REQUIRED — provide DB table mapping or 'Not Applicable'; CHG API-CHG-0021] |
| Audit Event | Conditional | Audit event codes |
| Domain Event | Conditional | Domain event names |
| Notification | Conditional | Notification events or templates |
| Security Control | Yes | AuthN, AuthZ, tenant isolation, masking, etc. |
| Test Scenario | Yes | API-16 scenario IDs or module tests |
| Owner | Yes | API/domain owner |
| Status | Yes | Traceability status |
| Change Reference | Conditional | API-20 change ID |

---

# 7. Endpoint Matrix Template

| Endpoint ID | API Document | Method | URL | Endpoint Name | FR Mapping | DB Mapping | Audit Event | Domain Event | Test Scenario | Owner | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|
| API-XX-001 | API-XX | POST | `/api/v1/example` | Example Action | FR-XXX-001 | `schema.table` | EXAMPLE_ACTION | example.action | API-16-CONTRACT, Module test | API Architecture | Draft |

---

# 8. Governance Matrix Template

| Governance ID | API Document | Governance Area | Source Mapping | Output Mapping | Test Scenario | Owner | Status |
|---|---|---|---|---|---|---|---|
| GOV-API-15-001 | API-15 | Environment Variables | API-00, API-16 | CI variables and collection env | API-16 environment validation | DevOps / QA | Draft |

---

# 9. Baseline Domain Coverage

| API Document | Domain Area | Source FR Coverage | Primary DB Mapping | Required Test Coverage |
|---|---|---|---|---|
| API-01 | Platform Administration | FR-02 | `platform.*` | Platform config, feature flags, maintenance |
| API-02 | Organization, Facility, Site | FR-03, FR-04, FR-05 | `tenant.*` | Hierarchy, lifecycle, tenant isolation |
| API-03 | Identity, User, Role | FR-06 | `identity.*`, `security.*` | AuthN, RBAC, sessions |
| API-04 | Customer Management | FR-07 | `customer.*` | PII, lifecycle, search |
| API-05 | Membership Management | FR-08 | `membership.*` | Lifecycle, payment reference, concurrency |
| API-06 | Attendance and Walk-in | FR-09, FR-10 | `operations.*` | Eligibility, capacity, walk-in |
| API-07 | Trainer, Activity, Batch | FR-11, FR-12, FR-13 | `training.*` | Schedule, capacity, sessions |
| API-08 | Billing and Payment | FR-14 | `commercial.invoice`, `commercial.payment`, `commercial.refund` | Financial state, payment safety |
| API-09 | Subscription and License | FR-15, FR-16 | `commercial.subscription`, `commercial.license`, `commercial.entitlement` | Commercial access and entitlements |
| API-10 | Notification and Campaign | FR-17, FR-18 | `communication.*` | Consent, delivery, retry |
| API-11 | Reports and Analytics | FR-19 | `reporting.*` | Reports, exports, async |
| API-12 | Support Ticket | FR-20 | `support.*` | Ticket lifecycle and SLA |
| API-13 | Audit and Security | FR-21 | `audit.*`, `security.*` | Audit immutability and export |
 `tenant.facility_type` | Lookup correctness and caching |, `tenant.facility_type` | Lookup correctness and caching |

---

# 10. Governance Coverage

| API Document | Governance Area | Downstream Consumers |
|---|---|---|
| API-15 | Environment and Variables | QA, DevOps, Backend, Release |
| API-16 | API Test Scenarios | QA, CI/CD, Backend, Security |
| API-17 | Traceability Matrix | Product, BA, Architecture, QA, Release |
| API-18 | Webhook Specifications | Backend, Integration, Security, DevOps |
| API-19 | Error Code Catalog | Backend, QA, Support, Localization |
| API-20 | API Change Log | Release, Product, Architecture, Support |
| API-21 | OpenAPI Specification Governance | Backend, API Architecture, QA, DevOps |
| API-22 | Frontend API Consumption Standards | Frontend, UI/UX, QA, Product |
| API-23 | API Access Control Matrix | Security, Frontend, UI/UX, QA |
| API-24 | API State and Workflow Contract | Product, UI/UX, Frontend, Backend, QA |
| API-25 | API Mocking and Sandbox Strategy | Frontend, QA, DevOps, Implementation |
| API-26 | API Release and Consumer Readiness Checklist | Release, Product, Frontend, QA, Support |

---

# 11. Functional Requirement Mapping Rules

- Use exact FR IDs from FR-02 through FR-21.
- Use FR ranges only when the endpoint collection covers a whole module and endpoint-level mappings are listed elsewhere in the same API document.
- If a module has generated placeholder FR IDs that require review, keep the ID and mark row status as `Review Pending`.
 use [CTO ACTION REQUIRED — confirm or replace TBD mappings], use [CTO ACTION REQUIRED — confirm or replace TBD mappings].
- Do not create new FR IDs in API documents.

---

# 12. Business Process Mapping Rules

| Source | Usage |
|---|---|
| BA-03 | Business process catalogue mappings |
| BA-04 | Business process flow mappings |
| BA-06 | User journey alignment |
| BA-08 | Requirement traceability references |

When a specific process ID is unavailable, the row shall reference the source document and mark the mapping as `Source Pending`.

---

# 13. UI Mapping Rules

- Use UI screen IDs when available.
- If UI screen IDs are unavailable, use approved screen names from API module documents.
- API screen mappings shall not define new UI navigation or wireframes.
- Missing UI mapping shall not block API Design Draft status, but shall block Frozen status unless formally waived.

---

# 14. Database Mapping Rules

| Mapping Type | Rule |
|---|---|
| Primary table | Required for endpoint rows |
| Secondary table | Required when endpoint changes related records |
| Audit table | Required for audited actions |
| Outbox table | Use `integration.outbox_event` from `DB-11_Database_DDL_DML_Scripts.md` |
| Reporting projection | Required for report/dashboard endpoints |
| Reference table | Required for lookup endpoints |

Database mappings shall use approved schema-qualified names from DB-11 where available.

---

# 15. Audit and Event Mapping Rules

Sensitive, lifecycle, commercial, security, export, administrative, and restricted read endpoints shall map to audit events.

Domain event mapping is required where the action triggers:

- Notification delivery.
- Reporting projection refresh.
- Webhook publication.
- Integration processing.
- Support or audit downstream workflows.
- Async job execution.

---

# 16. Security Control Mapping

| Control | Applies To |
|---|---|
| JWT authentication | Authenticated APIs |
| Provider signature validation | Webhook callbacks |
| Platform authorization | Platform admin APIs |
| Tenant isolation | Tenant APIs |
| Facility/Site hierarchy validation | Facility and Site APIs |
| Data masking | PII, financial, audit, security, support notes |
| Idempotency | Create, lifecycle, payment, retry-prone actions |
| Optimistic concurrency | Mutable protected resources |
| Rate limiting | Auth, search, payment, report, webhook, retry |
| Audit logging | Sensitive, lifecycle, financial, security, export |

---

# 17. Test Mapping Rules

Each endpoint row shall map to:

- At least one positive path test.
- At least one authorization test.
- At least one tenant isolation test for tenant APIs.
- Validation tests for body/query/path input.
- Idempotency tests where `Idempotency-Key` is required.
- Concurrency tests where `If-Match` is required.
- Audit/event tests where applicable.
- Async tests where response is `202 Accepted`.

---

# 18. Sample Endpoint Traceability Rows

| Endpoint ID | API Document | Method | URL | Endpoint Name | FR Mapping | DB Mapping | Audit Event | Domain Event | Test Scenario | Owner | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|
| API-05-001 | API-05 | POST | `/api/v1/memberships` | Create Membership | FR-MEM-001 | `membership.customer_membership`, `membership.membership_lifecycle_history` | MEMBERSHIP_CREATED | membership.created | API-16-IDEMP-001, API-16-TEN-001 | API Architecture | Draft |
| API-06-001 | API-06 | POST | `/api/v1/attendance/check-in` | Record Customer Check-in | FR-ATT-001 | `operations.attendance`, `operations.attendance_eligibility` | ATTENDANCE_CHECKED_IN | attendance.checked_in | API-16-LIFE-004, API-16-TEN-001 | API Architecture | Draft |
| API-08-009 | API-08 | POST | `/api/v1/payments/online` | Process Online Payment | FR-BPM-009 | `commercial.payment`, `commercial.payment_attempt` | ONLINE_PAYMENT_PROCESSED | payment.collected | API-16-IDEMP-001, API-16-SEC-003 | API Architecture | Draft |
| API-11-009 | API-11 | POST | `/api/v1/report-executions/{execution_id}/exports` | Export Report | FR-RPT-009 | `reporting.report_export`, `audit.data_export_record` | REPORT_EXPORT_REQUESTED | report.export_requested | API-16-ASYNC-005, API-16-SEC-005 | API Architecture | Draft |
| API-13-009 | API-13 | POST | `/api/v1/audit-events/export` | Export Audit History | FR-AUD-009 | `audit.audit_event`, `audit.data_export_record` | AUDIT_EXPORT_REQUESTED | audit.export_requested | API-16-SEC-005, API-16-AUD-003 | API Architecture | Draft |

---

# 19. Traceability Review Workflow

1. API Architecture creates or updates endpoint rows.
2. Business Analysis validates FR and BA mappings.
3. Data Architecture validates database mappings.
4. Security Architecture validates security controls and audit mappings.
5. QA validates test scenario coverage.
6. Release Owner validates API-20 change references.
7. Architecture Review marks row `Verified` or returns corrections.

---

# 20. Traceability Completeness Rules

| Document State | Required Completeness |
|---|---|
| Planned | Document registered only |
| Design Draft | Endpoint IDs, source FR where known, DB mapping summary, test category |
| Frozen — 2026-07-26 | Endpoint-level FR, DB, audit, event, and test rows reviewed |
| Frozen | No unresolved required mappings unless formally waived |
| Deprecated | Replacement endpoint and change reference required |
| Retired | Retirement change reference required |

---

# 21. Gap Register Template

| Gap ID | API Document | Missing Mapping | Impact | Owner | Target Resolution |
|---|---|---|---|---|---|
| API-TRC-GAP-001 | API-14 | FR mapping for common references | Cannot freeze endpoint rows | Business Analysis | Future BA/FR update |
| API-TRC-GAP-002 | API-01 to API-14 | UI screen IDs | Screen-level traceability pending | UI/UX | Future UI baseline |
| API-TRC-GAP-003 | API-01 to API-14 | Outbox table mapping | Resolved through `integration.outbox_event` in DB-11 | Data Architecture | Closed in current baseline |

---

# 22. Change Traceability

Every API-20 change record shall identify affected traceability rows.

| Change Type | Traceability Update Required |
|---|---|
| Added endpoint | New endpoint row |
| Modified endpoint | Existing row updated with change ID |
| Deprecated endpoint | Replacement mapping and deprecation status |
| Retired endpoint | Retirement status and release reference |
| Error code change | API-19 mapping update |
| Webhook change | API-18 event and delivery mapping update |
| Schema change | DB mapping and test scenario update |

---

# 23. Reporting and Metrics

Traceability reporting shall measure:

- Endpoint rows by API document.
- Rows with missing FR mapping.
- Rows with missing DB mapping.
- Rows with missing test mapping.
- Rows with missing audit mapping where required.
- Rows changed since last review.
- Rows blocked from Frozen status.

---

# 24. Governance Controls

- Traceability updates are required for endpoint additions, behavior changes, schema changes, error changes, webhook changes, and deprecations.
- Source mappings shall not be invented.
[MANDATE — entries flagged TBD must include owner and resolution path before Freeze; owners: add owner/resolution; CHG API-CHG-0021]
- QA shall not mark an endpoint test-complete until its traceability row maps to API-16 scenarios.

---

# 25. Document Acceptance Criteria

This document is acceptable when:

- Matrix columns are defined.
- Mapping rules are clear for FR, BA, UI, DB, security, audit, event, notification, test, and release references.
- Baseline coverage identifies every API document from API-01 to API-26 and the API support artifacts.
- Sample rows demonstrate endpoint-level traceability.
- Gap handling and review workflow are documented.

---

# 26. Summary

API-17 defines the traceability backbone for the Digitize API documentation set. It ensures every API contract can be traced to approved requirements, database design, security controls, tests, audit behavior, domain events, and release changes.
