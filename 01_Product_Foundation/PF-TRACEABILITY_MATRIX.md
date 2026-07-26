# PF — Traceability Matrix (Product Foundation → Downstream Artifacts)

**Document ID:** PF-TRACE

**Purpose:** Provide a concise, implementation-ready mapping from Product Foundation items to downstream artifacts (BRD, FRS, API, DB, UI, Tests). This file is intended to be used by Business Analysts, Architects, and Engineers to ensure changes in Product Foundation are traced to implementation artifacts.

---

| PF Item | PF Source File | Consumer Artifact | Recommended Target File / Location | Notes / Acceptance Criteria |
|---|---:|---|---|---|
| Business Terminology (Glossary) | PF-01_Product_Glossary.md | BRD, FRS, API, DB, UI | `docs/03_Business_Analysis/BRD.md`, `docs/04_Functional_Requirements/FRS-*.md`, `docs/07_API_Collections/` | All downstream documents must reference PF-01 for definitions. Changes require versioned update in PF-01 and Decision Record.
| Domain Model (entities & relationships) | PF-02_Domain_Model.md | Database Design, Backend, API | `docs/06_Database_Design/ERD.md`, `docs/10_Backend_Engineering/` | Domain entities map to logical DB tables and API resources; ownership and lifecycle must be preserved.
| Approval Workflow (governance) | PF-02 & PF-01 | BRD, FRS, UI, API | `docs/04_Functional_Requirements/Approval_Flows.md`, `docs/07_API_Collections/approval-api.md` | Approval request lifecycle must be implemented with audit trail and notifications.
| Roles & RBAC | PF-01 & PF-02 | UI, API, Backend | `docs/07_API_Collections/auth.md`, `docs/10_Backend_Engineering/rbac.md` | Map role names and permissions exactly as PF docs; Platform/Organization/Site Admin roles must match.
| Membership & Billing | PF-02 & PF-04 | FRS, API, DB | `docs/04_Functional_Requirements/membership.md`, `docs/06_Database_Design/billing.md` | Payment flows must follow PCI guidance and audit controls.
| Notifications & Campaigns | PF-01 & PF-05 | API, UI | `docs/07_API_Collections/notifications.md`, `docs/09_UI_UX_Design/` | Notification templates and triggers must be specified in FRS.
| Roadmap Phase 1 Scope | PF-05 | Implementation Backlog, Release Plan | `docs/16_Development_Readiness/release-plan.md` | Phase 1 modules become MCP; out-of-scope items listed must not be included in Phase 1 deliveries.
| Security & Compliance (controls) | README + PF-06 | Tech Architecture, DB, API | `docs/05_Technical_Architecture/security.md`, `docs/06_Database_Design/` | Must be implemented and verified before freeze; see PF-06 checklist.

---

## Usage

- Business Analysts and Architects must reference this matrix when authoring BRD/FRS and ensure traceability IDs are added to requirement sections.
- Engineers must link code and DB designs to PF item IDs in their design docs.
- QA must include traceability checks in test plans to validate PF requirements.

---

## Next steps (recommended)

1. Add Requirement IDs in BRD/FRS linking back to PF document and section (e.g., `PF-02:6.3.2`).
2. Update API docs to include `PF` trace reference in resource descriptions.
3. Ensure DB ERD includes owner and lifecycle mapping for each entity from PF-02.
