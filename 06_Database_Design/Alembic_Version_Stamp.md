# Alembic `digitize-services/migrations/` — version stamp

Alembic in `digitize-services/migrations/` is a **version stamp** for the frozen DB-11 schema.

```text
Current physical migration path:
database/migrations/001–008

Physical source of truth:
DB-11

Alembic:
single baseline db11_foundation_baseline (does not create tables)

ORM:
does not create the production schema
```

```text
DO NOT RUN ALEMBIC AUTOGENERATE
DO NOT USE ALEMBIC TO PROVISION AN EMPTY DATABASE
```

## Provision / refresh PostgreSQL

```bash
# from repository root, development only
export DIGITIZE_RESET_LOCAL_DB=1
./scripts/reset_local_digitize_schema.sh
```

Or apply SQL onto an empty database, then stamp Alembic:

```bash
./scripts/run_migrations_local.sh
cd digitize-services
poetry run alembic upgrade head
```

The old 117-revision scaffold (`organization.*` / `facility.*` / `subscription.*`) has been removed.

See also [`DATABASE_FOUNDATION_FREEZE.md`](DATABASE_FOUNDATION_FREEZE.md) and [`../10_Backend_Engineering/digitize-services_Local_Development.md`](../10_Backend_Engineering/digitize-services_Local_Development.md).
