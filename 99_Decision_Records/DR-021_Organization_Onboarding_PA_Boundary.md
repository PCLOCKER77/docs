# DR-021 Organization Onboarding Lifecycle and Platform Admin Security Boundary

> Freezes the Organization onboarding lifecycle and the Platform Admin / Organization Admin security boundary without redesigning Authentication, RBAC roles, hierarchy, or the 228 numbered product API catalog.

---

# Document Control

| Field | Value |
| --- | --- |
| Document ID | DR-021 |
| Document Name | Organization Onboarding Lifecycle and Platform Admin Security Boundary |
| Folder | 99_Decision_Records |
| Product | Digitize by OreeOn Technologies Pvt. Ltd. |
| Status | Implementation Complete / Browser Verification Pending |
| Owner | Architecture / Product |
| Reviewers | Architecture, Product, Backend, Identity, Security |
| Version | 1.1 |
| Last Updated | 2026-09-22 |
| Clarifies | DR-004 (hierarchy unchanged); DR-019 (PA ≠ tenant-data superuser); AUTH freeze (AuthN/AuthZ unchanged) |
| Supersedes | Prior FR-ORG-007 assumption that Platform Admin always manually activates every Organization after readiness |
| Closure | See §5 Implementation Closure |

---

# 1. Decision Summary

## 1.1 Platform Admin principle

**Platform Admin controls the Digitize platform; Organization Admin controls the Organization's business.**

PLATFORM_ADMIN is the platform-control and governance authority. PLATFORM_ADMIN is **not** a universal tenant-data superuser.

PLATFORM_ADMIN must not:

- Impersonate Organization Admin
- Use a generic "view as Organization" bypass
- Decrypt tenant business data
- Obtain Organization Data Encryption Keys (DEKs)
- Bypass Organization-level data permissions or tenant cryptographic authorization

## 1.2 Organization onboarding lifecycle

```text
PA creates Organization (business_status = PENDING)
  → provisions initial Organization Admin (no PA-entered password)
  → credentials emailed via existing EmailService/outbox:
       Local/Development: temporary password (Mailpit)
       QA/Production: secure single-use setup link (OA chooses password)
  → OA completes credential setup / first password change
  → OA reviews Organization details and accepts Terms & Conditions

If OA accepts with no initial changes:
  → Organization becomes ACTIVE automatically

If OA changes initial Organization details:
  → Organization remains PENDING
  → PA reviews and approves (API-02-005 activate) or rejects
  → OA may correct and resubmit while PENDING

Once ACTIVE:
  → Normal OA changes do NOT require PA approval
  → OA owns Facilities, Sites, operational configuration, and tenant data (subject to permissions)
```

Do **not** add an `onboarding` database column merely for UI state. Flutter may derive `status = pending` and `onboarding = draft | awaiting_review | complete` from `business_status` plus onboarding metadata.

## 1.3 PENDING capability gate

While `business_status = PENDING`, backend authorization allows only explicitly required onboarding operations and blocks operational tenant resources (Facilities, Sites, Membership Plans, Customers, operational Staff management, and similar).

Enforcement is backend-authoritative. Flutter guards are not a security boundary.

## 1.4 Tenant cryptographic isolation

PostgreSQL disk encryption alone is not sufficient. Digitize uses application-level envelope encryption per Organization DEK. PA authorization does not imply cryptographic authorization.

## 1.5 Data classification

Reusable classification: `NORMAL`, `SENSITIVE`, `HIGHLY_SENSITIVE`. Customer health data and health documents are `HIGHLY_SENSITIVE` unless a documented exception exists. Passwords remain hashed, not encrypted.

## 1.6 API catalog

Official numbered product API count remains **228**. Onboarding accept/reject and archive/restore remain **extras** (unnumbered). Do not renumber or duplicate Auth/Organization numbered APIs.

---

# 2. Context

FR-03 previously assumed Platform Admin activates every Organization after a readiness checklist. Implementation already created Organizations as `PENDING` and optionally provisioned an Organization Admin, but activation remained PA-only and UI did not capture OA details or T&C.

This record freezes the OA-driven initial activation path and the PA tenant-data boundary so documentation, backend, and Flutter converge without redesigning Authentication or RBAC.

---

# 3. Consequences

- FR-ORG-001 / FR-ORG-007, BA-02/BA-04/BA-06, PF-01 Platform Admin example, and API-02 activate semantics must describe the conditional activation path.
- Organization Create captures Admin Full Name, Admin Email, optional Admin Phone. "Same as Organization Email" is UI-only and is not persisted.
- Temporary credentials (local/dev) and setup-link credentials (QA/production) reuse existing identity/email outbox and `PasswordResetRequest` infrastructure; plaintext passwords and raw tokens are never returned in API responses.
- Terms & Conditions acceptance is auditable (`terms_version`, `accepted_at`, `accepted_by`, Organization).
- Onboarding T&C master data is Platform Admin–managed in `platform.terms_document` (extras ORG-TERMS-001…006). Acceptance still binds to the **current published** version + content hash. Mandatory reacceptance for existing organizations is **deferred** and must not be invented under DR-021. SaaS commercial terms remain a separate domain.
- Tenant-mutation governance remains the path for any future PA mutation of tenant business data; no impersonation.
- Customer / Membership API implementation remains out of scope for this decision's delivery slice.

---

# 4. Traceability

- Freeze companion: `docs/architecture/ORGANIZATION_ONBOARDING_PA_BOUNDARY_FREEZE.md`
- Access boundary: DR-019 + `ACCESS_MOBILE_COMMERCE_ARCHITECTURE_FREEZE.md`
- Auth contract: `AUTH_CONTRACT_FREEZE.md`
- API inventory: `API_CONTRACT_REGISTRY.md` (228)
- FR module: `FR-03_Organization_Management.md`

---

# 5. Implementation Closure (2026-09-22)

**Decision status:** `IMPLEMENTATION COMPLETE / VERIFICATION PENDING`

**Credential provisioning amendment (DR-021):** Organization Admin credentials are environment-policy driven — local temporary password via Mailpit; QA/Production secure setup link. Do not reopen Auth architecture.

**Verification (2026-09-22):** Fresh SMTP→Mailpit with amended template **PASS**; QA/Production setup-link + token security **PASS** (controlled/memory); API catalog **228**; targeted backend/auth tests **PASS**; full backend suite **PASS WITH PRE-EXISTING FAILURES** (same 3). Flutter auth/setup tests **PASS**; full `flutter test` has 1 pre-existing UI revamp failure unrelated to credentials. **Browser click-through NOT VERIFIED** (no browser automation in this environment).

**Do not reopen DR-021 design.** Authentication, hierarchy, API catalog numbering, and the frozen onboarding lifecycle remain closed.

## 5.1 Verification evidence (non-browser)

| Check | Result |
| --- | --- |
| Code inspection of create / OA provision / PENDING / T&C / auto-ACTIVE / PA approve / PENDING gate / PA customer denial / DEK gate / 228 catalog | Confirmed in current tree |
| Automated suite (onboarding foundation, live onboarding, OA provisioning, archive/restore, contract registry, auth API) | **59 passed** |
| Live HTTP Path A (no-change → ACTIVE) + Mailpit temp credential | **PASS** |
| Live HTTP Path B (OA change → PENDING → PA activate → ACTIVE) | **PASS** |
| Live HTTP Path C (Facility create while PENDING → 409 for OA and PA) | **PASS** |
| Live HTTP Path D (PA `GET /customers` → 403; no plaintext) | **PASS** |
| ACTIVE OA normal profile update without PA approval | **PASS** |
| PA `assert_tenant_crypto_access` denial | **PASS** |
| `NUMBERED_COUNT` / `NUMBERED_OPERATIONS` length | **228** |
| Browser click-through | **NOT AVAILABLE** (`BROWSER_VERIFICATION = NOT AVAILABLE`) |

## 5.2 Remaining gaps (documented; out of DR-021 reopen)

1. Browser click-through not performed in this environment (no browser automation tooling).
2. OA password-change still requires re-login before onboarding review UX (existing Auth behavior).
3. Full field-level encryption of Customer/SENSITIVE columns is **not** implemented; DEK wrap + helpers are foundation only.
4. Stale “Draft” wording remains in non-authoritative spots (e.g. BA-04 later steps; DB migration review CK note). Authoritative status vocabulary is **Pending**.
5. Full Platform Admin dashboard / aggregate capability surfaces remain future work.

## 5.3 Next record

DR-022 (Customer Data Protection + Customer Module) consumes the reusable foundations listed in `docs/architecture/DR-022_TRANSITION_FROM_DR-021.md`. **Do not begin DR-022 implementation under DR-021.**
