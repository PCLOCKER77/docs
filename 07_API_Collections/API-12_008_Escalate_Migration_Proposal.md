# API-12-008 Support Ticket Escalate — Migration Proposal (refined)

**Status:** **Approved and implemented (2026-11-09)** — GAP-API12-001 history-only Phase 1; migration `083_support_ticket_escalation`; live route `support_tickets_escalate`.  
**Related:** [API-12_Support_Implementation_Report.md](API-12_Support_Implementation_Report.md), [DEV-19](../16_Development_Readiness/DEV-19_Feature_Completion_Tracker.md)  
**Catalog:** `support_tickets_escalate` → `BACKEND_IMPLEMENTED` (`IMPLEMENTED_NUMBERED_KEYS`).  
**Head:** `083_support_ticket_escalation` (revises `082_billing_manual_reconciliation`).

## Validation against current module

| Check | Finding |
| --- | --- |
| Ticket table | `support.support_ticket` with `organization_id`, `priority_id`, `ticket_status`, `severity`, `version_number` |
| Existing escalate surface | **None** — migration 070 explicitly does **not** create `support.ticket_escalation` |
| Related live ops | classify, assign, priority, accept, progress, info-request, resolve, close, reopen |
| Permissions | No `escalate.ticket`; closest: `set.ticket.priority`, `assign.ticket` |
| Tenant boundary | Tickets are **organization-scoped** (no facility/site column); Site Admin must not gain org-wide ticket grants (070 documents this) |
| Status vocab | Current default `OPEN`; no `ESCALATED` in live service |

## Approved Phase-1 semantics (history-only)

**Immutable escalation history only** — ticket status unchanged; no `ESCALATED` status:

1. Insert `support.ticket_escalation` row (always).
2. Do **not** mutate `priority_id`, `severity`, or assignee in Phase 1 (`to_priority_id` / `to_severity` rejected with 422).
3. Emit `record_audit_event` with action `SUPPORT_TICKET_ESCALATED`.
4. Require `If-Match` / `version_number` like other ticket mutations.

## Proposed DDL (additive twin)

```sql
-- support.ticket_escalation
CREATE TABLE IF NOT EXISTS support.ticket_escalation (
    record_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID NOT NULL
        REFERENCES tenant.organization (record_id) ON DELETE RESTRICT,
    ticket_id UUID NOT NULL
        REFERENCES support.support_ticket (record_id) ON DELETE CASCADE,
    from_priority_id UUID NULL
        REFERENCES support.ticket_priority (record_id) ON DELETE RESTRICT,
    to_priority_id UUID NULL
        REFERENCES support.ticket_priority (record_id) ON DELETE RESTRICT,
    from_severity VARCHAR(40) NULL,
    to_severity VARCHAR(40) NULL,
    escalation_reason TEXT NOT NULL,
    escalated_by_user_id UUID NULL
        REFERENCES identity.user_account (record_id) ON DELETE SET NULL,
    escalated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by UUID NULL,
    version_number INTEGER NOT NULL DEFAULT 1,
    CONSTRAINT ck_ticket_escalation_reason_nonempty
        CHECK (char_length(btrim(escalation_reason)) >= 1)
);

CREATE INDEX IF NOT EXISTS idx_ticket_escalation_ticket
    ON support.ticket_escalation (ticket_id, escalated_at DESC);

CREATE INDEX IF NOT EXISTS idx_ticket_escalation_org
    ON support.ticket_escalation (organization_id, escalated_at DESC);
```

Permission seed (same style as 070):

```sql
INSERT INTO identity.permission (
    permission_code, permission_name, module_code, capability_code
) VALUES (
    'escalate.ticket', 'Escalate Ticket', 'SUPPORT', 'ESCALATE'
) ON CONFLICT (permission_code) DO NOTHING;
-- Grant to Organization Admin pack roles only (not Platform Admin tenant bypass;
-- not Site Administrator — tickets are org-scoped).
```

## Product decisions still required

1. Escalate = history-only vs history + priority/severity mutation vs new `ESCALATED` status.  
2. Confirm permission `escalate.ticket` and role grants (Org Admin / support agent roles only).  
3. Request body fields: `escalation_reason` required; optional `to_priority_id`, `to_severity`, `assignee_user_id`.  
4. Whether escalate is allowed from all open operational statuses or a subset.

## Explicit non-actions until authorized

- Do not register a 501-replacement live route that stores escalations only in memory.  
- Do not apply this migration to `digitize`, QA, or production.  
- Do not grant Site Administrator org-wide escalate (same reason as 070).

## After authorization

1. Author `migrations/versions/072_…py` + `migrations/sql/072_….sql`.  
2. Implement `SupportTicketService.escalate` + route `operation_id=support_tickets_escalate`.  
3. Mark catalog implemented; add unit tests for authz, org isolation, and priority validation.  
4. Apply only to explicitly named environments.
