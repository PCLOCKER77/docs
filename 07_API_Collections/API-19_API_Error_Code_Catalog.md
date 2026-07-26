> **Status:** Frozen — 2026-07-26 — 2026-07-26

# API-19 API Error Code Catalog

**Document ID:** API-19  
**Document Name:** API Error Code Catalog  
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
**Reviewer:** Solution Architecture / Security Architecture / Backend Engineering / QA / Support  
**Dependencies:** API-00, API-01 to API-18, API-20, Security Architecture, QA  
**Last Updated:** July 2026

---

# 1. Document Metadata

| Attribute | Value |
|---|---|
| Document ID | API-19 |
| Document Name | API Error Code Catalog |
| Output File | API-19_API_Error_Code_Catalog.md |
| API Version | v1 |
| Document Version | 0.1 |
| Status | Design Draft |
| Governing Standard | API-00_API_Collection_Standards.md |

---

# 2. Purpose

This document defines the centralized Digitize API error code catalog.

It governs error code naming, HTTP status mapping, error category, severity, retry classification, safe messages, localization readiness, sensitive-data handling, observability, ownership, lifecycle, test mapping, and change governance.

---

# 3. Scope

In scope:

- Error code standards for API-01 through API-18.
- Common platform error codes.
- Domain module error code ownership.
- HTTP status mappings.
- Safe-message rules.
- Retryability and support handling.
- Error lifecycle, deprecation, and change tracking.

Out of scope:

- UI error copy finalization.
- Localization file implementation.
- Exception class implementation.
- Vendor-specific provider error payloads.
- Stack trace and debug log formats.

---

# 4. Error Design Principles

| Principle | Standard |
|---|---|
| Stable code | Error codes shall remain stable across releases unless formally changed |
| Safe message | Error messages shall not expose secrets or internal implementation details |
| Machine readable | Clients shall use `error_code`, not free-text message matching |
| Human supportable | Messages shall be clear enough for support triage |
| Retry explicit | Retryability shall be documented |
| Category aligned | Error category shall map to API-00 behavior |
| Traceable | Error codes shall map to owner, tests, and change records |

---

# 5. Error Code Format

Standard format:

```text
{DOMAIN}_{CATEGORY}_{NNN}
```

Examples:

```text
CUSTOMER_VALIDATION_001
MEMBERSHIP_CONCURRENCY_001
PAYMENT_PROVIDER_001
WEBHOOK_SIGNATURE_001
```

Rules:

- Use uppercase snake case.
- Use stable three-digit numeric suffixes.
- Do not reuse retired codes.
- Do not change the meaning of an existing code.
- Do not encode tenant, user, provider secret, or resource ID in the code.

---

# 6. Error Categories

| Category | Meaning | Typical HTTP Status |
|---|---|---|
| AUTHENTICATION | Missing, invalid, expired, or revoked authentication | 401 |
| AUTHORIZATION | User lacks permission or scope | 403 or safe 404 |
| VALIDATION | Request payload, path, query, or header validation failed | 400, 415, 422 |
| SCOPE | Tenant, Facility, Site, or object scope is invalid | 403, 404, 409 |
| CONFLICT | Current resource state conflicts with request | 409 |
| CONCURRENCY | Version or ETag precondition failed | 412 |
| IDEMPOTENCY | Idempotency key missing, replayed, or conflicting | 400, 409 |
| BUSINESS | Domain rule prevents action | 409 |
| RATE_LIMIT | Request exceeded configured rate limit | 429 |
| PROVIDER | External provider failure or callback issue | 400, 401, 409, 502, 503 |
| ASYNC | Async operation failed or is unavailable | 202, 409, 500, 503 |
| INTERNAL | Unexpected platform failure | 500 |
| UNAVAILABLE | Dependency unavailable or timed out | 502, 503, 504 |

---

# 7. HTTP Status Mapping

| HTTP Status | Standard Usage | Retryable Default |
|---|---|---|
| 400 | Malformed request or invalid required header | No |
| 401 | Authentication failed | Conditional after token refresh |
| 403 | Authorization denied | No |
| 404 | Resource not found or safe non-disclosure | No |
| 409 | Business conflict, lifecycle conflict, idempotency conflict | No |
| 412 | Optimistic concurrency precondition failed | Yes after refresh |
| 413 | Payload too large | No |
| 415 | Unsupported media type | No |
| 422 | Semantic validation failed | No |
| 429 | Rate limit exceeded | Yes after backoff |
| 500 | Internal server error | Conditional |
| 502 | External dependency bad gateway | Yes |
| 503 | Service unavailable | Yes |
| 504 | Gateway timeout | Yes |

---

# 8. Error Response Shape

All errors shall use the API-00 error envelope. Required fields:

| Field | Required | Description |
|---|---|---|
| `success` | Yes | Always `false` for error responses |
| `error.error_code` | Yes | Stable code from this catalog or module document |
| `error.message` | Yes | Safe user-facing message |
| `error.category` | Yes | Error category |
| `error.retryable` | Yes | Boolean retry guidance |
| `error.details` | Conditional | Safe field-level details |
| `metadata.correlation_id` | Yes | Traceability |
| `metadata.timestamp` | Yes | UTC timestamp |

---

# 9. Safe Message Rules

Error messages shall not include:

- SQL text.
- Stack traces.
- File paths.
- Tokens.
- Passwords.
- Provider secrets.
- Raw payment card data.
- Tenant names for unauthorized resources.
- Full PII values.
- Internal hostnames.
- Access policy internals that help bypass authorization.

Messages should:

- Explain the safe reason.
- Indicate whether user correction is possible.
- Avoid blaming a specific internal system.
- Be ready for localization.
- Be consistent across modules.

---

# 10. Severity Levels

| Severity | Meaning | Support Handling |
|---|---|---|
| Critical | Blocks transaction, security, financial, audit, or tenant isolation | Immediate triage |
| High | Blocks important workflow or creates operational risk | Priority triage |
| Medium | Blocks non-critical workflow or has workaround | Standard triage |
| Low | Informational or minor correction | Backlog or support guidance |

---

# 11. Retry Classification

| Retryable | Meaning | Client Guidance |
|---|---|---|
| Yes | Request may succeed later without payload changes | Retry with backoff |
| No | Request requires user/action/payload/permission change | Do not retry automatically |
| Conditional | Retry depends on token refresh, ETag refresh, or provider status | Follow documented condition |

Retry-safe automatic retries require idempotency when the operation changes state.

---

# 12. Common Error Catalog

| Error Code | HTTP Status | Category | Severity | Safe Message | Retryable |
|---|---|---|---|---|---|
| API_AUTHENTICATION_001 | 401 | AUTHENTICATION | High | Authentication is required. | Conditional |
| API_AUTHENTICATION_002 | 401 | AUTHENTICATION | High | Authentication token is invalid or expired. | Conditional |
| API_AUTHORIZATION_001 | 403 | AUTHORIZATION | Critical | User is not authorized for this action. | No |
| API_SCOPE_001 | 404 | AUTHORIZATION | Critical | Requested resource is unavailable. | No |
| API_VALIDATION_001 | 422 | VALIDATION | Medium | Request validation failed. | No |
| API_CONTENT_TYPE_001 | 415 | VALIDATION | Medium | Content type is not supported. | No |
| API_IDEMPOTENCY_001 | 400 | IDEMPOTENCY | High | Idempotency key is required. | No |
| API_IDEMPOTENCY_002 | 409 | IDEMPOTENCY | High | Idempotency key conflicts with a previous request. | No |
| API_CONCURRENCY_001 | 412 | CONCURRENCY | Medium | Resource changed before the request completed. | Yes |
| API_RATE_LIMIT_001 | 429 | RATE_LIMIT | Medium | Request rate limit exceeded. | Yes |
| API_INTERNAL_001 | 500 | INTERNAL | Critical | An unexpected service error occurred. | Conditional |
| API_UNAVAILABLE_001 | 503 | UNAVAILABLE | High | Service is temporarily unavailable. | Yes |

---

# 13. Module Error Code Register

| API Document | Error Prefixes | Owner |
|---|---|---|
| API-01 | PLATFORM, FEATURE, MAINTENANCE, RELEASE | API Architecture |
| API-02 | TENANT, ORG, FACILITY, SITE, HIERARCHY | API Architecture |
| API-03 | AUTH, USER, ROLE, PERMISSION, SESSION, SECURITY | Security Architecture |
| API-04 | CUSTOMER | Customer Domain |
| API-05 | MEMBERSHIP | Membership Domain |
| API-06 | ATTENDANCE, WALKIN | Operations Domain |
| API-07 | TRAINER, TRAINING, BATCH, SESSION | Training Domain |
| API-08 | BILLING, PAYMENT, REFUND, RECONCILIATION | Commercial Domain |
| API-09 | SUBSCRIPTION, LICENSE, ENTITLEMENT, FEATURE_ACCESS | Commercial Domain |
| API-10 | CAMPAIGN, NOTIFICATION, DELIVERY | Communication Domain |
| API-11 | REPORT, EXPORT, KPI | Reporting Domain |
| API-12 | SUPPORT, TICKET, SLA | Support Domain |
| API-13 | AUDIT, COMPLIANCE, INVESTIGATION, SECURITY | Audit / Security Domain |
| API-14 | REFERENCE | Platform Reference Domain |
| API-18 | WEBHOOK | Integration Architecture |

---

# 14. Domain Error Baseline

| Error Code | HTTP Status | Category | Owner | Notes |
|---|---|---|---|---|
| CUSTOMER_VALIDATION_001 | 422 | VALIDATION | API-04 | Customer request validation |
| CUSTOMER_DUPLICATE_001 | 409 | CONFLICT | API-04 | Duplicate customer match |
| MEMBERSHIP_ELIGIBILITY_001 | 409 | BUSINESS | API-05 | Membership action not eligible |
| MEMBERSHIP_PAYMENT_001 | 409 | BUSINESS | API-05 | Payment condition not satisfied |
| ATTENDANCE_ELIGIBILITY_001 | 409 | BUSINESS | API-06 | Attendance eligibility failure |
| ATTENDANCE_CAPACITY_001 | 409 | BUSINESS | API-06 | Capacity rule failure |
| TRAINING_ELIGIBILITY_001 | 409 | BUSINESS | API-07 | Training eligibility failure |
| TRAINER_CONFLICT_001 | 409 | BUSINESS | API-07 | Trainer schedule conflict |
| BILLING_VALIDATION_001 | 422 | VALIDATION | API-08 | Billing request validation |
| PAYMENT_PROVIDER_001 | 502 | PROVIDER | API-08 | Payment provider failure |
| SUBSCRIPTION_LIFECYCLE_001 | 409 | BUSINESS | API-09 | Subscription lifecycle conflict |
| LICENSE_AUTHORIZATION_001 | 403 | AUTHORIZATION | API-09 | License action denied |
| NOTIFICATION_DELIVERY_001 | 503 | PROVIDER | API-10 | Delivery provider failure |
| REPORT_ASYNC_001 | 202 | ASYNC | API-11 | Report accepted for async processing |
| SUPPORT_LIFECYCLE_001 | 409 | BUSINESS | API-12 | Ticket lifecycle conflict |
| AUDIT_EXPORT_001 | 403 | AUTHORIZATION | API-13 | Audit export denied |
| REFERENCE_VALIDATION_001 | 422 | VALIDATION | API-14 | Reference lookup validation |
| WEBHOOK_SIGNATURE_001 | 401 | AUTHENTICATION | API-18 | Signature validation failed |

---

# 15. Field-level Validation Detail Format

Validation errors may include field details:

```json
{
  "field": "customer_id",
  "code": "REQUIRED",
  "message": "Customer ID is required."
}
```

Rules:

- Field names shall use snake_case.
- Details shall not include rejected secret values.
- Details shall not expose database constraint names.
- Details shall be stable enough for test automation.

---

# 16. Localization Readiness

| Field | Localization Rule |
|---|---|
| `error_code` | Never localized |
| `message` | Localization-ready safe message |
| `details.message` | Localization-ready where exposed to users |
| `category` | Never localized in API response |
| Support metadata | Not user-facing unless approved |

Localized UI copy may differ from API safe message, but shall map back to the same `error_code`.

---

# 17. Observability Requirements

Every error log shall include:

- `correlation_id`.
- `error_code`.
- HTTP status.
- API document or module.
- Endpoint ID where available.
- Organization scope where safe.
- Actor identifier where safe.
- Retryable flag.
- Latency and dependency timing where applicable.

Error logs shall not include secrets, tokens, raw payment data, or full sensitive payloads.

---

# 18. Support Triage Mapping

| Category | Support Action |
|---|---|
| AUTHENTICATION | Guide token/session refresh or credential support |
| AUTHORIZATION | Verify role, permission, and scope |
| VALIDATION | Guide user correction |
| BUSINESS | Explain lifecycle or domain rule |
| CONCURRENCY | Ask user to refresh and retry |
| IDEMPOTENCY | Investigate duplicate or conflicting submission |
| PROVIDER | Check provider status and integration logs |
| RATE_LIMIT | Ask user/client to retry after backoff |
| INTERNAL | Escalate with correlation ID |
| UNAVAILABLE | Escalate to operations if persistent |

---

# 19. Test Mapping

| Error Area | API-16 Scenario |
|---|---|
| Authentication | API-16-AUTH-001 to API-16-AUTH-007 |
| Authorization | API-16-AZ-001 to API-16-AZ-006 |
| Tenant scope | API-16-TEN-001 to API-16-TEN-006 |
| Validation | API-16-VAL-001 to API-16-VAL-007 |
| Response contract | API-16-RSP-005 |
| Idempotency | API-16-IDEMP-001 to API-16-IDEMP-006 |
| Concurrency | API-16-CON-001 to API-16-CON-005 |
| Rate limit | API-16-RATE-001 to API-16-RATE-005 |
| Webhook | API-16-WHK-001 to API-16-WHK-007 |
| Security leakage | API-16-SEC-001 to API-16-SEC-006 |

---

# 20. Error Lifecycle

| Lifecycle State | Meaning |
|---|---|
| Proposed | Error code identified but not approved |
| Active | Error code approved for implementation and tests |
| Changed | Metadata changed without changing semantic meaning |
| Deprecated | Error code should not be used for new behavior |
| Retired | Error code no longer emitted |

Retired error codes shall not be reused.

---

# 21. Change Governance

API-20 change records are required when:

- A new error code is added.
- An error code changes HTTP status.
- Retryability changes.
- A safe message changes meaning.
- A code is deprecated or retired.
- Webhook, payment, auth, or tenant-scope error behavior changes.

---

# 22. Review Checklist

| Check | Required |
|---|---|
| Error code follows naming standard | Yes |
| HTTP status is appropriate | Yes |
| Category is defined | Yes |
| Safe message is approved | Yes |
| Retryable flag is set | Yes |
| Owner is assigned | Yes |
| API-16 negative test exists | Yes |
| API-17 traceability row updated | Yes |
| API-20 change record created if needed | Conditional |

---

# 23. Assumptions and Constraints

- Exact module-local codes remain owned by API-01 through API-14 and API-18.
- UI localization implementation is not part of this document.
- Provider-specific error translation requires integration-specific mapping.
- Frozen API documents shall not emit undocumented error codes.

---

# 24. Document Acceptance Criteria

This document is acceptable when:

- Error naming, categories, HTTP mappings, severity, retryability, and safe-message rules are defined.
- Common and module error registers are present.
- Support, observability, localization, and test mappings are documented.
- Error lifecycle and API-20 change governance are explicit.

---

# 25. Summary

API-19 centralizes Digitize API error governance. It ensures API errors are stable, safe, testable, supportable, localization-ready, traceable, and consistent across all API collection documents.
