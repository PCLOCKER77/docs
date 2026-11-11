# DEV-17 Development Tracking Workflow

> Repo-based development tracking workflow for Digitize features, stories, tasks, defects, status, ownership, sprint planning, and release readiness.

---

# Document Control

| Field | Value |
|---|---|
| Document ID | DEV-17 |
| Document Name | Development Tracking Workflow |
| Folder | 16_Development_Readiness |
| Product | Digitize by OreeOn Technologies Pvt. Ltd. |
| Status | Design Draft |
| Owner | Engineering Governance / Product |
| Reviewers | Product, Engineering, QA, DevOps, Release Management |
| Version | 1.0 |
| Last Updated | 2026-07-24 |

---

# 1. Purpose

This document defines how Digitize development shall be tracked without an external agile tool.

The documentation repository shall track:

- Features.
- User stories.
- Tasks.
- Defects.
- Owners.
- Status.
- Sprint scope.
- Release scope.
- Acceptance.
- Traceability.

---

# 2. Tracking Artifacts

| Artifact | File | Purpose |
|---|---|---|
| Feature Backlog | DEV-14 | Tracks product features by module |
| User Story Map | DEV-15 | Tracks user stories by module |
| Traceability Matrix | DEV-16 | Tracks feature/story links to docs, tests, and release |
| Complete User Story Catalog | DEV-18 | Tracks all FR-derived product stories and technical implementation stories before development starts |
| Feature Completion Tracker | DEV-19 | Authoritative implementation completion status for numbered APIs and related gates (not a substitute for DEV-14 backlog) |
| Sprint Backlog | DEV-09 | Tracks first sprint execution |
| Gap Register | PM-06 | Tracks unresolved documentation and source-mapping gaps |
| Code Review Checklist | DEV-10 | Tracks review expectations |

---

# 3. Work Item Types

| Type | Prefix | Example |
|---|---|---|
| Feature | `FEAT` | `FEAT-ORG-001` |
| User Story | `US` | `US-ORG-001` |
| Task | `TASK` | `TASK-BE-ORG-001` |
| Defect | `DEF` | `DEF-ORG-001` |
| Gap | `DOC-GAP` | `DOC-GAP-015` |
| Decision | `DR` | `DR-017` |

---

# 4. Status Workflow

```text
Backlog
    ↓
Ready
    ↓
In Development
    ↓
In Review
    ↓
QA Ready
    ↓
Done
```

Exception statuses:

- Blocked.
- Deferred.
- Superseded.

---

# 5. Status Entry Criteria

| Status | Entry Criteria |
|---|---|
| Backlog | Feature/story identified |
| Ready | Acceptance criteria, traceability, dependencies, and owner are clear |
| In Development | Assigned to developer and branch/work has started |
| In Review | Pull request or review artifact is available |
| QA Ready | Code review complete and test build available |
| Done | Acceptance criteria passed and traceability updated |
| Blocked | Active dependency prevents progress |
| Deferred | Product or release decision postpones work |

---

# 6. Repo-Based Tracking Procedure

Because no agile tool is used:

1. Select features from `DEV-14`.
2. Confirm complete story coverage in `DEV-18`.
3. Confirm module-level grouping in `DEV-15`.
4. Confirm traceability in `DEV-16`.
5. Add selected items to sprint backlog in `DEV-09` or a future sprint document.
6. Track implementation status in the same document row.
7. Update status during development.
8. Record blockers in PM-06 if documentation-related.
9. Record defects in the sprint document or testing evidence.
10. Update Release Management when feature is release candidate ready.

---

# 7. Task Breakdown Standard

Each story should be broken into tasks where applicable:

| Task Type | Example |
|---|---|
| Backend API | Add FastAPI route and schema |
| Backend Service | Add application service behavior |
| Repository | Add SQLAlchemy repository method |
| Migration | Add Alembic migration |
| Flutter UI | Add screen/page/widget |
| API Client | Add Flutter API client method |
| Fixture | Add mock request/response JSON |
| Test | Add unit/API/widget/integration test |
| Documentation | Update affected docs or gap register |

---

# 8. First Sprint Tracking Board

| Tracking ID | Type | Linked Item | Title | Owner | Status |
|---|---|---|---|---|---|
| TASK-FOUND-001 | Task | DEV-SP1-001 | Create monorepo folder structure | Engineering | Ready |
| TASK-FOUND-002 | Task | DEV-SP1-002 | Add Docker Compose for PostgreSQL and Redis | DevOps / Backend | Ready |
| TASK-BE-001 | Task | DEV-SP1-003 | Scaffold FastAPI app | Backend | Ready |
| TASK-BE-002 | Task | DEV-SP1-004 | Configure SQLAlchemy and Alembic | Backend / Database | Ready |
| TASK-BE-003 | Task | DEV-SP1-005 | Add logging, request ID, correlation ID | Backend | Ready |
| TASK-BE-004 | Task | DEV-SP1-006 | Configure Redis and Celery | Backend / DevOps | Ready |
| TASK-FE-001 | Task | DEV-SP1-007 | Scaffold Flutter app | Frontend | Ready |
| TASK-FE-002 | Task | DEV-SP1-008 | Add Flutter app shell | Frontend | Ready |
| TASK-FE-003 | Task | DEV-SP1-009 | Add Flutter API client baseline | Frontend | Ready |
| TASK-ORG-001 | Task | US-ORG-001 | Implement Organization create backend | Backend | Ready |
| TASK-ORG-002 | Task | US-ORG-002 | Implement Organization list backend | Backend | Ready |
| TASK-ORG-003 | Task | US-ORG-001, US-ORG-002 | Implement Organization list and form UI | Frontend | Ready |
| TASK-FAC-001 | Task | US-FAC-001, US-FAC-002 | Implement Facility backend and UI skeleton | Full Stack | Ready |
| TASK-SITE-001 | Task | US-SITE-001, US-SITE-002 | Implement Site backend and UI skeleton | Full Stack | Ready |
| TASK-QA-001 | Task | DEV-US-001 to DEV-US-007 | Add first-slice test coverage | QA / Engineering | Ready |
| TASK-CI-001 | Task | DEV-SP1-014 | Add GitHub Actions baseline | DevOps | Ready |

---

# 9. Defect Tracking Without Agile Tool

Defects shall be recorded in this format:

| Defect ID | Linked Story | Area | Summary | Severity | Owner | Status |
|---|---|---|---|---|---|---|
| DEF-EXAMPLE-001 | US-ORG-001 | Backend | Organization create accepts missing name | High | Backend | Example |

Severity:

- Critical: security, tenant isolation, data loss, app unusable.
- High: core story cannot be completed.
- Medium: non-critical behavior incorrect.
- Low: polish, copy, minor UI issue.

---

# 10. Release Tracking Rule

A feature may be included in a release candidate only when:

- Feature status is Done.
- User stories are Done.
- Traceability row is Done or accepted.
- Tests are complete.
- Known defects are accepted or resolved.
- Release Management includes the feature in approved scope.

---

# 11. Governance

- This workflow remains active until an external agile tool is adopted.
- If an agile tool is adopted later, these IDs shall be preserved and mapped.
- Documentation remains the source of truth for approved scope.
- Status updates shall be made in documentation at the end of each development checkpoint.
