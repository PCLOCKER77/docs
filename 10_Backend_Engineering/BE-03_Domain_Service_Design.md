# BE-03 Domain Service Design

> Application-service orchestration, domain-service responsibilities, commands, queries, state transitions, transactions, policies, side effects, and use-case execution standards.

---

# Document Control

| Field | Value |
|---|---|
| Document ID | BE-03 |
| Document Name | Domain Service Design |
| Folder | 10_Backend_Engineering |
| Product | Digitize by OreeOn Technologies Pvt. Ltd. |
| Status | Design Draft |
| Governing Standard | BE-00_Backend_Engineering_Standards.md |
| Owner | Backend Engineering |
| Reviewers | Backend, Architecture, Business Analysis, Functional, QA |
| Version | 1.0 |
| Last Updated | 2026-07-26 |

---

# 1. Purpose

This document defines how application services, domain services, domain policies, commands, queries, use-case orchestration, transactions, state transitions, and side effects shall be implemented in the Digitize backend.

It keeps business behavior out of routers and repositories while preserving framework isolation, tenant awareness, transaction correctness, and testability.

---

# 2. BE-00 Inheritance

This document inherits `BE-00_Backend_Engineering_Standards.md`.

This document does not redefine common backend standards for authentication, authorization, tenant context, persistence, logging, idempotency, observability, or release readiness. It defines how services apply those standards during business behavior execution.

---

# 3. Scope

This document covers:

- Application service responsibilities.
- Domain service responsibilities.
- Domain policy design.
- Use-case-oriented service design.
- Command and query responsibilities.
- Transaction and unit-of-work ownership.
- Authorization checkpoints.
- Tenant-aware service execution.
- Business-rule execution.
- State transitions and lifecycle operations.
- Aggregate and consistency-boundary guidance.
- Domain model versus persistence model separation.
- Service input and output contracts.
- Idempotent command handling.
- External provider coordination.
- Outbox record creation.
- Cross-module orchestration.
- Compensation, reconciliation, long-running workflow boundaries, side effects, errors, observability, testing, and anti-patterns.

---

# 4. Out of Scope

This document does not define:

- FastAPI routing and dependency injection.
- API endpoint catalogues.
- Repository session implementation.
- Database schemas.
- Provider-specific SDK behavior.
- Background-worker framework implementation.
- UI behavior.

---

# 5. Source Alignment

| Source Area | Alignment |
|---|---|
| BA-02 and BA-04 | Business rules and business process flows |
| FR-01 to FR-21 | Module behavior and acceptance expectations |
| API-01 to API-14 | Use cases exposed through module APIs |
| API-23 and API-24 | Access control and state/workflow behavior |
| DB-00 to DB-22 | Entity ownership, transaction impact, audit, and outbox data |
| IC-00 to IC-17 | Integration, retry, compensation, reconciliation, and observability behavior |
| UX-02 and UX-05 | User-flow outcomes that backend services support |
| BE-00 | Frozen backend service, transaction, validation, idempotency, and framework-isolation standards |
| BE-01 | Layer model, request flow, command/query responsibilities, and outbox architecture |

---

# 6. Service Responsibility Matrix

| Service Type | Responsibility |
|---|---|
| Application Service | Coordinates one approved use case, transaction, authorization checkpoints, tenant-aware execution, repository calls, domain services, outbox records, and result assembly |
| Domain Service | Executes reusable business rules, domain decisions, state transitions, calculations, and lifecycle rules |
| Domain Policy | Evaluates focused eligibility, restriction, entitlement, or state-guard rules |
| Query Service | Coordinates tenant-aware read-only queries, projections, dashboards, reports, search, and cross-aggregate views without hidden state changes |
| Integration Coordination Service | Coordinates provider-neutral adapter invocation where immediate external response is approved |

Services shall be named by business capability and use-case responsibility.

---

# 7. Application Service Responsibilities

Application services shall:

- Coordinate a single approved use case.
- Receive framework-independent inputs.
- Coordinate tenant-aware execution.
- Invoke coarse authorization and resource-level authorization where applicable.
- Resolve required repositories, query services, domain services, and policies.
- Own business transaction boundaries.
- Coordinate command or query flow.
- Persist state through repositories.
- Create outbox records where committed business events are required.
- Invoke provider-neutral adapter interfaces only when immediate provider response is approved.
- Return application-level results suitable for API response mapping.

Application services must not:

- Accept FastAPI request or response objects.
- Implement reusable domain decision logic.
- Silently bypass authorization.
- Mutate another module's tables directly.

---

# 8. Domain Service Responsibilities

Domain services shall:

- Implement reusable business rules and domain decisions.
- Validate lifecycle and state transitions.
- Evaluate domain invariants.
- Perform calculations and eligibility decisions.
- Remain independent of HTTP, FastAPI, database sessions, provider SDKs, and background-worker framework objects.
- Return domain-level results or controlled domain errors.

Domain services must not:

- Own transaction commits.
- Call provider SDKs directly.
- Persist data directly.
- Read FastAPI dependency state.
- Depend on UI visibility rules.

---

# 9. Application Versus Domain Service Boundary

| Concern | Application Service | Domain Service |
|---|---|---|
| Use-case orchestration | Owns | Supports |
| Transaction boundary | Owns | Does not own |
| Repository invocation | Owns | Does not own |
| Business decision | Coordinates | Owns reusable decision |
| State transition rule | Invokes | Evaluates |
| Outbox record creation | Owns | May indicate event need |
| Provider adapter coordination | Owns through interface | Does not own |
| HTTP framework dependency | Not allowed | Not allowed |

---

# 10. Use-Case-Oriented Design

Application services should be organized around approved use cases such as:

- Create organization.
- Activate membership.
- Record attendance.
- Initiate payment.
- Generate report export.
- Send campaign.
- Resolve support ticket.

Use-case services shall define:

- Actor and tenant context.
- Input contract.
- Preconditions.
- Authorization checkpoints.
- Domain decisions.
- Transaction boundary.
- State changes.
- Outbox or side effects.
- Output contract.
- Error behavior.

---

# 11. Command Responsibilities

Commands change business state.

Command handlers shall:

- Validate required preconditions.
- Apply coarse authorization before execution.
- Load required resources.
- Apply resource-level authorization.
- Execute domain rules.
- Own or participate in transaction orchestration.
- Persist state through repositories.
- Create outbox records inside the same business transaction where required.
- Return deterministic outcomes.

Retry-prone commands shall be idempotent.

---

# 12. Query Responsibilities

Queries read business state.

Query services shall:

- Remain tenant-aware.
- Avoid bypassing authorization.
- Avoid hidden state changes.
- Support search, list, detail, dashboard, reporting, projection, and cross-aggregate view needs.
- Preserve approved API filtering, sorting, pagination, and response behavior.
- Use explicitly owned query contracts for cross-module reads.

Command/query separation does not require full CQRS infrastructure.

---

# 13. Transaction and Unit-of-Work Ownership

Application services own business transaction boundaries unless explicitly approved otherwise.

Transaction boundaries shall:

- Begin after authentication, tenant context, boundary validation, and coarse authorization.
- Include state changes required for the business operation.
- Include outbox record creation when committed business events are required.
- Avoid long-running provider calls.
- Roll back on failure.
- Commit only after required persistence changes are complete.

Repositories participate in caller-owned transactions and must not silently commit.

---

# 14. Authorization Checkpoint Responsibilities

Authorization shall follow the two-stage BE-01 model.

| Authorization Stage | Service Responsibility |
|---|---|
| Coarse authorization | Confirm caller may attempt the operation |
| Resource-level authorization | Confirm caller may act on the loaded resource based on ownership, tenant scope, state, entitlement, or record-specific access |

Resource-level authorization shall occur after required resource loading and before domain rules mutate state.

---

# 15. Tenant-Aware Service Execution

Services shall:

- Receive resolved tenant context.
- Validate resource ownership where required.
- Pass tenant context to repositories and query services.
- Include tenant metadata in outbox records where required.
- Include tenant context in logs and audit handoff.
- Reject missing or conflicting tenant context for tenant-scoped operations.

Tenant hierarchy remains Platform -> Organization -> Facility -> Site.

---

# 16. Domain Policy Design

Domain policies shall be small, reusable, and testable.

Policy examples include:

- Membership eligibility.
- Attendance eligibility.
- Refund eligibility.
- Campaign send eligibility.
- Subscription entitlement.
- Support ticket transition eligibility.

Policies shall not own database transactions or provider calls.

---

# 17. State Transitions and Lifecycle Operations

State transitions shall align with API-24 and Functional Requirements.

State transition rules shall define:

- Allowed source state.
- Allowed target state.
- Actor permission.
- Tenant scope.
- Business condition.
- Audit requirement.
- Outbox event requirement.
- Failure behavior.

Forbidden transitions shall fail deterministically.

---

# 18. Aggregate and Consistency Boundary Guidance

Services shall identify the consistency boundary for each use case.

Strong consistency should be limited to the smallest reliable unit of work.

Cross-module consistency shall avoid hidden table mutation and should use explicit service interfaces, query contracts, events, or approved orchestration boundaries.

Long-running workflows shall avoid holding database transactions open.

---

# 19. Representation Boundaries

Services shall keep these representations separate:

- API request and response schemas.
- Domain models.
- Persistence models.
- Integration-provider models.
- Event payloads.
- Reporting projections.

Conversion between representations shall occur at controlled boundaries.

---

# 20. Service Input and Output Contracts

Service inputs should include:

- Actor or principal reference.
- Tenant context.
- Validated command or query data.
- Correlation ID.
- Idempotency key where required.

Service outputs should include:

- Business result.
- Result state.
- Resource reference.
- User-facing response data where appropriate.
- Generated event or outbox reference where applicable.

---

# 21. Idempotent Command Handling

Idempotent commands shall define:

- Idempotency key source.
- Key lifetime and retention.
- Duplicate-response behavior.
- Storage responsibility.
- Tenant scoping.
- Conflict behavior for mismatched duplicate requests.

Idempotency shall prevent duplicate business effects.

---

# 22. External Provider Coordination

Application services may invoke integration adapter interfaces synchronously only when the approved business flow requires an immediate provider response.

Examples include:

- Payment session creation.
- Authentication-provider verification.
- Real-time eligibility verification.

Retryable or non-immediate communication should use committed outbox or background-job processing.

Provider SDKs must not be used in domain services.

---

# 23. Outbox Record Creation

Application services shall create outbox records inside the same transaction as related business state changes.

Outbox processors publish committed records after transaction completion.

Domain services may indicate that a business event should be emitted, but application services own persistence coordination.

---

# 24. Cross-Module Orchestration

Cross-module orchestration shall:

- Use explicit application interfaces, query contracts, events, or approved service boundaries.
- Avoid circular module dependencies.
- Avoid direct mutation of another module's tables.
- Minimize cross-module transactions.
- Document ownership of resulting state.

---

# 25. Compensation and Reconciliation

Services shall identify when compensation or reconciliation is required.

Examples include:

- Payment confirmation failure.
- Provider callback mismatch.
- Report generation failure.
- Notification dispatch failure.
- Outbox publication failure.

Compensation and reconciliation behavior shall align with Integration Contracts.

---

# 26. Side-Effect Handling

Side effects shall be explicit.

Side effects may include:

- Audit event handoff.
- Outbox record creation.
- Background job scheduling.
- Provider adapter invocation.
- Notification scheduling.
- Report export initiation.

Side effects shall not be hidden inside repositories or domain policies.

---

# 27. Domain Error Design

Domain and application errors shall be controlled and mappable to approved API errors.

Error categories include:

- Business rule violation.
- Invalid state transition.
- Eligibility failure.
- Authorization failure.
- Tenant ownership failure.
- Idempotency conflict.
- Integration scheduling failure.
- Persistence conflict surfaced through repository boundary.

---

# 28. Service Observability

Services shall emit or hand off:

- Operation name.
- Correlation ID.
- Request ID.
- Actor reference.
- Tenant context.
- Outcome.
- Error category.
- Latency where measured.
- Outbox or job reference where applicable.

Sensitive data shall not be logged.

---

# 29. Service Testing Expectations

Service tests shall cover:

- Positive use cases.
- Business rule failures.
- Coarse authorization failures.
- Resource-level authorization failures.
- Tenant ownership failures.
- State transition failures.
- Transaction rollback behavior.
- Outbox record creation.
- Idempotency behavior.
- Query service tenant and authorization behavior.
- Compensation and reconciliation triggers where applicable.

---

# 30. Anti-Patterns

The following are prohibited:

- Business logic in routers.
- Business logic in repositories.
- Provider SDKs in domain services.
- Direct transaction commits from domain services.
- Passing HTTP objects into domain services.
- Hidden cross-module mutations.
- Long-running workflows inside open database transactions.
- UI visibility treated as authorization.

---

# 31. Traceability Requirements

Service design shall trace to:

- Functional Requirements for behavior.
- Business Analysis for rules and process flows.
- API Collections for command/query exposure.
- Database Design for persistence impact.
- Integration Contracts for outbox, retry, compensation, and reconciliation.
- UI/UX documents where service outcomes support user-facing flows.

Traceability sources: see [docs/10_Backend_Engineering/BE-TRACEABILITY_MAPPINGS.md](BE-TRACEABILITY_MAPPINGS.md) — primary sources include [docs/04_Functional_Requirements/FR-08_Membership_Management.md](../04_Functional_Requirements/FR-08_Membership_Management.md), [docs/04_Functional_Requirements/FR-09_Attendance_Management.md](../04_Functional_Requirements/FR-09_Attendance_Management.md), [docs/04_Functional_Requirements/FR-11_Trainer_Management.md](../04_Functional_Requirements/FR-11_Trainer_Management.md), [docs/07_API_Collections/API-24_API_State_and_Workflow_Contract.md](../07_API_Collections/API-24_API_State_and_Workflow_Contract.md), and [docs/08_Integration_Contracts/IC-09_Event_Outbox_Integration_Contract.md](../08_Integration_Contracts/IC-09_Event_Outbox_Integration_Contract.md).

---

# 32. Acceptance Criteria

This document is acceptable when:

- Application and domain service responsibilities are clearly separated.
- Use-case, command, query, policy, transaction, and unit-of-work rules are defined.
- Coarse and resource-level authorization responsibilities are defined.
- Tenant-aware execution is defined.
- State transition, aggregate, representation, idempotency, provider coordination, outbox, cross-module, compensation, and side-effect rules are defined.
- Service observability and testing expectations are defined.
- Anti-patterns are explicit.

---

# 33. Freeze Rule

This document may be frozen only after BE-01 confirms architecture compatibility, BE-04 confirms repository transaction participation, BE-05 confirms authorization checkpoint behavior, and BE-09 confirms outbox and background-job coordination.

---

# 34. Summary

BE-03 defines the service design baseline for Digitize backend implementation.

It keeps business behavior in application services, domain services, and policies; assigns transaction and outbox ownership clearly; separates commands from queries; protects tenant and authorization boundaries; and makes side effects, errors, observability, testing, and anti-patterns explicit.

