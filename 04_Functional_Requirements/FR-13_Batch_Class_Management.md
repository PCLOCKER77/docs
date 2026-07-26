# FR-13 Batch / Class Management

**Document ID:** FR-13  
**Document Name:** Batch / Class Management Functional Requirements  
**Company:** OreeOn Technologies Pvt. Ltd.  
**Product:** Digitize  
**Document Type:** Functional Requirements  
**Version:** 1.0  
**Status:** Draft  
**Owner:** Product Management  
**Prepared By:** Product Management, Business Analysis, and Solution Architecture  
**Last Updated:** July 2026

---

## FR-BAT-001 - Create Activity

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-BAT-001 |
| Requirement Name | Create Activity |
| Functional Module | Batch / Class Management |
| Business Domain | Activity & Batch |
| Business Capability | Activity Management |
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
| Business Requirement | BA-08 BR-015 Activity Configuration |
| Business Rule | BA-02 BR-ORG-004, BR-FAC-004, BR-SEC-004 |
| Business Process | BA-03 BP-ACT-001 Create Activity |
| Business Process Flow | BA-04 Section 21 Activity Management Flow, Section 22 Batch Management Flow |
| Persona | BA-05 Facility Manager, Trainer, Reception Staff, Customer |
| User Journey | BA-06 Section 5 Facility Manager Journey, Section 8 Trainer Journey, Section 17 Attendance Journey |
| Stakeholder | BA-07 Facility Manager, Trainer, Reception Staff, Customer |
| Non-Functional Requirement | BA-09 Section 2.8 Configurability, Section 2.4 Performance, Section 2.10 Auditability |
| Assumption / Constraint / Risk | BA-10 BA-ASS-011, BA-RSK-006 |

### Purpose

To enable Activity Management within Batch / Class Management so Digitize can execute Create Activity consistently across Organizations, Facilities, Sites, users, and related operational or commercial services.

### Functional Requirement

The system shall support Create Activity as an atomic Batch / Class Management capability, including scoped data capture, business-rule validation, permission enforcement, lifecycle handling, related service synchronization, notification generation, reporting contribution, and immutable audit recording.

### Business Justification

Create Activity is required to preserve operational control, revenue accuracy, service continuity, customer trust, and enterprise traceability for Activity & Batch processes. Without this capability, downstream modules would rely on incomplete, manual, or inconsistent records.

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
- Actor has permission for Create Activity.
- Required Activity & Batch configuration and policies are available.
- Related records required by BA-03 BP-ACT-001 Create Activity are available and within authorized scope.

### Trigger

The capability is triggered when Organization Administrator or the System initiates Create Activity from Activity Management, a related workflow, a scheduled job, or an approved integration event.

### In Scope

- Capture or retrieve required Activity & Batch context.
- Validate Organization, Facility, Site, Customer, user, and policy scope where applicable.
- Execute Create Activity according to approved business rules.
- Persist the resulting Activity state or transaction.
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
- Activity reference
- Customer reference, where applicable
- Effective date and time, where applicable
- Status or action reason, where applicable
- Payment, billing, trainer, session, or subscription reference where applicable
- Actor remarks, where applicable

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Activity ID | Primary business record reference | Identifier | Yes | System / User | Must exist or be generated within scope | Core reference for Create Activity |
| Organization ID | Tenant Organization context | Identifier | Yes | Session / System | Must be Active and authorized | Enforces tenant isolation |
| Facility ID | Facility context | Identifier | Conditional | User / System | Must be Active where applicable | Required for facility-level operations |
| Site ID | Site context | Identifier | Conditional | User / System | Must belong to Facility where applicable | Required for site-level operations |
| Status | Lifecycle or processing state | Enum | Yes | System | Must follow allowed state transitions | Drives UI and downstream access |
| Effective Date | Date when action applies | DateTime | Conditional | User / System | Must satisfy policy | Supports scheduled or immediate actions |
| Reason / Remarks | Business explanation | Text | Conditional | User | Required for governed changes | Stored for audit |

### Main Flow

1. Actor opens Activity Management or the related workflow.
2. The system validates authentication, authorization, tenant scope, and current operating context.
3. The system loads the required Activity & Batch records, related configuration, and policy controls.
4. Actor enters or confirms the information required to create activity.
5. The system validates mandatory data, lifecycle status, ownership, eligibility, financial, capacity, schedule, and security rules where applicable.
6. The system executes Create Activity and persists the resulting Activity state or transaction.
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

- Activity record created, updated, validated, or reported according to the action.
- Lifecycle or processing status updated.
- Related history entry created.
- Business events emitted.
- Notifications generated where configured.
- Audit events recorded.
- Reports or dashboards updated where applicable.

### UI Behaviour

Activity Management shall display scoped context, mandatory fields, lifecycle status, policy warnings, validation results, available actions, confirmation prompts, read-only states, pagination or filters where applicable, and responsive behavior for front-desk and administrative usage.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-BAT-001-001 | Actor must have permission to execute Create Activity. | Deny request and audit. | Critical |
| VAL-BAT-001-002 | Record must belong to the authorized Organization scope. | Deny request. | Critical |
| VAL-BAT-001-003 | Mandatory inputs must be complete and valid. | Block submission. | Critical |
| VAL-BAT-001-004 | Lifecycle and policy rules from BA-02 must be satisfied. | Reject or route for approval. | High |
| VAL-BAT-001-005 | Historical and audit records must be preserved. | Roll back or mark for recovery. | Critical |

### Business Rules

- BA-02 BR-ORG-004
- BA-02 BR-FAC-004
- BA-02 BR-SEC-004

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| bat.create.activity.view | Organization Administrator | Read | View Create Activity context |
| bat.create.activity.execute | Organization Administrator | Execute | Execute Create Activity |
| bat.create.activity.approve | Organization Administrator | Approve | Approve governed exceptions where configured |
| bat.create.activity.audit.view | Organization Administrator / Support Executive | Read | View audit trace |

### Security Considerations

The capability shall enforce authentication, role-based authorization, tenant isolation, Organization scope, Facility and Site access boundaries, sensitive data masking, secure references, and immutable audit logging.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Create Activity Completed | Primary actor and configured stakeholders | In-App / Email | Action completes | Include reference, status, and effective date where applicable |
| Create Activity Requires Approval | Approver | In-App | Approval rule applies | Include safe summary and requested action |
| Create Activity Failed | Primary actor | In-App | Validation or processing fails | Include safe failure reason and next action |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| CreateActivityRequested | Batch / Class Management | Approval Workflow, Audit Service |
| CreateActivityCompleted | Batch / Class Management | Notification Service, Reporting Service, Audit Service |
| CreateActivityRejected | Batch / Class Management | Notification Service, Audit Service |

### Audit Events

| Audit Event | Description | Actor | Target Entity | Key Data |
|---|---|---|---|---|
| CREATE_ACTIVITY_REQUESTED | Create Activity requested | Organization Administrator | Activity | Scope, reference, and reason |
| CREATE_ACTIVITY_COMPLETED | Create Activity completed | Organization Administrator / System | Activity | Previous and new state |
| CREATE_ACTIVITY_REJECTED | Create Activity rejected | System | Activity | Rejection reason |

### Reports Generated

- Batch / Class Management Operational Report
- Batch / Class Management History Report
- Batch / Class Management Exception Report
- Executive Dashboard

### Related Screens

- Activity Management
- Batch / Class Management Dashboard
- Batch / Class Management History
- Audit Log Viewer

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/activities | POST | Authorized token | Execute Create Activity | 200 OK or 201 Created with result |
| /api/v1/activities/history | GET | Authorized token | Retrieve Create Activity history | 200 OK with history |
| /api/v1/audit-logs | GET | Authorized token | Retrieve related audit events | 200 OK with scoped audit records |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Activity | Create / Update / Read | Support Create Activity | Governed by Organization scope |
| Batch | Read / Insert | Support Create Activity | Governed by Organization scope |
| Batch Schedule | Read / Insert | Support Create Activity | Governed by Organization scope |
| Batch Capacity | Read / Insert | Support Create Activity | Governed by Organization scope |
| Trainer Assignment | Read / Insert | Support Create Activity | Governed by Organization scope |
| Audit Log | Insert | Record auditable activity | Immutable |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Draft | Create Activity initiated | Configured | Organization Administrator | Required data captured |
| Configured | Validation succeeds | Active | System | BA-02 rules satisfied |
| Active | Processing completes | Inactive | System | Related updates succeed |
| Active | Approval or policy failure | Archived | System / Approver | Request rejected |
| Inactive | View history | Inactive | Authorized user | Read-only historical access |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| BAT-001-001 | Create Activity cannot be completed because required information is missing. | Missing mandatory data | Complete required fields |
| BAT-001-002 | You do not have permission to perform this action. | Authorization failure | Request access |
| BAT-001-003 | The selected record is not eligible for this action. | Policy or lifecycle violation | Review record status |
| BAT-001-004 | Create Activity could not be completed due to a system or integration error. | Processing failure | Retry or contact support |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Execute Create Activity | Given the actor has required permission and valid scope | When the actor submits valid information | Then the system shall complete Create Activity successfully |
| Enforce validation | Given mandatory data or policy conditions are invalid | When the action is submitted | Then the system shall reject the request with a clear message |
| Preserve audit | Given the action completes or fails | When processing ends | Then audit events shall record actor, timestamp, scope, and outcome |
| Protect scope | Given the selected record is outside authorized scope | When the action is requested | Then the system shall deny access |

### Dependencies

- Facility Management
- Site Management
- Trainer Management
- Customer Management
- Membership Management
- Attendance Management
- Notification Management

### Operational Considerations

Create Activity should be designed for high-volume operational use, retry-safe processing, clear exception handling, and support-team diagnostics without exposing sensitive data.

### Non-Functional Considerations

This requirement shall satisfy Digitize non-functional expectations for availability, reliability, performance, scalability, security, configurability, maintainability, and auditability.

### Assumptions

- Required master data and configuration are maintained by authorized users.
- Related services expose stable APIs for validation and synchronization.
- Organization policies define approval, retention, notification, and exception behavior.

### Success Criteria

Create Activity is completed accurately, securely, and audibly, with downstream records synchronized and no loss of historical traceability.

### Related Functional Requirements

- FR-BAT-002 - Update Activity
- FR-BAT-003 - Configure Activity Rules
- FR-BAT-004 - Create Batch
- FR-BAT-005 - Update Batch
- FR-AUD-001 - Record Audit Events

### Notes

Create Activity shall remain aligned with the approved BA source documents and shall not introduce behavior that bypasses tenant isolation, lifecycle governance, financial controls, or auditability.

---

## FR-BAT-002 - Update Activity

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-BAT-002 |
| Requirement Name | Update Activity |
| Functional Module | Batch / Class Management |
| Business Domain | Activity & Batch |
| Business Capability | Activity Management |
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
| Business Requirement | BA-08 BR-015 Activity Configuration |
| Business Rule | BA-02 BR-ORG-004, BR-FAC-004, BR-AUD-003, BR-SEC-004 |
| Business Process | BA-03 BP-ACT-002 Update Activity |
| Business Process Flow | BA-04 Section 21 Activity Management Flow, Section 22 Batch Management Flow |
| Persona | BA-05 Facility Manager, Trainer, Reception Staff, Customer |
| User Journey | BA-06 Section 5 Facility Manager Journey, Section 8 Trainer Journey, Section 17 Attendance Journey |
| Stakeholder | BA-07 Facility Manager, Trainer, Reception Staff, Customer |
| Non-Functional Requirement | BA-09 Section 2.8 Configurability, Section 2.4 Performance, Section 2.10 Auditability |
| Assumption / Constraint / Risk | BA-10 BA-ASS-011, BA-RSK-006 |

### Purpose

To enable Activity Management within Batch / Class Management so Digitize can execute Update Activity consistently across Organizations, Facilities, Sites, users, and related operational or commercial services.

### Functional Requirement

The system shall support Update Activity as an atomic Batch / Class Management capability, including scoped data capture, business-rule validation, permission enforcement, lifecycle handling, related service synchronization, notification generation, reporting contribution, and immutable audit recording.

### Business Justification

Update Activity is required to preserve operational control, revenue accuracy, service continuity, customer trust, and enterprise traceability for Activity & Batch processes. Without this capability, downstream modules would rely on incomplete, manual, or inconsistent records.

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
- Actor has permission for Update Activity.
- Required Activity & Batch configuration and policies are available.
- Related records required by BA-03 BP-ACT-002 Update Activity are available and within authorized scope.

### Trigger

The capability is triggered when Organization Administrator or the System initiates Update Activity from Activity Management, a related workflow, a scheduled job, or an approved integration event.

### In Scope

- Capture or retrieve required Activity & Batch context.
- Validate Organization, Facility, Site, Customer, user, and policy scope where applicable.
- Execute Update Activity according to approved business rules.
- Persist the resulting Activity state or transaction.
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
- Activity reference
- Customer reference, where applicable
- Effective date and time, where applicable
- Status or action reason, where applicable
- Payment, billing, trainer, session, or subscription reference where applicable
- Actor remarks, where applicable

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Activity ID | Primary business record reference | Identifier | Yes | System / User | Must exist or be generated within scope | Core reference for Update Activity |
| Organization ID | Tenant Organization context | Identifier | Yes | Session / System | Must be Active and authorized | Enforces tenant isolation |
| Facility ID | Facility context | Identifier | Conditional | User / System | Must be Active where applicable | Required for facility-level operations |
| Site ID | Site context | Identifier | Conditional | User / System | Must belong to Facility where applicable | Required for site-level operations |
| Status | Lifecycle or processing state | Enum | Yes | System | Must follow allowed state transitions | Drives UI and downstream access |
| Effective Date | Date when action applies | DateTime | Conditional | User / System | Must satisfy policy | Supports scheduled or immediate actions |
| Reason / Remarks | Business explanation | Text | Conditional | User | Required for governed changes | Stored for audit |

### Main Flow

1. Actor opens Activity Management or the related workflow.
2. The system validates authentication, authorization, tenant scope, and current operating context.
3. The system loads the required Activity & Batch records, related configuration, and policy controls.
4. Actor enters or confirms the information required to update activity.
5. The system validates mandatory data, lifecycle status, ownership, eligibility, financial, capacity, schedule, and security rules where applicable.
6. The system executes Update Activity and persists the resulting Activity state or transaction.
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

- Activity record created, updated, validated, or reported according to the action.
- Lifecycle or processing status updated.
- Related history entry created.
- Business events emitted.
- Notifications generated where configured.
- Audit events recorded.
- Reports or dashboards updated where applicable.

### UI Behaviour

Activity Management shall display scoped context, mandatory fields, lifecycle status, policy warnings, validation results, available actions, confirmation prompts, read-only states, pagination or filters where applicable, and responsive behavior for front-desk and administrative usage.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-BAT-002-001 | Actor must have permission to execute Update Activity. | Deny request and audit. | Critical |
| VAL-BAT-002-002 | Record must belong to the authorized Organization scope. | Deny request. | Critical |
| VAL-BAT-002-003 | Mandatory inputs must be complete and valid. | Block submission. | Critical |
| VAL-BAT-002-004 | Lifecycle and policy rules from BA-02 must be satisfied. | Reject or route for approval. | High |
| VAL-BAT-002-005 | Historical and audit records must be preserved. | Roll back or mark for recovery. | Critical |

### Business Rules

- BA-02 BR-ORG-004
- BA-02 BR-FAC-004
- BA-02 BR-AUD-003
- BA-02 BR-SEC-004

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| bat.update.activity.view | Organization Administrator | Read | View Update Activity context |
| bat.update.activity.execute | Organization Administrator | Execute | Execute Update Activity |
| bat.update.activity.approve | Organization Administrator | Approve | Approve governed exceptions where configured |
| bat.update.activity.audit.view | Organization Administrator / Support Executive | Read | View audit trace |

### Security Considerations

The capability shall enforce authentication, role-based authorization, tenant isolation, Organization scope, Facility and Site access boundaries, sensitive data masking, secure references, and immutable audit logging.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Update Activity Completed | Primary actor and configured stakeholders | In-App / Email | Action completes | Include reference, status, and effective date where applicable |
| Update Activity Requires Approval | Approver | In-App | Approval rule applies | Include safe summary and requested action |
| Update Activity Failed | Primary actor | In-App | Validation or processing fails | Include safe failure reason and next action |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| UpdateActivityRequested | Batch / Class Management | Approval Workflow, Audit Service |
| UpdateActivityCompleted | Batch / Class Management | Notification Service, Reporting Service, Audit Service |
| UpdateActivityRejected | Batch / Class Management | Notification Service, Audit Service |

### Audit Events

| Audit Event | Description | Actor | Target Entity | Key Data |
|---|---|---|---|---|
| UPDATE_ACTIVITY_REQUESTED | Update Activity requested | Organization Administrator | Activity | Scope, reference, and reason |
| UPDATE_ACTIVITY_COMPLETED | Update Activity completed | Organization Administrator / System | Activity | Previous and new state |
| UPDATE_ACTIVITY_REJECTED | Update Activity rejected | System | Activity | Rejection reason |

### Reports Generated

- Batch / Class Management Operational Report
- Batch / Class Management History Report
- Batch / Class Management Exception Report
- Executive Dashboard

### Related Screens

- Activity Management
- Batch / Class Management Dashboard
- Batch / Class Management History
- Audit Log Viewer

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/activities/{activityId} | PATCH | Authorized token | Execute Update Activity | 200 OK or 201 Created with result |
| /api/v1/activities/{activityId}/history | GET | Authorized token | Retrieve Update Activity history | 200 OK with history |
| /api/v1/audit-logs | GET | Authorized token | Retrieve related audit events | 200 OK with scoped audit records |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Activity | Create / Update / Read | Support Update Activity | Governed by Organization scope |
| Batch | Read / Insert | Support Update Activity | Governed by Organization scope |
| Batch Schedule | Read / Insert | Support Update Activity | Governed by Organization scope |
| Batch Capacity | Read / Insert | Support Update Activity | Governed by Organization scope |
| Trainer Assignment | Read / Insert | Support Update Activity | Governed by Organization scope |
| Audit Log | Insert | Record auditable activity | Immutable |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Draft | Update Activity initiated | Configured | Organization Administrator | Required data captured |
| Configured | Validation succeeds | Active | System | BA-02 rules satisfied |
| Active | Processing completes | Inactive | System | Related updates succeed |
| Active | Approval or policy failure | Archived | System / Approver | Request rejected |
| Inactive | View history | Inactive | Authorized user | Read-only historical access |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| BAT-002-001 | Update Activity cannot be completed because required information is missing. | Missing mandatory data | Complete required fields |
| BAT-002-002 | You do not have permission to perform this action. | Authorization failure | Request access |
| BAT-002-003 | The selected record is not eligible for this action. | Policy or lifecycle violation | Review record status |
| BAT-002-004 | Update Activity could not be completed due to a system or integration error. | Processing failure | Retry or contact support |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Execute Update Activity | Given the actor has required permission and valid scope | When the actor submits valid information | Then the system shall complete Update Activity successfully |
| Enforce validation | Given mandatory data or policy conditions are invalid | When the action is submitted | Then the system shall reject the request with a clear message |
| Preserve audit | Given the action completes or fails | When processing ends | Then audit events shall record actor, timestamp, scope, and outcome |
| Protect scope | Given the selected record is outside authorized scope | When the action is requested | Then the system shall deny access |

### Dependencies

- Facility Management
- Site Management
- Trainer Management
- Customer Management
- Membership Management
- Attendance Management
- Notification Management

### Operational Considerations

Update Activity should be designed for high-volume operational use, retry-safe processing, clear exception handling, and support-team diagnostics without exposing sensitive data.

### Non-Functional Considerations

This requirement shall satisfy Digitize non-functional expectations for availability, reliability, performance, scalability, security, configurability, maintainability, and auditability.

### Assumptions

- Required master data and configuration are maintained by authorized users.
- Related services expose stable APIs for validation and synchronization.
- Organization policies define approval, retention, notification, and exception behavior.

### Success Criteria

Update Activity is completed accurately, securely, and audibly, with downstream records synchronized and no loss of historical traceability.

### Related Functional Requirements

- FR-BAT-001 - Create Activity
- FR-BAT-003 - Configure Activity Rules
- FR-BAT-004 - Create Batch
- FR-BAT-005 - Update Batch
- FR-AUD-001 - Record Audit Events

### Notes

Update Activity shall remain aligned with the approved BA source documents and shall not introduce behavior that bypasses tenant isolation, lifecycle governance, financial controls, or auditability.

---

## FR-BAT-003 - Configure Activity Rules

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-BAT-003 |
| Requirement Name | Configure Activity Rules |
| Functional Module | Batch / Class Management |
| Business Domain | Activity & Batch |
| Business Capability | Activity Configuration |
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
| Business Requirement | BA-08 BR-015 Activity Configuration |
| Business Rule | BA-02 BR-ORG-004, BR-FAC-004, BR-ATT-001, BR-SEC-004 |
| Business Process | BA-03 BP-ACT-003 Configure Activity Rules |
| Business Process Flow | BA-04 Section 21 Activity Management Flow, Section 22 Batch Management Flow |
| Persona | BA-05 Facility Manager, Trainer, Reception Staff, Customer |
| User Journey | BA-06 Section 5 Facility Manager Journey, Section 8 Trainer Journey, Section 17 Attendance Journey |
| Stakeholder | BA-07 Facility Manager, Trainer, Reception Staff, Customer |
| Non-Functional Requirement | BA-09 Section 2.8 Configurability, Section 2.4 Performance, Section 2.10 Auditability |
| Assumption / Constraint / Risk | BA-10 BA-ASS-011, BA-RSK-006 |

### Purpose

To enable Activity Configuration within Batch / Class Management so Digitize can execute Configure Activity Rules consistently across Organizations, Facilities, Sites, users, and related operational or commercial services.

### Functional Requirement

The system shall support Configure Activity Rules as an atomic Batch / Class Management capability, including scoped data capture, business-rule validation, permission enforcement, lifecycle handling, related service synchronization, notification generation, reporting contribution, and immutable audit recording.

### Business Justification

Configure Activity Rules is required to preserve operational control, revenue accuracy, service continuity, customer trust, and enterprise traceability for Activity & Batch processes. Without this capability, downstream modules would rely on incomplete, manual, or inconsistent records.

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
- Actor has permission for Configure Activity Rules.
- Required Activity & Batch configuration and policies are available.
- Related records required by BA-03 BP-ACT-003 Configure Activity Rules are available and within authorized scope.

### Trigger

The capability is triggered when Organization Administrator or the System initiates Configure Activity Rules from Activity Rules, a related workflow, a scheduled job, or an approved integration event.

### In Scope

- Capture or retrieve required Activity & Batch context.
- Validate Organization, Facility, Site, Customer, user, and policy scope where applicable.
- Execute Configure Activity Rules according to approved business rules.
- Persist the resulting Activity state or transaction.
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
- Activity reference
- Customer reference, where applicable
- Effective date and time, where applicable
- Status or action reason, where applicable
- Payment, billing, trainer, session, or subscription reference where applicable
- Actor remarks, where applicable

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Activity ID | Primary business record reference | Identifier | Yes | System / User | Must exist or be generated within scope | Core reference for Configure Activity Rules |
| Organization ID | Tenant Organization context | Identifier | Yes | Session / System | Must be Active and authorized | Enforces tenant isolation |
| Facility ID | Facility context | Identifier | Conditional | User / System | Must be Active where applicable | Required for facility-level operations |
| Site ID | Site context | Identifier | Conditional | User / System | Must belong to Facility where applicable | Required for site-level operations |
| Status | Lifecycle or processing state | Enum | Yes | System | Must follow allowed state transitions | Drives UI and downstream access |
| Effective Date | Date when action applies | DateTime | Conditional | User / System | Must satisfy policy | Supports scheduled or immediate actions |
| Reason / Remarks | Business explanation | Text | Conditional | User | Required for governed changes | Stored for audit |

### Main Flow

1. Actor opens Activity Rules or the related workflow.
2. The system validates authentication, authorization, tenant scope, and current operating context.
3. The system loads the required Activity & Batch records, related configuration, and policy controls.
4. Actor enters or confirms the information required to configure activity rules.
5. The system validates mandatory data, lifecycle status, ownership, eligibility, financial, capacity, schedule, and security rules where applicable.
6. The system executes Configure Activity Rules and persists the resulting Activity state or transaction.
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

- Activity record created, updated, validated, or reported according to the action.
- Lifecycle or processing status updated.
- Related history entry created.
- Business events emitted.
- Notifications generated where configured.
- Audit events recorded.
- Reports or dashboards updated where applicable.

### UI Behaviour

Activity Rules shall display scoped context, mandatory fields, lifecycle status, policy warnings, validation results, available actions, confirmation prompts, read-only states, pagination or filters where applicable, and responsive behavior for front-desk and administrative usage.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-BAT-003-001 | Actor must have permission to execute Configure Activity Rules. | Deny request and audit. | Critical |
| VAL-BAT-003-002 | Record must belong to the authorized Organization scope. | Deny request. | Critical |
| VAL-BAT-003-003 | Mandatory inputs must be complete and valid. | Block submission. | Critical |
| VAL-BAT-003-004 | Lifecycle and policy rules from BA-02 must be satisfied. | Reject or route for approval. | High |
| VAL-BAT-003-005 | Historical and audit records must be preserved. | Roll back or mark for recovery. | Critical |

### Business Rules

- BA-02 BR-ORG-004
- BA-02 BR-FAC-004
- BA-02 BR-ATT-001
- BA-02 BR-SEC-004

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| bat.configure.activity.rules.view | Organization Administrator | Read | View Configure Activity Rules context |
| bat.configure.activity.rules.execute | Organization Administrator | Execute | Execute Configure Activity Rules |
| bat.configure.activity.rules.approve | Organization Administrator | Approve | Approve governed exceptions where configured |
| bat.configure.activity.rules.audit.view | Organization Administrator / Support Executive | Read | View audit trace |

### Security Considerations

The capability shall enforce authentication, role-based authorization, tenant isolation, Organization scope, Facility and Site access boundaries, sensitive data masking, secure references, and immutable audit logging.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Configure Activity Rules Completed | Primary actor and configured stakeholders | In-App / Email | Action completes | Include reference, status, and effective date where applicable |
| Configure Activity Rules Requires Approval | Approver | In-App | Approval rule applies | Include safe summary and requested action |
| Configure Activity Rules Failed | Primary actor | In-App | Validation or processing fails | Include safe failure reason and next action |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| ConfigureActivityRulesRequested | Batch / Class Management | Approval Workflow, Audit Service |
| ConfigureActivityRulesCompleted | Batch / Class Management | Notification Service, Reporting Service, Audit Service |
| ConfigureActivityRulesRejected | Batch / Class Management | Notification Service, Audit Service |

### Audit Events

| Audit Event | Description | Actor | Target Entity | Key Data |
|---|---|---|---|---|
| CONFIGURE_ACTIVITY_RULES_REQUESTED | Configure Activity Rules requested | Organization Administrator | Activity | Scope, reference, and reason |
| CONFIGURE_ACTIVITY_RULES_COMPLETED | Configure Activity Rules completed | Organization Administrator / System | Activity | Previous and new state |
| CONFIGURE_ACTIVITY_RULES_REJECTED | Configure Activity Rules rejected | System | Activity | Rejection reason |

### Reports Generated

- Batch / Class Management Operational Report
- Batch / Class Management History Report
- Batch / Class Management Exception Report
- Executive Dashboard

### Related Screens

- Activity Rules
- Batch / Class Management Dashboard
- Batch / Class Management History
- Audit Log Viewer

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/activities/{activityId}/rules | PUT | Authorized token | Execute Configure Activity Rules | 200 OK or 201 Created with result |
| /api/v1/activities/{activityId}/rules/history | GET | Authorized token | Retrieve Configure Activity Rules history | 200 OK with history |
| /api/v1/audit-logs | GET | Authorized token | Retrieve related audit events | 200 OK with scoped audit records |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Activity | Create / Update / Read | Support Configure Activity Rules | Governed by Organization scope |
| Batch | Read / Insert | Support Configure Activity Rules | Governed by Organization scope |
| Batch Schedule | Read / Insert | Support Configure Activity Rules | Governed by Organization scope |
| Batch Capacity | Read / Insert | Support Configure Activity Rules | Governed by Organization scope |
| Trainer Assignment | Read / Insert | Support Configure Activity Rules | Governed by Organization scope |
| Audit Log | Insert | Record auditable activity | Immutable |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Draft | Configure Activity Rules initiated | Configured | Organization Administrator | Required data captured |
| Configured | Validation succeeds | Active | System | BA-02 rules satisfied |
| Active | Processing completes | Inactive | System | Related updates succeed |
| Active | Approval or policy failure | Archived | System / Approver | Request rejected |
| Inactive | View history | Inactive | Authorized user | Read-only historical access |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| BAT-003-001 | Configure Activity Rules cannot be completed because required information is missing. | Missing mandatory data | Complete required fields |
| BAT-003-002 | You do not have permission to perform this action. | Authorization failure | Request access |
| BAT-003-003 | The selected record is not eligible for this action. | Policy or lifecycle violation | Review record status |
| BAT-003-004 | Configure Activity Rules could not be completed due to a system or integration error. | Processing failure | Retry or contact support |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Execute Configure Activity Rules | Given the actor has required permission and valid scope | When the actor submits valid information | Then the system shall complete Configure Activity Rules successfully |
| Enforce validation | Given mandatory data or policy conditions are invalid | When the action is submitted | Then the system shall reject the request with a clear message |
| Preserve audit | Given the action completes or fails | When processing ends | Then audit events shall record actor, timestamp, scope, and outcome |
| Protect scope | Given the selected record is outside authorized scope | When the action is requested | Then the system shall deny access |

### Dependencies

- Facility Management
- Site Management
- Trainer Management
- Customer Management
- Membership Management
- Attendance Management
- Notification Management

### Operational Considerations

Configure Activity Rules should be designed for high-volume operational use, retry-safe processing, clear exception handling, and support-team diagnostics without exposing sensitive data.

### Non-Functional Considerations

This requirement shall satisfy Digitize non-functional expectations for availability, reliability, performance, scalability, security, configurability, maintainability, and auditability.

### Assumptions

- Required master data and configuration are maintained by authorized users.
- Related services expose stable APIs for validation and synchronization.
- Organization policies define approval, retention, notification, and exception behavior.

### Success Criteria

Configure Activity Rules is completed accurately, securely, and audibly, with downstream records synchronized and no loss of historical traceability.

### Related Functional Requirements

- FR-BAT-001 - Create Activity
- FR-BAT-002 - Update Activity
- FR-BAT-004 - Create Batch
- FR-BAT-005 - Update Batch
- FR-AUD-001 - Record Audit Events

### Notes

Configure Activity Rules shall remain aligned with the approved BA source documents and shall not introduce behavior that bypasses tenant isolation, lifecycle governance, financial controls, or auditability.

---

## FR-BAT-004 - Create Batch

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-BAT-004 |
| Requirement Name | Create Batch |
| Functional Module | Batch / Class Management |
| Business Domain | Activity & Batch |
| Business Capability | Batch Management |
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
| Business Requirement | BA-08 BR-016 Batch Scheduling |
| Business Rule | BA-02 BR-TRN-004, BR-ATT-006, BR-SEC-004 |
| Business Process | BA-03 BP-ACT-004 Create Batch |
| Business Process Flow | BA-04 Section 21 Activity Management Flow, Section 22 Batch Management Flow |
| Persona | BA-05 Facility Manager, Trainer, Reception Staff, Customer |
| User Journey | BA-06 Section 5 Facility Manager Journey, Section 8 Trainer Journey, Section 17 Attendance Journey |
| Stakeholder | BA-07 Facility Manager, Trainer, Reception Staff, Customer |
| Non-Functional Requirement | BA-09 Section 2.8 Configurability, Section 2.4 Performance, Section 2.10 Auditability |
| Assumption / Constraint / Risk | BA-10 BA-ASS-011, BA-RSK-006 |

### Purpose

To enable Batch Management within Batch / Class Management so Digitize can execute Create Batch consistently across Organizations, Facilities, Sites, users, and related operational or commercial services.

### Functional Requirement

The system shall support Create Batch as an atomic Batch / Class Management capability, including scoped data capture, business-rule validation, permission enforcement, lifecycle handling, related service synchronization, notification generation, reporting contribution, and immutable audit recording.

### Business Justification

Create Batch is required to preserve operational control, revenue accuracy, service continuity, customer trust, and enterprise traceability for Activity & Batch processes. Without this capability, downstream modules would rely on incomplete, manual, or inconsistent records.

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
- Actor has permission for Create Batch.
- Required Activity & Batch configuration and policies are available.
- Related records required by BA-03 BP-ACT-004 Create Batch are available and within authorized scope.

### Trigger

The capability is triggered when Facility Manager or the System initiates Create Batch from Batch Management, a related workflow, a scheduled job, or an approved integration event.

### In Scope

- Capture or retrieve required Activity & Batch context.
- Validate Organization, Facility, Site, Customer, user, and policy scope where applicable.
- Execute Create Batch according to approved business rules.
- Persist the resulting Activity state or transaction.
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
- Activity reference
- Customer reference, where applicable
- Effective date and time, where applicable
- Status or action reason, where applicable
- Payment, billing, trainer, session, or subscription reference where applicable
- Actor remarks, where applicable

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Activity ID | Primary business record reference | Identifier | Yes | System / User | Must exist or be generated within scope | Core reference for Create Batch |
| Organization ID | Tenant Organization context | Identifier | Yes | Session / System | Must be Active and authorized | Enforces tenant isolation |
| Facility ID | Facility context | Identifier | Conditional | User / System | Must be Active where applicable | Required for facility-level operations |
| Site ID | Site context | Identifier | Conditional | User / System | Must belong to Facility where applicable | Required for site-level operations |
| Status | Lifecycle or processing state | Enum | Yes | System | Must follow allowed state transitions | Drives UI and downstream access |
| Effective Date | Date when action applies | DateTime | Conditional | User / System | Must satisfy policy | Supports scheduled or immediate actions |
| Reason / Remarks | Business explanation | Text | Conditional | User | Required for governed changes | Stored for audit |

### Main Flow

1. Actor opens Batch Management or the related workflow.
2. The system validates authentication, authorization, tenant scope, and current operating context.
3. The system loads the required Activity & Batch records, related configuration, and policy controls.
4. Actor enters or confirms the information required to create batch.
5. The system validates mandatory data, lifecycle status, ownership, eligibility, financial, capacity, schedule, and security rules where applicable.
6. The system executes Create Batch and persists the resulting Activity state or transaction.
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

- Activity record created, updated, validated, or reported according to the action.
- Lifecycle or processing status updated.
- Related history entry created.
- Business events emitted.
- Notifications generated where configured.
- Audit events recorded.
- Reports or dashboards updated where applicable.

### UI Behaviour

Batch Management shall display scoped context, mandatory fields, lifecycle status, policy warnings, validation results, available actions, confirmation prompts, read-only states, pagination or filters where applicable, and responsive behavior for front-desk and administrative usage.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-BAT-004-001 | Actor must have permission to execute Create Batch. | Deny request and audit. | Critical |
| VAL-BAT-004-002 | Record must belong to the authorized Organization scope. | Deny request. | Critical |
| VAL-BAT-004-003 | Mandatory inputs must be complete and valid. | Block submission. | Critical |
| VAL-BAT-004-004 | Lifecycle and policy rules from BA-02 must be satisfied. | Reject or route for approval. | High |
| VAL-BAT-004-005 | Historical and audit records must be preserved. | Roll back or mark for recovery. | Critical |

### Business Rules

- BA-02 BR-TRN-004
- BA-02 BR-ATT-006
- BA-02 BR-SEC-004

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| bat.create.batch.view | Facility Manager | Read | View Create Batch context |
| bat.create.batch.execute | Facility Manager | Execute | Execute Create Batch |
| bat.create.batch.approve | Organization Administrator | Approve | Approve governed exceptions where configured |
| bat.create.batch.audit.view | Organization Administrator / Support Executive | Read | View audit trace |

### Security Considerations

The capability shall enforce authentication, role-based authorization, tenant isolation, Organization scope, Facility and Site access boundaries, sensitive data masking, secure references, and immutable audit logging.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Create Batch Completed | Primary actor and configured stakeholders | In-App / Email | Action completes | Include reference, status, and effective date where applicable |
| Create Batch Requires Approval | Approver | In-App | Approval rule applies | Include safe summary and requested action |
| Create Batch Failed | Primary actor | In-App | Validation or processing fails | Include safe failure reason and next action |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| CreateBatchRequested | Batch / Class Management | Approval Workflow, Audit Service |
| CreateBatchCompleted | Batch / Class Management | Notification Service, Reporting Service, Audit Service |
| CreateBatchRejected | Batch / Class Management | Notification Service, Audit Service |

### Audit Events

| Audit Event | Description | Actor | Target Entity | Key Data |
|---|---|---|---|---|
| CREATE_BATCH_REQUESTED | Create Batch requested | Facility Manager | Activity | Scope, reference, and reason |
| CREATE_BATCH_COMPLETED | Create Batch completed | Facility Manager / System | Activity | Previous and new state |
| CREATE_BATCH_REJECTED | Create Batch rejected | System | Activity | Rejection reason |

### Reports Generated

- Batch / Class Management Operational Report
- Batch / Class Management History Report
- Batch / Class Management Exception Report
- Executive Dashboard

### Related Screens

- Batch Management
- Batch / Class Management Dashboard
- Batch / Class Management History
- Audit Log Viewer

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/batches | POST | Authorized token | Execute Create Batch | 200 OK or 201 Created with result |
| /api/v1/batches/history | GET | Authorized token | Retrieve Create Batch history | 200 OK with history |
| /api/v1/audit-logs | GET | Authorized token | Retrieve related audit events | 200 OK with scoped audit records |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Activity | Create / Update / Read | Support Create Batch | Governed by Organization scope |
| Batch | Read / Insert | Support Create Batch | Governed by Organization scope |
| Batch Schedule | Read / Insert | Support Create Batch | Governed by Organization scope |
| Batch Capacity | Read / Insert | Support Create Batch | Governed by Organization scope |
| Trainer Assignment | Read / Insert | Support Create Batch | Governed by Organization scope |
| Audit Log | Insert | Record auditable activity | Immutable |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Draft | Create Batch initiated | Validated | Facility Manager | Required data captured |
| Validated | Validation succeeds | Pending Approval | System | BA-02 rules satisfied |
| Pending Approval | Processing completes | Completed | System | Related updates succeed |
| Pending Approval | Approval or policy failure | Rejected | System / Approver | Request rejected |
| Completed | View history | Completed | Authorized user | Read-only historical access |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| BAT-004-001 | Create Batch cannot be completed because required information is missing. | Missing mandatory data | Complete required fields |
| BAT-004-002 | You do not have permission to perform this action. | Authorization failure | Request access |
| BAT-004-003 | The selected record is not eligible for this action. | Policy or lifecycle violation | Review record status |
| BAT-004-004 | Create Batch could not be completed due to a system or integration error. | Processing failure | Retry or contact support |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Execute Create Batch | Given the actor has required permission and valid scope | When the actor submits valid information | Then the system shall complete Create Batch successfully |
| Enforce validation | Given mandatory data or policy conditions are invalid | When the action is submitted | Then the system shall reject the request with a clear message |
| Preserve audit | Given the action completes or fails | When processing ends | Then audit events shall record actor, timestamp, scope, and outcome |
| Protect scope | Given the selected record is outside authorized scope | When the action is requested | Then the system shall deny access |

### Dependencies

- Facility Management
- Site Management
- Trainer Management
- Customer Management
- Membership Management
- Attendance Management
- Notification Management

### Operational Considerations

Create Batch should be designed for high-volume operational use, retry-safe processing, clear exception handling, and support-team diagnostics without exposing sensitive data.

### Non-Functional Considerations

This requirement shall satisfy Digitize non-functional expectations for availability, reliability, performance, scalability, security, configurability, maintainability, and auditability.

### Assumptions

- Required master data and configuration are maintained by authorized users.
- Related services expose stable APIs for validation and synchronization.
- Organization policies define approval, retention, notification, and exception behavior.

### Success Criteria

Create Batch is completed accurately, securely, and audibly, with downstream records synchronized and no loss of historical traceability.

### Related Functional Requirements

- FR-BAT-001 - Create Activity
- FR-BAT-002 - Update Activity
- FR-BAT-003 - Configure Activity Rules
- FR-BAT-005 - Update Batch
- FR-AUD-001 - Record Audit Events

### Notes

Create Batch shall remain aligned with the approved BA source documents and shall not introduce behavior that bypasses tenant isolation, lifecycle governance, financial controls, or auditability.

---

## FR-BAT-005 - Update Batch

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-BAT-005 |
| Requirement Name | Update Batch |
| Functional Module | Batch / Class Management |
| Business Domain | Activity & Batch |
| Business Capability | Batch Management |
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
| Business Requirement | BA-08 BR-016 Batch Scheduling |
| Business Rule | BA-02 BR-TRN-004, BR-ATT-006, BR-AUD-003 |
| Business Process | BA-03 BP-ACT-005 Update Batch |
| Business Process Flow | BA-04 Section 21 Activity Management Flow, Section 22 Batch Management Flow |
| Persona | BA-05 Facility Manager, Trainer, Reception Staff, Customer |
| User Journey | BA-06 Section 5 Facility Manager Journey, Section 8 Trainer Journey, Section 17 Attendance Journey |
| Stakeholder | BA-07 Facility Manager, Trainer, Reception Staff, Customer |
| Non-Functional Requirement | BA-09 Section 2.8 Configurability, Section 2.4 Performance, Section 2.10 Auditability |
| Assumption / Constraint / Risk | BA-10 BA-ASS-011, BA-RSK-006 |

### Purpose

To enable Batch Management within Batch / Class Management so Digitize can execute Update Batch consistently across Organizations, Facilities, Sites, users, and related operational or commercial services.

### Functional Requirement

The system shall support Update Batch as an atomic Batch / Class Management capability, including scoped data capture, business-rule validation, permission enforcement, lifecycle handling, related service synchronization, notification generation, reporting contribution, and immutable audit recording.

### Business Justification

Update Batch is required to preserve operational control, revenue accuracy, service continuity, customer trust, and enterprise traceability for Activity & Batch processes. Without this capability, downstream modules would rely on incomplete, manual, or inconsistent records.

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
- Actor has permission for Update Batch.
- Required Activity & Batch configuration and policies are available.
- Related records required by BA-03 BP-ACT-005 Update Batch are available and within authorized scope.

### Trigger

The capability is triggered when Facility Manager or the System initiates Update Batch from Batch Management, a related workflow, a scheduled job, or an approved integration event.

### In Scope

- Capture or retrieve required Activity & Batch context.
- Validate Organization, Facility, Site, Customer, user, and policy scope where applicable.
- Execute Update Batch according to approved business rules.
- Persist the resulting Activity state or transaction.
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
- Activity reference
- Customer reference, where applicable
- Effective date and time, where applicable
- Status or action reason, where applicable
- Payment, billing, trainer, session, or subscription reference where applicable
- Actor remarks, where applicable

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Activity ID | Primary business record reference | Identifier | Yes | System / User | Must exist or be generated within scope | Core reference for Update Batch |
| Organization ID | Tenant Organization context | Identifier | Yes | Session / System | Must be Active and authorized | Enforces tenant isolation |
| Facility ID | Facility context | Identifier | Conditional | User / System | Must be Active where applicable | Required for facility-level operations |
| Site ID | Site context | Identifier | Conditional | User / System | Must belong to Facility where applicable | Required for site-level operations |
| Status | Lifecycle or processing state | Enum | Yes | System | Must follow allowed state transitions | Drives UI and downstream access |
| Effective Date | Date when action applies | DateTime | Conditional | User / System | Must satisfy policy | Supports scheduled or immediate actions |
| Reason / Remarks | Business explanation | Text | Conditional | User | Required for governed changes | Stored for audit |

### Main Flow

1. Actor opens Batch Management or the related workflow.
2. The system validates authentication, authorization, tenant scope, and current operating context.
3. The system loads the required Activity & Batch records, related configuration, and policy controls.
4. Actor enters or confirms the information required to update batch.
5. The system validates mandatory data, lifecycle status, ownership, eligibility, financial, capacity, schedule, and security rules where applicable.
6. The system executes Update Batch and persists the resulting Activity state or transaction.
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

- Activity record created, updated, validated, or reported according to the action.
- Lifecycle or processing status updated.
- Related history entry created.
- Business events emitted.
- Notifications generated where configured.
- Audit events recorded.
- Reports or dashboards updated where applicable.

### UI Behaviour

Batch Management shall display scoped context, mandatory fields, lifecycle status, policy warnings, validation results, available actions, confirmation prompts, read-only states, pagination or filters where applicable, and responsive behavior for front-desk and administrative usage.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-BAT-005-001 | Actor must have permission to execute Update Batch. | Deny request and audit. | Critical |
| VAL-BAT-005-002 | Record must belong to the authorized Organization scope. | Deny request. | Critical |
| VAL-BAT-005-003 | Mandatory inputs must be complete and valid. | Block submission. | Critical |
| VAL-BAT-005-004 | Lifecycle and policy rules from BA-02 must be satisfied. | Reject or route for approval. | High |
| VAL-BAT-005-005 | Historical and audit records must be preserved. | Roll back or mark for recovery. | Critical |

### Business Rules

- BA-02 BR-TRN-004
- BA-02 BR-ATT-006
- BA-02 BR-AUD-003

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| bat.update.batch.view | Facility Manager | Read | View Update Batch context |
| bat.update.batch.execute | Facility Manager | Execute | Execute Update Batch |
| bat.update.batch.approve | Organization Administrator | Approve | Approve governed exceptions where configured |
| bat.update.batch.audit.view | Organization Administrator / Support Executive | Read | View audit trace |

### Security Considerations

The capability shall enforce authentication, role-based authorization, tenant isolation, Organization scope, Facility and Site access boundaries, sensitive data masking, secure references, and immutable audit logging.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Update Batch Completed | Primary actor and configured stakeholders | In-App / Email | Action completes | Include reference, status, and effective date where applicable |
| Update Batch Requires Approval | Approver | In-App | Approval rule applies | Include safe summary and requested action |
| Update Batch Failed | Primary actor | In-App | Validation or processing fails | Include safe failure reason and next action |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| UpdateBatchRequested | Batch / Class Management | Approval Workflow, Audit Service |
| UpdateBatchCompleted | Batch / Class Management | Notification Service, Reporting Service, Audit Service |
| UpdateBatchRejected | Batch / Class Management | Notification Service, Audit Service |

### Audit Events

| Audit Event | Description | Actor | Target Entity | Key Data |
|---|---|---|---|---|
| UPDATE_BATCH_REQUESTED | Update Batch requested | Facility Manager | Activity | Scope, reference, and reason |
| UPDATE_BATCH_COMPLETED | Update Batch completed | Facility Manager / System | Activity | Previous and new state |
| UPDATE_BATCH_REJECTED | Update Batch rejected | System | Activity | Rejection reason |

### Reports Generated

- Batch / Class Management Operational Report
- Batch / Class Management History Report
- Batch / Class Management Exception Report
- Executive Dashboard

### Related Screens

- Batch Management
- Batch / Class Management Dashboard
- Batch / Class Management History
- Audit Log Viewer

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/batches/{batchId} | PATCH | Authorized token | Execute Update Batch | 200 OK or 201 Created with result |
| /api/v1/batches/{batchId}/history | GET | Authorized token | Retrieve Update Batch history | 200 OK with history |
| /api/v1/audit-logs | GET | Authorized token | Retrieve related audit events | 200 OK with scoped audit records |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Activity | Create / Update / Read | Support Update Batch | Governed by Organization scope |
| Batch | Read / Insert | Support Update Batch | Governed by Organization scope |
| Batch Schedule | Read / Insert | Support Update Batch | Governed by Organization scope |
| Batch Capacity | Read / Insert | Support Update Batch | Governed by Organization scope |
| Trainer Assignment | Read / Insert | Support Update Batch | Governed by Organization scope |
| Audit Log | Insert | Record auditable activity | Immutable |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Draft | Update Batch initiated | Configured | Facility Manager | Required data captured |
| Configured | Validation succeeds | Active | System | BA-02 rules satisfied |
| Active | Processing completes | Inactive | System | Related updates succeed |
| Active | Approval or policy failure | Archived | System / Approver | Request rejected |
| Inactive | View history | Inactive | Authorized user | Read-only historical access |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| BAT-005-001 | Update Batch cannot be completed because required information is missing. | Missing mandatory data | Complete required fields |
| BAT-005-002 | You do not have permission to perform this action. | Authorization failure | Request access |
| BAT-005-003 | The selected record is not eligible for this action. | Policy or lifecycle violation | Review record status |
| BAT-005-004 | Update Batch could not be completed due to a system or integration error. | Processing failure | Retry or contact support |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Execute Update Batch | Given the actor has required permission and valid scope | When the actor submits valid information | Then the system shall complete Update Batch successfully |
| Enforce validation | Given mandatory data or policy conditions are invalid | When the action is submitted | Then the system shall reject the request with a clear message |
| Preserve audit | Given the action completes or fails | When processing ends | Then audit events shall record actor, timestamp, scope, and outcome |
| Protect scope | Given the selected record is outside authorized scope | When the action is requested | Then the system shall deny access |

### Dependencies

- Facility Management
- Site Management
- Trainer Management
- Customer Management
- Membership Management
- Attendance Management
- Notification Management

### Operational Considerations

Update Batch should be designed for high-volume operational use, retry-safe processing, clear exception handling, and support-team diagnostics without exposing sensitive data.

### Non-Functional Considerations

This requirement shall satisfy Digitize non-functional expectations for availability, reliability, performance, scalability, security, configurability, maintainability, and auditability.

### Assumptions

- Required master data and configuration are maintained by authorized users.
- Related services expose stable APIs for validation and synchronization.
- Organization policies define approval, retention, notification, and exception behavior.

### Success Criteria

Update Batch is completed accurately, securely, and audibly, with downstream records synchronized and no loss of historical traceability.

### Related Functional Requirements

- FR-BAT-001 - Create Activity
- FR-BAT-002 - Update Activity
- FR-BAT-003 - Configure Activity Rules
- FR-BAT-004 - Create Batch
- FR-AUD-001 - Record Audit Events

### Notes

Update Batch shall remain aligned with the approved BA source documents and shall not introduce behavior that bypasses tenant isolation, lifecycle governance, financial controls, or auditability.

---

## FR-BAT-006 - Schedule Batch

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-BAT-006 |
| Requirement Name | Schedule Batch |
| Functional Module | Batch / Class Management |
| Business Domain | Activity & Batch |
| Business Capability | Batch Scheduling |
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
| Business Requirement | BA-08 BR-016 Batch Scheduling |
| Business Rule | BA-02 BR-TRN-005, BR-TRN-008, BR-ATT-006, BR-SEC-004 |
| Business Process | BA-03 BP-ACT-006 Schedule Batch |
| Business Process Flow | BA-04 Section 21 Activity Management Flow, Section 22 Batch Management Flow |
| Persona | BA-05 Facility Manager, Trainer, Reception Staff, Customer |
| User Journey | BA-06 Section 5 Facility Manager Journey, Section 8 Trainer Journey, Section 17 Attendance Journey |
| Stakeholder | BA-07 Facility Manager, Trainer, Reception Staff, Customer |
| Non-Functional Requirement | BA-09 Section 2.8 Configurability, Section 2.4 Performance, Section 2.10 Auditability |
| Assumption / Constraint / Risk | BA-10 BA-ASS-011, BA-RSK-006 |

### Purpose

To enable Batch Scheduling within Batch / Class Management so Digitize can execute Schedule Batch consistently across Organizations, Facilities, Sites, users, and related operational or commercial services.

### Functional Requirement

The system shall support Schedule Batch as an atomic Batch / Class Management capability, including scoped data capture, business-rule validation, permission enforcement, lifecycle handling, related service synchronization, notification generation, reporting contribution, and immutable audit recording.

### Business Justification

Schedule Batch is required to preserve operational control, revenue accuracy, service continuity, customer trust, and enterprise traceability for Activity & Batch processes. Without this capability, downstream modules would rely on incomplete, manual, or inconsistent records.

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
- Actor has permission for Schedule Batch.
- Required Activity & Batch configuration and policies are available.
- Related records required by BA-03 BP-ACT-006 Schedule Batch are available and within authorized scope.

### Trigger

The capability is triggered when Facility Manager or the System initiates Schedule Batch from Batch Schedule, a related workflow, a scheduled job, or an approved integration event.

### In Scope

- Capture or retrieve required Activity & Batch context.
- Validate Organization, Facility, Site, Customer, user, and policy scope where applicable.
- Execute Schedule Batch according to approved business rules.
- Persist the resulting Activity state or transaction.
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
- Activity reference
- Customer reference, where applicable
- Effective date and time, where applicable
- Status or action reason, where applicable
- Payment, billing, trainer, session, or subscription reference where applicable
- Actor remarks, where applicable

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Activity ID | Primary business record reference | Identifier | Yes | System / User | Must exist or be generated within scope | Core reference for Schedule Batch |
| Organization ID | Tenant Organization context | Identifier | Yes | Session / System | Must be Active and authorized | Enforces tenant isolation |
| Facility ID | Facility context | Identifier | Conditional | User / System | Must be Active where applicable | Required for facility-level operations |
| Site ID | Site context | Identifier | Conditional | User / System | Must belong to Facility where applicable | Required for site-level operations |
| Status | Lifecycle or processing state | Enum | Yes | System | Must follow allowed state transitions | Drives UI and downstream access |
| Effective Date | Date when action applies | DateTime | Conditional | User / System | Must satisfy policy | Supports scheduled or immediate actions |
| Reason / Remarks | Business explanation | Text | Conditional | User | Required for governed changes | Stored for audit |

### Main Flow

1. Actor opens Batch Schedule or the related workflow.
2. The system validates authentication, authorization, tenant scope, and current operating context.
3. The system loads the required Activity & Batch records, related configuration, and policy controls.
4. Actor enters or confirms the information required to schedule batch.
5. The system validates mandatory data, lifecycle status, ownership, eligibility, financial, capacity, schedule, and security rules where applicable.
6. The system executes Schedule Batch and persists the resulting Activity state or transaction.
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

- Activity record created, updated, validated, or reported according to the action.
- Lifecycle or processing status updated.
- Related history entry created.
- Business events emitted.
- Notifications generated where configured.
- Audit events recorded.
- Reports or dashboards updated where applicable.

### UI Behaviour

Batch Schedule shall display scoped context, mandatory fields, lifecycle status, policy warnings, validation results, available actions, confirmation prompts, read-only states, pagination or filters where applicable, and responsive behavior for front-desk and administrative usage.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-BAT-006-001 | Actor must have permission to execute Schedule Batch. | Deny request and audit. | Critical |
| VAL-BAT-006-002 | Record must belong to the authorized Organization scope. | Deny request. | Critical |
| VAL-BAT-006-003 | Mandatory inputs must be complete and valid. | Block submission. | Critical |
| VAL-BAT-006-004 | Lifecycle and policy rules from BA-02 must be satisfied. | Reject or route for approval. | High |
| VAL-BAT-006-005 | Historical and audit records must be preserved. | Roll back or mark for recovery. | Critical |

### Business Rules

- BA-02 BR-TRN-005
- BA-02 BR-TRN-008
- BA-02 BR-ATT-006
- BA-02 BR-SEC-004

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| bat.schedule.batch.view | Facility Manager | Read | View Schedule Batch context |
| bat.schedule.batch.execute | Facility Manager | Execute | Execute Schedule Batch |
| bat.schedule.batch.approve | Organization Administrator | Approve | Approve governed exceptions where configured |
| bat.schedule.batch.audit.view | Organization Administrator / Support Executive | Read | View audit trace |

### Security Considerations

The capability shall enforce authentication, role-based authorization, tenant isolation, Organization scope, Facility and Site access boundaries, sensitive data masking, secure references, and immutable audit logging.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Schedule Batch Completed | Primary actor and configured stakeholders | In-App / Email | Action completes | Include reference, status, and effective date where applicable |
| Schedule Batch Requires Approval | Approver | In-App | Approval rule applies | Include safe summary and requested action |
| Schedule Batch Failed | Primary actor | In-App | Validation or processing fails | Include safe failure reason and next action |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| ScheduleBatchRequested | Batch / Class Management | Approval Workflow, Audit Service |
| ScheduleBatchCompleted | Batch / Class Management | Notification Service, Reporting Service, Audit Service |
| ScheduleBatchRejected | Batch / Class Management | Notification Service, Audit Service |

### Audit Events

| Audit Event | Description | Actor | Target Entity | Key Data |
|---|---|---|---|---|
| SCHEDULE_BATCH_REQUESTED | Schedule Batch requested | Facility Manager | Activity | Scope, reference, and reason |
| SCHEDULE_BATCH_COMPLETED | Schedule Batch completed | Facility Manager / System | Activity | Previous and new state |
| SCHEDULE_BATCH_REJECTED | Schedule Batch rejected | System | Activity | Rejection reason |

### Reports Generated

- Batch / Class Management Operational Report
- Batch / Class Management History Report
- Batch / Class Management Exception Report
- Executive Dashboard

### Related Screens

- Batch Schedule
- Batch / Class Management Dashboard
- Batch / Class Management History
- Audit Log Viewer

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/batches/{batchId}/schedule | POST | Authorized token | Execute Schedule Batch | 200 OK or 201 Created with result |
| /api/v1/batches/{batchId}/schedule/history | GET | Authorized token | Retrieve Schedule Batch history | 200 OK with history |
| /api/v1/audit-logs | GET | Authorized token | Retrieve related audit events | 200 OK with scoped audit records |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Activity | Create / Update / Read | Support Schedule Batch | Governed by Organization scope |
| Batch | Read / Insert | Support Schedule Batch | Governed by Organization scope |
| Batch Schedule | Read / Insert | Support Schedule Batch | Governed by Organization scope |
| Batch Capacity | Read / Insert | Support Schedule Batch | Governed by Organization scope |
| Trainer Assignment | Read / Insert | Support Schedule Batch | Governed by Organization scope |
| Audit Log | Insert | Record auditable activity | Immutable |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Draft | Schedule Batch initiated | Validated | Facility Manager | Required data captured |
| Validated | Validation succeeds | Pending Approval | System | BA-02 rules satisfied |
| Pending Approval | Processing completes | Completed | System | Related updates succeed |
| Pending Approval | Approval or policy failure | Rejected | System / Approver | Request rejected |
| Completed | View history | Completed | Authorized user | Read-only historical access |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| BAT-006-001 | Schedule Batch cannot be completed because required information is missing. | Missing mandatory data | Complete required fields |
| BAT-006-002 | You do not have permission to perform this action. | Authorization failure | Request access |
| BAT-006-003 | The selected record is not eligible for this action. | Policy or lifecycle violation | Review record status |
| BAT-006-004 | Schedule Batch could not be completed due to a system or integration error. | Processing failure | Retry or contact support |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Execute Schedule Batch | Given the actor has required permission and valid scope | When the actor submits valid information | Then the system shall complete Schedule Batch successfully |
| Enforce validation | Given mandatory data or policy conditions are invalid | When the action is submitted | Then the system shall reject the request with a clear message |
| Preserve audit | Given the action completes or fails | When processing ends | Then audit events shall record actor, timestamp, scope, and outcome |
| Protect scope | Given the selected record is outside authorized scope | When the action is requested | Then the system shall deny access |

### Dependencies

- Facility Management
- Site Management
- Trainer Management
- Customer Management
- Membership Management
- Attendance Management
- Notification Management

### Operational Considerations

Schedule Batch should be designed for high-volume operational use, retry-safe processing, clear exception handling, and support-team diagnostics without exposing sensitive data.

### Non-Functional Considerations

This requirement shall satisfy Digitize non-functional expectations for availability, reliability, performance, scalability, security, configurability, maintainability, and auditability.

### Assumptions

- Required master data and configuration are maintained by authorized users.
- Related services expose stable APIs for validation and synchronization.
- Organization policies define approval, retention, notification, and exception behavior.

### Success Criteria

Schedule Batch is completed accurately, securely, and audibly, with downstream records synchronized and no loss of historical traceability.

### Related Functional Requirements

- FR-BAT-001 - Create Activity
- FR-BAT-002 - Update Activity
- FR-BAT-003 - Configure Activity Rules
- FR-BAT-004 - Create Batch
- FR-AUD-001 - Record Audit Events

### Notes

Schedule Batch shall remain aligned with the approved BA source documents and shall not introduce behavior that bypasses tenant isolation, lifecycle governance, financial controls, or auditability.

---

## FR-BAT-007 - Assign Trainer to Batch

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-BAT-007 |
| Requirement Name | Assign Trainer to Batch |
| Functional Module | Batch / Class Management |
| Business Domain | Activity & Batch |
| Business Capability | Resource Management |
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
| Business Process Flow | BA-04 Section 21 Activity Management Flow, Section 22 Batch Management Flow |
| Persona | BA-05 Facility Manager, Trainer, Reception Staff, Customer |
| User Journey | BA-06 Section 5 Facility Manager Journey, Section 8 Trainer Journey, Section 17 Attendance Journey |
| Stakeholder | BA-07 Facility Manager, Trainer, Reception Staff, Customer |
| Non-Functional Requirement | BA-09 Section 2.8 Configurability, Section 2.4 Performance, Section 2.10 Auditability |
| Assumption / Constraint / Risk | BA-10 BA-ASS-011, BA-RSK-006 |

### Purpose

To enable Resource Management within Batch / Class Management so Digitize can execute Assign Trainer to Batch consistently across Organizations, Facilities, Sites, users, and related operational or commercial services.

### Functional Requirement

The system shall support Assign Trainer to Batch as an atomic Batch / Class Management capability, including scoped data capture, business-rule validation, permission enforcement, lifecycle handling, related service synchronization, notification generation, reporting contribution, and immutable audit recording.

### Business Justification

Assign Trainer to Batch is required to preserve operational control, revenue accuracy, service continuity, customer trust, and enterprise traceability for Activity & Batch processes. Without this capability, downstream modules would rely on incomplete, manual, or inconsistent records.

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
- Required Activity & Batch configuration and policies are available.
- Related records required by BA-03 BP-ACT-007 Assign Trainer to Batch are available and within authorized scope.

### Trigger

The capability is triggered when Facility Manager or the System initiates Assign Trainer to Batch from Batch Trainer Assignment, a related workflow, a scheduled job, or an approved integration event.

### In Scope

- Capture or retrieve required Activity & Batch context.
- Validate Organization, Facility, Site, Customer, user, and policy scope where applicable.
- Execute Assign Trainer to Batch according to approved business rules.
- Persist the resulting Activity state or transaction.
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
- Activity reference
- Customer reference, where applicable
- Effective date and time, where applicable
- Status or action reason, where applicable
- Payment, billing, trainer, session, or subscription reference where applicable
- Actor remarks, where applicable

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Activity ID | Primary business record reference | Identifier | Yes | System / User | Must exist or be generated within scope | Core reference for Assign Trainer to Batch |
| Organization ID | Tenant Organization context | Identifier | Yes | Session / System | Must be Active and authorized | Enforces tenant isolation |
| Facility ID | Facility context | Identifier | Conditional | User / System | Must be Active where applicable | Required for facility-level operations |
| Site ID | Site context | Identifier | Conditional | User / System | Must belong to Facility where applicable | Required for site-level operations |
| Status | Lifecycle or processing state | Enum | Yes | System | Must follow allowed state transitions | Drives UI and downstream access |
| Effective Date | Date when action applies | DateTime | Conditional | User / System | Must satisfy policy | Supports scheduled or immediate actions |
| Reason / Remarks | Business explanation | Text | Conditional | User | Required for governed changes | Stored for audit |

### Main Flow

1. Actor opens Batch Trainer Assignment or the related workflow.
2. The system validates authentication, authorization, tenant scope, and current operating context.
3. The system loads the required Activity & Batch records, related configuration, and policy controls.
4. Actor enters or confirms the information required to assign trainer to batch.
5. The system validates mandatory data, lifecycle status, ownership, eligibility, financial, capacity, schedule, and security rules where applicable.
6. The system executes Assign Trainer to Batch and persists the resulting Activity state or transaction.
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

- Activity record created, updated, validated, or reported according to the action.
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
| VAL-BAT-007-001 | Actor must have permission to execute Assign Trainer to Batch. | Deny request and audit. | Critical |
| VAL-BAT-007-002 | Record must belong to the authorized Organization scope. | Deny request. | Critical |
| VAL-BAT-007-003 | Mandatory inputs must be complete and valid. | Block submission. | Critical |
| VAL-BAT-007-004 | Lifecycle and policy rules from BA-02 must be satisfied. | Reject or route for approval. | High |
| VAL-BAT-007-005 | Historical and audit records must be preserved. | Roll back or mark for recovery. | Critical |

### Business Rules

- BA-02 BR-TRN-004
- BA-02 BR-TRN-005
- BA-02 BR-TRN-008
- BA-02 BR-SEC-004

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| bat.assign.trainer.to.batch.view | Facility Manager | Read | View Assign Trainer to Batch context |
| bat.assign.trainer.to.batch.execute | Facility Manager | Execute | Execute Assign Trainer to Batch |
| bat.assign.trainer.to.batch.approve | Organization Administrator | Approve | Approve governed exceptions where configured |
| bat.assign.trainer.to.batch.audit.view | Organization Administrator / Support Executive | Read | View audit trace |

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
| AssignTrainerToBatchRequested | Batch / Class Management | Approval Workflow, Audit Service |
| AssignTrainerToBatchCompleted | Batch / Class Management | Notification Service, Reporting Service, Audit Service |
| AssignTrainerToBatchRejected | Batch / Class Management | Notification Service, Audit Service |

### Audit Events

| Audit Event | Description | Actor | Target Entity | Key Data |
|---|---|---|---|---|
| ASSIGN_TRAINER_TO_BATCH_REQUESTED | Assign Trainer to Batch requested | Facility Manager | Activity | Scope, reference, and reason |
| ASSIGN_TRAINER_TO_BATCH_COMPLETED | Assign Trainer to Batch completed | Facility Manager / System | Activity | Previous and new state |
| ASSIGN_TRAINER_TO_BATCH_REJECTED | Assign Trainer to Batch rejected | System | Activity | Rejection reason |

### Reports Generated

- Batch / Class Management Operational Report
- Batch / Class Management History Report
- Batch / Class Management Exception Report
- Executive Dashboard

### Related Screens

- Batch Trainer Assignment
- Batch / Class Management Dashboard
- Batch / Class Management History
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
| Activity | Create / Update / Read | Support Assign Trainer to Batch | Governed by Organization scope |
| Batch | Read / Insert | Support Assign Trainer to Batch | Governed by Organization scope |
| Batch Schedule | Read / Insert | Support Assign Trainer to Batch | Governed by Organization scope |
| Batch Capacity | Read / Insert | Support Assign Trainer to Batch | Governed by Organization scope |
| Trainer Assignment | Read / Insert | Support Assign Trainer to Batch | Governed by Organization scope |
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
| BAT-007-001 | Assign Trainer to Batch cannot be completed because required information is missing. | Missing mandatory data | Complete required fields |
| BAT-007-002 | You do not have permission to perform this action. | Authorization failure | Request access |
| BAT-007-003 | The selected record is not eligible for this action. | Policy or lifecycle violation | Review record status |
| BAT-007-004 | Assign Trainer to Batch could not be completed due to a system or integration error. | Processing failure | Retry or contact support |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Execute Assign Trainer to Batch | Given the actor has required permission and valid scope | When the actor submits valid information | Then the system shall complete Assign Trainer to Batch successfully |
| Enforce validation | Given mandatory data or policy conditions are invalid | When the action is submitted | Then the system shall reject the request with a clear message |
| Preserve audit | Given the action completes or fails | When processing ends | Then audit events shall record actor, timestamp, scope, and outcome |
| Protect scope | Given the selected record is outside authorized scope | When the action is requested | Then the system shall deny access |

### Dependencies

- Facility Management
- Site Management
- Trainer Management
- Customer Management
- Membership Management
- Attendance Management
- Notification Management

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

- FR-BAT-001 - Create Activity
- FR-BAT-002 - Update Activity
- FR-BAT-003 - Configure Activity Rules
- FR-BAT-004 - Create Batch
- FR-AUD-001 - Record Audit Events

### Notes

Assign Trainer to Batch shall remain aligned with the approved BA source documents and shall not introduce behavior that bypasses tenant isolation, lifecycle governance, financial controls, or auditability.

---

## FR-BAT-008 - Configure Batch Capacity

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-BAT-008 |
| Requirement Name | Configure Batch Capacity |
| Functional Module | Batch / Class Management |
| Business Domain | Activity & Batch |
| Business Capability | Capacity Management |
| Requirement Type | Functional |
| Requirement Category | Configuration |
| Requirement Version | 1.0 |
| Requirement Status | Approved |
| Priority | Critical |
| Complexity | Medium |
| Release Version | 1.0 |
| Owner | Product Management |

### Traceability References

| Traceability Type | Reference |
|---|---|
| Business Requirement | BA-08 BR-016 Batch Scheduling |
| Business Rule | BA-02 BR-ATT-006, BR-FAC-004, BR-SIT-006, BR-SEC-004 |
| Business Process | BA-03 BP-ACT-008 Configure Batch Capacity |
| Business Process Flow | BA-04 Section 21 Activity Management Flow, Section 22 Batch Management Flow |
| Persona | BA-05 Facility Manager, Trainer, Reception Staff, Customer |
| User Journey | BA-06 Section 5 Facility Manager Journey, Section 8 Trainer Journey, Section 17 Attendance Journey |
| Stakeholder | BA-07 Facility Manager, Trainer, Reception Staff, Customer |
| Non-Functional Requirement | BA-09 Section 2.8 Configurability, Section 2.4 Performance, Section 2.10 Auditability |
| Assumption / Constraint / Risk | BA-10 BA-ASS-011, BA-RSK-006 |

### Purpose

To enable Capacity Management within Batch / Class Management so Digitize can execute Configure Batch Capacity consistently across Organizations, Facilities, Sites, users, and related operational or commercial services.

### Functional Requirement

The system shall support Configure Batch Capacity as an atomic Batch / Class Management capability, including scoped data capture, business-rule validation, permission enforcement, lifecycle handling, related service synchronization, notification generation, reporting contribution, and immutable audit recording.

### Business Justification

Configure Batch Capacity is required to preserve operational control, revenue accuracy, service continuity, customer trust, and enterprise traceability for Activity & Batch processes. Without this capability, downstream modules would rely on incomplete, manual, or inconsistent records.

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
- Actor has permission for Configure Batch Capacity.
- Required Activity & Batch configuration and policies are available.
- Related records required by BA-03 BP-ACT-008 Configure Batch Capacity are available and within authorized scope.

### Trigger

The capability is triggered when Facility Manager or the System initiates Configure Batch Capacity from Batch Capacity, a related workflow, a scheduled job, or an approved integration event.

### In Scope

- Capture or retrieve required Activity & Batch context.
- Validate Organization, Facility, Site, Customer, user, and policy scope where applicable.
- Execute Configure Batch Capacity according to approved business rules.
- Persist the resulting Activity state or transaction.
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
- Activity reference
- Customer reference, where applicable
- Effective date and time, where applicable
- Status or action reason, where applicable
- Payment, billing, trainer, session, or subscription reference where applicable
- Actor remarks, where applicable

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Activity ID | Primary business record reference | Identifier | Yes | System / User | Must exist or be generated within scope | Core reference for Configure Batch Capacity |
| Organization ID | Tenant Organization context | Identifier | Yes | Session / System | Must be Active and authorized | Enforces tenant isolation |
| Facility ID | Facility context | Identifier | Conditional | User / System | Must be Active where applicable | Required for facility-level operations |
| Site ID | Site context | Identifier | Conditional | User / System | Must belong to Facility where applicable | Required for site-level operations |
| Status | Lifecycle or processing state | Enum | Yes | System | Must follow allowed state transitions | Drives UI and downstream access |
| Effective Date | Date when action applies | DateTime | Conditional | User / System | Must satisfy policy | Supports scheduled or immediate actions |
| Reason / Remarks | Business explanation | Text | Conditional | User | Required for governed changes | Stored for audit |

### Main Flow

1. Actor opens Batch Capacity or the related workflow.
2. The system validates authentication, authorization, tenant scope, and current operating context.
3. The system loads the required Activity & Batch records, related configuration, and policy controls.
4. Actor enters or confirms the information required to configure batch capacity.
5. The system validates mandatory data, lifecycle status, ownership, eligibility, financial, capacity, schedule, and security rules where applicable.
6. The system executes Configure Batch Capacity and persists the resulting Activity state or transaction.
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

- Activity record created, updated, validated, or reported according to the action.
- Lifecycle or processing status updated.
- Related history entry created.
- Business events emitted.
- Notifications generated where configured.
- Audit events recorded.
- Reports or dashboards updated where applicable.

### UI Behaviour

Batch Capacity shall display scoped context, mandatory fields, lifecycle status, policy warnings, validation results, available actions, confirmation prompts, read-only states, pagination or filters where applicable, and responsive behavior for front-desk and administrative usage.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-BAT-008-001 | Actor must have permission to execute Configure Batch Capacity. | Deny request and audit. | Critical |
| VAL-BAT-008-002 | Record must belong to the authorized Organization scope. | Deny request. | Critical |
| VAL-BAT-008-003 | Mandatory inputs must be complete and valid. | Block submission. | Critical |
| VAL-BAT-008-004 | Lifecycle and policy rules from BA-02 must be satisfied. | Reject or route for approval. | High |
| VAL-BAT-008-005 | Historical and audit records must be preserved. | Roll back or mark for recovery. | Critical |

### Business Rules

- BA-02 BR-ATT-006
- BA-02 BR-FAC-004
- BA-02 BR-SIT-006
- BA-02 BR-SEC-004

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| bat.configure.batch.capacity.view | Facility Manager | Read | View Configure Batch Capacity context |
| bat.configure.batch.capacity.execute | Facility Manager | Execute | Execute Configure Batch Capacity |
| bat.configure.batch.capacity.approve | Organization Administrator | Approve | Approve governed exceptions where configured |
| bat.configure.batch.capacity.audit.view | Organization Administrator / Support Executive | Read | View audit trace |

### Security Considerations

The capability shall enforce authentication, role-based authorization, tenant isolation, Organization scope, Facility and Site access boundaries, sensitive data masking, secure references, and immutable audit logging.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Configure Batch Capacity Completed | Primary actor and configured stakeholders | In-App / Email | Action completes | Include reference, status, and effective date where applicable |
| Configure Batch Capacity Requires Approval | Approver | In-App | Approval rule applies | Include safe summary and requested action |
| Configure Batch Capacity Failed | Primary actor | In-App | Validation or processing fails | Include safe failure reason and next action |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| ConfigureBatchCapacityRequested | Batch / Class Management | Approval Workflow, Audit Service |
| ConfigureBatchCapacityCompleted | Batch / Class Management | Notification Service, Reporting Service, Audit Service |
| ConfigureBatchCapacityRejected | Batch / Class Management | Notification Service, Audit Service |

### Audit Events

| Audit Event | Description | Actor | Target Entity | Key Data |
|---|---|---|---|---|
| CONFIGURE_BATCH_CAPACITY_REQUESTED | Configure Batch Capacity requested | Facility Manager | Activity | Scope, reference, and reason |
| CONFIGURE_BATCH_CAPACITY_COMPLETED | Configure Batch Capacity completed | Facility Manager / System | Activity | Previous and new state |
| CONFIGURE_BATCH_CAPACITY_REJECTED | Configure Batch Capacity rejected | System | Activity | Rejection reason |

### Reports Generated

- Batch / Class Management Operational Report
- Batch / Class Management History Report
- Batch / Class Management Exception Report
- Executive Dashboard

### Related Screens

- Batch Capacity
- Batch / Class Management Dashboard
- Batch / Class Management History
- Audit Log Viewer

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/batches/{batchId}/capacity | PUT | Authorized token | Execute Configure Batch Capacity | 200 OK or 201 Created with result |
| /api/v1/batches/{batchId}/capacity/history | GET | Authorized token | Retrieve Configure Batch Capacity history | 200 OK with history |
| /api/v1/audit-logs | GET | Authorized token | Retrieve related audit events | 200 OK with scoped audit records |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Activity | Create / Update / Read | Support Configure Batch Capacity | Governed by Organization scope |
| Batch | Read / Insert | Support Configure Batch Capacity | Governed by Organization scope |
| Batch Schedule | Read / Insert | Support Configure Batch Capacity | Governed by Organization scope |
| Batch Capacity | Read / Insert | Support Configure Batch Capacity | Governed by Organization scope |
| Trainer Assignment | Read / Insert | Support Configure Batch Capacity | Governed by Organization scope |
| Audit Log | Insert | Record auditable activity | Immutable |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Draft | Configure Batch Capacity initiated | Configured | Facility Manager | Required data captured |
| Configured | Validation succeeds | Active | System | BA-02 rules satisfied |
| Active | Processing completes | Inactive | System | Related updates succeed |
| Active | Approval or policy failure | Archived | System / Approver | Request rejected |
| Inactive | View history | Inactive | Authorized user | Read-only historical access |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| BAT-008-001 | Configure Batch Capacity cannot be completed because required information is missing. | Missing mandatory data | Complete required fields |
| BAT-008-002 | You do not have permission to perform this action. | Authorization failure | Request access |
| BAT-008-003 | The selected record is not eligible for this action. | Policy or lifecycle violation | Review record status |
| BAT-008-004 | Configure Batch Capacity could not be completed due to a system or integration error. | Processing failure | Retry or contact support |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Execute Configure Batch Capacity | Given the actor has required permission and valid scope | When the actor submits valid information | Then the system shall complete Configure Batch Capacity successfully |
| Enforce validation | Given mandatory data or policy conditions are invalid | When the action is submitted | Then the system shall reject the request with a clear message |
| Preserve audit | Given the action completes or fails | When processing ends | Then audit events shall record actor, timestamp, scope, and outcome |
| Protect scope | Given the selected record is outside authorized scope | When the action is requested | Then the system shall deny access |

### Dependencies

- Facility Management
- Site Management
- Trainer Management
- Customer Management
- Membership Management
- Attendance Management
- Notification Management

### Operational Considerations

Configure Batch Capacity should be designed for high-volume operational use, retry-safe processing, clear exception handling, and support-team diagnostics without exposing sensitive data.

### Non-Functional Considerations

This requirement shall satisfy Digitize non-functional expectations for availability, reliability, performance, scalability, security, configurability, maintainability, and auditability.

### Assumptions

- Required master data and configuration are maintained by authorized users.
- Related services expose stable APIs for validation and synchronization.
- Organization policies define approval, retention, notification, and exception behavior.

### Success Criteria

Configure Batch Capacity is completed accurately, securely, and audibly, with downstream records synchronized and no loss of historical traceability.

### Related Functional Requirements

- FR-BAT-001 - Create Activity
- FR-BAT-002 - Update Activity
- FR-BAT-003 - Configure Activity Rules
- FR-BAT-004 - Create Batch
- FR-AUD-001 - Record Audit Events

### Notes

Configure Batch Capacity shall remain aligned with the approved BA source documents and shall not introduce behavior that bypasses tenant isolation, lifecycle governance, financial controls, or auditability.

---

## FR-BAT-009 - Enroll Customer into Batch

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-BAT-009 |
| Requirement Name | Enroll Customer into Batch |
| Functional Module | Batch / Class Management |
| Business Domain | Activity & Batch |
| Business Capability | Batch Enrollment |
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
| Business Requirement | BA-08 BR-016 Batch Scheduling |
| Business Rule | BA-02 BR-ATT-001, BR-ATT-006, BR-CUS-006, BR-SEC-004 |
| Business Process | BA-03 BP-ACT-009 Enroll Customer into Batch |
| Business Process Flow | BA-04 Section 21 Activity Management Flow, Section 22 Batch Management Flow |
| Persona | BA-05 Facility Manager, Trainer, Reception Staff, Customer |
| User Journey | BA-06 Section 5 Facility Manager Journey, Section 8 Trainer Journey, Section 17 Attendance Journey |
| Stakeholder | BA-07 Facility Manager, Trainer, Reception Staff, Customer |
| Non-Functional Requirement | BA-09 Section 2.8 Configurability, Section 2.4 Performance, Section 2.10 Auditability |
| Assumption / Constraint / Risk | BA-10 BA-ASS-011, BA-RSK-006 |

### Purpose

To enable Batch Enrollment within Batch / Class Management so Digitize can execute Enroll Customer into Batch consistently across Organizations, Facilities, Sites, users, and related operational or commercial services.

### Functional Requirement

The system shall support Enroll Customer into Batch as an atomic Batch / Class Management capability, including scoped data capture, business-rule validation, permission enforcement, lifecycle handling, related service synchronization, notification generation, reporting contribution, and immutable audit recording.

### Business Justification

Enroll Customer into Batch is required to preserve operational control, revenue accuracy, service continuity, customer trust, and enterprise traceability for Activity & Batch processes. Without this capability, downstream modules would rely on incomplete, manual, or inconsistent records.

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
- Actor has permission for Enroll Customer into Batch.
- Required Activity & Batch configuration and policies are available.
- Related records required by BA-03 BP-ACT-009 Enroll Customer into Batch are available and within authorized scope.

### Trigger

The capability is triggered when Reception Staff or the System initiates Enroll Customer into Batch from Batch Enrollment, a related workflow, a scheduled job, or an approved integration event.

### In Scope

- Capture or retrieve required Activity & Batch context.
- Validate Organization, Facility, Site, Customer, user, and policy scope where applicable.
- Execute Enroll Customer into Batch according to approved business rules.
- Persist the resulting Activity state or transaction.
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
- Activity reference
- Customer reference, where applicable
- Effective date and time, where applicable
- Status or action reason, where applicable
- Payment, billing, trainer, session, or subscription reference where applicable
- Actor remarks, where applicable

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Activity ID | Primary business record reference | Identifier | Yes | System / User | Must exist or be generated within scope | Core reference for Enroll Customer into Batch |
| Organization ID | Tenant Organization context | Identifier | Yes | Session / System | Must be Active and authorized | Enforces tenant isolation |
| Facility ID | Facility context | Identifier | Conditional | User / System | Must be Active where applicable | Required for facility-level operations |
| Site ID | Site context | Identifier | Conditional | User / System | Must belong to Facility where applicable | Required for site-level operations |
| Status | Lifecycle or processing state | Enum | Yes | System | Must follow allowed state transitions | Drives UI and downstream access |
| Effective Date | Date when action applies | DateTime | Conditional | User / System | Must satisfy policy | Supports scheduled or immediate actions |
| Reason / Remarks | Business explanation | Text | Conditional | User | Required for governed changes | Stored for audit |

### Main Flow

1. Actor opens Batch Enrollment or the related workflow.
2. The system validates authentication, authorization, tenant scope, and current operating context.
3. The system loads the required Activity & Batch records, related configuration, and policy controls.
4. Actor enters or confirms the information required to enroll customer into batch.
5. The system validates mandatory data, lifecycle status, ownership, eligibility, financial, capacity, schedule, and security rules where applicable.
6. The system executes Enroll Customer into Batch and persists the resulting Activity state or transaction.
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

- Activity record created, updated, validated, or reported according to the action.
- Lifecycle or processing status updated.
- Related history entry created.
- Business events emitted.
- Notifications generated where configured.
- Audit events recorded.
- Reports or dashboards updated where applicable.

### UI Behaviour

Batch Enrollment shall display scoped context, mandatory fields, lifecycle status, policy warnings, validation results, available actions, confirmation prompts, read-only states, pagination or filters where applicable, and responsive behavior for front-desk and administrative usage.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-BAT-009-001 | Actor must have permission to execute Enroll Customer into Batch. | Deny request and audit. | Critical |
| VAL-BAT-009-002 | Record must belong to the authorized Organization scope. | Deny request. | Critical |
| VAL-BAT-009-003 | Mandatory inputs must be complete and valid. | Block submission. | Critical |
| VAL-BAT-009-004 | Lifecycle and policy rules from BA-02 must be satisfied. | Reject or route for approval. | High |
| VAL-BAT-009-005 | Historical and audit records must be preserved. | Roll back or mark for recovery. | Critical |

### Business Rules

- BA-02 BR-ATT-001
- BA-02 BR-ATT-006
- BA-02 BR-CUS-006
- BA-02 BR-SEC-004

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| bat.enroll.customer.into.batch.view | Reception Staff | Read | View Enroll Customer into Batch context |
| bat.enroll.customer.into.batch.execute | Reception Staff | Execute | Execute Enroll Customer into Batch |
| bat.enroll.customer.into.batch.approve | Organization Administrator | Approve | Approve governed exceptions where configured |
| bat.enroll.customer.into.batch.audit.view | Organization Administrator / Support Executive | Read | View audit trace |

### Security Considerations

The capability shall enforce authentication, role-based authorization, tenant isolation, Organization scope, Facility and Site access boundaries, sensitive data masking, secure references, and immutable audit logging.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Enroll Customer into Batch Completed | Primary actor and configured stakeholders | In-App / Email | Action completes | Include reference, status, and effective date where applicable |
| Enroll Customer into Batch Requires Approval | Approver | In-App | Approval rule applies | Include safe summary and requested action |
| Enroll Customer into Batch Failed | Primary actor | In-App | Validation or processing fails | Include safe failure reason and next action |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| EnrollCustomerIntoBatchRequested | Batch / Class Management | Approval Workflow, Audit Service |
| EnrollCustomerIntoBatchCompleted | Batch / Class Management | Notification Service, Reporting Service, Audit Service |
| EnrollCustomerIntoBatchRejected | Batch / Class Management | Notification Service, Audit Service |

### Audit Events

| Audit Event | Description | Actor | Target Entity | Key Data |
|---|---|---|---|---|
| ENROLL_CUSTOMER_INTO_BATCH_REQUESTED | Enroll Customer into Batch requested | Reception Staff | Activity | Scope, reference, and reason |
| ENROLL_CUSTOMER_INTO_BATCH_COMPLETED | Enroll Customer into Batch completed | Reception Staff / System | Activity | Previous and new state |
| ENROLL_CUSTOMER_INTO_BATCH_REJECTED | Enroll Customer into Batch rejected | System | Activity | Rejection reason |

### Reports Generated

- Batch / Class Management Operational Report
- Batch / Class Management History Report
- Batch / Class Management Exception Report
- Executive Dashboard

### Related Screens

- Batch Enrollment
- Batch / Class Management Dashboard
- Batch / Class Management History
- Audit Log Viewer

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/batches/{batchId}/enrollments | POST | Authorized token | Execute Enroll Customer into Batch | 200 OK or 201 Created with result |
| /api/v1/batches/{batchId}/enrollments/history | GET | Authorized token | Retrieve Enroll Customer into Batch history | 200 OK with history |
| /api/v1/audit-logs | GET | Authorized token | Retrieve related audit events | 200 OK with scoped audit records |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Activity | Create / Update / Read | Support Enroll Customer into Batch | Governed by Organization scope |
| Batch | Read / Insert | Support Enroll Customer into Batch | Governed by Organization scope |
| Batch Schedule | Read / Insert | Support Enroll Customer into Batch | Governed by Organization scope |
| Batch Capacity | Read / Insert | Support Enroll Customer into Batch | Governed by Organization scope |
| Trainer Assignment | Read / Insert | Support Enroll Customer into Batch | Governed by Organization scope |
| Audit Log | Insert | Record auditable activity | Immutable |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Draft | Enroll Customer into Batch initiated | Validated | Reception Staff | Required data captured |
| Validated | Validation succeeds | Pending Approval | System | BA-02 rules satisfied |
| Pending Approval | Processing completes | Completed | System | Related updates succeed |
| Pending Approval | Approval or policy failure | Rejected | System / Approver | Request rejected |
| Completed | View history | Completed | Authorized user | Read-only historical access |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| BAT-009-001 | Enroll Customer into Batch cannot be completed because required information is missing. | Missing mandatory data | Complete required fields |
| BAT-009-002 | You do not have permission to perform this action. | Authorization failure | Request access |
| BAT-009-003 | The selected record is not eligible for this action. | Policy or lifecycle violation | Review record status |
| BAT-009-004 | Enroll Customer into Batch could not be completed due to a system or integration error. | Processing failure | Retry or contact support |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Execute Enroll Customer into Batch | Given the actor has required permission and valid scope | When the actor submits valid information | Then the system shall complete Enroll Customer into Batch successfully |
| Enforce validation | Given mandatory data or policy conditions are invalid | When the action is submitted | Then the system shall reject the request with a clear message |
| Preserve audit | Given the action completes or fails | When processing ends | Then audit events shall record actor, timestamp, scope, and outcome |
| Protect scope | Given the selected record is outside authorized scope | When the action is requested | Then the system shall deny access |

### Dependencies

- Facility Management
- Site Management
- Trainer Management
- Customer Management
- Membership Management
- Attendance Management
- Notification Management

### Operational Considerations

Enroll Customer into Batch should be designed for high-volume operational use, retry-safe processing, clear exception handling, and support-team diagnostics without exposing sensitive data.

### Non-Functional Considerations

This requirement shall satisfy Digitize non-functional expectations for availability, reliability, performance, scalability, security, configurability, maintainability, and auditability.

### Assumptions

- Required master data and configuration are maintained by authorized users.
- Related services expose stable APIs for validation and synchronization.
- Organization policies define approval, retention, notification, and exception behavior.

### Success Criteria

Enroll Customer into Batch is completed accurately, securely, and audibly, with downstream records synchronized and no loss of historical traceability.

### Related Functional Requirements

- FR-BAT-001 - Create Activity
- FR-BAT-002 - Update Activity
- FR-BAT-003 - Configure Activity Rules
- FR-BAT-004 - Create Batch
- FR-AUD-001 - Record Audit Events

### Notes

Enroll Customer into Batch shall remain aligned with the approved BA source documents and shall not introduce behavior that bypasses tenant isolation, lifecycle governance, financial controls, or auditability.

---

## FR-BAT-010 - Remove Customer from Batch

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-BAT-010 |
| Requirement Name | Remove Customer from Batch |
| Functional Module | Batch / Class Management |
| Business Domain | Activity & Batch |
| Business Capability | Batch Enrollment |
| Requirement Type | Functional |
| Requirement Category | Workflow |
| Requirement Version | 1.0 |
| Requirement Status | Approved |
| Priority | Medium |
| Complexity | Medium |
| Release Version | 1.0 |
| Owner | Product Management |

### Traceability References

| Traceability Type | Reference |
|---|---|
| Business Requirement | BA-08 BR-016 Batch Scheduling |
| Business Rule | BA-02 BR-ATT-009, BR-CUS-009, BR-AUD-003, BR-SEC-004 |
| Business Process | BA-03 BP-ACT-010 Remove Customer from Batch |
| Business Process Flow | BA-04 Section 21 Activity Management Flow, Section 22 Batch Management Flow |
| Persona | BA-05 Facility Manager, Trainer, Reception Staff, Customer |
| User Journey | BA-06 Section 5 Facility Manager Journey, Section 8 Trainer Journey, Section 17 Attendance Journey |
| Stakeholder | BA-07 Facility Manager, Trainer, Reception Staff, Customer |
| Non-Functional Requirement | BA-09 Section 2.8 Configurability, Section 2.4 Performance, Section 2.10 Auditability |
| Assumption / Constraint / Risk | BA-10 BA-ASS-011, BA-RSK-006 |

### Purpose

To enable Batch Enrollment within Batch / Class Management so Digitize can execute Remove Customer from Batch consistently across Organizations, Facilities, Sites, users, and related operational or commercial services.

### Functional Requirement

The system shall support Remove Customer from Batch as an atomic Batch / Class Management capability, including scoped data capture, business-rule validation, permission enforcement, lifecycle handling, related service synchronization, notification generation, reporting contribution, and immutable audit recording.

### Business Justification

Remove Customer from Batch is required to preserve operational control, revenue accuracy, service continuity, customer trust, and enterprise traceability for Activity & Batch processes. Without this capability, downstream modules would rely on incomplete, manual, or inconsistent records.

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
- Actor has permission for Remove Customer from Batch.
- Required Activity & Batch configuration and policies are available.
- Related records required by BA-03 BP-ACT-010 Remove Customer from Batch are available and within authorized scope.

### Trigger

The capability is triggered when Reception Staff or the System initiates Remove Customer from Batch from Batch Enrollment, a related workflow, a scheduled job, or an approved integration event.

### In Scope

- Capture or retrieve required Activity & Batch context.
- Validate Organization, Facility, Site, Customer, user, and policy scope where applicable.
- Execute Remove Customer from Batch according to approved business rules.
- Persist the resulting Activity state or transaction.
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
- Activity reference
- Customer reference, where applicable
- Effective date and time, where applicable
- Status or action reason, where applicable
- Payment, billing, trainer, session, or subscription reference where applicable
- Actor remarks, where applicable

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Activity ID | Primary business record reference | Identifier | Yes | System / User | Must exist or be generated within scope | Core reference for Remove Customer from Batch |
| Organization ID | Tenant Organization context | Identifier | Yes | Session / System | Must be Active and authorized | Enforces tenant isolation |
| Facility ID | Facility context | Identifier | Conditional | User / System | Must be Active where applicable | Required for facility-level operations |
| Site ID | Site context | Identifier | Conditional | User / System | Must belong to Facility where applicable | Required for site-level operations |
| Status | Lifecycle or processing state | Enum | Yes | System | Must follow allowed state transitions | Drives UI and downstream access |
| Effective Date | Date when action applies | DateTime | Conditional | User / System | Must satisfy policy | Supports scheduled or immediate actions |
| Reason / Remarks | Business explanation | Text | Conditional | User | Required for governed changes | Stored for audit |

### Main Flow

1. Actor opens Batch Enrollment or the related workflow.
2. The system validates authentication, authorization, tenant scope, and current operating context.
3. The system loads the required Activity & Batch records, related configuration, and policy controls.
4. Actor enters or confirms the information required to remove customer from batch.
5. The system validates mandatory data, lifecycle status, ownership, eligibility, financial, capacity, schedule, and security rules where applicable.
6. The system executes Remove Customer from Batch and persists the resulting Activity state or transaction.
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

- Activity record created, updated, validated, or reported according to the action.
- Lifecycle or processing status updated.
- Related history entry created.
- Business events emitted.
- Notifications generated where configured.
- Audit events recorded.
- Reports or dashboards updated where applicable.

### UI Behaviour

Batch Enrollment shall display scoped context, mandatory fields, lifecycle status, policy warnings, validation results, available actions, confirmation prompts, read-only states, pagination or filters where applicable, and responsive behavior for front-desk and administrative usage.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-BAT-010-001 | Actor must have permission to execute Remove Customer from Batch. | Deny request and audit. | Critical |
| VAL-BAT-010-002 | Record must belong to the authorized Organization scope. | Deny request. | Critical |
| VAL-BAT-010-003 | Mandatory inputs must be complete and valid. | Block submission. | Critical |
| VAL-BAT-010-004 | Lifecycle and policy rules from BA-02 must be satisfied. | Reject or route for approval. | High |
| VAL-BAT-010-005 | Historical and audit records must be preserved. | Roll back or mark for recovery. | Critical |

### Business Rules

- BA-02 BR-ATT-009
- BA-02 BR-CUS-009
- BA-02 BR-AUD-003
- BA-02 BR-SEC-004

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| bat.remove.customer.from.batch.view | Reception Staff | Read | View Remove Customer from Batch context |
| bat.remove.customer.from.batch.execute | Reception Staff | Execute | Execute Remove Customer from Batch |
| bat.remove.customer.from.batch.approve | Organization Administrator | Approve | Approve governed exceptions where configured |
| bat.remove.customer.from.batch.audit.view | Organization Administrator / Support Executive | Read | View audit trace |

### Security Considerations

The capability shall enforce authentication, role-based authorization, tenant isolation, Organization scope, Facility and Site access boundaries, sensitive data masking, secure references, and immutable audit logging.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Remove Customer from Batch Completed | Primary actor and configured stakeholders | In-App / Email | Action completes | Include reference, status, and effective date where applicable |
| Remove Customer from Batch Requires Approval | Approver | In-App | Approval rule applies | Include safe summary and requested action |
| Remove Customer from Batch Failed | Primary actor | In-App | Validation or processing fails | Include safe failure reason and next action |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| RemoveCustomerFromBatchRequested | Batch / Class Management | Approval Workflow, Audit Service |
| RemoveCustomerFromBatchCompleted | Batch / Class Management | Notification Service, Reporting Service, Audit Service |
| RemoveCustomerFromBatchRejected | Batch / Class Management | Notification Service, Audit Service |

### Audit Events

| Audit Event | Description | Actor | Target Entity | Key Data |
|---|---|---|---|---|
| REMOVE_CUSTOMER_FROM_BATCH_REQUESTED | Remove Customer from Batch requested | Reception Staff | Activity | Scope, reference, and reason |
| REMOVE_CUSTOMER_FROM_BATCH_COMPLETED | Remove Customer from Batch completed | Reception Staff / System | Activity | Previous and new state |
| REMOVE_CUSTOMER_FROM_BATCH_REJECTED | Remove Customer from Batch rejected | System | Activity | Rejection reason |

### Reports Generated

- Batch / Class Management Operational Report
- Batch / Class Management History Report
- Batch / Class Management Exception Report
- Executive Dashboard

### Related Screens

- Batch Enrollment
- Batch / Class Management Dashboard
- Batch / Class Management History
- Audit Log Viewer

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/batches/{batchId}/enrollments/{enrollmentId} | DELETE | Authorized token | Execute Remove Customer from Batch | 200 OK or 201 Created with result |
| /api/v1/batches/{batchId}/enrollments/{enrollmentId}/history | GET | Authorized token | Retrieve Remove Customer from Batch history | 200 OK with history |
| /api/v1/audit-logs | GET | Authorized token | Retrieve related audit events | 200 OK with scoped audit records |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Activity | Create / Update / Read | Support Remove Customer from Batch | Governed by Organization scope |
| Batch | Read / Insert | Support Remove Customer from Batch | Governed by Organization scope |
| Batch Schedule | Read / Insert | Support Remove Customer from Batch | Governed by Organization scope |
| Batch Capacity | Read / Insert | Support Remove Customer from Batch | Governed by Organization scope |
| Trainer Assignment | Read / Insert | Support Remove Customer from Batch | Governed by Organization scope |
| Audit Log | Insert | Record auditable activity | Immutable |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Draft | Remove Customer from Batch initiated | Validated | Reception Staff | Required data captured |
| Validated | Validation succeeds | Pending Approval | System | BA-02 rules satisfied |
| Pending Approval | Processing completes | Completed | System | Related updates succeed |
| Pending Approval | Approval or policy failure | Rejected | System / Approver | Request rejected |
| Completed | View history | Completed | Authorized user | Read-only historical access |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| BAT-010-001 | Remove Customer from Batch cannot be completed because required information is missing. | Missing mandatory data | Complete required fields |
| BAT-010-002 | You do not have permission to perform this action. | Authorization failure | Request access |
| BAT-010-003 | The selected record is not eligible for this action. | Policy or lifecycle violation | Review record status |
| BAT-010-004 | Remove Customer from Batch could not be completed due to a system or integration error. | Processing failure | Retry or contact support |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Execute Remove Customer from Batch | Given the actor has required permission and valid scope | When the actor submits valid information | Then the system shall complete Remove Customer from Batch successfully |
| Enforce validation | Given mandatory data or policy conditions are invalid | When the action is submitted | Then the system shall reject the request with a clear message |
| Preserve audit | Given the action completes or fails | When processing ends | Then audit events shall record actor, timestamp, scope, and outcome |
| Protect scope | Given the selected record is outside authorized scope | When the action is requested | Then the system shall deny access |

### Dependencies

- Facility Management
- Site Management
- Trainer Management
- Customer Management
- Membership Management
- Attendance Management
- Notification Management

### Operational Considerations

Remove Customer from Batch should be designed for high-volume operational use, retry-safe processing, clear exception handling, and support-team diagnostics without exposing sensitive data.

### Non-Functional Considerations

This requirement shall satisfy Digitize non-functional expectations for availability, reliability, performance, scalability, security, configurability, maintainability, and auditability.

### Assumptions

- Required master data and configuration are maintained by authorized users.
- Related services expose stable APIs for validation and synchronization.
- Organization policies define approval, retention, notification, and exception behavior.

### Success Criteria

Remove Customer from Batch is completed accurately, securely, and audibly, with downstream records synchronized and no loss of historical traceability.

### Related Functional Requirements

- FR-BAT-001 - Create Activity
- FR-BAT-002 - Update Activity
- FR-BAT-003 - Configure Activity Rules
- FR-BAT-004 - Create Batch
- FR-AUD-001 - Record Audit Events

### Notes

Remove Customer from Batch shall remain aligned with the approved BA source documents and shall not introduce behavior that bypasses tenant isolation, lifecycle governance, financial controls, or auditability.

---

## FR-BAT-011 - Start Session

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-BAT-011 |
| Requirement Name | Start Session |
| Functional Module | Batch / Class Management |
| Business Domain | Activity & Batch |
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
| Business Requirement | BA-08 BR-016 Batch Scheduling |
| Business Rule | BA-02 BR-TRN-004, BR-TRN-007, BR-ATT-002, BR-SEC-004 |
| Business Process | BA-03 BP-ACT-011 Start Session |
| Business Process Flow | BA-04 Section 21 Activity Management Flow, Section 22 Batch Management Flow |
| Persona | BA-05 Facility Manager, Trainer, Reception Staff, Customer |
| User Journey | BA-06 Section 5 Facility Manager Journey, Section 8 Trainer Journey, Section 17 Attendance Journey |
| Stakeholder | BA-07 Facility Manager, Trainer, Reception Staff, Customer |
| Non-Functional Requirement | BA-09 Section 2.8 Configurability, Section 2.4 Performance, Section 2.10 Auditability |
| Assumption / Constraint / Risk | BA-10 BA-ASS-011, BA-RSK-006 |

### Purpose

To enable Session Management within Batch / Class Management so Digitize can execute Start Session consistently across Organizations, Facilities, Sites, users, and related operational or commercial services.

### Functional Requirement

The system shall support Start Session as an atomic Batch / Class Management capability, including scoped data capture, business-rule validation, permission enforcement, lifecycle handling, related service synchronization, notification generation, reporting contribution, and immutable audit recording.

### Business Justification

Start Session is required to preserve operational control, revenue accuracy, service continuity, customer trust, and enterprise traceability for Activity & Batch processes. Without this capability, downstream modules would rely on incomplete, manual, or inconsistent records.

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
- Actor has permission for Start Session.
- Required Activity & Batch configuration and policies are available.
- Related records required by BA-03 BP-ACT-011 Start Session are available and within authorized scope.

### Trigger

The capability is triggered when Trainer or the System initiates Start Session from Batch Session, a related workflow, a scheduled job, or an approved integration event.

### In Scope

- Capture or retrieve required Activity & Batch context.
- Validate Organization, Facility, Site, Customer, user, and policy scope where applicable.
- Execute Start Session according to approved business rules.
- Persist the resulting Activity state or transaction.
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
- Activity reference
- Customer reference, where applicable
- Effective date and time, where applicable
- Status or action reason, where applicable
- Payment, billing, trainer, session, or subscription reference where applicable
- Actor remarks, where applicable

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Activity ID | Primary business record reference | Identifier | Yes | System / User | Must exist or be generated within scope | Core reference for Start Session |
| Organization ID | Tenant Organization context | Identifier | Yes | Session / System | Must be Active and authorized | Enforces tenant isolation |
| Facility ID | Facility context | Identifier | Conditional | User / System | Must be Active where applicable | Required for facility-level operations |
| Site ID | Site context | Identifier | Conditional | User / System | Must belong to Facility where applicable | Required for site-level operations |
| Status | Lifecycle or processing state | Enum | Yes | System | Must follow allowed state transitions | Drives UI and downstream access |
| Effective Date | Date when action applies | DateTime | Conditional | User / System | Must satisfy policy | Supports scheduled or immediate actions |
| Reason / Remarks | Business explanation | Text | Conditional | User | Required for governed changes | Stored for audit |

### Main Flow

1. Actor opens Batch Session or the related workflow.
2. The system validates authentication, authorization, tenant scope, and current operating context.
3. The system loads the required Activity & Batch records, related configuration, and policy controls.
4. Actor enters or confirms the information required to start session.
5. The system validates mandatory data, lifecycle status, ownership, eligibility, financial, capacity, schedule, and security rules where applicable.
6. The system executes Start Session and persists the resulting Activity state or transaction.
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

- Activity record created, updated, validated, or reported according to the action.
- Lifecycle or processing status updated.
- Related history entry created.
- Business events emitted.
- Notifications generated where configured.
- Audit events recorded.
- Reports or dashboards updated where applicable.

### UI Behaviour

Batch Session shall display scoped context, mandatory fields, lifecycle status, policy warnings, validation results, available actions, confirmation prompts, read-only states, pagination or filters where applicable, and responsive behavior for front-desk and administrative usage.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-BAT-011-001 | Actor must have permission to execute Start Session. | Deny request and audit. | Critical |
| VAL-BAT-011-002 | Record must belong to the authorized Organization scope. | Deny request. | Critical |
| VAL-BAT-011-003 | Mandatory inputs must be complete and valid. | Block submission. | Critical |
| VAL-BAT-011-004 | Lifecycle and policy rules from BA-02 must be satisfied. | Reject or route for approval. | High |
| VAL-BAT-011-005 | Historical and audit records must be preserved. | Roll back or mark for recovery. | Critical |

### Business Rules

- BA-02 BR-TRN-004
- BA-02 BR-TRN-007
- BA-02 BR-ATT-002
- BA-02 BR-SEC-004

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| bat.start.session.view | Trainer | Read | View Start Session context |
| bat.start.session.execute | Trainer | Execute | Execute Start Session |
| bat.start.session.approve | Organization Administrator | Approve | Approve governed exceptions where configured |
| bat.start.session.audit.view | Organization Administrator / Support Executive | Read | View audit trace |

### Security Considerations

The capability shall enforce authentication, role-based authorization, tenant isolation, Organization scope, Facility and Site access boundaries, sensitive data masking, secure references, and immutable audit logging.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Start Session Completed | Primary actor and configured stakeholders | In-App / Email | Action completes | Include reference, status, and effective date where applicable |
| Start Session Requires Approval | Approver | In-App | Approval rule applies | Include safe summary and requested action |
| Start Session Failed | Primary actor | In-App | Validation or processing fails | Include safe failure reason and next action |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| StartSessionRequested | Batch / Class Management | Approval Workflow, Audit Service |
| StartSessionCompleted | Batch / Class Management | Notification Service, Reporting Service, Audit Service |
| StartSessionRejected | Batch / Class Management | Notification Service, Audit Service |

### Audit Events

| Audit Event | Description | Actor | Target Entity | Key Data |
|---|---|---|---|---|
| START_SESSION_REQUESTED | Start Session requested | Trainer | Activity | Scope, reference, and reason |
| START_SESSION_COMPLETED | Start Session completed | Trainer / System | Activity | Previous and new state |
| START_SESSION_REJECTED | Start Session rejected | System | Activity | Rejection reason |

### Reports Generated

- Batch / Class Management Operational Report
- Batch / Class Management History Report
- Batch / Class Management Exception Report
- Executive Dashboard

### Related Screens

- Batch Session
- Batch / Class Management Dashboard
- Batch / Class Management History
- Audit Log Viewer

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/batch-sessions/{sessionId}/start | POST | Authorized token | Execute Start Session | 200 OK or 201 Created with result |
| /api/v1/batch-sessions/{sessionId}/start/history | GET | Authorized token | Retrieve Start Session history | 200 OK with history |
| /api/v1/audit-logs | GET | Authorized token | Retrieve related audit events | 200 OK with scoped audit records |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Activity | Create / Update / Read | Support Start Session | Governed by Organization scope |
| Batch | Read / Insert | Support Start Session | Governed by Organization scope |
| Batch Schedule | Read / Insert | Support Start Session | Governed by Organization scope |
| Batch Capacity | Read / Insert | Support Start Session | Governed by Organization scope |
| Trainer Assignment | Read / Insert | Support Start Session | Governed by Organization scope |
| Audit Log | Insert | Record auditable activity | Immutable |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Draft | Start Session initiated | Validated | Trainer | Required data captured |
| Validated | Validation succeeds | Pending Approval | System | BA-02 rules satisfied |
| Pending Approval | Processing completes | Completed | System | Related updates succeed |
| Pending Approval | Approval or policy failure | Rejected | System / Approver | Request rejected |
| Completed | View history | Completed | Authorized user | Read-only historical access |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| BAT-011-001 | Start Session cannot be completed because required information is missing. | Missing mandatory data | Complete required fields |
| BAT-011-002 | You do not have permission to perform this action. | Authorization failure | Request access |
| BAT-011-003 | The selected record is not eligible for this action. | Policy or lifecycle violation | Review record status |
| BAT-011-004 | Start Session could not be completed due to a system or integration error. | Processing failure | Retry or contact support |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Execute Start Session | Given the actor has required permission and valid scope | When the actor submits valid information | Then the system shall complete Start Session successfully |
| Enforce validation | Given mandatory data or policy conditions are invalid | When the action is submitted | Then the system shall reject the request with a clear message |
| Preserve audit | Given the action completes or fails | When processing ends | Then audit events shall record actor, timestamp, scope, and outcome |
| Protect scope | Given the selected record is outside authorized scope | When the action is requested | Then the system shall deny access |

### Dependencies

- Facility Management
- Site Management
- Trainer Management
- Customer Management
- Membership Management
- Attendance Management
- Notification Management

### Operational Considerations

Start Session should be designed for high-volume operational use, retry-safe processing, clear exception handling, and support-team diagnostics without exposing sensitive data.

### Non-Functional Considerations

This requirement shall satisfy Digitize non-functional expectations for availability, reliability, performance, scalability, security, configurability, maintainability, and auditability.

### Assumptions

- Required master data and configuration are maintained by authorized users.
- Related services expose stable APIs for validation and synchronization.
- Organization policies define approval, retention, notification, and exception behavior.

### Success Criteria

Start Session is completed accurately, securely, and audibly, with downstream records synchronized and no loss of historical traceability.

### Related Functional Requirements

- FR-BAT-001 - Create Activity
- FR-BAT-002 - Update Activity
- FR-BAT-003 - Configure Activity Rules
- FR-BAT-004 - Create Batch
- FR-AUD-001 - Record Audit Events

### Notes

Start Session shall remain aligned with the approved BA source documents and shall not introduce behavior that bypasses tenant isolation, lifecycle governance, financial controls, or auditability.

---

## FR-BAT-012 - Complete Session

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-BAT-012 |
| Requirement Name | Complete Session |
| Functional Module | Batch / Class Management |
| Business Domain | Activity & Batch |
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
| Business Requirement | BA-08 BR-016 Batch Scheduling |
| Business Rule | BA-02 BR-TRN-007, BR-ATT-009, BR-AUD-003, BR-SEC-004 |
| Business Process | BA-03 BP-ACT-012 Complete Session |
| Business Process Flow | BA-04 Section 21 Activity Management Flow, Section 22 Batch Management Flow |
| Persona | BA-05 Facility Manager, Trainer, Reception Staff, Customer |
| User Journey | BA-06 Section 5 Facility Manager Journey, Section 8 Trainer Journey, Section 17 Attendance Journey |
| Stakeholder | BA-07 Facility Manager, Trainer, Reception Staff, Customer |
| Non-Functional Requirement | BA-09 Section 2.8 Configurability, Section 2.4 Performance, Section 2.10 Auditability |
| Assumption / Constraint / Risk | BA-10 BA-ASS-011, BA-RSK-006 |

### Purpose

To enable Session Management within Batch / Class Management so Digitize can execute Complete Session consistently across Organizations, Facilities, Sites, users, and related operational or commercial services.

### Functional Requirement

The system shall support Complete Session as an atomic Batch / Class Management capability, including scoped data capture, business-rule validation, permission enforcement, lifecycle handling, related service synchronization, notification generation, reporting contribution, and immutable audit recording.

### Business Justification

Complete Session is required to preserve operational control, revenue accuracy, service continuity, customer trust, and enterprise traceability for Activity & Batch processes. Without this capability, downstream modules would rely on incomplete, manual, or inconsistent records.

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
- Actor has permission for Complete Session.
- Required Activity & Batch configuration and policies are available.
- Related records required by BA-03 BP-ACT-012 Complete Session are available and within authorized scope.

### Trigger

The capability is triggered when Trainer or the System initiates Complete Session from Batch Session, a related workflow, a scheduled job, or an approved integration event.

### In Scope

- Capture or retrieve required Activity & Batch context.
- Validate Organization, Facility, Site, Customer, user, and policy scope where applicable.
- Execute Complete Session according to approved business rules.
- Persist the resulting Activity state or transaction.
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
- Activity reference
- Customer reference, where applicable
- Effective date and time, where applicable
- Status or action reason, where applicable
- Payment, billing, trainer, session, or subscription reference where applicable
- Actor remarks, where applicable

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Activity ID | Primary business record reference | Identifier | Yes | System / User | Must exist or be generated within scope | Core reference for Complete Session |
| Organization ID | Tenant Organization context | Identifier | Yes | Session / System | Must be Active and authorized | Enforces tenant isolation |
| Facility ID | Facility context | Identifier | Conditional | User / System | Must be Active where applicable | Required for facility-level operations |
| Site ID | Site context | Identifier | Conditional | User / System | Must belong to Facility where applicable | Required for site-level operations |
| Status | Lifecycle or processing state | Enum | Yes | System | Must follow allowed state transitions | Drives UI and downstream access |
| Effective Date | Date when action applies | DateTime | Conditional | User / System | Must satisfy policy | Supports scheduled or immediate actions |
| Reason / Remarks | Business explanation | Text | Conditional | User | Required for governed changes | Stored for audit |

### Main Flow

1. Actor opens Batch Session or the related workflow.
2. The system validates authentication, authorization, tenant scope, and current operating context.
3. The system loads the required Activity & Batch records, related configuration, and policy controls.
4. Actor enters or confirms the information required to complete session.
5. The system validates mandatory data, lifecycle status, ownership, eligibility, financial, capacity, schedule, and security rules where applicable.
6. The system executes Complete Session and persists the resulting Activity state or transaction.
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

- Activity record created, updated, validated, or reported according to the action.
- Lifecycle or processing status updated.
- Related history entry created.
- Business events emitted.
- Notifications generated where configured.
- Audit events recorded.
- Reports or dashboards updated where applicable.

### UI Behaviour

Batch Session shall display scoped context, mandatory fields, lifecycle status, policy warnings, validation results, available actions, confirmation prompts, read-only states, pagination or filters where applicable, and responsive behavior for front-desk and administrative usage.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-BAT-012-001 | Actor must have permission to execute Complete Session. | Deny request and audit. | Critical |
| VAL-BAT-012-002 | Record must belong to the authorized Organization scope. | Deny request. | Critical |
| VAL-BAT-012-003 | Mandatory inputs must be complete and valid. | Block submission. | Critical |
| VAL-BAT-012-004 | Lifecycle and policy rules from BA-02 must be satisfied. | Reject or route for approval. | High |
| VAL-BAT-012-005 | Historical and audit records must be preserved. | Roll back or mark for recovery. | Critical |

### Business Rules

- BA-02 BR-TRN-007
- BA-02 BR-ATT-009
- BA-02 BR-AUD-003
- BA-02 BR-SEC-004

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| bat.complete.session.view | Trainer | Read | View Complete Session context |
| bat.complete.session.execute | Trainer | Execute | Execute Complete Session |
| bat.complete.session.approve | Organization Administrator | Approve | Approve governed exceptions where configured |
| bat.complete.session.audit.view | Organization Administrator / Support Executive | Read | View audit trace |

### Security Considerations

The capability shall enforce authentication, role-based authorization, tenant isolation, Organization scope, Facility and Site access boundaries, sensitive data masking, secure references, and immutable audit logging.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Complete Session Completed | Primary actor and configured stakeholders | In-App / Email | Action completes | Include reference, status, and effective date where applicable |
| Complete Session Requires Approval | Approver | In-App | Approval rule applies | Include safe summary and requested action |
| Complete Session Failed | Primary actor | In-App | Validation or processing fails | Include safe failure reason and next action |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| CompleteSessionRequested | Batch / Class Management | Approval Workflow, Audit Service |
| CompleteSessionCompleted | Batch / Class Management | Notification Service, Reporting Service, Audit Service |
| CompleteSessionRejected | Batch / Class Management | Notification Service, Audit Service |

### Audit Events

| Audit Event | Description | Actor | Target Entity | Key Data |
|---|---|---|---|---|
| COMPLETE_SESSION_REQUESTED | Complete Session requested | Trainer | Activity | Scope, reference, and reason |
| COMPLETE_SESSION_COMPLETED | Complete Session completed | Trainer / System | Activity | Previous and new state |
| COMPLETE_SESSION_REJECTED | Complete Session rejected | System | Activity | Rejection reason |

### Reports Generated

- Batch / Class Management Operational Report
- Batch / Class Management History Report
- Batch / Class Management Exception Report
- Executive Dashboard

### Related Screens

- Batch Session
- Batch / Class Management Dashboard
- Batch / Class Management History
- Audit Log Viewer

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/batch-sessions/{sessionId}/complete | POST | Authorized token | Execute Complete Session | 200 OK or 201 Created with result |
| /api/v1/batch-sessions/{sessionId}/complete/history | GET | Authorized token | Retrieve Complete Session history | 200 OK with history |
| /api/v1/audit-logs | GET | Authorized token | Retrieve related audit events | 200 OK with scoped audit records |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Activity | Create / Update / Read | Support Complete Session | Governed by Organization scope |
| Batch | Read / Insert | Support Complete Session | Governed by Organization scope |
| Batch Schedule | Read / Insert | Support Complete Session | Governed by Organization scope |
| Batch Capacity | Read / Insert | Support Complete Session | Governed by Organization scope |
| Trainer Assignment | Read / Insert | Support Complete Session | Governed by Organization scope |
| Audit Log | Insert | Record auditable activity | Immutable |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Draft | Complete Session initiated | Validated | Trainer | Required data captured |
| Validated | Validation succeeds | Pending Approval | System | BA-02 rules satisfied |
| Pending Approval | Processing completes | Completed | System | Related updates succeed |
| Pending Approval | Approval or policy failure | Rejected | System / Approver | Request rejected |
| Completed | View history | Completed | Authorized user | Read-only historical access |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| BAT-012-001 | Complete Session cannot be completed because required information is missing. | Missing mandatory data | Complete required fields |
| BAT-012-002 | You do not have permission to perform this action. | Authorization failure | Request access |
| BAT-012-003 | The selected record is not eligible for this action. | Policy or lifecycle violation | Review record status |
| BAT-012-004 | Complete Session could not be completed due to a system or integration error. | Processing failure | Retry or contact support |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Execute Complete Session | Given the actor has required permission and valid scope | When the actor submits valid information | Then the system shall complete Complete Session successfully |
| Enforce validation | Given mandatory data or policy conditions are invalid | When the action is submitted | Then the system shall reject the request with a clear message |
| Preserve audit | Given the action completes or fails | When processing ends | Then audit events shall record actor, timestamp, scope, and outcome |
| Protect scope | Given the selected record is outside authorized scope | When the action is requested | Then the system shall deny access |

### Dependencies

- Facility Management
- Site Management
- Trainer Management
- Customer Management
- Membership Management
- Attendance Management
- Notification Management

### Operational Considerations

Complete Session should be designed for high-volume operational use, retry-safe processing, clear exception handling, and support-team diagnostics without exposing sensitive data.

### Non-Functional Considerations

This requirement shall satisfy Digitize non-functional expectations for availability, reliability, performance, scalability, security, configurability, maintainability, and auditability.

### Assumptions

- Required master data and configuration are maintained by authorized users.
- Related services expose stable APIs for validation and synchronization.
- Organization policies define approval, retention, notification, and exception behavior.

### Success Criteria

Complete Session is completed accurately, securely, and audibly, with downstream records synchronized and no loss of historical traceability.

### Related Functional Requirements

- FR-BAT-001 - Create Activity
- FR-BAT-002 - Update Activity
- FR-BAT-003 - Configure Activity Rules
- FR-BAT-004 - Create Batch
- FR-AUD-001 - Record Audit Events

### Notes

Complete Session shall remain aligned with the approved BA source documents and shall not introduce behavior that bypasses tenant isolation, lifecycle governance, financial controls, or auditability.

---

## FR-BAT-013 - Cancel Session

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-BAT-013 |
| Requirement Name | Cancel Session |
| Functional Module | Batch / Class Management |
| Business Domain | Activity & Batch |
| Business Capability | Session Administration |
| Requirement Type | Functional |
| Requirement Category | Workflow |
| Requirement Version | 1.0 |
| Requirement Status | Approved |
| Priority | Medium |
| Complexity | Medium |
| Release Version | 1.0 |
| Owner | Product Management |

### Traceability References

| Traceability Type | Reference |
|---|---|
| Business Requirement | BA-08 BR-016 Batch Scheduling |
| Business Rule | BA-02 BR-ATT-009, BR-AUD-003, BR-SEC-004 |
| Business Process | BA-03 BP-ACT-013 Cancel Session |
| Business Process Flow | BA-04 Section 21 Activity Management Flow, Section 22 Batch Management Flow |
| Persona | BA-05 Facility Manager, Trainer, Reception Staff, Customer |
| User Journey | BA-06 Section 5 Facility Manager Journey, Section 8 Trainer Journey, Section 17 Attendance Journey |
| Stakeholder | BA-07 Facility Manager, Trainer, Reception Staff, Customer |
| Non-Functional Requirement | BA-09 Section 2.8 Configurability, Section 2.4 Performance, Section 2.10 Auditability |
| Assumption / Constraint / Risk | BA-10 BA-ASS-011, BA-RSK-006 |

### Purpose

To enable Session Administration within Batch / Class Management so Digitize can execute Cancel Session consistently across Organizations, Facilities, Sites, users, and related operational or commercial services.

### Functional Requirement

The system shall support Cancel Session as an atomic Batch / Class Management capability, including scoped data capture, business-rule validation, permission enforcement, lifecycle handling, related service synchronization, notification generation, reporting contribution, and immutable audit recording.

### Business Justification

Cancel Session is required to preserve operational control, revenue accuracy, service continuity, customer trust, and enterprise traceability for Activity & Batch processes. Without this capability, downstream modules would rely on incomplete, manual, or inconsistent records.

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
- Actor has permission for Cancel Session.
- Required Activity & Batch configuration and policies are available.
- Related records required by BA-03 BP-ACT-013 Cancel Session are available and within authorized scope.

### Trigger

The capability is triggered when Facility Manager or the System initiates Cancel Session from Session Cancellation, a related workflow, a scheduled job, or an approved integration event.

### In Scope

- Capture or retrieve required Activity & Batch context.
- Validate Organization, Facility, Site, Customer, user, and policy scope where applicable.
- Execute Cancel Session according to approved business rules.
- Persist the resulting Activity state or transaction.
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
- Activity reference
- Customer reference, where applicable
- Effective date and time, where applicable
- Status or action reason, where applicable
- Payment, billing, trainer, session, or subscription reference where applicable
- Actor remarks, where applicable

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Activity ID | Primary business record reference | Identifier | Yes | System / User | Must exist or be generated within scope | Core reference for Cancel Session |
| Organization ID | Tenant Organization context | Identifier | Yes | Session / System | Must be Active and authorized | Enforces tenant isolation |
| Facility ID | Facility context | Identifier | Conditional | User / System | Must be Active where applicable | Required for facility-level operations |
| Site ID | Site context | Identifier | Conditional | User / System | Must belong to Facility where applicable | Required for site-level operations |
| Status | Lifecycle or processing state | Enum | Yes | System | Must follow allowed state transitions | Drives UI and downstream access |
| Effective Date | Date when action applies | DateTime | Conditional | User / System | Must satisfy policy | Supports scheduled or immediate actions |
| Reason / Remarks | Business explanation | Text | Conditional | User | Required for governed changes | Stored for audit |

### Main Flow

1. Actor opens Session Cancellation or the related workflow.
2. The system validates authentication, authorization, tenant scope, and current operating context.
3. The system loads the required Activity & Batch records, related configuration, and policy controls.
4. Actor enters or confirms the information required to cancel session.
5. The system validates mandatory data, lifecycle status, ownership, eligibility, financial, capacity, schedule, and security rules where applicable.
6. The system executes Cancel Session and persists the resulting Activity state or transaction.
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

- Activity record created, updated, validated, or reported according to the action.
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
| VAL-BAT-013-001 | Actor must have permission to execute Cancel Session. | Deny request and audit. | Critical |
| VAL-BAT-013-002 | Record must belong to the authorized Organization scope. | Deny request. | Critical |
| VAL-BAT-013-003 | Mandatory inputs must be complete and valid. | Block submission. | Critical |
| VAL-BAT-013-004 | Lifecycle and policy rules from BA-02 must be satisfied. | Reject or route for approval. | High |
| VAL-BAT-013-005 | Historical and audit records must be preserved. | Roll back or mark for recovery. | Critical |

### Business Rules

- BA-02 BR-ATT-009
- BA-02 BR-AUD-003
- BA-02 BR-SEC-004

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| bat.cancel.session.view | Facility Manager | Read | View Cancel Session context |
| bat.cancel.session.execute | Facility Manager | Execute | Execute Cancel Session |
| bat.cancel.session.approve | Organization Administrator | Approve | Approve governed exceptions where configured |
| bat.cancel.session.audit.view | Organization Administrator / Support Executive | Read | View audit trace |

### Security Considerations

The capability shall enforce authentication, role-based authorization, tenant isolation, Organization scope, Facility and Site access boundaries, sensitive data masking, secure references, and immutable audit logging.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Cancel Session Completed | Primary actor and configured stakeholders | In-App / Email | Action completes | Include reference, status, and effective date where applicable |
| Cancel Session Requires Approval | Approver | In-App | Approval rule applies | Include safe summary and requested action |
| Cancel Session Failed | Primary actor | In-App | Validation or processing fails | Include safe failure reason and next action |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| CancelSessionRequested | Batch / Class Management | Approval Workflow, Audit Service |
| CancelSessionCompleted | Batch / Class Management | Notification Service, Reporting Service, Audit Service |
| CancelSessionRejected | Batch / Class Management | Notification Service, Audit Service |

### Audit Events

| Audit Event | Description | Actor | Target Entity | Key Data |
|---|---|---|---|---|
| CANCEL_SESSION_REQUESTED | Cancel Session requested | Facility Manager | Activity | Scope, reference, and reason |
| CANCEL_SESSION_COMPLETED | Cancel Session completed | Facility Manager / System | Activity | Previous and new state |
| CANCEL_SESSION_REJECTED | Cancel Session rejected | System | Activity | Rejection reason |

### Reports Generated

- Batch / Class Management Operational Report
- Batch / Class Management History Report
- Batch / Class Management Exception Report
- Executive Dashboard

### Related Screens

- Session Cancellation
- Batch / Class Management Dashboard
- Batch / Class Management History
- Audit Log Viewer

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/batch-sessions/{sessionId}/cancel | POST | Authorized token | Execute Cancel Session | 200 OK or 201 Created with result |
| /api/v1/batch-sessions/{sessionId}/cancel/history | GET | Authorized token | Retrieve Cancel Session history | 200 OK with history |
| /api/v1/audit-logs | GET | Authorized token | Retrieve related audit events | 200 OK with scoped audit records |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Activity | Create / Update / Read | Support Cancel Session | Governed by Organization scope |
| Batch | Read / Insert | Support Cancel Session | Governed by Organization scope |
| Batch Schedule | Read / Insert | Support Cancel Session | Governed by Organization scope |
| Batch Capacity | Read / Insert | Support Cancel Session | Governed by Organization scope |
| Trainer Assignment | Read / Insert | Support Cancel Session | Governed by Organization scope |
| Audit Log | Insert | Record auditable activity | Immutable |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Draft | Cancel Session initiated | Validated | Facility Manager | Required data captured |
| Validated | Validation succeeds | Pending Approval | System | BA-02 rules satisfied |
| Pending Approval | Processing completes | Completed | System | Related updates succeed |
| Pending Approval | Approval or policy failure | Rejected | System / Approver | Request rejected |
| Completed | View history | Completed | Authorized user | Read-only historical access |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| BAT-013-001 | Cancel Session cannot be completed because required information is missing. | Missing mandatory data | Complete required fields |
| BAT-013-002 | You do not have permission to perform this action. | Authorization failure | Request access |
| BAT-013-003 | The selected record is not eligible for this action. | Policy or lifecycle violation | Review record status |
| BAT-013-004 | Cancel Session could not be completed due to a system or integration error. | Processing failure | Retry or contact support |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Execute Cancel Session | Given the actor has required permission and valid scope | When the actor submits valid information | Then the system shall complete Cancel Session successfully |
| Enforce validation | Given mandatory data or policy conditions are invalid | When the action is submitted | Then the system shall reject the request with a clear message |
| Preserve audit | Given the action completes or fails | When processing ends | Then audit events shall record actor, timestamp, scope, and outcome |
| Protect scope | Given the selected record is outside authorized scope | When the action is requested | Then the system shall deny access |

### Dependencies

- Facility Management
- Site Management
- Trainer Management
- Customer Management
- Membership Management
- Attendance Management
- Notification Management

### Operational Considerations

Cancel Session should be designed for high-volume operational use, retry-safe processing, clear exception handling, and support-team diagnostics without exposing sensitive data.

### Non-Functional Considerations

This requirement shall satisfy Digitize non-functional expectations for availability, reliability, performance, scalability, security, configurability, maintainability, and auditability.

### Assumptions

- Required master data and configuration are maintained by authorized users.
- Related services expose stable APIs for validation and synchronization.
- Organization policies define approval, retention, notification, and exception behavior.

### Success Criteria

Cancel Session is completed accurately, securely, and audibly, with downstream records synchronized and no loss of historical traceability.

### Related Functional Requirements

- FR-BAT-001 - Create Activity
- FR-BAT-002 - Update Activity
- FR-BAT-003 - Configure Activity Rules
- FR-BAT-004 - Create Batch
- FR-AUD-001 - Record Audit Events

### Notes

Cancel Session shall remain aligned with the approved BA source documents and shall not introduce behavior that bypasses tenant isolation, lifecycle governance, financial controls, or auditability.

---

## FR-BAT-014 - View Batch Schedule

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-BAT-014 |
| Requirement Name | View Batch Schedule |
| Functional Module | Batch / Class Management |
| Business Domain | Activity & Batch |
| Business Capability | Operational Monitoring |
| Requirement Type | Functional |
| Requirement Category | Reporting |
| Requirement Version | 1.0 |
| Requirement Status | Approved |
| Priority | Medium |
| Complexity | Low |
| Release Version | 1.0 |
| Owner | Product Management |

### Traceability References

| Traceability Type | Reference |
|---|---|
| Business Requirement | BA-08 BR-016 Batch Scheduling |
| Business Rule | BA-02 BR-TRN-005, BR-ATT-009, BR-SEC-004 |
| Business Process | BA-03 BP-ACT-014 View Batch Schedule |
| Business Process Flow | BA-04 Section 21 Activity Management Flow, Section 22 Batch Management Flow |
| Persona | BA-05 Facility Manager, Trainer, Reception Staff, Customer |
| User Journey | BA-06 Section 5 Facility Manager Journey, Section 8 Trainer Journey, Section 17 Attendance Journey |
| Stakeholder | BA-07 Facility Manager, Trainer, Reception Staff, Customer |
| Non-Functional Requirement | BA-09 Section 2.8 Configurability, Section 2.4 Performance, Section 2.10 Auditability |
| Assumption / Constraint / Risk | BA-10 BA-ASS-011, BA-RSK-006 |

### Purpose

To enable Operational Monitoring within Batch / Class Management so Digitize can execute View Batch Schedule consistently across Organizations, Facilities, Sites, users, and related operational or commercial services.

### Functional Requirement

The system shall support View Batch Schedule as an atomic Batch / Class Management capability, including scoped data capture, business-rule validation, permission enforcement, lifecycle handling, related service synchronization, notification generation, reporting contribution, and immutable audit recording.

### Business Justification

View Batch Schedule is required to preserve operational control, revenue accuracy, service continuity, customer trust, and enterprise traceability for Activity & Batch processes. Without this capability, downstream modules would rely on incomplete, manual, or inconsistent records.

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
- Actor has permission for View Batch Schedule.
- Required Activity & Batch configuration and policies are available.
- Related records required by BA-03 BP-ACT-014 View Batch Schedule are available and within authorized scope.

### Trigger

The capability is triggered when Reception Staff or the System initiates View Batch Schedule from Batch Schedule, a related workflow, a scheduled job, or an approved integration event.

### In Scope

- Capture or retrieve required Activity & Batch context.
- Validate Organization, Facility, Site, Customer, user, and policy scope where applicable.
- Execute View Batch Schedule according to approved business rules.
- Persist the resulting Activity state or transaction.
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
- Activity reference
- Customer reference, where applicable
- Effective date and time, where applicable
- Status or action reason, where applicable
- Payment, billing, trainer, session, or subscription reference where applicable
- Actor remarks, where applicable

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Activity ID | Primary business record reference | Identifier | Yes | System / User | Must exist or be generated within scope | Core reference for View Batch Schedule |
| Organization ID | Tenant Organization context | Identifier | Yes | Session / System | Must be Active and authorized | Enforces tenant isolation |
| Facility ID | Facility context | Identifier | Conditional | User / System | Must be Active where applicable | Required for facility-level operations |
| Site ID | Site context | Identifier | Conditional | User / System | Must belong to Facility where applicable | Required for site-level operations |
| Status | Lifecycle or processing state | Enum | Yes | System | Must follow allowed state transitions | Drives UI and downstream access |
| Effective Date | Date when action applies | DateTime | Conditional | User / System | Must satisfy policy | Supports scheduled or immediate actions |
| Reason / Remarks | Business explanation | Text | Conditional | User | Required for governed changes | Stored for audit |

### Main Flow

1. Actor opens Batch Schedule or the related workflow.
2. The system validates authentication, authorization, tenant scope, and current operating context.
3. The system loads the required Activity & Batch records, related configuration, and policy controls.
4. Actor enters or confirms the information required to view batch schedule.
5. The system validates mandatory data, lifecycle status, ownership, eligibility, financial, capacity, schedule, and security rules where applicable.
6. The system executes View Batch Schedule and persists the resulting Activity state or transaction.
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

- Activity record created, updated, validated, or reported according to the action.
- Lifecycle or processing status updated.
- Related history entry created.
- Business events emitted.
- Notifications generated where configured.
- Audit events recorded.
- Reports or dashboards updated where applicable.

### UI Behaviour

Batch Schedule shall display scoped context, mandatory fields, lifecycle status, policy warnings, validation results, available actions, confirmation prompts, read-only states, pagination or filters where applicable, and responsive behavior for front-desk and administrative usage.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-BAT-014-001 | Actor must have permission to execute View Batch Schedule. | Deny request and audit. | Critical |
| VAL-BAT-014-002 | Record must belong to the authorized Organization scope. | Deny request. | Critical |
| VAL-BAT-014-003 | Mandatory inputs must be complete and valid. | Block submission. | Critical |
| VAL-BAT-014-004 | Lifecycle and policy rules from BA-02 must be satisfied. | Reject or route for approval. | High |
| VAL-BAT-014-005 | Historical and audit records must be preserved. | Roll back or mark for recovery. | Critical |

### Business Rules

- BA-02 BR-TRN-005
- BA-02 BR-ATT-009
- BA-02 BR-SEC-004

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| bat.view.batch.schedule.view | Reception Staff | Read | View View Batch Schedule context |
| bat.view.batch.schedule.execute | Reception Staff | Execute | Execute View Batch Schedule |
| bat.view.batch.schedule.approve | Organization Administrator | Approve | Approve governed exceptions where configured |
| bat.view.batch.schedule.audit.view | Organization Administrator / Support Executive | Read | View audit trace |

### Security Considerations

The capability shall enforce authentication, role-based authorization, tenant isolation, Organization scope, Facility and Site access boundaries, sensitive data masking, secure references, and immutable audit logging.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| View Batch Schedule Completed | Primary actor and configured stakeholders | In-App / Email | Action completes | Include reference, status, and effective date where applicable |
| View Batch Schedule Requires Approval | Approver | In-App | Approval rule applies | Include safe summary and requested action |
| View Batch Schedule Failed | Primary actor | In-App | Validation or processing fails | Include safe failure reason and next action |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| ViewBatchScheduleRequested | Batch / Class Management | Approval Workflow, Audit Service |
| ViewBatchScheduleCompleted | Batch / Class Management | Notification Service, Reporting Service, Audit Service |
| ViewBatchScheduleRejected | Batch / Class Management | Notification Service, Audit Service |

### Audit Events

| Audit Event | Description | Actor | Target Entity | Key Data |
|---|---|---|---|---|
| VIEW_BATCH_SCHEDULE_REQUESTED | View Batch Schedule requested | Reception Staff | Activity | Scope, reference, and reason |
| VIEW_BATCH_SCHEDULE_COMPLETED | View Batch Schedule completed | Reception Staff / System | Activity | Previous and new state |
| VIEW_BATCH_SCHEDULE_REJECTED | View Batch Schedule rejected | System | Activity | Rejection reason |

### Reports Generated

- Batch / Class Management Operational Report
- Batch / Class Management History Report
- Batch / Class Management Exception Report
- Executive Dashboard

### Related Screens

- Batch Schedule
- Batch / Class Management Dashboard
- Batch / Class Management History
- Audit Log Viewer

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/batches/schedule | GET | Authorized token | Execute View Batch Schedule | 200 OK or 201 Created with result |
| /api/v1/batches/schedule/history | GET | Authorized token | Retrieve View Batch Schedule history | 200 OK with history |
| /api/v1/audit-logs | GET | Authorized token | Retrieve related audit events | 200 OK with scoped audit records |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Activity | Read | Support View Batch Schedule | Governed by Organization scope |
| Batch | Read / Insert | Support View Batch Schedule | Governed by Organization scope |
| Batch Schedule | Read / Insert | Support View Batch Schedule | Governed by Organization scope |
| Batch Capacity | Read / Insert | Support View Batch Schedule | Governed by Organization scope |
| Trainer Assignment | Read / Insert | Support View Batch Schedule | Governed by Organization scope |
| Audit Log | Insert | Record auditable activity | Immutable |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Not Requested | View Batch Schedule initiated | Generating | Reception Staff | Required data captured |
| Generating | Validation succeeds | Ready | System | BA-02 rules satisfied |
| Ready | Processing completes | Export Pending | System | Related updates succeed |
| Ready | Approval or policy failure | Failed | System / Approver | Request rejected |
| Export Pending | View history | Export Pending | Authorized user | Read-only historical access |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| BAT-014-001 | View Batch Schedule cannot be completed because required information is missing. | Missing mandatory data | Complete required fields |
| BAT-014-002 | You do not have permission to perform this action. | Authorization failure | Request access |
| BAT-014-003 | The selected record is not eligible for this action. | Policy or lifecycle violation | Review record status |
| BAT-014-004 | View Batch Schedule could not be completed due to a system or integration error. | Processing failure | Retry or contact support |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Execute View Batch Schedule | Given the actor has required permission and valid scope | When the actor submits valid information | Then the system shall complete View Batch Schedule successfully |
| Enforce validation | Given mandatory data or policy conditions are invalid | When the action is submitted | Then the system shall reject the request with a clear message |
| Preserve audit | Given the action completes or fails | When processing ends | Then audit events shall record actor, timestamp, scope, and outcome |
| Protect scope | Given the selected record is outside authorized scope | When the action is requested | Then the system shall deny access |

### Dependencies

- Facility Management
- Site Management
- Trainer Management
- Customer Management
- Membership Management
- Attendance Management
- Notification Management

### Operational Considerations

View Batch Schedule should be designed for high-volume operational use, retry-safe processing, clear exception handling, and support-team diagnostics without exposing sensitive data.

### Non-Functional Considerations

This requirement shall satisfy Digitize non-functional expectations for availability, reliability, performance, scalability, security, configurability, maintainability, and auditability.

### Assumptions

- Required master data and configuration are maintained by authorized users.
- Related services expose stable APIs for validation and synchronization.
- Organization policies define approval, retention, notification, and exception behavior.

### Success Criteria

View Batch Schedule is completed accurately, securely, and audibly, with downstream records synchronized and no loss of historical traceability.

### Related Functional Requirements

- FR-BAT-001 - Create Activity
- FR-BAT-002 - Update Activity
- FR-BAT-003 - Configure Activity Rules
- FR-BAT-004 - Create Batch
- FR-AUD-001 - Record Audit Events

### Notes

View Batch Schedule shall remain aligned with the approved BA source documents and shall not introduce behavior that bypasses tenant isolation, lifecycle governance, financial controls, or auditability.

---

## FR-BAT-015 - View Activity Performance

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-BAT-015 |
| Requirement Name | View Activity Performance |
| Functional Module | Batch / Class Management |
| Business Domain | Activity & Batch |
| Business Capability | Activity Analytics |
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
| Business Requirement | BA-08 BR-015 Activity Configuration |
| Business Rule | BA-02 BR-ATT-009, BR-TRN-009, BR-SEC-004 |
| Business Process | BA-03 BP-ACT-015 View Activity Performance |
| Business Process Flow | BA-04 Section 21 Activity Management Flow, Section 22 Batch Management Flow |
| Persona | BA-05 Facility Manager, Trainer, Reception Staff, Customer |
| User Journey | BA-06 Section 5 Facility Manager Journey, Section 8 Trainer Journey, Section 17 Attendance Journey |
| Stakeholder | BA-07 Facility Manager, Trainer, Reception Staff, Customer |
| Non-Functional Requirement | BA-09 Section 2.8 Configurability, Section 2.4 Performance, Section 2.10 Auditability |
| Assumption / Constraint / Risk | BA-10 BA-ASS-011, BA-RSK-006 |

### Purpose

To enable Activity Analytics within Batch / Class Management so Digitize can execute View Activity Performance consistently across Organizations, Facilities, Sites, users, and related operational or commercial services.

### Functional Requirement

The system shall support View Activity Performance as an atomic Batch / Class Management capability, including scoped data capture, business-rule validation, permission enforcement, lifecycle handling, related service synchronization, notification generation, reporting contribution, and immutable audit recording.

### Business Justification

View Activity Performance is required to preserve operational control, revenue accuracy, service continuity, customer trust, and enterprise traceability for Activity & Batch processes. Without this capability, downstream modules would rely on incomplete, manual, or inconsistent records.

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
- Actor has permission for View Activity Performance.
- Required Activity & Batch configuration and policies are available.
- Related records required by BA-03 BP-ACT-015 View Activity Performance are available and within authorized scope.

### Trigger

The capability is triggered when Facility Manager or the System initiates View Activity Performance from Activity Performance, a related workflow, a scheduled job, or an approved integration event.

### In Scope

- Capture or retrieve required Activity & Batch context.
- Validate Organization, Facility, Site, Customer, user, and policy scope where applicable.
- Execute View Activity Performance according to approved business rules.
- Persist the resulting Activity state or transaction.
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
- Activity reference
- Customer reference, where applicable
- Effective date and time, where applicable
- Status or action reason, where applicable
- Payment, billing, trainer, session, or subscription reference where applicable
- Actor remarks, where applicable

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Activity ID | Primary business record reference | Identifier | Yes | System / User | Must exist or be generated within scope | Core reference for View Activity Performance |
| Organization ID | Tenant Organization context | Identifier | Yes | Session / System | Must be Active and authorized | Enforces tenant isolation |
| Facility ID | Facility context | Identifier | Conditional | User / System | Must be Active where applicable | Required for facility-level operations |
| Site ID | Site context | Identifier | Conditional | User / System | Must belong to Facility where applicable | Required for site-level operations |
| Status | Lifecycle or processing state | Enum | Yes | System | Must follow allowed state transitions | Drives UI and downstream access |
| Effective Date | Date when action applies | DateTime | Conditional | User / System | Must satisfy policy | Supports scheduled or immediate actions |
| Reason / Remarks | Business explanation | Text | Conditional | User | Required for governed changes | Stored for audit |

### Main Flow

1. Actor opens Activity Performance or the related workflow.
2. The system validates authentication, authorization, tenant scope, and current operating context.
3. The system loads the required Activity & Batch records, related configuration, and policy controls.
4. Actor enters or confirms the information required to view activity performance.
5. The system validates mandatory data, lifecycle status, ownership, eligibility, financial, capacity, schedule, and security rules where applicable.
6. The system executes View Activity Performance and persists the resulting Activity state or transaction.
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

- Activity record created, updated, validated, or reported according to the action.
- Lifecycle or processing status updated.
- Related history entry created.
- Business events emitted.
- Notifications generated where configured.
- Audit events recorded.
- Reports or dashboards updated where applicable.

### UI Behaviour

Activity Performance shall display scoped context, mandatory fields, lifecycle status, policy warnings, validation results, available actions, confirmation prompts, read-only states, pagination or filters where applicable, and responsive behavior for front-desk and administrative usage.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-BAT-015-001 | Actor must have permission to execute View Activity Performance. | Deny request and audit. | Critical |
| VAL-BAT-015-002 | Record must belong to the authorized Organization scope. | Deny request. | Critical |
| VAL-BAT-015-003 | Mandatory inputs must be complete and valid. | Block submission. | Critical |
| VAL-BAT-015-004 | Lifecycle and policy rules from BA-02 must be satisfied. | Reject or route for approval. | High |
| VAL-BAT-015-005 | Historical and audit records must be preserved. | Roll back or mark for recovery. | Critical |

### Business Rules

- BA-02 BR-ATT-009
- BA-02 BR-TRN-009
- BA-02 BR-SEC-004

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| bat.view.activity.performance.view | Facility Manager | Read | View View Activity Performance context |
| bat.view.activity.performance.execute | Facility Manager | Execute | Execute View Activity Performance |
| bat.view.activity.performance.approve | Organization Administrator | Approve | Approve governed exceptions where configured |
| bat.view.activity.performance.audit.view | Organization Administrator / Support Executive | Read | View audit trace |

### Security Considerations

The capability shall enforce authentication, role-based authorization, tenant isolation, Organization scope, Facility and Site access boundaries, sensitive data masking, secure references, and immutable audit logging.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| View Activity Performance Completed | Primary actor and configured stakeholders | In-App / Email | Action completes | Include reference, status, and effective date where applicable |
| View Activity Performance Requires Approval | Approver | In-App | Approval rule applies | Include safe summary and requested action |
| View Activity Performance Failed | Primary actor | In-App | Validation or processing fails | Include safe failure reason and next action |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| ViewActivityPerformanceRequested | Batch / Class Management | Approval Workflow, Audit Service |
| ViewActivityPerformanceCompleted | Batch / Class Management | Notification Service, Reporting Service, Audit Service |
| ViewActivityPerformanceRejected | Batch / Class Management | Notification Service, Audit Service |

### Audit Events

| Audit Event | Description | Actor | Target Entity | Key Data |
|---|---|---|---|---|
| VIEW_ACTIVITY_PERFORMANCE_REQUESTED | View Activity Performance requested | Facility Manager | Activity | Scope, reference, and reason |
| VIEW_ACTIVITY_PERFORMANCE_COMPLETED | View Activity Performance completed | Facility Manager / System | Activity | Previous and new state |
| VIEW_ACTIVITY_PERFORMANCE_REJECTED | View Activity Performance rejected | System | Activity | Rejection reason |

### Reports Generated

- Batch / Class Management Operational Report
- Batch / Class Management History Report
- Batch / Class Management Exception Report
- Executive Dashboard

### Related Screens

- Activity Performance
- Batch / Class Management Dashboard
- Batch / Class Management History
- Audit Log Viewer

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/reports/activities/performance | GET | Authorized token | Execute View Activity Performance | 200 OK or 201 Created with result |
| /api/v1/reports/activities/performance/history | GET | Authorized token | Retrieve View Activity Performance history | 200 OK with history |
| /api/v1/audit-logs | GET | Authorized token | Retrieve related audit events | 200 OK with scoped audit records |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Activity | Read | Support View Activity Performance | Governed by Organization scope |
| Batch | Read / Insert | Support View Activity Performance | Governed by Organization scope |
| Batch Schedule | Read / Insert | Support View Activity Performance | Governed by Organization scope |
| Batch Capacity | Read / Insert | Support View Activity Performance | Governed by Organization scope |
| Trainer Assignment | Read / Insert | Support View Activity Performance | Governed by Organization scope |
| Audit Log | Insert | Record auditable activity | Immutable |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Not Requested | View Activity Performance initiated | Generating | Facility Manager | Required data captured |
| Generating | Validation succeeds | Ready | System | BA-02 rules satisfied |
| Ready | Processing completes | Export Pending | System | Related updates succeed |
| Ready | Approval or policy failure | Failed | System / Approver | Request rejected |
| Export Pending | View history | Export Pending | Authorized user | Read-only historical access |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| BAT-015-001 | View Activity Performance cannot be completed because required information is missing. | Missing mandatory data | Complete required fields |
| BAT-015-002 | You do not have permission to perform this action. | Authorization failure | Request access |
| BAT-015-003 | The selected record is not eligible for this action. | Policy or lifecycle violation | Review record status |
| BAT-015-004 | View Activity Performance could not be completed due to a system or integration error. | Processing failure | Retry or contact support |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Execute View Activity Performance | Given the actor has required permission and valid scope | When the actor submits valid information | Then the system shall complete View Activity Performance successfully |
| Enforce validation | Given mandatory data or policy conditions are invalid | When the action is submitted | Then the system shall reject the request with a clear message |
| Preserve audit | Given the action completes or fails | When processing ends | Then audit events shall record actor, timestamp, scope, and outcome |
| Protect scope | Given the selected record is outside authorized scope | When the action is requested | Then the system shall deny access |

### Dependencies

- Facility Management
- Site Management
- Trainer Management
- Customer Management
- Membership Management
- Attendance Management
- Notification Management

### Operational Considerations

View Activity Performance should be designed for high-volume operational use, retry-safe processing, clear exception handling, and support-team diagnostics without exposing sensitive data.

### Non-Functional Considerations

This requirement shall satisfy Digitize non-functional expectations for availability, reliability, performance, scalability, security, configurability, maintainability, and auditability.

### Assumptions

- Required master data and configuration are maintained by authorized users.
- Related services expose stable APIs for validation and synchronization.
- Organization policies define approval, retention, notification, and exception behavior.

### Success Criteria

View Activity Performance is completed accurately, securely, and audibly, with downstream records synchronized and no loss of historical traceability.

### Related Functional Requirements

- FR-BAT-001 - Create Activity
- FR-BAT-002 - Update Activity
- FR-BAT-003 - Configure Activity Rules
- FR-BAT-004 - Create Batch
- FR-AUD-001 - Record Audit Events

### Notes

View Activity Performance shall remain aligned with the approved BA source documents and shall not introduce behavior that bypasses tenant isolation, lifecycle governance, financial controls, or auditability.

---

**End of FR-13 - Batch / Class Management**
