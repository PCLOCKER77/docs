# BE Traceability Mappings

> Consolidated traceability references for BE-00 through BE-11.

Purpose: provide explicit upstream source links (Functional Requirements, API Collections, Database Design, Integration Contracts, Technical Architecture, Product Foundation and Decision Records) referenced by backend documents.

Notes:
- This file collects authoritative source documents referenced by BE documentation.
- For release-specific evidence (BE-11) populate release instances with links to CI/Test artifacts and approval records.

---

## Global source anchors
- Product Foundation: [docs/01_Product_Foundation/README.md](docs/01_Product_Foundation/README.md)
- Functional Requirements index: [docs/04_Functional_Requirements/README.md](docs/04_Functional_Requirements/README.md)
- API Collections index: [docs/07_API_Collections/README.md](docs/07_API_Collections/README.md)
- Database Design index: [docs/06_Database_Design/README.md](docs/06_Database_Design/README.md)
- Integration Contracts index: [docs/08_Integration_Contracts/README.md](docs/08_Integration_Contracts/README.md)
- Technical Architecture index: [docs/05_Technical_Architecture/README.md](docs/05_Technical_Architecture/README.md)
- Decision Records (DR/ADR): [docs/99_Decision_Records/README.md](docs/99_Decision_Records/README.md)
- UI/UX Design index: [docs/09_UI_UX_Design/README.md](docs/09_UI_UX_Design/README.md)

---

## BE-00 — Backend Engineering Standards
Trace to:
- Product Foundation: [docs/01_Product_Foundation/PF-02_Domain_Model.md](docs/01_Product_Foundation/PF-02_Domain_Model.md)
- Technical Architecture: [docs/05_Technical_Architecture/TA-00_Technical_Architecture_Standards.md](docs/05_Technical_Architecture/TA-00_Technical_Architecture_Standards.md)
- Database Decision Records: [docs/99_Decision_Records/DR-006_PostgreSQL_Database_Baseline.md](docs/99_Decision_Records/DR-006_PostgreSQL_Database_Baseline.md)
- ORM/Migration Decision: [docs/99_Decision_Records/DR-007_SQLAlchemy_Alembic_Data_Access_Baseline.md](docs/99_Decision_Records/DR-007_SQLAlchemy_Alembic_Data_Access_Baseline.md)
- Worker baseline: [docs/99_Decision_Records/DR-009_Celery_Background_Worker_Baseline.md](docs/99_Decision_Records/DR-009_Celery_Background_Worker_Baseline.md)
- Observability baseline: [docs/99_Decision_Records/DR-013_OpenTelemetry_Prometheus_Grafana_Observability_Baseline.md](docs/99_Decision_Records/DR-013_OpenTelemetry_Prometheus_Grafana_Observability_Baseline.md)
- API Collections guidance: [docs/07_API_Collections/API-00_API_Collection_Standards.md](docs/07_API_Collections/API-00_API_Collection_Standards.md)

## BE-01 — Backend Application Architecture
Trace to:
- Functional Requirements group: [docs/04_Functional_Requirements/README.md](docs/04_Functional_Requirements/README.md)
- Technical Architecture: [docs/05_Technical_Architecture/TA-02_System_Architecture.md](docs/05_Technical_Architecture/TA-02_System_Architecture.md)
- Database Design: [docs/06_Database_Design/DB-01_Conceptual_Data_Model.md](docs/06_Database_Design/DB-01_Conceptual_Data_Model.md)
- API Collections: [docs/07_API_Collections/README.md](docs/07_API_Collections/README.md)
- Integration Contracts: [docs/08_Integration_Contracts/README.md](docs/08_Integration_Contracts/README.md)

## BE-02 — FastAPI Project Structure
Trace to:
- Decision Record: `DR-005_Backend_FastAPI_Baseline` ([docs/99_Decision_Records/DR-005_Backend_FastAPI_Baseline.md](docs/99_Decision_Records/DR-005_Backend_FastAPI_Baseline.md))
- ORM/Migration: [docs/99_Decision_Records/DR-007_SQLAlchemy_Alembic_Data_Access_Baseline.md](docs/99_Decision_Records/DR-007_SQLAlchemy_Alembic_Data_Access_Baseline.md)
- Worker baseline: [docs/99_Decision_Records/DR-009_Celery_Background_Worker_Baseline.md](docs/99_Decision_Records/DR-009_Celery_Background_Worker_Baseline.md)
- CI baseline: [docs/99_Decision_Records/DR-012_GitHub_Actions_CI_CD_Baseline.md](docs/99_Decision_Records/DR-012_GitHub_Actions_CI_CD_Baseline.md)

## BE-03 — Domain Service Design
Trace to:
- Relevant Functional Requirements (example modules):
  - Membership: [docs/04_Functional_Requirements/FR-08_Membership_Management.md](docs/04_Functional_Requirements/FR-08_Membership_Management.md)
  - Attendance: [docs/04_Functional_Requirements/FR-09_Attendance_Management.md](docs/04_Functional_Requirements/FR-09_Attendance_Management.md)
  - Trainer/Batch: [docs/04_Functional_Requirements/FR-11_Trainer_Management.md](docs/04_Functional_Requirements/FR-11_Trainer_Management.md)
- API State & Workflow: [docs/07_API_Collections/API-24_API_State_and_Workflow_Contract.md](docs/07_API_Collections/API-24_API_State_and_Workflow_Contract.md)
- Integration Contracts for long-running flows: [docs/08_Integration_Contracts/IC-09_Event_Outbox_Integration_Contract.md](docs/08_Integration_Contracts/IC-09_Event_Outbox_Integration_Contract.md)

## BE-04 — Repository Data Access Standards
Trace to:
- Database design index: [docs/06_Database_Design/README.md](docs/06_Database_Design/README.md)
- DDL/DML scripts: [docs/06_Database_Design/DB-11_Database_DDL_DML_Scripts.md](docs/06_Database_Design/DB-11_Database_DDL_DML_Scripts.md)
- DR-007 (SQLAlchemy & Alembic): [docs/99_Decision_Records/DR-007_SQLAlchemy_Alembic_Data_Access_Baseline.md](docs/99_Decision_Records/DR-007_SQLAlchemy_Alembic_Data_Access_Baseline.md)

## BE-05 — Authentication & Authorization Implementation
Trace to:
- API Identity collection: [docs/07_API_Collections/API-03_Identity_User_Role_Collection.md](docs/07_API_Collections/API-03_Identity_User_Role_Collection.md)
- Security architecture: [docs/05_Technical_Architecture/TA-05_Security_Identity_Architecture.md](docs/05_Technical_Architecture/TA-05_Security_Identity_Architecture.md)
- Decision records for identity/provider: [docs/99_Decision_Records/ADR-039.md](docs/99_Decision_Records/ADR-039) <!-- ADR file placeholder if present -->

## BE-06 — Tenant Context Implementation
Trace to:
- Product domain model: [docs/01_Product_Foundation/PF-02_Domain_Model.md](docs/01_Product_Foundation/PF-02_Domain_Model.md)
- Functional Requirements: Organization/Facility/Site: [docs/04_Functional_Requirements/FR-03_Organization_Management.md](docs/04_Functional_Requirements/FR-03_Organization_Management.md)
- Database tenancy patterns: [docs/06_Database_Design/DB-04_Multi_Tenancy_Data_Design.md](docs/06_Database_Design/DB-04_Multi_Tenancy_Data_Design.md)
- Tenant ADRs/DRs: [docs/99_Decision_Records/DR-004_Platform_Tenant_Hierarchy.md](docs/99_Decision_Records/DR-004_Platform_Tenant_Hierarchy.md)

## BE-07 — API Implementation Standards
Trace to:
- API Collection standards and catalogs: [docs/07_API_Collections/API-00_API_Collection_Standards.md](docs/07_API_Collections/API-00_API_Collection_Standards.md)
- OpenAPI governance: [docs/07_API_Collections/API-21_OpenAPI_Specification_Governance.md](docs/07_API_Collections/API-21_OpenAPI_Specification_Governance.md)
- Error code catalog: [docs/07_API_Collections/API-19_API_Error_Code_Catalog.md](docs/07_API_Collections/API-19_API_Error_Code_Catalog.md)

## BE-08 — Error Handling & Logging Standards
Trace to:
- Observability architecture: [docs/05_Technical_Architecture/TA-07_Observability_Operations_Architecture.md](docs/05_Technical_Architecture/TA-07_Observability_Operations_Architecture.md)
- Integration observability: [docs/08_Integration_Contracts/IC-13_Integration_Observability_Contract.md](docs/08_Integration_Contracts/IC-13_Integration_Observability_Contract.md)
- Decision records for telemetry: [docs/99_Decision_Records/DR-013_OpenTelemetry_Prometheus_Grafana_Observability_Baseline.md](docs/99_Decision_Records/DR-013_OpenTelemetry_Prometheus_Grafana_Observability_Baseline.md)

## BE-09 — Background Jobs & Outbox Implementation
Trace to:
- Outbox integration contract: [docs/08_Integration_Contracts/IC-09_Event_Outbox_Integration_Contract.md](docs/08_Integration_Contracts/IC-09_Event_Outbox_Integration_Contract.md)
- Worker baseline: [docs/99_Decision_Records/DR-009_Celery_Background_Worker_Baseline.md](docs/99_Decision_Records/DR-009_Celery_Background_Worker_Baseline.md)
- Database outbox table reference: [docs/06_Database_Design/DB-11_Database_DDL_DML_Scripts.md](docs/06_Database_Design/DB-11_Database_DDL_DML_Scripts.md)

## BE-10 — Testing Quality Standards
Trace to:
- API test scenarios: [docs/07_API_Collections/API_Test_Cases.md](docs/07_API_Collections/API_Test_Cases.md)
- CI baseline: [docs/99_Decision_Records/DR-012_GitHub_Actions_CI_CD_Baseline.md](docs/99_Decision_Records/DR-012_GitHub_Actions_CI_CD_Baseline.md)
- Database testing guidelines: [docs/06_Database_Design/DB-18_Testing_and_SQL_Standards.md](docs/06_Database_Design/DB-18_Testing_and_SQL_Standards.md)

## BE-11 — Backend Release Readiness Checklist
Trace to (evidence anchors and reference docs):
- Release governance: [docs/14_Release_Management/README.md](docs/14_Release_Management/README.md)
- API release guidance: [docs/07_API_Collections/API-26_API_Release_and_Consumer_Readiness_Checklist.md](docs/07_API_Collections/API-26_API_Release_and_Consumer_Readiness_Checklist.md)
- Migration/DB review: [docs/06_Database_Design/DB-11_Database_DDL_DML_Scripts.md](docs/06_Database_Design/DB-11_Database_DDL_DML_Scripts.md)
- CI/CD evidence: [docs/99_Decision_Records/DR-012_GitHub_Actions_CI_CD_Baseline.md](docs/99_Decision_Records/DR-012_GitHub_Actions_CI_CD_Baseline.md)
- Security review guidance: [docs/05_Technical_Architecture/TA-05_Security_Identity_Architecture.md](docs/05_Technical_Architecture/TA-05_Security_Identity_Architecture.md)

---

If you want, I can now:
- Replace inline `[[TBD — Source mapping pending — see BE traceability mappings](docs/10_Backend_Engineering/BE-TRACEABILITY_MAPPINGS.md) — see BE traceability mappings](docs/10_Backend_Engineering/BE-TRACEABILITY_MAPPINGS.md)` occurrences inside each BE document with the specific links above (requires permission to edit each file).  
- Or keep this consolidated file as the single authoritative mapping and mark BE docs as referencing it.

Which would you prefer? (A) Apply mappings into each BE document, or (B) keep this central mapping file and leave BE docs unchanged (I recommend B for minimal edits). 
