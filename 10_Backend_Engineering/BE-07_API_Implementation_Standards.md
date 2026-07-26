# BE-07 API Implementation Standards

> Contract-first FastAPI implementation standards for routers, endpoint functions, schemas, parameters, headers, idempotency, responses, errors, versioning, observability, and testing.

---

# Document Control

| Field | Value |
|---|---|
| Document ID | BE-07 |
| Document Name | API Implementation Standards |
| Folder | 10_Backend_Engineering |
| Product | Digitize by OreeOn Technologies Pvt. Ltd. |
| Status | Design Draft |
| Governing Standard | BE-00_Backend_Engineering_Standards.md |
| Owner | Backend Engineering and API Architecture |
| Reviewers | API, Backend, Frontend, Mobile, Security, QA |
| Version | 1.0 |
| Last Updated | 2026-07-26 |

---

# 1. Purpose

This document defines how approved API Collection contracts are implemented in FastAPI without redefining the endpoint catalogue.

It keeps endpoint functions thin, secure, tenant-aware, service-driven, contract-compatible, observable, and aligned with API-00 through API-26.

---

# 2. BE-00 Inheritance

This document inherits `BE-00_Backend_Engineering_Standards.md`.

This document does not redefine API endpoint catalogues, Postman collections, domain rules, repository implementation, or UI behavior. It defines backend API implementation responsibilities only.

---

# 3. Scope

This document covers:

- Contract-first implementation.
- Router and endpoint-function responsibility.
- Request and response schema behavior.
- Transport-to-application mapping.
- Authentication, tenant context, and authorization invocation.
- Validation boundaries.
- Path, query, and header rules.
- Request and correlation identifiers.
- Pagination, filtering, sorting, search, field selection, bulk operations, idempotency, status codes, errors, rate limits, files, exports, versioning, compatibility, serialization, OpenAPI relationship, observability, security headers, tests, and anti-patterns.

---

# 4. Out of Scope

This document does not define:

- API endpoint catalogue contents.
- Business rules.
- Database schemas.
- Provider-specific contracts.
- UI layouts.
- Deployment topology.
- Production monitoring dashboards.

---

# 5. Source Alignment

| Source Area | Alignment |
|---|---|
| API-00 to API-26 | Endpoint contracts, payloads, errors, access, workflows, versioning, and readiness |
| API-19 | Error code catalog |
| API-21 | OpenAPI governance |
| API-22 | Frontend API consumption |
| API-23 | Access control matrix |
| API-24 | State and workflow contract |
| IC-01 to IC-03 | Frontend/backend, authentication, and tenant context behavior |
| BE-01 | API layer, request flow, and two-stage authorization |
| BE-02 | FastAPI project structure and schema organization |
| BE-03 | Application service orchestration |
| BE-05 | Authentication and authorization |
| BE-06 | Tenant context implementation |
| BE-08 | Error and logging behavior |

---

# 6. Contract-First Implementation

Backend APIs shall implement approved API Collection contracts.

Implementation shall:

- Match approved routes, methods, parameters, payloads, responses, errors, and access rules.
- Preserve approved resource lifecycle behavior.
- Preserve approved state and workflow actions.
- Remain backward compatible unless a breaking change is approved.
- Avoid inventing endpoint behavior in source code.

Approved API documentation remains the source of truth over generated OpenAPI output.

---

# 7. Router Responsibility

Routers shall:

- Group endpoints by capability.
- Apply approved prefixes, tags, and versioning.
- Register framework dependencies.
- Delegate execution to endpoint functions and application services.
- Avoid direct repository access.
- Avoid reusable business decisions.
- Avoid provider SDK access.

---

# 8. Endpoint-Function Responsibility

Endpoint functions shall:

- Establish or receive request and correlation context.
- Resolve authentication dependency.
- Resolve tenant context dependency.
- Validate request transport schema.
- Invoke coarse authorization where applicable.
- Map transport data into application inputs.
- Invoke application services.
- Map results into approved responses.
- Hand controlled errors to error mapping.

Endpoint functions shall remain thin.

---

# 9. Request and Response Schema Behavior

Request schemas shall:

- Match approved API request contracts.
- Validate shape, type, and required fields.
- Avoid accepting fields callers must not set.
- Support mass-assignment prevention.

Response schemas shall:

- Match approved API response contracts.
- Avoid persistence-object exposure.
- Exclude restricted fields unless caller is authorized.
- Preserve stable field names.

Schema placement is owned by BE-02.

---

# 10. Transport-to-Application Mapping

Transport-to-application mapping shall:

- Convert path, query, header, and body data into framework-independent service inputs.
- Include principal reference.
- Include tenant context.
- Include request and correlation identifiers.
- Include idempotency key where required.
- Avoid passing HTTP request or response objects into application or domain services.

---

# 11. Authentication and Tenant Dependencies

Protected endpoints shall invoke authentication before protected behavior.

Tenant-scoped endpoints shall resolve and validate tenant context before tenant-scoped data access.

Missing, invalid, or conflicting authentication or tenant context shall fail safely.

---

# 12. Authorization Invocation

Authorization shall be enforced server-side.

API implementation shall support:

- Coarse authorization before use-case execution where operation permission can be determined.
- Resource-level authorization after resource loading and before domain mutation.
- Action-level permissions.
- Tenant-scope checks.
- Entitlement checks where applicable.
- Resource-state checks where applicable.

UI visibility, hidden controls, disabled controls, and frontend route restrictions are not authorization enforcement.

---

# 13. Validation Boundaries

Validation is split by responsibility.

| Validation | Owner |
|---|---|
| Transport shape | API schema |
| Path and query format | API boundary |
| Header presence and format | API boundary |
| Tenant hierarchy | BE-06 tenant context |
| Permission and entitlement | BE-05 authorization |
| Business rule | BE-03 services |
| Persistence constraint | BE-04 repositories and database |

---

# 14. Path, Query, and Header Rules

Path parameters shall identify approved resources or parent scope.

Query parameters shall support only approved filtering, sorting, pagination, search, and field-selection behavior.

Headers shall follow approved operational header standards, including:

- `Authorization`.
- `X-Correlation-ID`.
- `X-Request-ID`.
- `X-Organization-ID`.
- `X-Facility-ID`.
- `X-Site-ID`.
- `Idempotency-Key` where required.

Headers shall not be trusted without validation.

---

# 15. Pagination, Filtering, Sorting, Search, and Field Selection

List APIs shall:

- Apply tenant and authorization restrictions.
- Validate pagination bounds.
- Preserve stable ordering.
- Apply approved filters.
- Apply approved sorting.
- Apply approved search behavior.
- Avoid unbounded result sets.
- Avoid restricted field exposure.

Field selection may be supported only where approved by API contracts and authorization rules.

---

# 16. Bulk Operations

Bulk operations shall:

- Be explicitly approved by API and Functional Requirements.
- Define transaction boundaries.
- Define partial success behavior.
- Enforce tenant and authorization checks for every affected resource.
- Define idempotency where retry-prone.
- Produce controlled error reporting.

Bulk operations shall avoid unbounded memory or transaction usage.

---

# 17. Idempotency-Key Handling

Retry-prone command endpoints shall support `Idempotency-Key` where approved.

API implementation shall:

- Validate key presence where required.
- Pass idempotency identity to application services.
- Scope idempotency to tenant and operation where required.
- Return duplicate-safe responses.
- Avoid duplicate business effects.

Idempotency storage and retention are owned by BE-03 and BE-04.

---

# 18. HTTP Status Code and Error Mapping

HTTP status codes shall match approved API contracts.

Error mapping shall handle:

- Validation errors.
- Authentication errors.
- Authorization errors.
- Tenant context errors.
- Not-found errors.
- Conflict errors.
- Rate-limit responses.
- Provider errors.
- Unexpected errors.

Cross-tenant not-found behavior shall not reveal another tenant's resource existence.

---

# 19. File Upload, Download, and Export Boundaries

File upload and download behavior shall:

- Validate tenant context.
- Validate authorization.
- Avoid exposing storage internals.
- Use approved file metadata behavior.
- Preserve audit expectations.

Export initiation shall normally create an asynchronous job or report execution according to API and integration contracts.

---

# 20. API Versioning, Backward Compatibility, and Deprecation

API implementation shall preserve backward compatibility.

Breaking changes require:

- Approved documentation update.
- Deprecation notice where applicable.
- Sunset period where applicable.
- Consumer migration period where applicable.
- Updated tests.
- Release-readiness approval.

---

# 21. Response Serialization

Serialization shall preserve approved representations for:

- Dates.
- Timestamps.
- Money.
- Identifiers.
- Enumerations.
- Status values.
- Pagination metadata.
- Error structures.

Serialization shall not expose internal persistence fields or provider internals.

---

# 22. OpenAPI Generation Relationship

FastAPI may generate OpenAPI output, but generated OpenAPI shall not replace approved API documentation.

OpenAPI generation shall align with API-21 for:

- Operation IDs.
- Tags.
- Schemas.
- Security schemes.
- Error schemas.
- Versioning.

---

# 23. API Observability

API implementation shall emit:

- Operation name.
- Route or endpoint identifier.
- Correlation ID.
- Request ID.
- Principal reference where safe.
- Tenant context.
- Outcome.
- Status code.
- Latency.
- Error code where applicable.

Sensitive data shall not be logged.

---

# 24. API Security Headers

Security headers may be applied where approved by Technical Architecture and API standards.

Security header implementation shall not substitute for backend authentication, authorization, tenant isolation, or secure error handling.

---

# 25. API Testing Expectations

API implementation tests shall cover:

- Request validation.
- Response contract compliance.
- Authentication enforcement.
- Tenant context enforcement.
- Coarse authorization.
- Resource-level authorization through service behavior.
- Path, query, and header behavior.
- Pagination, filtering, sorting, search, and field selection where approved.
- Idempotency.
- Bulk operation behavior where approved.
- Error mapping.
- Cross-tenant not-found behavior.
- Rate-limit response behavior where approved.
- File and export boundaries where applicable.
- OpenAPI compatibility where generated.
- Backward compatibility.

---

# 26. Anti-Patterns

The following are prohibited:

- Business logic in endpoint functions.
- Direct repository access from endpoints.
- Provider SDK access from endpoints.
- Passing HTTP objects into domain services.
- Returning persistence objects directly.
- Trusting tenant headers without validation.
- Treating frontend route guards as authorization.
- Inventing undocumented API behavior.
- Exposing stack traces or internal identifiers.

---

# 27. Traceability Requirements

API implementation shall trace to:

- API-00 through API-26 for contracts.
- API-19 for errors.
- API-23 for access control.
- API-24 for state and workflow behavior.
- BE-01 through BE-06 for backend execution boundaries.
- BE-08 for error and logging behavior.

Traceability sources: see [docs/10_Backend_Engineering/BE-TRACEABILITY_MAPPINGS.md](BE-TRACEABILITY_MAPPINGS.md) — primary sources include [docs/07_API_Collections/API-00_API_Collection_Standards.md](../07_API_Collections/API-00_API_Collection_Standards.md), [docs/07_API_Collections/API-21_OpenAPI_Specification_Governance.md](../07_API_Collections/API-21_OpenAPI_Specification_Governance.md), and [docs/07_API_Collections/API-19_API_Error_Code_Catalog.md](../07_API_Collections/API-19_API_Error_Code_Catalog.md).

---

# 28. Acceptance Criteria

This document is acceptable when:

- Contract-first API implementation is defined.
- Router and endpoint responsibilities are defined.
- Request/response schema behavior and transport-to-application mapping are defined.
- Authentication, tenant, authorization, validation, parameter, header, pagination, filtering, sorting, search, field selection, bulk, idempotency, status, error, file, export, versioning, serialization, OpenAPI, observability, security header, testing, and anti-pattern rules are defined.
- Endpoint implementation remains thin and service-driven.

---

# 29. Freeze Rule

This document may be frozen only after BE-01 confirms API layer boundaries, BE-03 confirms service-driven execution, BE-05 confirms authorization sequencing, BE-06 confirms tenant context behavior, and BE-08 confirms error mapping behavior.

---

# 30. Summary

BE-07 defines FastAPI API implementation standards for Digitize.

It implements approved API contracts without redefining them, keeping endpoints thin, secure, tenant-aware, service-driven, observable, backward compatible, and protected from persistence leakage or undocumented behavior.

