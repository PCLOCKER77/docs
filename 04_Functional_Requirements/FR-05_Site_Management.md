# FR-05 Site Management

**Document ID:** FR-05  
**Document Name:** Site Management Functional Requirements  
**Company:** OreeOn Technologies Pvt. Ltd.  
**Product:** Digitize  
**Document Type:** Functional Requirements  
**Version:** 1.0  
**Status:** Draft  
**Owner:** Product Management  
**Prepared By:** Product Management, Business Analysis, and Solution Architecture  
**Last Updated:** July 2026

---

## FR-SIT-001 - Create Site

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-SIT-001 |
| Requirement Name | Create Site |
| Functional Module | Site Management |
| Business Domain | Site |
| Business Capability | Site Management |
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
| Business Requirement | BA-08 BR-005 Site Creation |
| Business Rule | BA-02 BR-SIT-001, BR-SIT-002, BR-SIT-003, BR-SIT-004, BR-SIT-005, BR-FAC-001, BR-FAC-006 |
| Business Process | BA-03 BP-SIT-001 Create Site |
| Business Process Flow | BA-04 Section 11 Site Management Flow |
| Persona | BA-05 Organization Administrator, Facility Manager, Site Administrator |
| User Journey | BA-06 Section 4 Organization Administrator Journey, Section 5 Facility Manager Journey, Section 6 Site Administrator Journey |
| Stakeholder | BA-07 Organization Administrator, Facility Manager, Site Administrator |
| Non-Functional Requirement | BA-09 Section 2.8 Configurability, Section 3.2 Authorization |
| Assumption / Constraint / Risk | BA-10 BA-ASS-001, BA-CON-003 |

### Purpose

To allow authorized users to create a Site as a physical branch under an existing Facility.

### Functional Requirement

The system shall allow an Organization Administrator to create a Site under exactly one Facility with required branch identity, address, contact, inherited configuration, and initial lifecycle status.

### Business Justification

Sites represent the physical execution points for daily operations, customer service delivery, attendance, local reporting, and branch-level compliance while remaining governed by the parent Facility and Organization.

### Actors

- Organization Administrator
- Facility Manager
- Site Administrator
- Notification Service
- Audit Service
- System

### Preconditions

- Organization exists and is Active.
- Parent Facility exists and is Active or in a valid preparatory state.
- Parent Facility has valid operational entitlement.
- User is authenticated.
- User has Site creation permission.
- Site-level creation is allowed by Facility and Organization policy.

### Trigger

The Organization Administrator selects Create Site from Site Management or from the parent Facility context.

### In Scope

- Capture Site master data.
- Associate Site with exactly one Facility.
- Validate Site add-on licensing where applicable.
- Initialize inherited Site configuration.
- Set initial Site status.
- Record audit and notification events.

### Out of Scope

- Facility creation.
- Facility license purchase.
- Staff account creation.
- Customer registration.
- Attendance recording.
- Site activation beyond setup readiness.

### Inputs

- Facility reference
- Site name
- Site code
- Site address
- Site contact details
- Initial Site Manager or Site Administrator reference, if available
- Inherited configuration preference
- Site add-on license reference, if applicable

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Facility ID | Parent Facility reference | Identifier | Yes | Organization Administrator / System | Must exist and be eligible for Site creation | Site cannot exist independently |
| Site Name | Branch name | Text | Yes | Organization Administrator | Required and length validation | Used in screens and reports |
| Site Code | Branch operational code | Text | Yes | Organization Administrator / System | Unique within parent Facility | Used for lookup and reporting |
| Site Address | Physical branch address | Address | Yes | Organization Administrator | Complete address required | Supports local operations and compliance |
| Contact Details | Site contact email and phone | Structured Data | Yes | Organization Administrator | Valid email and phone formats | Used for local communication |
| Initial Status | Site lifecycle status | Enum | Yes | System | Must be Draft at creation | Activation handled separately |
| Site Add-on License Reference | License reference for additional Site entitlement | Identifier | Conditional | License Service | Required when entitlement threshold is exceeded | Site does not own subscription |

### Main Flow

1. Organization Administrator opens Create Site under the selected Facility.
2. The system loads parent Facility profile, configuration, existing Sites, and entitlement context.
3. Organization Administrator enters Site name, code, address, contact details, and optional manager reference.
4. The system validates Facility ownership, Facility status, duplicate Site identity, address completeness, and add-on licensing requirements.
5. The system creates the Site in Draft status.
6. The system initializes Site Settings, Operating Hours, Capacity, Policies, Documents, and Dashboard context using inherited Facility configuration.
7. The system records Site creation audit events.
8. The system sends Site Created and setup notifications where configured.
9. The system displays the Site Profile or Site setup summary.

### Alternate Flows

- If the Site is covered by existing entitlement, the system creates the Site without requiring a Site add-on license.
- If additional entitlement is required, the Site may be created in Draft but blocked from activation until licensing is resolved.
- If a Site Administrator is known during creation, the assignment may be captured for readiness tracking.

### Exception Flows

- If the parent Facility is not eligible, the system blocks creation.
- If duplicate Site Code exists within the Facility, the system rejects creation.
- If required address details are incomplete, the system blocks save.
- If Site add-on licensing is required and not available, the system records the entitlement blocker.
- If initialization fails, the system prevents incomplete operational Site creation.

### Outputs

- Site record created.
- Site status set to Draft.
- Inherited configuration initialized.
- Entitlement blocker recorded, if applicable.
- Notifications generated.
- Audit events recorded.

### UI Behaviour

The Create Site screen shall display parent Facility context, branch identity fields, address fields, contact details, entitlement status, and inherited configuration summary. Save shall be disabled until mandatory fields are valid.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-SIT-001 | Site must belong to exactly one eligible Facility. | Block creation. | Critical |
| VAL-SIT-002 | Site Code must be unique within the Facility. | Block save and show duplicate conflict. | Critical |
| VAL-SIT-003 | Complete Site address is mandatory. | Block save and highlight missing fields. | High |
| VAL-SIT-004 | Site add-on licensing must be validated where entitlement threshold is exceeded. | Mark activation blocker or block based on policy. | Critical |
| VAL-SIT-005 | Initial Site status must be Draft. | Reject invalid lifecycle state. | Critical |

### Business Rules

- BA-02 BR-SIT-001 - Site Ownership
- BA-02 BR-SIT-002 - Facility-to-Site Relationship
- BA-02 BR-SIT-003 - Site Add-on Licensing
- BA-02 BR-SIT-004 - Site Operational Status
- BA-02 BR-SIT-005 - Site Address
- BA-02 BR-FAC-001 - Facility Registration
- BA-02 BR-FAC-006 - Facility Status

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| site.create | Organization Administrator | Create | Required to create Sites |
| site.view | Organization Administrator, Facility Manager | Read | Required to view created Site |
| site.entitlement.view | Organization Administrator | Read | Required to view Site licensing readiness |
| audit.site.create.read | Organization Administrator | Read | Required to view Site creation audit |

### Security Considerations

Site creation shall enforce Organization and Facility scope, RBAC, tenant isolation, and audit logging. Site data shall not be visible outside the owning Organization and Facility hierarchy.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Site Created | Organization Administrator, Facility Manager | In-App, Email | Site record created | Include Site name, Facility, and status |
| Site Setup Required | Organization Administrator | In-App | Site created in Draft status | Include missing readiness areas |
| Site Add-on License Required | Organization Administrator | In-App, Email | Entitlement threshold exceeded | Include license requirement and action |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| SiteCreated | Site Management | Audit Service, Notification Service, Reporting Service |
| SiteDefaultsInitialized | Site Management | Configuration Service, Reporting Service |
| SiteEntitlementValidationCompleted | Site Management | License Service, Audit Service |

### Audit Events

| Audit Event | Trigger | Actor | Entity | Data Captured |
|---|---|---|---|---|
| Site Created | Site creation completed | Organization Administrator | Site | Site ID, Facility ID, status, address summary |
| Site Defaults Initialized | Default Site configuration created | System | Site Settings | Inherited source and initialized entities |
| Site Entitlement Checked | Add-on entitlement validated | System | Site | Entitlement result and license reference |

### Reports Generated

- Site Summary Report
- Site Status Report
- Site Configuration Report
- Executive Dashboard

### Related Screens

- Site Management
- Create Site
- Site Profile
- Facility Profile
- Site Dashboard

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/facilities/{facilityId}/sites | POST | Organization Administrator token | Create Site under Facility | 201 Created with Site resource |
| /api/v1/sites/{siteId} | GET | Authorized token | Retrieve Site profile | 200 OK with Site resource |
| /api/v1/sites/{siteId}/settings | POST | Organization Administrator token | Initialize Site Settings | 201 Created with settings resource |
| /api/v1/sites/{siteId}/entitlement-status | GET | Organization Administrator token | Retrieve Site entitlement status | 200 OK with entitlement result |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Facility | Read | Validate parent Facility | Parent entity |
| Site | Create | Store Site profile | Primary entity |
| Site Settings | Create | Initialize inherited configuration | Uses Facility defaults |
| Site Capacity | Create | Initialize capacity baseline | Constrained by Facility |
| Site Policy | Create | Initialize policy baseline | Inherits Facility policy |
| Site Operating Hours | Create | Initialize schedule | Inherits Facility hours |
| Site Documents | Initialize | Prepare document repository | Documents added later |
| Audit Log | Insert | Record Site creation | Required |
| Notification | Insert | Queue Site notifications | Conditional |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| None | Create Site | Draft | Organization Administrator | Required Site details valid |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| SIT-001 | Site name is required. | Mandatory field missing | Enter Site name |
| SIT-002 | Site code already exists for this Facility. | Duplicate Site Code | Enter a unique Site Code |
| SIT-003 | Complete Site address is required. | Address incomplete | Complete address fields |
| SIT-004 | Site cannot be created under the selected Facility state. | Parent Facility ineligible | Select eligible Facility |
| SIT-005 | Site add-on license is required before activation. | Entitlement threshold exceeded | Assign required license |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Create valid Site | Given an eligible Facility and user with Site creation permission | When valid Site details are submitted | Then the system shall create the Site in Draft status |
| Prevent duplicate Site | Given a Site Code already exists under the Facility | When the same code is submitted | Then the system shall block creation |
| Require address | Given address details are incomplete | When the user saves | Then the system shall block save and show missing address fields |
| Track entitlement blocker | Given add-on licensing is required | When Site is created | Then the system shall record activation blocker until entitlement is valid |

### Dependencies

- Active Organization
- Eligible Facility
- Facility configuration
- License Service
- Notification Service
- Audit Service

### Operational Considerations

Site creation failures shall be traceable through logs. Entitlement blockers shall be visible to implementation and support teams.

### Non-Functional Considerations

Site creation shall support tenant isolation, branch scalability, secure authorization, reliable initialization, and auditability.

### Assumptions

- Site is a physical branch under a Facility.
- Site does not own subscription or license independently.
- Initial Site configuration inherits from Facility defaults unless overridden later.

### Success Criteria

A Site is created under the correct Facility with valid branch identity, address, inherited configuration, entitlement visibility, and audit traceability.

### Related Functional Requirements

- FR-FAC-008 - Activate Facility
- FR-FAC-011 - View Facility Dashboard
- FR-SIT-003 - Configure Site Settings
- FR-SIT-007 - Activate Site
- FR-LIC-001 - Manage License Allocation

### Notes

Site creation enables branch setup but does not make the Site operational until activation readiness is complete.

---

## FR-SIT-002 - Update Site Details

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-SIT-002 |
| Requirement Name | Update Site Details |
| Functional Module | Site Management |
| Business Domain | Site |
| Business Capability | Site Management |
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
| Business Requirement | BA-08 Site Management |
| Business Rule | BA-02 BR-SIT-001, BR-SIT-004, BR-SIT-005, BR-SIT-008, BR-SIT-010, BR-SEC-004 |
| Business Process | BA-03 BP-SIT-002 Update Site Details |
| Business Process Flow | BA-04 Section 11 Site Management Flow |
| Persona | BA-05 Organization Administrator, Facility Manager, Site Administrator |
| User Journey | BA-06 Section 6 Site Administrator Journey |
| Stakeholder | BA-07 Organization Administrator, Facility Manager, Site Administrator |
| Non-Functional Requirement | BA-09 Section 2.5 Maintainability, Section 10 Data Management |
| Assumption / Constraint / Risk | BA-10 BA-ASS-006 |

### Purpose

To maintain accurate Site branch information throughout its operational lifecycle.

### Functional Requirement

The system shall allow authorized users to view and update permitted Site detail fields while enforcing Facility scope, lifecycle status, validation, approval, and audit controls.

### Business Justification

Accurate Site details are required for local operations, customer communication, staff coordination, branch reporting, compliance documentation, and emergency handling.

### Actors

- Organization Administrator
- Facility Manager
- Site Administrator
- Approval Workflow Service
- Notification Service
- Audit Service

### Preconditions

- Site exists.
- Site belongs to the user's authorized Facility scope.
- Site is not Archived.
- User is authenticated.
- User has Site detail update permission.

### Trigger

An authorized user opens Site Profile and submits Site detail changes.

### In Scope

- View Site details.
- Update permitted Site profile fields.
- Validate address, contact, duplicate identity, and scope.
- Route governed changes for approval where configured.
- Record notifications and audit events.

### Out of Scope

- Site Settings configuration.
- Site capacity configuration.
- Site lifecycle activation, suspension, or archival.
- Staff account creation.
- Customer operational transactions.

### Inputs

- Site ID
- Site name
- Site code
- Site address
- Contact details
- Change reason
- Approval reference, if required

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Site ID | Unique Site reference | Identifier | Yes | System | Must exist and match scope | Read-only |
| Site Name | Branch name | Text | Yes | Authorized user | Required and length validation | Editable |
| Site Code | Branch code | Text | Yes | Organization Administrator | Unique within Facility | May be governed after activation |
| Site Address | Physical address | Address | Yes | Authorized user | Complete address required | Critical for branch operations |
| Contact Email | Local contact email | Email | Yes | Authorized user | Valid email format | Communication |
| Contact Phone | Local contact phone | Phone | Yes | Authorized user | Valid phone format | Communication |
| Change Reason | Reason for update | Text | Conditional | Authorized user | Required for governed fields | Audit field |

### Main Flow

1. Authorized user opens Site Profile.
2. The system validates authentication, Facility scope, and permission.
3. The system loads current Site details and lifecycle status.
4. The system displays editable, read-only, and governed fields.
5. User updates permitted fields.
6. The system validates mandatory fields, address completeness, duplicate Site Code, format rules, and approval requirements.
7. If approval is not required, the system saves changes.
8. If approval is required, the system creates an approval request.
9. The system updates Site reports and related summaries.
10. The system records audit events and sends notifications.

### Alternate Flows

- If only local contact details are changed, the system may save immediately.
- If address changes affect compliance, the system may require approval.
- If Site is Suspended, limited detail maintenance may be permitted by policy.

### Exception Flows

- If Site is Archived, the system blocks updates.
- If user lacks scope, the system denies access and logs the event.
- If duplicate Site Code is entered, the system blocks save.
- If approval submission fails, governed changes are not applied.

### Outputs

- Updated Site profile.
- Pending approval request, if applicable.
- Updated dashboards and reports.
- Notification records.
- Audit log entries.

### UI Behaviour

Site Profile shall display lifecycle status, Facility context, editable fields, read-only fields, address validation, and approval status. Save shall be disabled until mandatory fields are valid.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-SIT-101 | Site must not be Archived for profile updates. | Block update. | Critical |
| VAL-SIT-102 | Site Code must be unique within parent Facility. | Block save. | Critical |
| VAL-SIT-103 | Site address must remain complete. | Block save and highlight missing fields. | High |
| VAL-SIT-104 | Governed fields require approval where configured. | Submit approval or block if route unavailable. | High |
| VAL-SIT-105 | User must have authorized Site scope. | Deny access and log event. | Critical |

### Business Rules

- BA-02 BR-SIT-001 - Site Ownership
- BA-02 BR-SIT-004 - Site Operational Status
- BA-02 BR-SIT-005 - Site Address
- BA-02 BR-SIT-008 - Site Reporting
- BA-02 BR-SIT-010 - Historical Records
- BA-02 BR-SEC-004 - Organization Data Isolation

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| site.profile.view | Organization Administrator, Facility Manager, Site Administrator | Read | Required to view Site Profile |
| site.profile.update | Organization Administrator | Update | Full profile update |
| site.profile.maintain | Facility Manager, Site Administrator | Update | Limited maintenance where allowed |
| site.profile.approve | Authorized Approver | Approve | Required for governed changes |

### Security Considerations

Site profile access shall enforce Organization, Facility, and Site scope. Sensitive local contact or compliance details shall be protected. All updates shall be auditable.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Site Updated | Facility Manager, Site Administrator | In-App, Email | Site profile saved | Include changed categories |
| Site Update Approval Required | Approver | In-App, Email | Governed field submitted | Include requester and reason |
| Site Update Approval Outcome | Requester | In-App, Email | Approval completed | Include decision result |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| SiteUpdated | Site Management | Audit Service, Reporting Service, Notification Service |
| SiteUpdateApprovalRequested | Site Management | Approval Workflow Service |
| SiteProfileChanged | Site Management | Facility Management, Reporting Service |

### Audit Events

| Audit Event | Trigger | Actor | Entity | Data Captured |
|---|---|---|---|---|
| Site Profile Viewed | Profile opened | Authorized user | Site | Site ID, actor, timestamp |
| Site Updated | Profile saved | Authorized user | Site | Previous values, new values, reason |
| Site Update Approval Requested | Governed update submitted | Authorized user | Approval Request | Requested changes and approval route |

### Reports Generated

- Site Summary Report
- Site Configuration Report
- Audit Trail Report

### Related Screens

- Site Profile
- Site Management
- Site Dashboard
- Approval Request
- Audit History

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/sites/{siteId} | GET | Authorized token | Retrieve Site profile | 200 OK with Site resource |
| /api/v1/sites/{siteId} | PATCH | Authorized token | Update Site details | 200 OK with updated Site |
| /api/v1/sites/{siteId}/approval-requests | POST | Authorized token | Submit governed Site change | 202 Accepted with approval request |
| /api/v1/sites/{siteId}/audit-events | GET | Authorized token | Retrieve Site audit events | 200 OK with audit list |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Site | Read, Update | Store Site profile | Primary entity |
| Facility | Read | Validate parent scope | Parent entity |
| Approval Request | Insert, Update | Manage governed changes | Conditional |
| Audit Log | Insert | Record Site updates | Required |
| Notification | Insert | Queue update notifications | Conditional |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Draft | Update details | Draft | Authorized user | Valid update |
| Active | Update non-governed details | Active | Authorized user | Valid permitted fields |
| Active | Submit governed change | Active with Pending Approval | Authorized user | Approval required |
| Suspended | Update permitted details | Suspended | Authorized user | Limited maintenance allowed |
| Archived | Attempt update | Archived | Authorized user | Update blocked |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| SIT-101 | Site cannot be updated in archived status. | Site is Archived | Contact administrator |
| SIT-102 | Site code already exists for this Facility. | Duplicate code | Enter a unique code |
| SIT-103 | Complete Site address is required. | Missing address fields | Complete address |
| SIT-104 | You do not have permission to update this Site. | Missing permission or scope | Request access |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Update Site details | Given the user has Site update permission | When valid changes are submitted | Then the system shall save the Site profile |
| Block archived update | Given the Site is Archived | When update is attempted | Then the system shall block the update |
| Enforce scope | Given the Site is outside user scope | When profile is requested | Then access shall be denied and logged |
| Audit update | Given Site profile is updated | When the transaction completes | Then previous and new values shall be audited |

### Dependencies

- Facility Management
- Approval Workflow Service
- Notification Service
- Audit Service
- Site lifecycle model

### Operational Considerations

Support teams shall be able to trace failed updates, scope denial, and pending approval status from audit logs.

### Non-Functional Considerations

Site update behavior shall be secure, tenant-isolated, auditable, responsive, and reliable for multi-branch Organizations.

### Assumptions

- Site Administrators may have limited update access based on policy.
- Site lifecycle actions are handled separately.
- Archived Sites are read-only.

### Success Criteria

Site profile information remains complete, current, authorized, and auditable.

### Related Functional Requirements

- FR-SIT-001 - Create Site
- FR-SIT-003 - Configure Site Settings
- FR-SIT-007 - Activate Site
- FR-SIT-010 - View Site Dashboard

### Notes

This requirement governs Site master data, not operational transactions.

---

## FR-SIT-003 - Configure Site Settings

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-SIT-003 |
| Requirement Name | Configure Site Settings |
| Functional Module | Site Management |
| Business Domain | Site |
| Business Capability | Site Configuration |
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
| Business Requirement | BA-08 Site Management |
| Business Rule | BA-02 BR-SIT-001, BR-SIT-002, BR-SIT-003, BR-SIT-004, BR-SIT-006, BR-FAC-004, BR-ORG-004 |
| Business Process | BA-03 BP-SIT-003 Configure Site Settings |
| Business Process Flow | BA-04 Section 11 Site Management Flow |
| Persona | BA-05 Organization Administrator, Facility Manager, Site Administrator |
| User Journey | BA-06 Section 6 Site Administrator Journey |
| Stakeholder | BA-07 Organization Administrator, Facility Manager, Site Administrator |
| Non-Functional Requirement | BA-09 Section 8 Business Configurability |
| Assumption / Constraint / Risk | BA-10 BA-ASS-006, BA-CON-006 |

### Purpose

To allow Site-level configuration while preserving inherited Facility and Organization governance.

### Functional Requirement

The system shall allow authorized users to configure Site Settings by inheriting Facility defaults or applying approved Site-level overrides within policy constraints.

### Business Justification

Sites may have local operational needs such as branch-specific communication, access rules, local defaults, and operational preferences, but those differences must remain controlled by parent Facility governance.

### Actors

- Organization Administrator
- Facility Manager
- Site Administrator
- Approval Workflow Service
- Notification Service
- Audit Service

### Preconditions

- Site exists.
- Parent Facility exists and is eligible.
- Site is not Archived.
- User is authenticated.
- User has Site settings permission.
- Site-level overrides are permitted by Facility and Organization policy.

### Trigger

Authorized user opens Site Settings and submits inherited or local configuration changes.

### In Scope

- View inherited Facility settings.
- Configure allowed Site-level settings.
- Validate override eligibility.
- Route governed overrides for approval.
- Update Site configuration context.
- Record audit and notification events.

### Out of Scope

- Facility-level settings.
- Organization-level settings.
- Site Operating Hours.
- Site Capacity Limits.
- Platform configuration.

### Inputs

- Site ID
- Setting category
- Setting value
- Inheritance mode
- Override reason
- Effective date
- Approval reference, if required

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Site ID | Site configuration context | Identifier | Yes | System | Must exist and match scope | Primary context |
| Setting Category | Local configuration group | Master Data | Yes | System | Must be enabled for Site | Controls available fields |
| Setting Value | Configured local value | Configuration | Conditional | Authorized user | Must match type and constraints | Required for override mode |
| Inheritance Mode | Inherit or override Facility value | Enum | Yes | Authorized user | Override must be allowed by policy | Key governance control |
| Override Reason | Reason for local override | Text | Conditional | Authorized user | Required for override | Audit field |
| Effective Date | Date change becomes active | Date | Yes | Authorized user | Must satisfy policy | Supports scheduling |

### Main Flow

1. Authorized user opens Site Settings.
2. The system loads Facility defaults, current Site settings, override rules, and Site status.
3. User selects inheritance or local override for allowed setting categories.
4. The system validates permission, Site status, Facility constraints, Organization policy, and data values.
5. The system displays impact on local operations.
6. If approval is required, the system creates an approval request.
7. If approval is not required, or after approval is granted, the system saves Site Settings.
8. The system updates local operational context and dashboard status.
9. The system records audit events and sends notifications.

### Alternate Flows

- If all settings inherit from Facility, the system stores inherited state without local values.
- If Facility updates later, inherited Site settings update automatically.
- If a local override is removed, the Site returns to inherited Facility value.

### Exception Flows

- If override is not permitted, the system blocks local setting changes.
- If the Site is Archived, settings are read-only.
- If the value violates Facility or Organization policy, save is blocked.
- If approval is rejected, inherited or existing active setting remains unchanged.

### Outputs

- Updated Site Settings.
- Inheritance or override status.
- Approval request, if applicable.
- Dashboard and configuration status updates.
- Notifications and audit events.

### UI Behaviour

Site Settings shall clearly display inherited values, local overrides, locked fields, parent Facility source, approval status, and impact messages. Users shall be able to revert allowed overrides back to inherited values.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-SIT-201 | Site Settings must remain within Facility and Organization constraints. | Block save and show constraint. | Critical |
| VAL-SIT-202 | Local override requires override permission and reason. | Block save or route approval. | High |
| VAL-SIT-203 | Archived Sites cannot update settings. | Block update. | Critical |
| VAL-SIT-204 | Inherited settings must reflect active Facility configuration. | Sync inherited value and log source. | High |
| VAL-SIT-205 | User must have Site settings permission. | Deny access and log event. | Critical |

### Business Rules

- BA-02 BR-SIT-001 - Site Ownership
- BA-02 BR-SIT-002 - Facility-to-Site Relationship
- BA-02 BR-SIT-003 - Site Add-on Licensing
- BA-02 BR-SIT-004 - Site Operational Status
- BA-02 BR-SIT-006 - Site Capacity
- BA-02 BR-FAC-004 - Facility Capacity
- BA-02 BR-ORG-004 - Organization Policies

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| site.settings.view | Organization Administrator, Facility Manager, Site Administrator | Read | Required to view settings |
| site.settings.update | Organization Administrator | Update | Full Site configuration access |
| site.settings.maintain | Facility Manager, Site Administrator | Update | Limited local maintenance |
| site.settings.approve | Authorized Approver | Approve | Required for governed overrides |

### Security Considerations

Site Settings shall enforce Organization, Facility, and Site scope. Overrides shall be controlled through RBAC and approval policies because they may affect customer access, attendance, scheduling, and local operations.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Site Configured | Facility Manager, Site Administrator | In-App, Email | Site Settings saved | Include changed setting categories |
| Site Override Approval Required | Approver | In-App, Email | Governed override submitted | Include override reason and parent value |
| Site Settings Reverted | Facility Manager, Site Administrator | In-App | Override removed | Include inherited source |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| SiteSettingsUpdated | Site Management | Attendance Management, Activity Management, Reporting Service |
| SiteOverrideRequested | Site Management | Approval Workflow Service |
| SiteInheritedSettingsSynchronized | Site Management | Audit Service, Notification Service |

### Audit Events

| Audit Event | Trigger | Actor | Entity | Data Captured |
|---|---|---|---|---|
| Site Settings Viewed | Settings opened | Authorized user | Site Settings | Site ID, actor, timestamp |
| Site Settings Updated | Settings saved | Authorized user | Site Settings | Previous values, new values, inheritance mode |
| Site Override Approved | Approval completed | Authorized Approver | Approval Request | Decision and override details |

### Reports Generated

- Site Configuration Report
- Site Summary Report
- Configuration Change Report
- Audit Trail Report

### Related Screens

- Site Settings
- Site Profile
- Site Dashboard
- Configuration Impact Summary
- Approval Request

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/sites/{siteId}/settings | GET | Authorized token | Retrieve Site Settings | 200 OK with settings resource |
| /api/v1/sites/{siteId}/settings | PATCH | Authorized token | Update Site Settings | 200 OK with updated settings |
| /api/v1/sites/{siteId}/settings/inheritance | GET | Authorized token | Retrieve inherited setting source | 200 OK with inheritance details |
| /api/v1/sites/{siteId}/settings/impact | POST | Authorized token | Evaluate Site setting impact | 200 OK with impact summary |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Site | Read | Validate scope and lifecycle | Parent context |
| Site Settings | Read, Update | Store Site configuration | Primary entity |
| Facility Settings | Read | Provide inherited defaults | Parent source |
| Facility Policy | Read | Validate constraints | Governance |
| Approval Request | Insert, Update | Manage governed overrides | Conditional |
| Audit Log | Insert | Record setting changes | Required |
| Notification | Insert | Queue notifications | Conditional |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Inherited | Create local override | Override Draft | Authorized user | Override allowed |
| Override Draft | Submit governed override | Pending Approval | Authorized user | Approval required |
| Override Draft | Save non-governed override | Override Active | Authorized user | Valid value |
| Pending Approval | Approve override | Override Active | Authorized Approver | Approval granted |
| Override Active | Revert to inherited | Inherited | Authorized user | Revert permitted |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| SIT-201 | Site setting violates Facility policy. | Parent constraint violation | Select an allowed value |
| SIT-202 | Local override is not permitted for this setting. | Override disabled | Use inherited setting |
| SIT-203 | Override reason is required. | Missing reason | Enter override reason |
| SIT-204 | You do not have permission to update Site Settings. | Missing permission | Request access |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Save valid Site setting | Given the user has Site settings permission | When valid setting values are submitted | Then the system shall save the Site Settings |
| Enforce inheritance | Given override is not allowed | When the user attempts a local override | Then the system shall block the override |
| Revert to inherited | Given a local override exists | When the user selects revert | Then the Site shall use the parent Facility value |
| Audit setting change | Given Site Settings change | When saved | Then audit history shall record source and values |

### Dependencies

- Facility Settings
- Facility Policy
- Organization policy
- Approval Workflow Service
- Notification Service
- Audit Service

### Operational Considerations

Inherited and overridden settings shall be visible to support teams to resolve branch-specific behavior issues.

### Non-Functional Considerations

Site Settings shall be secure, configurable, auditable, maintainable, and scalable across many branches.

### Assumptions

- Facility configuration is the default source for Site configuration.
- Site overrides require policy permission.
- Downstream operational modules consume active Site configuration.

### Success Criteria

Site configuration supports local operational needs without violating Facility or Organization governance.

### Related Functional Requirements

- FR-FAC-003 - Configure Facility Settings
- FR-FAC-012 - Manage Facility Policies
- FR-SIT-004 - Configure Site Operating Hours
- FR-SIT-005 - Configure Site Capacity Limits
- FR-SIT-011 - Manage Site Policies

### Notes

Site Settings are the local configuration layer beneath Facility Settings.

---

## FR-SIT-004 - Configure Site Operating Hours

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-SIT-004 |
| Requirement Name | Configure Site Operating Hours |
| Functional Module | Site Management |
| Business Domain | Site |
| Business Capability | Site Operations |
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
| Business Requirement | BA-08 Site Management |
| Business Rule | BA-02 BR-SIT-001, BR-SIT-004, BR-SIT-006, BR-FAC-005, BR-FAC-006, BR-ORG-004 |
| Business Process | BA-03 BP-SIT-004 Configure Site Operating Hours |
| Business Process Flow | BA-04 Section 11 Site Management Flow |
| Persona | BA-05 Organization Administrator, Facility Manager, Site Administrator |
| User Journey | BA-06 Section 6 Site Administrator Journey |
| Stakeholder | BA-07 Organization Administrator, Facility Manager, Site Administrator |
| Non-Functional Requirement | BA-09 Section 2.8 Configurability |
| Assumption / Constraint / Risk | BA-10 BA-ASS-006 |

### Purpose

To configure local Site operating schedules within parent Facility operating-hour rules.

### Functional Requirement

The system shall allow authorized users to configure Site Operating Hours, holidays, closures, and exceptions by inheriting Facility hours or applying approved local schedules.

### Business Justification

Sites may operate with local branch schedules due to location, staff availability, holidays, or branch-specific constraints, but must remain governed by Facility policies.

### Actors

- Organization Administrator
- Facility Manager
- Site Administrator
- Approval Workflow Service
- Notification Service
- Audit Service

### Preconditions

- Site exists.
- Parent Facility exists and is eligible.
- Site is not Archived.
- User is authenticated.
- User has Site operating hours permission.
- Facility operating hours are configured.

### Trigger

Authorized user opens Site Operating Hours and submits schedule changes.

### In Scope

- View inherited Facility operating hours.
- Configure allowed Site schedule overrides.
- Configure local holidays and closures.
- Validate parent schedule compatibility.
- Notify affected users and record audit events.

### Out of Scope

- Facility Operating Hours.
- Staff shift scheduling.
- Batch scheduling.
- Attendance check-in.
- Emergency incident handling.

### Inputs

- Site ID
- Inheritance mode
- Day of week
- Opening time
- Closing time
- Break periods
- Holiday or closure dates
- Effective date
- Change reason

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Site ID | Site schedule context | Identifier | Yes | System | Must exist and match scope | Primary context |
| Inheritance Mode | Inherit Facility schedule or override locally | Enum | Yes | Authorized user | Override must be permitted | Controls schedule source |
| Opening Time | Local opening time | Time | Conditional | Authorized user | Before closing time and within allowed rules | Required for operating days |
| Closing Time | Local closing time | Time | Conditional | Authorized user | After opening time | Required for operating days |
| Break Period | Local break interval | Time Range | No | Authorized user | Must be within operating window | Optional |
| Holiday Date | Local closure date | Date | No | Authorized user | Must satisfy policy | Used for exceptions |
| Change Reason | Schedule change reason | Text | Conditional | Authorized user | Required for override or governed change | Audit field |

### Main Flow

1. Authorized user opens Site Operating Hours.
2. The system loads Facility hours, current Site hours, inheritance status, and policy constraints.
3. User selects inherit or local override.
4. User enters local schedule, holidays, closures, and effective dates where applicable.
5. The system validates time ranges, Facility policy compatibility, active schedule impact, permission, and approval requirements.
6. If approval is required, the system creates an approval request.
7. If approval is not required, or after approval is granted, the system saves Site Operating Hours.
8. The system updates local calendars and scheduling context.
9. The system sends notifications and records audit events.

### Alternate Flows

- If the Site inherits Facility hours, local time fields remain read-only.
- If a local holiday is added, the Site calendar changes without changing Facility hours.
- If future-dated hours are configured, the system schedules activation.

### Exception Flows

- If local hours conflict with Facility policy, save is blocked.
- If operating hours affect active schedules, the system displays impact and may require approval.
- If Site is Archived, changes are blocked.
- If approval is rejected, current hours remain active.

### Outputs

- Updated Site Operating Hours.
- Inheritance or override status.
- Local calendar update.
- Approval request, if applicable.
- Notifications and audit events.

### UI Behaviour

The screen shall display Facility inherited hours, local override controls, holiday calendar, effective dates, and schedule impact. Local overrides shall show the parent Facility comparison.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-SIT-301 | Site hours must comply with Facility schedule policy. | Block save or route approval. | High |
| VAL-SIT-302 | Opening time must be before closing time. | Block save. | High |
| VAL-SIT-303 | Break periods must fall within local operating hours. | Block save. | High |
| VAL-SIT-304 | Local schedule override requires permission and reason. | Block save or require approval. | High |
| VAL-SIT-305 | Archived Sites cannot update operating hours. | Block update. | Critical |

### Business Rules

- BA-02 BR-SIT-001 - Site Ownership
- BA-02 BR-SIT-004 - Site Operational Status
- BA-02 BR-SIT-006 - Site Capacity
- BA-02 BR-FAC-005 - Facility Operating Hours
- BA-02 BR-FAC-006 - Facility Status
- BA-02 BR-ORG-004 - Organization Policies

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| site.operating-hours.view | Organization Administrator, Facility Manager, Site Administrator | Read | Required to view hours |
| site.operating-hours.update | Organization Administrator | Update | Full schedule update |
| site.operating-hours.maintain | Facility Manager, Site Administrator | Update | Limited local maintenance |
| site.operating-hours.approve | Authorized Approver | Approve | Required for governed overrides |

### Security Considerations

Site operating-hour changes shall be limited by Site scope, parent Facility policy, and user permissions. Customer-facing schedule changes shall be auditable.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Site Operating Hours Updated | Facility Manager, Site Administrator | In-App, Email | Hours saved | Include effective date and changed days |
| Site Schedule Override Approval Required | Approver | In-App, Email | Governed schedule override submitted | Include parent schedule comparison |
| Site Schedule Change Impact | Facility Manager, Site Administrator | In-App | Active schedules affected | Include affected items |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| SiteOperatingHoursUpdated | Site Management | Attendance Management, Activity Management, Batch Management |
| SiteScheduleOverrideRequested | Site Management | Approval Workflow Service |
| SiteCalendarUpdated | Site Management | Reporting Service, Notification Service |

### Audit Events

| Audit Event | Trigger | Actor | Entity | Data Captured |
|---|---|---|---|---|
| Site Operating Hours Viewed | Screen opened | Authorized user | Site Operating Hours | Site ID, actor, timestamp |
| Site Operating Hours Updated | Schedule saved | Authorized user | Site Operating Hours | Previous schedule, new schedule, source |
| Site Schedule Override Approved | Approval completed | Authorized Approver | Approval Request | Decision and schedule change |

### Reports Generated

- Site Configuration Report
- Site Operating Hours Report
- Site Dashboard

### Related Screens

- Site Operating Hours
- Site Settings
- Site Dashboard
- Schedule Impact Summary
- Approval Request

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/sites/{siteId}/operating-hours | GET | Authorized token | Retrieve Site Operating Hours | 200 OK with schedule |
| /api/v1/sites/{siteId}/operating-hours | PUT | Authorized token | Save Site Operating Hours | 200 OK with updated schedule |
| /api/v1/sites/{siteId}/operating-hours/impact | POST | Authorized token | Evaluate schedule impact | 200 OK with impact summary |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Site | Read | Validate Site scope and status | Parent context |
| Site Operating Hours | Create, Read, Update | Store local schedule | Primary entity |
| Facility Operating Hours | Read | Validate inherited schedule | Parent source |
| Site Policy | Read | Validate local rules | Governance |
| Audit Log | Insert | Record schedule changes | Required |
| Notification | Insert | Queue notifications | Conditional |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Inherited | Create local schedule | Override Active | Authorized user | Override allowed and valid |
| Override Active | Schedule future change | Scheduled Change | Authorized user | Future effective date |
| Scheduled Change | Effective date reached | Override Active | System | Scheduled change active |
| Override Active | Revert to inherited | Inherited | Authorized user | Revert allowed |
| Override Active | Submit governed change | Pending Approval | Authorized user | Approval required |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| SIT-301 | Site hours conflict with Facility policy. | Parent schedule constraint | Adjust Site hours |
| SIT-302 | Opening time must be before closing time. | Invalid time range | Correct time values |
| SIT-303 | Break period must be within operating hours. | Invalid break period | Adjust break period |
| SIT-304 | You do not have permission to update Site Operating Hours. | Missing permission | Request access |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Save valid local hours | Given user has permission and override is allowed | When valid Site hours are submitted | Then the system shall save Site Operating Hours |
| Inherit Facility hours | Given Site is configured to inherit | When Facility hours are active | Then Site shall use inherited Facility hours |
| Block conflict | Given Site hours violate Facility policy | When save is attempted | Then the system shall block save |
| Audit schedule | Given Site hours change | When saved | Then audit history shall record previous and new schedule |

### Dependencies

- Facility Operating Hours
- Facility Policy
- Activity and Batch Management
- Attendance Management
- Approval Workflow Service
- Audit Service

### Operational Considerations

Schedule changes shall expose local impact on attendance windows, batches, activities, and customer-facing availability.

### Non-Functional Considerations

Site Operating Hours shall be timezone-aware, auditable, reliable, usable, and maintainable.

### Assumptions

- Site timezone follows Organization or Facility configuration unless local override is allowed.
- Facility hours define the governance boundary.
- Downstream modules consume active Site schedule.

### Success Criteria

Site operating schedules are locally accurate, policy-compliant, auditable, and synchronized with branch operations.

### Related Functional Requirements

- FR-FAC-005 - Configure Operating Hours
- FR-SIT-003 - Configure Site Settings
- FR-SIT-007 - Activate Site
- FR-ACT-001 - Configure Activities
- FR-BAT-001 - Manage Batch Schedule

### Notes

Site Operating Hours enable branch-specific scheduling while preserving Facility governance.

---

## FR-SIT-005 - Configure Site Capacity Limits

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-SIT-005 |
| Requirement Name | Configure Site Capacity Limits |
| Functional Module | Site Management |
| Business Domain | Site |
| Business Capability | Site Operations |
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
| Business Requirement | BA-08 BR-SIT-006 Site Capacity |
| Business Rule | BA-02 BR-SIT-006, BR-SIT-004, BR-FAC-004, BR-FAC-006, BR-ORG-004, BR-ORG-010 |
| Business Process | BA-03 BP-SIT-005 Configure Site Capacity Limits |
| Business Process Flow | BA-04 Section 11 Site Management Flow |
| Persona | BA-05 Organization Administrator, Facility Manager, Site Administrator |
| User Journey | BA-06 Section 6 Site Administrator Journey |
| Stakeholder | BA-07 Organization Administrator, Facility Manager, Site Administrator |
| Non-Functional Requirement | BA-09 Section 2.3 Scalability, Section 8 Business Configurability |
| Assumption / Constraint / Risk | BA-10 BA-ASS-006, BA-RSK-004 |

### Purpose

To configure Site-level capacity limits that control local branch occupancy, sessions, batches, and bookings.

### Functional Requirement

The system shall allow authorized users to configure Site Capacity limits within Facility-level maximum capacity, Organization policy, and operational constraints.

### Business Justification

Site capacity control prevents unsafe occupancy, overbooking, and local service quality issues while allowing branches to operate independently within Facility governance.

### Actors

- Organization Administrator
- Facility Manager
- Site Administrator
- Notification Service
- Audit Service
- Reporting Service

### Preconditions

- Site exists.
- Parent Facility capacity is configured.
- Site is not Archived.
- User is authenticated.
- User has Site capacity permission.
- Capacity category is applicable to the Site.

### Trigger

Authorized user opens Site Capacity Limits and submits capacity changes.

### In Scope

- Configure Site capacity categories.
- Validate Facility upper-bound limits.
- Configure threshold alerts.
- Evaluate impact on active schedules and attendance.
- Record notifications and audit events.

### Out of Scope

- Facility Capacity configuration.
- Real-time attendance counting.
- Equipment inventory management.
- Batch enrollment processing.
- Emergency incident handling.

### Inputs

- Site ID
- Capacity category
- Capacity limit
- Effective date
- Threshold alert
- Override reason
- Approval reference, if applicable

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Capacity Category | Local capacity type | Master Data | Yes | System | Must be enabled by Facility Type | Examples include occupancy and batch capacity |
| Capacity Limit | Site-level maximum | Number | Yes | Authorized user | Positive and not above Facility limit | Primary value |
| Effective Date | Date limit becomes active | Date | Yes | Authorized user | Must satisfy policy | Supports scheduling |
| Threshold Alert | Alert value or percentage | Number | No | Authorized user | Must be below limit | Drives warnings |
| Override Reason | Reason for Site-specific limit | Text | Conditional | Authorized user | Required when below or different from inherited value | Audit field |

### Main Flow

1. Authorized user opens Site Capacity Limits.
2. The system loads Facility capacity, current Site capacity, policy constraints, and usage data.
3. User enters capacity values and threshold alerts.
4. The system validates positive values, Facility upper limits, policy rules, active usage impact, and approval requirements.
5. The system displays impact on local operations.
6. If approval is required, the system creates an approval request.
7. If approval is not required, or after approval is granted, the system saves Site Capacity.
8. The system updates capacity indicators and dashboard widgets.
9. The system records audit events and sends notifications.

### Alternate Flows

- If Site inherits Facility capacity, local values are not required.
- If temporary capacity override is configured for maintenance or event, the system schedules it with start and end dates.
- If Site capacity is below Facility capacity, the system accepts it when policy allows.

### Exception Flows

- If Site capacity exceeds Facility capacity, the system blocks save.
- If capacity reduction conflicts with current attendance or bookings, the system displays impact and may require approval.
- If category is unsupported, the system disables it.
- If Site is Archived, updates are blocked.

### Outputs

- Updated Site Capacity.
- Capacity threshold configuration.
- Impact summary.
- Notifications.
- Audit events.
- Updated dashboard metrics.

### UI Behaviour

The Site Capacity screen shall display Facility maximum, current Site limit, current usage, threshold alert, override status, and impact messages. Values exceeding Facility limits shall be visually rejected.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-SIT-401 | Site capacity must be positive. | Block save. | High |
| VAL-SIT-402 | Site capacity shall not exceed Facility capacity. | Block save and show Facility limit. | Critical |
| VAL-SIT-403 | Threshold alert must be below capacity limit. | Block save. | Medium |
| VAL-SIT-404 | Capacity reduction affecting active operations requires impact review. | Display impact and route approval if required. | High |
| VAL-SIT-405 | User must have Site capacity permission. | Deny access and log event. | Critical |

### Business Rules

- BA-02 BR-SIT-006 - Site Capacity
- BA-02 BR-SIT-004 - Site Operational Status
- BA-02 BR-FAC-004 - Facility Capacity
- BA-02 BR-FAC-006 - Facility Status
- BA-02 BR-ORG-004 - Organization Policies
- BA-02 BR-ORG-010 - Organization Audit Trail

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| site.capacity.view | Organization Administrator, Facility Manager, Site Administrator | Read | Required to view Site capacity |
| site.capacity.update | Organization Administrator | Update | Full capacity configuration |
| site.capacity.maintain | Facility Manager, Site Administrator | Update | Limited local maintenance |
| site.capacity.approve | Authorized Approver | Approve | Required for governed capacity changes |

### Security Considerations

Site Capacity shall be configured only by authorized users within Site scope. Capacity changes affecting safety or committed operations shall be auditable and approval-gated where configured.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Site Capacity Updated | Facility Manager, Site Administrator | In-App, Email | Capacity saved | Include limit and effective date |
| Site Capacity Approval Required | Approver | In-App, Email | Governed capacity change submitted | Include impact summary |
| Site Capacity Warning | Facility Manager, Site Administrator | In-App | Threshold reached | Include capacity category and usage |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| SiteCapacityUpdated | Site Management | Attendance Management, Batch Management, Reporting Service |
| SiteCapacityThresholdReached | Attendance Management | Notification Service, Reporting Service |
| SiteCapacityApprovalRequested | Site Management | Approval Workflow Service |

### Audit Events

| Audit Event | Trigger | Actor | Entity | Data Captured |
|---|---|---|---|---|
| Site Capacity Viewed | Screen opened | Authorized user | Site Capacity | Site ID, actor, timestamp |
| Site Capacity Updated | Limit saved | Authorized user | Site Capacity | Previous limit, new limit, category |
| Site Capacity Violation Attempted | Invalid limit submitted | Authorized user | Site Capacity | Submitted value and violated constraint |

### Reports Generated

- Site Capacity Report
- Site Dashboard
- Site Configuration Report
- Facility Capacity Report

### Related Screens

- Site Capacity
- Site Dashboard
- Capacity Overview
- Approval Request
- Audit History

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/sites/{siteId}/capacity-limits | GET | Authorized token | Retrieve Site capacity limits | 200 OK with capacity list |
| /api/v1/sites/{siteId}/capacity-limits | PUT | Authorized token | Save Site capacity limits | 200 OK with updated limits |
| /api/v1/sites/{siteId}/capacity-limits/impact | POST | Authorized token | Evaluate capacity impact | 200 OK with impact summary |
| /api/v1/sites/{siteId}/capacity-limits/violations | GET | Authorized token | Retrieve capacity violations | 200 OK with violation list |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Site | Read | Validate scope and lifecycle | Parent context |
| Site Capacity | Create, Read, Update | Store Site limits | Primary entity |
| Facility Capacity | Read | Validate upper boundary | Parent source |
| Site Policy | Read | Validate local constraints | Governance |
| Audit Log | Insert | Record capacity changes | Required |
| Notification | Insert | Queue capacity alerts | Conditional |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Inherited | Create local capacity | Override Active | Authorized user | Value within Facility limit |
| Override Active | Schedule capacity change | Scheduled Change | Authorized user | Future effective date |
| Scheduled Change | Effective date reached | Override Active | System | Change active |
| Override Active | Submit governed change | Pending Approval | Authorized user | Approval required |
| Override Active | Revert to inherited | Inherited | Authorized user | Revert allowed |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| SIT-401 | Site capacity must be greater than zero. | Invalid numeric value | Enter positive value |
| SIT-402 | Site capacity cannot exceed Facility capacity. | Facility limit exceeded | Lower Site capacity |
| SIT-403 | Capacity threshold must be below capacity limit. | Invalid threshold | Adjust threshold |
| SIT-404 | Capacity change conflicts with active operations. | Active dependency | Review impact |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Save valid capacity | Given user has permission | When valid capacity is submitted | Then the system shall save Site Capacity |
| Enforce Facility limit | Given Site capacity exceeds Facility limit | When save is attempted | Then the system shall block save |
| Trigger warning | Given capacity reaches threshold | When usage crosses threshold | Then the system shall generate Site Capacity Warning |
| Audit change | Given capacity changes | When saved | Then audit history shall record previous and new values |

### Dependencies

- Facility Capacity
- Site Policy
- Attendance Management
- Batch Management
- Reporting Service
- Audit Service

### Operational Considerations

Capacity changes shall show local impact and should not silently invalidate active operational commitments.

### Non-Functional Considerations

Site Capacity shall be reliable, auditable, scalable, and performant for high-frequency operational checks.

### Assumptions

- Facility Capacity is the upper boundary.
- Site capacity may be lower than Facility capacity.
- Downstream operational modules enforce active Site capacity.

### Success Criteria

Site capacity is configured safely within Facility constraints and supports controlled branch operations.

### Related Functional Requirements

- FR-FAC-006 - Configure Capacity Limits
- FR-SIT-003 - Configure Site Settings
- FR-SIT-007 - Activate Site
- FR-ATT-001 - Record Attendance
- FR-BAT-001 - Manage Batch Schedule

### Notes

Site capacity controls local limits and aggregates upward into Facility reporting.

---

## FR-SIT-006 - Manage Site Documents

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-SIT-006 |
| Requirement Name | Manage Site Documents |
| Functional Module | Site Management |
| Business Domain | Site |
| Business Capability | Site Administration |
| Requirement Type | Functional |
| Requirement Category | Transaction |
| Requirement Version | 1.0 |
| Requirement Status | Approved |
| Priority | High |
| Complexity | High |
| Release Version | 1.0 |
| Owner | Product Management |

### Traceability References

| Traceability Type | Reference |
|---|---|
| Business Requirement | BA-08 Site Management |
| Business Rule | BA-02 BR-SIT-005, BR-SIT-009, BR-SIT-010, BR-ORG-010, BR-AUD-001, BR-AUD-004 |
| Business Process | BA-03 BP-SIT-006 Manage Site Documents |
| Business Process Flow | BA-04 Section 11 Site Management Flow |
| Persona | BA-05 Organization Administrator, Facility Manager, Site Administrator |
| User Journey | BA-06 Section 6 Site Administrator Journey |
| Stakeholder | BA-07 Organization Administrator, Facility Manager, Site Administrator, External Auditor |
| Non-Functional Requirement | BA-09 Section 4 Compliance Requirements, Section 10 Data Management |
| Assumption / Constraint / Risk | BA-10 BA-RSK-007 |

### Purpose

To maintain Site-level compliance and operational documents with secure storage, versioning, retention, and auditability.

### Functional Requirement

The system shall allow authorized users to upload, classify, version, view, replace, retire, and audit Site Documents according to document type and retention rules.

### Business Justification

Physical Sites require permits, safety certificates, inspection reports, lease agreements, and local compliance documents to support branch operations and audit readiness.

### Actors

- Organization Administrator
- Facility Manager
- Site Administrator
- External Auditor
- Notification Service
- Audit Service

### Preconditions

- Site exists.
- Site is not Archived for standard document updates.
- User is authenticated.
- User has Site document permission.
- Site document types and retention rules are configured.

### Trigger

Authorized user opens Site Documents and uploads, replaces, views, downloads, or retires a document.

### In Scope

- Upload Site documents.
- Capture metadata.
- Manage document versions.
- Retire documents where allowed.
- Enforce retention and secure download.
- Notify stakeholders and audit activity.

### Out of Scope

- Organization documents.
- Facility documents.
- Customer documents.
- External e-signature integration.
- Legal document drafting.

### Inputs

- Site ID
- Document file
- Document type
- Document title
- Document number
- Issue date
- Expiry date
- Issuing authority
- Version notes
- Retirement reason

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Document File | Uploaded Site document | File | Yes | Authorized user | Allowed file type, size, malware scan | Stored securely |
| Document Type | Classification | Master Data | Yes | Authorized user | Must be active Site document type | Drives metadata |
| Document Title | Display name | Text | Yes | Authorized user | Length validation | Searchable |
| Document Number | Official identifier | Text | Conditional | Authorized user | Required by document type | Compliance metadata |
| Issue Date | Date issued | Date | Conditional | Authorized user | Must not be after expiry | Optional by type |
| Expiry Date | Date expires | Date | Conditional | Authorized user | Must be after issue date | Drives alerts |
| Issuing Authority | Authority name | Text | Conditional | Authorized user | Required by type | Compliance metadata |
| Version Notes | Reason for replacement | Text | Conditional | Authorized user | Required for replacement | Audit field |

### Main Flow

1. Authorized user opens Site Documents.
2. The system loads document register, document types, retention rules, and permissions.
3. User selects upload, replace, view, download, or retire.
4. For upload or replacement, user provides file and required metadata.
5. The system validates file type, size, malware scan, metadata, expiry dates, and permission.
6. The system stores the document securely and creates a version record.
7. The system supersedes prior version where replacement applies.
8. The system updates document register and compliance indicators.
9. The system sends notifications for uploads, replacements, retirements, and expiry-related changes.
10. The system records audit events.

### Alternate Flows

- If user views a document only, the system logs access without changing records.
- If document type has no expiry, expiry monitoring is not scheduled.
- If Site is Archived, authorized users may view historical documents in read-only mode.

### Exception Flows

- If file validation fails, upload is rejected.
- If malware scan fails, the file is blocked.
- If required metadata is missing, save is blocked.
- If retention rules prevent deletion, the system allows retirement only.
- If user lacks download permission, access is denied and logged.

### Outputs

- Site Document record created or updated.
- Document version history.
- Compliance indicator update.
- Expiry monitoring entry, if applicable.
- Notifications and audit events.

### UI Behaviour

Site Documents shall display a searchable document register with filters by type, status, expiry, and upload date. Historical versions shall remain visible to authorized users. Download actions shall respect permissions.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-SIT-501 | Document file is required for upload or replacement. | Block save. | Critical |
| VAL-SIT-502 | Document type must be active and valid for Site. | Block save. | High |
| VAL-SIT-503 | File must pass type, size, and malware validation. | Reject upload. | Critical |
| VAL-SIT-504 | Required metadata must be provided by document type. | Block save. | High |
| VAL-SIT-505 | Historical document versions must be retained by policy. | Disable deletion and allow retirement only. | Critical |

### Business Rules

- BA-02 BR-SIT-005 - Site Address
- BA-02 BR-SIT-009 - Site Closure
- BA-02 BR-SIT-010 - Historical Records
- BA-02 BR-ORG-010 - Organization Audit Trail
- BA-02 BR-AUD-001 - Audit Logging
- BA-02 BR-AUD-004 - Audit Record Contents

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| site.documents.view | Organization Administrator, Facility Manager, Site Administrator, External Auditor | Read | Required to view register |
| site.documents.upload | Organization Administrator, Facility Manager, Site Administrator | Create | Required to upload |
| site.documents.replace | Organization Administrator, Facility Manager, Site Administrator | Update | Required to replace |
| site.documents.retire | Organization Administrator | Update | Required to retire |
| site.documents.download | Authorized user | Read | Required to download files |

### Security Considerations

Site documents shall be protected using tenant isolation, secure storage, malware scanning, access control, encrypted download links, retention rules, and audit logging.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Site Document Uploaded | Facility Manager, Site Administrator | In-App, Email | Document stored | Include document type and title |
| Site Document Replaced | Facility Manager, Site Administrator | In-App, Email | Version replaced | Include version details |
| Site Document Expiry Alert | Facility Manager, Site Administrator | In-App, Email | Expiry threshold reached | Include expiry date |
| Site Document Retired | Organization Administrator, Facility Manager | In-App, Email | Document retired | Include reason |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| SiteDocumentUploaded | Site Management | Audit Service, Notification Service |
| SiteDocumentReplaced | Site Management | Audit Service, Compliance Reporting |
| SiteDocumentRetired | Site Management | Reporting Service, Audit Service |
| SiteDocumentExpiryDetected | Document Monitoring Job | Notification Service |

### Audit Events

| Audit Event | Trigger | Actor | Entity | Data Captured |
|---|---|---|---|---|
| Site Document Viewed | Document opened | Authorized user | Site Documents | Document ID, actor, timestamp |
| Site Document Downloaded | File downloaded | Authorized user | Site Documents | Document ID, source IP |
| Site Document Uploaded | Upload completed | Authorized user | Site Documents | Metadata, file reference, version |
| Site Document Replaced | Replacement completed | Authorized user | Site Documents | Old version, new version, reason |
| Site Document Retired | Retirement completed | Organization Administrator | Site Documents | Retirement reason and timestamp |

### Reports Generated

- Site Document Register
- Site Compliance Report
- Site Configuration Report
- Audit Trail Report

### Related Screens

- Site Documents
- Document Upload
- Document Version History
- Site Profile
- Audit History

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/sites/{siteId}/documents | GET | Authorized token | Retrieve Site document register | 200 OK with document list |
| /api/v1/sites/{siteId}/documents | POST | Authorized token | Upload Site document | 201 Created with document resource |
| /api/v1/sites/{siteId}/documents/{documentId} | GET | Authorized token | Retrieve document metadata | 200 OK with metadata |
| /api/v1/sites/{siteId}/documents/{documentId}/file | GET | Authorized token | Download document file | 200 OK with secure file response |
| /api/v1/sites/{siteId}/documents/{documentId}/replace | POST | Authorized token | Replace document version | 201 Created with new version |
| /api/v1/sites/{siteId}/documents/{documentId}/retire | POST | Organization Administrator token | Retire Site document | 200 OK with retired status |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Site | Read | Validate scope and status | Parent context |
| Site Documents | Create, Read, Update | Store metadata and version state | Primary entity |
| Audit Log | Insert | Record document activity | Required |
| Notification | Insert | Queue document notifications | Conditional |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| None | Upload document | Active | Authorized user | Valid file and metadata |
| Active | Replace document | Superseded | Authorized user | New version accepted |
| Active | Retire document | Retired | Organization Administrator | Retirement allowed |
| Active | Expiry date reached | Expired | System | Expiry monitoring detects expiry |
| Superseded | View history | Superseded | Authorized user | Read-only access |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| SIT-501 | Document file is required. | Missing file | Select document file |
| SIT-502 | Document type is not supported for Site. | Invalid type | Select supported type |
| SIT-503 | Document failed security validation. | Malware or scan failure | Upload safe file |
| SIT-504 | Required document metadata is incomplete. | Missing metadata | Complete highlighted fields |
| SIT-505 | Document cannot be deleted due to retention policy. | Retention rule | Retire document if permitted |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Upload Site document | Given user has upload permission | When valid file and metadata are submitted | Then the system shall store the document and version record |
| Replace document | Given an active document exists | When a valid replacement is uploaded | Then the prior version shall be superseded |
| Enforce security | Given file fails malware scan | When upload is attempted | Then the system shall reject upload |
| Retain history | Given a document is replaced or retired | When history is viewed | Then historical versions shall remain available to authorized users |

### Dependencies

- File storage service
- Malware scanning service
- Document type master data
- Retention policy
- Notification Service
- Audit Service

### Operational Considerations

Document upload, scan, storage, and download failures shall be logged with secure diagnostic context.

### Non-Functional Considerations

Site Document management shall support secure storage, privacy, availability, auditability, retention, and scalable branch compliance.

### Assumptions

- Site document types are configured by platform or implementation governance.
- Archived Sites allow read-only document access where policy permits.
- Deletion may be restricted by retention policy.

### Success Criteria

Site compliance documents are securely managed, versioned, searchable, retained, and auditable.

### Related Functional Requirements

- FR-SIT-001 - Create Site
- FR-SIT-002 - Update Site Details
- FR-SIT-007 - Activate Site
- FR-AUD-001 - Record Audit Events

### Notes

Site Documents support local branch compliance and audit readiness.

---

## FR-SIT-007 - Activate Site

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-SIT-007 |
| Requirement Name | Activate Site |
| Functional Module | Site Management |
| Business Domain | Site |
| Business Capability | Site Lifecycle |
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
| Business Requirement | BA-08 Site Management |
| Business Rule | BA-02 BR-SIT-001, BR-SIT-003, BR-SIT-004, BR-SIT-005, BR-SIT-006, BR-SIT-007, BR-FAC-006 |
| Business Process | BA-03 BP-SIT-007 Activate Site |
| Business Process Flow | BA-04 Section 11 Site Management Flow |
| Persona | BA-05 Organization Administrator, Facility Manager, Site Administrator |
| User Journey | BA-06 Section 6 Site Administrator Journey |
| Stakeholder | BA-07 Organization Administrator, Facility Manager, Site Administrator |
| Non-Functional Requirement | BA-09 Section 5 Availability & Business Continuity, Section 8 Business Configurability |
| Assumption / Constraint / Risk | BA-10 BA-ASS-002, BA-CON-003 |

### Purpose

To make a configured Site operational only after parent Facility, configuration, staff allocation, address, capacity, and entitlement conditions are satisfied.

### Functional Requirement

The system shall allow an Organization Administrator to activate an eligible Site and enable local operational transactions.

### Business Justification

Site activation prevents incomplete or non-compliant branches from accepting customers, recording attendance, scheduling activities, or generating operational transactions.

### Actors

- Organization Administrator
- Facility Manager
- Site Administrator
- License Service
- Notification Service
- Audit Service

### Preconditions

- Site exists in Draft status.
- Parent Facility is Active.
- Parent Facility entitlement is valid.
- Site address is complete.
- Site Settings, Operating Hours, Capacity, and required Policies are complete.
- Required Site staff allocation exists where configured.
- Site add-on license requirement is satisfied where applicable.

### Trigger

Organization Administrator selects Activate Site from Site lifecycle actions.

### In Scope

- Validate activation readiness.
- Validate parent Facility state and entitlement.
- Validate Site add-on license requirement.
- Activate Site.
- Enable local operational transactions.
- Notify stakeholders and audit lifecycle change.

### Out of Scope

- Facility activation.
- License purchase.
- Customer registration.
- Attendance recording.
- Membership plan publication.
- Staff account creation.

### Inputs

- Site ID
- Activation confirmation
- Activation notes
- Readiness validation result
- Entitlement validation result
- Effective activation timestamp

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Site ID | Site to activate | Identifier | Yes | Organization Administrator | Must exist and be Draft | Primary context |
| Activation Confirmation | Explicit confirmation | Boolean | Yes | Organization Administrator | Must be confirmed | Prevents accidental activation |
| Activation Notes | Activation comments | Text | No | Organization Administrator | Length validation | Audit field |
| Readiness Status | Setup validation result | Enum | Yes | System | Must be Ready | Derived from prerequisite checks |
| Entitlement Status | Site entitlement validation | Enum | Yes | License Service | Must be valid where required | Add-on dependency |

### Main Flow

1. Organization Administrator opens Site lifecycle actions.
2. Organization Administrator selects Activate Site.
3. The system validates parent Organization and Facility status, Site status, address, settings, hours, capacity, policies, staff allocation, and entitlement.
4. The system displays readiness checklist and blockers.
5. Organization Administrator confirms activation for a ready Site.
6. The system changes Site status from Draft to Active.
7. The system enables local operational transactions for the Site.
8. The system updates Site Dashboard, Facility Dashboard, and reporting context.
9. The system sends activation notifications.
10. The system records lifecycle audit events.

### Alternate Flows

- If optional warnings exist, activation may proceed where policy permits.
- If Site add-on licensing is pending, activation is blocked until entitlement is resolved.
- If approval is required, the system routes activation before status change.

### Exception Flows

- If parent Facility is not Active, activation is blocked.
- If readiness checks fail, activation is blocked and blockers are listed.
- If entitlement validation fails, Site remains Draft.
- If lifecycle update fails, Site remains in prior status and error is logged.

### Outputs

- Site status changed to Active.
- Local operational services enabled.
- Readiness result.
- Notifications.
- Audit events.
- Updated dashboards and reports.

### UI Behaviour

Activation shall display readiness checklist, parent Facility status, entitlement status, unresolved blockers, and explicit confirmation. Activation button shall be disabled when critical blockers exist.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-SIT-601 | Site must be Draft before activation. | Block activation. | Critical |
| VAL-SIT-602 | Parent Facility must be Active. | Block activation. | Critical |
| VAL-SIT-603 | Site address, settings, hours, capacity, and required policies must be complete. | Block activation and list blockers. | Critical |
| VAL-SIT-604 | Site add-on license must be valid where required. | Block activation and show entitlement action. | Critical |
| VAL-SIT-605 | User must have Site activation permission. | Deny action and log event. | Critical |

### Business Rules

- BA-02 BR-SIT-001 - Site Ownership
- BA-02 BR-SIT-003 - Site Add-on Licensing
- BA-02 BR-SIT-004 - Site Operational Status
- BA-02 BR-SIT-005 - Site Address
- BA-02 BR-SIT-006 - Site Capacity
- BA-02 BR-SIT-007 - Site Staff Allocation
- BA-02 BR-FAC-006 - Facility Status

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| site.lifecycle.view | Organization Administrator, Facility Manager, Site Administrator | Read | Required to view lifecycle |
| site.lifecycle.activate | Organization Administrator | Execute | Required to activate Site |
| site.readiness.view | Organization Administrator, Facility Manager | Read | Required to view readiness |
| site.entitlement-status.view | Organization Administrator | Read | Required to view entitlement status |

### Security Considerations

Site activation shall enforce Site scope, parent Facility validation, entitlement validation, RBAC, and audit logging. Activation shall not grant access beyond assigned roles and Site allocation.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Site Activated | Facility Manager, Site Administrator | In-App, Email | Site becomes Active | Include activation date and enabled operations |
| Site Activation Blocked | Organization Administrator | In-App | Readiness checks fail | Include blocker list |
| Site Add-on License Required | Organization Administrator | In-App, Email | Entitlement validation fails | Include license action |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| SiteActivationRequested | Site Management | License Service, Audit Service |
| SiteActivated | Site Management | Attendance Management, Activity Management, Reporting Service, Notification Service |
| SiteActivationBlocked | Site Management | Notification Service, Audit Service |

### Audit Events

| Audit Event | Trigger | Actor | Entity | Data Captured |
|---|---|---|---|---|
| Site Activation Readiness Checked | Readiness validation executed | Organization Administrator | Site | Readiness result and blockers |
| Site Activated | Status changed to Active | Organization Administrator | Site | Previous status, new status, entitlement result |
| Site Activation Blocked | Activation denied | System | Site | Failed checks and timestamp |

### Reports Generated

- Site Status Report
- Site Summary Report
- Site Dashboard
- Facility Dashboard
- Executive Dashboard

### Related Screens

- Site Activation
- Site Readiness Checklist
- Site Profile
- Site Dashboard
- Entitlement Status

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/sites/{siteId}/readiness | GET | Organization Administrator token | Retrieve activation readiness | 200 OK with readiness checklist |
| /api/v1/sites/{siteId}/entitlement-status | GET | Organization Administrator token | Retrieve Site entitlement status | 200 OK with entitlement result |
| /api/v1/sites/{siteId}/activate | POST | Organization Administrator token | Activate Site | 200 OK with active Site status |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Site | Read, Update | Validate and update lifecycle status | Primary entity |
| Facility | Read | Validate parent Facility status | Parent entity |
| Site Settings | Read | Validate configuration readiness | Prerequisite |
| Site Operating Hours | Read | Validate schedule readiness | Prerequisite |
| Site Capacity | Read | Validate capacity readiness | Prerequisite |
| Site Policy | Read | Validate policy readiness | Prerequisite |
| Audit Log | Insert | Record activation events | Required |
| Notification | Insert | Queue activation notices | Required |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Draft | Activate Site | Active | Organization Administrator | Readiness and entitlement checks pass |
| Draft | Activation blocked | Draft | System | Readiness or entitlement checks fail |
| Active | Activate Site | Active | Organization Administrator | Duplicate action blocked |
| Suspended | Activate Site | Suspended | Organization Administrator | Reactivation handled separately if supported |
| Archived | Activate Site | Archived | Organization Administrator | Action blocked |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| SIT-601 | Site is not ready for activation. | Readiness blockers exist | Complete listed setup items |
| SIT-602 | Parent Facility must be Active before Site activation. | Parent state invalid | Activate Facility first |
| SIT-603 | Site add-on license is required for activation. | Missing entitlement | Assign add-on license |
| SIT-604 | You do not have permission to activate this Site. | Missing permission | Request access |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Activate ready Site | Given readiness and entitlement checks pass | When Organization Administrator confirms activation | Then Site status shall become Active |
| Block inactive Facility | Given parent Facility is not Active | When activation is attempted | Then the system shall block activation |
| Enable local operations | Given activation succeeds | When Site status becomes Active | Then local operational transactions shall be enabled |
| Audit activation | Given activation is attempted | When action completes or fails | Then audit history shall record lifecycle event |

### Dependencies

- Active Facility
- Site Settings
- Site Operating Hours
- Site Capacity
- Site Policies
- License Service
- Notification Service
- Audit Service

### Operational Considerations

Site readiness checks shall provide actionable blockers for implementation and support teams.

### Non-Functional Considerations

Activation shall be reliable, auditable, secure, performant, and consistent across downstream Site operations.

### Assumptions

- Site activation requires active parent Facility.
- Site add-on licensing may be required depending on subscription entitlement.
- Activation does not create staff accounts or customer records.

### Success Criteria

Only complete, governed, and entitled Sites become Active and eligible for local operations.

### Related Functional Requirements

- FR-SIT-001 - Create Site
- FR-SIT-003 - Configure Site Settings
- FR-SIT-004 - Configure Site Operating Hours
- FR-SIT-005 - Configure Site Capacity Limits
- FR-SIT-011 - Manage Site Policies
- FR-LIC-001 - Manage License Allocation

### Notes

Site activation is the branch-level readiness checkpoint.

---

## FR-SIT-008 - Suspend Site

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-SIT-008 |
| Requirement Name | Suspend Site |
| Functional Module | Site Management |
| Business Domain | Site |
| Business Capability | Site Lifecycle |
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
| Business Requirement | BA-08 Site Management |
| Business Rule | BA-02 BR-SIT-004, BR-SIT-009, BR-SIT-010, BR-FAC-006, BR-ORG-010, BR-SEC-004 |
| Business Process | BA-03 BP-SIT-008 Suspend Site |
| Business Process Flow | BA-04 Section 11 Site Management Flow |
| Persona | BA-05 Organization Administrator, Facility Manager, Site Administrator |
| User Journey | BA-06 Section 6 Site Administrator Journey |
| Stakeholder | BA-07 Organization Administrator, Facility Manager, Site Administrator, Support Executive |
| Non-Functional Requirement | BA-09 Section 3 Security Requirements, Section 5 Business Continuity |
| Assumption / Constraint / Risk | BA-10 BA-RSK-004, BA-RSK-005 |

### Purpose

To temporarily restrict local Site operations while preserving historical Site records and reporting visibility.

### Functional Requirement

The system shall allow an Organization Administrator to suspend an Active Site, restrict new local operational transactions, notify stakeholders, and retain historical records.

### Business Justification

Site suspension supports temporary branch closure due to maintenance, safety, staffing, local compliance, or operational disruptions without impacting the parent Facility lifecycle.

### Actors

- Organization Administrator
- Facility Manager
- Site Administrator
- Notification Service
- Audit Service
- Reporting Service

### Preconditions

- Site exists.
- Site is Active.
- User is authenticated.
- User has Site suspension permission.
- Suspension reason is available.

### Trigger

Organization Administrator selects Suspend Site from Site lifecycle actions.

### In Scope

- Validate suspension eligibility.
- Capture suspension reason.
- Change Site status to Suspended.
- Restrict new local transactions.
- Preserve historical data and reporting access.
- Notify stakeholders and record audit events.

### Out of Scope

- Facility suspension.
- Site archival.
- Refund or membership cancellation.
- Customer communication outside configured notifications.
- Emergency incident management.

### Inputs

- Site ID
- Suspension reason
- Suspension category
- Effective date and time
- Local customer-facing message, if applicable
- Internal notes

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Site ID | Site to suspend | Identifier | Yes | Organization Administrator | Must exist and be Active | Primary context |
| Suspension Reason | Explanation for suspension | Text | Yes | Organization Administrator | Required and length validation | Audit field |
| Suspension Category | Local suspension type | Enum | Yes | Organization Administrator | Must use configured category | Reporting dimension |
| Effective DateTime | Effective timestamp | DateTime | Yes | Organization Administrator / System | Current or future as policy allows | Immediate by default |
| Customer Message | Optional local message | Text | No | Organization Administrator | Content policy validation | Used by Notification module |
| Internal Notes | Restricted operational notes | Text | No | Organization Administrator | Length validation | Internal use |

### Main Flow

1. Organization Administrator opens Site lifecycle actions.
2. Organization Administrator selects Suspend Site.
3. The system validates Site status, permission, Facility scope, and suspension eligibility.
4. Organization Administrator enters reason, category, effective time, and optional messages.
5. The system displays impact on local attendance, schedules, bookings, and reporting.
6. Organization Administrator confirms suspension.
7. The system changes Site status to Suspended immediately or schedules suspension.
8. The system restricts new local operational transactions.
9. The system sends notifications.
10. The system records audit events and updates dashboards.

### Alternate Flows

- If suspension is scheduled, the Site remains Active until effective timestamp.
- If limited read-only access is permitted, historical records remain visible.
- If parent Facility is suspended, the Site may inherit operational restriction.

### Exception Flows

- If Site is not Active, suspension is blocked.
- If reason is missing, confirmation is blocked.
- If impact evaluation fails, suspension is paused until impact can be assessed.
- If status update fails, Site remains Active and error is logged.

### Outputs

- Site status changed to Suspended or scheduled.
- Local operational restrictions applied.
- Notifications.
- Audit events.
- Updated dashboards and reports.

### UI Behaviour

Suspend Site shall require reason capture, impact review, and explicit confirmation. Suspended Sites shall display status badges and restricted action messaging in Site operational screens.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-SIT-701 | Site must be Active to suspend. | Block suspension. | Critical |
| VAL-SIT-702 | Suspension reason is mandatory. | Block confirmation. | Critical |
| VAL-SIT-703 | User must have Site suspension permission. | Deny action and log event. | Critical |
| VAL-SIT-704 | Suspension must preserve historical records. | Prevent destructive operation. | Critical |
| VAL-SIT-705 | Suspension shall not automatically suspend parent Facility. | Preserve Facility status. | High |

### Business Rules

- BA-02 BR-SIT-004 - Site Operational Status
- BA-02 BR-SIT-009 - Site Closure
- BA-02 BR-SIT-010 - Historical Records
- BA-02 BR-FAC-006 - Facility Status
- BA-02 BR-ORG-010 - Organization Audit Trail
- BA-02 BR-SEC-004 - Organization Data Isolation

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| site.lifecycle.view | Organization Administrator, Facility Manager, Site Administrator | Read | Required to view lifecycle |
| site.lifecycle.suspend | Organization Administrator | Execute | Required to suspend Site |
| site.suspension.impact.view | Organization Administrator, Facility Manager | Read | Required to view impact |
| site.suspended.view | Authorized user | Read | Limited access after suspension |

### Security Considerations

Suspension shall restrict local operational access while preserving secure historical visibility. Scope enforcement shall prevent Site suspension from affecting unrelated Sites or parent Facility status except through explicit parent lifecycle processes.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Site Suspended | Facility Manager, Site Administrator | In-App, Email | Site status becomes Suspended | Include reason category and effective date |
| Site Suspension Scheduled | Site Administrator | In-App, Email | Future suspension scheduled | Include effective timestamp |
| Site Suspension Completed | Organization Administrator | In-App, Email | Suspension succeeds | Include Site status |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| SiteSuspensionRequested | Site Management | Audit Service |
| SiteSuspended | Site Management | Attendance Management, Activity Management, Reporting Service |
| SiteSuspensionScheduled | Site Management | Scheduler, Notification Service |

### Audit Events

| Audit Event | Trigger | Actor | Entity | Data Captured |
|---|---|---|---|---|
| Site Suspension Requested | Suspension initiated | Organization Administrator | Site | Reason, category, effective date |
| Site Suspended | Status changed | Organization Administrator or System | Site | Previous status, new status, timestamp |
| Site Suspension Impact Viewed | Impact summary opened | Authorized user | Site | Impact categories and actor |

### Reports Generated

- Site Status Report
- Site Summary Report
- Suspension Audit Report
- Site Dashboard

### Related Screens

- Site Lifecycle
- Suspension Confirmation
- Site Dashboard
- Site Profile
- Audit History

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/sites/{siteId}/suspension-impact | GET | Authorized token | Retrieve suspension impact | 200 OK with impact summary |
| /api/v1/sites/{siteId}/suspend | POST | Organization Administrator token | Suspend Site | 200 OK with suspended status |
| /api/v1/sites/{siteId} | GET | Authorized token | Retrieve Site status | 200 OK with Site resource |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Site | Read, Update | Update lifecycle status | Primary entity |
| Facility | Read | Validate parent scope | Parent context |
| Site Policy | Read | Determine restriction behavior | Governance |
| Audit Log | Insert | Record suspension actions | Required |
| Notification | Insert | Queue suspension notices | Required |
| Dashboard | Update | Reflect suspended status | Reporting context |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Active | Suspend Site | Suspended | Organization Administrator | Valid reason and confirmation |
| Active | Schedule suspension | Active with Scheduled Suspension | Organization Administrator | Future effective timestamp |
| Active with Scheduled Suspension | Effective time reached | Suspended | System | Schedule due |
| Draft | Suspend Site | Draft | Organization Administrator | Action blocked |
| Archived | Suspend Site | Archived | Organization Administrator | Action blocked |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| SIT-701 | Only Active Sites can be suspended. | Invalid lifecycle state | Review Site status |
| SIT-702 | Suspension reason is required. | Missing reason | Enter suspension reason |
| SIT-703 | You do not have permission to suspend this Site. | Missing permission | Request access |
| SIT-704 | Site suspension could not be completed. | Status update failure | Retry or contact support |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Suspend Active Site | Given Site is Active and user has permission | When suspension is confirmed | Then Site status shall become Suspended |
| Do not suspend Facility | Given a Site is suspended | When lifecycle update completes | Then parent Facility status shall remain unchanged |
| Restrict local operations | Given Site is Suspended | When new local transactions are attempted | Then the system shall restrict them by policy |
| Audit suspension | Given suspension completes | When transaction finishes | Then lifecycle audit details shall be recorded |

### Dependencies

- Site lifecycle model
- Facility Management
- Attendance Management
- Activity and Batch Management
- Notification Service
- Audit Service

### Operational Considerations

Suspension impact shall show local operational effects without implying Facility-wide closure.

### Non-Functional Considerations

Site suspension shall be reliable, auditable, secure, and consistently enforced across local modules.

### Assumptions

- Suspension is temporary and preserves Site history.
- Site suspension does not automatically suspend Facility.
- Restricted operations are policy-driven.

### Success Criteria

Site operations are safely restricted while local history, reporting, and auditability remain intact.

### Related Functional Requirements

- FR-SIT-007 - Activate Site
- FR-SIT-009 - Archive Site
- FR-SIT-010 - View Site Dashboard
- FR-AUD-001 - Record Audit Events

### Notes

Site suspension is branch-specific and does not close the parent Facility.

---

## FR-SIT-009 - Archive Site

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-SIT-009 |
| Requirement Name | Archive Site |
| Functional Module | Site Management |
| Business Domain | Site |
| Business Capability | Site Lifecycle |
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
| Business Requirement | BA-08 Site Management |
| Business Rule | BA-02 BR-SIT-004, BR-SIT-009, BR-SIT-010, BR-FAC-006, BR-ORG-010, BR-AUD-008 |
| Business Process | BA-03 BP-SIT-009 Archive Site |
| Business Process Flow | BA-04 Section 11 Site Management Flow |
| Persona | BA-05 Organization Administrator, Facility Manager, Site Administrator |
| User Journey | BA-06 Section 6 Site Administrator Journey |
| Stakeholder | BA-07 Organization Administrator, Facility Manager, Site Administrator, External Auditor |
| Non-Functional Requirement | BA-09 Section 4.5 Data Retention, Section 10 Data Management |
| Assumption / Constraint / Risk | BA-10 BA-RSK-007, BA-CON-004 |

### Purpose

To retire a Site from operational use while retaining all historical operational, attendance, billing, compliance, and audit records.

### Functional Requirement

The system shall allow an Organization Administrator to archive an eligible Site after validating closure constraints, restricting operational actions, preserving historical records, and recording audit events.

### Business Justification

Site archival supports branch closure without deleting history or automatically closing the parent Facility, preserving reporting and compliance continuity.

### Actors

- Organization Administrator
- Facility Manager
- Site Administrator
- Reporting Service
- Notification Service
- Audit Service

### Preconditions

- Site exists.
- Site is not already Archived.
- User is authenticated.
- User has Site archive permission.
- Archival eligibility checks and retention rules are configured.

### Trigger

Organization Administrator selects Archive Site from Site lifecycle actions.

### In Scope

- Validate archive eligibility.
- Capture archive reason.
- Change Site status to Archived.
- Restrict local operational actions.
- Preserve historical records.
- Notify stakeholders and record audit events.

### Out of Scope

- Facility archival.
- Physical data deletion.
- Data purging.
- Financial settlement.
- Subscription or license cancellation.
- Customer membership cancellation.

### Inputs

- Site ID
- Archive reason
- Archive category
- Effective date and time
- Archival confirmation
- Internal notes

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Site ID | Site to archive | Identifier | Yes | Organization Administrator | Must exist and not be Archived | Primary context |
| Archive Reason | Reason for archival | Text | Yes | Organization Administrator | Required and length validation | Audit field |
| Archive Category | Closure category | Enum | Yes | Organization Administrator | Must use configured category | Reporting dimension |
| Effective DateTime | Archive effective timestamp | DateTime | Yes | Organization Administrator / System | Must satisfy policy | Immediate by default |
| Archival Confirmation | Explicit confirmation | Boolean | Yes | Organization Administrator | Must be confirmed | High-risk control |
| Internal Notes | Restricted notes | Text | No | Organization Administrator | Length validation | Internal visibility |

### Main Flow

1. Organization Administrator opens Site lifecycle actions.
2. Organization Administrator selects Archive Site.
3. The system validates Site status, permission, active attendance, bookings, local schedules, financial dependencies, and retention constraints.
4. The system displays archival impact and unresolved blockers.
5. Organization Administrator enters archive reason and confirms archival.
6. The system changes Site status to Archived.
7. The system blocks new local operational actions.
8. The system preserves historical records for reporting and audit.
9. The system sends archival notifications.
10. The system records audit events and updates dashboards.

### Alternate Flows

- If archival is scheduled, the Site remains in current status until effective timestamp.
- If unresolved blockers exist, archival is blocked and remediation guidance is displayed.
- If read-only access is permitted, authorized users may view historical Site data.

### Exception Flows

- If Site is already Archived, duplicate archival is blocked.
- If active operational dependencies prevent archival, archival is blocked.
- If the user lacks permission, the action is denied and logged.
- If archival execution fails, the Site remains in prior state and error is logged.

### Outputs

- Site status changed to Archived or archival blocked.
- Local operational actions restricted.
- Historical records preserved.
- Notifications.
- Audit events.
- Updated dashboards and reports.

### UI Behaviour

Archive Site shall display high-risk confirmation, impact summary, unresolved blockers, retention notice, and read-only implications. Archived Sites shall show read-only indicators.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-SIT-801 | Site must not already be Archived. | Block duplicate archival. | Critical |
| VAL-SIT-802 | Active dependencies must be resolved before archival where required. | Block archival and list blockers. | Critical |
| VAL-SIT-803 | Archive reason and confirmation are mandatory. | Block archival. | Critical |
| VAL-SIT-804 | Site archival shall not automatically close parent Facility. | Preserve Facility status. | Critical |
| VAL-SIT-805 | Historical records must be retained. | Prevent destructive operations. | Critical |

### Business Rules

- BA-02 BR-SIT-004 - Site Operational Status
- BA-02 BR-SIT-009 - Site Closure
- BA-02 BR-SIT-010 - Historical Records
- BA-02 BR-FAC-006 - Facility Status
- BA-02 BR-ORG-010 - Organization Audit Trail
- BA-02 BR-AUD-008 - Cross-Module Traceability

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| site.lifecycle.view | Organization Administrator, Facility Manager, Site Administrator | Read | Required to view lifecycle |
| site.lifecycle.archive | Organization Administrator | Execute | Required to archive Site |
| site.archive.impact.view | Organization Administrator, Facility Manager | Read | Required to view archive impact |
| site.archived.view | Authorized user | Read | Read-only archived access |

### Security Considerations

Site archival shall enforce Site scope, high-risk confirmation, role-based access, retention policy, and read-only controls. Archived Site data shall remain protected.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Site Archived | Facility Manager, Site Administrator | In-App, Email | Site status becomes Archived | Include archive date and reason category |
| Site Archive Blocked | Organization Administrator | In-App | Eligibility checks fail | Include blockers |
| Site Archive Scheduled | Facility Manager, Site Administrator | In-App, Email | Future archival scheduled | Include effective timestamp |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| SiteArchiveRequested | Site Management | Audit Service |
| SiteArchived | Site Management | Facility Management, Reporting Service, Audit Service, Notification Service |
| SiteArchiveBlocked | Site Management | Notification Service, Audit Service |

### Audit Events

| Audit Event | Trigger | Actor | Entity | Data Captured |
|---|---|---|---|---|
| Site Archive Eligibility Checked | Eligibility validation executed | Organization Administrator | Site | Eligibility result and blockers |
| Site Archived | Status changed to Archived | Organization Administrator or System | Site | Previous status, new status, reason |
| Archived Site Viewed | Archived record opened | Authorized user | Site | Actor, timestamp, purpose context |

### Reports Generated

- Site Status Report
- Archived Site Register
- Site Summary Report
- Audit Trail Report

### Related Screens

- Site Lifecycle
- Archive Confirmation
- Site Dashboard
- Archived Site Detail
- Audit History

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/sites/{siteId}/archive-impact | GET | Authorized token | Retrieve archive impact | 200 OK with impact summary |
| /api/v1/sites/{siteId}/archive | POST | Organization Administrator token | Archive Site | 200 OK with archived status |
| /api/v1/sites/{siteId} | GET | Authorized token | Retrieve Site details | 200 OK with Site resource |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Site | Read, Update | Update lifecycle status | Primary entity |
| Facility | Read | Preserve parent Facility relationship | Parent context |
| Site Settings | Read | Preserve configuration history | Read-only after archival |
| Site Capacity | Read | Preserve local capacity history | Read-only after archival |
| Site Operating Hours | Read | Preserve local schedule history | Read-only after archival |
| Site Documents | Read | Preserve compliance records | Retention applies |
| Audit Log | Insert | Record archival events | Required |
| Notification | Insert | Queue archival notices | Required |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Draft | Archive Site | Archived | Organization Administrator | Eligibility checks pass |
| Active | Archive Site | Archived | Organization Administrator | Eligibility checks pass |
| Suspended | Archive Site | Archived | Organization Administrator | Eligibility checks pass |
| Active | Archive blocked | Active | System | Active dependencies prevent archival |
| Archived | Archive Site | Archived | Organization Administrator | Duplicate action blocked |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| SIT-801 | Site cannot be archived because blockers exist. | Eligibility checks failed | Resolve listed blockers |
| SIT-802 | Site is already archived. | Duplicate action | No action required |
| SIT-803 | Archive reason is required. | Missing reason | Enter archive reason |
| SIT-804 | You do not have permission to archive this Site. | Missing permission | Request access |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Archive eligible Site | Given Site passes archival checks | When Organization Administrator confirms archival | Then Site status shall become Archived |
| Do not close Facility | Given Site is archived | When lifecycle update completes | Then parent Facility status shall remain unchanged |
| Preserve history | Given archival succeeds | When authorized users view history | Then historical records shall be read-only and available |
| Audit archive | Given archival is attempted | When action completes or fails | Then audit history shall record the event |

### Dependencies

- Site lifecycle model
- Facility Management
- Attendance Management
- Billing and Payment Management
- Data retention policy
- Notification Service
- Audit Service

### Operational Considerations

Archival blockers and retention behavior shall be visible for implementation, support, and audit teams.

### Non-Functional Considerations

Site archival shall support compliance, auditability, data retention, security, tenant isolation, and reliable read-only access.

### Assumptions

- Archive is not physical deletion.
- Site archival does not close the parent Facility.
- Historical records remain available according to retention policy.

### Success Criteria

Sites can be retired from branch operations without data loss, Facility disruption, or audit traceability gaps.

### Related Functional Requirements

- FR-SIT-007 - Activate Site
- FR-SIT-008 - Suspend Site
- FR-SIT-010 - View Site Dashboard
- FR-AUD-001 - Record Audit Events
- FR-RPT-001 - Generate Reports

### Notes

Site archival is branch-specific and retains historical operational context.

---

## FR-SIT-010 - View Site Dashboard

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-SIT-010 |
| Requirement Name | View Site Dashboard |
| Functional Module | Site Management |
| Business Domain | Site |
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
| Business Requirement | BA-08 Site Management |
| Business Rule | BA-02 BR-SIT-004, BR-SIT-006, BR-SIT-008, BR-SIT-010, BR-RPT-001, BR-RPT-002, BR-SEC-004 |
| Business Process | BA-03 BP-SIT-010 View Site Dashboard |
| Business Process Flow | BA-04 Section 11 Site Management Flow |
| Persona | BA-05 Site Administrator, Facility Manager, Organization Administrator |
| User Journey | BA-06 Section 6 Site Administrator Journey |
| Stakeholder | BA-07 Site Administrator, Facility Manager, Organization Administrator |
| Non-Functional Requirement | BA-09 Section 6.4 Reporting Performance, Section 11 Reporting Requirements |
| Assumption / Constraint / Risk | BA-10 BA-ASS-006, BA-RSK-004 |

### Purpose

To provide authorized users with a branch-level operational view of attendance, occupancy, schedule, capacity, alerts, and local performance.

### Functional Requirement

The system shall provide a Site Dashboard that displays authorized Site metrics, local alerts, capacity indicators, schedule summaries, and navigation to Site operational functions.

### Business Justification

Site Administrators need branch-specific visibility to manage daily execution, respond to local exceptions, and escalate issues to Facility Managers when required.

### Actors

- Site Administrator
- Facility Manager
- Organization Administrator
- Reception Staff
- Trainer
- Reporting Service
- Audit Service

### Preconditions

- Site exists.
- User is authenticated.
- User has Site dashboard permission.
- User scope includes the Site.
- Reporting data sources are available.

### Trigger

Authorized user opens Site Dashboard or receives a local operational notification.

### In Scope

- Display Site lifecycle status.
- Display local attendance, occupancy, capacity, schedule, activity, and alert metrics.
- Apply role-based visibility.
- Support filters and refresh.
- Record dashboard access audit events.

### Out of Scope

- Facility-wide dashboard.
- Organization-wide reporting.
- Detailed report builder.
- Transaction correction workflow.
- Predictive analytics.

### Inputs

- Site ID
- User role and permission scope
- Date range
- Activity or batch filter
- Attendance filter
- Refresh request

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Site ID | Dashboard Site context | Identifier | Yes | User session / selection | Must match authorized scope | Site boundary |
| Date Range | Reporting period | Date Range | Yes | User or default | Must be valid and within limits | Used by widgets |
| Activity Filter | Optional activity filter | Identifier | No | User | Must belong to Site context | Used for drill-down |
| Batch Filter | Optional batch filter | Identifier | No | User | Must belong to Site context | Used for schedule widgets |
| Metric Type | Widget category | Enum | No | System / User | Must be supported metric | Controls display |
| Refresh Action | Refresh request | Action | No | User | Must respect refresh limits | May use cached data |

### Main Flow

1. Authorized user opens Site Dashboard.
2. The system validates authentication, Site scope, and dashboard permission.
3. The system loads Site lifecycle status, configuration status, operating hours, capacity, and local alerts.
4. The system retrieves branch-level metrics from reporting sources.
5. The system applies role-based visibility, filters, and date range.
6. The system displays widgets for attendance, occupancy, capacity, schedule, alerts, and local performance.
7. User applies filters or refreshes metrics.
8. The system updates dashboard data and displays refresh timestamp.
9. The system records dashboard access and filter audit events.
10. The system provides permission-aware navigation.

### Alternate Flows

- If no data exists, the dashboard shows branch setup or empty-state guidance.
- If user has limited role scope, restricted widgets are hidden or unavailable.
- If cached metrics are used, last refreshed timestamp is displayed.

### Exception Flows

- If user lacks permission, dashboard access is denied.
- If a metric source is unavailable, the widget shows unavailable state without breaking the dashboard.
- If filters produce no results, the dashboard displays empty state.
- If Site is Archived, dashboard opens in read-only historical mode where allowed.

### Outputs

- Site Dashboard.
- Filtered local metrics.
- Operational alerts.
- Capacity indicators.
- Navigation actions.
- Audit events.

### UI Behaviour

Site Dashboard shall prioritize local operational metrics, status badges, branch alerts, capacity warnings, schedule visibility, filter controls, and refresh timestamps. Inherited vs. local configuration status shall be clear.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-SIT-901 | User must have Site dashboard permission. | Deny access and log event. | Critical |
| VAL-SIT-902 | Dashboard data must be limited to authorized Site scope. | Filter data and block unauthorized scope. | Critical |
| VAL-SIT-903 | Date range must be valid and within reporting limits. | Show validation error. | High |
| VAL-SIT-904 | Activity and batch filters must belong to Site scope. | Reject filter and log if unauthorized. | Critical |
| VAL-SIT-905 | Widget failure must not break the full dashboard. | Display widget-level unavailable state. | Medium |

### Business Rules

- BA-02 BR-SIT-004 - Site Operational Status
- BA-02 BR-SIT-006 - Site Capacity
- BA-02 BR-SIT-008 - Site Reporting
- BA-02 BR-SIT-010 - Historical Records
- BA-02 BR-RPT-001 - Report Access Control
- BA-02 BR-RPT-002 - Report Data Scope
- BA-02 BR-SEC-004 - Organization Data Isolation

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| site.dashboard.view | Site Administrator | Read | Site-scoped dashboard |
| site.dashboard.facility-view | Facility Manager | Read | Facility-authorized Site dashboard |
| site.dashboard.organization-view | Organization Administrator | Read | Organization-level access |
| site.dashboard.export | Organization Administrator, Facility Manager | Export | Export where enabled |

### Security Considerations

Dashboard data shall be scoped by Organization, Facility, Site, and role. Sensitive operational and staff information shall be visible only to authorized roles. Dashboard access shall be audited.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Site Warning Available | Site Administrator | In-App | Local warning generated | Include warning category and target |
| Site Capacity Alert | Facility Manager, Site Administrator | In-App, Email | Capacity threshold reached | Include current usage |
| Site Reporting Data Unavailable | Site Administrator | In-App | Metric source unavailable | Include affected widget |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| SiteDashboardViewed | Site Management | Audit Service |
| SiteDashboardFiltered | Site Management | Reporting Service |
| SiteOperationalAlertDisplayed | Reporting Service | Notification Service, Audit Service |

### Audit Events

| Audit Event | Trigger | Actor | Entity | Data Captured |
|---|---|---|---|---|
| Site Dashboard Viewed | Dashboard opened | Authorized user | Dashboard | Site ID, actor, role, timestamp |
| Site Dashboard Filter Applied | Filter changed | Authorized user | Dashboard | Filter values and date range |
| Site Dashboard Restricted Access Attempted | Unauthorized scope requested | User | Dashboard | Requested scope and actor |

### Reports Generated

- Site Dashboard
- Site Summary Report
- Site Capacity Report
- Attendance Summary Report
- Activity Performance Report

### Related Screens

- Site Dashboard
- Site Settings
- Site Operating Hours
- Site Capacity
- Attendance Summary
- Reports & Analytics

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/sites/{siteId}/dashboard | GET | Authorized token | Retrieve Site dashboard summary | 200 OK with dashboard metrics |
| /api/v1/sites/{siteId}/dashboard/widgets | GET | Authorized token | Retrieve available widgets | 200 OK with widget list |
| /api/v1/sites/{siteId}/dashboard/alerts | GET | Authorized token | Retrieve Site alerts | 200 OK with alert list |
| /api/v1/sites/{siteId}/dashboard/refresh | POST | Authorized token | Request dashboard refresh | 202 Accepted with refresh status |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Site | Read | Display profile and lifecycle context | Parent context |
| Site Settings | Read | Apply dashboard preferences | Configuration source |
| Site Capacity | Read | Display capacity metrics | Operational metric |
| Site Operating Hours | Read | Display schedule context | Operational metric |
| Dashboard | Read | Retrieve widget definitions | Reporting context |
| Audit Log | Insert | Record dashboard activity | Required |
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
| SIT-901 | You do not have permission to view this Site dashboard. | Missing permission or invalid scope | Request access |
| SIT-902 | Selected date range is not valid. | Invalid filter | Select a valid date range |
| SIT-903 | Selected filter is outside Site scope. | Unauthorized filter | Choose an authorized filter |
| SIT-904 | Some Site dashboard data is temporarily unavailable. | Reporting source issue | Retry later |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| View dashboard | Given user has Site dashboard permission | When they open Site Dashboard | Then the system shall display authorized Site metrics |
| Enforce Site scope | Given user is not assigned to the Site | When dashboard is requested | Then access shall be denied and logged |
| Show local alerts | Given Site alerts exist | When dashboard loads | Then alert indicators shall be displayed |
| Handle widget outage | Given one metric source is unavailable | When dashboard loads | Then available widgets shall still render |

### Dependencies

- Reporting Service
- Site Settings
- Site Capacity
- Site Operating Hours
- Attendance Management data
- Activity and Batch Management data
- Audit Service

### Operational Considerations

Dashboard widget failures shall be logged independently and should not prevent users from viewing available local metrics.

### Non-Functional Considerations

Site Dashboard shall support reporting performance, availability, usability, accessibility, secure data scoping, and scalable branch monitoring.

### Assumptions

- Site metrics are derived from operational and reporting data sources.
- Some metrics may be cached for performance.
- Site Administrator access is branch-scoped.

### Success Criteria

Site Administrators can monitor local attendance, occupancy, schedule, alerts, and branch health from one dashboard.

### Related Functional Requirements

- FR-SIT-003 - Configure Site Settings
- FR-SIT-004 - Configure Site Operating Hours
- FR-SIT-005 - Configure Site Capacity Limits
- FR-RPT-001 - Generate Reports
- FR-AUD-001 - Record Audit Events

### Notes

The Site Dashboard is branch-focused and constrained by inherited Facility governance.

---

## FR-SIT-011 - Manage Site Policies

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-SIT-011 |
| Requirement Name | Manage Site Policies |
| Functional Module | Site Management |
| Business Domain | Site |
| Business Capability | Site Configuration |
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
| Business Requirement | BA-08 Site Management |
| Business Rule | BA-02 BR-SIT-001, BR-SIT-004, BR-SIT-006, BR-SIT-009, BR-FAC-004, BR-FAC-005, BR-ORG-004 |
| Business Process | BA-03 BP-SIT-011 Manage Site Policies |
| Business Process Flow | BA-04 Section 11 Site Management Flow |
| Persona | BA-05 Organization Administrator, Facility Manager, Site Administrator |
| User Journey | BA-06 Section 6 Site Administrator Journey |
| Stakeholder | BA-07 Organization Administrator, Facility Manager, Site Administrator |
| Non-Functional Requirement | BA-09 Section 8.3 Business Rules Configuration |
| Assumption / Constraint / Risk | BA-10 BA-ASS-006, BA-RSK-004 |

### Purpose

To configure approved Site-level operational policies while preserving Facility and Organization governance.

### Functional Requirement

The system shall allow authorized users to create, update, schedule, publish, inherit, and audit Site Policies for local safety, emergency procedures, visitor rules, equipment usage, holidays, and operational rules.

### Business Justification

Site Policies allow branches to address local operational realities without compromising Facility-level standards, Organization governance, or platform consistency.

### Actors

- Organization Administrator
- Facility Manager
- Site Administrator
- Approval Workflow Service
- Notification Service
- Audit Service

### Preconditions

- Site exists.
- Site is not Archived.
- Parent Facility policies are available.
- User is authenticated.
- User has Site policy permission.
- Facility and Organization policies allow Site-level policy configuration.

### Trigger

Authorized user opens Site Policies and submits policy creation, update, schedule, publish, or inheritance change.

### In Scope

- View inherited Facility policies.
- Configure Site-level policy overrides.
- Validate policy precedence and constraints.
- Manage effective and expiry dates.
- Route governed policies for approval.
- Publish policies to local operational modules.
- Record notifications and audit events.

### Out of Scope

- Facility Policy management.
- Organization Policy management.
- Platform policy definition.
- Execution of transactions governed by policies.
- Legal drafting outside system configuration.

### Inputs

- Site ID
- Policy category
- Policy name
- Policy value
- Inheritance mode
- Effective date
- Expiry date
- Override reason
- Approval reference, if required

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Policy Category | Site operational policy category | Master Data | Yes | System | Must be allowed at Site level | Examples include safety and visitor rules |
| Policy Name | Specific policy identifier | Master Data | Yes | System | Must be active and configurable | Defined by parent policy model |
| Policy Value | Local policy value | Configuration | Conditional | Authorized user | Must match data type and constraints | Required for override |
| Inheritance Mode | Inherit Facility policy or override locally | Enum | Yes | Authorized user | Override must be permitted | Controls precedence |
| Effective Date | Policy activation date | Date | Yes | Authorized user | Must satisfy date rules | Supports scheduling |
| Expiry Date | Policy expiry date | Date | No | Authorized user | Must be after effective date | Optional |
| Override Reason | Reason for local policy override | Text | Conditional | Authorized user | Required for override | Audit field |

### Main Flow

1. Authorized user opens Site Policies.
2. The system loads Facility policies, current Site policies, inheritance state, and policy constraints.
3. User selects policy category and action.
4. User enters policy value, inheritance mode, effective dates, and override reason where required.
5. The system validates policy value, Facility and Organization constraints, precedence, dates, Site status, and approval requirements.
6. If approval is required, the system creates an approval request.
7. If approval is not required, or after approval is granted, the system saves or publishes the Site Policy.
8. The system publishes local policy context to Site operational modules.
9. The system updates configuration reports and dashboard indicators.
10. The system records audit events and sends notifications.

### Alternate Flows

- If policy inherits from Facility, the system stores inherited state without local value.
- If policy is future-dated, the system schedules publication.
- If a local policy expires, the system reverts to inherited Facility policy.
- If override is removed, the system uses the parent Facility policy immediately or from effective date.

### Exception Flows

- If policy violates Facility or Organization rules, save is blocked.
- If override is not permitted, the system blocks local policy configuration.
- If effective dates conflict, publication is blocked.
- If approval is rejected, existing policy remains active.
- If publication fails, failure status is logged and visible.

### Outputs

- Created or updated Site Policy.
- Inheritance or override status.
- Policy publication status.
- Approval request, if applicable.
- Notifications and audit events.
- Updated reports and dashboards.

### UI Behaviour

Site Policies shall display inherited Facility policy, local override status, effective dates, approval status, local impact, and publication state. Active, draft, scheduled, expired, rejected, inherited, and overridden policies shall be visually distinct.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-SIT-1001 | Site Policy must remain within Facility and Organization constraints. | Block save and show constraint. | Critical |
| VAL-SIT-1002 | Local policy override requires permission and reason. | Block save or route approval. | High |
| VAL-SIT-1003 | Effective periods must not conflict for the same policy. | Block publication. | High |
| VAL-SIT-1004 | Governed policy changes require approval. | Submit approval or block if route unavailable. | High |
| VAL-SIT-1005 | Archived Sites cannot publish policy changes. | Block publication. | Critical |

### Business Rules

- BA-02 BR-SIT-001 - Site Ownership
- BA-02 BR-SIT-004 - Site Operational Status
- BA-02 BR-SIT-006 - Site Capacity
- BA-02 BR-SIT-009 - Site Closure
- BA-02 BR-FAC-004 - Facility Capacity
- BA-02 BR-FAC-005 - Facility Operating Hours
- BA-02 BR-ORG-004 - Organization Policies

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| site.policies.view | Organization Administrator, Facility Manager, Site Administrator | Read | Required to view Site Policies |
| site.policies.update | Organization Administrator | Update | Full policy configuration |
| site.policies.maintain | Facility Manager, Site Administrator | Update | Limited local maintenance |
| site.policies.approve | Authorized Approver | Approve | Required for governed policies |
| site.policies.publish | Authorized user / System | Execute | Required to publish policies |

### Security Considerations

Site Policy changes shall be permission-controlled, Site-scoped, tenant-isolated, and auditable. Policies affecting safety, access, or customer operations may require approval.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Site Policy Updated | Facility Manager, Site Administrator | In-App, Email | Policy saved or published | Include policy category and effective date |
| Site Policy Approval Required | Approver | In-App, Email | Governed policy submitted | Include override reason and impact |
| Site Policy Published | Site Administrator | In-App | Policy becomes effective | Include affected local operations |
| Site Policy Expired | Facility Manager, Site Administrator | In-App | Expiry reached | Include fallback policy source |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| SitePolicyUpdated | Site Management | Audit Service, Reporting Service |
| SitePolicyApprovalRequested | Site Management | Approval Workflow Service |
| SitePolicyPublished | Site Management | Attendance Management, Activity Management, Notification Service |
| SitePolicyExpired | Scheduler | Site Management, Notification Service |

### Audit Events

| Audit Event | Trigger | Actor | Entity | Data Captured |
|---|---|---|---|---|
| Site Policy Viewed | Policy screen opened | Authorized user | Site Policy | Site ID, actor, timestamp |
| Site Policy Modified | Policy saved | Authorized user | Site Policy | Previous value, new value, source, reason |
| Site Policy Published | Policy becomes effective | Authorized user / System | Site Policy | Policy version, scope, publication result |
| Site Policy Approval Completed | Approval decision recorded | Approver | Approval Request | Decision, comments, timestamp |

### Reports Generated

- Site Policy Report
- Site Configuration Report
- Configuration Change Report
- Audit Trail Report

### Related Screens

- Site Policies
- Site Settings
- Policy Impact Summary
- Approval Request
- Audit History

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/sites/{siteId}/policies | GET | Authorized token | Retrieve Site Policies | 200 OK with policy list |
| /api/v1/sites/{siteId}/policies | POST | Authorized token | Create Site Policy | 201 Created with policy resource |
| /api/v1/sites/{siteId}/policies/{policyId} | PATCH | Authorized token | Update Site Policy | 200 OK with updated policy |
| /api/v1/sites/{siteId}/policies/{policyId}/publish | POST | Authorized token | Publish Site Policy | 202 Accepted with publication status |
| /api/v1/sites/{siteId}/policies/{policyId}/impact | POST | Authorized token | Evaluate policy impact | 200 OK with impact summary |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Site | Read | Validate scope and lifecycle | Parent context |
| Site Policy | Create, Read, Update | Store Site policy configuration | Primary entity |
| Facility Policy | Read | Provide inherited policy and constraints | Parent source |
| Business Policies | Read | Validate Organization policy boundary | Governance |
| Approval Request | Insert, Update | Manage governed policy changes | Conditional |
| Audit Log | Insert | Record policy changes | Required |
| Notification | Insert | Queue policy notifications | Conditional |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Inherited | Create local policy | Draft | Authorized user | Override allowed |
| Draft | Submit policy | Pending Approval | Authorized user | Approval required |
| Draft | Publish policy | Active | Authorized user | No approval required and effective now |
| Pending Approval | Approve policy | Scheduled or Active | Authorized Approver | Approval granted |
| Pending Approval | Reject policy | Rejected | Authorized Approver | Existing policy retained |
| Active | Expiry reached | Expired | System | Expiry date configured |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| SIT-1001 | Site Policy violates Facility policy. | Parent policy constraint | Select allowed value |
| SIT-1002 | Local policy override is not permitted. | Override disabled | Use inherited policy |
| SIT-1003 | Policy effective date conflicts with another policy. | Date overlap | Adjust effective date |
| SIT-1004 | Site Policy requires approval before activation. | Governed change | Submit for approval |
| SIT-1005 | Site Policy could not be published. | Publication failure | Review status or contact support |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Configure valid Site policy | Given user has Site policy permission | When valid policy values are submitted | Then the system shall save or publish the policy |
| Enforce Facility boundary | Given policy violates Facility constraint | When save is attempted | Then the system shall block the policy |
| Route approval | Given policy requires approval | When submitted | Then the system shall create an approval request |
| Revert to inherited | Given local policy exists | When user removes override | Then Site shall use inherited Facility policy |

### Dependencies

- Facility Policy
- Organization policy
- Approval Workflow Service
- Notification Service
- Audit Service
- Attendance and Activity modules

### Operational Considerations

Policy inheritance and override status shall be visible for support and implementation teams investigating local branch behavior.

### Non-Functional Considerations

Site Policy management shall support configurability, maintainability, auditability, reliable publication, and scalable branch governance.

### Assumptions

- Facility policy determines whether Site-level overrides are allowed.
- Downstream modules consume published Site Policy context.
- Archived Sites cannot publish policy changes.

### Success Criteria

Site Policies are configured within governance boundaries, published reliably, inherited correctly, and auditable.

### Related Functional Requirements

- FR-FAC-012 - Manage Facility Policies
- FR-SIT-003 - Configure Site Settings
- FR-SIT-004 - Configure Site Operating Hours
- FR-SIT-005 - Configure Site Capacity Limits
- FR-SIT-010 - View Site Dashboard

### Notes

Site Policies govern local branch behavior and must not bypass Facility or Organization governance.

---

**End of FR-05 - Site Management**
