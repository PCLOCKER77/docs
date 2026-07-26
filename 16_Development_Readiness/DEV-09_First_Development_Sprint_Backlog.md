# DEV-09 First Development Sprint Backlog

> Initial sprint backlog for scaffolding and first vertical slice implementation.

---

# Document Control

| Field | Value |
|---|---|
| Document ID | DEV-09 |
| Document Name | First Development Sprint Backlog |
| Folder | 16_Development_Readiness |
| Product | Digitize by OreeOn Technologies Pvt. Ltd. |
| Status | Design Draft |
| Owner | Product / Engineering |
| Reviewers | Frontend, Backend, Database, DevOps, QA |
| Version | 1.0 |
| Last Updated | 2026-07-24 |

---

# 1. Sprint Goal

Establish the initial monorepo, local development environment, backend foundation, Flutter foundation, and first Platform to Organization to Facility to Site vertical slice.

---

# 2. Sprint Backlog

| Item ID | Work Item | Owner | Dependency | Done Criteria | Priority |
|---|---|---|---|---|---|
| DEV-SP1-001 | Create monorepo folders | Engineering | DEV-01 | `backend`, `frontend`, `infra`, `scripts`, `.github` exist | Must |
| DEV-SP1-002 | Add local Docker Compose | DevOps / Backend | DEV-02 | PostgreSQL and Redis run locally | Must |
| DEV-SP1-003 | Scaffold FastAPI backend | Backend | DEV-04 | App starts and exposes health endpoint | Must |
| DEV-SP1-004 | Configure SQLAlchemy and Alembic | Backend / Database | DR-007 | Initial migration command runs | Must |
| DEV-SP1-005 | Configure structured logging | Backend | BE-08 | Request ID and correlation ID appear in logs | Must |
| DEV-SP1-006 | Configure Redis and Celery | Backend / DevOps | DR-008, DR-009 | Worker starts locally | Must |
| DEV-SP1-007 | Scaffold Flutter app | Frontend | DEV-03 | Flutter web starts locally | Must |
| DEV-SP1-008 | Add Flutter app shell | Frontend | DEV-07 | Shell renders on web and mobile targets | Must |
| DEV-SP1-009 | Add API client baseline | Frontend | DEV-08 | Flutter can call local backend health endpoint | Must |
| DEV-SP1-010 | Implement Organization API skeleton | Backend | API-02, DB-05 | List/create endpoints work locally | Must |
| DEV-SP1-011 | Implement Organization Flutter screens | Frontend | DEV-07 | List and form screens use API or mock mode | Must |
| DEV-SP1-012 | Implement Facility/Site skeleton | Backend / Frontend | DEV-05 | Basic list/create flow works | Should |
| DEV-SP1-013 | Add first-slice tests | QA / Engineering | DEV-06, TEST-00 | Backend and Flutter checks run locally | Must |
| DEV-SP1-014 | Add GitHub Actions baseline | DevOps | DR-012 | PR checks run basic backend/frontend validation | Should |

---

# 3. Sprint Exit Criteria

The sprint is complete when:

- Local development environment starts.
- Backend health/readiness works.
- Flutter web starts.
- Backend and Flutter communicate locally.
- Organization create/list flow works.
- First fixtures and tests exist.
- No real secrets are committed.

---

# 4. Sprint Dependencies

| Dependency | Required For | Owner | Status |
|---|---|---|---|
| Flutter SDK installed | Frontend scaffold | Frontend | Required |
| Python installed | Backend scaffold | Backend | Required |
| Docker available | Local PostgreSQL and Redis | DevOps / Engineering | Required |
| PostgreSQL baseline | DB migrations | Database | Ready |
| Redis baseline | Cache and Celery broker | DevOps / Backend | Ready |
| API-02 baseline | Organization/Facility/Site API | API / Backend | Ready |
| UX-05 screen catalog | Flutter screens | UI/UX / Frontend | Ready for first slice |
| DEV-12 fixtures | Mock mode and tests | API / QA | Ready for first slice |

---

# 5. Suggested Sprint Sequence

| Day Range | Focus |
|---|---|
| Day 1 | Create repo structure, local env, backend app, Flutter app |
| Day 2 | PostgreSQL, Alembic, Redis, Celery, health/readiness |
| Day 3 | Organization backend APIs and tests |
| Day 4 | Flutter app shell, API client, Organization list/form |
| Day 5 | Facility/Site skeleton, first integration test, CI baseline |

The schedule is a planning reference, not a commitment.

---

# 6. Backlog Detail

## DEV-SP1-003 Scaffold FastAPI Backend

Tasks:

- Create `backend/app/main.py`.
- Add settings module.
- Add router registration pattern.
- Add health route.
- Add readiness route.
- Add error handler scaffold.
- Add logging configuration.

Acceptance:

- `GET /api/v1/health` returns success.
- App starts locally without database dependency for health.
- Readiness reports database/cache unavailable until configured.

## DEV-SP1-007 Scaffold Flutter App

Tasks:

- Create Flutter project.
- Add app bootstrap.
- Add route configuration.
- Add app shell placeholder.
- Add theme placeholder.
- Add API client placeholder.

Acceptance:

- Flutter web starts.
- Android and iOS project folders exist.
- App shell renders without backend dependency.

## DEV-SP1-010 Organization API Skeleton

Tasks:

- Add organization module package.
- Add request/response schemas.
- Add SQLAlchemy model or mapped persistence structure.
- Add repository.
- Add service.
- Add API routes.
- Add tests.

Acceptance:

- Create Organization works locally.
- List Organizations works locally.
- Validation failures return controlled error shape.

---

# 7. Sprint Risks

| Risk | Mitigation |
|---|---|
| Flutter web layout differs from mobile behavior | Validate app shell on web and mobile simulator early |
| Backend foundation grows too large | Keep first sprint limited to foundation and Organization slice |
| DB model mismatches DB-11 | Review migrations against Database Design before commit |
| Tenant context is skipped | Add tenant-context placeholder early even before full auth |
| CI setup takes longer than expected | Start with minimal checks and expand after first slice |

---

# 8. Sprint Review Evidence

Sprint review should show:

- Running local backend.
- Running Flutter app.
- Health/readiness response.
- Organization list and create flow.
- Database migration.
- Test execution output.
- CI workflow execution where available.
- Known gaps and next-sprint backlog.

