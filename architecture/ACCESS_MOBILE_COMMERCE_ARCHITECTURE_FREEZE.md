# Access / Mobile / Commerce Architecture Freeze

**Status:** FROZEN  
**Date:** 13 September 2026  
**Revision:** 2 — Manager role reverted; Site Admin is authoritative  
**Scope:** Documentation-only architecture freeze. This document does **not** implement APIs, schema, Flutter, authentication, or API-05.

This is the **authoritative** access-model, Phase-1 application-persona, commercial-boundary, and account-lifecycle direction for Digitize by OreeOn.

Where older product, functional, or API-collection prose disagrees (including the **temporary Manager role** in revision 1 of this freeze / DR-019 v1.0), **this freeze wins**.

Historical documents remain for traceability. They are not rewritten in bulk. Implementers follow this freeze for role names, personas, and commerce boundaries.

**Does not change**

- Official API inventory = **228**
- API-01 through API-14 collection structure
- Authentication freeze / live `/api/v1/auth/*`
- API-02 implementation
- API-09 implementation
- Semantic runtime `operation_id`; `catalog_id` is product metadata only
- Platform → Organization → Facility → Site hierarchy
- Nested organization/facility HTTP routes (not reopened)
- Operation ID migration (**CLOSED / FROZEN** — not reopened)

**Related documents**

- Product Glossary (`docs/01_Product_Foundation/PF-01_Product_Glossary.md`)
- Tenant hierarchy: `docs/99_Decision_Records/DR-004_Platform_Tenant_Hierarchy.md`
- Decision record: `docs/99_Decision_Records/DR-019_Access_Mobile_Commerce_Architecture.md`
- Store compliance audit: `docs/architecture/MOBILE_STORE_PLATFORM_COMPLIANCE_AUDIT.md`
- API-03 identity: organization-scoped staff HTTP; Platform Admin accounts are not provisioned by API-03
- API-04 customer: Customer ≠ UserAccount; Customer ≠ Participant
- API-09: Organization SaaS subscription/license

---

## 1. Authoritative hierarchy

```text
Platform
  └── Organization
       └── Facility
            └── Site
```

Do **not** introduce Branch between Organization and Facility, Site between Organization and Facility, or any alternative hierarchy.

---

## 2. Authoritative role model

The authoritative roles are:

1. **Platform Admin**
2. **Organization Admin**
3. **Site Admin**
4. **Staff**

There is **NO Manager role**.

This corrects revision 1 of this freeze and DR-019 v1.0, which temporarily used Manager instead of Site Admin.

Do **not** introduce another operational administrative role.

Role administration chain (not a tenant hierarchy):

```text
Organization Admin → Site Admin → Staff
```

Never:

```text
Organization Admin → Manager → Staff
```

### 2.1 Platform Admin

Platform Admin has **platform-wide administrative access through the separate Platform Admin application**.

Platform Admin can, according to **platform permissions**:

- create and manage Organizations
- view and manage Facilities
- view and manage Sites
- view and administer Organization users
- view and administer Organization Admins
- view and administer Site Admins
- view and administer Staff across organizations
- manage subscriptions and licenses (Digitize SaaS)
- access platform-wide administrative and operational data
- suspend, revoke, deactivate, or otherwise administer users where platform administration requires it

**Binding distinction:**

> Platform Admin has platform-wide administrative authority.

Platform Admin is **not** restricted to the Organization Admin’s normal business-level workflow.

**Do NOT** document that Platform Admin cannot manage Organization users, Staff, Site Admins, or Organization Admins (subject to platform permissions).

**HTTP / inventory notes (unchanged implementation):**

- API-03 remains **organization-scoped staff identity** HTTP. It does **not** provision `PLATFORM_ADMIN` accounts (CLI bootstrap remains).
- API-01 remains platform settings/master data/health — not the full Platform Admin product surface.
- Platform-wide user administration is a **Platform Admin application** capability constrained by platform permissions; it is not a new numbered vertical in this freeze.

Platform Admin is **not** a Phase-1 operational mobile persona (see §3).

### 2.2 Organization Admin

Organization Admin is the **organization-level business administrator**.

Organization Admin:

- manages the Organization
- creates/configures Facilities
- assigns Facility → Site
- enters facility metadata
- manages the Organization’s Digitize SaaS subscription
- creates Site Admins
- assigns Site Admin access
- creates Staff
- assigns Staff access
- can suspend/revoke Site Admin and Staff access **within the Organization**
- manages the organization’s operational environment

Organization Admin is the normal business-level owner of the organization’s user and operational structure.

Organization Admin **cannot** manage Platform Admin accounts.

### 2.3 Site Admin

Site Admin is the **site-level operational administrator**.

Site Admin:

- operates within **assigned Site scope**
- manages/oversees the operational activities of the assigned Site
- has access according to Site-level permissions
- can perform the operational administration assigned to the Site Admin role
- works with Staff assigned to the Site
- must **not** automatically receive platform-wide or organization-wide authority

Existing Site-scoped permission language in FR-06, API collections, and the access matrix (for example `staff.directory.site-view`, site-scoped dashboards and reports) is **preserved** as the Site Admin permission model. This freeze does **not** invent extra Site Admin capabilities.

Site Admin is **not** a tenant level. Scope is assignment-driven under Platform → Organization → Facility → Site.

### 2.4 Staff

Staff is an **operational role**.

Staff:

- operates within assigned Site/facility scope
- receives access through assigned permissions
- performs operational tasks assigned to the role
- does not have Organization Admin or Platform Admin authority

### 2.5 Manager — not a role

**Manager is NOT a role.**  
**Manager is NOT a Phase-1 persona.**  
**Manager is NOT part of RBAC.**  
**Manager is NOT part of the access hierarchy.**  
**Manager must NOT be introduced into API contracts, API-05, or the architecture gate.**

The previously temporary Manager role is **reverted to Site Admin**.

Unrelated uses of “manager” (Release Manager, Product Manager, Secrets Manager, Campaign Manager as a job function in campaign docs) are **not** this role.

Historical **Facility Manager** labels in FR, UX, and API collections are **not** a fifth RBAC role. They are older BA operational titles. For architecture, facility-wide operational administration is either Organization Admin, Site Admin assigned across the relevant sites, or Staff with facility-scoped permissions — not a Manager role.

---

## 3. Application / persona boundary (Phase 1)

| Persona | Phase-1 operational application | Application |
| --- | --- | --- |
| Organization Admin | Yes | Operational application |
| Site Admin | Yes | Operational application |
| Staff | Yes | Operational application |
| Platform Admin | **No** | **Separate Platform Admin application** |
| Customer | **No** | Customer mobile is **Phase 2** |
| Participant | Not an app persona | Domain concept (see §3.1) |
| Guardian | Not a Phase-1 app persona | Future-ready relationship; detailed UX deferred |

### 3.1 Customer vs Participant

**Customer** and **Participant** are **separate domain concepts**.

Do **not** equate:

```text
Customer = Participant
```

- **Customer** is the facility commercial/service account holder (memberships, walk-in, training, classes) — API-04 / future API-05–08.
- **Participant** is who attends or takes part in an activity. A participant may be the Customer, a related person, or (in future) a minor under a Guardian Relationship.
- Customer records are **not** `identity.user_account` logins in Phase 1. Customer-as-app-user remains Phase 2.

### 3.2 Guardian / minor

Preserve the **future-ready** concept of **Guardian Relationship**.

Detailed guardian/minor UX remains **deferred**. Do not implement guardian/minor functionality in this documentation gate. Do not design API-05 as if the operational app were a children’s consumer product.

---

## 4. Commercial boundary

### Digitize SaaS commerce

```text
Organization → Digitize/OreeOn
```

This is the organization’s Digitize SaaS subscription/license (API-09). Organization Admin manages it at the organization level. Platform Admin may administer subscriptions/licenses according to platform permissions.

**Do not** introduce staff-mobile SaaS subscription purchasing (no in-app Digitize license checkout in the operational application).

Staff may participate in **facility** payment/collection workflows where already defined. That is **not** purchasing the organization’s Digitize SaaS subscription.

### Facility commerce

```text
Customer → Facility
```

This covers:

- memberships
- single-entry purchases
- training / personal training
- classes
- other facility services

**Do not** combine Digitize SaaS billing with facility customer commerce.

API-05 Membership Plan (next gate) must implement **facility commerce** only. Physical recreation fees (including gym-style memberships) use **non-store** payment channels when implemented. Digitize SaaS checkout stays off the operational mobile app.

---

## 5. Account lifecycle direction (document only)

Canonical lifecycle states:

- **Active**
- **Suspended**
- **Deactivated**
- **Deletion Requested**
- **Deleted / Anonymized**

**Binding:** Removing access, suspending a user, or revoking a user’s Organization/Site assignment is **not** equivalent to account deletion.

Account deletion/anonymization remains an **explicit future implementation requirement**. **Do not implement deletion in this documentation gate.**

Existing operator deactivate / customer archive remain **access and operational** controls, not store-grade deletion.

---

## 6. What this freeze does not reopen

Unchanged:

- 228 operations; API-01 … API-14
- Semantic `operation_id` runtime; numbered `catalog_id` metadata
- Auth contract; API-02; API-09
- Platform → Organization → Facility → Site
- No nested org/facility route invention unless already approved
- No Customer = Participant merge
- No staff-mobile SaaS IAP / SaaS checkout

---

## 7. Constraints API-05 must respect

When Membership Plan **contract review** starts (implementation is **not** this gate):

1. Treat API-05 as **Customer → Facility** commerce, not Organization → Digitize SaaS.
2. Do not add customer mobile login or customer self-checkout as Phase-1 operational-app requirements.
3. Do **not** introduce a Manager role. Site Admin remains the site-level operational administrator.
4. Do not treat Customer rows as Participants by default.
5. Do not implement account deletion as part of API-05.
6. Do not mix license/subscription (API-09) payloads or Play/App Store digital-goods checkout into membership plans.
7. Do not expand the 228 inventory or reopen operation IDs unless a separately approved inventory change exists.

---

## 8. Historical contradictions (superseded)

| Older statement | Superseding rule |
| --- | --- |
| Temporary freeze: Manager is a role; no Site Admin | **Site Admin is a role. Manager is not a role.** |
| Org Admin → Manager → Staff | **Organization Admin → Site Admin → Staff** |
| Org Admin creates Managers | Org Admin creates **Site Admins** and Staff |
| Platform Admin cannot manage organization users / Staff / Site Admins | Platform Admin **can**, via platform permissions and the Platform Admin application |
| Platform Admin cannot manage org users because API-03 excludes PLATFORM_ADMIN | API-03 still does not **provision** Platform Admins; that is not a ban on platform-wide administration |
| Mobile persona undecided | Phase-1 operational app = Org Admin, Site Admin, Staff; Customer app = Phase 2; Platform Admin = separate app |
| Customer = Participant | Separate concepts |
| SaaS billed in staff mobile | Forbidden; SaaS is Organization → Digitize/OreeOn |
| Historical FR “Facility Manager” as a fifth RBAC role | Not an authoritative role; see §2.5 |

FR-06, BA-05, UX-05, and API collection “Facility Manager” / “Site Administrator” rows remain **historical labels**. Implementers follow this freeze for architecture. Site-scoped FR permissions map to **Site Admin**. Operational FR permissions map to **Staff**.

---

## 9. Deferred implementation (architecture known, not built here)

- Account deletion / anonymization APIs, in-app + web deletion UX
- Platform Admin application product (beyond CLI bootstrap + existing platform APIs)
- Customer mobile application (Phase 2)
- Guardian/minor detailed UX
- Facility payment processor / API-08 live checkout
- Staff-mobile SaaS purchasing (permanently out of the Phase-1 operational app)
- Legal retention durations, privacy policy copy, store IDs, reviewer demo (store program; see compliance audit)
- API-05 **implementation** (next gate is **contract review only**)

---

## 10. Frozen vs deferred vs store blockers

### Frozen decisions (authoritative now)

Hierarchy, four roles, Platform Admin platform-wide access, Phase-1 operational personas, Customer mobile Phase 2, Customer ≠ Participant, Guardian future-ready, SaaS vs facility commerce, account-lifecycle **direction**, 228 inventory, semantic `operation_id`.

### Deferred implementation

Deletion/anonymization, Platform Admin product UI, customer mobile, guardian UX, live facility checkout, privacy-policy copy, store listing.

### Store-submission blockers (unchanged by this freeze)

In-app + web account deletion, privacy policy, production app IDs/signing, reviewer demo, Data Safety / App Privacy forms.

### API-05 constraints

Section 7. Membership Plan is **facility commerce** under Site/Staff operational use of the Phase-1 app. Not SaaS billing. Not customer mobile. Not Manager.

---

## 11. Gate

```text
ACCESS / MOBILE / COMMERCE ARCHITECTURE GATE

Status: FROZEN

Hierarchy:
Platform → Organization → Facility → Site

Authoritative roles:
Platform Admin
Organization Admin
Site Admin
Staff

Platform Admin:
Platform-wide administrative access through the separate Platform Admin application.

Organization Admin:
Organization-level business administration, including Facility, Site, Site Admin, and Staff administration within the Organization.

Site Admin:
Site-level operational administration within assigned Site scope.

Staff:
Operational access within assigned permissions and Site/facility scope.

Manager:
Not a role. The previously temporary Manager role has been reverted to Site Admin.

Operational application personas:
Organization Admin, Site Admin, Staff.

Platform Admin application:
Separate Platform Admin application.

Customer mobile:
Deferred to Phase 2.

Customer vs Participant:
Separate domain concepts.

Guardian/minor:
Future-ready; detailed UX deferred.

SaaS billing:
Organization → Digitize/OreeOn.

Facility commerce:
Customer → Facility.

Account deletion:
Required architecture capability; implementation deferred.

API inventory:
228 — unchanged.

Operation ID architecture:
Frozen; semantic runtime operation_id remains authoritative.

Next gate:
API-05 Membership Plan contract review.
```
