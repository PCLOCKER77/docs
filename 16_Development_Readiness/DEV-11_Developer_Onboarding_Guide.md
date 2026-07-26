# DEV-11 Developer Onboarding Guide

> Developer onboarding path for Digitize frontend, backend, and full-stack contributors.

---

# Document Control

| Field | Value |
|---|---|
| Document ID | DEV-11 |
| Document Name | Developer Onboarding Guide |
| Folder | 16_Development_Readiness |
| Product | Digitize by OreeOn Technologies Pvt. Ltd. |
| Status | Design Draft |
| Owner | Engineering Governance |
| Reviewers | Frontend, Backend, DevOps, QA |
| Version | 1.0 |
| Last Updated | 2026-07-24 |

---

# 1. Purpose

This guide defines what a new developer should read, install, run, and complete before taking feature work.

---

# 2. Required Reading

Developers should read:

1. `docs/README.md`
2. `01_Product_Foundation/README.md`
3. `03_Business_Analysis/README.md`
4. `04_Functional_Requirements/README.md`
5. `07_API_Collections/API-00_API_Collection_Standards.md`
6. `09_UI_UX_Design/UI-00_UI_UX_Standards.md`
7. `10_Backend_Engineering/BE-00_Backend_Engineering_Standards.md`
8. `16_Development_Readiness/README.md`

Backend developers should additionally read BE-01 through BE-11.

Frontend developers should additionally read DEV-03, DEV-07, UX-04, and UX-05.

---

# 3. Local Setup Checklist

- Install Python.
- Install Flutter.
- Install Docker.
- Install PostgreSQL client tools where useful.
- Install Git.
- Configure editor formatting.
- Copy `.env.example` to local environment file.
- Start local services.
- Run backend health check.
- Run Flutter web.
- Run initial tests.

---

# 4. First Developer Tasks

Recommended starter tasks:

- Run local backend.
- Run Flutter web.
- Execute migration command.
- Call backend health endpoint.
- Render app shell.
- Run a unit test.
- Review first vertical slice user stories.

---

# 5. Workflow Rules

- Create a branch for each change.
- Keep changes small and reviewable.
- Add tests with behavior changes.
- Update docs when implementation behavior differs from assumptions.
- Never commit secrets.
- Ask for Product review before changing business behavior.

---

# 6. Backend Onboarding Path

Backend developers should be able to:

- Start PostgreSQL and Redis locally.
- Start FastAPI locally.
- Run Alembic migrations.
- Run unit tests.
- Understand module boundaries.
- Add a route, schema, service, repository, and test.
- Read request ID and correlation ID from logs.
- Explain how tenant context is enforced.

First backend exercise:

```text
Add a read-only health dependency check and test it.
```

---

# 7. Frontend Onboarding Path

Flutter developers should be able to:

- Start Flutter web.
- Run Flutter tests.
- Understand app shell and routing.
- Use mock fixtures.
- Add a shared component.
- Add a feature screen.
- Call the API client.
- Display loading, empty, error, and success states.

First frontend exercise:

```text
Render Organization List using local fixture data.
```

---

# 8. QA Onboarding Path

QA engineers should be able to:

- Read user stories and acceptance criteria.
- Identify API fixtures.
- Run backend tests.
- Run Flutter widget tests.
- Validate first vertical slice manually.
- Report defects with story, API, screen, and environment references.

First QA exercise:

```text
Validate DEV-US-001 Create Organization against acceptance criteria.
```

---

# 9. Environment Checklist

| Check | Expected Result |
|---|---|
| Backend starts | FastAPI process is running |
| Health works | `/api/v1/health` returns success |
| Readiness works | PostgreSQL and Redis status visible |
| Migration runs | Alembic applies local schema |
| Flutter starts | Web app loads |
| API call works | Flutter can call backend health endpoint |
| Tests run | Backend and Flutter test commands complete |

---

# 10. Common Mistakes to Avoid

- Starting module work before local environment is stable.
- Hardcoding API URLs in Flutter widgets.
- Putting business rules in Flutter only.
- Returning ORM models directly from FastAPI.
- Skipping tenant context in early APIs.
- Committing local secrets.
- Creating migrations without reviewing DB ownership.

