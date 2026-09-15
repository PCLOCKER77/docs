# Follow-up TODOs — Issues to Open

This file lists lightweight, ready-to-post GitHub issues to capture gating items before documentation freeze. Copy the sections below into new issues, or ask me to open them (requires repo issue permissions).

---

## 1) Auth API Confirmation — CLOSED for Phase 1

HTTP contract is frozen in `docs/architecture/AUTH_CONTRACT_FREEZE.md`.
Do not implement from this issue. MFA/SSO remain deferred.

---

- Title: [Docs Blocker] Confirm Authentication API details (API-03)
- Labels: documentation, api, blocking, security
- Suggested Assignees: @api-owner, @security-owner, @product-design

### Description
The `UI-AUTH-001` Login screen and related auth flows reference `API-03` and `IC-02`. Before freezing the UI spec we need confirmation of the following API details so frontend and QA can map errors and UX accurately.

Required confirmations:
- Exact response payload shape on success (session token, refresh token, profile, available roles/tenants).
- Error codes and recommended user-facing messages for: invalid credentials (401), locked account (423), MFA required (if applicable), rate-limit (429 with Retry-After header), and generic provider errors (5xx).
- Rate-limit headers (names and semantics) and recommended client retry/backoff strategy.
- MFA / SSO decision: whether MFA/SSO flows are required or optional, and callback/welcome paths (deep-link behaviour).
- Correlation ID header name to display to users for support.

### Acceptance criteria
- API owner confirms payload samples and error codes in a comment or attaches OpenAPI fragment.
- Frontend mappings table produced (error code → user message) and attached to `docs/09_UI_UX_Design/UX-05_UI_Screens.md` or API repo.

---

## 2) Payment API / Provider Rules (API-08 / IC-04)

- Title: [Docs Blocker] Confirm Payment provider rules and reconciliation hooks (API-08 / IC-04)
- Labels: documentation, payments, blocking, finance
- Suggested Assignees: @payments-owner, @finance-owner, @product-design

### Description
`UI-WLK-002`, `UI-BIL-001`, and `UI-PAY-001` reference payment and refund behaviour. Need explicit provider rules and reconciliation contract details to complete acceptance criteria and QA.

Required confirmations:
- Refund eligibility per provider (full, partial limits, time windows), fees, and required fields for refund requests.
- Webhook callback semantics and idempotency guarantees for payment status updates.
- Recommended UI behaviour for pending-payment, timeout, and reconciliation-required statuses.
- Export / ledger artifact formats and reconciliation job endpoints (IC-04 / IC-07) including retention and masking rules for PII.

### Acceptance criteria
- Payments owner attaches provider documentation or OpenAPI fragments covering refunds, webhooks, and status transitions.
- Frontend mapping of payment states and refund flows added to `UX-05_UI_Screens.md` (or referenced API doc).

---

## 3) Brand Tokens and Design Tokens (UX-04)

- Title: [Design Blocker] Approve brand tokens (colors, typography, spacing) for UX-04
- Labels: design, documentation, blocking
- Suggested Assignees: @design-system-owner, @product-design

### Description
`UX-04_Design_System` needs a finalized token set (color palette, typography scale, spacing tokens) to make screen specs implementation-ready and to allow frontend components to consume canonical values.

Required confirmations:
- Final color palette with hex/alpha values and semantic token names (primary, secondary, critical, success, warning, neutral variants).
- Typography scale (font families, weights, sizes for H1/H2/H3/body/caption), line-heights, and responsive breakpoints.
- Spacing scale and component-level token mapping for common components (button, input, card, modal).
- Accessibility contrast verification report for all semantic colors.

### Acceptance criteria
- Design owner attaches token JSON/SASS/SCSS file or points to the canonical token file in the repo.
- UX-04 updated with token links and a note that tokens are frozen for implementation.

---

## 4) UI-00 Freeze Signoff

- Title: [Governance] Freeze `UI-00_UI_UX_Standards.md` and approve downstream freeze list
- Labels: governance, docs, freeze
- Suggested Assignees: @product-lead, @arch-lead, @security-lead

### Description
Before marking UX docs as Frozen, governance must sign off `UI-00` and confirm the list of specs to freeze and the approvers for any exceptions.

Required confirmations:
- Official approver list and sign-off date.
- Any approved exceptions (MFA/SSO deferred, payment provider TBD) with owner and timeline.

### Acceptance criteria
- Approver comments or formal sign-off in the issue; a `docs/freeze` label added and freeze date recorded.

---

If you want, I can also open these issues directly on GitHub — I will need permission or a GitHub token to create issues in the repository. Tell me which option you prefer: (A) I create the issues for you (ask for token/permissions), or (B) I leave these ready for you to copy/paste (current), or (C) I create GitHub Issue Templates instead so authors can file them from the UI.

---

Review note: Review of `UX-05_UI_Screens.md` completed on 2026-07-26. The items above are the active blockers to be filed. When you're ready, either file them via these templates or ask me to open them programmatically.
