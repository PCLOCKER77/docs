# FR-19 Reports & Analytics

**Document ID:** FR-19  
**Document Name:** Reports & Analytics Functional Requirements  
**Company:** OreeOn Technologies Pvt. Ltd.  
**Product:** Digitize  
**Document Type:** Functional Requirements  
**Version:** 1.0  
**Status:** Draft  
**Owner:** Product Management  
**Prepared By:** Product Management, Business Analysis, and Solution Architecture  
**Last Updated:** July 2026

---

## FR-RPT-001 - View Operational Dashboard

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-RPT-001 |
| Requirement Name | View Operational Dashboard |
| Functional Module | Reports & Analytics |
| Business Domain | Reporting |
| Business Capability | Business Intelligence |
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
| Business Requirement | BA-08 BR-024 Reporting and Analytics |
| Business Rule | BA-02 BR-RPT-001, BR-RPT-002, BR-RPT-003, BR-RPT-008, BR-SEC-004 |
| Business Process | BA-03 BP-RPT-001 View Operational Dashboard |
| Business Process Flow | BA-04 Section 31 Reporting & Analytics Flow |
| Persona | BA-05 Organization Administrator, Facility Manager, Finance Staff, Reception Staff, Platform Administrator |
| User Journey | BA-06 Section 22 Cross Persona Interaction |
| Stakeholder | BA-07 Organization Administrator, Facility Manager, Finance Staff, Platform Administrator |
| Non-Functional Requirement | BA-09 Section 6.4 Reporting Performance, Section 11 Reporting Requirements, Section 3.2 Authorization |
| Assumption / Constraint / Risk | BA-10 BA-RSK-006, BA-RSK-008, BA-RSK-014 |

### Purpose

To provide the Business Intelligence capability required for Reports & Analytics so Digitize can execute View Operational Dashboard consistently, securely, and audibly across tenant Organizations and related business modules.

### Functional Requirement

The system shall support View Operational Dashboard as an atomic Reports & Analytics capability with scoped data capture, BA-02 rule validation, lifecycle handling, permission enforcement, downstream synchronization, notifications, reporting contribution, and immutable audit events.

### Business Justification

View Operational Dashboard is necessary to maintain enterprise governance, operational continuity, commercial accuracy, customer trust, and traceability for the Reporting domain. The capability ensures approved business processes can run without manual workarounds or ungoverned exceptions.

### Actors

- Organization Administrator
- Platform Administrator
- Organization Administrator
- System
- Notification Service
- Reporting Service
- Audit Service

### Preconditions

- Platform services are available.
- Organization context is active where tenant data is involved.
- Actor is authenticated where the action is user initiated.
- Actor has the required permission for View Operational Dashboard.
- Required Reporting configuration, policies, and related master data are available.
- Related records required by BA-03 BP-RPT-001 View Operational Dashboard are within authorized scope.

### Trigger

The requirement is triggered when Organization Administrator or the System initiates View Operational Dashboard from Operational Dashboard, a related business workflow, a scheduled job, or an approved integration event.

### In Scope

- Retrieve and validate Reporting context.
- Enforce tenant, Organization, Facility, Site, user, and policy scope where applicable.
- Execute View Operational Dashboard according to BA-02 business rules.
- Persist Dashboard state, transaction, history, or report data.
- Emit business, notification, reporting, and audit events.
- Provide confirmation, exception messaging, and traceability.

### Out of Scope

- Cross-Organization data movement.
- Physical deletion of historical or audit records.
- Rewriting approved Business Analysis documents.
- Low-level implementation design belonging to SAD, API Specification, or Database Design.
- Manual bypass of security, approval, retention, notification, license, reporting, or audit controls.

### Inputs

- Organization ID, where applicable
- Facility ID, where applicable
- Site ID, where applicable
- Dashboard reference
- Actor or system context
- Effective date and time, where applicable
- Status, rule, schedule, recipient, report, or policy details where applicable
- Reason, remarks, or approval reference where governance applies

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Dashboard ID | Primary record reference | Identifier | Yes | System / User | Must exist or be generated within authorized scope | Core reference for View Operational Dashboard |
| Organization ID | Tenant Organization context | Identifier | Conditional | Session / System | Must be authorized | Enforces data isolation |
| Status | Current lifecycle or processing status | Enum | Yes | System | Must follow permitted transitions | Drives UI and downstream behavior |
| Effective Date | Date and time when the action applies | DateTime | Conditional | User / System | Must satisfy policy | Supports immediate or scheduled processing |
| Rule / Policy Reference | Governing configuration or policy | Identifier | Conditional | System | Must be active where required | Links operational governance |
| Reason / Remarks | Business explanation | Text | Conditional | User | Required for governed changes | Stored for audit and support |
| Source Reference | Upstream workflow, job, or event source | Identifier | Conditional | System | Must be traceable | Supports cross-module traceability |

### Main Flow

1. Actor opens Operational Dashboard or the related workflow, or the System receives the scheduled or event-driven trigger.
2. The system validates authentication, authorization, tenant scope, and current lifecycle state.
3. The system loads required Reporting data, related configuration, and policy controls.
4. Actor or System provides the required input for View Operational Dashboard.
5. The system validates mandatory fields, BA-02 rules, ownership, lifecycle status, security scope, and downstream dependencies.
6. The system executes View Operational Dashboard and persists the resulting state, transaction, report, or history record.
7. The system synchronizes related modules and reporting datasets where applicable.
8. The system emits business events and notification events where configured.
9. The system records immutable audit events with actor, timestamp, source, scope, outcome, and changed values where applicable.
10. The system displays or returns completion confirmation with reference number and final status.

### Alternate Flows

- If approval is required, the system routes the request to the configured approver and holds processing until approval is completed.
- If processing is scheduled, the system stores the future action and executes it through a monitored scheduler.
- If the action is read-only or analytical, the system renders authorized information without changing source transactions.
- If notification or reporting update is not configured, the system skips that downstream action while preserving audit traceability.

### Exception Flows

- If authorization fails, the system denies the request and records a security audit event.
- If required data is missing or invalid, the system blocks processing and displays field-level errors.
- If BA-02 policy validation fails, the system rejects the request or routes for approved override where configuration permits.
- If a dependent service fails, the system fails safely, prevents inconsistent partial updates, and records the failure for support review.
- If notification delivery or report export fails after the core transaction succeeds, the transaction remains valid and the failure is logged for retry.

### Outputs

- Dashboard state, transaction, report, or history updated according to the action.
- Lifecycle status and processing outcome recorded.
- Related history and reporting records synchronized where applicable.
- Notifications generated where configured.
- Business events emitted.
- Audit events recorded.

### UI Behaviour

Operational Dashboard shall show scoped context, lifecycle status, mandatory fields, validation messages, policy warnings, available actions, read-only states, confirmation prompts, filters or pagination where applicable, and responsive behavior for administrative and operational users.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-RPT-001-001 | Actor or system process must be authorized to execute View Operational Dashboard. | Deny request and audit. | Critical |
| VAL-RPT-001-002 | Record scope must remain within authorized tenant and Organization boundaries. | Deny request. | Critical |
| VAL-RPT-001-003 | Mandatory input fields must be complete and valid. | Block processing. | Critical |
| VAL-RPT-001-004 | Applicable BA-02 lifecycle, security, retention, reporting, notification, and audit rules must pass. | Reject or route for approval. | High |
| VAL-RPT-001-005 | Historical, reporting, and audit records must be preserved. | Roll back or mark for controlled recovery. | Critical |

### Business Rules

- BA-02 BR-RPT-001
- BA-02 BR-RPT-002
- BA-02 BR-RPT-003
- BA-02 BR-RPT-008
- BA-02 BR-SEC-004

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| rpt.view.operational.dashboard.view | Organization Administrator | Read | View View Operational Dashboard context |
| rpt.view.operational.dashboard.execute | Organization Administrator | Execute | Execute View Operational Dashboard |
| rpt.view.operational.dashboard.approve | Platform Administrator / Organization Administrator | Approve | Approve governed exceptions where configured |
| rpt.view.operational.dashboard.audit.view | Platform Administrator / Organization Administrator | Read | Review audit trace |

### Security Considerations

The capability shall enforce authentication, role-based authorization, least privilege, tenant isolation, sensitive data masking, secure integration references, tamper-resistant audit logging, and retention-aware access control.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| View Operational Dashboard Completed | Configured stakeholders | In-App / Email | Action completes | Include reference, final status, and effective date where applicable |
| View Operational Dashboard Requires Action | Responsible owner or approver | In-App / Email | Approval, review, retry, or exception is required | Include safe summary and next action |
| View Operational Dashboard Failed | Actor or support owner | In-App / Email | Validation, job, or integration failure occurs | Include safe failure reason and support reference |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| ViewOperationalDashboardRequested | Reports & Analytics | Audit Service, Notification Service |
| ViewOperationalDashboardCompleted | Reports & Analytics | Reporting Service, Notification Service, Audit Service |
| ViewOperationalDashboardRejectedOrFailed | Reports & Analytics | Support Ticket Management, Audit Service |

### Audit Events

| Audit Event | Description | Actor | Target Entity | Key Data |
|---|---|---|---|---|
| VIEW_OPERATIONAL_DASHBOARD_REQUESTED | View Operational Dashboard requested | Organization Administrator / System | Dashboard | Scope, source, and request details |
| VIEW_OPERATIONAL_DASHBOARD_COMPLETED | View Operational Dashboard completed | Organization Administrator / System | Dashboard | Previous state, new state, and outcome |
| VIEW_OPERATIONAL_DASHBOARD_REJECTED_OR_FAILED | View Operational Dashboard rejected or failed | System | Dashboard | Reason code and recovery reference |

### Reports Generated

- Reports & Analytics Operational Report
- Reports & Analytics History Report
- Reports & Analytics Exception Report
- Executive Dashboard

### Related Screens

- Operational Dashboard
- Reports & Analytics Dashboard
- Reports & Analytics History
- Audit Log Viewer

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/reports/dashboard | GET | Authorized token | Execute View Operational Dashboard | 200 OK or 201 Created with result |
| /api/v1/reports/dashboard/history | GET | Authorized token | Retrieve View Operational Dashboard history | 200 OK with history records |
| /api/v1/audit-logs | GET | Authorized token | Retrieve related audit events | 200 OK with scoped audit records |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Dashboard | Read | Support View Operational Dashboard | Governed by tenant and Organization scope |
| Report | Read / Insert / Update | Support View Operational Dashboard | Governed by tenant and Organization scope |
| KPI | Read / Insert / Update | Support View Operational Dashboard | Governed by tenant and Organization scope |
| Analytics Dataset | Read / Insert / Update | Support View Operational Dashboard | Governed by tenant and Organization scope |
| Report Schedule | Read / Insert / Update | Support View Operational Dashboard | Governed by tenant and Organization scope |
| Export History | Read / Insert / Update | Support View Operational Dashboard | Governed by tenant and Organization scope |
| Audit Log | Insert / Read | Record auditable activity | Immutable |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Not Requested | View Operational Dashboard initiated | Generating | Organization Administrator / System | Required context captured |
| Generating | Validation succeeds | Ready | System | BA-02 rules satisfied |
| Ready | Processing completes | Export Pending | System | Related updates succeed |
| Ready | Validation or approval fails | Failed | System / Approver | Request rejected or failed |
| Export Pending | History reviewed | Export Pending | Authorized user | Read-only traceability |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| RPT-001-001 | View Operational Dashboard cannot be completed because required information is missing. | Missing mandatory data | Complete required fields |
| RPT-001-002 | You do not have permission to perform this action. | Authorization failure | Request access |
| RPT-001-003 | The selected record or policy state is not eligible for this action. | Lifecycle or rule violation | Review current status and policy |
| RPT-001-004 | View Operational Dashboard could not be completed due to a system or integration error. | Processing failure | Retry or contact support |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Execute View Operational Dashboard | Given the actor has permission and valid scope | When valid information is submitted | Then the system shall complete View Operational Dashboard successfully |
| Enforce business rules | Given applicable BA-02 rules are not satisfied | When processing is attempted | Then the system shall reject or route the request according to policy |
| Preserve traceability | Given processing completes or fails | When audit history is reviewed | Then actor, timestamp, source, scope, and outcome shall be visible |
| Protect scope | Given the selected record is outside authorized scope | When the action is requested | Then access shall be denied and audited |

### Dependencies

- All Operational Modules
- Billing & Payment Management
- Membership Management
- Attendance Management
- Subscription Management
- License Management
- Audit Service

### Operational Considerations

View Operational Dashboard should support controlled retries, operational diagnostics, clear exception ownership, and predictable behavior during peak usage, scheduled jobs, or integration delays.

### Non-Functional Considerations

This requirement shall satisfy Digitize expectations for availability, reliability, scalability, performance, security, configurability, maintainability, compliance, and auditability.

### Assumptions

- Required policies and master data are configured by authorized users.
- Related services provide stable APIs for validation, synchronization, reporting, and audit.
- Retention, notification, approval, and exception behavior are governed by Organization or platform policy.

### Success Criteria

View Operational Dashboard is completed accurately, securely, and traceably with downstream records synchronized and no loss of historical or audit integrity.

### Related Functional Requirements

- FR-RPT-002 - Generate Membership Report
- FR-RPT-003 - Generate Attendance Report
- FR-RPT-004 - Generate Revenue Report
- FR-RPT-005 - Generate Customer Report
- FR-AUD-001 - Record Audit Events
- FR-SEC-001 - Enforce Authentication and Authorization

### Notes

View Operational Dashboard shall remain aligned with the frozen BA source documents and shall not introduce behavior that bypasses security, lifecycle governance, reporting integrity, notification preferences, retention controls, or auditability.

---

## FR-RPT-002 - Generate Membership Report

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-RPT-002 |
| Requirement Name | Generate Membership Report |
| Functional Module | Reports & Analytics |
| Business Domain | Reporting |
| Business Capability | Membership Analytics |
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
| Business Requirement | BA-08 BR-024 Reporting and Analytics |
| Business Rule | BA-02 BR-RPT-001, BR-RPT-002, BR-RPT-003, BR-RPT-007 |
| Business Process | BA-03 BP-RPT-002 Generate Membership Report |
| Business Process Flow | BA-04 Section 31 Reporting & Analytics Flow |
| Persona | BA-05 Organization Administrator, Facility Manager, Finance Staff, Reception Staff, Platform Administrator |
| User Journey | BA-06 Section 22 Cross Persona Interaction |
| Stakeholder | BA-07 Organization Administrator, Facility Manager, Finance Staff, Platform Administrator |
| Non-Functional Requirement | BA-09 Section 6.4 Reporting Performance, Section 11 Reporting Requirements, Section 3.2 Authorization |
| Assumption / Constraint / Risk | BA-10 BA-RSK-006, BA-RSK-008, BA-RSK-014 |

### Purpose

To provide the Membership Analytics capability required for Reports & Analytics so Digitize can execute Generate Membership Report consistently, securely, and audibly across tenant Organizations and related business modules.

### Functional Requirement

The system shall support Generate Membership Report as an atomic Reports & Analytics capability with scoped data capture, BA-02 rule validation, lifecycle handling, permission enforcement, downstream synchronization, notifications, reporting contribution, and immutable audit events.

### Business Justification

Generate Membership Report is necessary to maintain enterprise governance, operational continuity, commercial accuracy, customer trust, and traceability for the Reporting domain. The capability ensures approved business processes can run without manual workarounds or ungoverned exceptions.

### Actors

- Organization Administrator
- Platform Administrator
- Organization Administrator
- System
- Notification Service
- Reporting Service
- Audit Service

### Preconditions

- Platform services are available.
- Organization context is active where tenant data is involved.
- Actor is authenticated where the action is user initiated.
- Actor has the required permission for Generate Membership Report.
- Required Reporting configuration, policies, and related master data are available.
- Related records required by BA-03 BP-RPT-002 Generate Membership Report are within authorized scope.

### Trigger

The requirement is triggered when Organization Administrator or the System initiates Generate Membership Report from Membership Report, a related business workflow, a scheduled job, or an approved integration event.

### In Scope

- Retrieve and validate Reporting context.
- Enforce tenant, Organization, Facility, Site, user, and policy scope where applicable.
- Execute Generate Membership Report according to BA-02 business rules.
- Persist Dashboard state, transaction, history, or report data.
- Emit business, notification, reporting, and audit events.
- Provide confirmation, exception messaging, and traceability.

### Out of Scope

- Cross-Organization data movement.
- Physical deletion of historical or audit records.
- Rewriting approved Business Analysis documents.
- Low-level implementation design belonging to SAD, API Specification, or Database Design.
- Manual bypass of security, approval, retention, notification, license, reporting, or audit controls.

### Inputs

- Organization ID, where applicable
- Facility ID, where applicable
- Site ID, where applicable
- Dashboard reference
- Actor or system context
- Effective date and time, where applicable
- Status, rule, schedule, recipient, report, or policy details where applicable
- Reason, remarks, or approval reference where governance applies

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Dashboard ID | Primary record reference | Identifier | Yes | System / User | Must exist or be generated within authorized scope | Core reference for Generate Membership Report |
| Organization ID | Tenant Organization context | Identifier | Conditional | Session / System | Must be authorized | Enforces data isolation |
| Status | Current lifecycle or processing status | Enum | Yes | System | Must follow permitted transitions | Drives UI and downstream behavior |
| Effective Date | Date and time when the action applies | DateTime | Conditional | User / System | Must satisfy policy | Supports immediate or scheduled processing |
| Rule / Policy Reference | Governing configuration or policy | Identifier | Conditional | System | Must be active where required | Links operational governance |
| Reason / Remarks | Business explanation | Text | Conditional | User | Required for governed changes | Stored for audit and support |
| Source Reference | Upstream workflow, job, or event source | Identifier | Conditional | System | Must be traceable | Supports cross-module traceability |

### Main Flow

1. Actor opens Membership Report or the related workflow, or the System receives the scheduled or event-driven trigger.
2. The system validates authentication, authorization, tenant scope, and current lifecycle state.
3. The system loads required Reporting data, related configuration, and policy controls.
4. Actor or System provides the required input for Generate Membership Report.
5. The system validates mandatory fields, BA-02 rules, ownership, lifecycle status, security scope, and downstream dependencies.
6. The system executes Generate Membership Report and persists the resulting state, transaction, report, or history record.
7. The system synchronizes related modules and reporting datasets where applicable.
8. The system emits business events and notification events where configured.
9. The system records immutable audit events with actor, timestamp, source, scope, outcome, and changed values where applicable.
10. The system displays or returns completion confirmation with reference number and final status.

### Alternate Flows

- If approval is required, the system routes the request to the configured approver and holds processing until approval is completed.
- If processing is scheduled, the system stores the future action and executes it through a monitored scheduler.
- If the action is read-only or analytical, the system renders authorized information without changing source transactions.
- If notification or reporting update is not configured, the system skips that downstream action while preserving audit traceability.

### Exception Flows

- If authorization fails, the system denies the request and records a security audit event.
- If required data is missing or invalid, the system blocks processing and displays field-level errors.
- If BA-02 policy validation fails, the system rejects the request or routes for approved override where configuration permits.
- If a dependent service fails, the system fails safely, prevents inconsistent partial updates, and records the failure for support review.
- If notification delivery or report export fails after the core transaction succeeds, the transaction remains valid and the failure is logged for retry.

### Outputs

- Dashboard state, transaction, report, or history updated according to the action.
- Lifecycle status and processing outcome recorded.
- Related history and reporting records synchronized where applicable.
- Notifications generated where configured.
- Business events emitted.
- Audit events recorded.

### UI Behaviour

Membership Report shall show scoped context, lifecycle status, mandatory fields, validation messages, policy warnings, available actions, read-only states, confirmation prompts, filters or pagination where applicable, and responsive behavior for administrative and operational users.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-RPT-002-001 | Actor or system process must be authorized to execute Generate Membership Report. | Deny request and audit. | Critical |
| VAL-RPT-002-002 | Record scope must remain within authorized tenant and Organization boundaries. | Deny request. | Critical |
| VAL-RPT-002-003 | Mandatory input fields must be complete and valid. | Block processing. | Critical |
| VAL-RPT-002-004 | Applicable BA-02 lifecycle, security, retention, reporting, notification, and audit rules must pass. | Reject or route for approval. | High |
| VAL-RPT-002-005 | Historical, reporting, and audit records must be preserved. | Roll back or mark for controlled recovery. | Critical |

### Business Rules

- BA-02 BR-RPT-001
- BA-02 BR-RPT-002
- BA-02 BR-RPT-003
- BA-02 BR-RPT-007

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| rpt.generate.membership.report.view | Organization Administrator | Read | View Generate Membership Report context |
| rpt.generate.membership.report.execute | Organization Administrator | Execute | Execute Generate Membership Report |
| rpt.generate.membership.report.approve | Platform Administrator / Organization Administrator | Approve | Approve governed exceptions where configured |
| rpt.generate.membership.report.audit.view | Platform Administrator / Organization Administrator | Read | Review audit trace |

### Security Considerations

The capability shall enforce authentication, role-based authorization, least privilege, tenant isolation, sensitive data masking, secure integration references, tamper-resistant audit logging, and retention-aware access control.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Generate Membership Report Completed | Configured stakeholders | In-App / Email | Action completes | Include reference, final status, and effective date where applicable |
| Generate Membership Report Requires Action | Responsible owner or approver | In-App / Email | Approval, review, retry, or exception is required | Include safe summary and next action |
| Generate Membership Report Failed | Actor or support owner | In-App / Email | Validation, job, or integration failure occurs | Include safe failure reason and support reference |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| GenerateMembershipReportRequested | Reports & Analytics | Audit Service, Notification Service |
| GenerateMembershipReportCompleted | Reports & Analytics | Reporting Service, Notification Service, Audit Service |
| GenerateMembershipReportRejectedOrFailed | Reports & Analytics | Support Ticket Management, Audit Service |

### Audit Events

| Audit Event | Description | Actor | Target Entity | Key Data |
|---|---|---|---|---|
| GENERATE_MEMBERSHIP_REPORT_REQUESTED | Generate Membership Report requested | Organization Administrator / System | Dashboard | Scope, source, and request details |
| GENERATE_MEMBERSHIP_REPORT_COMPLETED | Generate Membership Report completed | Organization Administrator / System | Dashboard | Previous state, new state, and outcome |
| GENERATE_MEMBERSHIP_REPORT_REJECTED_OR_FAILED | Generate Membership Report rejected or failed | System | Dashboard | Reason code and recovery reference |

### Reports Generated

- Reports & Analytics Operational Report
- Reports & Analytics History Report
- Reports & Analytics Exception Report
- Executive Dashboard

### Related Screens

- Membership Report
- Reports & Analytics Dashboard
- Reports & Analytics History
- Audit Log Viewer

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/reports/memberships | GET | Authorized token | Execute Generate Membership Report | 200 OK or 201 Created with result |
| /api/v1/reports/memberships/history | GET | Authorized token | Retrieve Generate Membership Report history | 200 OK with history records |
| /api/v1/audit-logs | GET | Authorized token | Retrieve related audit events | 200 OK with scoped audit records |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Dashboard | Read | Support Generate Membership Report | Governed by tenant and Organization scope |
| Report | Read / Insert / Update | Support Generate Membership Report | Governed by tenant and Organization scope |
| KPI | Read / Insert / Update | Support Generate Membership Report | Governed by tenant and Organization scope |
| Analytics Dataset | Read / Insert / Update | Support Generate Membership Report | Governed by tenant and Organization scope |
| Report Schedule | Read / Insert / Update | Support Generate Membership Report | Governed by tenant and Organization scope |
| Export History | Read / Insert / Update | Support Generate Membership Report | Governed by tenant and Organization scope |
| Audit Log | Insert / Read | Record auditable activity | Immutable |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Not Requested | Generate Membership Report initiated | Generating | Organization Administrator / System | Required context captured |
| Generating | Validation succeeds | Ready | System | BA-02 rules satisfied |
| Ready | Processing completes | Export Pending | System | Related updates succeed |
| Ready | Validation or approval fails | Failed | System / Approver | Request rejected or failed |
| Export Pending | History reviewed | Export Pending | Authorized user | Read-only traceability |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| RPT-002-001 | Generate Membership Report cannot be completed because required information is missing. | Missing mandatory data | Complete required fields |
| RPT-002-002 | You do not have permission to perform this action. | Authorization failure | Request access |
| RPT-002-003 | The selected record or policy state is not eligible for this action. | Lifecycle or rule violation | Review current status and policy |
| RPT-002-004 | Generate Membership Report could not be completed due to a system or integration error. | Processing failure | Retry or contact support |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Execute Generate Membership Report | Given the actor has permission and valid scope | When valid information is submitted | Then the system shall complete Generate Membership Report successfully |
| Enforce business rules | Given applicable BA-02 rules are not satisfied | When processing is attempted | Then the system shall reject or route the request according to policy |
| Preserve traceability | Given processing completes or fails | When audit history is reviewed | Then actor, timestamp, source, scope, and outcome shall be visible |
| Protect scope | Given the selected record is outside authorized scope | When the action is requested | Then access shall be denied and audited |

### Dependencies

- All Operational Modules
- Billing & Payment Management
- Membership Management
- Attendance Management
- Subscription Management
- License Management
- Audit Service

### Operational Considerations

Generate Membership Report should support controlled retries, operational diagnostics, clear exception ownership, and predictable behavior during peak usage, scheduled jobs, or integration delays.

### Non-Functional Considerations

This requirement shall satisfy Digitize expectations for availability, reliability, scalability, performance, security, configurability, maintainability, compliance, and auditability.

### Assumptions

- Required policies and master data are configured by authorized users.
- Related services provide stable APIs for validation, synchronization, reporting, and audit.
- Retention, notification, approval, and exception behavior are governed by Organization or platform policy.

### Success Criteria

Generate Membership Report is completed accurately, securely, and traceably with downstream records synchronized and no loss of historical or audit integrity.

### Related Functional Requirements

- FR-RPT-001 - View Operational Dashboard
- FR-RPT-003 - Generate Attendance Report
- FR-RPT-004 - Generate Revenue Report
- FR-RPT-005 - Generate Customer Report
- FR-AUD-001 - Record Audit Events
- FR-SEC-001 - Enforce Authentication and Authorization

### Notes

Generate Membership Report shall remain aligned with the frozen BA source documents and shall not introduce behavior that bypasses security, lifecycle governance, reporting integrity, notification preferences, retention controls, or auditability.

---

## FR-RPT-003 - Generate Attendance Report

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-RPT-003 |
| Requirement Name | Generate Attendance Report |
| Functional Module | Reports & Analytics |
| Business Domain | Reporting |
| Business Capability | Operational Reporting |
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
| Business Requirement | BA-08 BR-024 Reporting and Analytics |
| Business Rule | BA-02 BR-RPT-001, BR-RPT-002, BR-RPT-003, BR-RPT-007 |
| Business Process | BA-03 BP-RPT-003 Generate Attendance Report |
| Business Process Flow | BA-04 Section 31 Reporting & Analytics Flow |
| Persona | BA-05 Organization Administrator, Facility Manager, Finance Staff, Reception Staff, Platform Administrator |
| User Journey | BA-06 Section 22 Cross Persona Interaction |
| Stakeholder | BA-07 Organization Administrator, Facility Manager, Finance Staff, Platform Administrator |
| Non-Functional Requirement | BA-09 Section 6.4 Reporting Performance, Section 11 Reporting Requirements, Section 3.2 Authorization |
| Assumption / Constraint / Risk | BA-10 BA-RSK-006, BA-RSK-008, BA-RSK-014 |

### Purpose

To provide the Operational Reporting capability required for Reports & Analytics so Digitize can execute Generate Attendance Report consistently, securely, and audibly across tenant Organizations and related business modules.

### Functional Requirement

The system shall support Generate Attendance Report as an atomic Reports & Analytics capability with scoped data capture, BA-02 rule validation, lifecycle handling, permission enforcement, downstream synchronization, notifications, reporting contribution, and immutable audit events.

### Business Justification

Generate Attendance Report is necessary to maintain enterprise governance, operational continuity, commercial accuracy, customer trust, and traceability for the Reporting domain. The capability ensures approved business processes can run without manual workarounds or ungoverned exceptions.

### Actors

- Facility Manager
- Platform Administrator
- Organization Administrator
- System
- Notification Service
- Reporting Service
- Audit Service

### Preconditions

- Platform services are available.
- Organization context is active where tenant data is involved.
- Actor is authenticated where the action is user initiated.
- Actor has the required permission for Generate Attendance Report.
- Required Reporting configuration, policies, and related master data are available.
- Related records required by BA-03 BP-RPT-003 Generate Attendance Report are within authorized scope.

### Trigger

The requirement is triggered when Facility Manager or the System initiates Generate Attendance Report from Attendance Report, a related business workflow, a scheduled job, or an approved integration event.

### In Scope

- Retrieve and validate Reporting context.
- Enforce tenant, Organization, Facility, Site, user, and policy scope where applicable.
- Execute Generate Attendance Report according to BA-02 business rules.
- Persist Dashboard state, transaction, history, or report data.
- Emit business, notification, reporting, and audit events.
- Provide confirmation, exception messaging, and traceability.

### Out of Scope

- Cross-Organization data movement.
- Physical deletion of historical or audit records.
- Rewriting approved Business Analysis documents.
- Low-level implementation design belonging to SAD, API Specification, or Database Design.
- Manual bypass of security, approval, retention, notification, license, reporting, or audit controls.

### Inputs

- Organization ID, where applicable
- Facility ID, where applicable
- Site ID, where applicable
- Dashboard reference
- Actor or system context
- Effective date and time, where applicable
- Status, rule, schedule, recipient, report, or policy details where applicable
- Reason, remarks, or approval reference where governance applies

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Dashboard ID | Primary record reference | Identifier | Yes | System / User | Must exist or be generated within authorized scope | Core reference for Generate Attendance Report |
| Organization ID | Tenant Organization context | Identifier | Conditional | Session / System | Must be authorized | Enforces data isolation |
| Status | Current lifecycle or processing status | Enum | Yes | System | Must follow permitted transitions | Drives UI and downstream behavior |
| Effective Date | Date and time when the action applies | DateTime | Conditional | User / System | Must satisfy policy | Supports immediate or scheduled processing |
| Rule / Policy Reference | Governing configuration or policy | Identifier | Conditional | System | Must be active where required | Links operational governance |
| Reason / Remarks | Business explanation | Text | Conditional | User | Required for governed changes | Stored for audit and support |
| Source Reference | Upstream workflow, job, or event source | Identifier | Conditional | System | Must be traceable | Supports cross-module traceability |

### Main Flow

1. Actor opens Attendance Report or the related workflow, or the System receives the scheduled or event-driven trigger.
2. The system validates authentication, authorization, tenant scope, and current lifecycle state.
3. The system loads required Reporting data, related configuration, and policy controls.
4. Actor or System provides the required input for Generate Attendance Report.
5. The system validates mandatory fields, BA-02 rules, ownership, lifecycle status, security scope, and downstream dependencies.
6. The system executes Generate Attendance Report and persists the resulting state, transaction, report, or history record.
7. The system synchronizes related modules and reporting datasets where applicable.
8. The system emits business events and notification events where configured.
9. The system records immutable audit events with actor, timestamp, source, scope, outcome, and changed values where applicable.
10. The system displays or returns completion confirmation with reference number and final status.

### Alternate Flows

- If approval is required, the system routes the request to the configured approver and holds processing until approval is completed.
- If processing is scheduled, the system stores the future action and executes it through a monitored scheduler.
- If the action is read-only or analytical, the system renders authorized information without changing source transactions.
- If notification or reporting update is not configured, the system skips that downstream action while preserving audit traceability.

### Exception Flows

- If authorization fails, the system denies the request and records a security audit event.
- If required data is missing or invalid, the system blocks processing and displays field-level errors.
- If BA-02 policy validation fails, the system rejects the request or routes for approved override where configuration permits.
- If a dependent service fails, the system fails safely, prevents inconsistent partial updates, and records the failure for support review.
- If notification delivery or report export fails after the core transaction succeeds, the transaction remains valid and the failure is logged for retry.

### Outputs

- Dashboard state, transaction, report, or history updated according to the action.
- Lifecycle status and processing outcome recorded.
- Related history and reporting records synchronized where applicable.
- Notifications generated where configured.
- Business events emitted.
- Audit events recorded.

### UI Behaviour

Attendance Report shall show scoped context, lifecycle status, mandatory fields, validation messages, policy warnings, available actions, read-only states, confirmation prompts, filters or pagination where applicable, and responsive behavior for administrative and operational users.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-RPT-003-001 | Actor or system process must be authorized to execute Generate Attendance Report. | Deny request and audit. | Critical |
| VAL-RPT-003-002 | Record scope must remain within authorized tenant and Organization boundaries. | Deny request. | Critical |
| VAL-RPT-003-003 | Mandatory input fields must be complete and valid. | Block processing. | Critical |
| VAL-RPT-003-004 | Applicable BA-02 lifecycle, security, retention, reporting, notification, and audit rules must pass. | Reject or route for approval. | High |
| VAL-RPT-003-005 | Historical, reporting, and audit records must be preserved. | Roll back or mark for controlled recovery. | Critical |

### Business Rules

- BA-02 BR-RPT-001
- BA-02 BR-RPT-002
- BA-02 BR-RPT-003
- BA-02 BR-RPT-007

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| rpt.generate.attendance.report.view | Facility Manager | Read | View Generate Attendance Report context |
| rpt.generate.attendance.report.execute | Facility Manager | Execute | Execute Generate Attendance Report |
| rpt.generate.attendance.report.approve | Platform Administrator / Organization Administrator | Approve | Approve governed exceptions where configured |
| rpt.generate.attendance.report.audit.view | Platform Administrator / Organization Administrator | Read | Review audit trace |

### Security Considerations

The capability shall enforce authentication, role-based authorization, least privilege, tenant isolation, sensitive data masking, secure integration references, tamper-resistant audit logging, and retention-aware access control.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Generate Attendance Report Completed | Configured stakeholders | In-App / Email | Action completes | Include reference, final status, and effective date where applicable |
| Generate Attendance Report Requires Action | Responsible owner or approver | In-App / Email | Approval, review, retry, or exception is required | Include safe summary and next action |
| Generate Attendance Report Failed | Actor or support owner | In-App / Email | Validation, job, or integration failure occurs | Include safe failure reason and support reference |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| GenerateAttendanceReportRequested | Reports & Analytics | Audit Service, Notification Service |
| GenerateAttendanceReportCompleted | Reports & Analytics | Reporting Service, Notification Service, Audit Service |
| GenerateAttendanceReportRejectedOrFailed | Reports & Analytics | Support Ticket Management, Audit Service |

### Audit Events

| Audit Event | Description | Actor | Target Entity | Key Data |
|---|---|---|---|---|
| GENERATE_ATTENDANCE_REPORT_REQUESTED | Generate Attendance Report requested | Facility Manager / System | Dashboard | Scope, source, and request details |
| GENERATE_ATTENDANCE_REPORT_COMPLETED | Generate Attendance Report completed | Facility Manager / System | Dashboard | Previous state, new state, and outcome |
| GENERATE_ATTENDANCE_REPORT_REJECTED_OR_FAILED | Generate Attendance Report rejected or failed | System | Dashboard | Reason code and recovery reference |

### Reports Generated

- Reports & Analytics Operational Report
- Reports & Analytics History Report
- Reports & Analytics Exception Report
- Executive Dashboard

### Related Screens

- Attendance Report
- Reports & Analytics Dashboard
- Reports & Analytics History
- Audit Log Viewer

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/reports/attendance | GET | Authorized token | Execute Generate Attendance Report | 200 OK or 201 Created with result |
| /api/v1/reports/attendance/history | GET | Authorized token | Retrieve Generate Attendance Report history | 200 OK with history records |
| /api/v1/audit-logs | GET | Authorized token | Retrieve related audit events | 200 OK with scoped audit records |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Dashboard | Read | Support Generate Attendance Report | Governed by tenant and Organization scope |
| Report | Read / Insert / Update | Support Generate Attendance Report | Governed by tenant and Organization scope |
| KPI | Read / Insert / Update | Support Generate Attendance Report | Governed by tenant and Organization scope |
| Analytics Dataset | Read / Insert / Update | Support Generate Attendance Report | Governed by tenant and Organization scope |
| Report Schedule | Read / Insert / Update | Support Generate Attendance Report | Governed by tenant and Organization scope |
| Export History | Read / Insert / Update | Support Generate Attendance Report | Governed by tenant and Organization scope |
| Audit Log | Insert / Read | Record auditable activity | Immutable |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Not Requested | Generate Attendance Report initiated | Generating | Facility Manager / System | Required context captured |
| Generating | Validation succeeds | Ready | System | BA-02 rules satisfied |
| Ready | Processing completes | Export Pending | System | Related updates succeed |
| Ready | Validation or approval fails | Failed | System / Approver | Request rejected or failed |
| Export Pending | History reviewed | Export Pending | Authorized user | Read-only traceability |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| RPT-003-001 | Generate Attendance Report cannot be completed because required information is missing. | Missing mandatory data | Complete required fields |
| RPT-003-002 | You do not have permission to perform this action. | Authorization failure | Request access |
| RPT-003-003 | The selected record or policy state is not eligible for this action. | Lifecycle or rule violation | Review current status and policy |
| RPT-003-004 | Generate Attendance Report could not be completed due to a system or integration error. | Processing failure | Retry or contact support |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Execute Generate Attendance Report | Given the actor has permission and valid scope | When valid information is submitted | Then the system shall complete Generate Attendance Report successfully |
| Enforce business rules | Given applicable BA-02 rules are not satisfied | When processing is attempted | Then the system shall reject or route the request according to policy |
| Preserve traceability | Given processing completes or fails | When audit history is reviewed | Then actor, timestamp, source, scope, and outcome shall be visible |
| Protect scope | Given the selected record is outside authorized scope | When the action is requested | Then access shall be denied and audited |

### Dependencies

- All Operational Modules
- Billing & Payment Management
- Membership Management
- Attendance Management
- Subscription Management
- License Management
- Audit Service

### Operational Considerations

Generate Attendance Report should support controlled retries, operational diagnostics, clear exception ownership, and predictable behavior during peak usage, scheduled jobs, or integration delays.

### Non-Functional Considerations

This requirement shall satisfy Digitize expectations for availability, reliability, scalability, performance, security, configurability, maintainability, compliance, and auditability.

### Assumptions

- Required policies and master data are configured by authorized users.
- Related services provide stable APIs for validation, synchronization, reporting, and audit.
- Retention, notification, approval, and exception behavior are governed by Organization or platform policy.

### Success Criteria

Generate Attendance Report is completed accurately, securely, and traceably with downstream records synchronized and no loss of historical or audit integrity.

### Related Functional Requirements

- FR-RPT-001 - View Operational Dashboard
- FR-RPT-002 - Generate Membership Report
- FR-RPT-004 - Generate Revenue Report
- FR-RPT-005 - Generate Customer Report
- FR-AUD-001 - Record Audit Events
- FR-SEC-001 - Enforce Authentication and Authorization

### Notes

Generate Attendance Report shall remain aligned with the frozen BA source documents and shall not introduce behavior that bypasses security, lifecycle governance, reporting integrity, notification preferences, retention controls, or auditability.

---

## FR-RPT-004 - Generate Revenue Report

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-RPT-004 |
| Requirement Name | Generate Revenue Report |
| Functional Module | Reports & Analytics |
| Business Domain | Reporting |
| Business Capability | Financial Reporting |
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
| Business Requirement | BA-08 BR-024 Reporting and Analytics |
| Business Rule | BA-02 BR-RPT-001, BR-RPT-002, BR-RPT-006, BR-BIL-008 |
| Business Process | BA-03 BP-RPT-004 Generate Revenue Report |
| Business Process Flow | BA-04 Section 31 Reporting & Analytics Flow |
| Persona | BA-05 Organization Administrator, Facility Manager, Finance Staff, Reception Staff, Platform Administrator |
| User Journey | BA-06 Section 22 Cross Persona Interaction |
| Stakeholder | BA-07 Organization Administrator, Facility Manager, Finance Staff, Platform Administrator |
| Non-Functional Requirement | BA-09 Section 6.4 Reporting Performance, Section 11 Reporting Requirements, Section 3.2 Authorization |
| Assumption / Constraint / Risk | BA-10 BA-RSK-006, BA-RSK-008, BA-RSK-014 |

### Purpose

To provide the Financial Reporting capability required for Reports & Analytics so Digitize can execute Generate Revenue Report consistently, securely, and audibly across tenant Organizations and related business modules.

### Functional Requirement

The system shall support Generate Revenue Report as an atomic Reports & Analytics capability with scoped data capture, BA-02 rule validation, lifecycle handling, permission enforcement, downstream synchronization, notifications, reporting contribution, and immutable audit events.

### Business Justification

Generate Revenue Report is necessary to maintain enterprise governance, operational continuity, commercial accuracy, customer trust, and traceability for the Reporting domain. The capability ensures approved business processes can run without manual workarounds or ungoverned exceptions.

### Actors

- Finance Staff
- Platform Administrator
- Organization Administrator
- System
- Notification Service
- Reporting Service
- Audit Service

### Preconditions

- Platform services are available.
- Organization context is active where tenant data is involved.
- Actor is authenticated where the action is user initiated.
- Actor has the required permission for Generate Revenue Report.
- Required Reporting configuration, policies, and related master data are available.
- Related records required by BA-03 BP-RPT-004 Generate Revenue Report are within authorized scope.

### Trigger

The requirement is triggered when Finance Staff or the System initiates Generate Revenue Report from Revenue Report, a related business workflow, a scheduled job, or an approved integration event.

### In Scope

- Retrieve and validate Reporting context.
- Enforce tenant, Organization, Facility, Site, user, and policy scope where applicable.
- Execute Generate Revenue Report according to BA-02 business rules.
- Persist Dashboard state, transaction, history, or report data.
- Emit business, notification, reporting, and audit events.
- Provide confirmation, exception messaging, and traceability.

### Out of Scope

- Cross-Organization data movement.
- Physical deletion of historical or audit records.
- Rewriting approved Business Analysis documents.
- Low-level implementation design belonging to SAD, API Specification, or Database Design.
- Manual bypass of security, approval, retention, notification, license, reporting, or audit controls.

### Inputs

- Organization ID, where applicable
- Facility ID, where applicable
- Site ID, where applicable
- Dashboard reference
- Actor or system context
- Effective date and time, where applicable
- Status, rule, schedule, recipient, report, or policy details where applicable
- Reason, remarks, or approval reference where governance applies

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Dashboard ID | Primary record reference | Identifier | Yes | System / User | Must exist or be generated within authorized scope | Core reference for Generate Revenue Report |
| Organization ID | Tenant Organization context | Identifier | Conditional | Session / System | Must be authorized | Enforces data isolation |
| Status | Current lifecycle or processing status | Enum | Yes | System | Must follow permitted transitions | Drives UI and downstream behavior |
| Effective Date | Date and time when the action applies | DateTime | Conditional | User / System | Must satisfy policy | Supports immediate or scheduled processing |
| Rule / Policy Reference | Governing configuration or policy | Identifier | Conditional | System | Must be active where required | Links operational governance |
| Reason / Remarks | Business explanation | Text | Conditional | User | Required for governed changes | Stored for audit and support |
| Source Reference | Upstream workflow, job, or event source | Identifier | Conditional | System | Must be traceable | Supports cross-module traceability |

### Main Flow

1. Actor opens Revenue Report or the related workflow, or the System receives the scheduled or event-driven trigger.
2. The system validates authentication, authorization, tenant scope, and current lifecycle state.
3. The system loads required Reporting data, related configuration, and policy controls.
4. Actor or System provides the required input for Generate Revenue Report.
5. The system validates mandatory fields, BA-02 rules, ownership, lifecycle status, security scope, and downstream dependencies.
6. The system executes Generate Revenue Report and persists the resulting state, transaction, report, or history record.
7. The system synchronizes related modules and reporting datasets where applicable.
8. The system emits business events and notification events where configured.
9. The system records immutable audit events with actor, timestamp, source, scope, outcome, and changed values where applicable.
10. The system displays or returns completion confirmation with reference number and final status.

### Alternate Flows

- If approval is required, the system routes the request to the configured approver and holds processing until approval is completed.
- If processing is scheduled, the system stores the future action and executes it through a monitored scheduler.
- If the action is read-only or analytical, the system renders authorized information without changing source transactions.
- If notification or reporting update is not configured, the system skips that downstream action while preserving audit traceability.

### Exception Flows

- If authorization fails, the system denies the request and records a security audit event.
- If required data is missing or invalid, the system blocks processing and displays field-level errors.
- If BA-02 policy validation fails, the system rejects the request or routes for approved override where configuration permits.
- If a dependent service fails, the system fails safely, prevents inconsistent partial updates, and records the failure for support review.
- If notification delivery or report export fails after the core transaction succeeds, the transaction remains valid and the failure is logged for retry.

### Outputs

- Dashboard state, transaction, report, or history updated according to the action.
- Lifecycle status and processing outcome recorded.
- Related history and reporting records synchronized where applicable.
- Notifications generated where configured.
- Business events emitted.
- Audit events recorded.

### UI Behaviour

Revenue Report shall show scoped context, lifecycle status, mandatory fields, validation messages, policy warnings, available actions, read-only states, confirmation prompts, filters or pagination where applicable, and responsive behavior for administrative and operational users.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-RPT-004-001 | Actor or system process must be authorized to execute Generate Revenue Report. | Deny request and audit. | Critical |
| VAL-RPT-004-002 | Record scope must remain within authorized tenant and Organization boundaries. | Deny request. | Critical |
| VAL-RPT-004-003 | Mandatory input fields must be complete and valid. | Block processing. | Critical |
| VAL-RPT-004-004 | Applicable BA-02 lifecycle, security, retention, reporting, notification, and audit rules must pass. | Reject or route for approval. | High |
| VAL-RPT-004-005 | Historical, reporting, and audit records must be preserved. | Roll back or mark for controlled recovery. | Critical |

### Business Rules

- BA-02 BR-RPT-001
- BA-02 BR-RPT-002
- BA-02 BR-RPT-006
- BA-02 BR-BIL-008

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| rpt.generate.revenue.report.view | Finance Staff | Read | View Generate Revenue Report context |
| rpt.generate.revenue.report.execute | Finance Staff | Execute | Execute Generate Revenue Report |
| rpt.generate.revenue.report.approve | Platform Administrator / Organization Administrator | Approve | Approve governed exceptions where configured |
| rpt.generate.revenue.report.audit.view | Platform Administrator / Organization Administrator | Read | Review audit trace |

### Security Considerations

The capability shall enforce authentication, role-based authorization, least privilege, tenant isolation, sensitive data masking, secure integration references, tamper-resistant audit logging, and retention-aware access control.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Generate Revenue Report Completed | Configured stakeholders | In-App / Email | Action completes | Include reference, final status, and effective date where applicable |
| Generate Revenue Report Requires Action | Responsible owner or approver | In-App / Email | Approval, review, retry, or exception is required | Include safe summary and next action |
| Generate Revenue Report Failed | Actor or support owner | In-App / Email | Validation, job, or integration failure occurs | Include safe failure reason and support reference |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| GenerateRevenueReportRequested | Reports & Analytics | Audit Service, Notification Service |
| GenerateRevenueReportCompleted | Reports & Analytics | Reporting Service, Notification Service, Audit Service |
| GenerateRevenueReportRejectedOrFailed | Reports & Analytics | Support Ticket Management, Audit Service |

### Audit Events

| Audit Event | Description | Actor | Target Entity | Key Data |
|---|---|---|---|---|
| GENERATE_REVENUE_REPORT_REQUESTED | Generate Revenue Report requested | Finance Staff / System | Dashboard | Scope, source, and request details |
| GENERATE_REVENUE_REPORT_COMPLETED | Generate Revenue Report completed | Finance Staff / System | Dashboard | Previous state, new state, and outcome |
| GENERATE_REVENUE_REPORT_REJECTED_OR_FAILED | Generate Revenue Report rejected or failed | System | Dashboard | Reason code and recovery reference |

### Reports Generated

- Reports & Analytics Operational Report
- Reports & Analytics History Report
- Reports & Analytics Exception Report
- Executive Dashboard

### Related Screens

- Revenue Report
- Reports & Analytics Dashboard
- Reports & Analytics History
- Audit Log Viewer

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/reports/revenue | GET | Authorized token | Execute Generate Revenue Report | 200 OK or 201 Created with result |
| /api/v1/reports/revenue/history | GET | Authorized token | Retrieve Generate Revenue Report history | 200 OK with history records |
| /api/v1/audit-logs | GET | Authorized token | Retrieve related audit events | 200 OK with scoped audit records |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Dashboard | Read | Support Generate Revenue Report | Governed by tenant and Organization scope |
| Report | Read / Insert / Update | Support Generate Revenue Report | Governed by tenant and Organization scope |
| KPI | Read / Insert / Update | Support Generate Revenue Report | Governed by tenant and Organization scope |
| Analytics Dataset | Read / Insert / Update | Support Generate Revenue Report | Governed by tenant and Organization scope |
| Report Schedule | Read / Insert / Update | Support Generate Revenue Report | Governed by tenant and Organization scope |
| Export History | Read / Insert / Update | Support Generate Revenue Report | Governed by tenant and Organization scope |
| Audit Log | Insert / Read | Record auditable activity | Immutable |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Not Requested | Generate Revenue Report initiated | Generating | Finance Staff / System | Required context captured |
| Generating | Validation succeeds | Ready | System | BA-02 rules satisfied |
| Ready | Processing completes | Export Pending | System | Related updates succeed |
| Ready | Validation or approval fails | Failed | System / Approver | Request rejected or failed |
| Export Pending | History reviewed | Export Pending | Authorized user | Read-only traceability |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| RPT-004-001 | Generate Revenue Report cannot be completed because required information is missing. | Missing mandatory data | Complete required fields |
| RPT-004-002 | You do not have permission to perform this action. | Authorization failure | Request access |
| RPT-004-003 | The selected record or policy state is not eligible for this action. | Lifecycle or rule violation | Review current status and policy |
| RPT-004-004 | Generate Revenue Report could not be completed due to a system or integration error. | Processing failure | Retry or contact support |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Execute Generate Revenue Report | Given the actor has permission and valid scope | When valid information is submitted | Then the system shall complete Generate Revenue Report successfully |
| Enforce business rules | Given applicable BA-02 rules are not satisfied | When processing is attempted | Then the system shall reject or route the request according to policy |
| Preserve traceability | Given processing completes or fails | When audit history is reviewed | Then actor, timestamp, source, scope, and outcome shall be visible |
| Protect scope | Given the selected record is outside authorized scope | When the action is requested | Then access shall be denied and audited |

### Dependencies

- All Operational Modules
- Billing & Payment Management
- Membership Management
- Attendance Management
- Subscription Management
- License Management
- Audit Service

### Operational Considerations

Generate Revenue Report should support controlled retries, operational diagnostics, clear exception ownership, and predictable behavior during peak usage, scheduled jobs, or integration delays.

### Non-Functional Considerations

This requirement shall satisfy Digitize expectations for availability, reliability, scalability, performance, security, configurability, maintainability, compliance, and auditability.

### Assumptions

- Required policies and master data are configured by authorized users.
- Related services provide stable APIs for validation, synchronization, reporting, and audit.
- Retention, notification, approval, and exception behavior are governed by Organization or platform policy.

### Success Criteria

Generate Revenue Report is completed accurately, securely, and traceably with downstream records synchronized and no loss of historical or audit integrity.

### Related Functional Requirements

- FR-RPT-001 - View Operational Dashboard
- FR-RPT-002 - Generate Membership Report
- FR-RPT-003 - Generate Attendance Report
- FR-RPT-005 - Generate Customer Report
- FR-AUD-001 - Record Audit Events
- FR-SEC-001 - Enforce Authentication and Authorization

### Notes

Generate Revenue Report shall remain aligned with the frozen BA source documents and shall not introduce behavior that bypasses security, lifecycle governance, reporting integrity, notification preferences, retention controls, or auditability.

---

## FR-RPT-005 - Generate Customer Report

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-RPT-005 |
| Requirement Name | Generate Customer Report |
| Functional Module | Reports & Analytics |
| Business Domain | Reporting |
| Business Capability | Customer Analytics |
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
| Business Requirement | BA-08 BR-024 Reporting and Analytics |
| Business Rule | BA-02 BR-RPT-001, BR-RPT-002, BR-RPT-003, BR-SEC-009 |
| Business Process | BA-03 BP-RPT-005 Generate Customer Report |
| Business Process Flow | BA-04 Section 31 Reporting & Analytics Flow |
| Persona | BA-05 Organization Administrator, Facility Manager, Finance Staff, Reception Staff, Platform Administrator |
| User Journey | BA-06 Section 22 Cross Persona Interaction |
| Stakeholder | BA-07 Organization Administrator, Facility Manager, Finance Staff, Platform Administrator |
| Non-Functional Requirement | BA-09 Section 6.4 Reporting Performance, Section 11 Reporting Requirements, Section 3.2 Authorization |
| Assumption / Constraint / Risk | BA-10 BA-RSK-006, BA-RSK-008, BA-RSK-014 |

### Purpose

To provide the Customer Analytics capability required for Reports & Analytics so Digitize can execute Generate Customer Report consistently, securely, and audibly across tenant Organizations and related business modules.

### Functional Requirement

The system shall support Generate Customer Report as an atomic Reports & Analytics capability with scoped data capture, BA-02 rule validation, lifecycle handling, permission enforcement, downstream synchronization, notifications, reporting contribution, and immutable audit events.

### Business Justification

Generate Customer Report is necessary to maintain enterprise governance, operational continuity, commercial accuracy, customer trust, and traceability for the Reporting domain. The capability ensures approved business processes can run without manual workarounds or ungoverned exceptions.

### Actors

- Reception Staff
- Platform Administrator
- Organization Administrator
- System
- Notification Service
- Reporting Service
- Audit Service

### Preconditions

- Platform services are available.
- Organization context is active where tenant data is involved.
- Actor is authenticated where the action is user initiated.
- Actor has the required permission for Generate Customer Report.
- Required Reporting configuration, policies, and related master data are available.
- Related records required by BA-03 BP-RPT-005 Generate Customer Report are within authorized scope.

### Trigger

The requirement is triggered when Reception Staff or the System initiates Generate Customer Report from Customer Report, a related business workflow, a scheduled job, or an approved integration event.

### In Scope

- Retrieve and validate Reporting context.
- Enforce tenant, Organization, Facility, Site, user, and policy scope where applicable.
- Execute Generate Customer Report according to BA-02 business rules.
- Persist Dashboard state, transaction, history, or report data.
- Emit business, notification, reporting, and audit events.
- Provide confirmation, exception messaging, and traceability.

### Out of Scope

- Cross-Organization data movement.
- Physical deletion of historical or audit records.
- Rewriting approved Business Analysis documents.
- Low-level implementation design belonging to SAD, API Specification, or Database Design.
- Manual bypass of security, approval, retention, notification, license, reporting, or audit controls.

### Inputs

- Organization ID, where applicable
- Facility ID, where applicable
- Site ID, where applicable
- Dashboard reference
- Actor or system context
- Effective date and time, where applicable
- Status, rule, schedule, recipient, report, or policy details where applicable
- Reason, remarks, or approval reference where governance applies

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Dashboard ID | Primary record reference | Identifier | Yes | System / User | Must exist or be generated within authorized scope | Core reference for Generate Customer Report |
| Organization ID | Tenant Organization context | Identifier | Conditional | Session / System | Must be authorized | Enforces data isolation |
| Status | Current lifecycle or processing status | Enum | Yes | System | Must follow permitted transitions | Drives UI and downstream behavior |
| Effective Date | Date and time when the action applies | DateTime | Conditional | User / System | Must satisfy policy | Supports immediate or scheduled processing |
| Rule / Policy Reference | Governing configuration or policy | Identifier | Conditional | System | Must be active where required | Links operational governance |
| Reason / Remarks | Business explanation | Text | Conditional | User | Required for governed changes | Stored for audit and support |
| Source Reference | Upstream workflow, job, or event source | Identifier | Conditional | System | Must be traceable | Supports cross-module traceability |

### Main Flow

1. Actor opens Customer Report or the related workflow, or the System receives the scheduled or event-driven trigger.
2. The system validates authentication, authorization, tenant scope, and current lifecycle state.
3. The system loads required Reporting data, related configuration, and policy controls.
4. Actor or System provides the required input for Generate Customer Report.
5. The system validates mandatory fields, BA-02 rules, ownership, lifecycle status, security scope, and downstream dependencies.
6. The system executes Generate Customer Report and persists the resulting state, transaction, report, or history record.
7. The system synchronizes related modules and reporting datasets where applicable.
8. The system emits business events and notification events where configured.
9. The system records immutable audit events with actor, timestamp, source, scope, outcome, and changed values where applicable.
10. The system displays or returns completion confirmation with reference number and final status.

### Alternate Flows

- If approval is required, the system routes the request to the configured approver and holds processing until approval is completed.
- If processing is scheduled, the system stores the future action and executes it through a monitored scheduler.
- If the action is read-only or analytical, the system renders authorized information without changing source transactions.
- If notification or reporting update is not configured, the system skips that downstream action while preserving audit traceability.

### Exception Flows

- If authorization fails, the system denies the request and records a security audit event.
- If required data is missing or invalid, the system blocks processing and displays field-level errors.
- If BA-02 policy validation fails, the system rejects the request or routes for approved override where configuration permits.
- If a dependent service fails, the system fails safely, prevents inconsistent partial updates, and records the failure for support review.
- If notification delivery or report export fails after the core transaction succeeds, the transaction remains valid and the failure is logged for retry.

### Outputs

- Dashboard state, transaction, report, or history updated according to the action.
- Lifecycle status and processing outcome recorded.
- Related history and reporting records synchronized where applicable.
- Notifications generated where configured.
- Business events emitted.
- Audit events recorded.

### UI Behaviour

Customer Report shall show scoped context, lifecycle status, mandatory fields, validation messages, policy warnings, available actions, read-only states, confirmation prompts, filters or pagination where applicable, and responsive behavior for administrative and operational users.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-RPT-005-001 | Actor or system process must be authorized to execute Generate Customer Report. | Deny request and audit. | Critical |
| VAL-RPT-005-002 | Record scope must remain within authorized tenant and Organization boundaries. | Deny request. | Critical |
| VAL-RPT-005-003 | Mandatory input fields must be complete and valid. | Block processing. | Critical |
| VAL-RPT-005-004 | Applicable BA-02 lifecycle, security, retention, reporting, notification, and audit rules must pass. | Reject or route for approval. | High |
| VAL-RPT-005-005 | Historical, reporting, and audit records must be preserved. | Roll back or mark for controlled recovery. | Critical |

### Business Rules

- BA-02 BR-RPT-001
- BA-02 BR-RPT-002
- BA-02 BR-RPT-003
- BA-02 BR-SEC-009

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| rpt.generate.customer.report.view | Reception Staff | Read | View Generate Customer Report context |
| rpt.generate.customer.report.execute | Reception Staff | Execute | Execute Generate Customer Report |
| rpt.generate.customer.report.approve | Platform Administrator / Organization Administrator | Approve | Approve governed exceptions where configured |
| rpt.generate.customer.report.audit.view | Platform Administrator / Organization Administrator | Read | Review audit trace |

### Security Considerations

The capability shall enforce authentication, role-based authorization, least privilege, tenant isolation, sensitive data masking, secure integration references, tamper-resistant audit logging, and retention-aware access control.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Generate Customer Report Completed | Configured stakeholders | In-App / Email | Action completes | Include reference, final status, and effective date where applicable |
| Generate Customer Report Requires Action | Responsible owner or approver | In-App / Email | Approval, review, retry, or exception is required | Include safe summary and next action |
| Generate Customer Report Failed | Actor or support owner | In-App / Email | Validation, job, or integration failure occurs | Include safe failure reason and support reference |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| GenerateCustomerReportRequested | Reports & Analytics | Audit Service, Notification Service |
| GenerateCustomerReportCompleted | Reports & Analytics | Reporting Service, Notification Service, Audit Service |
| GenerateCustomerReportRejectedOrFailed | Reports & Analytics | Support Ticket Management, Audit Service |

### Audit Events

| Audit Event | Description | Actor | Target Entity | Key Data |
|---|---|---|---|---|
| GENERATE_CUSTOMER_REPORT_REQUESTED | Generate Customer Report requested | Reception Staff / System | Dashboard | Scope, source, and request details |
| GENERATE_CUSTOMER_REPORT_COMPLETED | Generate Customer Report completed | Reception Staff / System | Dashboard | Previous state, new state, and outcome |
| GENERATE_CUSTOMER_REPORT_REJECTED_OR_FAILED | Generate Customer Report rejected or failed | System | Dashboard | Reason code and recovery reference |

### Reports Generated

- Reports & Analytics Operational Report
- Reports & Analytics History Report
- Reports & Analytics Exception Report
- Executive Dashboard

### Related Screens

- Customer Report
- Reports & Analytics Dashboard
- Reports & Analytics History
- Audit Log Viewer

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/reports/customers | GET | Authorized token | Execute Generate Customer Report | 200 OK or 201 Created with result |
| /api/v1/reports/customers/history | GET | Authorized token | Retrieve Generate Customer Report history | 200 OK with history records |
| /api/v1/audit-logs | GET | Authorized token | Retrieve related audit events | 200 OK with scoped audit records |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Dashboard | Read | Support Generate Customer Report | Governed by tenant and Organization scope |
| Report | Read / Insert / Update | Support Generate Customer Report | Governed by tenant and Organization scope |
| KPI | Read / Insert / Update | Support Generate Customer Report | Governed by tenant and Organization scope |
| Analytics Dataset | Read / Insert / Update | Support Generate Customer Report | Governed by tenant and Organization scope |
| Report Schedule | Read / Insert / Update | Support Generate Customer Report | Governed by tenant and Organization scope |
| Export History | Read / Insert / Update | Support Generate Customer Report | Governed by tenant and Organization scope |
| Audit Log | Insert / Read | Record auditable activity | Immutable |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Not Requested | Generate Customer Report initiated | Generating | Reception Staff / System | Required context captured |
| Generating | Validation succeeds | Ready | System | BA-02 rules satisfied |
| Ready | Processing completes | Export Pending | System | Related updates succeed |
| Ready | Validation or approval fails | Failed | System / Approver | Request rejected or failed |
| Export Pending | History reviewed | Export Pending | Authorized user | Read-only traceability |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| RPT-005-001 | Generate Customer Report cannot be completed because required information is missing. | Missing mandatory data | Complete required fields |
| RPT-005-002 | You do not have permission to perform this action. | Authorization failure | Request access |
| RPT-005-003 | The selected record or policy state is not eligible for this action. | Lifecycle or rule violation | Review current status and policy |
| RPT-005-004 | Generate Customer Report could not be completed due to a system or integration error. | Processing failure | Retry or contact support |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Execute Generate Customer Report | Given the actor has permission and valid scope | When valid information is submitted | Then the system shall complete Generate Customer Report successfully |
| Enforce business rules | Given applicable BA-02 rules are not satisfied | When processing is attempted | Then the system shall reject or route the request according to policy |
| Preserve traceability | Given processing completes or fails | When audit history is reviewed | Then actor, timestamp, source, scope, and outcome shall be visible |
| Protect scope | Given the selected record is outside authorized scope | When the action is requested | Then access shall be denied and audited |

### Dependencies

- All Operational Modules
- Billing & Payment Management
- Membership Management
- Attendance Management
- Subscription Management
- License Management
- Audit Service

### Operational Considerations

Generate Customer Report should support controlled retries, operational diagnostics, clear exception ownership, and predictable behavior during peak usage, scheduled jobs, or integration delays.

### Non-Functional Considerations

This requirement shall satisfy Digitize expectations for availability, reliability, scalability, performance, security, configurability, maintainability, compliance, and auditability.

### Assumptions

- Required policies and master data are configured by authorized users.
- Related services provide stable APIs for validation, synchronization, reporting, and audit.
- Retention, notification, approval, and exception behavior are governed by Organization or platform policy.

### Success Criteria

Generate Customer Report is completed accurately, securely, and traceably with downstream records synchronized and no loss of historical or audit integrity.

### Related Functional Requirements

- FR-RPT-001 - View Operational Dashboard
- FR-RPT-002 - Generate Membership Report
- FR-RPT-003 - Generate Attendance Report
- FR-RPT-004 - Generate Revenue Report
- FR-AUD-001 - Record Audit Events
- FR-SEC-001 - Enforce Authentication and Authorization

### Notes

Generate Customer Report shall remain aligned with the frozen BA source documents and shall not introduce behavior that bypasses security, lifecycle governance, reporting integrity, notification preferences, retention controls, or auditability.

---

## FR-RPT-006 - Generate Trainer Performance Report

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-RPT-006 |
| Requirement Name | Generate Trainer Performance Report |
| Functional Module | Reports & Analytics |
| Business Domain | Reporting |
| Business Capability | Workforce Analytics |
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
| Business Requirement | BA-08 BR-024 Reporting and Analytics |
| Business Rule | BA-02 BR-RPT-001, BR-RPT-002, BR-RPT-007, BR-TRN-009 |
| Business Process | BA-03 BP-RPT-006 Generate Trainer Performance Report |
| Business Process Flow | BA-04 Section 31 Reporting & Analytics Flow |
| Persona | BA-05 Organization Administrator, Facility Manager, Finance Staff, Reception Staff, Platform Administrator |
| User Journey | BA-06 Section 22 Cross Persona Interaction |
| Stakeholder | BA-07 Organization Administrator, Facility Manager, Finance Staff, Platform Administrator |
| Non-Functional Requirement | BA-09 Section 6.4 Reporting Performance, Section 11 Reporting Requirements, Section 3.2 Authorization |
| Assumption / Constraint / Risk | BA-10 BA-RSK-006, BA-RSK-008, BA-RSK-014 |

### Purpose

To provide the Workforce Analytics capability required for Reports & Analytics so Digitize can execute Generate Trainer Performance Report consistently, securely, and audibly across tenant Organizations and related business modules.

### Functional Requirement

The system shall support Generate Trainer Performance Report as an atomic Reports & Analytics capability with scoped data capture, BA-02 rule validation, lifecycle handling, permission enforcement, downstream synchronization, notifications, reporting contribution, and immutable audit events.

### Business Justification

Generate Trainer Performance Report is necessary to maintain enterprise governance, operational continuity, commercial accuracy, customer trust, and traceability for the Reporting domain. The capability ensures approved business processes can run without manual workarounds or ungoverned exceptions.

### Actors

- Facility Manager
- Platform Administrator
- Organization Administrator
- System
- Notification Service
- Reporting Service
- Audit Service

### Preconditions

- Platform services are available.
- Organization context is active where tenant data is involved.
- Actor is authenticated where the action is user initiated.
- Actor has the required permission for Generate Trainer Performance Report.
- Required Reporting configuration, policies, and related master data are available.
- Related records required by BA-03 BP-RPT-006 Generate Trainer Performance Report are within authorized scope.

### Trigger

The requirement is triggered when Facility Manager or the System initiates Generate Trainer Performance Report from Trainer Performance Report, a related business workflow, a scheduled job, or an approved integration event.

### In Scope

- Retrieve and validate Reporting context.
- Enforce tenant, Organization, Facility, Site, user, and policy scope where applicable.
- Execute Generate Trainer Performance Report according to BA-02 business rules.
- Persist Dashboard state, transaction, history, or report data.
- Emit business, notification, reporting, and audit events.
- Provide confirmation, exception messaging, and traceability.

### Out of Scope

- Cross-Organization data movement.
- Physical deletion of historical or audit records.
- Rewriting approved Business Analysis documents.
- Low-level implementation design belonging to SAD, API Specification, or Database Design.
- Manual bypass of security, approval, retention, notification, license, reporting, or audit controls.

### Inputs

- Organization ID, where applicable
- Facility ID, where applicable
- Site ID, where applicable
- Dashboard reference
- Actor or system context
- Effective date and time, where applicable
- Status, rule, schedule, recipient, report, or policy details where applicable
- Reason, remarks, or approval reference where governance applies

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Dashboard ID | Primary record reference | Identifier | Yes | System / User | Must exist or be generated within authorized scope | Core reference for Generate Trainer Performance Report |
| Organization ID | Tenant Organization context | Identifier | Conditional | Session / System | Must be authorized | Enforces data isolation |
| Status | Current lifecycle or processing status | Enum | Yes | System | Must follow permitted transitions | Drives UI and downstream behavior |
| Effective Date | Date and time when the action applies | DateTime | Conditional | User / System | Must satisfy policy | Supports immediate or scheduled processing |
| Rule / Policy Reference | Governing configuration or policy | Identifier | Conditional | System | Must be active where required | Links operational governance |
| Reason / Remarks | Business explanation | Text | Conditional | User | Required for governed changes | Stored for audit and support |
| Source Reference | Upstream workflow, job, or event source | Identifier | Conditional | System | Must be traceable | Supports cross-module traceability |

### Main Flow

1. Actor opens Trainer Performance Report or the related workflow, or the System receives the scheduled or event-driven trigger.
2. The system validates authentication, authorization, tenant scope, and current lifecycle state.
3. The system loads required Reporting data, related configuration, and policy controls.
4. Actor or System provides the required input for Generate Trainer Performance Report.
5. The system validates mandatory fields, BA-02 rules, ownership, lifecycle status, security scope, and downstream dependencies.
6. The system executes Generate Trainer Performance Report and persists the resulting state, transaction, report, or history record.
7. The system synchronizes related modules and reporting datasets where applicable.
8. The system emits business events and notification events where configured.
9. The system records immutable audit events with actor, timestamp, source, scope, outcome, and changed values where applicable.
10. The system displays or returns completion confirmation with reference number and final status.

### Alternate Flows

- If approval is required, the system routes the request to the configured approver and holds processing until approval is completed.
- If processing is scheduled, the system stores the future action and executes it through a monitored scheduler.
- If the action is read-only or analytical, the system renders authorized information without changing source transactions.
- If notification or reporting update is not configured, the system skips that downstream action while preserving audit traceability.

### Exception Flows

- If authorization fails, the system denies the request and records a security audit event.
- If required data is missing or invalid, the system blocks processing and displays field-level errors.
- If BA-02 policy validation fails, the system rejects the request or routes for approved override where configuration permits.
- If a dependent service fails, the system fails safely, prevents inconsistent partial updates, and records the failure for support review.
- If notification delivery or report export fails after the core transaction succeeds, the transaction remains valid and the failure is logged for retry.

### Outputs

- Dashboard state, transaction, report, or history updated according to the action.
- Lifecycle status and processing outcome recorded.
- Related history and reporting records synchronized where applicable.
- Notifications generated where configured.
- Business events emitted.
- Audit events recorded.

### UI Behaviour

Trainer Performance Report shall show scoped context, lifecycle status, mandatory fields, validation messages, policy warnings, available actions, read-only states, confirmation prompts, filters or pagination where applicable, and responsive behavior for administrative and operational users.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-RPT-006-001 | Actor or system process must be authorized to execute Generate Trainer Performance Report. | Deny request and audit. | Critical |
| VAL-RPT-006-002 | Record scope must remain within authorized tenant and Organization boundaries. | Deny request. | Critical |
| VAL-RPT-006-003 | Mandatory input fields must be complete and valid. | Block processing. | Critical |
| VAL-RPT-006-004 | Applicable BA-02 lifecycle, security, retention, reporting, notification, and audit rules must pass. | Reject or route for approval. | High |
| VAL-RPT-006-005 | Historical, reporting, and audit records must be preserved. | Roll back or mark for controlled recovery. | Critical |

### Business Rules

- BA-02 BR-RPT-001
- BA-02 BR-RPT-002
- BA-02 BR-RPT-007
- BA-02 BR-TRN-009

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| rpt.generate.trainer.performance.report.view | Facility Manager | Read | View Generate Trainer Performance Report context |
| rpt.generate.trainer.performance.report.execute | Facility Manager | Execute | Execute Generate Trainer Performance Report |
| rpt.generate.trainer.performance.report.approve | Platform Administrator / Organization Administrator | Approve | Approve governed exceptions where configured |
| rpt.generate.trainer.performance.report.audit.view | Platform Administrator / Organization Administrator | Read | Review audit trace |

### Security Considerations

The capability shall enforce authentication, role-based authorization, least privilege, tenant isolation, sensitive data masking, secure integration references, tamper-resistant audit logging, and retention-aware access control.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Generate Trainer Performance Report Completed | Configured stakeholders | In-App / Email | Action completes | Include reference, final status, and effective date where applicable |
| Generate Trainer Performance Report Requires Action | Responsible owner or approver | In-App / Email | Approval, review, retry, or exception is required | Include safe summary and next action |
| Generate Trainer Performance Report Failed | Actor or support owner | In-App / Email | Validation, job, or integration failure occurs | Include safe failure reason and support reference |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| GenerateTrainerPerformanceReportRequested | Reports & Analytics | Audit Service, Notification Service |
| GenerateTrainerPerformanceReportCompleted | Reports & Analytics | Reporting Service, Notification Service, Audit Service |
| GenerateTrainerPerformanceReportRejectedOrFailed | Reports & Analytics | Support Ticket Management, Audit Service |

### Audit Events

| Audit Event | Description | Actor | Target Entity | Key Data |
|---|---|---|---|---|
| GENERATE_TRAINER_PERFORMANCE_REPORT_REQUESTED | Generate Trainer Performance Report requested | Facility Manager / System | Dashboard | Scope, source, and request details |
| GENERATE_TRAINER_PERFORMANCE_REPORT_COMPLETED | Generate Trainer Performance Report completed | Facility Manager / System | Dashboard | Previous state, new state, and outcome |
| GENERATE_TRAINER_PERFORMANCE_REPORT_REJECTED_OR_FAILED | Generate Trainer Performance Report rejected or failed | System | Dashboard | Reason code and recovery reference |

### Reports Generated

- Reports & Analytics Operational Report
- Reports & Analytics History Report
- Reports & Analytics Exception Report
- Executive Dashboard

### Related Screens

- Trainer Performance Report
- Reports & Analytics Dashboard
- Reports & Analytics History
- Audit Log Viewer

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/reports/trainers/performance | GET | Authorized token | Execute Generate Trainer Performance Report | 200 OK or 201 Created with result |
| /api/v1/reports/trainers/performance/history | GET | Authorized token | Retrieve Generate Trainer Performance Report history | 200 OK with history records |
| /api/v1/audit-logs | GET | Authorized token | Retrieve related audit events | 200 OK with scoped audit records |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Dashboard | Read | Support Generate Trainer Performance Report | Governed by tenant and Organization scope |
| Report | Read / Insert / Update | Support Generate Trainer Performance Report | Governed by tenant and Organization scope |
| KPI | Read / Insert / Update | Support Generate Trainer Performance Report | Governed by tenant and Organization scope |
| Analytics Dataset | Read / Insert / Update | Support Generate Trainer Performance Report | Governed by tenant and Organization scope |
| Report Schedule | Read / Insert / Update | Support Generate Trainer Performance Report | Governed by tenant and Organization scope |
| Export History | Read / Insert / Update | Support Generate Trainer Performance Report | Governed by tenant and Organization scope |
| Audit Log | Insert / Read | Record auditable activity | Immutable |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Not Requested | Generate Trainer Performance Report initiated | Generating | Facility Manager / System | Required context captured |
| Generating | Validation succeeds | Ready | System | BA-02 rules satisfied |
| Ready | Processing completes | Export Pending | System | Related updates succeed |
| Ready | Validation or approval fails | Failed | System / Approver | Request rejected or failed |
| Export Pending | History reviewed | Export Pending | Authorized user | Read-only traceability |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| RPT-006-001 | Generate Trainer Performance Report cannot be completed because required information is missing. | Missing mandatory data | Complete required fields |
| RPT-006-002 | You do not have permission to perform this action. | Authorization failure | Request access |
| RPT-006-003 | The selected record or policy state is not eligible for this action. | Lifecycle or rule violation | Review current status and policy |
| RPT-006-004 | Generate Trainer Performance Report could not be completed due to a system or integration error. | Processing failure | Retry or contact support |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Execute Generate Trainer Performance Report | Given the actor has permission and valid scope | When valid information is submitted | Then the system shall complete Generate Trainer Performance Report successfully |
| Enforce business rules | Given applicable BA-02 rules are not satisfied | When processing is attempted | Then the system shall reject or route the request according to policy |
| Preserve traceability | Given processing completes or fails | When audit history is reviewed | Then actor, timestamp, source, scope, and outcome shall be visible |
| Protect scope | Given the selected record is outside authorized scope | When the action is requested | Then access shall be denied and audited |

### Dependencies

- All Operational Modules
- Billing & Payment Management
- Membership Management
- Attendance Management
- Subscription Management
- License Management
- Audit Service

### Operational Considerations

Generate Trainer Performance Report should support controlled retries, operational diagnostics, clear exception ownership, and predictable behavior during peak usage, scheduled jobs, or integration delays.

### Non-Functional Considerations

This requirement shall satisfy Digitize expectations for availability, reliability, scalability, performance, security, configurability, maintainability, compliance, and auditability.

### Assumptions

- Required policies and master data are configured by authorized users.
- Related services provide stable APIs for validation, synchronization, reporting, and audit.
- Retention, notification, approval, and exception behavior are governed by Organization or platform policy.

### Success Criteria

Generate Trainer Performance Report is completed accurately, securely, and traceably with downstream records synchronized and no loss of historical or audit integrity.

### Related Functional Requirements

- FR-RPT-001 - View Operational Dashboard
- FR-RPT-002 - Generate Membership Report
- FR-RPT-003 - Generate Attendance Report
- FR-RPT-004 - Generate Revenue Report
- FR-AUD-001 - Record Audit Events
- FR-SEC-001 - Enforce Authentication and Authorization

### Notes

Generate Trainer Performance Report shall remain aligned with the frozen BA source documents and shall not introduce behavior that bypasses security, lifecycle governance, reporting integrity, notification preferences, retention controls, or auditability.

---

## FR-RPT-007 - Generate Activity Performance Report

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-RPT-007 |
| Requirement Name | Generate Activity Performance Report |
| Functional Module | Reports & Analytics |
| Business Domain | Reporting |
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
| Business Requirement | BA-08 BR-024 Reporting and Analytics |
| Business Rule | BA-02 BR-RPT-001, BR-RPT-002, BR-RPT-007 |
| Business Process | BA-03 BP-RPT-007 Generate Activity Performance Report |
| Business Process Flow | BA-04 Section 31 Reporting & Analytics Flow |
| Persona | BA-05 Organization Administrator, Facility Manager, Finance Staff, Reception Staff, Platform Administrator |
| User Journey | BA-06 Section 22 Cross Persona Interaction |
| Stakeholder | BA-07 Organization Administrator, Facility Manager, Finance Staff, Platform Administrator |
| Non-Functional Requirement | BA-09 Section 6.4 Reporting Performance, Section 11 Reporting Requirements, Section 3.2 Authorization |
| Assumption / Constraint / Risk | BA-10 BA-RSK-006, BA-RSK-008, BA-RSK-014 |

### Purpose

To provide the Activity Analytics capability required for Reports & Analytics so Digitize can execute Generate Activity Performance Report consistently, securely, and audibly across tenant Organizations and related business modules.

### Functional Requirement

The system shall support Generate Activity Performance Report as an atomic Reports & Analytics capability with scoped data capture, BA-02 rule validation, lifecycle handling, permission enforcement, downstream synchronization, notifications, reporting contribution, and immutable audit events.

### Business Justification

Generate Activity Performance Report is necessary to maintain enterprise governance, operational continuity, commercial accuracy, customer trust, and traceability for the Reporting domain. The capability ensures approved business processes can run without manual workarounds or ungoverned exceptions.

### Actors

- Facility Manager
- Platform Administrator
- Organization Administrator
- System
- Notification Service
- Reporting Service
- Audit Service

### Preconditions

- Platform services are available.
- Organization context is active where tenant data is involved.
- Actor is authenticated where the action is user initiated.
- Actor has the required permission for Generate Activity Performance Report.
- Required Reporting configuration, policies, and related master data are available.
- Related records required by BA-03 BP-RPT-007 Generate Activity Performance Report are within authorized scope.

### Trigger

The requirement is triggered when Facility Manager or the System initiates Generate Activity Performance Report from Activity Performance Report, a related business workflow, a scheduled job, or an approved integration event.

### In Scope

- Retrieve and validate Reporting context.
- Enforce tenant, Organization, Facility, Site, user, and policy scope where applicable.
- Execute Generate Activity Performance Report according to BA-02 business rules.
- Persist Dashboard state, transaction, history, or report data.
- Emit business, notification, reporting, and audit events.
- Provide confirmation, exception messaging, and traceability.

### Out of Scope

- Cross-Organization data movement.
- Physical deletion of historical or audit records.
- Rewriting approved Business Analysis documents.
- Low-level implementation design belonging to SAD, API Specification, or Database Design.
- Manual bypass of security, approval, retention, notification, license, reporting, or audit controls.

### Inputs

- Organization ID, where applicable
- Facility ID, where applicable
- Site ID, where applicable
- Dashboard reference
- Actor or system context
- Effective date and time, where applicable
- Status, rule, schedule, recipient, report, or policy details where applicable
- Reason, remarks, or approval reference where governance applies

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Dashboard ID | Primary record reference | Identifier | Yes | System / User | Must exist or be generated within authorized scope | Core reference for Generate Activity Performance Report |
| Organization ID | Tenant Organization context | Identifier | Conditional | Session / System | Must be authorized | Enforces data isolation |
| Status | Current lifecycle or processing status | Enum | Yes | System | Must follow permitted transitions | Drives UI and downstream behavior |
| Effective Date | Date and time when the action applies | DateTime | Conditional | User / System | Must satisfy policy | Supports immediate or scheduled processing |
| Rule / Policy Reference | Governing configuration or policy | Identifier | Conditional | System | Must be active where required | Links operational governance |
| Reason / Remarks | Business explanation | Text | Conditional | User | Required for governed changes | Stored for audit and support |
| Source Reference | Upstream workflow, job, or event source | Identifier | Conditional | System | Must be traceable | Supports cross-module traceability |

### Main Flow

1. Actor opens Activity Performance Report or the related workflow, or the System receives the scheduled or event-driven trigger.
2. The system validates authentication, authorization, tenant scope, and current lifecycle state.
3. The system loads required Reporting data, related configuration, and policy controls.
4. Actor or System provides the required input for Generate Activity Performance Report.
5. The system validates mandatory fields, BA-02 rules, ownership, lifecycle status, security scope, and downstream dependencies.
6. The system executes Generate Activity Performance Report and persists the resulting state, transaction, report, or history record.
7. The system synchronizes related modules and reporting datasets where applicable.
8. The system emits business events and notification events where configured.
9. The system records immutable audit events with actor, timestamp, source, scope, outcome, and changed values where applicable.
10. The system displays or returns completion confirmation with reference number and final status.

### Alternate Flows

- If approval is required, the system routes the request to the configured approver and holds processing until approval is completed.
- If processing is scheduled, the system stores the future action and executes it through a monitored scheduler.
- If the action is read-only or analytical, the system renders authorized information without changing source transactions.
- If notification or reporting update is not configured, the system skips that downstream action while preserving audit traceability.

### Exception Flows

- If authorization fails, the system denies the request and records a security audit event.
- If required data is missing or invalid, the system blocks processing and displays field-level errors.
- If BA-02 policy validation fails, the system rejects the request or routes for approved override where configuration permits.
- If a dependent service fails, the system fails safely, prevents inconsistent partial updates, and records the failure for support review.
- If notification delivery or report export fails after the core transaction succeeds, the transaction remains valid and the failure is logged for retry.

### Outputs

- Dashboard state, transaction, report, or history updated according to the action.
- Lifecycle status and processing outcome recorded.
- Related history and reporting records synchronized where applicable.
- Notifications generated where configured.
- Business events emitted.
- Audit events recorded.

### UI Behaviour

Activity Performance Report shall show scoped context, lifecycle status, mandatory fields, validation messages, policy warnings, available actions, read-only states, confirmation prompts, filters or pagination where applicable, and responsive behavior for administrative and operational users.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-RPT-007-001 | Actor or system process must be authorized to execute Generate Activity Performance Report. | Deny request and audit. | Critical |
| VAL-RPT-007-002 | Record scope must remain within authorized tenant and Organization boundaries. | Deny request. | Critical |
| VAL-RPT-007-003 | Mandatory input fields must be complete and valid. | Block processing. | Critical |
| VAL-RPT-007-004 | Applicable BA-02 lifecycle, security, retention, reporting, notification, and audit rules must pass. | Reject or route for approval. | High |
| VAL-RPT-007-005 | Historical, reporting, and audit records must be preserved. | Roll back or mark for controlled recovery. | Critical |

### Business Rules

- BA-02 BR-RPT-001
- BA-02 BR-RPT-002
- BA-02 BR-RPT-007

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| rpt.generate.activity.performance.report.view | Facility Manager | Read | View Generate Activity Performance Report context |
| rpt.generate.activity.performance.report.execute | Facility Manager | Execute | Execute Generate Activity Performance Report |
| rpt.generate.activity.performance.report.approve | Platform Administrator / Organization Administrator | Approve | Approve governed exceptions where configured |
| rpt.generate.activity.performance.report.audit.view | Platform Administrator / Organization Administrator | Read | Review audit trace |

### Security Considerations

The capability shall enforce authentication, role-based authorization, least privilege, tenant isolation, sensitive data masking, secure integration references, tamper-resistant audit logging, and retention-aware access control.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Generate Activity Performance Report Completed | Configured stakeholders | In-App / Email | Action completes | Include reference, final status, and effective date where applicable |
| Generate Activity Performance Report Requires Action | Responsible owner or approver | In-App / Email | Approval, review, retry, or exception is required | Include safe summary and next action |
| Generate Activity Performance Report Failed | Actor or support owner | In-App / Email | Validation, job, or integration failure occurs | Include safe failure reason and support reference |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| GenerateActivityPerformanceReportRequested | Reports & Analytics | Audit Service, Notification Service |
| GenerateActivityPerformanceReportCompleted | Reports & Analytics | Reporting Service, Notification Service, Audit Service |
| GenerateActivityPerformanceReportRejectedOrFailed | Reports & Analytics | Support Ticket Management, Audit Service |

### Audit Events

| Audit Event | Description | Actor | Target Entity | Key Data |
|---|---|---|---|---|
| GENERATE_ACTIVITY_PERFORMANCE_REPORT_REQUESTED | Generate Activity Performance Report requested | Facility Manager / System | Dashboard | Scope, source, and request details |
| GENERATE_ACTIVITY_PERFORMANCE_REPORT_COMPLETED | Generate Activity Performance Report completed | Facility Manager / System | Dashboard | Previous state, new state, and outcome |
| GENERATE_ACTIVITY_PERFORMANCE_REPORT_REJECTED_OR_FAILED | Generate Activity Performance Report rejected or failed | System | Dashboard | Reason code and recovery reference |

### Reports Generated

- Reports & Analytics Operational Report
- Reports & Analytics History Report
- Reports & Analytics Exception Report
- Executive Dashboard

### Related Screens

- Activity Performance Report
- Reports & Analytics Dashboard
- Reports & Analytics History
- Audit Log Viewer

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/reports/activities/performance | GET | Authorized token | Execute Generate Activity Performance Report | 200 OK or 201 Created with result |
| /api/v1/reports/activities/performance/history | GET | Authorized token | Retrieve Generate Activity Performance Report history | 200 OK with history records |
| /api/v1/audit-logs | GET | Authorized token | Retrieve related audit events | 200 OK with scoped audit records |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Dashboard | Read | Support Generate Activity Performance Report | Governed by tenant and Organization scope |
| Report | Read / Insert / Update | Support Generate Activity Performance Report | Governed by tenant and Organization scope |
| KPI | Read / Insert / Update | Support Generate Activity Performance Report | Governed by tenant and Organization scope |
| Analytics Dataset | Read / Insert / Update | Support Generate Activity Performance Report | Governed by tenant and Organization scope |
| Report Schedule | Read / Insert / Update | Support Generate Activity Performance Report | Governed by tenant and Organization scope |
| Export History | Read / Insert / Update | Support Generate Activity Performance Report | Governed by tenant and Organization scope |
| Audit Log | Insert / Read | Record auditable activity | Immutable |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Not Requested | Generate Activity Performance Report initiated | Generating | Facility Manager / System | Required context captured |
| Generating | Validation succeeds | Ready | System | BA-02 rules satisfied |
| Ready | Processing completes | Export Pending | System | Related updates succeed |
| Ready | Validation or approval fails | Failed | System / Approver | Request rejected or failed |
| Export Pending | History reviewed | Export Pending | Authorized user | Read-only traceability |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| RPT-007-001 | Generate Activity Performance Report cannot be completed because required information is missing. | Missing mandatory data | Complete required fields |
| RPT-007-002 | You do not have permission to perform this action. | Authorization failure | Request access |
| RPT-007-003 | The selected record or policy state is not eligible for this action. | Lifecycle or rule violation | Review current status and policy |
| RPT-007-004 | Generate Activity Performance Report could not be completed due to a system or integration error. | Processing failure | Retry or contact support |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Execute Generate Activity Performance Report | Given the actor has permission and valid scope | When valid information is submitted | Then the system shall complete Generate Activity Performance Report successfully |
| Enforce business rules | Given applicable BA-02 rules are not satisfied | When processing is attempted | Then the system shall reject or route the request according to policy |
| Preserve traceability | Given processing completes or fails | When audit history is reviewed | Then actor, timestamp, source, scope, and outcome shall be visible |
| Protect scope | Given the selected record is outside authorized scope | When the action is requested | Then access shall be denied and audited |

### Dependencies

- All Operational Modules
- Billing & Payment Management
- Membership Management
- Attendance Management
- Subscription Management
- License Management
- Audit Service

### Operational Considerations

Generate Activity Performance Report should support controlled retries, operational diagnostics, clear exception ownership, and predictable behavior during peak usage, scheduled jobs, or integration delays.

### Non-Functional Considerations

This requirement shall satisfy Digitize expectations for availability, reliability, scalability, performance, security, configurability, maintainability, compliance, and auditability.

### Assumptions

- Required policies and master data are configured by authorized users.
- Related services provide stable APIs for validation, synchronization, reporting, and audit.
- Retention, notification, approval, and exception behavior are governed by Organization or platform policy.

### Success Criteria

Generate Activity Performance Report is completed accurately, securely, and traceably with downstream records synchronized and no loss of historical or audit integrity.

### Related Functional Requirements

- FR-RPT-001 - View Operational Dashboard
- FR-RPT-002 - Generate Membership Report
- FR-RPT-003 - Generate Attendance Report
- FR-RPT-004 - Generate Revenue Report
- FR-AUD-001 - Record Audit Events
- FR-SEC-001 - Enforce Authentication and Authorization

### Notes

Generate Activity Performance Report shall remain aligned with the frozen BA source documents and shall not introduce behavior that bypasses security, lifecycle governance, reporting integrity, notification preferences, retention controls, or auditability.

---

## FR-RPT-008 - Generate Subscription Report

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-RPT-008 |
| Requirement Name | Generate Subscription Report |
| Functional Module | Reports & Analytics |
| Business Domain | Reporting |
| Business Capability | Commercial Analytics |
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
| Business Requirement | BA-08 BR-024 Reporting and Analytics |
| Business Rule | BA-02 BR-RPT-001, BR-RPT-002, BR-RPT-003, BR-SUB-001 |
| Business Process | BA-03 BP-RPT-008 Generate Subscription Report |
| Business Process Flow | BA-04 Section 31 Reporting & Analytics Flow |
| Persona | BA-05 Organization Administrator, Facility Manager, Finance Staff, Reception Staff, Platform Administrator |
| User Journey | BA-06 Section 22 Cross Persona Interaction |
| Stakeholder | BA-07 Organization Administrator, Facility Manager, Finance Staff, Platform Administrator |
| Non-Functional Requirement | BA-09 Section 6.4 Reporting Performance, Section 11 Reporting Requirements, Section 3.2 Authorization |
| Assumption / Constraint / Risk | BA-10 BA-RSK-006, BA-RSK-008, BA-RSK-014 |

### Purpose

To provide the Commercial Analytics capability required for Reports & Analytics so Digitize can execute Generate Subscription Report consistently, securely, and audibly across tenant Organizations and related business modules.

### Functional Requirement

The system shall support Generate Subscription Report as an atomic Reports & Analytics capability with scoped data capture, BA-02 rule validation, lifecycle handling, permission enforcement, downstream synchronization, notifications, reporting contribution, and immutable audit events.

### Business Justification

Generate Subscription Report is necessary to maintain enterprise governance, operational continuity, commercial accuracy, customer trust, and traceability for the Reporting domain. The capability ensures approved business processes can run without manual workarounds or ungoverned exceptions.

### Actors

- Platform Administrator
- Platform Administrator
- Organization Administrator
- System
- Notification Service
- Reporting Service
- Audit Service

### Preconditions

- Platform services are available.
- Organization context is active where tenant data is involved.
- Actor is authenticated where the action is user initiated.
- Actor has the required permission for Generate Subscription Report.
- Required Reporting configuration, policies, and related master data are available.
- Related records required by BA-03 BP-RPT-008 Generate Subscription Report are within authorized scope.

### Trigger

The requirement is triggered when Platform Administrator or the System initiates Generate Subscription Report from Subscription Report, a related business workflow, a scheduled job, or an approved integration event.

### In Scope

- Retrieve and validate Reporting context.
- Enforce tenant, Organization, Facility, Site, user, and policy scope where applicable.
- Execute Generate Subscription Report according to BA-02 business rules.
- Persist Dashboard state, transaction, history, or report data.
- Emit business, notification, reporting, and audit events.
- Provide confirmation, exception messaging, and traceability.

### Out of Scope

- Cross-Organization data movement.
- Physical deletion of historical or audit records.
- Rewriting approved Business Analysis documents.
- Low-level implementation design belonging to SAD, API Specification, or Database Design.
- Manual bypass of security, approval, retention, notification, license, reporting, or audit controls.

### Inputs

- Organization ID, where applicable
- Facility ID, where applicable
- Site ID, where applicable
- Dashboard reference
- Actor or system context
- Effective date and time, where applicable
- Status, rule, schedule, recipient, report, or policy details where applicable
- Reason, remarks, or approval reference where governance applies

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Dashboard ID | Primary record reference | Identifier | Yes | System / User | Must exist or be generated within authorized scope | Core reference for Generate Subscription Report |
| Organization ID | Tenant Organization context | Identifier | Conditional | Session / System | Must be authorized | Enforces data isolation |
| Status | Current lifecycle or processing status | Enum | Yes | System | Must follow permitted transitions | Drives UI and downstream behavior |
| Effective Date | Date and time when the action applies | DateTime | Conditional | User / System | Must satisfy policy | Supports immediate or scheduled processing |
| Rule / Policy Reference | Governing configuration or policy | Identifier | Conditional | System | Must be active where required | Links operational governance |
| Reason / Remarks | Business explanation | Text | Conditional | User | Required for governed changes | Stored for audit and support |
| Source Reference | Upstream workflow, job, or event source | Identifier | Conditional | System | Must be traceable | Supports cross-module traceability |

### Main Flow

1. Actor opens Subscription Report or the related workflow, or the System receives the scheduled or event-driven trigger.
2. The system validates authentication, authorization, tenant scope, and current lifecycle state.
3. The system loads required Reporting data, related configuration, and policy controls.
4. Actor or System provides the required input for Generate Subscription Report.
5. The system validates mandatory fields, BA-02 rules, ownership, lifecycle status, security scope, and downstream dependencies.
6. The system executes Generate Subscription Report and persists the resulting state, transaction, report, or history record.
7. The system synchronizes related modules and reporting datasets where applicable.
8. The system emits business events and notification events where configured.
9. The system records immutable audit events with actor, timestamp, source, scope, outcome, and changed values where applicable.
10. The system displays or returns completion confirmation with reference number and final status.

### Alternate Flows

- If approval is required, the system routes the request to the configured approver and holds processing until approval is completed.
- If processing is scheduled, the system stores the future action and executes it through a monitored scheduler.
- If the action is read-only or analytical, the system renders authorized information without changing source transactions.
- If notification or reporting update is not configured, the system skips that downstream action while preserving audit traceability.

### Exception Flows

- If authorization fails, the system denies the request and records a security audit event.
- If required data is missing or invalid, the system blocks processing and displays field-level errors.
- If BA-02 policy validation fails, the system rejects the request or routes for approved override where configuration permits.
- If a dependent service fails, the system fails safely, prevents inconsistent partial updates, and records the failure for support review.
- If notification delivery or report export fails after the core transaction succeeds, the transaction remains valid and the failure is logged for retry.

### Outputs

- Dashboard state, transaction, report, or history updated according to the action.
- Lifecycle status and processing outcome recorded.
- Related history and reporting records synchronized where applicable.
- Notifications generated where configured.
- Business events emitted.
- Audit events recorded.

### UI Behaviour

Subscription Report shall show scoped context, lifecycle status, mandatory fields, validation messages, policy warnings, available actions, read-only states, confirmation prompts, filters or pagination where applicable, and responsive behavior for administrative and operational users.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-RPT-008-001 | Actor or system process must be authorized to execute Generate Subscription Report. | Deny request and audit. | Critical |
| VAL-RPT-008-002 | Record scope must remain within authorized tenant and Organization boundaries. | Deny request. | Critical |
| VAL-RPT-008-003 | Mandatory input fields must be complete and valid. | Block processing. | Critical |
| VAL-RPT-008-004 | Applicable BA-02 lifecycle, security, retention, reporting, notification, and audit rules must pass. | Reject or route for approval. | High |
| VAL-RPT-008-005 | Historical, reporting, and audit records must be preserved. | Roll back or mark for controlled recovery. | Critical |

### Business Rules

- BA-02 BR-RPT-001
- BA-02 BR-RPT-002
- BA-02 BR-RPT-003
- BA-02 BR-SUB-001

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| rpt.generate.subscription.report.view | Platform Administrator | Read | View Generate Subscription Report context |
| rpt.generate.subscription.report.execute | Platform Administrator | Execute | Execute Generate Subscription Report |
| rpt.generate.subscription.report.approve | Platform Administrator / Organization Administrator | Approve | Approve governed exceptions where configured |
| rpt.generate.subscription.report.audit.view | Platform Administrator / Organization Administrator | Read | Review audit trace |

### Security Considerations

The capability shall enforce authentication, role-based authorization, least privilege, tenant isolation, sensitive data masking, secure integration references, tamper-resistant audit logging, and retention-aware access control.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Generate Subscription Report Completed | Configured stakeholders | In-App / Email | Action completes | Include reference, final status, and effective date where applicable |
| Generate Subscription Report Requires Action | Responsible owner or approver | In-App / Email | Approval, review, retry, or exception is required | Include safe summary and next action |
| Generate Subscription Report Failed | Actor or support owner | In-App / Email | Validation, job, or integration failure occurs | Include safe failure reason and support reference |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| GenerateSubscriptionReportRequested | Reports & Analytics | Audit Service, Notification Service |
| GenerateSubscriptionReportCompleted | Reports & Analytics | Reporting Service, Notification Service, Audit Service |
| GenerateSubscriptionReportRejectedOrFailed | Reports & Analytics | Support Ticket Management, Audit Service |

### Audit Events

| Audit Event | Description | Actor | Target Entity | Key Data |
|---|---|---|---|---|
| GENERATE_SUBSCRIPTION_REPORT_REQUESTED | Generate Subscription Report requested | Platform Administrator / System | Dashboard | Scope, source, and request details |
| GENERATE_SUBSCRIPTION_REPORT_COMPLETED | Generate Subscription Report completed | Platform Administrator / System | Dashboard | Previous state, new state, and outcome |
| GENERATE_SUBSCRIPTION_REPORT_REJECTED_OR_FAILED | Generate Subscription Report rejected or failed | System | Dashboard | Reason code and recovery reference |

### Reports Generated

- Reports & Analytics Operational Report
- Reports & Analytics History Report
- Reports & Analytics Exception Report
- Executive Dashboard

### Related Screens

- Subscription Report
- Reports & Analytics Dashboard
- Reports & Analytics History
- Audit Log Viewer

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/reports/subscriptions | GET | Authorized token | Execute Generate Subscription Report | 200 OK or 201 Created with result |
| /api/v1/reports/subscriptions/history | GET | Authorized token | Retrieve Generate Subscription Report history | 200 OK with history records |
| /api/v1/audit-logs | GET | Authorized token | Retrieve related audit events | 200 OK with scoped audit records |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Dashboard | Read | Support Generate Subscription Report | Governed by tenant and Organization scope |
| Report | Read / Insert / Update | Support Generate Subscription Report | Governed by tenant and Organization scope |
| KPI | Read / Insert / Update | Support Generate Subscription Report | Governed by tenant and Organization scope |
| Analytics Dataset | Read / Insert / Update | Support Generate Subscription Report | Governed by tenant and Organization scope |
| Report Schedule | Read / Insert / Update | Support Generate Subscription Report | Governed by tenant and Organization scope |
| Export History | Read / Insert / Update | Support Generate Subscription Report | Governed by tenant and Organization scope |
| Audit Log | Insert / Read | Record auditable activity | Immutable |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Not Requested | Generate Subscription Report initiated | Generating | Platform Administrator / System | Required context captured |
| Generating | Validation succeeds | Ready | System | BA-02 rules satisfied |
| Ready | Processing completes | Export Pending | System | Related updates succeed |
| Ready | Validation or approval fails | Failed | System / Approver | Request rejected or failed |
| Export Pending | History reviewed | Export Pending | Authorized user | Read-only traceability |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| RPT-008-001 | Generate Subscription Report cannot be completed because required information is missing. | Missing mandatory data | Complete required fields |
| RPT-008-002 | You do not have permission to perform this action. | Authorization failure | Request access |
| RPT-008-003 | The selected record or policy state is not eligible for this action. | Lifecycle or rule violation | Review current status and policy |
| RPT-008-004 | Generate Subscription Report could not be completed due to a system or integration error. | Processing failure | Retry or contact support |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Execute Generate Subscription Report | Given the actor has permission and valid scope | When valid information is submitted | Then the system shall complete Generate Subscription Report successfully |
| Enforce business rules | Given applicable BA-02 rules are not satisfied | When processing is attempted | Then the system shall reject or route the request according to policy |
| Preserve traceability | Given processing completes or fails | When audit history is reviewed | Then actor, timestamp, source, scope, and outcome shall be visible |
| Protect scope | Given the selected record is outside authorized scope | When the action is requested | Then access shall be denied and audited |

### Dependencies

- All Operational Modules
- Billing & Payment Management
- Membership Management
- Attendance Management
- Subscription Management
- License Management
- Audit Service

### Operational Considerations

Generate Subscription Report should support controlled retries, operational diagnostics, clear exception ownership, and predictable behavior during peak usage, scheduled jobs, or integration delays.

### Non-Functional Considerations

This requirement shall satisfy Digitize expectations for availability, reliability, scalability, performance, security, configurability, maintainability, compliance, and auditability.

### Assumptions

- Required policies and master data are configured by authorized users.
- Related services provide stable APIs for validation, synchronization, reporting, and audit.
- Retention, notification, approval, and exception behavior are governed by Organization or platform policy.

### Success Criteria

Generate Subscription Report is completed accurately, securely, and traceably with downstream records synchronized and no loss of historical or audit integrity.

### Related Functional Requirements

- FR-RPT-001 - View Operational Dashboard
- FR-RPT-002 - Generate Membership Report
- FR-RPT-003 - Generate Attendance Report
- FR-RPT-004 - Generate Revenue Report
- FR-AUD-001 - Record Audit Events
- FR-SEC-001 - Enforce Authentication and Authorization

### Notes

Generate Subscription Report shall remain aligned with the frozen BA source documents and shall not introduce behavior that bypasses security, lifecycle governance, reporting integrity, notification preferences, retention controls, or auditability.

---

## FR-RPT-009 - Export Report

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-RPT-009 |
| Requirement Name | Export Report |
| Functional Module | Reports & Analytics |
| Business Domain | Reporting |
| Business Capability | Data Export |
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
| Business Requirement | BA-08 BR-024 Reporting and Analytics |
| Business Rule | BA-02 BR-RPT-001, BR-RPT-005, BR-SEC-004, BR-AUD-003 |
| Business Process | BA-03 BP-RPT-009 Export Report |
| Business Process Flow | BA-04 Section 31 Reporting & Analytics Flow |
| Persona | BA-05 Organization Administrator, Facility Manager, Finance Staff, Reception Staff, Platform Administrator |
| User Journey | BA-06 Section 22 Cross Persona Interaction |
| Stakeholder | BA-07 Organization Administrator, Facility Manager, Finance Staff, Platform Administrator |
| Non-Functional Requirement | BA-09 Section 6.4 Reporting Performance, Section 11 Reporting Requirements, Section 3.2 Authorization |
| Assumption / Constraint / Risk | BA-10 BA-RSK-006, BA-RSK-008, BA-RSK-014 |

### Purpose

To provide the Data Export capability required for Reports & Analytics so Digitize can execute Export Report consistently, securely, and audibly across tenant Organizations and related business modules.

### Functional Requirement

The system shall support Export Report as an atomic Reports & Analytics capability with scoped data capture, BA-02 rule validation, lifecycle handling, permission enforcement, downstream synchronization, notifications, reporting contribution, and immutable audit events.

### Business Justification

Export Report is necessary to maintain enterprise governance, operational continuity, commercial accuracy, customer trust, and traceability for the Reporting domain. The capability ensures approved business processes can run without manual workarounds or ungoverned exceptions.

### Actors

- Organization Administrator
- Platform Administrator
- Organization Administrator
- System
- Notification Service
- Reporting Service
- Audit Service

### Preconditions

- Platform services are available.
- Organization context is active where tenant data is involved.
- Actor is authenticated where the action is user initiated.
- Actor has the required permission for Export Report.
- Required Reporting configuration, policies, and related master data are available.
- Related records required by BA-03 BP-RPT-009 Export Report are within authorized scope.

### Trigger

The requirement is triggered when Organization Administrator or the System initiates Export Report from Report Export, a related business workflow, a scheduled job, or an approved integration event.

### In Scope

- Retrieve and validate Reporting context.
- Enforce tenant, Organization, Facility, Site, user, and policy scope where applicable.
- Execute Export Report according to BA-02 business rules.
- Persist Dashboard state, transaction, history, or report data.
- Emit business, notification, reporting, and audit events.
- Provide confirmation, exception messaging, and traceability.

### Out of Scope

- Cross-Organization data movement.
- Physical deletion of historical or audit records.
- Rewriting approved Business Analysis documents.
- Low-level implementation design belonging to SAD, API Specification, or Database Design.
- Manual bypass of security, approval, retention, notification, license, reporting, or audit controls.

### Inputs

- Organization ID, where applicable
- Facility ID, where applicable
- Site ID, where applicable
- Dashboard reference
- Actor or system context
- Effective date and time, where applicable
- Status, rule, schedule, recipient, report, or policy details where applicable
- Reason, remarks, or approval reference where governance applies

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Dashboard ID | Primary record reference | Identifier | Yes | System / User | Must exist or be generated within authorized scope | Core reference for Export Report |
| Organization ID | Tenant Organization context | Identifier | Conditional | Session / System | Must be authorized | Enforces data isolation |
| Status | Current lifecycle or processing status | Enum | Yes | System | Must follow permitted transitions | Drives UI and downstream behavior |
| Effective Date | Date and time when the action applies | DateTime | Conditional | User / System | Must satisfy policy | Supports immediate or scheduled processing |
| Rule / Policy Reference | Governing configuration or policy | Identifier | Conditional | System | Must be active where required | Links operational governance |
| Reason / Remarks | Business explanation | Text | Conditional | User | Required for governed changes | Stored for audit and support |
| Source Reference | Upstream workflow, job, or event source | Identifier | Conditional | System | Must be traceable | Supports cross-module traceability |

### Main Flow

1. Actor opens Report Export or the related workflow, or the System receives the scheduled or event-driven trigger.
2. The system validates authentication, authorization, tenant scope, and current lifecycle state.
3. The system loads required Reporting data, related configuration, and policy controls.
4. Actor or System provides the required input for Export Report.
5. The system validates mandatory fields, BA-02 rules, ownership, lifecycle status, security scope, and downstream dependencies.
6. The system executes Export Report and persists the resulting state, transaction, report, or history record.
7. The system synchronizes related modules and reporting datasets where applicable.
8. The system emits business events and notification events where configured.
9. The system records immutable audit events with actor, timestamp, source, scope, outcome, and changed values where applicable.
10. The system displays or returns completion confirmation with reference number and final status.

### Alternate Flows

- If approval is required, the system routes the request to the configured approver and holds processing until approval is completed.
- If processing is scheduled, the system stores the future action and executes it through a monitored scheduler.
- If the action is read-only or analytical, the system renders authorized information without changing source transactions.
- If notification or reporting update is not configured, the system skips that downstream action while preserving audit traceability.

### Exception Flows

- If authorization fails, the system denies the request and records a security audit event.
- If required data is missing or invalid, the system blocks processing and displays field-level errors.
- If BA-02 policy validation fails, the system rejects the request or routes for approved override where configuration permits.
- If a dependent service fails, the system fails safely, prevents inconsistent partial updates, and records the failure for support review.
- If notification delivery or report export fails after the core transaction succeeds, the transaction remains valid and the failure is logged for retry.

### Outputs

- Dashboard state, transaction, report, or history updated according to the action.
- Lifecycle status and processing outcome recorded.
- Related history and reporting records synchronized where applicable.
- Notifications generated where configured.
- Business events emitted.
- Audit events recorded.

### UI Behaviour

Report Export shall show scoped context, lifecycle status, mandatory fields, validation messages, policy warnings, available actions, read-only states, confirmation prompts, filters or pagination where applicable, and responsive behavior for administrative and operational users.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-RPT-009-001 | Actor or system process must be authorized to execute Export Report. | Deny request and audit. | Critical |
| VAL-RPT-009-002 | Record scope must remain within authorized tenant and Organization boundaries. | Deny request. | Critical |
| VAL-RPT-009-003 | Mandatory input fields must be complete and valid. | Block processing. | Critical |
| VAL-RPT-009-004 | Applicable BA-02 lifecycle, security, retention, reporting, notification, and audit rules must pass. | Reject or route for approval. | High |
| VAL-RPT-009-005 | Historical, reporting, and audit records must be preserved. | Roll back or mark for controlled recovery. | Critical |

### Business Rules

- BA-02 BR-RPT-001
- BA-02 BR-RPT-005
- BA-02 BR-SEC-004
- BA-02 BR-AUD-003

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| rpt.export.report.view | Organization Administrator | Read | View Export Report context |
| rpt.export.report.execute | Organization Administrator | Execute | Execute Export Report |
| rpt.export.report.approve | Platform Administrator / Organization Administrator | Approve | Approve governed exceptions where configured |
| rpt.export.report.audit.view | Platform Administrator / Organization Administrator | Read | Review audit trace |

### Security Considerations

The capability shall enforce authentication, role-based authorization, least privilege, tenant isolation, sensitive data masking, secure integration references, tamper-resistant audit logging, and retention-aware access control.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Export Report Completed | Configured stakeholders | In-App / Email | Action completes | Include reference, final status, and effective date where applicable |
| Export Report Requires Action | Responsible owner or approver | In-App / Email | Approval, review, retry, or exception is required | Include safe summary and next action |
| Export Report Failed | Actor or support owner | In-App / Email | Validation, job, or integration failure occurs | Include safe failure reason and support reference |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| ExportReportRequested | Reports & Analytics | Audit Service, Notification Service |
| ExportReportCompleted | Reports & Analytics | Reporting Service, Notification Service, Audit Service |
| ExportReportRejectedOrFailed | Reports & Analytics | Support Ticket Management, Audit Service |

### Audit Events

| Audit Event | Description | Actor | Target Entity | Key Data |
|---|---|---|---|---|
| EXPORT_REPORT_REQUESTED | Export Report requested | Organization Administrator / System | Dashboard | Scope, source, and request details |
| EXPORT_REPORT_COMPLETED | Export Report completed | Organization Administrator / System | Dashboard | Previous state, new state, and outcome |
| EXPORT_REPORT_REJECTED_OR_FAILED | Export Report rejected or failed | System | Dashboard | Reason code and recovery reference |

### Reports Generated

- Reports & Analytics Operational Report
- Reports & Analytics History Report
- Reports & Analytics Exception Report
- Executive Dashboard

### Related Screens

- Report Export
- Reports & Analytics Dashboard
- Reports & Analytics History
- Audit Log Viewer

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/reports/exports | POST | Authorized token | Execute Export Report | 200 OK or 201 Created with result |
| /api/v1/reports/exports/history | GET | Authorized token | Retrieve Export Report history | 200 OK with history records |
| /api/v1/audit-logs | GET | Authorized token | Retrieve related audit events | 200 OK with scoped audit records |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Dashboard | Read | Support Export Report | Governed by tenant and Organization scope |
| Report | Read / Insert / Update | Support Export Report | Governed by tenant and Organization scope |
| KPI | Read / Insert / Update | Support Export Report | Governed by tenant and Organization scope |
| Analytics Dataset | Read / Insert / Update | Support Export Report | Governed by tenant and Organization scope |
| Report Schedule | Read / Insert / Update | Support Export Report | Governed by tenant and Organization scope |
| Export History | Read / Insert / Update | Support Export Report | Governed by tenant and Organization scope |
| Audit Log | Insert / Read | Record auditable activity | Immutable |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Not Requested | Export Report initiated | Generating | Organization Administrator / System | Required context captured |
| Generating | Validation succeeds | Ready | System | BA-02 rules satisfied |
| Ready | Processing completes | Export Pending | System | Related updates succeed |
| Ready | Validation or approval fails | Failed | System / Approver | Request rejected or failed |
| Export Pending | History reviewed | Export Pending | Authorized user | Read-only traceability |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| RPT-009-001 | Export Report cannot be completed because required information is missing. | Missing mandatory data | Complete required fields |
| RPT-009-002 | You do not have permission to perform this action. | Authorization failure | Request access |
| RPT-009-003 | The selected record or policy state is not eligible for this action. | Lifecycle or rule violation | Review current status and policy |
| RPT-009-004 | Export Report could not be completed due to a system or integration error. | Processing failure | Retry or contact support |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Execute Export Report | Given the actor has permission and valid scope | When valid information is submitted | Then the system shall complete Export Report successfully |
| Enforce business rules | Given applicable BA-02 rules are not satisfied | When processing is attempted | Then the system shall reject or route the request according to policy |
| Preserve traceability | Given processing completes or fails | When audit history is reviewed | Then actor, timestamp, source, scope, and outcome shall be visible |
| Protect scope | Given the selected record is outside authorized scope | When the action is requested | Then access shall be denied and audited |

### Dependencies

- All Operational Modules
- Billing & Payment Management
- Membership Management
- Attendance Management
- Subscription Management
- License Management
- Audit Service

### Operational Considerations

Export Report should support controlled retries, operational diagnostics, clear exception ownership, and predictable behavior during peak usage, scheduled jobs, or integration delays.

### Non-Functional Considerations

This requirement shall satisfy Digitize expectations for availability, reliability, scalability, performance, security, configurability, maintainability, compliance, and auditability.

### Assumptions

- Required policies and master data are configured by authorized users.
- Related services provide stable APIs for validation, synchronization, reporting, and audit.
- Retention, notification, approval, and exception behavior are governed by Organization or platform policy.

### Success Criteria

Export Report is completed accurately, securely, and traceably with downstream records synchronized and no loss of historical or audit integrity.

### Related Functional Requirements

- FR-RPT-001 - View Operational Dashboard
- FR-RPT-002 - Generate Membership Report
- FR-RPT-003 - Generate Attendance Report
- FR-RPT-004 - Generate Revenue Report
- FR-AUD-001 - Record Audit Events
- FR-SEC-001 - Enforce Authentication and Authorization

### Notes

Export Report shall remain aligned with the frozen BA source documents and shall not introduce behavior that bypasses security, lifecycle governance, reporting integrity, notification preferences, retention controls, or auditability.

---

## FR-RPT-010 - Schedule Automated Report

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-RPT-010 |
| Requirement Name | Schedule Automated Report |
| Functional Module | Reports & Analytics |
| Business Domain | Reporting |
| Business Capability | Report Automation |
| Requirement Type | Functional |
| Requirement Category | Background Job |
| Requirement Version | 1.0 |
| Requirement Status | Approved |
| Priority | Medium |
| Complexity | Medium |
| Release Version | 1.0 |
| Owner | Product Management |

### Traceability References

| Traceability Type | Reference |
|---|---|
| Business Requirement | BA-08 BR-024 Reporting and Analytics |
| Business Rule | BA-02 BR-RPT-001, BR-RPT-004, BR-RPT-005, BR-NOT-001 |
| Business Process | BA-03 BP-RPT-010 Schedule Automated Report |
| Business Process Flow | BA-04 Section 31 Reporting & Analytics Flow |
| Persona | BA-05 Organization Administrator, Facility Manager, Finance Staff, Reception Staff, Platform Administrator |
| User Journey | BA-06 Section 22 Cross Persona Interaction |
| Stakeholder | BA-07 Organization Administrator, Facility Manager, Finance Staff, Platform Administrator |
| Non-Functional Requirement | BA-09 Section 6.4 Reporting Performance, Section 11 Reporting Requirements, Section 3.2 Authorization |
| Assumption / Constraint / Risk | BA-10 BA-RSK-006, BA-RSK-008, BA-RSK-014 |

### Purpose

To provide the Report Automation capability required for Reports & Analytics so Digitize can execute Schedule Automated Report consistently, securely, and audibly across tenant Organizations and related business modules.

### Functional Requirement

The system shall support Schedule Automated Report as an atomic Reports & Analytics capability with scoped data capture, BA-02 rule validation, lifecycle handling, permission enforcement, downstream synchronization, notifications, reporting contribution, and immutable audit events.

### Business Justification

Schedule Automated Report is necessary to maintain enterprise governance, operational continuity, commercial accuracy, customer trust, and traceability for the Reporting domain. The capability ensures approved business processes can run without manual workarounds or ungoverned exceptions.

### Actors

- Organization Administrator
- Platform Administrator
- Organization Administrator
- System
- Notification Service
- Reporting Service
- Audit Service

### Preconditions

- Platform services are available.
- Organization context is active where tenant data is involved.
- Actor is authenticated where the action is user initiated.
- Actor has the required permission for Schedule Automated Report.
- Required Reporting configuration, policies, and related master data are available.
- Related records required by BA-03 BP-RPT-010 Schedule Automated Report are within authorized scope.

### Trigger

The requirement is triggered when Organization Administrator or the System initiates Schedule Automated Report from Report Schedule, a related business workflow, a scheduled job, or an approved integration event.

### In Scope

- Retrieve and validate Reporting context.
- Enforce tenant, Organization, Facility, Site, user, and policy scope where applicable.
- Execute Schedule Automated Report according to BA-02 business rules.
- Persist Dashboard state, transaction, history, or report data.
- Emit business, notification, reporting, and audit events.
- Provide confirmation, exception messaging, and traceability.

### Out of Scope

- Cross-Organization data movement.
- Physical deletion of historical or audit records.
- Rewriting approved Business Analysis documents.
- Low-level implementation design belonging to SAD, API Specification, or Database Design.
- Manual bypass of security, approval, retention, notification, license, reporting, or audit controls.

### Inputs

- Organization ID, where applicable
- Facility ID, where applicable
- Site ID, where applicable
- Dashboard reference
- Actor or system context
- Effective date and time, where applicable
- Status, rule, schedule, recipient, report, or policy details where applicable
- Reason, remarks, or approval reference where governance applies

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Dashboard ID | Primary record reference | Identifier | Yes | System / User | Must exist or be generated within authorized scope | Core reference for Schedule Automated Report |
| Organization ID | Tenant Organization context | Identifier | Conditional | Session / System | Must be authorized | Enforces data isolation |
| Status | Current lifecycle or processing status | Enum | Yes | System | Must follow permitted transitions | Drives UI and downstream behavior |
| Effective Date | Date and time when the action applies | DateTime | Conditional | User / System | Must satisfy policy | Supports immediate or scheduled processing |
| Rule / Policy Reference | Governing configuration or policy | Identifier | Conditional | System | Must be active where required | Links operational governance |
| Reason / Remarks | Business explanation | Text | Conditional | User | Required for governed changes | Stored for audit and support |
| Source Reference | Upstream workflow, job, or event source | Identifier | Conditional | System | Must be traceable | Supports cross-module traceability |

### Main Flow

1. Actor opens Report Schedule or the related workflow, or the System receives the scheduled or event-driven trigger.
2. The system validates authentication, authorization, tenant scope, and current lifecycle state.
3. The system loads required Reporting data, related configuration, and policy controls.
4. Actor or System provides the required input for Schedule Automated Report.
5. The system validates mandatory fields, BA-02 rules, ownership, lifecycle status, security scope, and downstream dependencies.
6. The system executes Schedule Automated Report and persists the resulting state, transaction, report, or history record.
7. The system synchronizes related modules and reporting datasets where applicable.
8. The system emits business events and notification events where configured.
9. The system records immutable audit events with actor, timestamp, source, scope, outcome, and changed values where applicable.
10. The system displays or returns completion confirmation with reference number and final status.

### Alternate Flows

- If approval is required, the system routes the request to the configured approver and holds processing until approval is completed.
- If processing is scheduled, the system stores the future action and executes it through a monitored scheduler.
- If the action is read-only or analytical, the system renders authorized information without changing source transactions.
- If notification or reporting update is not configured, the system skips that downstream action while preserving audit traceability.

### Exception Flows

- If authorization fails, the system denies the request and records a security audit event.
- If required data is missing or invalid, the system blocks processing and displays field-level errors.
- If BA-02 policy validation fails, the system rejects the request or routes for approved override where configuration permits.
- If a dependent service fails, the system fails safely, prevents inconsistent partial updates, and records the failure for support review.
- If notification delivery or report export fails after the core transaction succeeds, the transaction remains valid and the failure is logged for retry.

### Outputs

- Dashboard state, transaction, report, or history updated according to the action.
- Lifecycle status and processing outcome recorded.
- Related history and reporting records synchronized where applicable.
- Notifications generated where configured.
- Business events emitted.
- Audit events recorded.

### UI Behaviour

Report Schedule shall show scoped context, lifecycle status, mandatory fields, validation messages, policy warnings, available actions, read-only states, confirmation prompts, filters or pagination where applicable, and responsive behavior for administrative and operational users.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-RPT-010-001 | Actor or system process must be authorized to execute Schedule Automated Report. | Deny request and audit. | Critical |
| VAL-RPT-010-002 | Record scope must remain within authorized tenant and Organization boundaries. | Deny request. | Critical |
| VAL-RPT-010-003 | Mandatory input fields must be complete and valid. | Block processing. | Critical |
| VAL-RPT-010-004 | Applicable BA-02 lifecycle, security, retention, reporting, notification, and audit rules must pass. | Reject or route for approval. | High |
| VAL-RPT-010-005 | Historical, reporting, and audit records must be preserved. | Roll back or mark for controlled recovery. | Critical |

### Business Rules

- BA-02 BR-RPT-001
- BA-02 BR-RPT-004
- BA-02 BR-RPT-005
- BA-02 BR-NOT-001

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| rpt.schedule.automated.report.view | Organization Administrator | Read | View Schedule Automated Report context |
| rpt.schedule.automated.report.execute | Organization Administrator | Execute | Execute Schedule Automated Report |
| rpt.schedule.automated.report.approve | Platform Administrator / Organization Administrator | Approve | Approve governed exceptions where configured |
| rpt.schedule.automated.report.audit.view | Platform Administrator / Organization Administrator | Read | Review audit trace |

### Security Considerations

The capability shall enforce authentication, role-based authorization, least privilege, tenant isolation, sensitive data masking, secure integration references, tamper-resistant audit logging, and retention-aware access control.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Schedule Automated Report Completed | Configured stakeholders | In-App / Email | Action completes | Include reference, final status, and effective date where applicable |
| Schedule Automated Report Requires Action | Responsible owner or approver | In-App / Email | Approval, review, retry, or exception is required | Include safe summary and next action |
| Schedule Automated Report Failed | Actor or support owner | In-App / Email | Validation, job, or integration failure occurs | Include safe failure reason and support reference |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| ScheduleAutomatedReportRequested | Reports & Analytics | Audit Service, Notification Service |
| ScheduleAutomatedReportCompleted | Reports & Analytics | Reporting Service, Notification Service, Audit Service |
| ScheduleAutomatedReportRejectedOrFailed | Reports & Analytics | Support Ticket Management, Audit Service |

### Audit Events

| Audit Event | Description | Actor | Target Entity | Key Data |
|---|---|---|---|---|
| SCHEDULE_AUTOMATED_REPORT_REQUESTED | Schedule Automated Report requested | Organization Administrator / System | Dashboard | Scope, source, and request details |
| SCHEDULE_AUTOMATED_REPORT_COMPLETED | Schedule Automated Report completed | Organization Administrator / System | Dashboard | Previous state, new state, and outcome |
| SCHEDULE_AUTOMATED_REPORT_REJECTED_OR_FAILED | Schedule Automated Report rejected or failed | System | Dashboard | Reason code and recovery reference |

### Reports Generated

- Reports & Analytics Operational Report
- Reports & Analytics History Report
- Reports & Analytics Exception Report
- Executive Dashboard

### Related Screens

- Report Schedule
- Reports & Analytics Dashboard
- Reports & Analytics History
- Audit Log Viewer

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/reports/schedules | POST | Authorized token | Execute Schedule Automated Report | 200 OK or 201 Created with result |
| /api/v1/reports/schedules/history | GET | Authorized token | Retrieve Schedule Automated Report history | 200 OK with history records |
| /api/v1/audit-logs | GET | Authorized token | Retrieve related audit events | 200 OK with scoped audit records |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Dashboard | Create / Update / Read | Support Schedule Automated Report | Governed by tenant and Organization scope |
| Report | Read / Insert / Update | Support Schedule Automated Report | Governed by tenant and Organization scope |
| KPI | Read / Insert / Update | Support Schedule Automated Report | Governed by tenant and Organization scope |
| Analytics Dataset | Read / Insert / Update | Support Schedule Automated Report | Governed by tenant and Organization scope |
| Report Schedule | Read / Insert / Update | Support Schedule Automated Report | Governed by tenant and Organization scope |
| Export History | Read / Insert / Update | Support Schedule Automated Report | Governed by tenant and Organization scope |
| Audit Log | Insert / Read | Record auditable activity | Immutable |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Scheduled | Schedule Automated Report initiated | Running | Organization Administrator / System | Required context captured |
| Running | Validation succeeds | Completed | System | BA-02 rules satisfied |
| Completed | Processing completes | Retry Pending | System | Related updates succeed |
| Completed | Validation or approval fails | Failed | System / Approver | Request rejected or failed |
| Retry Pending | History reviewed | Retry Pending | Authorized user | Read-only traceability |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| RPT-010-001 | Schedule Automated Report cannot be completed because required information is missing. | Missing mandatory data | Complete required fields |
| RPT-010-002 | You do not have permission to perform this action. | Authorization failure | Request access |
| RPT-010-003 | The selected record or policy state is not eligible for this action. | Lifecycle or rule violation | Review current status and policy |
| RPT-010-004 | Schedule Automated Report could not be completed due to a system or integration error. | Processing failure | Retry or contact support |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Execute Schedule Automated Report | Given the actor has permission and valid scope | When valid information is submitted | Then the system shall complete Schedule Automated Report successfully |
| Enforce business rules | Given applicable BA-02 rules are not satisfied | When processing is attempted | Then the system shall reject or route the request according to policy |
| Preserve traceability | Given processing completes or fails | When audit history is reviewed | Then actor, timestamp, source, scope, and outcome shall be visible |
| Protect scope | Given the selected record is outside authorized scope | When the action is requested | Then access shall be denied and audited |

### Dependencies

- All Operational Modules
- Billing & Payment Management
- Membership Management
- Attendance Management
- Subscription Management
- License Management
- Audit Service

### Operational Considerations

Schedule Automated Report should support controlled retries, operational diagnostics, clear exception ownership, and predictable behavior during peak usage, scheduled jobs, or integration delays.

### Non-Functional Considerations

This requirement shall satisfy Digitize expectations for availability, reliability, scalability, performance, security, configurability, maintainability, compliance, and auditability.

### Assumptions

- Required policies and master data are configured by authorized users.
- Related services provide stable APIs for validation, synchronization, reporting, and audit.
- Retention, notification, approval, and exception behavior are governed by Organization or platform policy.

### Success Criteria

Schedule Automated Report is completed accurately, securely, and traceably with downstream records synchronized and no loss of historical or audit integrity.

### Related Functional Requirements

- FR-RPT-001 - View Operational Dashboard
- FR-RPT-002 - Generate Membership Report
- FR-RPT-003 - Generate Attendance Report
- FR-RPT-004 - Generate Revenue Report
- FR-AUD-001 - Record Audit Events
- FR-SEC-001 - Enforce Authentication and Authorization

### Notes

Schedule Automated Report shall remain aligned with the frozen BA source documents and shall not introduce behavior that bypasses security, lifecycle governance, reporting integrity, notification preferences, retention controls, or auditability.

---

## FR-RPT-011 - Monitor Business KPIs

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-RPT-011 |
| Requirement Name | Monitor Business KPIs |
| Functional Module | Reports & Analytics |
| Business Domain | Reporting |
| Business Capability | Performance Monitoring |
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
| Business Requirement | BA-08 BR-024 Reporting and Analytics |
| Business Rule | BA-02 BR-RPT-001, BR-RPT-002, BR-RPT-008, BR-SEC-004 |
| Business Process | BA-03 BP-RPT-011 Monitor Business KPIs |
| Business Process Flow | BA-04 Section 31 Reporting & Analytics Flow |
| Persona | BA-05 Organization Administrator, Facility Manager, Finance Staff, Reception Staff, Platform Administrator |
| User Journey | BA-06 Section 22 Cross Persona Interaction |
| Stakeholder | BA-07 Organization Administrator, Facility Manager, Finance Staff, Platform Administrator |
| Non-Functional Requirement | BA-09 Section 6.4 Reporting Performance, Section 11 Reporting Requirements, Section 3.2 Authorization |
| Assumption / Constraint / Risk | BA-10 BA-RSK-006, BA-RSK-008, BA-RSK-014 |

### Purpose

To provide the Performance Monitoring capability required for Reports & Analytics so Digitize can execute Monitor Business KPIs consistently, securely, and audibly across tenant Organizations and related business modules.

### Functional Requirement

The system shall support Monitor Business KPIs as an atomic Reports & Analytics capability with scoped data capture, BA-02 rule validation, lifecycle handling, permission enforcement, downstream synchronization, notifications, reporting contribution, and immutable audit events.

### Business Justification

Monitor Business KPIs is necessary to maintain enterprise governance, operational continuity, commercial accuracy, customer trust, and traceability for the Reporting domain. The capability ensures approved business processes can run without manual workarounds or ungoverned exceptions.

### Actors

- Organization Administrator
- Platform Administrator
- Organization Administrator
- System
- Notification Service
- Reporting Service
- Audit Service

### Preconditions

- Platform services are available.
- Organization context is active where tenant data is involved.
- Actor is authenticated where the action is user initiated.
- Actor has the required permission for Monitor Business KPIs.
- Required Reporting configuration, policies, and related master data are available.
- Related records required by BA-03 BP-RPT-011 Monitor Business KPIs are within authorized scope.

### Trigger

The requirement is triggered when Organization Administrator or the System initiates Monitor Business KPIs from KPI Dashboard, a related business workflow, a scheduled job, or an approved integration event.

### In Scope

- Retrieve and validate Reporting context.
- Enforce tenant, Organization, Facility, Site, user, and policy scope where applicable.
- Execute Monitor Business KPIs according to BA-02 business rules.
- Persist Dashboard state, transaction, history, or report data.
- Emit business, notification, reporting, and audit events.
- Provide confirmation, exception messaging, and traceability.

### Out of Scope

- Cross-Organization data movement.
- Physical deletion of historical or audit records.
- Rewriting approved Business Analysis documents.
- Low-level implementation design belonging to SAD, API Specification, or Database Design.
- Manual bypass of security, approval, retention, notification, license, reporting, or audit controls.

### Inputs

- Organization ID, where applicable
- Facility ID, where applicable
- Site ID, where applicable
- Dashboard reference
- Actor or system context
- Effective date and time, where applicable
- Status, rule, schedule, recipient, report, or policy details where applicable
- Reason, remarks, or approval reference where governance applies

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Dashboard ID | Primary record reference | Identifier | Yes | System / User | Must exist or be generated within authorized scope | Core reference for Monitor Business KPIs |
| Organization ID | Tenant Organization context | Identifier | Conditional | Session / System | Must be authorized | Enforces data isolation |
| Status | Current lifecycle or processing status | Enum | Yes | System | Must follow permitted transitions | Drives UI and downstream behavior |
| Effective Date | Date and time when the action applies | DateTime | Conditional | User / System | Must satisfy policy | Supports immediate or scheduled processing |
| Rule / Policy Reference | Governing configuration or policy | Identifier | Conditional | System | Must be active where required | Links operational governance |
| Reason / Remarks | Business explanation | Text | Conditional | User | Required for governed changes | Stored for audit and support |
| Source Reference | Upstream workflow, job, or event source | Identifier | Conditional | System | Must be traceable | Supports cross-module traceability |

### Main Flow

1. Actor opens KPI Dashboard or the related workflow, or the System receives the scheduled or event-driven trigger.
2. The system validates authentication, authorization, tenant scope, and current lifecycle state.
3. The system loads required Reporting data, related configuration, and policy controls.
4. Actor or System provides the required input for Monitor Business KPIs.
5. The system validates mandatory fields, BA-02 rules, ownership, lifecycle status, security scope, and downstream dependencies.
6. The system executes Monitor Business KPIs and persists the resulting state, transaction, report, or history record.
7. The system synchronizes related modules and reporting datasets where applicable.
8. The system emits business events and notification events where configured.
9. The system records immutable audit events with actor, timestamp, source, scope, outcome, and changed values where applicable.
10. The system displays or returns completion confirmation with reference number and final status.

### Alternate Flows

- If approval is required, the system routes the request to the configured approver and holds processing until approval is completed.
- If processing is scheduled, the system stores the future action and executes it through a monitored scheduler.
- If the action is read-only or analytical, the system renders authorized information without changing source transactions.
- If notification or reporting update is not configured, the system skips that downstream action while preserving audit traceability.

### Exception Flows

- If authorization fails, the system denies the request and records a security audit event.
- If required data is missing or invalid, the system blocks processing and displays field-level errors.
- If BA-02 policy validation fails, the system rejects the request or routes for approved override where configuration permits.
- If a dependent service fails, the system fails safely, prevents inconsistent partial updates, and records the failure for support review.
- If notification delivery or report export fails after the core transaction succeeds, the transaction remains valid and the failure is logged for retry.

### Outputs

- Dashboard state, transaction, report, or history updated according to the action.
- Lifecycle status and processing outcome recorded.
- Related history and reporting records synchronized where applicable.
- Notifications generated where configured.
- Business events emitted.
- Audit events recorded.

### UI Behaviour

KPI Dashboard shall show scoped context, lifecycle status, mandatory fields, validation messages, policy warnings, available actions, read-only states, confirmation prompts, filters or pagination where applicable, and responsive behavior for administrative and operational users.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-RPT-011-001 | Actor or system process must be authorized to execute Monitor Business KPIs. | Deny request and audit. | Critical |
| VAL-RPT-011-002 | Record scope must remain within authorized tenant and Organization boundaries. | Deny request. | Critical |
| VAL-RPT-011-003 | Mandatory input fields must be complete and valid. | Block processing. | Critical |
| VAL-RPT-011-004 | Applicable BA-02 lifecycle, security, retention, reporting, notification, and audit rules must pass. | Reject or route for approval. | High |
| VAL-RPT-011-005 | Historical, reporting, and audit records must be preserved. | Roll back or mark for controlled recovery. | Critical |

### Business Rules

- BA-02 BR-RPT-001
- BA-02 BR-RPT-002
- BA-02 BR-RPT-008
- BA-02 BR-SEC-004

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| rpt.monitor.business.kpis.view | Organization Administrator | Read | View Monitor Business KPIs context |
| rpt.monitor.business.kpis.execute | Organization Administrator | Execute | Execute Monitor Business KPIs |
| rpt.monitor.business.kpis.approve | Platform Administrator / Organization Administrator | Approve | Approve governed exceptions where configured |
| rpt.monitor.business.kpis.audit.view | Platform Administrator / Organization Administrator | Read | Review audit trace |

### Security Considerations

The capability shall enforce authentication, role-based authorization, least privilege, tenant isolation, sensitive data masking, secure integration references, tamper-resistant audit logging, and retention-aware access control.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| Monitor Business KPIs Completed | Configured stakeholders | In-App / Email | Action completes | Include reference, final status, and effective date where applicable |
| Monitor Business KPIs Requires Action | Responsible owner or approver | In-App / Email | Approval, review, retry, or exception is required | Include safe summary and next action |
| Monitor Business KPIs Failed | Actor or support owner | In-App / Email | Validation, job, or integration failure occurs | Include safe failure reason and support reference |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| MonitorBusinessKpisRequested | Reports & Analytics | Audit Service, Notification Service |
| MonitorBusinessKpisCompleted | Reports & Analytics | Reporting Service, Notification Service, Audit Service |
| MonitorBusinessKpisRejectedOrFailed | Reports & Analytics | Support Ticket Management, Audit Service |

### Audit Events

| Audit Event | Description | Actor | Target Entity | Key Data |
|---|---|---|---|---|
| MONITOR_BUSINESS_KPIS_REQUESTED | Monitor Business KPIs requested | Organization Administrator / System | Dashboard | Scope, source, and request details |
| MONITOR_BUSINESS_KPIS_COMPLETED | Monitor Business KPIs completed | Organization Administrator / System | Dashboard | Previous state, new state, and outcome |
| MONITOR_BUSINESS_KPIS_REJECTED_OR_FAILED | Monitor Business KPIs rejected or failed | System | Dashboard | Reason code and recovery reference |

### Reports Generated

- Reports & Analytics Operational Report
- Reports & Analytics History Report
- Reports & Analytics Exception Report
- Executive Dashboard

### Related Screens

- KPI Dashboard
- Reports & Analytics Dashboard
- Reports & Analytics History
- Audit Log Viewer

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/reports/kpis | GET | Authorized token | Execute Monitor Business KPIs | 200 OK or 201 Created with result |
| /api/v1/reports/kpis/history | GET | Authorized token | Retrieve Monitor Business KPIs history | 200 OK with history records |
| /api/v1/audit-logs | GET | Authorized token | Retrieve related audit events | 200 OK with scoped audit records |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Dashboard | Read | Support Monitor Business KPIs | Governed by tenant and Organization scope |
| Report | Read / Insert / Update | Support Monitor Business KPIs | Governed by tenant and Organization scope |
| KPI | Read / Insert / Update | Support Monitor Business KPIs | Governed by tenant and Organization scope |
| Analytics Dataset | Read / Insert / Update | Support Monitor Business KPIs | Governed by tenant and Organization scope |
| Report Schedule | Read / Insert / Update | Support Monitor Business KPIs | Governed by tenant and Organization scope |
| Export History | Read / Insert / Update | Support Monitor Business KPIs | Governed by tenant and Organization scope |
| Audit Log | Insert / Read | Record auditable activity | Immutable |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Not Requested | Monitor Business KPIs initiated | Generating | Organization Administrator / System | Required context captured |
| Generating | Validation succeeds | Ready | System | BA-02 rules satisfied |
| Ready | Processing completes | Export Pending | System | Related updates succeed |
| Ready | Validation or approval fails | Failed | System / Approver | Request rejected or failed |
| Export Pending | History reviewed | Export Pending | Authorized user | Read-only traceability |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| RPT-011-001 | Monitor Business KPIs cannot be completed because required information is missing. | Missing mandatory data | Complete required fields |
| RPT-011-002 | You do not have permission to perform this action. | Authorization failure | Request access |
| RPT-011-003 | The selected record or policy state is not eligible for this action. | Lifecycle or rule violation | Review current status and policy |
| RPT-011-004 | Monitor Business KPIs could not be completed due to a system or integration error. | Processing failure | Retry or contact support |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Execute Monitor Business KPIs | Given the actor has permission and valid scope | When valid information is submitted | Then the system shall complete Monitor Business KPIs successfully |
| Enforce business rules | Given applicable BA-02 rules are not satisfied | When processing is attempted | Then the system shall reject or route the request according to policy |
| Preserve traceability | Given processing completes or fails | When audit history is reviewed | Then actor, timestamp, source, scope, and outcome shall be visible |
| Protect scope | Given the selected record is outside authorized scope | When the action is requested | Then access shall be denied and audited |

### Dependencies

- All Operational Modules
- Billing & Payment Management
- Membership Management
- Attendance Management
- Subscription Management
- License Management
- Audit Service

### Operational Considerations

Monitor Business KPIs should support controlled retries, operational diagnostics, clear exception ownership, and predictable behavior during peak usage, scheduled jobs, or integration delays.

### Non-Functional Considerations

This requirement shall satisfy Digitize expectations for availability, reliability, scalability, performance, security, configurability, maintainability, compliance, and auditability.

### Assumptions

- Required policies and master data are configured by authorized users.
- Related services provide stable APIs for validation, synchronization, reporting, and audit.
- Retention, notification, approval, and exception behavior are governed by Organization or platform policy.

### Success Criteria

Monitor Business KPIs is completed accurately, securely, and traceably with downstream records synchronized and no loss of historical or audit integrity.

### Related Functional Requirements

- FR-RPT-001 - View Operational Dashboard
- FR-RPT-002 - Generate Membership Report
- FR-RPT-003 - Generate Attendance Report
- FR-RPT-004 - Generate Revenue Report
- FR-AUD-001 - Record Audit Events
- FR-SEC-001 - Enforce Authentication and Authorization

### Notes

Monitor Business KPIs shall remain aligned with the frozen BA source documents and shall not introduce behavior that bypasses security, lifecycle governance, reporting integrity, notification preferences, retention controls, or auditability.

---

## FR-RPT-012 - View Historical Trends

### Requirement Metadata

| Attribute | Value |
|---|---|
| Requirement ID | FR-RPT-012 |
| Requirement Name | View Historical Trends |
| Functional Module | Reports & Analytics |
| Business Domain | Reporting |
| Business Capability | Business Analytics |
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
| Business Requirement | BA-08 BR-024 Reporting and Analytics |
| Business Rule | BA-02 BR-RPT-001, BR-RPT-002, BR-RPT-004, BR-RPT-008 |
| Business Process | BA-03 BP-RPT-012 View Historical Trends |
| Business Process Flow | BA-04 Section 31 Reporting & Analytics Flow |
| Persona | BA-05 Organization Administrator, Facility Manager, Finance Staff, Reception Staff, Platform Administrator |
| User Journey | BA-06 Section 22 Cross Persona Interaction |
| Stakeholder | BA-07 Organization Administrator, Facility Manager, Finance Staff, Platform Administrator |
| Non-Functional Requirement | BA-09 Section 6.4 Reporting Performance, Section 11 Reporting Requirements, Section 3.2 Authorization |
| Assumption / Constraint / Risk | BA-10 BA-RSK-006, BA-RSK-008, BA-RSK-014 |

### Purpose

To provide the Business Analytics capability required for Reports & Analytics so Digitize can execute View Historical Trends consistently, securely, and audibly across tenant Organizations and related business modules.

### Functional Requirement

The system shall support View Historical Trends as an atomic Reports & Analytics capability with scoped data capture, BA-02 rule validation, lifecycle handling, permission enforcement, downstream synchronization, notifications, reporting contribution, and immutable audit events.

### Business Justification

View Historical Trends is necessary to maintain enterprise governance, operational continuity, commercial accuracy, customer trust, and traceability for the Reporting domain. The capability ensures approved business processes can run without manual workarounds or ungoverned exceptions.

### Actors

- Organization Administrator
- Platform Administrator
- Organization Administrator
- System
- Notification Service
- Reporting Service
- Audit Service

### Preconditions

- Platform services are available.
- Organization context is active where tenant data is involved.
- Actor is authenticated where the action is user initiated.
- Actor has the required permission for View Historical Trends.
- Required Reporting configuration, policies, and related master data are available.
- Related records required by BA-03 BP-RPT-012 View Historical Trends are within authorized scope.

### Trigger

The requirement is triggered when Organization Administrator or the System initiates View Historical Trends from Historical Trends, a related business workflow, a scheduled job, or an approved integration event.

### In Scope

- Retrieve and validate Reporting context.
- Enforce tenant, Organization, Facility, Site, user, and policy scope where applicable.
- Execute View Historical Trends according to BA-02 business rules.
- Persist Dashboard state, transaction, history, or report data.
- Emit business, notification, reporting, and audit events.
- Provide confirmation, exception messaging, and traceability.

### Out of Scope

- Cross-Organization data movement.
- Physical deletion of historical or audit records.
- Rewriting approved Business Analysis documents.
- Low-level implementation design belonging to SAD, API Specification, or Database Design.
- Manual bypass of security, approval, retention, notification, license, reporting, or audit controls.

### Inputs

- Organization ID, where applicable
- Facility ID, where applicable
- Site ID, where applicable
- Dashboard reference
- Actor or system context
- Effective date and time, where applicable
- Status, rule, schedule, recipient, report, or policy details where applicable
- Reason, remarks, or approval reference where governance applies

### Field Definitions

| Field Name | Description | Data Type | Mandatory | Source | Validation | Notes |
|---|---|---|---|---|---|---|
| Dashboard ID | Primary record reference | Identifier | Yes | System / User | Must exist or be generated within authorized scope | Core reference for View Historical Trends |
| Organization ID | Tenant Organization context | Identifier | Conditional | Session / System | Must be authorized | Enforces data isolation |
| Status | Current lifecycle or processing status | Enum | Yes | System | Must follow permitted transitions | Drives UI and downstream behavior |
| Effective Date | Date and time when the action applies | DateTime | Conditional | User / System | Must satisfy policy | Supports immediate or scheduled processing |
| Rule / Policy Reference | Governing configuration or policy | Identifier | Conditional | System | Must be active where required | Links operational governance |
| Reason / Remarks | Business explanation | Text | Conditional | User | Required for governed changes | Stored for audit and support |
| Source Reference | Upstream workflow, job, or event source | Identifier | Conditional | System | Must be traceable | Supports cross-module traceability |

### Main Flow

1. Actor opens Historical Trends or the related workflow, or the System receives the scheduled or event-driven trigger.
2. The system validates authentication, authorization, tenant scope, and current lifecycle state.
3. The system loads required Reporting data, related configuration, and policy controls.
4. Actor or System provides the required input for View Historical Trends.
5. The system validates mandatory fields, BA-02 rules, ownership, lifecycle status, security scope, and downstream dependencies.
6. The system executes View Historical Trends and persists the resulting state, transaction, report, or history record.
7. The system synchronizes related modules and reporting datasets where applicable.
8. The system emits business events and notification events where configured.
9. The system records immutable audit events with actor, timestamp, source, scope, outcome, and changed values where applicable.
10. The system displays or returns completion confirmation with reference number and final status.

### Alternate Flows

- If approval is required, the system routes the request to the configured approver and holds processing until approval is completed.
- If processing is scheduled, the system stores the future action and executes it through a monitored scheduler.
- If the action is read-only or analytical, the system renders authorized information without changing source transactions.
- If notification or reporting update is not configured, the system skips that downstream action while preserving audit traceability.

### Exception Flows

- If authorization fails, the system denies the request and records a security audit event.
- If required data is missing or invalid, the system blocks processing and displays field-level errors.
- If BA-02 policy validation fails, the system rejects the request or routes for approved override where configuration permits.
- If a dependent service fails, the system fails safely, prevents inconsistent partial updates, and records the failure for support review.
- If notification delivery or report export fails after the core transaction succeeds, the transaction remains valid and the failure is logged for retry.

### Outputs

- Dashboard state, transaction, report, or history updated according to the action.
- Lifecycle status and processing outcome recorded.
- Related history and reporting records synchronized where applicable.
- Notifications generated where configured.
- Business events emitted.
- Audit events recorded.

### UI Behaviour

Historical Trends shall show scoped context, lifecycle status, mandatory fields, validation messages, policy warnings, available actions, read-only states, confirmation prompts, filters or pagination where applicable, and responsive behavior for administrative and operational users.

### Validation Rules

| Rule ID | Validation Rule | Error Handling | Severity |
|---|---|---|---|
| VAL-RPT-012-001 | Actor or system process must be authorized to execute View Historical Trends. | Deny request and audit. | Critical |
| VAL-RPT-012-002 | Record scope must remain within authorized tenant and Organization boundaries. | Deny request. | Critical |
| VAL-RPT-012-003 | Mandatory input fields must be complete and valid. | Block processing. | Critical |
| VAL-RPT-012-004 | Applicable BA-02 lifecycle, security, retention, reporting, notification, and audit rules must pass. | Reject or route for approval. | High |
| VAL-RPT-012-005 | Historical, reporting, and audit records must be preserved. | Roll back or mark for controlled recovery. | Critical |

### Business Rules

- BA-02 BR-RPT-001
- BA-02 BR-RPT-002
- BA-02 BR-RPT-004
- BA-02 BR-RPT-008

### Permissions

| Permission | Actor / Role | Access Level | Notes |
|---|---|---|---|
| rpt.view.historical.trends.view | Organization Administrator | Read | View View Historical Trends context |
| rpt.view.historical.trends.execute | Organization Administrator | Execute | Execute View Historical Trends |
| rpt.view.historical.trends.approve | Platform Administrator / Organization Administrator | Approve | Approve governed exceptions where configured |
| rpt.view.historical.trends.audit.view | Platform Administrator / Organization Administrator | Read | Review audit trace |

### Security Considerations

The capability shall enforce authentication, role-based authorization, least privilege, tenant isolation, sensitive data masking, secure integration references, tamper-resistant audit logging, and retention-aware access control.

### Notifications

| Notification Event | Recipient | Channel | Trigger | Template / Content Rule |
|---|---|---|---|---|
| View Historical Trends Completed | Configured stakeholders | In-App / Email | Action completes | Include reference, final status, and effective date where applicable |
| View Historical Trends Requires Action | Responsible owner or approver | In-App / Email | Approval, review, retry, or exception is required | Include safe summary and next action |
| View Historical Trends Failed | Actor or support owner | In-App / Email | Validation, job, or integration failure occurs | Include safe failure reason and support reference |

### Business Events

| Event | Producer | Consumer |
|---|---|---|
| ViewHistoricalTrendsRequested | Reports & Analytics | Audit Service, Notification Service |
| ViewHistoricalTrendsCompleted | Reports & Analytics | Reporting Service, Notification Service, Audit Service |
| ViewHistoricalTrendsRejectedOrFailed | Reports & Analytics | Support Ticket Management, Audit Service |

### Audit Events

| Audit Event | Description | Actor | Target Entity | Key Data |
|---|---|---|---|---|
| VIEW_HISTORICAL_TRENDS_REQUESTED | View Historical Trends requested | Organization Administrator / System | Dashboard | Scope, source, and request details |
| VIEW_HISTORICAL_TRENDS_COMPLETED | View Historical Trends completed | Organization Administrator / System | Dashboard | Previous state, new state, and outcome |
| VIEW_HISTORICAL_TRENDS_REJECTED_OR_FAILED | View Historical Trends rejected or failed | System | Dashboard | Reason code and recovery reference |

### Reports Generated

- Reports & Analytics Operational Report
- Reports & Analytics History Report
- Reports & Analytics Exception Report
- Executive Dashboard

### Related Screens

- Historical Trends
- Reports & Analytics Dashboard
- Reports & Analytics History
- Audit Log Viewer

### Related APIs

| API | Method | Authentication | Purpose | Response |
|---|---|---|---|---|
| /api/v1/reports/trends | GET | Authorized token | Execute View Historical Trends | 200 OK or 201 Created with result |
| /api/v1/reports/trends/history | GET | Authorized token | Retrieve View Historical Trends history | 200 OK with history records |
| /api/v1/audit-logs | GET | Authorized token | Retrieve related audit events | 200 OK with scoped audit records |

### Related Database Entities

| Entity | Operation | Purpose | Notes |
|---|---|---|---|
| Dashboard | Read | Support View Historical Trends | Governed by tenant and Organization scope |
| Report | Read / Insert / Update | Support View Historical Trends | Governed by tenant and Organization scope |
| KPI | Read / Insert / Update | Support View Historical Trends | Governed by tenant and Organization scope |
| Analytics Dataset | Read / Insert / Update | Support View Historical Trends | Governed by tenant and Organization scope |
| Report Schedule | Read / Insert / Update | Support View Historical Trends | Governed by tenant and Organization scope |
| Export History | Read / Insert / Update | Support View Historical Trends | Governed by tenant and Organization scope |
| Audit Log | Insert / Read | Record auditable activity | Immutable |

### State Transitions

| Current State | Action / Event | Next State | Actor | Rule / Condition |
|---|---|---|---|---|
| Not Requested | View Historical Trends initiated | Generating | Organization Administrator / System | Required context captured |
| Generating | Validation succeeds | Ready | System | BA-02 rules satisfied |
| Ready | Processing completes | Export Pending | System | Related updates succeed |
| Ready | Validation or approval fails | Failed | System / Approver | Request rejected or failed |
| Export Pending | History reviewed | Export Pending | Authorized user | Read-only traceability |

### Error Messages

| Error Code | Error Message | Cause | User Action |
|---|---|---|---|
| RPT-012-001 | View Historical Trends cannot be completed because required information is missing. | Missing mandatory data | Complete required fields |
| RPT-012-002 | You do not have permission to perform this action. | Authorization failure | Request access |
| RPT-012-003 | The selected record or policy state is not eligible for this action. | Lifecycle or rule violation | Review current status and policy |
| RPT-012-004 | View Historical Trends could not be completed due to a system or integration error. | Processing failure | Retry or contact support |

### Acceptance Criteria

| Scenario | Given | When | Then |
|---|---|---|---|
| Execute View Historical Trends | Given the actor has permission and valid scope | When valid information is submitted | Then the system shall complete View Historical Trends successfully |
| Enforce business rules | Given applicable BA-02 rules are not satisfied | When processing is attempted | Then the system shall reject or route the request according to policy |
| Preserve traceability | Given processing completes or fails | When audit history is reviewed | Then actor, timestamp, source, scope, and outcome shall be visible |
| Protect scope | Given the selected record is outside authorized scope | When the action is requested | Then access shall be denied and audited |

### Dependencies

- All Operational Modules
- Billing & Payment Management
- Membership Management
- Attendance Management
- Subscription Management
- License Management
- Audit Service

### Operational Considerations

View Historical Trends should support controlled retries, operational diagnostics, clear exception ownership, and predictable behavior during peak usage, scheduled jobs, or integration delays.

### Non-Functional Considerations

This requirement shall satisfy Digitize expectations for availability, reliability, scalability, performance, security, configurability, maintainability, compliance, and auditability.

### Assumptions

- Required policies and master data are configured by authorized users.
- Related services provide stable APIs for validation, synchronization, reporting, and audit.
- Retention, notification, approval, and exception behavior are governed by Organization or platform policy.

### Success Criteria

View Historical Trends is completed accurately, securely, and traceably with downstream records synchronized and no loss of historical or audit integrity.

### Related Functional Requirements

- FR-RPT-001 - View Operational Dashboard
- FR-RPT-002 - Generate Membership Report
- FR-RPT-003 - Generate Attendance Report
- FR-RPT-004 - Generate Revenue Report
- FR-AUD-001 - Record Audit Events
- FR-SEC-001 - Enforce Authentication and Authorization

### Notes

View Historical Trends shall remain aligned with the frozen BA source documents and shall not introduce behavior that bypasses security, lifecycle governance, reporting integrity, notification preferences, retention controls, or auditability.

---

**End of FR-19 - Reports & Analytics**
