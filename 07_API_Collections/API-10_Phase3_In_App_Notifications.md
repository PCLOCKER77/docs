# API-10 Phase 3 — In-app notification experience

## Scope

Current-user in-app notification inbox backed by `communication.message_recipients` and `communication.queued_messages` (IN_APP channel). Platform admins receive an empty inbox (governance-only).

## Catalog extras (not numbered 228)

| ID | Method | Path | operation_id |
|----|--------|------|--------------|
| INAPP-001 | GET | `/api/v1/me/notifications` | `me_notifications_list` |
| INAPP-002 | GET | `/api/v1/me/notifications/unread-count` | `me_notifications_unread_count_list` |
| INAPP-003 | PATCH | `/api/v1/me/notifications/{inbox_item_id}/read` | `me_notifications_read_update` |
| INAPP-004 | POST | `/api/v1/me/notifications/mark-read` | `me_notifications_mark_read_create` |

Numbered API-10 operations unchanged (157 implemented).

## Migration

- **066_in_app_notification_inbox** — `read_at`, `inbox_archived_at`, IN_APP channel seed, inbox index. Created, not applied.

## Flutter

- App shell notification bell (hidden for platform admin).
- Route `/notifications/inbox` with list, unread filter, mark-all-read, tap-to-read and best-effort navigation from payload (`entity_type`, `entity_id`).

## Delivery

`NotificationService.deliver` treats `IN_APP` as internally delivered (no external provider).

## Deferred

- Frozen numbered inbox operations (none in catalog); extras used instead.
- Real DB / E2E verification (migration not applied on protected databases).
- Push notifications (Phase 8).
