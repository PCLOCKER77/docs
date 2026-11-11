# API-10 Phase 4 — Templates and notification rules

## Scope

Frozen **API-10-013** and **API-10-014** implemented on existing `communication.message_templates` plus new `communication.notification_rules`. Campaign launch renders approved templates when `campaign.template_id` is set.

No Flutter UI (contracts are staff POST APIs only; no list/get template ops in numbered catalog).

## Frozen operations

| ID | operation_id | Method | Path | Permission | Audit |
|----|--------------|--------|------|------------|-------|
| API-10-013 | `notification_templates_create` | POST | `/api/v1/notification-templates` | `create.notification.template` | `CREATE_NOTIFICATION_TEMPLATE` |
| API-10-014 | `notification_rules_create` | POST | `/api/v1/notification-rules` | `configure.notification.rules` | `CONFIGURE_NOTIFICATION_RULES` |

## Template behavior

- Organization-scoped create (201); platform admins rejected (governance-only).
- Channels: `EMAIL`, `SMS`, `WHATSAPP`, `IN_APP` (provider delivery still phase 6+).
- Placeholders: `{{variable}}`; `required_variables` must cover all placeholders.
- `default_context` stored as `{required_variables, defaults}` in `message_templates.default_context`.
- Syntax validation; EMAIL requires `subject_template`.
- Unique per `(organization_id, template_code, channel_id)`.

## Rules behavior

- Upsert by `(organization_id, rule_code)` via POST configure.
- Categories: `OPERATIONAL`, `PROMOTIONAL` (consent enforcement deferred).
- Requires `template_id` and/or `channel_code`; optional `allowed_channels`, `required_variables`, `default_context`.
- Template must belong to the same organization and match channel when both provided.

## Rendering

`template_rendering.py` — separate from delivery. Campaign launch calls `TemplateService.render_for_campaign` with `configuration.template_variables`.

## Campaign integration

- Configure validates `template_id` org ownership and channel alignment.
- Launch renders template when `template_id` present; otherwise requires `configuration.body` as before.

## Migration

- **067_notification_templates_and_rules** — `notification_rules` table + permissions. Created, not applied (064–066 also unapplied).

## Tests

See phase report for commands and counts.

## Deferred

- List/update/archive template APIs (not in numbered 228).
- Rule evaluation on business events (Phase 5).
- Preferences (API-10-024).
- Real provider verification.
