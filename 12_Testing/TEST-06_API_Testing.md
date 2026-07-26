# TEST-06 API Testing

> REST API, contract, OpenAPI, Postman, authentication, authorization, tenant, payload, error, and workflow testing for Digitize APIs.

---

# Document Control

| Field | Value |
|---|---|
| Document ID | TEST-06 |
| Document Name | API Testing |
| Folder | 12_Testing |
| Product | Digitize by OrieOn Technologies Pvt. Ltd. |
| Status | Frozen (provisional) |
| Owner | QA / API Test Engineering |
| Reviewers | API Architecture, Backend Engineering, Security, Integration, DevOps, Release Management |
| Version | 1.0 |
| Last Updated | 2026-07-24 |

| Freeze Date | 2026-07-26 |
| Freeze Note | Freeze initiated (provisional). Approvals to be recorded in the freeze PR. |

---

# 1. Purpose

This document defines API testing standards for Digitize REST APIs.

It verifies approved API contracts, payloads, authentication, authorization, tenant context, error behavior, state workflows, mocks, OpenAPI alignment, and Postman governance.

---

# 2. Scope

This document covers:

- REST API testing.
- Contract testing.
- OpenAPI validation.
- Postman collection governance.
- Authentication testing.
- Authorization testing.
- Tenant-context testing.
- Payload and schema testing.
- Error response testing.
- Workflow and state testing.
- API regression and smoke testing.

---

# 3. Out of Scope

This document does not define:

- API endpoint catalogues.
- OpenAPI contract ownership.
- Backend controller implementation.
- Business requirements.
- Deployment execution.

API contract ownership remains in `07_API_Collections/`.

---

# 4. Governing Standard

This document inherits `TEST-00_Testing_Standards.md`.

It shall not redefine API contracts already governed by API Collections.

---

# 5. Source Alignment

| Source Area | Alignment |
|---|---|
| TEST-00 | API traceability, evidence, defect, and quality gate standards |
| API Collections | Approved endpoints, payloads, errors, access control, states, mocks, OpenAPI, Postman |
| Backend Engineering | API implementation, validation, auth, tenant, errors, and release readiness |
| Integration Contracts | API behavior consumed by integrations |
| Security | Authentication, authorization, tenant isolation, and sensitive data handling |
| Deployment | Environment and release artifact readiness |

---

# 6. API Test Scope

API testing shall cover:

- HTTP method and route behavior.
- Request payload validation.
- Query parameter validation.
- Path parameter validation.
- Response payload shape.
- Status codes.
- Error response format.
- Authentication requirement.
- Authorization enforcement.
- Tenant-context enforcement.
- Pagination, filtering, sorting where applicable.
- Idempotency where applicable.
- State transitions.
- Rate or throttling behavior where approved.

---

# 7. Contract and OpenAPI Validation

API tests shall verify:

- Implemented routes match approved contracts.
- Required fields are enforced.
- Optional fields behave as documented.
- Response fields match approved schemas.
- Error structures match approved API standards.
- OpenAPI documentation matches implementation where applicable.
- Breaking changes are identified before release recommendation.

Contract failures shall be assessed as release-impacting unless explicitly accepted.

---

# 8. Authentication and Authorization Testing

API security testing shall verify:

- Unauthenticated requests are rejected.
- Invalid tokens are rejected.
- Expired tokens are rejected.
- Valid tokens are accepted.
- Role permissions are enforced.
- Resource-level authorization is enforced.
- Cross-tenant access is denied.
- Administrative overrides are controlled where applicable.

Security-sensitive test evidence shall not expose tokens or credentials.

---

# 9. Postman Governance

Postman or equivalent API collections shall define:

- Collection version.
- Environment variables.
- Authentication setup without secret values.
- Request examples.
- Positive tests.
- Negative tests.
- Contract assertions.
- Error assertions.
- Tenant-context assertions.
- Collection execution evidence.

Postman collections shall not contain production secrets.

---

# 10. Evidence

API testing evidence shall include:

- API document reference.
- Endpoint or collection reference.
- Test environment.
- Request identifier.
- Test data scope.
- Response result.
- Assertion result.
- Defect reference where failed.
- Automation run reference where applicable.

Sensitive headers, tokens, passwords, and secret values shall be redacted.

---

# 11. Acceptance Criteria

This document is acceptable when:

- API test scope is defined.
- Contract and OpenAPI validation are covered.
- Authentication and authorization testing are documented.
- Tenant-context testing is covered.
- Postman governance is defined.
- Evidence expectations are documented.
- No rule contradicts API Collections, Backend Engineering, Security, or `TEST-00`.

---

# 12. Freeze Rule

This document shall remain `Design Draft` until `TEST-00` is reviewed and API testing is aligned with approved API Collections.
