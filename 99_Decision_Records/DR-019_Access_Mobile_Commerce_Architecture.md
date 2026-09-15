# DR-019 Access, Mobile Persona, and Commerce Architecture

> Authoritative freeze of Platform Admin vs Organization Admin access, Phase-1 mobile personas, SaaS vs facility commerce, and account-lifecycle direction.

---

# Document Control

| Field | Value |
| --- | --- |
| Document ID | DR-019 |
| Document Name | Access, Mobile Persona, and Commerce Architecture |
| Folder | 99_Decision_Records |
| Product | Digitize by OreeOn Technologies Pvt. Ltd. |
| Status | Accepted |
| Owner | Architecture / Product |
| Reviewers | Architecture, Product, Backend, Identity |
| Version | 2.0 |
| Last Updated | 2026-09-13 |
| Supersedes | DR-019 v1.0 (temporary Manager role; “no Site Admin”); store-audit “persona undecided” / mixed commerce ambiguity |
| Clarifies | DR-004 (hierarchy unchanged); API-03 (no Platform Admin HTTP provisioning); API-04 (Customer ≠ UserAccount; Customer ≠ Participant) |

---

# 1. Decision Summary

- Platform Admin has **platform-wide** administrative access, including Organizations, Facilities, Sites, Organization users, Organization Admins, Site Admins, and Staff, through the **Platform Admin application**, according to platform permissions.
- Organization Admin is the normal organization-level business administrator of Facilities, Sites, Site Admins, and Staff.
- **Site Admin** is the site-level operational administrator within assigned Site scope.
- There is **no Manager role**. DR-019 v1.0 is reverted on that point.
- Phase-1 operational application personas: Organization Admin, Site Admin, Staff. Platform Admin uses a separate application. Customer mobile is Phase 2.
- Customer and Participant remain separate domain concepts.
- SaaS commerce is Organization → Digitize/OreeOn. Facility commerce is Customer → Facility. Do not mix. No staff-mobile SaaS purchasing.
- Account lifecycle includes Active, Suspended, Deactivated, Deletion Requested, Deleted/Anonymized. Suspend/revoke ≠ deletion. Deletion implementation is deferred.
- API inventory remains 228. API-05 is the next **contract review** gate, not implementation in this record.

Normative detail: `docs/architecture/ACCESS_MOBILE_COMMERCE_ARCHITECTURE_FREEZE.md`.

---

# 2. Context

The mobile store compliance audit recorded persona and billing-channel product decisions as unresolved. DR-019 v1.0 temporarily replaced Site Admin with Manager. Product has reverted that: Site Admin is first-class; Manager is not a role. This record freezes the reconciled model without changing runtime code.

API-03 still does not provision `PLATFORM_ADMIN` accounts over HTTP. That constraint is **not** a statement that Platform Admin cannot administer organization users.

---

# 3. Consequences

- API-05 must not assume customer mobile, a Manager role, or mixed SaaS/facility checkout.
- Historical FR/BA/API-collection “Facility Manager” labels are not a fifth RBAC role; site-scoped FR permissions map to Site Admin.
- Store submission remains blocked on deletion/privacy implementation; those are deferred, not cancelled.

---

# 4. Traceability

- Freeze: `docs/architecture/ACCESS_MOBILE_COMMERCE_ARCHITECTURE_FREEZE.md`
- Audit: `docs/architecture/MOBILE_STORE_PLATFORM_COMPLIANCE_AUDIT.md`
- Glossary §8: `docs/01_Product_Foundation/PF-01_Product_Glossary.md`
- Hierarchy: DR-004
