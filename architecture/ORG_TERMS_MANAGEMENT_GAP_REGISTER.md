# Organization / Platform T&C Management — Gap Register

**Status:** Implementation complete for approved management extras (local `digitize` DB)  
**Last updated:** 2026-11-03  
**Related:** DR-021, ORG-TERMS-001…006 / ORG-ONBOARDING-ACCEPT-001 extras, DEV-19

## Separate domains

| Domain | Store | Consumers |
| --- | --- | --- |
| Organization onboarding T&C | `platform.terms_document` | Platform Admin CMS; OA `GET /terms/current` + onboarding accept |
| SaaS commercial terms | `commercial.saas_commercial_terms` | Checkout / SaaS commerce (unchanged; not merged) |

## Implemented extras (outside the frozen 228 numbered inventory)

| ID | Method | Path | Authz | Purpose |
| --- | --- | --- | --- | --- |
| ORG-TERMS-001 | GET | `/api/v1/terms/current` | Authenticated | Current **PUBLISHED** document (DB-backed) for OA |
| ORG-TERMS-002 | GET | `/api/v1/terms` | `platform.masterdata.view` | List drafts / published / superseded (summary; no OA draft leak) |
| ORG-TERMS-003 | POST | `/api/v1/terms` | `platform.masterdata.create` | Create draft |
| ORG-TERMS-004 | PATCH | `/api/v1/terms/{terms_id}` | `platform.masterdata.update` | Edit draft only |
| ORG-TERMS-005 | POST | `/api/v1/terms/{terms_id}/publish` | `platform.releases.publish` | Publish draft; supersede prior published atomically |
| ORG-TERMS-006 | GET | `/api/v1/terms/{terms_id}` | `platform.masterdata.view` | Full content (draft preview + historical retrieval) |
| ORG-ONBOARDING-ACCEPT-001 | POST | `/api/v1/organizations/{id}/onboarding/accept` | `organization.profile.update` | OA acceptance of current published version + hash |

**Naming note:** Product prose sometimes labels “draft creation” as ORG-TERMS-002. The **approved gap-register REST mapping above is authoritative** (002=list, 003=create, 004=patch, 005=publish, 006=get-by-id). Draft preview uses ORG-TERMS-006 (and Flutter local preview before save).

### Request / response essentials

- **Create / update draft:** `version_code`, `title`, `content` — server computes `content_hash` (SHA-256 of UTF-8 content).
- **Publish:** empty body; response is the new current document; prior PUBLISHED → SUPERSEDED in the same flush; unique partial index enforces one PUBLISHED.
- **List:** optional `document_status`, pagination; list payloads omit `content` (null); detail includes full `content`.
- **Current (OA):** `{ version, title, content, published_at, is_current, content_hash }`.
- **Accept:** `{ terms_version, accepted, content_hash? }` must match current published row; stores version + hash + acceptor + timestamp under `metadata.onboarding` without deleting prior history fields used for audit.

### Audit actions

- `TERMS_DOCUMENT_DRAFT_CREATED`
- `TERMS_DOCUMENT_DRAFT_UPDATED`
- `TERMS_DOCUMENT_PUBLISHED`
- `TERMS_DOCUMENT_SUPERSEDED`
- `ORGANIZATION_TERMS_ACCEPTED`

Full legal body is not written to audit payloads (version_code / content_hash / field names only).

## Database

| Artifact | Status |
| --- | --- |
| `platform.terms_document` | Applied via Alembic `072_platform_terms_document` on existing **`digitize`** DB |
| Seed | Initial PUBLISHED `1.0` from former code constants (hash preserved) |
| Constraints | Unique `version_code`; unique partial index one `PUBLISHED`; statuses DRAFT \| PUBLISHED \| SUPERSEDED |

Publishing does **not** deactivate, suspend, or restrict existing organizations.

## Existing-organization reacceptance

**Deferred by product decision.** New org onboarding must accept the current published version. Existing orgs keep historical acceptance; no mandatory reacceptance or operational block on newer versions.

## Flutter

| Surface | Status |
| --- | --- |
| OA onboarding scrollable T&C + checkbox + Accept and Continue | **Implemented** / **Tested** (widget) |
| Stale version reload + checkbox reset | **Implemented** / **Tested** |
| PA Terms CMS (list / draft / preview / publish / history) | **Implemented** (routes under `/platform/terms`) |
| Live E2E against shared environments | **Not Integration-verified** |

## DR-021

T&C acceptance remains one onboarding gate. It does not independently activate an organization when PA review, legal identity, or SaaS subscription requirements remain unsatisfied (`_terms_auto_activates` / `_legal_identity_ready_for_activation` unchanged).

## Tests

| Suite | Status (2026-11-03 reconciliation) |
| --- | --- |
| `tests/organization/test_onboarding_review.py` | **12 passed** (accept + hash + auto-activate rules) |
| `tests/api/test_module_routes.py` | Asserts `/api/v1/terms/*` paths registered |
| `tests/api/test_contract_registry.py` | **228** inventory + extras uniqueness |
| Flutter `organization_onboarding_terms_test.dart` | **4 passed** (OA UX) |
| PA Terms CMS | **Implemented**; widget tests per DEV-19 |
| Shared-env / PG IV for T&C | **Not Integration-verified** |

## Reconciliation note (2026-11-03)

All **ORG-TERMS-001…006** and **ORG-ONBOARDING-ACCEPT-001** are catalogued in
`EXTRA_OPERATIONS`, registered on the FastAPI app, and marked
`BACKEND_IMPLEMENTED`. They remain **outside** the frozen **228** numbered
inventory. Counting them as “+6 product APIs” without the other **150** approved
extras is misleading — see API_CONTRACT_REGISTRY § inventory reconciliation.

## Remaining limitations

- No live multi-admin concurrency soak for publish races (DB unique index is the safety net).
- No dedicated acceptance history table (still `metadata.onboarding` + audit).
- Publisher display in UI shows UUID until a principal-name join is authorized.
- EQ-011 / broad QA not in scope for this slice.
