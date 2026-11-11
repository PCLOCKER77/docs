# Repository-Wide Naming Audit

**Status:** Applied  
**Date:** 2026-09-12  
**Scope:** Digitize backend (`digitize-services`, `database/`, `docs/architecture`)  
**Constraint:** Symbol/naming refactor only. Frozen API contracts, permission
code strings, error codes, audit event names, API paths, operation IDs, and
migration history are unchanged.

This audit classifies identifiers by **what they represent**, not by which API
collection, ticket, or migration introduced them.

---

## A. Naming Principles

1. Name a code symbol according to its semantic responsibility.
2. Keep these identities distinct. Do not conflate them.

```text
API inventory identity        API-01, API-02, API-02-007
OpenAPI operation identity    organizations_create, facilities_create
Authorization identity        organization.create, facility.activate
Application/domain identity   OrganizationService, FacilityRepository
Error identity                AUTHENTICATION_FAILED, RESOURCE_NOT_FOUND
Audit/event identity          organization.created, facility.activated
Database identity             tenant.organization, identity.permission
Implementation/migration      010_api01_platform_admin, 011_api02_org_facility_site
```

3. API collection numbers may appear in inventory metadata, contract tests,
   registry documents, and historical migrations. They must not name
   permissions, services, schemas, authorization loaders, or domain events.
4. Prefer the smallest number of canonical registries. Do not create one
   permission registry per API number.
5. Do not leave obsolete aliases in active code.
6. Do not rewrite migration history to improve naming.
7. Do not perform cosmetic renames when the existing name is already semantic
   (`OrganizationService`, `FacilityCreate`, `require_permission`).

---

## B. Keep As-Is

| Identifier | Why it stays |
| --- | --- |
| `API-01`, `API-02`, `API-01-001` … `API-02-014` | Frozen API inventory IDs |
| OpenAPI `operationId` values (`organizations_create`, …) | Frozen API contract |
| `/api/v1/organizations`, `/api/v1/facilities`, `/api/v1/sites`, `/api/v1/platform/*` | Frozen API paths |
| Permission **values** (`organization.create`, `platform.settings.view`, …) | Frozen authorization contract |
| Error **values** in `app/api/error_codes.py` | Frozen error identity |
| Audit event **values** (`organization.created`, `facility.activated`, …) | Frozen event identity |
| Alembic revision IDs `010_api01_platform_admin`, `011_api02_org_facility_site` | Migration history |
| Files `010_api01_platform_administration.py`, `011_api02_organization_facility_site.py` | Migration history |
| SQL twins `010_seed_api01_platform_administration.sql`, `011_seed_api02_organization_facility_site.sql` | Migration history |
| `_API01_PERMISSION_CODES` / `_API02_PERMISSION_CODES` **inside Alembic files** | Historical migration locals |
| `COLLECTION_META`, `NUMBERED_OPERATIONS`, `NUMBERED_COUNT`, `IMPLEMENTED_NUMBERED_KEYS` | API inventory metadata |
| `API01_PATHS`, `API02_PATHS` in live contract tests | Explicit API-inventory path fixtures |
| `test_api01_requires_authentication` and siblings | Explicit API-01 contract tests |
| `test_011_organization_facility_site_migration.py`, `test_010_platform_administration_migration.py` | Tests of frozen migration identity |
| `OrganizationService`, `FacilityService`, `OrganizationRepository`, `FacilityRepository`, `SiteRepository` | Already semantic |
| `OrganizationCreate`, `FacilityUpdate`, `SiteActivate`, … | Already semantic |
| `Principal`, `require_permission`, `load_authorized_principal`, `load_platform_principal` | Already semantic |
| `PLATFORM_ADMIN_PERMISSION_CODE = "PLATFORM_ADMIN_MANAGE_SETTINGS"` | Legacy bootstrap permission from migration 008; database identity |
| `_assert_api00_error`, `test_success_envelope_has_api_00_fields` | API-00 envelope contract tests |
| Route modules `organization/routes.py`, `facility/routes.py`, `platform/routes.py` | Domain-oriented module layout already |

---

## C. Rename

### C.1 `API01_PERMISSION_CODES` → `PLATFORM_PERMISSION_CODES`

```text
Current:   API01_PERMISSION_CODES
Canonical: PLATFORM_PERMISSION_CODES
Reason:    The tuple is the platform authorization registry (platform.* codes).
           It is not API inventory metadata.
Category:  Authorization
Files:     app/modules/identity/constants.py
           tests/api/platform_auth.py
```

### C.2 `API02_PERMISSION_CODES` → domain permission registries

```text
Current:   API02_PERMISSION_CODES
Canonical: ORGANIZATION_PERMISSION_CODES
           FACILITY_PERMISSION_CODES
           SITE_PERMISSION_CODES
Reason:    The tuple mixed three authorization domains only because they were
           implemented in one API collection. Permissions are not API artifacts.
Category:  Authorization
Files:     app/modules/identity/constants.py
           tests/api/platform_auth.py
           tests/api/test_organization_facility_site.py
           tests/migrations/test_011_organization_facility_site_migration.py
```

### C.3 `API01_AUTHORIZATION` + `API02_AUTHORIZATION` → `OPERATION_AUTHORIZATION`

```text
Current:   API01_AUTHORIZATION, API02_AUTHORIZATION
Canonical: OPERATION_AUTHORIZATION
Reason:    Both maps are API-inventory → permission lookups. Splitting them by
           collection number created one registry per API number. One catalog
           map keyed by frozen API IDs is the correct inventory metadata.
Category:  API inventory metadata
Files:     app/api/contracts/catalog.py
           docs/architecture/API_01_PLATFORM_ADMIN_PREIMPLEMENTATION.md
```

Keys remain `API-01-001` … `API-02-014`. Values remain the same permission
strings. This is not a permission registry; it is contract metadata.

### C.4 Overly generic platform permission symbols

```text
Current:   PERM_SETTINGS_VIEW, PERM_SETTINGS_UPDATE, PERM_MASTERDATA_*,
           PERM_FEATURE_FLAGS_UPDATE, PERM_MAINTENANCE_SCHEDULE,
           PERM_RELEASES_PUBLISH, PERM_HEALTH_VIEW,
           PERM_SECURITY_POLICIES_UPDATE, PERM_REPORTS_VIEW,
           PERM_REPORTS_EXPORT
Canonical: PERM_PLATFORM_SETTINGS_VIEW, PERM_PLATFORM_SETTINGS_UPDATE,
           PERM_PLATFORM_MASTERDATA_*, PERM_PLATFORM_FEATURE_FLAGS_UPDATE,
           PERM_PLATFORM_MAINTENANCE_SCHEDULE, PERM_PLATFORM_RELEASES_PUBLISH,
           PERM_PLATFORM_HEALTH_VIEW, PERM_PLATFORM_SECURITY_POLICIES_UPDATE,
           PERM_PLATFORM_REPORTS_VIEW, PERM_PLATFORM_REPORTS_EXPORT
Reason:    Unprefixed names collide conceptually with organization/facility/site
           settings and reports. Values are unchanged.
Category:  Authorization
Files:     app/modules/identity/constants.py
           app/modules/platform/routes.py
           app/modules/platform/service.py
```

### C.5 Domain comments that named application concepts after API collections

```text
Current:   Docstrings / messages that say “API-01 mutations”, “API-02 facility
           service”, “rejected for API-01”, “API-01 updates platform-scoped…”
Canonical: Domain wording, with API inventory mentioned only when the sentence
           is about the frozen contract.
Reason:    Application code should describe platform / organization / facility /
           site / audit concepts. API numbers stay in inventory context.
Category:  Documentation / comments
Files:     app/modules/audit/service.py
           app/api/deps.py
           app/modules/organization/routes.py
           app/modules/organization/schemas.py
           app/modules/facility/routes.py
           app/modules/facility/schemas.py
           app/modules/platform/routes.py
           app/modules/platform/service.py
           app/modules/platform/models/platform_configuration.py
           app/modules/reporting/models.py
           app/api/contracts/catalog.py
           tests/core/test_access.py
           tests/api/platform_auth.py
```

### C.6 Test fixture identifiers that used API numbers as unique prefixes

```text
Current:   API01_{uuid} master-data codes; api01.test login identifiers
Canonical: STATUS_{uuid} / test.user.{uuid} style fixtures
Reason:    These are not API inventory IDs. Using API01 as a unique prefix
           mixes inventory identity into test data.
Category:  Tests
Files:     tests/api/test_platform_admin.py
           tests/api/platform_auth.py
```

---

## D. Duplicate Concepts

| Overlapping names | Canonical |
| --- | --- |
| `API01_PERMISSION_CODES` vs platform `PERM_*` string literals | Named `PERM_PLATFORM_*` constants; `PLATFORM_PERMISSION_CODES` is the tuple of those constants |
| `API02_PERMISSION_CODES` vs org/facility/site `PERM_*` | Named `PERM_ORGANIZATION_*` / `PERM_FACILITY_*` / `PERM_SITE_*`; domain tuples compose them |
| `API01_AUTHORIZATION` values vs `API01_PERMISSION_CODES` | Different responsibilities. Catalog map stays `OPERATION_AUTHORIZATION`. Permission registries stay in `identity.constants` |
| `_API02_PERMISSIONS` in `test_011_*` vs identity constants | Test now asserts the canonical domain tuples against the historical SQL seed |
| Alembic `_API01_PERMISSION_CODES` / `_API02_PERMISSION_CODES` vs identity constants | Left in migrations (history). Runtime does not import them |

No leftover aliases such as `API02_PERMISSION_CODES = ORGANIZATION_PERMISSION_CODES`.

---

## E. Historical Names

Leave unchanged in migration history and SQL twins:

- `010_api01_platform_administration.py` / revision `010_api01_platform_admin`
- `011_api02_organization_facility_site.py` / revision `011_api02_org_facility_site`
- `database/migrations/010_seed_api01_platform_administration.sql`
- `database/migrations/011_seed_api02_organization_facility_site.sql`
- Seed comments that say “API-01 permission codes” / “API-02 … permission seed”
- Seed data such as `REL-API01-001` (historical release code)

Document rather than rewrite.

---

## F. Ambiguous Names

| Name | Judgment |
| --- | --- |
| `API01_AUTHORIZATION` / `API02_AUTHORIZATION` | Inventory metadata, not a permission registry. Consolidated to one map rather than kept as per-collection dicts. |
| `platform_auth.py` | Shared live-DB identity helpers (platform admin + tenant tests). Filename kept; docstring corrected. Renaming the module would be cosmetic. |
| `load_platform_principal` vs `load_authorized_principal` | Already semantic. Platform loader is PLATFORM-scoped; authorized loader loads all assignments. |
| `PLATFORM_ADMIN_PERMISSION_CODE` | Legacy 008 code `PLATFORM_ADMIN_MANAGE_SETTINGS` (uppercase, not dotted). Keep; it is a database permission identity. |
| Schema names `OrganizationCreate` vs suggested `OrganizationCreateRequest` | Existing names match catalog `request_schema` strings (`OrganizationCreate`, `FacilityUpdate`, …). Cosmetic rename would churn the catalog without adding meaning. Keep. |
| `API01_PATHS` / `API02_PATHS` | Contract-test fixtures for numbered collections. Keep. |
| `test_api01_*` | Explicit API-01 contract tests. Keep. Domain tests in `test_organization_facility_site.py` are already semantic. |

---

## G. Out of Scope (already correct)

- No `API02Service`, `API02Repository`, `API02Auth`, `API02Principal`
- No `API02CreateOrganizationRequest` schemas
- No `API01_ENABLED` / `API02_PERMISSION_MODE` configuration
- No `api02_facility` database tables
- No `api02.organization.created` audit events
- No per-collection authorization systems
- Route modules already live under domain packages
