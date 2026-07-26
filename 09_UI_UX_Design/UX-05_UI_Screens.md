# UX-05 UI Screens

**Document ID:** UX-05  
**Document Name:** UI Screens  
**Company:** OreeOn Technologies Pvt. Ltd.  
**Product:** Digitize  
**Document Type:** UI/UX Design Documentation  
**Client Technology:** Flutter / Web  
**Backend Technology:** FastAPI  
**Database Engine:** PostgreSQL  
**Authentication:** JWT
**Version:** 0.1
**Status:** Review Complete — Pending blockers (see `docs/09_UI_UX_Design/ISSUES_TO_OPEN.md`)
**Owner:** Product Design / UI/UX Architecture  
**Reviewer:** Product Management / Business Analysis / Solution Architecture / Frontend Architecture / API Architecture / Integration Architecture / Security Architecture / QA  
**Dependencies:** UI-00, UX-01, UX-02, UX-03, UX-04, API-00 to API-26, IC-00 to IC-17  
**Last Updated:** 2026-07-26
**Review Completed By:** Product Design (reviewer group)

---

# 1. Document Metadata

| Attribute | Value |
|---|---|
| Document ID | UX-05 |
| Output File | UX-05_UI_Screens.md |
| Status | Review Complete — Pending blockers (see `docs/09_UI_UX_Design/ISSUES_TO_OPEN.md`) |
| Governing Standard | UI-00_UI_UX_Standards.md |

### 1.1 Review Summary

- Review completion date: 2026-07-26.
- Work completed: All MVP screen specs reviewed, implementation-ready screens annotated, PR checklist and issue templates added.
- Blockers recorded: Auth API (API-03), Payments/Provider rules (API-08 / IC-04), Brand tokens (UX-04), UI-00 freeze signoff. See `docs/09_UI_UX_Design/ISSUES_TO_OPEN.md`.
- Remaining TBD screens: `UI-CUS-003`, `UI-WLK-001`, `UI-PAY-001` (owners assigned in matrix where known).


---

# 2. Purpose

This document defines the implementation-ready UI screen specification baseline for Digitize.

It translates approved UX strategy, user flows, wireframes, design-system rules, API behavior, Integration Contract behavior, roles, permissions, tenant scope, validations, states, and acceptance criteria into screen-level UI contracts for frontend implementation and QA validation.

---

# 3. Scope

In scope:

- Screen inventory.
- Screen IDs.
- Screen purpose.
- Roles and permissions.
- Organization, Facility, and Site scope.
- Preconditions.
- Entry points.
- Exit paths.
- Layout regions.
- Sections.
- Fields.
- Controls.
- Actions.
- Data sources.
- API mappings.
- Integration mappings.
- Validations.
- Lifecycle states.
- Loading, empty, error, retry, offline, conflict, async, and success states.
- Responsive behavior.
- Accessibility.
- Audit-triggering actions.
- Acceptance criteria.
- Traceability.

Out of scope:

- Flutter source code.
- Web source code.
- Backend implementation.
- Database schema definitions.
- Provider SDK implementation.

---

# 4. Source Documents

| Source Area | Documents | Usage |
|---|---|---|
| UI Standards | UI-00 | Screen specification rules |
| UX Strategy | UX-01 | UX goals and strategy |
| User Flows | UX-02 | Flow and transition behavior |
| Wireframes | UX-03 | Low-fidelity structure |
| Design System | UX-04 | Components and visual rules |
| API Collections | API-01 to API-26 | Data, actions, states, errors, and permissions |
| Integration Contracts | IC-01 to IC-17 | Auth, tenant, payment, file, report, retry, security, observability, readiness |

---

# 5. Screen ID Standard

Screen ID format:

```text
UI-<DOMAIN>-<NUMBER>
```

Examples:

| Screen ID | Screen |
|---|---|
| UI-AUTH-001 | Login |
| UI-TEN-001 | Context Selection |
| UI-CUS-001 | Customer List |
| UI-MEM-001 | Membership Detail |
| UI-PAY-001 | Payment Status |

Screen IDs shall remain stable once frozen.

---

# 6. Screen Specification Template

Every screen specification shall include:

- Screen ID.
- Screen name.
- Business purpose.
- Primary roles.
- Supporting roles.
- Permission rules.
- Tenant scope.
- Preconditions.
- Entry points.
- Exit paths.
- Layout regions.
- Sections.
- Fields.
- Controls.
- Actions.
- Data sources.
- API mappings.
- Integration mappings.
- Validations.
- States.
- Responsive behavior.
- Accessibility requirements.
- Audit-triggering actions.
- Acceptance criteria.
- Traceability owner.

---

# 7. Global Screen Inventory

| Domain | Screen Group | Representative Screen IDs |
|---|---|---|
| Authentication | Login, reset, session expiry | UI-AUTH-001 to UI-AUTH-009 |
| Tenant Context | Organization, Facility, Site selection | UI-TEN-001 to UI-TEN-009 |
| Home | Role-aware landing and work queues | UI-HOME-001 to UI-HOME-009 |
| Platform Admin | Platform settings and master data | UI-PLT-001 to UI-PLT-099 |
| Organization / Facility / Site | Tenant hierarchy setup and settings | UI-ORG-001 to UI-SITE-099 |
| Identity | Users, roles, permissions, sessions | UI-IAM-001 to UI-IAM-099 |
| Customer | Customer search, profile, documents | UI-CUS-001 to UI-CUS-099 |
| Membership | Plans, purchase, lifecycle | UI-MEM-001 to UI-MEM-099 |
| Attendance / Walk-in | Check-in, check-out, walk-in | UI-ATT-001 to UI-WLK-099 |
| Trainer / Activity / Batch | Trainer, schedule, batches, calendar | UI-TRN-001 to UI-BAT-099 |
| Billing / Payment | Invoice, payment, refund, reconciliation | UI-BIL-001 to UI-PAY-099 |
| Subscription / License | SaaS subscription and license | UI-SUB-001 to UI-LIC-099 |
| Notification / Campaign | Templates, campaigns, delivery | UI-NOT-001 to UI-CMP-099 |
| Reports / Analytics | Reports, dashboards, exports | UI-RPT-001 to UI-ANA-099 |
| Support | Tickets, comments, attachments, SLA | UI-SUP-001 to UI-SUP-099 |
| Audit / Security | Audit search, events, investigations | UI-AUD-001 to UI-SEC-099 |
| Reference | Lookup and reference configuration | UI-REF-001 to UI-REF-099 |

## 7.1 MVP Screen Specification Matrix

| Screen ID | Screen Name | Primary Roles | Key Fields / Controls | Primary Actions | Required States |
|---|---|---|---|---|---|
| UI-AUTH-001 | Login | All users | Username, password, forgot password link | Sign in | Loading, invalid credentials, locked, success |
| UI-TEN-001 | Context Selection | Multi-context users | Organization selector, Facility selector, Site selector | Continue, cancel | Loading, empty, unauthorized, invalid context |
| UI-HOME-001 | Role-Aware Home | All authenticated users | Context summary, work queues, shortcuts, alerts | Open workflow, switch context | Loading, empty queues, denied shortcuts |
| UI-CUS-001 | Customer List | Site Staff, Facility Manager | Search, filters, status, customer rows | Search, create, open profile | Loading, empty, no results, restricted |
| UI-CUS-002 | Customer Profile | Site Staff, Facility Manager | Profile summary, contact, consent, documents, notes | Edit, upload document, change status | Loading, masked data, duplicate, inactive |
| UI-MEM-001 | Membership Detail | Site Staff, Facility Manager | Plan, status, dates, entitlement, lifecycle history | Renew, freeze, resume, cancel | Pending, active, frozen, expired, conflict |
| UI-ATT-001 | Attendance Check-in | Site Staff | Customer lookup, eligibility result, capacity status | Check in, override where permitted | Eligible, ineligible, full capacity, denied |
| UI-WLK-001 | Walk-in Registration | Site Staff | Customer details, visit type, payment association | Register, collect payment | Validation, payment pending, success, failure |
| UI-TRN-001 | Trainer Calendar | Trainer, Facility Manager | Date controls, trainer filter, activity filter, sessions | Create session, reschedule, cancel | Loading, conflict, capacity warning |
| UI-BIL-001 | Invoice Detail | Finance User, Site Staff | Invoice summary, line items, tax, status, receipts | Finalize, collect payment, cancel | Draft, finalized, paid, void, error |
| UI-PAY-001 | Payment Status | Finance User, Site Staff, Customer where applicable | Amount, provider status, reference, receipt | Retry, verify, refund where permitted | Pending, success, failed, timeout, reconciliation required |
| UI-SUB-001 | Subscription Status | Organization Owner, Platform Admin | Plan, billing cycle, license count, entitlement | Renew, cancel, assign license | Active, suspended, expired, paywall |
| UI-NOT-001 | Campaign Detail | Campaign User, Facility Manager | Audience, template, channel, schedule, delivery status | Activate, pause, cancel, retry | Draft, scheduled, active, paused, failed |
| UI-RPT-001 | Report Export | Manager, Finance, Support | Report, parameters, format, status | Generate, download, retry, cancel | Queued, running, ready, failed, expired |
| UI-SUP-001 | Ticket Detail | Customer, Staff, Support User | Summary, priority, comments, attachments, SLA | Reply, assign, escalate, close | Open, pending, escalated, closed, reopened |
| UI-AUD-001 | Audit Search | Security, Platform Admin, Support | Actor, event, entity, date filters, results | Search, view detail, export where permitted | Loading, empty, restricted, export pending |

## 7.3 Example: UI-AUTH-001 (Login) — Full Screen Specification

This example is a complete, implementation-ready screen specification that follows the template in Section 6. It is provided as a normative example for frontend, QA, and integration teams to follow when authoring other screen specifications.

- Screen ID: UI-AUTH-001
- Screen name: Login
 - Status: Ready — Product Design / Identity and Access Owner
- Business purpose: Authenticate a user and establish a secure, traceable session. After successful authentication the user is routed to context selection or a role-aware home depending on account configuration.
- Primary roles: All authenticated users (Platform Administrator, Organization Owner, Facility Manager, Site Staff, Trainer, Finance User, Support User, Customer where applicable)
- Supporting roles: None
- Permission rules: No pre-existing tenant permission required to authenticate; post-auth tenant and role availability are enforced by backend APIs (API-02, API-23). UI must not assume authorization based on visible elements.
- Tenant scope: No tenant selected at login. Tenant selection occurs after successful authentication if the user has access to multiple organizations/facilities/sites.
- Preconditions: Network connectivity; authentication service available; rate-limit quota not exceeded for client IP/session.
- Entry points: Deep link to login, app cold start, session expired flow, forced logout flow.
- Exit paths: Successful authentication → Context Selection (UI-TEN-001) or Role-Aware Home (UI-HOME-001). Failed authentication → show user-safe error and allow retry or password recovery.
- Layout regions:
	- Page header: Product name and optional branding
	- Form region: Username input, Password input, Remember-me (optional), Sign-in button
	- Secondary links: Forgot password, Help, Contact support
	- Feedback region: Field-level validation, form-level error banner, correlation/request reference on demand for support

- Sections:
	- Credential entry
	- Recovery links
	- Session and security notices (e.g., session expiry warnings when reached from expired-session flow)

- Fields:
	- `username` (string) — required. Accepts email or username per API-03. Validation: non-empty, trimmed, max length 254, email-format hint when `@` present.
	- `password` (string) — required. Validation: non-empty, min 8 characters (frontend hint only; backend enforces policy). Input type: password (masked). Provide toggle for reveal/hide.
	- `remember_me` (boolean) — optional. Hint: persists session per product session policy; backend enforces token lifetime.

- Controls / Actions:
	- `Sign In` (primary) — submits credentials to `POST /auth/login` (API-03). While in-flight, show inline loading state and disable inputs. Prevent duplicate submissions via button disable and idempotency token on retry attempts.
	- `Forgot password` (secondary link) — navigates to `UI-AUTH-002` (Password Reset Request).
	- `Help / Contact support` (tertiary) — shows support contact and correlation guidance.

- Data sources / API mappings:
	- Authenticate call: `POST /auth/login` (API-03). Expected success: 200 + session token, refresh token, user profile, available roles and tenant list (if included in payload). Failure cases: 401 invalid credentials, 423 account locked, 429 rate limit, 5xx provider error.
	- After success: call `GET /auth/me` (or included profile response) to obtain effective roles and authorized organizations (API-03 / API-02). Route to `UI-TEN-001` when multiple contexts exist.

- Integration mappings:
	- Integration contract: IC-02 for session lifecycle, token refresh, and forced logout behavior.
	- Observability: include correlation ID in logs and show user-safe support reference when requested.

- Validations and Rules:
	- Client-side: required fields, trimming, simple email-format hint. Do not enforce complex password policy solely on client.
	- Server-side: show server-provided validation messages mapped to field-level or banner messages. Map error codes to user-safe text using the Error and Recovery Standard (UI-00 / API-19).
	- Rate-limit handling: show friendly throttling message with retry-after where provided by API.
	- Account lock: show locked state with instructions to contact support and optional automated unlock flow reference.

- State Matrix (required states):
	- Initial: empty form
	- Loading: disable inputs, show progress on `Sign In`
	- Validation error: field-level messages (e.g., missing username)
	- Authentication failed: prominent banner with user-safe message; do not reveal which field was incorrect beyond general guidance
	- Account locked: banner with support path and correlation reference
	- Rate-limited: banner with retry window
	- Success: transition to Context Selection or Home

- Accessibility:
	- Inputs must have explicit `label` elements.
	- Error messages must be programmatically associated with inputs (aria-describedby or equivalent).
	- Keyboard-first navigation and logical tab order.
	- Visible focus states for all interactive controls.
	- Password reveal control must be accessible and announce state changes.
	- Color not the only indicator for errors.

- Security Requirements:
	- Password must be masked by default and not stored in client logs.
	- Use secure transport (HTTPS) for all auth calls.
	- Implement client-side rate-limit protection UI feedback; backend enforces server-side limits.
	- Do not display raw tokens or stack traces. Show only user-safe support reference.
	- Implement CSRF protections where applicable for web clients per IC-02 guidance.

- Audit and Observability:
	- Emit `auth.login.attempt` and `auth.login.success` / `auth.login.failure` audit events to API-13 where available.
	- Where feasible, surface a short correlation ID on-screen in the error banner for support reference.

- Notifications:
	- On account lock event, trigger notification to support or account owner per IC-05/IC-11 as defined by Integration Contracts (email or admin alert). UI displays only user-safe guidance.

- Multi-tenant Behavior:
	- No tenant selection at login. After success, if multiple organizations/facilities/sites are authorized, route to `UI-TEN-001` and preserve authentication context.

- Performance and Scalability:
	- Keep login payloads minimal. Defer heavy profile loading to a follow-up `GET /auth/me` where practical.

- Acceptance Criteria (pass/fail):
	- Given valid credentials, `Sign In` returns a session and navigates to `UI-TEN-001` or `UI-HOME-001` within 3s under nominal conditions.
	- Invalid credentials show a single user-safe banner message and do not reveal sensitive details.
	- Account lock state shows support guidance and emits an audit event.
	- All interactive controls are keyboard accessible and labelled for screen readers.
	- Rate-limit state displays retry-after when provided.

- QA Test Cases (representative):
	- Submit empty form: expect field-required messages.
	- Submit invalid email-format username: show inline hint where relevant.
	- Submit incorrect credentials repeatedly until lock: expect incremental messages and final locked banner.
	- Network failure during login: show retryable failure banner and allow retry.
	- Successful login when multiple tenant contexts: route to `UI-TEN-001` and show authorized contexts.

- Traceability owner: Product Design / Identity and Access Owner

This example should be used as the canonical pattern for completing other screen specifications in `UX-05`.

## Screen Specification Checklist

Use this checklist at the top of every screen specification to ensure implementation-readiness and freeze readiness:

- [ ] Screen ID and name present
- [ ] Business purpose defined
- [ ] Primary and supporting roles listed
- [ ] Permission rules and tenant scope defined
- [ ] Preconditions and entry/exit paths defined
- [ ] Layout regions and sections defined
- [ ] Fields and controls defined with validation rules
- [ ] API mappings and integration contracts listed
- [ ] State matrix (loading, empty, error, retry, offline, conflict) included
- [ ] Accessibility requirements included
- [ ] Security and privacy notes included
- [ ] Audit-triggering actions identified
- [ ] Acceptance criteria and QA test cases included
- [ ] Traceability owner assigned


---

## 7.4 Implementation-Ready Screens: MVP Examples

The following screens are provided as fully-detailed, implementation-ready specifications following the `UI-AUTH-001` example. Use these as canonical templates for other MVP screens.

### UI-CUS-001 — Customer List (Implementation-Ready)

- Screen ID: UI-CUS-001
- Screen name: Customer List
 - Status: Ready — Product Design / Customer Domain Owner
- Business purpose: Provide a fast, permission-aware interface for site staff and facility managers to search, filter, and access customer records for operational tasks (check-in, payments, enrollment, communications). Supports create-capture and duplicate detection.
- Primary roles: Site Staff, Facility Manager
- Supporting roles: Trainer, Support User
- Permission rules: Read access to customer list requires `customer.read` permission scoped to Site or Facility per API-04. Create requires `customer.create`. Masked fields when `customer.restricted_view` not granted.
- Tenant scope: Organization / Facility / Site (default to current Site context)
- Preconditions: Tenant context selected (UI-TEN-001); network connectivity; customer index available.
- Entry points: Role-Aware Home quick link, Attendance workflow, Customer search deep link.
- Exit paths: Open `UI-CUS-002` Customer Profile; Create → `UI-CUS-003` Create Customer flow; Select for attendance → `UI-ATT-001`.
- Layout regions:
	- Page header: Title, context summary, primary `Create Customer` action
	- Search bar: Free-text search with type-ahead
	- Filter panel: Status, membership status, tags, last-visited, custom attributes
	- Result list/table: Rows with summary fields, primary action, secondary menu
	- Bulk action bar: Appears when rows selected
	- Pagination / infinite scroll control

- Fields (per row):
	- `customer_id` (masked in UI when restricted)
	- `full_name`
	- `primary_contact`
	- `membership_status`
	- `last_visit_date`
	- `tags`
	- `row_actions`: Open profile, Quick check-in (where permitted), More menu (edit, documents, notes)

- Controls / Actions:
	- `Search` (primary): queries `GET /customers` (API-04) with q, filters, pagination.
	- `Create Customer` (primary): opens create flow.
	- `Row Open` (open profile): navigates to `UI-CUS-002`.
	- `Quick Check-in` (where permitted): calls `POST /attendance/checkin` (API-06) with customer reference; fallback to `UI-ATT-001` if additional input required.
	- `Bulk Actions`: Export, Tagging, Bulk assign (where permitted) — call appropriate APIs with job status tracking.

- Data sources / API mappings:
	- `GET /customers?q={q}&filters...` (API-04) — supports pagination, sort, permission-aware masking.
	- `POST /customers` (API-04) — create.
	- `POST /attendance/checkin` (API-06) for quick check-in where permitted.

- Validations and Rules:
	- Search hints: throttle client-side to avoid spamming API (type-ahead debounce 300ms).
	- Empty search: show recent or suggested customers if allowed.
	- Masked fields: show `Restricted` label where permission missing, provide support reference for access requests.
	- Duplicate detection: when creating, surface probable duplicates and require confirmation to create.

- State Matrix:
	- Loading: skeleton rows matching table structure
	- Empty: contextual empty state with `Create Customer` CTA
	- No results: suggest alternative filters
	- Partial results: show count and pagination
	- Authorization Denied: safe denied view with contact support
	- Retryable Failure: show retry CTA and correlation reference

- Accessibility:
	- Table headers use proper semantic markup.
	- Row actions are keyboard-accessible and have accessible names.
	- Filters announce applied state to assistive tech.

- Security & Privacy:
	- Mask PII when permission absent. Do not surface raw IDs in query strings or telemetry.
	- Export requires elevated permission and audit event emission.

- Audit & Observability:
	- Emit `customer.list.view` audit event including actor and tenant context when export or bulk actions initiated.

- Acceptance Criteria:
	- Search returns results within 2s under nominal conditions for typical page sizes.
	- Masked fields remain masked for users without permission.
	- Quick check-in triggers attendance API and reflects success state inline.

- QA Test Cases (sample):
	- Search with filters: expect correct results and counts.
	- Row action keyboard navigation: open profile.
	- Create customer with duplicate: ensure duplicate dialog appears and blocks accidental create.

- Traceability owner: Product Design / Customer Domain Owner

---

### UI-MEM-001 — Membership Detail (Implementation-Ready)

- Screen ID: UI-MEM-001
- Screen name: Membership Detail
 - Status: Ready — Product Design / Membership Domain Owner
- Business purpose: Display membership plan, lifecycle state, entitlements, and available lifecycle actions (renew, freeze, resume, cancel). Provide clear status and actionable pathways for staff and managers.
- Primary roles: Site Staff, Facility Manager
- Supporting roles: Finance User, Support User
- Permission rules: Read membership requires `membership.read`; lifecycle mutate actions require `membership.manage` scoped to Facility or Organization as per API-24.
- Tenant scope: Organization / Facility / Site
- Preconditions: Customer exists; membership linked to customer; membership lifecycle metadata available from API-24.
- Entry points: From Customer Profile (`UI-CUS-002`), Membership list, work queue.
- Exit paths: Return to Customer Profile, open Billing/Invoice (UI-BIL-001), launch Membership purchase flow.
- Layout regions:
	- Header: Membership ID, status badge, primary lifecycle action
	- Summary panel: Plan name, start/end dates, entitlements, assigned facility/site
	- Timeline: lifecycle history entries (activated, renewed, frozen, resumed, cancelled)
	- Actions panel: Renew, Freeze, Resume, Cancel, Transfer (where permitted)
	- Audit / Notes region: recent audit events and internal notes

- Fields:
	- `membership_id`
	- `plan_name`
	- `status` (Draft, Pending, Active, Frozen, Expired, Cancelled)
	- `start_date`, `end_date`
	- `entitlements` (sessions, access types)
	- `payment_reference` (masked where required)

- Controls / Actions:
	- `Renew` — initiates renewal flow and calls `POST /memberships/{id}/renew` (API-24). Multi-step if payment required.
	- `Freeze` — calls `POST /memberships/{id}/freeze` with reason; validates eligibility.
	- `Resume` — calls `POST /memberships/{id}/resume`.
	- `Cancel` — destructive-confirmation dialog; calls `POST /memberships/{id}/cancel` and emits audit event.
	- `View invoice` — navigates to `UI-BIL-001` if invoice exists.

- Data sources / API mappings:
	- `GET /memberships/{id}` (API-24) — membership detail and lifecycle history.
	- Mutation endpoints: `POST /memberships/{id}/renew`, `/freeze`, `/resume`, `/cancel` (API-24).

- Validations and Rules:
	- Eligibility checks performed server-side; UI must display server-provided reason when action rejected.
	- Freeze/resume constraints (min/max duration) surfaced as help text when available.
	- Cancel requires explicit confirmation and optional staff note.

- State Matrix:
	- Loading: skeleton detail panels
	- Pending mutation: show inline spinner and disable conflicting actions
	- Conflict: show latest state and provide refresh/override guidance where allowed
	- Success: update status and timeline, show transient toast and audit note
	- Failure: show actionable error with next steps and support reference

- Accessibility:
	- Action dialog must be keyboard-accessible and annouce confirmations to screen readers.

- Security & Privacy:
	- Mask payment references and PII as per permission.
	- Lifecycle actions emit audit events with actor and tenant context.

- Audit & Observability:
	- Emit `membership.action` events on lifecycle changes to API-13.

- Acceptance Criteria:
	- Lifecycle actions reflect server state consistently and update UI within 2s of backend confirmation.
	- Ineligible action attempts show server message and do not change state.

- QA Test Cases (sample):
	- Freeze an active membership: verify timeline entry and entitlement pause.
	- Attempt to resume when ineligible: verify server message displayed.

- Traceability owner: Product Design / Membership Domain Owner

---

### UI-ATT-001 — Attendance Check-in (Implementation-Ready)

- Screen ID: UI-ATT-001
- Screen name: Attendance Check-in
 - Status: Ready — Product Design / Operations Domain Owner
- Business purpose: Fast-access check-in for site staff to validate eligibility, enforce capacity, associate payment (if walk-in), and record attendance, with minimal latency and clear recovery for conflicts.
- Primary roles: Site Staff
- Supporting roles: Facility Manager, Support User
- Permission rules: `attendance.checkin` required; override requires `attendance.override` and triggers audit and maybe manager approval per policy.
- Tenant scope: Site
- Preconditions: Tenant context selected; user has check-in permission; realtime occupancy and capacity data available.
- Entry points: Home quick-check-in, Customer List quick-check-in, Walk-in registration flow.
- Exit paths: Success → inline confirmation and optional receipt; Failure → show reason and next steps; Override flow → manager approval or capture reason.
- Layout regions:
	- Quick search / scan area: barcode/QR scan or free-text customer lookup
	- Eligibility result panel: shows entitlement, membership status, blacklists, holds, capacity
	- Actions: `Check In`, `Override` (if permitted), `Collect Payment` (if walk-in), `Create Customer` when not found
	- Audit/notes: capture staff notes for override or correction

- Fields:
	- `lookup_input` (string / scan) — supports barcode, QR, phone, member ID
	- `eligibility_status` — enum (eligible, ineligible, pending_verification)
	- `capacity_status` — available seats vs capacity

- Controls / Actions:
	- `Check In` — `POST /attendance/checkin` (API-06) with idempotency token; returns success or conflict.
	- `Override` — prompts for reason and, if required, manager approval step or `POST /attendance/override`.
	- `Collect Payment` — navigates to `UI-WLK-001` or inline payment initiation calling API-08 where walk-in payment applies.

- Data sources / API mappings:
	- `GET /attendance/eligibility?customerId=...` (API-06)
	- `POST /attendance/checkin` (API-06)
	- `POST /attendance/override` (API-06) when permitted

- Validations and Rules:
	- Idempotency: prevent duplicate check-ins via client-side temporary lock and backend idempotency token.
	- Capacity enforcement: if full, show waitlist or deny; allow override only when permitted and audited.
	- Eligibility checks: show reasons (membership expired, not enrolled, blacklisted) and actionable next steps.

- State Matrix:
	- Idle: ready for scan/lookup
	- Lookup loading: show spinner and disable check-in until eligibility returned
	- Eligible: show `Check In` positive state
	- Ineligible: show clear guidance and possible next steps
	- Capacity full: show capacity message and alternative flows
	- Check-in pending: spinner and success/failure outcome
	- Conflict: show latest state and allow refresh or manual correction

- Accessibility:
	- Provide large, touch-friendly controls for quick operation on mobile devices.
	- Scanning input accessible and fallback to text entry.

- Security & Privacy:
	- Limit PII shown on quick results; provide link to full profile for authorized users.
	- Overrides and corrections require audit events and may require elevated permission.

- Audit & Observability:
	- Emit `attendance.checkin` and `attendance.override` events to API-13 including actor, tenant, and request correlation.

- Acceptance Criteria:
	- Check-in completes within 1.5s under nominal local network conditions for common operations.
	- Duplicate check-in is prevented and reported with an actionable message.
	- Override actions are audited and require explicit reason capture.

- QA Test Cases (sample):
	- Successful check-in using scan and text lookup.
	- Attempt check-in when capacity full: expect deny or override flow.
	- Duplicate submission prevention: rapid repeated taps result in a single check-in.

- Traceability owner: Product Design / Operations Domain Owner

---

---

### UI-CUS-002 — Customer Profile (Implementation-Ready)

- Screen ID: UI-CUS-002
- Screen name: Customer Profile
 - Status: Ready — Product Design / Customer Domain Owner
- Business purpose: Provide a complete view of a customer's profile, consents, documents, membership entitlements, activity history, and quick actions for operational tasks while enforcing permission-based masking and audit controls.
- Primary roles: Site Staff, Facility Manager
- Supporting roles: Trainer, Support User, Finance User
- Permission rules: `customer.read` required; sensitive fields (PII, payment refs) require `customer.restricted_view`. Edit requires `customer.edit`. Document access may require additional permissions per IC-06.
- Tenant scope: Organization / Facility / Site
- Preconditions: Customer selected from list; tenant context set; backend profile available via API-04.
- Entry points: Customer list row open, QR/ID scan, deep link
- Exit paths: Back to Customer List, Open Membership (UI-MEM-001), Open Billing (UI-BIL-001), Start Attendance (UI-ATT-001)
- Layout regions:
	- Header: Customer name, status badges (active, restricted), primary actions (Edit, Check-in shortcut)
	- Summary panel: contact, emergency contact, identifiers (masked where needed)
	- Membership panel: current memberships & entitlements
	- Activity timeline: recent attendance, purchases, notes
	- Documents & Attachments panel: upload, view, scan status
	- Internal notes & audit panel (permissioned)

- Fields / Key Data:
	- `customer_id` (masked when restricted)
	- `full_name`, `preferred_name`
	- `primary_contact` (phone/email)
	- `membership_summary`
	- `consent_status` (communications, data processing)
	- `documents` (list with scan/validation state)

- Controls / Actions:
	- `Edit Profile` — navigates to edit form; calls `PUT /customers/{id}` (API-04).
	- `Upload Document` — calls `POST /customers/{id}/documents` (IC-06) with progress and scan status.
	- `Open Membership` — navigates to `UI-MEM-001`.
	- `Quick Check-in` — calls `POST /attendance/checkin` (API-06) when permitted.
	- `Send Notification` — opens campaign/notification flow for the customer (IC-05).

- Data sources / API mappings:
	- `GET /customers/{id}` (API-04) — profile, consents, linked memberships, documents metadata.
	- `GET /memberships?customerId={id}` (API-24) — membership list preview.
	- `POST /customers/{id}/documents` (IC-06) — upload and scan initiation.

- Validations and Rules:
	- Edits are validated server-side; show field-level messages.
	- Consent toggles should not change historical records; changes require audit note.
	- Document uploads validate file types and size limits; quarantined files flagged and inaccessible until cleared.

- State Matrix:
	- Loading: skeleton for panels
	- Masked: show `Restricted` placeholders where permission missing
	- Empty: explicit CTAs (create membership, upload document)
	- Error: field-level or panel-level messages with support reference

- Accessibility:
	- Headings represent panel sections; document links have accessible labels; tab order logical.

- Security & Privacy:
	- Mask PII when permission absent; redact in exports.
	- Document downloads produce temporary signed URLs per IC-06 and respect TTL and permissions.

- Audit & Observability:
	- Emit `customer.view`, `customer.edit`, and `customer.document.upload` audit events to API-13 with tenant and actor context.

- Acceptance Criteria:
	- Profile loads within 2s under nominal conditions.
	- Sensitive fields masked correctly for roles without `customer.restricted_view`.
	- Upload lifecycle shows scanning and final state accurately.

- QA Test Cases (sample):
	- Edit profile with invalid phone: expect field-level validation.
	- Upload a quarantined document: verify UI shows quarantined state and prevents download.

- Traceability owner: Product Design / Customer Domain Owner

---

### UI-MEM-002 — Membership Purchase (Implementation-Ready)

- Screen ID: UI-MEM-002
- Screen name: Membership Purchase
 - Status: Ready — Product Design / Commercial Domain Owner
- Business purpose: Support purchase of membership plans, validating eligibility, collecting payment if required, applying promotions, and returning an entitlement record with clear states for pending, success, failure, and reconciliation.
- Primary roles: Site Staff, Facility Manager, Customer (self-service where enabled)
- Supporting roles: Finance User, Support User
- Permission rules: `membership.purchase` required for staff-assisted purchases; self-service purchases available via customer-facing flows with appropriate identity verification.
- Tenant scope: Organization / Facility / Site
- Preconditions: Customer selected or identified; plan available; pricing and tax data loaded from API-08/API-14.
- Entry points: From Customer Profile, Membership list, Sales workflow
- Exit paths: Success → Membership Detail (UI-MEM-001); Failure → show retry or contact support; Pending payment → Payment Status (UI-PAY-001)
- Layout regions:
	- Header: Plan summary and price
	- Purchase form: buyer (customer selection), billing details, promo code, payment method
	- Summary panel: tax, discounts, final amount
	- Actions: `Purchase` primary, `Cancel` secondary

- Fields:
	- `plan_id`, `plan_options` (add-ons)
	- `customer_id` (required for staff-assisted)
	- `promo_code` (optional) — validate via `POST /promotions/validate`
	- `payment_method` — brand, last4 masked, or new payment entry

- Controls / Actions:
	- `Purchase` — calls `POST /memberships/purchase` (API-05) which may return `accepted` (async), `pending_payment`, `success`, or `failure`.
	- `Apply Promo` — validate and apply discount to summary.
	- `Collect Payment` — invoke payment provider integration per IC-04 when immediate payment required.

- Data sources / API mappings:
	- `GET /plans/{id}` (API-05)
	- `POST /memberships/purchase` (API-05)
	- Payment: `POST /payments/initiate` (API-08) and provider callbacks per IC-04

- Validations and Rules:
	- Eligibility validated server-side; display reasons if ineligible.
	- Payment flow may be synchronous (immediate) or asynchronous (redirect/provider) — UI must support both.
	- Promo validation returns expiry and applicability; show messaging when promo invalid.

- State Matrix:
	- Initial: form ready
	- Validating: disable purchase while validating promo/payment
	- Pending: show queued/pending state with correlation reference
	- Success: navigate to `UI-MEM-001` and show entitlement
	- Failure: show actionable error and offer retry or manual assistance

- Accessibility:
	- Form fields labelled; payment fields follow PCI-safe practices and do not persist sensitive data.

- Security & Privacy:
	- Payment data handled via provider tokens; do not transmit raw card details to backend unless PCI scope is approved.
	- Emit audit event for purchase and payment initiation.

- Audit & Observability:
	- Emit `membership.purchase.initiated`, `membership.purchase.completed`, `payment.initiated`, `payment.completed` events to API-13 and payment reconciliation logs.

- Acceptance Criteria:
	- Purchase completes or enters a reconciliable pending state consistently and presents clear next steps to the user.
	- Promo codes apply correctly and validation messages are clear.

- QA Test Cases (sample):
	- Purchase with valid card: expect success and membership entitlement.
	- Purchase with declined card: show provider error and allow retry.

- Traceability owner: Product Design / Commercial Domain Owner

---

### UI-BIL-001 — Invoice Detail (Implementation-Ready)

- Screen ID: UI-BIL-001
- Screen name: Invoice Detail
 - Status: Ready — Product Design / Finance Domain Owner
- Business purpose: Display invoice information, line items, taxes, payment status, receipts, and actions such as finalize, void, or issue refund where permitted. Support reconciliation and export for finance users.
- Primary roles: Finance User, Site Staff
- Supporting roles: Support User, Organization Owner
- Permission rules: `invoice.view` required; financial actions require `invoice.manage` and may be limited to Organization-level roles.
- Tenant scope: Organization / Facility
- Preconditions: Invoice exists in system; invoice data available via API-08.
- Entry points: Billing list, Membership purchase flow, Payment flow
- Exit paths: Back to invoice list, Open Payment Status (UI-PAY-001), Initiate refund flow
- Layout regions:
	- Header: Invoice number, status badge, primary actions (Finalize, Refund)
	- Summary: Customer, invoice date, due date, total
	- Line items: description, qty, unit price, tax
	- Payments & receipts: list of payments applied
	- Notes & audit: internal notes, reconciliation flags

- Fields:
	- `invoice_id`, `status` (Draft, Finalized, Paid, Partially Paid, Voided)
	- `line_items[]`
	- `tax_summary`
	- `payments[]` (masked payment references)

- Controls / Actions:
	- `Finalize` — call `POST /invoices/{id}/finalize` (API-08). Emits audit; may create payable record.
	- `Record Payment` — navigates to payment initiation or attaches existing payment record.
	- `Issue Refund` — calls `POST /payments/{paymentId}/refund` (API-08) with confirmation.
	- `Export PDF` — generates and downloads signed PDF per IC-07 with audit event.

- Data sources / API mappings:
	- `GET /invoices/{id}` (API-08)
	- `POST /invoices/{id}/finalize` (API-08)
	- `POST /payments/{id}/refund` (API-08)

- Validations and Rules:
	- Only Draft invoices can be finalized; UI must disable Finalize when preconditions not met and display server-provided reason.
	- Refund eligibility validated server-side; partial refunds supported where permitted.

- State Matrix:
	- Loading: skeleton panels
	- Draft: editable fields where permitted
	- Finalized: read-only with payment actions
	- Paid: show receipts and no finalize option
	- Failure: show reconciliation error and support contact

- Accessibility:
	- Table semantics for line items; action buttons labelled.

- Security & Privacy:
	- Mask payment references; export only for authorized users.

- Audit & Observability:
	- Emit `invoice.view`, `invoice.finalize`, `payment.refund` events to API-13.

- Acceptance Criteria:
	- Finalize transitions invoice to Finalized and is reflected in downstream systems within expected window.
	- Refund is processed and payment status updated with reconciliation entries.

- QA Test Cases (sample):
	- Finalize draft invoice with missing required fields: expect blocked action with reason.
	- Issue partial refund: verify ledger and receipt update.

- Traceability owner: Product Design / Finance Domain Owner

---

### UI-ATT-003 — Attendance Bulk Check-out / Reconciliation (Implementation-Ready)

- Screen ID: UI-ATT-003
- Screen name: Attendance Bulk Check-out / Reconciliation
 - Status: Ready — Product Design / Operations Domain Owner
- Business purpose: Allow supervisors and finance users to perform bulk check-outs, reconcile attendance batches, resolve duplicates/conflicts, and generate reconciliation tickets for follow-up accounting adjustments.
- Primary roles: Facility Manager, Finance User
- Supporting roles: Support User, Operations Lead
- Permission rules: `attendance.bulk_checkout` and `attendance.reconcile` required; reconciliation initiation may require organization-level permission.
- Tenant scope: Facility / Organization
- Preconditions: Attendance batch exists (date range or session); user has reconciliation permission; audit logging enabled.
- Entry points: Attendance module, reporting workflows, scheduled reconciliation tasks.
- Exit paths: Batch processed → reconciled summary and export; partial failures → list of exceptions and reconciliation tickets created.
- Layout regions:
	- Header: Batch identifier, date range, facility
	- Filters: session, trainer, activity, date range
	- Result table: attendee, check-in time, current check-out time, status, reconcile action
	- Bulk action bar: `Bulk Check-out`, `Create Reconciliation Ticket`, `Export Exceptions`

- Fields / Row data:
	- `attendance_id`, `customer_id`, `check_in_time`, `check_out_time`, `status`, `notes`

- Controls / Actions:
	- `Bulk Check-out` — calls `POST /attendance/bulk-checkout` (API-06) with selected records; returns job id for async processing.
	- `Create Reconciliation Ticket` — `POST /reconciliation/tickets` (API-11 or appropriate) for records requiring manual finance action.
	- `Export Exceptions` — `POST /attendance/export` (IC-07) to generate CSV/PDF for audit or ledger ingestion.

- Data sources / API mappings:
	- `GET /attendance?batch=...` (API-06)
	- `POST /attendance/bulk-checkout` (API-06)
	- `POST /reconciliation/tickets` (API-11 or appropriate)

- Validations and Rules:
	- Bulk operations execute asynchronously and must return job status; partial failures must be reported with actionable items.
	- Business rules: do not auto-checkout records older than configured retention window without extra confirmation.

- State Matrix:
	- Loading: table skeleton
	- Job queued: show job id and progress
	- Partial success: list exceptions with reasons
	- Complete: show summary and links to exported artifacts

- Accessibility:
	- Bulk actions must be keyboard-accessible and confirm destructive batch actions.

- Security & Privacy:
	- Exports limited by permission; include redaction where necessary.

- Audit & Observability:
	- Emit `attendance.bulk.checkout.initiated`, `attendance.bulk.checkout.completed`, and `attendance.reconciliation.created` events to API-13.

- Acceptance Criteria:
	- Bulk check-out job completes with accurate results and exceptions highlighted for manual review.
	- Reconciliation tickets contain sufficient context for finance to resolve discrepancies.

- QA Test Cases (sample):
	- Execute bulk checkout on a batch with mixed states: verify job processing and exception handling.
	- Export exceptions and validate CSV contents and masking.

- Traceability owner: Product Design / Operations Domain Owner

---

### UI-WLK-002 — Walk-in Payments List (Implementation-Ready)

- Screen ID: UI-WLK-002
- Screen name: Walk-in Payments List
 - Status: Ready — Product Design / Finance Domain Owner
- Business purpose: Provide a pageable, filterable view of walk-in payments for finance and staff to reconcile payments against walk-ins, manage refunds, and surface payment exceptions.
- Primary roles: Finance User, Site Staff
- Supporting roles: Support User
- Permission rules: `payment.list` and `walkin.payment.view` required; refunds require `payment.refund`.
- Tenant scope: Facility / Organization
- Preconditions: Payment records exist and are accessible via API-08; user has finance/reconciliation permissions.
- Entry points: Billing module, Walk-in module, Payment reconciliation workflows.
- Exit paths: Open payment detail `UI-PAY-001`, initiate refund, create reconciliation ticket.
- Layout regions:
	- Header: Title, date range, quick filter
	- Filters: payment status, provider, reference, customer, amount range
	- Result table: payment id, walk-in ref, amount, status, timestamp, actions
	- Bulk actions: Export, Mark reconciled

- Fields (per row):
	- `payment_id`, `walkin_reference`, `customer_name`, `amount`, `currency`, `status`, `provider`, `timestamp`, `actions`

- Controls / Actions:
	- `Verify` — refresh payment status via `GET /payments/{id}` (API-08).
	- `Issue Refund` — `POST /payments/{id}/refund` (API-08) with confirmation.
	- `Export` — async export via `POST /payments/export` (IC-07).

- Data sources / API mappings:
	- `GET /payments?scope=walkin&filters...` (API-08)
	- `POST /payments/{id}/refund` (API-08)

- Validations and Rules:
	- Refund eligibility per payment provider rules; UI must surface provider-specific limits and fees.
	- Marking reconciled must require a reconciliation reference and emit audit.

- State Matrix:
	- Loading: skeleton rows
	- Empty: show guidance for no payments
	- Export pending: job with download link

- Accessibility:
	- Table and actions keyboard-accessible; filters accessible.

- Security & Privacy:
	- Mask payment instrument references and limit export scope based on permission.

- Audit & Observability:
	- Emit `payment.list.view`, `payment.verify`, `payment.refund.initiated` events to API-13.

- Acceptance Criteria:
	- Payment verification updates status reliably; refunds follow backend validations and produce audit records.

- QA Test Cases (sample):
	- Verify payment status transition after provider callback.
	- Initiate refund and validate refund record and audit.

- Traceability owner: Product Design / Finance Domain Owner

---

### UI-TRN-001 — Trainer Calendar (Detailed Implementation-Ready)

- Screen ID: UI-TRN-001
- Screen name: Trainer Calendar
 - Status: Ready — Product Design / Trainer Domain Owner
- Business purpose: Provide trainers and facility managers a calendar view for managing availability, sessions, enrollments, cancellations, and capacity, with conflict prevention and batch-level actions.
- Primary roles: Trainer, Facility Manager
- Supporting roles: Site Staff, Support User
- Permission rules: `trainer.calendar.view` to view, `trainer.calendar.manage` to create or edit sessions; enrollment actions require `enrollment.manage` as appropriate.
- Tenant scope: Facility / Site
- Preconditions: Trainer profiles and availability data loaded; timezone and locale configured for trainer.
- Entry points: Trainer module, schedule workflows, calendar deep links.
- Exit paths: Open session detail (session page), create session flow, enrollment management.
- Layout regions:
	- Header: Calendar controls (view mode, date range, trainer selector, activity filter)
	- Calendar grid / agenda: event cards with capacity, status, enrolment count
	- Side panel: selected session detail and actions (reschedule, cancel, enrollments)

- Fields / Session data:
	- `session_id`, `trainer_id`, `activity_type`, `start_time`, `end_time`, `capacity`, `enrolled_count`, `status`

- Controls / Actions:
	- `Create Session` — `POST /sessions` (API-07) with recurrence options where permitted.
	- `Reschedule` — `PUT /sessions/{id}` (API-07) with conflict detection.
	- `Cancel` — `POST /sessions/{id}/cancel` with optional refund or notification propagation.
	- `Manage Enrollments` — opens enrollment list and supports `POST /enrollments` or `DELETE /enrollments/{id}`.

- Data sources / API mappings:
	- `GET /sessions?trainerId=...&range=...` (API-07)
	- `POST /sessions`, `PUT /sessions/{id}`, `POST /sessions/{id}/cancel` (API-07)
	- `GET /enrollments?sessionId=...` (API-07)

- Validations and Rules:
	- Conflict prevention: when creating or rescheduling, validate trainer availability and facility capacity; surface conflicts with suggested alternatives.
	- Recurrence rules must align to timezone semantics and avoid overlapping sessions for the same trainer.

- State Matrix:
	- Loading: calendar skeleton and prefetch indicators
	- Conflict: highlight conflicting time slots and block save until resolved or override confirmed (override audited)
	- Success: reflect session immediately in calendar and notify enrolled users if configured
	- Cancellation: show cancelled state and optional refund/notification links

- Accessibility:
	- Keyboard navigation for day/week views; event cards focusable and actionable; timepicker accessible.

- Security & Privacy:
	- Trainer personal contact details masked unless role permits.

- Audit & Observability:
	- Emit `session.create`, `session.reschedule`, `session.cancel`, and `enrollment.change` events to API-13 with actor and tenant context.

- Acceptance Criteria:
	- Calendar operations respect trainer availability and capacity rules and update participants within configured notification windows.
	- Conflict prevention reliably prevents double-booking.

- QA Test Cases (sample):
	- Create recurring session and verify instances appear in calendar and do not overlap.
	- Reschedule to conflicting time: expect conflict UI and prevented save unless override by authorised user.

- Traceability owner: Product Design / Trainer Domain Owner

---

## PR Review Template for Screen Specs

Use the repository PR template for screen-spec reviews: [screen-spec-review.md](.github/PULL_REQUEST_TEMPLATE/screen-spec-review.md)

### MVP Specs Completeness Matrix

| Screen ID | Name | Status |
|---|---:|---|
| UI-AUTH-001 | Login | Ready — Product Design / Identity and Access Owner |
| UI-CUS-001 | Customer List | Ready — Product Design / Customer Domain Owner |
| UI-CUS-002 | Customer Profile | Ready — Product Design / Customer Domain Owner |
| UI-CUS-003 | Create Customer | TBD — Product Design / Customer Domain Owner |
| UI-CUS-004 | Edit Customer | Ready — Product Design / Customer Domain Owner |
| UI-MEM-001 | Membership Detail | Ready — Product Design / Membership Domain Owner |
| UI-MEM-002 | Membership Purchase | Ready — Product Design / Commercial Domain Owner |
| UI-ATT-001 | Attendance Check-in | Ready — Product Design / Operations Domain Owner |
| UI-ATT-002 | Attendance Check-out / Correction | Ready — Product Design / Operations Domain Owner |
| UI-ATT-003 | Attendance Bulk Check-out / Reconciliation | Ready — Product Design / Operations Domain Owner |
| UI-WLK-001 | Walk-in Registration | TBD — Product Design / Operations Domain Owner |
| UI-WLK-002 | Walk-in Payments List | Ready — Product Design / Finance Domain Owner |
| UI-BIL-001 | Invoice Detail | Ready — Product Design / Finance Domain Owner |
| UI-BIL-002 | Invoice List | Ready — Product Design / Finance Domain Owner |
| UI-PAY-001 | Payment Status | TBD — Product Design / Finance Domain Owner |
| UI-TRN-001 | Trainer Calendar | Ready — Product Design / Trainer Domain Owner |

If a spec is incomplete, replace the Status with `TBD — requires: <owner/issue>` and open a follow-up ticket.

## 7.2 MVP Screen Mapping Rules

- Every MVP screen shall identify role, permission, and tenant scope before Review Draft.
- Every mutation screen shall identify validation, idempotency, duplicate submission, success, and failure behavior.
- Every provider-backed screen shall identify pending, timeout, retry, and reconciliation behavior where applicable.
- Every report, file, payment, and audit screen shall identify sensitive data handling.
- Every screen using candidate IDs shall stabilize its Screen ID before Frozen status.

---

### UI-CUS-004 — Edit Customer / Create→Edit Flow Variations (Implementation-Ready)

- Screen ID: UI-CUS-004
- Screen name: Edit Customer (Create→Edit Variations)
 - Status: Ready — Product Design / Customer Domain Owner
- Business purpose: Provide an editable form for updating customer records, support save-as-draft, rollback, and handle create→edit conversions with clear validation, audit, and duplicate-handling behavior.
- Primary roles: Site Staff, Facility Manager
- Supporting roles: Support User, Implementation User
- Permission rules: `customer.edit` required to update; `customer.create` for save-as-new flows; role-based field-level restrictions apply (e.g., only managers edit restricted fields).
- Tenant scope: Organization / Facility / Site
- Preconditions: Customer profile loaded (`UI-CUS-002`) and tenant context set; required reference lists loaded from API-14.
- Entry points: `Edit` action from `UI-CUS-002`, Create→Edit after `UI-CUS-003` draft save, bulk update workflows.
- Exit paths: Save → `UI-CUS-002`; Cancel → return to previous view with dirty-state warning; Conflict resolution → present merge/overwrite options.
- Layout regions:
	- Header: Title `Edit Customer`, status (editing), save / cancel actions
	- Sections: Identity, Contact, Address, Emergency Contact, Consents, Documents, Internal notes
	- Footer: Save, Save Draft, Cancel

- Fields and validation rules:
	- Fields same as Create but include historical read-only fields and last-modified metadata.
	- Cross-field validation (e.g., DOB vs age-based plan eligibility) performed client-side where possible and server-validated on save.

- Controls / Actions:
	- `Save` — `PUT /customers/{id}` (API-04). Use optimistic concurrency: include `If-Match`/version or ETag header. On 409 (conflict), present latest record and allow merge or reload.
	- `Save Draft` — stores partial edits in a draft resource or client-side store depending on implementation; indicate owner and timestamp.
	- `Cancel` — warns on dirty state.

- Conflict and Merge Rules:
	- On detect conflict (server 409), show field-level differences with `Keep Mine` / `Keep Theirs` options and require explicit merge confirmation; emit `customer.edit.conflict` audit event.

- State Matrix:
	- Editing: unsaved changes tracked and indicated
	- Saving: disable inputs, show inline spinner
	- Conflict: present merge UI
	- Success: return to profile and show transient confirmation
	- Validation error: show per-field messages and error summary

- Accessibility:
	- Ensure form sections have headings and ARIA role `form`; error summary links to fields.

- Security & Privacy:
	- Edits to restricted fields require elevated permission and emit an audit event; redact sensitive fields in logs.

- Audit & Observability:
	- Emit `customer.edit.attempt`, `customer.edit.success`, `customer.edit.conflict`, `customer.edit.failure` to API-13 with actor, tenant, and field-change summary.

- Acceptance Criteria:
	- Save respects optimistic concurrency and prevents silent overwrites.
	- Drafts can be resumed and saved without data loss.

- QA Test Cases (sample):
	- Simulate concurrent edits: expect conflict UI and merge resolution.
	- Save draft and reopen: verify persistence and editability.

- Traceability owner: Product Design / Customer Domain Owner

---

### UI-ATT-002 — Attendance Check-out / Correction (Implementation-Ready)

- Screen ID: UI-ATT-002
- Screen name: Attendance Check-out / Correction
 - Status: Ready — Product Design / Operations Domain Owner
- Business purpose: Allow site staff and managers to check out attendees, correct erroneous check-ins, and apply corrections with audit trail and optional billing adjustments.
- Primary roles: Site Staff, Facility Manager
- Supporting roles: Support User, Finance User
- Permission rules: `attendance.checkout` required for check-out; `attendance.correct` required for corrections/overrides; corrections may require manager approval depending on tenant policy.
- Tenant scope: Site
- Preconditions: Attendance event exists; user has checkout or correction permissions; audit logging configured.
- Entry points: From Attendance list, Customer profile attendance timeline, or direct check-in entry.
- Exit paths: Success → updated attendance record and optional billing adjustment; Failure → display error and steps for manual reconciliation.
- Layout regions:
	- Header: Attendance record summary
	- Check-out panel: time, staff, notes
	- Correction panel: original record, proposed changes, reason, manager approval workflow (if required)
	- Actions: `Check Out`, `Apply Correction`, `Request Approval`

- Fields and rules:
	- `attendance_id`, `check_in_time`, `check_out_time` (editable if correction permitted)
	- `correction_reason` required for any modification

- Controls / Actions:
	- `Check Out` — `POST /attendance/{id}/checkout` (API-06) or `PUT` depending on API design; on success, update occupancy and emit audit.
	- `Apply Correction` — `POST /attendance/{id}/correction` (API-06) with required reason; if approval required, set status `pending_approval` and notify approver.
	- `Request Approval` — triggers notification to approver per IC-05 and records request.

- Data sources / API mappings:
	- `GET /attendance/{id}` (API-06)
	- `POST /attendance/{id}/checkout` (API-06)
	- `POST /attendance/{id}/correction` (API-06)

- Validations and Rules:
	- Corrections must include a reason and do not silently alter historical audit logs; original and corrected records are retained with change metadata.
	- Billing adjustments resulting from corrections must create a reconciliation ticket for Finance.

- State Matrix:
	- Idle: record displayed
	- Checkout pending: spinner until confirmation
	- Correction pending approval: show status and timeline
	- Correction applied: show updated record and notification
	- Failure: provide recovery steps and support reference

- Accessibility:
	- Ensure correction dialog is accessible and announces status updates.

- Security & Privacy:
	- Corrections are high-sensitivity actions and must be audited with actor, reason, and timestamps.

- Audit & Observability:
	- Emit `attendance.checkout`, `attendance.correction.request`, `attendance.correction.applied` events to API-13.

- Acceptance Criteria:
	- Check-out operations reflect in occupancy and reporting within configured window.
	- Corrections produce audit records and, where approval required, block until approved.

- QA Test Cases (sample):
	- Check-out an attendee: verify occupancy decremented and timeline updated.
	- Apply correction requiring approval: verify request creation and approver notification.

- Traceability owner: Product Design / Operations Domain Owner

---

### UI-BIL-002 — Invoice List (Implementation-Ready)

- Screen ID: UI-BIL-002
- Screen name: Invoice List
 - Status: Ready — Product Design / Finance Domain Owner
- Business purpose: Provide finance users with a paged, filterable, and exportable view of invoices for reconciliation, bulk actions, and navigation to `UI-BIL-001` Invoice Detail.
- Primary roles: Finance User, Organization Owner
- Supporting roles: Support User
- Permission rules: `invoice.list` required; export requires elevated finance permission and audit.
- Tenant scope: Organization / Facility
- Preconditions: Tenant context loaded; invoice index available via API-08.
- Entry points: Billing module nav, report links, reconciliation workflows.
- Exit paths: Open invoice `UI-BIL-001`, export selection to CSV/PDF, create reconciliation ticket.
- Layout regions:
	- Header: Title, date range selector, primary actions (Export, Reconciliation)
	- Filters: status, customer, date range, amount range, payment status
	- Result table: invoice number, customer, date, due, total, status, actions
	- Bulk action bar: Export, Mark as Reviewed, Create Reconciliation

- Fields (per row):
	- `invoice_number`, `customer_name`, `issue_date`, `due_date`, `total_amount`, `status`, `payment_status`, `actions`

- Controls / Actions:
	- `Search/Filter` — `GET /invoices` (API-08) with filter parameters.
	- `Export` — bulk export selected invoices to CSV/PDF via `POST /invoices/export` (IC-07) with job tracking.
	- `Open` — navigate to `UI-BIL-001`.

- Data sources / API mappings:
	- `GET /invoices?q=&filters...` (API-08)
	- `POST /invoices/export` (IC-07)

- Validations and Rules:
	- Exports limited by permission and rate; large exports require async job and notification when ready.
	- Filters persist in query string for deep-links and reproduceable views.

- State Matrix:
	- Loading: skeleton rows
	- Empty: show CTA to create invoices or adjust filters
	- Partial results: show counts and paging controls
	- Export pending: job status panel with download when ready

- Accessibility:
	- Table headers, sorting, and pagination controls accessible; bulk actions keyboard-operable.

- Security & Privacy:
	- Limit export fields based on permission; mask payment references in export where not permitted.

- Audit & Observability:
	- Emit `invoice.list.view`, `invoice.export.initiated` events to API-13 with actor and tenant.

- Acceptance Criteria:
	- Filters and search return correct results within 3s for default page sizes.
	- Export jobs complete and produce downloadable artifacts with audit trail.

- QA Test Cases (sample):
	- Filter by status and date: verify results and counts.
	- Initiate large export: verify async job creation and download availability.

- Traceability owner: Product Design / Finance Domain Owner

---

# 8. Global Application Shell

| Region | Purpose |
|---|---|
| App Header | Product identity, tenant context, notifications, user menu |
| Navigation | Role-aware access to approved modules |
| Page Header | Screen title, context, status, primary page actions |
| Main Content | Workflow-specific content |
| Secondary Panel | Filters, details, contextual help, or side actions |
| Feedback Region | Loading, empty, error, success, warning, and async feedback |

---

# 9. Authentication Screens

| Screen ID | Screen Name | Purpose | API / Integration |
|---|---|---|---|
| UI-AUTH-001 | Login | Authenticate user | API-03, IC-02 |
| UI-AUTH-002 | Password Reset Request | Start recovery | API-03, IC-02 |
| UI-AUTH-003 | Password Reset Complete | Complete recovery | API-03, IC-02 |
| UI-AUTH-004 | Session Expired | Recover expired session | IC-02 |
| UI-AUTH-005 | Forced Logout | Explain revoked session | IC-02 |

Required states:

- Loading.
- Invalid credentials.
- Account locked.
- Session expired.
- Refresh failed.
- Forced logout.
- Success.

---

# 10. Tenant Context Screens

| Screen ID | Screen Name | Purpose | API / Integration |
|---|---|---|---|
| UI-TEN-001 | Context Selection | Select Organization, Facility, and Site | API-02, IC-03 |
| UI-TEN-002 | Context Switch Confirmation | Confirm switch with unsaved work warning | IC-03 |
| UI-TEN-003 | Context Access Denied | Show safe denied state | API-23, IC-03 |

Tenant selectors shall show only authorized contexts.

Status notes:

- UI-TEN-001: Ready — Product Design / Identity and Access Owner


---

# 11. Role-Aware Home Screens

| Screen ID | Screen Name | Purpose |
|---|---|---|
| UI-HOME-001 | Role-Aware Home | Show permitted work queues and shortcuts |
| UI-HOME-002 | Operational Work Queue | Show pending user-specific tasks |
| UI-HOME-003 | Alerts and Exceptions | Show role-visible alerts |

Home screens shall prioritize actionable workflows rather than decorative dashboards.

---

# 12. Platform Administration Screens

| Screen Group | Purpose | Mapping |
|---|---|---|
| Platform Settings | Configure platform-owned settings | API-01 |
| Master Data | Manage global references | API-01, API-14 |
| Feature Flags | Enable/disable platform capabilities | API-01 |
| Maintenance Notices | Communicate platform events | API-01 |
| Platform Audit | Review administrative actions | API-13 |

All platform administration actions require audit-aware UI behavior.

---

# 13. Organization Facility Site Screens

Screen groups:

- Organization profile.
- Facility profile.
- Site profile.
- Address and contact.
- Settings and policies.
- Operational configuration.
- Onboarding state.
- Documents.

Mappings: API-02, IC-03, IC-06.

---

# 14. Identity User Role Screens

Screen groups:

- User list.
- User detail.
- Invite user.
- Role assignment.
- Permission review.
- Access scope.
- Session management.
- Lock/unlock.
- Revocation.

Mappings: API-03, API-23, IC-02, IC-12.

Permission-sensitive screens shall show visible, disabled, hidden, or denied states explicitly.

---

# 15. Customer Screens

Screen groups:

- Customer search.
- Customer create/edit.
- Customer profile.
- Contact and emergency contact.
- Preferences and consent.
- Documents.
- Notes.
- Status history.
- Duplicate detection.

Mappings: API-04, IC-01, IC-06.

Restricted customer data shall be masked where permission requires.

---

# 16. Membership Screens

Screen groups:

- Plan selection.
- Membership purchase.
- Membership detail.
- Renewal.
- Upgrade/downgrade.
- Freeze/resume.
- Cancellation.
- Expiry.
- Entitlement view.
- Lifecycle history.

Mappings: API-05, API-24.

Lifecycle actions shall follow allowed states from API-24.

---

# 17. Attendance and Walk-in Screens

Screen groups:

- Attendance search.
- Eligibility check.
- Check-in.
- Check-out.
- Correction.
- Override.
- Walk-in registration.
- Walk-in payment association.
- Occupancy view.

Mappings: API-06, IC-01.

Attendance screens shall prioritize speed, clarity, and recoverability.

---

# 18. Trainer Activity Batch Screens

Screen groups:

- Trainer profile.
- Availability.
- Activity list.
- Batch list.
- Batch detail.
- Session calendar.
- Enrollment.
- Attendance association.
- Progress and notes.
- Cancellation.

Mappings: API-07.

Scheduling screens shall expose conflict, capacity, and cancellation behavior.

---

# 19. Billing Payment Screens

Screen groups:

- Billing account.
- Invoice list.
- Invoice detail.
- Payment initiation.
- Payment status.
- Refund initiation.
- Refund status.
- Settlement and reconciliation.
- Receipt.

Mappings: API-08, API-09, IC-04, IC-11.

Financial screens shall define pending, success, failed, duplicate, refund, timeout, and reconciliation-required states.

---

# 20. Subscription License Screens

Screen groups:

- Subscription plan.
- Subscription purchase.
- Subscription status.
- Renewal.
- Cancellation.
- Suspension.
- License assignment.
- License release.
- Entitlement and feature access.
- Paywall.

Mappings: API-09.

Commercial eligibility behavior shall be clear and user-safe.

---

# 21. Notification Campaign Screens

Screen groups:

- Campaign list.
- Campaign create/edit.
- Audience selection.
- Template selection.
- Schedule.
- Activation.
- Pause/cancel.
- Delivery status.
- Consent and preference.
- Failure and retry.

Mappings: API-10, IC-05.

Notification UI shall respect consent, preferences, suppression, and sensitive-data restrictions.

---

# 22. Reports Analytics Screens

Screen groups:

- Report catalog.
- Report parameter entry.
- Report execution status.
- Export ready.
- Export failed.
- Dashboard.
- KPI view.
- Scheduled report where approved.

Mappings: API-11, IC-07.

Reports shall define masking, async generation, polling, download, expiry, and failure recovery.

---

# 23. Support Ticket Screens

Screen groups:

- Ticket list.
- Ticket create.
- Ticket detail.
- Comments.
- Attachments.
- Assignment.
- Escalation.
- SLA.
- Internal notes.
- Closure and reopening.

Mappings: API-12, IC-06.

Customer-visible and internal content shall be separated.

---

# 24. Audit Security Screens

Screen groups:

- Audit event search.
- Audit event detail.
- Security event list.
- Investigation workspace.
- Sensitive access review.
- Audit export.

Mappings: API-13, IC-12, IC-13.

Audit and security screens shall use restricted data controls and safe export behavior.

---

# 25. Common Reference Screens

Screen groups:

- Country and region references.
- Currency references.
- Language and timezone references.
- Facility type references.
- Activity type references.
- Status values.
- Payment methods.
- Communication channels.
- Lookup values.
- Localization values.

Mappings: API-14.

Reference screens shall preserve cache and localization expectations.

---

# 26. Screen State Matrix

| State | Required Behavior |
|---|---|
| Loading | Show progress or skeleton without layout jump |
| Empty | Explain no data and show allowed next action |
| Validation Error | Show field-level and summary-level messages |
| Authorization Denied | Show safe denied state without leaking restricted data |
| Tenant Denied | Show safe context error |
| Retryable Failure | Provide retry where safe |
| Offline | Disable unsafe actions and explain recovery |
| Conflict | Show latest-state refresh or conflict resolution |
| Async Pending | Show status and expected next step |
| Success | Confirm outcome and next available action |

---

# 27. Responsive Behavior Matrix

| Screen Type | Web | Mobile |
|---|---|---|
| Home | Work queue and panels | Prioritized stack |
| List | Table with filters | Search plus card/list rows |
| Detail | Header, tabs, side panels | Stacked sections |
| Form | Grouped sections | Single-column staged flow |
| Calendar | Grid or agenda | Agenda-first |
| Dashboard | Multi-panel layout | Priority metric stack |
| Modal | Dialog/drawer | Bottom sheet/full-screen flow |

---

# 28. Accessibility Requirements

Each screen shall define:

- Heading structure.
- Label requirements.
- Error association.
- Focus order where web applies.
- Touch target readiness where mobile applies.
- Non-color-only status communication.
- Contrast-sensitive states.
- Screen-reader label needs where applicable.

---

# 29. Audit-Triggering UI Actions

Audit-triggering actions include:

- Login and logout.
- Permission changes.
- Tenant configuration changes.
- Customer restricted data access.
- Membership lifecycle changes.
- Attendance override or correction.
- Payment and refund actions.
- Subscription and license changes.
- Campaign activation.
- Report export.
- Support internal notes.
- Audit export.

Mappings: API-13, IC-12, IC-13.

---

# 30. UI Traceability Matrix

| Screen Area | Flow Mapping | API Mapping | Integration Mapping |
|---|---|---|---|
| Authentication | UX-FLOW-AUTH-001 | API-03 | IC-02 |
| Tenant Context | UX-FLOW-TEN-001 | API-02, API-23 | IC-03 |
| Customer | UX-FLOW-CUS-001 | API-04 | IC-01, IC-06 |
| Membership | UX-FLOW-MEM-001 | API-05, API-24 | IC-01 |
| Attendance | UX-FLOW-ATT-001 | API-06 | IC-01 |
| Trainer Activity Batch | UX-FLOW-TRN-001 | API-07 | IC-01 |
| Billing Payment | UX-FLOW-PAY-001 | API-08 | IC-04, IC-11 |
| Subscription License | UX-FLOW-SUB-001 | API-09 | IC-01 |
| Notification Campaign | UX-FLOW-NOT-001 | API-10 | IC-05 |
| Reports Analytics | UX-FLOW-RPT-001 | API-11 | IC-07 |
| Support Ticket | UX-FLOW-SUP-001 | API-12 | IC-06 |
| Audit Security | UX-FLOW-AUD-001 | API-13 | IC-12, IC-13 |
| Common Reference | UX-FLOW-REF-001 | API-14 | IC-01 |

---

# 31. Screen Acceptance Criteria Standard

Each screen shall be accepted only when:

- Screen purpose is clear.
- Roles and permissions are defined.
- Tenant scope is defined.
- Entry and exit paths are defined.
- Layout and sections are defined.
- Fields and actions are defined.
- API and integration mappings are traceable.
- Validation and states are complete.
- Responsive behavior is defined.
- Accessibility expectations are defined.
- Audit-triggering actions are identified.

---

# 32. Assumptions and Constraints

- Screen IDs in this Design Draft may be refined during review but shall remain stable after Frozen status.
- Missing source mappings shall use `[TBD — Source mapping pending — see BE traceability mappings](docs/10_Backend_Engineering/BE-TRACEABILITY_MAPPINGS.md)`.
- UI screens shall not introduce unapproved roles, fields, actions, workflows, or permissions.
- Hidden and disabled controls are not security boundaries.

---

# 33. Acceptance Criteria

- Implementation-ready screen specification structure is defined.
- Global screen inventory is documented.
- MVP screen groups are mapped to API and Integration Contract sources.
- State, responsive, accessibility, audit, and traceability requirements are documented.
- Frontend and QA teams can use this document as the baseline for detailed screen implementation and validation.

---

# 34. Summary

UX-05 defines the implementation-ready UI screen specification baseline for Digitize. It connects approved UX strategy, user flows, wireframes, design-system rules, API behavior, and Integration Contract behavior into screen-level contracts for frontend implementation and QA validation.
