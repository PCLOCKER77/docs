# DR-022 Transition Note (from DR-021)

**Status:** Planning input only — **do not implement DR-022 under this note.**  
**Source freeze:** DR-021 (Implementation Complete / Browser Verification Pending)  
**Date:** 2026-09-22  

DR-022 will cover **Customer Data Protection + Customer Module**. **This ID is reserved** and must not be assigned to another decision (including hierarchy). The Company → Branch/Site → Facility proposal is **DR-023**.

DR-022 must **reuse** the following already-landed Digitize components. Do not redesign Authentication, Organization lifecycle, API numbering, or the PA boundary frozen by DR-021.

---

## Reusable components for DR-022

| Capability | Where to consume |
| --- | --- |
| Organization DEK infrastructure | `app/modules/tenant_crypto/` (`OrganizationDekService`, wrapped DEK table `security.organization_data_encryption_key`, migration 022) |
| Envelope wrap / unwrap helpers | `app/core/tenant_crypto.py` (`wrap_organization_dek`, `unwrap_organization_dek`, `encrypt_sensitive_bytes`, `decrypt_sensitive_bytes`) |
| Cryptographic authorization boundary | `assert_tenant_crypto_access` — PA cannot obtain/unseal Organization DEKs |
| Data classification | `app/core/data_classification.py` (`NORMAL` / `SENSITIVE` / `HIGHLY_SENSITIVE`; health = HIGHLY_SENSITIVE) |
| Blind-index capability | `blind_index` in `app/core/tenant_crypto.py` (HMAC keyed exact-search helper; not yet wired to Customer columns) |
| Audit + UoW | `record_audit_event` in same session/transaction; commit-then-email outbox pattern |
| Tenant authorization / isolation | `app/core/access.py` + org membership + RBAC permissions |
| PENDING / ACTIVE lifecycle gate | `app/core/organization_lifecycle.py` (`require_operational_organization`) — Customers already require ACTIVE org |
| PA tenant-data denial | `CustomerService` denies Platform Admin plaintext customer list/create/object access |
| Existing Customer API contracts | Numbered API-04 inventory remains inside the **228**; no renumber; no duplicate Auth IDs |
| Tenant-mutation governance (if PA ever mutates tenant customer data) | `app/modules/tenant_mutation/` + `tenant_mutation_policy` — no impersonation |

---

## Explicit non-goals for the transition

- Do not reopen DR-021 onboarding lifecycle.
- Do not implement Customer column encryption in this note’s delivery.
- Do not add PA bypass endpoints for verification.
- Do not change the official numbered product API count (**228**).
