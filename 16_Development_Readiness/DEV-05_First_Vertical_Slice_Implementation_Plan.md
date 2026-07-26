# DEV-05 First Vertical Slice Implementation Plan

> First end-to-end implementation slice for Digitize development.

---

# Document Control

| Field | Value |
|---|---|
| Document ID | DEV-05 |
| Document Name | First Vertical Slice Implementation Plan |
| Folder | 16_Development_Readiness |
| Product | Digitize by OreeOn Technologies Pvt. Ltd. |
| Status | Design Draft |
| Owner | Product / Engineering |
| Reviewers | Backend, Frontend, Database, API, UI/UX, QA, DevOps, Security |
| Version | 1.0 |
| Last Updated | 2026-07-24 |

---

# 1. Purpose

This document defines the first implementation slice that should be built before expanding across all modules.

---

# 2. Recommended First Slice

The first vertical slice shall be:

```text
Platform -> Organization -> Facility -> Site
```

This slice validates the core tenant hierarchy and development architecture.

---

# 3. Why This Slice First

This slice proves:

- Multi-tenant hierarchy.
- Backend modular monolith boundaries.
- PostgreSQL schema and migrations.
- FastAPI route structure.
- Flutter routing and forms.
- API client behavior.
- Tenant context handling.
- Basic authorization hooks.
- Validation and error handling.
- Local development environment.
- Basic CI checks.

---

# 4. Backend Scope

Backend first slice should include:

- Organization create/read/update basic flow.
- Facility create/read/update basic flow.
- Site create/read/update basic flow.
- Tenant-scoped queries.
- SQLAlchemy repositories.
- Alembic migration.
- API schemas.
- Error handling.
- Audit-ready metadata fields where approved.
- Tests for success, validation, authorization placeholder, and tenant isolation.

---

# 5. Frontend Scope

Flutter first slice should include:

- App shell.
- Login placeholder or development session scaffold.
- Organization list/detail/form.
- Facility list/detail/form.
- Site list/detail/form.
- Tenant hierarchy display.
- Loading, empty, error, and success states.
- API client integration.
- Responsive web layout.
- Android and iOS smoke run.

---

# 6. Database Scope

Database first slice should include:

- Organization table usage.
- Facility table usage.
- Site table usage.
- Tenant hierarchy constraints.
- Alembic migration.
- Seed data where required for local development.

---

# 7. Done Criteria

The first vertical slice is done when:

- Backend APIs run locally.
- Flutter can create and read Organization, Facility, and Site records.
- PostgreSQL migration is versioned.
- Tests cover API and repository basics.
- Logs include request and correlation context.
- Tenant hierarchy is visible in UI.
- CI runs backend and frontend checks.
- No real secrets are used.

---

# 8. Expansion After First Slice

After the first slice, module expansion should proceed in this order:

1. Identity, User, Role, and Permission.
2. Customer Management.
3. Membership Management.
4. Attendance and Walk-in.
5. Trainer, Activity, Batch, and Class.
6. Billing and Payment.
7. Subscription and License.
8. Notification and Campaign.
9. Reports and Analytics.
10. Support Ticket.
11. Audit and Compliance.

---

# 9. First Slice Architecture Flow

```text
Flutter Screen
    ↓
Flutter API Client
    ↓
FastAPI Router
    ↓
Application Service
    ↓
Repository
    ↓
PostgreSQL
```

Cross-cutting behavior:

- Auth context is resolved before protected route execution.
- Tenant context is resolved before tenant-scoped use cases.
- Authorization is checked before mutation.
- Validation occurs at API boundary and service/domain layer where required.
- Logs include request ID and correlation ID.

---

# 10. First Slice API Set

| Capability | Method | Path | Purpose |
|---|---|---|---|
| Health | GET | `/api/v1/health` | Process health |
| Readiness | GET | `/api/v1/readiness` | Dependency readiness |
| List Organizations | GET | `/api/v1/organizations` | Organization list |
| Create Organization | POST | `/api/v1/organizations` | Organization create |
| Get Organization | GET | `/api/v1/organizations/{organization_id}` | Organization detail |
| Update Organization | PATCH | `/api/v1/organizations/{organization_id}` | Organization update |
| List Facilities | GET | `/api/v1/organizations/{organization_id}/facilities` | Facility list |
| Create Facility | POST | `/api/v1/organizations/{organization_id}/facilities` | Facility create |
| List Sites | GET | `/api/v1/facilities/{facility_id}/sites` | Site list |
| Create Site | POST | `/api/v1/facilities/{facility_id}/sites` | Site create |

Exact paths shall be confirmed against API-02 before implementation.

---

# 11. First Slice Database Objects

| Object | Usage |
|---|---|
| `tenant.organization` | Organization tenant root |
| `tenant.facility` | Facility under Organization |
| `tenant.site` | Operational Site under Facility |
| `integration.outbox_event` | Future event publication state where first-slice events are emitted |
| Audit fields | Created/updated metadata and traceability |

---

# 12. First Slice Flutter Deliverables

Flutter deliverables:

- App shell.
- Login placeholder or mock session.
- Tenant context selector placeholder.
- Organization list.
- Organization form.
- Facility list.
- Facility form.
- Site list.
- Site form.
- API client.
- Fixture-backed mock mode.
- Widget tests for critical screens.

---

# 13. First Slice QA Scenarios

| Scenario ID | Scenario |
|---|---|
| VS-QA-001 | Create Organization successfully |
| VS-QA-002 | Organization create validation error |
| VS-QA-003 | Organization list empty state |
| VS-QA-004 | Organization list loaded state |
| VS-QA-005 | Create Facility under Organization |
| VS-QA-006 | Prevent Facility create under unauthorized Organization |
| VS-QA-007 | Create Site under Facility |
| VS-QA-008 | Invalid tenant context returns controlled error |
| VS-QA-009 | Permission-aware navigation hides unauthorized action |
| VS-QA-010 | Backend readiness reports dependency status |

