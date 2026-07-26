> **Status:** Frozen — 2026-07-26 — 2026-07-26

# API-21 OpenAPI Specification Governance

**Document ID:** API-21  
**Document Name:** OpenAPI Specification Governance  
**Company:** OreeOn Technologies Pvt. Ltd.  
**Product:** Digitize  
**Document Type:** API Governance Documentation  
**Backend Technology:** FastAPI  
**Database Engine:** PostgreSQL  
**Authentication:** JWT  
**API Version:** v1  
**Document Version:** 0.1  
**Status:** Design Draft  
**Owner:** API Architecture  
**Reviewer:** Solution Architecture / Security Architecture / Backend Engineering / QA / DevOps  
**Dependencies:** API-00 to API-26, TA-04, TA-05, TA-06  
**Last Updated:** July 2026

---

# 1. Document Metadata

| Attribute | Value |
|---|---|
| Document ID | API-21 |
| Document Name | OpenAPI Specification Governance |
| Output File | API-21_OpenAPI_Specification_Governance.md |
| API Version | v1 |
| Document Version | 0.1 |
| Status | Design Draft |
| Governing Standard | API-00_API_Collection_Standards.md |

---

# 2. Purpose

This document defines how Digitize Markdown API documentation shall be converted into governed FastAPI/OpenAPI contracts.

It does not generate OpenAPI JSON or YAML. It defines the standards, review controls, naming conventions, schema rules, security definitions, publication process, and breaking-change detection expectations for the generated OpenAPI specification.

---

# 3. Scope

In scope:

- OpenAPI version and FastAPI schema-generation standards.
- Operation ID, tag, summary, description, request schema, response schema, header, and error schema naming.
- Common reusable schemas for API-00 envelopes, pagination, errors, idempotency, and concurrency.
- Authentication and security scheme definitions.
- Environment-specific server URL representation.
- Deprecation representation.
- OpenAPI review, publication, versioning, and breaking-change detection.

Out of scope:

- Generated OpenAPI JSON/YAML files.
- FastAPI implementation code.
- SDK generation.
- Runtime API gateway configuration.
- Vendor-specific API portal tooling.

---

# 4. Governance Principles

| Principle | Standard |
|---|---|
| Documentation-led | OpenAPI output shall reflect API-00 through API-20 contracts |
| FastAPI-compatible | Schema definitions shall be implementable through FastAPI and Pydantic |
| Stable operations | Operation IDs shall remain stable once published |
| Reusable schemas | Common envelopes, errors, headers, and pagination shall be shared |
| Security explicit | JWT, service identity, and webhook security shall be represented |
| Environment-aware | Published specs shall list approved server profiles |
| Change-detected | Breaking schema changes shall be detected before release |

---

# 5. OpenAPI Version

| Item | Standard |
|---|---|
| OpenAPI version | `3.1.x` preferred |
| Fallback version | `3.0.3` only if tooling requires it |
| API version | `/api/v1` |
| Schema dialect | JSON Schema compatible with selected OpenAPI version |
| Source of truth | API Markdown documents plus FastAPI route/schema implementation |

---

# 6. FastAPI Generation Standards

FastAPI route definitions shall include:

- Explicit `response_model`.
- Explicit status codes.
- Tags matching API document folders.
- Summary and description text aligned to API documents.
- Stable operation IDs.
- Request body models for JSON payloads.
- Query/path/header parameter metadata.
- Response examples where approved.
- Error response references for common and module errors.

---

# 7. Operation ID Naming

Operation IDs shall use lower camel-like snake naming without module ambiguity:

```text
{domain}_{action}_{resource}
```

Examples:

| Endpoint | Operation ID |
|---|---|
| `POST /api/v1/customers` | `customer_register_customer` |
| `POST /api/v1/memberships/{membership_id}/freeze` | `membership_freeze_membership` |
| `POST /api/v1/payments/online` | `billing_process_online_payment` |
| `GET /api/v1/audit-events` | `audit_review_audit_events` |

Rules:

- Operation IDs shall not change after publication unless a breaking change is approved.
- Operation IDs shall be unique across the full API.
- Operation IDs shall not include HTTP method names unless needed to avoid ambiguity.

---

# 8. Tagging Conventions

| API Document | OpenAPI Tag |
|---|---|
| API-01 | Platform Administration |
| API-02 | Organization Facility Site |
| API-03 | Identity User Role |
| API-04 | Customer Management |
| API-05 | Membership Management |
| API-06 | Attendance Walk-in |
| API-07 | Trainer Activity Batch |
| API-08 | Billing Payment |
| API-09 | Subscription License |
| API-10 | Notification Campaign |
| API-11 | Reports Analytics |
| API-12 | Support Ticket |
| API-13 | Audit Security |
| API-14 | Common Reference |
| API-18 | Webhooks |

---

# 9. Summary and Description Rules

| Field | Standard |
|---|---|
| Summary | Short business action name |
| Description | Contract behavior, scope, auth, idempotency/concurrency note |
| Deprecated note | Include replacement and sunset where known |
| External docs | Link to Markdown document where supported |

Descriptions shall not contain implementation stack traces, internal service names unless approved, or sensitive security internals.

---

# 10. Schema Naming Standards

| Schema Type | Naming Pattern | Example |
|---|---|---|
| Create request | `{Resource}CreateRequest` | `CustomerCreateRequest` |
| Update request | `{Resource}UpdateRequest` | `CustomerUpdateRequest` |
| Action request | `{Resource}{Action}Request` | `MembershipFreezeRequest` |
| Response data | `{Resource}Response` | `MembershipResponse` |
| List response | `{Resource}ListResponse` | `CustomerListResponse` |
| Error response | `{Domain}ErrorResponse` | `MembershipErrorResponse` |
| Event payload | `{EventName}EventPayload` | `MembershipActivatedEventPayload` |

Schema names shall remain stable after publication.

---

# 11. Common Reusable Schemas

| Schema | Purpose |
|---|---|
| `SuccessEnvelope` | Standard API-00 success wrapper |
| `ErrorEnvelope` | Standard API-00 error wrapper |
| `ErrorDetail` | Field-level safe validation detail |
| `PaginationMetadata` | Offset pagination metadata |
| `CursorMetadata` | Cursor pagination metadata |
| `CorrelationMetadata` | Correlation and timestamp metadata |
| `AsyncOperationResponse` | `202 Accepted` operation status reference |
| `IdempotencyConflictError` | Idempotency replay/conflict error shape |
| `ConcurrencyError` | ETag/precondition error shape |

---

# 12. Header Definitions

| Header | OpenAPI Location | Required Rule |
|---|---|---|
| `Authorization` | Security scheme | Required for authenticated APIs |
| `X-Correlation-ID` | Header parameter | Required or generated |
| `X-Organization-ID` | Header parameter | Tenant APIs |
| `X-Facility-ID` | Header parameter | Facility APIs |
| `X-Site-ID` | Header parameter | Site APIs |
| `Idempotency-Key` | Header parameter | Create/lifecycle/payment/retry actions |
| `If-Match` | Header parameter | Protected updates/actions |
| `X-Digitize-Signature` | Header parameter | Outbound webhook documentation |
| Provider signature header | Header parameter | Inbound webhook callbacks |

---

# 13. Security Scheme Definitions

| Scheme | Type | Applies To |
|---|---|---|
| `BearerAuth` | HTTP bearer JWT | Tenant, Platform, Authentication-adjacent APIs |
| `ServiceAuth` | HTTP bearer or mutual TLS reference | Internal APIs |
| `WebhookSignature` | API key/header signature model | Webhook callbacks |
| `ProviderSignature` | Provider-specific header signature | Inbound provider callbacks |

JWT scopes/permissions shall be represented through endpoint descriptions or extension fields until final authorization schema is approved.

---

# 14. Error Schema References

Every endpoint shall reference:

- Common `ErrorEnvelope`.
- `401` authentication error where applicable.
- `403` authorization error where applicable.
- `404` safe not found where applicable.
- `409` conflict/lifecycle/idempotency error where applicable.
- `412` concurrency error where applicable.
- `422` validation error where applicable.
- `429` rate-limit error where applicable.
- Module-specific API-19 error codes in examples or extensions.

---

# 15. Pagination Schemas

Offset-paginated endpoints shall reference `PaginationMetadata`.

Cursor-paginated endpoints shall reference `CursorMetadata`.

OpenAPI parameters shall document:

- `page`.
- `page_size`.
- `cursor`.
- `limit`.
- Approved filter parameters.
- Approved sort parameters.
- Search query constraints.

---

# 16. Deprecated Endpoint Representation

Deprecated endpoints shall include:

| OpenAPI Field | Requirement |
|---|---|
| `deprecated` | `true` |
| Description | Replacement endpoint and migration note |
| Extension | `x-sunset-date` where known |
| Extension | `x-replacement-operation-id` where known |
| API-20 mapping | Required |

---

# 17. Server URL Definitions

Published OpenAPI documents may include server entries:

| Server | URL Pattern | Notes |
|---|---|---|
| Local | `http://localhost:{port}` | Local only |
| Development | `https://api.dev.{domain}` | Non-production |
| QA | `https://api.qa.{domain}` | Test |
| Staging | `https://api.staging.{domain}` | Release candidate |
| Sandbox | `https://api.sandbox.{domain}` | Partner/demo |
| Production | `https://api.{domain}` | Production |

Actual domains are environment-specific and governed by DevOps.

---

# 18. OpenAPI Review Process

1. API Markdown document reaches Design Draft.
2. FastAPI route and schema implementation is created.
3. OpenAPI artifact is generated.
4. API Architecture reviews operation IDs, tags, summaries, schemas, and response references.
5. Security Architecture reviews security schemes and sensitive fields.
6. QA reviews API-16 test compatibility.
7. DevOps reviews publication environment and artifact location.
8. API-20 change record is updated where needed.

---

# 19. Publication Rules

| Artifact | Publication Rule |
|---|---|
| OpenAPI JSON | Published for automation and tooling |
| OpenAPI YAML | Optional, if required by tooling |
| Human API docs | Generated from OpenAPI only after Markdown contract review |
| SDKs | Not generated until OpenAPI artifact is reviewed |
| Public portal | Requires Product and Security approval |

---

# 20. Breaking-change Detection

Breaking-change checks shall detect:

- Removed paths.
- Removed methods.
- Changed operation IDs.
- Removed or renamed schemas.
- Removed response fields.
- Request fields made required.
- Field type changes.
- Required header changes.
- Error response shape changes.
- Security scheme changes.
- Deprecated endpoint retirement.

Breaking changes require API-20 governance.

---

# 21. Validation Checklist

| Check | Required |
|---|---|
| OpenAPI version approved | Yes |
| All paths use `/api/v1` | Yes |
| Operation IDs are unique | Yes |
| Tags match API documents | Yes |
| Request/response schemas are named | Yes |
| Error responses reference API-19 | Yes |
| Headers match API-00/API-15 | Yes |
| Security schemes are defined | Yes |
| Deprecated endpoints are marked | Conditional |
| Breaking-change scan passed | Yes before release |

---

# 22. Traceability

| Source | Mapping |
|---|---|
| API-00 | Common API standards |
| API-15 | Environment and header variables |
| API-16 | Contract test validation |
| API-17 | Endpoint traceability |
| API-18 | Webhook schema and signature rules |
| API-19 | Error schemas and codes |
| API-20 | Change governance |

---

# 23. Assumptions and Constraints

- OpenAPI artifacts are generated from implementation but governed by Markdown contracts.
- Exact publication domain names are pending DevOps configuration.
- SDK generation is future scope.
- Public developer portal publication requires a separate approval.

---

# 24. Acceptance Criteria

This document is acceptable when OpenAPI versioning, schema naming, operation IDs, security schemes, common schemas, error references, publication, review, and breaking-change detection rules are implementation-ready.

---

# 25. Summary

API-21 bridges Markdown API design and generated FastAPI/OpenAPI contracts. It ensures OpenAPI artifacts remain stable, secure, traceable, testable, and aligned with the approved Digitize API documentation set.
