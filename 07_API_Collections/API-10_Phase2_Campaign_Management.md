# API-10 Phase 2 — Campaign Management

## Scope

Implements **all twelve** frozen campaign operations (API-10-001 through API-10-012) as an organization-scoped operational campaign vertical. Campaigns use the existing `campaign` ORM models aligned with migration **065** (created, not applied). Launch integrates with Phase 1 `NotificationService.send_manual` (enqueue only; delivery remains Phase 1 deliver/retry).

**Advertisement boundary:** `campaign_category=ADVERTISEMENT` is rejected at create with a validation error. Core SaaS org-admin permissions do not include advertisement billing or add-on entitlements.

**Flutter:** Not implemented — frozen ops 001–012 are backend lifecycle/performance/report endpoints without a mandated admin UI in this phase.

## Implemented operations

| ID | operation_id | Method | Path |
|---|---|---|---|
| API-10-001 | `campaigns_create` | POST | `/api/v1/campaigns` |
| API-10-002 | `campaigns_configuration_update` | PATCH | `/api/v1/campaigns/{campaign_id}/configuration` |
| API-10-003 | `campaigns_audiences` | POST | `/api/v1/campaigns/{campaign_id}/audiences` |
| API-10-004 | `campaigns_submit_for_approval` | POST | `/api/v1/campaigns/{campaign_id}/submit-for-approval` |
| API-10-005 | `campaigns_approve` | POST | `/api/v1/campaigns/{campaign_id}/approve` |
| API-10-006 | `campaigns_schedule` | POST | `/api/v1/campaigns/{campaign_id}/schedule` |
| API-10-007 | `campaigns_launch` | POST | `/api/v1/campaigns/{campaign_id}/launch` |
| API-10-008 | `campaigns_pause` | POST | `/api/v1/campaigns/{campaign_id}/pause` |
| API-10-009 | `campaigns_complete` | POST | `/api/v1/campaigns/{campaign_id}/complete` |
| API-10-010 | `campaigns_cancel` | POST | `/api/v1/campaigns/{campaign_id}/cancel` |
| API-10-011 | `campaigns_performance_list` | GET | `/api/v1/campaigns/{campaign_id}/performance` |
| API-10-012 | `campaigns_reports_list` | GET | `/api/v1/campaigns/{campaign_id}/reports` |

## Lifecycle

`DRAFT` → (submit) → `PENDING_APPROVAL` → (approve) → `APPROVED` → (schedule) → `SCHEDULED` → (launch) → `ACTIVE` → (pause) → `PAUSED` → (complete) → `COMPLETED`; cancel from several non-terminal states → `CANCELLED`.

Configuration and audience selection are allowed in `DRAFT` (configuration also in `PENDING_APPROVAL`). Launch requires configuration, audience, and `Idempotency-Key`; enqueues via outbox with idempotency `campaign-{campaign_id}-launch-{key}` and records `campaign.campaign_executions`.

## Targeting

Audience snapshots store explicit `recipients` (same shape as manual notifications). Optional `customer_id` values are validated against `customer.customer` organization scope.

## Scheduling

`scheduled_at` must be timezone-aware (offset required) and in the future (UTC comparison). No background worker — schedule persists `campaign.campaign_schedule`; launch is explicit via API-10-007.

## Authorization

Permissions match BA table (`create.campaign`, `configure.campaign`, …). Seeded in migration 065 for PLATFORM_ADMIN and ORGANIZATION_ADMIN. Operational writes use `require_organization_operational_saas` where applicable.

## Migrations

- **065_campaign_management.sql** — `campaign` schema, executions table, permissions (not applied).
- Depends on **064** and communication outbox tables.

## Tests

```bash
cd digitize-services
poetry run pytest tests/campaign/ tests/communication/ tests/migrations/test_065_campaign_management.py tests/identity/test_organization_admin_pack.py tests/api/test_module_routes.py tests/api/test_contract_registry.py -q
```

## Verification limits

No migration applied to protected databases; no PostgreSQL integration tests; metrics `delivered_count` not wired to provider callbacks; scheduled launch not auto-run without a worker.

## Deferred

API-10-013–024, advertisement product eligibility implementation, Flutter campaign UI, automatic scheduled launch worker.
