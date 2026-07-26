# Documentation Gap and Source Mapping Register

> Cross-folder register for unresolved documentation gaps, source mappings, baseline decisions, owners, and resolution paths.

---

# Document Control

| Field | Value |
|---|---|
| Document ID | PM-06 |
| Document Name | Documentation Gap and Source Mapping Register |
| Folder | 00_Project_Management |
| Product | Digitize by OreeOn Technologies Pvt. Ltd. |
| Status | Review Draft |
| Owner | Documentation Governance / Product Management |
| Reviewers | Product, Architecture, Database, API, Integration, UI/UX, Backend, DevOps, QA, Operations, Release Management |
| Version | 1.0 |
| Last Updated | 2026-07-24 |

---

# 1. Purpose

This register tracks documentation gaps and unresolved source mappings across the Digitize documentation set.

It prevents unresolved mappings from being hidden inside individual documents and provides an owner, impact, and resolution path for each major gap category.

---

# 2. Scope

This register covers:

- Missing folder indexes.
- Missing governing documents.
- Unresolved source mappings.
- Architecture decision gaps.
- Database mapping gaps.
- API traceability gaps.
- Integration provider mapping gaps.
- UI screen mapping gaps.
- Release evidence mapping gaps.
- Review lifecycle metadata gaps.

---

# 3. Status Definitions

| Status | Meaning |
|---|---|
| Open | Gap exists and needs resolution |
| In Progress | Owner is actively resolving the gap |
| Resolved | Gap is resolved in current documentation |
| Accepted Pending Freeze | Gap is acceptable during Design Draft but must be resolved or formally waived before Frozen |
| Not Applicable | Gap does not apply after review |

---

# 4. Gap Register

| Gap ID | Area | Gap | Impact | Owner | Resolution Path | DR Reference | Status |
|---|---|---|---|---|---|---|---|
| DOC-GAP-001 | Product Foundation | Folder README was missing | New readers lacked folder-level scope and governance | Product Governance | Added `01_Product_Foundation/README.md` | 99_Decision_Records/DR-001_Documentation_Folder_Hierarchy.md | Resolved |
| DOC-GAP-002 | Business Analysis | Folder README was empty | Business Analysis folder lacked scope, audience, register, and governance | Business Analysis / Product Governance | Populated `03_Business_Analysis/README.md` | 99_Decision_Records/DR-002_Governing_Document_Per_Folder.md | Resolved |
| DOC-GAP-003 | Documentation Root | Root docs index was missing | Full documentation hierarchy lacked a top-level index | Documentation Governance | Added `docs/README.md` | 99_Decision_Records/DR-001_Documentation_Folder_Hierarchy.md | Resolved |
| DOC-GAP-004 | Assets | Assets folder had no usage guidance | Asset ownership and safe usage were unclear | Documentation Governance | Added `docs/assets/README.md` | 99_Decision_Records/DR-002_Governing_Document_Per_Folder.md | Resolved |
| DOC-GAP-005 | Database | PostgreSQL was used before a decision record formally selected it | Database README and implementation docs had a governance mismatch | Architecture / Database Engineering | Added `DR-006_PostgreSQL_Database_Baseline.md` and updated Database README | 99_Decision_Records/DR-006_PostgreSQL_Database_Baseline.md | Resolved |
| DOC-GAP-006 | Backend | ORM and migration framework were unresolved | Backend repository and migration docs had implementation ambiguity | Backend Engineering / Database Engineering | Added `DR-007_SQLAlchemy_Alembic_Data_Access_Baseline.md` and updated backend docs | 99_Decision_Records/DR-007_SQLAlchemy_Alembic_Data_Access_Baseline.md | Resolved |
| DOC-GAP-007 | Backend | Cache technology was unresolved | Auth, authorization, and tenant-context caching rules were incomplete | Backend Engineering / DevOps | Added `DR-008_Redis_Cache_Baseline.md` and updated backend docs | 99_Decision_Records/DR-008_Redis_Cache_Baseline.md | Resolved |
| DOC-GAP-008 | Backend / Integration | Worker and queue framework were unresolved | Outbox processing, background jobs, and deployment runtime were ambiguous | Backend Engineering / DevOps | Added `DR-009_Celery_Background_Worker_Baseline.md` and updated BE/IC docs | 99_Decision_Records/DR-009_Celery_Background_Worker_Baseline.md | Resolved |
| DOC-GAP-009 | Deployment | Runtime deployment baseline was unresolved | Infrastructure placement and compute behavior were ambiguous | DevOps / Architecture | Added `DR-010_Kubernetes_Compatible_Container_Deployment_Baseline.md` and updated deployment docs | 99_Decision_Records/DR-010_Kubernetes_Compatible_Container_Deployment_Baseline.md | Resolved |
| DOC-GAP-010 | Security / Deployment | Secret manager was unresolved | Provider credentials, signing material, and deployment secrets lacked a governed baseline | Security / DevOps | Added `DR-011_HashiCorp_Vault_Secrets_Management_Baseline.md` and updated DEP/IC docs | 99_Decision_Records/DR-011_HashiCorp_Vault_Secrets_Management_Baseline.md | Resolved |
| DOC-GAP-011 | Deployment | CI/CD tooling and artifact retention were unresolved | Pipeline gates and release evidence were ambiguous | DevOps / Release Management | Added `DR-012_GitHub_Actions_CI_CD_Baseline.md` and updated DEP/BE docs | 99_Decision_Records/DR-012_GitHub_Actions_CI_CD_Baseline.md | Resolved |
| DOC-GAP-012 | Observability | Observability tooling was unresolved | Metrics, traces, logs, dashboards, and alerting lacked a concrete stack | Operations / DevOps | Added `DR-013_OpenTelemetry_Prometheus_Grafana_Observability_Baseline.md` and updated BE/IC docs | 99_Decision_Records/DR-013_OpenTelemetry_Prometheus_Grafana_Observability_Baseline.md | Resolved |
| DOC-GAP-013 | API / Integration | File storage and scanning baseline was unresolved | File upload/download, storage, scanning, and quarantine behavior were ambiguous | Security / Backend / DevOps | Added `DR-014_S3_Compatible_Object_Storage_File_Scanning_Baseline.md` and updated API/IC docs | 99_Decision_Records/DR-014_S3_Compatible_Object_Storage_File_Scanning_Baseline.md | Resolved |
| DOC-GAP-014 | Database / API | Approved outbox table was missing from DB-11 | API and Integration docs could not map event persistence | Database Engineering / Integration | Added `integration.outbox_event` and `integration.inbox_event` to DB-11 and updated API/IC docs | 99_Decision_Records/DR-009_Celery_Background_Worker_Baseline.md, 99_Decision_Records/DR-006_PostgreSQL_Database_Baseline.md | Resolved |
| DOC-GAP-015 | API | Common reference endpoints lack exact FR source IDs | API-14 cannot be frozen without BA/FR source confirmation | Business Analysis (BA Lead) | Add or confirm FR source IDs for countries, states, currencies, languages, timezones, facility types, activity types, statuses, payment methods, channels, lookup values, and localization. Owner: Business Analysis (BA Lead). Target: 2026-09-30 |  | Open |
| DOC-GAP-016 | API / UI | API screen-level mappings need final UI screen IDs | Screen traceability remains incomplete until UI screen catalog is reviewed | UI/UX (UX Lead) / API | Map API-01 to API-14 endpoints to approved UX-05 screen IDs. Owner: UI/UX (UX Lead). Target: 2026-09-30 |  | Open |
| DOC-GAP-017 | Release Notes | Version-specific release note fields depend on approved release closure | Release_v1.0 and changelog cannot be finalized before Release Management closure | Release Management / Release Notes | Populate release ID, date, type, scope, known issues, and closure reference after RELM-10 evidence is approved | 99_Decision_Records/DR-003_Release_Management_Folder_Addition.md | Accepted Pending Freeze |
| DOC-GAP-018 | Technical Architecture | Architecture review metadata remains Not Started in several TA documents | Architecture folder cannot move to Frozen lifecycle state | Architecture Governance | Perform TA review pass and update review metadata document by document |  | Open |
| DOC-GAP-019 | Database Design | Database review metadata remains Not Started in several DB documents | Database folder cannot move to Frozen lifecycle state | Database Engineering / Architecture | Perform DB review pass and update review metadata document by document |  | Open |
| DOC-GAP-020 | Frontend Development | Frontend engineering standards were missing for Flutter implementation | Development could start without frontend project structure, API client, auth, state, testing, and release rules | Frontend Engineering / UI/UX | Added `16_Development_Readiness/DEV-03_Flutter_Frontend_Engineering_Standards.md` and `DR-015_Flutter_Hybrid_Frontend_Baseline.md` | 99_Decision_Records/DR-015_Flutter_Hybrid_Frontend_Baseline.md | Resolved |
| DOC-GAP-021 | Cloud Provider | AWS provider baseline was not formally documented | Deployment planning lacked provider-specific cloud assumptions | Architecture / DevOps | Added `DR-016_AWS_Cloud_Provider_Baseline.md` | 99_Decision_Records/DR-016_AWS_Cloud_Provider_Baseline.md | Resolved |
| DOC-GAP-022 | Backend Architecture Style | Modular monolith decision was not formally documented | Backend implementation could drift toward microservices or unstructured monolith | Architecture / Backend Engineering | Added `DR-017_Modular_Monolith_Baseline.md` and `16_Development_Readiness/DEV-04_FastAPI_Backend_Start_Plan.md` | 99_Decision_Records/DR-017_Modular_Monolith_Baseline.md | Resolved |
| DOC-GAP-023 | Development Kickoff | Development start plan and first vertical slice were missing | Team lacked a controlled bridge from documentation to code | Engineering Governance / Product | Added `16_Development_Readiness/README.md`, `DEV-00`, `DEV-01`, `DEV-02`, and `DEV-05` |  | Resolved |
| DOC-GAP-024 | User Stories | Development-ready user stories and acceptance criteria were missing | Sprint planning would rely directly on large FRS documents instead of executable stories | Product / Engineering / QA | Added `DEV-06_User_Stories_and_Acceptance_Criteria.md` |  | Resolved |
| DOC-GAP-025 | Screen Handoff | Flutter screen route/widget/API handoff was missing | Frontend implementation could diverge from UI/UX and API contracts | UI/UX / Frontend Engineering | Added `DEV-07_Flutter_Screen_Implementation_Handoff.md` |  | Resolved |
| DOC-GAP-026 | Mock API and Fixtures | Mock strategy and reusable fixture guidance were missing | Frontend and tests could use inconsistent synthetic data | API / QA / Frontend Engineering | Added `DEV-08_Mock_API_and_Fixture_Strategy.md` and `DEV-12_API_Fixture_Catalog.md` |  | Resolved |
| DOC-GAP-027 | Sprint Backlog | First implementation sprint backlog was missing | Initial development scope could expand without control | Product / Engineering | Added `DEV-09_First_Development_Sprint_Backlog.md` |  | Resolved |
| DOC-GAP-028 | Code Review | Code review checklist was missing | Review quality could vary across frontend, backend, DB, security, and testing | Engineering Governance | Added `DEV-10_Code_Review_Checklist.md` |  | Resolved |
| DOC-GAP-029 | Developer Onboarding | Developer setup and onboarding guide was missing | New developers lacked a consistent setup path | Engineering Governance | Added `DEV-11_Developer_Onboarding_Guide.md` |  | Resolved |
| DOC-GAP-030 | Flutter Components | Flutter component implementation map was missing | UI implementation could duplicate or diverge from design system | UI/UX / Frontend Engineering | Added `DEV-13_Flutter_Component_Implementation_Map.md` |  | Resolved |
| DOC-GAP-031 | Assets | Asset and icon register was missing | Brand, icon, and runtime asset ownership was unclear | UI/UX / Frontend Engineering | Added `docs/assets/Asset_Register.md` |  | Resolved |
| DOC-GAP-032 | Feature Backlog | Actual product feature backlog was missing | Development could start without a controlled list of feature scope across modules | Product / Engineering | Added `DEV-14_Product_Feature_Backlog.md` |  | Resolved |
| DOC-GAP-033 | User Story Map | Actual module-level user stories were missing | Implementation tracking would rely on formats instead of real development stories | Product / Engineering / QA | Added `DEV-15_Module_User_Story_Map.md` |  | Resolved |
| DOC-GAP-034 | Feature Traceability | Feature and story traceability to FR, API, DB, UI, testing, and release readiness was missing | Teams could build features without clear source and verification linkage | Product / Engineering / QA | Added `DEV-16_Feature_Traceability_Matrix.md` |  | Resolved |
| DOC-GAP-035 | Development Tracking | Repo-based development tracking workflow was missing | Without an agile tool, statuses, tasks, defects, and release tracking could become inconsistent | Engineering Governance / Product | Added `DEV-17_Development_Tracking_Workflow.md` |  | Resolved |
| DOC-GAP-036 | Complete User Stories | Full FR-derived user story catalog was missing | Development could miss approved requirements or undercount frontend, backend, database, testing, and deployment work | Product / Engineering / QA / DevOps | Added `DEV-18_Complete_User_Story_Catalog.md` with 237 product stories and 40 technical implementation stories |  | Resolved |

---

# 5. Resolution Rules

- Resolved gaps shall remain in this register for traceability.
- Open gaps shall have an owner and resolution path before any affected folder is frozen.
- Source mappings shall be resolved to approved BA, FR, DB, API, UI, IC, BE, DEP, TEST, OPS, RELM, RN, or DR references.
- If a mapping cannot be resolved before freeze, it shall require an explicit waiver from the affected folder owner and Architecture or Product Governance.
- Waivers shall be time-bounded and traceable to a decision record or change request.

---

# 6. Freeze Rule

This register shall be reviewed before any major folder moves to Frozen status.

Open gaps are allowed during Design Draft only when they are explicitly owned, visible, and not blocking the current folder lifecycle.

---

# 7. Summary

This register is the control point for documentation completeness.

It turns unresolved placeholders into managed work items with owners, impact, and resolution paths.
