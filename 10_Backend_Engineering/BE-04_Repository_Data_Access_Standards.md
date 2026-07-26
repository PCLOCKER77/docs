# BE-04 Repository Data Access Standards

> Repository contracts, persistence access, SQLAlchemy session behavior, tenant filtering, transaction participation, query services, locking, migration compatibility, and persistence error handling standards.

---

# Document Control

| Field | Value |
|---|---|
| Document ID | BE-04 |
| Document Name | Repository Data Access Standards |
| Folder | 10_Backend_Engineering |
| Product | Digitize by OreeOn Technologies Pvt. Ltd. |
| Status | Design Draft |
| Governing Standard | BE-00_Backend_Engineering_Standards.md |
| Owner | Backend Engineering and Database Engineering |
| Reviewers | Backend, Database, Architecture, Security, QA |
| Version | 1.0 |
| Last Updated | 2026-07-26 |

---

# 1. Purpose

This document defines repository and data access standards for Digitize backend implementation.

It governs repository boundaries, persistence access, session participation, tenant filtering, query services, locking, migration compatibility, outbox persistence, and persistence error handling without redefining database schemas.

---

# 2. BE-00 Inheritance

This document inherits `BE-00_Backend_Engineering_Standards.md`.

This document defines repository-specific implementation responsibilities. It does not redefine common transaction, tenant, logging, security, testing, or database design standards.

---

# 3. Scope

This document covers:

- Repository purpose and boundaries.
- Repository interface and implementation rules.
- Module and aggregate ownership.
- Caller-owned transaction participation.
- SQLAlchemy session usage and approved ORM session behavior.
- Commit, rollback, and flush rules.
- Unit-of-work relationship.
- Tenant filtering for Organization, Facility, and Site.
- Cross-tenant protection and administrative override handling.
- Resource ownership validation.
- Query ownership and query-service rules.
- List, search, filter, sorting, pagination, reporting, dashboard, read-model, and projection patterns.
- ORM, domain, and API schema boundaries.
- Persistence error classification.
- Locking, concurrency, race-condition, N+1, performance, bulk-operation, soft-delete, audit, outbox, migration, and repository testing standards.

---

# 4. Out of Scope

This document does not define:

- Database tables, columns, indexes, or schema ownership.
- Migration policy ownership.
- Business rules.
- API endpoint catalogues.
- Provider-specific contracts.
- UI behavior.

Database Design remains the source of truth for schema and migration policy.

---

# 5. Source Alignment

| Source Area | Alignment |
|---|---|
| DB-00 to DB-22 | Schema, tenant model, constraints, indexing, migration, reporting, outbox, audit |
| DB-12 | Migration strategy, backfill, deployment ordering, rollback, online migration governance |
| DB-18 and DB-20 | Database testing and SQL coding standards |
| API-00 to API-26 | Data needed by API contracts |
| IC-09 and IC-17 | Outbox and release-readiness persistence behavior |
| BE-00 | Repository, transaction, tenant, migration, and security standards |
| BE-01 | Repository, query-service, outbox repository, and module interaction architecture |
| BE-03 | Application-service transaction ownership and repository participation |

---

# 6. Repository Purpose and Boundaries

Repositories are persistence boundaries.

Repositories shall:

- Own data access for a module, aggregate, or approved persistence concern.
- Encapsulate query construction.
- Apply tenant filters.
- Participate in caller-owned transactions.
- Return domain-appropriate objects or data transfer shapes.
- Convert persistence failures into controlled repository errors.
- Support outbox record persistence inside the caller-owned business transaction where required.

Repositories must not:

- Contain business decision logic beyond persistence concerns.
- Call external providers.
- Depend on API route handlers.
- Silently commit transactions.
- Mutate another module's tables without approved ownership.

---

# 7. Repository Interface Rules

Repository interfaces shall define:

- Owned entity, aggregate, or persistence concern.
- Supported read operations.
- Supported write operations.
- Tenant-scope requirements.
- Transaction participation expectations.
- Locking requirements.
- Error categories.
- Bulk-operation behavior where applicable.
- Performance expectations for list, search, export, and reporting queries.

Interfaces shall be stable for services that depend on them.

---

# 8. Repository Implementation Rules

Repository implementations shall:

- Use approved persistence infrastructure.
- Keep SQL or ORM details out of API layers.
- Apply tenant filtering consistently.
- Avoid N+1 query patterns.
- Avoid raw database error leakage.
- Map persistence errors to controlled repository errors.
- Avoid hidden side effects.
- Avoid direct integration adapter calls.

Repository implementation shall use SQLAlchemy and migration implementation shall use Alembic per `DR-007_SQLAlchemy_Alembic_Data_Access_Baseline.md`.

---

# 9. Module and Aggregate Ownership

Each module owns its business state.

Repository ownership shall align with:

- Functional requirement module.
- Database design ownership.
- API capability module.
- Domain consistency boundary.

A module shall not directly mutate another module's tables. Cross-module behavior shall use approved service boundaries, query contracts, or events.

---

# 10. Session Lifecycle

SQLAlchemy session usage, or equivalent approved ORM session behavior, shall follow these rules:

- Sessions are provided by infrastructure or dependency wiring.
- Session lifetime is controlled by application or request execution.
- Application services own transaction boundaries unless explicitly approved otherwise.
- Repositories participate in the provided session.
- Sessions shall not be stored in long-lived global state.
- Sessions shall not escape into API response models.

SQLAlchemy is the approved ORM baseline per `DR-007_SQLAlchemy_Alembic_Data_Access_Baseline.md`.

---

# 11. Commit, Rollback, and Flush Rules

Repositories shall not silently commit.

Commit and rollback ownership belongs to the caller-owned transaction boundary.

Repositories may flush when required to:

- Obtain generated identifiers.
- Validate persistence constraints early.
- Prepare dependent writes inside the same transaction.

Flush shall not be treated as commit.

Rollback shall be performed by the transaction owner.

---

# 12. Unit-of-Work Relationship

The unit of work represents the atomic persistence boundary for a business operation.

Application services coordinate unit-of-work behavior.

Repositories participate in the unit of work by performing reads and writes through the provided session or persistence context.

Outbox records shall be written within the same unit of work as the related state change.

---

# 13. Tenant Filter Enforcement

Tenant-scoped repository operations shall enforce tenant filters.

Filters shall include applicable:

- Organization.
- Facility.
- Site.
- Resource ownership.
- Approved administrative override scope.

Tenant filters shall not be optional flags that callers can omit accidentally.

---

# 14. Cross-Tenant Protection

Repositories shall protect against:

- Cross-tenant reads.
- Cross-tenant writes.
- Cross-tenant updates.
- Cross-tenant deletes.
- Cross-tenant search results.
- Cross-tenant reporting projections.
- Cross-tenant existence leakage through error responses.

Missing tenant-scoped resources shall return tenant-safe not-found or forbidden behavior through the service/API error mapping path.

---

# 15. Administrative Override Handling

Administrative override behavior shall be explicit.

Repositories shall not decide override eligibility.

Application and authorization services decide whether an override is allowed. Repositories apply the effective, approved tenant scope and preserve enough information for audit where required.

---

# 16. Resource Ownership Validation

Repositories may support resource ownership validation by retrieving tenant-scoped resources through approved filters.

Resource ownership decisions are coordinated by services and authorization logic.

Repositories shall not leak whether a resource exists outside the caller's allowed tenant scope.

---

# 17. Query Ownership and Query Services

Repositories own module-owned query construction.

Query services may coordinate:

- Read-optimized queries.
- Search.
- List views.
- Dashboards.
- Reports.
- Cross-aggregate views.
- Read models and projections.

Query services shall:

- Use explicitly owned query contracts.
- Remain tenant-aware.
- Avoid bypassing authorization.
- Avoid hidden state changes.
- Preserve approved API filtering, sorting, pagination, and response behavior.

---

# 18. List, Search, Filter, Sorting, and Pagination Patterns

List and search operations shall:

- Apply tenant filters first.
- Apply permission-sensitive field restrictions.
- Support approved pagination.
- Support approved sorting.
- Support approved filtering.
- Avoid unbounded result sets.
- Avoid returning restricted fields.
- Preserve stable ordering where pagination requires it.

Search shall not reveal cross-tenant resource existence.

---

# 19. Reporting, Dashboard, Read Model, and Projection Rules

Reporting and dashboards may use read models or projections where approved by Database Design.

Read models shall:

- Define authoritative source data.
- Preserve tenant isolation.
- Define refresh or update behavior.
- Define staleness expectations.
- Avoid hidden business mutations.

Reports and exports shall preserve Organization, Facility, and Site scoping.

---

# 20. Representation Boundaries

Repositories shall not expose persistence models directly to public APIs.

Backend implementation shall keep separate:

- API schemas.
- Domain models.
- Persistence models.
- Event payloads.
- Reporting projections.

Mapping between representations shall occur at controlled service or mapper boundaries.

---

# 21. Persistence Error Classification

Repository errors shall be controlled and mappable.

| Error Type | Expected Handling |
|---|---|
| Unique constraint error | Conflict |
| Foreign-key error | Validation or conflict |
| Missing tenant-scoped resource | Tenant-safe not found or forbidden |
| Concurrency conflict | Conflict |
| Lock timeout | Retryable or conflict based on operation |
| Deadlock | Retryable infrastructure error where approved |
| Migration incompatibility | Startup or release-readiness failure |
| Unexpected database error | Generic server error with safe diagnostics |

---

# 22. Locking, Concurrency, and Race Conditions

Repositories shall identify operations requiring:

- Optimistic locking.
- Pessimistic locking.
- Unique constraint protection.
- Idempotency record checks.
- Conflict detection.
- Retry-safe persistence.

Race-condition handling shall be tested for critical operations such as payment, membership activation, attendance, capacity, and license entitlement.

---

# 23. N+1 and Query Performance Expectations

Repository and query service implementation shall avoid N+1 query patterns.

Performance-sensitive paths shall define:

- Expected cardinality.
- Pagination limits.
- Index expectations from Database Design.
- Join or projection strategy.
- Export behavior for large data.

Query tuning shall align with Database Design and DB-13.

---

# 24. Bulk Operation Rules

Bulk operations shall:

- Be explicitly approved by API and Functional Requirements.
- Preserve tenant isolation.
- Define partial success behavior.
- Define transaction boundaries.
- Define idempotency where retry-prone.
- Define error reporting.
- Avoid unbounded memory or transaction usage.

---

# 25. Soft Delete and Lifecycle Data

Where soft delete or lifecycle status exists, repositories shall:

- Apply approved visibility filters.
- Preserve audit and retention needs.
- Avoid returning inactive records unless requested and authorized.
- Avoid physically deleting retained records unless approved.

---

# 26. Audit Data Persistence Boundaries

Audit persistence shall align with audit and compliance requirements.

Repositories may write audit-related records only when the owning service has identified the action and required context.

Audit logs shall not replace business state or outbox records.

---

# 27. Outbox Repository Behavior

Outbox repository methods shall:

- Write outbox records in the same transaction as related business state changes.
- Include event type.
- Include aggregate or resource reference.
- Include tenant metadata.
- Include correlation metadata.
- Include payload version.
- Include publication and retry state.

Outbox processors publish committed records after transaction completion.

---

# 28. Migration Coordination

Backend repository changes shall coordinate with migration governance.

Repository changes shall identify:

- ORM model changes.
- Expand-and-contract sequencing.
- Backfill requirements.
- Deployment-ordering constraints.
- Rollback limitations.
- Zero-downtime compatibility.

Database Design owns schema and migration policy. Backend Engineering owns application compatibility with that policy.

---

# 29. Repository Testing

Repository and query tests shall cover:

- Tenant filtering.
- Cross-tenant denial.
- Query correctness.
- Pagination and sorting.
- Search behavior.
- Persistence success.
- Persistence error mapping.
- Transaction participation.
- Flush behavior where used.
- Locking and concurrency.
- Outbox repository behavior.
- Migration compatibility assumptions.
- N+1 prevention for critical paths.

---

# 30. Prohibited Patterns

The following are prohibited:

- Business logic in repositories.
- Silent commits inside repositories.
- Returning persistence models directly from APIs.
- Tenant filters implemented as optional caller-controlled flags.
- Cross-module table mutation.
- Provider SDK calls from repositories.
- Unbounded list queries.
- Cross-tenant existence leakage.
- Ignoring migration ordering.

---

# 31. Traceability Requirements

Repository and query design shall trace to:

- Database Design for persistence ownership.
- Functional Requirements for business capability ownership.
- API Collections for read/write behavior.
- Integration Contracts for outbox and event persistence.
- BE-01 and BE-03 for layer and transaction ownership.

Traceability sources: see [docs/10_Backend_Engineering/BE-TRACEABILITY_MAPPINGS.md](BE-TRACEABILITY_MAPPINGS.md) — primary sources include [docs/06_Database_Design/README.md](../06_Database_Design/README.md), [docs/06_Database_Design/DB-11_Database_DDL_DML_Scripts.md](../06_Database_Design/DB-11_Database_DDL_DML_Scripts.md), and [docs/99_Decision_Records/DR-007_SQLAlchemy_Alembic_Data_Access_Baseline.md](../99_Decision_Records/DR-007_SQLAlchemy_Alembic_Data_Access_Baseline.md).

---

# 32. Acceptance Criteria

This document is acceptable when:

- Repository purpose, interface, implementation, and ownership rules are defined.
- Transaction, session, commit, rollback, flush, and unit-of-work behavior are defined.
- Tenant filters, cross-tenant protection, override handling, and resource ownership validation are defined.
- Query services, reporting, dashboards, read models, pagination, search, and performance expectations are defined.
- Representation boundaries, persistence errors, locking, concurrency, bulk operations, soft delete, audit, outbox, and migration compatibility are defined.
- Repository tests and prohibited patterns are defined.

---

# 33. Freeze Rule

This document may be frozen only after BE-03 confirms transaction ownership, BE-06 confirms tenant enforcement, BE-09 confirms outbox repository expectations, and Database Design migration alignment is reviewed.

---

# 34. Summary

BE-04 defines the repository and data access baseline for Digitize.

It ensures persistence access is tenant-aware, transaction-safe, migration-compatible, observable, testable, and separated from business decisions, API schemas, provider contracts, and cross-module shortcuts.
