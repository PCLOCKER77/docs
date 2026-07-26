# DR-007 SQLAlchemy and Alembic Data Access Baseline

> Decision record for selecting SQLAlchemy and Alembic as the backend data-access and migration baseline.

---

# Document Control

| Field | Value |
|---|---|
| Document ID | DR-007 |
| Document Name | SQLAlchemy and Alembic Data Access Baseline |
| Folder | 99_Decision_Records |
| Product | Digitize by OreeOn Technologies Pvt. Ltd. |
| Status | Accepted |
| Owner | Backend Engineering / Database Engineering |
| Reviewers | Architecture, Backend Engineering, Database Engineering, DevOps, QA, Security |
| Version | 1.0 |
| Last Updated | 2026-07-24 |
| Supersedes | None |
| Superseded By | None |

---

# 1. Decision Summary

SQLAlchemy is selected as the Python ORM/data-access baseline, and Alembic is selected as the database migration framework baseline for Digitize backend implementation.

---

# 2. Context

Digitize uses Python, FastAPI, and PostgreSQL. Backend documents need concrete repository, session, transaction, and migration guidance.

The backend architecture requires domain and application services to remain independent from FastAPI transport behavior while repositories own persistence concerns.

---

# 3. Decision

Digitize backend implementation shall use:

- SQLAlchemy for ORM models, SQL expression support, repository persistence, and transaction integration.
- Alembic for versioned database migrations.
- PostgreSQL as the target database engine.
- Repository classes to isolate persistence behavior from domain services.

Repositories shall not contain business decision logic beyond persistence concerns.

Alembic migrations shall align with Database Design and Deployment migration governance. Migrations shall not become the source of truth for schema ownership.

---

# 4. Alternatives Considered

| Option | Description | Outcome |
|---|---|---|
| SQLAlchemy + Alembic | Mature Python ORM and migration baseline for PostgreSQL-backed FastAPI systems | Accepted |
| Raw SQL only | Use SQL directly without ORM | Rejected because repository consistency and model mapping would become harder to standardize |
| Django ORM | Use Django ORM outside Django | Rejected because the backend baseline is FastAPI, not Django |
| Tortoise ORM | Async ORM option | Rejected for baseline because SQLAlchemy has broader enterprise adoption and migration ecosystem |

---

# 5. Rationale

SQLAlchemy and Alembic are mature, widely adopted, compatible with PostgreSQL, and suitable for enterprise Python services.

They support explicit transaction boundaries, repository patterns, migration versioning, testing, and operational review.

---

# 6. Consequences

## Positive Consequences

- Backend data-access guidance becomes concrete.
- Migration framework ambiguity is removed.
- Repository standards can define session and transaction behavior.
- Deployment can define Alembic migration execution and rollback controls.

## Tradeoffs

- Developers must understand SQLAlchemy session lifecycle and lazy-loading risks.
- Migrations require disciplined review with Database Design.

## Risks

- Business rules may leak into ORM models or repositories unless BE-00 boundaries are enforced.
- Alembic migrations may drift from approved DB design if review gates are skipped.

---

# 7. Affected Documentation

| Folder / Document | Impact |
|---|---|
| `10_Backend_Engineering/BE-02_FastAPI_Project_Structure.md` | Defines ORM and migrations folder behavior |
| `10_Backend_Engineering/BE-04_Repository_Data_Access_Standards.md` | Uses SQLAlchemy session and repository guidance |
| `11_Deployment/DEP-05_Database_Migration_Deployment.md` | Uses Alembic migration execution and evidence |
| `06_Database_Design/DB-12_Database_Migration_Strategy.md` | Aligns migration framework with DB strategy |

---

# 8. Ownership

| Concern | Owner |
|---|---|
| ORM baseline | Backend Engineering |
| Migration framework baseline | Backend Engineering / Database Engineering |
| Schema ownership | Database Engineering |
| Migration deployment | DevOps / Deployment |
| Future changes | Architecture Governance |

---

# 9. Review and Freeze Rule

This decision is `Accepted` as the current backend data-access baseline.

It may be frozen after backend repository, migration, deployment, and database governance documents align with SQLAlchemy and Alembic.

