# API-12 Support Tickets — Acceptance Evidence

**Document ID:** API-12-EVIDENCE  
**Last updated:** 2026-11-08 (Phase 12 — lifecycle re-verification)  
**Status:** PARTIALLY VERIFIED (11/12 live; API-12-008 gated)

## Operation matrix (API-12-001 … API-12-012)

| ID | Operation | Backend route | Status | Evidence |
|----|-----------|---------------|--------|----------|
| API-12-001 | Create ticket | POST `/support-tickets` | **Implemented** | Unit + PG IV |
| API-12-002 | Classify | POST `.../classify` | **Implemented** | Unit + PG IV |
| API-12-003 | Assign | POST `.../assign` | **Implemented** | Unit + PG IV |
| API-12-004 | Set priority | POST `.../priority` | **Implemented** | Unit |
| API-12-005 | Accept | POST `.../accept` | **Implemented** | Unit + PG IV |
| API-12-006 | Progress update | POST `.../progress` | **Implemented** | Unit + PG IV (If-Match) |
| API-12-007 | Request information | POST `.../info-request` | **Implemented** | Unit |
| API-12-008 | Escalate | POST `.../escalate` | **SKELETON** / **AWAITING_AUTHORIZATION** | GAP-API12-001 — no route, no `ticket_escalation` table |
| API-12-009 | Resolve | POST `.../resolve` | **Implemented** | Unit + PG IV |
| API-12-010 | Close | POST `.../close` | **Implemented** | Unit |
| API-12-011 | Reopen | POST `.../reopen` | **Implemented** | Unit |
| API-12-012 | Reports | GET `/support-tickets/reports` | **Implemented** | Unit + PG IV |

**Alembic head (repo):** `082_billing_manual_reconciliation` (support foundation **070** / **071** applied on `digitize`; no escalation migration).

## Gap map

| Gap ID | Status | Notes |
|--------|--------|-------|
| GAP-API12-002 | **INTEGRATION_VERIFIED** | `test_support_tickets_digitize_postgres.py` on local `digitize` |
| GAP-API12-001 | **AWAITING_AUTHORIZATION** | Migration + `escalate.ticket` + semantics + route — see [API-12_008_Escalate_Migration_Proposal.md](API-12_008_Escalate_Migration_Proposal.md) |
| GAP-API12-003 | Deferred / scope | Extra chat/FAQ beyond numbered 12 |

## Phase 12 regression (2026-11-08)

```bash
cd digitize-services
python3 -m pytest tests/support/ -q --ignore=tests/support/test_support_tickets_digitize_postgres.py
# 28 passed

DIGITIZE_SUPPORT_PG_TEST=1 ENVIRONMENT=development DB_NAME=digitize DB_HOST=localhost \
  python3 -m pytest tests/support/test_support_tickets_digitize_postgres.py -q
# 1 passed

cd digitize-ui
flutter test test/features/support_tickets/ test/features/support_center/ \
  test/features/support_agent/ test/features/support_conversations/ -r compact
# 18 passed
```

## Authorization / scope (test-backed)

| Check | Evidence |
|-------|----------|
| Org-scoped ticket lifecycle | PG IV + `test_support_tickets.py` |
| Escalate route not mounted | `test_module_routes.py` |
| No `ticket_escalation` DDL | `test_071_support_center_foundation.py`, migration SQL comments |
| No `escalate.ticket` in 070 | `test_070_support_ticket_permissions.py` |

## Out of scope (unchanged)

API-12-008 implementation, new migrations after head **082**, provider notifications, `digitize_test` EQ-011, full module registry CERTIFIED while 008 skeleton remains.
