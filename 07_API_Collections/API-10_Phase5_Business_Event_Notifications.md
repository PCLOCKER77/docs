# API-10 Phase 5 — Business-event notifications

## Event discovery

| Candidate event | Source of truth | Transaction boundary | Organization context | Eligibility | Decision |
|---|---|---|---|---|---|
| Membership activated | `MembershipLifecycleService.activate` after status → ACTIVE | Same request transaction as membership write + audit | `membership.organization_id` | Successful activation (not idempotency replay-only return before transition) | **Implemented** — `MEMBERSHIP_ACTIVATED` |
| Membership expired | `MembershipLifecycleService.expire` after status → EXPIRED | Same transaction | `membership.organization_id` | Successful expiry transition | **Implemented** — `MEMBERSHIP_EXPIRED` |
| Facility offline payment recorded | `OfflinePaymentService.record` after new SUCCESS payment | Same transaction | `invoice.organization_id` | New payment row (not idempotency replay / existing success short-circuit) | **Implemented** — `FACILITY_PAYMENT_RECORDED` |
| Training in-app ops | `queue_in_app_notification` in training module | Existing path | Per training service | Already queues IN_APP without rules | **Deferred** — separate pre-Phase-5 path; not duplicated |
| Subscription payment failure | No single persisted failure notification trigger found | — | — | Business rules not established in repo | **Deferred** |
| Campaign approval/complete | Campaign lifecycle | Campaign launch already queues messages | — | Covered by Phase 2 launch | **Deferred** (not business-event rules) |
| Invoice issued | `FacilityInvoiceService.create_membership_invoice` | Billing | Org | No customer rule product defined in API-10 | **Deferred** |

## Rule resolution policy

- Active rule where `notification_rules.rule_code` **equals** the event key (uppercase), scoped to `organization_id`.
- At most one rule per `(organization_id, rule_code)` (DB unique constraint).
- **No rule → no notification** (no default template).
- `PROMOTIONAL` rules are **skipped** until preference/consent phase (`PROMOTIONAL_CONSENT_NOT_ENFORCED`).
- Rule must reference `template_id`; channel(s) from `channel_code` and/or `rule_configuration.allowed_channels`.
- Template render uses Phase 4 `TemplateService.render_for_campaign` + variable merge (rule defaults + event variables).

## Idempotency

- Queue idempotency key: `biz-{EVENT_KEY}-{entity_id}-{rule_id}-{channel_code}` on `communication.queued_messages` (org-scoped unique).
- **At-least-once** domain processing with **at-most-one queued message per key** (replay returns existing row via `send_manual` / pre-check).
- Not exactly-once delivery to external providers.

## Transaction boundaries

- Dispatch runs in the **same SQLAlchemy session** as the domain operation, after the domain state change and domain audit.
- Failures in notification dispatch are **caught and logged**; they do **not** roll back membership/payment work.
- No external provider calls in the domain transaction.

## Channels

- Recipients resolved from customer PII per channel (EMAIL/PHONE); IN_APP not auto-resolved (no customer→user mapping in repo).
- Independent per-channel queue rows when `allowed_channels` lists multiple entries.

## Files

- `app/modules/communication/business_event_notifications.py`
- `app/modules/communication/recipient_resolution.py`
- Hooks: `membership/lifecycle_service.py`, `billing/payment_service.py`
- `constants.py`, `notification_service.py` (business-event audit source)

## Migration

None added in Phase 5. Migrations 064–067 remain **created, not applied**.

## Deferred

- PROMOTIONAL sends pending API-10-024 / consent.
- IN_APP business events pending customer user linkage.
- Training notifications remain on existing training helper.
