# BE-06 Tenant Context Implementation

> Tenant context resolution, validation, propagation, enforcement, logging, auditing, persistence, caching, background-job, integration, reporting, and cross-tenant protection standards.

---

# Document Control

| Field | Value |
|---|---|
| Document ID | BE-06 |
| Document Name | Tenant Context Implementation |
| Folder | 10_Backend_Engineering |
| Product | Digitize by OreeOn Technologies Pvt. Ltd. |
| Status | Design Draft |
| Governing Standard | BE-00_Backend_Engineering_Standards.md |
| Owner | Backend Engineering and Security Engineering |
| Reviewers | Security, Backend, Database, Architecture, QA |
| Version | 1.0 |
| Last Updated | 2026-07-26 |

---

# 1. Purpose

This document defines how tenant context is resolved, validated, propagated, enforced, logged, audited, persisted, cached, and carried into background and integration workflows in the Digitize backend.

It ensures Organization, Facility, and Site isolation is preserved across APIs, application services, repositories, query services, background jobs, outbox events, integration events, logs, audit records, cache keys, reports, exports, and administrative override paths.

---

# 2. BE-00 Inheritance

This document inherits `BE-00_Backend_Engineering_Standards.md`.

This document does not redefine database tenancy schema, API endpoint catalogues, role definitions, UI behavior, or infrastructure configuration. It defines backend tenant-context implementation responsibilities.

---

# 3. Scope

This document covers:

- Tenant-context principles.
- Tenant-context object and fields.
- Context sources, token claims, headers, route parameters, and server-side resolution.
- Context precedence and conflict detection.
- Organization, Facility, and Site validation.
- Context inheritance and narrowing.
- API dependency or middleware boundary.
- Application-service propagation.
- Repository and query-service enforcement.
- Cross-tenant denial and missing-context behavior.
- Platform-scoped operations and administrative overrides.
- Background jobs, scheduled jobs, outbox, events, integrations, logs, audit, cache, reports, exports, search, pagination, leakage prevention, errors, tests, and anti-patterns.

---

# 4. Out of Scope

This document does not define:

- Database tenancy schema.
- Role and permission catalogues.
- API endpoint catalogues.
- UI navigation or tenant switcher design.
- Production access-control runbooks.
- Infrastructure identity provider implementation.

---

# 5. Source Alignment

| Source Area | Alignment |
|---|---|
| PF-02 | Product hierarchy and domain model |
| FR-02 to FR-06 | Platform, organization, facility, site, user, role, and access requirements |
| TA-05 | Security and identity architecture |
| DB-04 | Multi-tenancy data design |
| API-02, API-03, API-23, API-24 | Tenant, identity, access, and workflow API behavior |
| IC-03 | Tenant context integration contract |
| BE-01 | Tenant context propagation through backend layers |
| BE-04 | Repository and query-service tenant filtering |
| BE-05 | Tenant-aware authorization |
| BE-09 | Tenant context in jobs, outbox, and integrations |

---

# 6. Tenant-Context Principles

Tenant context implementation shall follow these principles:

- Tenant context is mandatory for tenant-scoped operations.
- Tenant context shall preserve Platform -> Organization -> Facility -> Site hierarchy.
- Client-provided tenant values shall not be trusted without backend validation.
- Tenant context shall be resolved once at the boundary and propagated explicitly.
- Tenant filters shall be enforced in repositories and query services.
- Tenant context shall enrich logs, audit events, outbox records, jobs, reports, exports, and cache keys.
- Cross-tenant existence shall not be leaked.

---

# 7. Frozen Tenant Hierarchy

The frozen hierarchy is:

```text
Platform
└── Organization
    └── Facility
        └── Site
```

The following hierarchy is prohibited:

```text
Organization
└── Site
    └── Facility
```

---

# 8. Tenant-Context Object

Backend execution shall use a controlled tenant-context object or equivalent representation.

Tenant context should include:

- Platform scope indicator where applicable.
- Organization identifier.
- Facility identifier where applicable.
- Site identifier where applicable.
- Source of context.
- Effective scope.
- Administrative override indicator.
- Actor or principal reference.
- Correlation ID.
- Request ID.

Tenant context shall be immutable during a single operation unless context narrowing is explicitly performed.

---

# 9. Context Sources

Tenant context may be derived from approved sources.

| Source | Usage |
|---|---|
| Token claims | Principal tenant scope and platform-level access indicators |
| Approved tenant headers | Organization, Facility, and Site context where API contracts allow |
| Route parameters | Parent or resource identifiers used to resolve scope |
| Request body | Creation context where approved and validated |
| Server-side context | Internal service, job, or scheduled execution |
| Background job payload | Deferred tenant-scoped execution |
| Outbox metadata | Event and integration tenant propagation |

Unapproved sources shall be ignored or rejected.

---

# 10. Approved Tenant Headers

Approved tenant headers are:

- `X-Organization-ID`.
- `X-Facility-ID`.
- `X-Site-ID`.

Headers shall be validated against authenticated principal scope and hierarchy relationships.

Header presence alone does not prove tenant access.

---

# 11. Context Precedence and Conflict Detection

Tenant resolution shall define precedence among token claims, headers, route parameters, request body, and server-side context.

Conflicts shall be detected when:

- Header organization conflicts with route organization.
- Facility does not belong to organization.
- Site does not belong to facility.
- Request body tenant scope conflicts with resolved route scope.
- Principal does not have access to requested scope.
- Background job context conflicts with persisted resource ownership.

Conflicts shall fail safely and shall not leak cross-tenant existence.

---

# 12. Organization, Facility, and Site Validation

Validation shall confirm:

- Organization exists and is accessible to the principal.
- Facility belongs to the organization.
- Site belongs to the facility.
- Caller has allowed scope for the requested action.
- Resource belongs to the resolved scope.

Validation shall occur before tenant-scoped repository or query access.

---

# 13. Context Inheritance and Narrowing

Context inheritance follows the hierarchy.

| Provided Context | Validation |
|---|---|
| Organization | Caller has organization access |
| Organization and Facility | Facility belongs to organization and caller has scope |
| Organization, Facility, and Site | Site belongs to facility and caller has scope |
| Platform | Caller has approved platform authority |

Context narrowing may reduce scope from organization to facility or site.

Context widening shall require explicit authorization.

---

# 14. API Boundary

Tenant context shall be resolved through an API dependency, middleware, or controlled boundary component.

The boundary shall:

- Extract approved context inputs.
- Validate principal access.
- Detect conflicts.
- Create effective tenant context.
- Attach context to request execution.
- Preserve request and correlation identifiers.

Business logic shall not parse raw tenant headers directly.

---

# 15. Application-Service Propagation

Application services shall receive resolved tenant context as an explicit input.

Application services shall:

- Use tenant context for coarse and resource-level authorization.
- Pass tenant context to repositories and query services.
- Include tenant metadata in outbox records where required.
- Include tenant context in audit handoff where required.
- Reject missing tenant context for tenant-scoped operations.

---

# 16. Repository and Query-Service Enforcement

Repositories and query services shall enforce tenant filters.

Filtering rules:

- Organization-scoped data filters by organization.
- Facility-scoped data filters by organization and facility.
- Site-scoped data filters by organization, facility, and site.
- Reports and projections preserve tenant scope.
- Search and pagination preserve tenant scope.
- Soft-delete or lifecycle filters do not replace tenant filters.

Tenant filters shall not be optional caller-controlled flags.

---

# 17. Cross-Tenant Denial and Missing Context

Cross-tenant access shall be denied.

Missing tenant context shall fail for tenant-scoped operations.

Cross-tenant errors shall use tenant-safe not-found or forbidden behavior without confirming resource existence outside the caller's scope.

---

# 18. Global and Platform-Scoped Operations

Platform-scoped operations shall be explicit.

Platform operations shall:

- Require approved platform-level permission.
- Avoid accidental tenant-wide data exposure.
- Produce audit evidence where sensitive.
- Avoid bypassing tenant filters unless specifically approved.

Global reference data shall be clearly classified before it is treated as non-tenant-scoped.

---

# 19. Administrative Override

Administrative override shall:

- Require approved role and permission.
- Identify original actor.
- Identify effective tenant context.
- Identify override reason where required.
- Produce audit evidence.
- Avoid silent cross-tenant access.

Override authorization is owned by BE-05. Tenant context propagation is owned by BE-06.

---

# 20. Background and Scheduled Jobs

Tenant-scoped jobs shall carry tenant context.

Job payloads should include:

- Organization identifier.
- Facility identifier where applicable.
- Site identifier where applicable.
- Actor or service identity.
- Correlation ID.
- Source operation.

Scheduled jobs that iterate tenants shall validate each tenant scope independently and shall avoid one tenant failure blocking unrelated tenant processing unless the job design requires fail-fast behavior.

---

# 21. Outbox, Events, and Integration Propagation

Outbox records and integration events shall include tenant metadata where required.

Tenant metadata should include:

- Organization.
- Facility where applicable.
- Site where applicable.
- Aggregate or resource reference.
- Correlation ID.
- Source operation.

Integration adapters shall receive tenant context only when required by approved integration behavior and shall not leak tenant details to providers unnecessarily.

---

# 22. Log and Audit Enrichment

Logs and audit events shall include tenant context where applicable:

- Organization ID.
- Facility ID.
- Site ID.
- Actor.
- Operation.
- Correlation ID.
- Request ID.

Sensitive tenant data shall not be logged beyond approved diagnostic and audit needs.

---

# 23. Cache-Key Tenant Scoping

Tenant-scoped cached data shall use tenant-scoped keys.

Caching rules:

- Cache keys include tenant scope for tenant-owned data.
- Cached data identifies authoritative source.
- Expiration and invalidation ownership are defined.
- Authorization decisions are not cached beyond approved safe duration.
- Critical transactional operations do not rely on stale cached tenant state.

Tenant-context caching shall use Redis per `DR-008_Redis_Cache_Baseline.md` where caching is approved.

---

# 24. Reports, Exports, Search, and Pagination

Reports, exports, search, and pagination shall preserve tenant scope.

Rules:

- Report queries apply tenant filters.
- Export jobs carry tenant context.
- Search does not reveal cross-tenant existence.
- Pagination totals and cursors do not include unauthorized records.
- Dashboard projections remain tenant-isolated.

---

# 25. Data-Leakage Prevention

Backend implementation shall prevent:

- Cross-tenant results in lists, reports, exports, and dashboards.
- Tenant scope escalation through request parameters.
- Cache-key collisions across tenants.
- Outbox events without required tenant metadata.
- Logs exposing unrelated tenant data.
- Error messages confirming another tenant's resource existence.

---

# 26. Error Behavior

| Failure | Expected Behavior |
|---|---|
| Missing tenant context | Tenant-context or validation error |
| Conflicting tenant context | Tenant-context error |
| Unauthorized organization | Forbidden or tenant-safe error |
| Facility outside organization | Tenant-safe error |
| Site outside facility | Tenant-safe error |
| Cross-tenant resource access | Not found or forbidden without existence leakage |
| Unauthorized override | Forbidden and auditable |

---

# 27. Tenant Isolation Testing

Tests shall cover:

- Valid organization, facility, and site access.
- Missing tenant context.
- Conflicting tenant context.
- Context inheritance.
- Context narrowing.
- Cross-tenant read denial.
- Cross-tenant write denial.
- Repository tenant filters.
- Query-service tenant filters.
- Report and export scoping.
- Search and pagination scoping.
- Background-job tenant context.
- Scheduled tenant iteration.
- Outbox and event tenant metadata.
- Cache-key scoping where caching exists.
- Administrative override authorization and audit.

---

# 28. Negative and Cross-Tenant Test Cases

Negative tests shall prove:

- Tenant headers cannot override unauthorized token scope.
- Route parameters cannot access another tenant.
- Request body tenant fields cannot escalate scope.
- Cross-tenant resource identifiers do not reveal existence.
- Cached data does not leak across tenants.
- Reports and exports do not include unrelated tenant data.

---

# 29. Anti-Patterns

The following are prohibited:

- Treating tenant headers as trusted without validation.
- Omitting tenant filters in repositories or query services.
- Using global queries for tenant-scoped data.
- Caching tenant data without tenant-scoped keys.
- Logging unrelated tenant data.
- Publishing tenant-scoped events without required tenant metadata.
- Implementing administrative override without audit.
- Using Organization -> Site -> Facility hierarchy.

---

# 30. Traceability Requirements

Tenant implementation shall trace to:

- Product hierarchy and domain model.
- Functional Requirements for platform, organization, facility, site, user, role, and access behavior.
- Database Design for tenancy model.
- API Collections for tenant headers, access, state, and workflow behavior.
- Integration Contracts for tenant propagation.
- BE-01, BE-04, BE-05, and BE-09 for backend layer alignment.

Traceability sources: see [docs/10_Backend_Engineering/BE-TRACEABILITY_MAPPINGS.md](BE-TRACEABILITY_MAPPINGS.md) — primary sources include [docs/01_Product_Foundation/PF-02_Domain_Model.md](../01_Product_Foundation/PF-02_Domain_Model.md), [docs/04_Functional_Requirements/FR-03_Organization_Management.md](../04_Functional_Requirements/FR-03_Organization_Management.md), [docs/06_Database_Design/DB-04_Multi_Tenancy_Data_Design.md](../06_Database_Design/DB-04_Multi_Tenancy_Data_Design.md), and [docs/99_Decision_Records/DR-004_Platform_Tenant_Hierarchy.md](../99_Decision_Records/DR-004_Platform_Tenant_Hierarchy.md).

---

# 31. Acceptance Criteria

This document is acceptable when:

- Tenant principles, object, fields, sources, headers, route parameters, server-side resolution, precedence, and conflict handling are defined.
- Organization, Facility, and Site validation is defined.
- Context inheritance, narrowing, API boundary, service propagation, repository enforcement, query enforcement, cross-tenant denial, and missing-context behavior are defined.
- Platform operations, administrative override, background jobs, scheduled jobs, outbox, events, integrations, logs, audit, cache, reports, exports, search, pagination, leakage prevention, errors, tests, and anti-patterns are defined.

---

# 32. Freeze Rule

This document may be frozen only after BE-05 confirms tenant-aware authorization behavior, BE-07 confirms API boundary context behavior, BE-09 confirms tenant context propagation through jobs and outbox processing, and BE-10 confirms tenant-isolation tests.

---

# 33. Summary

BE-06 defines tenant context implementation for Digitize.

It preserves the approved Platform -> Organization -> Facility -> Site hierarchy across backend execution and ensures tenant context is resolved, validated, propagated, enforced, logged, audited, persisted, cached, and tested without cross-tenant leakage.
