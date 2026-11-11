# Route source inventory — bottom-up (2026-11-03)

**Primary evidence:** FastAPI route decorators and programmatic registrations in `app/**/*routes*.py` and `app/api/v1/health.py`, reconciled with `app.main:app` runtime routes.

**Machine output:** `digitize-services/scripts/route_source_inventory.py` → `var/route_source_per_file.csv`, `var/route_registered_unique.csv`, `var/route_source_inventory.json`.

**Naming note:** There is **no** file named exactly `route.py`. The repository uses `routes.py`, `routes_*.py`, and `*_routes.py` under each module.

## Other router registration (not route.py)

| File | Role | Endpoints |
| --- | --- | --- |
| `app/api/router.py` | Mounts v1 at `/api/v1` | 0 (aggregator) |
| `app/api/v1/routes.py` | Includes module routers + health | 0 (aggregator) |
| `app/main.py` | `include_router(api_router, prefix="/api")`; `/docs` HTML | 2 GET (non-API-00, non-product) |

## Per-file endpoint counts (AST + factory registrations)

| Route file | GET | POST | PUT | PATCH | DELETE | Other | Total (source) | Runtime methods |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| app/api/v1/health.py | 2 | 0 | 0 | 0 | 0 | 0 | 2 | 2 |
| app/api/v1/routes.py | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| app/modules/attendance/routes.py | 4 | 14 | 0 | 1 | 0 | 0 | 19 | 19 |
| app/modules/attendance/walk_in_admission_routes.py | 3 | 1 | 0 | 1 | 0 | 0 | 5 | 5 |
| app/modules/audit/routes.py | 2 | 1 | 0 | 0 | 0 | 0 | 3 | 3 |
| app/modules/authentication/routes.py | 0 | 5 | 0 | 0 | 0 | 0 | 5 | 5 |
| app/modules/billing/routes.py | 4 | 6 | 0 | 0 | 0 | 0 | 10 | 10 |
| app/modules/campaign/routes.py | 2 | 9 | 0 | 1 | 0 | 0 | 12 | 12 |
| app/modules/communication/routes.py | 5 | 10 | 0 | 2 | 1 | 0 | 18 | 18 |
| app/modules/customer/routes.py | 3 | 10 | 0 | 1 | 0 | 0 | 14 | 14 |
| app/modules/facility/operations/routes.py | 5 | 3 | 1 | 1 | 0 | 0 | 10 | 10 |
| app/modules/facility/routes.py | 15 | 10 | 1 | 6 | 2 | 0 | 34 | 34 |
| app/modules/identity/routes.py | 2 | 8 | 0 | 2 | 0 | 0 | 12 | 12 |
| app/modules/media/routes.py | 3 | 3 | 0 | 0 | 1 | 0 | 7 | 7 |
| app/modules/membership/routes.py | 4 | 11 | 0 | 1 | 1 | 0 | 17 | 17 |
| app/modules/organization/routes.py | 7 | 9 | 0 | 3 | 0 | 0 | 19 | 19 |
| app/modules/platform/routes.py | 3 | 4 | 0 | 4 | 0 | 0 | 11 | 11 |
| app/modules/reference/routes.py | 6 | 0 | 0 | 0 | 0 | 0 | 6 | 6 |
| app/modules/reportsandanalytics/routes.py | 7 | 12 | 0 | 0 | 1 | 0 | 20 | 19 |
| app/modules/subscription/routes.py | 23 | 37 | 0 | 2 | 1 | 0 | 63 | 63 |
| app/modules/support/routes.py | 1 | 9 | 0 | 1 | 0 | 0 | 11 | 11 |
| app/modules/support/routes_center.py | 9 | 9 | 0 | 2 | 0 | 0 | 20 | 20 |
| app/modules/support/ws_routes.py | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 |
| app/modules/training/routes.py | 4 | 4 | 0 | 1 | 0 | 0 | 9 | 9 |
| app/modules/training/routes_ops.py | 12 | 20 | 0 | 3 | 1 | 0 | 36 | 36 |
| ~~app/modules/users/routes.py~~ | — | — | — | — | — | — | — | **Removed** (GAP-API03-005, 2026-11-04; re-verified 2026-11-09) |
| **Grand total** | **127** | **196** | **2** | **32** | **8** | **1** | **366** | **363** |

**Zero endpoints:** `app/api/v1/routes.py` — router aggregator only (`LIVE_MODULE_ROUTERS`).

**Legacy users scaffold:** retired — module directory absent; canonical staff lifecycle under `app/modules/identity/routes.py`.

**Source vs runtime on reports:** AST counts 20 declarations (12 decorators + 7 `_post(...)` factories + 1 template `add_api_route` inside `_post`); runtime registers **19** HTTP handlers from that module. The template `add_api_route` inside `_post` must not be counted as a live route.

## Module subtotals (grouped by feature module)

| Module | Source total | Runtime methods |
| --- | ---: | ---: |
| subscription | 63 | 63 |
| training (+ routes_ops) | 45 | 45 |
| facility (+ operations) | 44 | 44 |
| support (+ center + ws) | 32 | 32 |
| attendance (+ walk-in) | 24 | 24 |
| organization | 19 | 19 |
| reportsandanalytics | 20 | 19 |
| communication | 18 | 18 |
| membership | 17 | 17 |
| customer | 14 | 14 |
| campaign | 12 | 12 |
| identity | 12 | 12 |
| platform | 11 | 11 |
| billing | 10 | 10 |
| media | 7 | 7 |
| reference | 6 | 6 |
| authentication | 5 | 5 |
| audit | 3 | 3 |
| api/health | 2 | 2 |
| users (unregistered) | 2 | 0 |

## A. Source declaration count vs B. Unique registered count

| Metric | Count |
| --- | ---: |
| A. Source declarations (all route files, incl. unregistered users) | **366** |
| A′. Source in mounted router tree (excl. users) | **364** |
| B. Unique registered `(method, path)` on app | **365** |
| B′. Unique `/api/v1` `(method, path)` | **363** (362 HTTP + 1 WebSocket) |
| B″. Unique `/api/v1` HTTP only | **362** |
| Non-v1 product routes | **2** (`GET /docs`, `GET /docs/oauth2-redirect`) |

**Reconciliation:**

- **362 HTTP `/api/v1`** matches catalog mapping **204 numbered implemented + 158 extras** (disjoint paths).
- **+1 WebSocket** (`/api/v1/support/ws/conversations/{ticket_id}`) is an approved support extra (not in 228).
- **+2** OpenAPI UI routes on `app` (technical, not product).
- **366 − 2 users − 1 reports template double-count ≈ 363** mounted source declarations aligned with runtime.

No duplicate `(method, path)` pairs on the running app.

## Post-hoc catalog classification (HTTP `/api/v1` only)

| Class | Count |
| --- | ---: |
| Numbered API-01…API-14 (`BACKEND_IMPLEMENTED`) | 204 |
| Catalog `EXTRA_OPERATIONS` | 158 |
| Unmapped HTTP v1 | **0** |
| Numbered skeleton (no route) | 24 |

ORG-TERMS routes in source: **6** HTTP handlers in `organization/routes.py` (plus onboarding accept as separate extra path).

## Implementation vs skeleton (source-based)

| Finding | Detail |
| --- | --- |
| HTTP 501 / placeholder handlers in route files | **None** found |
| Registered handlers | Delegate to module services/repositories |
| Numbered skeletons | **24** contracts with **no** route registration (not incomplete handlers) |
| Unregistered legacy | `users/routes.py` — real handlers but **not mounted** |

## Regenerate

```bash
cd digitize-services && poetry run python scripts/route_source_inventory.py
```
