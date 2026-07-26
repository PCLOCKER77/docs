# (status banner removed to preserve metadata `Status: Design Draft`)
# API-15 API Environment and Variables

**Document ID:** API-15  
**Document Name:** API Environment and Variables  
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
**Reviewer:** Solution Architecture / Security Architecture / Backend Engineering / DevOps / QA  
**Dependencies:** API-00, API-01 to API-14, API-16, API-17, API-19, DevOps, QA  
**Last Updated:** 2026-07-26

---

# 1. Document Metadata

| Attribute | Value |
|---|---|
| Document ID | API-15 |
| Document Name | API Environment and Variables |
| Output File | API-15_API_Environment_and_Variables.md |
| API Version | v1 |
| Document Version | 0.1 |
| Status | Design Draft |
| Governing Standard | API-00_API_Collection_Standards.md |

---

# 2. Purpose

This document defines the controlled API environment and variable strategy for Digitize API execution, testing, automation, and CI/CD.

It governs environment profiles, collection variables, tenant context variables, authentication variables, pagination variables, idempotency variables, concurrency variables, webhook variables, secret handling, pre-request scripts, test execution, reporting, and review controls.

---

# 3. Scope

In scope:

- Local, development, QA, staging, sandbox, production, and CI API environment profiles.
- Variable naming, ownership, data classification, source, defaulting, mutation, and reset rules.
- Authentication, tenant context, idempotency, correlation, pagination, filtering, sorting, and concurrency variables.
- Secure handling of credentials, JWTs, refresh tokens, provider secrets, webhook secrets, and payment references.
- Postman or compatible API client environment conventions.
- CI/CD collection execution and masked reporting.
- Environment review and promotion controls.

Out of scope:

- Infrastructure provisioning code.
- Deployment manifests.
- FastAPI runtime configuration source code.
- Database migration environment variables.
- Production secret values.
- OpenAPI generation.

---

# 4. Business Context

Digitize APIs are tenant-aware and scope-sensitive. A test or implementation environment that mixes tenant variables, stale tokens, production secrets, or incorrect base URLs can create false test results and security exposure.

API environments must therefore be deterministic, secure, reviewable, and compatible with automated contract testing.

---

# 5. Environment Principles

| Principle | Standard |
|---|---|
| Explicit environment | Every collection run shall identify the target environment |
| No production leakage | Production secrets and tenant records shall not be copied into lower environments |
| Tenant clarity | Organization, Facility, and Site variables shall be visible and controlled |
| Secret minimization | Secrets shall be injected from approved secret stores where possible |
| Repeatability | CI runs shall be repeatable and deterministic |
| Safe logging | Tokens, passwords, provider secrets, and sensitive references shall be masked |
| Contract alignment | Environment variables shall support API-00 response, error, and traceability assertions |

---

# 6. Environment Profiles

| Environment | Purpose | Base URL Variable | Data Classification | Owner | Usage |
|---|---|---|---|---|---|
| Local | Developer-local API execution | `base_url` | Synthetic | Backend Engineering | Developer testing |
| Development | Shared integration development | `base_url` | Synthetic / Internal | DevOps / Backend | Feature integration |
| QA | Functional and regression testing | `base_url` | Synthetic / Masked | QA | Test execution |
| Staging | Release candidate validation | `base_url` | Masked / Controlled | DevOps / Release | Release readiness |
| Sandbox | Partner or demo testing | `base_url` | Controlled | Product / Implementation | Non-production demos |
| Production | Live service | `base_url` | Production | Operations | Controlled operational use |
| CI | Automated pipeline run | `base_url` | Synthetic / Masked | DevOps / QA | Contract automation |

---

# 7. Base Environment Variables

| Variable | Required | Example | Owner | Notes |
|---|---|---|---|---|
| `base_url` | Yes | `https://api.qa.digitize.example` | DevOps | No trailing slash |
| `api_version` | Yes | `v1` | API Architecture | Used in `/api/{{api_version}}` |
| `request_timeout_ms` | Yes | `30000` | QA / DevOps | CI may use stricter timeouts |
| `retry_count` | Conditional | `2` | QA / DevOps | For retry-safe operations only |
| `environment_name` | Yes | `qa` | DevOps | Must match approved profile |
| `client_name` | Conditional | `postman-ci` | QA | Helps audit and observability |
| `build_id` | Conditional | `CI-12345` | DevOps | Required in CI |
| `release_version` | Conditional | `v1.0.0-rc1` | Release | Required in staging release runs |

---

# 8. Authentication Variables

| Variable | Required | Classification | Source | Reset Rule |
|---|---|---|---|---|
| `access_token` | Yes for authenticated APIs | Secret | Login flow or secret store | Refresh before expiry |
| `refresh_token` | Conditional | Secret | Login flow | Rotate and mask |
| `username` | Conditional | Secret | Secret store or local private env | Do not commit |
| `password` | Conditional | Secret | Secret store or local private env | Do not commit |
| `mfa_code` | Conditional | Secret | Authenticator / test provider | Never persist |
| `service_client_id` | Conditional | Secret | Secret store | CI and internal calls |
| `service_client_secret` | Conditional | Secret | Secret store | CI and internal calls |
| `token_expiry_at` | Conditional | Confidential | Pre-request script | Recomputed on login |
| `session_id` | Conditional | Confidential | API-03 response | Reset on logout |

---

# 9. Tenant Context Variables

| Variable | Required | Applies To | Validation Rule |
|---|---|---|---|
| `organization_id` | Yes | Tenant APIs | Must represent an authorized Organization |
| `facility_id` | Conditional | Facility APIs | Must belong to `organization_id` |
| `site_id` | Conditional | Site APIs | Must belong to `facility_id` |
| `target_organization_id` | Conditional | Transfer/admin tests | Must be explicitly authorized |
| `target_facility_id` | Conditional | Transfer/admin tests | Must be explicitly authorized |
| `target_site_id` | Conditional | Transfer/admin tests | Must be explicitly authorized |
| `unauthorized_organization_id` | Required for isolation tests | Negative tests | Must not be accessible to the current token |
| `unauthorized_facility_id` | Required for isolation tests | Negative tests | Must not be accessible to the current token |

Tenant context variables are request context only. They shall never be treated as proof of authorization.

---

# 10. Header Variable Mapping

| HTTP Header | Variable | Required | Notes |
|---|---|---|---|
| `Authorization` | `access_token` | Yes | Format: `Bearer {{access_token}}` |
| `Accept` | Static | Yes | `application/json` |
| `Content-Type` | Static | Conditional | Required for request bodies |
| `X-Correlation-ID` | `correlation_id` | Required or generated | UUID recommended |
| `X-Organization-ID` | `organization_id` | Yes for tenant APIs | Scope request |
| `X-Facility-ID` | `facility_id` | Conditional | Facility scope |
| `X-Site-ID` | `site_id` | Conditional | Site scope |
| `Idempotency-Key` | `idempotency_key` | Conditional | Create/lifecycle/payment/retry actions |
| `If-Match` | `etag` | Conditional | Protected updates/actions |

---

# 11. Resource Identifier Variables

| Variable | Resource | Source Document | Notes |
|---|---|---|---|
| `platform_setting_id` | Platform Setting | API-01 | Platform scope |
| `organization_resource_id` | Organization | API-02 | Tenant hierarchy |
| `user_id` | User Account | API-03 | Identity scope |
| `customer_id` | Customer | API-04 | Customer scope |
| `membership_id` | Customer Membership | API-05 | Membership lifecycle |
| `attendance_id` | Attendance | API-06 | Operational record |
| `walkin_visit_id` | Walk-in Visit | API-06 | Walk-in flow |
| `trainer_id` | Trainer | API-07 | Training scope |
| `batch_id` | Batch | API-07 | Batch flow |
| `session_id` | Class or Training Session | API-07 | Schedule flow |
| `invoice_id` | Invoice | API-08 | Financial |
| `payment_id` | Payment | API-08 | Payment reference |
| `subscription_id` | Subscription | API-09 | Commercial control |
| `license_id` | License | API-09 | License control |
| `campaign_id` | Campaign | API-10 | Communication |
| `notification_id` | Notification | API-10 | Delivery tracking |
| `report_execution_id` | Report Execution | API-11 | Async report |
| `ticket_id` | Support Ticket | API-12 | Support lifecycle |
| `audit_event_id` | Audit Event | API-13 | Audit review |

---

# 12. Pagination and Query Variables

| Variable | Default | Maximum | Applies To |
|---|---|---|---|
| `page` | `1` | Not Applicable | Offset pagination |
| `page_size` | `20` | `100` unless module overrides | Offset pagination |
| `cursor` | Empty | Not Applicable | Cursor pagination |
| `limit` | `20` | `100` unless module overrides | Cursor pagination |
| `from_date` | Test-specific | Not Applicable | Date filters |
| `to_date` | Test-specific | Not Applicable | Date filters |
| `sort` | Module default | Approved sort list | Sorting |
| `search` | Empty | Module-specific | Search endpoints |

---

# 13. Idempotency Variables

| Variable | Required For | Generation Rule | Reuse Rule |
|---|---|---|---|
| `idempotency_key` | Create, lifecycle, commercial, retry-prone actions | UUID v4 | Reuse only for intentional retry tests |
| `idempotency_key_replay` | Replay tests | Copy from original request | Same payload shall return replay-safe result |
| `idempotency_key_conflict` | Conflict tests | Copy from original request | Different payload shall return conflict |
| `provider_event_id` | Webhook/callback tests | Provider or test UUID | Must prevent duplicate callback processing |

---

# 14. Concurrency Variables

| Variable | Purpose | Source |
|---|---|---|
| `etag` | Current resource version | GET or create response |
| `stale_etag` | Negative concurrency test | Previously captured ETag |
| `current_version` | Optional version projection | API response |
| `resource_updated_at` | Human-readable validation | API response |

Protected update and lifecycle requests shall fail when `If-Match` is missing or stale where API-00 requires concurrency protection.

---

# 15. Webhook and Provider Variables

| Variable | Classification | Purpose |
|---|---|---|
| `webhook_secret` | Secret | Outbound webhook signing test |
| `webhook_signature` | Secret / Derived | Inbound callback signature |
| `webhook_timestamp` | Confidential | Replay-window validation |
| `webhook_delivery_id` | Confidential | Delivery tracking |
| `provider_payment_id` | Confidential | Payment gateway reference |
| `provider_refund_id` | Confidential | Refund gateway reference |
| `provider_notification_id` | Confidential | Notification provider reference |

Provider variables shall not contain raw card data, provider credentials, or production callback secrets.

---

# 16. Pre-request Script Requirements

Approved pre-request script responsibilities:

- Generate `correlation_id` when missing.
- Generate `idempotency_key` for create/lifecycle requests when test flow requires a new key.
- Attach `Authorization` header from `access_token`.
- Refresh token only through approved authentication flows.
- Validate that `base_url` and `environment_name` are consistent.
- Prevent production execution unless `production_run_approved` is explicitly set by an approved operator.

Pre-request scripts shall not:

- Log tokens, passwords, provider secrets, or personal data.
- Hard-code production credentials.
- Override tenant context silently.
- Suppress failed assertions.
- Retry non-idempotent operations without an idempotency key.

---

# 17. Test Script Requirements

Collection test scripts shall assert:

- HTTP status is expected.
- API-00 response envelope is present.
- `correlation_id` is returned or traceable.
- Error response includes stable `error_code`.
- JSON fields use snake_case.
- Sensitive values are masked or absent.
- Tenant scope cannot be bypassed through headers.
- Idempotency and concurrency behavior matches endpoint classification.

---

# 18. Environment File Naming

| File | Purpose | Commit Rule |
|---|---|---|
| `digitize.local.env.json` | Local developer template | May be committed only with placeholders |
| `digitize.dev.env.json` | Shared development template | May be committed only with placeholders |
| `digitize.qa.env.json` | QA template | May be committed only with placeholders |
| `digitize.staging.env.json` | Staging template | May be committed only with placeholders |
| `digitize.production.env.json` | Production template | Shall not contain secrets |
| `digitize.ci.env.json` | CI template | Secrets injected at runtime |

Actual secret-bearing environment files shall not be committed.

---

# 19. Secret Handling Rules

- Secrets shall be stored in approved local secret storage, CI secret storage, or managed vault tooling.
- Secrets shall not appear in Git, screenshots, exported collections, test reports, logs, audit detail payloads, or support tickets.
- Production tokens shall not be used in development, QA, or staging.
- Shared user accounts are not approved for production operational runs.
- CI service credentials shall use least privilege and short-lived tokens where available.

---

# 20. CI/CD Execution Profile

| Stage | Required Collections | Required Assertions | Failure Handling |
|---|---|---|---|
| Pull Request | Smoke and changed-module contract tests | Auth, envelope, validation | Block merge |
| Integration | Module collections | Tenant scope, success/error paths | Fail pipeline |
| Regression | API-01 to API-14 plus API-16 suites | Full contract baseline | Fail release candidate |
| Release Candidate | Critical path and migration checks | Backward compatibility | Block release |
| Production Smoke | Read-only and approved synthetic checks | Availability and response shape | Alert operations |

---

# 21. Environment Promotion Rules

Environment configuration changes shall be promoted in this order:

1. Local template validation.
2. Development execution.
3. QA execution.
4. Staging release-candidate execution.
5. Production approval.

Promotion requires DevOps and QA review when variables affect authentication, tenant scope, provider integration, webhook security, payment handling, or release validation.

---

# 22. Environment Validation Checklist

| Check | Required | Owner |
|---|---|---|
| Base URL points to expected environment | Yes | DevOps |
| API version is `v1` | Yes | API Architecture |
| Tokens are valid and scoped | Yes | QA / DevOps |
| Tenant variables belong to test tenant | Yes | QA |
| Unauthorized tenant variables are present for negative tests | Yes | QA |
| Secrets are masked in reports | Yes | DevOps |
| Idempotency and correlation generation works | Yes | QA |
| Production execution is guarded | Yes | DevOps |

---

# 23. Traceability

| Source | Mapping |
|---|---|
| API-00 | Header, authentication, tenant scope, response, error, idempotency, concurrency standards |
| API-01 to API-14 | Resource identifiers and module-specific request variables |
| API-16 | Test scenario execution requirements |
| API-17 | Traceability expectations |
| API-18 | Webhook and provider variables |
| API-19 | Error assertion variables |

---

# 24. Governance Controls

- Environment templates require API Architecture, QA, and DevOps review.
- Production variables require operational approval.
- Secret-bearing files shall be excluded from source control.
- Variable additions require naming review when they affect shared collections.
- Deprecated variables shall remain documented until all collection references are removed.

---

# 25. Document Acceptance Criteria

This document is acceptable when:

- All approved API execution environments are defined.
- Required variables have ownership, purpose, and security rules.
- Tenant context, idempotency, correlation, pagination, and concurrency variables are documented.
- Secret handling prevents credential leakage.
- CI/CD execution rules are implementation-ready.
- API-16 tests can reference these variables without additional assumptions.

---

# 26. Summary

API-15 establishes the governed environment and variable baseline for Digitize API execution. It ensures API collections can be run safely, repeatedly, and traceably across local, QA, staging, production, and CI contexts.
