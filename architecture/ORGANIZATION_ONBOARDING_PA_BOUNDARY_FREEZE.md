# Organization Onboarding and Platform Admin Boundary Freeze

**Status:** Accepted  
**Decision record:** DR-021  
**Last updated:** 2026-09-22  

This freeze is normative for Organization onboarding lifecycle, Platform Admin security boundary, data classification, and tenant cryptographic isolation foundations. It does **not** redesign Authentication, RBAC roles, product hierarchy, or the 228 numbered product APIs.

---

## 1. Platform Admin principle

> Platform Admin controls the Digitize platform; Organization Admin controls the Organization's business.

| PA may | PA must not |
| --- | --- |
| Create/archive/restore Organizations; manage structural metadata | Impersonate Organization Admin |
| Provision initial OA; resend onboarding credentials | Decrypt tenant business data |
| Approve/reject **initial** onboarding changes only | Obtain Organization DEKs |
| Manage platform metadata, subscriptions, platform identity | Bypass tenant crypto or data permissions |
| View aggregate platform dashboards/reports/audit | Access plaintext customer/health/documents |

Once an Organization is **ACTIVE**, normal OA changes do **not** require PA approval.

---

## 2. Frozen onboarding lifecycle

1. PA creates Organization → `business_status = PENDING` (no dedicated onboarding DB column).
2. Create form provisions initial OA: Admin Full Name (required), Admin Email (required), Admin Phone (optional). PA never enters an OA password.
3. System issues Organization Admin credentials via existing EmailService/outbox according to environment policy:
   - **Local / Development:** temporary password (Mailpit/SMTP); `password_must_change` applies on first login.
   - **QA / Production:** secure single-use, short-lived credential setup link; OA establishes permanent password; temporary passwords are never emailed.
4. OA completes credential setup (temp-password change or setup-link) → reviews Organization → accepts Terms & Conditions (auditable).
5. **No initial changes** after review → Organization becomes **ACTIVE** automatically.
6. **Initial changes** submitted → remains **PENDING** → PA reviews → approve (`organizations_activate` / API-02-005) or reject → OA corrects/resubmits.
7. While PENDING, backend blocks operational tenant resources (Facilities, Sites, Membership Plans, Customers, operational Staff management, etc.).
8. After ACTIVE, OA owns normal tenant administration without PA approval for ordinary changes.

UI-only: "Same as Organization Email" checkbox. Do **not** persist `admin_email_same_as_organization_email`. Organization Email and OA login email remain separate persisted values.

### Credential provisioning policy

Backend `CredentialProvisioningPolicy` is authoritative:

| Environment | Mode |
| --- | --- |
| development / local / test | Temporary password |
| qa / staging | Setup link (`/auth/setup-credentials?token=…`) |
| production | Setup link (same architecture as QA) |

Setup tokens reuse `identity.password_reset_request` (hashed at rest, single-use, TTL = `AUTH_RECOVERY_TTL_SECONDS`). Reissue invalidates prior open tokens. Raw tokens appear only in the outbound email URL and are never logged, audited, or returned in API responses.


---

## 3. Roles (unchanged)

`PLATFORM_ADMIN` · `ORGANIZATION_ADMIN` · `SITE_ADMINISTRATOR` · `STAFF`  
Do not introduce MANAGER as an RBAC role. Site Admin remains the authoritative site-level role name.

---

## 4. Data classification

Reusable model: `NORMAL` | `SENSITIVE` | `HIGHLY_SENSITIVE`.

| Domain | Classification |
| --- | --- |
| Platform metadata / catalogs | NORMAL |
| Organization structural metadata | NORMAL to SENSITIVE by field |
| Organization registration / documents | SENSITIVE |
| Customer identity/PII, membership, attendance, payments, staff | SENSITIVE |
| Customer health data / health documents | **HIGHLY_SENSITIVE** |
| Authentication secrets | HASHED / secret handling (not field encryption) |

Encrypt based on classification and query needs. Exact search over encrypted sensitive values uses keyed blind index / HMAC — not full-dataset decrypt.

---

## 5. Tenant cryptographic isolation

```text
KMS/HSM → platform/root KEK → Organization DEK → encrypted tenant data + protected key metadata
```

- Distinct DEK domain per Organization.
- Raw DEKs never stored plaintext in PostgreSQL.
- Application decrypts only after successful tenant authorization.
- PA platform authority ≠ cryptographic authorization.
- Protection extends to backups, object storage, exports, temp files; logs/audit must not contain sensitive plaintext.

---

## 6. API impact

| Surface | Rule |
| --- | --- |
| Numbered product APIs | Remain **228**; do not renumber |
| API-02-001 create | Extended: OA provisioning without PA password |
| API-02-002 update | OA may submit initial changes while PENDING |
| API-02-005 activate | PA approval path for initial-change review (and compatible PA activate) |
| ORG-ONBOARDING-ACCEPT / ORG-ONBOARDING-REJECT | Unnumbered extras |
| ORG-ARCHIVE / ORG-RESTORE | Unnumbered extras (unchanged) |
| Authentication APIs | Frozen; do not duplicate |

---

## 7. Administrative delegation

Any future PA mutation of tenant business data requires the existing tenant-mutation authorization foundation (requesting PA identity, Organization, resource, operation, scope, approval, expiration, replay protection, audit). Emergency override must preserve PA identity and must not grant DEK access merely from platform authority.
