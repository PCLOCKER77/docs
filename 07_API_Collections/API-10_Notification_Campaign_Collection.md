# (status banner removed to preserve metadata `Status: Design Draft`)
# API-10 Notification and Campaign Collection

**Document ID:** API-10  
**Document Name:** Notification and Campaign Collection  
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
**Dependencies:** API-00, API-04, API-13, API-18, FR-17, FR-18, BA-03, BA-04, DB-11  
**Last Updated:** 2026-07-26

---

# 1. Document Metadata

| Attribute | Value |
|---|---|
| Document ID | API-10 |
| Document Name | Notification and Campaign Collection |
| Output File | API-10_Notification_Campaign_Collection.md |
| API Version | v1 |
| Document Version | 0.1 |
| Status | Design Draft |
| Governing Standard | API-00_API_Collection_Standards.md |

---

# 2. Purpose

This document defines Notification and Campaign API contracts for campaigns, audiences, approvals, scheduling, launch, pause, completion, cancellation, templates, rules, system/manual/scheduled notifications, delivery, retry, history, status tracking, archive, reports, preferences, and consent-aware delivery.

---

# 3. Scope

In scope:

- Endpoint catalogue and REST contract rules for Notification and Campaign Collection.
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

Communication APIs must protect customer consent, support asynchronous delivery, preserve provider traceability, and avoid leaking sensitive content through logs or error messages.

---

# 5. Domain Overview

| Capability | Description | Source |
|---|---|---|
| Notification and Campaign | API contracts, validation, lifecycle, audit, events, and tests | FR-CMP-001 to FR-CMP-012, FR-NOT-001 to FR-NOT-012 |

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
| Primary Resources | `/api/v1/notification` | `communication.advertisement_campaign` |
| History and Reports | `/api/v1/notification/history` | `communication.advertisement_campaign` |

---

# 9. API Endpoint Catalogue

| Endpoint ID | Method | URL | Endpoint Name | FR Mapping |
|---|---|---|---|---|
| API-10-001 | POST | `/api/v1/campaigns` | Create Campaign | FR-CMP-001 |
| API-10-002 | PATCH | `/api/v1/campaigns/{campaign_id}/configuration` | Configure Campaign | FR-CMP-002 |
| API-10-003 | POST | `/api/v1/campaigns/{campaign_id}/audiences` | Select Target Audience | FR-CMP-003 |
| API-10-004 | POST | `/api/v1/campaigns/{campaign_id}/submit-for-approval` | Submit Campaign for Approval | FR-CMP-004 |
| API-10-005 | POST | `/api/v1/campaigns/{campaign_id}/approve` | Approve Campaign | FR-CMP-005 |
| API-10-006 | POST | `/api/v1/campaigns/{campaign_id}/schedule` | Schedule Campaign | FR-CMP-006 |
| API-10-007 | POST | `/api/v1/campaigns/{campaign_id}/launch` | Launch Campaign | FR-CMP-007 |
| API-10-008 | POST | `/api/v1/campaigns/{campaign_id}/pause` | Pause Campaign | FR-CMP-008 |
| API-10-009 | POST | `/api/v1/campaigns/{campaign_id}/complete` | Complete Campaign | FR-CMP-009 |
| API-10-010 | POST | `/api/v1/campaigns/{campaign_id}/cancel` | Cancel Campaign | FR-CMP-010 |
| API-10-011 | GET | `/api/v1/campaigns/{campaign_id}/performance` | Monitor Campaign Performance | FR-CMP-011 |
| API-10-012 | GET | `/api/v1/campaigns/{campaign_id}/reports` | Generate Campaign Report | FR-CMP-012 |
| API-10-013 | POST | `/api/v1/notification-templates` | Create Notification Template | FR-NOT-001 |
| API-10-014 | POST | `/api/v1/notification-rules` | Configure Notification Rules | FR-NOT-002 |
| API-10-015 | POST | `/api/v1/notifications/system` | Generate System Notification | FR-NOT-003 |
| API-10-016 | POST | `/api/v1/notifications/manual` | Send Manual Notification | FR-NOT-004 |
| API-10-017 | POST | `/api/v1/notifications/schedule` | Schedule Notification | FR-NOT-005 |
| API-10-018 | POST | `/api/v1/notifications/{notification_id}/deliver` | Deliver Notification | FR-NOT-006 |
| API-10-019 | POST | `/api/v1/notifications/{notification_id}/retry` | Retry Failed Notification | FR-NOT-007 |
| API-10-020 | GET | `/api/v1/notifications` | View Notification History | FR-NOT-008 |
| API-10-021 | GET | `/api/v1/notifications/{notification_id}/delivery-status` | Track Delivery Status | FR-NOT-009 |
| API-10-022 | POST | `/api/v1/notifications/{notification_id}/archive` | Archive Notification | FR-NOT-010 |
| API-10-023 | GET | `/api/v1/notifications/reports` | Generate Notification Reports | FR-NOT-011 |
| API-10-024 | PATCH | `/api/v1/notification-preferences/{preference_id}` | Manage Notification Preferences | FR-NOT-012 |

---

# 10. Common Authentication Requirements

All endpoints require JWT authentication unless explicitly classified as Public, Internal, Integration, or Webhook by API-00.

---

# 11. Common Authorization Requirements

Authorization shall validate Organization, Facility, Site where applicable, role, permission, object ownership, lifecycle status, subscription/license/feature access, and data classification before domain execution.

Approved permission families: notification.create, notification.update, notification.view, notification.lifecycle.manage, notification.history.view, notification.report.view.

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
| COMMUNICATION_AUTHORIZATION_001 | 403 | Authorization | User is not authorized for this notification and campaign collection action. | No |
| COMMUNICATION_VALIDATION_001 | 422 | Validation | Notification and Campaign Collection request validation failed. | No |
| COMMUNICATION_SCOPE_001 | 404 | Authorization | Requested resource is unavailable. | No |
| COMMUNICATION_LIFECYCLE_001 | 409 | Business | Requested lifecycle action is not allowed. | No |
| COMMUNICATION_CONCURRENCY_001 | 412 | Conflict | Resource changed before the request completed. | Yes |
| COMMUNICATION_IDEMPOTENCY_001 | 409 | Conflict | Idempotency key conflicts with a previous request. | No |

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
| API-10-001 | Create Campaign | `create.campaign` | 201/200 with resulting state | `communication.advertisement_campaign, communication.campaign_audience, communication.campaign_schedule, communication.campaign_delivery, communication.campaign_result, communication.notification_template, communication.notification, communication.notification_delivery, communication.notification_attempt, communication.notification_preference`, `audit.audit_event` | CREATE_CAMPAIGN | create.campaign | Scope, validation, audit, and error-path tests |
| API-10-002 | Configure Campaign | `configure.campaign` | 201/200 with resulting state | `communication.advertisement_campaign, communication.campaign_audience, communication.campaign_schedule, communication.campaign_delivery, communication.campaign_result, communication.notification_template, communication.notification, communication.notification_delivery, communication.notification_attempt, communication.notification_preference`, `audit.audit_event` | CONFIGURE_CAMPAIGN | configure.campaign | Scope, validation, audit, and error-path tests |
| API-10-003 | Select Target Audience | `select.target.audience` | 201/200 with resulting state | `communication.advertisement_campaign, communication.campaign_audience, communication.campaign_schedule, communication.campaign_delivery, communication.campaign_result, communication.notification_template, communication.notification, communication.notification_delivery, communication.notification_attempt, communication.notification_preference`, `audit.audit_event` | SELECT_TARGET_AUDIENCE | select.target.audience | Scope, validation, audit, and error-path tests |
| API-10-004 | Submit Campaign for Approval | `submit.campaign.for.approval` | 201/200 with resulting state | `communication.advertisement_campaign, communication.campaign_audience, communication.campaign_schedule, communication.campaign_delivery, communication.campaign_result, communication.notification_template, communication.notification, communication.notification_delivery, communication.notification_attempt, communication.notification_preference`, `audit.audit_event` | SUBMIT_CAMPAIGN_FOR_APPROVAL | submit.campaign.for.approval | Scope, validation, audit, and error-path tests |
| API-10-005 | Approve Campaign | `approve.campaign` | 201/200 with resulting state | `communication.advertisement_campaign, communication.campaign_audience, communication.campaign_schedule, communication.campaign_delivery, communication.campaign_result, communication.notification_template, communication.notification, communication.notification_delivery, communication.notification_attempt, communication.notification_preference`, `audit.audit_event` | APPROVE_CAMPAIGN | approve.campaign | Scope, validation, audit, and error-path tests |
| API-10-006 | Schedule Campaign | `schedule.campaign` | 201/200 with resulting state | `communication.advertisement_campaign, communication.campaign_audience, communication.campaign_schedule, communication.campaign_delivery, communication.campaign_result, communication.notification_template, communication.notification, communication.notification_delivery, communication.notification_attempt, communication.notification_preference`, `audit.audit_event` | SCHEDULE_CAMPAIGN | schedule.campaign | Scope, validation, audit, and error-path tests |
| API-10-007 | Launch Campaign | `launch.campaign` | 201/200 with resulting state | `communication.advertisement_campaign, communication.campaign_audience, communication.campaign_schedule, communication.campaign_delivery, communication.campaign_result, communication.notification_template, communication.notification, communication.notification_delivery, communication.notification_attempt, communication.notification_preference`, `audit.audit_event` | LAUNCH_CAMPAIGN | launch.campaign | Scope, validation, audit, and error-path tests |
| API-10-008 | Pause Campaign | `pause.campaign` | 201/200 with resulting state | `communication.advertisement_campaign, communication.campaign_audience, communication.campaign_schedule, communication.campaign_delivery, communication.campaign_result, communication.notification_template, communication.notification, communication.notification_delivery, communication.notification_attempt, communication.notification_preference`, `audit.audit_event` | PAUSE_CAMPAIGN | pause.campaign | Scope, validation, audit, and error-path tests |
| API-10-009 | Complete Campaign | `complete.campaign` | 201/200 with resulting state | `communication.advertisement_campaign, communication.campaign_audience, communication.campaign_schedule, communication.campaign_delivery, communication.campaign_result, communication.notification_template, communication.notification, communication.notification_delivery, communication.notification_attempt, communication.notification_preference`, `audit.audit_event` | COMPLETE_CAMPAIGN | complete.campaign | Scope, validation, audit, and error-path tests |
| API-10-010 | Cancel Campaign | `cancel.campaign` | 201/200 with resulting state | `communication.advertisement_campaign, communication.campaign_audience, communication.campaign_schedule, communication.campaign_delivery, communication.campaign_result, communication.notification_template, communication.notification, communication.notification_delivery, communication.notification_attempt, communication.notification_preference`, `audit.audit_event` | CANCEL_CAMPAIGN | cancel.campaign | Scope, validation, audit, and error-path tests |
| API-10-011 | Monitor Campaign Performance | `monitor.campaign.performance` | 200 OK | `communication.advertisement_campaign, communication.campaign_audience, communication.campaign_schedule, communication.campaign_delivery, communication.campaign_result, communication.notification_template, communication.notification, communication.notification_delivery, communication.notification_attempt, communication.notification_preference`, `audit.audit_event` | MONITOR_CAMPAIGN_PERFORMANCE | monitor.campaign.performance | Scope, validation, audit, and error-path tests |
| API-10-012 | Generate Campaign Report | `generate.campaign.report` | 200 OK | `communication.advertisement_campaign, communication.campaign_audience, communication.campaign_schedule, communication.campaign_delivery, communication.campaign_result, communication.notification_template, communication.notification, communication.notification_delivery, communication.notification_attempt, communication.notification_preference`, `audit.audit_event` | GENERATE_CAMPAIGN_REPORT | generate.campaign.report | Scope, validation, audit, and error-path tests |
| API-10-013 | Create Notification Template | `create.notification.template` | 201/200 with resulting state | `communication.advertisement_campaign, communication.campaign_audience, communication.campaign_schedule, communication.campaign_delivery, communication.campaign_result, communication.notification_template, communication.notification, communication.notification_delivery, communication.notification_attempt, communication.notification_preference`, `audit.audit_event` | CREATE_NOTIFICATION_TEMPLATE | create.notification.template | Scope, validation, audit, and error-path tests |
| API-10-014 | Configure Notification Rules | `configure.notification.rules` | 201/200 with resulting state | `communication.advertisement_campaign, communication.campaign_audience, communication.campaign_schedule, communication.campaign_delivery, communication.campaign_result, communication.notification_template, communication.notification, communication.notification_delivery, communication.notification_attempt, communication.notification_preference`, `audit.audit_event` | CONFIGURE_NOTIFICATION_RULES | configure.notification.rules | Scope, validation, audit, and error-path tests |
| API-10-015 | Generate System Notification | `generate.system.notification` | 201/200 with resulting state | `communication.advertisement_campaign, communication.campaign_audience, communication.campaign_schedule, communication.campaign_delivery, communication.campaign_result, communication.notification_template, communication.notification, communication.notification_delivery, communication.notification_attempt, communication.notification_preference`, `audit.audit_event` | GENERATE_SYSTEM_NOTIFICATION | generate.system.notification | Scope, validation, audit, and error-path tests |
| API-10-016 | Send Manual Notification | `send.manual.notification` | 201/200 with resulting state | `communication.advertisement_campaign, communication.campaign_audience, communication.campaign_schedule, communication.campaign_delivery, communication.campaign_result, communication.notification_template, communication.notification, communication.notification_delivery, communication.notification_attempt, communication.notification_preference`, `audit.audit_event` | SEND_MANUAL_NOTIFICATION | send.manual.notification | Scope, validation, audit, and error-path tests |
| API-10-017 | Schedule Notification | `schedule.notification` | 201/200 with resulting state | `communication.advertisement_campaign, communication.campaign_audience, communication.campaign_schedule, communication.campaign_delivery, communication.campaign_result, communication.notification_template, communication.notification, communication.notification_delivery, communication.notification_attempt, communication.notification_preference`, `audit.audit_event` | SCHEDULE_NOTIFICATION | schedule.notification | Scope, validation, audit, and error-path tests |
| API-10-018 | Deliver Notification | `deliver.notification` | 201/200 with resulting state | `communication.advertisement_campaign, communication.campaign_audience, communication.campaign_schedule, communication.campaign_delivery, communication.campaign_result, communication.notification_template, communication.notification, communication.notification_delivery, communication.notification_attempt, communication.notification_preference`, `audit.audit_event` | DELIVER_NOTIFICATION | deliver.notification | Scope, validation, audit, and error-path tests |
| API-10-019 | Retry Failed Notification | `retry.failed.notification` | 201/200 with resulting state | `communication.advertisement_campaign, communication.campaign_audience, communication.campaign_schedule, communication.campaign_delivery, communication.campaign_result, communication.notification_template, communication.notification, communication.notification_delivery, communication.notification_attempt, communication.notification_preference`, `audit.audit_event` | RETRY_FAILED_NOTIFICATION | retry.failed.notification | Scope, validation, audit, and error-path tests |
| API-10-020 | View Notification History | `view.notification.history` | 200 OK | `communication.advertisement_campaign, communication.campaign_audience, communication.campaign_schedule, communication.campaign_delivery, communication.campaign_result, communication.notification_template, communication.notification, communication.notification_delivery, communication.notification_attempt, communication.notification_preference`, `audit.audit_event` | VIEW_NOTIFICATION_HISTORY | view.notification.history | Scope, validation, audit, and error-path tests |
| API-10-021 | Track Delivery Status | `track.delivery.status` | 200 OK | `communication.advertisement_campaign, communication.campaign_audience, communication.campaign_schedule, communication.campaign_delivery, communication.campaign_result, communication.notification_template, communication.notification, communication.notification_delivery, communication.notification_attempt, communication.notification_preference`, `audit.audit_event` | TRACK_DELIVERY_STATUS | track.delivery.status | Scope, validation, audit, and error-path tests |
| API-10-022 | Archive Notification | `archive.notification` | 201/200 with resulting state | `communication.advertisement_campaign, communication.campaign_audience, communication.campaign_schedule, communication.campaign_delivery, communication.campaign_result, communication.notification_template, communication.notification, communication.notification_delivery, communication.notification_attempt, communication.notification_preference`, `audit.audit_event` | ARCHIVE_NOTIFICATION | archive.notification | Scope, validation, audit, and error-path tests |
| API-10-023 | Generate Notification Reports | `generate.notification.reports` | 200 OK | `communication.advertisement_campaign, communication.campaign_audience, communication.campaign_schedule, communication.campaign_delivery, communication.campaign_result, communication.notification_template, communication.notification, communication.notification_delivery, communication.notification_attempt, communication.notification_preference`, `audit.audit_event` | GENERATE_NOTIFICATION_REPORTS | generate.notification.reports | Scope, validation, audit, and error-path tests |
| API-10-024 | Manage Notification Preferences | `manage.notification.preferences` | 201/200 with resulting state | `communication.advertisement_campaign, communication.campaign_audience, communication.campaign_schedule, communication.campaign_delivery, communication.campaign_result, communication.notification_template, communication.notification, communication.notification_delivery, communication.notification_attempt, communication.notification_preference`, `audit.audit_event` | MANAGE_NOTIFICATION_PREFERENCES | manage.notification.preferences | Scope, validation, audit, and error-path tests |

---

# 23. Module Sequence Diagram

```mermaid
sequenceDiagram
    participant Client
    participant API as Notification and Campaign API
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
| Primary Domain | `communication.advertisement_campaign, communication.campaign_audience, communication.campaign_schedule, communication.campaign_delivery, communication.campaign_result, communication.notification_template, communication.notification, communication.notification_delivery, communication.notification_attempt, communication.notification_preference` |
| Audit | `audit.audit_event`, `audit.audit_entity_reference` |

---

# 26. Domain Event and Outbox Mapping

Outbox mapping is `integration.outbox_event` from `DB-11_Database_DDL_DML_Scripts.md`.

Events include campaign.created, campaign.approved, campaign.launched, campaign.paused, notification.generated, notification.delivered, notification.failed, notification.retried.

---

# 27. Audit and Notification Mapping

Audit events include CAMPAIGN_CREATED, CAMPAIGN_APPROVED, CAMPAIGN_LAUNCHED, CAMPAIGN_PAUSED, NOTIFICATION_TEMPLATE_CREATED, NOTIFICATION_DELIVERED, NOTIFICATION_RETRY_REQUESTED.

Asynchronous notifications may be triggered for customer-visible confirmations, operational alerts, approval requests, failures, lifecycle status changes, report/export completion, and compliance/security alerts where applicable.

---

# 28. Functional Requirement Mapping

| Source Document | Covered FR IDs |
|---|---|
| FR-17 Advertisement Campaign / FR-18 Notification Management | FR-CMP-001 to FR-CMP-012, FR-NOT-001 to FR-NOT-012 |

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
- Source mappings marked `TBD — Owner: Notifications/Integration; Action: provide provider/template mappings and callback fields.` require future BA/FR/API review.
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

API-10 defines Notification and Campaign Collection for Digitize. It establishes secure, tenant-aware, auditable API contracts aligned with approved functional, database, architecture, and governance source documents.
