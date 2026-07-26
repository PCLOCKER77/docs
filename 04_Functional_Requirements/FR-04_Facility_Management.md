# FR-04 Facility Management

**Document ID:** FR-04  
**Document Name:** Facility Management Functional Requirements  
**Company:** OreeOn Technologies Pvt. Ltd.  
**Product:** Digitize  
**Document Type:** Functional Requirements  
**Version:** 1.0  
**Status:** Draft  
**Owner:** Product Management  
**Prepared By:** Product Management, Business Analysis, and Solution Architecture  
**Last Updated:** July 2026

---

## FR-FAC-001 - Create Facility

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-FAC-001 |
| Requirement Name | Create Facility |
| Functional Module | Facility Management |
| Business Domain | Facility |
| Business Capability | Facility Management |
| Requirement Type | Functional |
| Requirement Category | Transaction |
| Requirement Version | 1.0 |
| Requirement Status | Approved |
| Priority | Critical |
| Complexity | High |
| Release Version | 1.0 |
| Owner | Product Management |

### Traceability References

| Traceability Type | Reference |
|---|---|
| Business Requirement | BA-08 BR-003 Facility Creation |
| Business Rule | BA-02 BR-FAC-001, BR-FAC-002, BR-FAC-003, BR-FAC-006, BR-ORG-003, BR-ORG-010 |
| Business Process | BA-03 BP-FAC-001 Create Facility |
| Business Process Flow | BA-04 Section 10 Facility Management Flow |
| Persona | BA-05 Organization Administrator, Facility Manager |
| User Journey | BA-06 Section 4 Organization Administrator Journey, Section 5 Facility Manager Journey |
| Stakeholder | BA-07 Organization Administrator, Facility Manager |
| Non-Functional Requirement | BA-09 Section 2.8 Configurability, Section 3.2 Authorization, Section 8 Business Configurability |
| Assumption / Constraint / Risk | BA-10 BA-ASS-001, BA-CON-003, BA-RSK-005 |

### Purpose

To allow authorized Organization Administrators to create a Facility as the primary operational business unit under an Active Organization.

### Functional Requirement

The system shall allow an Organization Administrator to create a Facility with required profile, ownership, type, contact, configuration baseline, and lifecycle information.

### Business Justification

Facilities define the business services delivered by an Organization and act as the operational parent for Sites, memberships, activities, attendance, billing context, staff assignment, and reporting.

### Actors

- Organization Administrator
- Facility Manager
- License Service
- Notification Service
- Audit Service
- System

### Preconditions

- Organization exists and is Active.
- Organization Administrator is authenticated.
- Organization Administrator has Facility creation permission.
- Required Facility Type definitions are available.
- Organization configuration allows Facility creation.
- Required license entitlement exists or can be assigned before activation.

### Trigger

The Organization Administrator selects Create Facility from Facility Management.

### In Scope

- Capture Facility master data.
- Associate Facility with exactly one Organization.
- Assign initial Facility Type.
- Initialize Facility Settings, Operating Hours, Capacity, Policies, and Dashboard context.
- Set initial Facility lifecycle status.
- Record audit and notification events.

### Out of Scope

- Site creation.
- Membership plan publication.
- Attendance recording.
- Subscription purchase.
- Payment processing.
- Facility activation beyond initial readiness preparation.

### Inputs

- Organization reference
- Facility name
- Facility code
- Facility type
- Facility description
- Facility contact details
- Facility address or operating location reference
- Initial manager reference, if available
- License reference, if available
- Default configuration values

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Organization ID | Parent Organization reference | Identifier | Yes | System / Organization Administrator | Must exist and be Active | Facility cannot exist independently |
| Facility Name | Business name of Facility | Text | Yes | Organization Administrator | Required and unique within Organization constraints | Used in screens and reports |
| Facility Code | Operational Facility identifier | Text | Yes | Organization Administrator / System | Must be unique within Organization | Used for search and integration references |
| Facility Type | Facility business type | Master Data | Yes | Organization Administrator | Must be active and allowed | Determines capabilities |
| Description | Business description | Text | No | Organization Administrator | Length validation | Used for internal context |
| Contact Details | Facility contact information | Structured Data | Yes | Organization Administrator | Email and phone format validation | Used for communication |
| Initial Status | Facility lifecycle status | Enum | Yes | System | Must be Draft at creation | Activation handled separately |

### Main Flow

1. Organization Administrator opens Create Facility.
2. The system loads Organization context, Facility Type options, and creation constraints.
3. Organization Administrator enters Facility profile, contact, and initial configuration data.
4. Organization Administrator selects a Facility Type.
5. The system validates Organization ownership, duplicate Facility identity, Facility Type eligibility, and mandatory fields.
6. The system creates the Facility in Draft status.
7. The system initializes Facility Settings, Operating Hours, Capacity, Policies, and Dashboard context.
8. The system records Facility creation audit events.
9. The system sends Facility Created notification where configured.
10. The system displays the Facility Profile or Facility setup summary.

### Alternate Flows

- If Facility Manager is known during creation, the Organization Administrator may assign the manager as part of setup.
- If license entitlement is not yet assigned, the Facility remains Draft and cannot become operational.
- If optional configuration is skipped, the system marks setup readiness as incomplete.

### Exception Flows

- If the selected Organization is not Active, the system blocks Facility creation.
- If duplicate Facility identity exists, the system rejects creation.
- If selected Facility Type is inactive or not allowed, the system blocks save.
- If initialization fails, the system prevents partial operational Facility creation and logs the failure.
- If the user lacks permission, the system denies access and records a security audit event.

### Outputs

- Facility record created.
- Facility status set to Draft.
- Facility Type assigned.
- Default Facility configuration initialized.
- Audit events recorded.
- Notifications generated.

### UI Behaviour

The Create Facility screen shall group fields into Organization context, Facility profile, Facility Type, contact details, and initial configuration. Save shall remain disabled until mandatory fields are valid. The UI shall display readiness gaps after creation so the Organization Administrator can complete configuration before activation.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-FAC-001 | Facility must belong to one Active Organization. | Block creation and display Organization status restriction. | Critical |
| VAL-FAC-002 | Facility Name is mandatory. | Block save and highlight field. | Critical |
| VAL-FAC-003 | Facility Code must be unique within the Organization. | Block save and show duplicate conflict. | Critical |
| VAL-FAC-004 | Facility Type is mandatory and must be active. | Block save and request valid Facility Type. | Critical |
| VAL-FAC-005 | Initial status must be Draft. | Reject invalid lifecycle state. | Critical |

### Business Rules

- BA-02 BR-FAC-001 - Facility Registration
- BA-02 BR-FAC-002 - Facility Subscription
- BA-02 BR-FAC-003 - Facility Type
- BA-02 BR-FAC-006 - Facility Status
- BA-02 BR-ORG-003 - Facility Ownership
- BA-02 BR-ORG-010 - Organization Audit Trail

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| facility.create | Organization Administrator | Create | Required to create Facility |
| facility.view | Organization Administrator | Read | Required to view created Facility |
| facility.type.assign | Organization Administrator | Execute | Required to assign Facility Type |
| audit.facility.create.read | Organization Administrator | Read | Required to view Facility creation audit |

### Security Considerations

Facility creation shall be restricted to the Organization tenant boundary. The system shall enforce RBAC, least privilege, Organization data isolation, and audit logging. Facility creation shall not expose or reuse another Organization's Facility identifiers.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Facility Created | Organization Administrator | In-App, Email | Facility record created | Include Facility name, type, and status |
| Facility Setup Required | Organization Administrator | In-App | Facility created in Draft status | Include missing readiness areas |
| Facility Manager Pending | Organization Administrator | In-App | No Facility Manager assigned | Include manager assignment action |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| FacilityCreated | Facility Management | Audit Service, Notification Service, Reporting Service |
| FacilityDefaultsInitialized | Facility Management | Configuration Service, Reporting Service |
| FacilityTypeAssignedDuringCreation | Facility Management | License Service, Configuration Service |

### Audit Events

| Audit Event | Trigger | Actor | Entity | Data Captured |
|---|---|---|---|---|
| Facility Created | Facility creation completed | Organization Administrator | Facility | Facility ID, Organization ID, Facility Type, status |
| Facility Defaults Initialized | Default configuration created | System | Facility Settings | Default source, initialized entities |
| Facility Creation Failed | Creation transaction failed | System | Facility | Failure reason and correlation ID |

### Reports Generated

- Facility Summary Report
- Facility Configuration Report
- Facility Status Report
- Executive Dashboard

### Related Screens

- Facility Management
- Create Facility
- Facility Profile
- Facility Settings
- Facility Dashboard

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/organizations/{organizationId}/facilities | POST | Organization Administrator token | Create Facility under Organization | 201 Created with Facility resource |
| /api/v1/facilities/{facilityId} | GET | Organization Administrator token | Retrieve Facility profile | 200 OK with Facility resource |
| /api/v1/facility-types | GET | Organization Administrator token | Retrieve available Facility Types | 200 OK with Facility Type list |
| /api/v1/facilities/{facilityId}/settings | POST | Organization Administrator token | Initialize Facility Settings | 201 Created with settings resource |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Organization | Read | Validate parent ownership and status | Parent entity |
| Facility | Create | Store Facility profile | Primary entity |
| Facility Type | Read | Validate selected type | Master data |
| Facility Settings | Create | Initialize configuration | Default values |
| Facility Operating Hours | Create | Initialize operating schedule | May be incomplete |
| Facility Capacity | Create | Initialize capacity records | May use defaults |
| Facility Policy | Create | Initialize policy baseline | Inherits Organization defaults |
| Audit Log | Insert | Record Facility creation | Required |
| Notification | Insert | Queue Facility notifications | Conditional |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| None | Create Facility | Draft | Organization Administrator | Required profile and Facility Type valid |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| FAC-001 | Facility name is required. | Mandatory field missing | Enter Facility name |
| FAC-002 | Facility code already exists for this Organization. | Duplicate Facility Code | Enter a unique Facility Code |
| FAC-003 | Facility Type is required. | Facility Type missing | Select a valid Facility Type |
| FAC-004 | Facility cannot be created because the Organization is not active. | Invalid Organization status | Activate Organization first |
| FAC-005 | Facility could not be initialized. | Configuration initialization failure | Retry or contact support |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Create valid Facility | Given an Active Organization and user with Facility creation permission | When valid Facility details are submitted | Then the system shall create the Facility in Draft status |
| Prevent duplicate Facility | Given a Facility Code already exists within the Organization | When the user submits the same code | Then the system shall block creation |
| Require Facility Type | Given no Facility Type is selected | When the user attempts to save | Then the system shall block save and request Facility Type |
| Record audit | Given Facility creation succeeds | When the transaction completes | Then the system shall record Facility creation audit events |

### Dependencies

- Active Organization
- Facility Type master data
- Organization Settings
- License entitlement model
- Notification Service
- Audit Service

### Operational Considerations

Facility creation failures shall be logged with correlation identifiers. Support teams shall be able to distinguish validation failures, entitlement gaps, and initialization failures.

### Non-Functional Considerations

Facility creation shall support tenant isolation, configurability, auditability, reliable transaction handling, and scalability for Organizations with many Facilities.

### Assumptions

- Organization-level onboarding is completed before Facility creation.
- Facility activation is handled separately.
- Facility license entitlement may be validated during setup and must be valid before operational activation.

### Success Criteria

A Facility is created under the correct Organization with valid identity, Facility Type, initialized configuration, audit history, and readiness visibility.

### Related Functional Requirements

- FR-ORG-007 - Activate Organization
- FR-FAC-003 - Configure Facility Settings
- FR-FAC-004 - Assign Facility Type
- FR-FAC-008 - Activate Facility
- FR-LIC-001 - Manage License Allocation

### Notes

Facility creation establishes the operational container but does not make the Facility available for service delivery until activation requirements are satisfied.

---

## FR-FAC-002 - Update Facility Details

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-FAC-002 |
| Requirement Name | Update Facility Details |
| Functional Module | Facility Management |
| Business Domain | Facility |
| Business Capability | Facility Management |
| Requirement Type | Functional |
| Requirement Category | Transaction |
| Requirement Version | 1.0 |
| Requirement Status | Approved |
| Priority | High |
| Complexity | Medium |
| Release Version | 1.0 |
| Owner | Product Management |

### Traceability References

| Traceability Type | Reference |
|---|---|
| Business Requirement | BA-08 Facility Management |
| Business Rule | BA-02 BR-FAC-001, BR-FAC-006, BR-FAC-009, BR-ORG-003, BR-ORG-010, BR-SEC-004 |
| Business Process | BA-03 BP-FAC-002 Update Facility Details |
| Business Process Flow | BA-04 Section 10 Facility Management Flow |
| Persona | BA-05 Organization Administrator, Facility Manager |
| User Journey | BA-06 Section 4 Organization Administrator Journey, Section 5 Facility Manager Journey |
| Stakeholder | BA-07 Organization Administrator, Facility Manager |
| Non-Functional Requirement | BA-09 Section 2.5 Maintainability, Section 10 Data Management |
| Assumption / Constraint / Risk | BA-10 BA-ASS-006, BA-CON-005 |

### Purpose

To allow authorized users to maintain accurate Facility profile information during the Facility lifecycle.

### Functional Requirement

The system shall allow authorized users to view and update permitted Facility detail fields while enforcing Organization scope, lifecycle status, validation, approval, and audit controls.

### Business Justification

Facility details must remain accurate for operational communication, staff coordination, customer-facing information, reporting, and governance across Sites and service delivery.

### Actors

- Organization Administrator
- Facility Manager
- Approval Workflow Service
- Notification Service
- Audit Service

### Preconditions

- Facility exists.
- Facility belongs to the user's Organization scope.
- Facility is not Archived.
- User is authenticated.
- User has Facility detail update permission.

### Trigger

An authorized user opens Facility Profile and submits Facility detail changes.

### In Scope

- View Facility details.
- Update permitted Facility profile fields.
- Validate duplicate identity and contact formats.
- Route governed changes for approval where configured.
- Record audit and notification events.

### Out of Scope

- Facility Type assignment.
- Facility Settings configuration.
- Operating Hours configuration.
- Capacity configuration.
- Lifecycle activation, suspension, or archival.

### Inputs

- Facility ID
- Facility name
- Facility code
- Description
- Contact details
- Address or location reference
- Change reason
- Approval reference, if required

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Facility ID | Unique Facility reference | Identifier | Yes | System | Must exist and match Organization scope | Read-only |
| Facility Name | Business name | Text | Yes | Authorized user | Required and length validation | Editable |
| Facility Code | Operational code | Text | Yes | Organization Administrator | Unique within Organization | May be governed after activation |
| Description | Facility description | Text | No | Authorized user | Length validation | Editable |
| Contact Email | Facility contact email | Email | Yes | Authorized user | Valid email format | Used for notifications |
| Contact Phone | Facility contact phone | Phone | Yes | Authorized user | Country-specific format | Used operationally |
| Change Reason | Reason for update | Text | Conditional | Authorized user | Required for governed fields | Stored in audit |

### Main Flow

1. Authorized user opens Facility Profile.
2. The system validates Organization scope and permission.
3. The system loads current Facility details and lifecycle status.
4. The system displays editable and read-only fields based on permission and status.
5. User updates permitted Facility fields.
6. The system validates mandatory fields, duplicate constraints, formats, status restrictions, and approval requirements.
7. If approval is not required, the system saves the Facility detail changes.
8. If approval is required, the system submits the change to Approval Workflow Service.
9. The system updates dependent summaries and reporting context.
10. The system records audit events and sends notifications.
11. The system displays confirmation or approval status.

### Alternate Flows

- If only non-governed contact details are changed, the system saves immediately.
- If Facility Code is governed after activation, the system routes the change for approval.
- If Facility is Suspended, limited detail maintenance may be permitted according to policy.

### Exception Flows

- If Facility is Archived, the system blocks updates.
- If the user lacks permission or Facility scope, access is denied.
- If duplicate Facility Code is entered, save is blocked.
- If approval submission fails, governed changes are not applied.
- If concurrent modification occurs, the system prompts the user to reload.

### Outputs

- Updated Facility profile.
- Pending approval request, if applicable.
- Updated reports and dashboards.
- Notifications.
- Audit log entries.

### UI Behaviour

Facility Profile shall display status badges, editable fields, read-only fields, pending approval indicators, and field-level validation. Save shall be disabled until mandatory values are valid. Changed governed fields shall show approval requirement before submission.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-FAC-101 | Facility must not be Archived for profile updates. | Block update. | Critical |
| VAL-FAC-102 | Facility Code must remain unique within the Organization. | Block save and show duplicate conflict. | Critical |
| VAL-FAC-103 | Contact details must follow configured formats. | Block save and highlight invalid fields. | High |
| VAL-FAC-104 | Governed fields require change reason and approval where configured. | Submit approval or block if approval unavailable. | High |
| VAL-FAC-105 | User must have Facility update permission. | Deny access and log event. | Critical |

### Business Rules

- BA-02 BR-FAC-001 - Facility Registration
- BA-02 BR-FAC-006 - Facility Status
- BA-02 BR-FAC-009 - Facility Reporting
- BA-02 BR-ORG-003 - Facility Ownership
- BA-02 BR-ORG-010 - Organization Audit Trail
- BA-02 BR-SEC-004 - Organization Data Isolation

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| facility.profile.view | Organization Administrator, Facility Manager | Read | Required to view Facility Profile |
| facility.profile.update | Organization Administrator | Update | Full profile update |
| facility.profile.maintain | Facility Manager | Update | Limited profile maintenance |
| facility.profile.approve | Authorized Approver | Approve | Required for governed changes |

### Security Considerations

Facility detail access shall enforce tenant isolation, Facility scope, RBAC, and least privilege. Sensitive operational contact data shall be protected. All before and after values for governed fields shall be audited.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Facility Updated | Organization Administrator, Facility Manager | In-App, Email | Facility profile update saved | Include changed categories |
| Facility Update Approval Required | Approver | In-App, Email | Governed field changed | Include requester and change reason |
| Facility Update Approval Outcome | Requester | In-App, Email | Approval completed | Include decision status |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| FacilityUpdated | Facility Management | Audit Service, Reporting Service, Notification Service |
| FacilityUpdateApprovalRequested | Facility Management | Approval Workflow Service |
| FacilityUpdateApprovalCompleted | Approval Workflow Service | Facility Management, Audit Service |

### Audit Events

| Audit Event | Trigger | Actor | Entity | Data Captured |
|---|---|---|---|---|
| Facility Profile Viewed | Profile opened | Authorized user | Facility | Facility ID, actor, timestamp |
| Facility Updated | Profile saved | Authorized user | Facility | Previous values, new values, change reason |
| Facility Update Approval Requested | Governed change submitted | Authorized user | Approval Request | Requested fields and approval route |

### Reports Generated

- Facility Summary Report
- Facility Configuration Report
- Audit Trail Report

### Related Screens

- Facility Profile
- Facility Management
- Facility Dashboard
- Approval Request
- Audit History

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/facilities/{facilityId} | GET | Authorized token | Retrieve Facility profile | 200 OK with Facility resource |
| /api/v1/facilities/{facilityId} | PATCH | Organization Administrator token | Update Facility details | 200 OK with updated Facility |
| /api/v1/facilities/{facilityId}/approval-requests | POST | Authorized token | Submit governed Facility change | 202 Accepted with approval request |
| /api/v1/facilities/{facilityId}/audit-events | GET | Authorized token | Retrieve Facility audit history | 200 OK with audit list |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Facility | Read, Update | Store Facility profile | Primary entity |
| Organization | Read | Validate parent Organization scope | Parent entity |
| Approval Request | Insert, Update | Manage governed profile changes | Conditional |
| Audit Log | Insert | Record Facility updates | Required |
| Notification | Insert | Queue update notifications | Conditional |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Draft | Update details | Draft | Organization Administrator | Valid update |
| Active | Update non-governed details | Active | Organization Administrator | Valid permitted fields |
| Active | Submit governed detail change | Active with Pending Approval | Organization Administrator | Approval required |
| Suspended | Update permitted details | Suspended | Organization Administrator | Limited maintenance allowed |
| Archived | Attempt update | Archived | Authorized user | Update blocked |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| FAC-101 | Facility cannot be updated in archived status. | Facility is Archived | Contact Organization Administrator |
| FAC-102 | Facility code already exists. | Duplicate code | Enter a unique code |
| FAC-103 | You do not have permission to update this Facility. | Missing permission | Request access |
| FAC-104 | This Facility change requires approval. | Governed field changed | Submit for approval |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Update Facility details | Given the user has Facility update permission | When valid Facility detail changes are submitted | Then the system shall save the changes |
| Block archived update | Given the Facility is Archived | When the user attempts to update details | Then the system shall block the update |
| Route governed change | Given a governed field is changed | When the user submits the update | Then the system shall create an approval request |
| Record audit | Given Facility details are updated | When the transaction completes | Then audit history shall capture previous and new values |

### Dependencies

- Organization Management
- Approval Workflow Service
- Notification Service
- Audit Service
- Facility lifecycle model

### Operational Considerations

Support teams shall be able to review failed updates, pending approvals, and duplicate conflicts from logs and audit history.

### Non-Functional Considerations

Facility updates shall be secure, tenant-isolated, auditable, reliable, and responsive for Organizations managing multiple Facilities.

### Assumptions

- Facility Managers may have limited update permissions based on Organization policy.
- Facility Type changes are managed by a separate requirement.
- Archived Facilities are read-only.

### Success Criteria

Facility profile information remains accurate, authorized, traceable, and available to downstream operational modules.

### Related Functional Requirements

- FR-FAC-001 - Create Facility
- FR-FAC-004 - Assign Facility Type
- FR-FAC-008 - Activate Facility
- FR-FAC-011 - View Facility Dashboard

### Notes

This requirement maintains Facility master data and does not control operating parameters or lifecycle actions.

---

## FR-FAC-003 - Configure Facility Settings

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-FAC-003 |
| Requirement Name | Configure Facility Settings |
| Functional Module | Facility Management |
| Business Domain | Facility |
| Business Capability | Facility Configuration |
| Requirement Type | Functional |
| Requirement Category | Configuration |
| Requirement Version | 1.0 |
| Requirement Status | Approved |
| Priority | Critical |
| Complexity | High |
| Release Version | 1.0 |
| Owner | Product Management |

### Traceability References

| Traceability Type | Reference |
|---|---|
| Business Requirement | BA-08 BR-004 Facility Configuration |
| Business Rule | BA-02 BR-FAC-001, BR-FAC-002, BR-FAC-003, BR-FAC-006, BR-FAC-008, BR-ORG-004, BR-ORG-010 |
| Business Process | BA-03 BP-FAC-003 Configure Facility Settings |
| Business Process Flow | BA-04 Section 10 Facility Management Flow |
| Persona | BA-05 Organization Administrator, Facility Manager |
| User Journey | BA-06 Section 4 Organization Administrator Journey, Section 5 Facility Manager Journey |
| Stakeholder | BA-07 Organization Administrator, Facility Manager |
| Non-Functional Requirement | BA-09 Section 8 Business Configurability |
| Assumption / Constraint / Risk | BA-10 BA-ASS-006, BA-CON-006 |

### Purpose

To allow authorized users to define Facility-level operational settings that act as the baseline for Sites and service delivery workflows.

### Functional Requirement

The system shall allow authorized users to configure Facility Settings within Organization policies, Facility Type capabilities, and license entitlement boundaries.

### Business Justification

Facility Settings support configurable operations across different business types while maintaining governance from Organization policies and platform constraints.

### Actors

- Organization Administrator
- Facility Manager
- License Service
- Approval Workflow Service
- Notification Service
- Audit Service

### Preconditions

- Facility exists.
- Parent Organization is Active.
- Facility is not Archived.
- User is authenticated.
- User has Facility settings permission.
- Facility Type is assigned.

### Trigger

An authorized user opens Facility Settings and submits setting changes.

### In Scope

- Configure Facility defaults.
- Manage inheritance from Organization Settings.
- Apply Facility Type capability constraints.
- Evaluate license entitlement impact.
- Propagate inherited settings to Sites where applicable.
- Record audit and notification events.

### Out of Scope

- Organization-level settings.
- Site-specific overrides.
- Operating Hours configuration.
- Capacity Limits configuration.
- Facility lifecycle activation.

### Inputs

- Facility ID
- Setting category
- Setting values
- Inheritance preference
- Applies-to scope
- Change reason
- Approval reference, if applicable

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Facility ID | Facility context | Identifier | Yes | System | Must exist and match Organization scope | Parent for settings |
| Setting Category | Operational setting group | Master Data | Yes | System | Must be enabled for Facility Type | Controls UI sections |
| Setting Value | Configured value | Configuration | Yes | Authorized user | Must match type, range, and policy constraints | Primary configuration |
| Inheritance Preference | Whether setting inherits from Organization | Enum | Yes | Authorized user | Must be allowed by policy | Supports override model |
| Applies-To Scope | Downstream impact scope | Enum | Yes | Authorized user | Facility or inherited Sites | Site overrides preserved |
| Change Reason | Reason for configuration change | Text | Conditional | Authorized user | Required for governed settings | Audit field |

### Main Flow

1. Authorized user opens Facility Settings.
2. The system loads current Facility Settings, Organization defaults, Facility Type capabilities, and license boundaries.
3. The system displays inherited values, Facility overrides, and locked settings.
4. User updates permitted setting values.
5. The system validates permissions, status, data types, Organization policy, Facility Type capability, and license limits.
6. The system evaluates impact on dependent Sites and operational services.
7. If approval is required, the system creates an approval request.
8. If approval is not required, or after approval is granted, the system saves the settings.
9. The system propagates inherited settings to Sites where applicable.
10. The system updates configuration reports and dashboards.
11. The system records audit events and sends notifications.

### Alternate Flows

- If the Facility inherits all values from Organization Settings, the user may save without local overrides.
- If Sites have approved overrides, the system preserves them during propagation.
- If a setting is locked by license entitlement, the system displays read-only value and entitlement reason.

### Exception Flows

- If the setting exceeds Organization policy or license boundaries, the system blocks saving.
- If the Facility Type does not support the selected capability, the setting is unavailable.
- If propagation to Sites fails, the system saves the Facility setting and records propagation failure where safe.
- If approval route is unavailable for governed setting, the system blocks submission.

### Outputs

- Updated Facility Settings.
- Configuration impact summary.
- Propagation status.
- Approval request, if applicable.
- Notifications and audit events.

### UI Behaviour

Facility Settings shall display inherited values, override indicators, locked fields, validation messages, and impact summaries. The UI shall clearly explain when a setting is unavailable due to Facility Type, Organization policy, or license entitlement.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-FAC-201 | Facility Settings must comply with Organization policy. | Block save and show policy violation. | Critical |
| VAL-FAC-202 | Facility Settings must be supported by Facility Type. | Disable unsupported controls. | Critical |
| VAL-FAC-203 | License-restricted settings cannot exceed entitlement. | Block save and show entitlement limit. | Critical |
| VAL-FAC-204 | Site-level approved overrides must not be overwritten. | Skip overridden Sites and log result. | High |
| VAL-FAC-205 | User must have settings permission. | Deny access and log event. | Critical |

### Business Rules

- BA-02 BR-FAC-001 - Facility Registration
- BA-02 BR-FAC-002 - Facility Subscription
- BA-02 BR-FAC-003 - Facility Type
- BA-02 BR-FAC-006 - Facility Status
- BA-02 BR-FAC-008 - Facility Services
- BA-02 BR-ORG-004 - Organization Policies
- BA-02 BR-ORG-010 - Organization Audit Trail

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| facility.settings.view | Organization Administrator, Facility Manager | Read | Required to view settings |
| facility.settings.update | Organization Administrator | Update | Required for full settings update |
| facility.settings.maintain | Facility Manager | Update | Limited setting maintenance where allowed |
| facility.settings.approve | Authorized Approver | Approve | Required for governed settings |

### Security Considerations

Facility Settings shall be scoped to the Facility and Organization. Settings that influence access, billing, or compliance shall require elevated permissions or approval where configured. All changes shall be auditable.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Facility Configured | Organization Administrator, Facility Manager | In-App, Email | Settings saved | Include changed setting categories |
| Facility Configuration Approval Required | Approver | In-App, Email | Governed setting submitted | Include change reason and impact |
| Facility Configuration Propagated | Site Administrator | In-App | Inherited setting applied to Site | Include affected setting category |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| FacilitySettingsUpdated | Facility Management | Site Management, Reporting Service, Audit Service |
| FacilitySettingsPropagationCompleted | Facility Management | Notification Service, Audit Service |
| FacilitySettingsApprovalRequested | Facility Management | Approval Workflow Service |

### Audit Events

| Audit Event | Trigger | Actor | Entity | Data Captured |
|---|---|---|---|---|
| Facility Settings Viewed | Settings opened | Authorized user | Facility Settings | Facility ID, actor, timestamp |
| Facility Settings Updated | Settings saved | Authorized user | Facility Settings | Previous values, new values, reason |
| Facility Settings Propagated | Site inheritance updated | System | Facility Settings | Affected Site references and status |

### Reports Generated

- Facility Configuration Report
- Facility Summary Report
- Configuration Change Report
- Executive Dashboard

### Related Screens

- Facility Settings
- Facility Configuration Impact
- Facility Dashboard
- Approval Request
- Audit History

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/facilities/{facilityId}/settings | GET | Authorized token | Retrieve Facility Settings | 200 OK with settings resource |
| /api/v1/facilities/{facilityId}/settings | PATCH | Organization Administrator token | Update Facility Settings | 200 OK with updated settings |
| /api/v1/facilities/{facilityId}/settings/impact | POST | Authorized token | Evaluate configuration impact | 200 OK with impact summary |
| /api/v1/facilities/{facilityId}/settings/propagation-status | GET | Authorized token | Retrieve propagation status | 200 OK with propagation details |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Facility | Read | Validate Facility scope and status | Parent context |
| Facility Settings | Read, Update | Store Facility configuration | Primary entity |
| Facility Type | Read | Validate capability support | Configuration constraint |
| Facility Policy | Read | Validate policy restrictions | Related governance |
| License | Read | Validate entitlement limits | Activation and capability dependency |
| Audit Log | Insert | Record settings changes | Required |
| Notification | Insert | Queue configuration notices | Conditional |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Draft | Save settings | Draft Configuration Complete | Organization Administrator | Mandatory settings complete |
| Active | Update settings | Active | Organization Administrator | Valid setting change |
| Active | Submit governed settings | Active with Pending Approval | Authorized user | Approval required |
| Suspended | Update permitted settings | Suspended | Organization Administrator | Limited maintenance allowed |
| Archived | Attempt settings update | Archived | Authorized user | Update blocked |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| FAC-201 | Facility setting violates Organization policy. | Policy constraint failure | Select an allowed value |
| FAC-202 | Facility Type does not support this setting. | Unsupported capability | Review Facility Type |
| FAC-203 | Setting exceeds Facility license entitlement. | License limit exceeded | Adjust value or update license |
| FAC-204 | You do not have permission to update Facility Settings. | Missing permission | Request access |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Save valid settings | Given the user has settings permission | When valid Facility settings are submitted | Then the system shall save the settings |
| Enforce Facility Type | Given a setting is unsupported by Facility Type | When the user attempts to configure it | Then the system shall prevent configuration |
| Enforce license boundary | Given a setting exceeds license entitlement | When the user saves | Then the system shall block the update |
| Preserve Site overrides | Given Sites have approved overrides | When Facility settings propagate | Then approved Site overrides shall remain unchanged |

### Dependencies

- Organization Settings
- Facility Type master data
- License Service
- Site Management
- Approval Workflow Service
- Audit Service

### Operational Considerations

Configuration propagation and entitlement validation failures shall be observable through logs and support dashboards.

### Non-Functional Considerations

Facility Settings shall support configurability, scalability, maintainability, secure scoping, and reliable propagation to many Sites.

### Assumptions

- Organization policies define the upper governance boundary for Facility Settings.
- Facility Type determines available capabilities.
- License entitlement may restrict operational settings.

### Success Criteria

Facility Settings are configurable within governance limits and correctly establish the operational baseline for downstream Sites and services.

### Related Functional Requirements

- FR-ORG-003 - Configure Organization Settings
- FR-FAC-004 - Assign Facility Type
- FR-FAC-005 - Configure Operating Hours
- FR-FAC-006 - Configure Capacity Limits
- FR-FAC-012 - Manage Facility Policies

### Notes

Facility Settings configure baseline behavior; specific operational transactions are handled by downstream modules.

---

## FR-FAC-004 - Assign Facility Type

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-FAC-004 |
| Requirement Name | Assign Facility Type |
| Functional Module | Facility Management |
| Business Domain | Facility |
| Business Capability | Facility Configuration |
| Requirement Type | Functional |
| Requirement Category | Configuration |
| Requirement Version | 1.0 |
| Requirement Status | Approved |
| Priority | Critical |
| Complexity | High |
| Release Version | 1.0 |
| Owner | Product Management |

### Traceability References

| Traceability Type | Reference |
|---|---|
| Business Requirement | BA-08 BR-004 Facility Configuration |
| Business Rule | BA-02 BR-FAC-003, BR-FAC-008, BR-FAC-006, BR-ORG-004, BR-ORG-010 |
| Business Process | BA-03 BP-FAC-004 Assign Facility Type |
| Business Process Flow | BA-04 Section 10 Facility Management Flow |
| Persona | BA-05 Organization Administrator |
| User Journey | BA-06 Section 4 Organization Administrator Journey |
| Stakeholder | BA-07 Organization Administrator, Facility Manager |
| Non-Functional Requirement | BA-09 Section 2.8 Configurability, Section 2.9 Extensibility |
| Assumption / Constraint / Risk | BA-10 BA-ASS-007, BA-CON-006 |

### Purpose

To assign exactly one Facility Type to each Facility so the platform can determine applicable capabilities, workflows, settings, services, and UI behavior.

### Functional Requirement

The system shall allow an Organization Administrator to assign or change a Facility Type according to lifecycle, dependency, approval, and configuration rules.

### Business Justification

Facility Type enables Digitize to support Swimming Pools initially and expand to Gyms, Yoga Studios, Dance Studios, Sports Academies, and other activity-based businesses through configuration rather than redevelopment.

### Actors

- Organization Administrator
- Facility Manager
- License Service
- Configuration Service
- Audit Service
- Notification Service

### Preconditions

- Facility exists.
- Parent Organization is Active.
- User is authenticated.
- User has Facility Type assignment permission.
- Facility Type master data is active.
- Facility lifecycle status permits assignment or change.

### Trigger

Organization Administrator selects or changes Facility Type from Facility Profile or Facility Settings.

### In Scope

- Assign one active Facility Type.
- Validate Facility Type availability.
- Apply default configuration baseline.
- Evaluate impact on services, settings, and downstream Sites.
- Restrict unsafe type changes after operations begin.
- Record audit and notification events.

### Out of Scope

- Creating global Facility Type master data.
- Custom module development.
- Site Type configuration.
- Membership plan design.
- Activity setup.

### Inputs

- Facility ID
- Facility Type ID
- Change reason
- Effective date, if applicable
- Confirmation of impact
- Approval reference, if required

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Facility ID | Facility receiving type assignment | Identifier | Yes | System | Must exist and match Organization scope | Primary context |
| Facility Type ID | Selected Facility Type | Identifier | Yes | Organization Administrator | Must be active and allowed | Exactly one per Facility |
| Change Reason | Reason for changing type | Text | Conditional | Organization Administrator | Required when changing existing type | Audit requirement |
| Effective Date | Date type change becomes effective | Date | Conditional | Organization Administrator | Must satisfy lifecycle policy | Usually immediate in Draft |
| Impact Confirmation | User confirmation of capability impact | Boolean | Conditional | Organization Administrator | Required for existing Facility changes | Prevents accidental disruption |

### Main Flow

1. Organization Administrator opens Facility Type section.
2. The system loads available Facility Types and current Facility configuration.
3. Organization Administrator selects a Facility Type.
4. The system validates Facility Type status, Organization eligibility, lifecycle status, license compatibility, and operational dependencies.
5. The system displays impacted capabilities, settings, services, and downstream Sites.
6. Organization Administrator confirms assignment or change.
7. If approval is required, the system routes the request for approval.
8. If approval is not required, or after approval is granted, the system assigns the Facility Type.
9. The system applies Facility Type default configuration where safe.
10. The system records audit events and sends notifications.

### Alternate Flows

- If the Facility is Draft, Facility Type assignment may occur without approval.
- If the Facility has operational transactions, Facility Type changes may be blocked or approval-gated.
- If the selected Facility Type has additional required settings, the system marks readiness as incomplete until configured.

### Exception Flows

- If Facility Type is inactive, the system blocks assignment.
- If Facility Type is incompatible with license entitlement, the system blocks assignment or activation readiness.
- If changing type would invalidate active services, the system blocks or requires approval based on policy.
- If the user lacks permission, the system denies the action and logs it.

### Outputs

- Facility Type assigned.
- Updated Facility capability context.
- Updated configuration baseline.
- Impact summary.
- Audit and notification events.

### UI Behaviour

The UI shall show current Facility Type, available types, capability summary, downstream impact, and locked-state reasons. Facility Type changes shall require confirmation when existing configuration or operational history may be affected.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-FAC-301 | Every Facility must have exactly one Facility Type. | Block save or activation readiness. | Critical |
| VAL-FAC-302 | Facility Type must be active and allowed for the Organization. | Block assignment. | Critical |
| VAL-FAC-303 | Facility Type must be compatible with license entitlement. | Block assignment or mark activation blocker. | Critical |
| VAL-FAC-304 | Facility Type change after operational activity requires governance. | Block or route for approval. | High |
| VAL-FAC-305 | Facility Type defaults must not overwrite governed existing configuration without approval. | Preserve existing values or require approval. | High |

### Business Rules

- BA-02 BR-FAC-003 - Facility Type
- BA-02 BR-FAC-008 - Facility Services
- BA-02 BR-FAC-006 - Facility Status
- BA-02 BR-ORG-004 - Organization Policies
- BA-02 BR-ORG-010 - Organization Audit Trail

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| facility.type.view | Organization Administrator, Facility Manager | Read | Required to view Facility Type |
| facility.type.assign | Organization Administrator | Execute | Required to assign Facility Type |
| facility.type.change | Organization Administrator | Update | Required to change existing type |
| facility.type.approve | Authorized Approver | Approve | Required when governed |

### Security Considerations

Facility Type assignment shall be restricted to authorized Organization-level users because it controls module availability and operational behavior. All changes shall remain tenant-scoped and auditable.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Facility Type Assigned | Organization Administrator, Facility Manager | In-App, Email | Facility Type assigned | Include type and affected capabilities |
| Facility Type Change Approval Required | Approver | In-App, Email | Governed type change submitted | Include impact summary |
| Facility Type Change Blocked | Organization Administrator | In-App | Validation prevents change | Include blocker reason |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| FacilityTypeAssigned | Facility Management | Configuration Service, License Service, Audit Service |
| FacilityTypeChangeRequested | Facility Management | Approval Workflow Service |
| FacilityCapabilityContextUpdated | Configuration Service | Site Management, Reporting Service |

### Audit Events

| Audit Event | Trigger | Actor | Entity | Data Captured |
|---|---|---|---|---|
| Facility Type Viewed | Type section opened | Authorized user | Facility Type | Facility ID, actor, timestamp |
| Facility Type Assigned | Type assigned | Organization Administrator | Facility | Previous type, new type, reason |
| Facility Capability Context Updated | Defaults applied | System | Facility Settings | Applied capabilities and skipped values |

### Reports Generated

- Facility Configuration Report
- Facility Summary Report
- Facility Type Usage Report

### Related Screens

- Facility Type Management
- Facility Profile
- Facility Settings
- Configuration Impact Summary
- Approval Request

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/facility-types | GET | Authorized token | Retrieve active Facility Types | 200 OK with Facility Type list |
| /api/v1/facilities/{facilityId}/type | GET | Authorized token | Retrieve assigned Facility Type | 200 OK with type details |
| /api/v1/facilities/{facilityId}/type | PUT | Organization Administrator token | Assign or change Facility Type | 200 OK with updated type assignment |
| /api/v1/facilities/{facilityId}/type/impact | POST | Organization Administrator token | Evaluate type change impact | 200 OK with impact summary |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Facility | Read, Update | Store assigned Facility Type | Primary context |
| Facility Type | Read | Validate selected type | Master data |
| Facility Settings | Read, Update | Apply type defaults | Conditional |
| License | Read | Validate compatibility | Entitlement check |
| Audit Log | Insert | Record type assignment | Required |
| Notification | Insert | Queue notifications | Conditional |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Facility Type Unassigned | Assign Facility Type | Facility Type Assigned | Organization Administrator | Active type selected |
| Facility Type Assigned | Change type in Draft | Facility Type Assigned | Organization Administrator | No blocking dependency |
| Facility Type Assigned | Submit governed type change | Pending Approval | Organization Administrator | Approval required |
| Pending Approval | Approve type change | Facility Type Assigned | Authorized Approver | Approval granted |
| Pending Approval | Reject type change | Facility Type Assigned | Authorized Approver | Existing type retained |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| FAC-301 | Facility Type is required. | Missing type | Select a Facility Type |
| FAC-302 | Selected Facility Type is not active. | Inactive master data | Select another Facility Type |
| FAC-303 | Facility Type is not compatible with current license. | Entitlement mismatch | Update license or select another type |
| FAC-304 | Facility Type cannot be changed because operational dependencies exist. | Active dependency | Resolve blockers or request approval |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Assign Facility Type | Given a Draft Facility and active Facility Type | When the Organization Administrator assigns the type | Then the system shall save exactly one Facility Type |
| Block inactive type | Given the selected Facility Type is inactive | When assignment is attempted | Then the system shall block the assignment |
| Show impact | Given Facility Type change affects capabilities | When impact is evaluated | Then the system shall display affected settings and services |
| Audit type assignment | Given Facility Type is assigned or changed | When the transaction completes | Then audit history shall record previous and new type |

### Dependencies

- Facility Type master data
- License Service
- Facility Settings
- Approval Workflow Service
- Audit Service

### Operational Considerations

Facility Type changes shall be treated carefully because they can affect enabled modules, UI behavior, operating settings, and downstream service configuration.

### Non-Functional Considerations

Facility Type assignment shall support extensibility, configurability, maintainability, auditability, and reliable capability resolution.

### Assumptions

- Facility Type master data is maintained through Platform Administration.
- Every Facility has exactly one Facility Type.
- Existing operational transactions may restrict type changes.

### Success Criteria

The Facility has a valid Facility Type that drives supported services, workflows, default configuration, and future extensibility.

### Related Functional Requirements

- FR-PLT-002 - Manage Global Master Data
- FR-FAC-001 - Create Facility
- FR-FAC-003 - Configure Facility Settings
- FR-FAC-008 - Activate Facility
- FR-LIC-001 - Manage License Allocation

### Notes

Facility Type is central to Digitize's multi-vertical expansion model.

---

## FR-FAC-005 - Configure Operating Hours

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-FAC-005 |
| Requirement Name | Configure Operating Hours |
| Functional Module | Facility Management |
| Business Domain | Facility |
| Business Capability | Facility Operations |
| Requirement Type | Functional |
| Requirement Category | Configuration |
| Requirement Version | 1.0 |
| Requirement Status | Approved |
| Priority | High |
| Complexity | Medium |
| Release Version | 1.0 |
| Owner | Product Management |

### Traceability References

| Traceability Type | Reference |
|---|---|
| Business Requirement | BA-08 BR-004 Facility Configuration |
| Business Rule | BA-02 BR-FAC-005, BR-FAC-006, BR-FAC-008, BR-ORG-004, BR-ORG-010 |
| Business Process | BA-03 BP-FAC-005 Configure Operating Hours |
| Business Process Flow | BA-04 Section 10 Facility Management Flow |
| Persona | BA-05 Organization Administrator, Facility Manager |
| User Journey | BA-06 Section 5 Facility Manager Journey |
| Stakeholder | BA-07 Organization Administrator, Facility Manager, Site Administrator |
| Non-Functional Requirement | BA-09 Section 2.8 Configurability |
| Assumption / Constraint / Risk | BA-10 BA-ASS-006 |

### Purpose

To define Facility operating schedules before customer-facing and operational transactions are allowed.

### Functional Requirement

The system shall allow authorized users to configure Facility Operating Hours, exceptions, holidays, and effective schedules within Organization and Facility policies.

### Business Justification

Operating Hours govern attendance, activity scheduling, batch planning, personal training availability, customer access, and operational staffing.

### Actors

- Organization Administrator
- Facility Manager
- Site Administrator
- Notification Service
- Audit Service

### Preconditions

- Facility exists.
- Facility is not Archived.
- Facility Type is assigned.
- User is authenticated.
- User has operating hours permission.

### Trigger

An authorized user opens Operating Hours Management and submits schedule changes.

### In Scope

- Configure weekly operating hours.
- Configure breaks, closures, holidays, and exceptions.
- Validate overlaps and effective dates.
- Propagate schedule defaults to Sites where applicable.
- Record audit and notifications.

### Out of Scope

- Staff shift scheduling.
- Batch schedule creation.
- Personal training booking.
- Attendance check-in.
- Site-specific operating hours overrides.

### Inputs

- Facility ID
- Day of week
- Opening time
- Closing time
- Break periods
- Holiday or closure dates
- Effective date
- Recurrence pattern
- Change reason

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Day of Week | Operating day | Enum | Yes | Authorized user | Must be valid weekday | Used for weekly schedule |
| Opening Time | Facility opening time | Time | Conditional | Authorized user | Must be before closing time | Required for operating days |
| Closing Time | Facility closing time | Time | Conditional | Authorized user | Must be after opening time | Required for operating days |
| Break Period | Non-operational interval | Time Range | No | Authorized user | Must fall within open-close window | Multiple allowed if policy permits |
| Holiday Date | Closure date | Date | No | Authorized user | Must not conflict with schedule rules | Used for exceptions |
| Effective Date | Schedule effective date | Date | Yes | Authorized user | Must satisfy policy | Supports future changes |
| Change Reason | Reason for schedule change | Text | Conditional | Authorized user | Required for governed changes | Audit field |

### Main Flow

1. Authorized user opens Operating Hours Management.
2. The system loads current Facility hours, Organization policy, Facility Type constraints, and Site inheritance status.
3. User configures weekly hours, breaks, holidays, closures, or effective schedules.
4. The system validates time ranges, overlaps, policy constraints, effective dates, and permission.
5. The system evaluates downstream scheduling impact.
6. If approval is required, the system creates an approval request.
7. If approval is not required, or after approval is granted, the system saves Operating Hours.
8. The system propagates inherited schedules to Sites where applicable.
9. The system updates scheduling context for affected modules.
10. The system records audit events and sends notifications.

### Alternate Flows

- If a Facility is closed on a day, opening and closing times are not required for that day.
- If a schedule is future-dated, the system stores it as scheduled until the effective date.
- If Sites have approved operating-hour overrides, the system preserves those overrides.

### Exception Flows

- If opening time is after closing time, the system blocks save.
- If operating hours overlap incorrectly with breaks or closures, the system shows validation errors.
- If schedule change conflicts with active bookings or batches, the system displays impact and may require approval.
- If Facility is Archived, the system blocks updates.

### Outputs

- Updated Facility Operating Hours.
- Schedule impact summary.
- Propagation status.
- Updated scheduling context.
- Notifications and audit events.

### UI Behaviour

Operating Hours Management shall provide weekly calendar controls, time pickers, exception lists, holiday indicators, effective-date labels, and impact warnings. Site inheritance and overrides shall be visible where applicable.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-FAC-401 | Operating days must have valid opening and closing times. | Block save and highlight invalid day. | High |
| VAL-FAC-402 | Opening time must be before closing time. | Block save. | High |
| VAL-FAC-403 | Break periods must fall within operating hours. | Block save. | High |
| VAL-FAC-404 | Operating hours must comply with Organization policy. | Block save or require approval. | High |
| VAL-FAC-405 | Operating hour changes affecting active schedules require impact review. | Display impact and require confirmation or approval. | High |

### Business Rules

- BA-02 BR-FAC-005 - Facility Operating Hours
- BA-02 BR-FAC-006 - Facility Status
- BA-02 BR-FAC-008 - Facility Services
- BA-02 BR-ORG-004 - Organization Policies
- BA-02 BR-ORG-010 - Organization Audit Trail

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| facility.operating-hours.view | Organization Administrator, Facility Manager | Read | Required to view hours |
| facility.operating-hours.update | Organization Administrator | Update | Required for full schedule updates |
| facility.operating-hours.maintain | Facility Manager | Update | Limited maintenance where allowed |
| facility.operating-hours.approve | Authorized Approver | Approve | Required for governed changes |

### Security Considerations

Operating Hours shall be editable only by authorized users within Facility scope. Schedule changes impacting customer access or billing-sensitive services shall be auditable and approval-gated where configured.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Operating Hours Updated | Facility Manager, Site Administrator | In-App, Email | Hours saved | Include effective date and changed days |
| Operating Hours Approval Required | Approver | In-App, Email | Governed schedule submitted | Include impact summary |
| Schedule Impact Detected | Facility Manager | In-App | Active schedules affected | Include affected schedules |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| FacilityOperatingHoursUpdated | Facility Management | Site Management, Activity Management, Attendance Management |
| FacilityScheduleImpactDetected | Facility Management | Notification Service, Approval Workflow Service |
| FacilityOperatingHoursPropagated | Facility Management | Audit Service, Reporting Service |

### Audit Events

| Audit Event | Trigger | Actor | Entity | Data Captured |
|---|---|---|---|---|
| Operating Hours Viewed | Screen opened | Authorized user | Facility Operating Hours | Facility ID, actor, timestamp |
| Operating Hours Updated | Schedule saved | Authorized user | Facility Operating Hours | Previous schedule, new schedule, reason |
| Operating Hours Propagated | Site inheritance updated | System | Facility Operating Hours | Affected Sites and propagation status |

### Reports Generated

- Facility Configuration Report
- Operating Hours Report
- Facility Dashboard

### Related Screens

- Operating Hours Management
- Facility Settings
- Facility Dashboard
- Schedule Impact Summary
- Approval Request

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/facilities/{facilityId}/operating-hours | GET | Authorized token | Retrieve Facility Operating Hours | 200 OK with schedule |
| /api/v1/facilities/{facilityId}/operating-hours | PUT | Authorized token | Save Facility Operating Hours | 200 OK with updated schedule |
| /api/v1/facilities/{facilityId}/operating-hours/impact | POST | Authorized token | Evaluate schedule impact | 200 OK with impact summary |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Facility | Read | Validate scope and status | Parent context |
| Facility Operating Hours | Create, Read, Update | Store schedule configuration | Primary entity |
| Facility Policy | Read | Validate schedule rules | Governance |
| Audit Log | Insert | Record schedule changes | Required |
| Notification | Insert | Queue schedule notifications | Conditional |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Not Configured | Save operating hours | Configured | Authorized user | Valid weekly schedule |
| Configured | Schedule future change | Scheduled Change | Authorized user | Future effective date |
| Scheduled Change | Effective date reached | Configured | System | Scheduled change active |
| Configured | Submit governed change | Pending Approval | Authorized user | Approval required |
| Pending Approval | Reject change | Configured | Authorized Approver | Existing schedule retained |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| FAC-401 | Opening time must be before closing time. | Invalid time range | Correct operating times |
| FAC-402 | Break period must be within operating hours. | Invalid break range | Adjust break period |
| FAC-403 | Operating hours change conflicts with active schedules. | Schedule dependency | Review impact |
| FAC-404 | You do not have permission to update operating hours. | Missing permission | Request access |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Save valid hours | Given the user has operating hours permission | When valid hours are submitted | Then the system shall save Facility Operating Hours |
| Block invalid range | Given opening time is after closing time | When the user saves | Then the system shall block save |
| Propagate hours | Given Sites inherit Facility hours | When hours are saved | Then inherited Site schedules shall be updated |
| Preserve audit | Given operating hours change | When saved | Then audit history shall record previous and new schedule |

### Dependencies

- Organization policies
- Site Management
- Activity and Batch Management
- Attendance Management
- Approval Workflow Service
- Audit Service

### Operational Considerations

Schedule changes should expose impact on future batches, bookings, attendance windows, and Site inheritance before confirmation.

### Non-Functional Considerations

Operating Hours configuration shall be usable, auditable, timezone-aware, maintainable, and reliable for schedule-dependent modules.

### Assumptions

- Facility timezone is derived from Organization or Facility Settings.
- Site-level overrides may exist and must be preserved.
- Downstream scheduling modules consume Facility Operating Hours.

### Success Criteria

Facility Operating Hours are valid, policy-compliant, visible to operational teams, and consistently applied to downstream scheduling contexts.

### Related Functional Requirements

- FR-FAC-003 - Configure Facility Settings
- FR-FAC-008 - Activate Facility
- FR-SIT-004 - Configure Site Operating Hours
- FR-ACT-001 - Configure Activities
- FR-BAT-001 - Manage Batch Schedule

### Notes

Operating Hours are mandatory before a Facility can accept customers or deliver operational services.

---

## FR-FAC-006 - Configure Capacity Limits

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-FAC-006 |
| Requirement Name | Configure Capacity Limits |
| Functional Module | Facility Management |
| Business Domain | Facility |
| Business Capability | Facility Operations |
| Requirement Type | Functional |
| Requirement Category | Configuration |
| Requirement Version | 1.0 |
| Requirement Status | Approved |
| Priority | High |
| Complexity | High |
| Release Version | 1.0 |
| Owner | Product Management |

### Traceability References

| Traceability Type | Reference |
|---|---|
| Business Requirement | BA-08 BR-004 Facility Configuration |
| Business Rule | BA-02 BR-FAC-004, BR-FAC-006, BR-FAC-008, BR-ORG-004, BR-ORG-010 |
| Business Process | BA-03 BP-FAC-006 Configure Capacity Limits |
| Business Process Flow | BA-04 Section 10 Facility Management Flow |
| Persona | BA-05 Organization Administrator, Facility Manager |
| User Journey | BA-06 Section 5 Facility Manager Journey |
| Stakeholder | BA-07 Organization Administrator, Facility Manager, Site Administrator |
| Non-Functional Requirement | BA-09 Section 2.3 Scalability, Section 8 Business Configurability |
| Assumption / Constraint / Risk | BA-10 BA-ASS-006, BA-RSK-004 |

### Purpose

To define Facility-level operational capacity limits that control safe, compliant, and commercially viable service delivery.

### Functional Requirement

The system shall allow authorized users to configure Facility Capacity limits for attendance, sessions, batches, occupancy, equipment, and bookings within Organization policy and license entitlement constraints.

### Business Justification

Capacity management prevents overbooking, supports safety and service quality, protects customer experience, and gives managers operational control over high-demand services.

### Actors

- Organization Administrator
- Facility Manager
- Site Administrator
- License Service
- Notification Service
- Audit Service

### Preconditions

- Facility exists.
- Facility is not Archived.
- Facility Type is assigned.
- User is authenticated.
- User has capacity management permission.
- Applicable capacity categories are enabled for Facility Type.

### Trigger

An authorized user opens Capacity Limits Management and submits capacity changes.

### In Scope

- Configure Facility-level capacity categories.
- Validate policy and license limits.
- Enforce upper boundaries for Sites.
- Evaluate operational impact.
- Notify stakeholders and record audit events.

### Out of Scope

- Real-time attendance counting.
- Batch enrollment processing.
- Equipment inventory management.
- Site-specific capacity overrides.
- Emergency closure workflow.

### Inputs

- Facility ID
- Capacity category
- Capacity limit
- Effective date
- Applies-to scope
- Threshold alert settings
- Change reason

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Capacity Category | Type of capacity limit | Master Data | Yes | System | Must be enabled for Facility Type | Examples include daily attendance and batch capacity |
| Capacity Limit | Maximum allowed capacity | Number | Yes | Authorized user | Must be positive and within policy/license limits | Primary limit |
| Effective Date | Date limit becomes active | Date | Yes | Authorized user | Must satisfy policy | Supports future limits |
| Applies-To Scope | Scope of capacity rule | Enum | Yes | Authorized user | Facility or inherited Site baseline | Site limits cannot exceed Facility limit |
| Threshold Alert | Alert percentage or count | Number | No | Authorized user | Must be below capacity limit | Supports operational alerts |
| Change Reason | Reason for capacity update | Text | Conditional | Authorized user | Required for governed changes | Audit field |

### Main Flow

1. Authorized user opens Capacity Limits Management.
2. The system loads current limits, Facility Type capability, Organization policy, license entitlement, and Site override status.
3. User selects capacity category and enters limit values.
4. The system validates numeric rules, policy constraints, license entitlement, Facility status, and downstream Site limits.
5. The system evaluates operational impact on active schedules, batches, bookings, and attendance.
6. If approval is required, the system creates an approval request.
7. If approval is not required, or after approval is granted, the system saves the capacity limits.
8. The system propagates upper-bound constraints to Sites where applicable.
9. The system updates capacity reports and dashboard widgets.
10. The system records audit events and sends notifications.

### Alternate Flows

- If no Site exists, capacity limits are saved as Facility-level baseline only.
- If Site capacity is lower than Facility capacity, the Site limit remains unchanged.
- If capacity reduction affects active bookings, the system displays impact and may require approval.

### Exception Flows

- If capacity exceeds license entitlement, the system blocks saving.
- If capacity is lower than existing committed usage, the system blocks or requires approval based on policy.
- If capacity category is unsupported by Facility Type, the system hides or disables the category.
- If Facility is Archived, the system blocks updates.

### Outputs

- Updated Facility Capacity records.
- Capacity impact summary.
- Site upper-bound constraints.
- Capacity alerts configuration.
- Notifications and audit events.

### UI Behaviour

Capacity Limits Management shall show capacity categories, current limits, license limits, Site usage, threshold alerts, and impact summaries. The UI shall distinguish hard limits from alert thresholds.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-FAC-501 | Capacity limit must be a positive number. | Block save. | High |
| VAL-FAC-502 | Facility capacity cannot exceed Organization policy or license entitlement. | Block save and show limit source. | Critical |
| VAL-FAC-503 | Site capacity limits cannot exceed Facility capacity. | Block or flag Site configuration conflict. | Critical |
| VAL-FAC-504 | Capacity reduction affecting committed operations requires impact review. | Display impact and require approval where configured. | High |
| VAL-FAC-505 | Capacity category must be supported by Facility Type. | Disable unsupported category. | High |

### Business Rules

- BA-02 BR-FAC-004 - Facility Capacity
- BA-02 BR-FAC-006 - Facility Status
- BA-02 BR-FAC-008 - Facility Services
- BA-02 BR-ORG-004 - Organization Policies
- BA-02 BR-ORG-010 - Organization Audit Trail

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| facility.capacity.view | Organization Administrator, Facility Manager | Read | Required to view limits |
| facility.capacity.update | Organization Administrator | Update | Required for capacity configuration |
| facility.capacity.maintain | Facility Manager | Update | Limited capacity maintenance where allowed |
| facility.capacity.approve | Authorized Approver | Approve | Required for governed changes |

### Security Considerations

Capacity configuration shall be accessible only to authorized Facility-scoped users. Changes affecting safety, commercial commitments, or license entitlement shall be auditable and approval-gated where configured.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Capacity Limits Updated | Facility Manager, Site Administrator | In-App, Email | Capacity saved | Include changed categories and effective date |
| Capacity Approval Required | Approver | In-App, Email | Governed capacity change submitted | Include impact summary |
| Capacity Constraint Violation | Organization Administrator, Facility Manager | In-App | Requested limit violates rule | Include violated constraint |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| FacilityCapacityUpdated | Facility Management | Site Management, Attendance Management, Batch Management |
| FacilityCapacityImpactDetected | Facility Management | Approval Workflow Service, Notification Service |
| FacilityCapacityConstraintApplied | Facility Management | Reporting Service, Audit Service |

### Audit Events

| Audit Event | Trigger | Actor | Entity | Data Captured |
|---|---|---|---|---|
| Capacity Limits Viewed | Screen opened | Authorized user | Facility Capacity | Facility ID, actor, timestamp |
| Capacity Limits Updated | Limits saved | Authorized user | Facility Capacity | Previous limit, new limit, category, reason |
| Capacity Constraint Violation | Invalid limit submitted | Authorized user | Facility Capacity | Submitted value and violated constraint |

### Reports Generated

- Capacity Report
- Facility Dashboard
- Facility Configuration Report
- Operational Dashboard

### Related Screens

- Capacity Limits Management
- Facility Dashboard
- Capacity Overview
- Schedule Impact Summary
- Approval Request

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/facilities/{facilityId}/capacity-limits | GET | Authorized token | Retrieve Facility capacity limits | 200 OK with capacity list |
| /api/v1/facilities/{facilityId}/capacity-limits | PUT | Authorized token | Save Facility capacity limits | 200 OK with updated limits |
| /api/v1/facilities/{facilityId}/capacity-limits/impact | POST | Authorized token | Evaluate capacity impact | 200 OK with impact summary |
| /api/v1/facilities/{facilityId}/capacity-limits/violations | GET | Authorized token | Retrieve capacity violations | 200 OK with violation list |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Facility | Read | Validate Facility scope and status | Parent context |
| Facility Capacity | Create, Read, Update | Store capacity limits | Primary entity |
| Facility Type | Read | Validate supported categories | Capability source |
| License | Read | Validate entitlement boundaries | Limit source |
| Facility Policy | Read | Validate capacity policy | Governance |
| Audit Log | Insert | Record capacity changes | Required |
| Notification | Insert | Queue capacity notifications | Conditional |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Not Configured | Save capacity limits | Configured | Authorized user | Valid limits |
| Configured | Schedule capacity change | Scheduled Change | Authorized user | Future effective date |
| Scheduled Change | Effective date reached | Configured | System | Change becomes active |
| Configured | Submit governed change | Pending Approval | Authorized user | Approval required |
| Pending Approval | Reject change | Configured | Authorized Approver | Existing limits retained |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| FAC-501 | Capacity limit must be greater than zero. | Invalid numeric value | Enter a positive value |
| FAC-502 | Capacity exceeds allowed entitlement. | License or policy limit exceeded | Reduce capacity or update entitlement |
| FAC-503 | Capacity reduction conflicts with existing commitments. | Active operational dependency | Review impact |
| FAC-504 | Capacity category is not supported for this Facility Type. | Unsupported category | Select a supported category |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Save valid capacity | Given the user has capacity permission | When valid capacity limits are submitted | Then the system shall save the limits |
| Enforce entitlement | Given capacity exceeds license entitlement | When the user saves | Then the system shall block the update |
| Enforce Site upper bound | Given Site capacity exceeds Facility limit | When Facility limit is applied | Then the system shall flag or block the Site conflict |
| Audit capacity change | Given capacity limits are updated | When saved | Then audit history shall capture previous and new values |

### Dependencies

- Facility Type configuration
- Organization policy
- License Service
- Site Management
- Attendance Management
- Batch Management
- Audit Service

### Operational Considerations

Capacity changes shall surface impact on operational commitments and future schedules before confirmation.

### Non-Functional Considerations

Capacity configuration shall be reliable, auditable, scalable, policy-driven, and capable of supporting high-volume operational checks.

### Assumptions

- Facility capacity defines an upper boundary for Site capacity.
- License entitlement may restrict maximum capacity.
- Downstream modules enforce active capacity rules.

### Success Criteria

Facility capacity is configured accurately and prevents operational overuse while preserving customer experience and compliance.

### Related Functional Requirements

- FR-FAC-003 - Configure Facility Settings
- FR-FAC-005 - Configure Operating Hours
- FR-FAC-008 - Activate Facility
- FR-SIT-005 - Configure Site Capacity Limits
- FR-ATT-001 - Record Attendance

### Notes

Capacity rules are configuration inputs for operational enforcement in Attendance, Batch, Booking, and Site modules.

---

## FR-FAC-007 - Assign Facility Manager

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-FAC-007 |
| Requirement Name | Assign Facility Manager |
| Functional Module | Facility Management |
| Business Domain | Facility |
| Business Capability | Workforce Management |
| Requirement Type | Functional |
| Requirement Category | Workflow |
| Requirement Version | 1.0 |
| Requirement Status | Approved |
| Priority | High |
| Complexity | Medium |
| Release Version | 1.0 |
| Owner | Product Management |

### Traceability References

| Traceability Type | Reference |
|---|---|
| Business Requirement | BA-08 Facility Management |
| Business Rule | BA-02 BR-FAC-007, BR-FAC-006, BR-ORG-005, BR-ORG-006, BR-ORG-010, BR-SEC-002 |
| Business Process | BA-03 BP-FAC-007 Assign Facility Manager |
| Business Process Flow | BA-04 Section 10 Facility Management Flow |
| Persona | BA-05 Organization Administrator, Facility Manager |
| User Journey | BA-06 Section 4 Organization Administrator Journey, Section 5 Facility Manager Journey |
| Stakeholder | BA-07 Organization Administrator, Facility Manager |
| Non-Functional Requirement | BA-09 Section 3.2 Authorization |
| Assumption / Constraint / Risk | BA-10 BA-ASS-006 |

### Purpose

To assign managerial responsibility for Facility operations, escalation handling, monitoring, and service delivery oversight.

### Functional Requirement

The system shall allow an Organization Administrator to assign, replace, or remove a Facility Manager according to staff eligibility, Organization policy, role assignment, and audit requirements.

### Business Justification

Every operational Facility requires accountable management so capacity, staffing, schedules, service delivery, alerts, and exceptions can be monitored and resolved.

### Actors

- Organization Administrator
- Facility Manager
- Identity Service
- Notification Service
- Audit Service

### Preconditions

- Facility exists.
- Facility is not Archived.
- Staff user exists within the Organization.
- User is authenticated.
- Organization Administrator has manager assignment permission.
- Staff role and eligibility rules are available.

### Trigger

Organization Administrator selects Assign Facility Manager from Facility Profile or Workforce Management.

### In Scope

- Assign Facility Manager.
- Replace Facility Manager.
- Remove Facility Manager where allowed.
- Validate staff eligibility.
- Update access scope or role association.
- Notify affected users.
- Record audit events.

### Out of Scope

- Creating staff accounts.
- Full role and permission configuration.
- Trainer assignment.
- Site staff scheduling.
- Payroll or HR management.

### Inputs

- Facility ID
- Staff user ID
- Assignment type
- Effective date
- Assignment reason
- Replacement reason, if applicable

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Facility ID | Facility receiving manager assignment | Identifier | Yes | System | Must exist and match Organization scope | Parent context |
| Staff User ID | Staff member assigned as manager | Identifier | Yes | Organization Administrator | Must belong to Organization and be active | Eligibility required |
| Assignment Type | Assign, replace, or remove | Enum | Yes | Organization Administrator | Must be supported action | Controls workflow |
| Effective Date | Date assignment becomes active | Date | Yes | Organization Administrator | Must satisfy policy | Supports planned replacement |
| Assignment Reason | Business reason | Text | Conditional | Organization Administrator | Required for replacement or removal | Audit field |

### Main Flow

1. Organization Administrator opens Facility Manager assignment.
2. The system loads current manager assignment and eligible staff users.
3. Organization Administrator selects staff user and assignment action.
4. The system validates staff eligibility, active account status, Organization membership, role compatibility, Facility scope, and lifecycle status.
5. The system displays access and responsibility impact.
6. Organization Administrator confirms assignment.
7. The system updates Facility Manager assignment.
8. The system updates access scope or role linkage where applicable.
9. The system sends notifications to previous and new managers.
10. The system records audit events.

### Alternate Flows

- If assigning a future-dated manager, the system schedules assignment activation.
- If replacing an existing manager, the system ends the previous assignment according to effective date.
- If multiple managers are permitted by policy, the system allows additional manager assignments.

### Exception Flows

- If selected staff user is inactive, the system blocks assignment.
- If selected user belongs to another Organization, the system blocks assignment.
- If manager removal would leave an Active Facility without required manager coverage, the system blocks removal.
- If Identity Service role update fails, the assignment is not completed and the failure is logged.

### Outputs

- Facility Manager assignment created or updated.
- Access scope updated where applicable.
- Notifications sent.
- Audit events recorded.
- Facility readiness status updated.

### UI Behaviour

The assignment UI shall display current manager, eligible staff list, role eligibility, assignment effective date, replacement warnings, and confirmation prompts. Ineligible users shall be hidden or displayed with non-selectable status and reason.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-FAC-601 | Facility Manager must be an active staff user within the Organization. | Block assignment. | Critical |
| VAL-FAC-602 | Staff user must have or be eligible for Facility Manager role. | Block assignment or prompt role assignment. | High |
| VAL-FAC-603 | Active Facility must retain required manager coverage. | Block removal if no replacement exists. | High |
| VAL-FAC-604 | Assignment effective date must satisfy Organization policy. | Block save. | Medium |
| VAL-FAC-605 | User must have manager assignment permission. | Deny action and log event. | Critical |

### Business Rules

- BA-02 BR-FAC-007 - Facility Staff Assignment
- BA-02 BR-FAC-006 - Facility Status
- BA-02 BR-ORG-005 - Organization Users
- BA-02 BR-ORG-006 - Role-Based Access
- BA-02 BR-ORG-010 - Organization Audit Trail
- BA-02 BR-SEC-002 - Role-Based Access Control

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| facility.manager.view | Organization Administrator, Facility Manager | Read | Required to view manager assignment |
| facility.manager.assign | Organization Administrator | Execute | Required to assign manager |
| facility.manager.replace | Organization Administrator | Update | Required to replace manager |
| facility.manager.remove | Organization Administrator | Update | Required to remove manager where allowed |

### Security Considerations

Manager assignment shall not automatically grant permissions outside assigned role and Facility scope. Access changes shall be synchronized securely with Identity Service and audited.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Facility Manager Assigned | New Facility Manager | In-App, Email | Manager assignment active | Include Facility name and responsibilities |
| Facility Manager Replaced | Previous Facility Manager | In-App, Email | Replacement completed | Include effective date |
| Facility Manager Assignment Failed | Organization Administrator | In-App | Assignment synchronization failed | Include failure reason |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| FacilityManagerAssigned | Facility Management | Identity Service, Notification Service, Audit Service |
| FacilityManagerReplaced | Facility Management | Identity Service, Notification Service |
| FacilityManagerAssignmentScheduled | Facility Management | Scheduler, Notification Service |

### Audit Events

| Audit Event | Trigger | Actor | Entity | Data Captured |
|---|---|---|---|---|
| Facility Manager Viewed | Assignment section opened | Authorized user | Facility | Facility ID, actor, timestamp |
| Facility Manager Assigned | Assignment saved | Organization Administrator | Facility, User | Staff user, effective date, role scope |
| Facility Manager Replaced | Replacement saved | Organization Administrator | Facility, User | Previous manager, new manager, reason |

### Reports Generated

- Facility Summary Report
- Staff Assignment Report
- Facility Configuration Report
- Audit Trail Report

### Related Screens

- Facility Profile
- Assign Facility Manager
- Staff Management
- Facility Dashboard
- Audit History

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/facilities/{facilityId}/managers | GET | Authorized token | Retrieve Facility Manager assignments | 200 OK with manager list |
| /api/v1/facilities/{facilityId}/managers | POST | Organization Administrator token | Assign Facility Manager | 201 Created with assignment |
| /api/v1/facilities/{facilityId}/managers/{assignmentId} | PATCH | Organization Administrator token | Update manager assignment | 200 OK with updated assignment |
| /api/v1/facilities/{facilityId}/managers/{assignmentId}/remove | POST | Organization Administrator token | Remove manager assignment | 200 OK with assignment status |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Facility | Read, Update | Store manager reference or readiness status | Parent context |
| User | Read | Validate staff user | Identity entity |
| Role Assignment | Create, Update | Apply manager role or scope | Identity dependency |
| Audit Log | Insert | Record manager assignment | Required |
| Notification | Insert | Queue manager notifications | Required |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| No Manager Assigned | Assign manager | Manager Assigned | Organization Administrator | Eligible staff user |
| Manager Assigned | Replace manager | Manager Assigned | Organization Administrator | Replacement eligible |
| Manager Assigned | Schedule replacement | Replacement Scheduled | Organization Administrator | Future effective date |
| Replacement Scheduled | Effective date reached | Manager Assigned | System | Scheduled change due |
| Manager Assigned | Remove manager | No Manager Assigned | Organization Administrator | Allowed only if policy permits |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| FAC-601 | Selected user is not eligible to be Facility Manager. | Staff eligibility failure | Select an eligible user |
| FAC-602 | Facility Manager must belong to the same Organization. | Tenant mismatch | Select Organization staff |
| FAC-603 | Active Facility requires manager coverage. | Removal would leave gap | Assign replacement manager |
| FAC-604 | Manager access could not be synchronized. | Identity Service failure | Retry or contact support |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Assign eligible manager | Given an active staff user is eligible | When assigned as Facility Manager | Then the system shall create the manager assignment |
| Block ineligible manager | Given selected user is inactive or outside Organization | When assignment is attempted | Then the system shall block assignment |
| Replace manager | Given an existing manager assignment | When a replacement is confirmed | Then the system shall end prior assignment and assign the new manager |
| Notify manager | Given assignment succeeds | When transaction completes | Then the new Facility Manager shall receive notification |

### Dependencies

- User & Role Management
- Identity Service
- Organization policy
- Notification Service
- Audit Service

### Operational Considerations

Manager assignment failures shall show whether the Facility assignment, Identity role sync, or notification step failed.

### Non-Functional Considerations

Manager assignment shall be secure, auditable, reliable, and maintainable while supporting Organizations with many Facilities and staff users.

### Assumptions

- Staff accounts are managed by User & Role Management.
- Organization policy determines whether multiple Facility Managers are allowed.
- Assignment may influence dashboard visibility and operational alerts.

### Success Criteria

Every operational Facility has accountable managerial coverage with correct role scope, notifications, and audit traceability.

### Related Functional Requirements

- FR-FAC-001 - Create Facility
- FR-FAC-008 - Activate Facility
- FR-USR-001 - Create Staff Account
- FR-USR-004 - Assign Role
- FR-FAC-011 - View Facility Dashboard

### Notes

Facility Manager assignment is a workforce governance capability and not a full staff management module.

---

## FR-FAC-008 - Activate Facility

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-FAC-008 |
| Requirement Name | Activate Facility |
| Functional Module | Facility Management |
| Business Domain | Facility |
| Business Capability | Facility Lifecycle |
| Requirement Type | Functional |
| Requirement Category | Workflow |
| Requirement Version | 1.0 |
| Requirement Status | Approved |
| Priority | Critical |
| Complexity | High |
| Release Version | 1.0 |
| Owner | Product Management |

### Traceability References

| Traceability Type | Reference |
|---|---|
| Business Requirement | BA-08 Facility Management |
| Business Rule | BA-02 BR-FAC-001, BR-FAC-002, BR-FAC-003, BR-FAC-004, BR-FAC-005, BR-FAC-006, BR-FAC-007, BR-ORG-010 |
| Business Process | BA-03 BP-FAC-008 Activate Facility |
| Business Process Flow | BA-04 Section 10 Facility Management Flow |
| Persona | BA-05 Organization Administrator, Facility Manager |
| User Journey | BA-06 Section 4 Organization Administrator Journey, Section 5 Facility Manager Journey |
| Stakeholder | BA-07 Organization Administrator, Facility Manager |
| Non-Functional Requirement | BA-09 Section 5 Availability & Business Continuity, Section 8 Business Configurability |
| Assumption / Constraint / Risk | BA-10 BA-ASS-002, BA-CON-003 |

### Purpose

To make a configured Facility operational only after required setup, manager assignment, and license entitlement validations are satisfied.

### Functional Requirement

The system shall allow an Organization Administrator to activate an eligible Facility and enable downstream operational services.

### Business Justification

Activation ensures Facilities do not accept customers, memberships, attendance, batches, activities, or billing operations until they are configured and entitled.

### Actors

- Organization Administrator
- Facility Manager
- License Service
- Notification Service
- Audit Service
- Reporting Service

### Preconditions

- Facility exists in Draft status.
- Parent Organization is Active.
- Facility Type is assigned.
- Mandatory Facility Settings are complete.
- Operating Hours are configured.
- Capacity Limits are configured.
- Facility Manager is assigned where required.
- Valid Facility license entitlement exists.

### Trigger

Organization Administrator selects Activate Facility from Facility lifecycle actions.

### In Scope

- Validate activation readiness.
- Validate license entitlement.
- Activate Facility.
- Enable downstream operational services.
- Notify stakeholders.
- Record audit and reporting events.

### Out of Scope

- Organization activation.
- Site activation.
- License purchase.
- Membership plan creation.
- Attendance or billing transaction processing.

### Inputs

- Facility ID
- Activation confirmation
- Activation notes
- Readiness validation results
- Effective activation timestamp

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Facility ID | Facility to activate | Identifier | Yes | Organization Administrator | Must exist and be Draft | Primary context |
| Activation Confirmation | Explicit confirmation | Boolean | Yes | Organization Administrator | Must be confirmed | Prevents accidental activation |
| Activation Notes | Activation comments | Text | No | Organization Administrator | Length validation | Audit field |
| Readiness Status | Setup validation result | Enum | Yes | System | Must be Ready | Derived from checks |
| License Status | Entitlement validation result | Enum | Yes | License Service | Must be Active or valid | Required before activation |

### Main Flow

1. Organization Administrator opens Facility lifecycle actions.
2. Organization Administrator selects Activate Facility.
3. The system validates Organization status, Facility status, Facility Type, settings, hours, capacity, manager assignment, policies, and license entitlement.
4. The system displays readiness checklist and unresolved blockers.
5. Organization Administrator confirms activation for a ready Facility.
6. The system changes Facility status from Draft to Active.
7. The system enables downstream operational services for the Facility.
8. The system refreshes Facility Dashboard and reporting context.
9. The system sends activation notifications.
10. The system records lifecycle audit events.

### Alternate Flows

- If optional readiness warnings exist, the system may allow activation where policy permits.
- If license entitlement is pending, the Facility remains Draft and the system displays License Required for Activation.
- If approval is required, the system routes activation before status change.

### Exception Flows

- If mandatory readiness checks fail, activation is blocked.
- If license entitlement is missing or inactive, activation is denied.
- If Facility is already Active, duplicate activation is blocked.
- If lifecycle update fails, Facility remains in prior state and error is logged.

### Outputs

- Facility status changed to Active.
- Operational services enabled.
- Readiness validation result.
- Notifications.
- Audit events.
- Updated reports and dashboards.

### UI Behaviour

Activation shall be available only to authorized Organization Administrators. The UI shall display a readiness checklist, license status, unresolved blockers, and explicit confirmation prompt before activation.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-FAC-701 | Facility must be Draft before activation. | Block activation. | Critical |
| VAL-FAC-702 | Parent Organization must be Active. | Block activation. | Critical |
| VAL-FAC-703 | Facility Type, Settings, Operating Hours, Capacity, and Manager coverage must satisfy readiness rules. | Block activation and show blockers. | Critical |
| VAL-FAC-704 | Valid Facility license entitlement is required. | Block activation and show license action. | Critical |
| VAL-FAC-705 | User must have activation permission. | Deny action and log event. | Critical |

### Business Rules

- BA-02 BR-FAC-001 - Facility Registration
- BA-02 BR-FAC-002 - Facility Subscription
- BA-02 BR-FAC-003 - Facility Type
- BA-02 BR-FAC-004 - Facility Capacity
- BA-02 BR-FAC-005 - Facility Operating Hours
- BA-02 BR-FAC-006 - Facility Status
- BA-02 BR-FAC-007 - Facility Staff Assignment
- BA-02 BR-ORG-010 - Organization Audit Trail

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| facility.lifecycle.view | Organization Administrator, Facility Manager | Read | Required to view lifecycle status |
| facility.lifecycle.activate | Organization Administrator | Execute | Required to activate Facility |
| facility.readiness.view | Organization Administrator | Read | Required to view readiness checklist |
| facility.license-status.view | Organization Administrator | Read | Required to view license status |

### Security Considerations

Facility activation shall enforce Organization scope, RBAC, license entitlement validation, and audit logging. Activation must not grant users permissions beyond existing roles and Facility assignments.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Facility Activated | Organization Administrator, Facility Manager | In-App, Email | Facility becomes Active | Include activation date and enabled services |
| License Required for Activation | Organization Administrator | In-App, Email | License validation fails | Include missing entitlement |
| Facility Activation Blocked | Organization Administrator | In-App | Readiness checks fail | Include blocker list |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| FacilityActivationRequested | Facility Management | License Service, Audit Service |
| FacilityActivated | Facility Management | Site Management, Membership Management, Attendance Management, Reporting Service |
| FacilityActivationBlocked | Facility Management | Notification Service, Audit Service |

### Audit Events

| Audit Event | Trigger | Actor | Entity | Data Captured |
|---|---|---|---|---|
| Facility Activation Readiness Checked | Readiness validation executed | Organization Administrator | Facility | Readiness result and blockers |
| Facility Activated | Status changed to Active | Organization Administrator | Facility | Previous status, new status, license reference |
| Facility Activation Blocked | Activation denied | System | Facility | Failed checks and timestamp |

### Reports Generated

- Facility Status Report
- Facility Summary Report
- Facility Dashboard
- Executive Dashboard

### Related Screens

- Facility Activation
- Facility Readiness Checklist
- Facility Profile
- Facility Dashboard
- License Status

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/facilities/{facilityId}/readiness | GET | Organization Administrator token | Retrieve activation readiness | 200 OK with readiness checklist |
| /api/v1/facilities/{facilityId}/license-status | GET | Organization Administrator token | Retrieve Facility license status | 200 OK with license status |
| /api/v1/facilities/{facilityId}/activate | POST | Organization Administrator token | Activate Facility | 200 OK with active Facility status |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Facility | Read, Update | Validate and update lifecycle status | Primary entity |
| Facility Type | Read | Validate type assignment | Prerequisite |
| Facility Settings | Read | Validate configuration readiness | Prerequisite |
| Facility Operating Hours | Read | Validate schedule readiness | Prerequisite |
| Facility Capacity | Read | Validate capacity readiness | Prerequisite |
| License | Read | Validate entitlement | Required |
| Audit Log | Insert | Record activation events | Required |
| Notification | Insert | Queue activation notices | Required |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Draft | Activate Facility | Active | Organization Administrator | Readiness and license checks pass |
| Draft | Activation blocked | Draft | System | Readiness or license checks fail |
| Active | Activate Facility | Active | Organization Administrator | Duplicate action blocked |
| Suspended | Activate Facility | Suspended | Organization Administrator | Reactivation handled separately if supported |
| Archived | Activate Facility | Archived | Organization Administrator | Action blocked |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| FAC-701 | Facility is not ready for activation. | Readiness blockers exist | Complete listed setup items |
| FAC-702 | Valid Facility license is required for activation. | Missing or inactive entitlement | Assign or renew license |
| FAC-703 | Facility must be in Draft status before activation. | Invalid lifecycle state | Review current status |
| FAC-704 | You do not have permission to activate this Facility. | Missing permission | Request access |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Activate ready Facility | Given readiness and license checks pass | When Organization Administrator confirms activation | Then Facility status shall become Active |
| Block missing license | Given license entitlement is missing | When activation is attempted | Then the system shall block activation |
| Enable operations | Given Facility activation succeeds | When status becomes Active | Then downstream operational modules shall be enabled |
| Audit activation | Given activation is attempted | When action completes or fails | Then audit history shall record the lifecycle event |

### Dependencies

- Active Organization
- Facility Settings
- Facility Type
- Operating Hours
- Capacity Limits
- Facility Manager assignment
- License Service
- Audit Service
- Notification Service

### Operational Considerations

Readiness check results shall be visible to implementation and support teams. Activation blockers shall link to the configuration area requiring correction where possible.

### Non-Functional Considerations

Activation shall be reliable, auditable, secure, performant, and consistent across all downstream modules.

### Assumptions

- Facility activation enables operational eligibility but does not automatically create Sites or memberships.
- License entitlement is required before operational use.
- Organization Administrator owns Facility lifecycle control.

### Success Criteria

Only fully configured and entitled Facilities become Active and eligible for service delivery.

### Related Functional Requirements

- FR-FAC-001 - Create Facility
- FR-FAC-003 - Configure Facility Settings
- FR-FAC-004 - Assign Facility Type
- FR-FAC-005 - Configure Operating Hours
- FR-FAC-006 - Configure Capacity Limits
- FR-FAC-007 - Assign Facility Manager
- FR-LIC-001 - Manage License Allocation

### Notes

Facility activation is the governance checkpoint between setup and operational service delivery.

---

## FR-FAC-009 - Suspend Facility

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-FAC-009 |
| Requirement Name | Suspend Facility |
| Functional Module | Facility Management |
| Business Domain | Facility |
| Business Capability | Facility Lifecycle |
| Requirement Type | Functional |
| Requirement Category | Workflow |
| Requirement Version | 1.0 |
| Requirement Status | Approved |
| Priority | Critical |
| Complexity | High |
| Release Version | 1.0 |
| Owner | Product Management |

### Traceability References

| Traceability Type | Reference |
|---|---|
| Business Requirement | BA-08 Facility Management |
| Business Rule | BA-02 BR-FAC-006, BR-FAC-010, BR-ORG-010, BR-SEC-002, BR-SEC-004 |
| Business Process | BA-03 BP-FAC-009 Suspend Facility |
| Business Process Flow | BA-04 Section 10 Facility Management Flow |
| Persona | BA-05 Organization Administrator, Facility Manager |
| User Journey | BA-06 Section 4 Organization Administrator Journey, Section 5 Facility Manager Journey |
| Stakeholder | BA-07 Organization Administrator, Facility Manager, Support Executive |
| Non-Functional Requirement | BA-09 Section 3 Security Requirements, Section 5 Business Continuity |
| Assumption / Constraint / Risk | BA-10 BA-RSK-004, BA-RSK-005 |

### Purpose

To temporarily restrict Facility operations while preserving historical data, reporting, and audit traceability.

### Functional Requirement

The system shall allow an Organization Administrator to suspend an Active Facility, restrict new operational transactions, notify stakeholders, and retain historical data.

### Business Justification

Suspension supports operational control during temporary closure, safety concerns, license issues, maintenance, commercial restrictions, or compliance exceptions without deleting Facility history.

### Actors

- Organization Administrator
- Facility Manager
- Site Administrator
- Notification Service
- Audit Service
- Reporting Service

### Preconditions

- Facility exists.
- Facility is Active.
- Parent Organization is Active or in a status that permits Facility suspension.
- User is authenticated.
- User has Facility suspension permission.

### Trigger

Organization Administrator selects Suspend Facility from Facility lifecycle actions.

### In Scope

- Validate suspension eligibility.
- Capture suspension reason.
- Change Facility status to Suspended.
- Restrict new operational transactions.
- Preserve historical data and reporting access.
- Notify stakeholders and record audit events.

### Out of Scope

- Archive Facility.
- Delete Facility.
- Refund processing.
- Subscription cancellation.
- Customer membership cancellation.
- Site-specific suspension unless driven by downstream rules.

### Inputs

- Facility ID
- Suspension reason
- Suspension category
- Effective date and time
- Customer-facing message, if applicable
- Internal notes

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Facility ID | Facility to suspend | Identifier | Yes | Organization Administrator | Must exist and be Active | Primary context |
| Suspension Reason | Explanation for suspension | Text | Yes | Organization Administrator | Required and length validation | Audit field |
| Suspension Category | Type of suspension | Enum | Yes | Organization Administrator | Must use configured category | Supports reporting |
| Effective DateTime | Suspension effective timestamp | DateTime | Yes | Organization Administrator / System | Current or future as policy allows | Immediate by default |
| Customer Message | Optional communication content | Text | No | Organization Administrator | Content length and policy validation | Used by Notification module |
| Internal Notes | Internal operational notes | Text | No | Organization Administrator | Length validation | Restricted visibility |

### Main Flow

1. Organization Administrator opens Facility lifecycle actions.
2. Organization Administrator selects Suspend Facility.
3. The system validates Facility status, permission, Organization scope, and suspension eligibility.
4. Organization Administrator enters suspension reason, category, effective time, and optional messages.
5. The system displays impact on Sites, memberships, attendance, batches, activities, and billing operations.
6. Organization Administrator confirms suspension.
7. The system changes Facility status to Suspended immediately or schedules suspension.
8. The system restricts new operational transactions according to policy.
9. The system sends notifications to affected stakeholders.
10. The system records audit events and updates dashboards.

### Alternate Flows

- If suspension is scheduled, the Facility remains Active until the effective timestamp.
- If partial operational access is allowed, read-only or maintenance actions remain available.
- If suspension is caused by license invalidation, the system may initiate suspension from License Service event.

### Exception Flows

- If Facility is not Active, the system blocks suspension.
- If required reason is missing, confirmation is blocked.
- If impact evaluation fails, the system prevents suspension until impact can be assessed.
- If status update fails, Facility remains Active and error is logged.

### Outputs

- Facility status changed to Suspended or suspension scheduled.
- Operational restrictions applied.
- Notifications.
- Audit events.
- Updated reports and dashboards.

### UI Behaviour

The Suspend action shall require reason capture and explicit confirmation. The UI shall display impact summary and restricted modules. Suspended Facilities shall show clear status indicators and restricted action messages.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-FAC-801 | Facility must be Active to suspend. | Block suspension. | Critical |
| VAL-FAC-802 | Suspension reason is mandatory. | Block confirmation. | Critical |
| VAL-FAC-803 | User must have suspension permission. | Deny action and log event. | Critical |
| VAL-FAC-804 | Suspension must preserve historical records. | Prevent destructive operations. | Critical |
| VAL-FAC-805 | Effective timestamp must satisfy lifecycle policy. | Block invalid schedule. | High |

### Business Rules

- BA-02 BR-FAC-006 - Facility Status
- BA-02 BR-FAC-010 - Facility Closure
- BA-02 BR-ORG-010 - Organization Audit Trail
- BA-02 BR-SEC-002 - Role-Based Access Control
- BA-02 BR-SEC-004 - Organization Data Isolation

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| facility.lifecycle.view | Organization Administrator, Facility Manager | Read | Required to view Facility status |
| facility.lifecycle.suspend | Organization Administrator | Execute | Required to suspend Facility |
| facility.suspension.impact.view | Organization Administrator | Read | Required to view impact |
| facility.suspended.view | Facility Manager | Read | Limited access after suspension |

### Security Considerations

Suspension shall restrict operational access while maintaining secure read-only historical access. All restriction enforcement shall remain tenant-scoped and role-aware.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Facility Suspended | Facility Manager, Site Administrator | In-App, Email | Facility status becomes Suspended | Include reason category and effective date |
| Facility Suspension Scheduled | Facility Manager | In-App, Email | Future suspension scheduled | Include effective timestamp |
| Facility Suspension Completed | Organization Administrator | In-App, Email | Suspension succeeds | Include Facility status |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| FacilitySuspensionRequested | Facility Management | Audit Service |
| FacilitySuspended | Facility Management | Site Management, Attendance Management, Activity Management, Reporting Service |
| FacilitySuspensionScheduled | Facility Management | Scheduler, Notification Service |

### Audit Events

| Audit Event | Trigger | Actor | Entity | Data Captured |
|---|---|---|---|---|
| Facility Suspension Requested | Suspension initiated | Organization Administrator | Facility | Reason, category, effective date |
| Facility Suspended | Status changed | Organization Administrator or System | Facility | Previous status, new status, timestamp |
| Facility Suspension Impact Viewed | Impact summary opened | Organization Administrator | Facility | Impact categories and actor |

### Reports Generated

- Facility Status Report
- Facility Summary Report
- Suspension Audit Report
- Facility Dashboard

### Related Screens

- Facility Lifecycle
- Suspension Confirmation
- Facility Dashboard
- Facility Profile
- Audit History

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/facilities/{facilityId}/suspension-impact | GET | Organization Administrator token | Retrieve suspension impact | 200 OK with impact summary |
| /api/v1/facilities/{facilityId}/suspend | POST | Organization Administrator token | Suspend Facility | 200 OK with suspended status |
| /api/v1/facilities/{facilityId} | GET | Authorized token | Retrieve Facility status | 200 OK with Facility resource |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Facility | Read, Update | Update lifecycle status | Primary entity |
| Facility Policy | Read | Determine restriction behavior | Governance |
| Audit Log | Insert | Record suspension actions | Required |
| Notification | Insert | Queue suspension notices | Required |
| Dashboard | Update | Reflect suspended status | Reporting context |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Active | Suspend Facility | Suspended | Organization Administrator | Valid reason and confirmation |
| Active | Schedule suspension | Active with Scheduled Suspension | Organization Administrator | Future effective timestamp |
| Active with Scheduled Suspension | Effective time reached | Suspended | System | Schedule due |
| Draft | Suspend Facility | Draft | Organization Administrator | Action blocked |
| Archived | Suspend Facility | Archived | Organization Administrator | Action blocked |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| FAC-801 | Only Active Facilities can be suspended. | Invalid lifecycle state | Review Facility status |
| FAC-802 | Suspension reason is required. | Missing reason | Enter suspension reason |
| FAC-803 | You do not have permission to suspend this Facility. | Missing permission | Request access |
| FAC-804 | Facility suspension could not be completed. | Status update failure | Retry or contact support |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Suspend Active Facility | Given Facility is Active and user has permission | When suspension is confirmed | Then Facility status shall become Suspended |
| Block invalid state | Given Facility is Draft or Archived | When suspension is attempted | Then the system shall block the action |
| Restrict operations | Given Facility is Suspended | When new operational transactions are attempted | Then the system shall restrict them according to policy |
| Audit suspension | Given suspension completes | When transaction finishes | Then lifecycle audit details shall be recorded |

### Dependencies

- Facility lifecycle model
- Site Management
- Membership Management
- Attendance Management
- Activity Management
- Notification Service
- Audit Service

### Operational Considerations

Suspension impact shall be clear to support teams, especially for customer-facing scheduling, attendance, and membership operations.

### Non-Functional Considerations

Suspension shall be reliable, auditable, secure, reversible through governed process, and consistently enforced across modules.

### Assumptions

- Suspension is temporary and preserves Facility history.
- Organization Administrator owns Facility suspension authority.
- Restricted operations are controlled by configured policies.

### Success Criteria

Facility operations are safely restricted while historical data, reporting, and auditability remain intact.

### Related Functional Requirements

- FR-FAC-008 - Activate Facility
- FR-FAC-010 - Archive Facility
- FR-FAC-011 - View Facility Dashboard
- FR-AUD-001 - Record Audit Events

### Notes

Suspension does not remove Facility data and shall not be treated as closure.

---

## FR-FAC-010 - Archive Facility

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-FAC-010 |
| Requirement Name | Archive Facility |
| Functional Module | Facility Management |
| Business Domain | Facility |
| Business Capability | Facility Lifecycle |
| Requirement Type | Functional |
| Requirement Category | Workflow |
| Requirement Version | 1.0 |
| Requirement Status | Approved |
| Priority | Critical |
| Complexity | Very High |
| Release Version | 1.0 |
| Owner | Product Management |

### Traceability References

| Traceability Type | Reference |
|---|---|
| Business Requirement | BA-08 Facility Management |
| Business Rule | BA-02 BR-FAC-006, BR-FAC-010, BR-ORG-003, BR-ORG-010, BR-AUD-001, BR-AUD-008 |
| Business Process | BA-03 BP-FAC-010 Archive Facility |
| Business Process Flow | BA-04 Section 10 Facility Management Flow |
| Persona | BA-05 Organization Administrator, Facility Manager |
| User Journey | BA-06 Section 4 Organization Administrator Journey |
| Stakeholder | BA-07 Organization Administrator, Facility Manager, External Auditor |
| Non-Functional Requirement | BA-09 Section 4.5 Data Retention, Section 10 Data Management |
| Assumption / Constraint / Risk | BA-10 BA-RSK-007, BA-CON-004 |

### Purpose

To retire a Facility from operational use while preserving all historical operational, financial, reporting, and audit records.

### Functional Requirement

The system shall allow an Organization Administrator to archive an eligible Facility after validating closure constraints, restricting operational actions, preserving historical data, and recording audit events.

### Business Justification

Archival supports controlled Facility closure without data loss, enabling compliance, reporting continuity, and historical traceability.

### Actors

- Organization Administrator
- Facility Manager
- Support Executive
- Reporting Service
- Notification Service
- Audit Service

### Preconditions

- Facility exists.
- Facility is not already Archived.
- User is authenticated.
- User has Facility archive permission.
- Archival eligibility checks are available.
- Retention rules are configured.

### Trigger

Organization Administrator selects Archive Facility from Facility lifecycle actions.

### In Scope

- Validate archive eligibility.
- Capture archive reason.
- Restrict operational actions.
- Preserve historical Facility records.
- Change Facility status to Archived.
- Notify stakeholders.
- Record audit events.

### Out of Scope

- Physical data deletion.
- Data purging.
- Organization archival.
- Site archival execution unless separately triggered.
- Financial settlement.
- Subscription or license cancellation.

### Inputs

- Facility ID
- Archive reason
- Archive category
- Effective date and time
- Archival confirmation
- Internal notes

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Facility ID | Facility to archive | Identifier | Yes | Organization Administrator | Must exist and not be Archived | Primary context |
| Archive Reason | Reason for archival | Text | Yes | Organization Administrator | Required and length validation | Audit field |
| Archive Category | Category of closure | Enum | Yes | Organization Administrator | Must use configured category | Reporting dimension |
| Effective DateTime | Archive effective timestamp | DateTime | Yes | Organization Administrator / System | Must satisfy policy | Immediate by default |
| Archival Confirmation | Explicit confirmation | Boolean | Yes | Organization Administrator | Must be confirmed | High-risk control |
| Internal Notes | Restricted notes | Text | No | Organization Administrator | Length validation | Internal visibility |

### Main Flow

1. Organization Administrator opens Facility lifecycle actions.
2. Organization Administrator selects Archive Facility.
3. The system validates Facility status, permission, active Site dependencies, active memberships, unresolved operational commitments, financial dependencies, and retention policy.
4. The system displays archival impact and unresolved blockers.
5. Organization Administrator enters archive reason and confirms archival.
6. The system changes Facility status to Archived.
7. The system blocks new operational create, update, and transaction actions.
8. The system preserves historical records for reporting and audit.
9. The system sends archival notifications.
10. The system records audit events and refreshes dashboards.

### Alternate Flows

- If archival is scheduled, the system archives the Facility at the configured effective timestamp.
- If unresolved blockers exist, the system blocks archival and lists required remediation.
- If read-only access is allowed, authorized users may view historical Facility data.

### Exception Flows

- If Facility is already Archived, duplicate archival is blocked.
- If active Sites or unresolved dependencies prevent archival, archival is blocked.
- If the user lacks permission, the system denies action.
- If archival execution fails, the system retains the prior state and logs the failure.

### Outputs

- Facility status changed to Archived or archival blocked.
- Operational actions restricted.
- Historical records preserved.
- Notifications.
- Audit events.
- Updated reports and dashboards.

### UI Behaviour

The Archive action shall display a high-risk confirmation dialog, impact summary, blocker list, retention notice, and read-only implications. Archived Facilities shall show clear status indicators and disabled operational actions.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-FAC-901 | Facility must not already be Archived. | Block duplicate archival. | Critical |
| VAL-FAC-902 | Active dependencies must be resolved before archival where policy requires. | Block archival and list blockers. | Critical |
| VAL-FAC-903 | Archive reason and confirmation are mandatory. | Block archival. | Critical |
| VAL-FAC-904 | Archival must preserve historical records. | Prevent destructive operations. | Critical |
| VAL-FAC-905 | User must have archive permission. | Deny action and log event. | Critical |

### Business Rules

- BA-02 BR-FAC-006 - Facility Status
- BA-02 BR-FAC-010 - Facility Closure
- BA-02 BR-ORG-003 - Facility Ownership
- BA-02 BR-ORG-010 - Organization Audit Trail
- BA-02 BR-AUD-001 - Audit Logging
- BA-02 BR-AUD-008 - Cross-Module Traceability

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| facility.lifecycle.view | Organization Administrator, Facility Manager | Read | Required to view lifecycle |
| facility.lifecycle.archive | Organization Administrator | Execute | Required to archive Facility |
| facility.archive.impact.view | Organization Administrator | Read | Required to view archive impact |
| facility.archived.view | Authorized user | Read | Read-only archived access |

### Security Considerations

Archival shall enforce tenant isolation, high-risk confirmation, role-based access, retention policy, and read-only controls. Archived Facility data must remain protected and auditable.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Facility Archived | Organization Administrator, Facility Manager | In-App, Email | Facility status becomes Archived | Include archive date and reason category |
| Facility Archive Blocked | Organization Administrator | In-App | Eligibility checks fail | Include blockers |
| Facility Archive Scheduled | Facility Manager | In-App, Email | Future archival scheduled | Include effective timestamp |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| FacilityArchiveRequested | Facility Management | Audit Service |
| FacilityArchived | Facility Management | Site Management, Reporting Service, Audit Service, Notification Service |
| FacilityArchiveBlocked | Facility Management | Notification Service, Audit Service |

### Audit Events

| Audit Event | Trigger | Actor | Entity | Data Captured |
|---|---|---|---|---|
| Facility Archive Eligibility Checked | Eligibility validation executed | Organization Administrator | Facility | Eligibility result and blockers |
| Facility Archived | Status changed to Archived | Organization Administrator or System | Facility | Previous status, new status, reason |
| Archived Facility Viewed | Archived record opened | Authorized user | Facility | Actor, timestamp, purpose context |

### Reports Generated

- Facility Status Report
- Archived Facility Register
- Facility Summary Report
- Audit Trail Report

### Related Screens

- Facility Lifecycle
- Archive Confirmation
- Facility Dashboard
- Archived Facility Detail
- Audit History

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/facilities/{facilityId}/archive-impact | GET | Organization Administrator token | Retrieve archive impact | 200 OK with impact summary |
| /api/v1/facilities/{facilityId}/archive | POST | Organization Administrator token | Archive Facility | 200 OK with archived status |
| /api/v1/facilities/{facilityId} | GET | Authorized token | Retrieve Facility details | 200 OK with Facility resource |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Facility | Read, Update | Update lifecycle status | Primary entity |
| Facility Settings | Read | Preserve configuration history | Read-only after archival |
| Facility Policy | Read | Preserve policy history | Read-only after archival |
| Facility Capacity | Read | Preserve operational limits | Read-only after archival |
| Facility Operating Hours | Read | Preserve schedule history | Read-only after archival |
| Audit Log | Insert | Record archival events | Required |
| Notification | Insert | Queue archival notices | Required |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Draft | Archive Facility | Archived | Organization Administrator | Eligibility checks pass |
| Active | Archive Facility | Archived | Organization Administrator | Eligibility checks pass |
| Suspended | Archive Facility | Archived | Organization Administrator | Eligibility checks pass |
| Active | Archive blocked | Active | System | Active dependencies prevent archival |
| Archived | Archive Facility | Archived | Organization Administrator | Duplicate action blocked |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| FAC-901 | Facility cannot be archived because blockers exist. | Eligibility checks failed | Resolve listed blockers |
| FAC-902 | Facility is already archived. | Duplicate action | No action required |
| FAC-903 | Archive reason is required. | Missing reason | Enter archive reason |
| FAC-904 | You do not have permission to archive this Facility. | Missing permission | Request access |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Archive eligible Facility | Given Facility passes archival checks | When Organization Administrator confirms archival | Then Facility status shall become Archived |
| Preserve history | Given archival succeeds | When authorized users view historical data | Then the system shall provide read-only access according to policy |
| Block unresolved blockers | Given active dependencies exist | When archival is attempted | Then the system shall block archival and list blockers |
| Audit archive | Given archival is attempted | When action completes or fails | Then audit history shall record the event |

### Dependencies

- Facility lifecycle model
- Site Management
- Membership Management
- Billing and Payment Management
- Data retention policy
- Audit Service
- Notification Service

### Operational Considerations

Archival should be handled as a high-risk action with clear blocker resolution, support visibility, and retention behavior.

### Non-Functional Considerations

Facility archival shall support compliance, auditability, data retention, security, tenant isolation, and reliable read-only access.

### Assumptions

- Archive is not physical deletion.
- Historical Facility data must remain available according to retention policy.
- Active dependencies may prevent archival.

### Success Criteria

Facilities can be retired from operational use without data loss, compliance gaps, or audit traceability loss.

### Related Functional Requirements

- FR-FAC-008 - Activate Facility
- FR-FAC-009 - Suspend Facility
- FR-FAC-011 - View Facility Dashboard
- FR-AUD-001 - Record Audit Events
- FR-RPT-001 - Generate Reports

### Notes

Archive is the controlled lifecycle endpoint for Facilities and should not be confused with data purging.

---

## FR-FAC-011 - View Facility Dashboard

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-FAC-011 |
| Requirement Name | View Facility Dashboard |
| Functional Module | Facility Management |
| Business Domain | Facility |
| Business Capability | Business Monitoring |
| Requirement Type | Functional |
| Requirement Category | Reporting |
| Requirement Version | 1.0 |
| Requirement Status | Approved |
| Priority | High |
| Complexity | High |
| Release Version | 1.0 |
| Owner | Product Management |

### Traceability References

| Traceability Type | Reference |
|---|---|
| Business Requirement | BA-08 Facility Management |
| Business Rule | BA-02 BR-FAC-009, BR-FAC-006, BR-ORG-006, BR-RPT-001, BR-RPT-002, BR-SEC-004 |
| Business Process | BA-03 BP-FAC-011 View Facility Dashboard |
| Business Process Flow | BA-04 Section 10 Facility Management Flow |
| Persona | BA-05 Facility Manager, Organization Administrator, Site Administrator |
| User Journey | BA-06 Section 5 Facility Manager Journey |
| Stakeholder | BA-07 Facility Manager, Organization Administrator, Site Administrator |
| Non-Functional Requirement | BA-09 Section 6.4 Reporting Performance, Section 11 Reporting Requirements |
| Assumption / Constraint / Risk | BA-10 BA-ASS-006, BA-RSK-004 |

### Purpose

To provide authorized users with a consolidated Facility-level view of utilization, attendance, activity, batch, capacity, alerts, and operational performance.

### Functional Requirement

The system shall provide a Facility Dashboard that displays authorized Facility metrics, alerts, capacity indicators, operational summaries, and navigation to related Facility functions.

### Business Justification

Facility Managers need timely operational visibility to manage service delivery, resolve capacity pressure, monitor resources, and escalate exceptions before customers are affected.

### Actors

- Facility Manager
- Organization Administrator
- Site Administrator
- Reporting Service
- Audit Service
- Notification Service

### Preconditions

- Facility exists.
- User is authenticated.
- User has Facility dashboard permission.
- User scope includes the Facility or authorized subset.
- Reporting data sources are available.

### Trigger

Authorized user opens Facility Dashboard or receives an operational alert.

### In Scope

- Display Facility lifecycle status.
- Display utilization, attendance, activity, batch, and capacity metrics.
- Display operational alerts and exceptions.
- Apply role-based and Facility-scoped data visibility.
- Support filters and refresh.
- Record dashboard access audit events.

### Out of Scope

- Detailed report builder.
- Organization-wide executive analytics.
- Site-specific dashboard implementation.
- Corrective transaction execution.
- Predictive analytics.

### Inputs

- Facility ID
- User role and permission scope
- Date range
- Site filter, if applicable
- Activity or batch filter, if applicable
- Refresh request

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Facility ID | Dashboard Facility context | Identifier | Yes | User selection or session | Must match authorized scope | Tenant and Facility boundary |
| Date Range | Reporting period | Date Range | Yes | User or defaults | Must be valid and within limits | Defaults from settings |
| Site Filter | Optional Site scope | Identifier | No | User | Must belong to Facility and user scope | Used for drill-down |
| Activity Filter | Optional activity scope | Identifier | No | User | Must belong to Facility scope | Used for operational analysis |
| Metric Type | Dashboard widget category | Enum | No | User / System | Must be supported metric | Controls widget display |
| Refresh Action | Request metric refresh | Action | No | User | Must respect refresh limits | May use cached data |

### Main Flow

1. Authorized user opens Facility Dashboard.
2. The system validates authentication, Facility scope, and dashboard permission.
3. The system loads Facility lifecycle status, manager assignment, settings summary, and operational configuration status.
4. The system retrieves dashboard metrics from reporting sources.
5. The system applies role-based visibility, Facility scope, filters, and date range.
6. The system displays widgets for utilization, attendance, capacity, activities, batches, alerts, and service performance.
7. User applies filters or refreshes metrics.
8. The system updates dashboard data and displays last refreshed timestamp.
9. The system records dashboard access and filter audit events.
10. The system displays permission-aware navigation links.

### Alternate Flows

- If no operational data exists, the dashboard shows onboarding or empty-state guidance.
- If user has Site-limited scope, only authorized Site data is displayed.
- If cached data is used, the dashboard displays last refreshed timestamp.

### Exception Flows

- If the user lacks permission, dashboard access is denied.
- If a metric source is unavailable, the widget shows unavailable state without breaking the dashboard.
- If filters produce no results, the dashboard displays an empty state.
- If Facility is Archived, dashboard opens in read-only historical mode where allowed.

### Outputs

- Facility Dashboard.
- Filtered operational metrics.
- Capacity alerts.
- Service delivery indicators.
- Navigation actions.
- Audit events.

### UI Behaviour

The dashboard shall present clear status badges, utilization indicators, alert panels, filter controls, refresh timestamps, and role-aware navigation. Critical alerts shall be visually prioritized without hiding normal operational metrics.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-FAC-1001 | User must have Facility dashboard permission. | Deny access and log event. | Critical |
| VAL-FAC-1002 | Dashboard data must be limited to authorized Facility scope. | Filter data and block unauthorized scope. | Critical |
| VAL-FAC-1003 | Date range must be valid and within reporting limits. | Show validation error. | High |
| VAL-FAC-1004 | Site filter must belong to the Facility. | Reject filter and log if unauthorized. | Critical |
| VAL-FAC-1005 | Widget failure must not break the entire dashboard. | Display widget-level unavailable state. | Medium |

### Business Rules

- BA-02 BR-FAC-009 - Facility Reporting
- BA-02 BR-FAC-006 - Facility Status
- BA-02 BR-ORG-006 - Role-Based Access
- BA-02 BR-RPT-001 - Report Access Control
- BA-02 BR-RPT-002 - Report Data Scope
- BA-02 BR-SEC-004 - Organization Data Isolation

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| facility.dashboard.view | Facility Manager | Read | Facility-scoped dashboard |
| facility.dashboard.organization-view | Organization Administrator | Read | Organization-level access to Facility dashboard |
| facility.dashboard.site-view | Site Administrator | Read | Site-scoped Facility summary |
| facility.dashboard.export | Organization Administrator, Facility Manager | Export | Export where enabled |

### Security Considerations

Dashboard data shall be limited by Organization, Facility, Site, and role scope. Sensitive commercial, capacity, and staff metrics shall be visible only to authorized users. Dashboard activity shall be audited.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Facility Alert Available | Facility Manager | In-App | Critical dashboard alert generated | Include alert category and target screen |
| Capacity Warning | Facility Manager, Site Administrator | In-App, Email | Capacity threshold reached | Include capacity category and usage |
| Facility Reporting Data Unavailable | Facility Manager | In-App | Metric source unavailable | Include affected widget |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| FacilityDashboardViewed | Facility Management | Audit Service |
| FacilityDashboardFiltered | Facility Management | Reporting Service |
| FacilityOperationalAlertDisplayed | Reporting Service | Notification Service, Audit Service |

### Audit Events

| Audit Event | Trigger | Actor | Entity | Data Captured |
|---|---|---|---|---|
| Facility Dashboard Viewed | Dashboard opened | Authorized user | Dashboard | Facility ID, actor, role, timestamp |
| Facility Dashboard Filter Applied | Filter changed | Authorized user | Dashboard | Filter values and date range |
| Facility Dashboard Restricted Access Attempted | Unauthorized scope requested | User | Dashboard | Requested scope and actor |

### Reports Generated

- Facility Dashboard
- Facility Summary Report
- Capacity Report
- Activity Performance Report
- Attendance Summary Report

### Related Screens

- Facility Dashboard
- Capacity Overview
- Batch Schedule
- Activity Performance
- Attendance Summary
- Reports & Analytics

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/facilities/{facilityId}/dashboard | GET | Authorized token | Retrieve Facility dashboard summary | 200 OK with dashboard metrics |
| /api/v1/facilities/{facilityId}/dashboard/widgets | GET | Authorized token | Retrieve available widgets | 200 OK with widget list |
| /api/v1/facilities/{facilityId}/dashboard/alerts | GET | Authorized token | Retrieve Facility alerts | 200 OK with alert list |
| /api/v1/facilities/{facilityId}/dashboard/refresh | POST | Authorized token | Request dashboard refresh | 202 Accepted with refresh status |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Facility | Read | Display profile and lifecycle context | Parent context |
| Facility Settings | Read | Apply dashboard preferences | Configuration source |
| Facility Capacity | Read | Display capacity metrics | Operational metric |
| Facility Operating Hours | Read | Display schedule context | Operational metric |
| Dashboard | Read | Retrieve widget definitions | Reporting context |
| Audit Log | Insert | Record dashboard access | Required |
| Notification | Read, Insert | Display and queue alerts | Conditional |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Dashboard Not Loaded | Open dashboard | Dashboard Loaded | Authorized user | Permission and scope valid |
| Dashboard Loaded | Apply filter | Dashboard Filtered | Authorized user | Valid filter criteria |
| Dashboard Loaded | Refresh requested | Refresh Pending | Authorized user | Refresh allowed |
| Refresh Pending | Refresh completed | Dashboard Loaded | System | Metrics available |
| Dashboard Loaded | Metric unavailable | Dashboard Partially Available | System | Widget-level failure |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| FAC-1001 | You do not have permission to view this Facility dashboard. | Missing permission or invalid scope | Request access |
| FAC-1002 | Selected date range is not valid. | Invalid filter | Select a valid date range |
| FAC-1003 | Selected Site is outside Facility scope. | Unauthorized filter | Choose an authorized Site |
| FAC-1004 | Some Facility dashboard data is temporarily unavailable. | Reporting source issue | Retry later |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| View dashboard | Given the user has Facility dashboard permission | When they open Facility Dashboard | Then the system shall display authorized Facility metrics |
| Enforce scope | Given the user has Site-limited scope | When dashboard loads | Then only authorized Site data shall be displayed |
| Show alerts | Given capacity or operational alerts exist | When dashboard loads | Then the system shall display alert indicators |
| Handle partial outage | Given one metric source is unavailable | When dashboard loads | Then available widgets shall still render |

### Dependencies

- Reporting Service
- Facility Settings
- Site Management data
- Attendance Management data
- Activity and Batch Management data
- Capacity configuration
- Audit Service

### Operational Considerations

Dashboard widgets shall expose refresh timestamps and source availability. Widget failures shall be logged independently.

### Non-Functional Considerations

Facility Dashboard shall support reporting performance, role-based visibility, scalability, availability, usability, accessibility, and secure data scoping.

### Assumptions

- Dashboard metrics are derived from operational and reporting data sources.
- Some metrics may be cached for performance.
- Facility Manager has access only to assigned Facility scope.

### Success Criteria

Facility Managers can monitor utilization, capacity, activities, attendance, and exceptions from one consolidated dashboard.

### Related Functional Requirements

- FR-FAC-003 - Configure Facility Settings
- FR-FAC-006 - Configure Capacity Limits
- FR-FAC-007 - Assign Facility Manager
- FR-RPT-001 - Generate Reports
- FR-AUD-001 - Record Audit Events

### Notes

The Facility Dashboard is monitoring-focused and does not replace detailed reports or transactional screens.

---

## FR-FAC-012 - Manage Facility Policies

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-FAC-012 |
| Requirement Name | Manage Facility Policies |
| Functional Module | Facility Management |
| Business Domain | Facility |
| Business Capability | Facility Configuration |
| Requirement Type | Functional |
| Requirement Category | Configuration |
| Requirement Version | 1.0 |
| Requirement Status | Approved |
| Priority | High |
| Complexity | High |
| Release Version | 1.0 |
| Owner | Product Management |

### Traceability References

| Traceability Type | Reference |
|---|---|
| Business Requirement | BA-08 BR-004 Facility Configuration |
| Business Rule | BA-02 BR-FAC-004, BR-FAC-005, BR-FAC-006, BR-FAC-008, BR-ORG-004, BR-ORG-010 |
| Business Process | BA-03 BP-FAC-012 Manage Facility Policies |
| Business Process Flow | BA-04 Section 10 Facility Management Flow |
| Persona | BA-05 Organization Administrator, Facility Manager |
| User Journey | BA-06 Section 4 Organization Administrator Journey, Section 5 Facility Manager Journey |
| Stakeholder | BA-07 Organization Administrator, Facility Manager, Site Administrator |
| Non-Functional Requirement | BA-09 Section 8.3 Business Rules Configuration |
| Assumption / Constraint / Risk | BA-10 BA-ASS-006, BA-RSK-004 |

### Purpose

To configure Facility-level business policies that govern operational behavior while remaining within Organization policy and platform constraints.

### Functional Requirement

The system shall allow authorized users to create, update, schedule, publish, inherit, and audit Facility Policies for attendance, refunds, cancellation, safety, guest access, holidays, and operational rules.

### Business Justification

Facility Policies define how each business unit operates and provide controlled flexibility for different service models while preserving Organization-level governance.

### Actors

- Organization Administrator
- Facility Manager
- Site Administrator
- Approval Workflow Service
- Notification Service
- Audit Service

### Preconditions

- Facility exists.
- Facility is not Archived.
- Facility Type is assigned.
- User is authenticated.
- User has Facility policy permission.
- Organization policy permits Facility-level policy configuration.

### Trigger

Authorized user opens Facility Policies and submits a policy create, update, schedule, or publish action.

### In Scope

- Configure Facility-level policies.
- Inherit Organization policies.
- Validate policy values and precedence.
- Manage effective dates and expiry dates.
- Route governed policy changes for approval.
- Publish policies to downstream Sites and operational modules.
- Record audit and notification events.

### Out of Scope

- Platform policy definition.
- Organization-level policy configuration.
- Site-specific policy overrides.
- Execution of transactions governed by policies.
- Legal policy authoring outside system configuration.

### Inputs

- Facility ID
- Policy category
- Policy name
- Policy value
- Inheritance mode
- Effective date
- Expiry date
- Change reason
- Approval reference, if applicable

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Policy Category | Operational domain governed by policy | Master Data | Yes | System | Must be active and supported by Facility Type | Examples include attendance and cancellation |
| Policy Name | Specific policy identifier | Master Data | Yes | System | Must be allowed at Facility level | Defined by platform/Organization |
| Policy Value | Configured policy value | Configuration | Yes | Authorized user | Must match data type and allowed range | Primary configuration |
| Inheritance Mode | Inherit or override Organization policy | Enum | Yes | Authorized user | Must be allowed by Organization policy | Controls precedence |
| Effective Date | Date policy becomes active | Date | Yes | Authorized user | Must satisfy date rules | Supports scheduling |
| Expiry Date | Policy expiry date | Date | No | Authorized user | Must be after effective date | Optional |
| Change Reason | Reason for policy change | Text | Conditional | Authorized user | Required for governed policies | Audit field |

### Main Flow

1. Authorized user opens Facility Policies.
2. The system loads Organization policies, current Facility policies, Facility Type capabilities, and policy constraints.
3. User selects a policy category and policy action.
4. User enters policy values, inheritance mode, effective dates, and change reason where required.
5. The system validates policy data type, scope, precedence, Facility Type support, Organization constraints, date conflicts, and approval requirements.
6. If approval is required, the system creates an approval request.
7. If approval is not required, or after approval is granted, the system saves or publishes the policy.
8. The system propagates policy context to Sites and operational modules where applicable.
9. The system updates Facility configuration reports and dashboard status.
10. The system records audit events and sends notifications.

### Alternate Flows

- If the policy inherits from Organization, the system stores inheritance state without local value.
- If the policy is future-dated, the system schedules publication.
- If Sites have approved overrides, the system preserves those overrides.
- If a policy expires, the system reverts to the applicable inherited or default policy.

### Exception Flows

- If policy violates Organization constraints, the system blocks save.
- If policy is unsupported by Facility Type, the system blocks configuration.
- If policy conflicts with another effective policy, the system blocks publication.
- If approval is rejected, existing policy remains active.
- If publication fails, the system logs failure and displays recovery status.

### Outputs

- Created or updated Facility Policy.
- Policy inheritance status.
- Policy publication status.
- Approval request, if applicable.
- Notifications and audit events.
- Updated configuration reports.

### UI Behaviour

Facility Policies shall display inherited Organization policy, local override status, effective dates, approval status, downstream impact, and publication state. The UI shall clearly distinguish active, draft, scheduled, expired, and rejected policies.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-FAC-1101 | Facility Policy must remain within Organization policy constraints. | Block save and show constraint. | Critical |
| VAL-FAC-1102 | Policy must be supported by Facility Type. | Disable or block unsupported policy. | High |
| VAL-FAC-1103 | Effective periods must not conflict for the same policy. | Block publication. | High |
| VAL-FAC-1104 | Governed policy changes require approval. | Submit approval or block if route unavailable. | High |
| VAL-FAC-1105 | Policy propagation must preserve approved Site overrides. | Skip overrides and log result. | High |

### Business Rules

- BA-02 BR-FAC-004 - Facility Capacity
- BA-02 BR-FAC-005 - Facility Operating Hours
- BA-02 BR-FAC-006 - Facility Status
- BA-02 BR-FAC-008 - Facility Services
- BA-02 BR-ORG-004 - Organization Policies
- BA-02 BR-ORG-010 - Organization Audit Trail

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| facility.policies.view | Organization Administrator, Facility Manager | Read | Required to view Facility Policies |
| facility.policies.update | Organization Administrator | Update | Required for policy configuration |
| facility.policies.maintain | Facility Manager | Update | Limited policy maintenance where allowed |
| facility.policies.approve | Authorized Approver | Approve | Required for governed policies |
| facility.policies.publish | Authorized user / System | Execute | Required to publish policies |

### Security Considerations

Facility Policy changes shall be tenant-scoped, permission-controlled, and auditable. Policies affecting financial, safety, access, or compliance behavior shall require appropriate governance and approval.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Facility Policy Updated | Organization Administrator, Facility Manager | In-App, Email | Policy saved or published | Include policy category and effective date |
| Facility Policy Approval Required | Approver | In-App, Email | Governed policy submitted | Include change reason and impact |
| Facility Policy Published | Site Administrator | In-App | Policy becomes effective | Include affected downstream scope |
| Facility Policy Expired | Facility Manager | In-App | Policy expiry reached | Include fallback policy source |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| FacilityPolicyUpdated | Facility Management | Audit Service, Reporting Service |
| FacilityPolicyApprovalRequested | Facility Management | Approval Workflow Service |
| FacilityPolicyPublished | Facility Management | Site Management, Membership Management, Attendance Management, Billing Management |
| FacilityPolicyExpired | Scheduler | Facility Management, Notification Service |

### Audit Events

| Audit Event | Trigger | Actor | Entity | Data Captured |
|---|---|---|---|---|
| Facility Policy Viewed | Policy screen opened | Authorized user | Facility Policy | Facility ID, actor, timestamp |
| Facility Policy Modified | Policy saved | Authorized user | Facility Policy | Previous value, new value, effective date, reason |
| Facility Policy Published | Policy becomes effective | Authorized user / System | Facility Policy | Policy version, scope, publication result |
| Facility Policy Approval Completed | Approval decision recorded | Approver | Approval Request | Decision, comments, timestamp |

### Reports Generated

- Facility Configuration Report
- Facility Policy Report
- Configuration Change Report
- Audit Trail Report

### Related Screens

- Facility Policies
- Facility Settings
- Policy Impact Summary
- Approval Request
- Audit History

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/facilities/{facilityId}/policies | GET | Authorized token | Retrieve Facility Policies | 200 OK with policy list |
| /api/v1/facilities/{facilityId}/policies | POST | Authorized token | Create Facility Policy | 201 Created with policy resource |
| /api/v1/facilities/{facilityId}/policies/{policyId} | PATCH | Authorized token | Update Facility Policy | 200 OK with updated policy |
| /api/v1/facilities/{facilityId}/policies/{policyId}/publish | POST | Authorized token | Publish Facility Policy | 202 Accepted with publication status |
| /api/v1/facilities/{facilityId}/policies/{policyId}/impact | POST | Authorized token | Evaluate policy impact | 200 OK with impact summary |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Facility | Read | Validate scope and lifecycle | Parent context |
| Facility Policy | Create, Read, Update | Store Facility policies | Primary entity |
| Facility Type | Read | Validate supported policy categories | Capability source |
| Organization Settings | Read | Validate inherited configuration | Parent configuration |
| Business Policies | Read | Validate Organization policy boundary | Governance |
| Approval Request | Insert, Update | Manage governed policy changes | Conditional |
| Audit Log | Insert | Record policy changes | Required |
| Notification | Insert | Queue policy notifications | Conditional |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Inherited | Create local policy | Draft | Authorized user | Local override allowed |
| Draft | Submit policy | Pending Approval | Authorized user | Approval required |
| Draft | Publish policy | Active | Authorized user | No approval required and effective now |
| Pending Approval | Approve policy | Scheduled or Active | Authorized Approver | Approval granted |
| Pending Approval | Reject policy | Rejected | Authorized Approver | Existing policy retained |
| Active | Expiry reached | Expired | System | Expiry date configured |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| FAC-1101 | Facility Policy violates Organization policy. | Parent policy constraint | Select an allowed value |
| FAC-1102 | This policy is not supported for the Facility Type. | Unsupported policy | Select a supported policy |
| FAC-1103 | Policy effective date conflicts with another active policy. | Date overlap | Adjust dates |
| FAC-1104 | Facility Policy requires approval before activation. | Governed change | Submit for approval |
| FAC-1105 | Facility Policy could not be published. | Publication failure | Review status or contact support |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Configure valid policy | Given the user has Facility policy permission | When valid policy values are submitted | Then the system shall save or publish the policy |
| Enforce Organization boundary | Given policy violates Organization constraint | When save is attempted | Then the system shall block the policy |
| Route approval | Given policy requires governance approval | When submitted | Then the system shall create an approval request |
| Publish policy | Given policy is approved and effective | When publication occurs | Then downstream modules shall receive the policy context |

### Dependencies

- Organization policy configuration
- Facility Type configuration
- Site Management
- Approval Workflow Service
- Notification Service
- Audit Service

### Operational Considerations

Policy publication status shall be visible to administrators and support teams. Failed publication shall not silently change operational behavior.

### Non-Functional Considerations

Facility Policy management shall support configurability, maintainability, auditability, reliable publication, and scalable inheritance across many Sites.

### Assumptions

- Organization policy determines whether Facility-level overrides are allowed.
- Facility Type determines applicable policy categories.
- Downstream modules consume published Facility Policy context.

### Success Criteria

Facility Policies are configured within governance boundaries, published reliably, inherited correctly, and auditable across operational modules.

### Related Functional Requirements

- FR-ORG-004 - Configure Business Policies
- FR-FAC-003 - Configure Facility Settings
- FR-FAC-005 - Configure Operating Hours
- FR-FAC-006 - Configure Capacity Limits
- FR-SIT-011 - Manage Site Policies

### Notes

Facility Policies provide operational governance and do not execute the downstream transactions they control.

---

**End of FR-04 - Facility Management**
