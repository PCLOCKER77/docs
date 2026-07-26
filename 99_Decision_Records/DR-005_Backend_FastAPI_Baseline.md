# DR-005 Backend FastAPI Baseline

> Decision record for the backend framework and baseline technology model.

---

# Document Control

| Field | Value |
|---|---|
| Document ID | DR-005 |
| Document Name | Backend FastAPI Baseline |
| Folder | 99_Decision_Records |
| Product | Digitize by OreeOn Technologies Pvt. Ltd. |
| Status | Design Draft |
| Owner | Backend Engineering / Architecture Governance |
| Reviewers | Architecture, Backend Engineering, API, Database, Security, DevOps, QA |
| Version | 1.0 |
| Last Updated | 2026-07-24 |
| Supersedes | None |
| Superseded By | None |

---

# 1. Decision Summary

Digitize backend engineering documentation shall use FastAPI and Python as the backend baseline while keeping domain and application services framework-independent.

---

# 2. Context

The backend documentation requires a concrete technology baseline so project structure, API handling, authentication, authorization, background jobs, database access, observability, testing, and deployment guidance can be written consistently.

At the same time, domain and application services should not be tightly coupled to HTTP transport behavior.

---

# 3. Decision

The backend baseline shall include:

- Python.
- FastAPI.
- PostgreSQL.
- REST APIs.
- JSON payloads.
- snake_case JSON properties.
- JWT-based authentication.
- Tenant context based on Organization, Facility, and Site.
- Framework-independent domain and application services.

Domain and application services shall remain reusable from HTTP APIs, background workers, scheduled jobs, CLI utilities, and future event consumers.

---

# 4. Alternatives Considered

| Option | Description | Outcome |
|---|---|---|
| FastAPI with framework-independent services | Use FastAPI at transport boundary and keep services reusable | Accepted |
| FastAPI coupled directly to business logic | Put domain behavior inside route handlers | Rejected because it weakens testability and reuse |
| Framework-neutral documentation only | Avoid naming a backend framework | Rejected because project structure and deployment guidance would remain ambiguous |
| Alternative backend framework | Use another Python or non-Python framework | Deferred until a formal technical evaluation is needed |

---

# 5. Rationale

FastAPI gives the backend documentation a practical and modern API baseline while still allowing clean separation between transport concerns and domain behavior.

The framework-independent service rule supports future background workers, scheduled processes, and event consumers without duplicating business rules.

---

# 6. Consequences

## Positive Consequences

- Backend documentation can be specific enough for implementation.
- API, authentication, validation, and dependency-injection patterns are easier to standardize.
- Domain logic remains testable outside HTTP routes.
- Background processing can reuse application services.

## Tradeoffs

- FastAPI-specific guidance must remain separated from domain rules.
- Future framework changes would require a superseding decision record.

## Risks

- Developers may place business logic inside route handlers unless BE-00 and BE-01 boundaries are enforced.

---

# 7. Affected Documentation

| Folder / Document | Impact |
|---|---|
| `10_Backend_Engineering/BE-00_Backend_Engineering_Standards.md` | Governing backend standard uses this baseline |
| `10_Backend_Engineering/BE-01_Backend_Application_Architecture.md` | Defines layer and dependency boundaries |
| `10_Backend_Engineering/BE-02_FastAPI_Project_Structure.md` | Defines FastAPI project structure |
| `07_API_Collections/` | API behavior aligns with backend transport boundary |
| `11_Deployment/` | Backend deployment assumes FastAPI runtime baseline |
| `12_Testing/` | Backend and API tests align with FastAPI services |

---

# 8. Ownership

| Concern | Owner |
|---|---|
| Backend baseline | Backend Engineering / Architecture Governance |
| API transport implementation | Backend Engineering |
| Domain/application service isolation | Backend Engineering |
| Deployment runtime alignment | DevOps / Deployment |
| Future technology changes | Architecture Governance |

---

# 9. Review and Freeze Rule

This decision shall remain `Design Draft` until BE-00 through BE-11 are reviewed for consistency with the baseline.

Once frozen, changes to the backend framework baseline shall be captured through a superseding decision record.

