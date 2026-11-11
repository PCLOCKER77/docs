# API inventory reconciliation — 2026-11-04

**Script:** `digitize-services/scripts/api_inventory_reconciliation.py`  
**Canonical registry:** `digitize-services/app/api/contracts/api_registry.py`  
**Output:** `digitize-services/var/api_inventory_reconciliation.json`  
**Related:** [API_CONTRACT_REGISTRY.md](../../architecture/API_CONTRACT_REGISTRY.md), [ROUTE_SOURCE_INVENTORY_2026-11-03.md](./ROUTE_SOURCE_INVENTORY_2026-11-03.md)

## Scope

Full bottom-up reconciliation of:

- 228 numbered product operations (`api_registry.py` numbered rows)
- 158 additional approved operations (`api_registry.py` additional rows), including ORG-TERMS-001…006 and ORG-ONBOARDING-ACCEPT-001
- FastAPI runtime HTTP, WebSocket, and documentation routes
- AST source declarations and unmounted handlers

## Calculated totals

| Metric | Value |
| --- | ---: |
| Numbered approved | 228 |
| Additional approved | 158 |
| Total approved identities | 386 |
| Numbered live HTTP | 204 |
| Numbered skeleton | 24 |
| Extra OPS health | 2 |
| Extra product (incl. T&C + onboarding) | 156 |
| ORG-TERMS | 6 |
| ORG-ONBOARDING-ACCEPT-001 | 1 |
| Runtime `/api/v1` HTTP pairs | 362 |
| WebSocket `/api/v1` | 1 |
| Documentation routes | 2 |
| Source declarations | 366 |
| Unmounted (users scaffold) | 2 |
| Unmapped v1 HTTP | 0 |

## ORG-TERMS and onboarding

All six ORG-TERMS `api_id` rows and `ORG-ONBOARDING-ACCEPT-001` are in `EXTRA_OPERATIONS` and reconcile to registered runtime routes via `org_terms_extra_pairs()` and catalogue validation.

## Unmounted source

`app/modules/users/routes.py` — 2 decorator handlers, excluded from `LIVE_MODULE_ROUTERS` in `app/api/v1/routes.py`. Not in `EXTRA_OPERATIONS` (retired scaffold).

## Defects fixed in this pass

| Issue | Fix |
| --- | --- |
| Split inventory ownership (`operations.py` + `extra_operations.py`) | Consolidated into **`api_registry.py`**; compatibility shims removed (2026-11-04 final cleanup) |
| Hardcoded per-collection counts in `validate_numbered_product_catalog()` | Derive expected counts from `NUMBERED_OPERATIONS` |
| `NUMBERED_COUNT = 228` literal | `NUMBERED_COUNT = len(NUMBERED_OPERATIONS)` |
| No single full-surface reconciliation script | Added `api_inventory_reconciliation.py` |
| Registry doc implied 228 = total API surface | Added § Complete inventory reconciliation in API_CONTRACT_REGISTRY |

## Validation

```bash
cd digitize-services
poetry run python scripts/api_inventory_reconciliation.py
poetry run pytest tests/api/test_api_inventory_reconciliation.py tests/api/test_runtime_catalog.py tests/api/test_contract_registry.py tests/api/test_module_routes.py -q
```

**Result:** catalogue validation passes; inventory tests pass.

## Assessment

**COMPLETE WITH APPROVED DEFERRED ITEMS** — inventory layers reconcile; 24 numbered skeletons and product-blocked verticals remain deferred per decision registers (not inventory defects).
