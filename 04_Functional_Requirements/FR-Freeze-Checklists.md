# Functional Requirements — Freeze Checklists

Generated: 2026-07-25
Purpose: Per-module freeze readiness checklists to support design freeze signoff.

Instructions: For each module, fill the blanks, assign owners, attach evidence (API specs, DB entity docs, test cases). Use `FRS-Missing-BR-Registry.md` to resolve business rule gaps before final signoff.

---

## FR-02 Platform Administration
- **Module doc:** [FR-02_Platform_Administration.md](FR-02_Platform_Administration.md)
- **Module owner:** TBD
- **Status:** Draft → Ready for Freeze? [ ] Yes [ ] No
- **Traceability:** BA refs present? [ ]; BRs resolved? See `FRS-Missing-BR-Registry.md` entries for BR-PLT-*.
- **Validation rules:** Present? [ ]; examples/test cases attached? [ ]
- **Approval flows:** Admin approvals defined? [ ]
- **Security & RBAC:** RBAC matrix attached? [ ]; audit events defined? [ ]
- **Multi-tenant support:** Tenant boundaries defined? [ ]
- **API readiness:** Endpoints listed with method/path/auth examples? [ ]
- **DB readiness:** Entities/tables listed with CRUD mapping? [ ]
- **Outstanding items:**
  - Author BR-PLT-003..BR-PLT-008 in registry (Owner: BA)
  - Add request/response examples for `Platform Settings` APIs (Owner: API)
  - Complete RBAC matrix and audit event fields (Owner: Security)
- **Signoff:** Product: ______  Security: ______  BA: ______  Date: ______

## FR-03 Organization Management
- **Module doc:** [FR-03_Organization_Management.md](FR-03_Organization_Management.md)
- **Module owner:** TBD
- **Status:** Draft → Ready for Freeze? [ ] Yes [ ] No
- **Traceability:** BA refs present? [ ]; resolve BR-ORG-* per registry.
- **Validation rules:** Organization uniqueness rules, jurisdiction constraints present? [ ]
- **Approval flows:** Org verification & legal approvals documented? [ ]
- **Security & Data:** PII fields identified & protection noted? [ ]
- **API readiness:** Onboarding APIs & idempotency defined? [ ]
- **DB readiness:** Org entities, owner FK, constraints listed? [ ]
- **Outstanding items:**
  - Author BR-ORG-001..BR-ORG-010 (Registry)
  - Add acceptance tests for org activation and ownership change (Owner: QA)
- **Signoff:** Product: ______  Legal: ______  BA: ______  Date: ______

## FR-04 Facility Management
- **Module doc:** [FR-04_Facility_Management.md](FR-04_Facility_Management.md)
- **Module owner:** TBD
- **Status:** Draft → Ready for Freeze? [ ] Yes [ ] No
- **Traceability:** BR-FAC-* resolution required (check registry)
- **Validation rules:** Facility capacity, open/close states, configuration constraints present? [ ]
- **API readiness:** Facility CRUD, configuration endpoints defined? [ ]
- **DB readiness:** Facility entity, capacity fields, indexing for queries? [ ]
- **Outstanding items:**
  - Author BR-FAC-001..BR-FAC-010
  - Add state transition diagram for facility lifecycle (Owner: SA)
- **Signoff:** Product: ______  Ops: ______  BA: ______  Date: ______

## FR-05 Site Management
- **Module doc:** [FR-05_Site_Management.md](FR-05_Site_Management.md)
- **Module owner:** TBD
- **Key checks:** Address validation, entitlement gating, locale rules, payment linkage for add-ons.
- **Outstanding items:** Complete BR-FAC/BR-SIT references; provide sample API for site activation.
- **Signoff:** Product: ______  Ops: ______  BA: ______  Date: ______

## FR-06 User & Role Management
- **Module doc:** [FR-06_User_Role_Management.md](FR-06_User_Role_Management.md)
- **Key checks:** RBAC matrix included; invitation/SSO flows; audit events for role changes.
- **Outstanding items:** Add RBAC matrix and test cases; map permissions to APIs.
- **Signoff:** Security: ______  Product: ______  BA: ______  Date: ______

## FR-07 Customer Management
- **Module doc:** [FR-07_Customer_Management.md](FR-07_Customer_Management.md)
- **Key checks:** Duplicate detection rules, identity verification (BR-CUS-*), consent capture.
- **Outstanding items:** Author BR-CUS-001..BR-CUS-010; add privacy/consent text and sample UI strings.
- **Signoff:** Product: ______  Privacy: ______  BA: ______  Date: ______

## FR-08 Membership Management
- **Module doc:** [FR-08_Membership_Management.md](FR-08_Membership_Management.md)
- **Key checks:** Billing integration points, pricing/tax rules, membership lifecycle transitions.
- **Outstanding items:** Author BR-MEM-* entries; add billing reference examples and test cases.
- **Signoff:** Product: ______  Finance: ______  BA: ______  Date: ______

## FR-09 Attendance Management
- **Module doc:** [FR-09_Attendance_Management.md](FR-09_Attendance_Management.md)
- **Key checks:** Capacity handling, override policies, audit of attendance events.
- **Outstanding items:** Author BR-ATT-* rules; document capacity overbooking behavior and notifications.
- **Signoff:** Product: ______  Ops: ______  BA: ______  Date: ______

## FR-10 Walkin Customer Management
- **Module doc:** [FR-10_Walkin_Customer_Management.md](FR-10_Walkin_Customer_Management.md)
- **Key checks:** Payment capture, receipt generation, temporary membership linkage.
- **Outstanding items:** Add payment idempotency behavior and sample receipts; align with BR-BIL-*.
- **Signoff:** Product: ______  Finance: ______  BA: ______  Date: ______

## FR-11 Trainer Management
- **Module doc:** [FR-11_Trainer_Management.md](FR-11_Trainer_Management.md)
- **Key checks:** Allocation rules, assignments, notifications, qualifications data.
- **Outstanding items:** Define trainer-to-staff relationship constraints; add BR-TRN-* as needed.
- **Signoff:** Product: ______  Ops: ______  BA: ______  Date: ______

## FR-12 Personal Training
- **Module doc:** [FR-12_Personal_Training.md](FR-12_Personal_Training.md)
- **Key checks:** Booking rules, cancellation policies, trainer availability APIs.
- **Outstanding items:** Add acceptance tests for booking/cancel flows; BR-TRN refs.
- **Signoff:** Product: ______  Ops: ______  BA: ______  Date: ______

## FR-13 Batch/Class Management
- **Module doc:** [FR-13_Batch_Class_Management.md](FR-13_Batch_Class_Management.md)
- **Key checks:** Recurrence rules, capacity, waitlist behavior, scheduling constraints.
- **Outstanding items:** Add schedule recurrence examples and batch reschedule behavior.
- **Signoff:** Product: ______  Ops: ______  BA: ______  Date: ______

## FR-14 Billing & Payment Management
- **Module doc:** [FR-14_Billing_Payment_Management.md](FR-14_Billing_Payment_Management.md)
- **Key checks:** Gateway contracts, idempotency, refunds (BR-020), settlement flow.
- **Outstanding items:** Author BR-BIL-* and BR-PAY-*; include sample refund workflow and error codes.
- **Signoff:** Finance: ______  Product: ______  BA: ______  Date: ______

## FR-15 Subscription Management
- **Module doc:** [FR-15_Subscription_Management.md](FR-15_Subscription_Management.md)
- **Key checks:** Lifecycle transitions, cancellation policy, prorations, entitlement mapping.
- **Outstanding items:** Author BR-SUB-*; provide API examples for subscription change events.
- **Signoff:** Product: ______  Finance: ______  BA: ______  Date: ______

## FR-16 License Management
- **Module doc:** [FR-16_License_Management.md](FR-16_License_Management.md)
- **Key checks:** License allocation, revocation, reporting, entitlements per tenant.
- **Outstanding items:** Document license limits, reporting exports, and reconciliation timing.
- **Signoff:** Product: ______  Ops: ______  BA: ______  Date: ______

## FR-17 Advertisement Campaign
- **Module doc:** [FR-17_Advertisement_Campaign.md](FR-17_Advertisement_Campaign.md)
- **Key checks:** Campaign targeting rules, suppression lists, privacy/consent handling.
- **Outstanding items:** Author BR-021 and related BR-RPT items; add sample campaign payloads.
- **Signoff:** Product: ______  Marketing: ______  BA: ______  Date: ______

## FR-18 Notification Management
- **Module doc:** [FR-18_Notification_Management.md](FR-18_Notification_Management.md)
- **Key checks:** Templates, localization, rate-limiting, delivery guarantees, error handling.
- **Outstanding items:** Author BR-NOT-*; provide template variable lists and example payloads.
- **Signoff:** Product: ______  Ops: ______  BA: ______  Date: ______

## FR-19 Reports & Analytics
- **Module doc:** [FR-19_Reports_Analytics.md](FR-19_Reports_Analytics.md)
- **Key checks:** Data retention, PII masking, scheduled jobs, refresh windows.
- **Outstanding items:** Author BR-RPT-*; document data sources and SLAs for report generation.
- **Signoff:** Product: ______  Data: ______  BA: ______  Date: ______

## FR-20 Support Ticket
- **Module doc:** [FR-20_Support_Ticket.md](FR-20_Support_Ticket.md)
- **Key checks:** SLA definitions, escalation matrix, ticket lifecycle, customer communications.
- **Outstanding items:** Add sample SLA tables and notification templates.
- **Signoff:** Product: ______  Support: ______  BA: ______  Date: ______

## FR-21 Audit & Compliance
- **Module doc:** [FR-21_Audit_Compliance.md](FR-21_Audit_Compliance.md)
- **Key checks:** Audit event schema, retention policy, export/attestation processes, regulatory mappings.
- **Outstanding items:** Author BR-AUD-*; finalize audit event list and retention durations.
- **Signoff:** Product: ______  Security: ______  BA: ______  Date: ______

---

How to use these checklists
- Assign an owner and update each checkbox with evidence links. Once all checks are complete and BRs are authored, request signoffs and move the module status to `Frozen` per `FR-01_FRS_Standards.md`.
