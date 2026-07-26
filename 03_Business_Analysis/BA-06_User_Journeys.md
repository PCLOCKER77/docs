# BA-06 User Journeys

**Document ID:** BA-06  
**Document Name:** User Journeys  
**Product:** Digitize by OrieOn Technologies Pvt. Ltd.
**Document Type:** Business Analysis  
**Version:** 1.0  
**Status:** Frozen  
**Owner:** Product Management  
**Prepared By:** Product & Business Analysis Team  
**Last Updated:** July 2026

---

# 1. Introduction

The purpose of this document is to describe the end-to-end journeys experienced by each user persona while interacting with the Digitize platform.

Unlike Business Process Flows, which focus on organizational workflows and business execution, User Journeys focus on the sequence of actions, decisions, interactions, and outcomes from the perspective of an individual user.

This document provides the behavioral foundation for:

- UX Design
- UI Navigation
- Screen Design
- User Story Creation
- Acceptance Criteria
- Usability Testing

---

# 2. User Journey Standards

## 2.1 Journey Documentation Standard

Every journey in this document shall follow the same structure.

- Purpose
- Primary Persona
- Supporting Personas
- Business Goal
- Trigger
- Preconditions
- Journey Steps
- Decision Points
- Alternate Journey
- Exception Journey
- Postconditions
- Notifications
- Pain Points
- UX Considerations
- Success Criteria
- Related Business Processes
- Related Personas
- Related Screens
- Related APIs
- Journey Diagram
- Notes

## 2.2 Journey Design Principles

- Journeys shall reflect the actual user experience, not only the backend workflow.
- Journeys shall remain aligned with the business hierarchy and persona definitions.
- Journeys must respect role-based access and tenant boundaries.
- Journeys should minimize friction for high-volume operational users.
- Journeys should preserve auditability for commercially or operationally significant actions.
- Future enhancements may expand journey paths without changing core journey intent.

## 2.3 Journey Traceability

This document aligns user journeys with business process domains, workflow flows, personas, business rules, and business capability and functional scope.

| Journey | BA-03 Process Domain | BA-04 Flow | BA-05 Persona | BA-02 Rule Category | BA-01 Business Module |
|---|---|---|---|---|---|
| Platform Administrator Journey | Platform Processes | Platform Administration Flow | Platform Administrator | Platform | Platform Administration |
| Organization Administrator Journey | Organization Processes | Organization Management Flow | Organization Administrator | Organization | Organization Management |
| Facility Manager Journey | Facility Processes | Facility Management Flow | Facility Manager | Facility | Organization Management |
| Site Administrator Journey | Site Processes | Site Management Flow | Site Administrator | Site | Organization Management |
| Reception Staff Journey | Customer, Membership, Attendance, Billing, Payment Processes | Customer Registration & Management Flow; Membership Purchase Flow; Attendance Management Flow; Billing Management Flow; Payment Management Flow | Reception Staff | Customer; Membership; Attendance; Billing; Payment | Customer Management; Membership Management; Attendance Management; Commercial Management |
| Trainer Journey | Activity & Batch Processes; Personal Training Processes | Activity Management Flow; Batch Management Flow; Personal Training Flow | Trainer | Trainer | Training Management |
| Finance Staff Journey | Billing Processes; Payment Processes | Billing Management Flow; Payment Management Flow; Invoice Management Flow; Refund Management Flow | Finance Staff | Billing; Payment | Commercial Management |
| Marketing Staff Journey | Advertisement Campaign Processes | Advertisement Campaign Flow | Marketing Staff | Commercial | Communication Management |
| Support Executive Journey | Support Ticket Processes | Support Ticket Management Flow | Support Executive | Security; Audit | Support Management |
| Customer Journey | Customer Processes | Customer Journey | Customer | Customer | Customer Management |

---

# 3. Platform Administrator Journey

## Purpose

Describe how the Platform Administrator governs the SaaS platform from global configuration through monitoring, subscription management, and operational review.

## Primary Persona

Platform Administrator

## Supporting Personas

System, Organization Administrator, Audit Service, Notification Service

## Business Goal

Maintain platform stability, govern tenant onboarding, manage global configuration, and ensure the commercial and security posture of the platform remains consistent.

## Trigger

The Platform Administrator logs in, receives an alert, or needs to review platform governance activity.

## Preconditions

- Platform Administrator account is active.
- MFA or other security controls are satisfied where enabled.
- Platform access is available.

## Journey Steps

1. The Platform Administrator signs in to the platform administration portal.
2. The dashboard presents platform health, tenant metrics, commercial metrics, and active alerts.
3. The administrator reviews pending organization onboarding or lifecycle items.
4. The administrator updates platform configuration, subscription plans, license templates, or feature flags as required.
5. The administrator reviews audit and security information.
6. The system persists changes and records the activity.

## Decision Points

- Is the platform healthy?
- Does an onboarding request require approval?
- Does a commercial or security change require a policy review?

## Alternate Journey

If no action is required, the administrator may only review reports and return to the dashboard without making changes.

## Exception Journey

If authentication fails or permissions are missing, access is denied and the event is recorded in the audit log.

## Postconditions

- Platform status is reviewed.
- Any approved configuration changes are saved.
- Audit records are generated.

## Notifications

- Platform alerts
- Organization onboarding requests
- Security notifications
- Scheduled maintenance notices

## Pain Points

- Large scope of responsibility.
- Need for fast incident awareness.
- Avoiding tenant-wide impact from configuration changes.

## UX Considerations

- Present critical indicators first.
- Use highly structured navigation for administrative tasks.
- Require explicit confirmation for high-risk actions.

## Success Criteria

- Platform state remains stable and governed.
- Administrative actions are traceable.
- Critical alerts are acted on promptly.

## Related Business Processes

- Platform Administration
- Subscription Management
- License Management
- Audit & Compliance

## Related Personas

- Platform Administrator
- Organization Administrator

## Related Screens

- Platform Dashboard
- Subscription Plan Management
- License Template Management
- Feature Management
- Audit Logs

## Related APIs

- Platform Configuration API
- Subscription API
- License API
- Audit API
- Notification API

## Journey Diagram

```text
Login -> Dashboard -> Review Alerts -> Manage Configuration -> Review Audit -> Exit
```

## Notes

This is the highest-privilege journey in the platform.

---

# 4. Organization Administrator Journey

## Purpose

Describe how the Organization Administrator manages tenant governance, operational configuration, staff access, facilities, sites, and organization-wide reporting.

## Primary Persona

Organization Administrator

## Supporting Personas

Platform Administrator, Facility Manager, Site Administrator, Reception Staff, Audit Service

## Business Goal

Maintain centralized control of the tenant organization while enabling efficient operational execution across subordinate facilities and sites.

## Trigger

The administrator opens the organization dashboard, receives an approval request, or needs to update organization governance.

## Preconditions

- Organization is active.
- Administrator account is active.
- Authorization scope covers the organization.

## Journey Steps

1. Sign in and open the organization dashboard.
2. Review organizational summary, facilities, sites, staff, and alerts.
3. Update organization profile, settings, business policies, branding, or documents.
4. Approve or review changes requiring governance.
5. Manage facilities, sites, and staff access.
6. Review reports and follow up on exceptions.

## Decision Points

- Does the requested action require approval?
- Is the target facility or site within scope?
- Is the change policy compliant?

## Alternate Journey

The administrator may move directly to reports or governance tasks without changing configuration.

## Exception Journey

If validation fails, the system blocks the action and shows the reason with audit logging.

## Postconditions

- Organization configuration is updated or reviewed.
- Governance actions are recorded.
- Relevant teams receive notifications.

## Notifications

- Approval requests
- Policy update notices
- Facility and site alerts
- Document status updates

## Pain Points

- Managing multiple facilities and sites.
- Ensuring consistent policy enforcement.
- Coordinating approvals without slowing operations.

## UX Considerations

- Provide a consolidated organization dashboard.
- Highlight exceptions and pending approvals.
- Make policy and configuration status immediately visible.

## Success Criteria

- Organization remains well governed and operationally visible.
- Configuration is current and compliant.
- Staff and business units are managed effectively.

## Related Business Processes

- Organization Management
- Facility Management
- Site Management
- Staff Identity & Access
- Approval Workflow

## Related Personas

- Organization Administrator
- Facility Manager
- Site Administrator

## Related Screens

- Organization Dashboard
- Organization Profile
- Business Policy Management
- Facility Dashboard
- Site Dashboard

## Related APIs

- Organization API
- Facility API
- Site API
- Approval Workflow API
- Reporting API

## Journey Diagram

```text
Login -> Org Dashboard -> Review/Configure -> Approve -> Monitor -> Exit
```

## Notes

This journey is the tenant governance hub for the platform.

---

# 5. Facility Manager Journey

## Purpose

Describe how the Facility Manager manages daily facility operations, service delivery, capacity, and performance.

## Primary Persona

Facility Manager

## Supporting Personas

Organization Administrator, Site Administrator, Trainer, Reception Staff

## Business Goal

Run the facility efficiently while maintaining service quality, capacity control, and operational readiness.

## Trigger

The Facility Manager opens the facility dashboard or receives an operational alert.

## Preconditions

- Facility is active.
- Manager is assigned to the facility.
- Operational data is available.

## Journey Steps

1. Open the facility dashboard.
2. Review utilization, attendance, activity, and batch status.
3. Check capacity and trainer assignments.
4. Resolve operational issues or escalate exceptions.
5. Review facility reports and trends.

## Decision Points

- Is the facility operating within capacity?
- Are trainers and batches aligned?
- Does the issue require organizational escalation?

## Alternate Journey

If no issue exists, the manager performs monitoring only and exits after reviewing performance data.

## Exception Journey

If the facility is inactive or inaccessible, the manager is prevented from performing operational actions.

## Postconditions

- Facility status is understood and monitored.
- Operational decisions are made or escalated.

## Notifications

- Capacity alerts
- Schedule changes
- Batch exceptions
- Facility warnings

## Pain Points

- Capacity pressure.
- Resource coordination.
- Schedule instability.

## UX Considerations

- Surface daily operational summaries.
- Highlight bottlenecks and anomalies.
- Make batch and capacity status easy to interpret.

## Success Criteria

- Facility operations remain controlled and visible.
- Issues are handled before they affect customers.

## Related Business Processes

- Facility Management
- Activity Management
- Batch Management
- Attendance Management

## Related Personas

- Facility Manager
- Site Administrator
- Trainer

## Related Screens

- Facility Dashboard
- Batch Schedule
- Capacity Overview
- Activity Performance

## Related APIs

- Facility API
- Batch API
- Attendance API
- Reporting API

## Journey Diagram

```text
Open Dashboard -> Review Status -> Resolve Issues -> Review Reports -> Exit
```

## Notes

The facility journey is performance-centric and operationally intensive.

---

# 6. Site Administrator Journey

## Purpose

Describe how the Site Administrator manages branch-level execution, local settings, site operations, and local compliance.

## Primary Persona

Site Administrator

## Supporting Personas

Organization Administrator, Facility Manager, Reception Staff, Trainer

## Business Goal

Keep the branch operational, compliant, and ready to serve customers.

## Trigger

The Site Administrator opens the site dashboard or receives a local operational notification.

## Preconditions

- Site is active.
- Access scope includes the site.
- Parent facility is active.

## Journey Steps

1. Open the site dashboard.
2. Review attendance, occupancy, schedule, and site alerts.
3. Update site settings or operating hours where permitted.
4. Coordinate local operational issues.
5. Review site-level reports.

## Decision Points

- Is the site within policy and capacity limits?
- Does the issue require facility-level escalation?

## Alternate Journey

The administrator may only monitor the site without changing any configuration.

## Exception Journey

If site access is not permitted, the journey is blocked and logged.

## Postconditions

- Site status is reviewed.
- Local operational actions are executed or escalated.

## Notifications

- Site warnings
- Capacity alerts
- Schedule changes
- Attendance exceptions

## Pain Points

- Local disruptions.
- Capacity constraints.
- Limited control compared with organization-level roles.

## UX Considerations

- Prioritize branch-specific operational metrics.
- Make local exceptions easy to surface.
- Keep inherited vs. local configuration clear.

## Success Criteria

- The site operates smoothly and stays within policy.

## Related Business Processes

- Site Management
- Attendance Management
- Activity & Batch Management

## Related Personas

- Site Administrator
- Site Manager
- Reception Staff

## Related Screens

- Site Dashboard
- Site Settings
- Site Operating Hours
- Site Capacity

## Related APIs

- Site API
- Attendance API
- Notification API

## Journey Diagram

```text
Open Site Dashboard -> Review Metrics -> Update Local Settings -> Monitor -> Exit
```

## Notes

This journey is branch-focused and constrained by inherited facility rules.

---

# 7. Reception Staff Journey

## Purpose

Describe how Reception Staff handles front-office customer service, membership transactions, attendance, billing, and payment collection.

## Primary Persona

Reception Staff

## Supporting Personas

Customer, Finance Staff, Trainer, Site Administrator, Support Executive

## Business Goal

Serve customers quickly and accurately while maintaining complete operational records.

## Trigger

A customer arrives, calls, books, renews, pays, or requests service at the front desk.

## Preconditions

- User is authenticated.
- Customer and service context are available.
- Required permissions are granted.

## Journey Steps

1. Search or register the customer.
2. Review membership, attendance, and service eligibility.
3. Create or renew membership where needed.
4. Record attendance or walk-in access.
5. Generate invoice and collect payment.
6. Confirm completion and issue communication.

## Decision Points

- Is the customer eligible for service?
- Is payment required now?
- Is the visit a walk-in or membership-based?

## Alternate Journey

The staff member may perform only lookup, only attendance, or only payment tasks depending on the visit.

## Exception Journey

If eligibility, pricing, or payment validation fails, the transaction is paused and the customer is informed.

## Postconditions

- Customer transaction is completed or appropriately deferred.
- Records are updated and auditable.

## Notifications

- Membership confirmations
- Attendance confirmations
- Payment confirmations
- Schedule reminders

## Pain Points

- Queue pressure.
- Repeated customer lookups.
- Handling exceptions at the counter.

## UX Considerations

- Minimize clicks and screen hops.
- Provide strong search and quick-action workflows.
- Make service eligibility highly visible.

## Success Criteria

- Customer service is fast, accurate, and complete.

## Related Business Processes

- Customer Management
- Membership Management
- Attendance Management
- Billing Management
- Payment Management

## Related Personas

- Customer
- Finance Staff
- Trainer

## Related Screens

- Customer Search
- Customer Profile
- Membership Purchase
- Attendance Check-in
- Invoice Management
- Payment Collection

## Related APIs

- Customer API
- Membership API
- Attendance API
- Billing API
- Payment API

## Journey Diagram

```text
Search/Register -> Validate -> Transact -> Confirm -> Notify
```

## Notes

This is one of the highest-volume operational journeys in the platform.

---

# 8. Trainer Journey

## Purpose

Describe how a Trainer delivers sessions, manages customer progress, and supports scheduled coaching operations.

## Primary Persona

Trainer

## Supporting Personas

Reception Staff, Facility Manager, Customer, Site Administrator

## Business Goal

Deliver reliable, well-documented training sessions and support customer progress.

## Trigger

A session begins, a schedule changes, or the trainer needs to record training outcomes.

## Preconditions

- Trainer account is active.
- Session or booking exists.
- Schedule access is available.

## Journey Steps

1. Review the schedule and assigned customers.
2. Start the session.
3. Deliver the training activity.
4. Record attendance or completion.
5. Add notes and progress updates.
6. End the session and review follow-up tasks.

## Decision Points

- Is the customer present?
- Has the session started on time?
- Does the session need to be rescheduled or cancelled?

## Alternate Journey

The trainer may only review upcoming work or update progress without starting a session.

## Exception Journey

If the trainer is unavailable or the session cannot proceed, the cancellation or reschedule flow is triggered.

## Postconditions

- Session status is updated.
- Progress and notes are retained.

## Notifications

- Session reminders
- Schedule changes
- Customer cancellations

## Pain Points

- Session disruptions.
- Missing customer context.
- Limited time between sessions.

## UX Considerations

- Emphasize schedule clarity.
- Make note-taking fast and structured.
- Support progress capture without interrupting session flow.

## Success Criteria

- Sessions are completed successfully and documented accurately.

## Related Business Processes

- Activity & Batch Management
- Personal Training
- Attendance Management

## Related Personas

- Trainer
- Reception Staff
- Customer

## Related Screens

- Session Schedule
- Training Session
- Training Notes
- Customer Progress

## Related APIs

- Personal Training API
- Attendance API
- Notification API

## Journey Diagram

```text
Review Schedule -> Start Session -> Deliver Coaching -> Capture Notes -> Close Session
```

## Notes

Trainer journeys are execution-heavy and require minimal disruption.

---

# 9. Finance Staff Journey

## Purpose

Describe how Finance Staff manages invoices, payments, refunds, reconciliation, and receivables.

## Primary Persona

Finance Staff

## Supporting Personas

Reception Staff, Organization Administrator, Payment Gateway, Support Executive

## Business Goal

Maintain financial accuracy and settlement integrity across the organization.

## Trigger

An invoice is due, a payment is received, a refund is requested, or reconciliation is required.

## Preconditions

- Financial data exists.
- Payment and billing configuration is active.
- User is authenticated.

## Journey Steps

1. Review invoices, outstanding balances, and payment queues.
2. Collect or verify payments.
3. Generate receipts and update statuses.
4. Process refunds or billing adjustments if approved.
5. Reconcile transactions and review variances.

## Decision Points

- Is the payment settled or pending?
- Is a refund eligible?
- Does the reconciliation match expected balances?

## Alternate Journey

The finance user may focus only on reconciliation or reporting during a given session.

## Exception Journey

If payment validation or refund processing fails, the item is retained for follow-up and audit.

## Postconditions

- Financial records are updated.
- Outstanding balances are visible.
- Audit trail is preserved.

## Notifications

- Payment confirmations
- Refund notices
- Outstanding balance alerts
- Reconciliation exceptions

## Pain Points

- Cross-channel payment reconciliation.
- Handling partial payments.
- Ensuring policy-compliant refunds.

## UX Considerations

- Show financial summaries and exceptions first.
- Keep invoice, receipt, and payment views connected.
- Make reconciliation and exception handling efficient.

## Success Criteria

- Financial records remain accurate and traceable.

## Related Business Processes

- Billing Management
- Payment Management
- Invoice Management
- Refund Management

## Related Personas

- Finance Staff
- Reception Staff
- Organization Administrator

## Related Screens

- Invoice Management
- Payment Collection
- Refund Management
- Reconciliation

## Related APIs

- Billing API
- Payment API
- Refund API
- Invoice API

## Journey Diagram

```text
Review Balances -> Collect/Verify -> Resolve Exceptions -> Reconcile -> Close
```

## Notes

This journey is financially sensitive and must remain auditable end-to-end.

---

# 10. Marketing Staff Journey

## Purpose

Describe how Marketing Staff creates campaigns, targets audiences, obtains approvals, and reviews performance.

## Primary Persona

Marketing Staff

## Supporting Personas

Organization Administrator, Notification Service, Support Executive

## Business Goal

Promote services effectively while staying aligned with governance and communication policies.

## Trigger

A campaign needs to be launched, updated, paused, or evaluated.

## Preconditions

- Campaign tools are available.
- Audience data and communication channels are configured.
- Approval rules are defined.

## Journey Steps

1. Draft the campaign.
2. Select the target audience.
3. Configure content, timing, and channels.
4. Submit for approval.
5. Launch after approval and monitor delivery.
6. Review performance and close the campaign.

## Decision Points

- Does the campaign require approval?
- Is the audience eligible and reachable?
- Should the campaign be paused or rescheduled?

## Alternate Journey

The marketer may work only on audience selection or only on reporting analysis.

## Exception Journey

If a campaign is rejected or delivery fails, the marketer revises the content or schedule and resubmits.

## Postconditions

- Campaign status is updated.
- Performance is measurable.

## Notifications

- Approval updates
- Delivery updates
- Campaign completion notices

## Pain Points

- Approval lead times.
- Audience precision.
- Measuring campaign impact.

## UX Considerations

- Provide a guided campaign builder.
- Show audience and channel validation clearly.
- Present performance data in a decision-friendly format.

## Success Criteria

- Campaigns are approved, delivered, and measurable.

## Related Business Processes

- Advertisement Campaign
- Notification Management
- Approval Workflow
- Reporting & Analytics

## Related Personas

- Marketing Staff
- Organization Administrator

## Related Screens

- Campaign Builder
- Audience Selection
- Campaign Schedule
- Campaign Analytics

## Related APIs

- Campaign API
- Notification API
- Approval Workflow API
- Reporting API

## Journey Diagram

```text
Draft -> Segment Audience -> Approve -> Launch -> Monitor -> Close
```

## Notes

Campaigns should remain governed, targeted, and measurable.

---

# 11. Support Executive Journey

## Purpose

Describe how Support Executives handle support tickets from assignment through resolution and closure.

## Primary Persona

Support Executive

## Supporting Personas

Support Administrator, Customer, Reception Staff, Organization Administrator

## Business Goal

Resolve issues efficiently while preserving communication history and SLA compliance.

## Trigger

A support ticket is assigned, escalated, or needs investigation.

## Preconditions

- Ticket exists.
- User is authenticated.
- Access to the ticket scope is granted.

## Journey Steps

1. Open the assigned ticket queue.
2. Review ticket details, priority, and SLA state.
3. Investigate the issue and communicate with the customer or staff.
4. Update progress notes and request information if needed.
5. Resolve the ticket and prepare closure.

## Decision Points

- Is more information required?
- Does the issue require escalation?
- Is the ticket ready for closure?

## Alternate Journey

The executive may handle only communication or only resolution documentation.

## Exception Journey

If the issue cannot be resolved within scope, it is escalated to the next level.

## Postconditions

- Ticket status is updated.
- Communication history is preserved.

## Notifications

- New ticket assignments
- Escalations
- Customer responses
- SLA warnings

## Pain Points

- Incomplete tickets.
- SLA pressure.
- Multiple follow-ups.

## UX Considerations

- Show ticket history and SLA timing prominently.
- Keep customer communication and internal notes distinct.
- Make status transitions explicit.

## Success Criteria

- Tickets are resolved on time and with complete history.

## Related Business Processes

- Support Ticket Management
- Notification Management
- Audit & Compliance

## Related Personas

- Support Executive
- Support Administrator
- Customer

## Related Screens

- Support Ticket Queue
- Ticket Details
- Escalation View
- Ticket History

## Related APIs

- Support Ticket API
- Notification API
- Audit API

## Journey Diagram

```text
Open Ticket -> Investigate -> Communicate -> Resolve -> Close
```

## Notes

Support journeys must preserve the full issue history for traceability.

---

# 12. Customer Journey

## Purpose

Describe how the Customer experiences the platform from registration through ongoing service consumption and support.

## Primary Persona

Customer

## Supporting Personas

Reception Staff, Trainer, Finance Staff, Support Executive, System

## Business Goal

Enable the customer to access services smoothly, understand entitlements clearly, and interact with the organization without friction.

## Trigger

The customer registers, visits the facility, attends a session, makes a payment, or raises a support request.

## Preconditions

- Customer profile exists or can be created.
- Services are available.
- Customer is eligible for the requested action.

## Journey Steps

1. Register or identify the customer.
2. Review service eligibility and membership status.
3. Purchase or renew services where needed.
4. Attend sessions or use walk-in services.
5. Receive notifications, receipts, and support responses.

## Decision Points

- Is the customer eligible for the requested service?
- Is payment or renewal required?
- Does the customer need support or follow-up?

## Alternate Journey

The customer may only browse information, receive notifications, or contact support without completing a transaction.

## Exception Journey

If entitlement, payment, or capacity validation fails, the customer is informed and the journey pauses or ends based on policy.

## Postconditions

- Customer records remain current.
- Service participation is tracked.
- Communication history is preserved.

## Notifications

- Registration confirmations
- Membership reminders
- Attendance confirmations
- Payment receipts
- Support updates

## Pain Points

- Confusing entitlement status.
- Delayed communication.
- Difficulty understanding the next step.

## UX Considerations

- Keep the journey simple and transparent.
- Surface entitlement, payments, and schedules clearly.
- Provide timely, actionable notifications.

## Success Criteria

- Customer can complete tasks with minimal friction.
- Service status is clear and reliable.

## Related Business Processes

- Customer Registration & Management
- Membership Management
- Attendance Management
- Billing Management
- Payment Management
- Support Ticket Management

## Related Personas

- Customer
- Reception Staff
- Trainer

## Related Screens

- Customer Dashboard
- Membership Details
- Attendance History
- Payment History
- Notifications

## Related APIs

- Customer API
- Membership API
- Attendance API
- Billing API
- Payment API
- Notification API

## Journey Diagram

```text
Register -> Purchase/Renew -> Attend -> Receive Updates -> Support if Needed
```

## Notes

The customer journey is the central value path of the platform.

---

# 13. Organization Onboarding Journey

## Purpose

Describe the path used to onboard a new customer organization into Digitize.

## Primary Persona

Platform Administrator

## Supporting Personas

Organization Administrator, System, Notification Service

## Business Goal

Create a valid tenant organization with commercial and operational readiness.

## Trigger

A new organization is approved for onboarding.

## Preconditions

- Subscription plan exists.
- Required license templates exist.
- Organization information is available.

## Journey Steps

1. Receive onboarding request.
2. Validate organization information.
3. Create organization profile and administrator account.
4. Assign subscription plan and generate license.
5. Configure initial settings and activate the organization.

## Decision Points

- Is the organization valid?
- Is commercial approval complete?
- Is license generation successful?

## Alternate Journey

If commercial approval is pending, the organization remains in draft until prerequisites are complete.

## Exception Journey

If validation or license generation fails, onboarding is halted and corrected before retry.

## Postconditions

- Organization is active.
- Subscription and license are linked.
- Audit history is created.

## Notifications

- Onboarding approvals
- Administrator account creation
- Subscription activation
- License generation

## Pain Points

- Document validation.
- Commercial coordination.
- Activation dependencies.

## UX Considerations

- Use a guided onboarding flow.
- Show dependency completion clearly.
- Keep status visible at each stage.

## Success Criteria

- The organization becomes operational without ambiguity or incomplete setup.

## Related Business Processes

- Organization Onboarding
- Subscription Management
- License Management

## Related Personas

- Platform Administrator
- Organization Administrator

## Related Screens

- Organization Registration
- Subscription Management
- License Management

## Related APIs

- Organization API
- Subscription API
- License API

## Journey Diagram

```text
Request -> Validate -> Create Org -> Assign Plan -> Generate License -> Activate
```

## Notes

This journey is the tenant entry point for the platform.

---

# 14. Membership Purchase Journey

## Purpose

Describe the customer-facing journey for acquiring a new membership.

## Primary Persona

Reception Staff

## Supporting Personas

Customer, Billing Service, Payment Gateway, System

## Business Goal

Create a valid membership entitlement and settle the associated commercial obligation.

## Trigger

A customer requests a membership or a staff member initiates membership purchase.

## Preconditions

- Customer exists.
- Plan exists.
- Payment and billing configuration is active.

## Journey Steps

1. Select customer.
2. Choose membership plan.
3. Configure terms and pricing.
4. Validate eligibility.
5. Collect payment if required.
6. Activate membership and confirm completion.

## Decision Points

- Is the customer eligible?
- Is payment required immediately?
- Is the plan available?

## Alternate Journey

If payment is not required immediately, the membership may remain pending until policy conditions are met.

## Exception Journey

If eligibility or payment validation fails, the membership is not activated.

## Postconditions

- Membership is created and tracked.
- Billing and payment state is updated.

## Notifications

- Membership purchase confirmation
- Payment request
- Activation notice

## Pain Points

- Plan selection complexity.
- Payment failures.
- Eligibility confusion.

## UX Considerations

- Present the plan, validity, and payment impact clearly.
- Keep validation feedback immediate.

## Success Criteria

- Membership is created accurately and can be used immediately where allowed.

## Related Business Processes

- Membership Purchase
- Billing Management
- Payment Management

## Related Personas

- Reception Staff
- Customer

## Related Screens

- Membership Purchase
- Plan Selection
- Billing Checkout

## Related APIs

- Membership API
- Billing API
- Payment API

## Journey Diagram

```text
Select Customer -> Select Plan -> Validate -> Pay -> Activate
```

## Notes

This journey is one of the most commercially important customer operations.

---

# 15. Membership Renewal Journey

## Purpose

Describe the journey for extending an existing membership period.

## Primary Persona

Reception Staff

## Supporting Personas

Customer, Billing Service, Payment Gateway, System

## Business Goal

Preserve service continuity by renewing entitlements in a controlled and auditable way.

## Trigger

A membership is nearing expiry or renewal is requested.

## Preconditions

- Membership exists.
- Renewal is permitted by policy.
- Billing rules are configured.

## Journey Steps

1. Open membership details.
2. Review renewal eligibility.
3. Configure renewal terms.
4. Generate charges and collect payment if required.
5. Extend validity and confirm renewal.

## Decision Points

- Is the membership eligible for renewal?
- Is the renewal before or after expiry?

## Alternate Journey

Renewal may be scheduled or deferred based on policy.

## Exception Journey

If payment fails or the membership is ineligible, renewal remains pending or is rejected.

## Postconditions

- Membership validity is extended.
- Renewal history is recorded.

## Notifications

- Renewal reminder
- Renewal confirmation
- Payment notice

## Pain Points

- Expiry timing.
- Payment failure.
- Renewal policy variance.

## UX Considerations

- Make expiry and renewal windows highly visible.
- Surface the renewal cost before confirmation.

## Success Criteria

- Membership continuity is preserved without data loss.

## Related Business Processes

- Membership Renewal
- Billing Management
- Payment Management

## Related Personas

- Reception Staff
- Customer

## Related Screens

- Membership Details
- Renewal Screen
- Billing Checkout

## Related APIs

- Membership API
- Billing API
- Payment API

## Journey Diagram

```text
Open Membership -> Review Renewal -> Charge -> Pay -> Extend Validity
```

## Notes

Renewal must preserve historical continuity.

---

# 16. Walk-in Customer Journey

## Purpose

Describe the journey for a customer who accesses a facility without an active membership.

## Primary Persona

Reception Staff

## Supporting Personas

Customer, Billing Service, Payment Gateway, System

## Business Goal

Provide controlled single-visit access while maintaining separate walk-in history and billing.

## Trigger

A non-member requests facility access.

## Preconditions

- Walk-in access is enabled.
- Capacity is available.

## Journey Steps

1. Identify or register the walk-in customer.
2. Validate capacity and pricing.
3. Record the walk-in visit.
4. Collect payment if required.
5. Record attendance and confirm access.

## Decision Points

- Is the customer already known?
- Is walk-in allowed?
- Is payment required immediately?

## Alternate Journey

The visit may be complimentary or may require registration first.

## Exception Journey

If walk-in access is blocked or capacity is full, the visit does not proceed.

## Postconditions

- Walk-in visit is recorded.
- Payment and attendance are stored separately from membership usage.

## Notifications

- Visit confirmation
- Payment receipt
- Access denied notice

## Pain Points

- Speed of registration.
- Payment at the counter.
- Capacity-based rejection handling.

## UX Considerations

- Make the walk-in flow fast and minimal.
- Keep walk-in records clearly distinct from memberships.

## Success Criteria

- Walk-in access is recorded and billed correctly.

## Related Business Processes

- Walk-in Customer Flow
- Attendance Management
- Billing Management
- Payment Management

## Related Personas

- Reception Staff
- Customer

## Related Screens

- Walk-in Registration
- Attendance Check-in
- Billing Checkout

## Related APIs

- Walk-in API
- Attendance API
- Billing API
- Payment API

## Journey Diagram

```text
Identify -> Validate -> Register Visit -> Pay -> Check In
```

## Notes

Walk-in journeys must remain distinct from membership journeys.

---

# 17. Attendance Journey

## Purpose

Describe the journey for recording customer attendance for sessions, visits, or service usage.

## Primary Persona

Reception Staff

## Supporting Personas

Customer, Trainer, System

## Business Goal

Capture accurate participation data for operations, billing, and reporting.

## Trigger

A customer arrives for service or a session begins.

## Preconditions

- Customer and service context exist.
- Eligibility and capacity checks are available.

## Journey Steps

1. Identify the customer.
2. Validate membership or service eligibility.
3. Record check-in.
4. Optionally record check-out.
5. Confirm completion and store history.

## Decision Points

- Is the customer eligible?
- Is this a session, walk-in, or membership visit?

## Alternate Journey

Attendance may be corrected or cancelled by authorized users later.

## Exception Journey

If eligibility fails or capacity is exceeded, attendance is denied.

## Postconditions

- Attendance history is updated.
- Related operational records are synchronized.

## Notifications

- Check-in confirmation
- Attendance denial
- Check-out confirmation

## Pain Points

- Fast processing during peak hours.
- Validation issues.
- Duplicate entry handling.

## UX Considerations

- Optimize for speed.
- Make eligibility status obvious before confirmation.

## Success Criteria

- Attendance is captured accurately and on time.

## Related Business Processes

- Attendance Management
- Membership Management
- Activity & Batch Management

## Related Personas

- Reception Staff
- Trainer
- Customer

## Related Screens

- Attendance Check-in
- Attendance Check-out
- Attendance History

## Related APIs

- Attendance API
- Membership API
- Customer API

## Journey Diagram

```text
Identify -> Validate -> Check In -> Check Out -> Archive History
```

## Notes

Attendance is the operational proof of service consumption.

---

# 18. Personal Training Journey

## Purpose

Describe the journey for booking, delivering, and documenting personal training sessions.

## Primary Persona

Trainer

## Supporting Personas

Reception Staff, Customer, System

## Business Goal

Deliver premium coaching services while maintaining progress and session continuity.

## Trigger

A session is booked, begins, or needs to be updated.

## Preconditions

- Training package exists.
- Trainer is assigned.
- Customer is eligible.

## Journey Steps

1. Review the booking or schedule.
2. Start the session.
3. Deliver coaching.
4. Record notes and progress.
5. Complete the session and confirm follow-up needs.

## Decision Points

- Is the customer present?
- Does the session need rescheduling?
- Are notes or progress updates required?

## Alternate Journey

The session may be rescheduled or cancelled if the trainer or customer is unavailable.

## Exception Journey

If the session cannot proceed, the booking is updated and the customer is notified.

## Postconditions

- Session status is updated.
- Training history is preserved.

## Notifications

- Booking confirmation
- Reminder
- Reschedule notice
- Completion notice

## Pain Points

- Session overlap.
- Rescheduling complexity.
- Need for accurate coaching notes.

## UX Considerations

- Keep session actions close to the schedule.
- Make note capture fast and structured.

## Success Criteria

- Sessions are completed with reliable progress tracking.

## Related Business Processes

- Personal Training
- Attendance Management
- Billing Management

## Related Personas

- Trainer
- Reception Staff
- Customer

## Related Screens

- Training Schedule
- Session Detail
- Training Notes

## Related APIs

- Personal Training API
- Attendance API
- Notification API

## Journey Diagram

```text
Book -> Start -> Coach -> Record Progress -> Complete
```

## Notes

Personal training requires a high level of service continuity and documentation quality.

---

# 19. Payment Journey

## Purpose

Describe the journey for settling invoices and handling payment outcomes.

## Primary Persona

Finance Staff

## Supporting Personas

Reception Staff, Payment Gateway, System, Customer

## Business Goal

Complete payment collection securely and reconcile the commercial record accurately.

## Trigger

An invoice is due or a payment is initiated.

## Preconditions

- Valid invoice exists.
- Payment method is available.

## Journey Steps

1. Open the invoice or payment queue.
2. Select the payment method.
3. Collect or process the payment.
4. Verify the transaction.
5. Generate a receipt and update the invoice.

## Decision Points

- Is the payment successful?
- Is the payment partial?
- Does the transaction require refund handling later?

## Alternate Journey

Payment may be processed online, in cash, or via other configured channels.

## Exception Journey

If payment fails, the invoice remains unsettled and the issue is retained for follow-up.

## Postconditions

- Payment status is recorded.
- Invoice status is updated.

## Notifications

- Payment received
- Payment failed
- Receipt issued

## Pain Points

- Multi-channel reconciliation.
- Payment failures.
- Receipt generation accuracy.

## UX Considerations

- Make invoice-to-payment linking obvious.
- Show outstanding balances clearly.

## Success Criteria

- Payment is collected and settled without ambiguity.

## Related Business Processes

- Payment Management
- Billing Management
- Invoice Management

## Related Personas

- Finance Staff
- Reception Staff
- Customer

## Related Screens

- Payment Collection
- Payment History
- Receipt View

## Related APIs

- Payment API
- Billing API
- Receipt API

## Journey Diagram

```text
Open Invoice -> Collect -> Verify -> Receipt -> Reconcile
```

## Notes

Payment completion should always be traceable back to the source invoice.

---

# 20. Advertisement Campaign Journey

## Purpose

Describe the journey for creating, approving, delivering, and reviewing promotional campaigns.

## Primary Persona

Marketing Staff

## Supporting Personas

Organization Administrator, Notification Service, System

## Business Goal

Deliver targeted campaigns that support acquisition, retention, and customer engagement.

## Trigger

A campaign needs to be launched or updated.

## Preconditions

- Audience and channels are available.
- Approval workflow exists where required.

## Journey Steps

1. Draft the campaign.
2. Define the audience and message.
3. Obtain approval.
4. Schedule and launch delivery.
5. Monitor performance and close the campaign.

## Decision Points

- Is approval required?
- Should the campaign be paused?
- Is delivery on target?

## Alternate Journey

The marketer may use the journey for planning only, without launch.

## Exception Journey

If the campaign is rejected or delivery fails, the marketer revises and resubmits.

## Postconditions

- Campaign history is preserved.
- Performance data is available.

## Notifications

- Approval decisions
- Delivery updates
- Campaign completion

## Pain Points

- Approval delays.
- Targeting accuracy.
- Measuring business value.

## UX Considerations

- Provide a guided builder and clear performance feedback.

## Success Criteria

- Campaigns are compliant, delivered, and measurable.

## Related Business Processes

- Advertisement Campaign
- Notification Management
- Approval Workflow

## Related Personas

- Marketing Staff
- Organization Administrator

## Related Screens

- Campaign Builder
- Audience Selection
- Campaign Analytics

## Related APIs

- Campaign API
- Notification API
- Approval Workflow API

## Journey Diagram

```text
Draft -> Approve -> Schedule -> Launch -> Measure -> Close
```

## Notes

Campaign journeys must remain governed and traceable.

---

# 21. Support Ticket Journey

## Purpose

Describe the journey for reporting, handling, resolving, and closing support tickets.

## Primary Persona

Support Executive

## Supporting Personas

Support Administrator, Customer, Reception Staff, Organization Administrator

## Business Goal

Resolve issues efficiently while keeping customers informed and support history complete.

## Trigger

A support issue is reported or assigned.

## Preconditions

- Ticketing is enabled.
- User has access to the ticket scope.

## Journey Steps

1. Create or receive a ticket.
2. Classify and prioritize the issue.
3. Investigate and respond.
4. Request more information if needed.
5. Resolve, verify, and close the ticket.

## Decision Points

- Is escalation required?
- Is customer input still needed?
- Can the ticket be closed?

## Alternate Journey

The support process may pause while awaiting customer or internal input.

## Exception Journey

If the issue persists or recurs, the ticket may be reopened and reprocessed.

## Postconditions

- Ticket history is preserved.
- Support outcome is recorded.

## Notifications

- Assignment notice
- Escalation notice
- Resolution notice
- Closure notice

## Pain Points

- SLA pressure.
- Incomplete information.
- Cross-team dependencies.

## UX Considerations

- Keep ticket history and SLA timing visible.
- Separate internal notes from customer-facing communication.

## Success Criteria

- Issues are resolved with minimal delays and complete documentation.

## Related Business Processes

- Support Ticket Management

## Related Personas

- Support Executive
- Support Administrator
- Customer

## Related Screens

- Support Ticket Queue
- Ticket Detail
- Escalation View

## Related APIs

- Support Ticket API
- Notification API
- Audit API

## Journey Diagram

```text
Create/Assign -> Investigate -> Resolve -> Close -> Reopen if Needed
```

## Notes

Support journeys should preserve a complete communication trail.

---

# 22. Cross Persona Interaction

Cross persona interaction describes the primary touchpoints between personas during common operational scenarios.

## 22.1 Interaction Themes

- Platform Administrator coordinates with Organization Administrator on onboarding and governance.
- Organization Administrator coordinates with Facility Manager, Site Administrator, Reception Staff, Finance Staff, and Support Executive.
- Reception Staff coordinates with Customers, Trainers, and Finance Staff during service delivery.
- Finance Staff coordinates with Reception Staff, Customers, and Payment services during billing and settlement.
- Support Executive coordinates with Customers and staff across business units to resolve issues.

## 22.2 Interaction Principles

- Higher-level personas govern lower-level personas, but lower-level personas execute operational detail.
- Customer interactions must remain simple, fast, and transparent.
- Cross persona transitions should preserve context and audit history.

---

# 23. Journey Dependency Matrix

| Journey | Depends On |
|---|---|
| Platform Administrator Journey | Platform Administration, Audit & Compliance |
| Organization Administrator Journey | Platform Administration, Organization Management |
| Facility Manager Journey | Organization Management, Facility Management |
| Site Administrator Journey | Facility Management, Site Management |
| Reception Staff Journey | Customer Management, Membership Management, Billing, Payment |
| Trainer Journey | Activity & Batch Management, Personal Training, Attendance Management |
| Finance Staff Journey | Billing Management, Payment Management, Invoice Management, Refund Management |
| Marketing Staff Journey | Advertisement Campaign, Notification Management, Approval Workflow |
| Support Executive Journey | Support Ticket Management, Notification Management, Audit & Compliance |
| Customer Journey | Customer Management, Membership Management, Attendance, Billing, Payment, Support |
| Organization Onboarding Journey | Subscription Management, License Management |
| Membership Purchase Journey | Membership Management, Billing Management, Payment Management |
| Membership Renewal Journey | Membership Management, Billing Management, Payment Management |
| Walk-in Customer Journey | Attendance Management, Billing Management, Payment Management |
| Attendance Journey | Membership Management, Attendance Management |
| Personal Training Journey | Personal Training, Attendance Management, Billing Management |
| Payment Journey | Billing Management, Payment Management |
| Advertisement Campaign Journey | Advertisement Campaign, Notification Management, Approval Workflow |
| Support Ticket Journey | Support Ticket Management |

---

# 24. Journey Pain Points

The following pain points recur across multiple journeys:

- Excessive screen hops for high-volume users.
- Ambiguous entitlement or eligibility states.
- Delayed approvals or operational dependencies.
- Incomplete or inconsistent customer data.
- Payment failures and reconciliation exceptions.
- Lack of visibility into cross-functional status.
- Branch or site scope confusion.
- Fragmented notification and follow-up handling.

---

# 25. Future Journey Enhancements

Future journey enhancements may include:

- Guided wizards for high-volume transactions.
- Role-aware dashboards with contextual action queues.
- Mobile-first customer self-service journeys.
- AI-assisted recommendations for support and operations.
- Automated approval routing and escalation support.
- More advanced integration-driven journeys for partners and external systems.
- Consent-aware guardian journeys for dependent customers.

---

# 26. Summary

The User Journeys document describes how each persona experiences Digitize from an interaction perspective.

It translates enterprise business operations into user-centered sequences that support UX design, screen design, user stories, acceptance criteria, and usability testing.

By standardizing journey structure across all personas and key business scenarios, Digitize can deliver a consistent, role-aware, and scalable experience that supports efficient operations and strong governance across the platform.

**End of BA-06 - User Journeys**
