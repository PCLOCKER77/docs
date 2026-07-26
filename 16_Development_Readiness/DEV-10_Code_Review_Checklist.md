# DEV-10 Code Review Checklist

> Code review checklist for Digitize frontend, backend, database, API, security, testing, and documentation changes.

---

# Document Control

| Field | Value |
|---|---|
| Document ID | DEV-10 |
| Document Name | Code Review Checklist |
| Folder | 16_Development_Readiness |
| Product | Digitize by OreeOn Technologies Pvt. Ltd. |
| Status | Design Draft |
| Owner | Engineering Governance |
| Reviewers | Frontend, Backend, Database, API, Security, QA, DevOps |
| Version | 1.0 |
| Last Updated | 2026-07-24 |

---

# 1. Purpose

This checklist defines minimum review expectations for implementation changes.

---

# 2. General Review Checks

- Change matches approved documentation.
- No unrelated refactor is included.
- Naming follows project conventions.
- Errors are handled safely.
- Tests are included or risk is explained.
- No secrets or sensitive data are committed.
- Logs do not expose sensitive values.
- Documentation is updated where behavior changes.

---

# 3. Backend Review Checks

- FastAPI route contains transport logic only.
- Application service owns use-case orchestration.
- Domain rules are not placed in routers.
- Repository owns persistence concerns only.
- Tenant context is enforced.
- Authorization is enforced server-side.
- Transactions are explicit.
- SQLAlchemy session use is safe.
- Alembic migration is reviewed where schema changes occur.
- Outbox event is used for async side effects where required.

---

# 4. Flutter Review Checks

- Screen follows approved UX handoff.
- API calls go through client layer.
- Loading, empty, error, and success states exist.
- Validation is clear and user-safe.
- Permissions affect UI but do not replace backend enforcement.
- Layout works on mobile, tablet, and web.
- No environment URLs or secrets are hardcoded.
- Widget tests exist for critical components.

---

# 5. Database Review Checks

- Migration is reversible where practical.
- Tenant-owned tables include tenant scope.
- Indexes support expected queries.
- Constraints protect integrity.
- Seed data is safe and environment-aware.
- No production data is embedded.

---

# 6. Security Review Checks

- Authentication and authorization are enforced.
- Tenant isolation is preserved.
- Sensitive data is redacted.
- File handling uses scanning and safe metadata.
- Secrets use approved configuration paths.
- Dependency risks are reviewed.

---

# 7. Approval Rule

High-risk changes require review from the relevant owner:

- Security for auth, secrets, permissions, sensitive data.
- Database for schema and migration changes.
- DevOps for deployment and CI/CD changes.
- Product or BA for behavior changes.

---

# 8. Pull Request Template Checklist

Every pull request should answer:

- What changed?
- Which requirement, story, or gap does this address?
- Which user roles are affected?
- Which tenant scopes are affected?
- Which API contracts are affected?
- Which migrations are included?
- Which tests were added or updated?
- Which documentation changed?
- Are there deployment or rollback considerations?

---

# 9. Reviewer Matrix

| Change Type | Required Reviewer |
|---|---|
| Product behavior | Product / Business Analysis |
| API contract | API / Backend |
| Database migration | Database Engineering |
| Auth or permissions | Security / Backend |
| Tenant context | Architecture / Backend |
| Flutter screen | UI/UX / Frontend |
| Shared Flutter component | UI/UX / Frontend |
| CI/CD | DevOps |
| Deployment config | DevOps / Security |
| Test framework | QA / Engineering |

---

# 10. Severity Guidance

| Severity | Meaning | Merge Rule |
|---|---|---|
| Critical | Security, tenant isolation, data loss, release blocker | Must fix before merge |
| High | Functional breakage, migration risk, contract mismatch | Must fix or explicitly approve |
| Medium | Maintainability, incomplete tests, unclear ownership | Fix before release branch |
| Low | Style, naming, minor cleanup | May fix in same PR or follow-up |

---

# 11. Flutter-Specific Review Details

Reviewers shall check:

- `BuildContext` is not used after unsafe async gaps.
- State updates are guarded where widget lifecycle requires it.
- Widget tree remains readable.
- Shared components are reused instead of duplicated.
- Platform-specific code is isolated.
- App works with keyboard and touch input where applicable.
- Large screens do not look like stretched mobile screens.

---

# 12. FastAPI-Specific Review Details

Reviewers shall check:

- Pydantic schemas are separated from ORM models.
- Route dependencies are explicit.
- Error responses follow API standards.
- DB session lifecycle is controlled.
- Async/sync boundaries are intentional.
- Background jobs are not launched before transaction commit unless safe.
- Idempotency is considered for retry-prone operations.

---

# 13. Migration Review Details

Reviewers shall check:

- Migration has a clear purpose.
- Migration order is safe.
- Existing data impact is understood.
- Downgrade or rollback limitation is documented.
- Index creation is considered for large tables.
- Tenant-scoped uniqueness is correct.
- Seed data is idempotent where applicable.

