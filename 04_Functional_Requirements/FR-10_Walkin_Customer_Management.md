# FR-10 Walk-in Customer Management

**Document ID:** FR-10  
**Document Name:** Walk-in Customer Management Functional Requirements  
**Company:** OreeOn Technologies Pvt. Ltd.  
**Product:** Digitize  
**Document Type:** Functional Requirements  
**Version:** 1.0  
**Status:** Draft  
**Owner:** Product Management  
**Prepared By:** Product Management, Business Analysis, and Solution Architecture  
**Last Updated:** July 2026

---

## FR-WLK-001 - Identify or Register Walk-in Customer

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-WLK-001 |
| Requirement Name | Identify or Register Walk-in Customer |
| Functional Module | Walk-in Customer Management |
| Business Domain | Walk-in |
| Business Capability | Walk-in Customer Identification |
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
| Business Requirement | BA-08 BR-014 Walk-in Visit Recording |
| Business Rule | BA-02 BR-CUS-001, BR-CUS-003, BR-CUS-004, BR-ATT-005, BR-SEC-004 |
| Business Process | BA-03 BP-ATT-004 Record Walk-in Attendance |
| Business Process Flow | BA-04 Section 20 Walk-in Customer Flow |
| Persona | BA-05 Reception Staff, Customer, Finance Staff |
| User Journey | BA-06 Section 16 Walk-in Customer Journey, Section 17 Attendance Journey |
| Stakeholder | BA-07 Reception Staff, Customer, Finance Staff |
| Non-Functional Requirement | BA-09 Section 2.4 Performance, Section 2.10 Auditability, Section 3.7 Data Protection |
| Assumption / Constraint / Risk | BA-10 BA-ASS-011, BA-RSK-008, BA-RSK-012 |
| Product Foundation | PF-01, PF-02, PF-05 |

### Purpose

To enable Walk-in Customer Identification within Walk-in Customer Management so Digitize can execute Identify or Register Walk-in Customer consistently across Organizations, Facilities, Sites, users, and related operational or commercial services.

### Functional Requirement

The system shall support Identify or Register Walk-in Customer as an atomic Walk-in Customer Management capability, including scoped data capture, business-rule validation, permission enforcement, lifecycle handling, related service synchronization, notification generation, reporting contribution, and immutable audit recording.

### Business Justification

Identify or Register Walk-in Customer is required to preserve operational control, revenue accuracy, service continuity, customer trust, and enterprise traceability for Walk-in processes. Without this capability, downstream modules would rely on incomplete, manual, or inconsistent records.

### Actors

- Reception Staff
- Organization Admin
- Customer
- System
- Notification Service
- Reporting Service
- Audit Service

### Preconditions

- Organization is Active.
- Facility and Site context are Active where applicable.
- Actor is authenticated.
- Actor has permission for Identify or Register Walk-in Customer.
- Required Walk-in configuration and policies are available.
- Related records required by BA-03 BP-ATT-004 Record Walk-in Attendance are available and within authorized scope.

### Trigger

The capability is triggered when Reception Staff or the System initiates Identify or Register Walk-in Customer from Walk-in Registration, a related workflow, a scheduled job, or an approved integration event.

### In Scope

- Capture or retrieve required Walk-in context.
- Validate Organization, Facility, Site, Customer, user, and policy scope where applicable.
- Execute Identify or Register Walk-in Customer according to approved business rules.
- Persist the resulting Walk-in Visit state or transaction.
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
- Walk-in Visit reference
- Customer reference, where applicable
- Effective date and time, where applicable
- Status or action reason, where applicable
- Payment, billing, trainer, session, or subscription reference where applicable
- Actor remarks, where applicable

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Walk-in Visit ID | Primary business record reference | Identifier | Yes | System / User | Must exist or be generated within scope | Core reference for Identify or Register Walk-in Customer |
| Organization ID | Tenant Organization context | Identifier | Yes | Session / System | Must be Active and authorized | Enforces tenant isolation |
| Facility ID | Facility context | Identifier | Conditional | User / System | Must be Active where applicable | Required for facility-level operations |
| Site ID | Site context | Identifier | Conditional | User / System | Must belong to Facility where applicable | Required for site-level operations |
| Status | Lifecycle or processing state | Enum | Yes | System | Must follow allowed state transitions | Drives UI and downstream access |
| Effective Date | Date when action applies | DateTime | Conditional | User / System | Must satisfy policy | Supports scheduled or immediate actions |
| Reason / Remarks | Business explanation | Text | Conditional | User | Required for governed changes | Stored for audit |

### Main Flow

1. Actor opens Walk-in Registration or the related workflow.
2. The system validates authentication, authorization, tenant scope, and current operating context.
3. The system loads the required Walk-in records, related configuration, and policy controls.
4. Actor enters or confirms the information required to identify or register walk-in customer.
5. The system validates mandatory data, lifecycle status, ownership, eligibility, financial, capacity, schedule, and security rules where applicable.
6. The system executes Identify or Register Walk-in Customer and persists the resulting Walk-in Visit state or transaction.
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

- Walk-in Visit record created, updated, validated, or reported according to the action.
- Lifecycle or processing status updated.
- Related history entry created.
- Business events emitted.
- Notifications generated where configured.
- Audit events recorded.
- Reports or dashboards updated where applicable.

### UI Behaviour

Walk-in Registration shall display scoped context, mandatory fields, lifecycle status, policy warnings, validation results, available actions, confirmation prompts, read-only states, pagination or filters where applicable, and responsive behavior for front-desk and administrative usage.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-WLK-001-001 | Actor must have permission to execute Identify or Register Walk-in Customer. | Deny request and audit. | Critical |
| VAL-WLK-001-002 | Record must belong to the authorized Organization scope. | Deny request. | Critical |
| VAL-WLK-001-003 | Mandatory inputs must be complete and valid. | Block submission. | Critical |
| VAL-WLK-001-004 | Lifecycle and policy rules from BA-02 must be satisfied. | Reject or route for approval. | High |
| VAL-WLK-001-005 | Historical and audit records must be preserved. | Roll back or mark for recovery. | Critical |

### Business Rules

- BA-02 BR-CUS-001
- BA-02 BR-CUS-003
- BA-02 BR-CUS-004
- BA-02 BR-ATT-005
- BA-02 BR-SEC-004

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| wlk.identify.or.register.walk.in.customer.view | Reception Staff | Read | View Identify or Register Walk-in Customer context |
| wlk.identify.or.register.walk.in.customer.execute | Reception Staff | Execute | Execute Identify or Register Walk-in Customer |
| wlk.identify.or.register.walk.in.customer.approve | Organization Admin | Approve | Approve governed exceptions where configured |
| wlk.identify.or.register.walk.in.customer.audit.view | Organization Admin / Support Executive | Read | View audit trace |

### Security Considerations

The capability shall enforce authentication, role-based authorization, tenant isolation, Organization scope, Facility and Site access boundaries, sensitive data masking, secure references, and immutable audit logging.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Identify or Register Walk-in Customer Completed | Primary actor and configured stakeholders | In-App / Email | Action completes | Include reference, status, and effective date where applicable |
| Identify or Register Walk-in Customer Requires Approval | Approver | In-App | Approval rule applies | Include safe summary and requested action |
| Identify or Register Walk-in Customer Failed | Primary actor | In-App | Validation or processing fails | Include safe failure reason and next action |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| IdentifyOrRegisterWalkinCustomerRequested | Walk-in Customer Management | Approval Workflow, Audit Service |
| IdentifyOrRegisterWalkinCustomerCompleted | Walk-in Customer Management | Notification Service, Reporting Service, Audit Service |
| IdentifyOrRegisterWalkinCustomerRejected | Walk-in Customer Management | Notification Service, Audit Service |

### Audit Events

| Audit Event | Description | Actor | Target Entity | Key Data |
|---|---|---|---|---|
| IDENTIFY_OR_REGISTER_WALKIN_CUSTOMER_REQUESTED | Identify or Register Walk-in Customer requested | Reception Staff | Walk-in Visit | Scope, reference, and reason |
| IDENTIFY_OR_REGISTER_WALKIN_CUSTOMER_COMPLETED | Identify or Register Walk-in Customer completed | Reception Staff / System | Walk-in Visit | Previous and new state |
| IDENTIFY_OR_REGISTER_WALKIN_CUSTOMER_REJECTED | Identify or Register Walk-in Customer rejected | System | Walk-in Visit | Rejection reason |

### Reports Generated

- Walk-in Customer Management Operational Report
- Walk-in Customer Management History Report
- Walk-in Customer Management Exception Report
- Executive Dashboard

### Related Screens

- Walk-in Registration
- Walk-in Customer Management Dashboard
- Walk-in Customer Management History
- Audit Log Viewer

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/walkins/customers/identify | POST | Authorized token | Execute Identify or Register Walk-in Customer | 200 OK or 201 Created with result |
| /api/v1/walkins/customers/identify/history | GET | Authorized token | Retrieve Identify or Register Walk-in Customer history | 200 OK with history |
| /api/v1/audit-logs | GET | Authorized token | Retrieve related audit events | 200 OK with scoped audit records |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Walk-in Visit | Create / Update / Read | Support Identify or Register Walk-in Customer | Governed by Organization scope |
| Customer | Read / Insert | Support Identify or Register Walk-in Customer | Governed by Organization scope |
| Attendance | Read / Insert | Support Identify or Register Walk-in Customer | Governed by Organization scope |
| Invoice | Read / Insert | Support Identify or Register Walk-in Customer | Governed by Organization scope |
| Payment | Read / Insert | Support Identify or Register Walk-in Customer | Governed by Organization scope |
| Audit Log | Insert | Record auditable activity | Immutable |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Draft | Identify or Register Walk-in Customer initiated | Validated | Reception Staff | Required data captured |
| Validated | Validation succeeds | Pending Approval | System | BA-02 rules satisfied |
| Pending Approval | Processing completes | Completed | System | Related updates succeed |
| Pending Approval | Approval or policy failure | Rejected | System / Approver | Request rejected |
| Completed | View history | Completed | Authorized user | Read-only historical access |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| WLK-001-001 | Identify or Register Walk-in Customer cannot be completed because required information is missing. | Missing mandatory data | Complete required fields |
| WLK-001-002 | You do not have permission to perform this action. | Authorization failure | Request access |
| WLK-001-003 | The selected record is not eligible for this action. | Policy or lifecycle violation | Review record status |
| WLK-001-004 | Identify or Register Walk-in Customer could not be completed due to a system or integration error. | Processing failure | Retry or contact support |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Execute Identify or Register Walk-in Customer | Given the actor has required permission and valid scope | When the actor submits valid information | Then the system shall complete Identify or Register Walk-in Customer successfully |
| Enforce validation | Given mandatory data or policy conditions are invalid | When the action is submitted | Then the system shall reject the request with a clear message |
| Preserve audit | Given the action completes or fails | When processing ends | Then audit events shall record actor, timestamp, scope, and outcome |
| Protect scope | Given the selected record is outside authorized scope | When the action is requested | Then the system shall deny access |

### Dependencies

- Customer Management
- Attendance Management
- Billing Management
- Payment Management
- Notification Management
- Audit Service

### Operational Considerations

Identify or Register Walk-in Customer should be designed for high-volume operational use, retry-safe processing, clear exception handling, and support-team diagnostics without exposing sensitive data.

### Non-Functional Considerations

This requirement shall satisfy Digitize non-functional expectations for availability, reliability, performance, scalability, security, configurability, maintainability, and auditability.

### Assumptions

- Required master data and configuration are maintained by authorized users.
- Related services expose stable APIs for validation and synchronization.
- Organization policies define approval, retention, notification, and exception behavior.

### Success Criteria

Identify or Register Walk-in Customer is completed accurately, securely, and audibly, with downstream records synchronized and no loss of historical traceability.

### Related Functional Requirements

- FR-WLK-002 - Validate Walk-in Eligibility
- FR-WLK-003 - Create Walk-in Visit
- FR-WLK-004 - Calculate Walk-in Charges
- FR-WLK-005 - Collect Walk-in Payment
- FR-AUD-001 - Record Audit Events

### Notes

Identify or Register Walk-in Customer shall remain aligned with the approved BA source documents and shall not introduce behavior that bypasses tenant isolation, lifecycle governance, financial controls, or auditability.

---

## FR-WLK-002 - Validate Walk-in Eligibility

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-WLK-002 |
| Requirement Name | Validate Walk-in Eligibility |
| Functional Module | Walk-in Customer Management |
| Business Domain | Walk-in |
| Business Capability | Walk-in Eligibility |
| Requirement Type | Functional |
| Requirement Category | Validation |
| Requirement Version | 1.0 |
| Requirement Status | Approved |
| Priority | Critical |
| Complexity | Medium |
| Release Version | 1.0 |
| Owner | Product Management |

### Traceability References

| Traceability Type | Reference |
|---|---|
| Business Requirement | BA-08 BR-014 Walk-in Visit Recording |
| Business Rule | BA-02 BR-ATT-001, BR-ATT-005, BR-ATT-006, BR-SEC-004 |
| Business Process | BA-03 BP-ATT-004 Record Walk-in Attendance |
| Business Process Flow | BA-04 Section 20 Walk-in Customer Flow |
| Persona | BA-05 Reception Staff, Customer, Finance Staff |
| User Journey | BA-06 Section 16 Walk-in Customer Journey, Section 17 Attendance Journey |
| Stakeholder | BA-07 Reception Staff, Customer, Finance Staff |
| Non-Functional Requirement | BA-09 Section 2.4 Performance, Section 2.10 Auditability, Section 3.7 Data Protection |
| Assumption / Constraint / Risk | BA-10 BA-ASS-011, BA-RSK-008, BA-RSK-012 |

### Purpose

To enable Walk-in Eligibility within Walk-in Customer Management so Digitize can execute Validate Walk-in Eligibility consistently across Organizations, Facilities, Sites, users, and related operational or commercial services.

### Functional Requirement

The system shall support Validate Walk-in Eligibility as an atomic Walk-in Customer Management capability, including scoped data capture, business-rule validation, permission enforcement, lifecycle handling, related service synchronization, notification generation, reporting contribution, and immutable audit recording.

### Business Justification

Validate Walk-in Eligibility is required to preserve operational control, revenue accuracy, service continuity, customer trust, and enterprise traceability for Walk-in processes. Without this capability, downstream modules would rely on incomplete, manual, or inconsistent records.

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
- Actor has permission for Validate Walk-in Eligibility.
- Required Walk-in configuration and policies are available.
- Related records required by BA-03 BP-ATT-004 Record Walk-in Attendance are available and within authorized scope.

### Trigger

The capability is triggered when System or the System initiates Validate Walk-in Eligibility from Walk-in Eligibility, a related workflow, a scheduled job, or an approved integration event.

### In Scope

- Capture or retrieve required Walk-in context.
- Validate Organization, Facility, Site, Customer, user, and policy scope where applicable.
- Execute Validate Walk-in Eligibility according to approved business rules.
- Persist the resulting Walk-in Visit state or transaction.
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
- Walk-in Visit reference
- Customer reference, where applicable
- Effective date and time, where applicable
- Status or action reason, where applicable
- Payment, billing, trainer, session, or subscription reference where applicable
- Actor remarks, where applicable

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Walk-in Visit ID | Primary business record reference | Identifier | Yes | System / User | Must exist or be generated within scope | Core reference for Validate Walk-in Eligibility |
| Organization ID | Tenant Organization context | Identifier | Yes | Session / System | Must be Active and authorized | Enforces tenant isolation |
| Facility ID | Facility context | Identifier | Conditional | User / System | Must be Active where applicable | Required for facility-level operations |
| Site ID | Site context | Identifier | Conditional | User / System | Must belong to Facility where applicable | Required for site-level operations |
| Status | Lifecycle or processing state | Enum | Yes | System | Must follow allowed state transitions | Drives UI and downstream access |
| Effective Date | Date when action applies | DateTime | Conditional | User / System | Must satisfy policy | Supports scheduled or immediate actions |
| Reason / Remarks | Business explanation | Text | Conditional | User | Required for governed changes | Stored for audit |

### Main Flow

1. Actor opens Walk-in Eligibility or the related workflow.
2. The system validates authentication, authorization, tenant scope, and current operating context.
3. The system loads the required Walk-in records, related configuration, and policy controls.
4. Actor enters or confirms the information required to validate walk-in eligibility.
5. The system validates mandatory data, lifecycle status, ownership, eligibility, financial, capacity, schedule, and security rules where applicable.
6. The system executes Validate Walk-in Eligibility and persists the resulting Walk-in Visit state or transaction.
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

- Walk-in Visit record created, updated, validated, or reported according to the action.
- Lifecycle or processing status updated.
- Related history entry created.
- Business events emitted.
- Notifications generated where configured.
- Audit events recorded.
- Reports or dashboards updated where applicable.

### UI Behaviour

Walk-in Eligibility shall display scoped context, mandatory fields, lifecycle status, policy warnings, validation results, available actions, confirmation prompts, read-only states, pagination or filters where applicable, and responsive behavior for front-desk and administrative usage.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-WLK-002-001 | Actor must have permission to execute Validate Walk-in Eligibility. | Deny request and audit. | Critical |
| VAL-WLK-002-002 | Record must belong to the authorized Organization scope. | Deny request. | Critical |
| VAL-WLK-002-003 | Mandatory inputs must be complete and valid. | Block submission. | Critical |
| VAL-WLK-002-004 | Lifecycle and policy rules from BA-02 must be satisfied. | Reject or route for approval. | High |
| VAL-WLK-002-005 | Historical and audit records must be preserved. | Roll back or mark for recovery. | Critical |

### Business Rules

- BA-02 BR-ATT-001
- BA-02 BR-ATT-005
- BA-02 BR-ATT-006
- BA-02 BR-SEC-004

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| wlk.validate.walk.in.eligibility.view | System | Read | View Validate Walk-in Eligibility context |
| wlk.validate.walk.in.eligibility.execute | System | Execute | Execute Validate Walk-in Eligibility |
| wlk.validate.walk.in.eligibility.approve | Organization Administrator | Approve | Approve governed exceptions where configured |
| wlk.validate.walk.in.eligibility.audit.view | Organization Administrator / Support Executive | Read | View audit trace |

### Security Considerations

The capability shall enforce authentication, role-based authorization, tenant isolation, Organization scope, Facility and Site access boundaries, sensitive data masking, secure references, and immutable audit logging.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Validate Walk-in Eligibility Completed | Primary actor and configured stakeholders | In-App / Email | Action completes | Include reference, status, and effective date where applicable |
| Validate Walk-in Eligibility Requires Approval | Approver | In-App | Approval rule applies | Include safe summary and requested action |
| Validate Walk-in Eligibility Failed | Primary actor | In-App | Validation or processing fails | Include safe failure reason and next action |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| ValidateWalkinEligibilityRequested | Walk-in Customer Management | Approval Workflow, Audit Service |
| ValidateWalkinEligibilityCompleted | Walk-in Customer Management | Notification Service, Reporting Service, Audit Service |
| ValidateWalkinEligibilityRejected | Walk-in Customer Management | Notification Service, Audit Service |

### Audit Events

| Audit Event | Description | Actor | Target Entity | Key Data |
|---|---|---|---|---|
| VALIDATE_WALKIN_ELIGIBILITY_REQUESTED | Validate Walk-in Eligibility requested | System | Walk-in Visit | Scope, reference, and reason |
| VALIDATE_WALKIN_ELIGIBILITY_COMPLETED | Validate Walk-in Eligibility completed | System / System | Walk-in Visit | Previous and new state |
| VALIDATE_WALKIN_ELIGIBILITY_REJECTED | Validate Walk-in Eligibility rejected | System | Walk-in Visit | Rejection reason |

### Reports Generated

- Walk-in Customer Management Operational Report
- Walk-in Customer Management History Report
- Walk-in Customer Management Exception Report
- Executive Dashboard

### Related Screens

- Walk-in Eligibility
- Walk-in Customer Management Dashboard
- Walk-in Customer Management History
- Audit Log Viewer

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/walkins/eligibility | POST | Authorized token | Execute Validate Walk-in Eligibility | 200 OK or 201 Created with result |
| /api/v1/walkins/eligibility/history | GET | Authorized token | Retrieve Validate Walk-in Eligibility history | 200 OK with history |
| /api/v1/audit-logs | GET | Authorized token | Retrieve related audit events | 200 OK with scoped audit records |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Walk-in Visit | Create / Update / Read | Support Validate Walk-in Eligibility | Governed by Organization scope |
| Customer | Read / Insert | Support Validate Walk-in Eligibility | Governed by Organization scope |
| Attendance | Read / Insert | Support Validate Walk-in Eligibility | Governed by Organization scope |
| Invoice | Read / Insert | Support Validate Walk-in Eligibility | Governed by Organization scope |
| Payment | Read / Insert | Support Validate Walk-in Eligibility | Governed by Organization scope |
| Audit Log | Insert | Record auditable activity | Immutable |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Requested | Validate Walk-in Eligibility initiated | Eligible | System | Required data captured |
| Eligible | Validation succeeds | Requires Override | System | BA-02 rules satisfied |
| Requires Override | Processing completes | Denied | System | Related updates succeed |
| Requires Override | Approval or policy failure | Failed | System / Approver | Request rejected |
| Denied | View history | Denied | Authorized user | Read-only historical access |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| WLK-002-001 | Validate Walk-in Eligibility cannot be completed because required information is missing. | Missing mandatory data | Complete required fields |
| WLK-002-002 | You do not have permission to perform this action. | Authorization failure | Request access |
| WLK-002-003 | The selected record is not eligible for this action. | Policy or lifecycle violation | Review record status |
| WLK-002-004 | Validate Walk-in Eligibility could not be completed due to a system or integration error. | Processing failure | Retry or contact support |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Execute Validate Walk-in Eligibility | Given the actor has required permission and valid scope | When the actor submits valid information | Then the system shall complete Validate Walk-in Eligibility successfully |
| Enforce validation | Given mandatory data or policy conditions are invalid | When the action is submitted | Then the system shall reject the request with a clear message |
| Preserve audit | Given the action completes or fails | When processing ends | Then audit events shall record actor, timestamp, scope, and outcome |
| Protect scope | Given the selected record is outside authorized scope | When the action is requested | Then the system shall deny access |

### Dependencies

- Customer Management
- Attendance Management
- Billing Management
- Payment Management
- Notification Management
- Audit Service

### Operational Considerations

Validate Walk-in Eligibility should be designed for high-volume operational use, retry-safe processing, clear exception handling, and support-team diagnostics without exposing sensitive data.

### Non-Functional Considerations

This requirement shall satisfy Digitize non-functional expectations for availability, reliability, performance, scalability, security, configurability, maintainability, and auditability.

### Assumptions

- Required master data and configuration are maintained by authorized users.
- Related services expose stable APIs for validation and synchronization.
- Organization policies define approval, retention, notification, and exception behavior.

### Success Criteria

Validate Walk-in Eligibility is completed accurately, securely, and audibly, with downstream records synchronized and no loss of historical traceability.

### Related Functional Requirements

- FR-WLK-001 - Identify or Register Walk-in Customer
- FR-WLK-003 - Create Walk-in Visit
- FR-WLK-004 - Calculate Walk-in Charges
- FR-WLK-005 - Collect Walk-in Payment
- FR-AUD-001 - Record Audit Events

### Notes

Validate Walk-in Eligibility shall remain aligned with the approved BA source documents and shall not introduce behavior that bypasses tenant isolation, lifecycle governance, financial controls, or auditability.

---

## FR-WLK-003 - Create Walk-in Visit

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-WLK-003 |
| Requirement Name | Create Walk-in Visit |
| Functional Module | Walk-in Customer Management |
| Business Domain | Walk-in |
| Business Capability | Walk-in Visit Management |
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
| Business Requirement | BA-08 BR-014 Walk-in Visit Recording |
| Business Rule | BA-02 BR-ATT-002, BR-ATT-003, BR-ATT-005, BR-CUS-009, BR-SEC-004 |
| Business Process | BA-03 BP-ATT-004 Record Walk-in Attendance |
| Business Process Flow | BA-04 Section 20 Walk-in Customer Flow |
| Persona | BA-05 Reception Staff, Customer, Finance Staff |
| User Journey | BA-06 Section 16 Walk-in Customer Journey, Section 17 Attendance Journey |
| Stakeholder | BA-07 Reception Staff, Customer, Finance Staff |
| Non-Functional Requirement | BA-09 Section 2.4 Performance, Section 2.10 Auditability, Section 3.7 Data Protection |
| Assumption / Constraint / Risk | BA-10 BA-ASS-011, BA-RSK-008, BA-RSK-012 |

### Purpose

To enable Walk-in Visit Management within Walk-in Customer Management so Digitize can execute Create Walk-in Visit consistently across Organizations, Facilities, Sites, users, and related operational or commercial services.

### Functional Requirement

The system shall support Create Walk-in Visit as an atomic Walk-in Customer Management capability, including scoped data capture, business-rule validation, permission enforcement, lifecycle handling, related service synchronization, notification generation, reporting contribution, and immutable audit recording.

### Business Justification

Create Walk-in Visit is required to preserve operational control, revenue accuracy, service continuity, customer trust, and enterprise traceability for Walk-in processes. Without this capability, downstream modules would rely on incomplete, manual, or inconsistent records.

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
- Actor has permission for Create Walk-in Visit.
- Required Walk-in configuration and policies are available.
- Related records required by BA-03 BP-ATT-004 Record Walk-in Attendance are available and within authorized scope.

### Trigger

The capability is triggered when Reception Staff or the System initiates Create Walk-in Visit from Walk-in Visit, a related workflow, a scheduled job, or an approved integration event.

### In Scope

- Capture or retrieve required Walk-in context.
- Validate Organization, Facility, Site, Customer, user, and policy scope where applicable.
- Execute Create Walk-in Visit according to approved business rules.
- Persist the resulting Walk-in Visit state or transaction.
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
- Walk-in Visit reference
- Customer reference, where applicable
- Effective date and time, where applicable
- Status or action reason, where applicable
- Payment, billing, trainer, session, or subscription reference where applicable
- Actor remarks, where applicable

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Walk-in Visit ID | Primary business record reference | Identifier | Yes | System / User | Must exist or be generated within scope | Core reference for Create Walk-in Visit |
| Organization ID | Tenant Organization context | Identifier | Yes | Session / System | Must be Active and authorized | Enforces tenant isolation |
| Facility ID | Facility context | Identifier | Conditional | User / System | Must be Active where applicable | Required for facility-level operations |
| Site ID | Site context | Identifier | Conditional | User / System | Must belong to Facility where applicable | Required for site-level operations |
| Status | Lifecycle or processing state | Enum | Yes | System | Must follow allowed state transitions | Drives UI and downstream access |
| Effective Date | Date when action applies | DateTime | Conditional | User / System | Must satisfy policy | Supports scheduled or immediate actions |
| Reason / Remarks | Business explanation | Text | Conditional | User | Required for governed changes | Stored for audit |

### Main Flow

1. Actor opens Walk-in Visit or the related workflow.
2. The system validates authentication, authorization, tenant scope, and current operating context.
3. The system loads the required Walk-in records, related configuration, and policy controls.
4. Actor enters or confirms the information required to create walk-in visit.
5. The system validates mandatory data, lifecycle status, ownership, eligibility, financial, capacity, schedule, and security rules where applicable.
6. The system executes Create Walk-in Visit and persists the resulting Walk-in Visit state or transaction.
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

- Walk-in Visit record created, updated, validated, or reported according to the action.
- Lifecycle or processing status updated.
- Related history entry created.
- Business events emitted.
- Notifications generated where configured.
- Audit events recorded.
- Reports or dashboards updated where applicable.

### UI Behaviour

Walk-in Visit shall display scoped context, mandatory fields, lifecycle status, policy warnings, validation results, available actions, confirmation prompts, read-only states, pagination or filters where applicable, and responsive behavior for front-desk and administrative usage.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-WLK-003-001 | Actor must have permission to execute Create Walk-in Visit. | Deny request and audit. | Critical |
| VAL-WLK-003-002 | Record must belong to the authorized Organization scope. | Deny request. | Critical |
| VAL-WLK-003-003 | Mandatory inputs must be complete and valid. | Block submission. | Critical |
| VAL-WLK-003-004 | Lifecycle and policy rules from BA-02 must be satisfied. | Reject or route for approval. | High |
| VAL-WLK-003-005 | Historical and audit records must be preserved. | Roll back or mark for recovery. | Critical |

### Business Rules

- BA-02 BR-ATT-002
- BA-02 BR-ATT-003
- BA-02 BR-ATT-005
- BA-02 BR-CUS-009
- BA-02 BR-SEC-004

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| wlk.create.walk.in.visit.view | Reception Staff | Read | View Create Walk-in Visit context |
| wlk.create.walk.in.visit.execute | Reception Staff | Execute | Execute Create Walk-in Visit |
| wlk.create.walk.in.visit.approve | Organization Administrator | Approve | Approve governed exceptions where configured |
| wlk.create.walk.in.visit.audit.view | Organization Administrator / Support Executive | Read | View audit trace |

### Security Considerations

The capability shall enforce authentication, role-based authorization, tenant isolation, Organization scope, Facility and Site access boundaries, sensitive data masking, secure references, and immutable audit logging.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Create Walk-in Visit Completed | Primary actor and configured stakeholders | In-App / Email | Action completes | Include reference, status, and effective date where applicable |
| Create Walk-in Visit Requires Approval | Approver | In-App | Approval rule applies | Include safe summary and requested action |
| Create Walk-in Visit Failed | Primary actor | In-App | Validation or processing fails | Include safe failure reason and next action |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| CreateWalkinVisitRequested | Walk-in Customer Management | Approval Workflow, Audit Service |
| CreateWalkinVisitCompleted | Walk-in Customer Management | Notification Service, Reporting Service, Audit Service |
| CreateWalkinVisitRejected | Walk-in Customer Management | Notification Service, Audit Service |

### Audit Events

| Audit Event | Description | Actor | Target Entity | Key Data |
|---|---|---|---|---|
| CREATE_WALKIN_VISIT_REQUESTED | Create Walk-in Visit requested | Reception Staff | Walk-in Visit | Scope, reference, and reason |
| CREATE_WALKIN_VISIT_COMPLETED | Create Walk-in Visit completed | Reception Staff / System | Walk-in Visit | Previous and new state |
| CREATE_WALKIN_VISIT_REJECTED | Create Walk-in Visit rejected | System | Walk-in Visit | Rejection reason |

### Reports Generated

- Walk-in Customer Management Operational Report
- Walk-in Customer Management History Report
- Walk-in Customer Management Exception Report
- Executive Dashboard

### Related Screens

- Walk-in Visit
- Walk-in Customer Management Dashboard
- Walk-in Customer Management History
- Audit Log Viewer

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/walkins | POST | Authorized token | Execute Create Walk-in Visit | 200 OK or 201 Created with result |
| /api/v1/walkins/history | GET | Authorized token | Retrieve Create Walk-in Visit history | 200 OK with history |
| /api/v1/audit-logs | GET | Authorized token | Retrieve related audit events | 200 OK with scoped audit records |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Walk-in Visit | Create / Update / Read | Support Create Walk-in Visit | Governed by Organization scope |
| Customer | Read / Insert | Support Create Walk-in Visit | Governed by Organization scope |
| Attendance | Read / Insert | Support Create Walk-in Visit | Governed by Organization scope |
| Invoice | Read / Insert | Support Create Walk-in Visit | Governed by Organization scope |
| Payment | Read / Insert | Support Create Walk-in Visit | Governed by Organization scope |
| Audit Log | Insert | Record auditable activity | Immutable |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Draft | Create Walk-in Visit initiated | Validated | Reception Staff | Required data captured |
| Validated | Validation succeeds | Pending Approval | System | BA-02 rules satisfied |
| Pending Approval | Processing completes | Completed | System | Related updates succeed |
| Pending Approval | Approval or policy failure | Rejected | System / Approver | Request rejected |
| Completed | View history | Completed | Authorized user | Read-only historical access |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| WLK-003-001 | Create Walk-in Visit cannot be completed because required information is missing. | Missing mandatory data | Complete required fields |
| WLK-003-002 | You do not have permission to perform this action. | Authorization failure | Request access |
| WLK-003-003 | The selected record is not eligible for this action. | Policy or lifecycle violation | Review record status |
| WLK-003-004 | Create Walk-in Visit could not be completed due to a system or integration error. | Processing failure | Retry or contact support |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Execute Create Walk-in Visit | Given the actor has required permission and valid scope | When the actor submits valid information | Then the system shall complete Create Walk-in Visit successfully |
| Enforce validation | Given mandatory data or policy conditions are invalid | When the action is submitted | Then the system shall reject the request with a clear message |
| Preserve audit | Given the action completes or fails | When processing ends | Then audit events shall record actor, timestamp, scope, and outcome |
| Protect scope | Given the selected record is outside authorized scope | When the action is requested | Then the system shall deny access |

### Dependencies

- Customer Management
- Attendance Management
- Billing Management
- Payment Management
- Notification Management
- Audit Service

### Operational Considerations

Create Walk-in Visit should be designed for high-volume operational use, retry-safe processing, clear exception handling, and support-team diagnostics without exposing sensitive data.

### Non-Functional Considerations

This requirement shall satisfy Digitize non-functional expectations for availability, reliability, performance, scalability, security, configurability, maintainability, and auditability.

### Assumptions

- Required master data and configuration are maintained by authorized users.
- Related services expose stable APIs for validation and synchronization.
- Organization policies define approval, retention, notification, and exception behavior.

### Success Criteria

Create Walk-in Visit is completed accurately, securely, and audibly, with downstream records synchronized and no loss of historical traceability.

### Related Functional Requirements

- FR-WLK-001 - Identify or Register Walk-in Customer
- FR-WLK-002 - Validate Walk-in Eligibility
- FR-WLK-004 - Calculate Walk-in Charges
- FR-WLK-005 - Collect Walk-in Payment
- FR-AUD-001 - Record Audit Events

### Notes

Create Walk-in Visit shall remain aligned with the approved BA source documents and shall not introduce behavior that bypasses tenant isolation, lifecycle governance, financial controls, or auditability.

---

## FR-WLK-004 - Calculate Walk-in Charges

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-WLK-004 |
| Requirement Name | Calculate Walk-in Charges |
| Functional Module | Walk-in Customer Management |
| Business Domain | Walk-in |
| Business Capability | Walk-in Billing |
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
| Business Requirement | BA-08 BR-014 Walk-in Visit Recording |
| Business Rule | BA-02 BR-BIL-001, BR-BIL-004, BR-BIL-008, BR-ATT-005 |
| Business Process | BA-03 BP-BIL-003 Calculate Walk-in Charges |
| Business Process Flow | BA-04 Section 20 Walk-in Customer Flow |
| Persona | BA-05 Reception Staff, Customer, Finance Staff |
| User Journey | BA-06 Section 16 Walk-in Customer Journey, Section 17 Attendance Journey |
| Stakeholder | BA-07 Reception Staff, Customer, Finance Staff |
| Non-Functional Requirement | BA-09 Section 2.4 Performance, Section 2.10 Auditability, Section 3.7 Data Protection |
| Assumption / Constraint / Risk | BA-10 BA-ASS-011, BA-RSK-008, BA-RSK-012 |

### Purpose

To enable Walk-in Billing within Walk-in Customer Management so Digitize can execute Calculate Walk-in Charges consistently across Organizations, Facilities, Sites, users, and related operational or commercial services.

### Functional Requirement

The system shall support Calculate Walk-in Charges as an atomic Walk-in Customer Management capability, including scoped data capture, business-rule validation, permission enforcement, lifecycle handling, related service synchronization, notification generation, reporting contribution, and immutable audit recording.

### Business Justification

Calculate Walk-in Charges is required to preserve operational control, revenue accuracy, service continuity, customer trust, and enterprise traceability for Walk-in processes. Without this capability, downstream modules would rely on incomplete, manual, or inconsistent records.

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
- Actor has permission for Calculate Walk-in Charges.
- Required Walk-in configuration and policies are available.
- Related records required by BA-03 BP-BIL-003 Calculate Walk-in Charges are available and within authorized scope.

### Trigger

The capability is triggered when System or the System initiates Calculate Walk-in Charges from Billing Checkout, a related workflow, a scheduled job, or an approved integration event.

### In Scope

- Capture or retrieve required Walk-in context.
- Validate Organization, Facility, Site, Customer, user, and policy scope where applicable.
- Execute Calculate Walk-in Charges according to approved business rules.
- Persist the resulting Walk-in Visit state or transaction.
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
- Walk-in Visit reference
- Customer reference, where applicable
- Effective date and time, where applicable
- Status or action reason, where applicable
- Payment, billing, trainer, session, or subscription reference where applicable
- Actor remarks, where applicable

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Walk-in Visit ID | Primary business record reference | Identifier | Yes | System / User | Must exist or be generated within scope | Core reference for Calculate Walk-in Charges |
| Organization ID | Tenant Organization context | Identifier | Yes | Session / System | Must be Active and authorized | Enforces tenant isolation |
| Facility ID | Facility context | Identifier | Conditional | User / System | Must be Active where applicable | Required for facility-level operations |
| Site ID | Site context | Identifier | Conditional | User / System | Must belong to Facility where applicable | Required for site-level operations |
| Status | Lifecycle or processing state | Enum | Yes | System | Must follow allowed state transitions | Drives UI and downstream access |
| Effective Date | Date when action applies | DateTime | Conditional | User / System | Must satisfy policy | Supports scheduled or immediate actions |
| Reason / Remarks | Business explanation | Text | Conditional | User | Required for governed changes | Stored for audit |

### Main Flow

1. Actor opens Billing Checkout or the related workflow.
2. The system validates authentication, authorization, tenant scope, and current operating context.
3. The system loads the required Walk-in records, related configuration, and policy controls.
4. Actor enters or confirms the information required to calculate walk-in charges.
5. The system validates mandatory data, lifecycle status, ownership, eligibility, financial, capacity, schedule, and security rules where applicable.
6. The system executes Calculate Walk-in Charges and persists the resulting Walk-in Visit state or transaction.
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

- Walk-in Visit record created, updated, validated, or reported according to the action.
- Lifecycle or processing status updated.
- Related history entry created.
- Business events emitted.
- Notifications generated where configured.
- Audit events recorded.
- Reports or dashboards updated where applicable.

### UI Behaviour

Billing Checkout shall display scoped context, mandatory fields, lifecycle status, policy warnings, validation results, available actions, confirmation prompts, read-only states, pagination or filters where applicable, and responsive behavior for front-desk and administrative usage.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-WLK-004-001 | Actor must have permission to execute Calculate Walk-in Charges. | Deny request and audit. | Critical |
| VAL-WLK-004-002 | Record must belong to the authorized Organization scope. | Deny request. | Critical |
| VAL-WLK-004-003 | Mandatory inputs must be complete and valid. | Block submission. | Critical |
| VAL-WLK-004-004 | Lifecycle and policy rules from BA-02 must be satisfied. | Reject or route for approval. | High |
| VAL-WLK-004-005 | Historical and audit records must be preserved. | Roll back or mark for recovery. | Critical |

### Business Rules

- BA-02 BR-BIL-001
- BA-02 BR-BIL-004
- BA-02 BR-BIL-008
- BA-02 BR-ATT-005

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| wlk.calculate.walk.in.charges.view | System | Read | View Calculate Walk-in Charges context |
| wlk.calculate.walk.in.charges.execute | System | Execute | Execute Calculate Walk-in Charges |
| wlk.calculate.walk.in.charges.approve | Organization Administrator | Approve | Approve governed exceptions where configured |
| wlk.calculate.walk.in.charges.audit.view | Organization Administrator / Support Executive | Read | View audit trace |

### Security Considerations

The capability shall enforce authentication, role-based authorization, tenant isolation, Organization scope, Facility and Site access boundaries, sensitive data masking, secure references, and immutable audit logging.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Calculate Walk-in Charges Completed | Primary actor and configured stakeholders | In-App / Email | Action completes | Include reference, status, and effective date where applicable |
| Calculate Walk-in Charges Requires Approval | Approver | In-App | Approval rule applies | Include safe summary and requested action |
| Calculate Walk-in Charges Failed | Primary actor | In-App | Validation or processing fails | Include safe failure reason and next action |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| CalculateWalkinChargesRequested | Walk-in Customer Management | Approval Workflow, Audit Service |
| CalculateWalkinChargesCompleted | Walk-in Customer Management | Notification Service, Reporting Service, Audit Service |
| CalculateWalkinChargesRejected | Walk-in Customer Management | Notification Service, Audit Service |

### Audit Events

| Audit Event | Description | Actor | Target Entity | Key Data |
|---|---|---|---|---|
| CALCULATE_WALKIN_CHARGES_REQUESTED | Calculate Walk-in Charges requested | System | Walk-in Visit | Scope, reference, and reason |
| CALCULATE_WALKIN_CHARGES_COMPLETED | Calculate Walk-in Charges completed | System / System | Walk-in Visit | Previous and new state |
| CALCULATE_WALKIN_CHARGES_REJECTED | Calculate Walk-in Charges rejected | System | Walk-in Visit | Rejection reason |

### Reports Generated

- Walk-in Customer Management Operational Report
- Walk-in Customer Management History Report
- Walk-in Customer Management Exception Report
- Executive Dashboard

### Related Screens

- Billing Checkout
- Walk-in Customer Management Dashboard
- Walk-in Customer Management History
- Audit Log Viewer

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/billing/walk-in-charges | POST | Authorized token | Execute Calculate Walk-in Charges | 200 OK or 201 Created with result |
| /api/v1/billing/walk-in-charges/history | GET | Authorized token | Retrieve Calculate Walk-in Charges history | 200 OK with history |
| /api/v1/audit-logs | GET | Authorized token | Retrieve related audit events | 200 OK with scoped audit records |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Walk-in Visit | Create / Update / Read | Support Calculate Walk-in Charges | Governed by Organization scope |
| Customer | Read / Insert | Support Calculate Walk-in Charges | Governed by Organization scope |
| Attendance | Read / Insert | Support Calculate Walk-in Charges | Governed by Organization scope |
| Invoice | Read / Insert | Support Calculate Walk-in Charges | Governed by Organization scope |
| Payment | Read / Insert | Support Calculate Walk-in Charges | Governed by Organization scope |
| Audit Log | Insert | Record auditable activity | Immutable |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Requested | Calculate Walk-in Charges initiated | Eligible | System | Required data captured |
| Eligible | Validation succeeds | Requires Override | System | BA-02 rules satisfied |
| Requires Override | Processing completes | Denied | System | Related updates succeed |
| Requires Override | Approval or policy failure | Failed | System / Approver | Request rejected |
| Denied | View history | Denied | Authorized user | Read-only historical access |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| WLK-004-001 | Calculate Walk-in Charges cannot be completed because required information is missing. | Missing mandatory data | Complete required fields |
| WLK-004-002 | You do not have permission to perform this action. | Authorization failure | Request access |
| WLK-004-003 | The selected record is not eligible for this action. | Policy or lifecycle violation | Review record status |
| WLK-004-004 | Calculate Walk-in Charges could not be completed due to a system or integration error. | Processing failure | Retry or contact support |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Execute Calculate Walk-in Charges | Given the actor has required permission and valid scope | When the actor submits valid information | Then the system shall complete Calculate Walk-in Charges successfully |
| Enforce validation | Given mandatory data or policy conditions are invalid | When the action is submitted | Then the system shall reject the request with a clear message |
| Preserve audit | Given the action completes or fails | When processing ends | Then audit events shall record actor, timestamp, scope, and outcome |
| Protect scope | Given the selected record is outside authorized scope | When the action is requested | Then the system shall deny access |

### Dependencies

- Customer Management
- Attendance Management
- Billing Management
- Payment Management
- Notification Management
- Audit Service

### Operational Considerations

Calculate Walk-in Charges should be designed for high-volume operational use, retry-safe processing, clear exception handling, and support-team diagnostics without exposing sensitive data.

### Non-Functional Considerations

This requirement shall satisfy Digitize non-functional expectations for availability, reliability, performance, scalability, security, configurability, maintainability, and auditability.

### Assumptions

- Required master data and configuration are maintained by authorized users.
- Related services expose stable APIs for validation and synchronization.
- Organization policies define approval, retention, notification, and exception behavior.

### Success Criteria

Calculate Walk-in Charges is completed accurately, securely, and audibly, with downstream records synchronized and no loss of historical traceability.

### Related Functional Requirements

- FR-WLK-001 - Identify or Register Walk-in Customer
- FR-WLK-002 - Validate Walk-in Eligibility
- FR-WLK-003 - Create Walk-in Visit
- FR-WLK-005 - Collect Walk-in Payment
- FR-AUD-001 - Record Audit Events

### Notes

Calculate Walk-in Charges shall remain aligned with the approved BA source documents and shall not introduce behavior that bypasses tenant isolation, lifecycle governance, financial controls, or auditability.

---

## FR-WLK-005 - Collect Walk-in Payment

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-WLK-005 |
| Requirement Name | Collect Walk-in Payment |
| Functional Module | Walk-in Customer Management |
| Business Domain | Walk-in |
| Business Capability | Walk-in Payment |
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
| Business Requirement | BA-08 BR-014 Walk-in Visit Recording, BR-019 Payment Collection |
| Business Rule | BA-02 BR-PAY-001, BR-PAY-002, BR-PAY-003, BR-PAY-005, BR-PAY-007 |
| Business Process | BA-03 BP-PAY-001 Collect Payment |
| Business Process Flow | BA-04 Section 20 Walk-in Customer Flow |
| Persona | BA-05 Reception Staff, Customer, Finance Staff |
| User Journey | BA-06 Section 16 Walk-in Customer Journey, Section 17 Attendance Journey |
| Stakeholder | BA-07 Reception Staff, Customer, Finance Staff |
| Non-Functional Requirement | BA-09 Section 2.4 Performance, Section 2.10 Auditability, Section 3.7 Data Protection |
| Assumption / Constraint / Risk | BA-10 BA-ASS-011, BA-RSK-008, BA-RSK-012 |

### Purpose

To enable Walk-in Payment within Walk-in Customer Management so Digitize can execute Collect Walk-in Payment consistently across Organizations, Facilities, Sites, users, and related operational or commercial services.

### Functional Requirement

The system shall support Collect Walk-in Payment as an atomic Walk-in Customer Management capability, including scoped data capture, business-rule validation, permission enforcement, lifecycle handling, related service synchronization, notification generation, reporting contribution, and immutable audit recording.

### Business Justification

Collect Walk-in Payment is required to preserve operational control, revenue accuracy, service continuity, customer trust, and enterprise traceability for Walk-in processes. Without this capability, downstream modules would rely on incomplete, manual, or inconsistent records.

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
- Actor has permission for Collect Walk-in Payment.
- Required Walk-in configuration and policies are available.
- Related records required by BA-03 BP-PAY-001 Collect Payment are available and within authorized scope.

### Trigger

The capability is triggered when Reception Staff or the System initiates Collect Walk-in Payment from Payment Collection, a related workflow, a scheduled job, or an approved integration event.

### In Scope

- Capture or retrieve required Walk-in context.
- Validate Organization, Facility, Site, Customer, user, and policy scope where applicable.
- Execute Collect Walk-in Payment according to approved business rules.
- Persist the resulting Walk-in Visit state or transaction.
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
- Walk-in Visit reference
- Customer reference, where applicable
- Effective date and time, where applicable
- Status or action reason, where applicable
- Payment, billing, trainer, session, or subscription reference where applicable
- Actor remarks, where applicable

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Walk-in Visit ID | Primary business record reference | Identifier | Yes | System / User | Must exist or be generated within scope | Core reference for Collect Walk-in Payment |
| Organization ID | Tenant Organization context | Identifier | Yes | Session / System | Must be Active and authorized | Enforces tenant isolation |
| Facility ID | Facility context | Identifier | Conditional | User / System | Must be Active where applicable | Required for facility-level operations |
| Site ID | Site context | Identifier | Conditional | User / System | Must belong to Facility where applicable | Required for site-level operations |
| Status | Lifecycle or processing state | Enum | Yes | System | Must follow allowed state transitions | Drives UI and downstream access |
| Effective Date | Date when action applies | DateTime | Conditional | User / System | Must satisfy policy | Supports scheduled or immediate actions |
| Reason / Remarks | Business explanation | Text | Conditional | User | Required for governed changes | Stored for audit |

### Main Flow

1. Actor opens Payment Collection or the related workflow.
2. The system validates authentication, authorization, tenant scope, and current operating context.
3. The system loads the required Walk-in records, related configuration, and policy controls.
4. Actor enters or confirms the information required to collect walk-in payment.
5. The system validates mandatory data, lifecycle status, ownership, eligibility, financial, capacity, schedule, and security rules where applicable.
6. The system executes Collect Walk-in Payment and persists the resulting Walk-in Visit state or transaction.
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

- Walk-in Visit record created, updated, validated, or reported according to the action.
- Lifecycle or processing status updated.
- Related history entry created.
- Business events emitted.
- Notifications generated where configured.
- Audit events recorded.
- Reports or dashboards updated where applicable.

### UI Behaviour

Payment Collection shall display scoped context, mandatory fields, lifecycle status, policy warnings, validation results, available actions, confirmation prompts, read-only states, pagination or filters where applicable, and responsive behavior for front-desk and administrative usage.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-WLK-005-001 | Actor must have permission to execute Collect Walk-in Payment. | Deny request and audit. | Critical |
| VAL-WLK-005-002 | Record must belong to the authorized Organization scope. | Deny request. | Critical |
| VAL-WLK-005-003 | Mandatory inputs must be complete and valid. | Block submission. | Critical |
| VAL-WLK-005-004 | Lifecycle and policy rules from BA-02 must be satisfied. | Reject or route for approval. | High |
| VAL-WLK-005-005 | Historical and audit records must be preserved. | Roll back or mark for recovery. | Critical |

### Business Rules

- BA-02 BR-PAY-001
- BA-02 BR-PAY-002
- BA-02 BR-PAY-003
- BA-02 BR-PAY-005
- BA-02 BR-PAY-007

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| wlk.collect.walk.in.payment.view | Reception Staff | Read | View Collect Walk-in Payment context |
| wlk.collect.walk.in.payment.execute | Reception Staff | Execute | Execute Collect Walk-in Payment |
| wlk.collect.walk.in.payment.approve | Organization Administrator | Approve | Approve governed exceptions where configured |
| wlk.collect.walk.in.payment.audit.view | Organization Administrator / Support Executive | Read | View audit trace |

### Security Considerations

The capability shall enforce authentication, role-based authorization, tenant isolation, Organization scope, Facility and Site access boundaries, sensitive data masking, secure references, and immutable audit logging.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Collect Walk-in Payment Completed | Primary actor and configured stakeholders | In-App / Email | Action completes | Include reference, status, and effective date where applicable |
| Collect Walk-in Payment Requires Approval | Approver | In-App | Approval rule applies | Include safe summary and requested action |
| Collect Walk-in Payment Failed | Primary actor | In-App | Validation or processing fails | Include safe failure reason and next action |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| CollectWalkinPaymentRequested | Walk-in Customer Management | Approval Workflow, Audit Service |
| CollectWalkinPaymentCompleted | Walk-in Customer Management | Notification Service, Reporting Service, Audit Service |
| CollectWalkinPaymentRejected | Walk-in Customer Management | Notification Service, Audit Service |

### Audit Events

| Audit Event | Description | Actor | Target Entity | Key Data |
|---|---|---|---|---|
| COLLECT_WALKIN_PAYMENT_REQUESTED | Collect Walk-in Payment requested | Reception Staff | Walk-in Visit | Scope, reference, and reason |
| COLLECT_WALKIN_PAYMENT_COMPLETED | Collect Walk-in Payment completed | Reception Staff / System | Walk-in Visit | Previous and new state |
| COLLECT_WALKIN_PAYMENT_REJECTED | Collect Walk-in Payment rejected | System | Walk-in Visit | Rejection reason |

### Reports Generated

- Walk-in Customer Management Operational Report
- Walk-in Customer Management History Report
- Walk-in Customer Management Exception Report
- Executive Dashboard

### Related Screens

- Payment Collection
- Walk-in Customer Management Dashboard
- Walk-in Customer Management History
- Audit Log Viewer

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/payments | POST | Authorized token | Execute Collect Walk-in Payment | 200 OK or 201 Created with result |
| /api/v1/payments/history | GET | Authorized token | Retrieve Collect Walk-in Payment history | 200 OK with history |
| /api/v1/audit-logs | GET | Authorized token | Retrieve related audit events | 200 OK with scoped audit records |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Walk-in Visit | Create / Update / Read | Support Collect Walk-in Payment | Governed by Organization scope |
| Customer | Read / Insert | Support Collect Walk-in Payment | Governed by Organization scope |
| Attendance | Read / Insert | Support Collect Walk-in Payment | Governed by Organization scope |
| Invoice | Read / Insert | Support Collect Walk-in Payment | Governed by Organization scope |
| Payment | Read / Insert | Support Collect Walk-in Payment | Governed by Organization scope |
| Audit Log | Insert | Record auditable activity | Immutable |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Draft | Collect Walk-in Payment initiated | Validated | Reception Staff | Required data captured |
| Validated | Validation succeeds | Pending Approval | System | BA-02 rules satisfied |
| Pending Approval | Processing completes | Completed | System | Related updates succeed |
| Pending Approval | Approval or policy failure | Rejected | System / Approver | Request rejected |
| Completed | View history | Completed | Authorized user | Read-only historical access |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| WLK-005-001 | Collect Walk-in Payment cannot be completed because required information is missing. | Missing mandatory data | Complete required fields |
| WLK-005-002 | You do not have permission to perform this action. | Authorization failure | Request access |
| WLK-005-003 | The selected record is not eligible for this action. | Policy or lifecycle violation | Review record status |
| WLK-005-004 | Collect Walk-in Payment could not be completed due to a system or integration error. | Processing failure | Retry or contact support |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Execute Collect Walk-in Payment | Given the actor has required permission and valid scope | When the actor submits valid information | Then the system shall complete Collect Walk-in Payment successfully |
| Enforce validation | Given mandatory data or policy conditions are invalid | When the action is submitted | Then the system shall reject the request with a clear message |
| Preserve audit | Given the action completes or fails | When processing ends | Then audit events shall record actor, timestamp, scope, and outcome |
| Protect scope | Given the selected record is outside authorized scope | When the action is requested | Then the system shall deny access |

### Dependencies

- Customer Management
- Attendance Management
- Billing Management
- Payment Management
- Notification Management
- Audit Service

### Operational Considerations

Collect Walk-in Payment should be designed for high-volume operational use, retry-safe processing, clear exception handling, and support-team diagnostics without exposing sensitive data.

### Non-Functional Considerations

This requirement shall satisfy Digitize non-functional expectations for availability, reliability, performance, scalability, security, configurability, maintainability, and auditability.

### Assumptions

- Required master data and configuration are maintained by authorized users.
- Related services expose stable APIs for validation and synchronization.
- Organization policies define approval, retention, notification, and exception behavior.

### Success Criteria

Collect Walk-in Payment is completed accurately, securely, and audibly, with downstream records synchronized and no loss of historical traceability.

### Related Functional Requirements

- FR-WLK-001 - Identify or Register Walk-in Customer
- FR-WLK-002 - Validate Walk-in Eligibility
- FR-WLK-003 - Create Walk-in Visit
- FR-WLK-004 - Calculate Walk-in Charges
- FR-AUD-001 - Record Audit Events

### Notes

Collect Walk-in Payment shall remain aligned with the approved BA source documents and shall not introduce behavior that bypasses tenant isolation, lifecycle governance, financial controls, or auditability.

---

## FR-WLK-006 - Record Walk-in Attendance

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-WLK-006 |
| Requirement Name | Record Walk-in Attendance |
| Functional Module | Walk-in Customer Management |
| Business Domain | Walk-in |
| Business Capability | Walk-in Attendance |
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
| Business Requirement | BA-08 BR-014 Walk-in Visit Recording |
| Business Rule | BA-02 BR-ATT-002, BR-ATT-003, BR-ATT-005, BR-ATT-006, BR-ATT-009 |
| Business Process | BA-03 BP-ATT-004 Record Walk-in Attendance |
| Business Process Flow | BA-04 Section 20 Walk-in Customer Flow |
| Persona | BA-05 Reception Staff, Customer, Finance Staff |
| User Journey | BA-06 Section 16 Walk-in Customer Journey, Section 17 Attendance Journey |
| Stakeholder | BA-07 Reception Staff, Customer, Finance Staff |
| Non-Functional Requirement | BA-09 Section 2.4 Performance, Section 2.10 Auditability, Section 3.7 Data Protection |
| Assumption / Constraint / Risk | BA-10 BA-ASS-011, BA-RSK-008, BA-RSK-012 |

### Purpose

To enable Walk-in Attendance within Walk-in Customer Management so Digitize can execute Record Walk-in Attendance consistently across Organizations, Facilities, Sites, users, and related operational or commercial services.

### Functional Requirement

The system shall support Record Walk-in Attendance as an atomic Walk-in Customer Management capability, including scoped data capture, business-rule validation, permission enforcement, lifecycle handling, related service synchronization, notification generation, reporting contribution, and immutable audit recording.

### Business Justification

Record Walk-in Attendance is required to preserve operational control, revenue accuracy, service continuity, customer trust, and enterprise traceability for Walk-in processes. Without this capability, downstream modules would rely on incomplete, manual, or inconsistent records.

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
- Actor has permission for Record Walk-in Attendance.
- Required Walk-in configuration and policies are available.
- Related records required by BA-03 BP-ATT-004 Record Walk-in Attendance are available and within authorized scope.

### Trigger

The capability is triggered when Reception Staff or the System initiates Record Walk-in Attendance from Attendance Check-in, a related workflow, a scheduled job, or an approved integration event.

### In Scope

- Capture or retrieve required Walk-in context.
- Validate Organization, Facility, Site, Customer, user, and policy scope where applicable.
- Execute Record Walk-in Attendance according to approved business rules.
- Persist the resulting Walk-in Visit state or transaction.
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
- Walk-in Visit reference
- Customer reference, where applicable
- Effective date and time, where applicable
- Status or action reason, where applicable
- Payment, billing, trainer, session, or subscription reference where applicable
- Actor remarks, where applicable

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Walk-in Visit ID | Primary business record reference | Identifier | Yes | System / User | Must exist or be generated within scope | Core reference for Record Walk-in Attendance |
| Organization ID | Tenant Organization context | Identifier | Yes | Session / System | Must be Active and authorized | Enforces tenant isolation |
| Facility ID | Facility context | Identifier | Conditional | User / System | Must be Active where applicable | Required for facility-level operations |
| Site ID | Site context | Identifier | Conditional | User / System | Must belong to Facility where applicable | Required for site-level operations |
| Status | Lifecycle or processing state | Enum | Yes | System | Must follow allowed state transitions | Drives UI and downstream access |
| Effective Date | Date when action applies | DateTime | Conditional | User / System | Must satisfy policy | Supports scheduled or immediate actions |
| Reason / Remarks | Business explanation | Text | Conditional | User | Required for governed changes | Stored for audit |

### Main Flow

1. Actor opens Attendance Check-in or the related workflow.
2. The system validates authentication, authorization, tenant scope, and current operating context.
3. The system loads the required Walk-in records, related configuration, and policy controls.
4. Actor enters or confirms the information required to record walk-in attendance.
5. The system validates mandatory data, lifecycle status, ownership, eligibility, financial, capacity, schedule, and security rules where applicable.
6. The system executes Record Walk-in Attendance and persists the resulting Walk-in Visit state or transaction.
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

- Walk-in Visit record created, updated, validated, or reported according to the action.
- Lifecycle or processing status updated.
- Related history entry created.
- Business events emitted.
- Notifications generated where configured.
- Audit events recorded.
- Reports or dashboards updated where applicable.

### UI Behaviour

Attendance Check-in shall display scoped context, mandatory fields, lifecycle status, policy warnings, validation results, available actions, confirmation prompts, read-only states, pagination or filters where applicable, and responsive behavior for front-desk and administrative usage.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-WLK-006-001 | Actor must have permission to execute Record Walk-in Attendance. | Deny request and audit. | Critical |
| VAL-WLK-006-002 | Record must belong to the authorized Organization scope. | Deny request. | Critical |
| VAL-WLK-006-003 | Mandatory inputs must be complete and valid. | Block submission. | Critical |
| VAL-WLK-006-004 | Lifecycle and policy rules from BA-02 must be satisfied. | Reject or route for approval. | High |
| VAL-WLK-006-005 | Historical and audit records must be preserved. | Roll back or mark for recovery. | Critical |

### Business Rules

- BA-02 BR-ATT-002
- BA-02 BR-ATT-003
- BA-02 BR-ATT-005
- BA-02 BR-ATT-006
- BA-02 BR-ATT-009

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| wlk.record.walk.in.attendance.view | Reception Staff | Read | View Record Walk-in Attendance context |
| wlk.record.walk.in.attendance.execute | Reception Staff | Execute | Execute Record Walk-in Attendance |
| wlk.record.walk.in.attendance.approve | Organization Administrator | Approve | Approve governed exceptions where configured |
| wlk.record.walk.in.attendance.audit.view | Organization Administrator / Support Executive | Read | View audit trace |

### Security Considerations

The capability shall enforce authentication, role-based authorization, tenant isolation, Organization scope, Facility and Site access boundaries, sensitive data masking, secure references, and immutable audit logging.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Record Walk-in Attendance Completed | Primary actor and configured stakeholders | In-App / Email | Action completes | Include reference, status, and effective date where applicable |
| Record Walk-in Attendance Requires Approval | Approver | In-App | Approval rule applies | Include safe summary and requested action |
| Record Walk-in Attendance Failed | Primary actor | In-App | Validation or processing fails | Include safe failure reason and next action |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| RecordWalkinAttendanceRequested | Walk-in Customer Management | Approval Workflow, Audit Service |
| RecordWalkinAttendanceCompleted | Walk-in Customer Management | Notification Service, Reporting Service, Audit Service |
| RecordWalkinAttendanceRejected | Walk-in Customer Management | Notification Service, Audit Service |

### Audit Events

| Audit Event | Description | Actor | Target Entity | Key Data |
|---|---|---|---|---|
| RECORD_WALKIN_ATTENDANCE_REQUESTED | Record Walk-in Attendance requested | Reception Staff | Walk-in Visit | Scope, reference, and reason |
| RECORD_WALKIN_ATTENDANCE_COMPLETED | Record Walk-in Attendance completed | Reception Staff / System | Walk-in Visit | Previous and new state |
| RECORD_WALKIN_ATTENDANCE_REJECTED | Record Walk-in Attendance rejected | System | Walk-in Visit | Rejection reason |

### Reports Generated

- Walk-in Customer Management Operational Report
- Walk-in Customer Management History Report
- Walk-in Customer Management Exception Report
- Executive Dashboard

### Related Screens

- Attendance Check-in
- Walk-in Customer Management Dashboard
- Walk-in Customer Management History
- Audit Log Viewer

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/attendance/walk-ins | POST | Authorized token | Execute Record Walk-in Attendance | 200 OK or 201 Created with result |
| /api/v1/attendance/walk-ins/history | GET | Authorized token | Retrieve Record Walk-in Attendance history | 200 OK with history |
| /api/v1/audit-logs | GET | Authorized token | Retrieve related audit events | 200 OK with scoped audit records |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Walk-in Visit | Create / Update / Read | Support Record Walk-in Attendance | Governed by Organization scope |
| Customer | Read / Insert | Support Record Walk-in Attendance | Governed by Organization scope |
| Attendance | Read / Insert | Support Record Walk-in Attendance | Governed by Organization scope |
| Invoice | Read / Insert | Support Record Walk-in Attendance | Governed by Organization scope |
| Payment | Read / Insert | Support Record Walk-in Attendance | Governed by Organization scope |
| Audit Log | Insert | Record auditable activity | Immutable |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Draft | Record Walk-in Attendance initiated | Validated | Reception Staff | Required data captured |
| Validated | Validation succeeds | Pending Approval | System | BA-02 rules satisfied |
| Pending Approval | Processing completes | Completed | System | Related updates succeed |
| Pending Approval | Approval or policy failure | Rejected | System / Approver | Request rejected |
| Completed | View history | Completed | Authorized user | Read-only historical access |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| WLK-006-001 | Record Walk-in Attendance cannot be completed because required information is missing. | Missing mandatory data | Complete required fields |
| WLK-006-002 | You do not have permission to perform this action. | Authorization failure | Request access |
| WLK-006-003 | The selected record is not eligible for this action. | Policy or lifecycle violation | Review record status |
| WLK-006-004 | Record Walk-in Attendance could not be completed due to a system or integration error. | Processing failure | Retry or contact support |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Execute Record Walk-in Attendance | Given the actor has required permission and valid scope | When the actor submits valid information | Then the system shall complete Record Walk-in Attendance successfully |
| Enforce validation | Given mandatory data or policy conditions are invalid | When the action is submitted | Then the system shall reject the request with a clear message |
| Preserve audit | Given the action completes or fails | When processing ends | Then audit events shall record actor, timestamp, scope, and outcome |
| Protect scope | Given the selected record is outside authorized scope | When the action is requested | Then the system shall deny access |

### Dependencies

- Customer Management
- Attendance Management
- Billing Management
- Payment Management
- Notification Management
- Audit Service

### Operational Considerations

Record Walk-in Attendance should be designed for high-volume operational use, retry-safe processing, clear exception handling, and support-team diagnostics without exposing sensitive data.

### Non-Functional Considerations

This requirement shall satisfy Digitize non-functional expectations for availability, reliability, performance, scalability, security, configurability, maintainability, and auditability.

### Assumptions

- Required master data and configuration are maintained by authorized users.
- Related services expose stable APIs for validation and synchronization.
- Organization policies define approval, retention, notification, and exception behavior.

### Success Criteria

Record Walk-in Attendance is completed accurately, securely, and audibly, with downstream records synchronized and no loss of historical traceability.

### Related Functional Requirements

- FR-WLK-001 - Identify or Register Walk-in Customer
- FR-WLK-002 - Validate Walk-in Eligibility
- FR-WLK-003 - Create Walk-in Visit
- FR-WLK-004 - Calculate Walk-in Charges
- FR-AUD-001 - Record Audit Events

### Notes

Record Walk-in Attendance shall remain aligned with the approved BA source documents and shall not introduce behavior that bypasses tenant isolation, lifecycle governance, financial controls, or auditability.

---

## FR-WLK-007 - View Walk-in History and Reports

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-WLK-007 |
| Requirement Name | View Walk-in History and Reports |
| Functional Module | Walk-in Customer Management |
| Business Domain | Walk-in |
| Business Capability | Walk-in Monitoring |
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
| Business Requirement | BA-08 BR-014 Walk-in Visit Recording |
| Business Rule | BA-02 BR-ATT-005, BR-ATT-009, BR-ATT-010, BR-BIL-008, BR-SEC-004 |
| Business Process | BA-03 BP-ATT-004 Record Walk-in Attendance |
| Business Process Flow | BA-04 Section 20 Walk-in Customer Flow |
| Persona | BA-05 Reception Staff, Customer, Finance Staff |
| User Journey | BA-06 Section 16 Walk-in Customer Journey, Section 17 Attendance Journey |
| Stakeholder | BA-07 Reception Staff, Customer, Finance Staff |
| Non-Functional Requirement | BA-09 Section 2.4 Performance, Section 2.10 Auditability, Section 3.7 Data Protection |
| Assumption / Constraint / Risk | BA-10 BA-ASS-011, BA-RSK-008, BA-RSK-012 |

### Purpose

To enable Walk-in Monitoring within Walk-in Customer Management so Digitize can execute View Walk-in History and Reports consistently across Organizations, Facilities, Sites, users, and related operational or commercial services.

### Functional Requirement

The system shall support View Walk-in History and Reports as an atomic Walk-in Customer Management capability, including scoped data capture, business-rule validation, permission enforcement, lifecycle handling, related service synchronization, notification generation, reporting contribution, and immutable audit recording.

### Business Justification

View Walk-in History and Reports is required to preserve operational control, revenue accuracy, service continuity, customer trust, and enterprise traceability for Walk-in processes. Without this capability, downstream modules would rely on incomplete, manual, or inconsistent records.

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
- Actor has permission for View Walk-in History and Reports.
- Required Walk-in configuration and policies are available.
- Related records required by BA-03 BP-ATT-004 Record Walk-in Attendance are available and within authorized scope.

### Trigger

The capability is triggered when Reception Staff or the System initiates View Walk-in History and Reports from Walk-in History, a related workflow, a scheduled job, or an approved integration event.

### In Scope

- Capture or retrieve required Walk-in context.
- Validate Organization, Facility, Site, Customer, user, and policy scope where applicable.
- Execute View Walk-in History and Reports according to approved business rules.
- Persist the resulting Walk-in Visit state or transaction.
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
- Walk-in Visit reference
- Customer reference, where applicable
- Effective date and time, where applicable
- Status or action reason, where applicable
- Payment, billing, trainer, session, or subscription reference where applicable
- Actor remarks, where applicable

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Walk-in Visit ID | Primary business record reference | Identifier | Yes | System / User | Must exist or be generated within scope | Core reference for View Walk-in History and Reports |
| Organization ID | Tenant Organization context | Identifier | Yes | Session / System | Must be Active and authorized | Enforces tenant isolation |
| Facility ID | Facility context | Identifier | Conditional | User / System | Must be Active where applicable | Required for facility-level operations |
| Site ID | Site context | Identifier | Conditional | User / System | Must belong to Facility where applicable | Required for site-level operations |
| Status | Lifecycle or processing state | Enum | Yes | System | Must follow allowed state transitions | Drives UI and downstream access |
| Effective Date | Date when action applies | DateTime | Conditional | User / System | Must satisfy policy | Supports scheduled or immediate actions |
| Reason / Remarks | Business explanation | Text | Conditional | User | Required for governed changes | Stored for audit |

### Main Flow

1. Actor opens Walk-in History or the related workflow.
2. The system validates authentication, authorization, tenant scope, and current operating context.
3. The system loads the required Walk-in records, related configuration, and policy controls.
4. Actor enters or confirms the information required to view walk-in history and reports.
5. The system validates mandatory data, lifecycle status, ownership, eligibility, financial, capacity, schedule, and security rules where applicable.
6. The system executes View Walk-in History and Reports and persists the resulting Walk-in Visit state or transaction.
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

- Walk-in Visit record created, updated, validated, or reported according to the action.
- Lifecycle or processing status updated.
- Related history entry created.
- Business events emitted.
- Notifications generated where configured.
- Audit events recorded.
- Reports or dashboards updated where applicable.

### UI Behaviour

Walk-in History shall display scoped context, mandatory fields, lifecycle status, policy warnings, validation results, available actions, confirmation prompts, read-only states, pagination or filters where applicable, and responsive behavior for front-desk and administrative usage.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-WLK-007-001 | Actor must have permission to execute View Walk-in History and Reports. | Deny request and audit. | Critical |
| VAL-WLK-007-002 | Record must belong to the authorized Organization scope. | Deny request. | Critical |
| VAL-WLK-007-003 | Mandatory inputs must be complete and valid. | Block submission. | Critical |
| VAL-WLK-007-004 | Lifecycle and policy rules from BA-02 must be satisfied. | Reject or route for approval. | High |
| VAL-WLK-007-005 | Historical and audit records must be preserved. | Roll back or mark for recovery. | Critical |

### Business Rules

- BA-02 BR-ATT-005
- BA-02 BR-ATT-009
- BA-02 BR-ATT-010
- BA-02 BR-BIL-008
- BA-02 BR-SEC-004

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| wlk.view.walk.in.history.and.reports.view | Reception Staff | Read | View View Walk-in History and Reports context |
| wlk.view.walk.in.history.and.reports.execute | Reception Staff | Execute | Execute View Walk-in History and Reports |
| wlk.view.walk.in.history.and.reports.approve | Organization Administrator | Approve | Approve governed exceptions where configured |
| wlk.view.walk.in.history.and.reports.audit.view | Organization Administrator / Support Executive | Read | View audit trace |

### Security Considerations

The capability shall enforce authentication, role-based authorization, tenant isolation, Organization scope, Facility and Site access boundaries, sensitive data masking, secure references, and immutable audit logging.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| View Walk-in History and Reports Completed | Primary actor and configured stakeholders | In-App / Email | Action completes | Include reference, status, and effective date where applicable |
| View Walk-in History and Reports Requires Approval | Approver | In-App | Approval rule applies | Include safe summary and requested action |
| View Walk-in History and Reports Failed | Primary actor | In-App | Validation or processing fails | Include safe failure reason and next action |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| ViewWalkinHistoryAndReportsRequested | Walk-in Customer Management | Approval Workflow, Audit Service |
| ViewWalkinHistoryAndReportsCompleted | Walk-in Customer Management | Notification Service, Reporting Service, Audit Service |
| ViewWalkinHistoryAndReportsRejected | Walk-in Customer Management | Notification Service, Audit Service |

### Audit Events

| Audit Event | Description | Actor | Target Entity | Key Data |
|---|---|---|---|---|
| VIEW_WALKIN_HISTORY_AND_REPORTS_REQUESTED | View Walk-in History and Reports requested | Reception Staff | Walk-in Visit | Scope, reference, and reason |
| VIEW_WALKIN_HISTORY_AND_REPORTS_COMPLETED | View Walk-in History and Reports completed | Reception Staff / System | Walk-in Visit | Previous and new state |
| VIEW_WALKIN_HISTORY_AND_REPORTS_REJECTED | View Walk-in History and Reports rejected | System | Walk-in Visit | Rejection reason |

### Reports Generated

- Walk-in Customer Management Operational Report
- Walk-in Customer Management History Report
- Walk-in Customer Management Exception Report
- Executive Dashboard

### Related Screens

- Walk-in History
- Walk-in Customer Management Dashboard
- Walk-in Customer Management History
- Audit Log Viewer

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/walkins/history | GET | Authorized token | Execute View Walk-in History and Reports | 200 OK or 201 Created with result |
| /api/v1/walkins/history/history | GET | Authorized token | Retrieve View Walk-in History and Reports history | 200 OK with history |
| /api/v1/audit-logs | GET | Authorized token | Retrieve related audit events | 200 OK with scoped audit records |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Walk-in Visit | Read | Support View Walk-in History and Reports | Governed by Organization scope |
| Customer | Read / Insert | Support View Walk-in History and Reports | Governed by Organization scope |
| Attendance | Read / Insert | Support View Walk-in History and Reports | Governed by Organization scope |
| Invoice | Read / Insert | Support View Walk-in History and Reports | Governed by Organization scope |
| Payment | Read / Insert | Support View Walk-in History and Reports | Governed by Organization scope |
| Audit Log | Insert | Record auditable activity | Immutable |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Not Requested | View Walk-in History and Reports initiated | Generating | Reception Staff | Required data captured |
| Generating | Validation succeeds | Ready | System | BA-02 rules satisfied |
| Ready | Processing completes | Export Pending | System | Related updates succeed |
| Ready | Approval or policy failure | Failed | System / Approver | Request rejected |
| Export Pending | View history | Export Pending | Authorized user | Read-only historical access |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| WLK-007-001 | View Walk-in History and Reports cannot be completed because required information is missing. | Missing mandatory data | Complete required fields |
| WLK-007-002 | You do not have permission to perform this action. | Authorization failure | Request access |
| WLK-007-003 | The selected record is not eligible for this action. | Policy or lifecycle violation | Review record status |
| WLK-007-004 | View Walk-in History and Reports could not be completed due to a system or integration error. | Processing failure | Retry or contact support |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Execute View Walk-in History and Reports | Given the actor has required permission and valid scope | When the actor submits valid information | Then the system shall complete View Walk-in History and Reports successfully |
| Enforce validation | Given mandatory data or policy conditions are invalid | When the action is submitted | Then the system shall reject the request with a clear message |
| Preserve audit | Given the action completes or fails | When processing ends | Then audit events shall record actor, timestamp, scope, and outcome |
| Protect scope | Given the selected record is outside authorized scope | When the action is requested | Then the system shall deny access |

### Dependencies

- Customer Management
- Attendance Management
- Billing Management
- Payment Management
- Notification Management
- Audit Service

### Operational Considerations

View Walk-in History and Reports should be designed for high-volume operational use, retry-safe processing, clear exception handling, and support-team diagnostics without exposing sensitive data.

### Non-Functional Considerations

This requirement shall satisfy Digitize non-functional expectations for availability, reliability, performance, scalability, security, configurability, maintainability, and auditability.

### Assumptions

- Required master data and configuration are maintained by authorized users.
- Related services expose stable APIs for validation and synchronization.
- Organization policies define approval, retention, notification, and exception behavior.

### Success Criteria

View Walk-in History and Reports is completed accurately, securely, and audibly, with downstream records synchronized and no loss of historical traceability.

### Related Functional Requirements

- FR-WLK-001 - Identify or Register Walk-in Customer
- FR-WLK-002 - Validate Walk-in Eligibility
- FR-WLK-003 - Create Walk-in Visit
- FR-WLK-004 - Calculate Walk-in Charges
- FR-AUD-001 - Record Audit Events

### Notes

View Walk-in History and Reports shall remain aligned with the approved BA source documents and shall not introduce behavior that bypasses tenant isolation, lifecycle governance, financial controls, or auditability.

---

**End of FR-10 - Walk-in Customer Management**
