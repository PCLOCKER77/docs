# FR-11 Trainer Management

**Document ID:** FR-11  
**Document Name:** Trainer Management Functional Requirements  
**Company:** OreeOn Technologies Pvt. Ltd.  
**Product:** Digitize  
**Document Type:** Functional Requirements  
**Version:** 1.0  
**Status:** Draft  
**Owner:** Product Management  
**Prepared By:** Product Management, Business Analysis, and Solution Architecture  
**Last Updated:** July 2026

---

## FR-TRN-001 - Register Trainer Profile

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-TRN-001 |
| Requirement Name | Register Trainer Profile |
| Functional Module | Trainer Management |
| Business Domain | Trainer |
| Business Capability | Trainer Registration |
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
| Business Requirement | BA-01 Section 15 Membership Lifecycle |
| Business Rule | BA-02 BR-TRN-001, BR-TRN-006, BR-TRN-009, BR-TRN-010, BR-SEC-004 |
| Business Process | BA-03 Staff Identity & Access Processes |
| Business Process Flow | BA-04 Section 22 Batch Management Flow, Section 23 Personal Training Flow |
| Persona | BA-05 Trainer, Facility Manager, Organization Administrator, Reception Staff |
| User Journey | BA-06 Section 8 Trainer Journey, Section 18 Personal Training Journey |
| Stakeholder | BA-07 Trainer, Facility Manager, Organization Administrator |
| Non-Functional Requirement | BA-09 Section 2.6 Usability, Section 2.10 Auditability, Section 3.2 Authorization |
| Assumption / Constraint / Risk | BA-10 BA-ASS-004, BA-ASS-011, BA-RSK-009 |

### Purpose

To enable Trainer Registration within Trainer Management so Digitize can execute Register Trainer Profile consistently across Organizations, Facilities, Sites, users, and related operational or commercial services.

### Functional Requirement

The system shall support Register Trainer Profile as an atomic Trainer Management capability, including scoped data capture, business-rule validation, permission enforcement, lifecycle handling, related service synchronization, notification generation, reporting contribution, and immutable audit recording.

### Business Justification

Register Trainer Profile is required to preserve operational control, revenue accuracy, service continuity, customer trust, and enterprise traceability for Trainer processes. Without this capability, downstream modules would rely on incomplete, manual, or inconsistent records.

### Actors

- Organization Administrator
- Organization Administrator
- Customer
- System
- Notification Service
- Reporting Service
- Audit Service

### Preconditions

- Organization is Active.
- Facility and Site context are Active where applicable.
- Actor is authenticated.
- Actor has permission for Register Trainer Profile.
- Required Trainer configuration and policies are available.
- Related records required by BA-03 Staff Identity & Access Processes are available and within authorized scope.

### Trigger

The capability is triggered when Organization Administrator or the System initiates Register Trainer Profile from Trainer Registration, a related workflow, a scheduled job, or an approved integration event.

### In Scope

- Capture or retrieve required Trainer context.
- Validate Organization, Facility, Site, Customer, user, and policy scope where applicable.
- Execute Register Trainer Profile according to approved business rules.
- Persist the resulting Trainer state or transaction.
- Synchronize related operational, commercial, reporting, notification, and audit records.
- Provide confirmation, exception handling, and traceability.

### Out of Scope

- Cross-Organization data movement.
- Physical deletion of historical records.
- Changes to frozen BA source documents.
- Technical implementation details belonging to SAD, API Specification, or Database Design.
- Manual bypass of configured approval, payment, capacity, security, or audit controls.

### Inputs

- Organization ID
- Facility ID, where applicable
- Site ID, where applicable
- Trainer reference
- Customer reference, where applicable
- Effective date and time, where applicable
- Status or action reason, where applicable
- Payment, billing, trainer, session, or subscription reference where applicable
- Actor remarks, where applicable

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Trainer ID | Primary business record reference | Identifier | Yes | System / User | Must exist or be generated within scope | Core reference for Register Trainer Profile |
| Organization ID | Tenant Organization context | Identifier | Yes | Session / System | Must be Active and authorized | Enforces tenant isolation |
| Facility ID | Facility context | Identifier | Conditional | User / System | Must be Active where applicable | Required for facility-level operations |
| Site ID | Site context | Identifier | Conditional | User / System | Must belong to Facility where applicable | Required for site-level operations |
| Status | Lifecycle or processing state | Enum | Yes | System | Must follow allowed state transitions | Drives UI and downstream access |
| Effective Date | Date when action applies | DateTime | Conditional | User / System | Must satisfy policy | Supports scheduled or immediate actions |
| Reason / Remarks | Business explanation | Text | Conditional | User | Required for governed changes | Stored for audit |

### Main Flow

1. Actor opens Trainer Registration or the related workflow.
2. The system validates authentication, authorization, tenant scope, and current operating context.
3. The system loads the required Trainer records, related configuration, and policy controls.
4. Actor enters or confirms the information required to register trainer profile.
5. The system validates mandatory data, lifecycle status, ownership, eligibility, financial, capacity, schedule, and security rules where applicable.
6. The system executes Register Trainer Profile and persists the resulting Trainer state or transaction.
7. The system updates related history, reporting read models, and downstream references.
8. The system emits business events and notification events.
9. The system records immutable audit events with actor, timestamp, scope, and changed values.
10. The system displays confirmation with the resulting status and reference number.

### Alternate Flows

- If the action requires approval, the system creates an approval request and holds processing in a pending state until approval is completed.
- If the action is scheduled for a future date, the system stores the requested change and applies it through the scheduler on the effective date.
- If payment, billing, capacity, trainer, session, or entitlement handling is not applicable, the system skips that validation path while preserving audit traceability.
- If the user has read-only access, the system displays current details but hides or disables execution controls.

### Exception Flows

- If the actor lacks permission, the request is denied and a security audit event is recorded.
- If required data is missing or invalid, the system blocks submission and highlights the validation errors.
- If the action violates Organization, Facility, Site, capacity, schedule, payment, or lifecycle policy, the system rejects the request or routes for approved override where configured.
- If a related service is unavailable, the system fails safely, records the failure, and prevents inconsistent partial updates.
- If notification delivery fails, the core transaction remains valid and the notification failure is logged for retry.

### Outputs

- Trainer record created, updated, validated, or reported according to the action.
- Lifecycle or processing status updated.
- Related history entry created.
- Business events emitted.
- Notifications generated where configured.
- Audit events recorded.
- Reports or dashboards updated where applicable.

### UI Behaviour

Trainer Registration shall display scoped context, mandatory fields, lifecycle status, policy warnings, validation results, available actions, confirmation prompts, read-only states, pagination or filters where applicable, and responsive behavior for front-desk and administrative usage.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-TRN-001-001 | Actor must have permission to execute Register Trainer Profile. | Deny request and audit. | Critical |
| VAL-TRN-001-002 | Record must belong to the authorized Organization scope. | Deny request. | Critical |
| VAL-TRN-001-003 | Mandatory inputs must be complete and valid. | Block submission. | Critical |
| VAL-TRN-001-004 | Lifecycle and policy rules from BA-02 must be satisfied. | Reject or route for approval. | High |
| VAL-TRN-001-005 | Historical and audit records must be preserved. | Roll back or mark for recovery. | Critical |

### Business Rules

- BA-02 BR-TRN-001
- BA-02 BR-TRN-006
- BA-02 BR-TRN-009
- BA-02 BR-TRN-010
- BA-02 BR-SEC-004

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| trn.register.trainer.profile.view | Organization Administrator | Read | View Register Trainer Profile context |
| trn.register.trainer.profile.execute | Organization Administrator | Execute | Execute Register Trainer Profile |
| trn.register.trainer.profile.approve | Organization Administrator | Approve | Approve governed exceptions where configured |
| trn.register.trainer.profile.audit.view | Organization Administrator / Support Executive | Read | View audit trace |

### Security Considerations

The capability shall enforce authentication, role-based authorization, tenant isolation, Organization scope, Facility and Site access boundaries, sensitive data masking, secure references, and immutable audit logging.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Register Trainer Profile Completed | Primary actor and configured stakeholders | In-App / Email | Action completes | Include reference, status, and effective date where applicable |
| Register Trainer Profile Requires Approval | Approver | In-App | Approval rule applies | Include safe summary and requested action |
| Register Trainer Profile Failed | Primary actor | In-App | Validation or processing fails | Include safe failure reason and next action |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| RegisterTrainerProfileRequested | Trainer Management | Approval Workflow, Audit Service |
| RegisterTrainerProfileCompleted | Trainer Management | Notification Service, Reporting Service, Audit Service |
| RegisterTrainerProfileRejected | Trainer Management | Notification Service, Audit Service |

### Audit Events

| Audit Event | Description | Actor | Target Entity | Key Data |
|---|---|---|---|---|
| REGISTER_TRAINER_PROFILE_REQUESTED | Register Trainer Profile requested | Organization Administrator | Trainer | Scope, reference, and reason |
| REGISTER_TRAINER_PROFILE_COMPLETED | Register Trainer Profile completed | Organization Administrator / System | Trainer | Previous and new state |
| REGISTER_TRAINER_PROFILE_REJECTED | Register Trainer Profile rejected | System | Trainer | Rejection reason |

### Reports Generated

- Trainer Management Operational Report
- Trainer Management History Report
- Trainer Management Exception Report
- Executive Dashboard

### Related Screens

- Trainer Registration
- Trainer Management Dashboard
- Trainer Management History
- Audit Log Viewer

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/trainers | POST | Authorized token | Execute Register Trainer Profile | 200 OK or 201 Created with result |
| /api/v1/trainers/history | GET | Authorized token | Retrieve Register Trainer Profile history | 200 OK with history |
| /api/v1/audit-logs | GET | Authorized token | Retrieve related audit events | 200 OK with scoped audit records |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Trainer | Create / Update / Read | Support Register Trainer Profile | Governed by Organization scope |
| Trainer Assignment | Read / Insert | Support Register Trainer Profile | Governed by Organization scope |
| Trainer Availability | Read / Insert | Support Register Trainer Profile | Governed by Organization scope |
| Trainer Status | Read / Insert | Support Register Trainer Profile | Governed by Organization scope |
| Trainer History | Read / Insert | Support Register Trainer Profile | Governed by Organization scope |
| Audit Log | Insert | Record auditable activity | Immutable |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Draft | Register Trainer Profile initiated | Validated | Organization Administrator | Required data captured |
| Validated | Validation succeeds | Pending Approval | System | BA-02 rules satisfied |
| Pending Approval | Processing completes | Completed | System | Related updates succeed |
| Pending Approval | Approval or policy failure | Rejected | System / Approver | Request rejected |
| Completed | View history | Completed | Authorized user | Read-only historical access |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| TRN-001-001 | Register Trainer Profile cannot be completed because required information is missing. | Missing mandatory data | Complete required fields |
| TRN-001-002 | You do not have permission to perform this action. | Authorization failure | Request access |
| TRN-001-003 | The selected record is not eligible for this action. | Policy or lifecycle violation | Review record status |
| TRN-001-004 | Register Trainer Profile could not be completed due to a system or integration error. | Processing failure | Retry or contact support |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Execute Register Trainer Profile | Given the actor has required permission and valid scope | When the actor submits valid information | Then the system shall complete Register Trainer Profile successfully |
| Enforce validation | Given mandatory data or policy conditions are invalid | When the action is submitted | Then the system shall reject the request with a clear message |
| Preserve audit | Given the action completes or fails | When processing ends | Then audit events shall record actor, timestamp, scope, and outcome |
| Protect scope | Given the selected record is outside authorized scope | When the action is requested | Then the system shall deny access |

### Dependencies

- User & Role Management
- Facility Management
- Site Management
- Activity & Batch Management
- Personal Training
- Attendance Management
- Audit Service

### Operational Considerations

Register Trainer Profile should be designed for high-volume operational use, retry-safe processing, clear exception handling, and support-team diagnostics without exposing sensitive data.

### Non-Functional Considerations

This requirement shall satisfy Digitize non-functional expectations for availability, reliability, performance, scalability, security, configurability, maintainability, and auditability.

### Assumptions

- Required master data and configuration are maintained by authorized users.
- Related services expose stable APIs for validation and synchronization.
- Organization policies define approval, retention, notification, and exception behavior.

### Success Criteria

Register Trainer Profile is completed accurately, securely, and audibly, with downstream records synchronized and no loss of historical traceability.

### Related Functional Requirements

- FR-TRN-002 - Assign Trainer to Facilities and Sites
- FR-TRN-003 - Maintain Trainer Availability
- FR-TRN-004 - Validate Trainer Schedule Conflicts
- FR-TRN-005 - Assign Trainer to Batch
- FR-AUD-001 - Record Audit Events

### Notes

Register Trainer Profile shall remain aligned with the approved BA source documents and shall not introduce behavior that bypasses tenant isolation, lifecycle governance, financial controls, or auditability.

---

## FR-TRN-002 - Assign Trainer to Facilities and Sites

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-TRN-002 |
| Requirement Name | Assign Trainer to Facilities and Sites |
| Functional Module | Trainer Management |
| Business Domain | Trainer |
| Business Capability | Trainer Assignment |
| Requirement Type | Functional |
| Requirement Category | Workflow |
| Requirement Version | 1.0 |
| Requirement Status | Approved |
| Priority | High |
| Complexity | High |
| Release Version | 1.0 |
| Owner | Product Management |

### Traceability References

| Traceability Type | Reference |
|---|---|
| Business Requirement | BA-01 Section 15 Membership Lifecycle |
| Business Rule | BA-02 BR-TRN-002, BR-SIT-001, BR-SIT-004, BR-SEC-004 |
| Business Process | BA-03 BP-ACT-007 Assign Trainer to Batch, BP-PTR-003 Assign Trainer |
| Business Process Flow | BA-04 Section 22 Batch Management Flow, Section 23 Personal Training Flow |
| Persona | BA-05 Trainer, Facility Manager, Organization Administrator, Reception Staff |
| User Journey | BA-06 Section 8 Trainer Journey, Section 18 Personal Training Journey |
| Stakeholder | BA-07 Trainer, Facility Manager, Organization Administrator |
| Non-Functional Requirement | BA-09 Section 2.6 Usability, Section 2.10 Auditability, Section 3.2 Authorization |
| Assumption / Constraint / Risk | BA-10 BA-ASS-004, BA-ASS-011, BA-RSK-009 |

### Purpose

To enable Trainer Assignment within Trainer Management so Digitize can execute Assign Trainer to Facilities and Sites consistently across Organizations, Facilities, Sites, users, and related operational or commercial services.

### Functional Requirement

The system shall support Assign Trainer to Facilities and Sites as an atomic Trainer Management capability, including scoped data capture, business-rule validation, permission enforcement, lifecycle handling, related service synchronization, notification generation, reporting contribution, and immutable audit recording.

### Business Justification

Assign Trainer to Facilities and Sites is required to preserve operational control, revenue accuracy, service continuity, customer trust, and enterprise traceability for Trainer processes. Without this capability, downstream modules would rely on incomplete, manual, or inconsistent records.

### Actors

- Facility Manager
- Organization Administrator
- Customer
- System
- Notification Service
- Reporting Service
- Audit Service

### Preconditions

- Organization is Active.
- Facility and Site context are Active where applicable.
- Actor is authenticated.
- Actor has permission for Assign Trainer to Facilities and Sites.
- Required Trainer configuration and policies are available.
- Related records required by BA-03 BP-ACT-007 Assign Trainer to Batch, BP-PTR-003 Assign Trainer are available and within authorized scope.

### Trigger

The capability is triggered when Facility Manager or the System initiates Assign Trainer to Facilities and Sites from Trainer Assignment, a related workflow, a scheduled job, or an approved integration event.

### In Scope

- Capture or retrieve required Trainer context.
- Validate Organization, Facility, Site, Customer, user, and policy scope where applicable.
- Execute Assign Trainer to Facilities and Sites according to approved business rules.
- Persist the resulting Trainer state or transaction.
- Synchronize related operational, commercial, reporting, notification, and audit records.
- Provide confirmation, exception handling, and traceability.

### Out of Scope

- Cross-Organization data movement.
- Physical deletion of historical records.
- Changes to frozen BA source documents.
- Technical implementation details belonging to SAD, API Specification, or Database Design.
- Manual bypass of configured approval, payment, capacity, security, or audit controls.

### Inputs

- Organization ID
- Facility ID, where applicable
- Site ID, where applicable
- Trainer reference
- Customer reference, where applicable
- Effective date and time, where applicable
- Status or action reason, where applicable
- Payment, billing, trainer, session, or subscription reference where applicable
- Actor remarks, where applicable

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Trainer ID | Primary business record reference | Identifier | Yes | System / User | Must exist or be generated within scope | Core reference for Assign Trainer to Facilities and Sites |
| Organization ID | Tenant Organization context | Identifier | Yes | Session / System | Must be Active and authorized | Enforces tenant isolation |
| Facility ID | Facility context | Identifier | Conditional | User / System | Must be Active where applicable | Required for facility-level operations |
| Site ID | Site context | Identifier | Conditional | User / System | Must belong to Facility where applicable | Required for site-level operations |
| Status | Lifecycle or processing state | Enum | Yes | System | Must follow allowed state transitions | Drives UI and downstream access |
| Effective Date | Date when action applies | DateTime | Conditional | User / System | Must satisfy policy | Supports scheduled or immediate actions |
| Reason / Remarks | Business explanation | Text | Conditional | User | Required for governed changes | Stored for audit |

### Main Flow

1. Actor opens Trainer Assignment or the related workflow.
2. The system validates authentication, authorization, tenant scope, and current operating context.
3. The system loads the required Trainer records, related configuration, and policy controls.
4. Actor enters or confirms the information required to assign trainer to facilities and sites.
5. The system validates mandatory data, lifecycle status, ownership, eligibility, financial, capacity, schedule, and security rules where applicable.
6. The system executes Assign Trainer to Facilities and Sites and persists the resulting Trainer state or transaction.
7. The system updates related history, reporting read models, and downstream references.
8. The system emits business events and notification events.
9. The system records immutable audit events with actor, timestamp, scope, and changed values.
10. The system displays confirmation with the resulting status and reference number.

### Alternate Flows

- If the action requires approval, the system creates an approval request and holds processing in a pending state until approval is completed.
- If the action is scheduled for a future date, the system stores the requested change and applies it through the scheduler on the effective date.
- If payment, billing, capacity, trainer, session, or entitlement handling is not applicable, the system skips that validation path while preserving audit traceability.
- If the user has read-only access, the system displays current details but hides or disables execution controls.

### Exception Flows

- If the actor lacks permission, the request is denied and a security audit event is recorded.
- If required data is missing or invalid, the system blocks submission and highlights the validation errors.
- If the action violates Organization, Facility, Site, capacity, schedule, payment, or lifecycle policy, the system rejects the request or routes for approved override where configured.
- If a related service is unavailable, the system fails safely, records the failure, and prevents inconsistent partial updates.
- If notification delivery fails, the core transaction remains valid and the notification failure is logged for retry.

### Outputs

- Trainer record created, updated, validated, or reported according to the action.
- Lifecycle or processing status updated.
- Related history entry created.
- Business events emitted.
- Notifications generated where configured.
- Audit events recorded.
- Reports or dashboards updated where applicable.

### UI Behaviour

Trainer Assignment shall display scoped context, mandatory fields, lifecycle status, policy warnings, validation results, available actions, confirmation prompts, read-only states, pagination or filters where applicable, and responsive behavior for front-desk and administrative usage.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-TRN-002-001 | Actor must have permission to execute Assign Trainer to Facilities and Sites. | Deny request and audit. | Critical |
| VAL-TRN-002-002 | Record must belong to the authorized Organization scope. | Deny request. | Critical |
| VAL-TRN-002-003 | Mandatory inputs must be complete and valid. | Block submission. | Critical |
| VAL-TRN-002-004 | Lifecycle and policy rules from BA-02 must be satisfied. | Reject or route for approval. | High |
| VAL-TRN-002-005 | Historical and audit records must be preserved. | Roll back or mark for recovery. | Critical |

### Business Rules

- BA-02 BR-TRN-002
- BA-02 BR-SIT-001
- BA-02 BR-SIT-004
- BA-02 BR-SEC-004

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| trn.assign.trainer.to.facilities.and.sites.view | Facility Manager | Read | View Assign Trainer to Facilities and Sites context |
| trn.assign.trainer.to.facilities.and.sites.execute | Facility Manager | Execute | Execute Assign Trainer to Facilities and Sites |
| trn.assign.trainer.to.facilities.and.sites.approve | Organization Administrator | Approve | Approve governed exceptions where configured |
| trn.assign.trainer.to.facilities.and.sites.audit.view | Organization Administrator / Support Executive | Read | View audit trace |

### Security Considerations

The capability shall enforce authentication, role-based authorization, tenant isolation, Organization scope, Facility and Site access boundaries, sensitive data masking, secure references, and immutable audit logging.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Assign Trainer to Facilities and Sites Completed | Primary actor and configured stakeholders | In-App / Email | Action completes | Include reference, status, and effective date where applicable |
| Assign Trainer to Facilities and Sites Requires Approval | Approver | In-App | Approval rule applies | Include safe summary and requested action |
| Assign Trainer to Facilities and Sites Failed | Primary actor | In-App | Validation or processing fails | Include safe failure reason and next action |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| AssignTrainerToFacilitiesAndSitesRequested | Trainer Management | Approval Workflow, Audit Service |
| AssignTrainerToFacilitiesAndSitesCompleted | Trainer Management | Notification Service, Reporting Service, Audit Service |
| AssignTrainerToFacilitiesAndSitesRejected | Trainer Management | Notification Service, Audit Service |

### Audit Events

| Audit Event | Description | Actor | Target Entity | Key Data |
|---|---|---|---|---|
| ASSIGN_TRAINER_TO_FACILITIES_AND_SITES_REQUESTED | Assign Trainer to Facilities and Sites requested | Facility Manager | Trainer | Scope, reference, and reason |
| ASSIGN_TRAINER_TO_FACILITIES_AND_SITES_COMPLETED | Assign Trainer to Facilities and Sites completed | Facility Manager / System | Trainer | Previous and new state |
| ASSIGN_TRAINER_TO_FACILITIES_AND_SITES_REJECTED | Assign Trainer to Facilities and Sites rejected | System | Trainer | Rejection reason |

### Reports Generated

- Trainer Management Operational Report
- Trainer Management History Report
- Trainer Management Exception Report
- Executive Dashboard

### Related Screens

- Trainer Assignment
- Trainer Management Dashboard
- Trainer Management History
- Audit Log Viewer

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/trainers/{trainerId}/assignments | POST | Authorized token | Execute Assign Trainer to Facilities and Sites | 200 OK or 201 Created with result |
| /api/v1/trainers/{trainerId}/assignments/history | GET | Authorized token | Retrieve Assign Trainer to Facilities and Sites history | 200 OK with history |
| /api/v1/audit-logs | GET | Authorized token | Retrieve related audit events | 200 OK with scoped audit records |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Trainer | Create / Update / Read | Support Assign Trainer to Facilities and Sites | Governed by Organization scope |
| Trainer Assignment | Read / Insert | Support Assign Trainer to Facilities and Sites | Governed by Organization scope |
| Trainer Availability | Read / Insert | Support Assign Trainer to Facilities and Sites | Governed by Organization scope |
| Trainer Status | Read / Insert | Support Assign Trainer to Facilities and Sites | Governed by Organization scope |
| Trainer History | Read / Insert | Support Assign Trainer to Facilities and Sites | Governed by Organization scope |
| Audit Log | Insert | Record auditable activity | Immutable |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Draft | Assign Trainer to Facilities and Sites initiated | Validated | Facility Manager | Required data captured |
| Validated | Validation succeeds | Pending Approval | System | BA-02 rules satisfied |
| Pending Approval | Processing completes | Completed | System | Related updates succeed |
| Pending Approval | Approval or policy failure | Rejected | System / Approver | Request rejected |
| Completed | View history | Completed | Authorized user | Read-only historical access |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| TRN-002-001 | Assign Trainer to Facilities and Sites cannot be completed because required information is missing. | Missing mandatory data | Complete required fields |
| TRN-002-002 | You do not have permission to perform this action. | Authorization failure | Request access |
| TRN-002-003 | The selected record is not eligible for this action. | Policy or lifecycle violation | Review record status |
| TRN-002-004 | Assign Trainer to Facilities and Sites could not be completed due to a system or integration error. | Processing failure | Retry or contact support |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Execute Assign Trainer to Facilities and Sites | Given the actor has required permission and valid scope | When the actor submits valid information | Then the system shall complete Assign Trainer to Facilities and Sites successfully |
| Enforce validation | Given mandatory data or policy conditions are invalid | When the action is submitted | Then the system shall reject the request with a clear message |
| Preserve audit | Given the action completes or fails | When processing ends | Then audit events shall record actor, timestamp, scope, and outcome |
| Protect scope | Given the selected record is outside authorized scope | When the action is requested | Then the system shall deny access |

### Dependencies

- User & Role Management
- Facility Management
- Site Management
- Activity & Batch Management
- Personal Training
- Attendance Management
- Audit Service

### Operational Considerations

Assign Trainer to Facilities and Sites should be designed for high-volume operational use, retry-safe processing, clear exception handling, and support-team diagnostics without exposing sensitive data.

### Non-Functional Considerations

This requirement shall satisfy Digitize non-functional expectations for availability, reliability, performance, scalability, security, configurability, maintainability, and auditability.

### Assumptions

- Required master data and configuration are maintained by authorized users.
- Related services expose stable APIs for validation and synchronization.
- Organization policies define approval, retention, notification, and exception behavior.

### Success Criteria

Assign Trainer to Facilities and Sites is completed accurately, securely, and audibly, with downstream records synchronized and no loss of historical traceability.

### Related Functional Requirements

- FR-TRN-001 - Register Trainer Profile
- FR-TRN-003 - Maintain Trainer Availability
- FR-TRN-004 - Validate Trainer Schedule Conflicts
- FR-TRN-005 - Assign Trainer to Batch
- FR-AUD-001 - Record Audit Events

### Notes

Assign Trainer to Facilities and Sites shall remain aligned with the approved BA source documents and shall not introduce behavior that bypasses tenant isolation, lifecycle governance, financial controls, or auditability.

---

## FR-TRN-003 - Maintain Trainer Availability

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-TRN-003 |
| Requirement Name | Maintain Trainer Availability |
| Functional Module | Trainer Management |
| Business Domain | Trainer |
| Business Capability | Trainer Availability |
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
| Business Requirement | BA-01 Section 15 Membership Lifecycle |
| Business Rule | BA-02 BR-TRN-005, BR-TRN-006, BR-TRN-008, BR-SEC-004 |
| Business Process | BA-03 BP-PTR-003 Assign Trainer |
| Business Process Flow | BA-04 Section 22 Batch Management Flow, Section 23 Personal Training Flow |
| Persona | BA-05 Trainer, Facility Manager, Organization Administrator, Reception Staff |
| User Journey | BA-06 Section 8 Trainer Journey, Section 18 Personal Training Journey |
| Stakeholder | BA-07 Trainer, Facility Manager, Organization Administrator |
| Non-Functional Requirement | BA-09 Section 2.6 Usability, Section 2.10 Auditability, Section 3.2 Authorization |
| Assumption / Constraint / Risk | BA-10 BA-ASS-004, BA-ASS-011, BA-RSK-009 |

### Purpose

To enable Trainer Availability within Trainer Management so Digitize can execute Maintain Trainer Availability consistently across Organizations, Facilities, Sites, users, and related operational or commercial services.

### Functional Requirement

The system shall support Maintain Trainer Availability as an atomic Trainer Management capability, including scoped data capture, business-rule validation, permission enforcement, lifecycle handling, related service synchronization, notification generation, reporting contribution, and immutable audit recording.

### Business Justification

Maintain Trainer Availability is required to preserve operational control, revenue accuracy, service continuity, customer trust, and enterprise traceability for Trainer processes. Without this capability, downstream modules would rely on incomplete, manual, or inconsistent records.

### Actors

- Trainer
- Organization Administrator
- Customer
- System
- Notification Service
- Reporting Service
- Audit Service

### Preconditions

- Organization is Active.
- Facility and Site context are Active where applicable.
- Actor is authenticated.
- Actor has permission for Maintain Trainer Availability.
- Required Trainer configuration and policies are available.
- Related records required by BA-03 BP-PTR-003 Assign Trainer are available and within authorized scope.

### Trigger

The capability is triggered when Trainer or the System initiates Maintain Trainer Availability from Trainer Availability, a related workflow, a scheduled job, or an approved integration event.

### In Scope

- Capture or retrieve required Trainer context.
- Validate Organization, Facility, Site, Customer, user, and policy scope where applicable.
- Execute Maintain Trainer Availability according to approved business rules.
- Persist the resulting Trainer state or transaction.
- Synchronize related operational, commercial, reporting, notification, and audit records.
- Provide confirmation, exception handling, and traceability.

### Out of Scope

- Cross-Organization data movement.
- Physical deletion of historical records.
- Changes to frozen BA source documents.
- Technical implementation details belonging to SAD, API Specification, or Database Design.
- Manual bypass of configured approval, payment, capacity, security, or audit controls.

### Inputs

- Organization ID
- Facility ID, where applicable
- Site ID, where applicable
- Trainer reference
- Customer reference, where applicable
- Effective date and time, where applicable
- Status or action reason, where applicable
- Payment, billing, trainer, session, or subscription reference where applicable
- Actor remarks, where applicable

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Trainer ID | Primary business record reference | Identifier | Yes | System / User | Must exist or be generated within scope | Core reference for Maintain Trainer Availability |
| Organization ID | Tenant Organization context | Identifier | Yes | Session / System | Must be Active and authorized | Enforces tenant isolation |
| Facility ID | Facility context | Identifier | Conditional | User / System | Must be Active where applicable | Required for facility-level operations |
| Site ID | Site context | Identifier | Conditional | User / System | Must belong to Facility where applicable | Required for site-level operations |
| Status | Lifecycle or processing state | Enum | Yes | System | Must follow allowed state transitions | Drives UI and downstream access |
| Effective Date | Date when action applies | DateTime | Conditional | User / System | Must satisfy policy | Supports scheduled or immediate actions |
| Reason / Remarks | Business explanation | Text | Conditional | User | Required for governed changes | Stored for audit |

### Main Flow

1. Actor opens Trainer Availability or the related workflow.
2. The system validates authentication, authorization, tenant scope, and current operating context.
3. The system loads the required Trainer records, related configuration, and policy controls.
4. Actor enters or confirms the information required to maintain trainer availability.
5. The system validates mandatory data, lifecycle status, ownership, eligibility, financial, capacity, schedule, and security rules where applicable.
6. The system executes Maintain Trainer Availability and persists the resulting Trainer state or transaction.
7. The system updates related history, reporting read models, and downstream references.
8. The system emits business events and notification events.
9. The system records immutable audit events with actor, timestamp, scope, and changed values.
10. The system displays confirmation with the resulting status and reference number.

### Alternate Flows

- If the action requires approval, the system creates an approval request and holds processing in a pending state until approval is completed.
- If the action is scheduled for a future date, the system stores the requested change and applies it through the scheduler on the effective date.
- If payment, billing, capacity, trainer, session, or entitlement handling is not applicable, the system skips that validation path while preserving audit traceability.
- If the user has read-only access, the system displays current details but hides or disables execution controls.

### Exception Flows

- If the actor lacks permission, the request is denied and a security audit event is recorded.
- If required data is missing or invalid, the system blocks submission and highlights the validation errors.
- If the action violates Organization, Facility, Site, capacity, schedule, payment, or lifecycle policy, the system rejects the request or routes for approved override where configured.
- If a related service is unavailable, the system fails safely, records the failure, and prevents inconsistent partial updates.
- If notification delivery fails, the core transaction remains valid and the notification failure is logged for retry.

### Outputs

- Trainer record created, updated, validated, or reported according to the action.
- Lifecycle or processing status updated.
- Related history entry created.
- Business events emitted.
- Notifications generated where configured.
- Audit events recorded.
- Reports or dashboards updated where applicable.

### UI Behaviour

Trainer Availability shall display scoped context, mandatory fields, lifecycle status, policy warnings, validation results, available actions, confirmation prompts, read-only states, pagination or filters where applicable, and responsive behavior for front-desk and administrative usage.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-TRN-003-001 | Actor must have permission to execute Maintain Trainer Availability. | Deny request and audit. | Critical |
| VAL-TRN-003-002 | Record must belong to the authorized Organization scope. | Deny request. | Critical |
| VAL-TRN-003-003 | Mandatory inputs must be complete and valid. | Block submission. | Critical |
| VAL-TRN-003-004 | Lifecycle and policy rules from BA-02 must be satisfied. | Reject or route for approval. | High |
| VAL-TRN-003-005 | Historical and audit records must be preserved. | Roll back or mark for recovery. | Critical |

### Business Rules

- BA-02 BR-TRN-005
- BA-02 BR-TRN-006
- BA-02 BR-TRN-008
- BA-02 BR-SEC-004

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| trn.maintain.trainer.availability.view | Trainer | Read | View Maintain Trainer Availability context |
| trn.maintain.trainer.availability.execute | Trainer | Execute | Execute Maintain Trainer Availability |
| trn.maintain.trainer.availability.approve | Organization Administrator | Approve | Approve governed exceptions where configured |
| trn.maintain.trainer.availability.audit.view | Organization Administrator / Support Executive | Read | View audit trace |

### Security Considerations

The capability shall enforce authentication, role-based authorization, tenant isolation, Organization scope, Facility and Site access boundaries, sensitive data masking, secure references, and immutable audit logging.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Maintain Trainer Availability Completed | Primary actor and configured stakeholders | In-App / Email | Action completes | Include reference, status, and effective date where applicable |
| Maintain Trainer Availability Requires Approval | Approver | In-App | Approval rule applies | Include safe summary and requested action |
| Maintain Trainer Availability Failed | Primary actor | In-App | Validation or processing fails | Include safe failure reason and next action |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| MaintainTrainerAvailabilityRequested | Trainer Management | Approval Workflow, Audit Service |
| MaintainTrainerAvailabilityCompleted | Trainer Management | Notification Service, Reporting Service, Audit Service |
| MaintainTrainerAvailabilityRejected | Trainer Management | Notification Service, Audit Service |

### Audit Events

| Audit Event | Description | Actor | Target Entity | Key Data |
|---|---|---|---|---|
| MAINTAIN_TRAINER_AVAILABILITY_REQUESTED | Maintain Trainer Availability requested | Trainer | Trainer | Scope, reference, and reason |
| MAINTAIN_TRAINER_AVAILABILITY_COMPLETED | Maintain Trainer Availability completed | Trainer / System | Trainer | Previous and new state |
| MAINTAIN_TRAINER_AVAILABILITY_REJECTED | Maintain Trainer Availability rejected | System | Trainer | Rejection reason |

### Reports Generated

- Trainer Management Operational Report
- Trainer Management History Report
- Trainer Management Exception Report
- Executive Dashboard

### Related Screens

- Trainer Availability
- Trainer Management Dashboard
- Trainer Management History
- Audit Log Viewer

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/trainers/{trainerId}/availability | PUT | Authorized token | Execute Maintain Trainer Availability | 200 OK or 201 Created with result |
| /api/v1/trainers/{trainerId}/availability/history | GET | Authorized token | Retrieve Maintain Trainer Availability history | 200 OK with history |
| /api/v1/audit-logs | GET | Authorized token | Retrieve related audit events | 200 OK with scoped audit records |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Trainer | Create / Update / Read | Support Maintain Trainer Availability | Governed by Organization scope |
| Trainer Assignment | Read / Insert | Support Maintain Trainer Availability | Governed by Organization scope |
| Trainer Availability | Read / Insert | Support Maintain Trainer Availability | Governed by Organization scope |
| Trainer Status | Read / Insert | Support Maintain Trainer Availability | Governed by Organization scope |
| Trainer History | Read / Insert | Support Maintain Trainer Availability | Governed by Organization scope |
| Audit Log | Insert | Record auditable activity | Immutable |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Draft | Maintain Trainer Availability initiated | Configured | Trainer | Required data captured |
| Configured | Validation succeeds | Active | System | BA-02 rules satisfied |
| Active | Processing completes | Inactive | System | Related updates succeed |
| Active | Approval or policy failure | Archived | System / Approver | Request rejected |
| Inactive | View history | Inactive | Authorized user | Read-only historical access |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| TRN-003-001 | Maintain Trainer Availability cannot be completed because required information is missing. | Missing mandatory data | Complete required fields |
| TRN-003-002 | You do not have permission to perform this action. | Authorization failure | Request access |
| TRN-003-003 | The selected record is not eligible for this action. | Policy or lifecycle violation | Review record status |
| TRN-003-004 | Maintain Trainer Availability could not be completed due to a system or integration error. | Processing failure | Retry or contact support |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Execute Maintain Trainer Availability | Given the actor has required permission and valid scope | When the actor submits valid information | Then the system shall complete Maintain Trainer Availability successfully |
| Enforce validation | Given mandatory data or policy conditions are invalid | When the action is submitted | Then the system shall reject the request with a clear message |
| Preserve audit | Given the action completes or fails | When processing ends | Then audit events shall record actor, timestamp, scope, and outcome |
| Protect scope | Given the selected record is outside authorized scope | When the action is requested | Then the system shall deny access |

### Dependencies

- User & Role Management
- Facility Management
- Site Management
- Activity & Batch Management
- Personal Training
- Attendance Management
- Audit Service

### Operational Considerations

Maintain Trainer Availability should be designed for high-volume operational use, retry-safe processing, clear exception handling, and support-team diagnostics without exposing sensitive data.

### Non-Functional Considerations

This requirement shall satisfy Digitize non-functional expectations for availability, reliability, performance, scalability, security, configurability, maintainability, and auditability.

### Assumptions

- Required master data and configuration are maintained by authorized users.
- Related services expose stable APIs for validation and synchronization.
- Organization policies define approval, retention, notification, and exception behavior.

### Success Criteria

Maintain Trainer Availability is completed accurately, securely, and audibly, with downstream records synchronized and no loss of historical traceability.

### Related Functional Requirements

- FR-TRN-001 - Register Trainer Profile
- FR-TRN-002 - Assign Trainer to Facilities and Sites
- FR-TRN-004 - Validate Trainer Schedule Conflicts
- FR-TRN-005 - Assign Trainer to Batch
- FR-AUD-001 - Record Audit Events

### Notes

Maintain Trainer Availability shall remain aligned with the approved BA source documents and shall not introduce behavior that bypasses tenant isolation, lifecycle governance, financial controls, or auditability.

---

## FR-TRN-004 - Validate Trainer Schedule Conflicts

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-TRN-004 |
| Requirement Name | Validate Trainer Schedule Conflicts |
| Functional Module | Trainer Management |
| Business Domain | Trainer |
| Business Capability | Trainer Schedule Governance |
| Requirement Type | Functional |
| Requirement Category | Validation |
| Requirement Version | 1.0 |
| Requirement Status | Approved |
| Priority | High |
| Complexity | Medium |
| Release Version | 1.0 |
| Owner | Product Management |

### Traceability References

| Traceability Type | Reference |
|---|---|
| Business Requirement | BA-01 Section 15 Membership Lifecycle |
| Business Rule | BA-02 BR-TRN-005, BR-TRN-008, BR-TRN-009 |
| Business Process | BA-03 BP-ACT-007 Assign Trainer to Batch, BP-PTR-003 Assign Trainer |
| Business Process Flow | BA-04 Section 22 Batch Management Flow, Section 23 Personal Training Flow |
| Persona | BA-05 Trainer, Facility Manager, Organization Administrator, Reception Staff |
| User Journey | BA-06 Section 8 Trainer Journey, Section 18 Personal Training Journey |
| Stakeholder | BA-07 Trainer, Facility Manager, Organization Administrator |
| Non-Functional Requirement | BA-09 Section 2.6 Usability, Section 2.10 Auditability, Section 3.2 Authorization |
| Assumption / Constraint / Risk | BA-10 BA-ASS-004, BA-ASS-011, BA-RSK-009 |

### Purpose

To enable Trainer Schedule Governance within Trainer Management so Digitize can execute Validate Trainer Schedule Conflicts consistently across Organizations, Facilities, Sites, users, and related operational or commercial services.

### Functional Requirement

The system shall support Validate Trainer Schedule Conflicts as an atomic Trainer Management capability, including scoped data capture, business-rule validation, permission enforcement, lifecycle handling, related service synchronization, notification generation, reporting contribution, and immutable audit recording.

### Business Justification

Validate Trainer Schedule Conflicts is required to preserve operational control, revenue accuracy, service continuity, customer trust, and enterprise traceability for Trainer processes. Without this capability, downstream modules would rely on incomplete, manual, or inconsistent records.

### Actors

- System
- Organization Administrator
- Customer
- System
- Notification Service
- Reporting Service
- Audit Service

### Preconditions

- Organization is Active.
- Facility and Site context are Active where applicable.
- Actor is authenticated.
- Actor has permission for Validate Trainer Schedule Conflicts.
- Required Trainer configuration and policies are available.
- Related records required by BA-03 BP-ACT-007 Assign Trainer to Batch, BP-PTR-003 Assign Trainer are available and within authorized scope.

### Trigger

The capability is triggered when System or the System initiates Validate Trainer Schedule Conflicts from Trainer Schedule, a related workflow, a scheduled job, or an approved integration event.

### In Scope

- Capture or retrieve required Trainer context.
- Validate Organization, Facility, Site, Customer, user, and policy scope where applicable.
- Execute Validate Trainer Schedule Conflicts according to approved business rules.
- Persist the resulting Trainer state or transaction.
- Synchronize related operational, commercial, reporting, notification, and audit records.
- Provide confirmation, exception handling, and traceability.

### Out of Scope

- Cross-Organization data movement.
- Physical deletion of historical records.
- Changes to frozen BA source documents.
- Technical implementation details belonging to SAD, API Specification, or Database Design.
- Manual bypass of configured approval, payment, capacity, security, or audit controls.

### Inputs

- Organization ID
- Facility ID, where applicable
- Site ID, where applicable
- Trainer reference
- Customer reference, where applicable
- Effective date and time, where applicable
- Status or action reason, where applicable
- Payment, billing, trainer, session, or subscription reference where applicable
- Actor remarks, where applicable

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Trainer ID | Primary business record reference | Identifier | Yes | System / User | Must exist or be generated within scope | Core reference for Validate Trainer Schedule Conflicts |
| Organization ID | Tenant Organization context | Identifier | Yes | Session / System | Must be Active and authorized | Enforces tenant isolation |
| Facility ID | Facility context | Identifier | Conditional | User / System | Must be Active where applicable | Required for facility-level operations |
| Site ID | Site context | Identifier | Conditional | User / System | Must belong to Facility where applicable | Required for site-level operations |
| Status | Lifecycle or processing state | Enum | Yes | System | Must follow allowed state transitions | Drives UI and downstream access |
| Effective Date | Date when action applies | DateTime | Conditional | User / System | Must satisfy policy | Supports scheduled or immediate actions |
| Reason / Remarks | Business explanation | Text | Conditional | User | Required for governed changes | Stored for audit |

### Main Flow

1. Actor opens Trainer Schedule or the related workflow.
2. The system validates authentication, authorization, tenant scope, and current operating context.
3. The system loads the required Trainer records, related configuration, and policy controls.
4. Actor enters or confirms the information required to validate trainer schedule conflicts.
5. The system validates mandatory data, lifecycle status, ownership, eligibility, financial, capacity, schedule, and security rules where applicable.
6. The system executes Validate Trainer Schedule Conflicts and persists the resulting Trainer state or transaction.
7. The system updates related history, reporting read models, and downstream references.
8. The system emits business events and notification events.
9. The system records immutable audit events with actor, timestamp, scope, and changed values.
10. The system displays confirmation with the resulting status and reference number.

### Alternate Flows

- If the action requires approval, the system creates an approval request and holds processing in a pending state until approval is completed.
- If the action is scheduled for a future date, the system stores the requested change and applies it through the scheduler on the effective date.
- If payment, billing, capacity, trainer, session, or entitlement handling is not applicable, the system skips that validation path while preserving audit traceability.
- If the user has read-only access, the system displays current details but hides or disables execution controls.

### Exception Flows

- If the actor lacks permission, the request is denied and a security audit event is recorded.
- If required data is missing or invalid, the system blocks submission and highlights the validation errors.
- If the action violates Organization, Facility, Site, capacity, schedule, payment, or lifecycle policy, the system rejects the request or routes for approved override where configured.
- If a related service is unavailable, the system fails safely, records the failure, and prevents inconsistent partial updates.
- If notification delivery fails, the core transaction remains valid and the notification failure is logged for retry.

### Outputs

- Trainer record created, updated, validated, or reported according to the action.
- Lifecycle or processing status updated.
- Related history entry created.
- Business events emitted.
- Notifications generated where configured.
- Audit events recorded.
- Reports or dashboards updated where applicable.

### UI Behaviour

Trainer Schedule shall display scoped context, mandatory fields, lifecycle status, policy warnings, validation results, available actions, confirmation prompts, read-only states, pagination or filters where applicable, and responsive behavior for front-desk and administrative usage.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-TRN-004-001 | Actor must have permission to execute Validate Trainer Schedule Conflicts. | Deny request and audit. | Critical |
| VAL-TRN-004-002 | Record must belong to the authorized Organization scope. | Deny request. | Critical |
| VAL-TRN-004-003 | Mandatory inputs must be complete and valid. | Block submission. | Critical |
| VAL-TRN-004-004 | Lifecycle and policy rules from BA-02 must be satisfied. | Reject or route for approval. | High |
| VAL-TRN-004-005 | Historical and audit records must be preserved. | Roll back or mark for recovery. | Critical |

### Business Rules

- BA-02 BR-TRN-005
- BA-02 BR-TRN-008
- BA-02 BR-TRN-009

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| trn.validate.trainer.schedule.conflicts.view | System | Read | View Validate Trainer Schedule Conflicts context |
| trn.validate.trainer.schedule.conflicts.execute | System | Execute | Execute Validate Trainer Schedule Conflicts |
| trn.validate.trainer.schedule.conflicts.approve | Organization Administrator | Approve | Approve governed exceptions where configured |
| trn.validate.trainer.schedule.conflicts.audit.view | Organization Administrator / Support Executive | Read | View audit trace |

### Security Considerations

The capability shall enforce authentication, role-based authorization, tenant isolation, Organization scope, Facility and Site access boundaries, sensitive data masking, secure references, and immutable audit logging.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Validate Trainer Schedule Conflicts Completed | Primary actor and configured stakeholders | In-App / Email | Action completes | Include reference, status, and effective date where applicable |
| Validate Trainer Schedule Conflicts Requires Approval | Approver | In-App | Approval rule applies | Include safe summary and requested action |
| Validate Trainer Schedule Conflicts Failed | Primary actor | In-App | Validation or processing fails | Include safe failure reason and next action |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| ValidateTrainerScheduleConflictsRequested | Trainer Management | Approval Workflow, Audit Service |
| ValidateTrainerScheduleConflictsCompleted | Trainer Management | Notification Service, Reporting Service, Audit Service |
| ValidateTrainerScheduleConflictsRejected | Trainer Management | Notification Service, Audit Service |

### Audit Events

| Audit Event | Description | Actor | Target Entity | Key Data |
|---|---|---|---|---|
| VALIDATE_TRAINER_SCHEDULE_CONFLICTS_REQUESTED | Validate Trainer Schedule Conflicts requested | System | Trainer | Scope, reference, and reason |
| VALIDATE_TRAINER_SCHEDULE_CONFLICTS_COMPLETED | Validate Trainer Schedule Conflicts completed | System / System | Trainer | Previous and new state |
| VALIDATE_TRAINER_SCHEDULE_CONFLICTS_REJECTED | Validate Trainer Schedule Conflicts rejected | System | Trainer | Rejection reason |

### Reports Generated

- Trainer Management Operational Report
- Trainer Management History Report
- Trainer Management Exception Report
- Executive Dashboard

### Related Screens

- Trainer Schedule
- Trainer Management Dashboard
- Trainer Management History
- Audit Log Viewer

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/trainers/schedule-conflicts/validate | POST | Authorized token | Execute Validate Trainer Schedule Conflicts | 200 OK or 201 Created with result |
| /api/v1/trainers/schedule-conflicts/validate/history | GET | Authorized token | Retrieve Validate Trainer Schedule Conflicts history | 200 OK with history |
| /api/v1/audit-logs | GET | Authorized token | Retrieve related audit events | 200 OK with scoped audit records |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Trainer | Create / Update / Read | Support Validate Trainer Schedule Conflicts | Governed by Organization scope |
| Trainer Assignment | Read / Insert | Support Validate Trainer Schedule Conflicts | Governed by Organization scope |
| Trainer Availability | Read / Insert | Support Validate Trainer Schedule Conflicts | Governed by Organization scope |
| Trainer Status | Read / Insert | Support Validate Trainer Schedule Conflicts | Governed by Organization scope |
| Trainer History | Read / Insert | Support Validate Trainer Schedule Conflicts | Governed by Organization scope |
| Audit Log | Insert | Record auditable activity | Immutable |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Requested | Validate Trainer Schedule Conflicts initiated | Eligible | System | Required data captured |
| Eligible | Validation succeeds | Requires Override | System | BA-02 rules satisfied |
| Requires Override | Processing completes | Denied | System | Related updates succeed |
| Requires Override | Approval or policy failure | Failed | System / Approver | Request rejected |
| Denied | View history | Denied | Authorized user | Read-only historical access |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| TRN-004-001 | Validate Trainer Schedule Conflicts cannot be completed because required information is missing. | Missing mandatory data | Complete required fields |
| TRN-004-002 | You do not have permission to perform this action. | Authorization failure | Request access |
| TRN-004-003 | The selected record is not eligible for this action. | Policy or lifecycle violation | Review record status |
| TRN-004-004 | Validate Trainer Schedule Conflicts could not be completed due to a system or integration error. | Processing failure | Retry or contact support |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Execute Validate Trainer Schedule Conflicts | Given the actor has required permission and valid scope | When the actor submits valid information | Then the system shall complete Validate Trainer Schedule Conflicts successfully |
| Enforce validation | Given mandatory data or policy conditions are invalid | When the action is submitted | Then the system shall reject the request with a clear message |
| Preserve audit | Given the action completes or fails | When processing ends | Then audit events shall record actor, timestamp, scope, and outcome |
| Protect scope | Given the selected record is outside authorized scope | When the action is requested | Then the system shall deny access |

### Dependencies

- User & Role Management
- Facility Management
- Site Management
- Activity & Batch Management
- Personal Training
- Attendance Management
- Audit Service

### Operational Considerations

Validate Trainer Schedule Conflicts should be designed for high-volume operational use, retry-safe processing, clear exception handling, and support-team diagnostics without exposing sensitive data.

### Non-Functional Considerations

This requirement shall satisfy Digitize non-functional expectations for availability, reliability, performance, scalability, security, configurability, maintainability, and auditability.

### Assumptions

- Required master data and configuration are maintained by authorized users.
- Related services expose stable APIs for validation and synchronization.
- Organization policies define approval, retention, notification, and exception behavior.

### Success Criteria

Validate Trainer Schedule Conflicts is completed accurately, securely, and audibly, with downstream records synchronized and no loss of historical traceability.

### Related Functional Requirements

- FR-TRN-001 - Register Trainer Profile
- FR-TRN-002 - Assign Trainer to Facilities and Sites
- FR-TRN-003 - Maintain Trainer Availability
- FR-TRN-005 - Assign Trainer to Batch
- FR-AUD-001 - Record Audit Events

### Notes

Validate Trainer Schedule Conflicts shall remain aligned with the approved BA source documents and shall not introduce behavior that bypasses tenant isolation, lifecycle governance, financial controls, or auditability.

---

## FR-TRN-005 - Assign Trainer to Batch

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-TRN-005 |
| Requirement Name | Assign Trainer to Batch |
| Functional Module | Trainer Management |
| Business Domain | Trainer |
| Business Capability | Batch Trainer Assignment |
| Requirement Type | Functional |
| Requirement Category | Workflow |
| Requirement Version | 1.0 |
| Requirement Status | Approved |
| Priority | High |
| Complexity | High |
| Release Version | 1.0 |
| Owner | Product Management |

### Traceability References

| Traceability Type | Reference |
|---|---|
| Business Requirement | BA-08 BR-016 Batch Scheduling |
| Business Rule | BA-02 BR-TRN-004, BR-TRN-005, BR-TRN-008, BR-SEC-004 |
| Business Process | BA-03 BP-ACT-007 Assign Trainer to Batch |
| Business Process Flow | BA-04 Section 22 Batch Management Flow, Section 23 Personal Training Flow |
| Persona | BA-05 Trainer, Facility Manager, Organization Administrator, Reception Staff |
| User Journey | BA-06 Section 8 Trainer Journey, Section 18 Personal Training Journey |
| Stakeholder | BA-07 Trainer, Facility Manager, Organization Administrator |
| Non-Functional Requirement | BA-09 Section 2.6 Usability, Section 2.10 Auditability, Section 3.2 Authorization |
| Assumption / Constraint / Risk | BA-10 BA-ASS-004, BA-ASS-011, BA-RSK-009 |

### Purpose

To enable Batch Trainer Assignment within Trainer Management so Digitize can execute Assign Trainer to Batch consistently across Organizations, Facilities, Sites, users, and related operational or commercial services.

### Functional Requirement

The system shall support Assign Trainer to Batch as an atomic Trainer Management capability, including scoped data capture, business-rule validation, permission enforcement, lifecycle handling, related service synchronization, notification generation, reporting contribution, and immutable audit recording.

### Business Justification

Assign Trainer to Batch is required to preserve operational control, revenue accuracy, service continuity, customer trust, and enterprise traceability for Trainer processes. Without this capability, downstream modules would rely on incomplete, manual, or inconsistent records.

### Actors

- Facility Manager
- Organization Administrator
- Customer
- System
- Notification Service
- Reporting Service
- Audit Service

### Preconditions

- Organization is Active.
- Facility and Site context are Active where applicable.
- Actor is authenticated.
- Actor has permission for Assign Trainer to Batch.
- Required Trainer configuration and policies are available.
- Related records required by BA-03 BP-ACT-007 Assign Trainer to Batch are available and within authorized scope.

### Trigger

The capability is triggered when Facility Manager or the System initiates Assign Trainer to Batch from Batch Trainer Assignment, a related workflow, a scheduled job, or an approved integration event.

### In Scope

- Capture or retrieve required Trainer context.
- Validate Organization, Facility, Site, Customer, user, and policy scope where applicable.
- Execute Assign Trainer to Batch according to approved business rules.
- Persist the resulting Trainer state or transaction.
- Synchronize related operational, commercial, reporting, notification, and audit records.
- Provide confirmation, exception handling, and traceability.

### Out of Scope

- Cross-Organization data movement.
- Physical deletion of historical records.
- Changes to frozen BA source documents.
- Technical implementation details belonging to SAD, API Specification, or Database Design.
- Manual bypass of configured approval, payment, capacity, security, or audit controls.

### Inputs

- Organization ID
- Facility ID, where applicable
- Site ID, where applicable
- Trainer reference
- Customer reference, where applicable
- Effective date and time, where applicable
- Status or action reason, where applicable
- Payment, billing, trainer, session, or subscription reference where applicable
- Actor remarks, where applicable

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Trainer ID | Primary business record reference | Identifier | Yes | System / User | Must exist or be generated within scope | Core reference for Assign Trainer to Batch |
| Organization ID | Tenant Organization context | Identifier | Yes | Session / System | Must be Active and authorized | Enforces tenant isolation |
| Facility ID | Facility context | Identifier | Conditional | User / System | Must be Active where applicable | Required for facility-level operations |
| Site ID | Site context | Identifier | Conditional | User / System | Must belong to Facility where applicable | Required for site-level operations |
| Status | Lifecycle or processing state | Enum | Yes | System | Must follow allowed state transitions | Drives UI and downstream access |
| Effective Date | Date when action applies | DateTime | Conditional | User / System | Must satisfy policy | Supports scheduled or immediate actions |
| Reason / Remarks | Business explanation | Text | Conditional | User | Required for governed changes | Stored for audit |

### Main Flow

1. Actor opens Batch Trainer Assignment or the related workflow.
2. The system validates authentication, authorization, tenant scope, and current operating context.
3. The system loads the required Trainer records, related configuration, and policy controls.
4. Actor enters or confirms the information required to assign trainer to batch.
5. The system validates mandatory data, lifecycle status, ownership, eligibility, financial, capacity, schedule, and security rules where applicable.
6. The system executes Assign Trainer to Batch and persists the resulting Trainer state or transaction.
7. The system updates related history, reporting read models, and downstream references.
8. The system emits business events and notification events.
9. The system records immutable audit events with actor, timestamp, scope, and changed values.
10. The system displays confirmation with the resulting status and reference number.

### Alternate Flows

- If the action requires approval, the system creates an approval request and holds processing in a pending state until approval is completed.
- If the action is scheduled for a future date, the system stores the requested change and applies it through the scheduler on the effective date.
- If payment, billing, capacity, trainer, session, or entitlement handling is not applicable, the system skips that validation path while preserving audit traceability.
- If the user has read-only access, the system displays current details but hides or disables execution controls.

### Exception Flows

- If the actor lacks permission, the request is denied and a security audit event is recorded.
- If required data is missing or invalid, the system blocks submission and highlights the validation errors.
- If the action violates Organization, Facility, Site, capacity, schedule, payment, or lifecycle policy, the system rejects the request or routes for approved override where configured.
- If a related service is unavailable, the system fails safely, records the failure, and prevents inconsistent partial updates.
- If notification delivery fails, the core transaction remains valid and the notification failure is logged for retry.

### Outputs

- Trainer record created, updated, validated, or reported according to the action.
- Lifecycle or processing status updated.
- Related history entry created.
- Business events emitted.
- Notifications generated where configured.
- Audit events recorded.
- Reports or dashboards updated where applicable.

### UI Behaviour

Batch Trainer Assignment shall display scoped context, mandatory fields, lifecycle status, policy warnings, validation results, available actions, confirmation prompts, read-only states, pagination or filters where applicable, and responsive behavior for front-desk and administrative usage.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-TRN-005-001 | Actor must have permission to execute Assign Trainer to Batch. | Deny request and audit. | Critical |
| VAL-TRN-005-002 | Record must belong to the authorized Organization scope. | Deny request. | Critical |
| VAL-TRN-005-003 | Mandatory inputs must be complete and valid. | Block submission. | Critical |
| VAL-TRN-005-004 | Lifecycle and policy rules from BA-02 must be satisfied. | Reject or route for approval. | High |
| VAL-TRN-005-005 | Historical and audit records must be preserved. | Roll back or mark for recovery. | Critical |

### Business Rules

- BA-02 BR-TRN-004
- BA-02 BR-TRN-005
- BA-02 BR-TRN-008
- BA-02 BR-SEC-004

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| trn.assign.trainer.to.batch.view | Facility Manager | Read | View Assign Trainer to Batch context |
| trn.assign.trainer.to.batch.execute | Facility Manager | Execute | Execute Assign Trainer to Batch |
| trn.assign.trainer.to.batch.approve | Organization Administrator | Approve | Approve governed exceptions where configured |
| trn.assign.trainer.to.batch.audit.view | Organization Administrator / Support Executive | Read | View audit trace |

### Security Considerations

The capability shall enforce authentication, role-based authorization, tenant isolation, Organization scope, Facility and Site access boundaries, sensitive data masking, secure references, and immutable audit logging.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Assign Trainer to Batch Completed | Primary actor and configured stakeholders | In-App / Email | Action completes | Include reference, status, and effective date where applicable |
| Assign Trainer to Batch Requires Approval | Approver | In-App | Approval rule applies | Include safe summary and requested action |
| Assign Trainer to Batch Failed | Primary actor | In-App | Validation or processing fails | Include safe failure reason and next action |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| AssignTrainerToBatchRequested | Trainer Management | Approval Workflow, Audit Service |
| AssignTrainerToBatchCompleted | Trainer Management | Notification Service, Reporting Service, Audit Service |
| AssignTrainerToBatchRejected | Trainer Management | Notification Service, Audit Service |

### Audit Events

| Audit Event | Description | Actor | Target Entity | Key Data |
|---|---|---|---|---|
| ASSIGN_TRAINER_TO_BATCH_REQUESTED | Assign Trainer to Batch requested | Facility Manager | Trainer | Scope, reference, and reason |
| ASSIGN_TRAINER_TO_BATCH_COMPLETED | Assign Trainer to Batch completed | Facility Manager / System | Trainer | Previous and new state |
| ASSIGN_TRAINER_TO_BATCH_REJECTED | Assign Trainer to Batch rejected | System | Trainer | Rejection reason |

### Reports Generated

- Trainer Management Operational Report
- Trainer Management History Report
- Trainer Management Exception Report
- Executive Dashboard

### Related Screens

- Batch Trainer Assignment
- Trainer Management Dashboard
- Trainer Management History
- Audit Log Viewer

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/batches/{batchId}/trainers | POST | Authorized token | Execute Assign Trainer to Batch | 200 OK or 201 Created with result |
| /api/v1/batches/{batchId}/trainers/history | GET | Authorized token | Retrieve Assign Trainer to Batch history | 200 OK with history |
| /api/v1/audit-logs | GET | Authorized token | Retrieve related audit events | 200 OK with scoped audit records |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Trainer | Create / Update / Read | Support Assign Trainer to Batch | Governed by Organization scope |
| Trainer Assignment | Read / Insert | Support Assign Trainer to Batch | Governed by Organization scope |
| Trainer Availability | Read / Insert | Support Assign Trainer to Batch | Governed by Organization scope |
| Trainer Status | Read / Insert | Support Assign Trainer to Batch | Governed by Organization scope |
| Trainer History | Read / Insert | Support Assign Trainer to Batch | Governed by Organization scope |
| Audit Log | Insert | Record auditable activity | Immutable |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Draft | Assign Trainer to Batch initiated | Validated | Facility Manager | Required data captured |
| Validated | Validation succeeds | Pending Approval | System | BA-02 rules satisfied |
| Pending Approval | Processing completes | Completed | System | Related updates succeed |
| Pending Approval | Approval or policy failure | Rejected | System / Approver | Request rejected |
| Completed | View history | Completed | Authorized user | Read-only historical access |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| TRN-005-001 | Assign Trainer to Batch cannot be completed because required information is missing. | Missing mandatory data | Complete required fields |
| TRN-005-002 | You do not have permission to perform this action. | Authorization failure | Request access |
| TRN-005-003 | The selected record is not eligible for this action. | Policy or lifecycle violation | Review record status |
| TRN-005-004 | Assign Trainer to Batch could not be completed due to a system or integration error. | Processing failure | Retry or contact support |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Execute Assign Trainer to Batch | Given the actor has required permission and valid scope | When the actor submits valid information | Then the system shall complete Assign Trainer to Batch successfully |
| Enforce validation | Given mandatory data or policy conditions are invalid | When the action is submitted | Then the system shall reject the request with a clear message |
| Preserve audit | Given the action completes or fails | When processing ends | Then audit events shall record actor, timestamp, scope, and outcome |
| Protect scope | Given the selected record is outside authorized scope | When the action is requested | Then the system shall deny access |

### Dependencies

- User & Role Management
- Facility Management
- Site Management
- Activity & Batch Management
- Personal Training
- Attendance Management
- Audit Service

### Operational Considerations

Assign Trainer to Batch should be designed for high-volume operational use, retry-safe processing, clear exception handling, and support-team diagnostics without exposing sensitive data.

### Non-Functional Considerations

This requirement shall satisfy Digitize non-functional expectations for availability, reliability, performance, scalability, security, configurability, maintainability, and auditability.

### Assumptions

- Required master data and configuration are maintained by authorized users.
- Related services expose stable APIs for validation and synchronization.
- Organization policies define approval, retention, notification, and exception behavior.

### Success Criteria

Assign Trainer to Batch is completed accurately, securely, and audibly, with downstream records synchronized and no loss of historical traceability.

### Related Functional Requirements

- FR-TRN-001 - Register Trainer Profile
- FR-TRN-002 - Assign Trainer to Facilities and Sites
- FR-TRN-003 - Maintain Trainer Availability
- FR-TRN-004 - Validate Trainer Schedule Conflicts
- FR-AUD-001 - Record Audit Events

### Notes

Assign Trainer to Batch shall remain aligned with the approved BA source documents and shall not introduce behavior that bypasses tenant isolation, lifecycle governance, financial controls, or auditability.

---

## FR-TRN-006 - Assign Trainer to Personal Training Session

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-TRN-006 |
| Requirement Name | Assign Trainer to Personal Training Session |
| Functional Module | Trainer Management |
| Business Domain | Trainer |
| Business Capability | Personal Training Allocation |
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
| Business Requirement | BA-08 BR-017 Personal Training Booking |
| Business Rule | BA-02 BR-TRN-003, BR-TRN-005, BR-TRN-008, BR-SEC-004 |
| Business Process | BA-03 BP-PTR-003 Assign Trainer |
| Business Process Flow | BA-04 Section 22 Batch Management Flow, Section 23 Personal Training Flow |
| Persona | BA-05 Trainer, Facility Manager, Organization Administrator, Reception Staff |
| User Journey | BA-06 Section 8 Trainer Journey, Section 18 Personal Training Journey |
| Stakeholder | BA-07 Trainer, Facility Manager, Organization Administrator |
| Non-Functional Requirement | BA-09 Section 2.6 Usability, Section 2.10 Auditability, Section 3.2 Authorization |
| Assumption / Constraint / Risk | BA-10 BA-ASS-004, BA-ASS-011, BA-RSK-009 |

### Purpose

To enable Personal Training Allocation within Trainer Management so Digitize can execute Assign Trainer to Personal Training Session consistently across Organizations, Facilities, Sites, users, and related operational or commercial services.

### Functional Requirement

The system shall support Assign Trainer to Personal Training Session as an atomic Trainer Management capability, including scoped data capture, business-rule validation, permission enforcement, lifecycle handling, related service synchronization, notification generation, reporting contribution, and immutable audit recording.

### Business Justification

Assign Trainer to Personal Training Session is required to preserve operational control, revenue accuracy, service continuity, customer trust, and enterprise traceability for Trainer processes. Without this capability, downstream modules would rely on incomplete, manual, or inconsistent records.

### Actors

- Reception Staff
- Organization Administrator
- Customer
- System
- Notification Service
- Reporting Service
- Audit Service

### Preconditions

- Organization is Active.
- Facility and Site context are Active where applicable.
- Actor is authenticated.
- Actor has permission for Assign Trainer to Personal Training Session.
- Required Trainer configuration and policies are available.
- Related records required by BA-03 BP-PTR-003 Assign Trainer are available and within authorized scope.

### Trigger

The capability is triggered when Reception Staff or the System initiates Assign Trainer to Personal Training Session from Personal Training Assignment, a related workflow, a scheduled job, or an approved integration event.

### In Scope

- Capture or retrieve required Trainer context.
- Validate Organization, Facility, Site, Customer, user, and policy scope where applicable.
- Execute Assign Trainer to Personal Training Session according to approved business rules.
- Persist the resulting Trainer state or transaction.
- Synchronize related operational, commercial, reporting, notification, and audit records.
- Provide confirmation, exception handling, and traceability.

### Out of Scope

- Cross-Organization data movement.
- Physical deletion of historical records.
- Changes to frozen BA source documents.
- Technical implementation details belonging to SAD, API Specification, or Database Design.
- Manual bypass of configured approval, payment, capacity, security, or audit controls.

### Inputs

- Organization ID
- Facility ID, where applicable
- Site ID, where applicable
- Trainer reference
- Customer reference, where applicable
- Effective date and time, where applicable
- Status or action reason, where applicable
- Payment, billing, trainer, session, or subscription reference where applicable
- Actor remarks, where applicable

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Trainer ID | Primary business record reference | Identifier | Yes | System / User | Must exist or be generated within scope | Core reference for Assign Trainer to Personal Training Session |
| Organization ID | Tenant Organization context | Identifier | Yes | Session / System | Must be Active and authorized | Enforces tenant isolation |
| Facility ID | Facility context | Identifier | Conditional | User / System | Must be Active where applicable | Required for facility-level operations |
| Site ID | Site context | Identifier | Conditional | User / System | Must belong to Facility where applicable | Required for site-level operations |
| Status | Lifecycle or processing state | Enum | Yes | System | Must follow allowed state transitions | Drives UI and downstream access |
| Effective Date | Date when action applies | DateTime | Conditional | User / System | Must satisfy policy | Supports scheduled or immediate actions |
| Reason / Remarks | Business explanation | Text | Conditional | User | Required for governed changes | Stored for audit |

### Main Flow

1. Actor opens Personal Training Assignment or the related workflow.
2. The system validates authentication, authorization, tenant scope, and current operating context.
3. The system loads the required Trainer records, related configuration, and policy controls.
4. Actor enters or confirms the information required to assign trainer to personal training session.
5. The system validates mandatory data, lifecycle status, ownership, eligibility, financial, capacity, schedule, and security rules where applicable.
6. The system executes Assign Trainer to Personal Training Session and persists the resulting Trainer state or transaction.
7. The system updates related history, reporting read models, and downstream references.
8. The system emits business events and notification events.
9. The system records immutable audit events with actor, timestamp, scope, and changed values.
10. The system displays confirmation with the resulting status and reference number.

### Alternate Flows

- If the action requires approval, the system creates an approval request and holds processing in a pending state until approval is completed.
- If the action is scheduled for a future date, the system stores the requested change and applies it through the scheduler on the effective date.
- If payment, billing, capacity, trainer, session, or entitlement handling is not applicable, the system skips that validation path while preserving audit traceability.
- If the user has read-only access, the system displays current details but hides or disables execution controls.

### Exception Flows

- If the actor lacks permission, the request is denied and a security audit event is recorded.
- If required data is missing or invalid, the system blocks submission and highlights the validation errors.
- If the action violates Organization, Facility, Site, capacity, schedule, payment, or lifecycle policy, the system rejects the request or routes for approved override where configured.
- If a related service is unavailable, the system fails safely, records the failure, and prevents inconsistent partial updates.
- If notification delivery fails, the core transaction remains valid and the notification failure is logged for retry.

### Outputs

- Trainer record created, updated, validated, or reported according to the action.
- Lifecycle or processing status updated.
- Related history entry created.
- Business events emitted.
- Notifications generated where configured.
- Audit events recorded.
- Reports or dashboards updated where applicable.

### UI Behaviour

Personal Training Assignment shall display scoped context, mandatory fields, lifecycle status, policy warnings, validation results, available actions, confirmation prompts, read-only states, pagination or filters where applicable, and responsive behavior for front-desk and administrative usage.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-TRN-006-001 | Actor must have permission to execute Assign Trainer to Personal Training Session. | Deny request and audit. | Critical |
| VAL-TRN-006-002 | Record must belong to the authorized Organization scope. | Deny request. | Critical |
| VAL-TRN-006-003 | Mandatory inputs must be complete and valid. | Block submission. | Critical |
| VAL-TRN-006-004 | Lifecycle and policy rules from BA-02 must be satisfied. | Reject or route for approval. | High |
| VAL-TRN-006-005 | Historical and audit records must be preserved. | Roll back or mark for recovery. | Critical |

### Business Rules

- BA-02 BR-TRN-003
- BA-02 BR-TRN-005
- BA-02 BR-TRN-008
- BA-02 BR-SEC-004

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| trn.assign.trainer.to.personal.training.session.view | Reception Staff | Read | View Assign Trainer to Personal Training Session context |
| trn.assign.trainer.to.personal.training.session.execute | Reception Staff | Execute | Execute Assign Trainer to Personal Training Session |
| trn.assign.trainer.to.personal.training.session.approve | Organization Administrator | Approve | Approve governed exceptions where configured |
| trn.assign.trainer.to.personal.training.session.audit.view | Organization Administrator / Support Executive | Read | View audit trace |

### Security Considerations

The capability shall enforce authentication, role-based authorization, tenant isolation, Organization scope, Facility and Site access boundaries, sensitive data masking, secure references, and immutable audit logging.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Assign Trainer to Personal Training Session Completed | Primary actor and configured stakeholders | In-App / Email | Action completes | Include reference, status, and effective date where applicable |
| Assign Trainer to Personal Training Session Requires Approval | Approver | In-App | Approval rule applies | Include safe summary and requested action |
| Assign Trainer to Personal Training Session Failed | Primary actor | In-App | Validation or processing fails | Include safe failure reason and next action |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| AssignTrainerToPersonalTrainingSessionRequested | Trainer Management | Approval Workflow, Audit Service |
| AssignTrainerToPersonalTrainingSessionCompleted | Trainer Management | Notification Service, Reporting Service, Audit Service |
| AssignTrainerToPersonalTrainingSessionRejected | Trainer Management | Notification Service, Audit Service |

### Audit Events

| Audit Event | Description | Actor | Target Entity | Key Data |
|---|---|---|---|---|
| ASSIGN_TRAINER_TO_PERSONAL_TRAINING_SESSION_REQUESTED | Assign Trainer to Personal Training Session requested | Reception Staff | Trainer | Scope, reference, and reason |
| ASSIGN_TRAINER_TO_PERSONAL_TRAINING_SESSION_COMPLETED | Assign Trainer to Personal Training Session completed | Reception Staff / System | Trainer | Previous and new state |
| ASSIGN_TRAINER_TO_PERSONAL_TRAINING_SESSION_REJECTED | Assign Trainer to Personal Training Session rejected | System | Trainer | Rejection reason |

### Reports Generated

- Trainer Management Operational Report
- Trainer Management History Report
- Trainer Management Exception Report
- Executive Dashboard

### Related Screens

- Personal Training Assignment
- Trainer Management Dashboard
- Trainer Management History
- Audit Log Viewer

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/training-sessions/{sessionId}/trainer-assignment | POST | Authorized token | Execute Assign Trainer to Personal Training Session | 200 OK or 201 Created with result |
| /api/v1/training-sessions/{sessionId}/trainer-assignment/history | GET | Authorized token | Retrieve Assign Trainer to Personal Training Session history | 200 OK with history |
| /api/v1/audit-logs | GET | Authorized token | Retrieve related audit events | 200 OK with scoped audit records |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Trainer | Create / Update / Read | Support Assign Trainer to Personal Training Session | Governed by Organization scope |
| Trainer Assignment | Read / Insert | Support Assign Trainer to Personal Training Session | Governed by Organization scope |
| Trainer Availability | Read / Insert | Support Assign Trainer to Personal Training Session | Governed by Organization scope |
| Trainer Status | Read / Insert | Support Assign Trainer to Personal Training Session | Governed by Organization scope |
| Trainer History | Read / Insert | Support Assign Trainer to Personal Training Session | Governed by Organization scope |
| Audit Log | Insert | Record auditable activity | Immutable |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Draft | Assign Trainer to Personal Training Session initiated | Validated | Reception Staff | Required data captured |
| Validated | Validation succeeds | Pending Approval | System | BA-02 rules satisfied |
| Pending Approval | Processing completes | Completed | System | Related updates succeed |
| Pending Approval | Approval or policy failure | Rejected | System / Approver | Request rejected |
| Completed | View history | Completed | Authorized user | Read-only historical access |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| TRN-006-001 | Assign Trainer to Personal Training Session cannot be completed because required information is missing. | Missing mandatory data | Complete required fields |
| TRN-006-002 | You do not have permission to perform this action. | Authorization failure | Request access |
| TRN-006-003 | The selected record is not eligible for this action. | Policy or lifecycle violation | Review record status |
| TRN-006-004 | Assign Trainer to Personal Training Session could not be completed due to a system or integration error. | Processing failure | Retry or contact support |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Execute Assign Trainer to Personal Training Session | Given the actor has required permission and valid scope | When the actor submits valid information | Then the system shall complete Assign Trainer to Personal Training Session successfully |
| Enforce validation | Given mandatory data or policy conditions are invalid | When the action is submitted | Then the system shall reject the request with a clear message |
| Preserve audit | Given the action completes or fails | When processing ends | Then audit events shall record actor, timestamp, scope, and outcome |
| Protect scope | Given the selected record is outside authorized scope | When the action is requested | Then the system shall deny access |

### Dependencies

- User & Role Management
- Facility Management
- Site Management
- Activity & Batch Management
- Personal Training
- Attendance Management
- Audit Service

### Operational Considerations

Assign Trainer to Personal Training Session should be designed for high-volume operational use, retry-safe processing, clear exception handling, and support-team diagnostics without exposing sensitive data.

### Non-Functional Considerations

This requirement shall satisfy Digitize non-functional expectations for availability, reliability, performance, scalability, security, configurability, maintainability, and auditability.

### Assumptions

- Required master data and configuration are maintained by authorized users.
- Related services expose stable APIs for validation and synchronization.
- Organization policies define approval, retention, notification, and exception behavior.

### Success Criteria

Assign Trainer to Personal Training Session is completed accurately, securely, and audibly, with downstream records synchronized and no loss of historical traceability.

### Related Functional Requirements

- FR-TRN-001 - Register Trainer Profile
- FR-TRN-002 - Assign Trainer to Facilities and Sites
- FR-TRN-003 - Maintain Trainer Availability
- FR-TRN-004 - Validate Trainer Schedule Conflicts
- FR-AUD-001 - Record Audit Events

### Notes

Assign Trainer to Personal Training Session shall remain aligned with the approved BA source documents and shall not introduce behavior that bypasses tenant isolation, lifecycle governance, financial controls, or auditability.

---

## FR-TRN-007 - Record Trainer Attendance

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-TRN-007 |
| Requirement Name | Record Trainer Attendance |
| Functional Module | Trainer Management |
| Business Domain | Trainer |
| Business Capability | Trainer Attendance |
| Requirement Type | Functional |
| Requirement Category | Transaction |
| Requirement Version | 1.0 |
| Requirement Status | Approved |
| Priority | Medium |
| Complexity | Medium |
| Release Version | 1.0 |
| Owner | Product Management |

### Traceability References

| Traceability Type | Reference |
|---|---|
| Business Requirement | BA-01 Section 15 Membership Lifecycle |
| Business Rule | BA-02 BR-TRN-007, BR-TRN-009, BR-AUD-003, BR-SEC-004 |
| Business Process | BA-03 BP-PTR-007 Start Personal Training Session, BP-ACT-011 Start Session |
| Business Process Flow | BA-04 Section 22 Batch Management Flow, Section 23 Personal Training Flow |
| Persona | BA-05 Trainer, Facility Manager, Organization Administrator, Reception Staff |
| User Journey | BA-06 Section 8 Trainer Journey, Section 18 Personal Training Journey |
| Stakeholder | BA-07 Trainer, Facility Manager, Organization Administrator |
| Non-Functional Requirement | BA-09 Section 2.6 Usability, Section 2.10 Auditability, Section 3.2 Authorization |
| Assumption / Constraint / Risk | BA-10 BA-ASS-004, BA-ASS-011, BA-RSK-009 |

### Purpose

To enable Trainer Attendance within Trainer Management so Digitize can execute Record Trainer Attendance consistently across Organizations, Facilities, Sites, users, and related operational or commercial services.

### Functional Requirement

The system shall support Record Trainer Attendance as an atomic Trainer Management capability, including scoped data capture, business-rule validation, permission enforcement, lifecycle handling, related service synchronization, notification generation, reporting contribution, and immutable audit recording.

### Business Justification

Record Trainer Attendance is required to preserve operational control, revenue accuracy, service continuity, customer trust, and enterprise traceability for Trainer processes. Without this capability, downstream modules would rely on incomplete, manual, or inconsistent records.

### Actors

- Trainer
- Organization Administrator
- Customer
- System
- Notification Service
- Reporting Service
- Audit Service

### Preconditions

- Organization is Active.
- Facility and Site context are Active where applicable.
- Actor is authenticated.
- Actor has permission for Record Trainer Attendance.
- Required Trainer configuration and policies are available.
- Related records required by BA-03 BP-PTR-007 Start Personal Training Session, BP-ACT-011 Start Session are available and within authorized scope.

### Trigger

The capability is triggered when Trainer or the System initiates Record Trainer Attendance from Trainer Attendance, a related workflow, a scheduled job, or an approved integration event.

### In Scope

- Capture or retrieve required Trainer context.
- Validate Organization, Facility, Site, Customer, user, and policy scope where applicable.
- Execute Record Trainer Attendance according to approved business rules.
- Persist the resulting Trainer state or transaction.
- Synchronize related operational, commercial, reporting, notification, and audit records.
- Provide confirmation, exception handling, and traceability.

### Out of Scope

- Cross-Organization data movement.
- Physical deletion of historical records.
- Changes to frozen BA source documents.
- Technical implementation details belonging to SAD, API Specification, or Database Design.
- Manual bypass of configured approval, payment, capacity, security, or audit controls.

### Inputs

- Organization ID
- Facility ID, where applicable
- Site ID, where applicable
- Trainer reference
- Customer reference, where applicable
- Effective date and time, where applicable
- Status or action reason, where applicable
- Payment, billing, trainer, session, or subscription reference where applicable
- Actor remarks, where applicable

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Trainer ID | Primary business record reference | Identifier | Yes | System / User | Must exist or be generated within scope | Core reference for Record Trainer Attendance |
| Organization ID | Tenant Organization context | Identifier | Yes | Session / System | Must be Active and authorized | Enforces tenant isolation |
| Facility ID | Facility context | Identifier | Conditional | User / System | Must be Active where applicable | Required for facility-level operations |
| Site ID | Site context | Identifier | Conditional | User / System | Must belong to Facility where applicable | Required for site-level operations |
| Status | Lifecycle or processing state | Enum | Yes | System | Must follow allowed state transitions | Drives UI and downstream access |
| Effective Date | Date when action applies | DateTime | Conditional | User / System | Must satisfy policy | Supports scheduled or immediate actions |
| Reason / Remarks | Business explanation | Text | Conditional | User | Required for governed changes | Stored for audit |

### Main Flow

1. Actor opens Trainer Attendance or the related workflow.
2. The system validates authentication, authorization, tenant scope, and current operating context.
3. The system loads the required Trainer records, related configuration, and policy controls.
4. Actor enters or confirms the information required to record trainer attendance.
5. The system validates mandatory data, lifecycle status, ownership, eligibility, financial, capacity, schedule, and security rules where applicable.
6. The system executes Record Trainer Attendance and persists the resulting Trainer state or transaction.
7. The system updates related history, reporting read models, and downstream references.
8. The system emits business events and notification events.
9. The system records immutable audit events with actor, timestamp, scope, and changed values.
10. The system displays confirmation with the resulting status and reference number.

### Alternate Flows

- If the action requires approval, the system creates an approval request and holds processing in a pending state until approval is completed.
- If the action is scheduled for a future date, the system stores the requested change and applies it through the scheduler on the effective date.
- If payment, billing, capacity, trainer, session, or entitlement handling is not applicable, the system skips that validation path while preserving audit traceability.
- If the user has read-only access, the system displays current details but hides or disables execution controls.

### Exception Flows

- If the actor lacks permission, the request is denied and a security audit event is recorded.
- If required data is missing or invalid, the system blocks submission and highlights the validation errors.
- If the action violates Organization, Facility, Site, capacity, schedule, payment, or lifecycle policy, the system rejects the request or routes for approved override where configured.
- If a related service is unavailable, the system fails safely, records the failure, and prevents inconsistent partial updates.
- If notification delivery fails, the core transaction remains valid and the notification failure is logged for retry.

### Outputs

- Trainer record created, updated, validated, or reported according to the action.
- Lifecycle or processing status updated.
- Related history entry created.
- Business events emitted.
- Notifications generated where configured.
- Audit events recorded.
- Reports or dashboards updated where applicable.

### UI Behaviour

Trainer Attendance shall display scoped context, mandatory fields, lifecycle status, policy warnings, validation results, available actions, confirmation prompts, read-only states, pagination or filters where applicable, and responsive behavior for front-desk and administrative usage.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-TRN-007-001 | Actor must have permission to execute Record Trainer Attendance. | Deny request and audit. | Critical |
| VAL-TRN-007-002 | Record must belong to the authorized Organization scope. | Deny request. | Critical |
| VAL-TRN-007-003 | Mandatory inputs must be complete and valid. | Block submission. | Critical |
| VAL-TRN-007-004 | Lifecycle and policy rules from BA-02 must be satisfied. | Reject or route for approval. | High |
| VAL-TRN-007-005 | Historical and audit records must be preserved. | Roll back or mark for recovery. | Critical |

### Business Rules

- BA-02 BR-TRN-007
- BA-02 BR-TRN-009
- BA-02 BR-AUD-003
- BA-02 BR-SEC-004

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| trn.record.trainer.attendance.view | Trainer | Read | View Record Trainer Attendance context |
| trn.record.trainer.attendance.execute | Trainer | Execute | Execute Record Trainer Attendance |
| trn.record.trainer.attendance.approve | Organization Administrator | Approve | Approve governed exceptions where configured |
| trn.record.trainer.attendance.audit.view | Organization Administrator / Support Executive | Read | View audit trace |

### Security Considerations

The capability shall enforce authentication, role-based authorization, tenant isolation, Organization scope, Facility and Site access boundaries, sensitive data masking, secure references, and immutable audit logging.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Record Trainer Attendance Completed | Primary actor and configured stakeholders | In-App / Email | Action completes | Include reference, status, and effective date where applicable |
| Record Trainer Attendance Requires Approval | Approver | In-App | Approval rule applies | Include safe summary and requested action |
| Record Trainer Attendance Failed | Primary actor | In-App | Validation or processing fails | Include safe failure reason and next action |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| RecordTrainerAttendanceRequested | Trainer Management | Approval Workflow, Audit Service |
| RecordTrainerAttendanceCompleted | Trainer Management | Notification Service, Reporting Service, Audit Service |
| RecordTrainerAttendanceRejected | Trainer Management | Notification Service, Audit Service |

### Audit Events

| Audit Event | Description | Actor | Target Entity | Key Data |
|---|---|---|---|---|
| RECORD_TRAINER_ATTENDANCE_REQUESTED | Record Trainer Attendance requested | Trainer | Trainer | Scope, reference, and reason |
| RECORD_TRAINER_ATTENDANCE_COMPLETED | Record Trainer Attendance completed | Trainer / System | Trainer | Previous and new state |
| RECORD_TRAINER_ATTENDANCE_REJECTED | Record Trainer Attendance rejected | System | Trainer | Rejection reason |

### Reports Generated

- Trainer Management Operational Report
- Trainer Management History Report
- Trainer Management Exception Report
- Executive Dashboard

### Related Screens

- Trainer Attendance
- Trainer Management Dashboard
- Trainer Management History
- Audit Log Viewer

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/trainers/{trainerId}/attendance | POST | Authorized token | Execute Record Trainer Attendance | 200 OK or 201 Created with result |
| /api/v1/trainers/{trainerId}/attendance/history | GET | Authorized token | Retrieve Record Trainer Attendance history | 200 OK with history |
| /api/v1/audit-logs | GET | Authorized token | Retrieve related audit events | 200 OK with scoped audit records |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Trainer | Create / Update / Read | Support Record Trainer Attendance | Governed by Organization scope |
| Trainer Assignment | Read / Insert | Support Record Trainer Attendance | Governed by Organization scope |
| Trainer Availability | Read / Insert | Support Record Trainer Attendance | Governed by Organization scope |
| Trainer Status | Read / Insert | Support Record Trainer Attendance | Governed by Organization scope |
| Trainer History | Read / Insert | Support Record Trainer Attendance | Governed by Organization scope |
| Audit Log | Insert | Record auditable activity | Immutable |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Draft | Record Trainer Attendance initiated | Validated | Trainer | Required data captured |
| Validated | Validation succeeds | Pending Approval | System | BA-02 rules satisfied |
| Pending Approval | Processing completes | Completed | System | Related updates succeed |
| Pending Approval | Approval or policy failure | Rejected | System / Approver | Request rejected |
| Completed | View history | Completed | Authorized user | Read-only historical access |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| TRN-007-001 | Record Trainer Attendance cannot be completed because required information is missing. | Missing mandatory data | Complete required fields |
| TRN-007-002 | You do not have permission to perform this action. | Authorization failure | Request access |
| TRN-007-003 | The selected record is not eligible for this action. | Policy or lifecycle violation | Review record status |
| TRN-007-004 | Record Trainer Attendance could not be completed due to a system or integration error. | Processing failure | Retry or contact support |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Execute Record Trainer Attendance | Given the actor has required permission and valid scope | When the actor submits valid information | Then the system shall complete Record Trainer Attendance successfully |
| Enforce validation | Given mandatory data or policy conditions are invalid | When the action is submitted | Then the system shall reject the request with a clear message |
| Preserve audit | Given the action completes or fails | When processing ends | Then audit events shall record actor, timestamp, scope, and outcome |
| Protect scope | Given the selected record is outside authorized scope | When the action is requested | Then the system shall deny access |

### Dependencies

- User & Role Management
- Facility Management
- Site Management
- Activity & Batch Management
- Personal Training
- Attendance Management
- Audit Service

### Operational Considerations

Record Trainer Attendance should be designed for high-volume operational use, retry-safe processing, clear exception handling, and support-team diagnostics without exposing sensitive data.

### Non-Functional Considerations

This requirement shall satisfy Digitize non-functional expectations for availability, reliability, performance, scalability, security, configurability, maintainability, and auditability.

### Assumptions

- Required master data and configuration are maintained by authorized users.
- Related services expose stable APIs for validation and synchronization.
- Organization policies define approval, retention, notification, and exception behavior.

### Success Criteria

Record Trainer Attendance is completed accurately, securely, and audibly, with downstream records synchronized and no loss of historical traceability.

### Related Functional Requirements

- FR-TRN-001 - Register Trainer Profile
- FR-TRN-002 - Assign Trainer to Facilities and Sites
- FR-TRN-003 - Maintain Trainer Availability
- FR-TRN-004 - Validate Trainer Schedule Conflicts
- FR-AUD-001 - Record Audit Events

### Notes

Record Trainer Attendance shall remain aligned with the approved BA source documents and shall not introduce behavior that bypasses tenant isolation, lifecycle governance, financial controls, or auditability.

---

## FR-TRN-008 - Manage Trainer Status

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-TRN-008 |
| Requirement Name | Manage Trainer Status |
| Functional Module | Trainer Management |
| Business Domain | Trainer |
| Business Capability | Trainer Lifecycle |
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
| Business Requirement | BA-01 Section 15 Membership Lifecycle |
| Business Rule | BA-02 BR-TRN-006, BR-TRN-009, BR-TRN-010, BR-AUD-003 |
| Business Process | BA-03 Staff Identity & Access Processes |
| Business Process Flow | BA-04 Section 22 Batch Management Flow, Section 23 Personal Training Flow |
| Persona | BA-05 Trainer, Facility Manager, Organization Administrator, Reception Staff |
| User Journey | BA-06 Section 8 Trainer Journey, Section 18 Personal Training Journey |
| Stakeholder | BA-07 Trainer, Facility Manager, Organization Administrator |
| Non-Functional Requirement | BA-09 Section 2.6 Usability, Section 2.10 Auditability, Section 3.2 Authorization |
| Assumption / Constraint / Risk | BA-10 BA-ASS-004, BA-ASS-011, BA-RSK-009 |

### Purpose

To enable Trainer Lifecycle within Trainer Management so Digitize can execute Manage Trainer Status consistently across Organizations, Facilities, Sites, users, and related operational or commercial services.

### Functional Requirement

The system shall support Manage Trainer Status as an atomic Trainer Management capability, including scoped data capture, business-rule validation, permission enforcement, lifecycle handling, related service synchronization, notification generation, reporting contribution, and immutable audit recording.

### Business Justification

Manage Trainer Status is required to preserve operational control, revenue accuracy, service continuity, customer trust, and enterprise traceability for Trainer processes. Without this capability, downstream modules would rely on incomplete, manual, or inconsistent records.

### Actors

- Organization Administrator
- Organization Administrator
- Customer
- System
- Notification Service
- Reporting Service
- Audit Service

### Preconditions

- Organization is Active.
- Facility and Site context are Active where applicable.
- Actor is authenticated.
- Actor has permission for Manage Trainer Status.
- Required Trainer configuration and policies are available.
- Related records required by BA-03 Staff Identity & Access Processes are available and within authorized scope.

### Trigger

The capability is triggered when Organization Administrator or the System initiates Manage Trainer Status from Trainer Status, a related workflow, a scheduled job, or an approved integration event.

### In Scope

- Capture or retrieve required Trainer context.
- Validate Organization, Facility, Site, Customer, user, and policy scope where applicable.
- Execute Manage Trainer Status according to approved business rules.
- Persist the resulting Trainer state or transaction.
- Synchronize related operational, commercial, reporting, notification, and audit records.
- Provide confirmation, exception handling, and traceability.

### Out of Scope

- Cross-Organization data movement.
- Physical deletion of historical records.
- Changes to frozen BA source documents.
- Technical implementation details belonging to SAD, API Specification, or Database Design.
- Manual bypass of configured approval, payment, capacity, security, or audit controls.

### Inputs

- Organization ID
- Facility ID, where applicable
- Site ID, where applicable
- Trainer reference
- Customer reference, where applicable
- Effective date and time, where applicable
- Status or action reason, where applicable
- Payment, billing, trainer, session, or subscription reference where applicable
- Actor remarks, where applicable

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Trainer ID | Primary business record reference | Identifier | Yes | System / User | Must exist or be generated within scope | Core reference for Manage Trainer Status |
| Organization ID | Tenant Organization context | Identifier | Yes | Session / System | Must be Active and authorized | Enforces tenant isolation |
| Facility ID | Facility context | Identifier | Conditional | User / System | Must be Active where applicable | Required for facility-level operations |
| Site ID | Site context | Identifier | Conditional | User / System | Must belong to Facility where applicable | Required for site-level operations |
| Status | Lifecycle or processing state | Enum | Yes | System | Must follow allowed state transitions | Drives UI and downstream access |
| Effective Date | Date when action applies | DateTime | Conditional | User / System | Must satisfy policy | Supports scheduled or immediate actions |
| Reason / Remarks | Business explanation | Text | Conditional | User | Required for governed changes | Stored for audit |

### Main Flow

1. Actor opens Trainer Status or the related workflow.
2. The system validates authentication, authorization, tenant scope, and current operating context.
3. The system loads the required Trainer records, related configuration, and policy controls.
4. Actor enters or confirms the information required to manage trainer status.
5. The system validates mandatory data, lifecycle status, ownership, eligibility, financial, capacity, schedule, and security rules where applicable.
6. The system executes Manage Trainer Status and persists the resulting Trainer state or transaction.
7. The system updates related history, reporting read models, and downstream references.
8. The system emits business events and notification events.
9. The system records immutable audit events with actor, timestamp, scope, and changed values.
10. The system displays confirmation with the resulting status and reference number.

### Alternate Flows

- If the action requires approval, the system creates an approval request and holds processing in a pending state until approval is completed.
- If the action is scheduled for a future date, the system stores the requested change and applies it through the scheduler on the effective date.
- If payment, billing, capacity, trainer, session, or entitlement handling is not applicable, the system skips that validation path while preserving audit traceability.
- If the user has read-only access, the system displays current details but hides or disables execution controls.

### Exception Flows

- If the actor lacks permission, the request is denied and a security audit event is recorded.
- If required data is missing or invalid, the system blocks submission and highlights the validation errors.
- If the action violates Organization, Facility, Site, capacity, schedule, payment, or lifecycle policy, the system rejects the request or routes for approved override where configured.
- If a related service is unavailable, the system fails safely, records the failure, and prevents inconsistent partial updates.
- If notification delivery fails, the core transaction remains valid and the notification failure is logged for retry.

### Outputs

- Trainer record created, updated, validated, or reported according to the action.
- Lifecycle or processing status updated.
- Related history entry created.
- Business events emitted.
- Notifications generated where configured.
- Audit events recorded.
- Reports or dashboards updated where applicable.

### UI Behaviour

Trainer Status shall display scoped context, mandatory fields, lifecycle status, policy warnings, validation results, available actions, confirmation prompts, read-only states, pagination or filters where applicable, and responsive behavior for front-desk and administrative usage.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-TRN-008-001 | Actor must have permission to execute Manage Trainer Status. | Deny request and audit. | Critical |
| VAL-TRN-008-002 | Record must belong to the authorized Organization scope. | Deny request. | Critical |
| VAL-TRN-008-003 | Mandatory inputs must be complete and valid. | Block submission. | Critical |
| VAL-TRN-008-004 | Lifecycle and policy rules from BA-02 must be satisfied. | Reject or route for approval. | High |
| VAL-TRN-008-005 | Historical and audit records must be preserved. | Roll back or mark for recovery. | Critical |

### Business Rules

- BA-02 BR-TRN-006
- BA-02 BR-TRN-009
- BA-02 BR-TRN-010
- BA-02 BR-AUD-003

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| trn.manage.trainer.status.view | Organization Administrator | Read | View Manage Trainer Status context |
| trn.manage.trainer.status.execute | Organization Administrator | Execute | Execute Manage Trainer Status |
| trn.manage.trainer.status.approve | Organization Administrator | Approve | Approve governed exceptions where configured |
| trn.manage.trainer.status.audit.view | Organization Administrator / Support Executive | Read | View audit trace |

### Security Considerations

The capability shall enforce authentication, role-based authorization, tenant isolation, Organization scope, Facility and Site access boundaries, sensitive data masking, secure references, and immutable audit logging.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Manage Trainer Status Completed | Primary actor and configured stakeholders | In-App / Email | Action completes | Include reference, status, and effective date where applicable |
| Manage Trainer Status Requires Approval | Approver | In-App | Approval rule applies | Include safe summary and requested action |
| Manage Trainer Status Failed | Primary actor | In-App | Validation or processing fails | Include safe failure reason and next action |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| ManageTrainerStatusRequested | Trainer Management | Approval Workflow, Audit Service |
| ManageTrainerStatusCompleted | Trainer Management | Notification Service, Reporting Service, Audit Service |
| ManageTrainerStatusRejected | Trainer Management | Notification Service, Audit Service |

### Audit Events

| Audit Event | Description | Actor | Target Entity | Key Data |
|---|---|---|---|---|
| MANAGE_TRAINER_STATUS_REQUESTED | Manage Trainer Status requested | Organization Administrator | Trainer | Scope, reference, and reason |
| MANAGE_TRAINER_STATUS_COMPLETED | Manage Trainer Status completed | Organization Administrator / System | Trainer | Previous and new state |
| MANAGE_TRAINER_STATUS_REJECTED | Manage Trainer Status rejected | System | Trainer | Rejection reason |

### Reports Generated

- Trainer Management Operational Report
- Trainer Management History Report
- Trainer Management Exception Report
- Executive Dashboard

### Related Screens

- Trainer Status
- Trainer Management Dashboard
- Trainer Management History
- Audit Log Viewer

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/trainers/{trainerId}/status | PATCH | Authorized token | Execute Manage Trainer Status | 200 OK or 201 Created with result |
| /api/v1/trainers/{trainerId}/status/history | GET | Authorized token | Retrieve Manage Trainer Status history | 200 OK with history |
| /api/v1/audit-logs | GET | Authorized token | Retrieve related audit events | 200 OK with scoped audit records |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Trainer | Create / Update / Read | Support Manage Trainer Status | Governed by Organization scope |
| Trainer Assignment | Read / Insert | Support Manage Trainer Status | Governed by Organization scope |
| Trainer Availability | Read / Insert | Support Manage Trainer Status | Governed by Organization scope |
| Trainer Status | Read / Insert | Support Manage Trainer Status | Governed by Organization scope |
| Trainer History | Read / Insert | Support Manage Trainer Status | Governed by Organization scope |
| Audit Log | Insert | Record auditable activity | Immutable |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Draft | Manage Trainer Status initiated | Validated | Organization Administrator | Required data captured |
| Validated | Validation succeeds | Pending Approval | System | BA-02 rules satisfied |
| Pending Approval | Processing completes | Completed | System | Related updates succeed |
| Pending Approval | Approval or policy failure | Rejected | System / Approver | Request rejected |
| Completed | View history | Completed | Authorized user | Read-only historical access |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| TRN-008-001 | Manage Trainer Status cannot be completed because required information is missing. | Missing mandatory data | Complete required fields |
| TRN-008-002 | You do not have permission to perform this action. | Authorization failure | Request access |
| TRN-008-003 | The selected record is not eligible for this action. | Policy or lifecycle violation | Review record status |
| TRN-008-004 | Manage Trainer Status could not be completed due to a system or integration error. | Processing failure | Retry or contact support |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Execute Manage Trainer Status | Given the actor has required permission and valid scope | When the actor submits valid information | Then the system shall complete Manage Trainer Status successfully |
| Enforce validation | Given mandatory data or policy conditions are invalid | When the action is submitted | Then the system shall reject the request with a clear message |
| Preserve audit | Given the action completes or fails | When processing ends | Then audit events shall record actor, timestamp, scope, and outcome |
| Protect scope | Given the selected record is outside authorized scope | When the action is requested | Then the system shall deny access |

### Dependencies

- User & Role Management
- Facility Management
- Site Management
- Activity & Batch Management
- Personal Training
- Attendance Management
- Audit Service

### Operational Considerations

Manage Trainer Status should be designed for high-volume operational use, retry-safe processing, clear exception handling, and support-team diagnostics without exposing sensitive data.

### Non-Functional Considerations

This requirement shall satisfy Digitize non-functional expectations for availability, reliability, performance, scalability, security, configurability, maintainability, and auditability.

### Assumptions

- Required master data and configuration are maintained by authorized users.
- Related services expose stable APIs for validation and synchronization.
- Organization policies define approval, retention, notification, and exception behavior.

### Success Criteria

Manage Trainer Status is completed accurately, securely, and audibly, with downstream records synchronized and no loss of historical traceability.

### Related Functional Requirements

- FR-TRN-001 - Register Trainer Profile
- FR-TRN-002 - Assign Trainer to Facilities and Sites
- FR-TRN-003 - Maintain Trainer Availability
- FR-TRN-004 - Validate Trainer Schedule Conflicts
- FR-AUD-001 - Record Audit Events

### Notes

Manage Trainer Status shall remain aligned with the approved BA source documents and shall not introduce behavior that bypasses tenant isolation, lifecycle governance, financial controls, or auditability.

---

## FR-TRN-009 - View Trainer History

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-TRN-009 |
| Requirement Name | View Trainer History |
| Functional Module | Trainer Management |
| Business Domain | Trainer |
| Business Capability | Trainer History |
| Requirement Type | Functional |
| Requirement Category | Reporting |
| Requirement Version | 1.0 |
| Requirement Status | Approved |
| Priority | Medium |
| Complexity | Medium |
| Release Version | 1.0 |
| Owner | Product Management |

### Traceability References

| Traceability Type | Reference |
|---|---|
| Business Requirement | BA-01 Section 15 Membership Lifecycle |
| Business Rule | BA-02 BR-TRN-009, BR-TRN-010, BR-AUD-008, BR-SEC-004 |
| Business Process | BA-03 BP-PTR-011 View Training History |
| Business Process Flow | BA-04 Section 22 Batch Management Flow, Section 23 Personal Training Flow |
| Persona | BA-05 Trainer, Facility Manager, Organization Administrator, Reception Staff |
| User Journey | BA-06 Section 8 Trainer Journey, Section 18 Personal Training Journey |
| Stakeholder | BA-07 Trainer, Facility Manager, Organization Administrator |
| Non-Functional Requirement | BA-09 Section 2.6 Usability, Section 2.10 Auditability, Section 3.2 Authorization |
| Assumption / Constraint / Risk | BA-10 BA-ASS-004, BA-ASS-011, BA-RSK-009 |

### Purpose

To enable Trainer History within Trainer Management so Digitize can execute View Trainer History consistently across Organizations, Facilities, Sites, users, and related operational or commercial services.

### Functional Requirement

The system shall support View Trainer History as an atomic Trainer Management capability, including scoped data capture, business-rule validation, permission enforcement, lifecycle handling, related service synchronization, notification generation, reporting contribution, and immutable audit recording.

### Business Justification

View Trainer History is required to preserve operational control, revenue accuracy, service continuity, customer trust, and enterprise traceability for Trainer processes. Without this capability, downstream modules would rely on incomplete, manual, or inconsistent records.

### Actors

- Facility Manager
- Organization Administrator
- Customer
- System
- Notification Service
- Reporting Service
- Audit Service

### Preconditions

- Organization is Active.
- Facility and Site context are Active where applicable.
- Actor is authenticated.
- Actor has permission for View Trainer History.
- Required Trainer configuration and policies are available.
- Related records required by BA-03 BP-PTR-011 View Training History are available and within authorized scope.

### Trigger

The capability is triggered when Facility Manager or the System initiates View Trainer History from Trainer History, a related workflow, a scheduled job, or an approved integration event.

### In Scope

- Capture or retrieve required Trainer context.
- Validate Organization, Facility, Site, Customer, user, and policy scope where applicable.
- Execute View Trainer History according to approved business rules.
- Persist the resulting Trainer state or transaction.
- Synchronize related operational, commercial, reporting, notification, and audit records.
- Provide confirmation, exception handling, and traceability.

### Out of Scope

- Cross-Organization data movement.
- Physical deletion of historical records.
- Changes to frozen BA source documents.
- Technical implementation details belonging to SAD, API Specification, or Database Design.
- Manual bypass of configured approval, payment, capacity, security, or audit controls.

### Inputs

- Organization ID
- Facility ID, where applicable
- Site ID, where applicable
- Trainer reference
- Customer reference, where applicable
- Effective date and time, where applicable
- Status or action reason, where applicable
- Payment, billing, trainer, session, or subscription reference where applicable
- Actor remarks, where applicable

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Trainer ID | Primary business record reference | Identifier | Yes | System / User | Must exist or be generated within scope | Core reference for View Trainer History |
| Organization ID | Tenant Organization context | Identifier | Yes | Session / System | Must be Active and authorized | Enforces tenant isolation |
| Facility ID | Facility context | Identifier | Conditional | User / System | Must be Active where applicable | Required for facility-level operations |
| Site ID | Site context | Identifier | Conditional | User / System | Must belong to Facility where applicable | Required for site-level operations |
| Status | Lifecycle or processing state | Enum | Yes | System | Must follow allowed state transitions | Drives UI and downstream access |
| Effective Date | Date when action applies | DateTime | Conditional | User / System | Must satisfy policy | Supports scheduled or immediate actions |
| Reason / Remarks | Business explanation | Text | Conditional | User | Required for governed changes | Stored for audit |

### Main Flow

1. Actor opens Trainer History or the related workflow.
2. The system validates authentication, authorization, tenant scope, and current operating context.
3. The system loads the required Trainer records, related configuration, and policy controls.
4. Actor enters or confirms the information required to view trainer history.
5. The system validates mandatory data, lifecycle status, ownership, eligibility, financial, capacity, schedule, and security rules where applicable.
6. The system executes View Trainer History and persists the resulting Trainer state or transaction.
7. The system updates related history, reporting read models, and downstream references.
8. The system emits business events and notification events.
9. The system records immutable audit events with actor, timestamp, scope, and changed values.
10. The system displays confirmation with the resulting status and reference number.

### Alternate Flows

- If the action requires approval, the system creates an approval request and holds processing in a pending state until approval is completed.
- If the action is scheduled for a future date, the system stores the requested change and applies it through the scheduler on the effective date.
- If payment, billing, capacity, trainer, session, or entitlement handling is not applicable, the system skips that validation path while preserving audit traceability.
- If the user has read-only access, the system displays current details but hides or disables execution controls.

### Exception Flows

- If the actor lacks permission, the request is denied and a security audit event is recorded.
- If required data is missing or invalid, the system blocks submission and highlights the validation errors.
- If the action violates Organization, Facility, Site, capacity, schedule, payment, or lifecycle policy, the system rejects the request or routes for approved override where configured.
- If a related service is unavailable, the system fails safely, records the failure, and prevents inconsistent partial updates.
- If notification delivery fails, the core transaction remains valid and the notification failure is logged for retry.

### Outputs

- Trainer record created, updated, validated, or reported according to the action.
- Lifecycle or processing status updated.
- Related history entry created.
- Business events emitted.
- Notifications generated where configured.
- Audit events recorded.
- Reports or dashboards updated where applicable.

### UI Behaviour

Trainer History shall display scoped context, mandatory fields, lifecycle status, policy warnings, validation results, available actions, confirmation prompts, read-only states, pagination or filters where applicable, and responsive behavior for front-desk and administrative usage.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-TRN-009-001 | Actor must have permission to execute View Trainer History. | Deny request and audit. | Critical |
| VAL-TRN-009-002 | Record must belong to the authorized Organization scope. | Deny request. | Critical |
| VAL-TRN-009-003 | Mandatory inputs must be complete and valid. | Block submission. | Critical |
| VAL-TRN-009-004 | Lifecycle and policy rules from BA-02 must be satisfied. | Reject or route for approval. | High |
| VAL-TRN-009-005 | Historical and audit records must be preserved. | Roll back or mark for recovery. | Critical |

### Business Rules

- BA-02 BR-TRN-009
- BA-02 BR-TRN-010
- BA-02 BR-AUD-008
- BA-02 BR-SEC-004

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| trn.view.trainer.history.view | Facility Manager | Read | View View Trainer History context |
| trn.view.trainer.history.execute | Facility Manager | Execute | Execute View Trainer History |
| trn.view.trainer.history.approve | Organization Administrator | Approve | Approve governed exceptions where configured |
| trn.view.trainer.history.audit.view | Organization Administrator / Support Executive | Read | View audit trace |

### Security Considerations

The capability shall enforce authentication, role-based authorization, tenant isolation, Organization scope, Facility and Site access boundaries, sensitive data masking, secure references, and immutable audit logging.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| View Trainer History Completed | Primary actor and configured stakeholders | In-App / Email | Action completes | Include reference, status, and effective date where applicable |
| View Trainer History Requires Approval | Approver | In-App | Approval rule applies | Include safe summary and requested action |
| View Trainer History Failed | Primary actor | In-App | Validation or processing fails | Include safe failure reason and next action |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| ViewTrainerHistoryRequested | Trainer Management | Approval Workflow, Audit Service |
| ViewTrainerHistoryCompleted | Trainer Management | Notification Service, Reporting Service, Audit Service |
| ViewTrainerHistoryRejected | Trainer Management | Notification Service, Audit Service |

### Audit Events

| Audit Event | Description | Actor | Target Entity | Key Data |
|---|---|---|---|---|
| VIEW_TRAINER_HISTORY_REQUESTED | View Trainer History requested | Facility Manager | Trainer | Scope, reference, and reason |
| VIEW_TRAINER_HISTORY_COMPLETED | View Trainer History completed | Facility Manager / System | Trainer | Previous and new state |
| VIEW_TRAINER_HISTORY_REJECTED | View Trainer History rejected | System | Trainer | Rejection reason |

### Reports Generated

- Trainer Management Operational Report
- Trainer Management History Report
- Trainer Management Exception Report
- Executive Dashboard

### Related Screens

- Trainer History
- Trainer Management Dashboard
- Trainer Management History
- Audit Log Viewer

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/trainers/{trainerId}/history | GET | Authorized token | Execute View Trainer History | 200 OK or 201 Created with result |
| /api/v1/trainers/{trainerId}/history/history | GET | Authorized token | Retrieve View Trainer History history | 200 OK with history |
| /api/v1/audit-logs | GET | Authorized token | Retrieve related audit events | 200 OK with scoped audit records |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Trainer | Read | Support View Trainer History | Governed by Organization scope |
| Trainer Assignment | Read / Insert | Support View Trainer History | Governed by Organization scope |
| Trainer Availability | Read / Insert | Support View Trainer History | Governed by Organization scope |
| Trainer Status | Read / Insert | Support View Trainer History | Governed by Organization scope |
| Trainer History | Read / Insert | Support View Trainer History | Governed by Organization scope |
| Audit Log | Insert | Record auditable activity | Immutable |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Not Requested | View Trainer History initiated | Generating | Facility Manager | Required data captured |
| Generating | Validation succeeds | Ready | System | BA-02 rules satisfied |
| Ready | Processing completes | Export Pending | System | Related updates succeed |
| Ready | Approval or policy failure | Failed | System / Approver | Request rejected |
| Export Pending | View history | Export Pending | Authorized user | Read-only historical access |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| TRN-009-001 | View Trainer History cannot be completed because required information is missing. | Missing mandatory data | Complete required fields |
| TRN-009-002 | You do not have permission to perform this action. | Authorization failure | Request access |
| TRN-009-003 | The selected record is not eligible for this action. | Policy or lifecycle violation | Review record status |
| TRN-009-004 | View Trainer History could not be completed due to a system or integration error. | Processing failure | Retry or contact support |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Execute View Trainer History | Given the actor has required permission and valid scope | When the actor submits valid information | Then the system shall complete View Trainer History successfully |
| Enforce validation | Given mandatory data or policy conditions are invalid | When the action is submitted | Then the system shall reject the request with a clear message |
| Preserve audit | Given the action completes or fails | When processing ends | Then audit events shall record actor, timestamp, scope, and outcome |
| Protect scope | Given the selected record is outside authorized scope | When the action is requested | Then the system shall deny access |

### Dependencies

- User & Role Management
- Facility Management
- Site Management
- Activity & Batch Management
- Personal Training
- Attendance Management
- Audit Service

### Operational Considerations

View Trainer History should be designed for high-volume operational use, retry-safe processing, clear exception handling, and support-team diagnostics without exposing sensitive data.

### Non-Functional Considerations

This requirement shall satisfy Digitize non-functional expectations for availability, reliability, performance, scalability, security, configurability, maintainability, and auditability.

### Assumptions

- Required master data and configuration are maintained by authorized users.
- Related services expose stable APIs for validation and synchronization.
- Organization policies define approval, retention, notification, and exception behavior.

### Success Criteria

View Trainer History is completed accurately, securely, and audibly, with downstream records synchronized and no loss of historical traceability.

### Related Functional Requirements

- FR-TRN-001 - Register Trainer Profile
- FR-TRN-002 - Assign Trainer to Facilities and Sites
- FR-TRN-003 - Maintain Trainer Availability
- FR-TRN-004 - Validate Trainer Schedule Conflicts
- FR-AUD-001 - Record Audit Events

### Notes

View Trainer History shall remain aligned with the approved BA source documents and shall not introduce behavior that bypasses tenant isolation, lifecycle governance, financial controls, or auditability.

---

## FR-TRN-010 - Generate Trainer Performance Summary

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-TRN-010 |
| Requirement Name | Generate Trainer Performance Summary |
| Functional Module | Trainer Management |
| Business Domain | Trainer |
| Business Capability | Trainer Performance Monitoring |
| Requirement Type | Functional |
| Requirement Category | Reporting |
| Requirement Version | 1.0 |
| Requirement Status | Approved |
| Priority | Medium |
| Complexity | Medium |
| Release Version | 1.0 |
| Owner | Product Management |

### Traceability References

| Traceability Type | Reference |
|---|---|
| Business Requirement | BA-01 Section 15 Membership Lifecycle |
| Business Rule | BA-02 BR-TRN-003, BR-TRN-004, BR-TRN-007, BR-TRN-009 |
| Business Process | BA-03 BP-PTR-012 Generate Trainer Performance Report |
| Business Process Flow | BA-04 Section 22 Batch Management Flow, Section 23 Personal Training Flow |
| Persona | BA-05 Trainer, Facility Manager, Organization Administrator, Reception Staff |
| User Journey | BA-06 Section 8 Trainer Journey, Section 18 Personal Training Journey |
| Stakeholder | BA-07 Trainer, Facility Manager, Organization Administrator |
| Non-Functional Requirement | BA-09 Section 2.6 Usability, Section 2.10 Auditability, Section 3.2 Authorization |
| Assumption / Constraint / Risk | BA-10 BA-ASS-004, BA-ASS-011, BA-RSK-009 |

### Purpose

To enable Trainer Performance Monitoring within Trainer Management so Digitize can execute Generate Trainer Performance Summary consistently across Organizations, Facilities, Sites, users, and related operational or commercial services.

### Functional Requirement

The system shall support Generate Trainer Performance Summary as an atomic Trainer Management capability, including scoped data capture, business-rule validation, permission enforcement, lifecycle handling, related service synchronization, notification generation, reporting contribution, and immutable audit recording.

### Business Justification

Generate Trainer Performance Summary is required to preserve operational control, revenue accuracy, service continuity, customer trust, and enterprise traceability for Trainer processes. Without this capability, downstream modules would rely on incomplete, manual, or inconsistent records.

### Actors

- Facility Manager
- Organization Administrator
- Customer
- System
- Notification Service
- Reporting Service
- Audit Service

### Preconditions

- Organization is Active.
- Facility and Site context are Active where applicable.
- Actor is authenticated.
- Actor has permission for Generate Trainer Performance Summary.
- Required Trainer configuration and policies are available.
- Related records required by BA-03 BP-PTR-012 Generate Trainer Performance Report are available and within authorized scope.

### Trigger

The capability is triggered when Facility Manager or the System initiates Generate Trainer Performance Summary from Trainer Performance Report, a related workflow, a scheduled job, or an approved integration event.

### In Scope

- Capture or retrieve required Trainer context.
- Validate Organization, Facility, Site, Customer, user, and policy scope where applicable.
- Execute Generate Trainer Performance Summary according to approved business rules.
- Persist the resulting Trainer state or transaction.
- Synchronize related operational, commercial, reporting, notification, and audit records.
- Provide confirmation, exception handling, and traceability.

### Out of Scope

- Cross-Organization data movement.
- Physical deletion of historical records.
- Changes to frozen BA source documents.
- Technical implementation details belonging to SAD, API Specification, or Database Design.
- Manual bypass of configured approval, payment, capacity, security, or audit controls.

### Inputs

- Organization ID
- Facility ID, where applicable
- Site ID, where applicable
- Trainer reference
- Customer reference, where applicable
- Effective date and time, where applicable
- Status or action reason, where applicable
- Payment, billing, trainer, session, or subscription reference where applicable
- Actor remarks, where applicable

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Trainer ID | Primary business record reference | Identifier | Yes | System / User | Must exist or be generated within scope | Core reference for Generate Trainer Performance Summary |
| Organization ID | Tenant Organization context | Identifier | Yes | Session / System | Must be Active and authorized | Enforces tenant isolation |
| Facility ID | Facility context | Identifier | Conditional | User / System | Must be Active where applicable | Required for facility-level operations |
| Site ID | Site context | Identifier | Conditional | User / System | Must belong to Facility where applicable | Required for site-level operations |
| Status | Lifecycle or processing state | Enum | Yes | System | Must follow allowed state transitions | Drives UI and downstream access |
| Effective Date | Date when action applies | DateTime | Conditional | User / System | Must satisfy policy | Supports scheduled or immediate actions |
| Reason / Remarks | Business explanation | Text | Conditional | User | Required for governed changes | Stored for audit |

### Main Flow

1. Actor opens Trainer Performance Report or the related workflow.
2. The system validates authentication, authorization, tenant scope, and current operating context.
3. The system loads the required Trainer records, related configuration, and policy controls.
4. Actor enters or confirms the information required to generate trainer performance summary.
5. The system validates mandatory data, lifecycle status, ownership, eligibility, financial, capacity, schedule, and security rules where applicable.
6. The system executes Generate Trainer Performance Summary and persists the resulting Trainer state or transaction.
7. The system updates related history, reporting read models, and downstream references.
8. The system emits business events and notification events.
9. The system records immutable audit events with actor, timestamp, scope, and changed values.
10. The system displays confirmation with the resulting status and reference number.

### Alternate Flows

- If the action requires approval, the system creates an approval request and holds processing in a pending state until approval is completed.
- If the action is scheduled for a future date, the system stores the requested change and applies it through the scheduler on the effective date.
- If payment, billing, capacity, trainer, session, or entitlement handling is not applicable, the system skips that validation path while preserving audit traceability.
- If the user has read-only access, the system displays current details but hides or disables execution controls.

### Exception Flows

- If the actor lacks permission, the request is denied and a security audit event is recorded.
- If required data is missing or invalid, the system blocks submission and highlights the validation errors.
- If the action violates Organization, Facility, Site, capacity, schedule, payment, or lifecycle policy, the system rejects the request or routes for approved override where configured.
- If a related service is unavailable, the system fails safely, records the failure, and prevents inconsistent partial updates.
- If notification delivery fails, the core transaction remains valid and the notification failure is logged for retry.

### Outputs

- Trainer record created, updated, validated, or reported according to the action.
- Lifecycle or processing status updated.
- Related history entry created.
- Business events emitted.
- Notifications generated where configured.
- Audit events recorded.
- Reports or dashboards updated where applicable.

### UI Behaviour

Trainer Performance Report shall display scoped context, mandatory fields, lifecycle status, policy warnings, validation results, available actions, confirmation prompts, read-only states, pagination or filters where applicable, and responsive behavior for front-desk and administrative usage.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-TRN-010-001 | Actor must have permission to execute Generate Trainer Performance Summary. | Deny request and audit. | Critical |
| VAL-TRN-010-002 | Record must belong to the authorized Organization scope. | Deny request. | Critical |
| VAL-TRN-010-003 | Mandatory inputs must be complete and valid. | Block submission. | Critical |
| VAL-TRN-010-004 | Lifecycle and policy rules from BA-02 must be satisfied. | Reject or route for approval. | High |
| VAL-TRN-010-005 | Historical and audit records must be preserved. | Roll back or mark for recovery. | Critical |

### Business Rules

- BA-02 BR-TRN-003
- BA-02 BR-TRN-004
- BA-02 BR-TRN-007
- BA-02 BR-TRN-009

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| trn.generate.trainer.performance.summary.view | Facility Manager | Read | View Generate Trainer Performance Summary context |
| trn.generate.trainer.performance.summary.execute | Facility Manager | Execute | Execute Generate Trainer Performance Summary |
| trn.generate.trainer.performance.summary.approve | Organization Administrator | Approve | Approve governed exceptions where configured |
| trn.generate.trainer.performance.summary.audit.view | Organization Administrator / Support Executive | Read | View audit trace |

### Security Considerations

The capability shall enforce authentication, role-based authorization, tenant isolation, Organization scope, Facility and Site access boundaries, sensitive data masking, secure references, and immutable audit logging.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Generate Trainer Performance Summary Completed | Primary actor and configured stakeholders | In-App / Email | Action completes | Include reference, status, and effective date where applicable |
| Generate Trainer Performance Summary Requires Approval | Approver | In-App | Approval rule applies | Include safe summary and requested action |
| Generate Trainer Performance Summary Failed | Primary actor | In-App | Validation or processing fails | Include safe failure reason and next action |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| GenerateTrainerPerformanceSummaryRequested | Trainer Management | Approval Workflow, Audit Service |
| GenerateTrainerPerformanceSummaryCompleted | Trainer Management | Notification Service, Reporting Service, Audit Service |
| GenerateTrainerPerformanceSummaryRejected | Trainer Management | Notification Service, Audit Service |

### Audit Events

| Audit Event | Description | Actor | Target Entity | Key Data |
|---|---|---|---|---|
| GENERATE_TRAINER_PERFORMANCE_SUMMARY_REQUESTED | Generate Trainer Performance Summary requested | Facility Manager | Trainer | Scope, reference, and reason |
| GENERATE_TRAINER_PERFORMANCE_SUMMARY_COMPLETED | Generate Trainer Performance Summary completed | Facility Manager / System | Trainer | Previous and new state |
| GENERATE_TRAINER_PERFORMANCE_SUMMARY_REJECTED | Generate Trainer Performance Summary rejected | System | Trainer | Rejection reason |

### Reports Generated

- Trainer Management Operational Report
- Trainer Management History Report
- Trainer Management Exception Report
- Executive Dashboard

### Related Screens

- Trainer Performance Report
- Trainer Management Dashboard
- Trainer Management History
- Audit Log Viewer

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/reports/trainers/performance | GET | Authorized token | Execute Generate Trainer Performance Summary | 200 OK or 201 Created with result |
| /api/v1/reports/trainers/performance/history | GET | Authorized token | Retrieve Generate Trainer Performance Summary history | 200 OK with history |
| /api/v1/audit-logs | GET | Authorized token | Retrieve related audit events | 200 OK with scoped audit records |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Trainer | Read | Support Generate Trainer Performance Summary | Governed by Organization scope |
| Trainer Assignment | Read / Insert | Support Generate Trainer Performance Summary | Governed by Organization scope |
| Trainer Availability | Read / Insert | Support Generate Trainer Performance Summary | Governed by Organization scope |
| Trainer Status | Read / Insert | Support Generate Trainer Performance Summary | Governed by Organization scope |
| Trainer History | Read / Insert | Support Generate Trainer Performance Summary | Governed by Organization scope |
| Audit Log | Insert | Record auditable activity | Immutable |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Not Requested | Generate Trainer Performance Summary initiated | Generating | Facility Manager | Required data captured |
| Generating | Validation succeeds | Ready | System | BA-02 rules satisfied |
| Ready | Processing completes | Export Pending | System | Related updates succeed |
| Ready | Approval or policy failure | Failed | System / Approver | Request rejected |
| Export Pending | View history | Export Pending | Authorized user | Read-only historical access |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| TRN-010-001 | Generate Trainer Performance Summary cannot be completed because required information is missing. | Missing mandatory data | Complete required fields |
| TRN-010-002 | You do not have permission to perform this action. | Authorization failure | Request access |
| TRN-010-003 | The selected record is not eligible for this action. | Policy or lifecycle violation | Review record status |
| TRN-010-004 | Generate Trainer Performance Summary could not be completed due to a system or integration error. | Processing failure | Retry or contact support |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Execute Generate Trainer Performance Summary | Given the actor has required permission and valid scope | When the actor submits valid information | Then the system shall complete Generate Trainer Performance Summary successfully |
| Enforce validation | Given mandatory data or policy conditions are invalid | When the action is submitted | Then the system shall reject the request with a clear message |
| Preserve audit | Given the action completes or fails | When processing ends | Then audit events shall record actor, timestamp, scope, and outcome |
| Protect scope | Given the selected record is outside authorized scope | When the action is requested | Then the system shall deny access |

### Dependencies

- User & Role Management
- Facility Management
- Site Management
- Activity & Batch Management
- Personal Training
- Attendance Management
- Audit Service

### Operational Considerations

Generate Trainer Performance Summary should be designed for high-volume operational use, retry-safe processing, clear exception handling, and support-team diagnostics without exposing sensitive data.

### Non-Functional Considerations

This requirement shall satisfy Digitize non-functional expectations for availability, reliability, performance, scalability, security, configurability, maintainability, and auditability.

### Assumptions

- Required master data and configuration are maintained by authorized users.
- Related services expose stable APIs for validation and synchronization.
- Organization policies define approval, retention, notification, and exception behavior.

### Success Criteria

Generate Trainer Performance Summary is completed accurately, securely, and audibly, with downstream records synchronized and no loss of historical traceability.

### Related Functional Requirements

- FR-TRN-001 - Register Trainer Profile
- FR-TRN-002 - Assign Trainer to Facilities and Sites
- FR-TRN-003 - Maintain Trainer Availability
- FR-TRN-004 - Validate Trainer Schedule Conflicts
- FR-AUD-001 - Record Audit Events

### Notes

Generate Trainer Performance Summary shall remain aligned with the approved BA source documents and shall not introduce behavior that bypasses tenant isolation, lifecycle governance, financial controls, or auditability.

---

**End of FR-11 - Trainer Management**
