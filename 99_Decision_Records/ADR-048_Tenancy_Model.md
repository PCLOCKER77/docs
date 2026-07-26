---
title: ADR-048 Tenancy Model
date: 2026-07-26
status: Proposed
deciders: [Product Architecture, Solution Architecture, Data Architecture]
technical_lead: Data Architecture Team
---

# ADR-048: Tenancy Model

## Context

The Digitize platform must operate as a multi-tenant SaaS product. The tenancy model impacts schema design, operational processes, backup/restore, migration complexity, indexing strategy, and cross-tenant reporting.

Previous documents have discussed three primary tenancy approaches:

- Shared database, shared schema (tenant scope via `organization_id` column)
- Shared database, schema-per-tenant (each tenant has its own schema)
- Database-per-tenant (each tenant deployed to a separate database)

DB-11 currently contains a provisional implementation assumption (`DB-11-ASM-003`) that adopts a shared database + shared schema model.

## Decision

We propose the following provisional decision for review and approval:

- Decision: Adopt the Shared-Database / Shared-Schema tenancy model for the initial production launch, using `organization_id` as the tenant root column and explicit tenant scoping on all tenant-owned tables.

This decision is provisional and intended to reduce operational complexity for the foundation release while preserving a clear migration path to schema-per-tenant or database-per-tenant if future scale, regulatory, or isolation requirements mandate it.

## Rationale

- Operational simplicity: single logical database simplifies backups, restores, monitoring, and schema migrations during early rollout.
- Cost efficiency: avoids per-tenant database or schema lifecycle costs and reduces DevOps overhead.
- Development velocity: simplifies testing and continuous integration by providing a unified baseline.
- Migration path: the physical design will require tenant_id (`organization_id`) on all tenant tables, enabling later extraction or migration to schema-per-tenant with scripted transformations.

## Consequences

- Indexing and partitioning: tables need tenant-aware composite indexes and planned partitioning strategies for high-volume tables (e.g., `operations.attendance`).
- Security and isolation: require Row-Level Security (RLS) and application-layer enforcement as defense-in-depth; privacy-sensitive columns must be masked/encrypted.
- Migration complexity: migrating to schema-per-tenant/db-per-tenant later will require planned ETL and downtime windows for large customers; this risk must be accepted or mitigated per-customer.
- Compliance: some regulatory requirements may force schema or database isolation for specific customers; those will require a documented exception process.

## Implementation Impact

- DB-11 DDL will continue to use `organization_id`, `facility_id`, and `site_id` scoping columns on tenant-owned tables.
- Migration artifacts must be crafted to be reversible where possible and idempotent. Use Flyway-style versioned SQL migrations.
- Add RLS policies for sensitive tables as part of the security hardening sprint (see DB-15).
- Add tenant-aware indexing and consider partitioning strategies for high-volume tables.

## Mitigations and Next Steps

1. Implement RLS policies for critical tables as a defense-in-depth control and document in DB-15.
2. Define retention and masking/encryption mapping for sensitive columns (DB-10 column-level traceability updates required).
3. Create a tenant-migration playbook and scripts to enable future migration to schema-per-tenant if required.
4. Finalize operational runbooks for backup/restore, cross-tenant reporting, and per-tenant support.
5. Approve this ADR formally via Solution Architecture and Product Architecture sign-off before promoting DB-11 migration artifacts to production.

## Alternatives Considered

- Schema-per-tenant: Improves isolation but increases operational overhead and complexity for schema updates.
- Database-per-tenant: Strongest isolation but highest operational and cost burden; not justified for initial launch.

## Related Documents

- DB-03_Physical_Data_Model.md
- DB-04_Multi_Tenancy_Data_Design.md
- DB-11_Database_DDL_DML_Scripts.md
- DB-15_Database_Security_Hardening_Guide.md

## Decision Log

- Proposed: 2026-07-26 by Data Architecture Team
