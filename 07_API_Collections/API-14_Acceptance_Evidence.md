# API-14 Common Reference — Acceptance Evidence

**Document ID:** API-14-EVIDENCE  
**Last updated:** 2026-11-09 (16-skeleton master implementation pass)  
**Status:** PARTIALLY VERIFIED (6/12 live; 6 product/migration gated)

**Decision register:** [API-14_REFERENCE_SOURCE_OF_TRUTH.md](../architecture/API-14_REFERENCE_SOURCE_OF_TRUTH.md) (proposal — GMD seeds **not** authorized).

## Live operations (INTEGRATION_VERIFIED / catalog tests)

| ID | Operation | Route | Source of truth | Evidence |
|----|-----------|-------|-----------------|----------|
| API-14-003 | List currencies | GET `/reference/currencies` | GMD `CURRENCY` | `test_reference_aliases.py`, `test_catalog_validation.py` |
| API-14-006 | List facility types | GET `/reference/facility-types` | `tenant.facility_type` | `test_contract_registry.py` alias check |
| API-14-008 | List status values | GET `/reference/status-values` | GMD `STATUS` | Catalog live tests |
| API-14-009 | List payment methods | GET `/reference/payment-methods` | `APPROVED_OFFLINE_PAYMENT_METHODS` | `test_reference_aliases.py` |
| API-14-010 | List communication channels | GET `/reference/communication-channels` | `APPROVED_CHANNEL_CODES` | Same |
| API-14-011 | List lookup values | GET `/reference/lookup-values/{group}` | Approved GMD groups | Catalog validation |

## Operation matrix (001–012) — remaining scope

| ID | Status | Blocker |
|----|--------|---------|
| API-14-001 countries | **BLOCKED_BY_SCHEMA_OR_MIGRATION_AUTHORIZATION** | GMD `COUNTRY` + seed pack |
| API-14-002 states-regions | **BLOCKED_BY_SCHEMA_OR_MIGRATION_AUTHORIZATION** | Depends on 001 |
| API-14-004 languages | **BLOCKED_BY_SCHEMA_OR_MIGRATION_AUTHORIZATION** | GMD `LANGUAGE` |
| API-14-005 timezones | **DEFERRED_BY_PRODUCT_DECISION** | Curated vs full IANA |
| API-14-007 activity-types | **DEFERRED_BY_PRODUCT_DECISION** | GMD vs training ownership |
| API-14-012 localization | **DEFERRED_BY_PRODUCT_DECISION** | Settings snapshot vs GMD |

`operation_tracking.py` `_SKELETON_GATES` matches the six skeleton rows above.

## Authorization (test-backed)

| Check | Evidence |
|-------|----------|
| Tenant GMD read active-only | `can_list_global_master_data` + `TENANT_READABLE_MASTER_DATA_GROUPS` |
| Facility types not via GMD | `reference_facility_types` uses `FacilityTypeService` |
| No skeleton routes on wire | `expected_absent_v1_http_pairs()` excludes 001/002/004/005/007/012 |

## Regression (2026-11-09)

```bash
cd digitize-services
.venv/bin/pytest tests/api/test_reference_aliases.py tests/api/test_catalog_validation.py -q
# reference_aliases: 4 passed; catalog_validation: see full api/ suite
```

## Remaining approvals

- Product sign-off on GMD seed groups (GAP-API14-001…004 in DEV-21).
- Single additive migration twin for approved groups only (DEV-23 Phase 3).

## Out of scope

- Platform Admin GMD create/update (API-01-003…005) — separate collection.
