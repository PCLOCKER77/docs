# API-12 Support implementation report

Live catalog authority: `digitize-services/app/api/contracts/catalog.py`.
Official numbered product API count: **228** (unchanged). API-12 collection: **12**
numbered operations; **11 implemented**, **API-12-008 escalate** unregistered.

**Production readiness:** Not declared. **Readiness documentation complete; live
integration verification pending.**

Contract proposal:
[API-12_Support_Center_Contract_Extension_Proposal.md](API-12_Support_Center_Contract_Extension_Proposal.md).

API-12-008 escalate persistence proposal (not applied):
[API-12_008_Escalate_Migration_Proposal.md](API-12_008_Escalate_Migration_Proposal.md).

---

## Readiness checkpoint — 2026-11-02

### 1. First-release scope assumption

**First Support Center release serves organization staff** using existing
authenticated identities and permission packs (`participate.support.conversation`,
`view.support.faq`, `view.support.ticket`, and where assigned `SUPPORT_AGENT` /
numbered ticket permissions). This is a **working assumption for verification
planning**, not permanent product approval.

- **Member-facing / end-customer support:** separate product decision — no
  member-only roles, routes, or permissions added in this checkpoint.
- **Platform Admin:** governance-only; tenant support operations denied in
  `SupportTicketService._require_tenant_operator` (`AuthorizationFailed`, not
  broad tenant access).
- **Site Administrator:** not seeded for support in migrations 070/071 (documented
  rationale: tickets are organization-scoped, no site column).

### 2. Repository baseline (inspected)

| Repo | Branch (tracked) | Notes |
| --- | --- | --- |
| `digitize-services` | `release/qa-smoke-20261016` | Large uncommitted working tree; preserved. |
| `digitize-ui` | `release/20261019` | Large uncommitted working tree (includes Support Center features); preserved. |

**Baseline vs last reported tests:** Phase 4 reported **43** backend / **18**
Flutter passes. Re-run after checkpoint adds one WS-behavior test:

- Backend: **44 passed**, 0 failed, 0 skipped (66 warnings).
- Flutter: **18 passed**, 0 failed, 0 skipped.

No code regressions detected in focused suites; backend count increased by one
documenting test only.

### 3. Role-and-permission matrix (staff first release)

Legend: **Y** = allowed when migration **071** (+ **070** for numbered ops) applied
and role assigned; **N** = denied by seeds/service; **P** = partial / client or
WS caveat; **—** = not applicable.

| Capability | Org Admin (070+071) | Other org staff | Site Admin | Support Agent (071) | Platform Admin | Unauthenticated |
| --- | --- | --- | --- | --- | --- | --- |
| FAQ search/read (`view.support.faq`) | Y | Only if granted | N | Y | N* | N |
| FAQ admin (`manage.support.faq`) | Y | Only if granted | N | N | N* | N |
| Create conversation (`participate…`) | Y | Only if granted | N | Y | N* | N |
| List own live-chat (`CAT-SUP-CHAT-005`) | Y | Only if granted | N | Y | N* | N |
| View ticket detail (`view.support.ticket`) | Y | Only if granted | N | Y | N* | N |
| Send customer-visible messages | Y | Only if granted | N | Y | N* | N |
| Internal notes (read/write) | N** | N** | N | Y | N* | N |
| Agent inbox / queue | N*** | N*** | N | Y | N* | N |
| Claim (auto-assign) | N*** | N*** | N | Y (+ `assign.ticket`, active profile) | N* | N |
| Assign / reassign (`assign.ticket`) | Y (070) | Only if granted | N | Y | N* | N |
| Priority (`set.ticket.priority`) | Y (070) | Only if granted | N | N**** | N* | N |
| Status transitions (accept/resolve/…) | Y (070) | Only if granted | N | Y (subset in 071) | N* | N |
| Org-wide ticket reports | Y (`generate.support.reports`) | Only if granted | N | Y | N* | N |

\* Platform Admin: no support permission seeds; service raises
`Platform governance does not include tenant support operations` for tenant ops.

\*\* Org Admin lacks `act.as.support.agent` in 071 seeds; internal notes require
agent permission in `ChatService.send_message` / list filtering.

\*\*\* Requires `view.support.agent.inbox` + `act.as.support.agent` (Support Agent role).

\*\*\*\* `SUPPORT_AGENT` role in 071 SQL does not include `set.ticket.priority` or
`classify.ticket`; Org Admin retains those via 070.

**Conversation list scope:** `list_my_conversations` filters
`created_by_user_id = principal` and `conversation_channel = LIVE_CHAT` — not
all organization tickets.

### 4. Authorization findings (backend-enforced)

| # | Check | Result |
| --- | --- | --- |
| 1 | Auth required for protected routes | Y — FastAPI `require_permission` / tenant loader on support routers. |
| 2 | Organization boundaries | Y — `_require_tenant_operator`; wrong org → `NotFoundError` (no existence leak). |
| 3 | Cross-org ticket existence | Y — same as (2) on load. |
| 4 | Internal notes on customer REST | Y — `list_messages` filters non-agent to customer-visible visibilities. |
| 5 | Internal notes on customer WS | **Fixed Phase 5** — hub skips `INTERNAL` unless `receive_internal` at connect (agent permission). Flutter filter remains defense-in-depth. |
| 6 | Customer cannot create internal notes | Y — `_validate_visibility` raises `AuthorizationFailed` without agent perm. |
| 7 | Agent-only routes reject others | Y — route deps + service checks (`AgentService`, assign permission on auto-assign). |
| 8 | Platform Admin tenant support | Y — denied at `_require_tenant_operator`. |
| 9 | Site Administrator scope | Y — not granted in 070/071 seeds. |
| 10 | Assignment eligibility | Y — auto-assign uses active `support_agent_profile`, load caps, optional category; manual assign validates assignee in org. |

**Unresolved product decisions (documented, not resolved):**

1. Dedicated end-customer principal vs staff `participate` permission.
2. WS server-side filtering of internal frames (security hardening).
3. Priority/agent pickers without list APIs (UX only).

### 5. Migration readiness (063–071) — static only, **NOT APPLIED**

| Revision | Parent | Purpose | Dependencies | Static review | ORM / SQL twin | Downgrade | Live verification | Outstanding risk |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `063_facility_billing_membership` | `062_trainer_schedule_conflict_override` | Facility billing / membership invoice schema | 062+ | Pass | Twin `063_…sql` | Drops billing tables (review FK order) | **NOT RUN** | Large API-08 billing surface |
| `064_notification_delivery_foundation` | 063 | Notification delivery infra | 063 | Pass | Twin present | Partial drop | **NOT RUN** | Chains comms migrations |
| `065_campaign_management` | 064 | Campaign tables | 064 | Pass | Twin present | Partial drop | **NOT RUN** | — |
| `066_in_app_notification_inbox` | 065 | In-app inbox | 065 | Pass | Twin present | Partial drop | **NOT RUN** | API-10 dependency |
| `067_notification_templates_and_rules` | 066 | Templates/rules | 066 | Pass | Twin present | Partial drop | **NOT RUN** | — |
| `068_push_device_tokens_and_reports` | 067 | Push device tokens | 067 | Pass | Twin present | Partial drop | **NOT RUN** | — |
| `069_billing_refunds` | 068 | **API-08 refunds** table + `billing.refund.process` | 068 | Pass | Twin present | Drops `billing.refunds`, permission | **NOT RUN** | Refund scope approval required |
| `070_support_ticket_permissions` | 069 | API-12 ticket permission seeds → `ORGANIZATION_ADMIN` | **069** | Pass | Twin + isolated test | Deletes permission rows | **NOT RUN** | Applying 070 implies 069 |
| `071_support_center_foundation` | 070 | FAQ, `ticket_message`, `support_agent_profile`, channel column, support perms/roles | **070→069 chain** | Pass | Twin + isolated test | Partial column/table drop | **NOT RUN** | Requires full chain; no FAQ seed data |

**Migration approval requirements (explicit, not satisfied by this task):**

1. Approved database target (not `digitize` / `digitize_test` / `digitize_mig_cold` without authorization).
2. Written authorization for exact revision range (e.g. 063–071).
3. Confirmation all parents exist on target.
4. Backup + documented rollback (downgrade scripts are partial — test on clone first).
5. Post-apply verification plan (schema, constraints, role_permission rows, smoke tests).

### 6. Integration verification plan (all steps **PENDING** until authorized run)

#### A. Migration verification
1. Record `alembic current` on target — **PENDING**
2. Confirm head parent chain 062→…→071 — **PENDING**
3. Apply only authorized revisions — **PENDING**
4. Verify tables: `support.faq_*`, `support.ticket_message`, `support.support_agent_profile`, `conversation_channel` — **PENDING**
5. Verify role_permission for ORG_ADMIN, SUPPORT_AGENT — **PENDING**
6. Review downgrade on clone only — **PENDING**

#### B. Staff Help + conversation workflow
| # | Role | Step | Expected | Status |
| --- | --- | --- | --- | --- |
| B1 | Staff + `view.support.faq` | Help search | Published articles only | PENDING |
| B2 | Same | Article + feedback | Feedback accepted | PENDING |
| B3 | Staff + `participate` | Contact support from FAQ | `source_entity_*` on ticket | PENDING |
| B4 | Same | Create conversation | 201, appears in CHAT-005 list | PENDING |
| B5 | Same | Send message | REST persist | PENDING |
| B6 | Same | Reload | History intact | PENDING |
| B7 | Same | Double submit UI | Single conversation | PENDING |

#### C. Agent workflow
| # | Role | Step | Expected | Status |
| --- | --- | --- | --- | --- |
| C1 | SUPPORT_AGENT + profile | Inbox / queue | Paginated lists | PENDING |
| C2 | Same | Auto-assign / assign | Assignment row | PENDING |
| C3 | Agent + `set.ticket.priority` or Org Admin | Priority change | Version++ | PENDING |
| C4 | Agent | Valid status transition | Status change | PENDING |
| C5 | Agent | Invalid transition | 4xx invalid state | PENDING |
| C6 | Agent | Internal note | REST hidden from staff list | PENDING |
| C7 | Staff participant | View messages | No internal in REST | PENDING |
| C8 | Agent | Progress with stale If-Match | 412 / refresh | PENDING |

#### D. WebSocket workflow
| # | Role | Step | Expected | Status |
| --- | --- | --- | --- | --- |
| D1 | Staff/agent | Connect with token | 101 accepted | PENDING |
| D2 | Same | Receive `message.created` | Customer-visible events | PENDING |
| D3 | Same | Disconnect / reconnect | Client backoff; REST catch-up | PENDING |
| D4 | Same | Duplicate events | UI dedupe by `message_id` | PENDING |
| D5 | Same | Logout / leave screen | Socket disposed | PENDING |
| D6 | Ops | Multi-worker | **No cross-worker fan-out** (document limitation) | PENDING |

#### E. Negative authorization
| # | Actor | Action | Expected | Status |
| --- | --- | --- | --- | --- |
| E1 | Unauthenticated | Any protected route | 401 | PENDING |
| E2 | Org A user | Org B ticket id | Not found | PENDING |
| E3 | Staff without agent | Inbox / internal send | 403 | PENDING |
| E4 | Staff | POST internal visibility | 403 | PENDING |
| E5 | Platform Admin | Tenant ticket create | 403 platform denied | PENDING |
| E6 | Site Admin | Support routes | 403 / access denied | PENDING |

#### F. Responsive UI
Mobile / tablet / desktop layouts; loading, empty, error, retry, conflict states;
internal-note styling — **PENDING** (manual/browser).

### 7. WebSocket production-readiness

**Client (`SupportConversationLiveClient`):**

- Max **5** reconnect attempts; backoff **500ms × attempt**.
- `onReconnected` triggers REST `after_message_id` refresh (authoritative).
- Deduplication by `message_id` in UI; pending send retry with idempotency keys.
- No token/URL logging in Flutter client.

**Server:**

- In-process `SupportConversationHub`; auth via WS query `access_token` (unchanged).
- Ticket access validated before accept (`_load_ticket`).
- **Limitation:** no cross-worker delivery; sticky sessions or shared pub/sub required for horizontal scale.

**Future multi-instance recommendation (not implemented):**

| Option | Pros | Cons |
| --- | --- | --- |
| Redis pub/sub (or Redis Streams) | Low latency fan-out; common pattern | Ops overhead, ACL, another SPOF without HA |
| SNS/SQS or EventBridge | Managed, fits AWS | Higher latency; more wiring |
| Sticky sessions only | No new infra | Poor failover; uneven load |

Prefer **Redis pub/sub** (or Streams) keyed by `ticket_id` with short TTL and
server-side visibility filter before publish when internal-note WS leak is fixed.

### 8. API / contract integrity (verified)

- **228** numbered APIs — `NUMBERED_COUNT` in catalog.
- **API-12-008** — not registered; no escalation table.
- **CAT-SUP-*** — remain extras; CHAT-005 list conversations documented in proposal.
- No new numbered operations; no FAQ seed content; no member-facing expansion.

### 9. Tests run (this checkpoint)

**Backend** (fixtures use mocks / SQL file parsing; `DIGITIZE_API_TEST` not required):

```bash
cd digitize-services && pytest tests/support tests/migrations/test_070_support_ticket_permissions.py tests/migrations/test_071_support_center_foundation.py tests/api/test_contract_registry.py -q
```

**44 passed, 0 failed, 0 skipped**, 66 warnings.

**Flutter:**

```bash
cd digitize-ui && flutter test test/features/support_center/support_center_pages_test.dart test/features/support_tickets/support_ticket_pages_test.dart test/features/support_conversations/support_live_client_test.dart test/features/support_agent/support_agent_controls_test.dart
```

**18 passed, 0 failed, 0 skipped**.

**Not run:** full app test suite, live API DB tests, browser E2E, WebSocket server integration, PostgreSQL with applied migrations.

### 10. Outstanding approvals and blockers

1. Authorized DB target + migration apply approval (063–071).
2. API-08 refund acceptance for 069.
3. Live integration checklist execution (sections 6A–6F).
4. Product decision: staff-only vs future member support.
5. ~~WS hardening: server-side internal-note filter~~ **Done Phase 5** (hub + connect flag).
6. API-12-008 escalation design + migration authorization — see [API-12_008_Escalate_Migration_Proposal.md](API-12_008_Escalate_Migration_Proposal.md).

### 11. Safety confirmation (this checkpoint)

- No migrations applied.
- No database created, mutated, truncated, or seeded.
- No use of `digitize_test` or `digitize_mig_cold` for mutating tests.
- No infrastructure, deploy, commit, or push.
- No outbound notifications.

---

## Phase 4 summary (2026-11-02)

Agent workspace controls, injectable WebSocket client, focused tests, and static
migration review were delivered in Phase 4. See git history / prior transcript for
file-level detail. Flutter routes: `/help`, `/support/conversations/*`,
`/support/workspace/*`.

---

## Phase 5 — WebSocket security hardening (2026-11-02)

### Root cause

`SupportConversationHub.broadcast` sent every `message.created` payload to all
sockets in a ticket room. Internal notes (`message_visibility = INTERNAL`) were
included. REST `list_messages` already filtered non-agent principals; WebSocket
did not, so any connected participant could receive internal payloads if they
ignored or bypassed the Flutter UI.

### Server-side enforcement

- Hub stores `_RoomMember(websocket, receive_internal)` per connection.
- On connect (`ws_routes.py`), `receive_internal = _is_agent(principal)` (requires
  `act.as.support.agent`). Participants with only `participate.support.conversation`
  cannot receive internal frames.
- On `broadcast`, payloads with `INTERNAL` visibility are delivered only to members
  with `receive_internal=True`. `CUSTOMER` and `AGENT_PUBLIC` reach all authorized
  room members.
- Connection authorization unchanged: JWT query param, participate or agent
  permission, `_load_ticket` org scope before accept; failures close with 4401/4403/4404
  without ticket existence leaks for cross-org.

### Connection authorization (unchanged, verified in code)

| Check | Mechanism |
| --- | --- |
| Unauthenticated | No token → close 4401 |
| No participate/agent | close 4403 |
| Cross-org / unknown ticket | `_load_ticket` → close 4404 |
| Platform tenant ops | Denied in `_require_tenant_operator` before WS accept |
| Cleanup | `disconnect` on WebSocketDisconnect; failed send removes socket |

### Regression tests

- `tests/support/test_support_ws_hub.py` — hub delivery to customer vs agent sockets (5 tests).
- `tests/support/test_support_ws_routes.py` — mocked WS connect auth and `receive_internal` flag (5 tests).
- `tests/support/test_support_center.py` — `test_internal_message_ws_delivery_filtered_by_hub`, `test_list_messages_hides_internal_for_participant`.

### Tests run (Phase 5)

```bash
cd digitize-services && pytest tests/support tests/migrations/test_070_support_ticket_permissions.py tests/migrations/test_071_support_center_foundation.py tests/api/test_contract_registry.py -q
```

**55 passed**, 0 failed, 0 skipped (66 warnings).

```bash
cd digitize-ui && flutter test test/features/support_center/support_center_pages_test.dart test/features/support_tickets/support_ticket_pages_test.dart test/features/support_conversations/support_live_client_test.dart test/features/support_agent/support_agent_controls_test.dart
```

**18 passed**, 0 failed, 0 skipped. No Flutter code changes in Phase 5; client-side visibility filter remains defense-in-depth only.

### Architecture limits (unchanged)

- In-process hub only; **no cross-worker** fan-out (future broker required for multi-worker).
- Auth token still in query string (documented risk); not changed in this phase.

### Remaining authorization uncertainty

- Cross-org WS rejection relies on the same `_load_ticket` path as REST; not exercised against a live database in this phase.
- Staff-without-agent permission cannot send or receive internal notes over WS or REST; verified in unit tests only.

### Live verification

WebSocket server integration, browser, and PostgreSQL tests **not run**.

### Safety

No migrations applied. No database mutations. No infra/deploy/commit/push.
Official numbered API count remains **228**.
