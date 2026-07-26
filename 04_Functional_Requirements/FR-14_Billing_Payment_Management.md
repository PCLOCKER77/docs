# FR-14 Billing & Payment Management

**Document ID:** FR-14  
**Document Name:** Billing & Payment Management Functional Requirements  
**Company:** OreeOn Technologies Pvt. Ltd.  
**Product:** Digitize  
**Document Type:** Functional Requirements  
**Version:** 1.0  
**Status:** Draft  
**Owner:** Product Management  
**Prepared By:** Product Management, Business Analysis, and Solution Architecture  
**Last Updated:** July 2026

---

## FR-BPM-001 - Generate Invoice

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-BPM-001 |
| Requirement Name | Generate Invoice |
| Functional Module | Billing & Payment Management |
| Business Domain | Billing & Payment |
| Business Capability | Invoice Management |
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
| Business Requirement | BA-08 BR-018 Billing and Invoice Generation |
| Business Rule | BA-02 BR-BIL-001, BR-BIL-002, BR-BIL-003, BR-BIL-004, BR-BIL-005, BR-BIL-008 |
| Business Process | BA-03 BP-BIL-001 Generate Invoice |
| Business Process Flow | BA-04 Section 24 Billing Management Flow, Section 25 Payment Management Flow, Section 26 Invoice Management Flow, Section 27 Refund Management Flow |
| Persona | BA-05 Finance Staff, Reception Staff, Customer, Organization Administrator |
| User Journey | BA-06 Section 19 Payment Journey |
| Stakeholder | BA-07 Finance Staff, Reception Staff, Customer |
| Non-Functional Requirement | BA-09 Section 3.7 Data Protection, Section 4.4 Financial Compliance, Section 11 Reporting Requirements |
| Assumption / Constraint / Risk | BA-10 BA-RSK-011, BA-RSK-012, BA-RSK-014 |

### Purpose

To enable Invoice Management within Billing & Payment Management so Digitize can execute Generate Invoice consistently across Organizations, Facilities, Sites, users, and related operational or commercial services.

### Functional Requirement

The system shall support Generate Invoice as an atomic Billing & Payment Management capability, including scoped data capture, business-rule validation, permission enforcement, lifecycle handling, related service synchronization, notification generation, reporting contribution, and immutable audit recording.

### Business Justification

Generate Invoice is required to preserve operational control, revenue accuracy, service continuity, customer trust, and enterprise traceability for Billing & Payment processes. Without this capability, downstream modules would rely on incomplete, manual, or inconsistent records.

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
- Actor has permission for Generate Invoice.
- Required Billing & Payment configuration and policies are available.
- Related records required by BA-03 BP-BIL-001 Generate Invoice are available and within authorized scope.

### Trigger

The capability is triggered when Reception Staff or the System initiates Generate Invoice from Invoice Management, a related workflow, a scheduled job, or an approved integration event.

### In Scope

- Capture or retrieve required Billing & Payment context.
- Validate Organization, Facility, Site, Customer, user, and policy scope where applicable.
- Execute Generate Invoice according to approved business rules.
- Persist the resulting Invoice state or transaction.
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
- Invoice reference
- Customer reference, where applicable
- Effective date and time, where applicable
- Status or action reason, where applicable
- Payment, billing, trainer, session, or subscription reference where applicable
- Actor remarks, where applicable

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Invoice ID | Primary business record reference | Identifier | Yes | System / User | Must exist or be generated within scope | Core reference for Generate Invoice |
| Organization ID | Tenant Organization context | Identifier | Yes | Session / System | Must be Active and authorized | Enforces tenant isolation |
| Facility ID | Facility context | Identifier | Conditional | User / System | Must be Active where applicable | Required for facility-level operations |
| Site ID | Site context | Identifier | Conditional | User / System | Must belong to Facility where applicable | Required for site-level operations |
| Status | Lifecycle or processing state | Enum | Yes | System | Must follow allowed state transitions | Drives UI and downstream access |
| Effective Date | Date when action applies | DateTime | Conditional | User / System | Must satisfy policy | Supports scheduled or immediate actions |
| Reason / Remarks | Business explanation | Text | Conditional | User | Required for governed changes | Stored for audit |

### Main Flow

1. Actor opens Invoice Management or the related workflow.
2. The system validates authentication, authorization, tenant scope, and current operating context.
3. The system loads the required Billing & Payment records, related configuration, and policy controls.
4. Actor enters or confirms the information required to generate invoice.
5. The system validates mandatory data, lifecycle status, ownership, eligibility, financial, capacity, schedule, and security rules where applicable.
6. The system executes Generate Invoice and persists the resulting Invoice state or transaction.
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

- Invoice record created, updated, validated, or reported according to the action.
- Lifecycle or processing status updated.
- Related history entry created.
- Business events emitted.
- Notifications generated where configured.
- Audit events recorded.
- Reports or dashboards updated where applicable.

### UI Behaviour

Invoice Management shall display scoped context, mandatory fields, lifecycle status, policy warnings, validation results, available actions, confirmation prompts, read-only states, pagination or filters where applicable, and responsive behavior for front-desk and administrative usage.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-BPM-001-001 | Actor must have permission to execute Generate Invoice. | Deny request and audit. | Critical |
| VAL-BPM-001-002 | Record must belong to the authorized Organization scope. | Deny request. | Critical |
| VAL-BPM-001-003 | Mandatory inputs must be complete and valid. | Block submission. | Critical |
| VAL-BPM-001-004 | Lifecycle and policy rules from BA-02 must be satisfied. | Reject or route for approval. | High |
| VAL-BPM-001-005 | Historical and audit records must be preserved. | Roll back or mark for recovery. | Critical |

### Business Rules

- BA-02 BR-BIL-001
- BA-02 BR-BIL-002
- BA-02 BR-BIL-003
- BA-02 BR-BIL-004
- BA-02 BR-BIL-005
- BA-02 BR-BIL-008

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| bpm.generate.invoice.view | Reception Staff | Read | View Generate Invoice context |
| bpm.generate.invoice.execute | Reception Staff | Execute | Execute Generate Invoice |
| bpm.generate.invoice.approve | Organization Administrator | Approve | Approve governed exceptions where configured |
| bpm.generate.invoice.audit.view | Organization Administrator / Support Executive | Read | View audit trace |

### Security Considerations

The capability shall enforce authentication, role-based authorization, tenant isolation, Organization scope, Facility and Site access boundaries, sensitive data masking, secure references, and immutable audit logging.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Generate Invoice Completed | Primary actor and configured stakeholders | In-App / Email | Action completes | Include reference, status, and effective date where applicable |
| Generate Invoice Requires Approval | Approver | In-App | Approval rule applies | Include safe summary and requested action |
| Generate Invoice Failed | Primary actor | In-App | Validation or processing fails | Include safe failure reason and next action |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| GenerateInvoiceRequested | Billing & Payment Management | Approval Workflow, Audit Service |
| GenerateInvoiceCompleted | Billing & Payment Management | Notification Service, Reporting Service, Audit Service |
| GenerateInvoiceRejected | Billing & Payment Management | Notification Service, Audit Service |

### Audit Events

| Audit Event | Description | Actor | Target Entity | Key Data |
|---|---|---|---|---|
| GENERATE_INVOICE_REQUESTED | Generate Invoice requested | Reception Staff | Invoice | Scope, reference, and reason |
| GENERATE_INVOICE_COMPLETED | Generate Invoice completed | Reception Staff / System | Invoice | Previous and new state |
| GENERATE_INVOICE_REJECTED | Generate Invoice rejected | System | Invoice | Rejection reason |

### Reports Generated

- Billing & Payment Management Operational Report
- Billing & Payment Management History Report
- Billing & Payment Management Exception Report
- Executive Dashboard

### Related Screens

- Invoice Management
- Billing & Payment Management Dashboard
- Billing & Payment Management History
- Audit Log Viewer

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/invoices | POST | Authorized token | Execute Generate Invoice | 200 OK or 201 Created with result |
| /api/v1/invoices/history | GET | Authorized token | Retrieve Generate Invoice history | 200 OK with history |
| /api/v1/audit-logs | GET | Authorized token | Retrieve related audit events | 200 OK with scoped audit records |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Invoice | Create / Update / Read | Support Generate Invoice | Governed by Organization scope |
| Invoice Item | Read / Insert | Support Generate Invoice | Governed by Organization scope |
| Charge | Read / Insert | Support Generate Invoice | Governed by Organization scope |
| Discount | Read / Insert | Support Generate Invoice | Governed by Organization scope |
| Tax | Read / Insert | Support Generate Invoice | Governed by Organization scope |
| Audit Log | Insert | Record auditable activity | Immutable |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Draft | Generate Invoice initiated | Validated | Reception Staff | Required data captured |
| Validated | Validation succeeds | Pending Approval | System | BA-02 rules satisfied |
| Pending Approval | Processing completes | Completed | System | Related updates succeed |
| Pending Approval | Approval or policy failure | Rejected | System / Approver | Request rejected |
| Completed | View history | Completed | Authorized user | Read-only historical access |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| BPM-001-001 | Generate Invoice cannot be completed because required information is missing. | Missing mandatory data | Complete required fields |
| BPM-001-002 | You do not have permission to perform this action. | Authorization failure | Request access |
| BPM-001-003 | The selected record is not eligible for this action. | Policy or lifecycle violation | Review record status |
| BPM-001-004 | Generate Invoice could not be completed due to a system or integration error. | Processing failure | Retry or contact support |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Execute Generate Invoice | Given the actor has required permission and valid scope | When the actor submits valid information | Then the system shall complete Generate Invoice successfully |
| Enforce validation | Given mandatory data or policy conditions are invalid | When the action is submitted | Then the system shall reject the request with a clear message |
| Preserve audit | Given the action completes or fails | When processing ends | Then audit events shall record actor, timestamp, scope, and outcome |
| Protect scope | Given the selected record is outside authorized scope | When the action is requested | Then the system shall deny access |

### Dependencies

- Customer Management
- Membership Management
- Walk-in Customer Management
- Personal Training
- Notification Management
- Reporting Service
- Audit Service

### Operational Considerations

Generate Invoice should be designed for high-volume operational use, retry-safe processing, clear exception handling, and support-team diagnostics without exposing sensitive data.

### Non-Functional Considerations

This requirement shall satisfy Digitize non-functional expectations for availability, reliability, performance, scalability, security, configurability, maintainability, and auditability.

### Assumptions

- Required master data and configuration are maintained by authorized users.
- Related services expose stable APIs for validation and synchronization.
- Organization policies define approval, retention, notification, and exception behavior.

### Success Criteria

Generate Invoice is completed accurately, securely, and audibly, with downstream records synchronized and no loss of historical traceability.

### Related Functional Requirements

- FR-BPM-002 - Calculate Service Charges
- FR-BPM-003 - Apply Discounts
- FR-BPM-004 - Calculate Taxes
- FR-BPM-005 - Apply Billing Adjustments
- FR-AUD-001 - Record Audit Events

### Notes

Generate Invoice shall remain aligned with the approved BA source documents and shall not introduce behavior that bypasses tenant isolation, lifecycle governance, financial controls, or auditability.

---

## FR-BPM-002 - Calculate Service Charges

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-BPM-002 |
| Requirement Name | Calculate Service Charges |
| Functional Module | Billing & Payment Management |
| Business Domain | Billing & Payment |
| Business Capability | Charge Calculation |
| Requirement Type | Functional |
| Requirement Category | Validation |
| Requirement Version | 1.0 |
| Requirement Status | Approved |
| Priority | Critical |
| Complexity | High |
| Release Version | 1.0 |
| Owner | Product Management |

### Traceability References

| Traceability Type | Reference |
|---|---|
| Business Requirement | BA-08 BR-018 Billing and Invoice Generation |
| Business Rule | BA-02 BR-BIL-001, BR-BIL-004, BR-BIL-008 |
| Business Process | BA-03 BP-BIL-002, BP-BIL-003, BP-BIL-004 |
| Business Process Flow | BA-04 Section 24 Billing Management Flow, Section 25 Payment Management Flow, Section 26 Invoice Management Flow, Section 27 Refund Management Flow |
| Persona | BA-05 Finance Staff, Reception Staff, Customer, Organization Administrator |
| User Journey | BA-06 Section 19 Payment Journey |
| Stakeholder | BA-07 Finance Staff, Reception Staff, Customer |
| Non-Functional Requirement | BA-09 Section 3.7 Data Protection, Section 4.4 Financial Compliance, Section 11 Reporting Requirements |
| Assumption / Constraint / Risk | BA-10 BA-RSK-011, BA-RSK-012, BA-RSK-014 |

### Purpose

To enable Charge Calculation within Billing & Payment Management so Digitize can execute Calculate Service Charges consistently across Organizations, Facilities, Sites, users, and related operational or commercial services.

### Functional Requirement

The system shall support Calculate Service Charges as an atomic Billing & Payment Management capability, including scoped data capture, business-rule validation, permission enforcement, lifecycle handling, related service synchronization, notification generation, reporting contribution, and immutable audit recording.

### Business Justification

Calculate Service Charges is required to preserve operational control, revenue accuracy, service continuity, customer trust, and enterprise traceability for Billing & Payment processes. Without this capability, downstream modules would rely on incomplete, manual, or inconsistent records.

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
- Actor has permission for Calculate Service Charges.
- Required Billing & Payment configuration and policies are available.
- Related records required by BA-03 BP-BIL-002, BP-BIL-003, BP-BIL-004 are available and within authorized scope.

### Trigger

The capability is triggered when System or the System initiates Calculate Service Charges from Charge Calculation, a related workflow, a scheduled job, or an approved integration event.

### In Scope

- Capture or retrieve required Billing & Payment context.
- Validate Organization, Facility, Site, Customer, user, and policy scope where applicable.
- Execute Calculate Service Charges according to approved business rules.
- Persist the resulting Invoice state or transaction.
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
- Invoice reference
- Customer reference, where applicable
- Effective date and time, where applicable
- Status or action reason, where applicable
- Payment, billing, trainer, session, or subscription reference where applicable
- Actor remarks, where applicable

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Invoice ID | Primary business record reference | Identifier | Yes | System / User | Must exist or be generated within scope | Core reference for Calculate Service Charges |
| Organization ID | Tenant Organization context | Identifier | Yes | Session / System | Must be Active and authorized | Enforces tenant isolation |
| Facility ID | Facility context | Identifier | Conditional | User / System | Must be Active where applicable | Required for facility-level operations |
| Site ID | Site context | Identifier | Conditional | User / System | Must belong to Facility where applicable | Required for site-level operations |
| Status | Lifecycle or processing state | Enum | Yes | System | Must follow allowed state transitions | Drives UI and downstream access |
| Effective Date | Date when action applies | DateTime | Conditional | User / System | Must satisfy policy | Supports scheduled or immediate actions |
| Reason / Remarks | Business explanation | Text | Conditional | User | Required for governed changes | Stored for audit |

### Main Flow

1. Actor opens Charge Calculation or the related workflow.
2. The system validates authentication, authorization, tenant scope, and current operating context.
3. The system loads the required Billing & Payment records, related configuration, and policy controls.
4. Actor enters or confirms the information required to calculate service charges.
5. The system validates mandatory data, lifecycle status, ownership, eligibility, financial, capacity, schedule, and security rules where applicable.
6. The system executes Calculate Service Charges and persists the resulting Invoice state or transaction.
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

- Invoice record created, updated, validated, or reported according to the action.
- Lifecycle or processing status updated.
- Related history entry created.
- Business events emitted.
- Notifications generated where configured.
- Audit events recorded.
- Reports or dashboards updated where applicable.

### UI Behaviour

Charge Calculation shall display scoped context, mandatory fields, lifecycle status, policy warnings, validation results, available actions, confirmation prompts, read-only states, pagination or filters where applicable, and responsive behavior for front-desk and administrative usage.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-BPM-002-001 | Actor must have permission to execute Calculate Service Charges. | Deny request and audit. | Critical |
| VAL-BPM-002-002 | Record must belong to the authorized Organization scope. | Deny request. | Critical |
| VAL-BPM-002-003 | Mandatory inputs must be complete and valid. | Block submission. | Critical |
| VAL-BPM-002-004 | Lifecycle and policy rules from BA-02 must be satisfied. | Reject or route for approval. | High |
| VAL-BPM-002-005 | Historical and audit records must be preserved. | Roll back or mark for recovery. | Critical |

### Business Rules

- BA-02 BR-BIL-001
- BA-02 BR-BIL-004
- BA-02 BR-BIL-008

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| bpm.calculate.service.charges.view | System | Read | View Calculate Service Charges context |
| bpm.calculate.service.charges.execute | System | Execute | Execute Calculate Service Charges |
| bpm.calculate.service.charges.approve | Organization Administrator | Approve | Approve governed exceptions where configured |
| bpm.calculate.service.charges.audit.view | Organization Administrator / Support Executive | Read | View audit trace |

### Security Considerations

The capability shall enforce authentication, role-based authorization, tenant isolation, Organization scope, Facility and Site access boundaries, sensitive data masking, secure references, and immutable audit logging.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Calculate Service Charges Completed | Primary actor and configured stakeholders | In-App / Email | Action completes | Include reference, status, and effective date where applicable |
| Calculate Service Charges Requires Approval | Approver | In-App | Approval rule applies | Include safe summary and requested action |
| Calculate Service Charges Failed | Primary actor | In-App | Validation or processing fails | Include safe failure reason and next action |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| CalculateServiceChargesRequested | Billing & Payment Management | Approval Workflow, Audit Service |
| CalculateServiceChargesCompleted | Billing & Payment Management | Notification Service, Reporting Service, Audit Service |
| CalculateServiceChargesRejected | Billing & Payment Management | Notification Service, Audit Service |

### Audit Events

| Audit Event | Description | Actor | Target Entity | Key Data |
|---|---|---|---|---|
| CALCULATE_SERVICE_CHARGES_REQUESTED | Calculate Service Charges requested | System | Invoice | Scope, reference, and reason |
| CALCULATE_SERVICE_CHARGES_COMPLETED | Calculate Service Charges completed | System / System | Invoice | Previous and new state |
| CALCULATE_SERVICE_CHARGES_REJECTED | Calculate Service Charges rejected | System | Invoice | Rejection reason |

### Reports Generated

- Billing & Payment Management Operational Report
- Billing & Payment Management History Report
- Billing & Payment Management Exception Report
- Executive Dashboard

### Related Screens

- Charge Calculation
- Billing & Payment Management Dashboard
- Billing & Payment Management History
- Audit Log Viewer

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/billing/charges | POST | Authorized token | Execute Calculate Service Charges | 200 OK or 201 Created with result |
| /api/v1/billing/charges/history | GET | Authorized token | Retrieve Calculate Service Charges history | 200 OK with history |
| /api/v1/audit-logs | GET | Authorized token | Retrieve related audit events | 200 OK with scoped audit records |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Invoice | Create / Update / Read | Support Calculate Service Charges | Governed by Organization scope |
| Invoice Item | Read / Insert | Support Calculate Service Charges | Governed by Organization scope |
| Charge | Read / Insert | Support Calculate Service Charges | Governed by Organization scope |
| Discount | Read / Insert | Support Calculate Service Charges | Governed by Organization scope |
| Tax | Read / Insert | Support Calculate Service Charges | Governed by Organization scope |
| Audit Log | Insert | Record auditable activity | Immutable |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Requested | Calculate Service Charges initiated | Eligible | System | Required data captured |
| Eligible | Validation succeeds | Requires Override | System | BA-02 rules satisfied |
| Requires Override | Processing completes | Denied | System | Related updates succeed |
| Requires Override | Approval or policy failure | Failed | System / Approver | Request rejected |
| Denied | View history | Denied | Authorized user | Read-only historical access |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| BPM-002-001 | Calculate Service Charges cannot be completed because required information is missing. | Missing mandatory data | Complete required fields |
| BPM-002-002 | You do not have permission to perform this action. | Authorization failure | Request access |
| BPM-002-003 | The selected record is not eligible for this action. | Policy or lifecycle violation | Review record status |
| BPM-002-004 | Calculate Service Charges could not be completed due to a system or integration error. | Processing failure | Retry or contact support |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Execute Calculate Service Charges | Given the actor has required permission and valid scope | When the actor submits valid information | Then the system shall complete Calculate Service Charges successfully |
| Enforce validation | Given mandatory data or policy conditions are invalid | When the action is submitted | Then the system shall reject the request with a clear message |
| Preserve audit | Given the action completes or fails | When processing ends | Then audit events shall record actor, timestamp, scope, and outcome |
| Protect scope | Given the selected record is outside authorized scope | When the action is requested | Then the system shall deny access |

### Dependencies

- Customer Management
- Membership Management
- Walk-in Customer Management
- Personal Training
- Notification Management
- Reporting Service
- Audit Service

### Operational Considerations

Calculate Service Charges should be designed for high-volume operational use, retry-safe processing, clear exception handling, and support-team diagnostics without exposing sensitive data.

### Non-Functional Considerations

This requirement shall satisfy Digitize non-functional expectations for availability, reliability, performance, scalability, security, configurability, maintainability, and auditability.

### Assumptions

- Required master data and configuration are maintained by authorized users.
- Related services expose stable APIs for validation and synchronization.
- Organization policies define approval, retention, notification, and exception behavior.

### Success Criteria

Calculate Service Charges is completed accurately, securely, and audibly, with downstream records synchronized and no loss of historical traceability.

### Related Functional Requirements

- FR-BPM-001 - Generate Invoice
- FR-BPM-003 - Apply Discounts
- FR-BPM-004 - Calculate Taxes
- FR-BPM-005 - Apply Billing Adjustments
- FR-AUD-001 - Record Audit Events

### Notes

Calculate Service Charges shall remain aligned with the approved BA source documents and shall not introduce behavior that bypasses tenant isolation, lifecycle governance, financial controls, or auditability.

---

## FR-BPM-003 - Apply Discounts

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-BPM-003 |
| Requirement Name | Apply Discounts |
| Functional Module | Billing & Payment Management |
| Business Domain | Billing & Payment |
| Business Capability | Discount Management |
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
| Business Requirement | BA-08 BR-018 Billing and Invoice Generation |
| Business Rule | BA-02 BR-BIL-001, BR-BIL-007, BR-BIL-008 |
| Business Process | BA-03 BP-BIL-005 Apply Discounts |
| Business Process Flow | BA-04 Section 24 Billing Management Flow, Section 25 Payment Management Flow, Section 26 Invoice Management Flow, Section 27 Refund Management Flow |
| Persona | BA-05 Finance Staff, Reception Staff, Customer, Organization Administrator |
| User Journey | BA-06 Section 19 Payment Journey |
| Stakeholder | BA-07 Finance Staff, Reception Staff, Customer |
| Non-Functional Requirement | BA-09 Section 3.7 Data Protection, Section 4.4 Financial Compliance, Section 11 Reporting Requirements |
| Assumption / Constraint / Risk | BA-10 BA-RSK-011, BA-RSK-012, BA-RSK-014 |

### Purpose

To enable Discount Management within Billing & Payment Management so Digitize can execute Apply Discounts consistently across Organizations, Facilities, Sites, users, and related operational or commercial services.

### Functional Requirement

The system shall support Apply Discounts as an atomic Billing & Payment Management capability, including scoped data capture, business-rule validation, permission enforcement, lifecycle handling, related service synchronization, notification generation, reporting contribution, and immutable audit recording.

### Business Justification

Apply Discounts is required to preserve operational control, revenue accuracy, service continuity, customer trust, and enterprise traceability for Billing & Payment processes. Without this capability, downstream modules would rely on incomplete, manual, or inconsistent records.

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
- Actor has permission for Apply Discounts.
- Required Billing & Payment configuration and policies are available.
- Related records required by BA-03 BP-BIL-005 Apply Discounts are available and within authorized scope.

### Trigger

The capability is triggered when Reception Staff or the System initiates Apply Discounts from Discount Management, a related workflow, a scheduled job, or an approved integration event.

### In Scope

- Capture or retrieve required Billing & Payment context.
- Validate Organization, Facility, Site, Customer, user, and policy scope where applicable.
- Execute Apply Discounts according to approved business rules.
- Persist the resulting Invoice state or transaction.
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
- Invoice reference
- Customer reference, where applicable
- Effective date and time, where applicable
- Status or action reason, where applicable
- Payment, billing, trainer, session, or subscription reference where applicable
- Actor remarks, where applicable

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Invoice ID | Primary business record reference | Identifier | Yes | System / User | Must exist or be generated within scope | Core reference for Apply Discounts |
| Organization ID | Tenant Organization context | Identifier | Yes | Session / System | Must be Active and authorized | Enforces tenant isolation |
| Facility ID | Facility context | Identifier | Conditional | User / System | Must be Active where applicable | Required for facility-level operations |
| Site ID | Site context | Identifier | Conditional | User / System | Must belong to Facility where applicable | Required for site-level operations |
| Status | Lifecycle or processing state | Enum | Yes | System | Must follow allowed state transitions | Drives UI and downstream access |
| Effective Date | Date when action applies | DateTime | Conditional | User / System | Must satisfy policy | Supports scheduled or immediate actions |
| Reason / Remarks | Business explanation | Text | Conditional | User | Required for governed changes | Stored for audit |

### Main Flow

1. Actor opens Discount Management or the related workflow.
2. The system validates authentication, authorization, tenant scope, and current operating context.
3. The system loads the required Billing & Payment records, related configuration, and policy controls.
4. Actor enters or confirms the information required to apply discounts.
5. The system validates mandatory data, lifecycle status, ownership, eligibility, financial, capacity, schedule, and security rules where applicable.
6. The system executes Apply Discounts and persists the resulting Invoice state or transaction.
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

- Invoice record created, updated, validated, or reported according to the action.
- Lifecycle or processing status updated.
- Related history entry created.
- Business events emitted.
- Notifications generated where configured.
- Audit events recorded.
- Reports or dashboards updated where applicable.

### UI Behaviour

Discount Management shall display scoped context, mandatory fields, lifecycle status, policy warnings, validation results, available actions, confirmation prompts, read-only states, pagination or filters where applicable, and responsive behavior for front-desk and administrative usage.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-BPM-003-001 | Actor must have permission to execute Apply Discounts. | Deny request and audit. | Critical |
| VAL-BPM-003-002 | Record must belong to the authorized Organization scope. | Deny request. | Critical |
| VAL-BPM-003-003 | Mandatory inputs must be complete and valid. | Block submission. | Critical |
| VAL-BPM-003-004 | Lifecycle and policy rules from BA-02 must be satisfied. | Reject or route for approval. | High |
| VAL-BPM-003-005 | Historical and audit records must be preserved. | Roll back or mark for recovery. | Critical |

### Business Rules

- BA-02 BR-BIL-001
- BA-02 BR-BIL-007
- BA-02 BR-BIL-008

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| bpm.apply.discounts.view | Reception Staff | Read | View Apply Discounts context |
| bpm.apply.discounts.execute | Reception Staff | Execute | Execute Apply Discounts |
| bpm.apply.discounts.approve | Organization Administrator | Approve | Approve governed exceptions where configured |
| bpm.apply.discounts.audit.view | Organization Administrator / Support Executive | Read | View audit trace |

### Security Considerations

The capability shall enforce authentication, role-based authorization, tenant isolation, Organization scope, Facility and Site access boundaries, sensitive data masking, secure references, and immutable audit logging.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Apply Discounts Completed | Primary actor and configured stakeholders | In-App / Email | Action completes | Include reference, status, and effective date where applicable |
| Apply Discounts Requires Approval | Approver | In-App | Approval rule applies | Include safe summary and requested action |
| Apply Discounts Failed | Primary actor | In-App | Validation or processing fails | Include safe failure reason and next action |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| ApplyDiscountsRequested | Billing & Payment Management | Approval Workflow, Audit Service |
| ApplyDiscountsCompleted | Billing & Payment Management | Notification Service, Reporting Service, Audit Service |
| ApplyDiscountsRejected | Billing & Payment Management | Notification Service, Audit Service |

### Audit Events

| Audit Event | Description | Actor | Target Entity | Key Data |
|---|---|---|---|---|
| APPLY_DISCOUNTS_REQUESTED | Apply Discounts requested | Reception Staff | Invoice | Scope, reference, and reason |
| APPLY_DISCOUNTS_COMPLETED | Apply Discounts completed | Reception Staff / System | Invoice | Previous and new state |
| APPLY_DISCOUNTS_REJECTED | Apply Discounts rejected | System | Invoice | Rejection reason |

### Reports Generated

- Billing & Payment Management Operational Report
- Billing & Payment Management History Report
- Billing & Payment Management Exception Report
- Executive Dashboard

### Related Screens

- Discount Management
- Billing & Payment Management Dashboard
- Billing & Payment Management History
- Audit Log Viewer

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/invoices/{invoiceId}/discounts | POST | Authorized token | Execute Apply Discounts | 200 OK or 201 Created with result |
| /api/v1/invoices/{invoiceId}/discounts/history | GET | Authorized token | Retrieve Apply Discounts history | 200 OK with history |
| /api/v1/audit-logs | GET | Authorized token | Retrieve related audit events | 200 OK with scoped audit records |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Invoice | Create / Update / Read | Support Apply Discounts | Governed by Organization scope |
| Invoice Item | Read / Insert | Support Apply Discounts | Governed by Organization scope |
| Charge | Read / Insert | Support Apply Discounts | Governed by Organization scope |
| Discount | Read / Insert | Support Apply Discounts | Governed by Organization scope |
| Tax | Read / Insert | Support Apply Discounts | Governed by Organization scope |
| Audit Log | Insert | Record auditable activity | Immutable |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Draft | Apply Discounts initiated | Validated | Reception Staff | Required data captured |
| Validated | Validation succeeds | Pending Approval | System | BA-02 rules satisfied |
| Pending Approval | Processing completes | Completed | System | Related updates succeed |
| Pending Approval | Approval or policy failure | Rejected | System / Approver | Request rejected |
| Completed | View history | Completed | Authorized user | Read-only historical access |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| BPM-003-001 | Apply Discounts cannot be completed because required information is missing. | Missing mandatory data | Complete required fields |
| BPM-003-002 | You do not have permission to perform this action. | Authorization failure | Request access |
| BPM-003-003 | The selected record is not eligible for this action. | Policy or lifecycle violation | Review record status |
| BPM-003-004 | Apply Discounts could not be completed due to a system or integration error. | Processing failure | Retry or contact support |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Execute Apply Discounts | Given the actor has required permission and valid scope | When the actor submits valid information | Then the system shall complete Apply Discounts successfully |
| Enforce validation | Given mandatory data or policy conditions are invalid | When the action is submitted | Then the system shall reject the request with a clear message |
| Preserve audit | Given the action completes or fails | When processing ends | Then audit events shall record actor, timestamp, scope, and outcome |
| Protect scope | Given the selected record is outside authorized scope | When the action is requested | Then the system shall deny access |

### Dependencies

- Customer Management
- Membership Management
- Walk-in Customer Management
- Personal Training
- Notification Management
- Reporting Service
- Audit Service

### Operational Considerations

Apply Discounts should be designed for high-volume operational use, retry-safe processing, clear exception handling, and support-team diagnostics without exposing sensitive data.

### Non-Functional Considerations

This requirement shall satisfy Digitize non-functional expectations for availability, reliability, performance, scalability, security, configurability, maintainability, and auditability.

### Assumptions

- Required master data and configuration are maintained by authorized users.
- Related services expose stable APIs for validation and synchronization.
- Organization policies define approval, retention, notification, and exception behavior.

### Success Criteria

Apply Discounts is completed accurately, securely, and audibly, with downstream records synchronized and no loss of historical traceability.

### Related Functional Requirements

- FR-BPM-001 - Generate Invoice
- FR-BPM-002 - Calculate Service Charges
- FR-BPM-004 - Calculate Taxes
- FR-BPM-005 - Apply Billing Adjustments
- FR-AUD-001 - Record Audit Events

### Notes

Apply Discounts shall remain aligned with the approved BA source documents and shall not introduce behavior that bypasses tenant isolation, lifecycle governance, financial controls, or auditability.

---

## FR-BPM-004 - Calculate Taxes

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-BPM-004 |
| Requirement Name | Calculate Taxes |
| Functional Module | Billing & Payment Management |
| Business Domain | Billing & Payment |
| Business Capability | Tax Management |
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
| Business Requirement | BA-08 BR-018 Billing and Invoice Generation |
| Business Rule | BA-02 BR-BIL-004, BR-BIL-008 |
| Business Process | BA-03 BP-BIL-006 Calculate Taxes |
| Business Process Flow | BA-04 Section 24 Billing Management Flow, Section 25 Payment Management Flow, Section 26 Invoice Management Flow, Section 27 Refund Management Flow |
| Persona | BA-05 Finance Staff, Reception Staff, Customer, Organization Administrator |
| User Journey | BA-06 Section 19 Payment Journey |
| Stakeholder | BA-07 Finance Staff, Reception Staff, Customer |
| Non-Functional Requirement | BA-09 Section 3.7 Data Protection, Section 4.4 Financial Compliance, Section 11 Reporting Requirements |
| Assumption / Constraint / Risk | BA-10 BA-RSK-011, BA-RSK-012, BA-RSK-014 |

### Purpose

To enable Tax Management within Billing & Payment Management so Digitize can execute Calculate Taxes consistently across Organizations, Facilities, Sites, users, and related operational or commercial services.

### Functional Requirement

The system shall support Calculate Taxes as an atomic Billing & Payment Management capability, including scoped data capture, business-rule validation, permission enforcement, lifecycle handling, related service synchronization, notification generation, reporting contribution, and immutable audit recording.

### Business Justification

Calculate Taxes is required to preserve operational control, revenue accuracy, service continuity, customer trust, and enterprise traceability for Billing & Payment processes. Without this capability, downstream modules would rely on incomplete, manual, or inconsistent records.

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
- Actor has permission for Calculate Taxes.
- Required Billing & Payment configuration and policies are available.
- Related records required by BA-03 BP-BIL-006 Calculate Taxes are available and within authorized scope.

### Trigger

The capability is triggered when System or the System initiates Calculate Taxes from Tax Calculation, a related workflow, a scheduled job, or an approved integration event.

### In Scope

- Capture or retrieve required Billing & Payment context.
- Validate Organization, Facility, Site, Customer, user, and policy scope where applicable.
- Execute Calculate Taxes according to approved business rules.
- Persist the resulting Invoice state or transaction.
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
- Invoice reference
- Customer reference, where applicable
- Effective date and time, where applicable
- Status or action reason, where applicable
- Payment, billing, trainer, session, or subscription reference where applicable
- Actor remarks, where applicable

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Invoice ID | Primary business record reference | Identifier | Yes | System / User | Must exist or be generated within scope | Core reference for Calculate Taxes |
| Organization ID | Tenant Organization context | Identifier | Yes | Session / System | Must be Active and authorized | Enforces tenant isolation |
| Facility ID | Facility context | Identifier | Conditional | User / System | Must be Active where applicable | Required for facility-level operations |
| Site ID | Site context | Identifier | Conditional | User / System | Must belong to Facility where applicable | Required for site-level operations |
| Status | Lifecycle or processing state | Enum | Yes | System | Must follow allowed state transitions | Drives UI and downstream access |
| Effective Date | Date when action applies | DateTime | Conditional | User / System | Must satisfy policy | Supports scheduled or immediate actions |
| Reason / Remarks | Business explanation | Text | Conditional | User | Required for governed changes | Stored for audit |

### Main Flow

1. Actor opens Tax Calculation or the related workflow.
2. The system validates authentication, authorization, tenant scope, and current operating context.
3. The system loads the required Billing & Payment records, related configuration, and policy controls.
4. Actor enters or confirms the information required to calculate taxes.
5. The system validates mandatory data, lifecycle status, ownership, eligibility, financial, capacity, schedule, and security rules where applicable.
6. The system executes Calculate Taxes and persists the resulting Invoice state or transaction.
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

- Invoice record created, updated, validated, or reported according to the action.
- Lifecycle or processing status updated.
- Related history entry created.
- Business events emitted.
- Notifications generated where configured.
- Audit events recorded.
- Reports or dashboards updated where applicable.

### UI Behaviour

Tax Calculation shall display scoped context, mandatory fields, lifecycle status, policy warnings, validation results, available actions, confirmation prompts, read-only states, pagination or filters where applicable, and responsive behavior for front-desk and administrative usage.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-BPM-004-001 | Actor must have permission to execute Calculate Taxes. | Deny request and audit. | Critical |
| VAL-BPM-004-002 | Record must belong to the authorized Organization scope. | Deny request. | Critical |
| VAL-BPM-004-003 | Mandatory inputs must be complete and valid. | Block submission. | Critical |
| VAL-BPM-004-004 | Lifecycle and policy rules from BA-02 must be satisfied. | Reject or route for approval. | High |
| VAL-BPM-004-005 | Historical and audit records must be preserved. | Roll back or mark for recovery. | Critical |

### Business Rules

- BA-02 BR-BIL-004
- BA-02 BR-BIL-008

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| bpm.calculate.taxes.view | System | Read | View Calculate Taxes context |
| bpm.calculate.taxes.execute | System | Execute | Execute Calculate Taxes |
| bpm.calculate.taxes.approve | Organization Administrator | Approve | Approve governed exceptions where configured |
| bpm.calculate.taxes.audit.view | Organization Administrator / Support Executive | Read | View audit trace |

### Security Considerations

The capability shall enforce authentication, role-based authorization, tenant isolation, Organization scope, Facility and Site access boundaries, sensitive data masking, secure references, and immutable audit logging.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Calculate Taxes Completed | Primary actor and configured stakeholders | In-App / Email | Action completes | Include reference, status, and effective date where applicable |
| Calculate Taxes Requires Approval | Approver | In-App | Approval rule applies | Include safe summary and requested action |
| Calculate Taxes Failed | Primary actor | In-App | Validation or processing fails | Include safe failure reason and next action |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| CalculateTaxesRequested | Billing & Payment Management | Approval Workflow, Audit Service |
| CalculateTaxesCompleted | Billing & Payment Management | Notification Service, Reporting Service, Audit Service |
| CalculateTaxesRejected | Billing & Payment Management | Notification Service, Audit Service |

### Audit Events

| Audit Event | Description | Actor | Target Entity | Key Data |
|---|---|---|---|---|
| CALCULATE_TAXES_REQUESTED | Calculate Taxes requested | System | Invoice | Scope, reference, and reason |
| CALCULATE_TAXES_COMPLETED | Calculate Taxes completed | System / System | Invoice | Previous and new state |
| CALCULATE_TAXES_REJECTED | Calculate Taxes rejected | System | Invoice | Rejection reason |

### Reports Generated

- Billing & Payment Management Operational Report
- Billing & Payment Management History Report
- Billing & Payment Management Exception Report
- Executive Dashboard

### Related Screens

- Tax Calculation
- Billing & Payment Management Dashboard
- Billing & Payment Management History
- Audit Log Viewer

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/billing/taxes/calculate | POST | Authorized token | Execute Calculate Taxes | 200 OK or 201 Created with result |
| /api/v1/billing/taxes/calculate/history | GET | Authorized token | Retrieve Calculate Taxes history | 200 OK with history |
| /api/v1/audit-logs | GET | Authorized token | Retrieve related audit events | 200 OK with scoped audit records |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Invoice | Create / Update / Read | Support Calculate Taxes | Governed by Organization scope |
| Invoice Item | Read / Insert | Support Calculate Taxes | Governed by Organization scope |
| Charge | Read / Insert | Support Calculate Taxes | Governed by Organization scope |
| Discount | Read / Insert | Support Calculate Taxes | Governed by Organization scope |
| Tax | Read / Insert | Support Calculate Taxes | Governed by Organization scope |
| Audit Log | Insert | Record auditable activity | Immutable |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Requested | Calculate Taxes initiated | Eligible | System | Required data captured |
| Eligible | Validation succeeds | Requires Override | System | BA-02 rules satisfied |
| Requires Override | Processing completes | Denied | System | Related updates succeed |
| Requires Override | Approval or policy failure | Failed | System / Approver | Request rejected |
| Denied | View history | Denied | Authorized user | Read-only historical access |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| BPM-004-001 | Calculate Taxes cannot be completed because required information is missing. | Missing mandatory data | Complete required fields |
| BPM-004-002 | You do not have permission to perform this action. | Authorization failure | Request access |
| BPM-004-003 | The selected record is not eligible for this action. | Policy or lifecycle violation | Review record status |
| BPM-004-004 | Calculate Taxes could not be completed due to a system or integration error. | Processing failure | Retry or contact support |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Execute Calculate Taxes | Given the actor has required permission and valid scope | When the actor submits valid information | Then the system shall complete Calculate Taxes successfully |
| Enforce validation | Given mandatory data or policy conditions are invalid | When the action is submitted | Then the system shall reject the request with a clear message |
| Preserve audit | Given the action completes or fails | When processing ends | Then audit events shall record actor, timestamp, scope, and outcome |
| Protect scope | Given the selected record is outside authorized scope | When the action is requested | Then the system shall deny access |

### Dependencies

- Customer Management
- Membership Management
- Walk-in Customer Management
- Personal Training
- Notification Management
- Reporting Service
- Audit Service

### Operational Considerations

Calculate Taxes should be designed for high-volume operational use, retry-safe processing, clear exception handling, and support-team diagnostics without exposing sensitive data.

### Non-Functional Considerations

This requirement shall satisfy Digitize non-functional expectations for availability, reliability, performance, scalability, security, configurability, maintainability, and auditability.

### Assumptions

- Required master data and configuration are maintained by authorized users.
- Related services expose stable APIs for validation and synchronization.
- Organization policies define approval, retention, notification, and exception behavior.

### Success Criteria

Calculate Taxes is completed accurately, securely, and audibly, with downstream records synchronized and no loss of historical traceability.

### Related Functional Requirements

- FR-BPM-001 - Generate Invoice
- FR-BPM-002 - Calculate Service Charges
- FR-BPM-003 - Apply Discounts
- FR-BPM-005 - Apply Billing Adjustments
- FR-AUD-001 - Record Audit Events

### Notes

Calculate Taxes shall remain aligned with the approved BA source documents and shall not introduce behavior that bypasses tenant isolation, lifecycle governance, financial controls, or auditability.

---

## FR-BPM-005 - Apply Billing Adjustments

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-BPM-005 |
| Requirement Name | Apply Billing Adjustments |
| Functional Module | Billing & Payment Management |
| Business Domain | Billing & Payment |
| Business Capability | Billing Administration |
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
| Business Requirement | BA-08 BR-018 Billing and Invoice Generation |
| Business Rule | BA-02 BR-BIL-007, BR-BIL-008, BR-AUD-003 |
| Business Process | BA-03 BP-BIL-007 Apply Billing Adjustments |
| Business Process Flow | BA-04 Section 24 Billing Management Flow, Section 25 Payment Management Flow, Section 26 Invoice Management Flow, Section 27 Refund Management Flow |
| Persona | BA-05 Finance Staff, Reception Staff, Customer, Organization Administrator |
| User Journey | BA-06 Section 19 Payment Journey |
| Stakeholder | BA-07 Finance Staff, Reception Staff, Customer |
| Non-Functional Requirement | BA-09 Section 3.7 Data Protection, Section 4.4 Financial Compliance, Section 11 Reporting Requirements |
| Assumption / Constraint / Risk | BA-10 BA-RSK-011, BA-RSK-012, BA-RSK-014 |

### Purpose

To enable Billing Administration within Billing & Payment Management so Digitize can execute Apply Billing Adjustments consistently across Organizations, Facilities, Sites, users, and related operational or commercial services.

### Functional Requirement

The system shall support Apply Billing Adjustments as an atomic Billing & Payment Management capability, including scoped data capture, business-rule validation, permission enforcement, lifecycle handling, related service synchronization, notification generation, reporting contribution, and immutable audit recording.

### Business Justification

Apply Billing Adjustments is required to preserve operational control, revenue accuracy, service continuity, customer trust, and enterprise traceability for Billing & Payment processes. Without this capability, downstream modules would rely on incomplete, manual, or inconsistent records.

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
- Actor has permission for Apply Billing Adjustments.
- Required Billing & Payment configuration and policies are available.
- Related records required by BA-03 BP-BIL-007 Apply Billing Adjustments are available and within authorized scope.

### Trigger

The capability is triggered when Organization Administrator or the System initiates Apply Billing Adjustments from Billing Adjustment, a related workflow, a scheduled job, or an approved integration event.

### In Scope

- Capture or retrieve required Billing & Payment context.
- Validate Organization, Facility, Site, Customer, user, and policy scope where applicable.
- Execute Apply Billing Adjustments according to approved business rules.
- Persist the resulting Invoice state or transaction.
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
- Invoice reference
- Customer reference, where applicable
- Effective date and time, where applicable
- Status or action reason, where applicable
- Payment, billing, trainer, session, or subscription reference where applicable
- Actor remarks, where applicable

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Invoice ID | Primary business record reference | Identifier | Yes | System / User | Must exist or be generated within scope | Core reference for Apply Billing Adjustments |
| Organization ID | Tenant Organization context | Identifier | Yes | Session / System | Must be Active and authorized | Enforces tenant isolation |
| Facility ID | Facility context | Identifier | Conditional | User / System | Must be Active where applicable | Required for facility-level operations |
| Site ID | Site context | Identifier | Conditional | User / System | Must belong to Facility where applicable | Required for site-level operations |
| Status | Lifecycle or processing state | Enum | Yes | System | Must follow allowed state transitions | Drives UI and downstream access |
| Effective Date | Date when action applies | DateTime | Conditional | User / System | Must satisfy policy | Supports scheduled or immediate actions |
| Reason / Remarks | Business explanation | Text | Conditional | User | Required for governed changes | Stored for audit |

### Main Flow

1. Actor opens Billing Adjustment or the related workflow.
2. The system validates authentication, authorization, tenant scope, and current operating context.
3. The system loads the required Billing & Payment records, related configuration, and policy controls.
4. Actor enters or confirms the information required to apply billing adjustments.
5. The system validates mandatory data, lifecycle status, ownership, eligibility, financial, capacity, schedule, and security rules where applicable.
6. The system executes Apply Billing Adjustments and persists the resulting Invoice state or transaction.
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

- Invoice record created, updated, validated, or reported according to the action.
- Lifecycle or processing status updated.
- Related history entry created.
- Business events emitted.
- Notifications generated where configured.
- Audit events recorded.
- Reports or dashboards updated where applicable.

### UI Behaviour

Billing Adjustment shall display scoped context, mandatory fields, lifecycle status, policy warnings, validation results, available actions, confirmation prompts, read-only states, pagination or filters where applicable, and responsive behavior for front-desk and administrative usage.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-BPM-005-001 | Actor must have permission to execute Apply Billing Adjustments. | Deny request and audit. | Critical |
| VAL-BPM-005-002 | Record must belong to the authorized Organization scope. | Deny request. | Critical |
| VAL-BPM-005-003 | Mandatory inputs must be complete and valid. | Block submission. | Critical |
| VAL-BPM-005-004 | Lifecycle and policy rules from BA-02 must be satisfied. | Reject or route for approval. | High |
| VAL-BPM-005-005 | Historical and audit records must be preserved. | Roll back or mark for recovery. | Critical |

### Business Rules

- BA-02 BR-BIL-007
- BA-02 BR-BIL-008
- BA-02 BR-AUD-003

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| bpm.apply.billing.adjustments.view | Organization Administrator | Read | View Apply Billing Adjustments context |
| bpm.apply.billing.adjustments.execute | Organization Administrator | Execute | Execute Apply Billing Adjustments |
| bpm.apply.billing.adjustments.approve | Organization Administrator | Approve | Approve governed exceptions where configured |
| bpm.apply.billing.adjustments.audit.view | Organization Administrator / Support Executive | Read | View audit trace |

### Security Considerations

The capability shall enforce authentication, role-based authorization, tenant isolation, Organization scope, Facility and Site access boundaries, sensitive data masking, secure references, and immutable audit logging.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Apply Billing Adjustments Completed | Primary actor and configured stakeholders | In-App / Email | Action completes | Include reference, status, and effective date where applicable |
| Apply Billing Adjustments Requires Approval | Approver | In-App | Approval rule applies | Include safe summary and requested action |
| Apply Billing Adjustments Failed | Primary actor | In-App | Validation or processing fails | Include safe failure reason and next action |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| ApplyBillingAdjustmentsRequested | Billing & Payment Management | Approval Workflow, Audit Service |
| ApplyBillingAdjustmentsCompleted | Billing & Payment Management | Notification Service, Reporting Service, Audit Service |
| ApplyBillingAdjustmentsRejected | Billing & Payment Management | Notification Service, Audit Service |

### Audit Events

| Audit Event | Description | Actor | Target Entity | Key Data |
|---|---|---|---|---|
| APPLY_BILLING_ADJUSTMENTS_REQUESTED | Apply Billing Adjustments requested | Organization Administrator | Invoice | Scope, reference, and reason |
| APPLY_BILLING_ADJUSTMENTS_COMPLETED | Apply Billing Adjustments completed | Organization Administrator / System | Invoice | Previous and new state |
| APPLY_BILLING_ADJUSTMENTS_REJECTED | Apply Billing Adjustments rejected | System | Invoice | Rejection reason |

### Reports Generated

- Billing & Payment Management Operational Report
- Billing & Payment Management History Report
- Billing & Payment Management Exception Report
- Executive Dashboard

### Related Screens

- Billing Adjustment
- Billing & Payment Management Dashboard
- Billing & Payment Management History
- Audit Log Viewer

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/invoices/{invoiceId}/adjustments | POST | Authorized token | Execute Apply Billing Adjustments | 200 OK or 201 Created with result |
| /api/v1/invoices/{invoiceId}/adjustments/history | GET | Authorized token | Retrieve Apply Billing Adjustments history | 200 OK with history |
| /api/v1/audit-logs | GET | Authorized token | Retrieve related audit events | 200 OK with scoped audit records |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Invoice | Create / Update / Read | Support Apply Billing Adjustments | Governed by Organization scope |
| Invoice Item | Read / Insert | Support Apply Billing Adjustments | Governed by Organization scope |
| Charge | Read / Insert | Support Apply Billing Adjustments | Governed by Organization scope |
| Discount | Read / Insert | Support Apply Billing Adjustments | Governed by Organization scope |
| Tax | Read / Insert | Support Apply Billing Adjustments | Governed by Organization scope |
| Audit Log | Insert | Record auditable activity | Immutable |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Draft | Apply Billing Adjustments initiated | Validated | Organization Administrator | Required data captured |
| Validated | Validation succeeds | Pending Approval | System | BA-02 rules satisfied |
| Pending Approval | Processing completes | Completed | System | Related updates succeed |
| Pending Approval | Approval or policy failure | Rejected | System / Approver | Request rejected |
| Completed | View history | Completed | Authorized user | Read-only historical access |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| BPM-005-001 | Apply Billing Adjustments cannot be completed because required information is missing. | Missing mandatory data | Complete required fields |
| BPM-005-002 | You do not have permission to perform this action. | Authorization failure | Request access |
| BPM-005-003 | The selected record is not eligible for this action. | Policy or lifecycle violation | Review record status |
| BPM-005-004 | Apply Billing Adjustments could not be completed due to a system or integration error. | Processing failure | Retry or contact support |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Execute Apply Billing Adjustments | Given the actor has required permission and valid scope | When the actor submits valid information | Then the system shall complete Apply Billing Adjustments successfully |
| Enforce validation | Given mandatory data or policy conditions are invalid | When the action is submitted | Then the system shall reject the request with a clear message |
| Preserve audit | Given the action completes or fails | When processing ends | Then audit events shall record actor, timestamp, scope, and outcome |
| Protect scope | Given the selected record is outside authorized scope | When the action is requested | Then the system shall deny access |

### Dependencies

- Customer Management
- Membership Management
- Walk-in Customer Management
- Personal Training
- Notification Management
- Reporting Service
- Audit Service

### Operational Considerations

Apply Billing Adjustments should be designed for high-volume operational use, retry-safe processing, clear exception handling, and support-team diagnostics without exposing sensitive data.

### Non-Functional Considerations

This requirement shall satisfy Digitize non-functional expectations for availability, reliability, performance, scalability, security, configurability, maintainability, and auditability.

### Assumptions

- Required master data and configuration are maintained by authorized users.
- Related services expose stable APIs for validation and synchronization.
- Organization policies define approval, retention, notification, and exception behavior.

### Success Criteria

Apply Billing Adjustments is completed accurately, securely, and audibly, with downstream records synchronized and no loss of historical traceability.

### Related Functional Requirements

- FR-BPM-001 - Generate Invoice
- FR-BPM-002 - Calculate Service Charges
- FR-BPM-003 - Apply Discounts
- FR-BPM-004 - Calculate Taxes
- FR-AUD-001 - Record Audit Events

### Notes

Apply Billing Adjustments shall remain aligned with the approved BA source documents and shall not introduce behavior that bypasses tenant isolation, lifecycle governance, financial controls, or auditability.

---

## FR-BPM-006 - Cancel Invoice

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-BPM-006 |
| Requirement Name | Cancel Invoice |
| Functional Module | Billing & Payment Management |
| Business Domain | Billing & Payment |
| Business Capability | Billing Administration |
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
| Business Requirement | BA-08 BR-018 Billing and Invoice Generation |
| Business Rule | BA-02 BR-BIL-005, BR-BIL-008, BR-AUD-003 |
| Business Process | BA-03 BP-BIL-008 Cancel Invoice |
| Business Process Flow | BA-04 Section 24 Billing Management Flow, Section 25 Payment Management Flow, Section 26 Invoice Management Flow, Section 27 Refund Management Flow |
| Persona | BA-05 Finance Staff, Reception Staff, Customer, Organization Administrator |
| User Journey | BA-06 Section 19 Payment Journey |
| Stakeholder | BA-07 Finance Staff, Reception Staff, Customer |
| Non-Functional Requirement | BA-09 Section 3.7 Data Protection, Section 4.4 Financial Compliance, Section 11 Reporting Requirements |
| Assumption / Constraint / Risk | BA-10 BA-RSK-011, BA-RSK-012, BA-RSK-014 |

### Purpose

To enable Billing Administration within Billing & Payment Management so Digitize can execute Cancel Invoice consistently across Organizations, Facilities, Sites, users, and related operational or commercial services.

### Functional Requirement

The system shall support Cancel Invoice as an atomic Billing & Payment Management capability, including scoped data capture, business-rule validation, permission enforcement, lifecycle handling, related service synchronization, notification generation, reporting contribution, and immutable audit recording.

### Business Justification

Cancel Invoice is required to preserve operational control, revenue accuracy, service continuity, customer trust, and enterprise traceability for Billing & Payment processes. Without this capability, downstream modules would rely on incomplete, manual, or inconsistent records.

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
- Actor has permission for Cancel Invoice.
- Required Billing & Payment configuration and policies are available.
- Related records required by BA-03 BP-BIL-008 Cancel Invoice are available and within authorized scope.

### Trigger

The capability is triggered when Organization Administrator or the System initiates Cancel Invoice from Invoice Cancellation, a related workflow, a scheduled job, or an approved integration event.

### In Scope

- Capture or retrieve required Billing & Payment context.
- Validate Organization, Facility, Site, Customer, user, and policy scope where applicable.
- Execute Cancel Invoice according to approved business rules.
- Persist the resulting Invoice state or transaction.
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
- Invoice reference
- Customer reference, where applicable
- Effective date and time, where applicable
- Status or action reason, where applicable
- Payment, billing, trainer, session, or subscription reference where applicable
- Actor remarks, where applicable

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Invoice ID | Primary business record reference | Identifier | Yes | System / User | Must exist or be generated within scope | Core reference for Cancel Invoice |
| Organization ID | Tenant Organization context | Identifier | Yes | Session / System | Must be Active and authorized | Enforces tenant isolation |
| Facility ID | Facility context | Identifier | Conditional | User / System | Must be Active where applicable | Required for facility-level operations |
| Site ID | Site context | Identifier | Conditional | User / System | Must belong to Facility where applicable | Required for site-level operations |
| Status | Lifecycle or processing state | Enum | Yes | System | Must follow allowed state transitions | Drives UI and downstream access |
| Effective Date | Date when action applies | DateTime | Conditional | User / System | Must satisfy policy | Supports scheduled or immediate actions |
| Reason / Remarks | Business explanation | Text | Conditional | User | Required for governed changes | Stored for audit |

### Main Flow

1. Actor opens Invoice Cancellation or the related workflow.
2. The system validates authentication, authorization, tenant scope, and current operating context.
3. The system loads the required Billing & Payment records, related configuration, and policy controls.
4. Actor enters or confirms the information required to cancel invoice.
5. The system validates mandatory data, lifecycle status, ownership, eligibility, financial, capacity, schedule, and security rules where applicable.
6. The system executes Cancel Invoice and persists the resulting Invoice state or transaction.
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

- Invoice record created, updated, validated, or reported according to the action.
- Lifecycle or processing status updated.
- Related history entry created.
- Business events emitted.
- Notifications generated where configured.
- Audit events recorded.
- Reports or dashboards updated where applicable.

### UI Behaviour

Invoice Cancellation shall display scoped context, mandatory fields, lifecycle status, policy warnings, validation results, available actions, confirmation prompts, read-only states, pagination or filters where applicable, and responsive behavior for front-desk and administrative usage.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-BPM-006-001 | Actor must have permission to execute Cancel Invoice. | Deny request and audit. | Critical |
| VAL-BPM-006-002 | Record must belong to the authorized Organization scope. | Deny request. | Critical |
| VAL-BPM-006-003 | Mandatory inputs must be complete and valid. | Block submission. | Critical |
| VAL-BPM-006-004 | Lifecycle and policy rules from BA-02 must be satisfied. | Reject or route for approval. | High |
| VAL-BPM-006-005 | Historical and audit records must be preserved. | Roll back or mark for recovery. | Critical |

### Business Rules

- BA-02 BR-BIL-005
- BA-02 BR-BIL-008
- BA-02 BR-AUD-003

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| bpm.cancel.invoice.view | Organization Administrator | Read | View Cancel Invoice context |
| bpm.cancel.invoice.execute | Organization Administrator | Execute | Execute Cancel Invoice |
| bpm.cancel.invoice.approve | Organization Administrator | Approve | Approve governed exceptions where configured |
| bpm.cancel.invoice.audit.view | Organization Administrator / Support Executive | Read | View audit trace |

### Security Considerations

The capability shall enforce authentication, role-based authorization, tenant isolation, Organization scope, Facility and Site access boundaries, sensitive data masking, secure references, and immutable audit logging.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Cancel Invoice Completed | Primary actor and configured stakeholders | In-App / Email | Action completes | Include reference, status, and effective date where applicable |
| Cancel Invoice Requires Approval | Approver | In-App | Approval rule applies | Include safe summary and requested action |
| Cancel Invoice Failed | Primary actor | In-App | Validation or processing fails | Include safe failure reason and next action |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| CancelInvoiceRequested | Billing & Payment Management | Approval Workflow, Audit Service |
| CancelInvoiceCompleted | Billing & Payment Management | Notification Service, Reporting Service, Audit Service |
| CancelInvoiceRejected | Billing & Payment Management | Notification Service, Audit Service |

### Audit Events

| Audit Event | Description | Actor | Target Entity | Key Data |
|---|---|---|---|---|
| CANCEL_INVOICE_REQUESTED | Cancel Invoice requested | Organization Administrator | Invoice | Scope, reference, and reason |
| CANCEL_INVOICE_COMPLETED | Cancel Invoice completed | Organization Administrator / System | Invoice | Previous and new state |
| CANCEL_INVOICE_REJECTED | Cancel Invoice rejected | System | Invoice | Rejection reason |

### Reports Generated

- Billing & Payment Management Operational Report
- Billing & Payment Management History Report
- Billing & Payment Management Exception Report
- Executive Dashboard

### Related Screens

- Invoice Cancellation
- Billing & Payment Management Dashboard
- Billing & Payment Management History
- Audit Log Viewer

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/invoices/{invoiceId}/cancel | POST | Authorized token | Execute Cancel Invoice | 200 OK or 201 Created with result |
| /api/v1/invoices/{invoiceId}/cancel/history | GET | Authorized token | Retrieve Cancel Invoice history | 200 OK with history |
| /api/v1/audit-logs | GET | Authorized token | Retrieve related audit events | 200 OK with scoped audit records |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Invoice | Create / Update / Read | Support Cancel Invoice | Governed by Organization scope |
| Invoice Item | Read / Insert | Support Cancel Invoice | Governed by Organization scope |
| Charge | Read / Insert | Support Cancel Invoice | Governed by Organization scope |
| Discount | Read / Insert | Support Cancel Invoice | Governed by Organization scope |
| Tax | Read / Insert | Support Cancel Invoice | Governed by Organization scope |
| Audit Log | Insert | Record auditable activity | Immutable |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Draft | Cancel Invoice initiated | Validated | Organization Administrator | Required data captured |
| Validated | Validation succeeds | Pending Approval | System | BA-02 rules satisfied |
| Pending Approval | Processing completes | Completed | System | Related updates succeed |
| Pending Approval | Approval or policy failure | Rejected | System / Approver | Request rejected |
| Completed | View history | Completed | Authorized user | Read-only historical access |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| BPM-006-001 | Cancel Invoice cannot be completed because required information is missing. | Missing mandatory data | Complete required fields |
| BPM-006-002 | You do not have permission to perform this action. | Authorization failure | Request access |
| BPM-006-003 | The selected record is not eligible for this action. | Policy or lifecycle violation | Review record status |
| BPM-006-004 | Cancel Invoice could not be completed due to a system or integration error. | Processing failure | Retry or contact support |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Execute Cancel Invoice | Given the actor has required permission and valid scope | When the actor submits valid information | Then the system shall complete Cancel Invoice successfully |
| Enforce validation | Given mandatory data or policy conditions are invalid | When the action is submitted | Then the system shall reject the request with a clear message |
| Preserve audit | Given the action completes or fails | When processing ends | Then audit events shall record actor, timestamp, scope, and outcome |
| Protect scope | Given the selected record is outside authorized scope | When the action is requested | Then the system shall deny access |

### Dependencies

- Customer Management
- Membership Management
- Walk-in Customer Management
- Personal Training
- Notification Management
- Reporting Service
- Audit Service

### Operational Considerations

Cancel Invoice should be designed for high-volume operational use, retry-safe processing, clear exception handling, and support-team diagnostics without exposing sensitive data.

### Non-Functional Considerations

This requirement shall satisfy Digitize non-functional expectations for availability, reliability, performance, scalability, security, configurability, maintainability, and auditability.

### Assumptions

- Required master data and configuration are maintained by authorized users.
- Related services expose stable APIs for validation and synchronization.
- Organization policies define approval, retention, notification, and exception behavior.

### Success Criteria

Cancel Invoice is completed accurately, securely, and audibly, with downstream records synchronized and no loss of historical traceability.

### Related Functional Requirements

- FR-BPM-001 - Generate Invoice
- FR-BPM-002 - Calculate Service Charges
- FR-BPM-003 - Apply Discounts
- FR-BPM-004 - Calculate Taxes
- FR-AUD-001 - Record Audit Events

### Notes

Cancel Invoice shall remain aligned with the approved BA source documents and shall not introduce behavior that bypasses tenant isolation, lifecycle governance, financial controls, or auditability.

---

## FR-BPM-007 - Generate Credit Note

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-BPM-007 |
| Requirement Name | Generate Credit Note |
| Functional Module | Billing & Payment Management |
| Business Domain | Billing & Payment |
| Business Capability | Credit Management |
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
| Business Requirement | BA-08 BR-020 Refund Processing |
| Business Rule | BA-02 BR-BIL-006, BR-BIL-008, BR-PAY-006 |
| Business Process | BA-03 BP-BIL-009 Generate Credit Note |
| Business Process Flow | BA-04 Section 24 Billing Management Flow, Section 25 Payment Management Flow, Section 26 Invoice Management Flow, Section 27 Refund Management Flow |
| Persona | BA-05 Finance Staff, Reception Staff, Customer, Organization Administrator |
| User Journey | BA-06 Section 19 Payment Journey |
| Stakeholder | BA-07 Finance Staff, Reception Staff, Customer |
| Non-Functional Requirement | BA-09 Section 3.7 Data Protection, Section 4.4 Financial Compliance, Section 11 Reporting Requirements |
| Assumption / Constraint / Risk | BA-10 BA-RSK-011, BA-RSK-012, BA-RSK-014 |

### Purpose

To enable Credit Management within Billing & Payment Management so Digitize can execute Generate Credit Note consistently across Organizations, Facilities, Sites, users, and related operational or commercial services.

### Functional Requirement

The system shall support Generate Credit Note as an atomic Billing & Payment Management capability, including scoped data capture, business-rule validation, permission enforcement, lifecycle handling, related service synchronization, notification generation, reporting contribution, and immutable audit recording.

### Business Justification

Generate Credit Note is required to preserve operational control, revenue accuracy, service continuity, customer trust, and enterprise traceability for Billing & Payment processes. Without this capability, downstream modules would rely on incomplete, manual, or inconsistent records.

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
- Actor has permission for Generate Credit Note.
- Required Billing & Payment configuration and policies are available.
- Related records required by BA-03 BP-BIL-009 Generate Credit Note are available and within authorized scope.

### Trigger

The capability is triggered when Organization Administrator or the System initiates Generate Credit Note from Credit Note, a related workflow, a scheduled job, or an approved integration event.

### In Scope

- Capture or retrieve required Billing & Payment context.
- Validate Organization, Facility, Site, Customer, user, and policy scope where applicable.
- Execute Generate Credit Note according to approved business rules.
- Persist the resulting Invoice state or transaction.
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
- Invoice reference
- Customer reference, where applicable
- Effective date and time, where applicable
- Status or action reason, where applicable
- Payment, billing, trainer, session, or subscription reference where applicable
- Actor remarks, where applicable

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Invoice ID | Primary business record reference | Identifier | Yes | System / User | Must exist or be generated within scope | Core reference for Generate Credit Note |
| Organization ID | Tenant Organization context | Identifier | Yes | Session / System | Must be Active and authorized | Enforces tenant isolation |
| Facility ID | Facility context | Identifier | Conditional | User / System | Must be Active where applicable | Required for facility-level operations |
| Site ID | Site context | Identifier | Conditional | User / System | Must belong to Facility where applicable | Required for site-level operations |
| Status | Lifecycle or processing state | Enum | Yes | System | Must follow allowed state transitions | Drives UI and downstream access |
| Effective Date | Date when action applies | DateTime | Conditional | User / System | Must satisfy policy | Supports scheduled or immediate actions |
| Reason / Remarks | Business explanation | Text | Conditional | User | Required for governed changes | Stored for audit |

### Main Flow

1. Actor opens Credit Note or the related workflow.
2. The system validates authentication, authorization, tenant scope, and current operating context.
3. The system loads the required Billing & Payment records, related configuration, and policy controls.
4. Actor enters or confirms the information required to generate credit note.
5. The system validates mandatory data, lifecycle status, ownership, eligibility, financial, capacity, schedule, and security rules where applicable.
6. The system executes Generate Credit Note and persists the resulting Invoice state or transaction.
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

- Invoice record created, updated, validated, or reported according to the action.
- Lifecycle or processing status updated.
- Related history entry created.
- Business events emitted.
- Notifications generated where configured.
- Audit events recorded.
- Reports or dashboards updated where applicable.

### UI Behaviour

Credit Note shall display scoped context, mandatory fields, lifecycle status, policy warnings, validation results, available actions, confirmation prompts, read-only states, pagination or filters where applicable, and responsive behavior for front-desk and administrative usage.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-BPM-007-001 | Actor must have permission to execute Generate Credit Note. | Deny request and audit. | Critical |
| VAL-BPM-007-002 | Record must belong to the authorized Organization scope. | Deny request. | Critical |
| VAL-BPM-007-003 | Mandatory inputs must be complete and valid. | Block submission. | Critical |
| VAL-BPM-007-004 | Lifecycle and policy rules from BA-02 must be satisfied. | Reject or route for approval. | High |
| VAL-BPM-007-005 | Historical and audit records must be preserved. | Roll back or mark for recovery. | Critical |

### Business Rules

- BA-02 BR-BIL-006
- BA-02 BR-BIL-008
- BA-02 BR-PAY-006

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| bpm.generate.credit.note.view | Organization Administrator | Read | View Generate Credit Note context |
| bpm.generate.credit.note.execute | Organization Administrator | Execute | Execute Generate Credit Note |
| bpm.generate.credit.note.approve | Organization Administrator | Approve | Approve governed exceptions where configured |
| bpm.generate.credit.note.audit.view | Organization Administrator / Support Executive | Read | View audit trace |

### Security Considerations

The capability shall enforce authentication, role-based authorization, tenant isolation, Organization scope, Facility and Site access boundaries, sensitive data masking, secure references, and immutable audit logging.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Generate Credit Note Completed | Primary actor and configured stakeholders | In-App / Email | Action completes | Include reference, status, and effective date where applicable |
| Generate Credit Note Requires Approval | Approver | In-App | Approval rule applies | Include safe summary and requested action |
| Generate Credit Note Failed | Primary actor | In-App | Validation or processing fails | Include safe failure reason and next action |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| GenerateCreditNoteRequested | Billing & Payment Management | Approval Workflow, Audit Service |
| GenerateCreditNoteCompleted | Billing & Payment Management | Notification Service, Reporting Service, Audit Service |
| GenerateCreditNoteRejected | Billing & Payment Management | Notification Service, Audit Service |

### Audit Events

| Audit Event | Description | Actor | Target Entity | Key Data |
|---|---|---|---|---|
| GENERATE_CREDIT_NOTE_REQUESTED | Generate Credit Note requested | Organization Administrator | Invoice | Scope, reference, and reason |
| GENERATE_CREDIT_NOTE_COMPLETED | Generate Credit Note completed | Organization Administrator / System | Invoice | Previous and new state |
| GENERATE_CREDIT_NOTE_REJECTED | Generate Credit Note rejected | System | Invoice | Rejection reason |

### Reports Generated

- Billing & Payment Management Operational Report
- Billing & Payment Management History Report
- Billing & Payment Management Exception Report
- Executive Dashboard

### Related Screens

- Credit Note
- Billing & Payment Management Dashboard
- Billing & Payment Management History
- Audit Log Viewer

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/credit-notes | POST | Authorized token | Execute Generate Credit Note | 200 OK or 201 Created with result |
| /api/v1/credit-notes/history | GET | Authorized token | Retrieve Generate Credit Note history | 200 OK with history |
| /api/v1/audit-logs | GET | Authorized token | Retrieve related audit events | 200 OK with scoped audit records |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Invoice | Create / Update / Read | Support Generate Credit Note | Governed by Organization scope |
| Invoice Item | Read / Insert | Support Generate Credit Note | Governed by Organization scope |
| Charge | Read / Insert | Support Generate Credit Note | Governed by Organization scope |
| Discount | Read / Insert | Support Generate Credit Note | Governed by Organization scope |
| Tax | Read / Insert | Support Generate Credit Note | Governed by Organization scope |
| Audit Log | Insert | Record auditable activity | Immutable |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Draft | Generate Credit Note initiated | Validated | Organization Administrator | Required data captured |
| Validated | Validation succeeds | Pending Approval | System | BA-02 rules satisfied |
| Pending Approval | Processing completes | Completed | System | Related updates succeed |
| Pending Approval | Approval or policy failure | Rejected | System / Approver | Request rejected |
| Completed | View history | Completed | Authorized user | Read-only historical access |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| BPM-007-001 | Generate Credit Note cannot be completed because required information is missing. | Missing mandatory data | Complete required fields |
| BPM-007-002 | You do not have permission to perform this action. | Authorization failure | Request access |
| BPM-007-003 | The selected record is not eligible for this action. | Policy or lifecycle violation | Review record status |
| BPM-007-004 | Generate Credit Note could not be completed due to a system or integration error. | Processing failure | Retry or contact support |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Execute Generate Credit Note | Given the actor has required permission and valid scope | When the actor submits valid information | Then the system shall complete Generate Credit Note successfully |
| Enforce validation | Given mandatory data or policy conditions are invalid | When the action is submitted | Then the system shall reject the request with a clear message |
| Preserve audit | Given the action completes or fails | When processing ends | Then audit events shall record actor, timestamp, scope, and outcome |
| Protect scope | Given the selected record is outside authorized scope | When the action is requested | Then the system shall deny access |

### Dependencies

- Customer Management
- Membership Management
- Walk-in Customer Management
- Personal Training
- Notification Management
- Reporting Service
- Audit Service

### Operational Considerations

Generate Credit Note should be designed for high-volume operational use, retry-safe processing, clear exception handling, and support-team diagnostics without exposing sensitive data.

### Non-Functional Considerations

This requirement shall satisfy Digitize non-functional expectations for availability, reliability, performance, scalability, security, configurability, maintainability, and auditability.

### Assumptions

- Required master data and configuration are maintained by authorized users.
- Related services expose stable APIs for validation and synchronization.
- Organization policies define approval, retention, notification, and exception behavior.

### Success Criteria

Generate Credit Note is completed accurately, securely, and audibly, with downstream records synchronized and no loss of historical traceability.

### Related Functional Requirements

- FR-BPM-001 - Generate Invoice
- FR-BPM-002 - Calculate Service Charges
- FR-BPM-003 - Apply Discounts
- FR-BPM-004 - Calculate Taxes
- FR-AUD-001 - Record Audit Events

### Notes

Generate Credit Note shall remain aligned with the approved BA source documents and shall not introduce behavior that bypasses tenant isolation, lifecycle governance, financial controls, or auditability.

---

## FR-BPM-008 - Collect Payment

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-BPM-008 |
| Requirement Name | Collect Payment |
| Functional Module | Billing & Payment Management |
| Business Domain | Billing & Payment |
| Business Capability | Payment Management |
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
| Business Requirement | BA-08 BR-019 Payment Collection |
| Business Rule | BA-02 BR-PAY-001, BR-PAY-002, BR-PAY-003, BR-PAY-004, BR-PAY-007 |
| Business Process | BA-03 BP-PAY-001 Collect Payment |
| Business Process Flow | BA-04 Section 24 Billing Management Flow, Section 25 Payment Management Flow, Section 26 Invoice Management Flow, Section 27 Refund Management Flow |
| Persona | BA-05 Finance Staff, Reception Staff, Customer, Organization Administrator |
| User Journey | BA-06 Section 19 Payment Journey |
| Stakeholder | BA-07 Finance Staff, Reception Staff, Customer |
| Non-Functional Requirement | BA-09 Section 3.7 Data Protection, Section 4.4 Financial Compliance, Section 11 Reporting Requirements |
| Assumption / Constraint / Risk | BA-10 BA-RSK-011, BA-RSK-012, BA-RSK-014 |

### Purpose

To enable Payment Management within Billing & Payment Management so Digitize can execute Collect Payment consistently across Organizations, Facilities, Sites, users, and related operational or commercial services.

### Functional Requirement

The system shall support Collect Payment as an atomic Billing & Payment Management capability, including scoped data capture, business-rule validation, permission enforcement, lifecycle handling, related service synchronization, notification generation, reporting contribution, and immutable audit recording.

### Business Justification

Collect Payment is required to preserve operational control, revenue accuracy, service continuity, customer trust, and enterprise traceability for Billing & Payment processes. Without this capability, downstream modules would rely on incomplete, manual, or inconsistent records.

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
- Actor has permission for Collect Payment.
- Required Billing & Payment configuration and policies are available.
- Related records required by BA-03 BP-PAY-001 Collect Payment are available and within authorized scope.

### Trigger

The capability is triggered when Reception Staff or the System initiates Collect Payment from Payment Collection, a related workflow, a scheduled job, or an approved integration event.

### In Scope

- Capture or retrieve required Billing & Payment context.
- Validate Organization, Facility, Site, Customer, user, and policy scope where applicable.
- Execute Collect Payment according to approved business rules.
- Persist the resulting Payment state or transaction.
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
- Payment reference
- Customer reference, where applicable
- Effective date and time, where applicable
- Status or action reason, where applicable
- Payment, billing, trainer, session, or subscription reference where applicable
- Actor remarks, where applicable

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Payment ID | Primary business record reference | Identifier | Yes | System / User | Must exist or be generated within scope | Core reference for Collect Payment |
| Organization ID | Tenant Organization context | Identifier | Yes | Session / System | Must be Active and authorized | Enforces tenant isolation |
| Facility ID | Facility context | Identifier | Conditional | User / System | Must be Active where applicable | Required for facility-level operations |
| Site ID | Site context | Identifier | Conditional | User / System | Must belong to Facility where applicable | Required for site-level operations |
| Status | Lifecycle or processing state | Enum | Yes | System | Must follow allowed state transitions | Drives UI and downstream access |
| Effective Date | Date when action applies | DateTime | Conditional | User / System | Must satisfy policy | Supports scheduled or immediate actions |
| Reason / Remarks | Business explanation | Text | Conditional | User | Required for governed changes | Stored for audit |

### Main Flow

1. Actor opens Payment Collection or the related workflow.
2. The system validates authentication, authorization, tenant scope, and current operating context.
3. The system loads the required Billing & Payment records, related configuration, and policy controls.
4. Actor enters or confirms the information required to collect payment.
5. The system validates mandatory data, lifecycle status, ownership, eligibility, financial, capacity, schedule, and security rules where applicable.
6. The system executes Collect Payment and persists the resulting Payment state or transaction.
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

- Payment record created, updated, validated, or reported according to the action.
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
| VAL-BPM-008-001 | Actor must have permission to execute Collect Payment. | Deny request and audit. | Critical |
| VAL-BPM-008-002 | Record must belong to the authorized Organization scope. | Deny request. | Critical |
| VAL-BPM-008-003 | Mandatory inputs must be complete and valid. | Block submission. | Critical |
| VAL-BPM-008-004 | Lifecycle and policy rules from BA-02 must be satisfied. | Reject or route for approval. | High |
| VAL-BPM-008-005 | Historical and audit records must be preserved. | Roll back or mark for recovery. | Critical |

### Business Rules

- BA-02 BR-PAY-001
- BA-02 BR-PAY-002
- BA-02 BR-PAY-003
- BA-02 BR-PAY-004
- BA-02 BR-PAY-007

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| bpm.collect.payment.view | Reception Staff | Read | View Collect Payment context |
| bpm.collect.payment.execute | Reception Staff | Execute | Execute Collect Payment |
| bpm.collect.payment.approve | Organization Administrator | Approve | Approve governed exceptions where configured |
| bpm.collect.payment.audit.view | Organization Administrator / Support Executive | Read | View audit trace |

### Security Considerations

The capability shall enforce authentication, role-based authorization, tenant isolation, Organization scope, Facility and Site access boundaries, sensitive data masking, secure references, and immutable audit logging.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Collect Payment Completed | Primary actor and configured stakeholders | In-App / Email | Action completes | Include reference, status, and effective date where applicable |
| Collect Payment Requires Approval | Approver | In-App | Approval rule applies | Include safe summary and requested action |
| Collect Payment Failed | Primary actor | In-App | Validation or processing fails | Include safe failure reason and next action |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| CollectPaymentRequested | Billing & Payment Management | Approval Workflow, Audit Service |
| CollectPaymentCompleted | Billing & Payment Management | Notification Service, Reporting Service, Audit Service |
| CollectPaymentRejected | Billing & Payment Management | Notification Service, Audit Service |

### Audit Events

| Audit Event | Description | Actor | Target Entity | Key Data |
|---|---|---|---|---|
| COLLECT_PAYMENT_REQUESTED | Collect Payment requested | Reception Staff | Payment | Scope, reference, and reason |
| COLLECT_PAYMENT_COMPLETED | Collect Payment completed | Reception Staff / System | Payment | Previous and new state |
| COLLECT_PAYMENT_REJECTED | Collect Payment rejected | System | Payment | Rejection reason |

### Reports Generated

- Billing & Payment Management Operational Report
- Billing & Payment Management History Report
- Billing & Payment Management Exception Report
- Executive Dashboard

### Related Screens

- Payment Collection
- Billing & Payment Management Dashboard
- Billing & Payment Management History
- Audit Log Viewer

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/payments | POST | Authorized token | Execute Collect Payment | 200 OK or 201 Created with result |
| /api/v1/payments/history | GET | Authorized token | Retrieve Collect Payment history | 200 OK with history |
| /api/v1/audit-logs | GET | Authorized token | Retrieve related audit events | 200 OK with scoped audit records |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Payment | Create / Update / Read | Support Collect Payment | Governed by Organization scope |
| Payment Transaction | Read / Insert | Support Collect Payment | Governed by Organization scope |
| Payment Receipt | Read / Insert | Support Collect Payment | Governed by Organization scope |
| Refund | Read / Insert | Support Collect Payment | Governed by Organization scope |
| Reconciliation | Read / Insert | Support Collect Payment | Governed by Organization scope |
| Audit Log | Insert | Record auditable activity | Immutable |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Draft | Collect Payment initiated | Validated | Reception Staff | Required data captured |
| Validated | Validation succeeds | Pending Approval | System | BA-02 rules satisfied |
| Pending Approval | Processing completes | Completed | System | Related updates succeed |
| Pending Approval | Approval or policy failure | Rejected | System / Approver | Request rejected |
| Completed | View history | Completed | Authorized user | Read-only historical access |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| BPM-008-001 | Collect Payment cannot be completed because required information is missing. | Missing mandatory data | Complete required fields |
| BPM-008-002 | You do not have permission to perform this action. | Authorization failure | Request access |
| BPM-008-003 | The selected record is not eligible for this action. | Policy or lifecycle violation | Review record status |
| BPM-008-004 | Collect Payment could not be completed due to a system or integration error. | Processing failure | Retry or contact support |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Execute Collect Payment | Given the actor has required permission and valid scope | When the actor submits valid information | Then the system shall complete Collect Payment successfully |
| Enforce validation | Given mandatory data or policy conditions are invalid | When the action is submitted | Then the system shall reject the request with a clear message |
| Preserve audit | Given the action completes or fails | When processing ends | Then audit events shall record actor, timestamp, scope, and outcome |
| Protect scope | Given the selected record is outside authorized scope | When the action is requested | Then the system shall deny access |

### Dependencies

- Customer Management
- Membership Management
- Walk-in Customer Management
- Personal Training
- Notification Management
- Reporting Service
- Audit Service

### Operational Considerations

Collect Payment should be designed for high-volume operational use, retry-safe processing, clear exception handling, and support-team diagnostics without exposing sensitive data.

### Non-Functional Considerations

This requirement shall satisfy Digitize non-functional expectations for availability, reliability, performance, scalability, security, configurability, maintainability, and auditability.

### Assumptions

- Required master data and configuration are maintained by authorized users.
- Related services expose stable APIs for validation and synchronization.
- Organization policies define approval, retention, notification, and exception behavior.

### Success Criteria

Collect Payment is completed accurately, securely, and audibly, with downstream records synchronized and no loss of historical traceability.

### Related Functional Requirements

- FR-BPM-001 - Generate Invoice
- FR-BPM-002 - Calculate Service Charges
- FR-BPM-003 - Apply Discounts
- FR-BPM-004 - Calculate Taxes
- FR-AUD-001 - Record Audit Events

### Notes

Collect Payment shall remain aligned with the approved BA source documents and shall not introduce behavior that bypasses tenant isolation, lifecycle governance, financial controls, or auditability.

---

## FR-BPM-009 - Process Online Payment

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-BPM-009 |
| Requirement Name | Process Online Payment |
| Functional Module | Billing & Payment Management |
| Business Domain | Billing & Payment |
| Business Capability | Digital Payment Processing |
| Requirement Type | Functional |
| Requirement Category | Integration |
| Requirement Version | 1.0 |
| Requirement Status | Approved |
| Priority | Critical |
| Complexity | High |
| Release Version | 1.0 |
| Owner | Product Management |

### Traceability References

| Traceability Type | Reference |
|---|---|
| Business Requirement | BA-08 BR-019 Payment Collection |
| Business Rule | BA-02 BR-PAY-001, BR-PAY-002, BR-PAY-003, BR-PAY-005, BR-PAY-007 |
| Business Process | BA-03 BP-PAY-002 Process Online Payment |
| Business Process Flow | BA-04 Section 24 Billing Management Flow, Section 25 Payment Management Flow, Section 26 Invoice Management Flow, Section 27 Refund Management Flow |
| Persona | BA-05 Finance Staff, Reception Staff, Customer, Organization Administrator |
| User Journey | BA-06 Section 19 Payment Journey |
| Stakeholder | BA-07 Finance Staff, Reception Staff, Customer |
| Non-Functional Requirement | BA-09 Section 3.7 Data Protection, Section 4.4 Financial Compliance, Section 11 Reporting Requirements |
| Assumption / Constraint / Risk | BA-10 BA-RSK-011, BA-RSK-012, BA-RSK-014 |

### Purpose

To enable Digital Payment Processing within Billing & Payment Management so Digitize can execute Process Online Payment consistently across Organizations, Facilities, Sites, users, and related operational or commercial services.

### Functional Requirement

The system shall support Process Online Payment as an atomic Billing & Payment Management capability, including scoped data capture, business-rule validation, permission enforcement, lifecycle handling, related service synchronization, notification generation, reporting contribution, and immutable audit recording.

### Business Justification

Process Online Payment is required to preserve operational control, revenue accuracy, service continuity, customer trust, and enterprise traceability for Billing & Payment processes. Without this capability, downstream modules would rely on incomplete, manual, or inconsistent records.

### Actors

- Payment Gateway
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
- Actor has permission for Process Online Payment.
- Required Billing & Payment configuration and policies are available.
- Related records required by BA-03 BP-PAY-002 Process Online Payment are available and within authorized scope.

### Trigger

The capability is triggered when Payment Gateway or the System initiates Process Online Payment from Online Payment, a related workflow, a scheduled job, or an approved integration event.

### In Scope

- Capture or retrieve required Billing & Payment context.
- Validate Organization, Facility, Site, Customer, user, and policy scope where applicable.
- Execute Process Online Payment according to approved business rules.
- Persist the resulting Payment state or transaction.
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
- Payment reference
- Customer reference, where applicable
- Effective date and time, where applicable
- Status or action reason, where applicable
- Payment, billing, trainer, session, or subscription reference where applicable
- Actor remarks, where applicable

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Payment ID | Primary business record reference | Identifier | Yes | System / User | Must exist or be generated within scope | Core reference for Process Online Payment |
| Organization ID | Tenant Organization context | Identifier | Yes | Session / System | Must be Active and authorized | Enforces tenant isolation |
| Facility ID | Facility context | Identifier | Conditional | User / System | Must be Active where applicable | Required for facility-level operations |
| Site ID | Site context | Identifier | Conditional | User / System | Must belong to Facility where applicable | Required for site-level operations |
| Status | Lifecycle or processing state | Enum | Yes | System | Must follow allowed state transitions | Drives UI and downstream access |
| Effective Date | Date when action applies | DateTime | Conditional | User / System | Must satisfy policy | Supports scheduled or immediate actions |
| Reason / Remarks | Business explanation | Text | Conditional | User | Required for governed changes | Stored for audit |

### Main Flow

1. Actor opens Online Payment or the related workflow.
2. The system validates authentication, authorization, tenant scope, and current operating context.
3. The system loads the required Billing & Payment records, related configuration, and policy controls.
4. Actor enters or confirms the information required to process online payment.
5. The system validates mandatory data, lifecycle status, ownership, eligibility, financial, capacity, schedule, and security rules where applicable.
6. The system executes Process Online Payment and persists the resulting Payment state or transaction.
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

- Payment record created, updated, validated, or reported according to the action.
- Lifecycle or processing status updated.
- Related history entry created.
- Business events emitted.
- Notifications generated where configured.
- Audit events recorded.
- Reports or dashboards updated where applicable.

### UI Behaviour

Online Payment shall display scoped context, mandatory fields, lifecycle status, policy warnings, validation results, available actions, confirmation prompts, read-only states, pagination or filters where applicable, and responsive behavior for front-desk and administrative usage.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-BPM-009-001 | Actor must have permission to execute Process Online Payment. | Deny request and audit. | Critical |
| VAL-BPM-009-002 | Record must belong to the authorized Organization scope. | Deny request. | Critical |
| VAL-BPM-009-003 | Mandatory inputs must be complete and valid. | Block submission. | Critical |
| VAL-BPM-009-004 | Lifecycle and policy rules from BA-02 must be satisfied. | Reject or route for approval. | High |
| VAL-BPM-009-005 | Historical and audit records must be preserved. | Roll back or mark for recovery. | Critical |

### Business Rules

- BA-02 BR-PAY-001
- BA-02 BR-PAY-002
- BA-02 BR-PAY-003
- BA-02 BR-PAY-005
- BA-02 BR-PAY-007

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| bpm.process.online.payment.view | Payment Gateway | Read | View Process Online Payment context |
| bpm.process.online.payment.execute | Payment Gateway | Execute | Execute Process Online Payment |
| bpm.process.online.payment.approve | Organization Administrator | Approve | Approve governed exceptions where configured |
| bpm.process.online.payment.audit.view | Organization Administrator / Support Executive | Read | View audit trace |

### Security Considerations

The capability shall enforce authentication, role-based authorization, tenant isolation, Organization scope, Facility and Site access boundaries, sensitive data masking, secure references, and immutable audit logging.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Process Online Payment Completed | Primary actor and configured stakeholders | In-App / Email | Action completes | Include reference, status, and effective date where applicable |
| Process Online Payment Requires Approval | Approver | In-App | Approval rule applies | Include safe summary and requested action |
| Process Online Payment Failed | Primary actor | In-App | Validation or processing fails | Include safe failure reason and next action |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| ProcessOnlinePaymentRequested | Billing & Payment Management | Approval Workflow, Audit Service |
| ProcessOnlinePaymentCompleted | Billing & Payment Management | Notification Service, Reporting Service, Audit Service |
| ProcessOnlinePaymentRejected | Billing & Payment Management | Notification Service, Audit Service |

### Audit Events

| Audit Event | Description | Actor | Target Entity | Key Data |
|---|---|---|---|---|
| PROCESS_ONLINE_PAYMENT_REQUESTED | Process Online Payment requested | Payment Gateway | Payment | Scope, reference, and reason |
| PROCESS_ONLINE_PAYMENT_COMPLETED | Process Online Payment completed | Payment Gateway / System | Payment | Previous and new state |
| PROCESS_ONLINE_PAYMENT_REJECTED | Process Online Payment rejected | System | Payment | Rejection reason |

### Reports Generated

- Billing & Payment Management Operational Report
- Billing & Payment Management History Report
- Billing & Payment Management Exception Report
- Executive Dashboard

### Related Screens

- Online Payment
- Billing & Payment Management Dashboard
- Billing & Payment Management History
- Audit Log Viewer

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/payments/online | POST | Authorized token | Execute Process Online Payment | 200 OK or 201 Created with result |
| /api/v1/payments/online/history | GET | Authorized token | Retrieve Process Online Payment history | 200 OK with history |
| /api/v1/audit-logs | GET | Authorized token | Retrieve related audit events | 200 OK with scoped audit records |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Payment | Create / Update / Read | Support Process Online Payment | Governed by Organization scope |
| Payment Transaction | Read / Insert | Support Process Online Payment | Governed by Organization scope |
| Payment Receipt | Read / Insert | Support Process Online Payment | Governed by Organization scope |
| Refund | Read / Insert | Support Process Online Payment | Governed by Organization scope |
| Reconciliation | Read / Insert | Support Process Online Payment | Governed by Organization scope |
| Audit Log | Insert | Record auditable activity | Immutable |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Initiated | Process Online Payment initiated | Processing | Payment Gateway | Required data captured |
| Processing | Validation succeeds | Successful | System | BA-02 rules satisfied |
| Successful | Processing completes | Failed | System | Related updates succeed |
| Successful | Approval or policy failure | Reconciled | System / Approver | Request rejected |
| Failed | View history | Failed | Authorized user | Read-only historical access |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| BPM-009-001 | Process Online Payment cannot be completed because required information is missing. | Missing mandatory data | Complete required fields |
| BPM-009-002 | You do not have permission to perform this action. | Authorization failure | Request access |
| BPM-009-003 | The selected record is not eligible for this action. | Policy or lifecycle violation | Review record status |
| BPM-009-004 | Process Online Payment could not be completed due to a system or integration error. | Processing failure | Retry or contact support |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Execute Process Online Payment | Given the actor has required permission and valid scope | When the actor submits valid information | Then the system shall complete Process Online Payment successfully |
| Enforce validation | Given mandatory data or policy conditions are invalid | When the action is submitted | Then the system shall reject the request with a clear message |
| Preserve audit | Given the action completes or fails | When processing ends | Then audit events shall record actor, timestamp, scope, and outcome |
| Protect scope | Given the selected record is outside authorized scope | When the action is requested | Then the system shall deny access |

### Dependencies

- Customer Management
- Membership Management
- Walk-in Customer Management
- Personal Training
- Notification Management
- Reporting Service
- Audit Service

### Operational Considerations

Process Online Payment should be designed for high-volume operational use, retry-safe processing, clear exception handling, and support-team diagnostics without exposing sensitive data.

### Non-Functional Considerations

This requirement shall satisfy Digitize non-functional expectations for availability, reliability, performance, scalability, security, configurability, maintainability, and auditability.

### Assumptions

- Required master data and configuration are maintained by authorized users.
- Related services expose stable APIs for validation and synchronization.
- Organization policies define approval, retention, notification, and exception behavior.

### Success Criteria

Process Online Payment is completed accurately, securely, and audibly, with downstream records synchronized and no loss of historical traceability.

### Related Functional Requirements

- FR-BPM-001 - Generate Invoice
- FR-BPM-002 - Calculate Service Charges
- FR-BPM-003 - Apply Discounts
- FR-BPM-004 - Calculate Taxes
- FR-AUD-001 - Record Audit Events

### Notes

Process Online Payment shall remain aligned with the approved BA source documents and shall not introduce behavior that bypasses tenant isolation, lifecycle governance, financial controls, or auditability.

---

## FR-BPM-010 - Record Offline Payment

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-BPM-010 |
| Requirement Name | Record Offline Payment |
| Functional Module | Billing & Payment Management |
| Business Domain | Billing & Payment |
| Business Capability | Cash and Counter Payment |
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
| Business Requirement | BA-08 BR-019 Payment Collection |
| Business Rule | BA-02 BR-PAY-002, BR-PAY-003, BR-PAY-007, BR-PAY-008 |
| Business Process | BA-03 BP-PAY-003, BP-PAY-004, BP-PAY-005 |
| Business Process Flow | BA-04 Section 24 Billing Management Flow, Section 25 Payment Management Flow, Section 26 Invoice Management Flow, Section 27 Refund Management Flow |
| Persona | BA-05 Finance Staff, Reception Staff, Customer, Organization Administrator |
| User Journey | BA-06 Section 19 Payment Journey |
| Stakeholder | BA-07 Finance Staff, Reception Staff, Customer |
| Non-Functional Requirement | BA-09 Section 3.7 Data Protection, Section 4.4 Financial Compliance, Section 11 Reporting Requirements |
| Assumption / Constraint / Risk | BA-10 BA-RSK-011, BA-RSK-012, BA-RSK-014 |

### Purpose

To enable Cash and Counter Payment within Billing & Payment Management so Digitize can execute Record Offline Payment consistently across Organizations, Facilities, Sites, users, and related operational or commercial services.

### Functional Requirement

The system shall support Record Offline Payment as an atomic Billing & Payment Management capability, including scoped data capture, business-rule validation, permission enforcement, lifecycle handling, related service synchronization, notification generation, reporting contribution, and immutable audit recording.

### Business Justification

Record Offline Payment is required to preserve operational control, revenue accuracy, service continuity, customer trust, and enterprise traceability for Billing & Payment processes. Without this capability, downstream modules would rely on incomplete, manual, or inconsistent records.

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
- Actor has permission for Record Offline Payment.
- Required Billing & Payment configuration and policies are available.
- Related records required by BA-03 BP-PAY-003, BP-PAY-004, BP-PAY-005 are available and within authorized scope.

### Trigger

The capability is triggered when Reception Staff or the System initiates Record Offline Payment from Offline Payment, a related workflow, a scheduled job, or an approved integration event.

### In Scope

- Capture or retrieve required Billing & Payment context.
- Validate Organization, Facility, Site, Customer, user, and policy scope where applicable.
- Execute Record Offline Payment according to approved business rules.
- Persist the resulting Payment state or transaction.
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
- Payment reference
- Customer reference, where applicable
- Effective date and time, where applicable
- Status or action reason, where applicable
- Payment, billing, trainer, session, or subscription reference where applicable
- Actor remarks, where applicable

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Payment ID | Primary business record reference | Identifier | Yes | System / User | Must exist or be generated within scope | Core reference for Record Offline Payment |
| Organization ID | Tenant Organization context | Identifier | Yes | Session / System | Must be Active and authorized | Enforces tenant isolation |
| Facility ID | Facility context | Identifier | Conditional | User / System | Must be Active where applicable | Required for facility-level operations |
| Site ID | Site context | Identifier | Conditional | User / System | Must belong to Facility where applicable | Required for site-level operations |
| Status | Lifecycle or processing state | Enum | Yes | System | Must follow allowed state transitions | Drives UI and downstream access |
| Effective Date | Date when action applies | DateTime | Conditional | User / System | Must satisfy policy | Supports scheduled or immediate actions |
| Reason / Remarks | Business explanation | Text | Conditional | User | Required for governed changes | Stored for audit |

### Main Flow

1. Actor opens Offline Payment or the related workflow.
2. The system validates authentication, authorization, tenant scope, and current operating context.
3. The system loads the required Billing & Payment records, related configuration, and policy controls.
4. Actor enters or confirms the information required to record offline payment.
5. The system validates mandatory data, lifecycle status, ownership, eligibility, financial, capacity, schedule, and security rules where applicable.
6. The system executes Record Offline Payment and persists the resulting Payment state or transaction.
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

- Payment record created, updated, validated, or reported according to the action.
- Lifecycle or processing status updated.
- Related history entry created.
- Business events emitted.
- Notifications generated where configured.
- Audit events recorded.
- Reports or dashboards updated where applicable.

### UI Behaviour

Offline Payment shall display scoped context, mandatory fields, lifecycle status, policy warnings, validation results, available actions, confirmation prompts, read-only states, pagination or filters where applicable, and responsive behavior for front-desk and administrative usage.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-BPM-010-001 | Actor must have permission to execute Record Offline Payment. | Deny request and audit. | Critical |
| VAL-BPM-010-002 | Record must belong to the authorized Organization scope. | Deny request. | Critical |
| VAL-BPM-010-003 | Mandatory inputs must be complete and valid. | Block submission. | Critical |
| VAL-BPM-010-004 | Lifecycle and policy rules from BA-02 must be satisfied. | Reject or route for approval. | High |
| VAL-BPM-010-005 | Historical and audit records must be preserved. | Roll back or mark for recovery. | Critical |

### Business Rules

- BA-02 BR-PAY-002
- BA-02 BR-PAY-003
- BA-02 BR-PAY-007
- BA-02 BR-PAY-008

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| bpm.record.offline.payment.view | Reception Staff | Read | View Record Offline Payment context |
| bpm.record.offline.payment.execute | Reception Staff | Execute | Execute Record Offline Payment |
| bpm.record.offline.payment.approve | Organization Administrator | Approve | Approve governed exceptions where configured |
| bpm.record.offline.payment.audit.view | Organization Administrator / Support Executive | Read | View audit trace |

### Security Considerations

The capability shall enforce authentication, role-based authorization, tenant isolation, Organization scope, Facility and Site access boundaries, sensitive data masking, secure references, and immutable audit logging.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Record Offline Payment Completed | Primary actor and configured stakeholders | In-App / Email | Action completes | Include reference, status, and effective date where applicable |
| Record Offline Payment Requires Approval | Approver | In-App | Approval rule applies | Include safe summary and requested action |
| Record Offline Payment Failed | Primary actor | In-App | Validation or processing fails | Include safe failure reason and next action |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| RecordOfflinePaymentRequested | Billing & Payment Management | Approval Workflow, Audit Service |
| RecordOfflinePaymentCompleted | Billing & Payment Management | Notification Service, Reporting Service, Audit Service |
| RecordOfflinePaymentRejected | Billing & Payment Management | Notification Service, Audit Service |

### Audit Events

| Audit Event | Description | Actor | Target Entity | Key Data |
|---|---|---|---|---|
| RECORD_OFFLINE_PAYMENT_REQUESTED | Record Offline Payment requested | Reception Staff | Payment | Scope, reference, and reason |
| RECORD_OFFLINE_PAYMENT_COMPLETED | Record Offline Payment completed | Reception Staff / System | Payment | Previous and new state |
| RECORD_OFFLINE_PAYMENT_REJECTED | Record Offline Payment rejected | System | Payment | Rejection reason |

### Reports Generated

- Billing & Payment Management Operational Report
- Billing & Payment Management History Report
- Billing & Payment Management Exception Report
- Executive Dashboard

### Related Screens

- Offline Payment
- Billing & Payment Management Dashboard
- Billing & Payment Management History
- Audit Log Viewer

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/payments/offline | POST | Authorized token | Execute Record Offline Payment | 200 OK or 201 Created with result |
| /api/v1/payments/offline/history | GET | Authorized token | Retrieve Record Offline Payment history | 200 OK with history |
| /api/v1/audit-logs | GET | Authorized token | Retrieve related audit events | 200 OK with scoped audit records |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Payment | Create / Update / Read | Support Record Offline Payment | Governed by Organization scope |
| Payment Transaction | Read / Insert | Support Record Offline Payment | Governed by Organization scope |
| Payment Receipt | Read / Insert | Support Record Offline Payment | Governed by Organization scope |
| Refund | Read / Insert | Support Record Offline Payment | Governed by Organization scope |
| Reconciliation | Read / Insert | Support Record Offline Payment | Governed by Organization scope |
| Audit Log | Insert | Record auditable activity | Immutable |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Draft | Record Offline Payment initiated | Validated | Reception Staff | Required data captured |
| Validated | Validation succeeds | Pending Approval | System | BA-02 rules satisfied |
| Pending Approval | Processing completes | Completed | System | Related updates succeed |
| Pending Approval | Approval or policy failure | Rejected | System / Approver | Request rejected |
| Completed | View history | Completed | Authorized user | Read-only historical access |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| BPM-010-001 | Record Offline Payment cannot be completed because required information is missing. | Missing mandatory data | Complete required fields |
| BPM-010-002 | You do not have permission to perform this action. | Authorization failure | Request access |
| BPM-010-003 | The selected record is not eligible for this action. | Policy or lifecycle violation | Review record status |
| BPM-010-004 | Record Offline Payment could not be completed due to a system or integration error. | Processing failure | Retry or contact support |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Execute Record Offline Payment | Given the actor has required permission and valid scope | When the actor submits valid information | Then the system shall complete Record Offline Payment successfully |
| Enforce validation | Given mandatory data or policy conditions are invalid | When the action is submitted | Then the system shall reject the request with a clear message |
| Preserve audit | Given the action completes or fails | When processing ends | Then audit events shall record actor, timestamp, scope, and outcome |
| Protect scope | Given the selected record is outside authorized scope | When the action is requested | Then the system shall deny access |

### Dependencies

- Customer Management
- Membership Management
- Walk-in Customer Management
- Personal Training
- Notification Management
- Reporting Service
- Audit Service

### Operational Considerations

Record Offline Payment should be designed for high-volume operational use, retry-safe processing, clear exception handling, and support-team diagnostics without exposing sensitive data.

### Non-Functional Considerations

This requirement shall satisfy Digitize non-functional expectations for availability, reliability, performance, scalability, security, configurability, maintainability, and auditability.

### Assumptions

- Required master data and configuration are maintained by authorized users.
- Related services expose stable APIs for validation and synchronization.
- Organization policies define approval, retention, notification, and exception behavior.

### Success Criteria

Record Offline Payment is completed accurately, securely, and audibly, with downstream records synchronized and no loss of historical traceability.

### Related Functional Requirements

- FR-BPM-001 - Generate Invoice
- FR-BPM-002 - Calculate Service Charges
- FR-BPM-003 - Apply Discounts
- FR-BPM-004 - Calculate Taxes
- FR-AUD-001 - Record Audit Events

### Notes

Record Offline Payment shall remain aligned with the approved BA source documents and shall not introduce behavior that bypasses tenant isolation, lifecycle governance, financial controls, or auditability.

---

## FR-BPM-011 - Verify Payment Status

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-BPM-011 |
| Requirement Name | Verify Payment Status |
| Functional Module | Billing & Payment Management |
| Business Domain | Billing & Payment |
| Business Capability | Payment Validation |
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
| Business Requirement | BA-08 BR-019 Payment Collection |
| Business Rule | BA-02 BR-PAY-001, BR-PAY-003, BR-PAY-005, BR-PAY-007 |
| Business Process | BA-03 BP-PAY-006 Verify Payment Status |
| Business Process Flow | BA-04 Section 24 Billing Management Flow, Section 25 Payment Management Flow, Section 26 Invoice Management Flow, Section 27 Refund Management Flow |
| Persona | BA-05 Finance Staff, Reception Staff, Customer, Organization Administrator |
| User Journey | BA-06 Section 19 Payment Journey |
| Stakeholder | BA-07 Finance Staff, Reception Staff, Customer |
| Non-Functional Requirement | BA-09 Section 3.7 Data Protection, Section 4.4 Financial Compliance, Section 11 Reporting Requirements |
| Assumption / Constraint / Risk | BA-10 BA-RSK-011, BA-RSK-012, BA-RSK-014 |

### Purpose

To enable Payment Validation within Billing & Payment Management so Digitize can execute Verify Payment Status consistently across Organizations, Facilities, Sites, users, and related operational or commercial services.

### Functional Requirement

The system shall support Verify Payment Status as an atomic Billing & Payment Management capability, including scoped data capture, business-rule validation, permission enforcement, lifecycle handling, related service synchronization, notification generation, reporting contribution, and immutable audit recording.

### Business Justification

Verify Payment Status is required to preserve operational control, revenue accuracy, service continuity, customer trust, and enterprise traceability for Billing & Payment processes. Without this capability, downstream modules would rely on incomplete, manual, or inconsistent records.

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
- Actor has permission for Verify Payment Status.
- Required Billing & Payment configuration and policies are available.
- Related records required by BA-03 BP-PAY-006 Verify Payment Status are available and within authorized scope.

### Trigger

The capability is triggered when System or the System initiates Verify Payment Status from Payment Status, a related workflow, a scheduled job, or an approved integration event.

### In Scope

- Capture or retrieve required Billing & Payment context.
- Validate Organization, Facility, Site, Customer, user, and policy scope where applicable.
- Execute Verify Payment Status according to approved business rules.
- Persist the resulting Payment state or transaction.
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
- Payment reference
- Customer reference, where applicable
- Effective date and time, where applicable
- Status or action reason, where applicable
- Payment, billing, trainer, session, or subscription reference where applicable
- Actor remarks, where applicable

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Payment ID | Primary business record reference | Identifier | Yes | System / User | Must exist or be generated within scope | Core reference for Verify Payment Status |
| Organization ID | Tenant Organization context | Identifier | Yes | Session / System | Must be Active and authorized | Enforces tenant isolation |
| Facility ID | Facility context | Identifier | Conditional | User / System | Must be Active where applicable | Required for facility-level operations |
| Site ID | Site context | Identifier | Conditional | User / System | Must belong to Facility where applicable | Required for site-level operations |
| Status | Lifecycle or processing state | Enum | Yes | System | Must follow allowed state transitions | Drives UI and downstream access |
| Effective Date | Date when action applies | DateTime | Conditional | User / System | Must satisfy policy | Supports scheduled or immediate actions |
| Reason / Remarks | Business explanation | Text | Conditional | User | Required for governed changes | Stored for audit |

### Main Flow

1. Actor opens Payment Status or the related workflow.
2. The system validates authentication, authorization, tenant scope, and current operating context.
3. The system loads the required Billing & Payment records, related configuration, and policy controls.
4. Actor enters or confirms the information required to verify payment status.
5. The system validates mandatory data, lifecycle status, ownership, eligibility, financial, capacity, schedule, and security rules where applicable.
6. The system executes Verify Payment Status and persists the resulting Payment state or transaction.
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

- Payment record created, updated, validated, or reported according to the action.
- Lifecycle or processing status updated.
- Related history entry created.
- Business events emitted.
- Notifications generated where configured.
- Audit events recorded.
- Reports or dashboards updated where applicable.

### UI Behaviour

Payment Status shall display scoped context, mandatory fields, lifecycle status, policy warnings, validation results, available actions, confirmation prompts, read-only states, pagination or filters where applicable, and responsive behavior for front-desk and administrative usage.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-BPM-011-001 | Actor must have permission to execute Verify Payment Status. | Deny request and audit. | Critical |
| VAL-BPM-011-002 | Record must belong to the authorized Organization scope. | Deny request. | Critical |
| VAL-BPM-011-003 | Mandatory inputs must be complete and valid. | Block submission. | Critical |
| VAL-BPM-011-004 | Lifecycle and policy rules from BA-02 must be satisfied. | Reject or route for approval. | High |
| VAL-BPM-011-005 | Historical and audit records must be preserved. | Roll back or mark for recovery. | Critical |

### Business Rules

- BA-02 BR-PAY-001
- BA-02 BR-PAY-003
- BA-02 BR-PAY-005
- BA-02 BR-PAY-007

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| bpm.verify.payment.status.view | System | Read | View Verify Payment Status context |
| bpm.verify.payment.status.execute | System | Execute | Execute Verify Payment Status |
| bpm.verify.payment.status.approve | Organization Administrator | Approve | Approve governed exceptions where configured |
| bpm.verify.payment.status.audit.view | Organization Administrator / Support Executive | Read | View audit trace |

### Security Considerations

The capability shall enforce authentication, role-based authorization, tenant isolation, Organization scope, Facility and Site access boundaries, sensitive data masking, secure references, and immutable audit logging.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Verify Payment Status Completed | Primary actor and configured stakeholders | In-App / Email | Action completes | Include reference, status, and effective date where applicable |
| Verify Payment Status Requires Approval | Approver | In-App | Approval rule applies | Include safe summary and requested action |
| Verify Payment Status Failed | Primary actor | In-App | Validation or processing fails | Include safe failure reason and next action |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| VerifyPaymentStatusRequested | Billing & Payment Management | Approval Workflow, Audit Service |
| VerifyPaymentStatusCompleted | Billing & Payment Management | Notification Service, Reporting Service, Audit Service |
| VerifyPaymentStatusRejected | Billing & Payment Management | Notification Service, Audit Service |

### Audit Events

| Audit Event | Description | Actor | Target Entity | Key Data |
|---|---|---|---|---|
| VERIFY_PAYMENT_STATUS_REQUESTED | Verify Payment Status requested | System | Payment | Scope, reference, and reason |
| VERIFY_PAYMENT_STATUS_COMPLETED | Verify Payment Status completed | System / System | Payment | Previous and new state |
| VERIFY_PAYMENT_STATUS_REJECTED | Verify Payment Status rejected | System | Payment | Rejection reason |

### Reports Generated

- Billing & Payment Management Operational Report
- Billing & Payment Management History Report
- Billing & Payment Management Exception Report
- Executive Dashboard

### Related Screens

- Payment Status
- Billing & Payment Management Dashboard
- Billing & Payment Management History
- Audit Log Viewer

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/payments/{paymentId}/status | GET | Authorized token | Execute Verify Payment Status | 200 OK or 201 Created with result |
| /api/v1/payments/{paymentId}/status/history | GET | Authorized token | Retrieve Verify Payment Status history | 200 OK with history |
| /api/v1/audit-logs | GET | Authorized token | Retrieve related audit events | 200 OK with scoped audit records |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Payment | Create / Update / Read | Support Verify Payment Status | Governed by Organization scope |
| Payment Transaction | Read / Insert | Support Verify Payment Status | Governed by Organization scope |
| Payment Receipt | Read / Insert | Support Verify Payment Status | Governed by Organization scope |
| Refund | Read / Insert | Support Verify Payment Status | Governed by Organization scope |
| Reconciliation | Read / Insert | Support Verify Payment Status | Governed by Organization scope |
| Audit Log | Insert | Record auditable activity | Immutable |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Requested | Verify Payment Status initiated | Eligible | System | Required data captured |
| Eligible | Validation succeeds | Requires Override | System | BA-02 rules satisfied |
| Requires Override | Processing completes | Denied | System | Related updates succeed |
| Requires Override | Approval or policy failure | Failed | System / Approver | Request rejected |
| Denied | View history | Denied | Authorized user | Read-only historical access |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| BPM-011-001 | Verify Payment Status cannot be completed because required information is missing. | Missing mandatory data | Complete required fields |
| BPM-011-002 | You do not have permission to perform this action. | Authorization failure | Request access |
| BPM-011-003 | The selected record is not eligible for this action. | Policy or lifecycle violation | Review record status |
| BPM-011-004 | Verify Payment Status could not be completed due to a system or integration error. | Processing failure | Retry or contact support |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Execute Verify Payment Status | Given the actor has required permission and valid scope | When the actor submits valid information | Then the system shall complete Verify Payment Status successfully |
| Enforce validation | Given mandatory data or policy conditions are invalid | When the action is submitted | Then the system shall reject the request with a clear message |
| Preserve audit | Given the action completes or fails | When processing ends | Then audit events shall record actor, timestamp, scope, and outcome |
| Protect scope | Given the selected record is outside authorized scope | When the action is requested | Then the system shall deny access |

### Dependencies

- Customer Management
- Membership Management
- Walk-in Customer Management
- Personal Training
- Notification Management
- Reporting Service
- Audit Service

### Operational Considerations

Verify Payment Status should be designed for high-volume operational use, retry-safe processing, clear exception handling, and support-team diagnostics without exposing sensitive data.

### Non-Functional Considerations

This requirement shall satisfy Digitize non-functional expectations for availability, reliability, performance, scalability, security, configurability, maintainability, and auditability.

### Assumptions

- Required master data and configuration are maintained by authorized users.
- Related services expose stable APIs for validation and synchronization.
- Organization policies define approval, retention, notification, and exception behavior.

### Success Criteria

Verify Payment Status is completed accurately, securely, and audibly, with downstream records synchronized and no loss of historical traceability.

### Related Functional Requirements

- FR-BPM-001 - Generate Invoice
- FR-BPM-002 - Calculate Service Charges
- FR-BPM-003 - Apply Discounts
- FR-BPM-004 - Calculate Taxes
- FR-AUD-001 - Record Audit Events

### Notes

Verify Payment Status shall remain aligned with the approved BA source documents and shall not introduce behavior that bypasses tenant isolation, lifecycle governance, financial controls, or auditability.

---

## FR-BPM-012 - Generate Payment Receipt

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-BPM-012 |
| Requirement Name | Generate Payment Receipt |
| Functional Module | Billing & Payment Management |
| Business Domain | Billing & Payment |
| Business Capability | Receipt Management |
| Requirement Type | Functional |
| Requirement Category | Transaction |
| Requirement Version | 1.0 |
| Requirement Status | Approved |
| Priority | Critical |
| Complexity | Medium |
| Release Version | 1.0 |
| Owner | Product Management |

### Traceability References

| Traceability Type | Reference |
|---|---|
| Business Requirement | BA-08 BR-019 Payment Collection |
| Business Rule | BA-02 BR-PAY-001, BR-PAY-003, BR-PAY-007 |
| Business Process | BA-03 BP-PAY-007 Generate Payment Receipt |
| Business Process Flow | BA-04 Section 24 Billing Management Flow, Section 25 Payment Management Flow, Section 26 Invoice Management Flow, Section 27 Refund Management Flow |
| Persona | BA-05 Finance Staff, Reception Staff, Customer, Organization Administrator |
| User Journey | BA-06 Section 19 Payment Journey |
| Stakeholder | BA-07 Finance Staff, Reception Staff, Customer |
| Non-Functional Requirement | BA-09 Section 3.7 Data Protection, Section 4.4 Financial Compliance, Section 11 Reporting Requirements |
| Assumption / Constraint / Risk | BA-10 BA-RSK-011, BA-RSK-012, BA-RSK-014 |

### Purpose

To enable Receipt Management within Billing & Payment Management so Digitize can execute Generate Payment Receipt consistently across Organizations, Facilities, Sites, users, and related operational or commercial services.

### Functional Requirement

The system shall support Generate Payment Receipt as an atomic Billing & Payment Management capability, including scoped data capture, business-rule validation, permission enforcement, lifecycle handling, related service synchronization, notification generation, reporting contribution, and immutable audit recording.

### Business Justification

Generate Payment Receipt is required to preserve operational control, revenue accuracy, service continuity, customer trust, and enterprise traceability for Billing & Payment processes. Without this capability, downstream modules would rely on incomplete, manual, or inconsistent records.

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
- Actor has permission for Generate Payment Receipt.
- Required Billing & Payment configuration and policies are available.
- Related records required by BA-03 BP-PAY-007 Generate Payment Receipt are available and within authorized scope.

### Trigger

The capability is triggered when System or the System initiates Generate Payment Receipt from Receipt View, a related workflow, a scheduled job, or an approved integration event.

### In Scope

- Capture or retrieve required Billing & Payment context.
- Validate Organization, Facility, Site, Customer, user, and policy scope where applicable.
- Execute Generate Payment Receipt according to approved business rules.
- Persist the resulting Payment state or transaction.
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
- Payment reference
- Customer reference, where applicable
- Effective date and time, where applicable
- Status or action reason, where applicable
- Payment, billing, trainer, session, or subscription reference where applicable
- Actor remarks, where applicable

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Payment ID | Primary business record reference | Identifier | Yes | System / User | Must exist or be generated within scope | Core reference for Generate Payment Receipt |
| Organization ID | Tenant Organization context | Identifier | Yes | Session / System | Must be Active and authorized | Enforces tenant isolation |
| Facility ID | Facility context | Identifier | Conditional | User / System | Must be Active where applicable | Required for facility-level operations |
| Site ID | Site context | Identifier | Conditional | User / System | Must belong to Facility where applicable | Required for site-level operations |
| Status | Lifecycle or processing state | Enum | Yes | System | Must follow allowed state transitions | Drives UI and downstream access |
| Effective Date | Date when action applies | DateTime | Conditional | User / System | Must satisfy policy | Supports scheduled or immediate actions |
| Reason / Remarks | Business explanation | Text | Conditional | User | Required for governed changes | Stored for audit |

### Main Flow

1. Actor opens Receipt View or the related workflow.
2. The system validates authentication, authorization, tenant scope, and current operating context.
3. The system loads the required Billing & Payment records, related configuration, and policy controls.
4. Actor enters or confirms the information required to generate payment receipt.
5. The system validates mandatory data, lifecycle status, ownership, eligibility, financial, capacity, schedule, and security rules where applicable.
6. The system executes Generate Payment Receipt and persists the resulting Payment state or transaction.
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

- Payment record created, updated, validated, or reported according to the action.
- Lifecycle or processing status updated.
- Related history entry created.
- Business events emitted.
- Notifications generated where configured.
- Audit events recorded.
- Reports or dashboards updated where applicable.

### UI Behaviour

Receipt View shall display scoped context, mandatory fields, lifecycle status, policy warnings, validation results, available actions, confirmation prompts, read-only states, pagination or filters where applicable, and responsive behavior for front-desk and administrative usage.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-BPM-012-001 | Actor must have permission to execute Generate Payment Receipt. | Deny request and audit. | Critical |
| VAL-BPM-012-002 | Record must belong to the authorized Organization scope. | Deny request. | Critical |
| VAL-BPM-012-003 | Mandatory inputs must be complete and valid. | Block submission. | Critical |
| VAL-BPM-012-004 | Lifecycle and policy rules from BA-02 must be satisfied. | Reject or route for approval. | High |
| VAL-BPM-012-005 | Historical and audit records must be preserved. | Roll back or mark for recovery. | Critical |

### Business Rules

- BA-02 BR-PAY-001
- BA-02 BR-PAY-003
- BA-02 BR-PAY-007

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| bpm.generate.payment.receipt.view | System | Read | View Generate Payment Receipt context |
| bpm.generate.payment.receipt.execute | System | Execute | Execute Generate Payment Receipt |
| bpm.generate.payment.receipt.approve | Organization Administrator | Approve | Approve governed exceptions where configured |
| bpm.generate.payment.receipt.audit.view | Organization Administrator / Support Executive | Read | View audit trace |

### Security Considerations

The capability shall enforce authentication, role-based authorization, tenant isolation, Organization scope, Facility and Site access boundaries, sensitive data masking, secure references, and immutable audit logging.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Generate Payment Receipt Completed | Primary actor and configured stakeholders | In-App / Email | Action completes | Include reference, status, and effective date where applicable |
| Generate Payment Receipt Requires Approval | Approver | In-App | Approval rule applies | Include safe summary and requested action |
| Generate Payment Receipt Failed | Primary actor | In-App | Validation or processing fails | Include safe failure reason and next action |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| GeneratePaymentReceiptRequested | Billing & Payment Management | Approval Workflow, Audit Service |
| GeneratePaymentReceiptCompleted | Billing & Payment Management | Notification Service, Reporting Service, Audit Service |
| GeneratePaymentReceiptRejected | Billing & Payment Management | Notification Service, Audit Service |

### Audit Events

| Audit Event | Description | Actor | Target Entity | Key Data |
|---|---|---|---|---|
| GENERATE_PAYMENT_RECEIPT_REQUESTED | Generate Payment Receipt requested | System | Payment | Scope, reference, and reason |
| GENERATE_PAYMENT_RECEIPT_COMPLETED | Generate Payment Receipt completed | System / System | Payment | Previous and new state |
| GENERATE_PAYMENT_RECEIPT_REJECTED | Generate Payment Receipt rejected | System | Payment | Rejection reason |

### Reports Generated

- Billing & Payment Management Operational Report
- Billing & Payment Management History Report
- Billing & Payment Management Exception Report
- Executive Dashboard

### Related Screens

- Receipt View
- Billing & Payment Management Dashboard
- Billing & Payment Management History
- Audit Log Viewer

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/receipts | POST | Authorized token | Execute Generate Payment Receipt | 200 OK or 201 Created with result |
| /api/v1/receipts/history | GET | Authorized token | Retrieve Generate Payment Receipt history | 200 OK with history |
| /api/v1/audit-logs | GET | Authorized token | Retrieve related audit events | 200 OK with scoped audit records |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Payment | Create / Update / Read | Support Generate Payment Receipt | Governed by Organization scope |
| Payment Transaction | Read / Insert | Support Generate Payment Receipt | Governed by Organization scope |
| Payment Receipt | Read / Insert | Support Generate Payment Receipt | Governed by Organization scope |
| Refund | Read / Insert | Support Generate Payment Receipt | Governed by Organization scope |
| Reconciliation | Read / Insert | Support Generate Payment Receipt | Governed by Organization scope |
| Audit Log | Insert | Record auditable activity | Immutable |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Draft | Generate Payment Receipt initiated | Validated | System | Required data captured |
| Validated | Validation succeeds | Pending Approval | System | BA-02 rules satisfied |
| Pending Approval | Processing completes | Completed | System | Related updates succeed |
| Pending Approval | Approval or policy failure | Rejected | System / Approver | Request rejected |
| Completed | View history | Completed | Authorized user | Read-only historical access |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| BPM-012-001 | Generate Payment Receipt cannot be completed because required information is missing. | Missing mandatory data | Complete required fields |
| BPM-012-002 | You do not have permission to perform this action. | Authorization failure | Request access |
| BPM-012-003 | The selected record is not eligible for this action. | Policy or lifecycle violation | Review record status |
| BPM-012-004 | Generate Payment Receipt could not be completed due to a system or integration error. | Processing failure | Retry or contact support |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Execute Generate Payment Receipt | Given the actor has required permission and valid scope | When the actor submits valid information | Then the system shall complete Generate Payment Receipt successfully |
| Enforce validation | Given mandatory data or policy conditions are invalid | When the action is submitted | Then the system shall reject the request with a clear message |
| Preserve audit | Given the action completes or fails | When processing ends | Then audit events shall record actor, timestamp, scope, and outcome |
| Protect scope | Given the selected record is outside authorized scope | When the action is requested | Then the system shall deny access |

### Dependencies

- Customer Management
- Membership Management
- Walk-in Customer Management
- Personal Training
- Notification Management
- Reporting Service
- Audit Service

### Operational Considerations

Generate Payment Receipt should be designed for high-volume operational use, retry-safe processing, clear exception handling, and support-team diagnostics without exposing sensitive data.

### Non-Functional Considerations

This requirement shall satisfy Digitize non-functional expectations for availability, reliability, performance, scalability, security, configurability, maintainability, and auditability.

### Assumptions

- Required master data and configuration are maintained by authorized users.
- Related services expose stable APIs for validation and synchronization.
- Organization policies define approval, retention, notification, and exception behavior.

### Success Criteria

Generate Payment Receipt is completed accurately, securely, and audibly, with downstream records synchronized and no loss of historical traceability.

### Related Functional Requirements

- FR-BPM-001 - Generate Invoice
- FR-BPM-002 - Calculate Service Charges
- FR-BPM-003 - Apply Discounts
- FR-BPM-004 - Calculate Taxes
- FR-AUD-001 - Record Audit Events

### Notes

Generate Payment Receipt shall remain aligned with the approved BA source documents and shall not introduce behavior that bypasses tenant isolation, lifecycle governance, financial controls, or auditability.

---

## FR-BPM-013 - Process Refund

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-BPM-013 |
| Requirement Name | Process Refund |
| Functional Module | Billing & Payment Management |
| Business Domain | Billing & Payment |
| Business Capability | Refund Management |
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
| Business Requirement | BA-08 BR-020 Refund Processing |
| Business Rule | BA-02 BR-PAY-006, BR-PAY-007, BR-PAY-008, BR-BIL-006 |
| Business Process | BA-03 BP-PAY-008 Process Refund |
| Business Process Flow | BA-04 Section 24 Billing Management Flow, Section 25 Payment Management Flow, Section 26 Invoice Management Flow, Section 27 Refund Management Flow |
| Persona | BA-05 Finance Staff, Reception Staff, Customer, Organization Administrator |
| User Journey | BA-06 Section 19 Payment Journey |
| Stakeholder | BA-07 Finance Staff, Reception Staff, Customer |
| Non-Functional Requirement | BA-09 Section 3.7 Data Protection, Section 4.4 Financial Compliance, Section 11 Reporting Requirements |
| Assumption / Constraint / Risk | BA-10 BA-RSK-011, BA-RSK-012, BA-RSK-014 |

### Purpose

To enable Refund Management within Billing & Payment Management so Digitize can execute Process Refund consistently across Organizations, Facilities, Sites, users, and related operational or commercial services.

### Functional Requirement

The system shall support Process Refund as an atomic Billing & Payment Management capability, including scoped data capture, business-rule validation, permission enforcement, lifecycle handling, related service synchronization, notification generation, reporting contribution, and immutable audit recording.

### Business Justification

Process Refund is required to preserve operational control, revenue accuracy, service continuity, customer trust, and enterprise traceability for Billing & Payment processes. Without this capability, downstream modules would rely on incomplete, manual, or inconsistent records.

### Actors

- Finance Staff
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
- Actor has permission for Process Refund.
- Required Billing & Payment configuration and policies are available.
- Related records required by BA-03 BP-PAY-008 Process Refund are available and within authorized scope.

### Trigger

The capability is triggered when Finance Staff or the System initiates Process Refund from Refund Management, a related workflow, a scheduled job, or an approved integration event.

### In Scope

- Capture or retrieve required Billing & Payment context.
- Validate Organization, Facility, Site, Customer, user, and policy scope where applicable.
- Execute Process Refund according to approved business rules.
- Persist the resulting Payment state or transaction.
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
- Payment reference
- Customer reference, where applicable
- Effective date and time, where applicable
- Status or action reason, where applicable
- Payment, billing, trainer, session, or subscription reference where applicable
- Actor remarks, where applicable

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Payment ID | Primary business record reference | Identifier | Yes | System / User | Must exist or be generated within scope | Core reference for Process Refund |
| Organization ID | Tenant Organization context | Identifier | Yes | Session / System | Must be Active and authorized | Enforces tenant isolation |
| Facility ID | Facility context | Identifier | Conditional | User / System | Must be Active where applicable | Required for facility-level operations |
| Site ID | Site context | Identifier | Conditional | User / System | Must belong to Facility where applicable | Required for site-level operations |
| Status | Lifecycle or processing state | Enum | Yes | System | Must follow allowed state transitions | Drives UI and downstream access |
| Effective Date | Date when action applies | DateTime | Conditional | User / System | Must satisfy policy | Supports scheduled or immediate actions |
| Reason / Remarks | Business explanation | Text | Conditional | User | Required for governed changes | Stored for audit |

### Main Flow

1. Actor opens Refund Management or the related workflow.
2. The system validates authentication, authorization, tenant scope, and current operating context.
3. The system loads the required Billing & Payment records, related configuration, and policy controls.
4. Actor enters or confirms the information required to process refund.
5. The system validates mandatory data, lifecycle status, ownership, eligibility, financial, capacity, schedule, and security rules where applicable.
6. The system executes Process Refund and persists the resulting Payment state or transaction.
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

- Payment record created, updated, validated, or reported according to the action.
- Lifecycle or processing status updated.
- Related history entry created.
- Business events emitted.
- Notifications generated where configured.
- Audit events recorded.
- Reports or dashboards updated where applicable.

### UI Behaviour

Refund Management shall display scoped context, mandatory fields, lifecycle status, policy warnings, validation results, available actions, confirmation prompts, read-only states, pagination or filters where applicable, and responsive behavior for front-desk and administrative usage.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-BPM-013-001 | Actor must have permission to execute Process Refund. | Deny request and audit. | Critical |
| VAL-BPM-013-002 | Record must belong to the authorized Organization scope. | Deny request. | Critical |
| VAL-BPM-013-003 | Mandatory inputs must be complete and valid. | Block submission. | Critical |
| VAL-BPM-013-004 | Lifecycle and policy rules from BA-02 must be satisfied. | Reject or route for approval. | High |
| VAL-BPM-013-005 | Historical and audit records must be preserved. | Roll back or mark for recovery. | Critical |

### Business Rules

- BA-02 BR-PAY-006
- BA-02 BR-PAY-007
- BA-02 BR-PAY-008
- BA-02 BR-BIL-006

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| bpm.process.refund.view | Finance Staff | Read | View Process Refund context |
| bpm.process.refund.execute | Finance Staff | Execute | Execute Process Refund |
| bpm.process.refund.approve | Organization Administrator | Approve | Approve governed exceptions where configured |
| bpm.process.refund.audit.view | Organization Administrator / Support Executive | Read | View audit trace |

### Security Considerations

The capability shall enforce authentication, role-based authorization, tenant isolation, Organization scope, Facility and Site access boundaries, sensitive data masking, secure references, and immutable audit logging.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Process Refund Completed | Primary actor and configured stakeholders | In-App / Email | Action completes | Include reference, status, and effective date where applicable |
| Process Refund Requires Approval | Approver | In-App | Approval rule applies | Include safe summary and requested action |
| Process Refund Failed | Primary actor | In-App | Validation or processing fails | Include safe failure reason and next action |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| ProcessRefundRequested | Billing & Payment Management | Approval Workflow, Audit Service |
| ProcessRefundCompleted | Billing & Payment Management | Notification Service, Reporting Service, Audit Service |
| ProcessRefundRejected | Billing & Payment Management | Notification Service, Audit Service |

### Audit Events

| Audit Event | Description | Actor | Target Entity | Key Data |
|---|---|---|---|---|
| PROCESS_REFUND_REQUESTED | Process Refund requested | Finance Staff | Payment | Scope, reference, and reason |
| PROCESS_REFUND_COMPLETED | Process Refund completed | Finance Staff / System | Payment | Previous and new state |
| PROCESS_REFUND_REJECTED | Process Refund rejected | System | Payment | Rejection reason |

### Reports Generated

- Billing & Payment Management Operational Report
- Billing & Payment Management History Report
- Billing & Payment Management Exception Report
- Executive Dashboard

### Related Screens

- Refund Management
- Billing & Payment Management Dashboard
- Billing & Payment Management History
- Audit Log Viewer

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/refunds | POST | Authorized token | Execute Process Refund | 200 OK or 201 Created with result |
| /api/v1/refunds/history | GET | Authorized token | Retrieve Process Refund history | 200 OK with history |
| /api/v1/audit-logs | GET | Authorized token | Retrieve related audit events | 200 OK with scoped audit records |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Payment | Create / Update / Read | Support Process Refund | Governed by Organization scope |
| Payment Transaction | Read / Insert | Support Process Refund | Governed by Organization scope |
| Payment Receipt | Read / Insert | Support Process Refund | Governed by Organization scope |
| Refund | Read / Insert | Support Process Refund | Governed by Organization scope |
| Reconciliation | Read / Insert | Support Process Refund | Governed by Organization scope |
| Audit Log | Insert | Record auditable activity | Immutable |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Draft | Process Refund initiated | Validated | Finance Staff | Required data captured |
| Validated | Validation succeeds | Pending Approval | System | BA-02 rules satisfied |
| Pending Approval | Processing completes | Completed | System | Related updates succeed |
| Pending Approval | Approval or policy failure | Rejected | System / Approver | Request rejected |
| Completed | View history | Completed | Authorized user | Read-only historical access |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| BPM-013-001 | Process Refund cannot be completed because required information is missing. | Missing mandatory data | Complete required fields |
| BPM-013-002 | You do not have permission to perform this action. | Authorization failure | Request access |
| BPM-013-003 | The selected record is not eligible for this action. | Policy or lifecycle violation | Review record status |
| BPM-013-004 | Process Refund could not be completed due to a system or integration error. | Processing failure | Retry or contact support |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Execute Process Refund | Given the actor has required permission and valid scope | When the actor submits valid information | Then the system shall complete Process Refund successfully |
| Enforce validation | Given mandatory data or policy conditions are invalid | When the action is submitted | Then the system shall reject the request with a clear message |
| Preserve audit | Given the action completes or fails | When processing ends | Then audit events shall record actor, timestamp, scope, and outcome |
| Protect scope | Given the selected record is outside authorized scope | When the action is requested | Then the system shall deny access |

### Dependencies

- Customer Management
- Membership Management
- Walk-in Customer Management
- Personal Training
- Notification Management
- Reporting Service
- Audit Service

### Operational Considerations

Process Refund should be designed for high-volume operational use, retry-safe processing, clear exception handling, and support-team diagnostics without exposing sensitive data.

### Non-Functional Considerations

This requirement shall satisfy Digitize non-functional expectations for availability, reliability, performance, scalability, security, configurability, maintainability, and auditability.

### Assumptions

- Required master data and configuration are maintained by authorized users.
- Related services expose stable APIs for validation and synchronization.
- Organization policies define approval, retention, notification, and exception behavior.

### Success Criteria

Process Refund is completed accurately, securely, and audibly, with downstream records synchronized and no loss of historical traceability.

### Related Functional Requirements

- FR-BPM-001 - Generate Invoice
- FR-BPM-002 - Calculate Service Charges
- FR-BPM-003 - Apply Discounts
- FR-BPM-004 - Calculate Taxes
- FR-AUD-001 - Record Audit Events

### Notes

Process Refund shall remain aligned with the approved BA source documents and shall not introduce behavior that bypasses tenant isolation, lifecycle governance, financial controls, or auditability.

---

## FR-BPM-014 - Reconcile Payment

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-BPM-014 |
| Requirement Name | Reconcile Payment |
| Functional Module | Billing & Payment Management |
| Business Domain | Billing & Payment |
| Business Capability | Financial Reconciliation |
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
| Business Requirement | BA-08 BR-019 Payment Collection |
| Business Rule | BA-02 BR-PAY-007, BR-PAY-008, BR-BIL-008 |
| Business Process | BA-03 BP-PAY-009 Reconcile Payment |
| Business Process Flow | BA-04 Section 24 Billing Management Flow, Section 25 Payment Management Flow, Section 26 Invoice Management Flow, Section 27 Refund Management Flow |
| Persona | BA-05 Finance Staff, Reception Staff, Customer, Organization Administrator |
| User Journey | BA-06 Section 19 Payment Journey |
| Stakeholder | BA-07 Finance Staff, Reception Staff, Customer |
| Non-Functional Requirement | BA-09 Section 3.7 Data Protection, Section 4.4 Financial Compliance, Section 11 Reporting Requirements |
| Assumption / Constraint / Risk | BA-10 BA-RSK-011, BA-RSK-012, BA-RSK-014 |

### Purpose

To enable Financial Reconciliation within Billing & Payment Management so Digitize can execute Reconcile Payment consistently across Organizations, Facilities, Sites, users, and related operational or commercial services.

### Functional Requirement

The system shall support Reconcile Payment as an atomic Billing & Payment Management capability, including scoped data capture, business-rule validation, permission enforcement, lifecycle handling, related service synchronization, notification generation, reporting contribution, and immutable audit recording.

### Business Justification

Reconcile Payment is required to preserve operational control, revenue accuracy, service continuity, customer trust, and enterprise traceability for Billing & Payment processes. Without this capability, downstream modules would rely on incomplete, manual, or inconsistent records.

### Actors

- Finance Staff
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
- Actor has permission for Reconcile Payment.
- Required Billing & Payment configuration and policies are available.
- Related records required by BA-03 BP-PAY-009 Reconcile Payment are available and within authorized scope.

### Trigger

The capability is triggered when Finance Staff or the System initiates Reconcile Payment from Payment Reconciliation, a related workflow, a scheduled job, or an approved integration event.

### In Scope

- Capture or retrieve required Billing & Payment context.
- Validate Organization, Facility, Site, Customer, user, and policy scope where applicable.
- Execute Reconcile Payment according to approved business rules.
- Persist the resulting Payment state or transaction.
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
- Payment reference
- Customer reference, where applicable
- Effective date and time, where applicable
- Status or action reason, where applicable
- Payment, billing, trainer, session, or subscription reference where applicable
- Actor remarks, where applicable

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Payment ID | Primary business record reference | Identifier | Yes | System / User | Must exist or be generated within scope | Core reference for Reconcile Payment |
| Organization ID | Tenant Organization context | Identifier | Yes | Session / System | Must be Active and authorized | Enforces tenant isolation |
| Facility ID | Facility context | Identifier | Conditional | User / System | Must be Active where applicable | Required for facility-level operations |
| Site ID | Site context | Identifier | Conditional | User / System | Must belong to Facility where applicable | Required for site-level operations |
| Status | Lifecycle or processing state | Enum | Yes | System | Must follow allowed state transitions | Drives UI and downstream access |
| Effective Date | Date when action applies | DateTime | Conditional | User / System | Must satisfy policy | Supports scheduled or immediate actions |
| Reason / Remarks | Business explanation | Text | Conditional | User | Required for governed changes | Stored for audit |

### Main Flow

1. Actor opens Payment Reconciliation or the related workflow.
2. The system validates authentication, authorization, tenant scope, and current operating context.
3. The system loads the required Billing & Payment records, related configuration, and policy controls.
4. Actor enters or confirms the information required to reconcile payment.
5. The system validates mandatory data, lifecycle status, ownership, eligibility, financial, capacity, schedule, and security rules where applicable.
6. The system executes Reconcile Payment and persists the resulting Payment state or transaction.
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

- Payment record created, updated, validated, or reported according to the action.
- Lifecycle or processing status updated.
- Related history entry created.
- Business events emitted.
- Notifications generated where configured.
- Audit events recorded.
- Reports or dashboards updated where applicable.

### UI Behaviour

Payment Reconciliation shall display scoped context, mandatory fields, lifecycle status, policy warnings, validation results, available actions, confirmation prompts, read-only states, pagination or filters where applicable, and responsive behavior for front-desk and administrative usage.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-BPM-014-001 | Actor must have permission to execute Reconcile Payment. | Deny request and audit. | Critical |
| VAL-BPM-014-002 | Record must belong to the authorized Organization scope. | Deny request. | Critical |
| VAL-BPM-014-003 | Mandatory inputs must be complete and valid. | Block submission. | Critical |
| VAL-BPM-014-004 | Lifecycle and policy rules from BA-02 must be satisfied. | Reject or route for approval. | High |
| VAL-BPM-014-005 | Historical and audit records must be preserved. | Roll back or mark for recovery. | Critical |

### Business Rules

- BA-02 BR-PAY-007
- BA-02 BR-PAY-008
- BA-02 BR-BIL-008

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| bpm.reconcile.payment.view | Finance Staff | Read | View Reconcile Payment context |
| bpm.reconcile.payment.execute | Finance Staff | Execute | Execute Reconcile Payment |
| bpm.reconcile.payment.approve | Organization Administrator | Approve | Approve governed exceptions where configured |
| bpm.reconcile.payment.audit.view | Organization Administrator / Support Executive | Read | View audit trace |

### Security Considerations

The capability shall enforce authentication, role-based authorization, tenant isolation, Organization scope, Facility and Site access boundaries, sensitive data masking, secure references, and immutable audit logging.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Reconcile Payment Completed | Primary actor and configured stakeholders | In-App / Email | Action completes | Include reference, status, and effective date where applicable |
| Reconcile Payment Requires Approval | Approver | In-App | Approval rule applies | Include safe summary and requested action |
| Reconcile Payment Failed | Primary actor | In-App | Validation or processing fails | Include safe failure reason and next action |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| ReconcilePaymentRequested | Billing & Payment Management | Approval Workflow, Audit Service |
| ReconcilePaymentCompleted | Billing & Payment Management | Notification Service, Reporting Service, Audit Service |
| ReconcilePaymentRejected | Billing & Payment Management | Notification Service, Audit Service |

### Audit Events

| Audit Event | Description | Actor | Target Entity | Key Data |
|---|---|---|---|---|
| RECONCILE_PAYMENT_REQUESTED | Reconcile Payment requested | Finance Staff | Payment | Scope, reference, and reason |
| RECONCILE_PAYMENT_COMPLETED | Reconcile Payment completed | Finance Staff / System | Payment | Previous and new state |
| RECONCILE_PAYMENT_REJECTED | Reconcile Payment rejected | System | Payment | Rejection reason |

### Reports Generated

- Billing & Payment Management Operational Report
- Billing & Payment Management History Report
- Billing & Payment Management Exception Report
- Executive Dashboard

### Related Screens

- Payment Reconciliation
- Billing & Payment Management Dashboard
- Billing & Payment Management History
- Audit Log Viewer

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/payments/reconciliation | POST | Authorized token | Execute Reconcile Payment | 200 OK or 201 Created with result |
| /api/v1/payments/reconciliation/history | GET | Authorized token | Retrieve Reconcile Payment history | 200 OK with history |
| /api/v1/audit-logs | GET | Authorized token | Retrieve related audit events | 200 OK with scoped audit records |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Payment | Create / Update / Read | Support Reconcile Payment | Governed by Organization scope |
| Payment Transaction | Read / Insert | Support Reconcile Payment | Governed by Organization scope |
| Payment Receipt | Read / Insert | Support Reconcile Payment | Governed by Organization scope |
| Refund | Read / Insert | Support Reconcile Payment | Governed by Organization scope |
| Reconciliation | Read / Insert | Support Reconcile Payment | Governed by Organization scope |
| Audit Log | Insert | Record auditable activity | Immutable |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Draft | Reconcile Payment initiated | Validated | Finance Staff | Required data captured |
| Validated | Validation succeeds | Pending Approval | System | BA-02 rules satisfied |
| Pending Approval | Processing completes | Completed | System | Related updates succeed |
| Pending Approval | Approval or policy failure | Rejected | System / Approver | Request rejected |
| Completed | View history | Completed | Authorized user | Read-only historical access |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| BPM-014-001 | Reconcile Payment cannot be completed because required information is missing. | Missing mandatory data | Complete required fields |
| BPM-014-002 | You do not have permission to perform this action. | Authorization failure | Request access |
| BPM-014-003 | The selected record is not eligible for this action. | Policy or lifecycle violation | Review record status |
| BPM-014-004 | Reconcile Payment could not be completed due to a system or integration error. | Processing failure | Retry or contact support |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Execute Reconcile Payment | Given the actor has required permission and valid scope | When the actor submits valid information | Then the system shall complete Reconcile Payment successfully |
| Enforce validation | Given mandatory data or policy conditions are invalid | When the action is submitted | Then the system shall reject the request with a clear message |
| Preserve audit | Given the action completes or fails | When processing ends | Then audit events shall record actor, timestamp, scope, and outcome |
| Protect scope | Given the selected record is outside authorized scope | When the action is requested | Then the system shall deny access |

### Dependencies

- Customer Management
- Membership Management
- Walk-in Customer Management
- Personal Training
- Notification Management
- Reporting Service
- Audit Service

### Operational Considerations

Reconcile Payment should be designed for high-volume operational use, retry-safe processing, clear exception handling, and support-team diagnostics without exposing sensitive data.

### Non-Functional Considerations

This requirement shall satisfy Digitize non-functional expectations for availability, reliability, performance, scalability, security, configurability, maintainability, and auditability.

### Assumptions

- Required master data and configuration are maintained by authorized users.
- Related services expose stable APIs for validation and synchronization.
- Organization policies define approval, retention, notification, and exception behavior.

### Success Criteria

Reconcile Payment is completed accurately, securely, and audibly, with downstream records synchronized and no loss of historical traceability.

### Related Functional Requirements

- FR-BPM-001 - Generate Invoice
- FR-BPM-002 - Calculate Service Charges
- FR-BPM-003 - Apply Discounts
- FR-BPM-004 - Calculate Taxes
- FR-AUD-001 - Record Audit Events

### Notes

Reconcile Payment shall remain aligned with the approved BA source documents and shall not introduce behavior that bypasses tenant isolation, lifecycle governance, financial controls, or auditability.

---

## FR-BPM-015 - Cancel Payment

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-BPM-015 |
| Requirement Name | Cancel Payment |
| Functional Module | Billing & Payment Management |
| Business Domain | Billing & Payment |
| Business Capability | Payment Administration |
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
| Business Requirement | BA-08 BR-019 Payment Collection |
| Business Rule | BA-02 BR-PAY-005, BR-PAY-007, BR-PAY-008 |
| Business Process | BA-03 BP-PAY-010 Cancel Payment |
| Business Process Flow | BA-04 Section 24 Billing Management Flow, Section 25 Payment Management Flow, Section 26 Invoice Management Flow, Section 27 Refund Management Flow |
| Persona | BA-05 Finance Staff, Reception Staff, Customer, Organization Administrator |
| User Journey | BA-06 Section 19 Payment Journey |
| Stakeholder | BA-07 Finance Staff, Reception Staff, Customer |
| Non-Functional Requirement | BA-09 Section 3.7 Data Protection, Section 4.4 Financial Compliance, Section 11 Reporting Requirements |
| Assumption / Constraint / Risk | BA-10 BA-RSK-011, BA-RSK-012, BA-RSK-014 |

### Purpose

To enable Payment Administration within Billing & Payment Management so Digitize can execute Cancel Payment consistently across Organizations, Facilities, Sites, users, and related operational or commercial services.

### Functional Requirement

The system shall support Cancel Payment as an atomic Billing & Payment Management capability, including scoped data capture, business-rule validation, permission enforcement, lifecycle handling, related service synchronization, notification generation, reporting contribution, and immutable audit recording.

### Business Justification

Cancel Payment is required to preserve operational control, revenue accuracy, service continuity, customer trust, and enterprise traceability for Billing & Payment processes. Without this capability, downstream modules would rely on incomplete, manual, or inconsistent records.

### Actors

- Finance Staff
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
- Actor has permission for Cancel Payment.
- Required Billing & Payment configuration and policies are available.
- Related records required by BA-03 BP-PAY-010 Cancel Payment are available and within authorized scope.

### Trigger

The capability is triggered when Finance Staff or the System initiates Cancel Payment from Payment Cancellation, a related workflow, a scheduled job, or an approved integration event.

### In Scope

- Capture or retrieve required Billing & Payment context.
- Validate Organization, Facility, Site, Customer, user, and policy scope where applicable.
- Execute Cancel Payment according to approved business rules.
- Persist the resulting Payment state or transaction.
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
- Payment reference
- Customer reference, where applicable
- Effective date and time, where applicable
- Status or action reason, where applicable
- Payment, billing, trainer, session, or subscription reference where applicable
- Actor remarks, where applicable

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Payment ID | Primary business record reference | Identifier | Yes | System / User | Must exist or be generated within scope | Core reference for Cancel Payment |
| Organization ID | Tenant Organization context | Identifier | Yes | Session / System | Must be Active and authorized | Enforces tenant isolation |
| Facility ID | Facility context | Identifier | Conditional | User / System | Must be Active where applicable | Required for facility-level operations |
| Site ID | Site context | Identifier | Conditional | User / System | Must belong to Facility where applicable | Required for site-level operations |
| Status | Lifecycle or processing state | Enum | Yes | System | Must follow allowed state transitions | Drives UI and downstream access |
| Effective Date | Date when action applies | DateTime | Conditional | User / System | Must satisfy policy | Supports scheduled or immediate actions |
| Reason / Remarks | Business explanation | Text | Conditional | User | Required for governed changes | Stored for audit |

### Main Flow

1. Actor opens Payment Cancellation or the related workflow.
2. The system validates authentication, authorization, tenant scope, and current operating context.
3. The system loads the required Billing & Payment records, related configuration, and policy controls.
4. Actor enters or confirms the information required to cancel payment.
5. The system validates mandatory data, lifecycle status, ownership, eligibility, financial, capacity, schedule, and security rules where applicable.
6. The system executes Cancel Payment and persists the resulting Payment state or transaction.
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

- Payment record created, updated, validated, or reported according to the action.
- Lifecycle or processing status updated.
- Related history entry created.
- Business events emitted.
- Notifications generated where configured.
- Audit events recorded.
- Reports or dashboards updated where applicable.

### UI Behaviour

Payment Cancellation shall display scoped context, mandatory fields, lifecycle status, policy warnings, validation results, available actions, confirmation prompts, read-only states, pagination or filters where applicable, and responsive behavior for front-desk and administrative usage.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-BPM-015-001 | Actor must have permission to execute Cancel Payment. | Deny request and audit. | Critical |
| VAL-BPM-015-002 | Record must belong to the authorized Organization scope. | Deny request. | Critical |
| VAL-BPM-015-003 | Mandatory inputs must be complete and valid. | Block submission. | Critical |
| VAL-BPM-015-004 | Lifecycle and policy rules from BA-02 must be satisfied. | Reject or route for approval. | High |
| VAL-BPM-015-005 | Historical and audit records must be preserved. | Roll back or mark for recovery. | Critical |

### Business Rules

- BA-02 BR-PAY-005
- BA-02 BR-PAY-007
- BA-02 BR-PAY-008

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| bpm.cancel.payment.view | Finance Staff | Read | View Cancel Payment context |
| bpm.cancel.payment.execute | Finance Staff | Execute | Execute Cancel Payment |
| bpm.cancel.payment.approve | Organization Administrator | Approve | Approve governed exceptions where configured |
| bpm.cancel.payment.audit.view | Organization Administrator / Support Executive | Read | View audit trace |

### Security Considerations

The capability shall enforce authentication, role-based authorization, tenant isolation, Organization scope, Facility and Site access boundaries, sensitive data masking, secure references, and immutable audit logging.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Cancel Payment Completed | Primary actor and configured stakeholders | In-App / Email | Action completes | Include reference, status, and effective date where applicable |
| Cancel Payment Requires Approval | Approver | In-App | Approval rule applies | Include safe summary and requested action |
| Cancel Payment Failed | Primary actor | In-App | Validation or processing fails | Include safe failure reason and next action |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| CancelPaymentRequested | Billing & Payment Management | Approval Workflow, Audit Service |
| CancelPaymentCompleted | Billing & Payment Management | Notification Service, Reporting Service, Audit Service |
| CancelPaymentRejected | Billing & Payment Management | Notification Service, Audit Service |

### Audit Events

| Audit Event | Description | Actor | Target Entity | Key Data |
|---|---|---|---|---|
| CANCEL_PAYMENT_REQUESTED | Cancel Payment requested | Finance Staff | Payment | Scope, reference, and reason |
| CANCEL_PAYMENT_COMPLETED | Cancel Payment completed | Finance Staff / System | Payment | Previous and new state |
| CANCEL_PAYMENT_REJECTED | Cancel Payment rejected | System | Payment | Rejection reason |

### Reports Generated

- Billing & Payment Management Operational Report
- Billing & Payment Management History Report
- Billing & Payment Management Exception Report
- Executive Dashboard

### Related Screens

- Payment Cancellation
- Billing & Payment Management Dashboard
- Billing & Payment Management History
- Audit Log Viewer

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/payments/{paymentId}/cancel | POST | Authorized token | Execute Cancel Payment | 200 OK or 201 Created with result |
| /api/v1/payments/{paymentId}/cancel/history | GET | Authorized token | Retrieve Cancel Payment history | 200 OK with history |
| /api/v1/audit-logs | GET | Authorized token | Retrieve related audit events | 200 OK with scoped audit records |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Payment | Create / Update / Read | Support Cancel Payment | Governed by Organization scope |
| Payment Transaction | Read / Insert | Support Cancel Payment | Governed by Organization scope |
| Payment Receipt | Read / Insert | Support Cancel Payment | Governed by Organization scope |
| Refund | Read / Insert | Support Cancel Payment | Governed by Organization scope |
| Reconciliation | Read / Insert | Support Cancel Payment | Governed by Organization scope |
| Audit Log | Insert | Record auditable activity | Immutable |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Draft | Cancel Payment initiated | Validated | Finance Staff | Required data captured |
| Validated | Validation succeeds | Pending Approval | System | BA-02 rules satisfied |
| Pending Approval | Processing completes | Completed | System | Related updates succeed |
| Pending Approval | Approval or policy failure | Rejected | System / Approver | Request rejected |
| Completed | View history | Completed | Authorized user | Read-only historical access |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| BPM-015-001 | Cancel Payment cannot be completed because required information is missing. | Missing mandatory data | Complete required fields |
| BPM-015-002 | You do not have permission to perform this action. | Authorization failure | Request access |
| BPM-015-003 | The selected record is not eligible for this action. | Policy or lifecycle violation | Review record status |
| BPM-015-004 | Cancel Payment could not be completed due to a system or integration error. | Processing failure | Retry or contact support |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Execute Cancel Payment | Given the actor has required permission and valid scope | When the actor submits valid information | Then the system shall complete Cancel Payment successfully |
| Enforce validation | Given mandatory data or policy conditions are invalid | When the action is submitted | Then the system shall reject the request with a clear message |
| Preserve audit | Given the action completes or fails | When processing ends | Then audit events shall record actor, timestamp, scope, and outcome |
| Protect scope | Given the selected record is outside authorized scope | When the action is requested | Then the system shall deny access |

### Dependencies

- Customer Management
- Membership Management
- Walk-in Customer Management
- Personal Training
- Notification Management
- Reporting Service
- Audit Service

### Operational Considerations

Cancel Payment should be designed for high-volume operational use, retry-safe processing, clear exception handling, and support-team diagnostics without exposing sensitive data.

### Non-Functional Considerations

This requirement shall satisfy Digitize non-functional expectations for availability, reliability, performance, scalability, security, configurability, maintainability, and auditability.

### Assumptions

- Required master data and configuration are maintained by authorized users.
- Related services expose stable APIs for validation and synchronization.
- Organization policies define approval, retention, notification, and exception behavior.

### Success Criteria

Cancel Payment is completed accurately, securely, and audibly, with downstream records synchronized and no loss of historical traceability.

### Related Functional Requirements

- FR-BPM-001 - Generate Invoice
- FR-BPM-002 - Calculate Service Charges
- FR-BPM-003 - Apply Discounts
- FR-BPM-004 - Calculate Taxes
- FR-AUD-001 - Record Audit Events

### Notes

Cancel Payment shall remain aligned with the approved BA source documents and shall not introduce behavior that bypasses tenant isolation, lifecycle governance, financial controls, or auditability.

---

## FR-BPM-016 - View Billing and Payment History

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-BPM-016 |
| Requirement Name | View Billing and Payment History |
| Functional Module | Billing & Payment Management |
| Business Domain | Billing & Payment |
| Business Capability | Commercial Monitoring |
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
| Business Requirement | BA-08 BR-018, BR-019 |
| Business Rule | BA-02 BR-BIL-008, BR-PAY-007, BR-PAY-008, BR-SEC-004 |
| Business Process | BA-03 BP-BIL-010 View Billing History, BP-PAY-011 View Payment History |
| Business Process Flow | BA-04 Section 24 Billing Management Flow, Section 25 Payment Management Flow, Section 26 Invoice Management Flow, Section 27 Refund Management Flow |
| Persona | BA-05 Finance Staff, Reception Staff, Customer, Organization Administrator |
| User Journey | BA-06 Section 19 Payment Journey |
| Stakeholder | BA-07 Finance Staff, Reception Staff, Customer |
| Non-Functional Requirement | BA-09 Section 3.7 Data Protection, Section 4.4 Financial Compliance, Section 11 Reporting Requirements |
| Assumption / Constraint / Risk | BA-10 BA-RSK-011, BA-RSK-012, BA-RSK-014 |

### Purpose

To enable Commercial Monitoring within Billing & Payment Management so Digitize can execute View Billing and Payment History consistently across Organizations, Facilities, Sites, users, and related operational or commercial services.

### Functional Requirement

The system shall support View Billing and Payment History as an atomic Billing & Payment Management capability, including scoped data capture, business-rule validation, permission enforcement, lifecycle handling, related service synchronization, notification generation, reporting contribution, and immutable audit recording.

### Business Justification

View Billing and Payment History is required to preserve operational control, revenue accuracy, service continuity, customer trust, and enterprise traceability for Billing & Payment processes. Without this capability, downstream modules would rely on incomplete, manual, or inconsistent records.

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
- Actor has permission for View Billing and Payment History.
- Required Billing & Payment configuration and policies are available.
- Related records required by BA-03 BP-BIL-010 View Billing History, BP-PAY-011 View Payment History are available and within authorized scope.

### Trigger

The capability is triggered when Reception Staff or the System initiates View Billing and Payment History from Billing and Payment History, a related workflow, a scheduled job, or an approved integration event.

### In Scope

- Capture or retrieve required Billing & Payment context.
- Validate Organization, Facility, Site, Customer, user, and policy scope where applicable.
- Execute View Billing and Payment History according to approved business rules.
- Persist the resulting Payment state or transaction.
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
- Payment reference
- Customer reference, where applicable
- Effective date and time, where applicable
- Status or action reason, where applicable
- Payment, billing, trainer, session, or subscription reference where applicable
- Actor remarks, where applicable

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Payment ID | Primary business record reference | Identifier | Yes | System / User | Must exist or be generated within scope | Core reference for View Billing and Payment History |
| Organization ID | Tenant Organization context | Identifier | Yes | Session / System | Must be Active and authorized | Enforces tenant isolation |
| Facility ID | Facility context | Identifier | Conditional | User / System | Must be Active where applicable | Required for facility-level operations |
| Site ID | Site context | Identifier | Conditional | User / System | Must belong to Facility where applicable | Required for site-level operations |
| Status | Lifecycle or processing state | Enum | Yes | System | Must follow allowed state transitions | Drives UI and downstream access |
| Effective Date | Date when action applies | DateTime | Conditional | User / System | Must satisfy policy | Supports scheduled or immediate actions |
| Reason / Remarks | Business explanation | Text | Conditional | User | Required for governed changes | Stored for audit |

### Main Flow

1. Actor opens Billing and Payment History or the related workflow.
2. The system validates authentication, authorization, tenant scope, and current operating context.
3. The system loads the required Billing & Payment records, related configuration, and policy controls.
4. Actor enters or confirms the information required to view billing and payment history.
5. The system validates mandatory data, lifecycle status, ownership, eligibility, financial, capacity, schedule, and security rules where applicable.
6. The system executes View Billing and Payment History and persists the resulting Payment state or transaction.
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

- Payment record created, updated, validated, or reported according to the action.
- Lifecycle or processing status updated.
- Related history entry created.
- Business events emitted.
- Notifications generated where configured.
- Audit events recorded.
- Reports or dashboards updated where applicable.

### UI Behaviour

Billing and Payment History shall display scoped context, mandatory fields, lifecycle status, policy warnings, validation results, available actions, confirmation prompts, read-only states, pagination or filters where applicable, and responsive behavior for front-desk and administrative usage.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-BPM-016-001 | Actor must have permission to execute View Billing and Payment History. | Deny request and audit. | Critical |
| VAL-BPM-016-002 | Record must belong to the authorized Organization scope. | Deny request. | Critical |
| VAL-BPM-016-003 | Mandatory inputs must be complete and valid. | Block submission. | Critical |
| VAL-BPM-016-004 | Lifecycle and policy rules from BA-02 must be satisfied. | Reject or route for approval. | High |
| VAL-BPM-016-005 | Historical and audit records must be preserved. | Roll back or mark for recovery. | Critical |

### Business Rules

- BA-02 BR-BIL-008
- BA-02 BR-PAY-007
- BA-02 BR-PAY-008
- BA-02 BR-SEC-004

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| bpm.view.billing.and.payment.history.view | Reception Staff | Read | View View Billing and Payment History context |
| bpm.view.billing.and.payment.history.execute | Reception Staff | Execute | Execute View Billing and Payment History |
| bpm.view.billing.and.payment.history.approve | Organization Administrator | Approve | Approve governed exceptions where configured |
| bpm.view.billing.and.payment.history.audit.view | Organization Administrator / Support Executive | Read | View audit trace |

### Security Considerations

The capability shall enforce authentication, role-based authorization, tenant isolation, Organization scope, Facility and Site access boundaries, sensitive data masking, secure references, and immutable audit logging.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| View Billing and Payment History Completed | Primary actor and configured stakeholders | In-App / Email | Action completes | Include reference, status, and effective date where applicable |
| View Billing and Payment History Requires Approval | Approver | In-App | Approval rule applies | Include safe summary and requested action |
| View Billing and Payment History Failed | Primary actor | In-App | Validation or processing fails | Include safe failure reason and next action |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| ViewBillingAndPaymentHistoryRequested | Billing & Payment Management | Approval Workflow, Audit Service |
| ViewBillingAndPaymentHistoryCompleted | Billing & Payment Management | Notification Service, Reporting Service, Audit Service |
| ViewBillingAndPaymentHistoryRejected | Billing & Payment Management | Notification Service, Audit Service |

### Audit Events

| Audit Event | Description | Actor | Target Entity | Key Data |
|---|---|---|---|---|
| VIEW_BILLING_AND_PAYMENT_HISTORY_REQUESTED | View Billing and Payment History requested | Reception Staff | Payment | Scope, reference, and reason |
| VIEW_BILLING_AND_PAYMENT_HISTORY_COMPLETED | View Billing and Payment History completed | Reception Staff / System | Payment | Previous and new state |
| VIEW_BILLING_AND_PAYMENT_HISTORY_REJECTED | View Billing and Payment History rejected | System | Payment | Rejection reason |

### Reports Generated

- Billing & Payment Management Operational Report
- Billing & Payment Management History Report
- Billing & Payment Management Exception Report
- Executive Dashboard

### Related Screens

- Billing and Payment History
- Billing & Payment Management Dashboard
- Billing & Payment Management History
- Audit Log Viewer

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/customers/{customerId}/commercial-history | GET | Authorized token | Execute View Billing and Payment History | 200 OK or 201 Created with result |
| /api/v1/customers/{customerId}/commercial-history/history | GET | Authorized token | Retrieve View Billing and Payment History history | 200 OK with history |
| /api/v1/audit-logs | GET | Authorized token | Retrieve related audit events | 200 OK with scoped audit records |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Payment | Read | Support View Billing and Payment History | Governed by Organization scope |
| Payment Transaction | Read / Insert | Support View Billing and Payment History | Governed by Organization scope |
| Payment Receipt | Read / Insert | Support View Billing and Payment History | Governed by Organization scope |
| Refund | Read / Insert | Support View Billing and Payment History | Governed by Organization scope |
| Reconciliation | Read / Insert | Support View Billing and Payment History | Governed by Organization scope |
| Audit Log | Insert | Record auditable activity | Immutable |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Not Requested | View Billing and Payment History initiated | Generating | Reception Staff | Required data captured |
| Generating | Validation succeeds | Ready | System | BA-02 rules satisfied |
| Ready | Processing completes | Export Pending | System | Related updates succeed |
| Ready | Approval or policy failure | Failed | System / Approver | Request rejected |
| Export Pending | View history | Export Pending | Authorized user | Read-only historical access |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| BPM-016-001 | View Billing and Payment History cannot be completed because required information is missing. | Missing mandatory data | Complete required fields |
| BPM-016-002 | You do not have permission to perform this action. | Authorization failure | Request access |
| BPM-016-003 | The selected record is not eligible for this action. | Policy or lifecycle violation | Review record status |
| BPM-016-004 | View Billing and Payment History could not be completed due to a system or integration error. | Processing failure | Retry or contact support |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Execute View Billing and Payment History | Given the actor has required permission and valid scope | When the actor submits valid information | Then the system shall complete View Billing and Payment History successfully |
| Enforce validation | Given mandatory data or policy conditions are invalid | When the action is submitted | Then the system shall reject the request with a clear message |
| Preserve audit | Given the action completes or fails | When processing ends | Then audit events shall record actor, timestamp, scope, and outcome |
| Protect scope | Given the selected record is outside authorized scope | When the action is requested | Then the system shall deny access |

### Dependencies

- Customer Management
- Membership Management
- Walk-in Customer Management
- Personal Training
- Notification Management
- Reporting Service
- Audit Service

### Operational Considerations

View Billing and Payment History should be designed for high-volume operational use, retry-safe processing, clear exception handling, and support-team diagnostics without exposing sensitive data.

### Non-Functional Considerations

This requirement shall satisfy Digitize non-functional expectations for availability, reliability, performance, scalability, security, configurability, maintainability, and auditability.

### Assumptions

- Required master data and configuration are maintained by authorized users.
- Related services expose stable APIs for validation and synchronization.
- Organization policies define approval, retention, notification, and exception behavior.

### Success Criteria

View Billing and Payment History is completed accurately, securely, and audibly, with downstream records synchronized and no loss of historical traceability.

### Related Functional Requirements

- FR-BPM-001 - Generate Invoice
- FR-BPM-002 - Calculate Service Charges
- FR-BPM-003 - Apply Discounts
- FR-BPM-004 - Calculate Taxes
- FR-AUD-001 - Record Audit Events

### Notes

View Billing and Payment History shall remain aligned with the approved BA source documents and shall not introduce behavior that bypasses tenant isolation, lifecycle governance, financial controls, or auditability.

---

## FR-BPM-017 - Generate Commercial Reports

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-BPM-017 |
| Requirement Name | Generate Commercial Reports |
| Functional Module | Billing & Payment Management |
| Business Domain | Billing & Payment |
| Business Capability | Financial Analytics |
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
| Business Requirement | BA-08 BR-018, BR-019, BR-020 |
| Business Rule | BA-02 BR-BIL-008, BR-PAY-007, BR-PAY-008, BR-SEC-004 |
| Business Process | BA-03 BP-BIL-012 Generate Billing Reports, BP-PAY-012 Generate Payment Reports |
| Business Process Flow | BA-04 Section 24 Billing Management Flow, Section 25 Payment Management Flow, Section 26 Invoice Management Flow, Section 27 Refund Management Flow |
| Persona | BA-05 Finance Staff, Reception Staff, Customer, Organization Administrator |
| User Journey | BA-06 Section 19 Payment Journey |
| Stakeholder | BA-07 Finance Staff, Reception Staff, Customer |
| Non-Functional Requirement | BA-09 Section 3.7 Data Protection, Section 4.4 Financial Compliance, Section 11 Reporting Requirements |
| Assumption / Constraint / Risk | BA-10 BA-RSK-011, BA-RSK-012, BA-RSK-014 |

### Purpose

To enable Financial Analytics within Billing & Payment Management so Digitize can execute Generate Commercial Reports consistently across Organizations, Facilities, Sites, users, and related operational or commercial services.

### Functional Requirement

The system shall support Generate Commercial Reports as an atomic Billing & Payment Management capability, including scoped data capture, business-rule validation, permission enforcement, lifecycle handling, related service synchronization, notification generation, reporting contribution, and immutable audit recording.

### Business Justification

Generate Commercial Reports is required to preserve operational control, revenue accuracy, service continuity, customer trust, and enterprise traceability for Billing & Payment processes. Without this capability, downstream modules would rely on incomplete, manual, or inconsistent records.

### Actors

- Finance Staff
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
- Actor has permission for Generate Commercial Reports.
- Required Billing & Payment configuration and policies are available.
- Related records required by BA-03 BP-BIL-012 Generate Billing Reports, BP-PAY-012 Generate Payment Reports are available and within authorized scope.

### Trigger

The capability is triggered when Finance Staff or the System initiates Generate Commercial Reports from Commercial Reports, a related workflow, a scheduled job, or an approved integration event.

### In Scope

- Capture or retrieve required Billing & Payment context.
- Validate Organization, Facility, Site, Customer, user, and policy scope where applicable.
- Execute Generate Commercial Reports according to approved business rules.
- Persist the resulting Invoice state or transaction.
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
- Invoice reference
- Customer reference, where applicable
- Effective date and time, where applicable
- Status or action reason, where applicable
- Payment, billing, trainer, session, or subscription reference where applicable
- Actor remarks, where applicable

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Invoice ID | Primary business record reference | Identifier | Yes | System / User | Must exist or be generated within scope | Core reference for Generate Commercial Reports |
| Organization ID | Tenant Organization context | Identifier | Yes | Session / System | Must be Active and authorized | Enforces tenant isolation |
| Facility ID | Facility context | Identifier | Conditional | User / System | Must be Active where applicable | Required for facility-level operations |
| Site ID | Site context | Identifier | Conditional | User / System | Must belong to Facility where applicable | Required for site-level operations |
| Status | Lifecycle or processing state | Enum | Yes | System | Must follow allowed state transitions | Drives UI and downstream access |
| Effective Date | Date when action applies | DateTime | Conditional | User / System | Must satisfy policy | Supports scheduled or immediate actions |
| Reason / Remarks | Business explanation | Text | Conditional | User | Required for governed changes | Stored for audit |

### Main Flow

1. Actor opens Commercial Reports or the related workflow.
2. The system validates authentication, authorization, tenant scope, and current operating context.
3. The system loads the required Billing & Payment records, related configuration, and policy controls.
4. Actor enters or confirms the information required to generate commercial reports.
5. The system validates mandatory data, lifecycle status, ownership, eligibility, financial, capacity, schedule, and security rules where applicable.
6. The system executes Generate Commercial Reports and persists the resulting Invoice state or transaction.
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

- Invoice record created, updated, validated, or reported according to the action.
- Lifecycle or processing status updated.
- Related history entry created.
- Business events emitted.
- Notifications generated where configured.
- Audit events recorded.
- Reports or dashboards updated where applicable.

### UI Behaviour

Commercial Reports shall display scoped context, mandatory fields, lifecycle status, policy warnings, validation results, available actions, confirmation prompts, read-only states, pagination or filters where applicable, and responsive behavior for front-desk and administrative usage.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-BPM-017-001 | Actor must have permission to execute Generate Commercial Reports. | Deny request and audit. | Critical |
| VAL-BPM-017-002 | Record must belong to the authorized Organization scope. | Deny request. | Critical |
| VAL-BPM-017-003 | Mandatory inputs must be complete and valid. | Block submission. | Critical |
| VAL-BPM-017-004 | Lifecycle and policy rules from BA-02 must be satisfied. | Reject or route for approval. | High |
| VAL-BPM-017-005 | Historical and audit records must be preserved. | Roll back or mark for recovery. | Critical |

### Business Rules

- BA-02 BR-BIL-008
- BA-02 BR-PAY-007
- BA-02 BR-PAY-008
- BA-02 BR-SEC-004

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| bpm.generate.commercial.reports.view | Finance Staff | Read | View Generate Commercial Reports context |
| bpm.generate.commercial.reports.execute | Finance Staff | Execute | Execute Generate Commercial Reports |
| bpm.generate.commercial.reports.approve | Organization Administrator | Approve | Approve governed exceptions where configured |
| bpm.generate.commercial.reports.audit.view | Organization Administrator / Support Executive | Read | View audit trace |

### Security Considerations

The capability shall enforce authentication, role-based authorization, tenant isolation, Organization scope, Facility and Site access boundaries, sensitive data masking, secure references, and immutable audit logging.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Generate Commercial Reports Completed | Primary actor and configured stakeholders | In-App / Email | Action completes | Include reference, status, and effective date where applicable |
| Generate Commercial Reports Requires Approval | Approver | In-App | Approval rule applies | Include safe summary and requested action |
| Generate Commercial Reports Failed | Primary actor | In-App | Validation or processing fails | Include safe failure reason and next action |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| GenerateCommercialReportsRequested | Billing & Payment Management | Approval Workflow, Audit Service |
| GenerateCommercialReportsCompleted | Billing & Payment Management | Notification Service, Reporting Service, Audit Service |
| GenerateCommercialReportsRejected | Billing & Payment Management | Notification Service, Audit Service |

### Audit Events

| Audit Event | Description | Actor | Target Entity | Key Data |
|---|---|---|---|---|
| GENERATE_COMMERCIAL_REPORTS_REQUESTED | Generate Commercial Reports requested | Finance Staff | Invoice | Scope, reference, and reason |
| GENERATE_COMMERCIAL_REPORTS_COMPLETED | Generate Commercial Reports completed | Finance Staff / System | Invoice | Previous and new state |
| GENERATE_COMMERCIAL_REPORTS_REJECTED | Generate Commercial Reports rejected | System | Invoice | Rejection reason |

### Reports Generated

- Billing & Payment Management Operational Report
- Billing & Payment Management History Report
- Billing & Payment Management Exception Report
- Executive Dashboard

### Related Screens

- Commercial Reports
- Billing & Payment Management Dashboard
- Billing & Payment Management History
- Audit Log Viewer

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/reports/commercial | GET | Authorized token | Execute Generate Commercial Reports | 200 OK or 201 Created with result |
| /api/v1/reports/commercial/history | GET | Authorized token | Retrieve Generate Commercial Reports history | 200 OK with history |
| /api/v1/audit-logs | GET | Authorized token | Retrieve related audit events | 200 OK with scoped audit records |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Invoice | Read | Support Generate Commercial Reports | Governed by Organization scope |
| Invoice Item | Read / Insert | Support Generate Commercial Reports | Governed by Organization scope |
| Charge | Read / Insert | Support Generate Commercial Reports | Governed by Organization scope |
| Discount | Read / Insert | Support Generate Commercial Reports | Governed by Organization scope |
| Tax | Read / Insert | Support Generate Commercial Reports | Governed by Organization scope |
| Audit Log | Insert | Record auditable activity | Immutable |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Not Requested | Generate Commercial Reports initiated | Generating | Finance Staff | Required data captured |
| Generating | Validation succeeds | Ready | System | BA-02 rules satisfied |
| Ready | Processing completes | Export Pending | System | Related updates succeed |
| Ready | Approval or policy failure | Failed | System / Approver | Request rejected |
| Export Pending | View history | Export Pending | Authorized user | Read-only historical access |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| BPM-017-001 | Generate Commercial Reports cannot be completed because required information is missing. | Missing mandatory data | Complete required fields |
| BPM-017-002 | You do not have permission to perform this action. | Authorization failure | Request access |
| BPM-017-003 | The selected record is not eligible for this action. | Policy or lifecycle violation | Review record status |
| BPM-017-004 | Generate Commercial Reports could not be completed due to a system or integration error. | Processing failure | Retry or contact support |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Execute Generate Commercial Reports | Given the actor has required permission and valid scope | When the actor submits valid information | Then the system shall complete Generate Commercial Reports successfully |
| Enforce validation | Given mandatory data or policy conditions are invalid | When the action is submitted | Then the system shall reject the request with a clear message |
| Preserve audit | Given the action completes or fails | When processing ends | Then audit events shall record actor, timestamp, scope, and outcome |
| Protect scope | Given the selected record is outside authorized scope | When the action is requested | Then the system shall deny access |

### Dependencies

- Customer Management
- Membership Management
- Walk-in Customer Management
- Personal Training
- Notification Management
- Reporting Service
- Audit Service

### Operational Considerations

Generate Commercial Reports should be designed for high-volume operational use, retry-safe processing, clear exception handling, and support-team diagnostics without exposing sensitive data.

### Non-Functional Considerations

This requirement shall satisfy Digitize non-functional expectations for availability, reliability, performance, scalability, security, configurability, maintainability, and auditability.

### Assumptions

- Required master data and configuration are maintained by authorized users.
- Related services expose stable APIs for validation and synchronization.
- Organization policies define approval, retention, notification, and exception behavior.

### Success Criteria

Generate Commercial Reports is completed accurately, securely, and audibly, with downstream records synchronized and no loss of historical traceability.

### Related Functional Requirements

- FR-BPM-001 - Generate Invoice
- FR-BPM-002 - Calculate Service Charges
- FR-BPM-003 - Apply Discounts
- FR-BPM-004 - Calculate Taxes
- FR-AUD-001 - Record Audit Events

### Notes

Generate Commercial Reports shall remain aligned with the approved BA source documents and shall not introduce behavior that bypasses tenant isolation, lifecycle governance, financial controls, or auditability.

---

## FR-BPM-018 - Generate Outstanding Statement

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-BPM-018 |
| Requirement Name | Generate Outstanding Statement |
| Functional Module | Billing & Payment Management |
| Business Domain | Billing & Payment |
| Business Capability | Receivable Management |
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
| Business Requirement | BA-08 BR-018 Billing and Invoice Generation |
| Business Rule | BA-02 BR-BIL-005, BR-BIL-008, BR-PAY-004 |
| Business Process | BA-03 BP-BIL-011 Generate Outstanding Statement |
| Business Process Flow | BA-04 Section 24 Billing Management Flow, Section 25 Payment Management Flow, Section 26 Invoice Management Flow, Section 27 Refund Management Flow |
| Persona | BA-05 Finance Staff, Reception Staff, Customer, Organization Administrator |
| User Journey | BA-06 Section 19 Payment Journey |
| Stakeholder | BA-07 Finance Staff, Reception Staff, Customer |
| Non-Functional Requirement | BA-09 Section 3.7 Data Protection, Section 4.4 Financial Compliance, Section 11 Reporting Requirements |
| Assumption / Constraint / Risk | BA-10 BA-RSK-011, BA-RSK-012, BA-RSK-014 |

### Purpose

To enable Receivable Management within Billing & Payment Management so Digitize can execute Generate Outstanding Statement consistently across Organizations, Facilities, Sites, users, and related operational or commercial services.

### Functional Requirement

The system shall support Generate Outstanding Statement as an atomic Billing & Payment Management capability, including scoped data capture, business-rule validation, permission enforcement, lifecycle handling, related service synchronization, notification generation, reporting contribution, and immutable audit recording.

### Business Justification

Generate Outstanding Statement is required to preserve operational control, revenue accuracy, service continuity, customer trust, and enterprise traceability for Billing & Payment processes. Without this capability, downstream modules would rely on incomplete, manual, or inconsistent records.

### Actors

- Finance Staff
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
- Actor has permission for Generate Outstanding Statement.
- Required Billing & Payment configuration and policies are available.
- Related records required by BA-03 BP-BIL-011 Generate Outstanding Statement are available and within authorized scope.

### Trigger

The capability is triggered when Finance Staff or the System initiates Generate Outstanding Statement from Outstanding Statement, a related workflow, a scheduled job, or an approved integration event.

### In Scope

- Capture or retrieve required Billing & Payment context.
- Validate Organization, Facility, Site, Customer, user, and policy scope where applicable.
- Execute Generate Outstanding Statement according to approved business rules.
- Persist the resulting Invoice state or transaction.
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
- Invoice reference
- Customer reference, where applicable
- Effective date and time, where applicable
- Status or action reason, where applicable
- Payment, billing, trainer, session, or subscription reference where applicable
- Actor remarks, where applicable

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Invoice ID | Primary business record reference | Identifier | Yes | System / User | Must exist or be generated within scope | Core reference for Generate Outstanding Statement |
| Organization ID | Tenant Organization context | Identifier | Yes | Session / System | Must be Active and authorized | Enforces tenant isolation |
| Facility ID | Facility context | Identifier | Conditional | User / System | Must be Active where applicable | Required for facility-level operations |
| Site ID | Site context | Identifier | Conditional | User / System | Must belong to Facility where applicable | Required for site-level operations |
| Status | Lifecycle or processing state | Enum | Yes | System | Must follow allowed state transitions | Drives UI and downstream access |
| Effective Date | Date when action applies | DateTime | Conditional | User / System | Must satisfy policy | Supports scheduled or immediate actions |
| Reason / Remarks | Business explanation | Text | Conditional | User | Required for governed changes | Stored for audit |

### Main Flow

1. Actor opens Outstanding Statement or the related workflow.
2. The system validates authentication, authorization, tenant scope, and current operating context.
3. The system loads the required Billing & Payment records, related configuration, and policy controls.
4. Actor enters or confirms the information required to generate outstanding statement.
5. The system validates mandatory data, lifecycle status, ownership, eligibility, financial, capacity, schedule, and security rules where applicable.
6. The system executes Generate Outstanding Statement and persists the resulting Invoice state or transaction.
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

- Invoice record created, updated, validated, or reported according to the action.
- Lifecycle or processing status updated.
- Related history entry created.
- Business events emitted.
- Notifications generated where configured.
- Audit events recorded.
- Reports or dashboards updated where applicable.

### UI Behaviour

Outstanding Statement shall display scoped context, mandatory fields, lifecycle status, policy warnings, validation results, available actions, confirmation prompts, read-only states, pagination or filters where applicable, and responsive behavior for front-desk and administrative usage.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-BPM-018-001 | Actor must have permission to execute Generate Outstanding Statement. | Deny request and audit. | Critical |
| VAL-BPM-018-002 | Record must belong to the authorized Organization scope. | Deny request. | Critical |
| VAL-BPM-018-003 | Mandatory inputs must be complete and valid. | Block submission. | Critical |
| VAL-BPM-018-004 | Lifecycle and policy rules from BA-02 must be satisfied. | Reject or route for approval. | High |
| VAL-BPM-018-005 | Historical and audit records must be preserved. | Roll back or mark for recovery. | Critical |

### Business Rules

- BA-02 BR-BIL-005
- BA-02 BR-BIL-008
- BA-02 BR-PAY-004

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| bpm.generate.outstanding.statement.view | Finance Staff | Read | View Generate Outstanding Statement context |
| bpm.generate.outstanding.statement.execute | Finance Staff | Execute | Execute Generate Outstanding Statement |
| bpm.generate.outstanding.statement.approve | Organization Administrator | Approve | Approve governed exceptions where configured |
| bpm.generate.outstanding.statement.audit.view | Organization Administrator / Support Executive | Read | View audit trace |

### Security Considerations

The capability shall enforce authentication, role-based authorization, tenant isolation, Organization scope, Facility and Site access boundaries, sensitive data masking, secure references, and immutable audit logging.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Generate Outstanding Statement Completed | Primary actor and configured stakeholders | In-App / Email | Action completes | Include reference, status, and effective date where applicable |
| Generate Outstanding Statement Requires Approval | Approver | In-App | Approval rule applies | Include safe summary and requested action |
| Generate Outstanding Statement Failed | Primary actor | In-App | Validation or processing fails | Include safe failure reason and next action |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| GenerateOutstandingStatementRequested | Billing & Payment Management | Approval Workflow, Audit Service |
| GenerateOutstandingStatementCompleted | Billing & Payment Management | Notification Service, Reporting Service, Audit Service |
| GenerateOutstandingStatementRejected | Billing & Payment Management | Notification Service, Audit Service |

### Audit Events

| Audit Event | Description | Actor | Target Entity | Key Data |
|---|---|---|---|---|
| GENERATE_OUTSTANDING_STATEMENT_REQUESTED | Generate Outstanding Statement requested | Finance Staff | Invoice | Scope, reference, and reason |
| GENERATE_OUTSTANDING_STATEMENT_COMPLETED | Generate Outstanding Statement completed | Finance Staff / System | Invoice | Previous and new state |
| GENERATE_OUTSTANDING_STATEMENT_REJECTED | Generate Outstanding Statement rejected | System | Invoice | Rejection reason |

### Reports Generated

- Billing & Payment Management Operational Report
- Billing & Payment Management History Report
- Billing & Payment Management Exception Report
- Executive Dashboard

### Related Screens

- Outstanding Statement
- Billing & Payment Management Dashboard
- Billing & Payment Management History
- Audit Log Viewer

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/billing/outstanding-statements | GET | Authorized token | Execute Generate Outstanding Statement | 200 OK or 201 Created with result |
| /api/v1/billing/outstanding-statements/history | GET | Authorized token | Retrieve Generate Outstanding Statement history | 200 OK with history |
| /api/v1/audit-logs | GET | Authorized token | Retrieve related audit events | 200 OK with scoped audit records |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Invoice | Read | Support Generate Outstanding Statement | Governed by Organization scope |
| Invoice Item | Read / Insert | Support Generate Outstanding Statement | Governed by Organization scope |
| Charge | Read / Insert | Support Generate Outstanding Statement | Governed by Organization scope |
| Discount | Read / Insert | Support Generate Outstanding Statement | Governed by Organization scope |
| Tax | Read / Insert | Support Generate Outstanding Statement | Governed by Organization scope |
| Audit Log | Insert | Record auditable activity | Immutable |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Not Requested | Generate Outstanding Statement initiated | Generating | Finance Staff | Required data captured |
| Generating | Validation succeeds | Ready | System | BA-02 rules satisfied |
| Ready | Processing completes | Export Pending | System | Related updates succeed |
| Ready | Approval or policy failure | Failed | System / Approver | Request rejected |
| Export Pending | View history | Export Pending | Authorized user | Read-only historical access |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| BPM-018-001 | Generate Outstanding Statement cannot be completed because required information is missing. | Missing mandatory data | Complete required fields |
| BPM-018-002 | You do not have permission to perform this action. | Authorization failure | Request access |
| BPM-018-003 | The selected record is not eligible for this action. | Policy or lifecycle violation | Review record status |
| BPM-018-004 | Generate Outstanding Statement could not be completed due to a system or integration error. | Processing failure | Retry or contact support |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Execute Generate Outstanding Statement | Given the actor has required permission and valid scope | When the actor submits valid information | Then the system shall complete Generate Outstanding Statement successfully |
| Enforce validation | Given mandatory data or policy conditions are invalid | When the action is submitted | Then the system shall reject the request with a clear message |
| Preserve audit | Given the action completes or fails | When processing ends | Then audit events shall record actor, timestamp, scope, and outcome |
| Protect scope | Given the selected record is outside authorized scope | When the action is requested | Then the system shall deny access |

### Dependencies

- Customer Management
- Membership Management
- Walk-in Customer Management
- Personal Training
- Notification Management
- Reporting Service
- Audit Service

### Operational Considerations

Generate Outstanding Statement should be designed for high-volume operational use, retry-safe processing, clear exception handling, and support-team diagnostics without exposing sensitive data.

### Non-Functional Considerations

This requirement shall satisfy Digitize non-functional expectations for availability, reliability, performance, scalability, security, configurability, maintainability, and auditability.

### Assumptions

- Required master data and configuration are maintained by authorized users.
- Related services expose stable APIs for validation and synchronization.
- Organization policies define approval, retention, notification, and exception behavior.

### Success Criteria

Generate Outstanding Statement is completed accurately, securely, and audibly, with downstream records synchronized and no loss of historical traceability.

### Related Functional Requirements

- FR-BPM-001 - Generate Invoice
- FR-BPM-002 - Calculate Service Charges
- FR-BPM-003 - Apply Discounts
- FR-BPM-004 - Calculate Taxes
- FR-AUD-001 - Record Audit Events

### Notes

Generate Outstanding Statement shall remain aligned with the approved BA source documents and shall not introduce behavior that bypasses tenant isolation, lifecycle governance, financial controls, or auditability.

---

**End of FR-14 - Billing & Payment Management**
