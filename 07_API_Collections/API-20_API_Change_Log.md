> **Status:** Frozen — 2026-07-26 — 2026-07-26

# API-20 API Change Log

**Document ID:** API-20  
**Document Name:** API Change Log  
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
**Reviewer:** Solution Architecture / Product Management / Backend Engineering / QA / DevOps / Support  
**Dependencies:** API-00, API-01 to API-19, Release Governance  
**Last Updated:** July 2026

---

# 1. Document Metadata

| Attribute | Value |
|---|---|
| Document ID | API-20 |
| Document Name | API Change Log |
| Output File | API-20_API_Change_Log.md |
| API Version | v1 |
| Document Version | 0.1 |
| Status | Design Draft |
| Governing Standard | API-00_API_Collection_Standards.md |

---

# 2. Purpose

This document tracks and governs API changes for Digitize.

It defines change types, change record fields, compatibility rules, approval workflow, deprecation and retirement rules, migration guidance, release mapping, consumer communication, testing requirements, traceability updates, and the controlled API change history.

---

# 3. Scope

In scope:

- API endpoint additions, modifications, deprecations, and retirements.
- Request and response schema changes.
- Header, authentication, authorization, tenant context, pagination, idempotency, and concurrency changes.
- Webhook event, payload, signature, retry, and delivery changes.
- Error code changes.
- Environment and test governance changes.
- Release mapping and migration guidance.

Out of scope:

- Internal implementation refactors that do not alter API behavior.
- Database-only changes that do not affect API contracts.
- UI-only changes that do not alter API usage.
- Infrastructure changes with no API consumer impact.

---

# 4. Change Principles

| Principle | Standard |
|---|---|
| Traceable | Every material API change shall have a change record |
| Reviewed | Breaking and security-sensitive changes require Architecture Review |
| Testable | Changes shall map to API-16 test updates |
| Compatible by default | Prefer additive non-breaking changes |
| Consumer aware | Breaking, deprecated, or retired behavior requires communication |
| Version governed | API versioning and payload versioning shall follow API-00 and API-18 |
| Auditable | Approval, release, and migration decisions shall be retained |

---

# 5. Change Types

| Change Type | Description | Compatibility |
|---|---|---|
| Added Document | New API documentation artifact added | Non-breaking |
| Added Endpoint | New endpoint added | Usually non-breaking |
| Modified Endpoint | Existing behavior changed | Depends on change |
| Deprecated Endpoint | Endpoint remains available but should not be used | Non-breaking initially |
| Retired Endpoint | Endpoint removed or disabled | Breaking |
| Request Schema Change | Request fields changed | Depends on required/optional behavior |
| Response Schema Change | Response fields changed | Depends on removal/rename/type change |
| Header Change | Required or optional header behavior changed | Depends on requirement |
| Error Code Change | Error code/status/message/retryability changed | Depends on clients |
| Webhook Change | Event, envelope, signature, retry, or payload changed | Depends on versioning |
| Environment Change | API-15 variable or execution profile changed | Usually non-breaking |
| Test Change | API-16 scenario or automation expectation changed | Usually non-breaking |
| Documentation Correction | Clarification without behavior change | Non-breaking |

---

# 6. Compatibility Classification

| Classification | Meaning | Examples |
|---|---|---|
| Non-breaking | Existing compliant clients continue working | Add optional response field, add new endpoint |
| Conditionally breaking | Some clients may be affected depending on usage | Tighten validation, change rate limit |
| Breaking | Existing clients must change | Remove field, rename field, change required header |
| Security mandatory | Breaking or not, change required for security | Disable unsafe behavior, rotate signature version |
| Documentation only | No runtime behavior change | Clarify table mapping or test reference |

---

# 7. Change Record Required Fields

| Field | Required | Description |
|---|---|---|
| Change ID | Yes | Stable identifier |
| Date | Yes | Change date |
| API Version | Yes | API version affected |
| API Document | Yes | API document affected |
| Endpoint/Error/Webhook | Conditional | Specific changed contract |
| Change Type | Yes | Approved change type |
| Compatibility | Yes | Compatibility classification |
| Description | Yes | Clear summary |
| Reason | Yes | Business, security, defect, compliance, or architecture driver |
| Migration Guidance | Conditional | Required for breaking/deprecated changes |
| Test Impact | Yes | API-16 scenario update or no-impact statement |
| Traceability Impact | Yes | API-17 update requirement |
| Approval | Conditional | Required approver or review body |
| Release | Yes | Release or target milestone |
| Status | Yes | Proposed, Approved, Implemented, Deprecated, Retired |

---

# 8. Change ID Format

Format:

```text
API-CHG-0001
```

Rules:

- Use sequential numeric IDs.
- Do not reuse retired or rejected IDs.
- One change record may reference multiple endpoints only when they are part of one approved change package.
- Split changes when compatibility impact differs.

---

# 9. Change Log Template

| Change ID | Date | API Version | API Document | Endpoint/Error/Webhook | Change Type | Compatibility | Description | Migration Guidance | Approval | Release | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|
| API-CHG-0001 | 2026-07-26 | v1 | Postman_Collection / API Environment Template | N/A | Added Document | Non-breaking | Added Postman collection template and environment template for QA, CI, and consumer onboarding. | Not Applicable | API Architecture | v1.x | Implemented |
| API-CHG-XXXX | YYYY-MM-DD | v1 | API-XX | API-XX-001 | Added Endpoint | Non-breaking | Summary | Not Applicable | API Architecture | v1.x | Proposed |
[CHANGELOG NOTE — updated: owners confirmed mapping updates; if further changes required, update CHG record. CHG references: API-CHG-0020]

---

# 10. Initial Change Log

| Change ID | Date | API Version | API Document | Endpoint/Error/Webhook | Change Type | Compatibility | Description | Migration Guidance | Approval | Release | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|
| API-CHG-0001 | July 2026 | v1 | API-00 | API Standards | Added Document | Non-breaking | Initial API collection standards baseline created | Not Applicable | API Architecture | Foundation Documentation | Implemented |
| API-CHG-0002 | July 2026 | v1 | API-01 to API-05 | Domain API collections | Added Document | Non-breaking | Initial Design Draft domain API collections generated through Membership Management | Not Applicable | API Architecture | Foundation Documentation | Implemented |
| API-CHG-0003 | July 2026 | v1 | API-06 to API-14 | Domain API collections | Added Document | Non-breaking | Initial Design Draft domain API collections generated for Attendance through Common Reference | Not Applicable | API Architecture | Foundation Documentation | Implemented |
| API-CHG-0004 | July 2026 | v1 | API-15 to API-20 | Governance API documents | Documentation Correction | Non-breaking | Governance documents expanded with implementation-ready catalogs, matrices, templates, controls, and acceptance criteria | Not Applicable | API Architecture | Foundation Documentation | Implemented |
| API-CHG-0005 | July 2026 | v1 | Postman_Collection.md | Postman collection blueprint | Added Document | Non-breaking | Initial Postman collection execution blueprint generated for API-01 through API-26 | Not Applicable | API Architecture / QA | Foundation Documentation | Implemented |
| API-CHG-0006 | July 2026 | v1 | API-21 to API-26 | API-to-UI bridge governance | Added Document | Non-breaking | Added OpenAPI governance, frontend consumption standards, API access matrix, state/workflow contract, mocking and sandbox strategy, and release/consumer readiness checklist before UI/UX design | Not Applicable | API Architecture / Frontend Architecture / QA | Foundation Documentation | Implemented |
| API-CHG-0007 | July 2026 | v1 | README, API-16, API-17, API_Test_Cases.md, Postman_Collection.md | Documentation correction | Non-breaking | Fixed API-21 through API-26 register and cross-reference gaps and generated the API test cases support artifact | Not Applicable | API Architecture / QA | Foundation Documentation | Implemented |

## Proposed TBD Resolution Change Records

[CHANGELOG NOTE — proposed CHGs remain Proposed until owners provide authoritative IDs and approval. See docs/07_API_Collections/issues/ for assignment.]

| Change ID | Date | API Version | API Document | Endpoint/Error/Webhook | Change Type | Compatibility | Description | Migration Guidance | Approval | Release | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|
[CHANGELOG ACTION — CHG API-CHG-0008: owners to resolve 3 TBDs in API-00; see docs/07_API_Collections/issues/]
| API-CHG-0009 | 2026-07-26 | v1 | API-01_Platform_Administration_Collection.md | N/A | Traceability Mapping | Non-breaking | Resolve 12 [CTO: assigned — confirm or replace TBD mappings] occurrences (platform health, events, FR mappings); update API-17 and API-16 references. | Not Applicable | API Architecture / BA / Platform Owners | v1.x | Proposed |
| API-CHG-0010 | 2026-07-26 | v1 | API-02_Organization_Facility_Site_Collection.md | N/A | Traceability Mapping | Non-breaking | Resolve 4 [CTO: assigned — confirm or replace TBD mappings] occurrences for org/facility/site events and config mappings. | Not Applicable | API Architecture / BA / Owners | v1.x | Proposed |
| API-CHG-0011 | 2026-07-26 | v1 | API-03_Identity_User_Role_Collection.md | N/A | Traceability Mapping | Non-breaking | Resolve 2 [CTO: assigned — confirm or replace TBD mappings] occurrences for authentication/login source mappings and FR linkage. | Not Applicable | API Architecture / Security / BA | v1.x | Proposed |
| API-CHG-0012 | 2026-07-26 | v1 | API-06_Attendance_Walkin_Collection.md | N/A | Traceability Mapping | Non-breaking | Resolve 1 [CTO: assigned — confirm or replace TBD mapping] occurrence in attendance/walkin mapping. | Not Applicable | API Architecture / BA / Owners | v1.x | Proposed |
| API-CHG-0013 | 2026-07-26 | v1 | API-07_Trainer_Activity_Batch_Collection.md | N/A | Traceability Mapping | Non-breaking | Resolve 1 [CTO: assigned — confirm or replace TBD mapping] occurrence in trainer/activity/batch mappings. | Not Applicable | API Architecture / BA / Owners | v1.x | Proposed |
| API-CHG-0014 | 2026-07-26 | v1 | API-08_Billing_Payment_Collection.md | N/A | Traceability Mapping | Non-breaking | Resolve 1 [CTO: assigned — confirm or replace TBD mapping] occurrence in billing/payment mappings (provider callback mappings may be required). | Not Applicable | API Architecture / Security / Commercial | v1.x | Proposed |
| API-CHG-0015 | 2026-07-26 | v1 | API-09_Subscription_License_Collection.md | N/A | Traceability Mapping | Non-breaking | Resolve 1 [CTO: assigned — confirm or replace TBD mapping] occurrence in subscription/license mappings. | Not Applicable | API Architecture / BA / Owners | v1.x | Proposed |
| API-CHG-0016 | 2026-07-26 | v1 | API-10_Notification_Campaign_Collection.md | N/A | Traceability Mapping | Non-breaking | Resolve 1 [CTO: assigned — confirm or replace TBD mapping] occurrence in notification/campaign mapping. | Not Applicable | API Architecture / BA / Owners | v1.x | Proposed |
| API-CHG-0017 | 2026-07-26 | v1 | API-11_Reports_Analytics_Collection.md | N/A | Traceability Mapping | Non-breaking | Resolve 1 [CTO: assigned — confirm or replace TBD mapping] occurrence in reporting/analytics mappings. | Not Applicable | API Architecture / BI / Owners | v1.x | Proposed |
| API-CHG-0018 | 2026-07-26 | v1 | API-12_Support_Ticket_Collection.md | N/A | Traceability Mapping | Non-breaking | Resolve 1 [CTO: assigned — confirm or replace TBD mapping] occurrence in support ticket mapping. | Not Applicable | API Architecture / Support / BA | v1.x | Proposed |
| API-CHG-0019 | 2026-07-26 | v1 | API-13_Audit_Security_Collection.md | N/A | Traceability Mapping | Non-breaking | Resolve 1 [CTO: assigned — confirm or replace TBD mapping] occurrence in audit/security mapping and ensure audit event IDs are linked. | Not Applicable | API Architecture / Security | v1.x | Proposed |
| API-CHG-0020 | 2026-07-26 | v1 | API-14_Common_Reference_Collection.md | N/A | Traceability Mapping | Non-breaking | Resolve 3 [CTO: assigned — confirm or replace TBD mappings] occurrences in common reference endpoints and lookup mappings. | Not Applicable | API Architecture / BA / Owners | v1.x | Proposed |
| API-CHG-0021 | 2026-07-26 | v1 | API-17_API_Traceability_Matrix.md | N/A | Traceability Mapping | Non-breaking | Resolve 5 [CTO: assigned — confirm or replace TBD mappings] entries in API-17 traceability matrix; authoritative IDs required. | Not Applicable | API Architecture / Business Analysis / Owners | v1.x | Proposed |
| API-CHG-0022 | 2026-07-26 | v1 | API-18_Webhook_Specifications.md | N/A | Traceability Mapping | Non-breaking | Resolve 2 [CTO: assigned — confirm or replace TBD mappings] occurrences in webhook DB mapping and signature mappings. | Not Applicable | API Architecture / Security / Integration Owners | v1.x | Proposed |
| API-CHG-0023 | 2026-07-26 | v1 | README.md | N/A | Documentation Correction | Non-breaking | Replace README [CTO: assigned — confirm or replace TBD guidance] guidance with resolved owner mappings once TBDs are cleared across collection docs. | Not Applicable | API Architecture / BA | v1.x | Proposed |

---

# 11. Endpoint Addition Rules

New endpoints require:

- Endpoint ID.
- Method and URL.
- Purpose.
- API classification.
- Data classification.
- Authentication and authorization rules.
- Tenant scope rules.
- Request and response behavior.
- Error mappings.
- Database mapping.
- Audit/event mapping.
- API-16 test mapping.
- API-17 traceability row.
- API-20 change record.

---

# 12. Endpoint Modification Rules

Endpoint modifications require impact analysis for:

- Method.
- URL.
- Path/query parameters.
- Request body fields.
- Response body fields.
- Required headers.
- Authentication or authorization behavior.
- Tenant context behavior.
- Error codes or HTTP statuses.
- Idempotency or concurrency requirements.
- Audit, event, or notification behavior.
- Rate limit or caching behavior.

---

# 13. Breaking Change Rules

Breaking changes include:

- Removing an endpoint.
- Renaming a URL path.
- Changing HTTP method.
- Removing a response field used by clients.
- Renaming a request or response field.
- Changing field type.
- Making an optional request field required.
- Tightening authorization in a way that affects existing approved clients.
- Changing error code meaning.
- Changing webhook signature verification without compatible versioning.

Breaking changes require:

- Architecture Review.
- Product approval.
- QA regression plan.
- API-17 traceability update.
- API-16 test update.
- Migration guidance.
- Release notes.
- Consumer communication.

---

# 14. Non-breaking Change Rules

Usually non-breaking changes include:

- Adding a new endpoint.
- Adding an optional request field.
- Adding a response field.
- Adding a new error code for a new scenario.
- Adding a new webhook event type.
- Adding a new reference value where clients are expected to handle unknown values.
- Clarifying documentation without runtime behavior change.

Non-breaking changes still require API documentation, tests, and traceability updates.

---

# 15. Deprecation Rules

Deprecation records shall include:

| Field | Required |
|---|---|
| Deprecated endpoint/error/webhook | Yes |
| Replacement | Yes where available |
| Deprecation date | Yes |
| Sunset date | Conditional |
| Consumer impact | Yes |
| Migration guidance | Yes |
| Monitoring plan | Yes |
| Approval | Yes |

Deprecated endpoints shall remain documented until retirement.

---

# 16. Retirement Rules

Retirement requires:

- Prior deprecation unless waived for security or legal reasons.
- Replacement endpoint or explanation.
- Consumer impact review.
- Production usage review.
- Support readiness.
- API-20 retirement change record.
- API-17 mapping status update.
- API-16 test update.
- Release approval.

Retired error codes shall not be reused.

---

# 17. Request Schema Change Rules

| Change | Compatibility | Required Action |
|---|---|---|
| Add optional field | Non-breaking | Document and test |
| Add required field | Breaking | Migration guidance |
| Remove field | Breaking | Deprecation/migration |
| Rename field | Breaking | Version or migration |
| Change enum values | Conditional | Client impact review |
| Change validation rule | Conditional | QA and support review |

---

# 18. Response Schema Change Rules

| Change | Compatibility | Required Action |
|---|---|---|
| Add field | Usually non-breaking | Document and test |
| Remove field | Breaking | Deprecation/migration |
| Rename field | Breaking | Version or migration |
| Change type | Breaking | Version or migration |
| Change nullability | Conditional | Client impact review |
| Change pagination metadata | Breaking if clients depend on it | Migration guidance |

---

# 19. Error Code Change Rules

Error code changes require API-19 update when:

- New error code is introduced.
- HTTP status changes.
- Retryability changes.
- Category changes.
- Safe message meaning changes.
- Error code is deprecated or retired.

Every error code change shall include API-16 negative test coverage.

---

# 20. Webhook Change Rules

Webhook changes require API-18 update when:

- Event type changes.
- Event payload changes.
- Event envelope changes.
- Signature version changes.
- Replay window changes.
- Retry policy changes.
- Dead-letter behavior changes.
- Subscription management behavior changes.

Breaking webhook payload changes require a new `event_version`.

---

# 21. Environment and Test Change Rules

API-15 updates are required when:

- Environment profile changes.
- Variable is added, renamed, or retired.
- Secret handling changes.
- CI/CD execution profile changes.

API-16 updates are required when:

- New behavior requires new test scenario coverage.
- Existing scenario expectation changes.
- New endpoint category is introduced.
- New security, webhook, async, idempotency, or concurrency rule is added.

---

# 22. Approval Matrix

| Change Area | Required Approval |
|---|---|
| Documentation correction | API Architecture |
| New non-breaking endpoint | API Architecture / Product |
| Breaking endpoint change | Architecture Review / Product / QA |
| Security behavior change | Security Architecture / Architecture Review |
| Payment or financial behavior | Commercial Architecture / Finance / QA |
| Webhook signature or retry change | Security Architecture / Integration Architecture |
| Error catalog change | API Architecture / QA / Support |
| Production environment change | DevOps / Operations |
| Deprecation or retirement | Architecture Review / Product / Support |

---

# 23. Migration Guidance Template

Migration guidance shall include:

- Summary of changed behavior.
- Affected endpoint, error, webhook, or variable.
- Old behavior.
- New behavior.
- Consumer action required.
- Example old request/response where safe.
- Example new request/response where safe.
- Testing recommendation.
- Deadline or sunset date.
- Support contact path.

---

# 24. Release Mapping

| Release Stage | Required Change State |
|---|---|
| Design Draft | Proposed or Approved |
| Frozen — 2026-07-26 | Approved |
| Release Candidate | Implemented and test-mapped |
| Production Release | Implemented and release-noted |
| Post-release | Monitored |
| Deprecation Window | Deprecated |
| Retirement Release | Retired |

---

# 25. Consumer Communication

Consumer communication is required for:

- Breaking changes.
- Deprecations.
- Retirements.
- Security mandatory changes.
- Webhook payload or signature changes.
- Error behavior changes that client automation depends on.
- Rate limit changes.

Communication shall include migration guidance and target dates.

---

# 26. Test and Traceability Requirements

Every material change shall update:

- API document section.
- API-16 test scenario or module test.
- API-17 traceability matrix.
- API-19 error catalog where error behavior changes.
- API-18 webhook specification where webhook behavior changes.
- Release notes where consumer-visible.

---

# 27. Change Review Checklist

| Check | Required |
|---|---|
| Change type selected | Yes |
| Compatibility classified | Yes |
| Affected API documents identified | Yes |
| Endpoint/error/webhook/variable identified | Conditional |
| Migration guidance included | Conditional |
| Security impact reviewed | Yes |
| Tenant isolation impact reviewed | Yes |
| Test impact reviewed | Yes |
| Traceability updated | Yes |
| Release mapped | Yes |
| Approval recorded | Yes |

---

# 28. Change Status Definitions

| Status | Meaning |
|---|---|
| Proposed | Change identified but not approved |
| Approved | Change approved for implementation/documentation |
| Implemented | Change reflected in documentation and/or implementation |
| Deferred | Change postponed |
| Rejected | Change not approved |
| Deprecated | Existing behavior marked for future removal |
| Retired | Existing behavior removed or no longer supported |

---

# 29. Monitoring After Change

Post-change monitoring shall review:

- Error rates.
- Latency changes.
- Authorization failures.
- Tenant scope failures.
- Webhook delivery failures.
- Consumer support tickets.
- Deprecated endpoint usage.
- Retired endpoint attempts.
- Payment or commercial reconciliation impact.

---

# 30. Assumptions and Constraints

- API implementation may lag documentation during Design Draft.
- Frozen API documents require complete change records for material changes.
- Source mappings marked pending shall be resolved before Frozen status unless formally waived.
- Emergency security changes may compress approval steps but still require retroactive documentation.

---

# 31. Document Acceptance Criteria

This document is acceptable when:

- Change types and compatibility classes are defined.
- Change record fields and templates are complete.
- Breaking, non-breaking, deprecation, retirement, schema, error, webhook, environment, and test rules are documented.
- Approval, release, migration, communication, monitoring, test, and traceability requirements are explicit.
- Initial baseline change records exist.

---

# 32. Summary

API-20 establishes the API change governance baseline for Digitize. It ensures API evolution is traceable, reviewed, testable, release-aware, migration-friendly, and safe for consumers across the API lifecycle.
