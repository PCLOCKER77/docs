# API-12 Support Center — proposed contract extension (not numbered)

Official product API count remains **228**. The operations below are **catalog
extras** (`CAT-SUP-*`) pending product approval. They are implemented in code
behind live routes documented here; they are **not** added to
`operations.py` numbered inventory until approved.

## Migration chain (not applied)

| Revision | Depends on | Notes |
| --- | --- | --- |
| 063–068 | prior | Existing chain |
| 069_billing_refunds | 068 | Unapplied; refund reporting flag |
| 070_support_ticket_permissions | 069 | API-12 permission seeds |
| **071_support_center_foundation** | **070** | FAQ, messages, agent profiles, new permissions |

Do not apply 071 without applying 070 and 069 first.

## Reused numbered API-12 operations

| API ID | Use |
| --- | --- |
| API-12-001 | Ticket/conversation anchor (`conversation_channel=LIVE_CHAT` on new conversation create extra) |
| API-12-003 | Supervisor manual assign (reassign) |
| API-12-005–011 | Agent lifecycle on conversations |
| API-12-012 | Reporting; superseded for detail by `support_tickets_get` extra |

## Proposed extras (approval status: **PROPOSED**)

| Extra ID | Method | Path | Permission(s) | Purpose |
| --- | --- | --- | --- | --- |
| CAT-SUP-TKT-001 | GET | `/api/v1/support-tickets/{ticket_id}` | `view.support.ticket` | Ticket detail (closes Flutter reload gap) |
| CAT-SUP-FAQ-001 | GET | `/api/v1/support/faq/categories` | `view.support.faq` | Browse categories |
| CAT-SUP-FAQ-002 | GET | `/api/v1/support/faq/articles` | `view.support.faq` | Search/list articles |
| CAT-SUP-FAQ-003 | GET | `/api/v1/support/faq/articles/{article_id}` | `view.support.faq` | Article detail |
| CAT-SUP-FAQ-004 | GET | `/api/v1/support/faq/articles/{article_id}/related` | `view.support.faq` | Related articles |
| CAT-SUP-FAQ-005 | POST | `/api/v1/support/faq/articles/{article_id}/feedback` | `view.support.faq` | Helpful / not helpful |
| CAT-SUP-FAQ-010 | POST | `/api/v1/support/faq/categories` | `manage.support.faq` | Create category |
| CAT-SUP-FAQ-011 | PATCH | `/api/v1/support/faq/categories/{category_id}` | `manage.support.faq` | Update category |
| CAT-SUP-FAQ-012 | POST | `/api/v1/support/faq/articles` | `manage.support.faq` | Create article (draft) |
| CAT-SUP-FAQ-013 | PATCH | `/api/v1/support/faq/articles/{article_id}` | `manage.support.faq` | Update article |
| CAT-SUP-FAQ-014 | POST | `/api/v1/support/faq/articles/{id}/publish` | `manage.support.faq` | Publish |
| CAT-SUP-FAQ-015 | POST | `/api/v1/support/faq/articles/{id}/unpublish` | `manage.support.faq` | Unpublish |
| CAT-SUP-FAQ-016 | POST | `/api/v1/support/faq/articles/{id}/archive` | `manage.support.faq` | Archive |
| CAT-SUP-CHAT-001 | POST | `/api/v1/support/conversations` | `participate.support.conversation` | Start live chat ticket; optional `source_entity_type` / `source_entity_id` (FAQ handoff) |
| CAT-SUP-CHAT-002 | GET | `/api/v1/support-tickets/{ticket_id}/messages` | participate **or** agent | Paginated history / catch-up |
| CAT-SUP-CHAT-003 | POST | `/api/v1/support-tickets/{ticket_id}/messages` | participate **or** agent | Persist message; `Idempotency-Key` |
| CAT-SUP-CHAT-005 | GET | `/api/v1/support/conversations` | `participate.support.conversation` | Live-chat tickets created by caller |
| CAT-SUP-CHAT-004 | WS | `/api/v1/support/ws/conversations/{ticket_id}` | participate **or** agent | Real-time fan-out (single worker) |
| CAT-SUP-AGT-001 | GET | `/api/v1/support/agent/inbox` | inbox **or** agent | Assigned conversations |
| CAT-SUP-AGT-002 | GET | `/api/v1/support/agent/queue/unassigned` | inbox **or** agent | Unassigned queue |
| CAT-SUP-AGT-003 | POST | `/api/v1/support-tickets/{ticket_id}/auto-assign` | `act.as.support.agent` + `assign.ticket` | Lowest-load eligible agent |

## New permissions (migration 071)

- `view.support.faq`, `manage.support.faq`
- `participate.support.conversation`, `view.support.ticket`
- `act.as.support.agent`, `view.support.agent.inbox`

Role `SUPPORT_AGENT` (organization scope) receives agent + ticket ops, not FAQ
admin. `ORGANIZATION_ADMIN` receives FAQ manage/view and conversation
participate, not automatic agent inbox unless explicitly granted the agent role.

Platform Admin and Site Administrator are not granted tenant support superuser
access.

## Semantic decisions

- `support.ticket_comment` remains operational notes (progress, information
  requests). Customer chat uses `support.ticket_message` with visibility.
- No FAQ seed content ships in migrations. Verified articles are created via
  admin API after product review.
- WebSocket hub is in-process only; multi-worker needs Redis/EventBridge (not
  provisioned).
- Notification bridge writes `SUPPORT_NOTIFICATION_INTENT` audit events; full
  API-10 in-app delivery requires communication migrations applied.

## Idempotency

`POST .../messages` accepts optional `Idempotency-Key`, unique per ticket in
`support.ticket_message`.
