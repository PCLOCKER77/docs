# Decision Records Documentation

> Cross-folder decision records, rationale, alternatives, consequences, and traceability for Digitize by OreeOn Technologies Pvt. Ltd.

---

# 1. Purpose

This folder preserves major decisions made across the Digitize documentation set.

Decision Records explain what was decided, why it was decided, what alternatives were considered, what tradeoffs were accepted, and which documentation areas are affected.

This folder supports future architecture review, onboarding, audit review, implementation planning, and controlled change management.

---

# 2. Scope

This folder covers:

- Product decisions.
- Architecture decisions.
- Documentation governance decisions.
- Platform hierarchy decisions.
- Engineering baseline decisions.
- Release governance decisions.
- Cross-folder ownership decisions.
- Supersession and decision-change history.

---

# 3. Out of Scope

This folder does not define:

- Product requirements.
- Business process details.
- Database schema definitions.
- API endpoint catalogs.
- Integration behavior.
- UI screen layouts.
- Backend implementation details.
- Deployment runbooks.
- Test execution.
- Operational procedures.
- Release notes.

Those artifacts remain owned by their respective documentation folders.

---

# 4. Folder Position

```text
01_Product_Foundation/
02_Commercial_Strategy/
03_Business_Analysis/
04_Functional_Requirements/
05_Technical_Architecture/
06_Database_Design/
07_API_Collections/
08_Integration_Contracts/
09_UI_UX_Design/
10_Backend_Engineering/
11_Deployment/
12_Testing/
13_Operations/
14_Release_Management/
15_Release_Notes/
16_Development_Readiness/
99_Decision_Records/
```

Decision Records sits outside the normal delivery sequence.

It does not replace folder-level standards. It records decisions that materially affect multiple folders or long-term governance.

---

# 5. Relationship with Existing Decision Documents

| Existing Document | Relationship |
|---|---|
| `00_Project_Management/Decision_Log.md` | Product and project decision register |
| `05_Technical_Architecture/TA-10_Architecture_Decision_Records.md` | Architecture decision index for technical architecture |
| `99_Decision_Records/` | Cross-folder decision records with rationale, consequences, and traceability |

The existing decision log and TA-10 may remain as source or index documents.

This folder provides detailed cross-folder records for decisions that need durable governance.

---

# 6. Folder Structure

```text
99_Decision_Records/
├── README.md
├── DR-00_Decision_Record_Standards.md
├── DR-Template_Decision_Record_Template.md
├── DR-001_Documentation_Folder_Hierarchy.md
├── DR-002_Governing_Document_Per_Folder.md
├── DR-003_Release_Management_Folder_Addition.md
├── DR-004_Platform_Tenant_Hierarchy.md
├── DR-005_Backend_FastAPI_Baseline.md
├── DR-006_PostgreSQL_Database_Baseline.md
├── DR-007_SQLAlchemy_Alembic_Data_Access_Baseline.md
├── DR-008_Redis_Cache_Baseline.md
├── DR-009_Celery_Background_Worker_Baseline.md
├── DR-010_Kubernetes_Compatible_Container_Deployment_Baseline.md
├── DR-011_HashiCorp_Vault_Secrets_Management_Baseline.md
├── DR-012_GitHub_Actions_CI_CD_Baseline.md
├── DR-013_OpenTelemetry_Prometheus_Grafana_Observability_Baseline.md
├── DR-014_S3_Compatible_Object_Storage_File_Scanning_Baseline.md
├── DR-015_Flutter_Hybrid_Frontend_Baseline.md
├── DR-016_AWS_Cloud_Provider_Baseline.md
├── DR-017_Modular_Monolith_Baseline.md
├── DR-018_Engineering_Foundation_Runtime.md
├── DR-019_Access_Mobile_Commerce_Architecture.md
├── DR-020_API-05_Membership_Plan_and_Membership_Scope.md
├── DR-021_Organization_Onboarding_PA_Boundary.md
└── DR-023_Company_Branch_Site_Facility_Hierarchy.md
```

DR-022 is reserved outside this folder for Customer Data Protection + Customer Module (`docs/architecture/DR-022_TRANSITION_FROM_DR-021.md`) and is not issued here.

---

# 7. Document Register

| Document ID | Document Name | Status | Purpose |
|---|---|---|---|
| README | Decision Records Documentation | Review Draft | Defines folder scope, boundaries, structure, and governance |
| DR-00 | Decision Record Standards | Design Draft | Defines common standards for decision records |
| DR-Template | Decision Record Template | Design Draft | Provides the reusable decision-record template |
| DR-001 | Documentation Folder Hierarchy | Design Draft | Records the approved documentation hierarchy decision |
| DR-002 | Governing Document Per Folder | Design Draft | Records the folder governance model |
| DR-003 | Release Management Folder Addition | Design Draft | Records the decision to add Release Management before Release Notes |
| DR-004 | Platform Tenant Hierarchy | Design Draft | Records the Platform to Organization to Facility to Site hierarchy |
| DR-005 | Backend FastAPI Baseline | Design Draft | Records the backend framework and baseline technology decision |
| DR-006 | PostgreSQL Database Baseline | Accepted | Records PostgreSQL as the database implementation baseline |
| DR-007 | SQLAlchemy and Alembic Data Access Baseline | Accepted | Records ORM and migration framework baseline |
| DR-008 | Redis Cache Baseline | Accepted | Records Redis as the runtime cache baseline |
| DR-009 | Celery Background Worker Baseline | Accepted | Records Celery as the background worker baseline |
| DR-010 | Kubernetes-Compatible Container Deployment Baseline | Accepted | Records containerized deployment and orchestration baseline |
| DR-011 | HashiCorp Vault Secrets Management Baseline | Accepted | Records secrets-management baseline |
| DR-012 | GitHub Actions CI/CD Baseline | Accepted | Records CI/CD orchestration baseline |
| DR-013 | OpenTelemetry, Prometheus, and Grafana Observability Baseline | Accepted | Records observability tooling baseline |
| DR-014 | S3-Compatible Object Storage and File Scanning Baseline | Accepted | Records object storage and malware scanning baseline |
| DR-015 | Flutter Hybrid Frontend Baseline | Accepted | Records Flutter as the web, Android, and iOS frontend baseline |
| DR-016 | AWS Cloud Provider Baseline | Accepted | Records AWS as the cloud provider baseline |
| DR-017 | Modular Monolith Baseline | Accepted | Records modular monolith as the initial backend architecture style |
| DR-018 | Engineering Foundation Runtime | Accepted | Records logging, IDs, UoW, pool, and deferred Redis/S3/Celery/JWT wiring |
| DR-019 | Access, Mobile Persona, and Commerce Architecture | Accepted | Records roles, Phase-1 personas, SaaS vs facility commerce (v2.0: Site Admin; no Manager role) |
| DR-020 | API-05 Membership Plan and Membership Scope | Accepted | Option C; Slice 1 = 12 membership ops; plan status DRAFT/ACTIVE/ARCHIVED; 228 unchanged |
| DR-021 | Organization Onboarding and PA Boundary | Implementation Complete / Verification Pending | OA T&C / conditional PA approve; OA credential policy (local temp / QA+Prod setup link); PA ≠ tenant-data superuser; 228 unchanged; browser click-through pending; do not reopen |
| DR-022 | Customer Data Protection + Customer Module | Reserved (not issued in this folder) | Reserved by `docs/architecture/DR-022_TRANSITION_FROM_DR-021.md`. Do not reuse this ID. |
| DR-023 | Company → Branch/Site → Facility Hierarchy | Accepted | Target Company → Site/Branch → Facility → Staff; no Site/Branch Admin; facility billing unchanged. Development implementation authorized 2026-10-16. Deploy/`main` not authorized. Plan: `docs/architecture/DR-023_HIERARCHY_MIGRATION_PLAN.md`. |

---

# 8. Decision Record Principles

Decision Records follow these principles:

- Decisions are explicit.
- Rationale is preserved.
- Alternatives are documented.
- Consequences are acknowledged.
- Ownership is clear.
- Status is visible.
- Superseded decisions are not deleted.
- Cross-folder impact is traceable.
- Decision records do not redefine implementation details.

---

# 9. Governance

Decision Records documentation follows these governance rules:

- `DR-00` governs all decision records in this folder.
- Each decision record shall use a stable decision ID.
- Frozen decision records shall not be edited to change the decision outcome.
- A changed decision shall be captured through a new superseding decision record.
- Superseded decisions shall remain available for historical traceability.
- Decision records shall reference affected documentation folders.
- Decision records shall not duplicate full content from source documents.

---

# 10. Summary

The Decision Records folder is the long-term memory of the Digitize documentation set.

It explains why major choices were made and helps future teams change the platform with context instead of guesswork.
