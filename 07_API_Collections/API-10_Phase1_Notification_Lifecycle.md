# API-10 Phase 1 — Notification Lifecycle

## Selected scope

Phase 1 delivers a **manual notification outbox lifecycle** mapped to the existing `communication.queued_messages` / `message_recipients` outbox (migration 044/045). Campaign management (API-10-001–012), templates/rules (013–014), system/scheduled enqueue (015, 017), archive/reports/preferences (022–024) are **deferred**.

**Rationale:** The outbox and PII encryption helpers already exist; the smallest coherent vertical slice is enqueue → deliver → retry → history/status without campaign tables or advertisement product boundaries.

## Implemented frozen operations

| Catalog ID | operation_id | Method | Path |
|---|---|---|---|
| API-10-016 | `notifications_manual_create` | POST | `/api/v1/notifications/manual` |
| API-10-018 | `notifications_deliver` | POST | `/api/v1/notifications/{notification_id}/deliver` |
| API-10-019 | `notifications_retry` | POST | `/api/v1/notifications/{notification_id}/retry` |
| API-10-020 | `notifications_list` | GET | `/api/v1/notifications` |
| API-10-021 | `notifications_delivery_status_list` | GET | `/api/v1/notifications/{notification_id}/delivery-status` |

`notification_id` in paths is `communication.queued_messages.queued_message_id`.

## Lifecycle and states

- **Queued:** `PENDING` after manual create (payload/recipients persisted; optional PII encryption via existing helpers).
- **Deliver:** Processes all recipients through `NotificationDeliveryProvider` (default **mock** in-process provider). Writes `communication.message_delivery_attempts` rows. Sets message `SENT` when all recipients succeed, `FAILED` otherwise; increments `attempted_count`; sets `next_attempt_at` on failure.
- **Retry:** Allowed only from `FAILED` (and under max attempts). Resets to `PENDING`, audits retry, then runs deliver with a derived idempotency key.
- **Terminal / other:** `CANCELLED` unchanged; max attempts enforced (`MAX_DELIVERY_ATTEMPTS = 5`).

## Authorization and tenant isolation

| operation_id | Permission |
|---|---|
| `notifications_manual_create` | `send.manual.notification` |
| `notifications_deliver` | `deliver.notification` |
| `notifications_retry` | `retry.failed.notification` |
| `notifications_list` | `view.notification.history` |
| `notifications_delivery_status_list` | `track.delivery.status` |

Organization scoping: `organization_id` on create/list is validated with `require_organization_access`. Deliver/retry/status load the message and enforce the same. Operational writes also call `require_organization_operational_saas` (company SaaS eligibility). Platform Admin governance-only behavior is unchanged.

Permissions and role grants are defined in migration **064** (file only; not applied in this task). Organization Admin pack in code includes notification permissions.

## Idempotency

- **Create:** `Idempotency-Key` → unique `(organization_id, idempotency_key)` on `queued_messages`.
- **Deliver:** Separate `delivery_idempotency_key` on the message; replay when status is already `SENT` and key matches.
- **Retry:** Requires `Idempotency-Key`; deliver step uses `{key}:retry:{attempt}`.

## Persistence and migration

- **064_notification_delivery_foundation** (created, **not applied**): `message_delivery_attempts`, `idempotency_key`, `delivery_idempotency_key`, default channel seeds, identity permissions.
- Audit events: `SEND_MANUAL_NOTIFICATION`, `DELIVER_NOTIFICATION`, `RETRY_FAILED_NOTIFICATION` on `communication.queued_messages`.

## Delivery provider

`app/modules/communication/delivery.py` — replaceable provider; production external delivery is **not verified** (mock provider used in tests).

## Flutter

No user-facing screen required for this slice in the frozen contracts beyond API operations; **Flutter integration deferred** (no new UI/repository in this phase).

## Tests executed

```bash
cd digitize-services
poetry run pytest tests/communication/ tests/migrations/test_064_notification_delivery_foundation.py tests/identity/test_organization_admin_pack.py tests/api/test_module_routes.py tests/api/test_contract_registry.py -q
```

## Verification limits

- Migration **not** applied to `digitize` or any other database.
- No real PostgreSQL integration tests for new tables/FKs.
- Audit row durability not verified against a live DB.
- External SMS/email/WhatsApp delivery not verified (mock provider only).

## Deferred API-10 work

Campaign CRUD and lifecycle (001–012), templates/rules (013–014), system/scheduled notifications (015, 017), archive/reports/preferences (022–024), and Flutter campaign/notification UI.
