# DR-004 Platform Tenant Hierarchy

> Decision record for the Digitize Platform to Organization to Facility to Site hierarchy.

---

# Document Control

| Field | Value |
|---|---|
| Document ID | DR-004 |
| Document Name | Platform Tenant Hierarchy |
| Folder | 99_Decision_Records |
| Product | Digitize by OreeOn Technologies Pvt. Ltd. |
| Status | Design Draft |
| Owner | Product / Architecture Governance |
| Reviewers | Product, Business Analysis, Architecture, Database, Backend Engineering, API, UI/UX, Operations |
| Version | 1.0 |
| Last Updated | 2026-07-24 |
| Related Source | `00_Project_Management/Decision_Log.md` DEC-003 |
| Supersedes | None |
| Superseded By | None |

---

# 1. Decision Summary

Digitize shall use the following hierarchy:

```text
Platform
    ↓
Organization
    ↓
Facility
    ↓
Site
```

---

# 2. Context

Digitize is intended to support configurable SaaS operations across multiple business and activity types.

The hierarchy must support an organization operating multiple facilities and each facility operating one or more physical or operational sites.

---

# 3. Decision

The platform hierarchy shall be:

- Platform: the Digitize SaaS platform.
- Organization: the legal or commercial customer entity.
- Facility: the business or activity type operated by an organization.
- Site: the operational location or unit where day-to-day work occurs.

All product, database, API, integration, UI/UX, backend, deployment, testing, operations, release management, and release notes documentation shall respect this hierarchy where tenant context or operational ownership is relevant.

---

# 4. Alternatives Considered

| Option | Description | Outcome |
|---|---|---|
| Platform to Organization only | Simple tenant model | Rejected because facility and site operations require separate governance |
| Organization to Site only | Treat sites as the primary operating unit | Rejected because future facility types need a middle layer |
| Platform to Organization to Facility to Site | Supports multi-facility and multi-site operations | Accepted |

---

# 5. Rationale

The accepted hierarchy supports current swimming pool operations while preserving future extensibility for other facility types such as gym, yoga center, sports academy, or activity venue.

It also aligns tenant isolation, role assignment, reporting, pricing, operations, and support with the way customer organizations are expected to operate.

---

# 6. Consequences

## Positive Consequences

- Multi-tenant boundaries are clearer.
- Facility expansion is supported without changing the platform model.
- Site-level operations can vary by location.
- API, database, UI, and backend documents share a common hierarchy.

## Tradeoffs

- The model is more complex than a flat tenant model.
- Authorization and reporting must account for multiple hierarchy levels.

## Risks

- If tenant context is inconsistently applied, data isolation and operational correctness may be affected.

---

# 7. Affected Documentation

| Folder / Document | Impact |
|---|---|
| `01_Product_Foundation/` | Product terminology and hierarchy |
| `03_Business_Analysis/` | Business actors and workflows |
| `04_Functional_Requirements/` | Tenant-aware requirements |
| `05_Technical_Architecture/` | Multi-tenant architecture |
| `06_Database_Design/` | Tenant-scoped schema and relationships |
| `07_API_Collections/` | Tenant context headers and endpoint behavior |
| `08_Integration_Contracts/` | Tenant-aware integration behavior |
| `09_UI_UX_Design/` | Navigation and access context |
| `10_Backend_Engineering/` | Tenant context enforcement |

---

# 8. Ownership

| Concern | Owner |
|---|---|
| Hierarchy definition | Product / Architecture Governance |
| Tenant enforcement | Backend Engineering / Database / API |
| UI representation | UI/UX Design |
| Future hierarchy changes | Product / Architecture Governance |

---

# 9. Review and Freeze Rule

This decision shall remain `Design Draft` until hierarchy usage is verified across Product Foundation, Technical Architecture, Database Design, API Collections, Integration Contracts, UI/UX, and Backend Engineering.

Once frozen, hierarchy changes shall be captured through a superseding decision record.
