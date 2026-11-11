# GAP-JRN-012 — Support ticket lifecycle (Flutter)

**Date:** 2026-11-08  
**Scope:** Connect Flutter support ticket journey to **registered** API-12 and support-center ticket/message routes. **Exclude** API-12-008 escalation (GAP-API12-001).

## Backend operations consumed (unchanged contracts)

| Operation | HTTP |
| --- | --- |
| Create ticket | `POST /api/v1/support-tickets` |
| List / reports | `GET /api/v1/support-tickets/reports` |
| Ticket detail | `GET /api/v1/support-tickets/{ticket_id}` |
| Classify, assign, priority, accept, progress, information, resolve, close, reopen | `POST /api/v1/support-tickets/{ticket_id}/…` |
| Messages (conversation) | `GET /api/v1/support-tickets/{ticket_id}/messages` |
| Open chat navigation | `/support/conversations/{ticket_id}` (existing route) |

Escalate: **not** registered; UI shows static unavailability only (`SupportTicketEscalationNotice`).

## Flutter changes (ticket lifecycle)

- Detail reload uses `getTicket` instead of scanning reports.
- Lifecycle actions refresh ticket via `getTicket` after success; progress conflicts (`412`) reload + user message.
- List pagination (`Load more`) on reports.
- Status / priority / category chips on detail and list subtitles.
- Conversation panel on detail when `participate.support.conversation` is granted (reuses `SupportConversationRepository`).

## Flutter changes (agent workspace)

| Operation | HTTP |
| --- | --- |
| Assigned inbox | `GET /api/v1/support/agent/inbox` |
| Unassigned queue | `GET /api/v1/support/agent/queue/unassigned` |
| Auto-assign | `POST /api/v1/support-tickets/{ticket_id}/auto-assign` |

- `SupportAgentDashboardPage`: permission gate, retry/refresh, priority in rows.
- `SupportAgentTicketControls`: `getTicket` refresh after lifecycle actions.

## Backend fix

- `routes_center.py`: six paginated endpoints used invalid `pagination_metadata(page, page_size, total)`; fixed to keyword args per `envelopes.py`.

## Tests

| Suite | Command | Result |
| --- | --- | --- |
| Flutter widget (tickets) | `flutter test test/features/support_tickets/support_ticket_pages_test.dart` | **11 passed** |
| Flutter widget (agent) | `flutter test test/features/support_agent/` | **4 passed** |
| Backend unit | `poetry run pytest tests/support/ -q` (excl. PG opt-in) | **31 passed** |
| Backend PG IV | `DIGITIZE_SUPPORT_PG_TEST=1 pytest tests/support/test_support_tickets_digitize_postgres.py -q` | **1 passed** |

## Status

- **GAP-JRN-012:** **Partial** — authorized lifecycle + messages preview **TESTED**; escalation remains **GAP-API12-001 AWAITING_AUTHORIZATION**.
