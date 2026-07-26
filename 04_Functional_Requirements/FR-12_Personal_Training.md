# FR-12 Personal Training

**Document ID:** FR-12  
**Document Name:** Personal Training Functional Requirements  
**Company:** OreeOn Technologies Pvt. Ltd.  
**Product:** Digitize  
**Document Type:** Functional Requirements  
**Version:** 1.0  
**Status:** Draft  
**Owner:** Product Management  
**Prepared By:** Product Management, Business Analysis, and Solution Architecture  
**Last Updated:** July 2026

---

## FR-PTR-001 - Create Personal Training Package

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-PTR-001 |
| Requirement Name | Create Personal Training Package |
| Functional Module | Personal Training |
| Business Domain | Personal Training |
| Business Capability | Training Package Management |
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
| Business Requirement | BA-08 BR-017 Personal Training Booking |
| Business Rule | BA-02 BR-TRN-003, BR-TRN-005, BR-BIL-001, BR-SEC-004 |
| Business Process | BA-03 BP-PTR-001 Create Personal Training Package |
| Business Process Flow | BA-04 Section 23 Personal Training Flow |
| Persona | BA-05 Trainer, Reception Staff, Customer, Facility Manager |
| User Journey | BA-06 Section 18 Personal Training Journey |
| Stakeholder | BA-07 Trainer, Reception Staff, Customer, Facility Manager |
| Non-Functional Requirement | BA-09 Section 2.6 Usability, Section 2.10 Auditability, Section 11 Reporting Requirements |
| Assumption / Constraint / Risk | BA-10 BA-ASS-011, BA-RSK-006, BA-RSK-012 |

### Purpose

To enable Training Package Management within Personal Training so Digitize can execute Create Personal Training Package consistently across Organizations, Facilities, Sites, users, and related operational or commercial services.

### Functional Requirement

The system shall support Create Personal Training Package as an atomic Personal Training capability, including scoped data capture, business-rule validation, permission enforcement, lifecycle handling, related service synchronization, notification generation, reporting contribution, and immutable audit recording.

### Business Justification

Create Personal Training Package is required to preserve operational control, revenue accuracy, service continuity, customer trust, and enterprise traceability for Personal Training processes. Without this capability, downstream modules would rely on incomplete, manual, or inconsistent records.

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
- Actor has permission for Create Personal Training Package.
- Required Personal Training configuration and policies are available.
- Related records required by BA-03 BP-PTR-001 Create Personal Training Package are available and within authorized scope.

### Trigger

The capability is triggered when Organization Administrator or the System initiates Create Personal Training Package from Training Package, a related workflow, a scheduled job, or an approved integration event.

### In Scope

- Capture or retrieve required Personal Training context.
- Validate Organization, Facility, Site, Customer, user, and policy scope where applicable.
- Execute Create Personal Training Package according to approved business rules.
- Persist the resulting Personal Training Package state or transaction.
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
- Personal Training Package reference
- Customer reference, where applicable
- Effective date and time, where applicable
- Status or action reason, where applicable
- Payment, billing, trainer, session, or subscription reference where applicable
- Actor remarks, where applicable

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Personal Training Package ID | Primary business record reference | Identifier | Yes | System / User | Must exist or be generated within scope | Core reference for Create Personal Training Package |
| Organization ID | Tenant Organization context | Identifier | Yes | Session / System | Must be Active and authorized | Enforces tenant isolation |
| Facility ID | Facility context | Identifier | Conditional | User / System | Must be Active where applicable | Required for facility-level operations |
| Site ID | Site context | Identifier | Conditional | User / System | Must belong to Facility where applicable | Required for site-level operations |
| Status | Lifecycle or processing state | Enum | Yes | System | Must follow allowed state transitions | Drives UI and downstream access |
| Effective Date | Date when action applies | DateTime | Conditional | User / System | Must satisfy policy | Supports scheduled or immediate actions |
| Reason / Remarks | Business explanation | Text | Conditional | User | Required for governed changes | Stored for audit |

### Main Flow

1. Actor opens Training Package or the related workflow.
2. The system validates authentication, authorization, tenant scope, and current operating context.
3. The system loads the required Personal Training records, related configuration, and policy controls.
4. Actor enters or confirms the information required to create personal training package.
5. The system validates mandatory data, lifecycle status, ownership, eligibility, financial, capacity, schedule, and security rules where applicable.
6. The system executes Create Personal Training Package and persists the resulting Personal Training Package state or transaction.
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

- Personal Training Package record created, updated, validated, or reported according to the action.
- Lifecycle or processing status updated.
- Related history entry created.
- Business events emitted.
- Notifications generated where configured.
- Audit events recorded.
- Reports or dashboards updated where applicable.

### UI Behaviour

Training Package shall display scoped context, mandatory fields, lifecycle status, policy warnings, validation results, available actions, confirmation prompts, read-only states, pagination or filters where applicable, and responsive behavior for front-desk and administrative usage.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-PTR-001-001 | Actor must have permission to execute Create Personal Training Package. | Deny request and audit. | Critical |
| VAL-PTR-001-002 | Record must belong to the authorized Organization scope. | Deny request. | Critical |
| VAL-PTR-001-003 | Mandatory inputs must be complete and valid. | Block submission. | Critical |
| VAL-PTR-001-004 | Lifecycle and policy rules from BA-02 must be satisfied. | Reject or route for approval. | High |
| VAL-PTR-001-005 | Historical and audit records must be preserved. | Roll back or mark for recovery. | Critical |

### Business Rules

- BA-02 BR-TRN-003
- BA-02 BR-TRN-005
- BA-02 BR-BIL-001
- BA-02 BR-SEC-004

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| ptr.create.personal.training.package.view | Organization Administrator | Read | View Create Personal Training Package context |
| ptr.create.personal.training.package.execute | Organization Administrator | Execute | Execute Create Personal Training Package |
| ptr.create.personal.training.package.approve | Organization Administrator | Approve | Approve governed exceptions where configured |
| ptr.create.personal.training.package.audit.view | Organization Administrator / Support Executive | Read | View audit trace |

### Security Considerations

The capability shall enforce authentication, role-based authorization, tenant isolation, Organization scope, Facility and Site access boundaries, sensitive data masking, secure references, and immutable audit logging.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Create Personal Training Package Completed | Primary actor and configured stakeholders | In-App / Email | Action completes | Include reference, status, and effective date where applicable |
| Create Personal Training Package Requires Approval | Approver | In-App | Approval rule applies | Include safe summary and requested action |
| Create Personal Training Package Failed | Primary actor | In-App | Validation or processing fails | Include safe failure reason and next action |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| CreatePersonalTrainingPackageRequested | Personal Training | Approval Workflow, Audit Service |
| CreatePersonalTrainingPackageCompleted | Personal Training | Notification Service, Reporting Service, Audit Service |
| CreatePersonalTrainingPackageRejected | Personal Training | Notification Service, Audit Service |

### Audit Events

| Audit Event | Description | Actor | Target Entity | Key Data |
|---|---|---|---|---|
| CREATE_PERSONAL_TRAINING_PACKAGE_REQUESTED | Create Personal Training Package requested | Organization Administrator | Personal Training Package | Scope, reference, and reason |
| CREATE_PERSONAL_TRAINING_PACKAGE_COMPLETED | Create Personal Training Package completed | Organization Administrator / System | Personal Training Package | Previous and new state |
| CREATE_PERSONAL_TRAINING_PACKAGE_REJECTED | Create Personal Training Package rejected | System | Personal Training Package | Rejection reason |

### Reports Generated

- Personal Training Operational Report
- Personal Training History Report
- Personal Training Exception Report
- Executive Dashboard

### Related Screens

- Training Package
- Personal Training Dashboard
- Personal Training History
- Audit Log Viewer

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/personal-training/packages | POST | Authorized token | Execute Create Personal Training Package | 200 OK or 201 Created with result |
| /api/v1/personal-training/packages/history | GET | Authorized token | Retrieve Create Personal Training Package history | 200 OK with history |
| /api/v1/audit-logs | GET | Authorized token | Retrieve related audit events | 200 OK with scoped audit records |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Personal Training Package | Create / Update / Read | Support Create Personal Training Package | Governed by Organization scope |
| Personal Training Session | Read / Insert | Support Create Personal Training Package | Governed by Organization scope |
| Trainer Assignment | Read / Insert | Support Create Personal Training Package | Governed by Organization scope |
| Training Notes | Read / Insert | Support Create Personal Training Package | Governed by Organization scope |
| Customer Progress | Read / Insert | Support Create Personal Training Package | Governed by Organization scope |
| Audit Log | Insert | Record auditable activity | Immutable |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Draft | Create Personal Training Package initiated | Configured | Organization Administrator | Required data captured |
| Configured | Validation succeeds | Active | System | BA-02 rules satisfied |
| Active | Processing completes | Inactive | System | Related updates succeed |
| Active | Approval or policy failure | Archived | System / Approver | Request rejected |
| Inactive | View history | Inactive | Authorized user | Read-only historical access |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| PTR-001-001 | Create Personal Training Package cannot be completed because required information is missing. | Missing mandatory data | Complete required fields |
| PTR-001-002 | You do not have permission to perform this action. | Authorization failure | Request access |
| PTR-001-003 | The selected record is not eligible for this action. | Policy or lifecycle violation | Review record status |
| PTR-001-004 | Create Personal Training Package could not be completed due to a system or integration error. | Processing failure | Retry or contact support |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Execute Create Personal Training Package | Given the actor has required permission and valid scope | When the actor submits valid information | Then the system shall complete Create Personal Training Package successfully |
| Enforce validation | Given mandatory data or policy conditions are invalid | When the action is submitted | Then the system shall reject the request with a clear message |
| Preserve audit | Given the action completes or fails | When processing ends | Then audit events shall record actor, timestamp, scope, and outcome |
| Protect scope | Given the selected record is outside authorized scope | When the action is requested | Then the system shall deny access |

### Dependencies

- Trainer Management
- Customer Management
- Attendance Management
- Billing Management
- Payment Management
- Notification Management
- Reporting Service

### Operational Considerations

Create Personal Training Package should be designed for high-volume operational use, retry-safe processing, clear exception handling, and support-team diagnostics without exposing sensitive data.

### Non-Functional Considerations

This requirement shall satisfy Digitize non-functional expectations for availability, reliability, performance, scalability, security, configurability, maintainability, and auditability.

### Assumptions

- Required master data and configuration are maintained by authorized users.
- Related services expose stable APIs for validation and synchronization.
- Organization policies define approval, retention, notification, and exception behavior.

### Success Criteria

Create Personal Training Package is completed accurately, securely, and audibly, with downstream records synchronized and no loss of historical traceability.

### Related Functional Requirements

- FR-PTR-002 - Configure Training Package
- FR-PTR-003 - Assign Trainer
- FR-PTR-004 - Book Personal Training Session
- FR-PTR-005 - Reschedule Training Session
- FR-AUD-001 - Record Audit Events

### Notes

Create Personal Training Package shall remain aligned with the approved BA source documents and shall not introduce behavior that bypasses tenant isolation, lifecycle governance, financial controls, or auditability.

---

## FR-PTR-002 - Configure Training Package

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-PTR-002 |
| Requirement Name | Configure Training Package |
| Functional Module | Personal Training |
| Business Domain | Personal Training |
| Business Capability | Training Configuration |
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
| Business Requirement | BA-08 BR-017 Personal Training Booking |
| Business Rule | BA-02 BR-TRN-003, BR-BIL-004, BR-BIL-008, BR-SEC-004 |
| Business Process | BA-03 BP-PTR-002 Configure Training Package |
| Business Process Flow | BA-04 Section 23 Personal Training Flow |
| Persona | BA-05 Trainer, Reception Staff, Customer, Facility Manager |
| User Journey | BA-06 Section 18 Personal Training Journey |
| Stakeholder | BA-07 Trainer, Reception Staff, Customer, Facility Manager |
| Non-Functional Requirement | BA-09 Section 2.6 Usability, Section 2.10 Auditability, Section 11 Reporting Requirements |
| Assumption / Constraint / Risk | BA-10 BA-ASS-011, BA-RSK-006, BA-RSK-012 |

### Purpose

To enable Training Configuration within Personal Training so Digitize can execute Configure Training Package consistently across Organizations, Facilities, Sites, users, and related operational or commercial services.

### Functional Requirement

The system shall support Configure Training Package as an atomic Personal Training capability, including scoped data capture, business-rule validation, permission enforcement, lifecycle handling, related service synchronization, notification generation, reporting contribution, and immutable audit recording.

### Business Justification

Configure Training Package is required to preserve operational control, revenue accuracy, service continuity, customer trust, and enterprise traceability for Personal Training processes. Without this capability, downstream modules would rely on incomplete, manual, or inconsistent records.

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
- Actor has permission for Configure Training Package.
- Required Personal Training configuration and policies are available.
- Related records required by BA-03 BP-PTR-002 Configure Training Package are available and within authorized scope.

### Trigger

The capability is triggered when Organization Administrator or the System initiates Configure Training Package from Training Package Configuration, a related workflow, a scheduled job, or an approved integration event.

### In Scope

- Capture or retrieve required Personal Training context.
- Validate Organization, Facility, Site, Customer, user, and policy scope where applicable.
- Execute Configure Training Package according to approved business rules.
- Persist the resulting Personal Training Package state or transaction.
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
- Personal Training Package reference
- Customer reference, where applicable
- Effective date and time, where applicable
- Status or action reason, where applicable
- Payment, billing, trainer, session, or subscription reference where applicable
- Actor remarks, where applicable

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Personal Training Package ID | Primary business record reference | Identifier | Yes | System / User | Must exist or be generated within scope | Core reference for Configure Training Package |
| Organization ID | Tenant Organization context | Identifier | Yes | Session / System | Must be Active and authorized | Enforces tenant isolation |
| Facility ID | Facility context | Identifier | Conditional | User / System | Must be Active where applicable | Required for facility-level operations |
| Site ID | Site context | Identifier | Conditional | User / System | Must belong to Facility where applicable | Required for site-level operations |
| Status | Lifecycle or processing state | Enum | Yes | System | Must follow allowed state transitions | Drives UI and downstream access |
| Effective Date | Date when action applies | DateTime | Conditional | User / System | Must satisfy policy | Supports scheduled or immediate actions |
| Reason / Remarks | Business explanation | Text | Conditional | User | Required for governed changes | Stored for audit |

### Main Flow

1. Actor opens Training Package Configuration or the related workflow.
2. The system validates authentication, authorization, tenant scope, and current operating context.
3. The system loads the required Personal Training records, related configuration, and policy controls.
4. Actor enters or confirms the information required to configure training package.
5. The system validates mandatory data, lifecycle status, ownership, eligibility, financial, capacity, schedule, and security rules where applicable.
6. The system executes Configure Training Package and persists the resulting Personal Training Package state or transaction.
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

- Personal Training Package record created, updated, validated, or reported according to the action.
- Lifecycle or processing status updated.
- Related history entry created.
- Business events emitted.
- Notifications generated where configured.
- Audit events recorded.
- Reports or dashboards updated where applicable.

### UI Behaviour

Training Package Configuration shall display scoped context, mandatory fields, lifecycle status, policy warnings, validation results, available actions, confirmation prompts, read-only states, pagination or filters where applicable, and responsive behavior for front-desk and administrative usage.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-PTR-002-001 | Actor must have permission to execute Configure Training Package. | Deny request and audit. | Critical |
| VAL-PTR-002-002 | Record must belong to the authorized Organization scope. | Deny request. | Critical |
| VAL-PTR-002-003 | Mandatory inputs must be complete and valid. | Block submission. | Critical |
| VAL-PTR-002-004 | Lifecycle and policy rules from BA-02 must be satisfied. | Reject or route for approval. | High |
| VAL-PTR-002-005 | Historical and audit records must be preserved. | Roll back or mark for recovery. | Critical |

### Business Rules

- BA-02 BR-TRN-003
- BA-02 BR-BIL-004
- BA-02 BR-BIL-008
- BA-02 BR-SEC-004

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| ptr.configure.training.package.view | Organization Administrator | Read | View Configure Training Package context |
| ptr.configure.training.package.execute | Organization Administrator | Execute | Execute Configure Training Package |
| ptr.configure.training.package.approve | Organization Administrator | Approve | Approve governed exceptions where configured |
| ptr.configure.training.package.audit.view | Organization Administrator / Support Executive | Read | View audit trace |

### Security Considerations

The capability shall enforce authentication, role-based authorization, tenant isolation, Organization scope, Facility and Site access boundaries, sensitive data masking, secure references, and immutable audit logging.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Configure Training Package Completed | Primary actor and configured stakeholders | In-App / Email | Action completes | Include reference, status, and effective date where applicable |
| Configure Training Package Requires Approval | Approver | In-App | Approval rule applies | Include safe summary and requested action |
| Configure Training Package Failed | Primary actor | In-App | Validation or processing fails | Include safe failure reason and next action |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| ConfigureTrainingPackageRequested | Personal Training | Approval Workflow, Audit Service |
| ConfigureTrainingPackageCompleted | Personal Training | Notification Service, Reporting Service, Audit Service |
| ConfigureTrainingPackageRejected | Personal Training | Notification Service, Audit Service |

### Audit Events

| Audit Event | Description | Actor | Target Entity | Key Data |
|---|---|---|---|---|
| CONFIGURE_TRAINING_PACKAGE_REQUESTED | Configure Training Package requested | Organization Administrator | Personal Training Package | Scope, reference, and reason |
| CONFIGURE_TRAINING_PACKAGE_COMPLETED | Configure Training Package completed | Organization Administrator / System | Personal Training Package | Previous and new state |
| CONFIGURE_TRAINING_PACKAGE_REJECTED | Configure Training Package rejected | System | Personal Training Package | Rejection reason |

### Reports Generated

- Personal Training Operational Report
- Personal Training History Report
- Personal Training Exception Report
- Executive Dashboard

### Related Screens

- Training Package Configuration
- Personal Training Dashboard
- Personal Training History
- Audit Log Viewer

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/personal-training/packages/{packageId} | PATCH | Authorized token | Execute Configure Training Package | 200 OK or 201 Created with result |
| /api/v1/personal-training/packages/{packageId}/history | GET | Authorized token | Retrieve Configure Training Package history | 200 OK with history |
| /api/v1/audit-logs | GET | Authorized token | Retrieve related audit events | 200 OK with scoped audit records |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Personal Training Package | Create / Update / Read | Support Configure Training Package | Governed by Organization scope |
| Personal Training Session | Read / Insert | Support Configure Training Package | Governed by Organization scope |
| Trainer Assignment | Read / Insert | Support Configure Training Package | Governed by Organization scope |
| Training Notes | Read / Insert | Support Configure Training Package | Governed by Organization scope |
| Customer Progress | Read / Insert | Support Configure Training Package | Governed by Organization scope |
| Audit Log | Insert | Record auditable activity | Immutable |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Draft | Configure Training Package initiated | Configured | Organization Administrator | Required data captured |
| Configured | Validation succeeds | Active | System | BA-02 rules satisfied |
| Active | Processing completes | Inactive | System | Related updates succeed |
| Active | Approval or policy failure | Archived | System / Approver | Request rejected |
| Inactive | View history | Inactive | Authorized user | Read-only historical access |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| PTR-002-001 | Configure Training Package cannot be completed because required information is missing. | Missing mandatory data | Complete required fields |
| PTR-002-002 | You do not have permission to perform this action. | Authorization failure | Request access |
| PTR-002-003 | The selected record is not eligible for this action. | Policy or lifecycle violation | Review record status |
| PTR-002-004 | Configure Training Package could not be completed due to a system or integration error. | Processing failure | Retry or contact support |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Execute Configure Training Package | Given the actor has required permission and valid scope | When the actor submits valid information | Then the system shall complete Configure Training Package successfully |
| Enforce validation | Given mandatory data or policy conditions are invalid | When the action is submitted | Then the system shall reject the request with a clear message |
| Preserve audit | Given the action completes or fails | When processing ends | Then audit events shall record actor, timestamp, scope, and outcome |
| Protect scope | Given the selected record is outside authorized scope | When the action is requested | Then the system shall deny access |

### Dependencies

- Trainer Management
- Customer Management
- Attendance Management
- Billing Management
- Payment Management
- Notification Management
- Reporting Service

### Operational Considerations

Configure Training Package should be designed for high-volume operational use, retry-safe processing, clear exception handling, and support-team diagnostics without exposing sensitive data.

### Non-Functional Considerations

This requirement shall satisfy Digitize non-functional expectations for availability, reliability, performance, scalability, security, configurability, maintainability, and auditability.

### Assumptions

- Required master data and configuration are maintained by authorized users.
- Related services expose stable APIs for validation and synchronization.
- Organization policies define approval, retention, notification, and exception behavior.

### Success Criteria

Configure Training Package is completed accurately, securely, and audibly, with downstream records synchronized and no loss of historical traceability.

### Related Functional Requirements

- FR-PTR-001 - Create Personal Training Package
- FR-PTR-003 - Assign Trainer
- FR-PTR-004 - Book Personal Training Session
- FR-PTR-005 - Reschedule Training Session
- FR-AUD-001 - Record Audit Events

### Notes

Configure Training Package shall remain aligned with the approved BA source documents and shall not introduce behavior that bypasses tenant isolation, lifecycle governance, financial controls, or auditability.

---

## FR-PTR-003 - Assign Trainer

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-PTR-003 |
| Requirement Name | Assign Trainer |
| Functional Module | Personal Training |
| Business Domain | Personal Training |
| Business Capability | Trainer Assignment |
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
| Business Process Flow | BA-04 Section 23 Personal Training Flow |
| Persona | BA-05 Trainer, Reception Staff, Customer, Facility Manager |
| User Journey | BA-06 Section 18 Personal Training Journey |
| Stakeholder | BA-07 Trainer, Reception Staff, Customer, Facility Manager |
| Non-Functional Requirement | BA-09 Section 2.6 Usability, Section 2.10 Auditability, Section 11 Reporting Requirements |
| Assumption / Constraint / Risk | BA-10 BA-ASS-011, BA-RSK-006, BA-RSK-012 |

### Purpose

To enable Trainer Assignment within Personal Training so Digitize can execute Assign Trainer consistently across Organizations, Facilities, Sites, users, and related operational or commercial services.

### Functional Requirement

The system shall support Assign Trainer as an atomic Personal Training capability, including scoped data capture, business-rule validation, permission enforcement, lifecycle handling, related service synchronization, notification generation, reporting contribution, and immutable audit recording.

### Business Justification

Assign Trainer is required to preserve operational control, revenue accuracy, service continuity, customer trust, and enterprise traceability for Personal Training processes. Without this capability, downstream modules would rely on incomplete, manual, or inconsistent records.

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
- Actor has permission for Assign Trainer.
- Required Personal Training configuration and policies are available.
- Related records required by BA-03 BP-PTR-003 Assign Trainer are available and within authorized scope.

### Trigger

The capability is triggered when Reception Staff or the System initiates Assign Trainer from Trainer Assignment, a related workflow, a scheduled job, or an approved integration event.

### In Scope

- Capture or retrieve required Personal Training context.
- Validate Organization, Facility, Site, Customer, user, and policy scope where applicable.
- Execute Assign Trainer according to approved business rules.
- Persist the resulting Personal Training Package state or transaction.
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
- Personal Training Package reference
- Customer reference, where applicable
- Effective date and time, where applicable
- Status or action reason, where applicable
- Payment, billing, trainer, session, or subscription reference where applicable
- Actor remarks, where applicable

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Personal Training Package ID | Primary business record reference | Identifier | Yes | System / User | Must exist or be generated within scope | Core reference for Assign Trainer |
| Organization ID | Tenant Organization context | Identifier | Yes | Session / System | Must be Active and authorized | Enforces tenant isolation |
| Facility ID | Facility context | Identifier | Conditional | User / System | Must be Active where applicable | Required for facility-level operations |
| Site ID | Site context | Identifier | Conditional | User / System | Must belong to Facility where applicable | Required for site-level operations |
| Status | Lifecycle or processing state | Enum | Yes | System | Must follow allowed state transitions | Drives UI and downstream access |
| Effective Date | Date when action applies | DateTime | Conditional | User / System | Must satisfy policy | Supports scheduled or immediate actions |
| Reason / Remarks | Business explanation | Text | Conditional | User | Required for governed changes | Stored for audit |

### Main Flow

1. Actor opens Trainer Assignment or the related workflow.
2. The system validates authentication, authorization, tenant scope, and current operating context.
3. The system loads the required Personal Training records, related configuration, and policy controls.
4. Actor enters or confirms the information required to assign trainer.
5. The system validates mandatory data, lifecycle status, ownership, eligibility, financial, capacity, schedule, and security rules where applicable.
6. The system executes Assign Trainer and persists the resulting Personal Training Package state or transaction.
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

- Personal Training Package record created, updated, validated, or reported according to the action.
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
| VAL-PTR-003-001 | Actor must have permission to execute Assign Trainer. | Deny request and audit. | Critical |
| VAL-PTR-003-002 | Record must belong to the authorized Organization scope. | Deny request. | Critical |
| VAL-PTR-003-003 | Mandatory inputs must be complete and valid. | Block submission. | Critical |
| VAL-PTR-003-004 | Lifecycle and policy rules from BA-02 must be satisfied. | Reject or route for approval. | High |
| VAL-PTR-003-005 | Historical and audit records must be preserved. | Roll back or mark for recovery. | Critical |

### Business Rules

- BA-02 BR-TRN-003
- BA-02 BR-TRN-005
- BA-02 BR-TRN-008
- BA-02 BR-SEC-004

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| ptr.assign.trainer.view | Reception Staff | Read | View Assign Trainer context |
| ptr.assign.trainer.execute | Reception Staff | Execute | Execute Assign Trainer |
| ptr.assign.trainer.approve | Organization Administrator | Approve | Approve governed exceptions where configured |
| ptr.assign.trainer.audit.view | Organization Administrator / Support Executive | Read | View audit trace |

### Security Considerations

The capability shall enforce authentication, role-based authorization, tenant isolation, Organization scope, Facility and Site access boundaries, sensitive data masking, secure references, and immutable audit logging.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Assign Trainer Completed | Primary actor and configured stakeholders | In-App / Email | Action completes | Include reference, status, and effective date where applicable |
| Assign Trainer Requires Approval | Approver | In-App | Approval rule applies | Include safe summary and requested action |
| Assign Trainer Failed | Primary actor | In-App | Validation or processing fails | Include safe failure reason and next action |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| AssignTrainerRequested | Personal Training | Approval Workflow, Audit Service |
| AssignTrainerCompleted | Personal Training | Notification Service, Reporting Service, Audit Service |
| AssignTrainerRejected | Personal Training | Notification Service, Audit Service |

### Audit Events

| Audit Event | Description | Actor | Target Entity | Key Data |
|---|---|---|---|---|
| ASSIGN_TRAINER_REQUESTED | Assign Trainer requested | Reception Staff | Personal Training Package | Scope, reference, and reason |
| ASSIGN_TRAINER_COMPLETED | Assign Trainer completed | Reception Staff / System | Personal Training Package | Previous and new state |
| ASSIGN_TRAINER_REJECTED | Assign Trainer rejected | System | Personal Training Package | Rejection reason |

### Reports Generated

- Personal Training Operational Report
- Personal Training History Report
- Personal Training Exception Report
- Executive Dashboard

### Related Screens

- Trainer Assignment
- Personal Training Dashboard
- Personal Training History
- Audit Log Viewer

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/personal-training/assignments | POST | Authorized token | Execute Assign Trainer | 200 OK or 201 Created with result |
| /api/v1/personal-training/assignments/history | GET | Authorized token | Retrieve Assign Trainer history | 200 OK with history |
| /api/v1/audit-logs | GET | Authorized token | Retrieve related audit events | 200 OK with scoped audit records |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Personal Training Package | Create / Update / Read | Support Assign Trainer | Governed by Organization scope |
| Personal Training Session | Read / Insert | Support Assign Trainer | Governed by Organization scope |
| Trainer Assignment | Read / Insert | Support Assign Trainer | Governed by Organization scope |
| Training Notes | Read / Insert | Support Assign Trainer | Governed by Organization scope |
| Customer Progress | Read / Insert | Support Assign Trainer | Governed by Organization scope |
| Audit Log | Insert | Record auditable activity | Immutable |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Draft | Assign Trainer initiated | Validated | Reception Staff | Required data captured |
| Validated | Validation succeeds | Pending Approval | System | BA-02 rules satisfied |
| Pending Approval | Processing completes | Completed | System | Related updates succeed |
| Pending Approval | Approval or policy failure | Rejected | System / Approver | Request rejected |
| Completed | View history | Completed | Authorized user | Read-only historical access |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| PTR-003-001 | Assign Trainer cannot be completed because required information is missing. | Missing mandatory data | Complete required fields |
| PTR-003-002 | You do not have permission to perform this action. | Authorization failure | Request access |
| PTR-003-003 | The selected record is not eligible for this action. | Policy or lifecycle violation | Review record status |
| PTR-003-004 | Assign Trainer could not be completed due to a system or integration error. | Processing failure | Retry or contact support |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Execute Assign Trainer | Given the actor has required permission and valid scope | When the actor submits valid information | Then the system shall complete Assign Trainer successfully |
| Enforce validation | Given mandatory data or policy conditions are invalid | When the action is submitted | Then the system shall reject the request with a clear message |
| Preserve audit | Given the action completes or fails | When processing ends | Then audit events shall record actor, timestamp, scope, and outcome |
| Protect scope | Given the selected record is outside authorized scope | When the action is requested | Then the system shall deny access |

### Dependencies

- Trainer Management
- Customer Management
- Attendance Management
- Billing Management
- Payment Management
- Notification Management
- Reporting Service

### Operational Considerations

Assign Trainer should be designed for high-volume operational use, retry-safe processing, clear exception handling, and support-team diagnostics without exposing sensitive data.

### Non-Functional Considerations

This requirement shall satisfy Digitize non-functional expectations for availability, reliability, performance, scalability, security, configurability, maintainability, and auditability.

### Assumptions

- Required master data and configuration are maintained by authorized users.
- Related services expose stable APIs for validation and synchronization.
- Organization policies define approval, retention, notification, and exception behavior.

### Success Criteria

Assign Trainer is completed accurately, securely, and audibly, with downstream records synchronized and no loss of historical traceability.

### Related Functional Requirements

- FR-PTR-001 - Create Personal Training Package
- FR-PTR-002 - Configure Training Package
- FR-PTR-004 - Book Personal Training Session
- FR-PTR-005 - Reschedule Training Session
- FR-AUD-001 - Record Audit Events

### Notes

Assign Trainer shall remain aligned with the approved BA source documents and shall not introduce behavior that bypasses tenant isolation, lifecycle governance, financial controls, or auditability.

---

## FR-PTR-004 - Book Personal Training Session

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-PTR-004 |
| Requirement Name | Book Personal Training Session |
| Functional Module | Personal Training |
| Business Domain | Personal Training |
| Business Capability | Session Scheduling |
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
| Business Requirement | BA-08 BR-017 Personal Training Booking |
| Business Rule | BA-02 BR-TRN-003, BR-TRN-005, BR-TRN-008, BR-PAY-001, BR-SEC-004 |
| Business Process | BA-03 BP-PTR-004 Book Personal Training Session |
| Business Process Flow | BA-04 Section 23 Personal Training Flow |
| Persona | BA-05 Trainer, Reception Staff, Customer, Facility Manager |
| User Journey | BA-06 Section 18 Personal Training Journey |
| Stakeholder | BA-07 Trainer, Reception Staff, Customer, Facility Manager |
| Non-Functional Requirement | BA-09 Section 2.6 Usability, Section 2.10 Auditability, Section 11 Reporting Requirements |
| Assumption / Constraint / Risk | BA-10 BA-ASS-011, BA-RSK-006, BA-RSK-012 |

### Purpose

To enable Session Scheduling within Personal Training so Digitize can execute Book Personal Training Session consistently across Organizations, Facilities, Sites, users, and related operational or commercial services.

### Functional Requirement

The system shall support Book Personal Training Session as an atomic Personal Training capability, including scoped data capture, business-rule validation, permission enforcement, lifecycle handling, related service synchronization, notification generation, reporting contribution, and immutable audit recording.

### Business Justification

Book Personal Training Session is required to preserve operational control, revenue accuracy, service continuity, customer trust, and enterprise traceability for Personal Training processes. Without this capability, downstream modules would rely on incomplete, manual, or inconsistent records.

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
- Actor has permission for Book Personal Training Session.
- Required Personal Training configuration and policies are available.
- Related records required by BA-03 BP-PTR-004 Book Personal Training Session are available and within authorized scope.

### Trigger

The capability is triggered when Reception Staff or the System initiates Book Personal Training Session from Session Booking, a related workflow, a scheduled job, or an approved integration event.

### In Scope

- Capture or retrieve required Personal Training context.
- Validate Organization, Facility, Site, Customer, user, and policy scope where applicable.
- Execute Book Personal Training Session according to approved business rules.
- Persist the resulting Personal Training Package state or transaction.
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
- Personal Training Package reference
- Customer reference, where applicable
- Effective date and time, where applicable
- Status or action reason, where applicable
- Payment, billing, trainer, session, or subscription reference where applicable
- Actor remarks, where applicable

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Personal Training Package ID | Primary business record reference | Identifier | Yes | System / User | Must exist or be generated within scope | Core reference for Book Personal Training Session |
| Organization ID | Tenant Organization context | Identifier | Yes | Session / System | Must be Active and authorized | Enforces tenant isolation |
| Facility ID | Facility context | Identifier | Conditional | User / System | Must be Active where applicable | Required for facility-level operations |
| Site ID | Site context | Identifier | Conditional | User / System | Must belong to Facility where applicable | Required for site-level operations |
| Status | Lifecycle or processing state | Enum | Yes | System | Must follow allowed state transitions | Drives UI and downstream access |
| Effective Date | Date when action applies | DateTime | Conditional | User / System | Must satisfy policy | Supports scheduled or immediate actions |
| Reason / Remarks | Business explanation | Text | Conditional | User | Required for governed changes | Stored for audit |

### Main Flow

1. Actor opens Session Booking or the related workflow.
2. The system validates authentication, authorization, tenant scope, and current operating context.
3. The system loads the required Personal Training records, related configuration, and policy controls.
4. Actor enters or confirms the information required to book personal training session.
5. The system validates mandatory data, lifecycle status, ownership, eligibility, financial, capacity, schedule, and security rules where applicable.
6. The system executes Book Personal Training Session and persists the resulting Personal Training Package state or transaction.
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

- Personal Training Package record created, updated, validated, or reported according to the action.
- Lifecycle or processing status updated.
- Related history entry created.
- Business events emitted.
- Notifications generated where configured.
- Audit events recorded.
- Reports or dashboards updated where applicable.

### UI Behaviour

Session Booking shall display scoped context, mandatory fields, lifecycle status, policy warnings, validation results, available actions, confirmation prompts, read-only states, pagination or filters where applicable, and responsive behavior for front-desk and administrative usage.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-PTR-004-001 | Actor must have permission to execute Book Personal Training Session. | Deny request and audit. | Critical |
| VAL-PTR-004-002 | Record must belong to the authorized Organization scope. | Deny request. | Critical |
| VAL-PTR-004-003 | Mandatory inputs must be complete and valid. | Block submission. | Critical |
| VAL-PTR-004-004 | Lifecycle and policy rules from BA-02 must be satisfied. | Reject or route for approval. | High |
| VAL-PTR-004-005 | Historical and audit records must be preserved. | Roll back or mark for recovery. | Critical |

### Business Rules

- BA-02 BR-TRN-003
- BA-02 BR-TRN-005
- BA-02 BR-TRN-008
- BA-02 BR-PAY-001
- BA-02 BR-SEC-004

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| ptr.book.personal.training.session.view | Reception Staff | Read | View Book Personal Training Session context |
| ptr.book.personal.training.session.execute | Reception Staff | Execute | Execute Book Personal Training Session |
| ptr.book.personal.training.session.approve | Organization Administrator | Approve | Approve governed exceptions where configured |
| ptr.book.personal.training.session.audit.view | Organization Administrator / Support Executive | Read | View audit trace |

### Security Considerations

The capability shall enforce authentication, role-based authorization, tenant isolation, Organization scope, Facility and Site access boundaries, sensitive data masking, secure references, and immutable audit logging.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Book Personal Training Session Completed | Primary actor and configured stakeholders | In-App / Email | Action completes | Include reference, status, and effective date where applicable |
| Book Personal Training Session Requires Approval | Approver | In-App | Approval rule applies | Include safe summary and requested action |
| Book Personal Training Session Failed | Primary actor | In-App | Validation or processing fails | Include safe failure reason and next action |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| BookPersonalTrainingSessionRequested | Personal Training | Approval Workflow, Audit Service |
| BookPersonalTrainingSessionCompleted | Personal Training | Notification Service, Reporting Service, Audit Service |
| BookPersonalTrainingSessionRejected | Personal Training | Notification Service, Audit Service |

### Audit Events

| Audit Event | Description | Actor | Target Entity | Key Data |
|---|---|---|---|---|
| BOOK_PERSONAL_TRAINING_SESSION_REQUESTED | Book Personal Training Session requested | Reception Staff | Personal Training Package | Scope, reference, and reason |
| BOOK_PERSONAL_TRAINING_SESSION_COMPLETED | Book Personal Training Session completed | Reception Staff / System | Personal Training Package | Previous and new state |
| BOOK_PERSONAL_TRAINING_SESSION_REJECTED | Book Personal Training Session rejected | System | Personal Training Package | Rejection reason |

### Reports Generated

- Personal Training Operational Report
- Personal Training History Report
- Personal Training Exception Report
- Executive Dashboard

### Related Screens

- Session Booking
- Personal Training Dashboard
- Personal Training History
- Audit Log Viewer

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/training-sessions | POST | Authorized token | Execute Book Personal Training Session | 200 OK or 201 Created with result |
| /api/v1/training-sessions/history | GET | Authorized token | Retrieve Book Personal Training Session history | 200 OK with history |
| /api/v1/audit-logs | GET | Authorized token | Retrieve related audit events | 200 OK with scoped audit records |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Personal Training Package | Create / Update / Read | Support Book Personal Training Session | Governed by Organization scope |
| Personal Training Session | Read / Insert | Support Book Personal Training Session | Governed by Organization scope |
| Trainer Assignment | Read / Insert | Support Book Personal Training Session | Governed by Organization scope |
| Training Notes | Read / Insert | Support Book Personal Training Session | Governed by Organization scope |
| Customer Progress | Read / Insert | Support Book Personal Training Session | Governed by Organization scope |
| Audit Log | Insert | Record auditable activity | Immutable |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Draft | Book Personal Training Session initiated | Validated | Reception Staff | Required data captured |
| Validated | Validation succeeds | Pending Approval | System | BA-02 rules satisfied |
| Pending Approval | Processing completes | Completed | System | Related updates succeed |
| Pending Approval | Approval or policy failure | Rejected | System / Approver | Request rejected |
| Completed | View history | Completed | Authorized user | Read-only historical access |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| PTR-004-001 | Book Personal Training Session cannot be completed because required information is missing. | Missing mandatory data | Complete required fields |
| PTR-004-002 | You do not have permission to perform this action. | Authorization failure | Request access |
| PTR-004-003 | The selected record is not eligible for this action. | Policy or lifecycle violation | Review record status |
| PTR-004-004 | Book Personal Training Session could not be completed due to a system or integration error. | Processing failure | Retry or contact support |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Execute Book Personal Training Session | Given the actor has required permission and valid scope | When the actor submits valid information | Then the system shall complete Book Personal Training Session successfully |
| Enforce validation | Given mandatory data or policy conditions are invalid | When the action is submitted | Then the system shall reject the request with a clear message |
| Preserve audit | Given the action completes or fails | When processing ends | Then audit events shall record actor, timestamp, scope, and outcome |
| Protect scope | Given the selected record is outside authorized scope | When the action is requested | Then the system shall deny access |

### Dependencies

- Trainer Management
- Customer Management
- Attendance Management
- Billing Management
- Payment Management
- Notification Management
- Reporting Service

### Operational Considerations

Book Personal Training Session should be designed for high-volume operational use, retry-safe processing, clear exception handling, and support-team diagnostics without exposing sensitive data.

### Non-Functional Considerations

This requirement shall satisfy Digitize non-functional expectations for availability, reliability, performance, scalability, security, configurability, maintainability, and auditability.

### Assumptions

- Required master data and configuration are maintained by authorized users.
- Related services expose stable APIs for validation and synchronization.
- Organization policies define approval, retention, notification, and exception behavior.

### Success Criteria

Book Personal Training Session is completed accurately, securely, and audibly, with downstream records synchronized and no loss of historical traceability.

### Related Functional Requirements

- FR-PTR-001 - Create Personal Training Package
- FR-PTR-002 - Configure Training Package
- FR-PTR-003 - Assign Trainer
- FR-PTR-005 - Reschedule Training Session
- FR-AUD-001 - Record Audit Events

### Notes

Book Personal Training Session shall remain aligned with the approved BA source documents and shall not introduce behavior that bypasses tenant isolation, lifecycle governance, financial controls, or auditability.

---

## FR-PTR-005 - Reschedule Training Session

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-PTR-005 |
| Requirement Name | Reschedule Training Session |
| Functional Module | Personal Training |
| Business Domain | Personal Training |
| Business Capability | Session Scheduling |
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
| Business Requirement | BA-08 BR-017 Personal Training Booking |
| Business Rule | BA-02 BR-TRN-005, BR-TRN-008, BR-TRN-009, BR-AUD-003 |
| Business Process | BA-03 BP-PTR-005 Reschedule Training Session |
| Business Process Flow | BA-04 Section 23 Personal Training Flow |
| Persona | BA-05 Trainer, Reception Staff, Customer, Facility Manager |
| User Journey | BA-06 Section 18 Personal Training Journey |
| Stakeholder | BA-07 Trainer, Reception Staff, Customer, Facility Manager |
| Non-Functional Requirement | BA-09 Section 2.6 Usability, Section 2.10 Auditability, Section 11 Reporting Requirements |
| Assumption / Constraint / Risk | BA-10 BA-ASS-011, BA-RSK-006, BA-RSK-012 |

### Purpose

To enable Session Scheduling within Personal Training so Digitize can execute Reschedule Training Session consistently across Organizations, Facilities, Sites, users, and related operational or commercial services.

### Functional Requirement

The system shall support Reschedule Training Session as an atomic Personal Training capability, including scoped data capture, business-rule validation, permission enforcement, lifecycle handling, related service synchronization, notification generation, reporting contribution, and immutable audit recording.

### Business Justification

Reschedule Training Session is required to preserve operational control, revenue accuracy, service continuity, customer trust, and enterprise traceability for Personal Training processes. Without this capability, downstream modules would rely on incomplete, manual, or inconsistent records.

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
- Actor has permission for Reschedule Training Session.
- Required Personal Training configuration and policies are available.
- Related records required by BA-03 BP-PTR-005 Reschedule Training Session are available and within authorized scope.

### Trigger

The capability is triggered when Reception Staff or the System initiates Reschedule Training Session from Session Reschedule, a related workflow, a scheduled job, or an approved integration event.

### In Scope

- Capture or retrieve required Personal Training context.
- Validate Organization, Facility, Site, Customer, user, and policy scope where applicable.
- Execute Reschedule Training Session according to approved business rules.
- Persist the resulting Personal Training Package state or transaction.
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
- Personal Training Package reference
- Customer reference, where applicable
- Effective date and time, where applicable
- Status or action reason, where applicable
- Payment, billing, trainer, session, or subscription reference where applicable
- Actor remarks, where applicable

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Personal Training Package ID | Primary business record reference | Identifier | Yes | System / User | Must exist or be generated within scope | Core reference for Reschedule Training Session |
| Organization ID | Tenant Organization context | Identifier | Yes | Session / System | Must be Active and authorized | Enforces tenant isolation |
| Facility ID | Facility context | Identifier | Conditional | User / System | Must be Active where applicable | Required for facility-level operations |
| Site ID | Site context | Identifier | Conditional | User / System | Must belong to Facility where applicable | Required for site-level operations |
| Status | Lifecycle or processing state | Enum | Yes | System | Must follow allowed state transitions | Drives UI and downstream access |
| Effective Date | Date when action applies | DateTime | Conditional | User / System | Must satisfy policy | Supports scheduled or immediate actions |
| Reason / Remarks | Business explanation | Text | Conditional | User | Required for governed changes | Stored for audit |

### Main Flow

1. Actor opens Session Reschedule or the related workflow.
2. The system validates authentication, authorization, tenant scope, and current operating context.
3. The system loads the required Personal Training records, related configuration, and policy controls.
4. Actor enters or confirms the information required to reschedule training session.
5. The system validates mandatory data, lifecycle status, ownership, eligibility, financial, capacity, schedule, and security rules where applicable.
6. The system executes Reschedule Training Session and persists the resulting Personal Training Package state or transaction.
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

- Personal Training Package record created, updated, validated, or reported according to the action.
- Lifecycle or processing status updated.
- Related history entry created.
- Business events emitted.
- Notifications generated where configured.
- Audit events recorded.
- Reports or dashboards updated where applicable.

### UI Behaviour

Session Reschedule shall display scoped context, mandatory fields, lifecycle status, policy warnings, validation results, available actions, confirmation prompts, read-only states, pagination or filters where applicable, and responsive behavior for front-desk and administrative usage.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-PTR-005-001 | Actor must have permission to execute Reschedule Training Session. | Deny request and audit. | Critical |
| VAL-PTR-005-002 | Record must belong to the authorized Organization scope. | Deny request. | Critical |
| VAL-PTR-005-003 | Mandatory inputs must be complete and valid. | Block submission. | Critical |
| VAL-PTR-005-004 | Lifecycle and policy rules from BA-02 must be satisfied. | Reject or route for approval. | High |
| VAL-PTR-005-005 | Historical and audit records must be preserved. | Roll back or mark for recovery. | Critical |

### Business Rules

- BA-02 BR-TRN-005
- BA-02 BR-TRN-008
- BA-02 BR-TRN-009
- BA-02 BR-AUD-003

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| ptr.reschedule.training.session.view | Reception Staff | Read | View Reschedule Training Session context |
| ptr.reschedule.training.session.execute | Reception Staff | Execute | Execute Reschedule Training Session |
| ptr.reschedule.training.session.approve | Organization Administrator | Approve | Approve governed exceptions where configured |
| ptr.reschedule.training.session.audit.view | Organization Administrator / Support Executive | Read | View audit trace |

### Security Considerations

The capability shall enforce authentication, role-based authorization, tenant isolation, Organization scope, Facility and Site access boundaries, sensitive data masking, secure references, and immutable audit logging.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Reschedule Training Session Completed | Primary actor and configured stakeholders | In-App / Email | Action completes | Include reference, status, and effective date where applicable |
| Reschedule Training Session Requires Approval | Approver | In-App | Approval rule applies | Include safe summary and requested action |
| Reschedule Training Session Failed | Primary actor | In-App | Validation or processing fails | Include safe failure reason and next action |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| RescheduleTrainingSessionRequested | Personal Training | Approval Workflow, Audit Service |
| RescheduleTrainingSessionCompleted | Personal Training | Notification Service, Reporting Service, Audit Service |
| RescheduleTrainingSessionRejected | Personal Training | Notification Service, Audit Service |

### Audit Events

| Audit Event | Description | Actor | Target Entity | Key Data |
|---|---|---|---|---|
| RESCHEDULE_TRAINING_SESSION_REQUESTED | Reschedule Training Session requested | Reception Staff | Personal Training Package | Scope, reference, and reason |
| RESCHEDULE_TRAINING_SESSION_COMPLETED | Reschedule Training Session completed | Reception Staff / System | Personal Training Package | Previous and new state |
| RESCHEDULE_TRAINING_SESSION_REJECTED | Reschedule Training Session rejected | System | Personal Training Package | Rejection reason |

### Reports Generated

- Personal Training Operational Report
- Personal Training History Report
- Personal Training Exception Report
- Executive Dashboard

### Related Screens

- Session Reschedule
- Personal Training Dashboard
- Personal Training History
- Audit Log Viewer

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/training-sessions/{sessionId}/reschedule | POST | Authorized token | Execute Reschedule Training Session | 200 OK or 201 Created with result |
| /api/v1/training-sessions/{sessionId}/reschedule/history | GET | Authorized token | Retrieve Reschedule Training Session history | 200 OK with history |
| /api/v1/audit-logs | GET | Authorized token | Retrieve related audit events | 200 OK with scoped audit records |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Personal Training Package | Create / Update / Read | Support Reschedule Training Session | Governed by Organization scope |
| Personal Training Session | Read / Insert | Support Reschedule Training Session | Governed by Organization scope |
| Trainer Assignment | Read / Insert | Support Reschedule Training Session | Governed by Organization scope |
| Training Notes | Read / Insert | Support Reschedule Training Session | Governed by Organization scope |
| Customer Progress | Read / Insert | Support Reschedule Training Session | Governed by Organization scope |
| Audit Log | Insert | Record auditable activity | Immutable |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Draft | Reschedule Training Session initiated | Validated | Reception Staff | Required data captured |
| Validated | Validation succeeds | Pending Approval | System | BA-02 rules satisfied |
| Pending Approval | Processing completes | Completed | System | Related updates succeed |
| Pending Approval | Approval or policy failure | Rejected | System / Approver | Request rejected |
| Completed | View history | Completed | Authorized user | Read-only historical access |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| PTR-005-001 | Reschedule Training Session cannot be completed because required information is missing. | Missing mandatory data | Complete required fields |
| PTR-005-002 | You do not have permission to perform this action. | Authorization failure | Request access |
| PTR-005-003 | The selected record is not eligible for this action. | Policy or lifecycle violation | Review record status |
| PTR-005-004 | Reschedule Training Session could not be completed due to a system or integration error. | Processing failure | Retry or contact support |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Execute Reschedule Training Session | Given the actor has required permission and valid scope | When the actor submits valid information | Then the system shall complete Reschedule Training Session successfully |
| Enforce validation | Given mandatory data or policy conditions are invalid | When the action is submitted | Then the system shall reject the request with a clear message |
| Preserve audit | Given the action completes or fails | When processing ends | Then audit events shall record actor, timestamp, scope, and outcome |
| Protect scope | Given the selected record is outside authorized scope | When the action is requested | Then the system shall deny access |

### Dependencies

- Trainer Management
- Customer Management
- Attendance Management
- Billing Management
- Payment Management
- Notification Management
- Reporting Service

### Operational Considerations

Reschedule Training Session should be designed for high-volume operational use, retry-safe processing, clear exception handling, and support-team diagnostics without exposing sensitive data.

### Non-Functional Considerations

This requirement shall satisfy Digitize non-functional expectations for availability, reliability, performance, scalability, security, configurability, maintainability, and auditability.

### Assumptions

- Required master data and configuration are maintained by authorized users.
- Related services expose stable APIs for validation and synchronization.
- Organization policies define approval, retention, notification, and exception behavior.

### Success Criteria

Reschedule Training Session is completed accurately, securely, and audibly, with downstream records synchronized and no loss of historical traceability.

### Related Functional Requirements

- FR-PTR-001 - Create Personal Training Package
- FR-PTR-002 - Configure Training Package
- FR-PTR-003 - Assign Trainer
- FR-PTR-004 - Book Personal Training Session
- FR-AUD-001 - Record Audit Events

### Notes

Reschedule Training Session shall remain aligned with the approved BA source documents and shall not introduce behavior that bypasses tenant isolation, lifecycle governance, financial controls, or auditability.

---

## FR-PTR-006 - Cancel Training Session

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-PTR-006 |
| Requirement Name | Cancel Training Session |
| Functional Module | Personal Training |
| Business Domain | Personal Training |
| Business Capability | Session Administration |
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
| Business Requirement | BA-08 BR-017 Personal Training Booking |
| Business Rule | BA-02 BR-TRN-009, BR-PAY-006, BR-AUD-003, BR-SEC-004 |
| Business Process | BA-03 BP-PTR-006 Cancel Training Session |
| Business Process Flow | BA-04 Section 23 Personal Training Flow |
| Persona | BA-05 Trainer, Reception Staff, Customer, Facility Manager |
| User Journey | BA-06 Section 18 Personal Training Journey |
| Stakeholder | BA-07 Trainer, Reception Staff, Customer, Facility Manager |
| Non-Functional Requirement | BA-09 Section 2.6 Usability, Section 2.10 Auditability, Section 11 Reporting Requirements |
| Assumption / Constraint / Risk | BA-10 BA-ASS-011, BA-RSK-006, BA-RSK-012 |

### Purpose

To enable Session Administration within Personal Training so Digitize can execute Cancel Training Session consistently across Organizations, Facilities, Sites, users, and related operational or commercial services.

### Functional Requirement

The system shall support Cancel Training Session as an atomic Personal Training capability, including scoped data capture, business-rule validation, permission enforcement, lifecycle handling, related service synchronization, notification generation, reporting contribution, and immutable audit recording.

### Business Justification

Cancel Training Session is required to preserve operational control, revenue accuracy, service continuity, customer trust, and enterprise traceability for Personal Training processes. Without this capability, downstream modules would rely on incomplete, manual, or inconsistent records.

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
- Actor has permission for Cancel Training Session.
- Required Personal Training configuration and policies are available.
- Related records required by BA-03 BP-PTR-006 Cancel Training Session are available and within authorized scope.

### Trigger

The capability is triggered when Reception Staff or the System initiates Cancel Training Session from Session Cancellation, a related workflow, a scheduled job, or an approved integration event.

### In Scope

- Capture or retrieve required Personal Training context.
- Validate Organization, Facility, Site, Customer, user, and policy scope where applicable.
- Execute Cancel Training Session according to approved business rules.
- Persist the resulting Personal Training Package state or transaction.
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
- Personal Training Package reference
- Customer reference, where applicable
- Effective date and time, where applicable
- Status or action reason, where applicable
- Payment, billing, trainer, session, or subscription reference where applicable
- Actor remarks, where applicable

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Personal Training Package ID | Primary business record reference | Identifier | Yes | System / User | Must exist or be generated within scope | Core reference for Cancel Training Session |
| Organization ID | Tenant Organization context | Identifier | Yes | Session / System | Must be Active and authorized | Enforces tenant isolation |
| Facility ID | Facility context | Identifier | Conditional | User / System | Must be Active where applicable | Required for facility-level operations |
| Site ID | Site context | Identifier | Conditional | User / System | Must belong to Facility where applicable | Required for site-level operations |
| Status | Lifecycle or processing state | Enum | Yes | System | Must follow allowed state transitions | Drives UI and downstream access |
| Effective Date | Date when action applies | DateTime | Conditional | User / System | Must satisfy policy | Supports scheduled or immediate actions |
| Reason / Remarks | Business explanation | Text | Conditional | User | Required for governed changes | Stored for audit |

### Main Flow

1. Actor opens Session Cancellation or the related workflow.
2. The system validates authentication, authorization, tenant scope, and current operating context.
3. The system loads the required Personal Training records, related configuration, and policy controls.
4. Actor enters or confirms the information required to cancel training session.
5. The system validates mandatory data, lifecycle status, ownership, eligibility, financial, capacity, schedule, and security rules where applicable.
6. The system executes Cancel Training Session and persists the resulting Personal Training Package state or transaction.
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

- Personal Training Package record created, updated, validated, or reported according to the action.
- Lifecycle or processing status updated.
- Related history entry created.
- Business events emitted.
- Notifications generated where configured.
- Audit events recorded.
- Reports or dashboards updated where applicable.

### UI Behaviour

Session Cancellation shall display scoped context, mandatory fields, lifecycle status, policy warnings, validation results, available actions, confirmation prompts, read-only states, pagination or filters where applicable, and responsive behavior for front-desk and administrative usage.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-PTR-006-001 | Actor must have permission to execute Cancel Training Session. | Deny request and audit. | Critical |
| VAL-PTR-006-002 | Record must belong to the authorized Organization scope. | Deny request. | Critical |
| VAL-PTR-006-003 | Mandatory inputs must be complete and valid. | Block submission. | Critical |
| VAL-PTR-006-004 | Lifecycle and policy rules from BA-02 must be satisfied. | Reject or route for approval. | High |
| VAL-PTR-006-005 | Historical and audit records must be preserved. | Roll back or mark for recovery. | Critical |

### Business Rules

- BA-02 BR-TRN-009
- BA-02 BR-PAY-006
- BA-02 BR-AUD-003
- BA-02 BR-SEC-004

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| ptr.cancel.training.session.view | Reception Staff | Read | View Cancel Training Session context |
| ptr.cancel.training.session.execute | Reception Staff | Execute | Execute Cancel Training Session |
| ptr.cancel.training.session.approve | Organization Administrator | Approve | Approve governed exceptions where configured |
| ptr.cancel.training.session.audit.view | Organization Administrator / Support Executive | Read | View audit trace |

### Security Considerations

The capability shall enforce authentication, role-based authorization, tenant isolation, Organization scope, Facility and Site access boundaries, sensitive data masking, secure references, and immutable audit logging.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Cancel Training Session Completed | Primary actor and configured stakeholders | In-App / Email | Action completes | Include reference, status, and effective date where applicable |
| Cancel Training Session Requires Approval | Approver | In-App | Approval rule applies | Include safe summary and requested action |
| Cancel Training Session Failed | Primary actor | In-App | Validation or processing fails | Include safe failure reason and next action |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| CancelTrainingSessionRequested | Personal Training | Approval Workflow, Audit Service |
| CancelTrainingSessionCompleted | Personal Training | Notification Service, Reporting Service, Audit Service |
| CancelTrainingSessionRejected | Personal Training | Notification Service, Audit Service |

### Audit Events

| Audit Event | Description | Actor | Target Entity | Key Data |
|---|---|---|---|---|
| CANCEL_TRAINING_SESSION_REQUESTED | Cancel Training Session requested | Reception Staff | Personal Training Package | Scope, reference, and reason |
| CANCEL_TRAINING_SESSION_COMPLETED | Cancel Training Session completed | Reception Staff / System | Personal Training Package | Previous and new state |
| CANCEL_TRAINING_SESSION_REJECTED | Cancel Training Session rejected | System | Personal Training Package | Rejection reason |

### Reports Generated

- Personal Training Operational Report
- Personal Training History Report
- Personal Training Exception Report
- Executive Dashboard

### Related Screens

- Session Cancellation
- Personal Training Dashboard
- Personal Training History
- Audit Log Viewer

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/training-sessions/{sessionId}/cancel | POST | Authorized token | Execute Cancel Training Session | 200 OK or 201 Created with result |
| /api/v1/training-sessions/{sessionId}/cancel/history | GET | Authorized token | Retrieve Cancel Training Session history | 200 OK with history |
| /api/v1/audit-logs | GET | Authorized token | Retrieve related audit events | 200 OK with scoped audit records |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Personal Training Package | Create / Update / Read | Support Cancel Training Session | Governed by Organization scope |
| Personal Training Session | Read / Insert | Support Cancel Training Session | Governed by Organization scope |
| Trainer Assignment | Read / Insert | Support Cancel Training Session | Governed by Organization scope |
| Training Notes | Read / Insert | Support Cancel Training Session | Governed by Organization scope |
| Customer Progress | Read / Insert | Support Cancel Training Session | Governed by Organization scope |
| Audit Log | Insert | Record auditable activity | Immutable |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Draft | Cancel Training Session initiated | Validated | Reception Staff | Required data captured |
| Validated | Validation succeeds | Pending Approval | System | BA-02 rules satisfied |
| Pending Approval | Processing completes | Completed | System | Related updates succeed |
| Pending Approval | Approval or policy failure | Rejected | System / Approver | Request rejected |
| Completed | View history | Completed | Authorized user | Read-only historical access |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| PTR-006-001 | Cancel Training Session cannot be completed because required information is missing. | Missing mandatory data | Complete required fields |
| PTR-006-002 | You do not have permission to perform this action. | Authorization failure | Request access |
| PTR-006-003 | The selected record is not eligible for this action. | Policy or lifecycle violation | Review record status |
| PTR-006-004 | Cancel Training Session could not be completed due to a system or integration error. | Processing failure | Retry or contact support |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Execute Cancel Training Session | Given the actor has required permission and valid scope | When the actor submits valid information | Then the system shall complete Cancel Training Session successfully |
| Enforce validation | Given mandatory data or policy conditions are invalid | When the action is submitted | Then the system shall reject the request with a clear message |
| Preserve audit | Given the action completes or fails | When processing ends | Then audit events shall record actor, timestamp, scope, and outcome |
| Protect scope | Given the selected record is outside authorized scope | When the action is requested | Then the system shall deny access |

### Dependencies

- Trainer Management
- Customer Management
- Attendance Management
- Billing Management
- Payment Management
- Notification Management
- Reporting Service

### Operational Considerations

Cancel Training Session should be designed for high-volume operational use, retry-safe processing, clear exception handling, and support-team diagnostics without exposing sensitive data.

### Non-Functional Considerations

This requirement shall satisfy Digitize non-functional expectations for availability, reliability, performance, scalability, security, configurability, maintainability, and auditability.

### Assumptions

- Required master data and configuration are maintained by authorized users.
- Related services expose stable APIs for validation and synchronization.
- Organization policies define approval, retention, notification, and exception behavior.

### Success Criteria

Cancel Training Session is completed accurately, securely, and audibly, with downstream records synchronized and no loss of historical traceability.

### Related Functional Requirements

- FR-PTR-001 - Create Personal Training Package
- FR-PTR-002 - Configure Training Package
- FR-PTR-003 - Assign Trainer
- FR-PTR-004 - Book Personal Training Session
- FR-AUD-001 - Record Audit Events

### Notes

Cancel Training Session shall remain aligned with the approved BA source documents and shall not introduce behavior that bypasses tenant isolation, lifecycle governance, financial controls, or auditability.

---

## FR-PTR-007 - Start Personal Training Session

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-PTR-007 |
| Requirement Name | Start Personal Training Session |
| Functional Module | Personal Training |
| Business Domain | Personal Training |
| Business Capability | Session Management |
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
| Business Requirement | BA-08 BR-017 Personal Training Booking |
| Business Rule | BA-02 BR-TRN-003, BR-TRN-007, BR-ATT-002, BR-SEC-004 |
| Business Process | BA-03 BP-PTR-007 Start Personal Training Session |
| Business Process Flow | BA-04 Section 23 Personal Training Flow |
| Persona | BA-05 Trainer, Reception Staff, Customer, Facility Manager |
| User Journey | BA-06 Section 18 Personal Training Journey |
| Stakeholder | BA-07 Trainer, Reception Staff, Customer, Facility Manager |
| Non-Functional Requirement | BA-09 Section 2.6 Usability, Section 2.10 Auditability, Section 11 Reporting Requirements |
| Assumption / Constraint / Risk | BA-10 BA-ASS-011, BA-RSK-006, BA-RSK-012 |

### Purpose

To enable Session Management within Personal Training so Digitize can execute Start Personal Training Session consistently across Organizations, Facilities, Sites, users, and related operational or commercial services.

### Functional Requirement

The system shall support Start Personal Training Session as an atomic Personal Training capability, including scoped data capture, business-rule validation, permission enforcement, lifecycle handling, related service synchronization, notification generation, reporting contribution, and immutable audit recording.

### Business Justification

Start Personal Training Session is required to preserve operational control, revenue accuracy, service continuity, customer trust, and enterprise traceability for Personal Training processes. Without this capability, downstream modules would rely on incomplete, manual, or inconsistent records.

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
- Actor has permission for Start Personal Training Session.
- Required Personal Training configuration and policies are available.
- Related records required by BA-03 BP-PTR-007 Start Personal Training Session are available and within authorized scope.

### Trigger

The capability is triggered when Trainer or the System initiates Start Personal Training Session from Session Detail, a related workflow, a scheduled job, or an approved integration event.

### In Scope

- Capture or retrieve required Personal Training context.
- Validate Organization, Facility, Site, Customer, user, and policy scope where applicable.
- Execute Start Personal Training Session according to approved business rules.
- Persist the resulting Personal Training Package state or transaction.
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
- Personal Training Package reference
- Customer reference, where applicable
- Effective date and time, where applicable
- Status or action reason, where applicable
- Payment, billing, trainer, session, or subscription reference where applicable
- Actor remarks, where applicable

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Personal Training Package ID | Primary business record reference | Identifier | Yes | System / User | Must exist or be generated within scope | Core reference for Start Personal Training Session |
| Organization ID | Tenant Organization context | Identifier | Yes | Session / System | Must be Active and authorized | Enforces tenant isolation |
| Facility ID | Facility context | Identifier | Conditional | User / System | Must be Active where applicable | Required for facility-level operations |
| Site ID | Site context | Identifier | Conditional | User / System | Must belong to Facility where applicable | Required for site-level operations |
| Status | Lifecycle or processing state | Enum | Yes | System | Must follow allowed state transitions | Drives UI and downstream access |
| Effective Date | Date when action applies | DateTime | Conditional | User / System | Must satisfy policy | Supports scheduled or immediate actions |
| Reason / Remarks | Business explanation | Text | Conditional | User | Required for governed changes | Stored for audit |

### Main Flow

1. Actor opens Session Detail or the related workflow.
2. The system validates authentication, authorization, tenant scope, and current operating context.
3. The system loads the required Personal Training records, related configuration, and policy controls.
4. Actor enters or confirms the information required to start personal training session.
5. The system validates mandatory data, lifecycle status, ownership, eligibility, financial, capacity, schedule, and security rules where applicable.
6. The system executes Start Personal Training Session and persists the resulting Personal Training Package state or transaction.
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

- Personal Training Package record created, updated, validated, or reported according to the action.
- Lifecycle or processing status updated.
- Related history entry created.
- Business events emitted.
- Notifications generated where configured.
- Audit events recorded.
- Reports or dashboards updated where applicable.

### UI Behaviour

Session Detail shall display scoped context, mandatory fields, lifecycle status, policy warnings, validation results, available actions, confirmation prompts, read-only states, pagination or filters where applicable, and responsive behavior for front-desk and administrative usage.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-PTR-007-001 | Actor must have permission to execute Start Personal Training Session. | Deny request and audit. | Critical |
| VAL-PTR-007-002 | Record must belong to the authorized Organization scope. | Deny request. | Critical |
| VAL-PTR-007-003 | Mandatory inputs must be complete and valid. | Block submission. | Critical |
| VAL-PTR-007-004 | Lifecycle and policy rules from BA-02 must be satisfied. | Reject or route for approval. | High |
| VAL-PTR-007-005 | Historical and audit records must be preserved. | Roll back or mark for recovery. | Critical |

### Business Rules

- BA-02 BR-TRN-003
- BA-02 BR-TRN-007
- BA-02 BR-ATT-002
- BA-02 BR-SEC-004

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| ptr.start.personal.training.session.view | Trainer | Read | View Start Personal Training Session context |
| ptr.start.personal.training.session.execute | Trainer | Execute | Execute Start Personal Training Session |
| ptr.start.personal.training.session.approve | Organization Administrator | Approve | Approve governed exceptions where configured |
| ptr.start.personal.training.session.audit.view | Organization Administrator / Support Executive | Read | View audit trace |

### Security Considerations

The capability shall enforce authentication, role-based authorization, tenant isolation, Organization scope, Facility and Site access boundaries, sensitive data masking, secure references, and immutable audit logging.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Start Personal Training Session Completed | Primary actor and configured stakeholders | In-App / Email | Action completes | Include reference, status, and effective date where applicable |
| Start Personal Training Session Requires Approval | Approver | In-App | Approval rule applies | Include safe summary and requested action |
| Start Personal Training Session Failed | Primary actor | In-App | Validation or processing fails | Include safe failure reason and next action |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| StartPersonalTrainingSessionRequested | Personal Training | Approval Workflow, Audit Service |
| StartPersonalTrainingSessionCompleted | Personal Training | Notification Service, Reporting Service, Audit Service |
| StartPersonalTrainingSessionRejected | Personal Training | Notification Service, Audit Service |

### Audit Events

| Audit Event | Description | Actor | Target Entity | Key Data |
|---|---|---|---|---|
| START_PERSONAL_TRAINING_SESSION_REQUESTED | Start Personal Training Session requested | Trainer | Personal Training Package | Scope, reference, and reason |
| START_PERSONAL_TRAINING_SESSION_COMPLETED | Start Personal Training Session completed | Trainer / System | Personal Training Package | Previous and new state |
| START_PERSONAL_TRAINING_SESSION_REJECTED | Start Personal Training Session rejected | System | Personal Training Package | Rejection reason |

### Reports Generated

- Personal Training Operational Report
- Personal Training History Report
- Personal Training Exception Report
- Executive Dashboard

### Related Screens

- Session Detail
- Personal Training Dashboard
- Personal Training History
- Audit Log Viewer

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/training-sessions/{sessionId}/start | POST | Authorized token | Execute Start Personal Training Session | 200 OK or 201 Created with result |
| /api/v1/training-sessions/{sessionId}/start/history | GET | Authorized token | Retrieve Start Personal Training Session history | 200 OK with history |
| /api/v1/audit-logs | GET | Authorized token | Retrieve related audit events | 200 OK with scoped audit records |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Personal Training Package | Create / Update / Read | Support Start Personal Training Session | Governed by Organization scope |
| Personal Training Session | Read / Insert | Support Start Personal Training Session | Governed by Organization scope |
| Trainer Assignment | Read / Insert | Support Start Personal Training Session | Governed by Organization scope |
| Training Notes | Read / Insert | Support Start Personal Training Session | Governed by Organization scope |
| Customer Progress | Read / Insert | Support Start Personal Training Session | Governed by Organization scope |
| Audit Log | Insert | Record auditable activity | Immutable |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Draft | Start Personal Training Session initiated | Validated | Trainer | Required data captured |
| Validated | Validation succeeds | Pending Approval | System | BA-02 rules satisfied |
| Pending Approval | Processing completes | Completed | System | Related updates succeed |
| Pending Approval | Approval or policy failure | Rejected | System / Approver | Request rejected |
| Completed | View history | Completed | Authorized user | Read-only historical access |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| PTR-007-001 | Start Personal Training Session cannot be completed because required information is missing. | Missing mandatory data | Complete required fields |
| PTR-007-002 | You do not have permission to perform this action. | Authorization failure | Request access |
| PTR-007-003 | The selected record is not eligible for this action. | Policy or lifecycle violation | Review record status |
| PTR-007-004 | Start Personal Training Session could not be completed due to a system or integration error. | Processing failure | Retry or contact support |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Execute Start Personal Training Session | Given the actor has required permission and valid scope | When the actor submits valid information | Then the system shall complete Start Personal Training Session successfully |
| Enforce validation | Given mandatory data or policy conditions are invalid | When the action is submitted | Then the system shall reject the request with a clear message |
| Preserve audit | Given the action completes or fails | When processing ends | Then audit events shall record actor, timestamp, scope, and outcome |
| Protect scope | Given the selected record is outside authorized scope | When the action is requested | Then the system shall deny access |

### Dependencies

- Trainer Management
- Customer Management
- Attendance Management
- Billing Management
- Payment Management
- Notification Management
- Reporting Service

### Operational Considerations

Start Personal Training Session should be designed for high-volume operational use, retry-safe processing, clear exception handling, and support-team diagnostics without exposing sensitive data.

### Non-Functional Considerations

This requirement shall satisfy Digitize non-functional expectations for availability, reliability, performance, scalability, security, configurability, maintainability, and auditability.

### Assumptions

- Required master data and configuration are maintained by authorized users.
- Related services expose stable APIs for validation and synchronization.
- Organization policies define approval, retention, notification, and exception behavior.

### Success Criteria

Start Personal Training Session is completed accurately, securely, and audibly, with downstream records synchronized and no loss of historical traceability.

### Related Functional Requirements

- FR-PTR-001 - Create Personal Training Package
- FR-PTR-002 - Configure Training Package
- FR-PTR-003 - Assign Trainer
- FR-PTR-004 - Book Personal Training Session
- FR-AUD-001 - Record Audit Events

### Notes

Start Personal Training Session shall remain aligned with the approved BA source documents and shall not introduce behavior that bypasses tenant isolation, lifecycle governance, financial controls, or auditability.

---

## FR-PTR-008 - Complete Personal Training Session

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-PTR-008 |
| Requirement Name | Complete Personal Training Session |
| Functional Module | Personal Training |
| Business Domain | Personal Training |
| Business Capability | Session Management |
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
| Business Requirement | BA-08 BR-017 Personal Training Booking |
| Business Rule | BA-02 BR-TRN-007, BR-TRN-009, BR-ATT-009, BR-AUD-003 |
| Business Process | BA-03 BP-PTR-008 Complete Personal Training Session |
| Business Process Flow | BA-04 Section 23 Personal Training Flow |
| Persona | BA-05 Trainer, Reception Staff, Customer, Facility Manager |
| User Journey | BA-06 Section 18 Personal Training Journey |
| Stakeholder | BA-07 Trainer, Reception Staff, Customer, Facility Manager |
| Non-Functional Requirement | BA-09 Section 2.6 Usability, Section 2.10 Auditability, Section 11 Reporting Requirements |
| Assumption / Constraint / Risk | BA-10 BA-ASS-011, BA-RSK-006, BA-RSK-012 |

### Purpose

To enable Session Management within Personal Training so Digitize can execute Complete Personal Training Session consistently across Organizations, Facilities, Sites, users, and related operational or commercial services.

### Functional Requirement

The system shall support Complete Personal Training Session as an atomic Personal Training capability, including scoped data capture, business-rule validation, permission enforcement, lifecycle handling, related service synchronization, notification generation, reporting contribution, and immutable audit recording.

### Business Justification

Complete Personal Training Session is required to preserve operational control, revenue accuracy, service continuity, customer trust, and enterprise traceability for Personal Training processes. Without this capability, downstream modules would rely on incomplete, manual, or inconsistent records.

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
- Actor has permission for Complete Personal Training Session.
- Required Personal Training configuration and policies are available.
- Related records required by BA-03 BP-PTR-008 Complete Personal Training Session are available and within authorized scope.

### Trigger

The capability is triggered when Trainer or the System initiates Complete Personal Training Session from Session Detail, a related workflow, a scheduled job, or an approved integration event.

### In Scope

- Capture or retrieve required Personal Training context.
- Validate Organization, Facility, Site, Customer, user, and policy scope where applicable.
- Execute Complete Personal Training Session according to approved business rules.
- Persist the resulting Personal Training Package state or transaction.
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
- Personal Training Package reference
- Customer reference, where applicable
- Effective date and time, where applicable
- Status or action reason, where applicable
- Payment, billing, trainer, session, or subscription reference where applicable
- Actor remarks, where applicable

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Personal Training Package ID | Primary business record reference | Identifier | Yes | System / User | Must exist or be generated within scope | Core reference for Complete Personal Training Session |
| Organization ID | Tenant Organization context | Identifier | Yes | Session / System | Must be Active and authorized | Enforces tenant isolation |
| Facility ID | Facility context | Identifier | Conditional | User / System | Must be Active where applicable | Required for facility-level operations |
| Site ID | Site context | Identifier | Conditional | User / System | Must belong to Facility where applicable | Required for site-level operations |
| Status | Lifecycle or processing state | Enum | Yes | System | Must follow allowed state transitions | Drives UI and downstream access |
| Effective Date | Date when action applies | DateTime | Conditional | User / System | Must satisfy policy | Supports scheduled or immediate actions |
| Reason / Remarks | Business explanation | Text | Conditional | User | Required for governed changes | Stored for audit |

### Main Flow

1. Actor opens Session Detail or the related workflow.
2. The system validates authentication, authorization, tenant scope, and current operating context.
3. The system loads the required Personal Training records, related configuration, and policy controls.
4. Actor enters or confirms the information required to complete personal training session.
5. The system validates mandatory data, lifecycle status, ownership, eligibility, financial, capacity, schedule, and security rules where applicable.
6. The system executes Complete Personal Training Session and persists the resulting Personal Training Package state or transaction.
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

- Personal Training Package record created, updated, validated, or reported according to the action.
- Lifecycle or processing status updated.
- Related history entry created.
- Business events emitted.
- Notifications generated where configured.
- Audit events recorded.
- Reports or dashboards updated where applicable.

### UI Behaviour

Session Detail shall display scoped context, mandatory fields, lifecycle status, policy warnings, validation results, available actions, confirmation prompts, read-only states, pagination or filters where applicable, and responsive behavior for front-desk and administrative usage.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-PTR-008-001 | Actor must have permission to execute Complete Personal Training Session. | Deny request and audit. | Critical |
| VAL-PTR-008-002 | Record must belong to the authorized Organization scope. | Deny request. | Critical |
| VAL-PTR-008-003 | Mandatory inputs must be complete and valid. | Block submission. | Critical |
| VAL-PTR-008-004 | Lifecycle and policy rules from BA-02 must be satisfied. | Reject or route for approval. | High |
| VAL-PTR-008-005 | Historical and audit records must be preserved. | Roll back or mark for recovery. | Critical |

### Business Rules

- BA-02 BR-TRN-007
- BA-02 BR-TRN-009
- BA-02 BR-ATT-009
- BA-02 BR-AUD-003

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| ptr.complete.personal.training.session.view | Trainer | Read | View Complete Personal Training Session context |
| ptr.complete.personal.training.session.execute | Trainer | Execute | Execute Complete Personal Training Session |
| ptr.complete.personal.training.session.approve | Organization Administrator | Approve | Approve governed exceptions where configured |
| ptr.complete.personal.training.session.audit.view | Organization Administrator / Support Executive | Read | View audit trace |

### Security Considerations

The capability shall enforce authentication, role-based authorization, tenant isolation, Organization scope, Facility and Site access boundaries, sensitive data masking, secure references, and immutable audit logging.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Complete Personal Training Session Completed | Primary actor and configured stakeholders | In-App / Email | Action completes | Include reference, status, and effective date where applicable |
| Complete Personal Training Session Requires Approval | Approver | In-App | Approval rule applies | Include safe summary and requested action |
| Complete Personal Training Session Failed | Primary actor | In-App | Validation or processing fails | Include safe failure reason and next action |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| CompletePersonalTrainingSessionRequested | Personal Training | Approval Workflow, Audit Service |
| CompletePersonalTrainingSessionCompleted | Personal Training | Notification Service, Reporting Service, Audit Service |
| CompletePersonalTrainingSessionRejected | Personal Training | Notification Service, Audit Service |

### Audit Events

| Audit Event | Description | Actor | Target Entity | Key Data |
|---|---|---|---|---|
| COMPLETE_PERSONAL_TRAINING_SESSION_REQUESTED | Complete Personal Training Session requested | Trainer | Personal Training Package | Scope, reference, and reason |
| COMPLETE_PERSONAL_TRAINING_SESSION_COMPLETED | Complete Personal Training Session completed | Trainer / System | Personal Training Package | Previous and new state |
| COMPLETE_PERSONAL_TRAINING_SESSION_REJECTED | Complete Personal Training Session rejected | System | Personal Training Package | Rejection reason |

### Reports Generated

- Personal Training Operational Report
- Personal Training History Report
- Personal Training Exception Report
- Executive Dashboard

### Related Screens

- Session Detail
- Personal Training Dashboard
- Personal Training History
- Audit Log Viewer

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/training-sessions/{sessionId}/complete | POST | Authorized token | Execute Complete Personal Training Session | 200 OK or 201 Created with result |
| /api/v1/training-sessions/{sessionId}/complete/history | GET | Authorized token | Retrieve Complete Personal Training Session history | 200 OK with history |
| /api/v1/audit-logs | GET | Authorized token | Retrieve related audit events | 200 OK with scoped audit records |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Personal Training Package | Create / Update / Read | Support Complete Personal Training Session | Governed by Organization scope |
| Personal Training Session | Read / Insert | Support Complete Personal Training Session | Governed by Organization scope |
| Trainer Assignment | Read / Insert | Support Complete Personal Training Session | Governed by Organization scope |
| Training Notes | Read / Insert | Support Complete Personal Training Session | Governed by Organization scope |
| Customer Progress | Read / Insert | Support Complete Personal Training Session | Governed by Organization scope |
| Audit Log | Insert | Record auditable activity | Immutable |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Draft | Complete Personal Training Session initiated | Validated | Trainer | Required data captured |
| Validated | Validation succeeds | Pending Approval | System | BA-02 rules satisfied |
| Pending Approval | Processing completes | Completed | System | Related updates succeed |
| Pending Approval | Approval or policy failure | Rejected | System / Approver | Request rejected |
| Completed | View history | Completed | Authorized user | Read-only historical access |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| PTR-008-001 | Complete Personal Training Session cannot be completed because required information is missing. | Missing mandatory data | Complete required fields |
| PTR-008-002 | You do not have permission to perform this action. | Authorization failure | Request access |
| PTR-008-003 | The selected record is not eligible for this action. | Policy or lifecycle violation | Review record status |
| PTR-008-004 | Complete Personal Training Session could not be completed due to a system or integration error. | Processing failure | Retry or contact support |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Execute Complete Personal Training Session | Given the actor has required permission and valid scope | When the actor submits valid information | Then the system shall complete Complete Personal Training Session successfully |
| Enforce validation | Given mandatory data or policy conditions are invalid | When the action is submitted | Then the system shall reject the request with a clear message |
| Preserve audit | Given the action completes or fails | When processing ends | Then audit events shall record actor, timestamp, scope, and outcome |
| Protect scope | Given the selected record is outside authorized scope | When the action is requested | Then the system shall deny access |

### Dependencies

- Trainer Management
- Customer Management
- Attendance Management
- Billing Management
- Payment Management
- Notification Management
- Reporting Service

### Operational Considerations

Complete Personal Training Session should be designed for high-volume operational use, retry-safe processing, clear exception handling, and support-team diagnostics without exposing sensitive data.

### Non-Functional Considerations

This requirement shall satisfy Digitize non-functional expectations for availability, reliability, performance, scalability, security, configurability, maintainability, and auditability.

### Assumptions

- Required master data and configuration are maintained by authorized users.
- Related services expose stable APIs for validation and synchronization.
- Organization policies define approval, retention, notification, and exception behavior.

### Success Criteria

Complete Personal Training Session is completed accurately, securely, and audibly, with downstream records synchronized and no loss of historical traceability.

### Related Functional Requirements

- FR-PTR-001 - Create Personal Training Package
- FR-PTR-002 - Configure Training Package
- FR-PTR-003 - Assign Trainer
- FR-PTR-004 - Book Personal Training Session
- FR-AUD-001 - Record Audit Events

### Notes

Complete Personal Training Session shall remain aligned with the approved BA source documents and shall not introduce behavior that bypasses tenant isolation, lifecycle governance, financial controls, or auditability.

---

## FR-PTR-009 - Record Training Notes

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-PTR-009 |
| Requirement Name | Record Training Notes |
| Functional Module | Personal Training |
| Business Domain | Personal Training |
| Business Capability | Training Documentation |
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
| Business Requirement | BA-08 BR-017 Personal Training Booking |
| Business Rule | BA-02 BR-TRN-009, BR-CUS-009, BR-SEC-009 |
| Business Process | BA-03 BP-PTR-009 Record Training Notes |
| Business Process Flow | BA-04 Section 23 Personal Training Flow |
| Persona | BA-05 Trainer, Reception Staff, Customer, Facility Manager |
| User Journey | BA-06 Section 18 Personal Training Journey |
| Stakeholder | BA-07 Trainer, Reception Staff, Customer, Facility Manager |
| Non-Functional Requirement | BA-09 Section 2.6 Usability, Section 2.10 Auditability, Section 11 Reporting Requirements |
| Assumption / Constraint / Risk | BA-10 BA-ASS-011, BA-RSK-006, BA-RSK-012 |

### Purpose

To enable Training Documentation within Personal Training so Digitize can execute Record Training Notes consistently across Organizations, Facilities, Sites, users, and related operational or commercial services.

### Functional Requirement

The system shall support Record Training Notes as an atomic Personal Training capability, including scoped data capture, business-rule validation, permission enforcement, lifecycle handling, related service synchronization, notification generation, reporting contribution, and immutable audit recording.

### Business Justification

Record Training Notes is required to preserve operational control, revenue accuracy, service continuity, customer trust, and enterprise traceability for Personal Training processes. Without this capability, downstream modules would rely on incomplete, manual, or inconsistent records.

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
- Actor has permission for Record Training Notes.
- Required Personal Training configuration and policies are available.
- Related records required by BA-03 BP-PTR-009 Record Training Notes are available and within authorized scope.

### Trigger

The capability is triggered when Trainer or the System initiates Record Training Notes from Training Notes, a related workflow, a scheduled job, or an approved integration event.

### In Scope

- Capture or retrieve required Personal Training context.
- Validate Organization, Facility, Site, Customer, user, and policy scope where applicable.
- Execute Record Training Notes according to approved business rules.
- Persist the resulting Personal Training Package state or transaction.
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
- Personal Training Package reference
- Customer reference, where applicable
- Effective date and time, where applicable
- Status or action reason, where applicable
- Payment, billing, trainer, session, or subscription reference where applicable
- Actor remarks, where applicable

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Personal Training Package ID | Primary business record reference | Identifier | Yes | System / User | Must exist or be generated within scope | Core reference for Record Training Notes |
| Organization ID | Tenant Organization context | Identifier | Yes | Session / System | Must be Active and authorized | Enforces tenant isolation |
| Facility ID | Facility context | Identifier | Conditional | User / System | Must be Active where applicable | Required for facility-level operations |
| Site ID | Site context | Identifier | Conditional | User / System | Must belong to Facility where applicable | Required for site-level operations |
| Status | Lifecycle or processing state | Enum | Yes | System | Must follow allowed state transitions | Drives UI and downstream access |
| Effective Date | Date when action applies | DateTime | Conditional | User / System | Must satisfy policy | Supports scheduled or immediate actions |
| Reason / Remarks | Business explanation | Text | Conditional | User | Required for governed changes | Stored for audit |

### Main Flow

1. Actor opens Training Notes or the related workflow.
2. The system validates authentication, authorization, tenant scope, and current operating context.
3. The system loads the required Personal Training records, related configuration, and policy controls.
4. Actor enters or confirms the information required to record training notes.
5. The system validates mandatory data, lifecycle status, ownership, eligibility, financial, capacity, schedule, and security rules where applicable.
6. The system executes Record Training Notes and persists the resulting Personal Training Package state or transaction.
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

- Personal Training Package record created, updated, validated, or reported according to the action.
- Lifecycle or processing status updated.
- Related history entry created.
- Business events emitted.
- Notifications generated where configured.
- Audit events recorded.
- Reports or dashboards updated where applicable.

### UI Behaviour

Training Notes shall display scoped context, mandatory fields, lifecycle status, policy warnings, validation results, available actions, confirmation prompts, read-only states, pagination or filters where applicable, and responsive behavior for front-desk and administrative usage.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-PTR-009-001 | Actor must have permission to execute Record Training Notes. | Deny request and audit. | Critical |
| VAL-PTR-009-002 | Record must belong to the authorized Organization scope. | Deny request. | Critical |
| VAL-PTR-009-003 | Mandatory inputs must be complete and valid. | Block submission. | Critical |
| VAL-PTR-009-004 | Lifecycle and policy rules from BA-02 must be satisfied. | Reject or route for approval. | High |
| VAL-PTR-009-005 | Historical and audit records must be preserved. | Roll back or mark for recovery. | Critical |

### Business Rules

- BA-02 BR-TRN-009
- BA-02 BR-CUS-009
- BA-02 BR-SEC-009

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| ptr.record.training.notes.view | Trainer | Read | View Record Training Notes context |
| ptr.record.training.notes.execute | Trainer | Execute | Execute Record Training Notes |
| ptr.record.training.notes.approve | Organization Administrator | Approve | Approve governed exceptions where configured |
| ptr.record.training.notes.audit.view | Organization Administrator / Support Executive | Read | View audit trace |

### Security Considerations

The capability shall enforce authentication, role-based authorization, tenant isolation, Organization scope, Facility and Site access boundaries, sensitive data masking, secure references, and immutable audit logging.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Record Training Notes Completed | Primary actor and configured stakeholders | In-App / Email | Action completes | Include reference, status, and effective date where applicable |
| Record Training Notes Requires Approval | Approver | In-App | Approval rule applies | Include safe summary and requested action |
| Record Training Notes Failed | Primary actor | In-App | Validation or processing fails | Include safe failure reason and next action |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| RecordTrainingNotesRequested | Personal Training | Approval Workflow, Audit Service |
| RecordTrainingNotesCompleted | Personal Training | Notification Service, Reporting Service, Audit Service |
| RecordTrainingNotesRejected | Personal Training | Notification Service, Audit Service |

### Audit Events

| Audit Event | Description | Actor | Target Entity | Key Data |
|---|---|---|---|---|
| RECORD_TRAINING_NOTES_REQUESTED | Record Training Notes requested | Trainer | Personal Training Package | Scope, reference, and reason |
| RECORD_TRAINING_NOTES_COMPLETED | Record Training Notes completed | Trainer / System | Personal Training Package | Previous and new state |
| RECORD_TRAINING_NOTES_REJECTED | Record Training Notes rejected | System | Personal Training Package | Rejection reason |

### Reports Generated

- Personal Training Operational Report
- Personal Training History Report
- Personal Training Exception Report
- Executive Dashboard

### Related Screens

- Training Notes
- Personal Training Dashboard
- Personal Training History
- Audit Log Viewer

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/training-sessions/{sessionId}/notes | POST | Authorized token | Execute Record Training Notes | 200 OK or 201 Created with result |
| /api/v1/training-sessions/{sessionId}/notes/history | GET | Authorized token | Retrieve Record Training Notes history | 200 OK with history |
| /api/v1/audit-logs | GET | Authorized token | Retrieve related audit events | 200 OK with scoped audit records |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Personal Training Package | Create / Update / Read | Support Record Training Notes | Governed by Organization scope |
| Personal Training Session | Read / Insert | Support Record Training Notes | Governed by Organization scope |
| Trainer Assignment | Read / Insert | Support Record Training Notes | Governed by Organization scope |
| Training Notes | Read / Insert | Support Record Training Notes | Governed by Organization scope |
| Customer Progress | Read / Insert | Support Record Training Notes | Governed by Organization scope |
| Audit Log | Insert | Record auditable activity | Immutable |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Draft | Record Training Notes initiated | Validated | Trainer | Required data captured |
| Validated | Validation succeeds | Pending Approval | System | BA-02 rules satisfied |
| Pending Approval | Processing completes | Completed | System | Related updates succeed |
| Pending Approval | Approval or policy failure | Rejected | System / Approver | Request rejected |
| Completed | View history | Completed | Authorized user | Read-only historical access |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| PTR-009-001 | Record Training Notes cannot be completed because required information is missing. | Missing mandatory data | Complete required fields |
| PTR-009-002 | You do not have permission to perform this action. | Authorization failure | Request access |
| PTR-009-003 | The selected record is not eligible for this action. | Policy or lifecycle violation | Review record status |
| PTR-009-004 | Record Training Notes could not be completed due to a system or integration error. | Processing failure | Retry or contact support |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Execute Record Training Notes | Given the actor has required permission and valid scope | When the actor submits valid information | Then the system shall complete Record Training Notes successfully |
| Enforce validation | Given mandatory data or policy conditions are invalid | When the action is submitted | Then the system shall reject the request with a clear message |
| Preserve audit | Given the action completes or fails | When processing ends | Then audit events shall record actor, timestamp, scope, and outcome |
| Protect scope | Given the selected record is outside authorized scope | When the action is requested | Then the system shall deny access |

### Dependencies

- Trainer Management
- Customer Management
- Attendance Management
- Billing Management
- Payment Management
- Notification Management
- Reporting Service

### Operational Considerations

Record Training Notes should be designed for high-volume operational use, retry-safe processing, clear exception handling, and support-team diagnostics without exposing sensitive data.

### Non-Functional Considerations

This requirement shall satisfy Digitize non-functional expectations for availability, reliability, performance, scalability, security, configurability, maintainability, and auditability.

### Assumptions

- Required master data and configuration are maintained by authorized users.
- Related services expose stable APIs for validation and synchronization.
- Organization policies define approval, retention, notification, and exception behavior.

### Success Criteria

Record Training Notes is completed accurately, securely, and audibly, with downstream records synchronized and no loss of historical traceability.

### Related Functional Requirements

- FR-PTR-001 - Create Personal Training Package
- FR-PTR-002 - Configure Training Package
- FR-PTR-003 - Assign Trainer
- FR-PTR-004 - Book Personal Training Session
- FR-AUD-001 - Record Audit Events

### Notes

Record Training Notes shall remain aligned with the approved BA source documents and shall not introduce behavior that bypasses tenant isolation, lifecycle governance, financial controls, or auditability.

---

## FR-PTR-010 - Record Customer Progress

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-PTR-010 |
| Requirement Name | Record Customer Progress |
| Functional Module | Personal Training |
| Business Domain | Personal Training |
| Business Capability | Progress Monitoring |
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
| Business Requirement | BA-08 BR-017 Personal Training Booking |
| Business Rule | BA-02 BR-TRN-009, BR-CUS-009, BR-SEC-009 |
| Business Process | BA-03 BP-PTR-010 Record Customer Progress |
| Business Process Flow | BA-04 Section 23 Personal Training Flow |
| Persona | BA-05 Trainer, Reception Staff, Customer, Facility Manager |
| User Journey | BA-06 Section 18 Personal Training Journey |
| Stakeholder | BA-07 Trainer, Reception Staff, Customer, Facility Manager |
| Non-Functional Requirement | BA-09 Section 2.6 Usability, Section 2.10 Auditability, Section 11 Reporting Requirements |
| Assumption / Constraint / Risk | BA-10 BA-ASS-011, BA-RSK-006, BA-RSK-012 |

### Purpose

To enable Progress Monitoring within Personal Training so Digitize can execute Record Customer Progress consistently across Organizations, Facilities, Sites, users, and related operational or commercial services.

### Functional Requirement

The system shall support Record Customer Progress as an atomic Personal Training capability, including scoped data capture, business-rule validation, permission enforcement, lifecycle handling, related service synchronization, notification generation, reporting contribution, and immutable audit recording.

### Business Justification

Record Customer Progress is required to preserve operational control, revenue accuracy, service continuity, customer trust, and enterprise traceability for Personal Training processes. Without this capability, downstream modules would rely on incomplete, manual, or inconsistent records.

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
- Actor has permission for Record Customer Progress.
- Required Personal Training configuration and policies are available.
- Related records required by BA-03 BP-PTR-010 Record Customer Progress are available and within authorized scope.

### Trigger

The capability is triggered when Trainer or the System initiates Record Customer Progress from Customer Progress, a related workflow, a scheduled job, or an approved integration event.

### In Scope

- Capture or retrieve required Personal Training context.
- Validate Organization, Facility, Site, Customer, user, and policy scope where applicable.
- Execute Record Customer Progress according to approved business rules.
- Persist the resulting Personal Training Package state or transaction.
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
- Personal Training Package reference
- Customer reference, where applicable
- Effective date and time, where applicable
- Status or action reason, where applicable
- Payment, billing, trainer, session, or subscription reference where applicable
- Actor remarks, where applicable

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Personal Training Package ID | Primary business record reference | Identifier | Yes | System / User | Must exist or be generated within scope | Core reference for Record Customer Progress |
| Organization ID | Tenant Organization context | Identifier | Yes | Session / System | Must be Active and authorized | Enforces tenant isolation |
| Facility ID | Facility context | Identifier | Conditional | User / System | Must be Active where applicable | Required for facility-level operations |
| Site ID | Site context | Identifier | Conditional | User / System | Must belong to Facility where applicable | Required for site-level operations |
| Status | Lifecycle or processing state | Enum | Yes | System | Must follow allowed state transitions | Drives UI and downstream access |
| Effective Date | Date when action applies | DateTime | Conditional | User / System | Must satisfy policy | Supports scheduled or immediate actions |
| Reason / Remarks | Business explanation | Text | Conditional | User | Required for governed changes | Stored for audit |

### Main Flow

1. Actor opens Customer Progress or the related workflow.
2. The system validates authentication, authorization, tenant scope, and current operating context.
3. The system loads the required Personal Training records, related configuration, and policy controls.
4. Actor enters or confirms the information required to record customer progress.
5. The system validates mandatory data, lifecycle status, ownership, eligibility, financial, capacity, schedule, and security rules where applicable.
6. The system executes Record Customer Progress and persists the resulting Personal Training Package state or transaction.
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

- Personal Training Package record created, updated, validated, or reported according to the action.
- Lifecycle or processing status updated.
- Related history entry created.
- Business events emitted.
- Notifications generated where configured.
- Audit events recorded.
- Reports or dashboards updated where applicable.

### UI Behaviour

Customer Progress shall display scoped context, mandatory fields, lifecycle status, policy warnings, validation results, available actions, confirmation prompts, read-only states, pagination or filters where applicable, and responsive behavior for front-desk and administrative usage.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-PTR-010-001 | Actor must have permission to execute Record Customer Progress. | Deny request and audit. | Critical |
| VAL-PTR-010-002 | Record must belong to the authorized Organization scope. | Deny request. | Critical |
| VAL-PTR-010-003 | Mandatory inputs must be complete and valid. | Block submission. | Critical |
| VAL-PTR-010-004 | Lifecycle and policy rules from BA-02 must be satisfied. | Reject or route for approval. | High |
| VAL-PTR-010-005 | Historical and audit records must be preserved. | Roll back or mark for recovery. | Critical |

### Business Rules

- BA-02 BR-TRN-009
- BA-02 BR-CUS-009
- BA-02 BR-SEC-009

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| ptr.record.customer.progress.view | Trainer | Read | View Record Customer Progress context |
| ptr.record.customer.progress.execute | Trainer | Execute | Execute Record Customer Progress |
| ptr.record.customer.progress.approve | Organization Administrator | Approve | Approve governed exceptions where configured |
| ptr.record.customer.progress.audit.view | Organization Administrator / Support Executive | Read | View audit trace |

### Security Considerations

The capability shall enforce authentication, role-based authorization, tenant isolation, Organization scope, Facility and Site access boundaries, sensitive data masking, secure references, and immutable audit logging.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Record Customer Progress Completed | Primary actor and configured stakeholders | In-App / Email | Action completes | Include reference, status, and effective date where applicable |
| Record Customer Progress Requires Approval | Approver | In-App | Approval rule applies | Include safe summary and requested action |
| Record Customer Progress Failed | Primary actor | In-App | Validation or processing fails | Include safe failure reason and next action |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| RecordCustomerProgressRequested | Personal Training | Approval Workflow, Audit Service |
| RecordCustomerProgressCompleted | Personal Training | Notification Service, Reporting Service, Audit Service |
| RecordCustomerProgressRejected | Personal Training | Notification Service, Audit Service |

### Audit Events

| Audit Event | Description | Actor | Target Entity | Key Data |
|---|---|---|---|---|
| RECORD_CUSTOMER_PROGRESS_REQUESTED | Record Customer Progress requested | Trainer | Personal Training Package | Scope, reference, and reason |
| RECORD_CUSTOMER_PROGRESS_COMPLETED | Record Customer Progress completed | Trainer / System | Personal Training Package | Previous and new state |
| RECORD_CUSTOMER_PROGRESS_REJECTED | Record Customer Progress rejected | System | Personal Training Package | Rejection reason |

### Reports Generated

- Personal Training Operational Report
- Personal Training History Report
- Personal Training Exception Report
- Executive Dashboard

### Related Screens

- Customer Progress
- Personal Training Dashboard
- Personal Training History
- Audit Log Viewer

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/personal-training/progress | POST | Authorized token | Execute Record Customer Progress | 200 OK or 201 Created with result |
| /api/v1/personal-training/progress/history | GET | Authorized token | Retrieve Record Customer Progress history | 200 OK with history |
| /api/v1/audit-logs | GET | Authorized token | Retrieve related audit events | 200 OK with scoped audit records |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Personal Training Package | Create / Update / Read | Support Record Customer Progress | Governed by Organization scope |
| Personal Training Session | Read / Insert | Support Record Customer Progress | Governed by Organization scope |
| Trainer Assignment | Read / Insert | Support Record Customer Progress | Governed by Organization scope |
| Training Notes | Read / Insert | Support Record Customer Progress | Governed by Organization scope |
| Customer Progress | Read / Insert | Support Record Customer Progress | Governed by Organization scope |
| Audit Log | Insert | Record auditable activity | Immutable |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Draft | Record Customer Progress initiated | Validated | Trainer | Required data captured |
| Validated | Validation succeeds | Pending Approval | System | BA-02 rules satisfied |
| Pending Approval | Processing completes | Completed | System | Related updates succeed |
| Pending Approval | Approval or policy failure | Rejected | System / Approver | Request rejected |
| Completed | View history | Completed | Authorized user | Read-only historical access |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| PTR-010-001 | Record Customer Progress cannot be completed because required information is missing. | Missing mandatory data | Complete required fields |
| PTR-010-002 | You do not have permission to perform this action. | Authorization failure | Request access |
| PTR-010-003 | The selected record is not eligible for this action. | Policy or lifecycle violation | Review record status |
| PTR-010-004 | Record Customer Progress could not be completed due to a system or integration error. | Processing failure | Retry or contact support |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Execute Record Customer Progress | Given the actor has required permission and valid scope | When the actor submits valid information | Then the system shall complete Record Customer Progress successfully |
| Enforce validation | Given mandatory data or policy conditions are invalid | When the action is submitted | Then the system shall reject the request with a clear message |
| Preserve audit | Given the action completes or fails | When processing ends | Then audit events shall record actor, timestamp, scope, and outcome |
| Protect scope | Given the selected record is outside authorized scope | When the action is requested | Then the system shall deny access |

### Dependencies

- Trainer Management
- Customer Management
- Attendance Management
- Billing Management
- Payment Management
- Notification Management
- Reporting Service

### Operational Considerations

Record Customer Progress should be designed for high-volume operational use, retry-safe processing, clear exception handling, and support-team diagnostics without exposing sensitive data.

### Non-Functional Considerations

This requirement shall satisfy Digitize non-functional expectations for availability, reliability, performance, scalability, security, configurability, maintainability, and auditability.

### Assumptions

- Required master data and configuration are maintained by authorized users.
- Related services expose stable APIs for validation and synchronization.
- Organization policies define approval, retention, notification, and exception behavior.

### Success Criteria

Record Customer Progress is completed accurately, securely, and audibly, with downstream records synchronized and no loss of historical traceability.

### Related Functional Requirements

- FR-PTR-001 - Create Personal Training Package
- FR-PTR-002 - Configure Training Package
- FR-PTR-003 - Assign Trainer
- FR-PTR-004 - Book Personal Training Session
- FR-AUD-001 - Record Audit Events

### Notes

Record Customer Progress shall remain aligned with the approved BA source documents and shall not introduce behavior that bypasses tenant isolation, lifecycle governance, financial controls, or auditability.

---

## FR-PTR-011 - View Training History

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-PTR-011 |
| Requirement Name | View Training History |
| Functional Module | Personal Training |
| Business Domain | Personal Training |
| Business Capability | Training History |
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
| Business Requirement | BA-08 BR-017 Personal Training Booking |
| Business Rule | BA-02 BR-TRN-009, BR-CUS-009, BR-AUD-008, BR-SEC-004 |
| Business Process | BA-03 BP-PTR-011 View Training History |
| Business Process Flow | BA-04 Section 23 Personal Training Flow |
| Persona | BA-05 Trainer, Reception Staff, Customer, Facility Manager |
| User Journey | BA-06 Section 18 Personal Training Journey |
| Stakeholder | BA-07 Trainer, Reception Staff, Customer, Facility Manager |
| Non-Functional Requirement | BA-09 Section 2.6 Usability, Section 2.10 Auditability, Section 11 Reporting Requirements |
| Assumption / Constraint / Risk | BA-10 BA-ASS-011, BA-RSK-006, BA-RSK-012 |

### Purpose

To enable Training History within Personal Training so Digitize can execute View Training History consistently across Organizations, Facilities, Sites, users, and related operational or commercial services.

### Functional Requirement

The system shall support View Training History as an atomic Personal Training capability, including scoped data capture, business-rule validation, permission enforcement, lifecycle handling, related service synchronization, notification generation, reporting contribution, and immutable audit recording.

### Business Justification

View Training History is required to preserve operational control, revenue accuracy, service continuity, customer trust, and enterprise traceability for Personal Training processes. Without this capability, downstream modules would rely on incomplete, manual, or inconsistent records.

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
- Actor has permission for View Training History.
- Required Personal Training configuration and policies are available.
- Related records required by BA-03 BP-PTR-011 View Training History are available and within authorized scope.

### Trigger

The capability is triggered when Trainer or the System initiates View Training History from Training History, a related workflow, a scheduled job, or an approved integration event.

### In Scope

- Capture or retrieve required Personal Training context.
- Validate Organization, Facility, Site, Customer, user, and policy scope where applicable.
- Execute View Training History according to approved business rules.
- Persist the resulting Personal Training Package state or transaction.
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
- Personal Training Package reference
- Customer reference, where applicable
- Effective date and time, where applicable
- Status or action reason, where applicable
- Payment, billing, trainer, session, or subscription reference where applicable
- Actor remarks, where applicable

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Personal Training Package ID | Primary business record reference | Identifier | Yes | System / User | Must exist or be generated within scope | Core reference for View Training History |
| Organization ID | Tenant Organization context | Identifier | Yes | Session / System | Must be Active and authorized | Enforces tenant isolation |
| Facility ID | Facility context | Identifier | Conditional | User / System | Must be Active where applicable | Required for facility-level operations |
| Site ID | Site context | Identifier | Conditional | User / System | Must belong to Facility where applicable | Required for site-level operations |
| Status | Lifecycle or processing state | Enum | Yes | System | Must follow allowed state transitions | Drives UI and downstream access |
| Effective Date | Date when action applies | DateTime | Conditional | User / System | Must satisfy policy | Supports scheduled or immediate actions |
| Reason / Remarks | Business explanation | Text | Conditional | User | Required for governed changes | Stored for audit |

### Main Flow

1. Actor opens Training History or the related workflow.
2. The system validates authentication, authorization, tenant scope, and current operating context.
3. The system loads the required Personal Training records, related configuration, and policy controls.
4. Actor enters or confirms the information required to view training history.
5. The system validates mandatory data, lifecycle status, ownership, eligibility, financial, capacity, schedule, and security rules where applicable.
6. The system executes View Training History and persists the resulting Personal Training Package state or transaction.
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

- Personal Training Package record created, updated, validated, or reported according to the action.
- Lifecycle or processing status updated.
- Related history entry created.
- Business events emitted.
- Notifications generated where configured.
- Audit events recorded.
- Reports or dashboards updated where applicable.

### UI Behaviour

Training History shall display scoped context, mandatory fields, lifecycle status, policy warnings, validation results, available actions, confirmation prompts, read-only states, pagination or filters where applicable, and responsive behavior for front-desk and administrative usage.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-PTR-011-001 | Actor must have permission to execute View Training History. | Deny request and audit. | Critical |
| VAL-PTR-011-002 | Record must belong to the authorized Organization scope. | Deny request. | Critical |
| VAL-PTR-011-003 | Mandatory inputs must be complete and valid. | Block submission. | Critical |
| VAL-PTR-011-004 | Lifecycle and policy rules from BA-02 must be satisfied. | Reject or route for approval. | High |
| VAL-PTR-011-005 | Historical and audit records must be preserved. | Roll back or mark for recovery. | Critical |

### Business Rules

- BA-02 BR-TRN-009
- BA-02 BR-CUS-009
- BA-02 BR-AUD-008
- BA-02 BR-SEC-004

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| ptr.view.training.history.view | Trainer | Read | View View Training History context |
| ptr.view.training.history.execute | Trainer | Execute | Execute View Training History |
| ptr.view.training.history.approve | Organization Administrator | Approve | Approve governed exceptions where configured |
| ptr.view.training.history.audit.view | Organization Administrator / Support Executive | Read | View audit trace |

### Security Considerations

The capability shall enforce authentication, role-based authorization, tenant isolation, Organization scope, Facility and Site access boundaries, sensitive data masking, secure references, and immutable audit logging.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| View Training History Completed | Primary actor and configured stakeholders | In-App / Email | Action completes | Include reference, status, and effective date where applicable |
| View Training History Requires Approval | Approver | In-App | Approval rule applies | Include safe summary and requested action |
| View Training History Failed | Primary actor | In-App | Validation or processing fails | Include safe failure reason and next action |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| ViewTrainingHistoryRequested | Personal Training | Approval Workflow, Audit Service |
| ViewTrainingHistoryCompleted | Personal Training | Notification Service, Reporting Service, Audit Service |
| ViewTrainingHistoryRejected | Personal Training | Notification Service, Audit Service |

### Audit Events

| Audit Event | Description | Actor | Target Entity | Key Data |
|---|---|---|---|---|
| VIEW_TRAINING_HISTORY_REQUESTED | View Training History requested | Trainer | Personal Training Package | Scope, reference, and reason |
| VIEW_TRAINING_HISTORY_COMPLETED | View Training History completed | Trainer / System | Personal Training Package | Previous and new state |
| VIEW_TRAINING_HISTORY_REJECTED | View Training History rejected | System | Personal Training Package | Rejection reason |

### Reports Generated

- Personal Training Operational Report
- Personal Training History Report
- Personal Training Exception Report
- Executive Dashboard

### Related Screens

- Training History
- Personal Training Dashboard
- Personal Training History
- Audit Log Viewer

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/personal-training/history | GET | Authorized token | Execute View Training History | 200 OK or 201 Created with result |
| /api/v1/personal-training/history/history | GET | Authorized token | Retrieve View Training History history | 200 OK with history |
| /api/v1/audit-logs | GET | Authorized token | Retrieve related audit events | 200 OK with scoped audit records |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Personal Training Package | Read | Support View Training History | Governed by Organization scope |
| Personal Training Session | Read / Insert | Support View Training History | Governed by Organization scope |
| Trainer Assignment | Read / Insert | Support View Training History | Governed by Organization scope |
| Training Notes | Read / Insert | Support View Training History | Governed by Organization scope |
| Customer Progress | Read / Insert | Support View Training History | Governed by Organization scope |
| Audit Log | Insert | Record auditable activity | Immutable |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Not Requested | View Training History initiated | Generating | Trainer | Required data captured |
| Generating | Validation succeeds | Ready | System | BA-02 rules satisfied |
| Ready | Processing completes | Export Pending | System | Related updates succeed |
| Ready | Approval or policy failure | Failed | System / Approver | Request rejected |
| Export Pending | View history | Export Pending | Authorized user | Read-only historical access |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| PTR-011-001 | View Training History cannot be completed because required information is missing. | Missing mandatory data | Complete required fields |
| PTR-011-002 | You do not have permission to perform this action. | Authorization failure | Request access |
| PTR-011-003 | The selected record is not eligible for this action. | Policy or lifecycle violation | Review record status |
| PTR-011-004 | View Training History could not be completed due to a system or integration error. | Processing failure | Retry or contact support |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Execute View Training History | Given the actor has required permission and valid scope | When the actor submits valid information | Then the system shall complete View Training History successfully |
| Enforce validation | Given mandatory data or policy conditions are invalid | When the action is submitted | Then the system shall reject the request with a clear message |
| Preserve audit | Given the action completes or fails | When processing ends | Then audit events shall record actor, timestamp, scope, and outcome |
| Protect scope | Given the selected record is outside authorized scope | When the action is requested | Then the system shall deny access |

### Dependencies

- Trainer Management
- Customer Management
- Attendance Management
- Billing Management
- Payment Management
- Notification Management
- Reporting Service

### Operational Considerations

View Training History should be designed for high-volume operational use, retry-safe processing, clear exception handling, and support-team diagnostics without exposing sensitive data.

### Non-Functional Considerations

This requirement shall satisfy Digitize non-functional expectations for availability, reliability, performance, scalability, security, configurability, maintainability, and auditability.

### Assumptions

- Required master data and configuration are maintained by authorized users.
- Related services expose stable APIs for validation and synchronization.
- Organization policies define approval, retention, notification, and exception behavior.

### Success Criteria

View Training History is completed accurately, securely, and audibly, with downstream records synchronized and no loss of historical traceability.

### Related Functional Requirements

- FR-PTR-001 - Create Personal Training Package
- FR-PTR-002 - Configure Training Package
- FR-PTR-003 - Assign Trainer
- FR-PTR-004 - Book Personal Training Session
- FR-AUD-001 - Record Audit Events

### Notes

View Training History shall remain aligned with the approved BA source documents and shall not introduce behavior that bypasses tenant isolation, lifecycle governance, financial controls, or auditability.

---

## FR-PTR-012 - Generate Trainer Performance Report

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-PTR-012 |
| Requirement Name | Generate Trainer Performance Report |
| Functional Module | Personal Training |
| Business Domain | Personal Training |
| Business Capability | Performance Analytics |
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
| Business Requirement | BA-08 BR-017 Personal Training Booking |
| Business Rule | BA-02 BR-TRN-003, BR-TRN-007, BR-TRN-009 |
| Business Process | BA-03 BP-PTR-012 Generate Trainer Performance Report |
| Business Process Flow | BA-04 Section 23 Personal Training Flow |
| Persona | BA-05 Trainer, Reception Staff, Customer, Facility Manager |
| User Journey | BA-06 Section 18 Personal Training Journey |
| Stakeholder | BA-07 Trainer, Reception Staff, Customer, Facility Manager |
| Non-Functional Requirement | BA-09 Section 2.6 Usability, Section 2.10 Auditability, Section 11 Reporting Requirements |
| Assumption / Constraint / Risk | BA-10 BA-ASS-011, BA-RSK-006, BA-RSK-012 |

### Purpose

To enable Performance Analytics within Personal Training so Digitize can execute Generate Trainer Performance Report consistently across Organizations, Facilities, Sites, users, and related operational or commercial services.

### Functional Requirement

The system shall support Generate Trainer Performance Report as an atomic Personal Training capability, including scoped data capture, business-rule validation, permission enforcement, lifecycle handling, related service synchronization, notification generation, reporting contribution, and immutable audit recording.

### Business Justification

Generate Trainer Performance Report is required to preserve operational control, revenue accuracy, service continuity, customer trust, and enterprise traceability for Personal Training processes. Without this capability, downstream modules would rely on incomplete, manual, or inconsistent records.

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
- Actor has permission for Generate Trainer Performance Report.
- Required Personal Training configuration and policies are available.
- Related records required by BA-03 BP-PTR-012 Generate Trainer Performance Report are available and within authorized scope.

### Trigger

The capability is triggered when Facility Manager or the System initiates Generate Trainer Performance Report from Trainer Performance Report, a related workflow, a scheduled job, or an approved integration event.

### In Scope

- Capture or retrieve required Personal Training context.
- Validate Organization, Facility, Site, Customer, user, and policy scope where applicable.
- Execute Generate Trainer Performance Report according to approved business rules.
- Persist the resulting Personal Training Package state or transaction.
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
- Personal Training Package reference
- Customer reference, where applicable
- Effective date and time, where applicable
- Status or action reason, where applicable
- Payment, billing, trainer, session, or subscription reference where applicable
- Actor remarks, where applicable

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Personal Training Package ID | Primary business record reference | Identifier | Yes | System / User | Must exist or be generated within scope | Core reference for Generate Trainer Performance Report |
| Organization ID | Tenant Organization context | Identifier | Yes | Session / System | Must be Active and authorized | Enforces tenant isolation |
| Facility ID | Facility context | Identifier | Conditional | User / System | Must be Active where applicable | Required for facility-level operations |
| Site ID | Site context | Identifier | Conditional | User / System | Must belong to Facility where applicable | Required for site-level operations |
| Status | Lifecycle or processing state | Enum | Yes | System | Must follow allowed state transitions | Drives UI and downstream access |
| Effective Date | Date when action applies | DateTime | Conditional | User / System | Must satisfy policy | Supports scheduled or immediate actions |
| Reason / Remarks | Business explanation | Text | Conditional | User | Required for governed changes | Stored for audit |

### Main Flow

1. Actor opens Trainer Performance Report or the related workflow.
2. The system validates authentication, authorization, tenant scope, and current operating context.
3. The system loads the required Personal Training records, related configuration, and policy controls.
4. Actor enters or confirms the information required to generate trainer performance report.
5. The system validates mandatory data, lifecycle status, ownership, eligibility, financial, capacity, schedule, and security rules where applicable.
6. The system executes Generate Trainer Performance Report and persists the resulting Personal Training Package state or transaction.
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

- Personal Training Package record created, updated, validated, or reported according to the action.
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
| VAL-PTR-012-001 | Actor must have permission to execute Generate Trainer Performance Report. | Deny request and audit. | Critical |
| VAL-PTR-012-002 | Record must belong to the authorized Organization scope. | Deny request. | Critical |
| VAL-PTR-012-003 | Mandatory inputs must be complete and valid. | Block submission. | Critical |
| VAL-PTR-012-004 | Lifecycle and policy rules from BA-02 must be satisfied. | Reject or route for approval. | High |
| VAL-PTR-012-005 | Historical and audit records must be preserved. | Roll back or mark for recovery. | Critical |

### Business Rules

- BA-02 BR-TRN-003
- BA-02 BR-TRN-007
- BA-02 BR-TRN-009

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| ptr.generate.trainer.performance.report.view | Facility Manager | Read | View Generate Trainer Performance Report context |
| ptr.generate.trainer.performance.report.execute | Facility Manager | Execute | Execute Generate Trainer Performance Report |
| ptr.generate.trainer.performance.report.approve | Organization Administrator | Approve | Approve governed exceptions where configured |
| ptr.generate.trainer.performance.report.audit.view | Organization Administrator / Support Executive | Read | View audit trace |

### Security Considerations

The capability shall enforce authentication, role-based authorization, tenant isolation, Organization scope, Facility and Site access boundaries, sensitive data masking, secure references, and immutable audit logging.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Generate Trainer Performance Report Completed | Primary actor and configured stakeholders | In-App / Email | Action completes | Include reference, status, and effective date where applicable |
| Generate Trainer Performance Report Requires Approval | Approver | In-App | Approval rule applies | Include safe summary and requested action |
| Generate Trainer Performance Report Failed | Primary actor | In-App | Validation or processing fails | Include safe failure reason and next action |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| GenerateTrainerPerformanceReportRequested | Personal Training | Approval Workflow, Audit Service |
| GenerateTrainerPerformanceReportCompleted | Personal Training | Notification Service, Reporting Service, Audit Service |
| GenerateTrainerPerformanceReportRejected | Personal Training | Notification Service, Audit Service |

### Audit Events

| Audit Event | Description | Actor | Target Entity | Key Data |
|---|---|---|---|---|
| GENERATE_TRAINER_PERFORMANCE_REPORT_REQUESTED | Generate Trainer Performance Report requested | Facility Manager | Personal Training Package | Scope, reference, and reason |
| GENERATE_TRAINER_PERFORMANCE_REPORT_COMPLETED | Generate Trainer Performance Report completed | Facility Manager / System | Personal Training Package | Previous and new state |
| GENERATE_TRAINER_PERFORMANCE_REPORT_REJECTED | Generate Trainer Performance Report rejected | System | Personal Training Package | Rejection reason |

### Reports Generated

- Personal Training Operational Report
- Personal Training History Report
- Personal Training Exception Report
- Executive Dashboard

### Related Screens

- Trainer Performance Report
- Personal Training Dashboard
- Personal Training History
- Audit Log Viewer

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/reports/personal-training/trainer-performance | GET | Authorized token | Execute Generate Trainer Performance Report | 200 OK or 201 Created with result |
| /api/v1/reports/personal-training/trainer-performance/history | GET | Authorized token | Retrieve Generate Trainer Performance Report history | 200 OK with history |
| /api/v1/audit-logs | GET | Authorized token | Retrieve related audit events | 200 OK with scoped audit records |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Personal Training Package | Read | Support Generate Trainer Performance Report | Governed by Organization scope |
| Personal Training Session | Read / Insert | Support Generate Trainer Performance Report | Governed by Organization scope |
| Trainer Assignment | Read / Insert | Support Generate Trainer Performance Report | Governed by Organization scope |
| Training Notes | Read / Insert | Support Generate Trainer Performance Report | Governed by Organization scope |
| Customer Progress | Read / Insert | Support Generate Trainer Performance Report | Governed by Organization scope |
| Audit Log | Insert | Record auditable activity | Immutable |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Not Requested | Generate Trainer Performance Report initiated | Generating | Facility Manager | Required data captured |
| Generating | Validation succeeds | Ready | System | BA-02 rules satisfied |
| Ready | Processing completes | Export Pending | System | Related updates succeed |
| Ready | Approval or policy failure | Failed | System / Approver | Request rejected |
| Export Pending | View history | Export Pending | Authorized user | Read-only historical access |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| PTR-012-001 | Generate Trainer Performance Report cannot be completed because required information is missing. | Missing mandatory data | Complete required fields |
| PTR-012-002 | You do not have permission to perform this action. | Authorization failure | Request access |
| PTR-012-003 | The selected record is not eligible for this action. | Policy or lifecycle violation | Review record status |
| PTR-012-004 | Generate Trainer Performance Report could not be completed due to a system or integration error. | Processing failure | Retry or contact support |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Execute Generate Trainer Performance Report | Given the actor has required permission and valid scope | When the actor submits valid information | Then the system shall complete Generate Trainer Performance Report successfully |
| Enforce validation | Given mandatory data or policy conditions are invalid | When the action is submitted | Then the system shall reject the request with a clear message |
| Preserve audit | Given the action completes or fails | When processing ends | Then audit events shall record actor, timestamp, scope, and outcome |
| Protect scope | Given the selected record is outside authorized scope | When the action is requested | Then the system shall deny access |

### Dependencies

- Trainer Management
- Customer Management
- Attendance Management
- Billing Management
- Payment Management
- Notification Management
- Reporting Service

### Operational Considerations

Generate Trainer Performance Report should be designed for high-volume operational use, retry-safe processing, clear exception handling, and support-team diagnostics without exposing sensitive data.

### Non-Functional Considerations

This requirement shall satisfy Digitize non-functional expectations for availability, reliability, performance, scalability, security, configurability, maintainability, and auditability.

### Assumptions

- Required master data and configuration are maintained by authorized users.
- Related services expose stable APIs for validation and synchronization.
- Organization policies define approval, retention, notification, and exception behavior.

### Success Criteria

Generate Trainer Performance Report is completed accurately, securely, and audibly, with downstream records synchronized and no loss of historical traceability.

### Related Functional Requirements

- FR-PTR-001 - Create Personal Training Package
- FR-PTR-002 - Configure Training Package
- FR-PTR-003 - Assign Trainer
- FR-PTR-004 - Book Personal Training Session
- FR-AUD-001 - Record Audit Events

### Notes

Generate Trainer Performance Report shall remain aligned with the approved BA source documents and shall not introduce behavior that bypasses tenant isolation, lifecycle governance, financial controls, or auditability.

---

**End of FR-12 - Personal Training**
