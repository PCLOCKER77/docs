# (status banner removed to preserve metadata `Status: Design Draft`)
# API-12 Support Ticket Collection

**Document ID:** API-12  
**Document Name:** Support Ticket Collection  
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
**Reviewer:** Solution Architecture / Security Architecture / Backend Engineering  
**Dependencies:** API-00, API-03, API-04, API-10, API-13, FR-20, BA-03, BA-04, DB-11  
**Last Updated:** 2026-07-26

---

# 1. Document Metadata

| Attribute | Value |
|---|---|
| Document ID | API-12 |
| Document Name | Support Ticket Collection |
| Output File | API-12_Support_Ticket_Collection.md |
| API Version | v1 |
| Document Version | 0.1 |
| Status | Design Draft |
| Governing Standard | API-00_API_Collection_Standards.md |

---

# 2. Purpose

This document defines Support Ticket API contracts for ticket creation, classification, assignment, priority, acceptance, progress updates, additional information requests, escalation, resolution, closure, reopening, comments, attachments metadata, SLA tracking, search, history, and support reports.

---

# 3. Scope

In scope:

- Endpoint catalogue and REST contract rules for Support Ticket Collection.
- Tenant-aware authentication, authorization, validation, response, error, audit, event, and test expectations.
- Lifecycle, history, report, and operational controls listed in the endpoint catalogue.
- Database mapping, observability, assumptions, dependencies, and acceptance criteria.

Out of scope:

- FastAPI controller or service implementation.
- OpenAPI JSON/YAML and Postman JSON export.
- Physical database migration changes.
- Capabilities owned by other API collection documents except where explicitly referenced.

---

# 4. Business Context

Support APIs coordinate operational support while protecting sensitive comments, customer context, attachment metadata, SLA evidence, and tenant isolation.

---

# 5. Domain Overview

| Capability | Description | Source |
|---|---|---|
| Support Ticket | API contracts, validation, lifecycle, audit, events, and tests | FR-TKT-001 to FR-TKT-012 |

---

# 6. Actors and Access Model

| Actor | Access Model |
|---|---|
| Organization Administrator | Organization-scoped administration and oversight |
| Facility Manager | Facility-scoped operational access |
| Site Administrator | Site-scoped operational access where applicable |
| Staff User | Permission-controlled execution access |
| Support Executive | Restricted support visibility where approved |
| System | Scheduled, asynchronous, event, and audit processing |

---

# 7. API Classification

| Endpoint Group | API Classification | Data Classification |
|---|---|---|
| Create/update/lifecycle endpoints | Tenant / Facility / Site | Confidential |
| History/report/export endpoints | Tenant / Facility / Site | Restricted where sensitive |
| Reference/status endpoints | Tenant / Facility / Site | Confidential |
| Internal callbacks or processing endpoints | Internal / Integration | Restricted |

---

# 8. Resource Model

| Resource | URL Base | Approved Database Mapping |
|---|---|---|
| Primary Resources | `/api/v1/support` | `support.ticket_category` |
| History and Reports | `/api/v1/support/history` | `support.ticket_category` |

---

# 9. API Endpoint Catalogue

| Endpoint ID | Method | URL | Endpoint Name | FR Mapping |
|---|---|---|---|---|
| API-12-001 | POST | `/api/v1/support-tickets` | Create Support Ticket | FR-TKT-001 |
| API-12-002 | POST | `/api/v1/support-tickets/{ticket_id}/classify` | Classify Ticket | FR-TKT-002 |
| API-12-003 | POST | `/api/v1/support-tickets/{ticket_id}/assign` | Assign Ticket | FR-TKT-003 |
| API-12-004 | POST | `/api/v1/support-tickets/{ticket_id}/priority` | Set Ticket Priority | FR-TKT-004 |
| API-12-005 | POST | `/api/v1/support-tickets/{ticket_id}/accept` | Accept Ticket | FR-TKT-005 |
| API-12-006 | PATCH | `/api/v1/support-tickets/{ticket_id}/progress` | Update Ticket Progress | FR-TKT-006 |
| API-12-007 | POST | `/api/v1/support-tickets/{ticket_id}/information-requests` | Request Additional Information | FR-TKT-007 |
| API-12-008 | POST | `/api/v1/support-tickets/{ticket_id}/escalate` | Escalate Ticket | FR-TKT-008 |
| API-12-009 | POST | `/api/v1/support-tickets/{ticket_id}/resolve` | Resolve Ticket | FR-TKT-009 |
| API-12-010 | POST | `/api/v1/support-tickets/{ticket_id}/close` | Close Ticket | FR-TKT-010 |
| API-12-011 | POST | `/api/v1/support-tickets/{ticket_id}/reopen` | Reopen Ticket | FR-TKT-011 |
| API-12-012 | GET | `/api/v1/support-tickets/reports` | Generate Support Reports | FR-TKT-012 |

---

# 10. Common Authentication Requirements

All endpoints require JWT authentication unless explicitly classified as Public, Internal, Integration, or Webhook by API-00.

---

# 11. Common Authorization Requirements

Authorization shall validate Organization, Facility, Site where applicable, role, permission, object ownership, lifecycle status, subscription/license/feature access, and data classification before domain execution.

Approved permission families: support.create, support.update, support.view, support.lifecycle.manage, support.history.view, support.report.view.

---

# 12. Tenant and Resource Scope Rules

- `X-Organization-ID` is required for tenant-scoped operations.
- `X-Facility-ID` is required for Facility-scoped operations unless scope is established through the resource.
- `X-Site-ID` is required for Site-scoped operations where Site is part of the business context.
- Resource ownership shall be validated against the authenticated security context.
- Cross-tenant access may return 404 where resource disclosure is unsafe.

---

# 13. Common Header Requirements

| Header | Required | Purpose |
|---|---|---|
| Authorization | Yes | JWT authentication |
| Accept | Yes | `application/json` |
| Content-Type | Conditional | Request body |
| X-Correlation-ID | Required or generated | Traceability |
| X-Organization-ID | Yes | Tenant scope |
| X-Facility-ID | Conditional | Facility scope |
| X-Site-ID | Conditional | Site scope |
| If-Match | Required for protected updates/actions | Concurrency |
| Idempotency-Key | Required for create, lifecycle, commercial, and retry-prone actions | Retry safety |

---

# 14. Request and Data Format Rules

- JSON fields use snake_case.
- UUID values use canonical lowercase strings.
- Date-time values use UTC RFC 3339.
- Status, type, category, method, and channel fields shall use approved reference values.
- Sensitive payload fields shall be masked in logs and audit details.

---

# 15. Standard Response Usage

All endpoints use API-00 response envelopes. Create endpoints return `201 Created`. Lifecycle actions normally return `200 OK` with the resulting state. Long-running work returns `202 Accepted` with a trackable status reference.

---

# 16. Module Error Codes

| Error Code | HTTP Status | Category | Safe Message | Retryable |
|---|---|---|---|---|
| SUPPORT_AUTHORIZATION_001 | 403 | Authorization | User is not authorized for this support ticket collection action. | No |
| SUPPORT_VALIDATION_001 | 422 | Validation | Support Ticket Collection request validation failed. | No |
| SUPPORT_SCOPE_001 | 404 | Authorization | Requested resource is unavailable. | No |
| SUPPORT_LIFECYCLE_001 | 409 | Business | Requested lifecycle action is not allowed. | No |
| SUPPORT_CONCURRENCY_001 | 412 | Conflict | Resource changed before the request completed. | Yes |
| SUPPORT_IDEMPOTENCY_001 | 409 | Conflict | Idempotency key conflicts with a previous request. | No |

---

# 17. Pagination, Filtering, Sorting, and Search

Offset pagination applies to operational list endpoints. Cursor pagination applies to high-volume history, event, audit, delivery, execution, or export-result endpoints.

Approved filters: `status, organization_id, facility_id, site_id, customer_id, from_date, to_date, and module-specific identifiers`.

Approved sort fields: `created_at, updated_at, status, effective_at, and module-specific display codes`.

Search is permitted only on approved business identifiers, display names, reference numbers, and safe projected fields. Sensitive identifiers require explicit permission.

---

# 18. Rate Limiting and Caching

Rate limiting protects create, search, lifecycle, report/export, retry, callback, and sensitive read endpoints.

Reference and configuration responses may be cached with invalidation. Mutable state, financial data, security data, audit data, and customer-sensitive data shall not be cached unless explicit cache-control rules are approved.

---

# 19. Idempotency and Optimistic Concurrency

Idempotency is required for create operations, lifecycle actions, payment-sensitive actions, retry-prone asynchronous commands, and provider callback handling where duplicate submissions are possible.

Optimistic concurrency is required for mutable resources and lifecycle actions where lost updates are possible. Protected requests shall use `If-Match` according to API-00.

---

# 20. Transaction Boundaries and Asynchronous Operations

Each state-changing endpoint shall persist the primary domain change, lifecycle/history record, audit event, and outbox/domain event within a controlled transaction boundary.

Asynchronous processing may be used for notifications, exports, reports, webhook delivery, retries, projection refresh, provider callbacks, and long-running analytics. Asynchronous endpoints return `202 Accepted` with a status reference.

---

# 21. Bulk Operations and File Handling

Bulk operations are not approved unless listed in the endpoint catalogue or explicitly governed by API-00 bulk-operation rules.

File upload/download is not part of this document unless explicitly listed. Attachment or export metadata may be stored, but binary storage and signed URL behavior require approved file-handling design.

---

# 22. API Endpoints

Each endpoint inherits API-00 Common Endpoint Documentation Template.

| Endpoint ID | Business Purpose | AuthZ Permission | Success | DB Mapping | Audit Event | Domain Event | Tests |
|---|---|---|---|---|---|---|---|
| API-12-001 | Create Support Ticket | `create.support.ticket` | 201/200 with resulting state | `support.ticket_category, support.ticket_priority, support.support_ticket, support.ticket_assignment, support.ticket_comment, support.ticket_attachment, support.ticket_escalation, support.sla_tracking`, `audit.audit_event` | CREATE_SUPPORT_TICKET | create.support.ticket | Scope, validation, audit, and error-path tests |
| API-12-002 | Classify Ticket | `classify.ticket` | 201/200 with resulting state | `support.ticket_category, support.ticket_priority, support.support_ticket, support.ticket_assignment, support.ticket_comment, support.ticket_attachment, support.ticket_escalation, support.sla_tracking`, `audit.audit_event` | CLASSIFY_TICKET | classify.ticket | Scope, validation, audit, and error-path tests |
| API-12-003 | Assign Ticket | `assign.ticket` | 201/200 with resulting state | `support.ticket_category, support.ticket_priority, support.support_ticket, support.ticket_assignment, support.ticket_comment, support.ticket_attachment, support.ticket_escalation, support.sla_tracking`, `audit.audit_event` | ASSIGN_TICKET | assign.ticket | Scope, validation, audit, and error-path tests |
| API-12-004 | Set Ticket Priority | `set.ticket.priority` | 201/200 with resulting state | `support.ticket_category, support.ticket_priority, support.support_ticket, support.ticket_assignment, support.ticket_comment, support.ticket_attachment, support.ticket_escalation, support.sla_tracking`, `audit.audit_event` | SET_TICKET_PRIORITY | set.ticket.priority | Scope, validation, audit, and error-path tests |
| API-12-005 | Accept Ticket | `accept.ticket` | 201/200 with resulting state | `support.ticket_category, support.ticket_priority, support.support_ticket, support.ticket_assignment, support.ticket_comment, support.ticket_attachment, support.ticket_escalation, support.sla_tracking`, `audit.audit_event` | ACCEPT_TICKET | accept.ticket | Scope, validation, audit, and error-path tests |
| API-12-006 | Update Ticket Progress | `update.ticket.progress` | 201/200 with resulting state | `support.ticket_category, support.ticket_priority, support.support_ticket, support.ticket_assignment, support.ticket_comment, support.ticket_attachment, support.ticket_escalation, support.sla_tracking`, `audit.audit_event` | UPDATE_TICKET_PROGRESS | update.ticket.progress | Scope, validation, audit, and error-path tests |
| API-12-007 | Request Additional Information | `request.additional.information` | 201/200 with resulting state | `support.ticket_category, support.ticket_priority, support.support_ticket, support.ticket_assignment, support.ticket_comment, support.ticket_attachment, support.ticket_escalation, support.sla_tracking`, `audit.audit_event` | REQUEST_ADDITIONAL_INFORMATION | request.additional.information | Scope, validation, audit, and error-path tests |
| API-12-008 | Escalate Ticket | `escalate.ticket` | 201/200 with resulting state | `support.ticket_category, support.ticket_priority, support.support_ticket, support.ticket_assignment, support.ticket_comment, support.ticket_attachment, support.ticket_escalation, support.sla_tracking`, `audit.audit_event` | ESCALATE_TICKET | escalate.ticket | Scope, validation, audit, and error-path tests |
| API-12-009 | Resolve Ticket | `resolve.ticket` | 201/200 with resulting state | `support.ticket_category, support.ticket_priority, support.support_ticket, support.ticket_assignment, support.ticket_comment, support.ticket_attachment, support.ticket_escalation, support.sla_tracking`, `audit.audit_event` | RESOLVE_TICKET | resolve.ticket | Scope, validation, audit, and error-path tests |
| API-12-010 | Close Ticket | `close.ticket` | 201/200 with resulting state | `support.ticket_category, support.ticket_priority, support.support_ticket, support.ticket_assignment, support.ticket_comment, support.ticket_attachment, support.ticket_escalation, support.sla_tracking`, `audit.audit_event` | CLOSE_TICKET | close.ticket | Scope, validation, audit, and error-path tests |
| API-12-011 | Reopen Ticket | `reopen.ticket` | 201/200 with resulting state | `support.ticket_category, support.ticket_priority, support.support_ticket, support.ticket_assignment, support.ticket_comment, support.ticket_attachment, support.ticket_escalation, support.sla_tracking`, `audit.audit_event` | REOPEN_TICKET | reopen.ticket | Scope, validation, audit, and error-path tests |
| API-12-012 | Generate Support Reports | `generate.support.reports` | 200 OK | `support.ticket_category, support.ticket_priority, support.support_ticket, support.ticket_assignment, support.ticket_comment, support.ticket_attachment, support.ticket_escalation, support.sla_tracking`, `audit.audit_event` | GENERATE_SUPPORT_REPORTS | generate.support.reports | Scope, validation, audit, and error-path tests |

---

# 23. Module Sequence Diagram

```mermaid
sequenceDiagram
    participant Client
    participant API as Support Ticket API
    participant Auth as AuthN/AuthZ
    participant Service as Domain Service
    participant DB as PostgreSQL
    participant Audit
    Client->>API: Submit request
    API->>Auth: Validate JWT, permission, and scope
    Auth-->>API: Access decision
    API->>Service: Validate business rules and lifecycle
    Service->>DB: Persist state/history transaction
    Service->>Audit: Write audit evidence
    API-->>Client: Standard response envelope
```

---

# 24. Request Flow Diagram

```mermaid
flowchart TD
    A[API Request] --> B[Authenticate]
    B --> C[Authorize]
    C --> D[Validate Tenant and Resource Scope]
    D --> E[Validate Payload and Lifecycle]
    E --> F[Persist Domain Transaction]
    F --> G[Write Audit and Domain Event]
    G --> H[Return Standard Response]
```

---

# 25. Database Mapping Summary

| Area | Tables |
|---|---|
| Primary Domain | `support.ticket_category, support.ticket_priority, support.support_ticket, support.ticket_assignment, support.ticket_comment, support.ticket_attachment, support.ticket_escalation, support.sla_tracking` |
| Audit | `audit.audit_event`, `audit.audit_entity_reference` |

---

# 26. Domain Event and Outbox Mapping

Outbox mapping is `integration.outbox_event` from `DB-11_Database_DDL_DML_Scripts.md`.

Events include support_ticket.created, support_ticket.assigned, support_ticket.escalated, support_ticket.resolved, support_ticket.closed, support_ticket.reopened.

---

# 27. Audit and Notification Mapping

Audit events include SUPPORT_TICKET_CREATED, SUPPORT_TICKET_CLASSIFIED, SUPPORT_TICKET_ASSIGNED, SUPPORT_TICKET_ESCALATED, SUPPORT_TICKET_RESOLVED, SUPPORT_TICKET_CLOSED.

Asynchronous notifications may be triggered for customer-visible confirmations, operational alerts, approval requests, failures, lifecycle status changes, report/export completion, and compliance/security alerts where applicable.

---

# 28. Functional Requirement Mapping

| Source Document | Covered FR IDs |
|---|---|
| FR-20 Support Ticket | FR-TKT-001 to FR-TKT-012 |

---

# 29. Business Process and UI Mapping

| Process Area | Covered Processes |
|---|---|
| Business Process Catalog | BA-03 mappings referenced by the source FR documents |
| Business Process Flows | BA-04 mappings referenced by the source FR documents |

UI screen IDs are unavailable in the current source set. Mapped screen names shall follow the endpoint catalogue and corresponding Functional Requirement workflow names.

---

# 30. Security Considerations

- Enforce tenant, Facility, and Site isolation.
- Restrict sensitive data, financial data, security data, audit data, and customer personal data by permission and data classification.
- Prevent lifecycle bypass and unauthorized override usage.
- Mask secrets, tokens, provider references, and sensitive payload values in logs.
- Audit restricted reads, exports, lifecycle actions, configuration changes, and administrative access.

---

# 31. Performance, Scalability, and Observability

- Index list, lookup, history, status, and date-range access paths.
- Use cursor pagination for high-volume append-only histories.
- Avoid unbounded synchronous report, export, search, or aggregation queries.
- Track request count, latency, validation failures, authorization failures, scope failures, lifecycle conflicts, idempotency conflicts, concurrency conflicts, async job status, audit write failures, and domain event publication failures.

---

# 32. Test Coverage Summary

Required coverage includes authentication, authorization, tenant isolation, validation, success responses, error envelopes, pagination, filtering, sorting, idempotency, concurrency, lifecycle transitions, audit/event creation, notification behavior, and relevant async or export flows.

---

# 33. Assumptions and Constraints

- UI screen IDs are unavailable.
- Outbox table mapping is `integration.outbox_event`.
- Source mappings marked `TBD — Owner: Support / BA; Action: provide FR/event mappings for support ticket flows.` require future BA/FR/API review.
- These documents define contracts and governance only; they do not generate FastAPI source code.

---

# 34. Dependencies

| Dependency | Description |
|---|---|
| API-00 | Governing standard |
| API-02 | Organization, Facility, and Site hierarchy |
| API-03 | Authentication, user, role, and permission context |
| API-13 | Audit and security |
| DB-11 | Approved database mappings |

---

# 35. Future Enhancements

- Additional query projections after UI screen IDs are finalized.
- Dedicated export status endpoint where report volume requires asynchronous processing.
- Webhook publication where external integration use cases are approved.

---

# 36. Document Acceptance Criteria

This document is acceptable when it follows API-00, uses approved `/api/v1` REST conventions, preserves tenant isolation, maps endpoints to source requirements where available, defines module errors, and documents audit/event/test coverage.

---

# 37. Summary

API-12 defines Support Ticket Collection for Digitize. It establishes secure, tenant-aware, auditable API contracts aligned with approved functional, database, architecture, and governance source documents.
