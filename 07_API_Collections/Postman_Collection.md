> **Status:** Frozen — 2026-07-26 — 2026-07-26

# Postman Collection

**Document Name:** Postman Collection  
**Company:** OreeOn Technologies Pvt. Ltd.  
**Product:** Digitize  
**Document Type:** API Execution and Collection Blueprint  
**Backend Technology:** FastAPI  
**Database Engine:** PostgreSQL  
**Authentication:** JWT  
**API Version:** v1  
**Document Version:** 0.1  
**Status:** Design Draft  
**Owner:** API Architecture / QA  
**Reviewer:** Solution Architecture / Security Architecture / Backend Engineering / DevOps  
**Dependencies:** API-00 to API-26  
**Last Updated:** July 2026

---

# 1. Document Metadata

| Attribute | Value |
|---|---|
| Document Name | Postman Collection |
| Output File | Postman_Collection.md |
| API Version | v1 |
| Document Version | 0.1 |
| Status | Design Draft |
| Governing Standards | API-00, API-15, API-16, API-17, API-19 |

---

# 2. Purpose

This document defines the Postman collection blueprint for Digitize APIs.

It is not the exported Postman JSON file. It defines how the Postman collection shall be structured, named, parameterized, secured, tested, executed, versioned, and governed before an executable `.postman_collection.json` artifact is generated.

---

# 3. Scope

In scope:

- Postman workspace and collection organization.
- Folder structure for API-01 through API-14 domain APIs.
- Governance folders for environment, test, traceability, webhook, error, and change-log validation.
- Request naming, URL conventions, headers, variables, pre-request scripts, and test scripts.
- Authentication, tenant context, idempotency, concurrency, pagination, and error validation.
- Newman/CI execution guidance.
- Export, versioning, review, and acceptance criteria.

Out of scope:

- Generated Postman JSON artifact.
- Real credentials, JWTs, tenant IDs, provider secrets, and payment tokens.
- OpenAPI generation.
- FastAPI implementation code.
- Production test data.

---

# 4. Collection Principles

| Principle | Standard |
|---|---|
| Contract-first | Requests shall follow API-00 and module API documents |
| Environment-driven | No hard-coded base URLs, tenant IDs, or secrets |
| Tenant-safe | Tenant context headers are explicit and tested |
| Repeatable | Requests can run locally and in CI with approved variables |
| Testable | Each request includes minimum API-16 assertions |
| Traceable | Request names include endpoint IDs |
| Secret-safe | Collection exports shall not contain live secrets |
| Reviewable | Changes map to API-20 change records where material |

---

# 5. Collection Naming

| Artifact | Naming Standard |
|---|---|
| Collection display name | `Digitize API v1 - Design Draft` |
| Exported collection file | `Digitize_API_v1.postman_collection.json` |
| Environment template | `Digitize_API_v1.environment.template.json` |
| QA environment file | `Digitize_API_v1.qa.environment.json` |
| CI environment file | `Digitize_API_v1.ci.environment.json` |
| Newman report | `digitize-api-v1-newman-report` |

Secret-bearing environment files shall not be committed.

---

# 6. Collection Folder Structure

```text
Digitize API v1
├── 00 Collection Setup
├── 01 Platform Administration
├── 02 Organization Facility Site
├── 03 Identity User Role
├── 04 Customer Management
├── 05 Membership Management
├── 06 Attendance Walk-in
├── 07 Trainer Activity Batch
├── 08 Billing Payment
├── 09 Subscription License
├── 10 Notification Campaign
├── 11 Reports Analytics
├── 12 Support Ticket
├── 13 Audit Security
├── 14 Common Reference
├── 15 Environment Validation
├── 16 Reusable Test Scenarios
├── 17 Traceability Checks
├── 18 Webhook Validation
├── 19 Error Code Validation
├── 20 Change Governance Checks
├── 21 OpenAPI Governance Checks
├── 22 Frontend Consumption Checks
├── 23 Access Control Checks
├── 24 State Workflow Checks
├── 25 Mocking Sandbox Checks
└── 26 Release Readiness Checks
```

Folder numbering shall match API documentation numbering.

---

# 7. Request Naming Standard

Request names shall use:

```text
{Endpoint ID} {Method} {Business Endpoint Name}
```

Examples:

```text
API-04-001 POST Register Customer
API-05-006 POST Freeze Membership
API-08-009 POST Process Online Payment
API-11-009 POST Export Report
```

Rules:

- Do not use unnumbered request names.
- Do not name requests only by URL.
- Do not duplicate endpoint IDs.
- Mark negative-path helper requests with a suffix such as `[Negative - Unauthorized]`.

---

# 8. URL Construction

All request URLs shall use environment variables:

```text
{{base_url}}/api/{{api_version}}/{resource}
```

Examples:

```text
{{base_url}}/api/{{api_version}}/customers
{{base_url}}/api/{{api_version}}/memberships/{{membership_id}}/freeze
{{base_url}}/api/{{api_version}}/payments/{{payment_id}}/refunds
```

Hard-coded environment-specific URLs are not approved.

---

# 9. Collection-level Authorization

Default collection authorization:

| Setting | Value |
|---|---|
| Type | Bearer Token |
| Token | `{{access_token}}` |

Request-level authorization may override collection-level authorization only for:

- Authentication endpoints.
- Public endpoints.
- Inbound webhook callback tests.
- Internal/service identity tests.

---

# 10. Collection-level Headers

| Header | Value | Required |
|---|---|---|
| `Accept` | `application/json` | Yes |
| `Content-Type` | `application/json` | Conditional |
| `X-Correlation-ID` | `{{correlation_id}}` | Required or generated |
| `X-Organization-ID` | `{{organization_id}}` | Tenant APIs |
| `X-Facility-ID` | `{{facility_id}}` | Facility APIs |
| `X-Site-ID` | `{{site_id}}` | Site APIs |
| `Idempotency-Key` | `{{idempotency_key}}` | Create/lifecycle/payment/retry actions |
| `If-Match` | `{{etag}}` | Protected updates/actions |

Headers that do not apply to an endpoint may be disabled at request level, but the reason shall be documented in the request description.

---

# 11. Environment Variables

The Postman collection shall use API-15 variables.

Required variable groups:

| Group | Variables |
|---|---|
| Base | `base_url`, `api_version`, `environment_name`, `request_timeout_ms` |
| Authentication | `access_token`, `refresh_token`, `username`, `password`, `session_id` |
| Tenant | `organization_id`, `facility_id`, `site_id`, `unauthorized_organization_id`, `unauthorized_facility_id` |
| Traceability | `correlation_id`, `build_id`, `release_version` |
| Retry Safety | `idempotency_key`, `idempotency_key_replay`, `idempotency_key_conflict` |
| Concurrency | `etag`, `stale_etag`, `current_version` |
| Pagination | `page`, `page_size`, `cursor`, `limit` |
| Date Filters | `from_date`, `to_date` |
| Resource IDs | `customer_id`, `membership_id`, `attendance_id`, `invoice_id`, `payment_id`, `subscription_id`, `license_id`, `ticket_id` |
| Webhook | `webhook_secret`, `webhook_signature`, `webhook_timestamp`, `provider_event_id` |

---

# 12. Initial Setup Folder

The `00 Collection Setup` folder shall include:

| Request | Purpose |
|---|---|
| `SETUP-001 GET Health Check` | Validate API availability |
| `SETUP-002 POST Login` | Acquire JWT access and refresh token |
| `SETUP-003 GET Current User Context` | Validate authenticated identity and scope |
| `SETUP-004 GET Tenant Context` | Validate Organization, Facility, Site variables |
| `SETUP-005 POST Refresh Token` | Validate token refresh |
| `SETUP-006 POST Logout` | Validate logout and session invalidation |

Setup requests shall run before module folders in CI.

---

# 13. Module Folder Mapping

| Folder | Source Document | Request Source |
|---|---|---|
| 01 Platform Administration | API-01 | API-01 endpoint catalogue |
| 02 Organization Facility Site | API-02 | API-02 endpoint catalogue |
| 03 Identity User Role | API-03 | API-03 endpoint catalogue |
| 04 Customer Management | API-04 | API-04 endpoint catalogue |
| 05 Membership Management | API-05 | API-05 endpoint catalogue |
| 06 Attendance Walk-in | API-06 | API-06 endpoint catalogue |
| 07 Trainer Activity Batch | API-07 | API-07 endpoint catalogue |
| 08 Billing Payment | API-08 | API-08 endpoint catalogue |
| 09 Subscription License | API-09 | API-09 endpoint catalogue |
| 10 Notification Campaign | API-10 | API-10 endpoint catalogue |
| 11 Reports Analytics | API-11 | API-11 endpoint catalogue |
| 12 Support Ticket | API-12 | API-12 endpoint catalogue |
| 13 Audit Security | API-13 | API-13 endpoint catalogue |
| 14 Common Reference | API-14 | API-14 endpoint catalogue |

---

# 14. Request Description Template

Every request shall include a description using this structure:

```text
Endpoint ID:
Business Purpose:
Source Document:
FR Mapping:
Authentication:
Authorization:
Tenant Scope:
Required Headers:
Idempotency:
Concurrency:
Expected Success:
Expected Error Codes:
Database Mapping:
Audit Event:
Domain Event:
API-16 Test Scenarios:
```

---

# 15. Body Payload Rules

Request bodies shall:

- Use JSON.
- Use snake_case fields.
- Include only approved request fields.
- Use variables for resource identifiers.
- Use sample values safe for non-production execution.
- Avoid real PII, payment card data, secrets, and production references.
- Include positive-path and negative-path examples where useful.

Example:

```json
{
  "customer_id": "{{customer_id}}",
  "membership_plan_id": "{{membership_plan_id}}",
  "starts_at": "{{from_date}}",
  "source": "front_desk"
}
```

---

# 16. Pre-request Script Standards

Collection-level pre-request scripts may:

- Generate `correlation_id`.
- Generate `idempotency_key`.
- Validate that `base_url` is present.
- Validate that `api_version` is `v1`.
- Guard production execution.

Approved collection-level script pattern:

```javascript
if (!pm.environment.get("correlation_id")) {
  pm.environment.set("correlation_id", pm.variables.replaceIn("{{$guid}}"));
}

if (!pm.environment.get("api_version")) {
  pm.environment.set("api_version", "v1");
}

const envName = pm.environment.get("environment_name");
const baseUrl = pm.environment.get("base_url");

if (!baseUrl) {
  throw new Error("base_url is required");
}

if (envName === "production" && pm.environment.get("production_run_approved") !== "true") {
  throw new Error("Production collection run is not approved");
}
```

Request-level scripts may generate idempotency keys only when the request is retry-safe or the scenario explicitly requires it.

---

# 17. Test Script Standards

Every request shall include minimum assertions:

```javascript
pm.test("Status code is expected", function () {
  pm.expect(pm.response.code).to.be.oneOf([200, 201, 202, 204]);
});

pm.test("Response is JSON when body is present", function () {
  if (pm.response.text()) {
    pm.response.to.have.jsonBody();
  }
});

pm.test("Correlation ID is available", function () {
  const body = pm.response.text() ? pm.response.json() : {};
  const correlationId = body?.metadata?.correlation_id || pm.response.headers.get("X-Correlation-ID");
  pm.expect(correlationId).to.exist;
});
```

Error-path requests shall assert:

```javascript
pm.test("Error response follows API-00", function () {
  const body = pm.response.json();
  pm.expect(body.success).to.eql(false);
  pm.expect(body.error.error_code).to.be.a("string");
  pm.expect(body.error.message).to.be.a("string");
});
```

---

# 18. Response Capture Rules

| Captured Value | Source | Variable |
|---|---|---|
| Access token | Login response | `access_token` |
| Refresh token | Login response | `refresh_token` |
| ETag | Response header or body metadata | `etag` |
| Customer ID | Customer create/search response | `customer_id` |
| Membership ID | Membership create response | `membership_id` |
| Attendance ID | Check-in response | `attendance_id` |
| Invoice ID | Invoice create response | `invoice_id` |
| Payment ID | Payment create response | `payment_id` |
| Report Execution ID | Report request response | `report_execution_id` |
| Webhook Delivery ID | Webhook delivery response | `webhook_delivery_id` |

Captured values shall be scoped to the current environment and shall not be committed.

---

# 19. Negative Test Folder Pattern

Each module folder should include a `Negative Tests` subfolder where useful:

```text
05 Membership Management
├── Positive Flows
├── Lifecycle Flows
├── Search and History
└── Negative Tests
    ├── Missing Authorization
    ├── Forbidden Scope
    ├── Validation Failure
    ├── Idempotency Conflict
    └── Concurrency Conflict
```

Negative tests shall not mutate production data.

---

# 20. Auth and Tenant Isolation Test Requests

Required cross-cutting requests:

| Request | Expected Result |
|---|---|
| Missing JWT | `401 Unauthorized` |
| Invalid JWT | `401 Unauthorized` |
| Expired JWT | `401 Unauthorized` |
| Missing permission | `403 Forbidden` |
| Cross-tenant resource ID | `404` or `403` |
| Cross-tenant Organization header | Denied |
| Facility not in Organization | Hierarchy error or safe not found |
| Site not in Facility | Hierarchy error or safe not found |

---

# 21. Idempotency Test Requests

For endpoints requiring `Idempotency-Key`, the collection shall include:

| Request | Expected Result |
|---|---|
| First submission | Resource created or action completed |
| Replay same key and same payload | Replay-safe same result |
| Replay same key and different payload | `409` idempotency conflict |
| Missing key where required | API-19 idempotency error |

---

# 22. Concurrency Test Requests

For endpoints requiring `If-Match`, the collection shall include:

| Request | Expected Result |
|---|---|
| GET current resource | Captures `etag` |
| PATCH with current `etag` | Success |
| PATCH with `stale_etag` | `412 Precondition Failed` |
| PATCH without `If-Match` | Precondition error where required |

---

# 23. Pagination Test Requests

List endpoints shall include:

| Request | Expected Result |
|---|---|
| Default page | Default pagination metadata |
| Maximum page size | Accepted up to approved maximum |
| Exceeded page size | Validation or capped behavior |
| Approved sort | Sorted response |
| Unsupported sort | Validation error or documented behavior |
| Approved filter | Filtered response |
| Unsupported filter | Validation error or documented behavior |

---

# 24. Webhook Test Requests

The `18 Webhook Validation` folder shall include:

| Request | Purpose |
|---|---|
| Valid payment callback | Verify provider callback acceptance |
| Invalid signature callback | Verify rejection |
| Replay callback | Verify duplicate event handling |
| Expired timestamp callback | Verify replay-window rejection |
| Outbound delivery success simulation | Verify delivery success state |
| Outbound delivery retry simulation | Verify retry scheduling |
| Outbound delivery dead-letter simulation | Verify terminal failure state |

---

# 25. Error Code Validation Requests

The `19 Error Code Validation` folder shall validate:

- Authentication errors.
- Authorization errors.
- Validation errors.
- Tenant scope errors.
- Idempotency errors.
- Concurrency errors.
- Rate limit errors where safe to test.
- Webhook signature and replay errors.
- Provider failure simulations where supported.

Every error validation request shall assert the API-00 error envelope and an API-19 error code.

---

# 26. Newman Execution

Recommended Newman command pattern:

```bash
newman run Digitize_API_v1.postman_collection.json \
  --environment Digitize_API_v1.qa.environment.json \
  --reporters cli,json,junit \
  --reporter-json-export reports/digitize-api-v1-newman.json \
  --reporter-junit-export reports/digitize-api-v1-newman.xml
```

CI shall inject secrets at runtime and mask output.

---

# 27. CI/CD Collection Execution

| Pipeline Stage | Collection Scope | Required |
|---|---|---|
| Pull Request | Setup, changed-module smoke, contract checks | Yes |
| Development Merge | Setup, module positive/negative tests | Yes |
| QA Regression | Full API-01 to API-14 collection | Yes |
| Release Candidate | Full collection plus webhook/error/change governance checks | Yes |
| Production Smoke | Read-only health and critical safe GET requests | Yes |

---

# 28. Collection Export Rules

Before committing or sharing exported collection files:

- Remove access tokens.
- Remove refresh tokens.
- Remove passwords.
- Remove provider secrets.
- Remove production tenant IDs.
- Remove real customer PII.
- Replace environment-specific values with variables.
- Confirm generated examples are synthetic.

---

# 29. Versioning Rules

| Artifact | Version Rule |
|---|---|
| Collection | Follows API version and document version |
| Request | Request name includes endpoint ID |
| Environment template | Updated when API-15 variables change |
| Test script | Updated when API-16 scenarios change |
| Error assertion | Updated when API-19 changes |
| Webhook request | Updated when API-18 changes |

---

# 30. Traceability Rules

Every request shall map to:

- API document.
- Endpoint ID.
- FR mapping where available.
- API-16 scenario IDs.
- API-17 traceability row.
- API-19 error codes for negative paths.
- API-20 change record when behavior changes.

---

# 31. Review Checklist

| Check | Required |
|---|---|
| Folder structure matches API numbering | Yes |
| Request names include endpoint IDs | Yes |
| URLs use `{{base_url}}/api/{{api_version}}` | Yes |
| No hard-coded secrets | Yes |
| Tenant headers are explicit | Yes |
| Idempotency keys used where required | Yes |
| `If-Match` used where required | Yes |
| API-00 response tests included | Yes |
| API-19 error tests included | Yes for negative tests |
| API-16 scenario mapping documented | Yes |
| Production execution guarded | Yes |

---

# 32. Assumptions and Constraints

- This document defines the Postman blueprint, not the generated JSON export.
- API implementation may not yet exist for every documented endpoint.
- Test data is synthetic unless production smoke tests are explicitly approved.
- Exact performance thresholds are governed outside this document.
- Provider callbacks require provider-specific integration details before executable callback tests are finalized.

---

# 33. Acceptance Criteria

This document is acceptable when:

- The collection folder structure maps to API-01 through API-26.
- Request naming, URLs, headers, variables, scripts, and tests are standardized.
- Environment usage aligns with API-15.
- Test coverage aligns with API-16.
- Traceability aligns with API-17.
- Webhook validation aligns with API-18.
- Error validation aligns with API-19.
- Change governance aligns with API-20.
- OpenAPI governance aligns with API-21.
- Frontend consumption aligns with API-22.
- Access control aligns with API-23.
- State and workflow behavior aligns with API-24.
- Mock and sandbox readiness aligns with API-25.
- Release readiness aligns with API-26.

---

# 34. Summary

Postman_Collection.md defines the execution blueprint for the Digitize API v1 Postman collection. It turns the API documentation set into a governed collection structure that can later be exported as executable Postman JSON and run safely through Newman or compatible CI tooling.
