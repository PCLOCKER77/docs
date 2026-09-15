<!-- DB-23: Create DB Guide -->
# DB-23 Create Database, Schemas, Tables and Indexes — Quick Guide

Purpose
-------
Practical, step-by-step guidance to create the PostgreSQL database, logical schemas, tables, relationships, and indexes for Digitize during development, CI, or initial environment provisioning. This guide complements the canonical DDL scripts in `database/migrations` and the implementation scripts in `DB-11_Database_DDL_DML_Scripts.md`. Physical validation of that path is recorded in `DATABASE_FOUNDATION_FREEZE.md`.

Prerequisites
-------------
- PostgreSQL 14+ running and reachable (container or managed service).
- `psql` client available on your path.
- Environment variables set: `PGHOST`, `PGPORT`, `PGUSER`, `PGPASSWORD`, and **required** `PGDATABASE` (dedicated empty database).
- Repository checked out and current working dir at project root.

Quick create (one-liner)
------------------------
Create the database and apply the canonical ordered SQL migrations:

```bash
# create database (requires a superuser or an admin account)
psql "host=$PGHOST port=$PGPORT user=$PGUSER dbname=postgres" -c "CREATE DATABASE $PGDATABASE;"

# run ordered SQL migrations from repository
scripts/run_migrations_local.sh
```

Schemas
-------
Digitize uses logical schemas to separate domains (platform, tenant, identity, customer, membership, operations, training, commercial, communication, reporting, support, audit, security, integration).

Example SQL to create schemas (idempotent):

```sql
CREATE SCHEMA IF NOT EXISTS platform;
CREATE SCHEMA IF NOT EXISTS tenant;
CREATE SCHEMA IF NOT EXISTS identity;
-- add others as required
```

Tables and columns
------------------
- Authoritative table definitions live in `database/migrations/*.sql` and `docs/06_Database_Design/DB-11_Database_DDL_DML_Scripts.md`.
- When authoring tables, follow the DB standards (`DB-00`) and naming conventions in `DB-20_SQL_CODING_STANDARDS.md`.

Minimal example: `platform.organizations`

```sql
CREATE TABLE IF NOT EXISTS platform.organizations (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  external_id citext NULL,
  name text NOT NULL,
  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NULL
);

-- tenant-aware example
CREATE TABLE IF NOT EXISTS tenant.customers (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  organization_id uuid NOT NULL REFERENCES platform.organizations(id),
  tenant_id uuid NOT NULL,
  first_name text NOT NULL,
  last_name text NOT NULL,
  email citext NULL,
  created_at timestamptz NOT NULL DEFAULT now()
);

ALTER TABLE tenant.customers ADD CONSTRAINT tenant_customers_tenant_org_uc UNIQUE (tenant_id, email);
```

Relationships and foreign keys
------------------------------
- Prefer declarative `FOREIGN KEY` constraints where referential integrity must be enforced.
- For cross-schema foreign keys, ensure the referenced schema/table exists prior to applying the FK (ordering matters in raw SQL migrations).
- When FK dependencies create circular ordering issues, break them by creating tables first, then add constraints in a later migration step.

Indexes and performance
-----------------------
- Create indexes for lookup columns and join keys. For tenant-scoped lookups, include `tenant_id` as a leading column in the index.

Examples:

```sql
CREATE INDEX IF NOT EXISTS idx_customers_tenant_email ON tenant.customers (tenant_id, email);
CREATE INDEX IF NOT EXISTS idx_org_name ON platform.organizations (lower(name));
```

Gist: multi-tenant indexing

- Use composite indexes such as `(tenant_id, <search_column>)` to make tenant-scoped queries selective.
- Consider partial indexes for high-volume tables when queries target a subset (e.g., `WHERE active = true`).

Physical provisioning path (frozen)
-----------------------------------
Provision DIGITIZE PostgreSQL with:

```text
database/migrations/001–008
scripts/run_migrations_local.sh
```

```text
DO NOT RUN ALEMBIC FOR DB-11 PROVISIONING
DO NOT RUN ALEMBIC AUTOGENERATE
```

`digitize-services/migrations/versions/` is an obsolete pre-production scaffold. Alembic reset vs retirement is a separate approved decision. See `DATABASE_FOUNDATION_FREEZE.md`.

Seeding data and idempotency
----------------------------
- Keep seed data minimal and idempotent (use `INSERT ... ON CONFLICT DO NOTHING` or `UPDATE` patterns).
- Prefer separate seed scripts or dedicated migration steps (e.g., `007_create_indexes_triggers_seed.sql` in our repository).

Verification and testing
------------------------
- After migrations run, the runner executes `database/migrations/verify_core_contract.sql` (RAISE on missing core contract) then diagnostic `verify_schema.sql`.
- CI job `.github/workflows/db-migrations-verify.yml` runs `scripts/run_migrations_local.sh` against a fresh Postgres service.

Rollback and migration governance
--------------------------------
- For SQL script-based provisioning, plan forward-only migrations with compensating scripts for destructive changes.
- Do not use the obsolete Alembic 117-revision chain for rollback or provisioning.

Operational notes
-----------------
- Use `pg_dump`/`pg_restore` for backups of schema and data. For PITR, configure WAL archiving per DB-14 guidance.
- Monitor `pg_stat_activity`, long-running queries, and autovacuum stats for high-volume tables.

References
----------
- `database/migrations` (ordered SQL scripts)
- `docs/06_Database_Design/DB-11_Database_DDL_DML_Scripts.md`
- `docs/06_Database_Design/DB-00_Database_Design_StandARDS.md`
- `docs/06_Database_Design/DB-20_SQL_CODING_STANDARDS.md`

--
Generated: DB-23 Create DB Guide
