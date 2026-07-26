# Database Design Freeze Checklist — Digitize

This checklist packages the minimal approvals and unresolved decisions required to freeze the Database Design artifacts under `docs/06_Database_Design`.

Status: Frozen (provisional) — sign-off package created; approvals pending. See docs/00_Project_Management/Signoff_Package_DB_Design_Freeze_2026-07-26.md

## Required approvals (sign-off)
- Product Architecture (Business Owner)
- Data Architecture (Technical Owner)
- Solution Architecture
- Security Architecture
- Finance/Commercial owner (billing & reconciliation)
- Compliance/Audit owner
- DevOps/Platform owner (migration & backup)

## Key unresolved architecture decisions to approve
- Tenancy implementation pattern (shared DB/shared schema vs schema-per-tenant vs db-per-tenant). Current docs assume shared DB/shared schema. (Owner: Solution Architecture)
- Migration tooling selection (Flyway recommended) and CI/CD migration pipeline ownership. (Owner: DevOps)
- RPO/RTO targets for production (DB-14 cross-check with SLA). (Owner: Platform / Ops)
- Retention classes and legal hold policies for audit/financial data (DB-09/DB-17). (Owner: Compliance)
- Row-Level Security adoption scope and enforcement (DB-15). (Owner: Security)
- Partitioning thresholds for time-series tables (attendance, audit, notifications) — approve partition strategy and timelines. (Owner: Data Architecture)

## Immediate pre-freeze tasks (must complete before freeze)
- All DB-* documents marked `Database Review: Ready for Review` (DONE)
- Owners assigned for each unresolved decision above (assign names and emails)
- DB-10 Data Dictionary: populate authoritative column-level traceability entries (owner: domain data owners)
- Convert DB-11 scripts into versioned migration files per chosen tooling (owner: Engineering)
- Create migration test suite per DB-18 and run on staging (owner: QA/Engineering)
- Run at least one full backup+restore verification exercise (owner: DevOps)

## Checklist sign-off (when all items completed)
- [ ] Product Architecture
- [ ] Data Architecture
- [ ] Solution Architecture
- [ ] Security Architecture
- [ ] Finance/Commercial
- [ ] Compliance/Audit
- [ ] DevOps/Platform
- [ ] QA Lead

## Notes / Next steps
- After sign-off, mark DB-* documents as `Database Review: Passed` and change `Document State` to `Frozen` where appropriate.
- Track final migration artifacts in a release branch and open a PR for review containing migrations and seed data.
