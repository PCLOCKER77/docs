# API-13 — Audit product decision recommendation

**Status:** **Approved product decisions (2026-11-09)** for trusted capture, governance entities, and security-event persistence. Retention durations remain **legal/professional approval** pending.  
**Inventory:** 3/12 **Implemented** (`GET /audit-events`, `POST /audit-events/export`, `GET /audit-analytics`); 9 **Deferred / Blocked**.  
**Recommendation date:** 2026-11-02.  
**Tracker:** [DEV-19](../16_Development_Readiness/DEV-19_Feature_Completion_Tracker.md).

## Classification

| ID | Operation | Class | Notes |
| --- | --- | --- | --- |
| API-13-005 | GET `/audit-events` | **Implemented** | Org-scoped read of `audit.audit_event` |
| API-13-009 | POST `/audit-events/export` | **Implemented** | Sync JSON export (first page) |
| API-13-012 | GET `/audit-analytics` | **Implemented** | Counts by action / entity_type |
| API-13-001 | POST `/audit-events` | **Client-writable capture** | Block — see recommendation |
| API-13-002 | POST `/authentication-events` | **Client-writable capture** | Auth stack already writes `security.authentication_event` |
| API-13-003 | POST `/audit-events/configuration-changes` | **Client-writable / undefined subtype** | Config changes already audited via domain `record_audit_event` |
| API-13-004 | POST `/security-events` | **Blocked — product + likely schema** | No `security.security_event` ORM; logs ≠ durable store |
| API-13-006 | POST `/investigations` | **Blocked — schema** | No investigation table |
| API-13-007 | POST `/compliance-records/reports` | **Blocked — product** | No compliance-record model; overlaps API-11 |
| API-13-008 | POST `/audit-events/archive` | **Blocked — product** | Archive destination/lifecycle undefined |
| API-13-010 | PATCH `/audit-policies/{id}` | **Blocked — schema** | Catalog `database_gap` |
| API-13-011 | GET `/compliance-violations` | **Blocked — schema** | Catalog `database_gap` |

## Recommendation (preserve server-authoritative audit)

1. **Keep capture POSTs (13-001/002/003) as non-client contracts.**  
   Business and auth events must continue to be written only by trusted server-side paths (`record_audit_event`, authentication service). Allowing authenticated clients to POST audit rows invents a forgeable audit surface and weakens tenant forensic value.

2. **Document FR mapping as “system side-effect,” not HTTP ingest.**  
   Prefer leaving these operation IDs as `SKELETON_CREATED` / documented deferred **or**, if product insists on inventory closure without ingest, authorize a **documentation-only** status (not implemented here) that maps FRs to existing side effects — do **not** register success routes that accept client bodies.

3. **Security events (13-004):** Either  
   - (A) declare satisfied by `security.authentication_event` + structured logs (no new API), or  
   - (B) authorize a new table + write policy (who may insert, what payload is allowed). Do not expose unrestricted client POST.

4. **Investigations / compliance / archive / policies / violations:** Require explicit schema + product lifecycle before any route registration.

5. **Permissions:** Phase 1 read APIs alias `report.view`. Optional hardening: seed `audit.events.view` under `AUDIT_COMPLIANCE` and grant Organization Admin — needs migration authorization.

6. **Sensitive data:** Continue using `materialize_audit_event_payload`; never return raw ciphertext, tokens, or password material in list/export/analytics.

## Decision asked of product

> Confirm that API-13-001/002/003 remain **server-side side effects only** (no client POST ingest), and choose (A) or (B) for security events / compliance schema work.
