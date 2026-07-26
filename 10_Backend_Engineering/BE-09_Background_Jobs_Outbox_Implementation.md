# BE-09 Background Jobs Outbox Implementation

> Asynchronous job execution, scheduled processing, transactional outbox persistence, event publication, retries, dead-letter handling, idempotency, reconciliation, and provider-adapter boundary standards.

---

# Document Control

| Field | Value |
|---|---|
| Document ID | BE-09 |
| Document Name | Background Jobs Outbox Implementation |
| Folder | 10_Backend_Engineering |
| Product | Digitize by OreeOn Technologies Pvt. Ltd. |
| Status | Design Draft |
| Governing Standard | BE-00_Backend_Engineering_Standards.md |
| Owner | Backend Engineering and Integration Architecture |
| Reviewers | Backend, Integration, Database, DevOps, Operations, QA |
| Version | 1.0 |
| Last Updated | 2026-07-26 |

---

# 1. Purpose

This document defines backend standards for background jobs, scheduled processing, transactional outbox persistence, event publication, retries, dead-letter handling, idempotency, reconciliation, and provider-adapter boundaries.

It ensures asynchronous processing in Digitize is transactionally safe, tenant-aware, retry-safe, observable, recoverable, and aligned with Integration Contracts.

---

# 2. BE-00 Inheritance

This document inherits `BE-00_Backend_Engineering_Standards.md`.

This document uses Celery with Redis broker as the approved worker baseline per `DR-009_Celery_Background_Worker_Baseline.md`. PostgreSQL outbox remains the durable source of truth for event publication state.

---

# 3. Scope

This document covers:

- Background-processing principles.
- Deferred, scheduled, periodic, and event-triggered jobs.
- Job ownership, input contracts, tenant propagation, correlation identifiers, idempotency, retry policies, backoff, limits, poison messages, dead-letter behavior, recovery, replay, state tracking, observability, cancellation, timeouts, duplicate prevention, scheduled concurrency, and per-tenant scheduled execution.
- Transactional outbox purpose, record creation, same-transaction guarantee, event metadata, publication state, retry state, claiming, locking, concurrency, delivery assumptions, consumer idempotency, ordering, replay, reconciliation, dead-letter outbox records, adapter invocation, provider timeout, notifications, reports, payment reconciliation, files, audit, support, tests, and anti-patterns.

---

# 4. Out of Scope

This document does not define:

- Specific queue, broker, scheduler, or worker framework.
- Provider commercial selection.
- Provider-specific API contracts.
- Database schema ownership.
- Deployment topology.
- Production runbooks.

---

# 5. Source Alignment

| Source Area | Alignment |
|---|---|
| IC-00 to IC-17 | Integration standards, retry, security, observability, testing, and release readiness |
| IC-09 | Event outbox integration contract |
| IC-11 | Error, retry, dead-letter, and escalation behavior |
| IC-13 | Observability expectations |
| DB-22 | Event and integration data architecture |
| API-18 and API-24 | Webhook behavior and workflow-driven events |
| BE-01 | Worker, outbox processor, and adapter architecture |
| BE-03 | Application-service outbox record creation |
| BE-04 | Outbox repository transaction participation |
| BE-06 | Tenant context propagation |
| BE-08 | Job, outbox, and provider diagnostics |

---

# 6. Background-Processing Principles

Background processing shall:

- Be owned by a backend module or platform service.
- Preserve tenant context.
- Preserve correlation metadata where available.
- Be idempotent when retried.
- Have bounded retry behavior.
- Record failure state.
- Support dead-letter handling.
- Support reconciliation where state can diverge.
- Be observable and testable.

Worker implementation shall use Celery with Redis broker per `DR-009_Celery_Background_Worker_Baseline.md`.

---

# 7. Job Categories

| Category | Example |
|---|---|
| Deferred Job | Report generation after API request |
| Scheduled Job | Nightly cleanup or reconciliation |
| Periodic Job | Regular notification retry sweep |
| Event-Triggered Job | Process committed outbox event |
| Provider Callback Job | Payment callback reconciliation |
| Maintenance Job | Archive or retention processing |

Each job shall define owner, trigger, input contract, tenant behavior, retry behavior, observability, and failure handling.

---

# 8. Job Input Contracts

Job input contracts shall define:

- Job type.
- Job identifier.
- Tenant context.
- Actor or service identity where applicable.
- Correlation ID.
- Request ID or source request reference where applicable.
- Resource reference.
- Payload version.
- Idempotency identity where required.

Job payloads shall avoid unnecessary sensitive data.

---

# 9. Tenant Context and Correlation

Tenant-scoped jobs shall carry and validate:

- Organization.
- Facility where applicable.
- Site where applicable.
- Actor or service identity.
- Correlation ID.
- Source operation.

Workers shall reject, quarantine, or fail safely when required tenant context is missing or conflicting.

---

# 10. Idempotent Processing and Duplicate Prevention

Retryable jobs shall be idempotent.

Idempotent processing shall define:

- Idempotency key or job identity.
- Retention behavior.
- Duplicate detection.
- Duplicate response or completion behavior.
- Storage mechanism.
- Tenant scope.

Duplicate jobs shall not create duplicate business effects.

---

# 11. Retry Policy and Backoff

Retry policy shall define:

- Retryable failures.
- Non-retryable failures.
- Maximum attempts.
- Exponential backoff alignment where approved.
- Timeout behavior.
- Circuit breaker behavior where applicable.
- Poison-message handling.
- Dead-letter threshold.
- Escalation behavior.

Retries shall be bounded and observable.

---

# 12. Poison Messages and Dead-Letter Behavior

Poison messages and exhausted retries shall move to dead-letter handling.

Dead-letter records shall preserve:

- Job or event identifier.
- Tenant metadata.
- Correlation metadata.
- Payload version.
- Failure reason.
- Retry count.
- Owner.
- Replay or reconciliation eligibility.

Dead-letter records shall not be silently discarded.

---

# 13. Recovery, Replay, and Reconciliation

Recovery and replay shall be controlled.

Replay shall:

- Preserve idempotency.
- Preserve tenant context.
- Record replay actor or system identity.
- Avoid duplicate business effects.
- Produce audit or support evidence where required.

Reconciliation shall define data source, owner, frequency, failure handling, and audit requirements.

---

# 14. Job State Tracking

Jobs should track:

- Pending.
- Running.
- Succeeded.
- Failed.
- Retrying.
- Dead-lettered.
- Cancelled where applicable.

State tracking shall support operations, support, and release readiness.

---

# 15. Job Cancellation, Timeouts, and Scheduled Concurrency

Job cancellation may be supported where business behavior allows it.

Timeouts shall be explicit.

Scheduled jobs shall define:

- Frequency.
- Per-tenant execution behavior.
- Concurrency control.
- Overlap behavior.
- Failure isolation between tenants.
- Backfill or catch-up behavior.

---

# 16. Transactional Outbox Purpose

Transactional outbox ensures committed business state changes can reliably trigger asynchronous publication.

Application services write outbox records in the same transaction as business state changes.

External publication happens only after transaction commit.

---

# 17. Outbox Record Requirements

Outbox records shall include:

- Event type.
- Aggregate reference.
- Resource reference where applicable.
- Tenant metadata.
- Correlation metadata.
- Payload version.
- Publication state.
- Retry state.
- Created timestamp.

Payload content shall avoid unnecessary sensitive data.

---

# 18. Same-Transaction Guarantee

Outbox records must be persisted in the same transaction as related business state changes.

If the business transaction rolls back, the outbox record shall roll back.

If the business transaction commits, the outbox record becomes eligible for publication.

---

# 19. Outbox Claiming, Locking, and Publisher Concurrency

Outbox processors shall claim records safely.

Claiming and locking behavior shall prevent uncontrolled duplicate concurrent publication while accepting at-least-once delivery assumptions.

Publisher concurrency shall be bounded and observable.

Outbox processors shall use PostgreSQL row-level claiming with `FOR UPDATE SKIP LOCKED` or an equivalent approved PostgreSQL-safe pattern. Claimed records shall be bounded by batch size, retry policy, and worker concurrency controls.

---

# 20. Delivery Assumptions, Consumer Idempotency, Ordering, and Replay

Outbox publication should assume at-least-once delivery unless approved otherwise.

Consumers shall handle duplicates safely.

Ordering requirements shall be explicit per event type.

Replay shall be controlled and auditable where required.

---

# 21. Dead-Letter Outbox Records

Outbox records that exhaust retries shall move to dead-letter handling.

Dead-letter outbox records shall support investigation, reconciliation, and approved replay.

Dead-letter movement shall be visible through logs and metrics.

---

# 22. Integration-Adapter Invocation

Outbox processors and workers invoke provider-neutral integration adapter interfaces.

Adapters shall hide provider SDK details from domain services and workers where possible.

Provider timeout and circuit-breaker behavior shall align with Integration Contracts.

Synchronous provider calls are allowed only where immediate provider response is approved.

---

# 23. Job-Type Specific Rules

| Job Type | Required Rule |
|---|---|
| Notification Jobs | Respect consent, retry, delivery state, and provider abstraction |
| Report Generation Jobs | Preserve tenant scope, export authorization, and expiry behavior |
| Payment Callback or Reconciliation Jobs | Preserve idempotency, settlement state, and audit evidence |
| File Processing Jobs | Preserve authorization, scan status where applicable, retention, and metadata |
| Webhook Jobs | Preserve signature, retry, dead-letter, and consumer readiness behavior |

---

# 24. Audit and Support Visibility

Background processing shall provide support visibility for:

- Job identity.
- Event identity.
- Tenant context.
- Current state.
- Last failure.
- Retry count.
- Dead-letter state.
- Reconciliation status.
- Correlation ID.

Sensitive data shall not be exposed in support views or logs.

---

# 25. Testing Expectations

Tests shall cover:

- Deferred jobs.
- Scheduled jobs.
- Periodic jobs.
- Event-triggered jobs.
- Tenant-context propagation.
- Correlation metadata.
- Idempotent processing.
- Retry behavior.
- Dead-letter behavior.
- Recovery and replay.
- Job state tracking.
- Timeouts.
- Duplicate-job prevention.
- Scheduled concurrency.
- Per-tenant scheduled execution.
- Outbox creation.
- Same-transaction guarantee.
- Outbox claiming and locking.
- Publisher concurrency.
- Consumer idempotency.
- Event ordering where required.
- Provider adapter failure.
- Reconciliation.

---

# 26. Anti-Patterns

The following are prohibited:

- Publishing outbox events before transaction commit.
- Writing outbox records outside the related business transaction.
- Unbounded retries.
- Silent job failure.
- Dead-letter records without owner.
- Jobs without tenant context for tenant-scoped work.
- Provider SDK usage inside domain services.
- Long-running provider calls inside database transactions.
- Duplicate processing that creates duplicate business effects.
- Selecting unapproved queue, broker, scheduler, or worker frameworks.

---

# 27. Traceability Requirements

Background job and outbox implementation shall trace to:

- Integration Contracts for retry, outbox, provider, security, observability, and release behavior.
- Database Design for outbox and integration data architecture.
- API Collections for webhook, report, payment, and workflow triggers.
- BE-01, BE-03, BE-04, BE-06, and BE-08 for backend architecture, service, repository, tenant, and diagnostics behavior.

Traceability sources: see [docs/10_Backend_Engineering/BE-TRACEABILITY_MAPPINGS.md](BE-TRACEABILITY_MAPPINGS.md) — primary sources include [docs/08_Integration_Contracts/IC-09_Event_Outbox_Integration_Contract.md](../08_Integration_Contracts/IC-09_Event_Outbox_Integration_Contract.md), [docs/99_Decision_Records/DR-009_Celery_Background_Worker_Baseline.md](../99_Decision_Records/DR-009_Celery_Background_Worker_Baseline.md), and [docs/06_Database_Design/DB-11_Database_DDL_DML_Scripts.md](../06_Database_Design/DB-11_Database_DDL_DML_Scripts.md).

---

# 28. Acceptance Criteria

This document is acceptable when:

- Background-processing principles, job categories, job ownership, input contracts, tenant propagation, correlation identifiers, idempotency, retries, poison messages, dead-letter behavior, recovery, replay, job state, cancellation, timeouts, duplicate prevention, scheduled concurrency, and per-tenant execution are defined.
- Transactional outbox purpose, record creation, same-transaction guarantee, event metadata, publication state, retry state, claiming, locking, publisher concurrency, delivery assumptions, consumer idempotency, ordering, replay, dead-letter records, adapter invocation, provider timeout, job-specific rules, audit, support, tests, and anti-patterns are defined.

---

# 29. Freeze Rule

This document may be frozen only after BE-01 confirms worker and outbox architecture, BE-04 confirms outbox repository participation, BE-06 confirms tenant propagation, BE-08 confirms diagnostics, and BE-10 confirms testing coverage.

---

# 30. Summary

BE-09 defines background jobs and transactional outbox implementation standards for Digitize.

It ensures deferred, scheduled, periodic, event-triggered, provider-facing, and outbox-driven backend work is tenant-aware, idempotent, retry-safe, observable, recoverable, integration-aligned, and protected from duplicate business effects.
