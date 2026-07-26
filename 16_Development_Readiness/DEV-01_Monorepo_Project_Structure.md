# DEV-01 Monorepo Project Structure

> Initial repository structure for Digitize frontend, backend, infrastructure, scripts, and documentation.

---

# Document Control

| Field | Value |
|---|---|
| Document ID | DEV-01 |
| Document Name | Monorepo Project Structure |
| Folder | 16_Development_Readiness |
| Product | Digitize by OreeOn Technologies Pvt. Ltd. |
| Status | Design Draft |
| Owner | Engineering Governance |
| Reviewers | Frontend Engineering, Backend Engineering, DevOps, QA, Security |
| Version | 1.0 |
| Last Updated | 2026-07-24 |

---

# 1. Purpose

This document defines the initial monorepo layout for development.

---

# 2. Approved Structure

```text
Digitize-by-OreeOn/
├── backend/
├── frontend/
├── infra/
├── scripts/
├── docs/
├── .github/
├── .env.example
├── docker-compose.yml
├── README.md
└── CONTRIBUTING.md
```

---

# 3. Backend Structure

```text
backend/
├── app/
│   ├── api/
│   ├── core/
│   ├── db/
│   ├── modules/
│   ├── schemas/
│   ├── workers/
│   └── main.py
├── migrations/
├── tests/
├── pyproject.toml
└── README.md
```

Backend modules shall follow the modular monolith decision in `DR-017_Modular_Monolith_Baseline.md`.

---

# 4. Frontend Structure

```text
frontend/
├── lib/
│   ├── app/
│   ├── core/
│   ├── features/
│   ├── shared/
│   └── main.dart
├── test/
├── integration_test/
├── android/
├── ios/
├── web/
├── pubspec.yaml
└── README.md
```

Flutter implementation shall follow `DR-015_Flutter_Hybrid_Frontend_Baseline.md`.

---

# 5. Infrastructure Structure

```text
infra/
├── docker/
├── aws/
├── local/
└── README.md
```

Infrastructure shall align with AWS and deployment decisions.

---

# 6. Governance

- Backend shall not depend on frontend code.
- Frontend shall consume backend only through approved API contracts.
- Infrastructure shall not store secrets.
- Scripts shall be safe, documented, and environment-aware.
- Documentation remains the source of truth for approved behavior.

---

# 7. Backend Module Layout

Each backend feature module should follow:

```text
backend/app/modules/<module_name>/
├── api.py
├── schemas.py
├── service.py
├── repository.py
├── models.py
├── permissions.py
├── errors.py
└── tests/
```

Module responsibilities:

| File | Responsibility |
|---|---|
| `api.py` | FastAPI routes and dependency wiring |
| `schemas.py` | Request and response DTOs |
| `service.py` | Use-case orchestration |
| `repository.py` | Persistence access |
| `models.py` | SQLAlchemy models where module-owned |
| `permissions.py` | Permission constants and checks |
| `errors.py` | Module-specific controlled errors |

---

# 8. Flutter Feature Layout

Each Flutter feature should follow:

```text
frontend/lib/features/<feature_name>/
├── data/
├── domain/
├── presentation/
│   ├── pages/
│   ├── widgets/
│   └── controllers/
└── <feature_name>_routes.dart
```

Responsibilities:

| Area | Responsibility |
|---|---|
| `data` | API DTOs, API client adapters, mappers |
| `domain` | UI-facing models and simple client-side rules |
| `presentation/pages` | Route-level screens |
| `presentation/widgets` | Feature widgets |
| `presentation/controllers` | State coordination |

---

# 9. Shared Package Layout

```text
frontend/lib/shared/
├── components/
├── theme/
├── validation/
├── errors/
└── async_state/
```

Shared components shall be generic and shall not contain module-specific business behavior.

---

# 10. Repository Root Files

| File | Purpose |
|---|---|
| `.env.example` | Safe local configuration template |
| `docker-compose.yml` | Local development services |
| `.gitignore` | Prevent generated files and secrets from being committed |
| `README.md` | Repository overview and startup instructions |
| `CONTRIBUTING.md` | Contribution rules |
| `.github/workflows/` | GitHub Actions workflows |

