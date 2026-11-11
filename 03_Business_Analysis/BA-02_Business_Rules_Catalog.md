# BA-02 Business Rules Catalog

**Document ID:** BA-02

**Document Name:** Business Rules Catalog

**Company:** OrieOn Technologies Pvt. Ltd.

**Product:** Digitize

**Document Type:** Business Analysis

**Version:** 1.0

**Status:** Frozen

**Owner:** Business Analysis Team

**Prepared By:** Product Management & Business Analysis

**Last Updated:** July 2026

---

# Table of Contents

## Part 1

1. Document Purpose

2. Business Rule Framework

3. Business Rule Classification

4. Rule Ownership

5. Rule Lifecycle

6. Rule Structure

7. Rule Priority

8. Rule Status

9. Rule Traceability

10. Rule Governance

---

## Part 2

11. Platform Rules

12. Organization Rules

13. Facility Rules

14. Site Rules

---

## Part 3

15. Customer Rules

16. Membership Rules

17. Attendance Rules

18. Trainer Rules

---

## Part 4

19. Subscription Rules

20. Billing Rules

21. Payment Rules

22. Commercial Rules

---

## Part 5

23. Notification Rules

24. Reporting Rules

25. Security Rules

26. Audit Rules

---

## Part 6

27. Rule Versioning

28. Rule Maintenance

29. References

30. Revision History

---

# 1. Document Purpose

The Business Rules Catalog defines the business policies that govern the operation of Digitize.

Business Rules represent decisions made by the business and are independent of software implementation.

These rules ensure consistent business behaviour across all organizations, facilities, operational processes, commercial activities, and platform administration.

Every Functional Requirement, Business Process, API, Database Entity, User Interface, and Test Case shall trace back to one or more Business Rules.

---

# 2. Business Rule Framework

Business Rules within Digitize are governed by the following principles:

* Business owned.
* Technology independent.
* Unambiguous.
* Version controlled.
* Traceable.
* Testable.
* Configurable wherever practical.
* Auditable.
* Consistently enforced.

Business Rules define **what must happen**, while Functional Requirements define **how the software supports those rules**.

---

# 3. Business Rule Classification

Business Rules are classified into the following domains.

| Domain       | Prefix |
| ------------ | ------ |
| Platform     | BR-PLT |
| Organization | BR-ORG |
| Facility     | BR-FAC |
| Site         | BR-SIT |
| Customer     | BR-CUS |
| Membership   | BR-MEM |
| Attendance   | BR-ATT |
| Trainer      | BR-TRN |
| Subscription | BR-SUB |
| Billing      | BR-BIL |
| Payment      | BR-PAY |
| Commercial   | BR-COM |
| Notification | BR-NOT |
| Reporting    | BR-RPT |
| Security     | BR-SEC |
| Audit        | BR-AUD |

Every rule shall have a permanent identifier.

Example:

```text
BR-MEM-001
```

Business Rule Number 001 under the Membership domain.

Rule identifiers are immutable and shall never be reused.

---

# 3.1 Business Rule Categories

In addition to Business Domains, Business Rules are categorized according to their purpose.

| Category | Description |
|-----------|-------------|
| Business Policy | Defines organizational policies. |
| Operational Rule | Governs day-to-day operations. |
| Validation Rule | Validates business data and transactions. |
| Commercial Rule | Governs pricing, subscriptions, and billing. |
| Security Rule | Protects business data and access. |
| Compliance Rule | Supports legal and regulatory requirements. |
| Workflow Rule | Defines process sequencing and approvals. |
---

# 4. Rule Ownership

Every Business Rule shall have a clearly defined owner.

| Owner               | Responsibility                    |
| ------------------- | --------------------------------- |
| Product Management  | Business policy approval          |
| Business Analysis   | Rule definition and documentation |
| Architecture Team   | Technical impact assessment       |
| Engineering         | Software implementation           |
| QA Team             | Rule validation                   |
| Customer Success    | Operational feedback              |
| Business Leadership | Final business approval           |

Ownership ensures accountability throughout the product lifecycle.

---

# 5. Rule Lifecycle

Every Business Rule progresses through the following lifecycle.

```text
Draft
   │
   ▼
Business Review
   │
   ▼
Approved
   │
   ▼
Implemented
   │
   ▼
Verified
   │
   ▼
Production
   │
   ▼
Deprecated (if applicable)
```

Rule changes shall follow the organization's change management process.

---

# 6. Rule Structure

Every Business Rule shall follow the standard structure below.

| Attribute | Description |
|------------|-------------|
| Rule ID | Permanent unique identifier |
| Rule Name | Business rule title |
| Business Domain | Related business domain |
| Business Capability | Related business capability |
| Business Process | Related business process |
| Rule Statement | Business policy |
| Priority | Criticality |
| Configuration | Fixed / Configurable |

This standard structure shall be used consistently across all business rule categories.

---

# 7. Rule Priority

Business Rules are prioritised according to business impact.

| Priority | Definition                                                                            |
| -------- | ------------------------------------------------------------------------------------- |
| Critical | Required for platform operation, legal compliance, security, or commercial integrity. |
| High     | Required for core operational functionality.                                          |
| Medium   | Improves operational efficiency and user experience.                                  |
| Low      | Optional enhancement with limited business impact.                                    |

Priority assists implementation planning and release management.

---

# 8. Rule Status

Each Business Rule shall maintain one of the following statuses.

| Status       | Description                             |
| ------------ | --------------------------------------- |
| Draft        | Rule under preparation.                 |
| Under Review | Awaiting stakeholder approval.          |
| Approved     | Business-approved rule.                 |
| Implemented  | Implemented in software.                |
| Verified     | Successfully validated through testing. |
| Deprecated   | Replaced or retired.                    |

Historical rule versions shall be retained for audit purposes.

---

# 9. Rule Traceability

Business Rules form the foundation of the Digitize traceability model.

```text
Business Objective
        │
        ▼
Business Capability
        │
        ▼
Business Process
        │
        ▼
Business Rule
        │
        ▼
Functional Requirement
        │
        ▼
User Interface
        │
        ▼
API
        │
        ▼
Database
        │
        ▼
Test Case
```

Every implementation artifact shall reference the Business Rule(s) that justify its existence.

---

# 10. Rule Governance

Business Rules are governed according to the following principles:

* Rules shall be uniquely identified.
* Rules shall not duplicate existing policies.
* Rules shall be independently testable.
* Rules shall be reviewed before implementation.
* Rules shall remain independent of software design.
* Rules shall support future platform expansion.
* Rules shall remain backward compatible whenever practical.
* Changes shall be documented through formal version control.

Governance ensures long-term consistency across the Digitize platform.

---

# 11. Business Rule Change Impact

Any modification to an approved Business Rule shall trigger an impact assessment on:

- Business Processes
- Functional Requirements (FRS)
- API Specifications
- Database Design
- User Interface Specifications
- Test Cases
- User Documentation
- Training Materials

---

# 11. Platform Business Rules

Platform Business Rules govern the overall operation of Digitize as a SaaS platform managed by **OrieOn Technologies Pvt. Ltd.**.

---

## BR-PLT-001 — Organization Registration Approval

| Attribute           | Value                              |
| ------------------- | ---------------------------------- |
| Rule ID             | BR-PLT-001                         |
| Rule Name           | Organization Registration Approval |
| Business Domain     | Platform                           |
| Business Capability | Organization Onboarding            |
| Business Process    | Organization Registration          |
| Priority            | Critical                           |
| Configuration       | Fixed                              |

### Rule Statement

Every organization shall be approved by the Platform Administrator before accessing the Digitize platform.

### Business Outcome

Only approved organizations may proceed with onboarding.

---

## BR-PLT-002 — Unique Organization Identifier

Every organization shall receive a globally unique Organization ID generated by the platform.

The Organization ID shall never be reused, even if the organization is deleted or archived.

Priority: **Critical**

---

## BR-PLT-003 — Multi-Tenant Isolation

Business data belonging to one organization shall never be visible or accessible to another organization unless explicitly supported through future platform features.

Priority: **Critical**

---

## BR-PLT-004 — Subscription Requirement

An organization shall maintain at least one active Facility Subscription before any facility can become operational.

Priority: **Critical**

---

## BR-PLT-005 — Platform License Validation

Every active facility shall possess a valid platform license associated with an active subscription.

Priority: **Critical**

---

## BR-PLT-006 — Platform Audit Logging

Every platform-level administrative action shall be recorded within the audit log.

Priority: **Critical**

---

## BR-PLT-007 — Platform Configuration Authority

Only Platform Administrators may modify global platform configuration settings.

Priority: **High**

---

## BR-PLT-008 — Platform Version Compatibility

Organizations shall always operate using supported platform versions.

Priority: **High**

---

## BR-PLT-009 — Platform Suspension

The Platform Administrator may suspend an organization for commercial, security, or compliance reasons.

Priority: **Critical**

---

## BR-PLT-010 — Platform Reactivation

Suspended organizations may only be reactivated following administrative approval.

Priority: **High**

---

# 12. Organization Business Rules

Organization Business Rules govern the internal business configuration of organizations operating on Digitize.

---

## BR-ORG-001 — Organization Ownership

Every organization shall have exactly one primary Organization Administrator responsible for business ownership.

Priority: **Critical**

---

## BR-ORG-002 — Organization Profile

Organizations shall maintain complete business profile information before operational activation.

Priority: **High**

---

## BR-ORG-003 — Facility Ownership

Every facility shall belong to one and only one organization.

Priority: **Critical**

---

## BR-ORG-004 — Organization Policies

Organizations may configure operational policies provided they remain within platform constraints.

Priority: **High**

---

## BR-ORG-005 — Organization Users

Every user account shall belong to a single organization.

Priority: **Critical**

---

## BR-ORG-006 — Role-Based Access

User permissions shall be governed through assigned roles.

Priority: **Critical**

---

## BR-ORG-007 — Organization Status

Organizations may exist in one of the following states:

* Pending
* Active
* Suspended
* Archived

**Onboarding (DR-021):** Platform Admin creates Organizations in **Pending** and provisions the initial Organization Admin. Organization Admin credentials are provisioned using a temporary password in local/development (Mailpit) or a secure credential setup link in QA/Production. After OA credential setup and Terms & Conditions acceptance:

* No initial Organization detail changes → Organization becomes **Active** automatically.
* Initial Organization detail changes → remains **Pending** until Platform Admin approves (or rejects for OA correction).

Once **Active**, normal Organization Admin changes do **not** require Platform Admin approval. Soft-delete (archive/restore) is separate from `business_status`.

Priority: **High**

---

## BR-ORG-008 — Organization Deactivation

Organizations with active facilities may not be permanently deleted.

Priority: **Critical**

---

## BR-ORG-009 — Business Configuration

Organizations shall complete mandatory business configuration before commencing operations.

Priority: **High**

---

## BR-ORG-010 — Organization Audit Trail

All organization configuration changes shall be auditable.

Priority: **Critical**

---

# 13. Facility Business Rules

Facility Business Rules govern the operational units through which organizations deliver services.

A Facility is the primary commercial and operational entity within Digitize.

---

## BR-FAC-001 — Facility Registration

Every facility shall be registered under an approved organization.

Priority: **Critical**

---

## BR-FAC-002 — Facility Subscription

Every operational facility shall maintain an active Facility Subscription.

Priority: **Critical**

---

## BR-FAC-003 — Facility Type

Every facility shall be assigned exactly one Facility Type.

Examples include:

* Swimming Pool
* Gym
* Yoga Centre
* Dance Studio

Priority: **High**

---

## BR-FAC-004 — Facility Capacity

Facilities shall define operational capacity limits according to business policy.

Priority: **High**

---

## BR-FAC-005 — Facility Operating Hours

Facilities shall define operating hours prior to accepting customers.

Priority: **High**

---

## BR-FAC-006 — Facility Status

Facilities may exist in the following states:

* Draft
* Operational
* Suspended
* Closed

Priority: **High**

---

## BR-FAC-007 — Facility Staff Assignment

Staff members shall be assigned to one or more facilities according to organizational policy.

Priority: **Medium**

---

## BR-FAC-008 — Facility Services

Each facility shall define the services it offers before publishing membership plans.

Priority: **Medium**

---

## BR-FAC-009 — Facility Reporting

Operational reporting shall be generated independently for each facility.

Priority: **Medium**

---

## BR-FAC-010 — Facility Closure

Closed facilities shall retain historical operational records.

Priority: **Critical**

---

# 14. Site Business Rules

A Site represents a physical location from which a Facility operates.

Sites are operational extensions of a Facility and may require additional commercial licensing according to the Subscription & Licensing Strategy.

---

## BR-SIT-001 — Site Ownership

Every Site shall belong to exactly one Facility.

Priority: **Critical**

---

## BR-SIT-002 — Facility-to-Site Relationship

A Facility may operate from one or more Sites.

Priority: **High**

---

## BR-SIT-003 — Site Add-on Licensing

Additional Sites beyond the subscription entitlement shall require a Site Add-on license.

Priority: **Critical**

---

## BR-SIT-004 — Site Operational Status

Sites may exist in the following states:

* Planned
* Active
* Suspended
* Closed

Priority: **High**

---

## BR-SIT-005 — Site Address

Every Site shall maintain a complete physical address.

Priority: **High**

---

## BR-SIT-006 — Site Capacity

Site capacity may differ from the overall Facility capacity and shall be configurable.

Priority: **Medium**

---

## BR-SIT-007 — Site Staff Allocation

Organizations may assign staff to one or multiple Sites within the same Facility.

Priority: **Medium**

---

## BR-SIT-008 — Site Reporting

Operational reports shall support Site-level filtering while aggregating into Facility-level reporting.

Priority: **Medium**

---

## BR-SIT-009 — Site Closure

Closing a Site shall not automatically close its parent Facility.

Priority: **High**

---

## BR-SIT-010 — Historical Records

Historical operational, attendance, billing, and audit records associated with a Site shall be retained after Site closure.

Priority: **Critical**

---

# 15. Customer Business Rules

Customer Business Rules govern the registration, management, and lifecycle of customers within Digitize.

---

## BR-CUS-001 — Customer Registration

Every customer shall be registered under exactly one Organization.

Priority: **Critical**

---

## BR-CUS-002 — Unique Customer Identifier

Every customer shall receive a globally unique Customer ID generated by Digitize.

Customer IDs shall never be reused.

Priority: **Critical**

---

## BR-CUS-003 — Mandatory Customer Information

The following information shall be mandatory during customer registration:

* Full Name
* Mobile Number
* Date of Birth (or Age, based on business policy)
* Gender
* Emergency Contact
* Primary Facility

Additional fields may be configured by the organization.

Priority: **High**

---

## BR-CUS-004 — Duplicate Customer Prevention

Organizations shall not maintain duplicate customer records using the same primary mobile number unless explicitly permitted by future business configuration.

Priority: **Critical**

---

## BR-CUS-005 — Customer Status

Customers may exist in one of the following states:

* Prospect
* Registered
* Active
* Inactive
* Blocked
* Archived

Priority: **High**

---

## BR-CUS-006 — Multiple Membership Ownership

A customer may simultaneously own multiple active memberships where permitted by organization policy.

Examples include:

* Swimming Membership
* Personal Training
* Summer Camp
* Family Membership

Priority: **Critical**

---

## BR-CUS-007 — Customer Transfer

A customer may transfer between Facilities within the same Organization only if permitted by organizational policy.

Transfers between different Organizations are not supported in Version 1.0.

Priority: **Medium**

---

## BR-CUS-008 — Customer Communication Consent

Organizations shall maintain customer communication preferences before sending promotional communications.

Priority: **Medium**

---

## BR-CUS-009 — Customer Historical Records

Historical attendance, billing, memberships, invoices, and payment records shall remain available even after customer deactivation.

Priority: **Critical**

---

## BR-CUS-010 — Customer Deletion

Customer records with historical transactions shall not be permanently deleted.

Priority: **Critical**

---

# 16. Membership Business Rules

Membership Business Rules govern the creation, sale, activation, renewal, suspension, and termination of memberships.

---

## BR-MEM-001 — Membership Plan Ownership

Every Membership Plan shall belong to exactly one Facility.

Priority: **Critical**

---

## BR-MEM-002 — Membership Purchase

Memberships shall only be purchased from active Membership Plans.

Priority: **Critical**

---

## BR-MEM-003 — Payment Before Activation

A membership shall become active only after successful payment confirmation unless organizational policy explicitly permits deferred payment.

Priority: **Critical**

---

## BR-MEM-004 — Membership Validity

Every membership shall define:

* Start Date
* End Date
* Validity Period

Priority: **Critical**

---

## BR-MEM-005 — Membership Types

Digitize shall support configurable membership types, including but not limited to:

* Individual
* Family
* Training
* Personal Training
* Seasonal
* Time-based
* Visit-based

Priority: **High**

---

## BR-MEM-006 — Membership Renewal

Organizations may renew memberships before or after expiry according to configured renewal policies.

Priority: **High**

---

## BR-MEM-007 — Membership Upgrade

Membership upgrades shall follow organization-defined pricing and business policies.

Priority: **Medium**

---

## BR-MEM-008 — Membership Suspension

Organizations may temporarily suspend memberships according to configured suspension policies.

Priority: **Medium**

---

## BR-MEM-009 — Membership Expiry

Expired memberships shall automatically lose access privileges unless a grace period has been configured.

Priority: **Critical**

---

## BR-MEM-010 — Membership Cancellation

Cancelled memberships shall retain complete historical financial and operational records.

Priority: **Critical**

---

# 17. Attendance Business Rules

Attendance Business Rules govern customer entry validation, visit recording, and operational capacity management.

---

## BR-ATT-001 — Attendance Eligibility

Only customers with valid attendance entitlements shall be permitted entry.

Priority: **Critical**

---

## BR-ATT-002 — Attendance Recording

Every customer visit shall generate an attendance record.

Priority: **Critical**

---

## BR-ATT-003 — Attendance Timestamp

Attendance records shall capture both entry and exit timestamps where applicable.

Priority: **High**

---

## BR-ATT-004 — Membership Validation

Attendance shall validate membership status before entry approval.

Priority: **Critical**

---

## BR-ATT-005 — Walk-in Attendance

Walk-in customers shall be recorded separately from membership attendance.

Priority: **High**

---

## BR-ATT-006 — Capacity Validation

Attendance shall not exceed configured Facility or Site capacity unless an override is authorised.

Priority: **Critical**

---

## BR-ATT-007 — Attendance Corrections

Attendance corrections shall require authorised staff approval and be fully auditable.

Priority: **High**

---

## BR-ATT-008 — Duplicate Entry Prevention

Customers shall not register multiple active attendance sessions simultaneously at the same Facility unless permitted by business policy.

Priority: **Critical**

---

## BR-ATT-009 — Attendance History

Complete attendance history shall remain available for reporting and auditing.

Priority: **Medium**

---

## BR-ATT-010 — Attendance Retention

Attendance records shall remain available according to the organization's retention policy.

Priority: **Medium**

---

# 18. Trainer Business Rules

Trainer Business Rules govern trainers, coaching activities, classes, and personal training services.

---

## BR-TRN-001 — Trainer Registration

Every trainer shall belong to one Organization.

Priority: **Critical**

---

## BR-TRN-002 — Trainer Assignment

Trainers may be assigned to one or more Facilities or Sites within the same Organization. Cross-organization trainer sharing is not supported in the current release.

Priority: **Medium**

---

## BR-TRN-003 — Personal Training Allocation

Personal training sessions shall be assigned to a designated trainer.

Priority: **Critical**

---

## BR-TRN-004 — Batch Assignment

Every scheduled batch shall have at least one assigned trainer.

**Enforcement (v1):** `schedule_batch` resolves an effective trainer from the request `trainer_id` or the active batch trainer assignment, rejects scheduling when none exists, requires the trainer to be active and organization-aligned, and persists the resolved trainer on the class session. Batch creation and configuration without a schedule remain unchanged.

Priority: **High**

---

## BR-TRN-005 — Trainer Availability

Trainer availability shall be maintained before scheduling sessions.

**Enforcement (v1):** Scheduling writes (`schedule_batch`, book/reschedule/assign personal training session) require the full session interval `[starts_at, ends_at)` to be covered by the union of persisted `AVAILABLE` rows in `training.trainer_availability` for that trainer (half-open merge on overlap or adjacency). `UNAVAILABLE` rows and absent coverage reject with HTTP 422 validation. This check runs before BR-TRN-008 conflict detection; schedule conflict overrides do not bypass availability.

Priority: **High**

---

## BR-TRN-006 — Trainer Status

Trainers may exist in one of the following states:

* Active
* On Leave
* Suspended
* Inactive

Priority: **Medium**

---

## BR-TRN-007 — Session Attendance

Trainer attendance shall be recorded independently from customer attendance.

Priority: **Medium**

---

## BR-TRN-008 — Trainer Schedule Conflicts

Digitize shall detect overlapping class and personal training sessions for the same trainer within an organization (half-open interval overlap; cancelled sessions excluded).

Scheduling writes that assign a trainer to a time window shall be rejected when C1–C3 conflicts exist unless an authorized actor supplies a valid override declaration: a trimmed reason of 10–500 characters and an acknowledgment that exactly matches the server-recomputed conflicts.

Organization Administrators may override within authorized organization and facility/site scope. Staff may override only when granted `override.trainer.schedule.conflicts` and the permission for the underlying write operation. Overrides must not bypass organization ownership, facility/site authorization, operational eligibility, trainer lifecycle status, or other integrity constraints.

Each successful override shall emit audit action `OVERRIDE_TRAINER_SCHEDULE_CONFLICT`. Validate-only conflict checks remain available via API-07-004 and audit as `VALIDATE_TRAINER_SCHEDULE_CONFLICTS`.

A second-approver approval workflow is deferred to a future product decision.

Priority: **High**

---

## BR-TRN-009 — Trainer Historical Records

Historical schedules, assignments, attendance, and session records shall remain available after trainer deactivation.

Priority: **Medium**

---

## BR-TRN-010 — Trainer Deletion

Trainers associated with completed sessions, customer records, or financial transactions shall not be permanently deleted.

Priority: **Critical**

---

# 19. Subscription Business Rules

Subscription Business Rules govern the commercial relationship between OrieOn Technologies Pvt. Ltd. and subscribing organizations.

Subscriptions provide organizations with access to the Digitize platform and are managed independently from customer memberships.

---

## BR-SUB-001 — Subscription Ownership

Every subscription shall belong to one Organization and one Facility.

Priority: **Critical**

---

## BR-SUB-002 — Facility-Level Subscription

Commercial subscriptions shall be licensed at the Facility level.

Priority: **Critical**

---

## BR-SUB-003 — Site Add-on Licensing

Organizations operating multiple Sites under a Facility shall purchase Site Add-on licenses where subscription entitlements are exceeded.

Priority: **Critical**

---

## BR-SUB-004 — Active Subscription Requirement

A Facility shall maintain an active subscription before commencing operational activities.

Priority: **Critical**

---

## BR-SUB-005 — Subscription Plan Assignment

Each Facility shall be assigned exactly one active subscription plan at any given time.

Examples:

* Launch
* Grow
* Scale
* Enterprise

Priority: **Critical**

---

## BR-SUB-006 — Subscription Activation

A subscription shall become active only after successful payment confirmation unless commercial approval authorizes deferred activation.

Priority: **Critical**

---

## BR-SUB-007 — Subscription Validity

Every subscription shall define:

* Activation Date
* Expiry Date
* Billing Cycle
* Renewal Policy

Priority: **Critical**

---

## BR-SUB-008 — Subscription Renewal

Subscriptions may be renewed before expiry according to the applicable commercial policy.

Priority: **High**

---

## BR-SUB-009 — Subscription Upgrade

Organizations may upgrade subscription plans at any time.

Commercial adjustments shall follow the approved pricing strategy.

Priority: **High**

---

## BR-SUB-010 — Subscription Downgrade

Subscription downgrades shall take effect according to the commercial downgrade policy and shall not invalidate historical records.

Priority: **Medium**

---

## BR-SUB-011 — Subscription Suspension

Facilities with suspended subscriptions shall have operational access restricted according to commercial policy.

Priority: **Critical**

---

## BR-SUB-012 — Subscription Expiry

Expired subscriptions shall transition the Facility into a restricted operational state after any configured grace period.

Priority: **Critical**

---

# 20. Billing Business Rules

Billing Business Rules govern invoice generation, taxation, adjustments, and financial records.

---

## BR-BIL-001 — Invoice Generation

Every commercial charge shall generate a corresponding invoice.

Priority: **Critical**

---

## BR-BIL-002 — Unique Invoice Number

Every invoice shall have a unique, immutable invoice number.

Priority: **Critical**

---

## BR-BIL-003 — Invoice Ownership

Invoices shall be issued to the subscribing Organization and identify the applicable Facility.

Priority: **High**

---

## BR-BIL-004 — Tax Calculation

Applicable taxes shall be calculated according to configured regional taxation rules.

Priority: **Critical**

---

## BR-BIL-005 — Invoice Status

Invoices may exist in one of the following states:

* Draft
* Issued
* Partially Paid
* Paid
* Overdue
* Cancelled

Priority: **High**

---

## BR-BIL-006 — Credit Notes

Credit Notes shall reference the original invoice and maintain a complete audit trail.

Priority: **Medium**

---

## BR-BIL-007 — Invoice Adjustments

Billing adjustments shall require authorized approval and shall preserve historical financial records.

Priority: **High**

---

## BR-BIL-008 — Financial History

Invoices and billing records shall never be permanently deleted.

Priority: **Critical**

---

# 21. Payment Business Rules

Payment Business Rules govern the collection, validation, and recording of commercial payments.

---

## BR-PAY-001 — Payment Confirmation

Subscriptions shall be activated only after successful payment confirmation unless deferred payment is explicitly approved.

Priority: **Critical**

---

## BR-PAY-002 — Supported Payment Methods

Digitize shall support organization-configurable payment methods, including:

* UPI
* Credit Card
* Debit Card
* Net Banking
* Bank Transfer
* Cash (where applicable)

Priority: **High**

---

## BR-PAY-003 — Payment Reference

Every payment shall have a unique payment reference.

Priority: **Critical**

---

## BR-PAY-004 — Partial Payments

Partial payments shall be supported only when permitted by commercial policy.

Priority: **Medium**

---

## BR-PAY-005 — Payment Failure

Failed payment attempts shall not activate subscriptions or settle invoices.

Priority: **Critical**

---

## BR-PAY-006 — Refunds

Refunds shall follow the organization's approved refund policy and maintain complete financial traceability.

Priority: **High**

---

## BR-PAY-007 — Payment Audit

All payment events shall be recorded within the financial audit trail.

Priority: **Critical**

---

## BR-PAY-008 — Payment Reconciliation

Digitize shall support reconciliation between invoices, payments, and outstanding balances.

Priority: **High**

---

# 22. Commercial Business Rules

Commercial Business Rules govern pricing, promotions, discounts, renewals, and commercial governance.

---

## BR-COM-001 — Pricing Authority

Only authorized commercial administrators may modify subscription pricing.

Priority: **Critical**

---

## BR-COM-002 — Commercial Offers

Promotional offers shall define:

* Validity Period
* Eligible Subscription Plans
* Eligibility Criteria
* Discount Type
* Discount Value

Priority: **High**

---

## BR-COM-003 — Discount Validation

Discounts shall be validated before invoice generation.

Priority: **Critical**

---

## BR-COM-004 — Offer Expiry

Expired commercial offers shall not be applied to new subscriptions or renewals.

Priority: **Critical**

---

## BR-COM-005 — Renewal Pricing

Subscription renewals shall use the applicable renewal pricing in effect at the time of renewal unless protected by contractual agreements.

Priority: **High**

---

## BR-COM-006 — Commercial Approval

Manual commercial adjustments exceeding configured approval thresholds shall require authorized approval.

Priority: **Critical**

---

## BR-COM-007 — Subscription Entitlements

Every subscription plan shall define its included entitlements, limits, and optional add-ons.

Examples include:

* Number of included Sites
* User limits (if applicable)
* Feature availability
* Storage or usage limits
* Premium modules
* Site Add-on eligibility

Priority: **Critical**

---

## BR-COM-008 — Commercial Audit Trail

All pricing changes, discounts, commercial approvals, and subscription modifications shall be fully auditable.

Priority: **Critical**

---

# 23. Notification Business Rules

Notification Business Rules govern the generation, delivery, and tracking of communications within Digitize.

Notifications may be delivered through one or more configured communication channels.

---

## BR-NOT-001 — Event-Based Notifications

Notifications shall be generated only in response to configured business events.

Examples include:

* Customer Registration
* Membership Purchase
* Membership Renewal
* Attendance Recorded
* Invoice Generated
* Payment Received
* Subscription Expiry
* Password Reset

Priority: **Critical**

---

## BR-NOT-002 — Notification Channels

Organizations may enable one or more communication channels, including:

* SMS
* Email
* WhatsApp
* Push Notification (Future)
* In-App Notification (Future)

Priority: **High**

---

## BR-NOT-003 — Organization Preferences

Organizations shall configure which business events generate notifications.

Priority: **Medium**

---

## BR-NOT-004 — Customer Communication Preferences

Customer notification preferences shall be respected for promotional communications.

Mandatory operational notifications may still be delivered where required by business or legal policy.

Priority: **High**

---

## BR-NOT-005 — Notification Templates

All notifications shall use approved templates.

Templates may support:

* Variables
* Localization
* Branding
* Dynamic content

Priority: **High**

---

## BR-NOT-006 — Notification Retry

Failed notification deliveries may be retried according to the configured retry policy.

Priority: **Medium**

---

## BR-NOT-007 — Notification Logging

Every notification attempt shall be recorded with:

* Event
* Recipient
* Channel
* Delivery Status
* Timestamp

Priority: **Critical**

---

## BR-NOT-008 — Notification History

Historical notification records shall remain available for reporting and auditing.

Priority: **Medium**

---

# 24. Reporting Business Rules

Reporting Business Rules govern the generation, availability, and integrity of business reports.

---

## BR-RPT-001 — Authorized Access

Reports shall only be accessible to users with appropriate permissions.

Priority: **Critical**

---

## BR-RPT-002 — Data Accuracy

Reports shall be generated using the latest committed business data available at the time of report execution.

Priority: **Critical**

---

## BR-RPT-003 — Reporting Scope

Reporting shall support:

* Organization-level reporting
* Facility-level reporting
* Site-level reporting (where applicable)

Priority: **High**

---

## BR-RPT-004 — Historical Reporting

Historical reports shall remain available according to the organization's configured data retention policy.

Priority: **Medium**

---

## BR-RPT-005 — Export Formats

Organizations may export reports in supported formats, including:

* PDF
* Excel
* CSV

Priority: **Medium**

---

## BR-RPT-006 — Financial Reports

Financial reports shall reconcile invoices, payments, refunds, and outstanding balances.

Priority: **Critical**

---

## BR-RPT-007 — Operational Reports

Operational reports shall include, where applicable:

* Attendance
* Memberships
* Trainer Activity
* Facility Utilization
* Customer Growth

Priority: **High**

---

## BR-RPT-008 — Dashboard Metrics

Business dashboards shall present key performance indicators using approved business calculations.

Priority: **Medium**

---

# 25. Security Business Rules

Security Business Rules govern authentication, authorization, access control, and protection of business data.

---

## BR-SEC-001 — Authentication

Every system user shall authenticate before accessing protected platform resources.

Priority: **Critical**

---

## BR-SEC-002 — Role-Based Access Control

Access to business functions shall be governed by assigned roles and permissions.

Priority: **Critical**

---

## BR-SEC-003 — Least Privilege

Users shall receive only the minimum permissions required to perform their assigned responsibilities.

Priority: **Critical**

---

## BR-SEC-004 — Organization Data Isolation

Users shall access only the data belonging to their Organization unless explicitly authorized by platform administration.

Priority: **Critical**

---

## BR-SEC-005 — Password Policy

Passwords shall comply with the organization's configured password policy or platform minimum security requirements.

Priority: **High**

---

## BR-SEC-006 — Account Lockout

Repeated failed authentication attempts shall trigger temporary account lockout according to configured security policies.

Priority: **High**

---

## BR-SEC-007 — Session Management

User sessions shall expire after a configurable period of inactivity.

Priority: **High**

---

## BR-SEC-008 — Permission Changes

Changes to user roles and permissions shall be logged and auditable.

Priority: **Critical**

---

## BR-SEC-009 — Sensitive Data Protection

Sensitive business and customer information shall be protected according to applicable privacy and security requirements.

Priority: **Critical**

---

## BR-SEC-010 — Administrative Actions

Platform administrative actions shall require elevated authorization and shall be fully auditable.

Priority: **Critical**

---

# 26. Audit Business Rules

Audit Business Rules ensure that business activities remain traceable, accountable, and compliant.

---

## BR-AUD-001 — Audit Logging

Business events identified as auditable shall generate audit records automatically.

Priority: **Critical**

---

## BR-AUD-002 — Immutable Audit Records

Audit records shall not be modified or deleted through standard application functionality.

Priority: **Critical**

---

## BR-AUD-003 — Auditable Events

The following events shall be auditable at a minimum:

* Organization creation
* Facility creation
* Site creation
* Customer registration
* Membership activation
* Attendance corrections
* Invoice generation
* Payment confirmation
* Subscription activation
* User role changes
* Security events
* Configuration changes

Priority: **Critical**

---

## BR-AUD-004 — Audit Record Contents

Audit records shall capture, where applicable:

* Event Identifier
* Event Type
* Date and Time
* Organization
* Facility
* Site
* User
* Previous Value
* New Value
* Source
* Outcome

Priority: **Critical**

---

## BR-AUD-005 — Audit Retention

Audit records shall be retained according to platform and regulatory retention policies.

Priority: **Critical**

---

## BR-AUD-006 — Audit Access

Audit logs shall only be accessible to authorized users with appropriate permissions.

Priority: **High**

---

## BR-AUD-007 — Compliance Support

Audit information shall support internal governance, customer audits, and regulatory compliance activities where applicable.

Priority: **High**

---

## BR-AUD-008 — Cross-Module Traceability

Audit records shall support traceability across business processes, functional requirements, APIs, database entities, and user actions.

Priority: **Critical**

---

# 27. Rule Versioning

## 27.1 Purpose

Business Rules are living business assets.

As Digitize evolves through new releases, regulatory changes, commercial strategies, and operational improvements, Business Rules may be introduced, modified, superseded, or retired.

Rule Versioning ensures that every change is controlled, traceable, and historically preserved.

---

## 27.2 Versioning Principles

Business Rules shall follow these versioning principles:

* Every rule shall have one permanent Rule ID.
* Rule IDs shall never be reused.
* Changes shall create a new rule version rather than a new Rule ID.
* Historical rule versions shall remain archived.
* Rule modifications shall maintain traceability to previous versions.
* Business Rules shall remain independent of software implementation.

---

## 27.3 Version Numbering

Business Rule documents shall use semantic versioning.

| Version | Meaning                                                                                                    |
| ------- | ---------------------------------------------------------------------------------------------------------- |
| Major   | Significant business policy changes affecting platform behaviour.                                          |
| Minor   | New rules or significant rule enhancements.                                                                |
| Patch   | Editorial corrections, clarifications, or documentation improvements with no change to business behaviour. |

Example:

| Version | Description                        |
| ------- | ---------------------------------- |
| 1.0     | Initial baseline release.          |
| 1.1     | New Membership Rules introduced.   |
| 1.2     | Commercial rule clarifications.    |
| 2.0     | Major subscription model revision. |

---

## 27.4 Rule Change Classification

Business Rule changes shall be classified as follows:

| Change Type | Description                                                                             |
| ----------- | --------------------------------------------------------------------------------------- |
| New         | Introduction of a new business rule.                                                    |
| Modified    | Existing rule updated without changing its Rule ID.                                     |
| Deprecated  | Rule retained for historical reference but no longer applicable to new implementations. |
| Retired     | Rule removed from active business operations while preserving historical traceability.  |

---

# 28. Rule Maintenance

## 28.1 Purpose

Business Rules require periodic review to ensure continued alignment with business objectives, commercial strategy, operational practices, and regulatory requirements.

---

## 28.2 Maintenance Responsibilities

| Role                    | Responsibility                                    |
| ----------------------- | ------------------------------------------------- |
| Product Management      | Approves business policy changes.                 |
| Business Analysis Team  | Authors and maintains business rules.             |
| Enterprise Architecture | Assesses architectural impact.                    |
| Engineering Team        | Evaluates implementation impact.                  |
| Quality Assurance       | Validates rule implementation.                    |
| Customer Success        | Provides operational feedback.                    |
| Executive Leadership    | Approves strategic policy changes where required. |

---

## 28.3 Rule Review Cycle

Business Rules should be reviewed:

* Before each major product release.
* Following regulatory changes.
* Following commercial strategy revisions.
* After significant customer feedback.
* After operational process improvements.
* Following architecture review recommendations.

---

## 28.4 Change Approval Process

```text
Business Requirement Identified
              │
              ▼
Business Rule Proposal
              │
              ▼
Business Analysis Review
              │
              ▼
Stakeholder Approval
              │
              ▼
Architecture Review
              │
              ▼
FRS Update
              │
              ▼
Development
              │
              ▼
Testing
              │
              ▼
Production Release
```

Business Rules shall always be approved before implementation begins.

---

# 29. Rule Traceability Matrix

## 29.1 Purpose

Every Business Rule shall maintain traceability throughout the product lifecycle.

---

## 29.2 Traceability Relationships

| Business Rule                | References                                                     |
| ---------------------------- | -------------------------------------------------------------- |
| Business Capability          | Defines why the rule exists.                                   |
| Business Process             | Defines where the rule applies.                                |
| User Journey                 | Defines who experiences the rule.                              |
| Functional Requirement (FRS) | Defines how the system implements the rule.                    |
| User Interface               | Defines where the rule is presented.                           |
| API Specification            | Defines how the rule is enforced programmatically.             |
| Database Design              | Defines where the business data supporting the rule is stored. |
| Test Case                    | Defines how compliance with the rule is verified.              |

---

## 29.3 Enterprise Traceability Model

```text
Business Vision
       │
       ▼
Business Objective
       │
       ▼
Business Capability
       │
       ▼
Business Process
       │
       ▼
Business Rule
       │
       ▼
Functional Requirement
       │
       ▼
User Interface
       │
       ▼
API
       │
       ▼
Database
       │
       ▼
Test Case
       │
       ▼
Production Feature
```

This traceability model shall be maintained across all Digitize documentation.

---

# 30. References

The Business Rules Catalog shall be read together with the following documents.

### Product Foundation

* PF-01 – Product Glossary
* PF-02 – Domain Model
* PF-03 – Product Vision
* PF-04 – Business Model
* PF-05 – Product Roadmap

### Commercial Strategy

* CS-01 – Subscription & Licensing Strategy
* CS-02 – Pricing Strategy
* CS-03 – Billing & Invoicing Strategy
* CS-04 – Commercial Offers & Incentive Strategy

### Business Analysis

* BA-01 – Business Requirements Document
* BA-03 – Business Process Catalog
* BA-04 – Business Process Flows
* BA-05 – User Personas
* BA-06 – User Journeys
* BA-07 – Stakeholder Analysis
* BA-08 – Requirement Traceability Matrix
* BA-09 – Non-Functional Business Requirements
* BA-10 – Business Assumptions, Constraints & Risks

### Downstream Design Documents

* Functional Requirements Specification (FRS)
* System Architecture Document (SAD)
* Database Design
* API Specification
* UI/UX Specification
* Test Strategy
* Deployment Architecture

---

# 31. Revision History

| Version | Date      | Author                                      | Description                                                                      |
| ------- | --------- | ------------------------------------------- | -------------------------------------------------------------------------------- |
| 1.0     | July 2026 | Product Management & Business Analysis Team | Initial baseline release of the Business Rules Catalog for Digitize Version 1.0. |

---

# End of Document
