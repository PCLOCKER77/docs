# BE-02 FastAPI Project Structure

> Physical Python and FastAPI project organization, package layout, dependency wiring, typed configuration, runtime lifecycle, and module structure standards.

---

# Document Control

| Field | Value |
|---|---|
| Document ID | BE-02 |
| Document Name | FastAPI Project Structure |
| Folder | 10_Backend_Engineering |
| Product | Digitize by OreeOn Technologies Pvt. Ltd. |
| Status | Design Draft |
| Governing Standard | BE-00_Backend_Engineering_Standards.md |
| Owner | Backend Engineering |
| Reviewers | Backend, Architecture, DevOps, Security, QA |
| Version | 1.0 |
| Last Updated | 2026-07-26 |

---

# 1. Purpose

This document defines the physical Python and FastAPI project structure for the Digitize backend.

It establishes package layout, module organization, routing structure, dependency wiring, typed configuration, application bootstrap, lifespan behavior, migration-directory relationship, test placement, scripts, and architecture enforcement boundaries.

---

# 2. BE-00 Inheritance

This document inherits `BE-00_Backend_Engineering_Standards.md`.

This document does not redefine domain rules, repository rules, tenant rules, authorization rules, logging rules, background-job rules, or release-readiness standards. It defines where FastAPI and Python implementation artifacts shall live and how framework-specific concerns shall be wired at controlled boundaries.

---

# 3. Scope

This document covers:

- Root backend repository structure.
- `src` layout.
- Main FastAPI application package layout.
- Capability-oriented module structure.
- Router, schema, service, domain, repository, query, integration, and worker placement.
- Shared package restrictions.
- Dependency injection structure.
- Application bootstrap and lifespan behavior.
- Middleware and exception-handler registration.
- Database session wiring.
- Typed settings and environment ownership.
- Test, migration, script, and administrative-command placement.
- Import rules, naming conventions, circular import prevention, and static architecture enforcement.

---

# 4. Out of Scope

This document does not define:

- Business rules.
- API endpoint catalogues.
- Database schemas.
- Provider-specific contracts.
- Deployment environment topology.
- Kubernetes configuration.
- CI/CD implementation.
- Production runbooks.

---

# 5. Source Alignment

| Source Area | Alignment |
|---|---|
| BE-00 | Framework isolation, configuration, dependency, security, and lifecycle standards |
| BE-01 | Logical layer model, dependency direction, runtime lifecycle, schema ownership split |
| API-00 to API-26 | Router and schema implementation must reflect approved API contracts |
| IC-00 to IC-17 | Correlation, request, tenant, integration, provider, retry, and observability needs |
| DB-00 to DB-22 | Migration relationship, repository infrastructure, and persistence boundaries |
| TA-00 to TA-10 | Runtime, security, observability, and deployment assumptions |

---

# 6. Project Structure Principles

FastAPI project structure shall follow these principles:

- Keep framework-specific wiring at API, bootstrap, middleware, and dependency boundaries.
- Keep application and domain services reusable outside HTTP request execution.
- Organize business capability modules consistently.
- Separate API schemas, domain models, persistence models, event payloads, provider models, and reporting projections.
- Keep shared utilities infrastructure-focused.
- Make dependency direction visible through package structure.
- Support testability without requiring production runtime infrastructure.
- Avoid selecting unapproved infrastructure providers or background-job frameworks.

---

# 7. Recommended Root Backend Structure

The recommended backend repository structure is:

```text
backend/
├── pyproject.toml
├── README.md
├── src/
│   └── digitize_backend/
├── migrations/
├── tests/
├── scripts/
├── docs/
└── tools/
```

This is a source-structure standard, not source code. The final implementation may adapt names where needed, but shall preserve the ownership boundaries defined here.

---

# 8. `src` Layout

The backend shall prefer a `src` layout to reduce accidental imports from the working directory.

```text
src/
└── digitize_backend/
    ├── main.py
    ├── app_factory.py
    ├── api/
    ├── core/
    ├── modules/
    ├── db/
    ├── integrations/
    ├── workers/
    ├── queries/
    ├── observability/
    └── shared/
```

The package name may be adjusted during implementation, but it shall be stable after adoption.

---

# 9. Main Application Package Layout

| Package | Responsibility |
|---|---|
| `main.py` | ASGI application entrypoint |
| `app_factory.py` | FastAPI application creation, bootstrap, middleware, routers, exception handlers, lifespan registration |
| `api/` | API router aggregation, version registration, common HTTP boundary dependencies |
| `core/` | Typed settings, security primitives, dependency providers, common exceptions |
| `modules/` | Capability-oriented business modules |
| `db/` | Engine/session wiring, repository infrastructure, migration integration hooks |
| `integrations/` | Provider-neutral adapter interfaces and implementations |
| `workers/` | Background workers, scheduled processors, outbox processors |
| `queries/` | Shared read-optimized query infrastructure where approved |
| `observability/` | Logging, metrics, tracing, health, readiness, diagnostics |
| `shared/` | Infrastructure-safe shared utilities only |

Shared packages shall not contain hidden business logic.

---

# 10. Capability Module Structure

Each capability module should use a consistent internal structure:

```text
modules/<capability>/
├── routes.py
├── schemas.py
├── application_services.py
├── domain_services.py
├── domain_policies.py
├── repositories.py
├── queries.py
├── persistence_models.py
├── events.py
├── permissions.py
├── errors.py
└── tests/
```

Large modules may split these files into subpackages when complexity justifies it.

Capability module names shall align with Functional Requirements and API Collections.

---

# 11. Router Organization

Routers shall:

- Be grouped by capability module.
- Be versioned according to approved API versioning.
- Use approved prefixes and tags.
- Attach authentication and tenant dependencies consistently.
- Delegate business behavior to application services.
- Avoid direct repository access.
- Avoid direct provider SDK usage.
- Avoid reusable domain decisions.

Router implementation behavior is owned by BE-07.

---

# 12. Request and Response Schema Placement

Request and response schemas shall live with the owning capability module unless explicitly shared.

Schema organization is owned by BE-02.

Schema behavior at the API boundary is owned by BE-07.

Schemas shall represent transport contracts and shall not be treated as domain models or persistence models.

---

# 13. Service Placement

Application services shall be placed in capability modules and shall orchestrate approved use cases.

Domain services and domain policies shall be placed near the business capability they govern.

Application services and domain services shall not import FastAPI routers, HTTP request objects, HTTP response objects, FastAPI dependency decorators, database sessions, provider SDKs, or worker framework objects.

---

# 14. Repository and Query Placement

Repositories shall be placed with the module or aggregate that owns the persisted business state.

Query services may be placed with the owning module or in approved read-model/query packages where cross-aggregate reads are required.

Query services shall remain tenant-aware, authorization-aware, and side-effect free.

---

# 15. Persistence Model Placement

Persistence models shall live in a controlled package owned by the module or database infrastructure boundary.

Persistence models shall not be returned directly from public API endpoints.

ORM model changes shall coordinate with Database Design and migration governance.

ORM implementation shall use SQLAlchemy per `DR-007_SQLAlchemy_Alembic_Data_Access_Baseline.md`.

---

# 16. Integration Adapter Placement

Integration adapters shall live under `integrations/` or a module-specific integration package where ownership is clearer.

Adapter interfaces shall be provider neutral.

Provider SDK details shall not leak into domain services.

---

# 17. Background Worker Placement

Background workers, scheduled processors, and outbox processors shall live under `workers/` or a module-owned worker package.

Worker code shall invoke application services or outbox processor components through approved interfaces.

Worker implementation shall use Celery with Redis broker per `DR-009_Celery_Background_Worker_Baseline.md`.

---

# 18. Shared Package Restrictions

Shared packages may contain:

- Common value helpers.
- Infrastructure-neutral constants.
- Error base classes.
- Safe serialization helpers.
- Observability helpers.
- Framework-neutral test utilities.

Shared packages must not contain:

- Module-specific business rules.
- Hidden authorization logic.
- Hidden tenant logic.
- Provider-specific business decisions.
- Cross-module mutation shortcuts.

---

# 19. Dependency Injection Structure

FastAPI dependency injection shall be used for framework-bound concerns:

- Authenticated principal resolution.
- Tenant context resolution.
- Request ID and correlation ID extraction.
- Database session provision.
- Application service wiring.
- Query service wiring.
- Configuration access.

Dependency functions shall translate framework-specific state into framework-independent inputs before service execution.

---

# 20. Application Bootstrap Convention

FastAPI bootstrap shall:

- Create the application instance.
- Load typed settings.
- Validate startup configuration.
- Register middleware.
- Register exception handlers.
- Register routers.
- Register health and readiness endpoints.
- Initialize observability hooks.
- Initialize worker and outbox processor hooks where applicable.
- Prepare lifecycle resources.

Bootstrap must not contain business rules.

---

# 21. Middleware Registration

Middleware may handle:

- Request ID and correlation ID establishment.
- Secure header behavior where approved.
- Logging context attachment.
- Timing and latency measurement.
- CORS where approved.

Middleware must not implement business authorization or tenant ownership decisions.

---

# 22. Exception Handler Registration

Exception handlers shall map controlled errors to approved API responses.

Exception handlers shall:

- Avoid stack trace exposure.
- Preserve request and correlation identifiers.
- Apply safe error messages.
- Delegate detailed error taxonomy ownership to BE-08.

---

# 23. Lifespan Startup and Shutdown

Startup shall validate:

- Required typed settings.
- Environment identity.
- Database connectivity where appropriate.
- Migration compatibility status where appropriate.
- Secret references.
- Provider configuration completeness where applicable.
- Observability configuration.
- Worker and outbox processor readiness where applicable.

Shutdown shall release:

- Database sessions and pools.
- Worker resources.
- Provider clients.
- Metrics or trace exporters.
- In-flight request resources where applicable.
- Background-job resources where applicable.

---

# 24. Database Session Wiring

Database sessions shall be provided through controlled infrastructure wiring.

API route handlers may receive session dependencies only to pass them into application service boundaries or repository infrastructure.

Domain services shall not own database sessions.

Repositories shall participate in caller-owned transactions according to BE-04.

---

# 25. Configuration and Typed Settings

Typed settings shall define:

- Environment name.
- Service name.
- API version.
- Database connection references.
- Authentication and token verification configuration.
- Secret references.
- Feature flags.
- Provider endpoint references.
- Logging and metrics settings.
- Security-related runtime settings.

Configuration values shall be immutable after application startup unless runtime reload is explicitly designed and approved.

---

# 26. Environment Ownership

Backend environments shall be distinguished as:

- Local.
- Development.
- Test.
- Staging.
- Production.

Environment variables shall have an owner, description, default behavior, validation rule, and secret classification where applicable.

Secrets shall be referenced, not embedded.

---

# 27. Feature Flags

Feature flags shall:

- Have an owner.
- Have a safe default.
- Be environment-aware.
- Be tenant-aware where applicable.
- Avoid bypassing authorization or tenant isolation.
- Be removed when obsolete.

Feature flags shall be stored as governed platform configuration in PostgreSQL and may use Redis cache snapshots per `DR-006_PostgreSQL_Database_Baseline.md` and `DR-008_Redis_Cache_Baseline.md`.

---

# 28. Import Rules and Circular Import Prevention

| Import Direction | Standard |
|---|---|
| Routes import schemas and services | Allowed |
| Routes import repositories directly | Not allowed |
| Services import repositories | Allowed |
| Services import domain services and policies | Allowed |
| Services import query services | Allowed for approved read use cases |
| Domain imports FastAPI | Not allowed |
| Domain imports database sessions | Not allowed |
| Repository imports routes | Not allowed |
| Repository imports provider SDKs | Not allowed |
| Query services mutate business state | Not allowed |

Circular module dependencies are prohibited.

---

# 29. Python Naming Conventions

Python naming shall be stable and readable:

| Artifact | Convention |
|---|---|
| Packages | `snake_case` |
| Modules | `snake_case.py` |
| Classes | `PascalCase` |
| Functions | `snake_case` |
| Constants | `UPPER_SNAKE_CASE` |
| Test files | `test_<behavior>.py` |

Specific formatter and linter configuration is owned by implementation tooling.

---

# 30. Test Directory Structure

Tests may be organized by layer and capability:

```text
tests/
├── unit/
├── services/
├── repositories/
├── api/
├── security/
├── tenant_isolation/
├── workers/
├── integrations/
└── regression/
```

Module-local tests may also exist when they improve ownership.

---

# 31. Migration Directory Relationship

The `migrations/` directory shall be treated as the implementation home for database migrations after a migration framework is approved.

Migration implementation shall use Alembic per `DR-007_SQLAlchemy_Alembic_Data_Access_Baseline.md`.

Migration contents shall align with Database Design and shall not become the source of truth for schema ownership.

---

# 32. Scripts and Administrative Commands

Administrative scripts shall live under `scripts/` or a controlled administrative-command package.

Scripts must:

- Use typed settings.
- Validate environment.
- Avoid hardcoded secrets.
- Respect tenant context where tenant-scoped.
- Produce audit or diagnostic evidence where required.
- Avoid bypassing approved service boundaries for business mutations.

---

# 33. Static Analysis and Architecture Enforcement

Architecture enforcement should include:

- Import boundary checks.
- Circular dependency checks.
- Formatting checks.
- Type checks where adopted.
- Security scanning where adopted.
- Secret scanning.
- Test discovery validation.

The baseline CI enforcement shall run through GitHub Actions per `DR-012_GitHub_Actions_CI_CD_Baseline.md`. Backend quality checks should include Ruff formatting/linting, mypy where typing coverage is adopted, Bandit security scanning, dependency vulnerability scanning, secret scanning, import-boundary checks, and test discovery validation.

---

# 34. Traceability Requirements

Project structure decisions shall trace to:

- BE-00 framework-isolation and configuration standards.
- BE-01 layer and dependency model.
- API Collections for route and schema organization.
- Database Design for migration and persistence ownership.
- Integration Contracts for worker and adapter placement.

Traceability sources: see [docs/10_Backend_Engineering/BE-TRACEABILITY_MAPPINGS.md](BE-TRACEABILITY_MAPPINGS.md) — primary sources include [docs/99_Decision_Records/DR-005_Backend_FastAPI_Baseline.md](../99_Decision_Records/DR-005_Backend_FastAPI_Baseline.md), [docs/99_Decision_Records/DR-007_SQLAlchemy_Alembic_Data_Access_Baseline.md](../99_Decision_Records/DR-007_SQLAlchemy_Alembic_Data_Access_Baseline.md), [docs/99_Decision_Records/DR-009_Celery_Background_Worker_Baseline.md](../99_Decision_Records/DR-009_Celery_Background_Worker_Baseline.md), and [docs/99_Decision_Records/DR-012_GitHub_Actions_CI_CD_Baseline.md](../99_Decision_Records/DR-012_GitHub_Actions_CI_CD_Baseline.md).

---

# 35. Acceptance Criteria

This document is acceptable when:

- Root backend structure is defined.
- `src` layout and main application package ownership are defined.
- Capability module structure is defined.
- Router, schema, service, repository, query, persistence, integration, and worker placement are defined.
- Dependency injection and bootstrap boundaries are defined.
- Lifespan startup and shutdown responsibilities are defined.
- Typed settings, environment variables, secrets, and feature flag ownership are defined.
- Import, naming, test, migration, script, and architecture-enforcement rules are defined.

---

# 36. Freeze Rule

This document may be frozen only after BE-01 confirms architecture compatibility, BE-03 confirms framework-independent services, BE-04 confirms persistence placement, and BE-07 confirms API boundary behavior.

---

# 37. Summary

BE-02 defines the FastAPI project structure baseline for Digitize.

It keeps framework wiring at controlled boundaries, organizes backend code by capability, protects architecture dependency direction, and provides a predictable implementation structure for APIs, services, repositories, query services, integrations, workers, configuration, tests, migrations, and scripts.
