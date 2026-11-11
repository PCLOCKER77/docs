# API-13 Audit & Security — Acceptance Evidence

**Document ID:** API-13-EVIDENCE  
**Last updated:** 2026-11-08 (Phase 13 — evidence reconciliation)  
**Status:** PARTIALLY VERIFIED (3/12 live reads; 9 product/schema gated)

**Decision register:** [API-13_AUDIT_PRODUCT_DECISION.md](../architecture/API-13_AUDIT_PRODUCT_DECISION.md) (proposal — client ingest **not** authorized).

## Live operations (INTEGRATION_VERIFIED)

| ID | Operation | Route | Evidence |
|----|-----------|-------|----------|
| API-13-005 | List audit events | GET `/audit-events` | `test_audit_reads_digitize_postgres.py` |
| API-13-009 | Export audit events | POST `/audit-events/export` | Same — **202** JSON page |
| API-13-012 | Audit analytics | GET `/audit-analytics` | Same — org-scoped aggregates |

**Guard:** `DIGITIZE_AUDIT_PG_TEST=1`, `DB_NAME=digitize`, loopback, no `DATABASE_URL`.

## Operation matrix (001–012)

| ID | Status | Notes |
|----|--------|-------|
| 001 POST `/audit-events` | **DEFERRED_BY_PRODUCT_DECISION** | No client ingest route |
| 002 POST `/authentication-events` | **DEFERRED** | Auth stack writes server-side |
| 003 POST `.../configuration-changes` | **DEFERRED** | Domain `record_audit_event` |
| 004 POST `/security-events` | **BLOCKED** | No durable `security_event` store approved |
| 005 | **INTEGRATION_VERIFIED** | See above |
| 006 POST `/investigations` | **BLOCKED (schema)** | GAP-API13-003 |
| 007 POST `/compliance-records/reports` | **DEFERRED** | GAP-API13-004 |
| 008 POST `/audit-events/archive` | **DEFERRED** | Archive lifecycle undefined |
| 009 | **INTEGRATION_VERIFIED** | See above |
| 010 PATCH `/audit-policies/{id}` | **BLOCKED (schema)** | GAP-API13-005 |
| 011 GET `/compliance-violations` | **BLOCKED (schema)** | GAP-API13-005 |
| 012 | **INTEGRATION_VERIFIED** | See above |

`operation_tracking.py` matches the above for skeleton ops **001–004, 006–008, 010–011**.

## Server-side capture (architectural boundary)

- **Writer:** `record_audit_event` in `app/modules/audit/service.py` — called from domain mutations (not HTTP client POST).
- **Readers:** `AuditReadService` — org scope + `PERM_AUDIT_EVENTS_VIEW` (alias `report.view`).
- **PII:** `materialize_audit_event_payload` — `test_audit_event_pii.py`.
- **Lifecycle:** `test_lifecycle_audit.py` — org mutations emit audit with principal context.
- **Coverage:** Not exhaustive for every mutation; spot checks + PG reads only.

## Phase 13 regression (2026-11-08)

```bash
cd digitize-services
python3 -m pytest tests/audit/test_audit_read_service.py \
  tests/audit/test_audit_event_pii.py tests/organization/test_lifecycle_audit.py -q
# 12 passed

DIGITIZE_AUDIT_PG_TEST=1 ENVIRONMENT=development DB_NAME=digitize DB_HOST=localhost \
  python3 -m pytest tests/audit/test_audit_reads_digitize_postgres.py -q
# 4 passed (list, analytics, export, cross-org deny)

cd digitize-ui
flutter test test/features/audit/ -r compact
# 11 passed
```

## Authorization (test-backed)

| Check | Evidence |
|-------|----------|
| Cross-org list | **403/404** — `test_cross_organization_audit_list_is_empty_or_denied` |
| Org-scoped export | Export payload `organization_id` matches principal org |
| PA without org query | Flutter governance guidance — `audit_events_page_test.dart` |
| No client POST routes | Only GET/POST export/analytics in `route_registered_unique.csv` |

## Remaining approvals

- Product sign-off on **001–003** server-side-only stance (GAP-API13-001).
- Security event persistence policy (**004**).
- Investigation / compliance / archive / policy schemas (**006–008, 010–011**).
- Optional `audit.events.view` permission seed (GAP-API13-007) — **not** authorized.

## Out of scope

Final security audit, `digitize_test` EQ-011, new DDL, client audit writers, full module CERTIFIED while 9 ops gated.
