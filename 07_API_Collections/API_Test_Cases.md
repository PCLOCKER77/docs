# (status banner removed to preserve metadata `Status: Design Draft`)
# API Test Cases

**Document Name:** API Test Cases  
**Company:** OreeOn Technologies Pvt. Ltd.  
**Product:** Digitize  
**Document Type:** API Test Case Documentation  
**Backend Technology:** FastAPI  
**Database Engine:** PostgreSQL  
**Authentication:** JWT  
**API Version:** v1  
**Document Version:** 0.1  
**Status:** Design Draft  
**Owner:** QA / API Architecture  
**Reviewer:** Solution Architecture / Security Architecture / Backend Engineering / DevOps  
**Dependencies:** API-00 to API-26, Postman_Collection.md  
**Last Updated:** 2026-07-26

---

# 1. Document Metadata

| Attribute | Value |
|---|---|
| Document Name | API Test Cases |
| Output File | API_Test_Cases.md |
| API Version | v1 |
| Document Version | 0.1 |
| Status | Design Draft |
| Governing Standards | API-00, API-15, API-16, API-17, API-19, API-26 |

---

# 2. Purpose

This document defines the executable API test case baseline for Digitize API v1.

It converts the reusable scenario standards in API-16 into test case groups that QA, backend engineering, security, DevOps, and frontend teams can use for manual validation, Postman/Newman execution, automated regression, release readiness, and consumer readiness.

---

# 3. Scope

In scope:

- Cross-cutting API test cases for authentication, authorization, tenant isolation, validation, response contracts, error contracts, pagination, idempotency, concurrency, lifecycle, async, webhook, security, and release readiness.
- Module-level test coverage for API-01 through API-14.
- Governance test coverage for API-15 through API-26.
- Postman/Newman execution alignment.
- Test evidence and readiness mapping.

Out of scope:

- Unit test source code.
- UI automation scripts.
- Load test scripts.
- Real production credentials or production test data.
- Vendor-specific provider certification tests.

---

# 4. Test Case Principles

| Principle | Standard |
|---|---|
| Scenario-backed | Every test case shall map to API-16 where applicable |
| Contract-first | Assertions shall validate API-00 envelopes and standards |
| Tenant-safe | Tests shall prove Organization, Facility, and Site isolation |
| Error-code driven | Negative tests shall assert API-19 error codes |
| Repeatable | Tests shall use API-15 variables and synthetic data |
| Traceable | Test cases shall map to API-17 rows |
| Release-aware | Release readiness shall map to API-26 |
| Automation-ready | Test cases shall be runnable through Postman/Newman or an approved runner |

---

# 5. Test Case ID Format

Format:

```text
TC-API-{AREA}-{NNN}
```

Examples:

```text
TC-API-AUTH-001
TC-API-TEN-001
TC-API-MEM-001
TC-API-WHK-001
```

Rules:

- Test case IDs shall not be reused.
- Retired test case IDs shall remain in history.
- Module test cases shall use a short area code aligned to the API document.
- Cross-cutting test cases shall use API-16 scenario families.

---

# 6. Test Environment Requirements

| Requirement | Source | Required |
|---|---|---|
| API environment variables | API-15 | Yes |
| JWT test users | API-03, API-23 | Yes |
| Tenant test data | API-02, API-25 | Yes |
| Positive and negative resource IDs | API-15, API-25 | Yes |
| Postman/Newman collection | Postman_Collection.md | Conditional |
| Mock/sandbox responses | API-25 | Conditional |
| Error code catalog | API-19 | Yes |
| Readiness checklist | API-26 | Yes |

---

# 7. Test Data Baseline

| Test Data | Required State |
|---|---|
| Organization A | ACTIVE |
| Organization B | ACTIVE and unauthorized to Organization A users |
| Facility A1 | ACTIVE |
| Site A1S1 | ACTIVE |
| Customer Active | ACTIVE |
| Customer Suspended | SUSPENDED |
| Membership Active | ACTIVE |
| Membership Pending Payment | PENDING_PAYMENT |
| Membership Frozen | FROZEN |
| Membership Expired | EXPIRED |
| Attendance Active | CHECKED_IN |
| Invoice Issued | ISSUED |
| Payment Success | SUCCESS |
| Subscription Active | ACTIVE |
| License Active | LICENSE_ACTIVE |
| Campaign Draft | DRAFT |
| Support Ticket Open | OPEN |
| Report Execution Pending | PENDING |

---

# 8. Common Preconditions

Unless the test case says otherwise:

- Target environment is non-production.
- `base_url` and `api_version` are configured.
- User has a valid JWT.
- `X-Correlation-ID` is supplied or generated.
- Tenant context variables are present.
- Test data belongs to the intended Organization, Facility, and Site.
- Secrets and tokens are masked in logs and reports.

---

# 9. Common Expected Results

Every test case shall validate:

- Expected HTTP status.
- API-00 response envelope.
- Stable API-19 error code for negative cases.
- Correlation ID traceability.
- Tenant-scoped data only.
- No secret or sensitive data leakage.
- Audit/event behavior where required.
- Test evidence captured with scenario ID and endpoint ID.

---

# 10. Authentication Test Cases

| Test Case ID | API-16 Scenario | Test Case | Expected Result |
|---|---|---|---|
| TC-API-AUTH-001 | API-16-AUTH-001 | Call protected endpoint without `Authorization` header | `401` API authentication error |
| TC-API-AUTH-002 | API-16-AUTH-002 | Call protected endpoint with invalid token signature | `401` API authentication error |
| TC-API-AUTH-003 | API-16-AUTH-003 | Call protected endpoint with expired access token | `401` or refresh flow where approved |
| TC-API-AUTH-004 | API-16-AUTH-004 | Use revoked session token | `401` and no business action |
| TC-API-AUTH-005 | API-16-AUTH-005 | Use valid JWT with correct issuer and audience | Request proceeds to authorization |
| TC-API-AUTH-006 | API-16-AUTH-006 | Execute login happy path | Access token returned using API-03 contract |
| TC-API-AUTH-007 | API-16-AUTH-007 | Logout then reuse token | Reuse rejected |

---

# 11. Authorization Test Cases

| Test Case ID | API-16 Scenario | Test Case | Expected Result |
|---|---|---|---|
| TC-API-AZ-001 | API-16-AZ-001 | User lacks endpoint permission | `403` or approved safe denial |
| TC-API-AZ-002 | API-16-AZ-002 | User has role but wrong scope | `403` or safe `404` |
| TC-API-AZ-003 | API-16-AZ-003 | Non-platform user calls platform-only endpoint | `403` |
| TC-API-AZ-004 | API-16-AZ-004 | User reads financial data without permission | Denied or masked |
| TC-API-AZ-005 | API-16-AZ-005 | User exports audit data without export permission | Denied and audited |
| TC-API-AZ-006 | API-16-AZ-006 | Authorized user performs allowed action | Success response |

---

# 12. Tenant Isolation Test Cases

| Test Case ID | API-16 Scenario | Test Case | Expected Result |
|---|---|---|---|
| TC-API-TEN-001 | API-16-TEN-001 | Organization A token requests Organization B resource | Safe `404` or `403` |
| TC-API-TEN-002 | API-16-TEN-002 | Organization A token sends Organization B header | Request denied |
| TC-API-TEN-003 | API-16-TEN-003 | Facility does not belong to Organization header | Hierarchy error or safe denial |
| TC-API-TEN-004 | API-16-TEN-004 | Site does not belong to Facility header | Hierarchy error or safe denial |
| TC-API-TEN-005 | API-16-TEN-005 | Search as Organization A | No Organization B data returned |
| TC-API-TEN-006 | API-16-TEN-006 | Export as Organization A | Export contains only Organization A data |

---

# 13. Validation Test Cases

| Test Case ID | API-16 Scenario | Test Case | Expected Result |
|---|---|---|---|
| TC-API-VAL-001 | API-16-VAL-001 | Submit missing required field | `422` validation error |
| TC-API-VAL-002 | API-16-VAL-002 | Submit invalid UUID | `422` validation error |
| TC-API-VAL-003 | API-16-VAL-003 | Submit invalid enum/reference value | `422` validation error |
| TC-API-VAL-004 | API-16-VAL-004 | Submit invalid date range | `422` validation error |
| TC-API-VAL-005 | API-16-VAL-005 | Submit unsupported content type | `415` error |
| TC-API-VAL-006 | API-16-VAL-006 | Attempt immutable field update | Validation error |
| TC-API-VAL-007 | API-16-VAL-007 | Submit oversized payload | Payload-size or validation error |

---

# 14. Response Contract Test Cases

| Test Case ID | API-16 Scenario | Test Case | Expected Result |
|---|---|---|---|
| TC-API-RSP-001 | API-16-RSP-001 | Create endpoint success | `201`, envelope, resource identifier |
| TC-API-RSP-002 | API-16-RSP-002 | Read endpoint success | `200`, envelope |
| TC-API-RSP-003 | API-16-RSP-003 | Lifecycle endpoint success | `200`, resulting state |
| TC-API-RSP-004 | API-16-RSP-004 | Async endpoint accepted | `202`, status reference |
| TC-API-RSP-005 | API-16-RSP-005 | Error response | API-00 error envelope |
| TC-API-RSP-006 | API-16-RSP-006 | Client supplies correlation ID | Same or traceable ID returned |
| TC-API-RSP-007 | API-16-RSP-007 | Client omits correlation ID | Server-generated or traceable ID returned |

---

# 15. Pagination, Filtering, Sorting, and Search Test Cases

| Test Case ID | API-16 Scenario | Test Case | Expected Result |
|---|---|---|---|
| TC-API-PAGE-001 | API-16-PAGE-001 | Request default page | Default metadata returned |
| TC-API-PAGE-002 | API-16-PAGE-002 | Request maximum page size | Maximum accepted |
| TC-API-PAGE-003 | API-16-PAGE-003 | Exceed maximum page size | Validation or capped response |
| TC-API-PAGE-004 | API-16-PAGE-004 | Request cursor first page | Cursor metadata returned |
| TC-API-PAGE-005 | API-16-PAGE-005 | Request cursor next page | Stable continuation |
| TC-API-FILTER-001 | API-16-FILTER-001 | Use approved filter | Correct subset returned |
| TC-API-FILTER-002 | API-16-FILTER-002 | Use unsupported filter | Validation or documented behavior |
| TC-API-SORT-001 | API-16-SORT-001 | Use approved sort | Correct order returned |
| TC-API-SEARCH-001 | API-16-SEARCH-001 | Search below minimum length | Validation or empty result |
| TC-API-SEARCH-002 | API-16-SEARCH-002 | Sensitive search without permission | Denied or masked |

---

# 16. Idempotency Test Cases

| Test Case ID | API-16 Scenario | Test Case | Expected Result |
|---|---|---|---|
| TC-API-IDEMP-001 | API-16-IDEMP-001 | Create with new idempotency key | Resource created |
| TC-API-IDEMP-002 | API-16-IDEMP-002 | Replay same key and same payload | Replay-safe result |
| TC-API-IDEMP-003 | API-16-IDEMP-003 | Replay same key with different payload | `409` idempotency conflict |
| TC-API-IDEMP-004 | API-16-IDEMP-004 | Omit required idempotency key | API-19 idempotency error |
| TC-API-IDEMP-005 | API-16-IDEMP-005 | Reuse key across tenant scope | Tenant-safe conflict handling |
| TC-API-IDEMP-006 | API-16-IDEMP-006 | Duplicate provider event ID | Duplicate ignored or replay-safe |

---

# 17. Optimistic Concurrency Test Cases

| Test Case ID | API-16 Scenario | Test Case | Expected Result |
|---|---|---|---|
| TC-API-CON-001 | API-16-CON-001 | Update with current `If-Match` | Success |
| TC-API-CON-002 | API-16-CON-002 | Update with stale `If-Match` | `412` |
| TC-API-CON-003 | API-16-CON-003 | Update without required `If-Match` | Precondition error |
| TC-API-CON-004 | API-16-CON-004 | Lifecycle action with stale version | No state change |
| TC-API-CON-005 | API-16-CON-005 | Concurrent update pair | One succeeds, one fails safely |

---

# 18. Lifecycle Test Cases

| Test Case ID | API Area | Test Case | Expected Result |
|---|---|---|---|
| TC-API-LIFE-001 | API-02 | Activate, suspend, and archive Organization/Facility/Site | Valid transitions only |
| TC-API-LIFE-002 | API-04 | Register, suspend, reactivate, archive customer | Valid customer lifecycle |
| TC-API-LIFE-003 | API-05 | Create, activate, renew, freeze, resume, cancel, expire membership | Valid membership state machine |
| TC-API-LIFE-004 | API-06 | Check-in, check-out, update, cancel attendance | Valid attendance lifecycle |
| TC-API-LIFE-005 | API-07 | Schedule, start, complete, cancel session | Valid training/session state |
| TC-API-LIFE-006 | API-08 | Invoice, payment, refund, reconcile, cancel | Valid financial state |
| TC-API-LIFE-007 | API-09 | Activate, renew, suspend, cancel, expire subscription/license | Valid commercial control |
| TC-API-LIFE-008 | API-10 | Submit, approve, schedule, launch, pause, archive campaign/notification | Valid communication lifecycle |
| TC-API-LIFE-009 | API-12 | Create, classify, assign, escalate, resolve, close, reopen ticket | Valid ticket lifecycle |
| TC-API-LIFE-010 | API-13 | Open investigation, export audit, archive records | Valid audit workflow |

---

# 19. Asynchronous Operation Test Cases

| Test Case ID | API-16 Scenario | Test Case | Expected Result |
|---|---|---|---|
| TC-API-ASYNC-001 | API-16-ASYNC-001 | Request report execution | `202`, execution ID |
| TC-API-ASYNC-002 | API-16-ASYNC-002 | Poll pending operation | Pending/running status |
| TC-API-ASYNC-003 | API-16-ASYNC-003 | Poll completed operation | Completed with result reference |
| TC-API-ASYNC-004 | API-16-ASYNC-004 | Poll failed operation | Failed with safe error |
| TC-API-ASYNC-005 | API-16-ASYNC-005 | Export completion | Export metadata and audit |
| TC-API-ASYNC-006 | API-16-ASYNC-006 | Notification retry | Retry attempt recorded |
| TC-API-ASYNC-007 | API-16-ASYNC-007 | Webhook delivery retry | Attempt count/status recorded |

---

# 20. Webhook Test Cases

| Test Case ID | API-16 Scenario | Test Case | Expected Result |
|---|---|---|---|
| TC-API-WHK-001 | API-16-WHK-001 | Valid inbound callback signature | Accepted |
| TC-API-WHK-002 | API-16-WHK-002 | Invalid callback signature | Rejected |
| TC-API-WHK-003 | API-16-WHK-003 | Timestamp outside replay window | Rejected |
| TC-API-WHK-004 | API-16-WHK-004 | Duplicate provider event ID | Replay-safe handling |
| TC-API-WHK-005 | API-16-WHK-005 | Outbound delivery success | Delivered |
| TC-API-WHK-006 | API-16-WHK-006 | Outbound transient failure | Retry scheduled |
| TC-API-WHK-007 | API-16-WHK-007 | Exhaust outbound retries | Dead-letter state |

---

# 21. Security and Privacy Test Cases

| Test Case ID | API-16 Scenario | Test Case | Expected Result |
|---|---|---|---|
| TC-API-SEC-001 | API-16-SEC-001 | Submit SQL-like input | No SQL/stack leakage |
| TC-API-SEC-002 | API-16-SEC-002 | Read PII without permission | Masked or denied |
| TC-API-SEC-003 | API-16-SEC-003 | Submit raw payment card data | Rejected or ignored per API-08 |
| TC-API-SEC-004 | API-16-SEC-004 | Inspect response/loggable data | No token leakage |
| TC-API-SEC-005 | API-16-SEC-005 | Export sensitive report without permission | Denied and audited |
| TC-API-SEC-006 | API-16-SEC-006 | Administrative cross-tenant access | Access record required |

---

# 22. Module Test Coverage Matrix

| API Document | Test Case Group | Minimum Cases |
|---|---|---|
| API-01 | TC-API-PLT | Platform settings, feature flags, maintenance, release, health |
| API-02 | TC-API-TEN | Organization, Facility, Site hierarchy and lifecycle |
| API-03 | TC-API-IDN | Login, refresh, logout, user, role, permission, session |
| API-04 | TC-API-CUS | Customer create, update, search, transfer, lifecycle, history |
| API-05 | TC-API-MEM | Membership create, activate, renew, freeze, resume, cancel, expire |
| API-06 | TC-API-ATT | Eligibility, check-in, check-out, walk-in, capacity, history |
| API-07 | TC-API-TRN | Trainer, activity, batch, session, enrollment, notes, progress |
| API-08 | TC-API-BIL | Invoice, charge, discount, tax, payment, refund, reconciliation |
| API-09 | TC-API-SUB | Subscription, license, entitlement, feature access |
| API-10 | TC-API-COM | Campaign, notification, consent, delivery, retry |
| API-11 | TC-API-RPT | Dashboard, reports, exports, KPI, schedules |
| API-12 | TC-API-SUP | Ticket create, assign, escalate, resolve, close, reopen |
| API-13 | TC-API-AUD | Audit events, security events, investigations, compliance export |
| API-14 | TC-API-REF | Reference lists, lookup values, cache behavior |

---

# 23. Governance Test Coverage Matrix

| API Document | Test Case Group | Minimum Cases |
|---|---|---|
| API-15 | TC-API-ENV | Environment variables, secrets masking, tenant context |
| API-16 | TC-API-SCN | Scenario ID coverage and expected-result consistency |
| API-17 | TC-API-TRC | Endpoint-to-requirement/test traceability completeness |
| API-18 | TC-API-WHK | Webhook signature, replay, retry, dead-letter |
| API-19 | TC-API-ERR | Error code format, HTTP mapping, safe messages |
| API-20 | TC-API-CHG | Change type, compatibility, approval, migration |
| API-21 | TC-API-OAS | OpenAPI operation IDs, tags, schemas, breaking-change scan |
| API-22 | TC-API-FE | Frontend token, tenant, retry, error, pagination behavior |
| API-23 | TC-API-ACL | Role/permission/scope/action visibility |
| API-24 | TC-API-WFL | State transitions and forbidden actions |
| API-25 | TC-API-MOCK | Mock/sandbox success, error, empty, async, payment, webhook |
| API-26 | TC-API-READY | Readiness checklist completion |

---

# 24. Release Readiness Test Cases

| Test Case ID | Source | Test Case | Expected Result |
|---|---|---|---|
| TC-API-READY-001 | API-26 | Verify API document exists and is Design Draft or higher | Pass |
| TC-API-READY-002 | API-26 | Verify OpenAPI schema is published or mock contract approved | Pass or waiver |
| TC-API-READY-003 | API-26 | Verify authentication and permissions are configured | Pass |
| TC-API-READY-004 | API-26 | Verify tenant isolation tests pass | Pass |
| TC-API-READY-005 | API-26 | Verify error codes finalized | Pass |
| TC-API-READY-006 | API-26 | Verify mocks/test data available | Pass |
| TC-API-READY-007 | API-26 | Verify frontend integration tested where applicable | Pass or deferred |
| TC-API-READY-008 | API-26 | Verify API-20 change records are complete | Pass |

---

# 25. Postman/Newman Execution Mapping

| Postman Folder | Test Case Mapping |
|---|---|
| 00 Collection Setup | TC-API-AUTH, TC-API-ENV |
| 01 to 14 Module Folders | Module groups TC-API-PLT through TC-API-REF |
| 15 Environment Validation | TC-API-ENV |
| 16 Reusable Test Scenarios | TC-API-AUTH through TC-API-SEC |
| 17 Traceability Checks | TC-API-TRC |
| 18 Webhook Validation | TC-API-WHK |
| 19 Error Code Validation | TC-API-ERR |
| 20 Change Governance Checks | TC-API-CHG |
| 21 to 26 Bridge Checks | TC-API-OAS, TC-API-FE, TC-API-ACL, TC-API-WFL, TC-API-MOCK, TC-API-READY |

---

# 26. Test Evidence Requirements

| Evidence | Required |
|---|---|
| Test case ID | Yes |
| API-16 scenario ID | Conditional |
| Endpoint ID | Conditional |
| API document | Yes |
| Environment | Yes |
| Tenant scope | Yes for tenant APIs |
| User/role profile | Yes for authorization tests |
| Request correlation ID | Yes |
| HTTP status | Yes |
| Error code | Yes for negative tests |
| Result | Yes |
| Defect reference | Conditional |
| Waiver reference | Conditional |

---

# 27. Defect Severity Guidance

| Severity | Examples |
|---|---|
| Critical | Tenant isolation failure, auth bypass, financial state corruption, audit failure |
| High | Lifecycle state error, payment/refund error, restricted data exposure |
| Medium | Validation mismatch, pagination defect, error code mismatch |
| Low | Documentation mismatch, cosmetic response example issue |

---

# 28. Governance Controls

- New endpoints require positive, validation, authorization, and tenant tests before Frozen — 2026-07-26.
- New lifecycle actions require state, idempotency, concurrency, audit, and notification tests where applicable.
- New webhook events require signature, replay, retry, and dead-letter tests.
- New frontend workflows require API-22, API-23, API-24, and API-25 coverage.
- Release readiness requires API-26 checks.

---

# 29. Assumptions and Constraints

- Exact executable scripts may be implemented in Postman/Newman, pytest, or another approved runner.
- Test data is synthetic or masked outside production.
- Some provider integration tests require sandbox provider availability.
- Performance thresholds are pending final SLO approval.

---

# 30. Acceptance Criteria

This document is acceptable when:

- API-16 scenarios are represented as executable test case groups.
- API-01 through API-14 module documents have coverage groups.
- API-15 through API-26 governance documents have validation groups.
- Postman/Newman execution can map requests to test case IDs.
- API-26 readiness gates can consume test evidence.

---

# 31. Summary

API_Test_Cases.md defines the executable test case baseline for Digitize API v1. It bridges API-16 scenario design, Postman/Newman execution, module API contracts, governance documents, and release readiness evidence.
