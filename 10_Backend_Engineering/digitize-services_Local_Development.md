# digitize-services — local development

**Document location:** `docs/10_Backend_Engineering/digitize-services_Local_Development.md`  
**Code:** `digitize-services/` in the monorepo

Project purpose
----------------
This repository is the production-ready scaffold for Digitize backend services. It provides the minimal, permanent infrastructure required by all backend developers: FastAPI app bootstrap, async SQLAlchemy engine, Alembic scaffolding, DI/lifespan wiring, middleware foundations, health endpoints, testing setup, quality tooling, Docker, and CI.

Engineering foundation
----------------------
Cross-cutting runtime rules (logging, correlation/request/trace IDs, Unit of Work, pool, Principal stub) are documented in:

- [`../architecture/BACKEND_CODING_STANDARDS.md`](../architecture/BACKEND_CODING_STANDARDS.md) (authoritative coding standard)
- [`../architecture/ENGINEERING_STANDARDS.md`](../architecture/ENGINEERING_STANDARDS.md)
- [`../architecture/BACKEND_FOUNDATION.md`](../architecture/BACKEND_FOUNDATION.md)
- [`../99_Decision_Records/DR-018_Engineering_Foundation_Runtime.md`](../99_Decision_Records/DR-018_Engineering_Foundation_Runtime.md)

Create the first Platform Admin (no login, no default credentials):

```bash
# set PASSWORD_PEPPER in .env first
poetry run digitize bootstrap-platform-admin
```

Production requires `--confirm-production`. Do not implement Authentication until the foundation gate is accepted.

Prerequisites
-------------
- Python 3.13 installed
- `pipx` recommended for installing Poetry (isolated user install)
- Local PostgreSQL 17 (database name `digitize`) **or** Docker Compose Postgres when you do not have a native instance

Environment setup
-----------------
Copy the example environment and set credentials for **your** local PostgreSQL role. Do not commit `.env`.

```bash
cp .env.example .env
# edit .env: DB_USER, DB_PASSWORD (and PGUSER/PGPASSWORD if you also run SQL migrations)
```

`ENVIRONMENT` selects how credentials are resolved (`app/config/db_config.py`):

| ENVIRONMENT | Database default | Credentials |
| ----------- | ---------------- | ----------- |
| `development` | `digitize` on `localhost:5432` | `DB_*` or `PG*` from `.env`. User defaults to your OS username if unset |
| `test` | `digitize_test` | Same pattern; do not point tests at a shared database with data |
| `staging` / `production` | none | `DB_HOST`, `DB_USER`, `DB_PASSWORD`, and `DB_NAME` (or `DATABASE_URL`) are required |

`DATABASE_URL` is optional. If set, it overrides the discrete fields. The app always uses `postgresql+asyncpg://`.

Local PostgreSQL 17
-------------------
If you already created database `digitize` on PostgreSQL 17.11, use that instance. Example `.env`:

```bash
ENVIRONMENT=development
DB_HOST=localhost
DB_PORT=5432
DB_USER=your_postgres_role
DB_PASSWORD=your_postgres_password
DB_NAME=digitize
```

Then provision or refresh the frozen schema (development only):

```bash
# from repository root
export DIGITIZE_RESET_LOCAL_DB=1
./scripts/reset_local_digitize_schema.sh
```

That drops DIGITIZE schemas, applies `database/migrations/001`–`008`, and stamps Alembic `db11_foundation_baseline`.

Do not run `alembic revision --autogenerate`. Alembic does not create the physical schema.

Docker Compose PostgreSQL (optional alternative)
------------------------------------------------
Start containerized PostgreSQL only if you are **not** using the native PostgreSQL 17 `digitize` database:

```bash
docker compose up -d db
```

Poetry installation (recommended)
---------------------------------
Install Poetry with `pipx` so the CLI is available system-wide but isolated from project interpreters:

```bash
python3 -m pip install --user pipx
python3 -m pipx ensurepath
pipx install poetry
```

Alternatively, install Poetry system-wide per Poetry docs. The container image installs Poetry for the build process.

Database provisioning
---------------------
The production physical schema is created by the SQL CreateDB path. Alembic only stamps the frozen baseline:

```text
database/migrations/001–008
scripts/run_migrations_local.sh
poetry run alembic upgrade head   # stamp only; fails if SQL was not applied
```

```text
DO NOT RUN ALEMBIC AUTOGENERATE
```

`digitize-services/migrations/versions/` contains only `db11_foundation_baseline`. See [`../06_Database_Design/DATABASE_FOUNDATION_FREEZE.md`](../06_Database_Design/DATABASE_FOUNDATION_FREEZE.md) and [`../06_Database_Design/Alembic_Version_Stamp.md`](../06_Database_Design/Alembic_Version_Stamp.md).

Application startup
-------------------
Install dependencies and run the development server:

```bash
cd digitize-services
poetry install
poetry run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Structure highlights:

- `app/main.py` — application factory and FastAPI entrypoint
- `app/api/v1/controllers` — HTTP controllers (request/response mapping)
- `app/services` — business logic and orchestration
- `app/repositories` — DB persistence adapters (SQLAlchemy)
- `app/models`, `app/schemas` — SQLAlchemy models and Pydantic schemas
- `app/db` — DB session and base
- `migrations/` — Alembic version stamp (see Alembic doc above)

Quality tooling
---------------
Linting and formatting with Ruff:

```bash
poetry run ruff format --check .
poetry run ruff check .
```

Type checking with MyPy:

```bash
poetry run mypy app
```

Testing
-------
Run tests with pytest:

```bash
poetry run pytest
```

Docker startup
--------------
Build and run the entire stack with Docker Compose (app + db):

```bash
docker compose up --build
```

Notes
-----
- Use `pipx` for Poetry locally to avoid installing Poetry into project virtual environments.
