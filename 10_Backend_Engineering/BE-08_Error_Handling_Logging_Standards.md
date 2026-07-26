# BE-08 Error Handling Logging Standards

> Exception design, API error mapping, structured logging, correlation, audit handoff, metrics, tracing, diagnostics, redaction, and support visibility standards.

---

# Document Control

| Field | Value |
|---|---|
| Document ID | BE-08 |
| Document Name | Error Handling Logging Standards |
| Folder | 10_Backend_Engineering |
| Product | Digitize by OreeOn Technologies Pvt. Ltd. |
| Status | Design Draft |
| Governing Standard | BE-00_Backend_Engineering_Standards.md |
| Owner | Backend Engineering and Operations |
| Reviewers | Backend, Security, DevOps, Operations, QA |
| Version | 1.0 |
| Last Updated | 2026-07-26 |

---

# 1. Purpose

This document defines backend exception design, error mapping, structured logging, correlation, audit handoff, metrics, tracing, diagnostics, redaction, and support visibility standards for Digitize.

It ensures errors are safe for clients, actionable for engineers, useful for support, auditable where required, and observable across API, service, repository, worker, outbox, and integration boundaries.

---

# 2. BE-00 Inheritance

This document inherits `BE-00_Backend_Engineering_Standards.md`.

This document does not define production dashboards, operations runbooks, API error catalogue ownership, or provider-specific error catalogues. It defines backend implementation responsibilities for errors, logs, and diagnostics.

---

# 3. Scope

This document covers:

- Error-handling principles.
- Exception taxonomy.
- Domain, application, validation, authentication, authorization, tenant, not-found, conflict, persistence, provider, timeout, rate-limit, background-job, and unexpected errors.
- Exception propagation.
- Error mapper responsibility.
- HTTP and approved API error mapping.
- Safe client messaging and internal diagnostics.
- Cross-tenant existence protection.
- Structured logging fields.
- Correlation ID, request ID, principal identity, tenant context, operation name, outcome, latency, error code, severity.
- Sensitive-data redaction and prohibited log content.
- Operational logging versus audit logging.
- Metrics, traces, health, readiness, provider-call, worker, queue, outbox, naming, support, alerting, retention, testing, and anti-pattern rules.

---

# 4. Out of Scope

This document does not define:

- Production monitoring dashboards.
- Operations runbooks.
- Incident-response procedures.
- Provider-specific error catalogues.
- API error code catalogue ownership.
- Business-rule definitions.

---

# 5. Source Alignment

| Source Area | Alignment |
|---|---|
| API-19 | API error code catalog |
| API-22 | Frontend API error consumption |
| API-26 | API release and consumer readiness |
| IC-11 | Integration error, retry, timeout, and dead-letter behavior |
| IC-13 | Integration observability contract |
| FR-21 | Audit and compliance expectations |
| TA-07 | Observability and operations architecture |
| BE-00 | Error, logging, audit, observability, security, and release standards |
| BE-07 | API error response mapping |
| BE-09 | Background-job and outbox failure behavior |

---

# 6. Error-Handling Principles

Backend error handling shall:

- Use controlled error categories.
- Map user-facing errors to approved API contracts.
- Avoid exposing stack traces or internal details.
- Preserve correlation and request identifiers.
- Protect cross-tenant existence.
- Preserve enough diagnostic context for investigation.
- Distinguish retryable and non-retryable failures where applicable.
- Avoid swallowing failures silently.

---

# 7. Exception Taxonomy

| Error Type | Owner | User-Facing |
|---|---|---|
| Domain Error | Domain or application service | Sometimes |
| Application Error | Application service | Sometimes |
| Validation Error | API schema or service | Yes |
| Authentication Error | Auth boundary | Yes |
| Authorization Error | Authorization boundary | Yes |
| Tenant Context Error | Tenant context boundary | Yes |
| Not Found Error | Service or repository boundary | Yes |
| Conflict Error | Service or repository boundary | Yes |
| Persistence Error | Repository boundary | Usually mapped |
| Provider Error | Integration adapter | Usually mapped |
| Timeout Error | Adapter, repository, worker | Sometimes |
| Rate-Limit Error | API or provider boundary | Yes where approved |
| Background Job Error | Worker boundary | Not usually direct |
| Unexpected Error | Global handler | Generic only |

---

# 8. Domain and Application Errors

Domain and application errors shall represent controlled business or orchestration failures.

Examples include:

- Invalid state transition.
- Eligibility failure.
- Business rule violation.
- Idempotency conflict.
- Resource-level authorization failure.
- Compensation scheduling failure.

These errors shall be mappable to approved API error responses where user-facing.

---

# 9. Validation, Authentication, Authorization, and Tenant Errors

Validation errors shall describe invalid client input safely.

Authentication errors shall not disclose token internals.

Authorization errors shall not reveal hidden permissions or unrelated tenant resources.

Tenant context errors shall not reveal whether a resource exists outside the caller's allowed scope.

---

# 10. Not-Found, Conflict, Persistence, Provider, Timeout, and Rate-Limit Errors

Not-found errors shall be tenant-safe.

Conflict errors shall represent duplicate, lifecycle, concurrency, idempotency, or state conflicts.

Persistence errors shall be converted from database or ORM failures into controlled backend errors.

Provider errors shall be translated by integration adapters and shall not expose provider secrets or raw provider payloads.

Timeout and rate-limit errors shall include retry guidance only where approved.

---

# 11. Background-Job and Unexpected Errors

Background-job errors shall include job identity, tenant context where applicable, retry state, and failure category.

Unexpected errors shall:

- Return generic client-safe messages.
- Emit diagnostic logs.
- Preserve correlation context.
- Avoid sensitive data exposure.
- Trigger alerting inputs where severity requires.

---

# 12. Exception Propagation Rules

Exceptions shall propagate through controlled boundaries.

| Boundary | Responsibility |
|---|---|
| Domain Service | Raise controlled domain errors |
| Application Service | Convert orchestration failures to controlled application errors |
| Repository | Convert persistence failures to controlled repository errors |
| Integration Adapter | Convert provider failures to controlled integration errors |
| API Boundary | Map controlled errors to approved API responses |
| Worker Boundary | Record retry, dead-letter, or failure state |

---

# 13. Error Mapper Responsibility

The error mapper shall:

- Map controlled errors to approved API error structures.
- Apply approved HTTP status codes.
- Preserve error codes.
- Preserve safe diagnostic references.
- Include correlation ID and request ID where applicable.
- Avoid stack traces.
- Avoid sensitive field exposure.
- Avoid cross-tenant existence leakage.

---

# 14. Approved API Error Structure

API error responses shall align with API-19.

The backend shall preserve approved fields such as:

- Error code.
- Message.
- Details where safe.
- Correlation ID.
- Request ID.
- Field-level validation details where approved.

The exact structure is owned by API Collections.

---

# 15. Safe Client Messaging and Internal Diagnostics

Client messages shall be clear but safe.

Internal diagnostics may include additional context in logs, traces, or error reporting systems, but shall not include secrets or prohibited sensitive data.

Support diagnostics shall allow investigation by correlation ID and request ID.

---

# 16. Structured Logging Fields

Backend logs shall use standardized field names.

| Field | Purpose |
|---|---|
| `timestamp` | Event time |
| `environment` | Runtime environment |
| `service` | Backend service name |
| `module` | Capability module |
| `operation` | Use case or endpoint operation |
| `correlation_id` | Distributed transaction identifier |
| `request_id` | Single request identifier |
| `principal_id` | Authenticated principal where safe |
| `organization_id` | Tenant context |
| `facility_id` | Tenant context where applicable |
| `site_id` | Tenant context where applicable |
| `outcome` | Success or failure |
| `latency_ms` | Duration |
| `error_code` | Controlled error code |
| `severity` | Log severity |

---

# 17. Log Severity

Log severity shall be used consistently.

| Severity | Usage |
|---|---|
| Debug | Local or controlled diagnostic detail |
| Info | Successful significant operation |
| Warning | Recoverable abnormal condition |
| Error | Failed operation requiring investigation |
| Critical | Severe service, data, security, or tenant isolation risk |

Production debug logging shall be controlled.

---

# 18. Sensitive-Data Redaction and Prohibited Log Content

Logs must not contain:

- Passwords.
- Raw access tokens.
- Refresh tokens.
- Private keys.
- Provider credentials.
- Payment card data.
- Sensitive personal data beyond approved audit needs.
- Raw provider payloads containing sensitive data.

Redaction shall occur before log emission.

---

# 19. Operational Logging Versus Audit Logging

Operational logs support troubleshooting and service health.

Audit logs provide business, security, and compliance evidence.

Audit events shall not be replaced by ordinary logs.

Sensitive actions shall hand off audit events according to Functional Requirements, API-13, Database Design, and BE-00.

---

# 20. Metrics and Traces

Metrics should include:

- Request count.
- Error count.
- Latency.
- Authentication failures.
- Authorization denials.
- Tenant-context failures.
- Repository failures.
- Provider failures.
- Worker failures.
- Outbox pending, processed, failed, retried, and dead-letter counts.

Traces should preserve execution across API, application service, repository, worker, outbox processor, and adapter boundaries using the OpenTelemetry baseline from `DR-013_OpenTelemetry_Prometheus_Grafana_Observability_Baseline.md`.

---

# 21. Health and Readiness Diagnostics

Health diagnostics indicate process availability.

Readiness diagnostics indicate ability to serve traffic safely.

Diagnostics shall:

- Avoid exposing secrets.
- Avoid exposing internal topology details.
- Identify unavailable required dependencies safely.
- Include worker and outbox processor readiness where applicable.

---

# 22. Provider, Worker, Queue, and Outbox Diagnostics

Provider-call diagnostics shall include provider-neutral operation names, outcome, latency, failure category, retryability, and correlation context.

Worker and queue diagnostics shall include job ID, job type, tenant context, status, retry count, and failure category.

Outbox diagnostics shall include event ID, event type, tenant metadata, publication state, retry count, and dead-letter state.

Queue and worker diagnostics shall align with the Celery and Redis worker baseline from `DR-009_Celery_Background_Worker_Baseline.md`.

---

# 23. Standard Naming Conventions

Log field names and metric names shall be standardized across backend services.

Metric names should identify:

- Service.
- Module.
- Operation.
- Outcome.
- Error category where applicable.

Names shall remain stable to preserve dashboards and alerts.

---

# 24. Support Diagnostic Requirements

Support diagnostics should include:

- User-facing error code.
- Correlation ID.
- Request ID.
- Tenant context.
- Operation name.
- Safe failure reason.
- Retry guidance where approved.
- Known limitation or escalation reference where applicable.

Support teams shall not require secret-bearing logs for ordinary diagnosis.

---

# 25. Alerting Inputs

Backend implementation should emit alerting inputs for:

- Critical security failures.
- Tenant-isolation failures.
- Elevated error rates.
- Elevated latency.
- Provider failure spikes.
- Outbox dead-letter growth.
- Worker backlog growth.
- Readiness failures.

Alert definitions are owned by Operations and Deployment documentation.

---

# 26. Retention and Immutability Alignment

Logs shall be immutable once written unless retention policies require archival or deletion.

Retention behavior shall align with security, compliance, operations, and database governance.

---

# 27. Observability Testing

Tests shall cover:

- Error mapping.
- Safe client messaging.
- Correlation and request ID propagation.
- Structured log fields.
- Sensitive-data redaction.
- Tenant-safe not-found behavior.
- Audit-event handoff where required.
- Metrics or trace hooks where practical.
- Worker and outbox diagnostics where applicable.

---

# 28. Anti-Patterns

The following are prohibited:

- Exposing stack traces to clients.
- Logging raw tokens or secrets.
- Swallowing exceptions without diagnostics.
- Returning raw provider errors to clients.
- Revealing cross-tenant resource existence.
- Using inconsistent log field names.
- Treating operational logs as audit evidence.
- Emitting high-cardinality sensitive metric labels.

---

# 29. Traceability Requirements

Error and logging implementation shall trace to:

- API-19 for error contracts.
- API-22 for frontend error behavior.
- IC-11 and IC-13 for integration errors and observability.
- FR-21 for audit and compliance.
- TA-07 for observability architecture.
- BE-07 for API error mapping.
- BE-09 for worker and outbox failures.

Traceability sources: see [docs/10_Backend_Engineering/BE-TRACEABILITY_MAPPINGS.md](BE-TRACEABILITY_MAPPINGS.md) — primary sources include [docs/05_Technical_Architecture/TA-07_Observability_Operations_Architecture.md](../05_Technical_Architecture/TA-07_Observability_Operations_Architecture.md), [docs/08_Integration_Contracts/IC-13_Integration_Observability_Contract.md](../08_Integration_Contracts/IC-13_Integration_Observability_Contract.md), and [docs/99_Decision_Records/DR-013_OpenTelemetry_Prometheus_Grafana_Observability_Baseline.md](../99_Decision_Records/DR-013_OpenTelemetry_Prometheus_Grafana_Observability_Baseline.md).

---

# 30. Acceptance Criteria

This document is acceptable when:

- Error principles, taxonomy, propagation, mapper, HTTP/API mapping, safe messaging, diagnostics, and cross-tenant protection are defined.
- Structured logging, correlation, request ID, principal, tenant context, operation, outcome, latency, error code, severity, redaction, prohibited content, audit handoff, metrics, traces, health/readiness, provider, worker, queue, outbox, naming, support, alerting, retention, tests, and anti-patterns are defined.

---

# 31. Freeze Rule

This document may be frozen only after BE-07 confirms API error mapping, BE-09 confirms background-job and outbox failure handling, and BE-10 confirms observability testing coverage.

---

# 32. Summary

BE-08 defines backend error handling, logging, and observability standards for Digitize.

It ensures failures are classified, mapped, logged, redacted, traced, measured, diagnosed, audited where required, and protected from leaking sensitive or cross-tenant information.
