# FR-06 User & Role Management

**Document ID:** FR-06  
**Document Name:** User & Role Management Functional Requirements  
**Company:** OreeOn Technologies Pvt. Ltd.  
**Product:** Digitize  
**Document Type:** Functional Requirements  
**Version:** 1.0  
**Status:** Draft  
**Owner:** Product Management  
**Prepared By:** Product Management, Business Analysis, and Solution Architecture  
**Last Updated:** July 2026

---

## FR-USR-001 - Create Staff Account

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-USR-001 |
| Requirement Name | Create Staff Account |
| Functional Module | User & Role Management |
| Business Domain | Staff Identity & Access |
| Business Capability | Identity Management |
| Requirement Type | Functional |
| Requirement Category | Security |
| Requirement Version | 1.0 |
| Requirement Status | Approved |
| Priority | Critical |
| Complexity | High |
| Release Version | 1.0 |
| Owner | Product Management |

### Traceability References

| Traceability Type | Reference |
|---|---|
| Business Requirement | BA-08 BR-006 Staff Account Creation |
| Business Rule | BA-02 BR-ORG-005, BR-ORG-006, BR-SEC-001, BR-SEC-002, BR-SEC-003, BR-SEC-004, BR-AUD-003 |
| Business Process | BA-03 BP-STA-001 Create Staff Account |
| Business Process Flow | BA-04 Section 12 User & Role Management Flow |
| Persona | BA-05 Organization Administrator |
| User Journey | BA-06 Section 4 Organization Administrator Journey |
| Stakeholder | BA-07 Organization Administrator |
| Non-Functional Requirement | BA-09 Section 3 Security Requirements |
| Assumption / Constraint / Risk | BA-10 BA-ASS-006, BA-RSK-004 |

### Purpose

To create authenticated internal Staff accounts for users who operate the Digitize platform on behalf of an Organization.

### Functional Requirement

The system shall allow an Organization Administrator to create a Staff Account with identity, contact, role readiness, access scope readiness, credential setup, lifecycle status, notifications, and audit history.

### Business Justification

Staff Accounts are the security foundation for operational execution because only authorized Staff users may access protected platform functions, perform business transactions, and administer Organization, Facility, and Site operations.

### Actors

- Organization Administrator
- Staff User
- Security Service
- Notification Service
- Audit Service
- System

### Preconditions

- Organization exists and is Active.
- Organization Administrator is authenticated.
- Organization Administrator has staff account creation permission.
- Security policies are configured.
- Role definitions are available.
- Staff identity does not already exist within duplicate-prevention rules.

### Trigger

Organization Administrator selects Create Staff Account from Staff Management.

### In Scope

- Capture Staff identity and contact details.
- Validate duplicate staff identity.
- Create Staff Account in Created status.
- Initiate credential setup or invitation.
- Track role and access readiness.
- Send account creation notification.
- Record audit events.

### Out of Scope

- Customer registration.
- Platform Administrator account provisioning.
- Final role assignment where handled separately.
- Facility or Site access assignment where handled separately.
- Payroll, HR, or employment contract management.

### Inputs

- Organization ID
- Staff full name
- Staff email address
- Staff mobile number
- Username
- Staff designation
- Initial role reference, if provided
- Initial Facility or Site assignment, if provided
- Invitation preference

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Organization ID | Owning Organization | Identifier | Yes | System | Must be Active and within administrator scope | Staff belongs to one Organization |
| Staff Name | Full staff name | Text | Yes | Organization Administrator | Required and length validation | Used in directory |
| Email Address | Staff email | Email | Yes | Organization Administrator | Valid format and duplicate check | Used for login or invitation |
| Mobile Number | Staff mobile number | Phone | Conditional | Organization Administrator | Valid format and duplicate check where configured | May be used for login or notification |
| Username | Staff login name | Text | Conditional | Organization Administrator / System | Must be unique where username login is enabled | May be generated |
| Designation | Business designation | Text | No | Organization Administrator | Length validation | Informational |
| Account Status | Lifecycle status | Enum | Yes | System | Must be Created at account creation | Activation handled separately |

### Main Flow

1. Organization Administrator opens Create Staff Account.
2. The system loads Organization context, security policy, and role definitions.
3. Organization Administrator enters Staff identity and contact details.
4. The system validates required fields, duplicate identity, contact formats, Organization scope, and security policy.
5. The system creates the Staff Account in Created status.
6. The system records initial role and access readiness status.
7. The system initiates credential setup or invitation according to security policy.
8. The system sends Staff Account Created notification.
9. The system records audit events.
10. The system displays Staff Account summary.

### Alternate Flows

- If initial role is provided, the system may create the account and route role assignment through role validation.
- If invitation is deferred, the account remains Created without active credentials.
- If mobile login is disabled, mobile number is retained for communication only.

### Exception Flows

- If duplicate Staff identity exists, account creation is blocked.
- If Organization is not Active, account creation is blocked.
- If credential invitation fails, Staff Account remains Created and the failure is logged.
- If user lacks permission, the system denies access and records a security event.

### Outputs

- Staff Account created.
- Staff profile created.
- Account status set to Created.
- Credential setup or invitation initiated.
- Notification generated.
- Audit events recorded.

### UI Behaviour

The Create Staff Account screen shall display identity, contact, security, and optional access setup sections. Save shall remain disabled until mandatory fields are valid. Duplicate identity warnings shall be shown before submission where possible.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-USR-001 | Staff must belong to exactly one Active Organization. | Block creation. | Critical |
| VAL-USR-002 | Staff name and primary contact are mandatory. | Block save and highlight fields. | Critical |
| VAL-USR-003 | Staff email, mobile, or username must satisfy duplicate-prevention rules. | Block save and show duplicate conflict. | Critical |
| VAL-USR-004 | Account status must be Created at creation. | Reject invalid lifecycle state. | Critical |
| VAL-USR-005 | User must have staff account creation permission. | Deny action and log event. | Critical |

### Business Rules

- BA-02 BR-ORG-005 - Organization Users
- BA-02 BR-ORG-006 - Role-Based Access
- BA-02 BR-SEC-001 - Authentication
- BA-02 BR-SEC-002 - Role-Based Access Control
- BA-02 BR-SEC-003 - Least Privilege
- BA-02 BR-SEC-004 - Organization Data Isolation
- BA-02 BR-AUD-003 - Auditable Events
 - BA-02 BR-SEC-PII-001 - PII Storage: Hashing vs Encryption

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| staff.account.create | Organization Administrator | Create | Required to create Staff Account |
| staff.account.view | Organization Administrator | Read | Required to view created account |
| staff.invitation.send | Organization Administrator / System | Execute | Required to send credential invitation |
| audit.staff.create.read | Organization Administrator | Read | Required to view Staff creation audit |

### Security Considerations

Staff Account creation shall enforce Organization data isolation, RBAC, duplicate identity prevention, secure credential invitation, least privilege, and audit logging. Customers shall not be created through Staff Account flows.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Staff Account Created | Organization Administrator | In-App, Email | Staff Account created | Include staff name and status |
| Staff Invitation Sent | Staff User | Email, SMS | Credential setup initiated | Include secure setup link and expiry |
| Staff Setup Incomplete | Organization Administrator | In-App | Role or access scope missing | Include missing readiness areas |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| StaffAccountCreated | User & Role Management | Audit Service, Notification Service, Reporting Service |
| StaffCredentialInvitationInitiated | User & Role Management | Security Service, Notification Service |
| StaffAccessReadinessInitialized | User & Role Management | Security Service, Audit Service |

### Audit Events

| Audit Event | Trigger | Actor | Entity | Data Captured |
|---|---|---|---|---|
| Staff Account Created | Account creation completed | Organization Administrator | Staff Account | Staff ID, Organization ID, status, contact references |
| Staff Invitation Initiated | Credential setup initiated | Organization Administrator / System | Staff Account | Invitation channel, expiry, outcome |
| Duplicate Staff Creation Blocked | Duplicate detected | Organization Administrator | Staff Account | Submitted identifiers and conflict reason |

### Reports Generated

- Staff Directory Report
- Access Control Report
- Workforce Administration Dashboard
- Security Monitoring Report

### Related Screens

- Staff Management
- Create Staff Account
- Staff Profile
- Staff Directory
- Access Readiness Summary

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/organizations/{organizationId}/staff | POST | Organization Administrator token | Create Staff Account | 201 Created with Staff Account resource |
| /api/v1/staff/{staffId} | GET | Organization Administrator token | Retrieve Staff Account | 200 OK with Staff Account resource |
| /api/v1/staff/{staffId}/invitations | POST | Organization Administrator token | Send credential setup invitation | 202 Accepted with invitation status |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Staff | Create | Store staff business profile | Organization-owned |
| Staff Account | Create | Store authentication account state | Created status |
| Role | Read | Validate available roles | Optional at creation |
| Login History | Initialize | Prepare authentication tracking | Security monitoring |
| Audit Log | Insert | Record account creation | Required |
| Notification | Insert | Queue account notifications | Conditional |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| None | Create Staff Account | Created | Organization Administrator | Valid identity and Organization scope |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| USR-001 | Staff name is required. | Mandatory field missing | Enter staff name |
| USR-002 | Staff account already exists. | Duplicate identity detected | Review existing account |
| USR-003 | Organization is not active for staff creation. | Invalid Organization status | Activate Organization first |
| USR-004 | Staff invitation could not be sent. | Notification or security failure | Retry invitation |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Create Staff Account | Given the Organization is Active and user has permission | When valid staff details are submitted | Then the system shall create Staff Account in Created status |
| Prevent duplicate account | Given duplicate staff identity exists | When account creation is attempted | Then the system shall block creation |
| Send invitation | Given invitation is enabled | When account is created | Then the system shall initiate credential setup notification |
| Record audit | Given Staff Account creation is attempted | When action completes or fails | Then audit history shall record the outcome |

### Dependencies

- Active Organization
- Security policies
- Role definitions
- Notification Service
- Audit Service

### Operational Considerations

Failed credential invitations shall be retryable and visible to Organization Administrators and support teams.

### Non-Functional Considerations

Staff Account creation shall be secure, auditable, tenant-isolated, reliable, and scalable for large Organizations.

### Assumptions

- Customers are not Staff users.
- Staff Accounts belong to one Organization.
- Activation is handled separately after role and access readiness.

### Success Criteria

The Organization can create Staff Accounts with secure identity setup, duplicate prevention, auditability, and readiness tracking.

### Related Functional Requirements

- FR-USR-003 - Assign Staff Role
- FR-USR-004 - Assign Facility Access
- FR-USR-005 - Assign Site Access
- FR-USR-007 - Activate Staff Account

### Notes

Staff Account creation establishes identity but does not guarantee operational access until activation and assignments are complete.

---

## FR-USR-002 - Update Staff Profile

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-USR-002 |
| Requirement Name | Update Staff Profile |
| Functional Module | User & Role Management |
| Business Domain | Staff Identity & Access |
| Business Capability | Identity Management |
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
| Business Requirement | BA-08 Staff Identity & Access |
| Business Rule | BA-02 BR-ORG-005, BR-ORG-006, BR-SEC-004, BR-SEC-008, BR-SEC-009, BR-AUD-003 |
| Business Process | BA-03 BP-STA-002 Update Staff Profile |
| Business Process Flow | BA-04 Section 12 User & Role Management Flow |
| Persona | BA-05 Organization Administrator |
| User Journey | BA-06 Section 4 Organization Administrator Journey |
| Stakeholder | BA-07 Organization Administrator |
| Non-Functional Requirement | BA-09 Section 3 Security Requirements, Section 10 Data Management |
| Assumption / Constraint / Risk | BA-10 BA-ASS-006 |

### Purpose

To maintain accurate Staff profile information while preserving identity controls and auditability.

### Functional Requirement

The system shall allow authorized users to update permitted Staff profile fields while enforcing Organization scope, validation, lifecycle restrictions, and audit rules.

### Business Justification

Accurate Staff profile information supports communication, role administration, operational responsibility, reporting, security reviews, and support.

### Actors

- Organization Administrator
- Staff User
- Security Service
- Notification Service
- Audit Service

### Preconditions

- Staff Account exists.
- Staff belongs to the Organization.
- User is authenticated.
- User has Staff profile update permission.
- Account is not Deactivated for standard maintenance unless policy permits read-only access.

### Trigger

Organization Administrator opens Staff Profile and submits profile changes.

### In Scope

- View Staff profile.
- Update permitted identity and contact fields.
- Validate duplicate contact identifiers.
- Notify affected Staff user.
- Record audit events.

### Out of Scope

- Role assignment.
- Facility access assignment.
- Site access assignment.
- Credential reset.
- Staff account activation, suspension, or deactivation.

### Inputs

- Staff ID
- Staff name
- Email address
- Mobile number
- Designation
- Profile status notes
- Change reason

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Staff ID | Staff reference | Identifier | Yes | System | Must exist within Organization | Read-only |
| Staff Name | Full staff name | Text | Yes | Organization Administrator | Required and length validation | Editable |
| Email Address | Staff email | Email | Yes | Organization Administrator | Valid format and duplicate rules | May be login identifier |
| Mobile Number | Staff mobile | Phone | Conditional | Organization Administrator | Valid format and duplicate rules | May be login identifier |
| Designation | Business designation | Text | No | Organization Administrator | Length validation | Informational |
| Change Reason | Reason for update | Text | Conditional | Organization Administrator | Required for governed identity fields | Audit field |

### Main Flow

1. Organization Administrator opens Staff Profile.
2. The system validates Organization scope and permission.
3. The system loads Staff profile, account status, roles, and access summary.
4. Organization Administrator updates permitted profile fields.
5. The system validates mandatory fields, duplicate identifiers, formats, and status restrictions.
6. The system saves valid profile changes.
7. The system updates Staff Directory and access summaries.
8. The system sends profile update notification where configured.
9. The system records audit events.

### Alternate Flows

- If a Staff user updates self-service fields where allowed, the system restricts changes to permitted fields.
- If login identifier changes, the system may require confirmation or re-verification.
- If Staff Account is Suspended, profile maintenance may remain available to administrators.

### Exception Flows

- If duplicate email, mobile, or username exists, save is blocked.
- If user lacks scope, access is denied and logged.
- If profile update conflicts with security policy, save is blocked.
- If concurrent update occurs, the user is asked to reload current data.

### Outputs

- Updated Staff profile.
- Updated Staff Directory.
- Notification events.
- Audit events.

### UI Behaviour

Staff Profile shall display identity fields, account status, role summary, Facility/Site access summary, and audit-visible change indicators. Restricted fields shall be read-only with explanatory text.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-USR-101 | Staff must belong to the user's Organization scope. | Deny access and log event. | Critical |
| VAL-USR-102 | Mandatory Staff profile fields must remain complete. | Block save. | High |
| VAL-USR-103 | Login identifiers must remain unique. | Block save and show conflict. | Critical |
| VAL-USR-104 | Sensitive identity field changes must be auditable. | Require reason where configured. | High |
| VAL-USR-105 | User must have Staff profile update permission. | Deny action and log event. | Critical |

### Business Rules

- BA-02 BR-ORG-005 - Organization Users
- BA-02 BR-ORG-006 - Role-Based Access
- BA-02 BR-SEC-004 - Organization Data Isolation
- BA-02 BR-SEC-008 - Permission Changes
- BA-02 BR-SEC-009 - Sensitive Data Protection
- BA-02 BR-AUD-003 - Auditable Events

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| staff.profile.view | Organization Administrator | Read | Required to view Staff Profile |
| staff.profile.update | Organization Administrator | Update | Required to edit Staff Profile |
| staff.profile.self-update | Staff User | Update | Limited self-service update where enabled |
| audit.staff.profile.read | Organization Administrator | Read | Required to view profile audit history |

### Security Considerations

Staff profile data shall be protected through Organization isolation, RBAC, sensitive data controls, and audit logging. Login identifier changes shall be governed to prevent account takeover or duplicate identity risks.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Staff Profile Updated | Staff User | In-App, Email | Profile update saved | Include changed categories |
| Staff Identifier Changed | Staff User, Organization Administrator | Email, SMS | Login identifier changed | Include security notice |
| Staff Profile Update Failed | Organization Administrator | In-App | Save fails | Include failure reason |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| StaffProfileUpdated | User & Role Management | Audit Service, Reporting Service, Notification Service |
| StaffLoginIdentifierChanged | User & Role Management | Security Service, Notification Service |
| StaffDirectoryUpdated | User & Role Management | Reporting Service |

### Audit Events

| Audit Event | Trigger | Actor | Entity | Data Captured |
|---|---|---|---|---|
| Staff Profile Viewed | Profile opened | Authorized user | Staff | Staff ID, actor, timestamp |
| Staff Profile Updated | Profile saved | Authorized user | Staff | Previous values, new values, reason |
| Staff Identifier Changed | Login identifier changed | Authorized user | Staff Account | Previous identifier, new identifier, timestamp |

### Reports Generated

- Staff Directory Report
- Access Control Report
- Security Monitoring Report
- Audit Trail Report

### Related Screens

- Staff Profile
- Staff Directory
- Staff Activity
- Audit History

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/staff/{staffId} | GET | Authorized token | Retrieve Staff profile | 200 OK with Staff resource |
| /api/v1/staff/{staffId} | PATCH | Organization Administrator token | Update Staff profile | 200 OK with updated Staff resource |
| /api/v1/staff/{staffId}/audit-events | GET | Organization Administrator token | Retrieve Staff audit history | 200 OK with audit event list |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Staff | Read, Update | Store Staff profile | Primary entity |
| Staff Account | Read, Update | Maintain login identifiers where applicable | Security entity |
| Login History | Read | Display account context | Security monitoring |
| Audit Log | Insert | Record Staff profile updates | Required |
| Notification | Insert | Queue profile notifications | Conditional |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Created | Update profile | Created | Organization Administrator | Valid update |
| Active | Update profile | Active | Organization Administrator | Valid update |
| Suspended | Update permitted profile | Suspended | Organization Administrator | Limited maintenance allowed |
| Deactivated | Attempt standard update | Deactivated | Organization Administrator | Update blocked unless policy permits |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| USR-101 | Staff profile cannot be updated. | Invalid account status or permission | Review status or request access |
| USR-102 | Staff login identifier already exists. | Duplicate email, mobile, or username | Enter a unique identifier |
| USR-103 | Required Staff information is incomplete. | Missing mandatory field | Complete highlighted fields |
| USR-104 | You do not have permission to update this Staff profile. | Missing permission | Request access |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Update Staff profile | Given user has Staff profile update permission | When valid profile changes are submitted | Then the system shall save the profile |
| Enforce uniqueness | Given updated identifier already exists | When save is attempted | Then the system shall block update |
| Protect scope | Given Staff belongs to another Organization | When profile is requested | Then access shall be denied |
| Audit update | Given profile changes are saved | When transaction completes | Then previous and new values shall be audited |

### Dependencies

- Organization Management
- Security Service
- Notification Service
- Audit Service
- Staff lifecycle model

### Operational Considerations

Profile update failures shall be traceable by support using audit events and correlation identifiers.

### Non-Functional Considerations

Staff profile updates shall be secure, auditable, tenant-isolated, reliable, and maintainable.

### Assumptions

- Staff profile updates do not automatically modify role or access scope.
- Staff users may have limited self-service profile update in future.
- Deactivated accounts remain available for historical audit.

### Success Criteria

Staff profile information remains accurate, secure, scoped, and auditable.

### Related Functional Requirements

- FR-USR-001 - Create Staff Account
- FR-USR-003 - Assign Staff Role
- FR-USR-004 - Assign Facility Access
- FR-USR-005 - Assign Site Access
- FR-USR-012 - View Staff Directory

### Notes

This requirement maintains staff identity information and does not grant operational permissions by itself.

---

## FR-USR-003 - Assign Staff Role

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-USR-003 |
| Requirement Name | Assign Staff Role |
| Functional Module | User & Role Management |
| Business Domain | Staff Identity & Access |
| Business Capability | Role Management |
| Requirement Type | Functional |
| Requirement Category | Security |
| Requirement Version | 1.0 |
| Requirement Status | Approved |
| Priority | Critical |
| Complexity | High |
| Release Version | 1.0 |
| Owner | Product Management |

### Traceability References

| Traceability Type | Reference |
|---|---|
| Business Requirement | BA-08 Staff Identity & Access |
| Business Rule | BA-02 BR-ORG-006, BR-SEC-002, BR-SEC-003, BR-SEC-004, BR-SEC-008, BR-SEC-010, BR-AUD-003 |
| Business Process | BA-03 BP-STA-003 Assign Staff Role |
| Business Process Flow | BA-04 Section 12 User & Role Management Flow |
| Persona | BA-05 Organization Administrator |
| User Journey | BA-06 Section 4 Organization Administrator Journey |
| Stakeholder | BA-07 Organization Administrator |
| Non-Functional Requirement | BA-09 Section 3.2 Authorization |
| Assumption / Constraint / Risk | BA-10 BA-RSK-004 |

### Purpose

To assign business roles that determine Staff responsibilities and default permissions.

### Functional Requirement

The system shall allow Organization Administrators to assign, update, and remove Staff roles according to RBAC, least privilege, segregation, lifecycle, and audit requirements.

### Business Justification

Role assignment translates business responsibilities into controlled system access and ensures Staff can perform only authorized operations.

### Actors

- Organization Administrator
- Staff User
- Security Service
- Notification Service
- Audit Service

### Preconditions

- Staff Account exists.
- Staff belongs to the Organization.
- Role definitions are active.
- User is authenticated.
- User has role assignment permission.
- Staff account status permits role changes.

### Trigger

Organization Administrator selects Assign Staff Role from Staff Profile or Role Management.

### In Scope

- Assign one or more roles.
- Remove roles where policy allows.
- Validate role eligibility.
- Apply role-derived permissions.
- Notify Staff user of role changes.
- Record audit events.

### Out of Scope

- Creating global role definitions.
- Configuring custom permission overrides.
- Facility or Site access assignment.
- Customer access management.

### Inputs

- Staff ID
- Role ID
- Assignment action
- Effective date
- Assignment reason
- Approval reference, if applicable

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Staff ID | Staff receiving role | Identifier | Yes | Organization Administrator | Must exist within Organization | Target account |
| Role ID | Role to assign or remove | Identifier | Yes | Organization Administrator | Must be active and assignable | Examples include Facility Manager and Trainer |
| Assignment Action | Assign or remove role | Enum | Yes | Organization Administrator | Must be supported action | Controls update |
| Effective Date | Date role becomes effective | Date | Yes | Organization Administrator | Must satisfy policy | Immediate by default |
| Assignment Reason | Business reason | Text | Conditional | Organization Administrator | Required for privileged roles | Audit field |

### Main Flow

1. Organization Administrator opens Staff Role assignment.
2. The system loads Staff account, current roles, assignable roles, and security policy.
3. Organization Administrator selects role assignment action.
4. The system validates role availability, eligibility, least privilege, status, scope requirements, and approval rules.
5. If approval is required, the system creates an approval request.
6. If approval is not required, or after approval is granted, the system updates Staff role assignments.
7. The system recalculates effective permissions.
8. The system sends role change notification.
9. The system records audit events.

### Alternate Flows

- If multiple roles are allowed, the system calculates combined effective permissions.
- If a privileged role is selected, elevated approval may be required.
- If a role requires Facility or Site scope, activation readiness remains incomplete until scope is assigned.

### Exception Flows

- If role is inactive or not assignable, assignment is blocked.
- If removing the last required role would leave active Staff without access definition, removal is blocked.
- If permission recalculation fails, role change is not finalized.
- If user lacks permission, action is denied and logged.

### Outputs

- Staff Role assignment created, updated, or removed.
- Effective permissions recalculated.
- Notification generated.
- Audit events recorded.
- Staff readiness status updated.

### UI Behaviour

Role assignment UI shall show current roles, available roles, role descriptions, permission summary, privileged role indicators, scope requirements, and approval status.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-USR-201 | Staff must have at least one role before activation. | Mark readiness blocker or block activation. | Critical |
| VAL-USR-202 | Role must be active and assignable within Organization policy. | Block assignment. | Critical |
| VAL-USR-203 | Privileged role assignment requires elevated authorization or approval where configured. | Route approval or block. | Critical |
| VAL-USR-204 | Role changes must recalculate effective permissions. | Roll back role update on failure. | Critical |
| VAL-USR-205 | Role changes must be audited. | Block completion if audit write fails. | Critical |

### Business Rules

- BA-02 BR-ORG-006 - Role-Based Access
- BA-02 BR-SEC-002 - Role-Based Access Control
- BA-02 BR-SEC-003 - Least Privilege
- BA-02 BR-SEC-004 - Organization Data Isolation
- BA-02 BR-SEC-008 - Permission Changes
- BA-02 BR-SEC-010 - Administrative Actions
- BA-02 BR-AUD-003 - Auditable Events

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| staff.roles.view | Organization Administrator | Read | Required to view roles |
| staff.roles.assign | Organization Administrator | Execute | Required to assign role |
| staff.roles.remove | Organization Administrator | Update | Required to remove role |
| staff.roles.approve | Authorized Approver | Approve | Required for governed roles |

### Security Considerations

Role changes directly affect authorization and shall enforce least privilege, Organization isolation, administrative authorization, approval for privileged roles, and immutable audit logging.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Role Assigned | Staff User | In-App, Email | Role assignment completed | Include role name and effective date |
| Role Removed | Staff User | In-App, Email | Role removed | Include role name and effective date |
| Role Assignment Approval Required | Approver | In-App, Email | Governed role requested | Include requester, Staff, and role |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| StaffRoleAssigned | User & Role Management | Security Service, Audit Service, Notification Service |
| StaffRoleRemoved | User & Role Management | Security Service, Audit Service |
| StaffEffectivePermissionsChanged | Security Service | Audit Service, Reporting Service |

### Audit Events

| Audit Event | Trigger | Actor | Entity | Data Captured |
|---|---|---|---|---|
| Staff Role Viewed | Role section opened | Organization Administrator | Staff Role | Staff ID, actor, timestamp |
| Staff Role Assigned | Role assigned | Organization Administrator | Staff Role | Role ID, effective date, reason |
| Staff Role Removed | Role removed | Organization Administrator | Staff Role | Removed role, reason, timestamp |
| Effective Permissions Recalculated | Role change processed | System | Permission | Permission set summary |

### Reports Generated

- Access Control Report
- Staff Directory Report
- Security Monitoring Report
- Audit Trail Report

### Related Screens

- Staff Role Assignment
- Staff Profile
- Role Management
- Access Summary
- Approval Request

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/staff/{staffId}/roles | GET | Organization Administrator token | Retrieve Staff roles | 200 OK with role list |
| /api/v1/staff/{staffId}/roles | POST | Organization Administrator token | Assign Staff role | 201 Created with role assignment |
| /api/v1/staff/{staffId}/roles/{roleAssignmentId} | DELETE | Organization Administrator token | Remove Staff role | 200 OK with updated role state |
| /api/v1/staff/{staffId}/effective-permissions | GET | Organization Administrator token | Retrieve effective permissions | 200 OK with permission summary |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Staff | Read | Validate Staff scope | Target entity |
| Staff Account | Read, Update | Update readiness and effective access context | Security entity |
| Role | Read | Validate assignable role | Master data |
| Staff Role | Create, Read, Delete | Store role assignment | Primary mapping |
| Permission | Read | Calculate effective permissions | Authorization entity |
| Audit Log | Insert | Record role changes | Required |
| Notification | Insert | Queue role notifications | Conditional |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| No Role Assigned | Assign role | Role Assigned | Organization Administrator | Active assignable role |
| Role Assigned | Assign additional role | Role Assigned | Organization Administrator | Multiple roles allowed |
| Role Assigned | Remove role | Role Assigned or No Role Assigned | Organization Administrator | At least one activation role retained where required |
| Role Change Requested | Approval granted | Role Assigned | Authorized Approver | Approval required and granted |
| Role Change Requested | Approval rejected | Existing Role State | Authorized Approver | Existing roles retained |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| USR-201 | Selected role is not available. | Inactive or unauthorized role | Select another role |
| USR-202 | Staff must have at least one role before activation. | Missing required role | Assign a role |
| USR-203 | Role assignment requires approval. | Privileged role selected | Submit for approval |
| USR-204 | Effective permissions could not be recalculated. | Security Service failure | Retry or contact support |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Assign role | Given user has role assignment permission | When an active role is assigned | Then the system shall create Staff Role assignment |
| Recalculate permissions | Given role assignment changes | When change is saved | Then effective permissions shall be recalculated |
| Govern privileged role | Given privileged role requires approval | When role is assigned | Then the system shall create approval request |
| Audit role change | Given role changes | When transaction completes | Then audit history shall record role change |

### Dependencies

- Role definitions
- Permission definitions
- Security Service
- Approval Workflow Service
- Notification Service
- Audit Service

### Operational Considerations

Role assignment changes should be immediately visible in access summaries and security monitoring reports.

### Non-Functional Considerations

Role management shall be secure, auditable, low-latency, tenant-isolated, and maintainable for future role expansion.

### Assumptions

- Role definitions are configured before assignment.
- Effective permissions are derived from roles and approved overrides.
- Privileged role assignments may require approval.

### Success Criteria

Staff users receive correct business roles and effective permissions while maintaining least privilege and traceability.

### Related Functional Requirements

- FR-USR-001 - Create Staff Account
- FR-USR-006 - Configure Staff Permissions
- FR-USR-007 - Activate Staff Account
- FR-USR-011 - View Staff Activity

### Notes

Role assignment determines responsibility; Facility and Site assignment determine operational scope.

---

## FR-USR-004 - Assign Facility Access

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-USR-004 |
| Requirement Name | Assign Facility Access |
| Functional Module | User & Role Management |
| Business Domain | Staff Identity & Access |
| Business Capability | Access Management |
| Requirement Type | Functional |
| Requirement Category | Security |
| Requirement Version | 1.0 |
| Requirement Status | Approved |
| Priority | Critical |
| Complexity | High |
| Release Version | 1.0 |
| Owner | Product Management |

### Traceability References

| Traceability Type | Reference |
|---|---|
| Business Requirement | BA-08 Staff Identity & Access |
| Business Rule | BA-02 BR-FAC-007, BR-ORG-005, BR-ORG-006, BR-SEC-002, BR-SEC-003, BR-SEC-004, BR-SEC-008 |
| Business Process | BA-03 BP-STA-004 Assign Facility Access |
| Business Process Flow | BA-04 Section 12 User & Role Management Flow |
| Persona | BA-05 Organization Administrator, Facility Manager |
| User Journey | BA-06 Section 4 Organization Administrator Journey, Section 5 Facility Manager Journey |
| Stakeholder | BA-07 Organization Administrator, Facility Manager |
| Non-Functional Requirement | BA-09 Section 3.2 Authorization |
| Assumption / Constraint / Risk | BA-10 BA-ASS-006 |

### Purpose

To define the Facilities where a Staff user is authorized to perform operational activities.

### Functional Requirement

The system shall allow Organization Administrators to assign, update, and remove Facility access for Staff users based on role, Organization scope, Facility eligibility, and least privilege.

### Business Justification

Facility access limits Staff activity to appropriate business units and prevents unauthorized access across multiple Facilities within the same Organization.

### Actors

- Organization Administrator
- Facility Manager
- Staff User
- Security Service
- Notification Service
- Audit Service

### Preconditions

- Staff Account exists.
- Staff belongs to the Organization.
- Facility exists under the same Organization.
- User is authenticated.
- User has Facility access assignment permission.
- Staff role permits Facility-scoped access.

### Trigger

Organization Administrator opens Staff Facility Access and submits assignment changes.

### In Scope

- Assign Staff to one or more Facilities.
- Remove Facility access.
- Validate role compatibility and Facility status.
- Recalculate effective access scope.
- Notify Staff user.
- Record audit events.

### Out of Scope

- Site access assignment.
- Facility Manager responsibility assignment where handled by Facility Management.
- Role definition management.
- Customer access.

### Inputs

- Staff ID
- Facility IDs
- Assignment action
- Effective date
- Assignment reason

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Staff ID | Staff receiving Facility access | Identifier | Yes | Organization Administrator | Must belong to Organization | Target user |
| Facility ID | Facility access scope | Identifier | Yes | Organization Administrator | Must belong to same Organization | Scope boundary |
| Assignment Action | Assign or remove access | Enum | Yes | Organization Administrator | Must be supported action | Controls update |
| Effective Date | Date access becomes effective | Date | Yes | Organization Administrator | Must satisfy policy | Immediate by default |
| Assignment Reason | Reason for access change | Text | Conditional | Organization Administrator | Required where governed | Audit field |

### Main Flow

1. Organization Administrator opens Staff Facility Access.
2. The system loads Staff account, current roles, current Facility assignments, and eligible Facilities.
3. Organization Administrator selects Facilities to assign or remove.
4. The system validates Organization ownership, Facility eligibility, Staff role compatibility, and least privilege.
5. The system updates Facility assignment records.
6. The system recalculates effective access scope.
7. The system invalidates or refreshes active sessions where security policy requires.
8. The system sends access change notifications.
9. The system records audit events.

### Alternate Flows

- If Staff has Organization-wide role, the system may automatically include all Facilities where policy permits.
- If future-dated access is configured, the system schedules activation.
- If removing Facility access would orphan required Site access, the system displays dependency impact.

### Exception Flows

- If Facility belongs to another Organization, assignment is blocked.
- If role does not permit Facility access, assignment is blocked.
- If removing access would violate required operational coverage, system blocks or requires approval.
- If Security Service synchronization fails, changes are rolled back or marked failed.

### Outputs

- Updated Staff Facility Assignment records.
- Updated effective access scope.
- Notifications.
- Audit events.
- Access summary update.

### UI Behaviour

Facility Access UI shall show assigned Facilities, available Facilities, Facility status, role compatibility, effective dates, and dependency warnings. Unauthorized Facilities shall not be selectable.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-USR-301 | Facility must belong to the same Organization as Staff. | Block assignment. | Critical |
| VAL-USR-302 | Staff role must support Facility-scoped access. | Block assignment or request role update. | High |
| VAL-USR-303 | Access changes must preserve least privilege. | Block excessive scope where policy disallows. | Critical |
| VAL-USR-304 | Facility access changes must recalculate effective permissions. | Roll back on recalculation failure. | Critical |
| VAL-USR-305 | Access changes must be audited. | Block completion if audit write fails. | Critical |

### Business Rules

- BA-02 BR-FAC-007 - Facility Staff Assignment
- BA-02 BR-ORG-005 - Organization Users
- BA-02 BR-ORG-006 - Role-Based Access
- BA-02 BR-SEC-002 - Role-Based Access Control
- BA-02 BR-SEC-003 - Least Privilege
- BA-02 BR-SEC-004 - Organization Data Isolation
- BA-02 BR-SEC-008 - Permission Changes

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| staff.facility-access.view | Organization Administrator | Read | Required to view Facility access |
| staff.facility-access.assign | Organization Administrator | Execute | Required to assign Facility scope |
| staff.facility-access.remove | Organization Administrator | Update | Required to remove Facility scope |
| staff.effective-access.view | Organization Administrator | Read | Required to view recalculated scope |

### Security Considerations

Facility access assignments shall enforce Organization scope, role compatibility, least privilege, session refresh rules, and audit logging. Users shall not gain access to Facilities outside their Organization.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Facility Access Assigned | Staff User | In-App, Email | Facility access added | Include Facility name and effective date |
| Facility Access Removed | Staff User | In-App, Email | Facility access removed | Include Facility name and effective date |
| Facility Access Changed | Organization Administrator | In-App | Assignment saved | Include changed access summary |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| StaffFacilityAccessAssigned | User & Role Management | Security Service, Audit Service, Notification Service |
| StaffFacilityAccessRemoved | User & Role Management | Security Service, Audit Service |
| StaffEffectiveScopeChanged | Security Service | Reporting Service, Audit Service |

### Audit Events

| Audit Event | Trigger | Actor | Entity | Data Captured |
|---|---|---|---|---|
| Staff Facility Access Viewed | Access screen opened | Organization Administrator | Staff Facility Assignment | Staff ID, actor, timestamp |
| Staff Facility Access Assigned | Facility assigned | Organization Administrator | Staff Facility Assignment | Staff ID, Facility ID, effective date |
| Staff Facility Access Removed | Facility removed | Organization Administrator | Staff Facility Assignment | Staff ID, Facility ID, reason |

### Reports Generated

- Access Control Report
- Staff Directory Report
- Security Monitoring Report
- Workforce Administration Dashboard

### Related Screens

- Staff Facility Access
- Staff Profile
- Staff Directory
- Access Summary

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/staff/{staffId}/facility-access | GET | Organization Administrator token | Retrieve Facility access | 200 OK with Facility assignment list |
| /api/v1/staff/{staffId}/facility-access | POST | Organization Administrator token | Assign Facility access | 201 Created with assignment |
| /api/v1/staff/{staffId}/facility-access/{assignmentId} | DELETE | Organization Administrator token | Remove Facility access | 200 OK with updated access |
| /api/v1/staff/{staffId}/effective-access | GET | Organization Administrator token | Retrieve effective access scope | 200 OK with scope summary |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Staff | Read | Validate Staff scope | Target user |
| Facility | Read | Validate Facility scope | Assignment target |
| Staff Facility Assignment | Create, Read, Delete | Store Facility access | Primary mapping |
| Role | Read | Validate role compatibility | Security dependency |
| Permission | Read | Recalculate effective access | Authorization |
| Audit Log | Insert | Record access changes | Required |
| Notification | Insert | Queue access notifications | Conditional |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| No Facility Access | Assign Facility | Facility Access Assigned | Organization Administrator | Eligible Facility |
| Facility Access Assigned | Add Facility | Facility Access Assigned | Organization Administrator | Multiple assignments allowed |
| Facility Access Assigned | Remove Facility | Facility Access Assigned or No Facility Access | Organization Administrator | Coverage policy satisfied |
| Facility Access Scheduled | Effective date reached | Facility Access Assigned | System | Scheduled assignment due |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| USR-301 | Facility is outside the Staff Organization. | Tenant mismatch | Select same-Organization Facility |
| USR-302 | Staff role does not support Facility access. | Role incompatibility | Assign appropriate role |
| USR-303 | Facility access change violates least privilege policy. | Excessive scope | Reduce assignment scope |
| USR-304 | Facility access could not be synchronized. | Security Service failure | Retry or contact support |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Assign Facility access | Given Staff and Facility belong to same Organization | When Facility access is assigned | Then Staff shall receive Facility scope |
| Block cross-tenant Facility | Given Facility belongs to another Organization | When assignment is attempted | Then the system shall block assignment |
| Recalculate access | Given Facility access changes | When saved | Then effective access scope shall be recalculated |
| Audit access change | Given assignment is added or removed | When transaction completes | Then audit history shall record access change |

### Dependencies

- Facility Management
- Role Management
- Security Service
- Notification Service
- Audit Service

### Operational Considerations

Access changes should be visible immediately in Staff access summaries and security monitoring.

### Non-Functional Considerations

Facility access management shall be secure, auditable, tenant-isolated, reliable, and scalable for multi-facility Organizations.

### Assumptions

- Staff belongs to one Organization.
- Facility access does not automatically grant Site access unless policy explicitly supports inheritance.
- Effective permissions are recalculated after every access change.

### Success Criteria

Staff access is limited to appropriate Facilities and fully traceable.

### Related Functional Requirements

- FR-FAC-007 - Assign Facility Manager
- FR-USR-003 - Assign Staff Role
- FR-USR-005 - Assign Site Access
- FR-USR-006 - Configure Staff Permissions

### Notes

Facility access defines operational scope; role assignment defines allowed actions.

---

## FR-USR-005 - Assign Site Access

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-USR-005 |
| Requirement Name | Assign Site Access |
| Functional Module | User & Role Management |
| Business Domain | Staff Identity & Access |
| Business Capability | Access Management |
| Requirement Type | Functional |
| Requirement Category | Security |
| Requirement Version | 1.0 |
| Requirement Status | Approved |
| Priority | Critical |
| Complexity | High |
| Release Version | 1.0 |
| Owner | Product Management |

### Traceability References

| Traceability Type | Reference |
|---|---|
| Business Requirement | BA-08 Staff Identity & Access |
| Business Rule | BA-02 BR-SIT-007, BR-ORG-005, BR-ORG-006, BR-SEC-002, BR-SEC-003, BR-SEC-004, BR-SEC-008 |
| Business Process | BA-03 BP-STA-005 Assign Site Access |
| Business Process Flow | BA-04 Section 12 User & Role Management Flow |
| Persona | BA-05 Organization Administrator, Site Administrator, Reception Staff, Trainer |
| User Journey | BA-06 Section 6 Site Administrator Journey, Section 7 Reception Staff Journey, Section 8 Trainer Journey |
| Stakeholder | BA-07 Organization Administrator, Site Administrator |
| Non-Functional Requirement | BA-09 Section 3.2 Authorization |
| Assumption / Constraint / Risk | BA-10 BA-ASS-006 |

### Purpose

To define the Sites where a Staff user is authorized to perform local branch operations.

### Functional Requirement

The system shall allow Organization Administrators to assign, update, and remove Site access for Staff users based on Staff role, Facility access, Site eligibility, and least privilege.

### Business Justification

Site access ensures Reception Staff, Trainers, Site Administrators, and other branch users operate only within authorized physical locations.

### Actors

- Organization Administrator
- Site Administrator
- Staff User
- Security Service
- Notification Service
- Audit Service

### Preconditions

- Staff Account exists.
- Site exists under the Organization.
- Parent Facility is within Staff's permitted scope where required.
- User is authenticated.
- User has Site access assignment permission.
- Staff role permits Site-scoped access.

### Trigger

Organization Administrator opens Staff Site Access and submits Site assignment changes.

### In Scope

- Assign Staff to one or more Sites.
- Remove Site access.
- Validate Site and Facility scope.
- Recalculate effective Site access.
- Notify affected Staff.
- Record audit events.

### Out of Scope

- Facility access assignment.
- Site Manager lifecycle assignment where handled by Site Management.
- Role definition management.
- Customer portal access.

### Inputs

- Staff ID
- Site IDs
- Assignment action
- Effective date
- Assignment reason

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Staff ID | Staff receiving Site access | Identifier | Yes | Organization Administrator | Must belong to Organization | Target user |
| Site ID | Site access scope | Identifier | Yes | Organization Administrator | Must belong to same Organization and valid Facility | Scope boundary |
| Assignment Action | Assign or remove access | Enum | Yes | Organization Administrator | Must be supported action | Controls update |
| Effective Date | Date access becomes effective | Date | Yes | Organization Administrator | Must satisfy policy | Immediate by default |
| Assignment Reason | Reason for access change | Text | Conditional | Organization Administrator | Required where governed | Audit field |

### Main Flow

1. Organization Administrator opens Staff Site Access.
2. The system loads Staff account, role assignments, Facility access, current Site access, and eligible Sites.
3. Organization Administrator selects Sites to assign or remove.
4. The system validates Organization scope, parent Facility relationship, Staff role compatibility, and least privilege.
5. The system updates Site assignment records.
6. The system recalculates effective access scope.
7. The system refreshes active sessions where security policy requires.
8. The system sends access change notifications.
9. The system records audit events.

### Alternate Flows

- If Staff has Facility-wide role, Site access may inherit all Sites under assigned Facility where policy allows.
- If a future-dated assignment is configured, the system schedules access activation.
- If a Site is Suspended, access may remain assigned but operational actions are restricted by Site status.

### Exception Flows

- If Site belongs to another Organization, assignment is blocked.
- If Site is outside assigned Facility scope, assignment is blocked unless policy permits direct Site assignment.
- If role does not support Site access, assignment is blocked.
- If Security Service synchronization fails, assignment is not completed.

### Outputs

- Updated Staff Site Assignment records.
- Updated effective access scope.
- Notifications.
- Audit events.
- Staff access summary updated.

### UI Behaviour

Site Access UI shall display assigned Sites, parent Facilities, Site status, inherited access, role compatibility, and dependency warnings. Sites outside scope shall not be selectable.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-USR-401 | Site must belong to the same Organization as Staff. | Block assignment. | Critical |
| VAL-USR-402 | Site assignment must comply with Facility access rules. | Block or request Facility access. | Critical |
| VAL-USR-403 | Staff role must support Site-scoped operations. | Block assignment or request role update. | High |
| VAL-USR-404 | Access changes must recalculate effective permissions. | Roll back on recalculation failure. | Critical |
| VAL-USR-405 | Site access changes must be audited. | Block completion if audit write fails. | Critical |

### Business Rules

- BA-02 BR-SIT-007 - Site Staff Allocation
- BA-02 BR-ORG-005 - Organization Users
- BA-02 BR-ORG-006 - Role-Based Access
- BA-02 BR-SEC-002 - Role-Based Access Control
- BA-02 BR-SEC-003 - Least Privilege
- BA-02 BR-SEC-004 - Organization Data Isolation
- BA-02 BR-SEC-008 - Permission Changes

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| staff.site-access.view | Organization Administrator | Read | Required to view Site access |
| staff.site-access.assign | Organization Administrator | Execute | Required to assign Site access |
| staff.site-access.remove | Organization Administrator | Update | Required to remove Site access |
| staff.effective-access.view | Organization Administrator | Read | Required to view recalculated scope |

### Security Considerations

Site access shall be constrained by Organization and Facility hierarchy, role compatibility, least privilege, and auditable permission changes. Users shall not access unauthorized branch data.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Site Access Assigned | Staff User | In-App, Email | Site access added | Include Site name and effective date |
| Site Access Removed | Staff User | In-App, Email | Site access removed | Include Site name and effective date |
| Site Access Changed | Organization Administrator | In-App | Assignment saved | Include access summary |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| StaffSiteAccessAssigned | User & Role Management | Security Service, Audit Service, Notification Service |
| StaffSiteAccessRemoved | User & Role Management | Security Service, Audit Service |
| StaffSiteScopeChanged | Security Service | Reporting Service, Audit Service |

### Audit Events

| Audit Event | Trigger | Actor | Entity | Data Captured |
|---|---|---|---|---|
| Staff Site Access Viewed | Access screen opened | Organization Administrator | Staff Site Assignment | Staff ID, actor, timestamp |
| Staff Site Access Assigned | Site assigned | Organization Administrator | Staff Site Assignment | Staff ID, Site ID, effective date |
| Staff Site Access Removed | Site removed | Organization Administrator | Staff Site Assignment | Staff ID, Site ID, reason |

### Reports Generated

- Access Control Report
- Staff Directory Report
- Site Staff Allocation Report
- Security Monitoring Report

### Related Screens

- Staff Site Access
- Staff Profile
- Site Staff Allocation
- Staff Directory
- Access Summary

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/staff/{staffId}/site-access | GET | Organization Administrator token | Retrieve Site access | 200 OK with Site assignment list |
| /api/v1/staff/{staffId}/site-access | POST | Organization Administrator token | Assign Site access | 201 Created with assignment |
| /api/v1/staff/{staffId}/site-access/{assignmentId} | DELETE | Organization Administrator token | Remove Site access | 200 OK with updated access |
| /api/v1/staff/{staffId}/effective-access | GET | Organization Administrator token | Retrieve effective access scope | 200 OK with scope summary |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Staff | Read | Validate Staff scope | Target user |
| Site | Read | Validate Site scope | Assignment target |
| Facility | Read | Validate parent Facility | Scope dependency |
| Staff Site Assignment | Create, Read, Delete | Store Site access | Primary mapping |
| Role | Read | Validate role compatibility | Security dependency |
| Permission | Read | Recalculate effective access | Authorization |
| Audit Log | Insert | Record Site access changes | Required |
| Notification | Insert | Queue access notifications | Conditional |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| No Site Access | Assign Site | Site Access Assigned | Organization Administrator | Eligible Site |
| Site Access Assigned | Add Site | Site Access Assigned | Organization Administrator | Multiple Sites allowed |
| Site Access Assigned | Remove Site | Site Access Assigned or No Site Access | Organization Administrator | Coverage policy satisfied |
| Site Access Scheduled | Effective date reached | Site Access Assigned | System | Scheduled assignment due |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| USR-401 | Site is outside the Staff Organization. | Tenant mismatch | Select same-Organization Site |
| USR-402 | Site is outside assigned Facility scope. | Facility scope mismatch | Assign Facility access or choose another Site |
| USR-403 | Staff role does not support Site access. | Role incompatibility | Assign appropriate role |
| USR-404 | Site access could not be synchronized. | Security Service failure | Retry or contact support |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Assign Site access | Given Staff and Site are within valid scope | When Site access is assigned | Then Staff shall receive Site scope |
| Block cross-tenant Site | Given Site belongs to another Organization | When assignment is attempted | Then the system shall block assignment |
| Validate Facility scope | Given Site is outside Staff Facility access | When assignment is attempted | Then assignment shall be blocked unless policy allows |
| Audit access change | Given Site access changes | When transaction completes | Then audit history shall record access change |

### Dependencies

- Site Management
- Facility Access assignment
- Role Management
- Security Service
- Notification Service
- Audit Service

### Operational Considerations

Site access changes should be visible in Staff access summaries, Site staff allocation views, and security reports.

### Non-Functional Considerations

Site access management shall be secure, auditable, tenant-isolated, reliable, and scalable for multi-site operations.

### Assumptions

- Site access may depend on Facility access.
- Some roles require Site scope before activation.
- Effective access is recalculated after every access change.

### Success Criteria

Staff access is limited to authorized Sites and supports secure local branch operations.

### Related Functional Requirements

- FR-SIT-007 - Activate Site
- FR-USR-003 - Assign Staff Role
- FR-USR-004 - Assign Facility Access
- FR-USR-006 - Configure Staff Permissions

### Notes

Site access provides local operating scope for Reception Staff, Trainers, and Site Administrators.

---

## FR-USR-006 - Configure Staff Permissions

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-USR-006 |
| Requirement Name | Configure Staff Permissions |
| Functional Module | User & Role Management |
| Business Domain | Staff Identity & Access |
| Business Capability | Access Control |
| Requirement Type | Functional |
| Requirement Category | Security |
| Requirement Version | 1.0 |
| Requirement Status | Approved |
| Priority | Critical |
| Complexity | Very High |
| Release Version | 1.0 |
| Owner | Product Management |

### Traceability References

| Traceability Type | Reference |
|---|---|
| Business Requirement | BA-08 Staff Identity & Access |
| Business Rule | BA-02 BR-ORG-006, BR-SEC-002, BR-SEC-003, BR-SEC-004, BR-SEC-008, BR-SEC-010, BR-AUD-003 |
| Business Process | BA-03 BP-STA-006 Configure Staff Permissions |
| Business Process Flow | BA-04 Section 12 User & Role Management Flow |
| Persona | BA-05 Organization Administrator |
| User Journey | BA-06 Section 4 Organization Administrator Journey |
| Stakeholder | BA-07 Organization Administrator, External Auditor |
| Non-Functional Requirement | BA-09 Section 3.2 Authorization, Section 3.8 Audit Logging |
| Assumption / Constraint / Risk | BA-10 BA-RSK-004, BA-RSK-005 |

### Purpose

To manage Staff effective permissions beyond role defaults where Organization policy allows controlled permission overrides.

### Functional Requirement

The system shall allow authorized administrators to configure Staff permission overrides, restrictions, or extensions within role, scope, approval, least privilege, and audit constraints.

### Business Justification

Permission configuration allows operational flexibility while maintaining enterprise-grade access control, security accountability, and traceable authorization decisions.

### Actors

- Organization Administrator
- Authorized Approver
- Security Service
- Audit Service
- Notification Service

### Preconditions

- Staff Account exists.
- Staff has at least one role.
- Permission definitions are available.
- User is authenticated.
- User has permission configuration authority.
- Organization policy permits permission overrides.

### Trigger

Organization Administrator opens Staff Permissions and submits permission changes.

### In Scope

- View effective permissions.
- Add allowed permission extensions.
- Apply permission restrictions.
- Validate least privilege and scope.
- Route sensitive permissions for approval.
- Recalculate effective authorization.
- Audit and notify changes.

### Out of Scope

- Global permission definition creation.
- Platform-wide security policy configuration.
- Role assignment.
- Facility and Site scope assignment.
- Customer consent management.

### Inputs

- Staff ID
- Permission ID
- Permission action
- Access level
- Scope reference
- Effective date
- Expiry date
- Justification

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Staff ID | Staff receiving permission change | Identifier | Yes | Organization Administrator | Must exist within Organization | Target user |
| Permission ID | Permission being changed | Identifier | Yes | Organization Administrator | Must be active and assignable | Authorization unit |
| Permission Action | Grant, restrict, or revoke | Enum | Yes | Organization Administrator | Must be supported action | Controls change |
| Access Level | Permission level | Enum | Yes | Organization Administrator | View, Create, Update, Approve, Export, Configure, or Execute | Based on permission type |
| Scope Reference | Organization, Facility, or Site scope | Identifier | Conditional | Organization Administrator | Must match Staff authorized scope | Required for scoped permissions |
| Effective Date | Date permission applies | Date | Yes | Organization Administrator | Must satisfy policy | Immediate by default |
| Justification | Business reason | Text | Yes | Organization Administrator | Required | Audit and approval support |

### Main Flow

1. Organization Administrator opens Staff Permissions.
2. The system loads Staff roles, existing permission overrides, effective permissions, and available permission definitions.
3. Organization Administrator selects permission action and scope.
4. The system validates role compatibility, scope, least privilege, sensitive permission restrictions, and approval requirements.
5. If approval is required, the system creates an approval request.
6. If approval is not required, or after approval is granted, the system applies the permission change.
7. The system recalculates effective permissions.
8. The system refreshes access summaries and active sessions where required.
9. The system sends notifications and records audit events.

### Alternate Flows

- If a permission restriction is applied, it may reduce access below role default.
- If permission has expiry date, the system automatically removes or expires it.
- If permission is read-only for role-based governance, the system displays it without allowing direct change.

### Exception Flows

- If permission violates least privilege policy, the system blocks change.
- If scope is outside Staff assignments, the system blocks change.
- If sensitive permission approval is rejected, existing permission state remains.
- If permission recalculation fails, change is rolled back.

### Outputs

- Updated Staff permission configuration.
- Effective permissions recalculated.
- Approval request, if applicable.
- Session refresh or invalidation event, if required.
- Notifications and audit events.

### UI Behaviour

Staff Permissions shall display role-derived permissions, explicit grants, restrictions, effective permission result, scope, expiry, justification, and approval state. Sensitive permissions shall be visually marked.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-USR-501 | Permission change must comply with least privilege. | Block or require approval. | Critical |
| VAL-USR-502 | Permission scope must be within Staff Organization, Facility, and Site assignments. | Block change. | Critical |
| VAL-USR-503 | Sensitive permissions require justification and approval where configured. | Route approval or block. | Critical |
| VAL-USR-504 | Effective permissions must be recalculated after every permission change. | Roll back on recalculation failure. | Critical |
| VAL-USR-505 | Permission changes must be audited. | Block completion if audit write fails. | Critical |

### Business Rules

- BA-02 BR-ORG-006 - Role-Based Access
- BA-02 BR-SEC-002 - Role-Based Access Control
- BA-02 BR-SEC-003 - Least Privilege
- BA-02 BR-SEC-004 - Organization Data Isolation
- BA-02 BR-SEC-008 - Permission Changes
- BA-02 BR-SEC-010 - Administrative Actions
- BA-02 BR-AUD-003 - Auditable Events

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| staff.permissions.view | Organization Administrator | Read | Required to view permissions |
| staff.permissions.configure | Organization Administrator | Configure | Required to configure permission overrides |
| staff.permissions.approve | Authorized Approver | Approve | Required for sensitive permission approval |
| staff.effective-permissions.view | Organization Administrator | Read | Required to view effective permissions |

### Security Considerations

Permission configuration is high-risk and shall enforce least privilege, segregation of duties where configured, scoped authorization, approval for sensitive actions, session refresh, and immutable audit logging.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Staff Permissions Updated | Staff User | In-App, Email | Permission change applied | Include changed permission category |
| Permission Approval Required | Approver | In-App, Email | Sensitive permission requested | Include justification and scope |
| Permission Expired | Staff User, Organization Administrator | In-App | Permission expiry reached | Include expired permission |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| StaffPermissionConfigured | User & Role Management | Security Service, Audit Service |
| StaffSensitivePermissionRequested | User & Role Management | Approval Workflow Service |
| StaffEffectivePermissionsRecalculated | Security Service | Audit Service, Reporting Service |

### Audit Events

| Audit Event | Trigger | Actor | Entity | Data Captured |
|---|---|---|---|---|
| Staff Permissions Viewed | Permission screen opened | Organization Administrator | Permission | Staff ID, actor, timestamp |
| Staff Permission Configured | Permission changed | Organization Administrator | Permission | Previous permission, new permission, scope, justification |
| Sensitive Permission Approved | Approval completed | Authorized Approver | Approval Request | Decision, comments, permission |

### Reports Generated

- Access Control Report
- Security Monitoring Report
- Permission Change Report
- Audit Trail Report

### Related Screens

- Staff Permissions
- Effective Access Summary
- Staff Profile
- Approval Request
- Security Monitoring

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/staff/{staffId}/permissions | GET | Organization Administrator token | Retrieve Staff permissions | 200 OK with permission list |
| /api/v1/staff/{staffId}/permissions | PATCH | Organization Administrator token | Configure Staff permissions | 200 OK with updated permissions |
| /api/v1/staff/{staffId}/effective-permissions | GET | Organization Administrator token | Retrieve effective permissions | 200 OK with effective permission summary |
| /api/v1/staff/{staffId}/permissions/approval-requests | POST | Organization Administrator token | Submit sensitive permission request | 202 Accepted with approval request |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Staff | Read | Validate Staff scope | Target user |
| Role | Read | Determine role-derived permissions | Source |
| Permission | Read | Validate permission definition | Authorization entity |
| Staff Role | Read | Calculate baseline access | Role mapping |
| Staff Permission | Create, Read, Update, Delete | Store explicit permission overrides | Primary mapping |
| Approval Request | Insert, Update | Manage sensitive permission approval | Conditional |
| Audit Log | Insert | Record permission changes | Required |
| Notification | Insert | Queue permission notifications | Conditional |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Role-Derived | Add override | Override Active | Organization Administrator | Allowed permission |
| Override Active | Revoke override | Role-Derived | Organization Administrator | Revoke allowed |
| Permission Requested | Approval granted | Override Active | Authorized Approver | Approval required and granted |
| Permission Requested | Approval rejected | Role-Derived | Authorized Approver | Existing state retained |
| Override Active | Expiry reached | Expired | System | Expiry date configured |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| USR-501 | Permission change violates least privilege policy. | Excessive access | Reduce permission scope |
| USR-502 | Permission scope is outside Staff assignment. | Invalid scope | Select authorized scope |
| USR-503 | Sensitive permission requires approval. | Governed permission | Submit approval request |
| USR-504 | Effective permissions could not be updated. | Security Service failure | Retry or contact support |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Configure allowed permission | Given user has permission configuration authority | When valid permission change is submitted | Then the system shall update Staff permissions |
| Enforce least privilege | Given permission exceeds allowed policy | When save is attempted | Then the system shall block or route approval |
| Recalculate effective permissions | Given permission changes | When saved | Then effective permissions shall be recalculated |
| Audit permission change | Given permission configuration changes | When transaction completes | Then audit history shall record the change |

### Dependencies

- Role and permission definitions
- Security Service
- Approval Workflow Service
- Audit Service
- Notification Service

### Operational Considerations

Permission changes should be visible in access reports and security monitoring immediately after effective recalculation.

### Non-Functional Considerations

Permission configuration shall be secure, auditable, reliable, performant, and maintainable for enterprise RBAC growth.

### Assumptions

- Permission overrides are allowed only where Organization policy permits.
- Role-derived permissions remain the baseline.
- Sensitive permissions may require approval.

### Success Criteria

Staff permissions remain accurate, scoped, least-privileged, and auditable.

### Related Functional Requirements

- FR-USR-003 - Assign Staff Role
- FR-USR-004 - Assign Facility Access
- FR-USR-005 - Assign Site Access
- FR-USR-011 - View Staff Activity

### Notes

Permission overrides should be used carefully and reviewed regularly.

---

## FR-USR-007 - Activate Staff Account

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-USR-007 |
| Requirement Name | Activate Staff Account |
| Functional Module | User & Role Management |
| Business Domain | Staff Identity & Access |
| Business Capability | Staff Lifecycle |
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
| Business Requirement | BA-08 Staff Identity & Access |
| Business Rule | BA-02 BR-ORG-005, BR-ORG-006, BR-SEC-001, BR-SEC-002, BR-SEC-003, BR-SEC-005, BR-AUD-003 |
| Business Process | BA-03 BP-STA-007 Activate Staff Account |
| Business Process Flow | BA-04 Section 12 User & Role Management Flow |
| Persona | BA-05 Organization Administrator, Staff User |
| User Journey | BA-06 Section 4 Organization Administrator Journey |
| Stakeholder | BA-07 Organization Administrator |
| Non-Functional Requirement | BA-09 Section 3.1 Authentication, Section 3.2 Authorization |
| Assumption / Constraint / Risk | BA-10 BA-ASS-002, BA-RSK-004 |

### Purpose

To enable a Staff Account for authenticated platform access after identity, role, access scope, and security readiness checks are complete.

### Functional Requirement

The system shall allow an Organization Administrator to activate an eligible Staff Account and enable login access according to configured security policies.

### Business Justification

Activation prevents incomplete or unauthorized Staff Accounts from accessing the platform before role, scope, and credential requirements are satisfied.

### Actors

- Organization Administrator
- Staff User
- Security Service
- Notification Service
- Audit Service

### Preconditions

- Staff Account exists in Created status.
- Organization is Active.
- Staff profile is complete.
- At least one role is assigned.
- Required Facility or Site access is assigned where role requires scope.
- Credential setup is complete or activation invitation is valid.
- User has Staff activation permission.

### Trigger

Organization Administrator selects Activate Staff Account.

### In Scope

- Validate activation readiness.
- Enable authentication.
- Set account status to Active.
- Apply effective permissions.
- Notify Staff user.
- Record audit events.

### Out of Scope

- Staff Account creation.
- Password reset.
- Role creation.
- Customer account activation.
- Platform Administrator activation.

### Inputs

- Staff ID
- Activation confirmation
- Activation notes
- Readiness validation result
- Effective activation timestamp

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Staff ID | Staff Account to activate | Identifier | Yes | Organization Administrator | Must exist and be Created | Target account |
| Activation Confirmation | Explicit confirmation | Boolean | Yes | Organization Administrator | Must be confirmed | Governance control |
| Activation Notes | Activation comments | Text | No | Organization Administrator | Length validation | Audit field |
| Readiness Status | Activation readiness result | Enum | Yes | System | Must be Ready | Derived from checks |
| Activation Timestamp | Date and time activated | DateTime | Yes | System | System-generated | Audit and reporting |

### Main Flow

1. Organization Administrator opens Staff Account lifecycle actions.
2. Organization Administrator selects Activate Staff Account.
3. The system validates Staff profile completeness, role assignment, required access scope, credential readiness, Organization status, and security policy.
4. The system displays readiness results.
5. Organization Administrator confirms activation.
6. The system changes account status to Active.
7. The system enables authentication and effective permissions.
8. The system sends Staff Account Activated notification.
9. The system records audit events.

### Alternate Flows

- If credentials are not yet set, the system may resend activation invitation instead of activating.
- If role requires scope, activation remains blocked until Facility or Site access is assigned.
- If optional readiness warnings exist, activation may proceed where policy permits.

### Exception Flows

- If mandatory readiness checks fail, activation is blocked.
- If account is Suspended or Deactivated, activation is blocked unless a separate reactivation process exists.
- If Security Service fails to enable authentication, status remains unchanged.
- If user lacks permission, action is denied and logged.

### Outputs

- Staff Account status changed to Active.
- Authentication enabled.
- Effective permissions applied.
- Notifications.
- Audit events.

### UI Behaviour

Activation UI shall show readiness checklist, missing role or scope blockers, credential status, and confirmation action. Activate button shall be disabled when critical blockers exist.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-USR-601 | Staff Account must be Created before activation. | Block activation. | Critical |
| VAL-USR-602 | Staff must have at least one assigned role. | Block activation. | Critical |
| VAL-USR-603 | Required Facility or Site scope must be assigned. | Block activation and show missing scope. | Critical |
| VAL-USR-604 | Credential setup must satisfy password policy. | Block activation or resend setup. | Critical |
| VAL-USR-605 | User must have Staff activation permission. | Deny action and log event. | Critical |

### Business Rules

- BA-02 BR-ORG-005 - Organization Users
- BA-02 BR-ORG-006 - Role-Based Access
- BA-02 BR-SEC-001 - Authentication
- BA-02 BR-SEC-002 - Role-Based Access Control
- BA-02 BR-SEC-003 - Least Privilege
- BA-02 BR-SEC-005 - Password Policy
- BA-02 BR-AUD-003 - Auditable Events

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| staff.lifecycle.view | Organization Administrator | Read | Required to view account status |
| staff.lifecycle.activate | Organization Administrator | Execute | Required to activate Staff Account |
| staff.readiness.view | Organization Administrator | Read | Required to view readiness |
| staff.login.access | Staff User | Execute | Available after activation |

### Security Considerations

Activation shall not occur until role, scope, and credential readiness are satisfied. Authentication access shall use configured password and session policies. All activation attempts shall be auditable.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Staff Account Activated | Staff User | In-App, Email | Account becomes Active | Include login readiness and support guidance |
| Staff Activation Blocked | Organization Administrator | In-App | Readiness checks fail | Include blocker list |
| Staff Credential Setup Required | Staff User | Email, SMS | Credentials incomplete | Include secure setup link |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| StaffActivationRequested | User & Role Management | Security Service, Audit Service |
| StaffAccountActivated | User & Role Management | Security Service, Notification Service, Reporting Service |
| StaffActivationBlocked | User & Role Management | Notification Service, Audit Service |

### Audit Events

| Audit Event | Trigger | Actor | Entity | Data Captured |
|---|---|---|---|---|
| Staff Activation Readiness Checked | Readiness validation executed | Organization Administrator | Staff Account | Readiness result and blockers |
| Staff Account Activated | Status changed to Active | Organization Administrator | Staff Account | Previous status, new status, timestamp |
| Staff Activation Blocked | Activation denied | System | Staff Account | Failed checks and timestamp |

### Reports Generated

- Staff Directory Report
- Access Control Report
- Security Monitoring Report
- Workforce Administration Dashboard

### Related Screens

- Staff Lifecycle
- Staff Readiness Checklist
- Staff Profile
- Staff Directory
- Access Summary

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/staff/{staffId}/readiness | GET | Organization Administrator token | Retrieve activation readiness | 200 OK with readiness checklist |
| /api/v1/staff/{staffId}/activate | POST | Organization Administrator token | Activate Staff Account | 200 OK with active account status |
| /api/v1/staff/{staffId}/effective-permissions | GET | Organization Administrator token | Retrieve effective permissions | 200 OK with permission summary |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Staff | Read | Validate Staff profile | Identity context |
| Staff Account | Read, Update | Update account status | Primary lifecycle entity |
| Staff Role | Read | Validate assigned roles | Readiness |
| Staff Facility Assignment | Read | Validate Facility scope | Conditional |
| Staff Site Assignment | Read | Validate Site scope | Conditional |
| Permission | Read | Validate effective access | Security context |
| Audit Log | Insert | Record activation events | Required |
| Notification | Insert | Queue activation notifications | Required |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Created | Activate Staff Account | Active | Organization Administrator | Readiness checks pass |
| Created | Activation blocked | Created | System | Readiness checks fail |
| Active | Activate Staff Account | Active | Organization Administrator | Duplicate action blocked |
| Suspended | Activate Staff Account | Suspended | Organization Administrator | Reactivation handled separately if supported |
| Deactivated | Activate Staff Account | Deactivated | Organization Administrator | Action blocked |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| USR-601 | Staff Account is not ready for activation. | Readiness blockers exist | Complete listed setup items |
| USR-602 | Staff role is required before activation. | Missing role | Assign role |
| USR-603 | Staff access scope is incomplete. | Missing Facility or Site scope | Assign required scope |
| USR-604 | You do not have permission to activate Staff Accounts. | Missing permission | Request access |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Activate ready Staff | Given readiness checks pass | When activation is confirmed | Then Staff Account status shall become Active |
| Block missing role | Given Staff has no role | When activation is attempted | Then activation shall be blocked |
| Enable login | Given activation succeeds | When Staff user authenticates | Then login shall be permitted subject to credentials |
| Audit activation | Given activation is attempted | When action completes or fails | Then audit history shall record the outcome |

### Dependencies

- Staff Account creation
- Role assignment
- Facility and Site access assignment
- Security Service
- Notification Service
- Audit Service

### Operational Considerations

Activation blockers shall be clear and actionable for Organization Administrators.

### Non-Functional Considerations

Staff activation shall be secure, auditable, reliable, and responsive.

### Assumptions

- Only Active Staff may authenticate.
- Created accounts are not allowed to perform operational actions.
- Required scope depends on assigned role.

### Success Criteria

Only fully configured and authorized Staff Accounts become Active.

### Related Functional Requirements

- FR-USR-001 - Create Staff Account
- FR-USR-003 - Assign Staff Role
- FR-USR-004 - Assign Facility Access
- FR-USR-005 - Assign Site Access
- FR-USR-009 - Reset Staff Credentials

### Notes

Activation is the security checkpoint before Staff operational access.

---

## FR-USR-008 - Suspend Staff Account

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-USR-008 |
| Requirement Name | Suspend Staff Account |
| Functional Module | User & Role Management |
| Business Domain | Staff Identity & Access |
| Business Capability | Staff Lifecycle |
| Requirement Type | Functional |
| Requirement Category | Security |
| Requirement Version | 1.0 |
| Requirement Status | Approved |
| Priority | Critical |
| Complexity | High |
| Release Version | 1.0 |
| Owner | Product Management |

### Traceability References

| Traceability Type | Reference |
|---|---|
| Business Requirement | BA-08 Staff Identity & Access |
| Business Rule | BA-02 BR-SEC-001, BR-SEC-002, BR-SEC-004, BR-SEC-006, BR-SEC-007, BR-SEC-008, BR-AUD-003 |
| Business Process | BA-03 BP-STA-008 Suspend Staff Account |
| Business Process Flow | BA-04 Section 12 User & Role Management Flow |
| Persona | BA-05 Organization Administrator |
| User Journey | BA-06 Section 4 Organization Administrator Journey |
| Stakeholder | BA-07 Organization Administrator, Support Executive |
| Non-Functional Requirement | BA-09 Section 3 Security Requirements |
| Assumption / Constraint / Risk | BA-10 BA-RSK-004, BA-RSK-005 |

### Purpose

To temporarily block Staff login access and operational actions while retaining account history.

### Functional Requirement

The system shall allow an Organization Administrator to suspend an Active Staff Account, block authentication, invalidate active sessions where configured, preserve history, notify stakeholders, and audit the action.

### Business Justification

Suspension protects business data and operations when Staff access must be temporarily restricted due to security, employment, policy, or operational reasons.

### Actors

- Organization Administrator
- Staff User
- Security Service
- Notification Service
- Audit Service

### Preconditions

- Staff Account exists.
- Staff Account is Active.
- User is authenticated.
- User has Staff suspension permission.
- Suspension reason is provided.

### Trigger

Organization Administrator selects Suspend Staff Account.

### In Scope

- Validate suspension eligibility.
- Capture suspension reason.
- Change account status to Suspended.
- Block login and operational actions.
- Invalidate sessions where configured.
- Notify Staff user and administrator.
- Record audit events.

### Out of Scope

- Permanent deactivation.
- Staff profile deletion.
- Role removal.
- Customer account suspension.
- Organization-wide lockout policy configuration.

### Inputs

- Staff ID
- Suspension reason
- Suspension category
- Effective date and time
- Internal notes

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Staff ID | Staff Account to suspend | Identifier | Yes | Organization Administrator | Must exist and be Active | Target account |
| Suspension Reason | Reason for suspension | Text | Yes | Organization Administrator | Required and length validation | Audit field |
| Suspension Category | Security or business category | Enum | Yes | Organization Administrator | Must use configured category | Reporting dimension |
| Effective DateTime | Suspension effective timestamp | DateTime | Yes | Organization Administrator / System | Current or future as policy allows | Immediate by default |
| Internal Notes | Restricted administrative notes | Text | No | Organization Administrator | Length validation | Internal visibility |

### Main Flow

1. Organization Administrator opens Staff lifecycle actions.
2. Organization Administrator selects Suspend Staff Account.
3. The system validates account status, permission, and Organization scope.
4. Organization Administrator enters reason and confirms suspension.
5. The system changes Staff Account status to Suspended.
6. The system blocks authentication and operational access.
7. The system invalidates active sessions where configured.
8. The system sends suspension notifications.
9. The system records audit events.

### Alternate Flows

- If suspension is scheduled, access remains active until effective timestamp.
- If Security Service triggers suspension after account lockout, the system records the automated reason.
- If read-only historical visibility is needed, administrators may still view activity and profile.

### Exception Flows

- If account is not Active, suspension is blocked.
- If reason is missing, confirmation is blocked.
- If Security Service fails to block access, status update is rolled back or marked failed.
- If user lacks permission, action is denied and logged.

### Outputs

- Staff Account status changed to Suspended.
- Login and operational access blocked.
- Sessions invalidated where configured.
- Notifications.
- Audit events.

### UI Behaviour

Suspend Staff Account shall require reason capture and confirmation. Suspended accounts shall show clear status badges and disabled operational access indicators.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-USR-701 | Staff Account must be Active to suspend. | Block suspension. | Critical |
| VAL-USR-702 | Suspension reason is mandatory. | Block confirmation. | Critical |
| VAL-USR-703 | Suspended accounts must not authenticate. | Block login. | Critical |
| VAL-USR-704 | Active sessions must follow configured session invalidation policy. | Invalidate or refresh sessions. | Critical |
| VAL-USR-705 | Suspension action must be audited. | Block completion if audit write fails. | Critical |

### Business Rules

- BA-02 BR-SEC-001 - Authentication
- BA-02 BR-SEC-002 - Role-Based Access Control
- BA-02 BR-SEC-004 - Organization Data Isolation
- BA-02 BR-SEC-006 - Account Lockout
- BA-02 BR-SEC-007 - Session Management
- BA-02 BR-SEC-008 - Permission Changes
- BA-02 BR-AUD-003 - Auditable Events

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| staff.lifecycle.view | Organization Administrator | Read | Required to view account status |
| staff.lifecycle.suspend | Organization Administrator | Execute | Required to suspend account |
| staff.sessions.invalidate | Security Service | Execute | Required to invalidate active sessions |
| staff.suspended.view | Organization Administrator | Read | Required for historical review |

### Security Considerations

Suspension shall immediately prevent access according to security policy. Active session behavior must be controlled to prevent continued unauthorized use. Historical records shall remain protected and auditable.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Staff Account Suspended | Staff User | Email, SMS | Account becomes Suspended | Include security notice and support contact |
| Staff Suspension Completed | Organization Administrator | In-App, Email | Suspension succeeds | Include staff name and timestamp |
| Staff Session Invalidated | Staff User | Email | Active session terminated | Include security reason where policy allows |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| StaffSuspensionRequested | User & Role Management | Security Service, Audit Service |
| StaffAccountSuspended | User & Role Management | Security Service, Notification Service, Reporting Service |
| StaffSessionsInvalidated | Security Service | Audit Service |

### Audit Events

| Audit Event | Trigger | Actor | Entity | Data Captured |
|---|---|---|---|---|
| Staff Suspension Requested | Suspension initiated | Organization Administrator | Staff Account | Reason, category, effective date |
| Staff Account Suspended | Status changed | Organization Administrator / System | Staff Account | Previous status, new status, timestamp |
| Staff Sessions Invalidated | Session invalidation executed | Security Service | Login History | Session references and outcome |

### Reports Generated

- Staff Directory Report
- Security Monitoring Report
- Access Control Report
- Audit Trail Report

### Related Screens

- Staff Lifecycle
- Staff Profile
- Staff Activity
- Security Monitoring
- Audit History

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/staff/{staffId}/suspend | POST | Organization Administrator token | Suspend Staff Account | 200 OK with suspended status |
| /api/v1/staff/{staffId}/sessions | DELETE | Security Service token | Invalidate active Staff sessions | 200 OK with invalidation result |
| /api/v1/staff/{staffId} | GET | Authorized token | Retrieve Staff Account status | 200 OK with Staff Account resource |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Staff Account | Read, Update | Update lifecycle status | Primary entity |
| Staff | Read | Validate Staff scope | Identity context |
| Login History | Update, Insert | Record session invalidation | Security entity |
| Audit Log | Insert | Record suspension events | Required |
| Notification | Insert | Queue suspension notifications | Required |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Active | Suspend Staff Account | Suspended | Organization Administrator | Valid reason and permission |
| Active | Schedule suspension | Active with Scheduled Suspension | Organization Administrator | Future effective timestamp |
| Active with Scheduled Suspension | Effective time reached | Suspended | System | Schedule due |
| Created | Suspend Staff Account | Created | Organization Administrator | Action blocked |
| Deactivated | Suspend Staff Account | Deactivated | Organization Administrator | Action blocked |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| USR-701 | Only Active Staff Accounts can be suspended. | Invalid account status | Review status |
| USR-702 | Suspension reason is required. | Missing reason | Enter suspension reason |
| USR-703 | Staff access could not be blocked. | Security Service failure | Retry or contact support |
| USR-704 | You do not have permission to suspend Staff Accounts. | Missing permission | Request access |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Suspend Active Staff | Given Staff Account is Active and user has permission | When suspension is confirmed | Then status shall become Suspended |
| Block authentication | Given Staff Account is Suspended | When Staff attempts login | Then authentication shall be blocked |
| Invalidate sessions | Given session invalidation is configured | When suspension completes | Then active sessions shall be invalidated |
| Audit suspension | Given suspension is attempted | When action completes or fails | Then audit history shall record the outcome |

### Dependencies

- Security Service
- Session management
- Notification Service
- Audit Service
- Staff lifecycle model

### Operational Considerations

Suspension should be visible in Staff Directory and Security Monitoring immediately.

### Non-Functional Considerations

Suspension shall be secure, reliable, auditable, and fast enough to prevent unauthorized continued access.

### Assumptions

- Suspended accounts retain historical activity.
- Suspended accounts cannot authenticate.
- Reactivation may be handled through a governed future process.

### Success Criteria

Staff access is safely and traceably blocked without deleting account history.

### Related Functional Requirements

- FR-USR-007 - Activate Staff Account
- FR-USR-009 - Reset Staff Credentials
- FR-USR-010 - Deactivate Staff Account
- FR-USR-011 - View Staff Activity

### Notes

Suspension is temporary access restriction, not permanent deactivation.

---

## FR-USR-009 - Reset Staff Credentials

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-USR-009 |
| Requirement Name | Reset Staff Credentials |
| Functional Module | User & Role Management |
| Business Domain | Staff Identity & Access |
| Business Capability | Security Management |
| Requirement Type | Functional |
| Requirement Category | Security |
| Requirement Version | 1.0 |
| Requirement Status | Approved |
| Priority | Critical |
| Complexity | High |
| Release Version | 1.0 |
| Owner | Product Management |

### Traceability References

| Traceability Type | Reference |
|---|---|
| Business Requirement | BA-08 Staff Identity & Access |
| Business Rule | BA-02 BR-SEC-001, BR-SEC-005, BR-SEC-006, BR-SEC-007, BR-SEC-008, BR-SEC-009, BR-AUD-003 |
| Business Process | BA-03 BP-STA-009 Reset Staff Credentials |
| Business Process Flow | BA-04 Section 12 User & Role Management Flow |
| Persona | BA-05 Organization Administrator, Staff User |
| User Journey | BA-06 Section 4 Organization Administrator Journey |
| Stakeholder | BA-07 Organization Administrator, Support Executive |
| Non-Functional Requirement | BA-09 Section 3.3 Password Policies, Section 3.4 Session Management |
| Assumption / Constraint / Risk | BA-10 BA-RSK-004 |

### Purpose

To securely reset Staff credentials when access recovery, security incident response, or administrative intervention is required.

### Functional Requirement

The system shall allow authorized users to initiate Staff credential reset, invalidate applicable credentials or sessions, enforce password policy, notify Staff securely, and audit the reset.

### Business Justification

Credential reset protects Staff access continuity while maintaining strong security controls against unauthorized access and account compromise.

### Actors

- Organization Administrator
- Staff User
- Security Service
- Notification Service
- Audit Service

### Preconditions

- Staff Account exists.
- Staff Account is not Deactivated unless policy permits administrative reset for recovery.
- User is authenticated.
- User has credential reset permission.
- Password and session policies are configured.

### Trigger

Organization Administrator selects Reset Staff Credentials or Staff user initiates approved recovery flow where enabled.

### In Scope

- Initiate credential reset.
- Generate secure reset token.
- Enforce token expiry.
- Force password change where required.
- Invalidate sessions where configured.
- Notify Staff user securely.
- Record audit events.

### Out of Scope

- MFA enrollment beyond future enhancement.
- Platform Administrator credential reset.
- Customer password reset.
- Password policy configuration.
- Identity provider integration configuration.

### Inputs

- Staff ID
- Reset reason
- Reset channel
- Force password change flag
- Session invalidation preference
- Request source

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Staff ID | Staff Account requiring reset | Identifier | Yes | Organization Administrator / System | Must exist within Organization scope | Target account |
| Reset Reason | Reason for reset | Text | Conditional | Organization Administrator | Required for administrative reset | Audit field |
| Reset Channel | Delivery channel | Enum | Yes | Organization Administrator / System | Must be enabled and verified | Email or SMS |
| Force Password Change | Requires password change after reset | Boolean | Yes | Organization Administrator / Policy | Must follow policy | Security control |
| Session Invalidation | Whether active sessions are invalidated | Boolean | Yes | Security Policy | Must follow policy | Security control |
| Request Source | Admin or self-service source | Enum | Yes | System | Must be valid source | Audit context |

### Main Flow

1. Authorized user initiates credential reset.
2. The system validates Staff Account status, Organization scope, permission, and reset policy.
3. The system generates a secure reset token with expiry.
4. The system invalidates existing reset tokens.
5. The system invalidates active sessions where configured.
6. The system sends reset instructions through approved channel.
7. Staff user completes credential setup using the secure token.
8. The system enforces password policy.
9. The system updates credential status.
10. The system records audit and security events.

### Alternate Flows

- If Staff user initiates self-service recovery, verification rules are applied before reset token generation.
- If reset token expires, user must request a new reset.
- If account is Suspended, reset may be allowed but login remains blocked until account is Active.

### Exception Flows

- If Staff Account is Deactivated, reset is blocked unless policy allows recovery.
- If reset channel is unavailable or unverified, reset cannot be sent.
- If password does not meet policy, credential update is rejected.
- If token is invalid or expired, reset completion is blocked.

### Outputs

- Credential reset token generated.
- Existing tokens invalidated.
- Sessions invalidated where applicable.
- Credential status updated.
- Notifications.
- Audit and security events.

### UI Behaviour

Credential reset UI shall require confirmation and reason for administrative resets. Reset completion screens shall not expose token details. Password policy guidance shall be shown during password setup.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-USR-801 | Reset request must be authorized. | Deny action and log event. | Critical |
| VAL-USR-802 | Reset token must be unique, secure, single-use, and time-bound. | Reject invalid token. | Critical |
| VAL-USR-803 | New password must comply with password policy. | Reject password and show policy guidance. | Critical |
| VAL-USR-804 | Reset channel must be enabled and valid. | Block reset notification. | High |
| VAL-USR-805 | Credential reset must be audited. | Block completion if audit write fails. | Critical |

### Business Rules

- BA-02 BR-SEC-001 - Authentication
- BA-02 BR-SEC-005 - Password Policy
- BA-02 BR-SEC-006 - Account Lockout
- BA-02 BR-SEC-007 - Session Management
- BA-02 BR-SEC-008 - Permission Changes
- BA-02 BR-SEC-009 - Sensitive Data Protection
- BA-02 BR-AUD-003 - Auditable Events

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| staff.credentials.reset | Organization Administrator | Execute | Required for administrative reset |
| staff.credentials.self-reset | Staff User | Execute | Self-service reset where enabled |
| staff.sessions.invalidate | Security Service | Execute | Required when policy invalidates sessions |
| audit.staff.credentials.read | Organization Administrator | Read | Required to view credential audit |

### Security Considerations

Credential reset shall use secure tokens, expiry, single-use validation, protected delivery channels, password policy enforcement, session controls, and audit logging. Reset tokens shall never be exposed in logs.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Credential Reset Initiated | Staff User | Email, SMS | Reset token generated | Include secure reset link and expiry |
| Credential Reset Completed | Staff User | Email, SMS | Password updated | Include security confirmation |
| Credential Reset Failed | Organization Administrator | In-App | Reset cannot be completed | Include non-sensitive failure reason |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| StaffCredentialResetRequested | User & Role Management | Security Service, Audit Service |
| StaffCredentialResetTokenGenerated | Security Service | Notification Service |
| StaffCredentialResetCompleted | Security Service | Audit Service, Notification Service |

### Audit Events

| Audit Event | Trigger | Actor | Entity | Data Captured |
|---|---|---|---|---|
| Staff Credential Reset Requested | Reset initiated | Organization Administrator / Staff User | Staff Account | Request source, reason, channel |
| Staff Credential Reset Token Generated | Token generated | Security Service | Staff Account | Token reference, expiry, channel |
| Staff Credential Reset Completed | Password updated | Staff User | Staff Account | Completion timestamp and source |
| Staff Credential Reset Failed | Reset failure | System | Staff Account | Failure category and timestamp |

### Reports Generated

- Security Monitoring Report
- Staff Activity Report
- Credential Reset Report
- Audit Trail Report

### Related Screens

- Staff Profile
- Credential Reset
- Password Setup
- Security Monitoring
- Audit History

### Related APIs

> **Superseded for self-service Authentication.** HTTP contracts for login
> are not listed here. Self-service recovery is frozen in
> `docs/architecture/AUTH_CONTRACT_FREEZE.md` as
> `POST /api/v1/auth/password-reset` and
> `POST /api/v1/auth/password-reset/confirm`.
> Administrative reset remains API-03-009
> (`POST /api/v1/identity/users/{user_id}/credential-reset`), not the
> FR table path below. Treat the table as historical FR mapping only.

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/staff/{staffId}/credentials/reset | POST | Organization Administrator token | Initiate administrative credential reset | 202 Accepted with reset status |
| /api/v1/auth/password-reset | POST | Public verified flow | Initiate self-service password reset | 202 Accepted |
| /api/v1/auth/password-reset/confirm | POST | Reset token | Complete password reset | 200 OK with completion status |
| /api/v1/staff/{staffId}/sessions | DELETE | Security Service token | Invalidate active sessions | 200 OK with invalidation result |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Staff Account | Read, Update | Manage credential state | Primary entity |
| Login History | Insert, Update | Record reset and session activity | Security entity |
| Audit Log | Insert | Record credential events | Required |
| Notification | Insert | Queue reset notifications | Required |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Credentials Active | Reset requested | Reset Pending | Organization Administrator / Staff User | Authorized request |
| Reset Pending | Token used successfully | Credentials Active | Staff User | Password policy satisfied |
| Reset Pending | Token expired | Reset Expired | System | Expiry reached |
| Reset Pending | Reset cancelled | Credentials Active | Organization Administrator / System | Cancellation allowed |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| USR-801 | Credential reset is not authorized. | Missing permission or verification | Request authorized reset |
| USR-802 | Reset link is invalid or expired. | Invalid token | Request new reset |
| USR-803 | Password does not meet security policy. | Password validation failure | Enter compliant password |
| USR-804 | Reset instructions could not be delivered. | Notification failure | Verify contact channel or retry |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Initiate reset | Given user has credential reset permission | When reset is requested | Then secure reset instructions shall be sent |
| Enforce password policy | Given Staff enters a new password | When reset is confirmed | Then password policy shall be enforced |
| Block expired token | Given reset token is expired | When used | Then reset shall be rejected |
| Audit reset | Given reset is requested or completed | When action occurs | Then audit history shall record credential event |

### Dependencies

- Security Service
- Password policy
- Session management
- Notification Service
- Audit Service

### Operational Considerations

Support teams shall be able to see reset status without viewing sensitive tokens or passwords.

### Non-Functional Considerations

Credential reset shall be secure, reliable, privacy-preserving, auditable, and resistant to token misuse.

### Assumptions

- Reset tokens are single-use and time-bound.
- Passwords are never stored or logged in plain text.
- Suspended accounts may reset credentials but cannot log in until Active.

### Success Criteria

Staff credentials can be securely reset without compromising authentication security or auditability.

### Related Functional Requirements

- FR-USR-001 - Create Staff Account
- FR-USR-007 - Activate Staff Account
- FR-USR-008 - Suspend Staff Account
- FR-USR-011 - View Staff Activity

### Notes

Credential reset is security-sensitive and must avoid exposing secrets in notifications, logs, or audit details.

---

## FR-USR-010 - Deactivate Staff Account

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-USR-010 |
| Requirement Name | Deactivate Staff Account |
| Functional Module | User & Role Management |
| Business Domain | Staff Identity & Access |
| Business Capability | Staff Lifecycle |
| Requirement Type | Functional |
| Requirement Category | Security |
| Requirement Version | 1.0 |
| Requirement Status | Approved |
| Priority | Critical |
| Complexity | High |
| Release Version | 1.0 |
| Owner | Product Management |

### Traceability References

| Traceability Type | Reference |
|---|---|
| Business Requirement | BA-08 Staff Identity & Access |
| Business Rule | BA-02 BR-ORG-005, BR-ORG-006, BR-SEC-001, BR-SEC-002, BR-SEC-004, BR-SEC-008, BR-AUD-003, BR-AUD-005 |
| Business Process | BA-03 BP-STA-010 Deactivate Staff Account |
| Business Process Flow | BA-04 Section 12 User & Role Management Flow |
| Persona | BA-05 Organization Administrator |
| User Journey | BA-06 Section 4 Organization Administrator Journey |
| Stakeholder | BA-07 Organization Administrator, External Auditor |
| Non-Functional Requirement | BA-09 Section 3 Security Requirements, Section 10 Data Management |
| Assumption / Constraint / Risk | BA-10 BA-RSK-007 |

### Purpose

To permanently remove operational access for Staff while retaining historical identity, activity, and audit records.

### Functional Requirement

The system shall allow an Organization Administrator to deactivate an eligible Staff Account, block future authentication, end active access assignments where required, preserve historical records, and audit the lifecycle change.

### Business Justification

Deactivation supports employee exits, role termination, and long-term access control without deleting historical business transaction accountability.

### Actors

- Organization Administrator
- Staff User
- Security Service
- Notification Service
- Audit Service

### Preconditions

- Staff Account exists.
- Staff Account is not already Deactivated.
- User is authenticated.
- User has Staff deactivation permission.
- Deactivation reason is provided.
- Required ownership or operational dependency checks are available.

### Trigger

Organization Administrator selects Deactivate Staff Account.

### In Scope

- Validate deactivation eligibility.
- Capture deactivation reason.
- Change account status to Deactivated.
- Block authentication and operational actions.
- End or retain access assignments according to policy.
- Preserve historical records.
- Notify stakeholders and audit action.

### Out of Scope

- Physical deletion of Staff records.
- Customer account deactivation.
- Payroll or HR exit management.
- Reassigning business ownership beyond dependency warnings.
- Purging audit records.

### Inputs

- Staff ID
- Deactivation reason
- Deactivation category
- Effective date and time
- Confirmation
- Internal notes

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Staff ID | Account to deactivate | Identifier | Yes | Organization Administrator | Must exist and not be Deactivated | Target account |
| Deactivation Reason | Reason for deactivation | Text | Yes | Organization Administrator | Required and length validation | Audit field |
| Deactivation Category | Business or security category | Enum | Yes | Organization Administrator | Must use configured category | Reporting dimension |
| Effective DateTime | Deactivation timestamp | DateTime | Yes | Organization Administrator / System | Current or future as policy allows | Immediate by default |
| Confirmation | Explicit confirmation | Boolean | Yes | Organization Administrator | Must be confirmed | High-risk control |
| Internal Notes | Restricted notes | Text | No | Organization Administrator | Length validation | Internal visibility |

### Main Flow

1. Organization Administrator opens Staff lifecycle actions.
2. Organization Administrator selects Deactivate Staff Account.
3. The system validates account status, permission, Organization scope, active ownership responsibilities, approval duties, and operational dependencies.
4. The system displays deactivation impact and blockers.
5. Organization Administrator enters reason and confirms deactivation.
6. The system changes Staff Account status to Deactivated.
7. The system blocks authentication and operational access.
8. The system invalidates active sessions.
9. The system preserves historical Staff, activity, and audit records.
10. The system sends notifications and records audit events.

### Alternate Flows

- If deactivation is scheduled, account remains active or suspended until effective timestamp.
- If unresolved responsibilities exist, deactivation may be blocked or require reassignment.
- If account is already Suspended, the system may allow deactivation after confirmation.

### Exception Flows

- If account is already Deactivated, duplicate action is blocked.
- If Staff owns required active responsibilities, deactivation is blocked until reassignment.
- If Security Service fails to block access, deactivation is not finalized.
- If user lacks permission, action is denied and logged.

### Outputs

- Staff Account status changed to Deactivated.
- Authentication blocked.
- Sessions invalidated.
- Access assignments ended or retained historically.
- Notifications.
- Audit events.

### UI Behaviour

Deactivate Staff Account shall display high-risk confirmation, impact summary, responsibility blockers, and retention notice. Deactivated Staff profiles shall be read-only and visibly marked.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-USR-901 | Staff Account must not already be Deactivated. | Block duplicate deactivation. | Critical |
| VAL-USR-902 | Deactivation reason and confirmation are mandatory. | Block deactivation. | Critical |
| VAL-USR-903 | Required operational responsibilities must be reassigned before deactivation where configured. | Block deactivation and list blockers. | Critical |
| VAL-USR-904 | Deactivated accounts must not authenticate. | Block login. | Critical |
| VAL-USR-905 | Historical Staff records must be retained. | Prevent destructive operations. | Critical |

### Business Rules

- BA-02 BR-ORG-005 - Organization Users
- BA-02 BR-ORG-006 - Role-Based Access
- BA-02 BR-SEC-001 - Authentication
- BA-02 BR-SEC-002 - Role-Based Access Control
- BA-02 BR-SEC-004 - Organization Data Isolation
- BA-02 BR-SEC-008 - Permission Changes
- BA-02 BR-AUD-003 - Auditable Events
- BA-02 BR-AUD-005 - Audit Retention

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| staff.lifecycle.view | Organization Administrator | Read | Required to view account status |
| staff.lifecycle.deactivate | Organization Administrator | Execute | Required to deactivate account |
| staff.deactivation.impact.view | Organization Administrator | Read | Required to view impact |
| staff.deactivated.view | Organization Administrator, Auditor | Read | Read-only historical access |

### Security Considerations

Deactivation shall permanently block login access while retaining auditable history. Deactivated accounts shall not be physically deleted through standard application functionality.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Staff Account Deactivated | Staff User | Email, SMS | Account becomes Deactivated | Include access termination notice |
| Staff Deactivation Completed | Organization Administrator | In-App, Email | Deactivation succeeds | Include timestamp |
| Staff Deactivation Blocked | Organization Administrator | In-App | Dependency checks fail | Include blocker list |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| StaffDeactivationRequested | User & Role Management | Security Service, Audit Service |
| StaffAccountDeactivated | User & Role Management | Security Service, Reporting Service, Notification Service |
| StaffDeactivationBlocked | User & Role Management | Notification Service, Audit Service |

### Audit Events

| Audit Event | Trigger | Actor | Entity | Data Captured |
|---|---|---|---|---|
| Staff Deactivation Eligibility Checked | Validation executed | Organization Administrator | Staff Account | Eligibility result and blockers |
| Staff Account Deactivated | Status changed | Organization Administrator | Staff Account | Previous status, new status, reason |
| Deactivated Staff Viewed | Historical profile opened | Authorized user | Staff Account | Actor, timestamp, purpose |

### Reports Generated

- Staff Directory Report
- Access Control Report
- Security Monitoring Report
- Deactivated Staff Register
- Audit Trail Report

### Related Screens

- Staff Lifecycle
- Deactivation Confirmation
- Staff Profile
- Staff Activity
- Audit History

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/staff/{staffId}/deactivation-impact | GET | Organization Administrator token | Retrieve deactivation impact | 200 OK with impact summary |
| /api/v1/staff/{staffId}/deactivate | POST | Organization Administrator token | Deactivate Staff Account | 200 OK with deactivated status |
| /api/v1/staff/{staffId}/sessions | DELETE | Security Service token | Invalidate active sessions | 200 OK with invalidation result |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Staff Account | Read, Update | Update lifecycle status | Primary entity |
| Staff | Read | Preserve identity profile | Historical context |
| Staff Role | Read, Update | End or retain role assignments historically | Policy-driven |
| Staff Facility Assignment | Read, Update | End or retain Facility assignments historically | Policy-driven |
| Staff Site Assignment | Read, Update | End or retain Site assignments historically | Policy-driven |
| Login History | Insert, Update | Record session invalidation | Security entity |
| Audit Log | Insert | Record deactivation events | Required |
| Notification | Insert | Queue deactivation notices | Required |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Created | Deactivate Staff Account | Deactivated | Organization Administrator | Eligibility checks pass |
| Active | Deactivate Staff Account | Deactivated | Organization Administrator | Eligibility checks pass |
| Suspended | Deactivate Staff Account | Deactivated | Organization Administrator | Eligibility checks pass |
| Active | Deactivation blocked | Active | System | Dependencies require reassignment |
| Deactivated | Deactivate Staff Account | Deactivated | Organization Administrator | Duplicate action blocked |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| USR-901 | Staff Account cannot be deactivated because blockers exist. | Responsibility dependencies | Resolve blockers |
| USR-902 | Staff Account is already deactivated. | Duplicate action | No action required |
| USR-903 | Deactivation reason is required. | Missing reason | Enter reason |
| USR-904 | You do not have permission to deactivate Staff Accounts. | Missing permission | Request access |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Deactivate eligible Staff | Given Staff passes dependency checks | When deactivation is confirmed | Then account status shall become Deactivated |
| Block authentication | Given account is Deactivated | When Staff attempts login | Then authentication shall be blocked |
| Preserve history | Given deactivation succeeds | When historical activity is viewed | Then records shall remain available to authorized users |
| Audit deactivation | Given deactivation is attempted | When action completes or fails | Then audit history shall record the event |

### Dependencies

- Security Service
- Staff role and access assignments
- Facility and Site responsibility checks
- Audit Service
- Notification Service

### Operational Considerations

Deactivation blockers should identify responsibilities that must be reassigned before access termination.

### Non-Functional Considerations

Deactivation shall be secure, auditable, reliable, privacy-preserving, and compliant with retention requirements.

### Assumptions

- Deactivation is not physical deletion.
- Historical records are retained for audit.
- Deactivated accounts cannot authenticate.

### Success Criteria

Staff access is permanently disabled while historical accountability remains intact.

### Related Functional Requirements

- FR-USR-008 - Suspend Staff Account
- FR-USR-011 - View Staff Activity
- FR-USR-012 - View Staff Directory
- FR-AUD-001 - Record Audit Events

### Notes

Deactivation is the terminal Staff Account lifecycle state for Version 1.0.

---

## FR-USR-011 - View Staff Activity

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-USR-011 |
| Requirement Name | View Staff Activity |
| Functional Module | User & Role Management |
| Business Domain | Staff Identity & Access |
| Business Capability | Security Monitoring |
| Requirement Type | Functional |
| Requirement Category | Reporting |
| Requirement Version | 1.0 |
| Requirement Status | Approved |
| Priority | Critical |
| Complexity | High |
| Release Version | 1.0 |
| Owner | Product Management |

### Traceability References

| Traceability Type | Reference |
|---|---|
| Business Requirement | BA-08 Staff Identity & Access |
| Business Rule | BA-02 BR-SEC-001, BR-SEC-006, BR-SEC-007, BR-SEC-008, BR-AUD-001, BR-AUD-003, BR-AUD-006 |
| Business Process | BA-03 BP-STA-011 View Staff Activity |
| Business Process Flow | BA-04 Section 12 User & Role Management Flow |
| Persona | BA-05 Organization Administrator, Support Executive, External Auditor |
| User Journey | BA-06 Section 4 Organization Administrator Journey |
| Stakeholder | BA-07 Organization Administrator, Support Executive, External Auditor |
| Non-Functional Requirement | BA-09 Section 3.8 Audit Logging, Section 7 Operational Requirements |
| Assumption / Constraint / Risk | BA-10 BA-RSK-004, BA-RSK-007 |

### Purpose

To provide authorized visibility into Staff login, access, security, and business activity history.

### Functional Requirement

The system shall allow authorized users to view, filter, search, and export Staff Activity records according to audit access permissions and data scope.

### Business Justification

Staff Activity visibility supports operational governance, security monitoring, accountability, support investigations, and audit readiness.

### Actors

- Organization Administrator
- Support Executive
- External Auditor
- Security Service
- Audit Service
- Reporting Service

### Preconditions

- Staff activity records exist.
- User is authenticated.
- User has Staff activity view permission.
- Audit access rules are configured.
- User scope covers requested Staff or Organization.

### Trigger

Authorized user opens Staff Activity or Security Monitoring.

### In Scope

- View login and logout events.
- View failed authentication attempts.
- View business transactions.
- View configuration changes.
- View approval decisions.
- Filter and export activity where permitted.
- Audit activity viewing.

### Out of Scope

- Editing audit records.
- Deleting activity history.
- Real-time threat analytics beyond available logs.
- System infrastructure log management.

### Inputs

- Staff ID
- Organization ID
- Facility or Site scope
- Date range
- Activity category
- Outcome filter
- Export request

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Staff ID | Staff activity subject | Identifier | Conditional | User filter | Must be within authorized scope | Optional for aggregate view |
| Date Range | Activity period | Date Range | Yes | User | Must be within reporting limits | Required |
| Activity Category | Activity type | Enum | No | User | Must be supported category | Login, transaction, configuration |
| Outcome Filter | Success or failure status | Enum | No | User | Must be valid outcome | Supports investigations |
| Scope Filter | Organization, Facility, or Site scope | Identifier | No | User | Must match user permissions | Limits data |
| Export Request | Export action | Boolean | No | User | Requires export permission | Optional |

### Main Flow

1. Authorized user opens Staff Activity.
2. The system validates authentication, permission, and data scope.
3. User enters filters such as Staff, date range, activity category, outcome, Facility, or Site.
4. The system retrieves matching Staff Activity and Audit records.
5. The system masks or hides sensitive fields according to permissions.
6. The system displays activity records with timestamps, actor, action, scope, source, and outcome.
7. User exports activity where permitted.
8. The system records audit event for activity access and export.

### Alternate Flows

- If Staff ID is not selected, the system displays Organization-scoped activity summary where permitted.
- If user has auditor role, the system provides read-only compliance view.
- If export is not permitted, export action remains disabled.

### Exception Flows

- If date range exceeds limits, the system blocks query.
- If user lacks audit access, activity view is denied.
- If no records match filters, empty state is displayed.
- If reporting source is unavailable, the system displays service-unavailable message and logs failure.

### Outputs

- Staff Activity list.
- Filtered security and audit records.
- Export file where permitted.
- Audit event for view or export.

### UI Behaviour

Staff Activity shall display searchable and filterable activity records with pagination, sorting, date range controls, outcome indicators, and export controls. Sensitive data shall be masked where required.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-USR-1001 | User must have Staff activity view permission. | Deny access and log event. | Critical |
| VAL-USR-1002 | Activity results must be scoped to authorized Organization, Facility, or Site. | Filter or block unauthorized scope. | Critical |
| VAL-USR-1003 | Date range must be valid and within configured limits. | Block query. | High |
| VAL-USR-1004 | Export requires explicit export permission. | Disable export or deny action. | High |
| VAL-USR-1005 | Audit records must not be modified through activity view. | Read-only enforcement. | Critical |

### Business Rules

- BA-02 BR-SEC-001 - Authentication
- BA-02 BR-SEC-006 - Account Lockout
- BA-02 BR-SEC-007 - Session Management
- BA-02 BR-SEC-008 - Permission Changes
- BA-02 BR-AUD-001 - Audit Logging
- BA-02 BR-AUD-003 - Auditable Events
- BA-02 BR-AUD-006 - Audit Access

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| staff.activity.view | Organization Administrator | Read | Organization-scoped activity access |
| staff.activity.security-view | Support Executive | Read | Support-scoped activity access |
| staff.activity.audit-view | External Auditor | Read | Read-only audit access |
| staff.activity.export | Authorized user | Export | Required for exports |

### Security Considerations

Staff Activity contains sensitive security and behavior data. Access shall be role-controlled, scoped, masked where required, and itself audited. Audit records shall be immutable.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Suspicious Staff Activity Detected | Organization Administrator | In-App, Email | Failed login or policy threshold reached | Include non-sensitive activity summary |
| Staff Activity Exported | Organization Administrator | In-App | Export generated | Include export timestamp and requester |
| Staff Activity Access Denied | Security Administrator / Audit Service | System Event | Unauthorized access attempt | Include attempted scope |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| StaffActivityViewed | User & Role Management | Audit Service |
| StaffActivityExported | User & Role Management | Audit Service, Reporting Service |
| SuspiciousStaffActivityDetected | Security Service | Notification Service, Audit Service |

### Audit Events

| Audit Event | Trigger | Actor | Entity | Data Captured |
|---|---|---|---|---|
| Staff Activity Viewed | Activity screen opened | Authorized user | Login History, Audit Log | Filters, scope, timestamp |
| Staff Activity Exported | Export requested | Authorized user | Audit Log | Export filters, format, timestamp |
| Staff Activity Access Denied | Unauthorized access attempted | User | Audit Log | Requested scope and reason |

### Reports Generated

- Staff Activity Report
- Security Monitoring Report
- Access Control Report
- Audit Trail Report

### Related Screens

- Staff Activity
- Security Monitoring
- Staff Profile
- Staff Directory
- Audit History

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/staff/{staffId}/activity | GET | Authorized token | Retrieve activity for Staff | 200 OK with activity list |
| /api/v1/staff/activity | GET | Authorized token | Retrieve scoped Staff activity | 200 OK with activity list |
| /api/v1/staff/activity/export | POST | Authorized token | Export Staff activity | 202 Accepted with export status |
| /api/v1/security/events | GET | Authorized token | Retrieve security events | 200 OK with event list |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Staff | Read | Resolve Staff subject | Identity context |
| Staff Account | Read | Display account status | Security context |
| Login History | Read | Retrieve authentication events | Security source |
| Audit Log | Read, Insert | Retrieve activity and record access | Immutable |
| Permission | Read | Validate activity view/export access | Authorization |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Activity Not Loaded | Search activity | Activity Loaded | Authorized user | Valid filters |
| Activity Loaded | Apply filters | Activity Filtered | Authorized user | Valid criteria |
| Activity Loaded | Export requested | Export Pending | Authorized user | Export permission |
| Export Pending | Export completed | Export Available | Reporting Service | Export generated |
| Activity Loaded | Unauthorized export attempted | Activity Loaded | User | Export denied and logged |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| USR-1001 | You do not have permission to view Staff Activity. | Missing permission | Request access |
| USR-1002 | Selected activity scope is not authorized. | Scope violation | Adjust filters |
| USR-1003 | Date range exceeds allowed limit. | Invalid date range | Select smaller range |
| USR-1004 | Staff Activity is temporarily unavailable. | Reporting source failure | Retry later |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| View Staff Activity | Given user has activity view permission | When valid filters are submitted | Then the system shall display scoped Staff Activity |
| Enforce audit scope | Given requested scope is unauthorized | When activity is requested | Then access shall be denied or data filtered |
| Export activity | Given user has export permission | When export is requested | Then the system shall generate activity export |
| Audit access | Given Staff Activity is viewed or exported | When action completes | Then access shall be audited |

### Dependencies

- Audit Service
- Security Service
- Reporting Service
- Permission model
- Login History

### Operational Considerations

Activity retrieval should support pagination, filtering, export tracking, and support-friendly correlation identifiers.

### Non-Functional Considerations

Staff Activity shall support auditability, security, performance, data retention, privacy, and reporting scalability.

### Assumptions

- Audit records are immutable.
- Activity access is itself auditable.
- Export may be restricted by policy.

### Success Criteria

Authorized stakeholders can investigate Staff behavior and access activity without compromising audit integrity or data privacy.

### Related Functional Requirements

- FR-USR-003 - Assign Staff Role
- FR-USR-006 - Configure Staff Permissions
- FR-USR-008 - Suspend Staff Account
- FR-USR-009 - Reset Staff Credentials
- FR-AUD-001 - Record Audit Events

### Notes

Staff Activity is security and audit focused; it must remain read-only.

---

## FR-USR-012 - View Staff Directory

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-USR-012 |
| Requirement Name | View Staff Directory |
| Functional Module | User & Role Management |
| Business Domain | Staff Identity & Access |
| Business Capability | Identity Management |
| Requirement Type | Functional |
| Requirement Category | Reporting |
| Requirement Version | 1.0 |
| Requirement Status | Approved |
| Priority | High |
| Complexity | Medium |
| Release Version | 1.0 |
| Owner | Product Management |

### Traceability References

| Traceability Type | Reference |
|---|---|
| Business Requirement | BA-08 Staff Identity & Access |
| Business Rule | BA-02 BR-ORG-005, BR-ORG-006, BR-SEC-002, BR-SEC-003, BR-SEC-004, BR-SEC-009 |
| Business Process | BA-03 BP-STA-012 View Staff Directory |
| Business Process Flow | BA-04 Section 12 User & Role Management Flow |
| Persona | BA-05 Organization Administrator, Facility Manager, Site Administrator |
| User Journey | BA-06 Section 4 Organization Administrator Journey, Section 5 Facility Manager Journey, Section 6 Site Administrator Journey |
| Stakeholder | BA-07 Organization Administrator, Facility Manager, Site Administrator |
| Non-Functional Requirement | BA-09 Section 6.4 Reporting Performance |
| Assumption / Constraint / Risk | BA-10 BA-ASS-006 |

### Purpose

To provide authorized users with a searchable directory of Staff users and their role, status, Facility, and Site access summaries.

### Functional Requirement

The system shall allow authorized users to view, search, filter, sort, and export Staff Directory information according to role and data scope.

### Business Justification

Staff Directory supports workforce administration, access review, operational coordination, support, and security governance.

### Actors

- Organization Administrator
- Facility Manager
- Site Administrator
- Reporting Service
- Audit Service

### Preconditions

- Staff records exist.
- User is authenticated.
- User has Staff Directory permission.
- User scope is available.

### Trigger

Authorized user opens Staff Directory.

### In Scope

- View Staff list.
- Search and filter Staff.
- Display account status, role summary, Facility access, and Site access.
- Export directory where permitted.
- Enforce data scope and masking.
- Record audit events for access and export.

### Out of Scope

- Creating Staff Accounts.
- Role assignment.
- Permission configuration.
- Activity investigation beyond summary.
- Customer directory.

### Inputs

- Organization ID
- Search text
- Role filter
- Account status filter
- Facility filter
- Site filter
- Export request

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Search Text | Staff search criteria | Text | No | User | Length and safe search validation | Name, email, mobile, username |
| Role Filter | Role-based filter | Identifier | No | User | Must be visible to user | Filters directory |
| Account Status Filter | Lifecycle status filter | Enum | No | User | Created, Active, Suspended, Deactivated | Supports review |
| Facility Filter | Facility scope filter | Identifier | No | User | Must be authorized | Limits result set |
| Site Filter | Site scope filter | Identifier | No | User | Must be authorized | Limits result set |
| Export Request | Export action | Boolean | No | User | Requires export permission | Optional |

### Main Flow

1. Authorized user opens Staff Directory.
2. The system validates permission and scope.
3. The system loads Staff records visible to the user.
4. User searches, filters, sorts, or paginates results.
5. The system applies Organization, Facility, Site, role, and masking rules.
6. The system displays Staff name, status, roles, and access summary.
7. User opens Staff Profile or exports directory where permitted.
8. The system records audit event for directory access or export.

### Alternate Flows

- If user is Facility Manager, results are limited to assigned Facility scope.
- If user is Site Administrator, results are limited to assigned Site scope where policy permits.
- If no Staff records match filters, empty state is displayed.

### Exception Flows

- If user lacks permission, directory access is denied.
- If filter scope is unauthorized, filter is rejected.
- If export fails, the system logs failure and displays retry guidance.
- If directory source is unavailable, an availability error is shown.

### Outputs

- Staff Directory list.
- Filtered and sorted Staff results.
- Staff access summaries.
- Export file where permitted.
- Audit events.

### UI Behaviour

Staff Directory shall provide search, filters, sorting, pagination, status badges, role chips, access summaries, and permission-aware row actions. Sensitive contact data shall be masked where required.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-USR-1101 | User must have Staff Directory permission. | Deny access and log event. | Critical |
| VAL-USR-1102 | Directory results must be scoped to authorized Organization, Facility, or Site. | Filter data and block unauthorized scope. | Critical |
| VAL-USR-1103 | Search text must satisfy safe query constraints. | Reject invalid search input. | Medium |
| VAL-USR-1104 | Export requires Staff Directory export permission. | Disable export or deny action. | High |
| VAL-USR-1105 | Sensitive contact data must be masked where permission is insufficient. | Mask fields. | High |

### Business Rules

- BA-02 BR-ORG-005 - Organization Users
- BA-02 BR-ORG-006 - Role-Based Access
- BA-02 BR-SEC-002 - Role-Based Access Control
- BA-02 BR-SEC-003 - Least Privilege
- BA-02 BR-SEC-004 - Organization Data Isolation
- BA-02 BR-SEC-009 - Sensitive Data Protection

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| staff.directory.view | Organization Administrator | Read | Full Organization directory |
| staff.directory.facility-view | Facility Manager | Read | Facility-scoped directory |
| staff.directory.site-view | Site Administrator | Read | Site-scoped directory |
| staff.directory.export | Authorized user | Export | Required for export |

### Security Considerations

Staff Directory shall enforce tenant isolation, data masking, role-based visibility, and export controls. Directory access and export shall be auditable where configured.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Staff Directory Exported | Organization Administrator | In-App | Directory export generated | Include requester and filter scope |
| Staff Directory Access Denied | Audit Service | System Event | Unauthorized directory access | Include attempted scope |
| Staff Directory Data Unavailable | Organization Administrator | In-App | Directory service unavailable | Include retry guidance |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| StaffDirectoryViewed | User & Role Management | Audit Service |
| StaffDirectoryFiltered | User & Role Management | Reporting Service |
| StaffDirectoryExported | User & Role Management | Audit Service, Reporting Service |

### Audit Events

| Audit Event | Trigger | Actor | Entity | Data Captured |
|---|---|---|---|---|
| Staff Directory Viewed | Directory opened | Authorized user | Staff | Scope, actor, timestamp |
| Staff Directory Filter Applied | Filter changed | Authorized user | Staff | Filter values and result scope |
| Staff Directory Exported | Export requested | Authorized user | Staff | Export filters, format, timestamp |

### Reports Generated

- Staff Directory Report
- Workforce Administration Dashboard
- Access Control Report

### Related Screens

- Staff Directory
- Staff Profile
- Staff Activity
- Access Summary
- Reports & Analytics

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/staff | GET | Authorized token | Retrieve Staff Directory | 200 OK with paginated Staff list |
| /api/v1/staff/search | GET | Authorized token | Search Staff Directory | 200 OK with search results |
| /api/v1/staff/export | POST | Authorized token | Export Staff Directory | 202 Accepted with export status |
| /api/v1/staff/{staffId}/access-summary | GET | Authorized token | Retrieve Staff access summary | 200 OK with access summary |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Staff | Read | Directory profile data | Primary entity |
| Staff Account | Read | Account status | Lifecycle data |
| Staff Role | Read | Role summary | Directory summary |
| Staff Facility Assignment | Read | Facility access summary | Scope data |
| Staff Site Assignment | Read | Site access summary | Scope data |
| Audit Log | Insert | Record directory access/export | Conditional |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Directory Not Loaded | Open directory | Directory Loaded | Authorized user | Permission valid |
| Directory Loaded | Apply filters | Directory Filtered | Authorized user | Valid filters |
| Directory Loaded | Export requested | Export Pending | Authorized user | Export permission |
| Export Pending | Export completed | Export Available | Reporting Service | Export generated |
| Directory Loaded | Unauthorized export attempted | Directory Loaded | User | Export denied and logged |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| USR-1101 | You do not have permission to view Staff Directory. | Missing permission | Request access |
| USR-1102 | Selected directory scope is not authorized. | Scope violation | Adjust filters |
| USR-1103 | Search criteria is not valid. | Invalid search input | Modify search |
| USR-1104 | Staff Directory is temporarily unavailable. | Service or reporting issue | Retry later |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| View Staff Directory | Given user has directory permission | When directory is opened | Then visible Staff records shall be displayed |
| Enforce scope | Given user has Facility or Site scope | When directory loads | Then results shall be limited to authorized scope |
| Search Staff | Given valid search criteria | When search is submitted | Then matching Staff records shall be displayed |
| Export directory | Given user has export permission | When export is requested | Then the system shall generate scoped export |

### Dependencies

- Staff Account records
- Role assignments
- Facility and Site assignments
- Permission model
- Reporting Service
- Audit Service

### Operational Considerations

Directory should support pagination, indexing, filtering, and scoped export for large Organizations.

### Non-Functional Considerations

Staff Directory shall support performance, scalability, usability, accessibility, security, and maintainability.

### Assumptions

- Staff Directory displays internal Staff only.
- Customers are excluded.
- Export is permission controlled.

### Success Criteria

Authorized users can efficiently find Staff and understand their status, roles, and access scope.

### Related Functional Requirements

- FR-USR-001 - Create Staff Account
- FR-USR-002 - Update Staff Profile
- FR-USR-003 - Assign Staff Role
- FR-USR-004 - Assign Facility Access
- FR-USR-005 - Assign Site Access
- FR-USR-011 - View Staff Activity

### Notes

Staff Directory is the operational index for internal users and access administration.

---

**End of FR-06 - User & Role Management**
