# Freeze Readiness Checklist — Functional Requirements

This consolidated checklist summarizes outstanding items required for per-module documentation freeze. Reviewers: Product Management, Business Analysis, Solution Architecture, Security, Finance, Legal, and Implementation leads.

Overview
- All module documents (FR-02..FR-21) set to `Status: Draft` to match README. `FR-01_FRS_Standards.md` remains `Frozen` as the canonical template.
- Role naming normalized (expanded `Platform Admin` → `Platform Administrator`) in multiple modules.
- Automated, non-invasive fixes applied only where safe.

Global missing items (action: BA owners)
- Missing Business Rule documents (BR-XXX) referenced by FRs: the repository contains BR documents for: BR-003, BR-004, BR-005, BR-006, BR-008, BR-011, BR-012, BR-014, BR-015, BR-016, BR-017, BR-020, BR-021, BR-023, BR-030. All other referenced BR IDs must have corresponding `FRS-BR-XXX_*.md` files created before freeze. Missing BR IDs (partial list):
  - BR-001, BR-002, BR-007, BR-009, BR-010, BR-013, BR-018, BR-019, BR-022, BR-024..BR-029
  - BR-ATT-001 .. BR-ATT-010
  - BR-AUD-001 .. BR-AUD-008
  - BR-BIL-001 .. BR-BIL-008
  - BR-CUS-001 .. BR-CUS-010
  - BR-FAC-001 .. BR-FAC-010 (many referenced, only some present)
  - BR-MEM-001 .. BR-MEM-010
  - BR-NOT-001 .. BR-NOT-008
  - BR-ORG-001 .. BR-ORG-010 (many present in FR text but not standalone BR doc)
  - BR-PAY-001 .. BR-PAY-008
  - BR-PLT-003 .. BR-PLT-008
  - BR-RPT-001 .. BR-RPT-008
  - BR-SEC-001 .. BR-SEC-010
  - BR-SIT-001 .. BR-SIT-010
  - BR-SUB-001 .. BR-SUB-012
  - BR-TRN-001 .. BR-TRN-010

Action: BA team must author `FRS-BR-<XXX>_*.md` for each referenced BR or update FRs to reference existing BR docs. Without these BR artifacts the FRs are not traceable to authoritative business rules.

Per-module freeze checklist (high-level)

- FR-02 Platform Administration
  - Traceability: Ensure BA-08 references exist and point to formal BA artifacts.
  - Business Rules: Verify BR-PLT-* documents exist for each referenced PLT BR.
  - Security: Confirm administrative RBAC mapping and auditing schema.
  - API readiness: Add request/response examples for platform settings APIs.
  - Approval: Product + Security signoff.

- FR-03 Organization Management
  - Traceability: Validate BA references and BA-02 BR-ORG-* existence.
  - Data: Confirm uniqueness/validation rules for registration numbers per jurisdiction.
  - Lifecycle: Confirm state transitions (Pending → Active) and activation checklist.
  - Audit: Define audit payload fields and retention rules.
  - Approval: Product + Legal (for registration/tax data) + Ops.

- FR-04 Facility Management
  - Licensing: Confirm license entitlement checks and BR-LIC mapping.
  - Master data: Facility Type master data source and API.
  - Activation gating: Define exact readiness conditions for activation.

- FR-05 Site Management
  - Entitlement: Confirm add-on licensing policy and how activation is blocked/unblocked.
  - Address validation rules and country-specific requirements.

- FR-06 User & Role Management
  - Security: Detailed RBAC matrix required; map roles → permissions in an annex.
  - Identity: Confirm invitation and credential workflows (SAML/OIDC/Email OTP) as applicable.
  - Audit: Ensure auditable events for role/permission changes are specified.

- FR-07 Customer Management
  - Privacy: Confirm consent capture fields and legal-approved text.
  - Duplicate rule: Provide precise duplicate matching algorithm and override policy.
  - ID generation: Confirm format and uniqueness constraints.

- FR-08 Membership Management
  - Billing integration: Confirm billing reference creation flow and API contract.
  - Pricing/taxes: Confirm tax calculation rules and rounding policy.
  - Status transitions: Define statuses and automation for activation on payment.

- FR-09 Attendance Management
  - Capacity/override: Define approver roles and override rationale capture.
  - Duplicate attendance prevention algorithm.

- FR-10 Walk-in Customer Management
  - Payment capture: Define walk-in fee flows and receipts (integration with Billing).

- FR-11 Trainer Management
  - Assignments: Define staff-to-trainer relationship constraints and notifications.

- FR-12 Personal Training
  - Booking: Confirm session booking validation and cancellation policies.

- FR-13 Batch / Class Management
  - Scheduling: Confirm recurrence rules and batch capacity handling.

- FR-14 Billing & Payment Management
  - Refunds: Ensure `FRS-BR-020_Refund_Processing.md` covers refund windows and approvals.
  - Payment: Confirm payment gateway contracts and idempotency rules.

- FR-15 Subscription Management
  - Subscription lifecycle and cancellation policy.

- FR-16 License Management
  - License allocation behavior and reporting.

- FR-17 Advertisement Campaign
  - Privacy & opt-in: Confirm campaign opt-in requirements and suppression lists.

- FR-18 Notification Management
  - Template variables, localization, and rate limits.

- FR-19 Reports & Analytics
  - Data retention, PII masking, and scheduled refresh jobs.

- FR-20 Support Ticket
  - SLA, escalation matrix, and contact points.

- FR-21 Audit & Compliance
  - Audit event schema, retention, and export/attestation processes.

Suggested immediate next steps (I can do these)
1. Create a `FRS-BR-XXX` document for each missing BR ID where the BA owner indicates ownership. I can auto-generate BR stubs (template with ID, name, description, and references) for BA to fill; confirm if you want me to scaffold these stubs.
2. For highest-risk modules (Platform, Organization, Billing, Subscription, License), I can generate API request/response stubs and state transition diagrams as separate artifacts.
3. Produce one-page freeze-ready signoff checklist per module (ready for signatures) and a combined sign-off matrix.

Requested decision
- Confirm whether you want me to scaffold missing BR stubs (yes/no). If yes, confirm naming/owner pattern (default: `FRS-BR-<XXX>_AutoStub.md` assigned to `Product Management`).

---
Generated: July 25, 2026
Generated by: Documentation Auditor (automated pass)