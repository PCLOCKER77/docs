# (status banner removed to preserve metadata `Status: Design Draft`)
# API-08 Billing and Payment Collection

**Document ID:** API-08  
**Document Name:** Billing and Payment Collection  
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
**Dependencies:** API-00, API-04, API-05, API-06, API-09, FR-14, BA-03, BA-04, CS-02, CS-03, CS-04, DB-11  
**Last Updated:** 2026-07-26

---

# 1. Document Metadata

| Attribute | Value |
|---|---|
| Document ID | API-08 |
| Document Name | Billing and Payment Collection |
| Output File | API-08_Billing_Payment_Collection.md |
| API Version | v1 |
| Document Version | 0.1 |
| Status | Design Draft |
| Governing Standard | API-00_API_Collection_Standards.md |

---

# 2. Purpose

This document defines Billing and Payment API contracts for invoices, charge calculation, discounts, taxes, adjustments, credit notes, payment collection, online/offline payment, receipts, refunds, reconciliation, payment cancellation, history, outstanding statements, and commercial reports.

---

# 3. Scope

In scope:

- Endpoint catalogue and REST contract rules for Billing and Payment Collection.
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

Billing and payment APIs protect revenue traceability. They must avoid raw card storage, preserve historical invoice values, support retry-safe gateway interactions, and keep financial state auditable.

---

# 5. Domain Overview

| Capability | Description | Source |
|---|---|---|
| Billing and Payment | API contracts, validation, lifecycle, audit, events, and tests | FR-BPM-001 to FR-BPM-018 |

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
| Primary Resources | `/api/v1/billing` | `commercial.invoice` |
| History and Reports | `/api/v1/billing/history` | `commercial.invoice` |

---

# 9. API Endpoint Catalogue

| Endpoint ID | Method | URL | Endpoint Name | FR Mapping |
|---|---|---|---|---|
| API-08-001 | POST | `/api/v1/invoices` | Generate Invoice | FR-BPM-001 |
| API-08-002 | POST | `/api/v1/billing/charges/calculate` | Calculate Service Charges | FR-BPM-002 |
| API-08-003 | POST | `/api/v1/invoices/{invoice_id}/discounts` | Apply Discounts | FR-BPM-003 |
| API-08-004 | POST | `/api/v1/invoices/{invoice_id}/taxes/calculate` | Calculate Taxes | FR-BPM-004 |
| API-08-005 | POST | `/api/v1/invoices/{invoice_id}/adjustments` | Apply Billing Adjustments | FR-BPM-005 |
| API-08-006 | POST | `/api/v1/invoices/{invoice_id}/cancel` | Cancel Invoice | FR-BPM-006 |
| API-08-007 | POST | `/api/v1/invoices/{invoice_id}/credit-notes` | Generate Credit Note | FR-BPM-007 |
| API-08-008 | POST | `/api/v1/payments` | Collect Payment | FR-BPM-008 |
| API-08-009 | POST | `/api/v1/payments/online` | Process Online Payment | FR-BPM-009 |
| API-08-010 | POST | `/api/v1/payments/offline` | Record Offline Payment | FR-BPM-010 |
| API-08-011 | GET | `/api/v1/payments/{payment_id}/status` | Verify Payment Status | FR-BPM-011 |
| API-08-012 | POST | `/api/v1/payments/{payment_id}/receipts` | Generate Payment Receipt | FR-BPM-012 |
| API-08-013 | POST | `/api/v1/payments/{payment_id}/refunds` | Process Refund | FR-BPM-013 |
| API-08-014 | POST | `/api/v1/reconciliations` | Reconcile Payment | FR-BPM-014 |
| API-08-015 | POST | `/api/v1/payments/{payment_id}/cancel` | Cancel Payment | FR-BPM-015 |
| API-08-016 | GET | `/api/v1/billing/history` | View Billing and Payment History | FR-BPM-016 |
| API-08-017 | GET | `/api/v1/commercial/reports` | Generate Commercial Reports | FR-BPM-017 |
| API-08-018 | GET | `/api/v1/billing/outstanding-statements` | Generate Outstanding Statement | FR-BPM-018 |

---

# 10. Common Authentication Requirements

All endpoints require JWT authentication unless explicitly classified as Public, Internal, Integration, or Webhook by API-00.

---

# 11. Common Authorization Requirements

Authorization shall validate Organization, Facility, Site where applicable, role, permission, object ownership, lifecycle status, subscription/license/feature access, and data classification before domain execution.

Approved permission families: billing.create, billing.update, billing.view, billing.lifecycle.manage, billing.history.view, billing.report.view.

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
| BILLING_AUTHORIZATION_001 | 403 | Authorization | User is not authorized for this billing and payment collection action. | No |
| BILLING_VALIDATION_001 | 422 | Validation | Billing and Payment Collection request validation failed. | No |
| BILLING_SCOPE_001 | 404 | Authorization | Requested resource is unavailable. | No |
| BILLING_LIFECYCLE_001 | 409 | Business | Requested lifecycle action is not allowed. | No |
| BILLING_CONCURRENCY_001 | 412 | Conflict | Resource changed before the request completed. | Yes |
| BILLING_IDEMPOTENCY_001 | 409 | Conflict | Idempotency key conflicts with a previous request. | No |

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
| API-08-001 | Generate Invoice | `generate.invoice` | 201/200 with resulting state | `commercial.invoice, commercial.invoice_item, commercial.billing_adjustment, commercial.payment, commercial.payment_attempt, commercial.receipt, commercial.refund, commercial.reconciliation`, `audit.audit_event` | GENERATE_INVOICE | generate.invoice | Scope, validation, audit, and error-path tests |
| API-08-002 | Calculate Service Charges | `calculate.service.charges` | 201/200 with resulting state | `commercial.invoice, commercial.invoice_item, commercial.billing_adjustment, commercial.payment, commercial.payment_attempt, commercial.receipt, commercial.refund, commercial.reconciliation`, `audit.audit_event` | CALCULATE_SERVICE_CHARGES | calculate.service.charges | Scope, validation, audit, and error-path tests |
| API-08-003 | Apply Discounts | `apply.discounts` | 201/200 with resulting state | `commercial.invoice, commercial.invoice_item, commercial.billing_adjustment, commercial.payment, commercial.payment_attempt, commercial.receipt, commercial.refund, commercial.reconciliation`, `audit.audit_event` | APPLY_DISCOUNTS | apply.discounts | Scope, validation, audit, and error-path tests |
| API-08-004 | Calculate Taxes | `calculate.taxes` | 201/200 with resulting state | `commercial.invoice, commercial.invoice_item, commercial.billing_adjustment, commercial.payment, commercial.payment_attempt, commercial.receipt, commercial.refund, commercial.reconciliation`, `audit.audit_event` | CALCULATE_TAXES | calculate.taxes | Scope, validation, audit, and error-path tests |
| API-08-005 | Apply Billing Adjustments | `apply.billing.adjustments` | 201/200 with resulting state | `commercial.invoice, commercial.invoice_item, commercial.billing_adjustment, commercial.payment, commercial.payment_attempt, commercial.receipt, commercial.refund, commercial.reconciliation`, `audit.audit_event` | APPLY_BILLING_ADJUSTMENTS | apply.billing.adjustments | Scope, validation, audit, and error-path tests |
| API-08-006 | Cancel Invoice | `cancel.invoice` | 201/200 with resulting state | `commercial.invoice, commercial.invoice_item, commercial.billing_adjustment, commercial.payment, commercial.payment_attempt, commercial.receipt, commercial.refund, commercial.reconciliation`, `audit.audit_event` | CANCEL_INVOICE | cancel.invoice | Scope, validation, audit, and error-path tests |
| API-08-007 | Generate Credit Note | `generate.credit.note` | 201/200 with resulting state | `commercial.invoice, commercial.invoice_item, commercial.billing_adjustment, commercial.payment, commercial.payment_attempt, commercial.receipt, commercial.refund, commercial.reconciliation`, `audit.audit_event` | GENERATE_CREDIT_NOTE | generate.credit.note | Scope, validation, audit, and error-path tests |
| API-08-008 | Collect Payment | `collect.payment` | 201/200 with resulting state | `commercial.invoice, commercial.invoice_item, commercial.billing_adjustment, commercial.payment, commercial.payment_attempt, commercial.receipt, commercial.refund, commercial.reconciliation`, `audit.audit_event` | COLLECT_PAYMENT | collect.payment | Scope, validation, audit, and error-path tests |
| API-08-009 | Process Online Payment | `process.online.payment` | 201/200 with resulting state | `commercial.invoice, commercial.invoice_item, commercial.billing_adjustment, commercial.payment, commercial.payment_attempt, commercial.receipt, commercial.refund, commercial.reconciliation`, `audit.audit_event` | PROCESS_ONLINE_PAYMENT | process.online.payment | Scope, validation, audit, and error-path tests |
| API-08-010 | Record Offline Payment | `record.offline.payment` | 201/200 with resulting state | `commercial.invoice, commercial.invoice_item, commercial.billing_adjustment, commercial.payment, commercial.payment_attempt, commercial.receipt, commercial.refund, commercial.reconciliation`, `audit.audit_event` | RECORD_OFFLINE_PAYMENT | record.offline.payment | Scope, validation, audit, and error-path tests |
| API-08-011 | Verify Payment Status | `verify.payment.status` | 200 OK | `commercial.invoice, commercial.invoice_item, commercial.billing_adjustment, commercial.payment, commercial.payment_attempt, commercial.receipt, commercial.refund, commercial.reconciliation`, `audit.audit_event` | VERIFY_PAYMENT_STATUS | verify.payment.status | Scope, validation, audit, and error-path tests |
| API-08-012 | Generate Payment Receipt | `generate.payment.receipt` | 201/200 with resulting state | `commercial.invoice, commercial.invoice_item, commercial.billing_adjustment, commercial.payment, commercial.payment_attempt, commercial.receipt, commercial.refund, commercial.reconciliation`, `audit.audit_event` | GENERATE_PAYMENT_RECEIPT | generate.payment.receipt | Scope, validation, audit, and error-path tests |
| API-08-013 | Process Refund | `process.refund` | 201/200 with resulting state | `commercial.invoice, commercial.invoice_item, commercial.billing_adjustment, commercial.payment, commercial.payment_attempt, commercial.receipt, commercial.refund, commercial.reconciliation`, `audit.audit_event` | PROCESS_REFUND | process.refund | Scope, validation, audit, and error-path tests |
| API-08-014 | Reconcile Payment | `reconcile.payment` | 201/200 with resulting state | `commercial.invoice, commercial.invoice_item, commercial.billing_adjustment, commercial.payment, commercial.payment_attempt, commercial.receipt, commercial.refund, commercial.reconciliation`, `audit.audit_event` | RECONCILE_PAYMENT | reconcile.payment | Scope, validation, audit, and error-path tests |
| API-08-015 | Cancel Payment | `cancel.payment` | 201/200 with resulting state | `commercial.invoice, commercial.invoice_item, commercial.billing_adjustment, commercial.payment, commercial.payment_attempt, commercial.receipt, commercial.refund, commercial.reconciliation`, `audit.audit_event` | CANCEL_PAYMENT | cancel.payment | Scope, validation, audit, and error-path tests |
| API-08-016 | View Billing and Payment History | `view.billing.and.payment.history` | 200 OK | `commercial.invoice, commercial.invoice_item, commercial.billing_adjustment, commercial.payment, commercial.payment_attempt, commercial.receipt, commercial.refund, commercial.reconciliation`, `audit.audit_event` | VIEW_BILLING_AND_PAYMENT_HISTORY | view.billing.and.payment.history | Scope, validation, audit, and error-path tests |
| API-08-017 | Generate Commercial Reports | `generate.commercial.reports` | 200 OK | `commercial.invoice, commercial.invoice_item, commercial.billing_adjustment, commercial.payment, commercial.payment_attempt, commercial.receipt, commercial.refund, commercial.reconciliation`, `audit.audit_event` | GENERATE_COMMERCIAL_REPORTS | generate.commercial.reports | Scope, validation, audit, and error-path tests |
| API-08-018 | Generate Outstanding Statement | `generate.outstanding.statement` | 200 OK | `commercial.invoice, commercial.invoice_item, commercial.billing_adjustment, commercial.payment, commercial.payment_attempt, commercial.receipt, commercial.refund, commercial.reconciliation`, `audit.audit_event` | GENERATE_OUTSTANDING_STATEMENT | generate.outstanding.statement | Scope, validation, audit, and error-path tests |

---

# 23. Module Sequence Diagram

```mermaid
sequenceDiagram
    participant Client
    participant API as Billing and Payment API
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
| Primary Domain | `commercial.invoice, commercial.invoice_item, commercial.billing_adjustment, commercial.payment, commercial.payment_attempt, commercial.receipt, commercial.refund, commercial.reconciliation` |
| Audit | `audit.audit_event`, `audit.audit_entity_reference` |

---

# 26. Domain Event and Outbox Mapping

Outbox mapping is `integration.outbox_event` from `DB-11_Database_DDL_DML_Scripts.md`.

Events include invoice.generated, payment.collected, payment.failed, receipt.generated, refund.processed, reconciliation.completed.

---

# 27. Audit and Notification Mapping

Audit events include INVOICE_GENERATED, PAYMENT_COLLECTED, ONLINE_PAYMENT_PROCESSED, OFFLINE_PAYMENT_RECORDED, RECEIPT_GENERATED, REFUND_PROCESSED, RECONCILIATION_COMPLETED.

Asynchronous notifications may be triggered for customer-visible confirmations, operational alerts, approval requests, failures, lifecycle status changes, report/export completion, and compliance/security alerts where applicable.

---

# 28. Functional Requirement Mapping

| Source Document | Covered FR IDs |
|---|---|
| FR-14 Billing and Payment Management | FR-BPM-001 to FR-BPM-018 |

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
- Source mappings marked `TBD — Owner: Commercial & Security; Action: provide provider field mappings and callback signature details, or confirm N/A.` require future BA/FR/API review.
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

API-08 defines Billing and Payment Collection for Digitize. It establishes secure, tenant-aware, auditable API contracts aligned with approved functional, database, architecture, and governance source documents.
