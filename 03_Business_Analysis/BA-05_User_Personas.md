# BA-05 User Personas

**Document ID:** BA-05  
**Document Name:** User Personas  
**Product:** Digitize by OrieOn Technologies Pvt. Ltd.
**Document Type:** Business Analysis  
**Version:** 1.0  
**Status:** Frozen  
**Owner:** Product Management  
**Prepared By:** Product & Business Analysis Team  
**Last Updated:** July 2026

---

# 1. Introduction

The purpose of this document is to define the primary user personas for the Digitize by OrieOn Technologies Pvt. Ltd. platform.

These personas represent the distinct business roles, responsibilities, motivations, and operational contexts that drive product behavior across the enterprise SaaS platform. The document is intended to support Product Management, Business Analysis, Solution Architecture, UI/UX Design, Functional Requirements, Quality Assurance, Implementation, Support, and Training.

Digitize is a configurable multi-tenant platform. As a result, persona definitions must reflect enterprise governance, role-based access, tenant boundaries, operational scope, and future scalability across multiple facility types and business models.

---

# 2. Persona Standards

Every persona in this document shall follow the same structure.

## 2.1 Standard Persona Structure

- Persona Name
- Purpose
- Role Description
- Business Goals
- Primary Responsibilities
- Typical Daily Activities
- Pain Points
- Business Capabilities
- System Permissions
- Accessible Modules
- Frequently Used Screens
- KPIs
- Success Metrics
- Notifications Received
- Reports Used
- Related Business Processes
- Security Considerations
- Future Enhancements
- Persona Notes

## 2.2 Persona Governance Principles

- Personas are defined by business responsibility, not only by job title.
- Personas must align with the business hierarchy in the Product Glossary.
- Personas must remain consistent across BA, FRS, UI/UX, QA, and support documentation.
- Personas must reflect multi-tenant governance and enterprise access control.
- Personas may evolve over time, but terminology must remain stable.
- Future personas may be introduced without changing the core persona framework.

## 2.3 Persona Traceability

This document aligns user personas with business processes, operational flows, user journeys, business rules, and functional scope.

| Persona | BA-03 Process Domains | BA-04 Flows | BA-06 Journeys | BA-02 Rule Categories | BA-01 Business Modules |
|---|---|---|---|---|---|
| Platform Administrator | Platform Processes | Platform Administration Flow | Platform Administrator Journey | Platform | Platform Administration |
| Organization Administrator | Organization Processes | Organization Management Flow | Organization Administrator Journey | Organization | Organization Management |
| Facility Manager | Facility Processes | Facility Management Flow | Facility Manager Journey | Facility | Organization Management |
| Site Administrator | Site Processes | Site Management Flow | Site Administrator Journey | Site | Organization Management |
| Reception Staff | Customer, Membership, Attendance, Billing, Payment Processes | Customer Registration & Management Flow; Membership Purchase Flow; Attendance Management Flow; Billing Management Flow; Payment Management Flow | Reception Staff Journey | Customer, Membership, Attendance, Billing, Payment | Customer Management; Membership Management; Attendance Management; Commercial Management |
| Trainer | Activity & Batch Processes; Personal Training Processes | Activity Management Flow; Batch Management Flow; Personal Training Flow | Trainer Journey | Trainer | Training Management |
| Finance Staff | Billing Processes; Payment Processes | Billing Management Flow; Payment Management Flow; Invoice Management Flow; Refund Management Flow | Finance Staff Journey | Billing; Payment | Commercial Management |
| Marketing Staff | Advertisement Campaign Processes | Advertisement Campaign Flow | Marketing Staff Journey | Commercial | Communication Management |
| Support Executive | Support Ticket Processes | Support Ticket Management Flow | Support Executive Journey | Security; Audit | Support Management |
| Customer | Customer Processes | Customer Journey | Customer Journey | Customer | Customer Management |

---

# 3. Platform Administrator

| Field | Details |
|---|---|
| Persona Name | Platform Administrator |
| Purpose | Govern the SaaS platform, manage tenant onboarding, control subscription and license structures, and maintain global platform health and security. |
| Role Description | The highest-privileged business persona responsible for centralized administration of the Digitize platform. |
| Business Goals | Maintain platform stability, enforce governance, manage commercial enablement, and ensure tenant operations remain compliant and auditable. |
| Primary Responsibilities | Manage platform settings, subscription plans, license templates, feature flags, security policies, platform monitoring, and organization lifecycle actions. |
| Typical Daily Activities | Review platform alerts, approve or reject organization onboarding actions, update global settings, monitor usage, inspect audit logs, and respond to incidents. |
| Pain Points | High governance burden, risk of tenant misconfiguration, security sensitivity, and the need to balance flexibility with strict control. |
| Business Capabilities | Platform Administration, Subscription Management, License Management, Security Governance, Audit Oversight, Executive Reporting. |
| System Permissions | Full platform administration access, tenant lifecycle control, global configuration access, commercial configuration access, and read access to all tenant-level reporting where permitted. |
| Accessible Modules | Platform Administration, Subscription Management, License Management, Audit & Compliance, Reporting & Analytics, Organization Governance. |
| Frequently Used Screens | Platform Dashboard, Organization Review, Subscription Plan Management, License Template Management, Feature Flag Management, Audit Logs, Platform Reports. |
| KPIs | Active organizations, subscription conversion rate, license utilization, platform uptime, security incident count, platform response time. |
| Success Metrics | Platform remains secure and available, tenant onboarding is controlled, commercial plans are accurately managed, and audit records are complete. |
| Notifications Received | Critical platform alerts, onboarding requests, security alerts, subscription events, license events, scheduled maintenance notices. |
| Reports Used | Platform Health Report, Subscription Summary Report, License Utilization Report, Executive Dashboard, Audit Report. |
| Related Business Processes | Platform Administration, Organization Onboarding, Subscription Management, License Management, Audit & Compliance, Reporting & Analytics. |
| Security Considerations | Requires the strongest access control, MFA where enabled, strict audit logging, least-privilege role assignment, and segregation of duties. |
| Future Enhancements | Advanced platform analytics, automated anomaly detection, policy recommendation support, and delegated administrative controls. |
| Persona Notes | This persona is the root governance authority in the tenant ecosystem and must be handled as a high-risk privileged role. |

---

# 4. Organization Administrator

| Field | Details |
|---|---|
| Persona Name | Organization Administrator |
| Purpose | Govern the tenant organization, configure business policies, manage facilities and sites, and oversee staff, customers, and operational performance. |
| Role Description | The primary tenant-side governance persona responsible for managing the organization as the business owner within the platform. |
| Business Goals | Maintain consistent organizational operations, enforce policy, control access, protect brand identity, and monitor business performance. |
| Primary Responsibilities | Manage organization profile, settings, branding, documents, policies, staff access, facility governance, site governance, and organization-level approvals. |
| Typical Daily Activities | Review dashboards, approve changes, maintain organization records, manage staff and access, review business reports, and handle governance exceptions. |
| Pain Points | Coordinating multiple facilities and sites, avoiding policy drift, controlling approvals, and ensuring all changes are auditable. |
| Business Capabilities | Organization Management, Facility Management, Site Management, Staff Administration, Approval Governance, Compliance Oversight, Business Reporting. |
| System Permissions | Organization-level create, update, approve, configure, and review permissions across permitted facilities and sites. |
| Accessible Modules | Organization Management, Facility Management, Site Management, Staff Identity & Access, Approval Workflow, Reporting & Analytics, Audit & Compliance. |
| Frequently Used Screens | Organization Dashboard, Organization Profile, Business Policy Management, Branding Management, Document Management, Facility Dashboard, Site Dashboard. |
| KPIs | Organization growth, facility utilization, site utilization, staff coverage, approval turnaround time, policy compliance, customer retention. |
| Success Metrics | Organization remains consistent, policy-compliant, operationally visible, and well governed across all subordinate business units. |
| Notifications Received | Approval requests, policy changes, facility alerts, site alerts, document events, customer or staff exceptions. |
| Reports Used | Organization Summary Report, Business Performance Report, Policy Compliance Report, Operational Dashboard, Executive Dashboard. |
| Related Business Processes | Organization Management, Facility Management, Site Management, Staff Identity & Access Management, Approval Workflow, Reporting & Analytics. |
| Security Considerations | Access must be constrained to the Organization scope, with approval authority clearly separated from platform-wide privileges. |
| Future Enhancements | Delegated approval roles, policy simulation, automated governance alerts, and organization-level self-service analytics. |
| Persona Notes | This is the central tenant governance role and a key decision-maker across most configuration workflows. |

---

# 5. Facility Manager

| Field | Details |
|---|---|
| Persona Name | Facility Manager |
| Purpose | Manage the operational performance of a Facility, coordinate resources, monitor service delivery, and enforce Facility-level business rules. |
| Role Description | The operational owner for a Facility, responsible for balancing service delivery, operational capacity, and business performance. |
| Business Goals | Run the facility efficiently, maintain operational standards, optimize capacity usage, and support service quality. |
| Primary Responsibilities | Manage facility settings, oversee activities and batches, allocate trainers, monitor utilization, review performance, and handle operational exceptions. |
| Typical Daily Activities | Check facility dashboard, review activity schedules, inspect occupancy, coordinate trainers, monitor alerts, and resolve local operational issues. |
| Pain Points | Capacity pressure, schedule conflicts, trainer availability issues, service disruptions, and the need for rapid response. |
| Business Capabilities | Facility Administration, Activity Management, Batch Management, Capacity Management, Operational Monitoring, Performance Analysis. |
| System Permissions | Facility-level configuration access, operational monitoring access, activity and batch control access, and read access to performance data. |
| Accessible Modules | Facility Management, Activity & Batch Management, Attendance Management, Reporting & Analytics, Notification. |
| Frequently Used Screens | Facility Dashboard, Activity Management, Batch Schedule, Capacity Limits, Trainer Allocation, Facility Reports. |
| KPIs | Occupancy rate, batch utilization, attendance rate, trainer utilization, service completion rate, facility revenue contribution. |
| Success Metrics | Facility operates within policy, services are delivered on time, resources are used efficiently, and performance metrics are visible. |
| Notifications Received | Capacity alerts, schedule changes, trainer changes, session cancellations, operational exceptions, escalation notices. |
| Reports Used | Facility Summary Report, Activity Performance Report, Batch Occupancy Report, Trainer Utilization Report, Operational Dashboard. |
| Related Business Processes | Facility Management, Activity Management, Batch Management, Attendance Management, Reporting & Analytics, Notification. |
| Security Considerations | Access must be restricted to assigned facilities and must not exceed organizational authorization scope. |
| Future Enhancements | Predictive occupancy planning, automated resource balancing, and facility performance benchmarking. |
| Persona Notes | This role bridges organizational governance and day-to-day facility execution. |

---

# 6. Site Administrator

| Field | Details |
|---|---|
| Persona Name | Site Administrator |
| Purpose | Administer a physical Site, support branch-level operations, and ensure local configuration remains aligned with Facility policy. |
| Role Description | The site-level governance persona responsible for managing the execution environment for a specific branch or location. |
| Business Goals | Maintain site readiness, ensure local compliance, coordinate staff and operations, and provide accurate site-level reporting. |
| Primary Responsibilities | Manage site settings, operating hours, documents, capacity, local policies, and site-level operational exceptions. |
| Typical Daily Activities | Review site operations, check capacity, monitor schedules, coordinate staff, update documents, and manage site-specific issues. |
| Pain Points | Local operational interruptions, capacity constraints, policy inconsistencies, and branch-specific exceptions. |
| Business Capabilities | Site Administration, Site Configuration, Branch Operations, Site Monitoring, Local Policy Management. |
| System Permissions | Site-scoped configuration, document management, operational monitoring, and limited administrative actions within the assigned site. |
| Accessible Modules | Site Management, Attendance Management, Activity & Batch Management, Reporting & Analytics, Notification. |
| Frequently Used Screens | Site Dashboard, Site Profile, Site Settings, Site Operating Hours, Site Capacity, Site Documents. |
| KPIs | Site occupancy, local attendance, service completion, site alert count, branch utilization, local exception resolution time. |
| Success Metrics | Site remains operational, policy-compliant, and aligned with Facility expectations. |
| Notifications Received | Site alerts, schedule changes, capacity warnings, approval requests, and operational exceptions. |
| Reports Used | Site Summary Report, Daily Operations Report, Site Utilization Report, Site Compliance Report. |
| Related Business Processes | Site Management, Attendance Management, Reporting & Analytics, Notification, Approval Workflow. |
| Security Considerations | Must be limited to the assigned site scope and inherit policy constraints from the parent Facility and Organization. |
| Future Enhancements | Site-specific operational automation, branch benchmarking, and location-based service optimization. |
| Persona Notes | This role is essential for multi-branch organizations that require local execution with central governance. |

---

# 7. Reception Staff

| Field | Details |
|---|---|
| Persona Name | Reception Staff |
| Purpose | Execute front-office operations including customer registration, membership handling, attendance, billing, and payment collection. |
| Role Description | The primary transactional persona for customer-facing operational workflows at the Facility or Site. |
| Business Goals | Deliver fast and accurate customer service, minimize queues, and ensure operational records are complete and correct. |
| Primary Responsibilities | Register customers, update profiles, record attendance, manage walk-ins, sell and renew memberships, generate invoices, and collect payments. |
| Typical Daily Activities | Search customers, check in customers, create memberships, issue invoices, collect payments, record walk-ins, and handle service questions. |
| Pain Points | Peak-hour transaction pressure, incomplete customer data, payment exceptions, and the need for rapid yet accurate processing. |
| Business Capabilities | Customer Management, Membership Management, Attendance Management, Billing Management, Payment Management, Walk-in Management. |
| System Permissions | Front-office create, update, record, and view permissions within assigned organizational scope. |
| Accessible Modules | Customer Management, Membership Management, Attendance Management, Billing, Payment, Notification, Support Tickets. |
| Frequently Used Screens | Customer Search, Customer Profile, Membership Purchase, Attendance Check-in, Walk-in Registration, Invoice Management, Payment Collection. |
| KPIs | Transaction accuracy, queue time, customer service time, payment completion rate, attendance recording accuracy. |
| Success Metrics | Customers are served quickly, records are accurate, and front-office operations are completed without rework. |
| Notifications Received | Membership updates, attendance confirmations, payment confirmations, customer alerts, operational reminders. |
| Reports Used | Daily Front Desk Report, Attendance Report, Billing Summary, Walk-in Report, Customer Activity Summary. |
| Related Business Processes | Customer Registration & Management, Membership Purchase, Attendance Management, Walk-in Customer Flow, Billing Management, Payment Management. |
| Security Considerations | Should have restricted access to financial and customer data based on organizational scope and assigned privileges. |
| Future Enhancements | Guided front-desk worklists, smart customer lookup, and queue optimization support. |
| Persona Notes | This is one of the highest-volume operational personas and requires efficient, low-friction workflows. |

---

# 8. Trainer

| Field | Details |
|---|---|
| Persona Name | Trainer |
| Purpose | Deliver training sessions, manage customer progress, and support coaching-based services across batches and personal training engagements. |
| Role Description | The service-delivery persona responsible for operational execution of structured training and coaching activities. |
| Business Goals | Deliver high-quality training, track progress, maintain session discipline, and support customer development. |
| Primary Responsibilities | Start and complete sessions, record training notes, update customer progress, review schedules, and support service quality. |
| Typical Daily Activities | Review schedule, conduct sessions, mark completion, record notes, update progress, and coordinate with operational teams. |
| Pain Points | Schedule changes, trainer overlaps, missing attendance context, and the need to maintain accurate coaching records. |
| Business Capabilities | Session Delivery, Progress Tracking, Training Documentation, Attendance Recording, Trainer Performance Support. |
| System Permissions | Session execution, progress entry, notes entry, limited schedule visibility, and read access to assigned customer information. |
| Accessible Modules | Activity & Batch Management, Personal Training, Attendance Management, Reporting & Analytics, Notification. |
| Frequently Used Screens | Session Schedule, Batch Schedule, Training Session, Training Notes, Customer Progress, Training History. |
| KPIs | Session completion rate, customer attendance, customer progress updates, schedule adherence, trainer utilization. |
| Success Metrics | Sessions are delivered on time, progress is documented, and customer engagement improves over time. |
| Notifications Received | Session reminders, schedule changes, customer cancellations, session status updates, trainer assignments. |
| Reports Used | Trainer Performance Report, Session Completion Report, Training History Report, Utilization Summary. |
| Related Business Processes | Activity Management, Batch Management, Personal Training, Attendance Management, Reporting & Analytics. |
| Security Considerations | Access must be limited to assigned sessions, customers, and facilities, with strong protection for customer progress data. |
| Future Enhancements | AI-assisted session planning, progress trend analytics, and digital coach notes enhancement. |
| Persona Notes | The Trainer is a key experience owner for premium and structured service delivery. |

---

# 9. Finance Staff

| Field | Details |
|---|---|
| Persona Name | Finance Staff |
| Purpose | Manage billing validation, payment settlement, refunds, reconciliations, receivables, and financial reporting support. |
| Role Description | The commercial control persona responsible for financial integrity across invoicing, collections, and refunds. |
| Business Goals | Ensure accurate billing, secure collections, controlled refunds, and reliable financial visibility. |
| Primary Responsibilities | Review invoices, collect payments, process refunds, reconcile transactions, monitor balances, and generate statements. |
| Typical Daily Activities | Check payment queues, validate receipts, reconcile collections, process refund requests, and review outstanding balances. |
| Pain Points | Multi-channel reconciliation, partial payment handling, refund approvals, and keeping records synchronized across operations. |
| Business Capabilities | Billing Management, Payment Management, Refund Management, Receivables Management, Financial Reporting. |
| System Permissions | Finance-scoped billing, payment, refund, and reconciliation permissions with audit tracing. |
| Accessible Modules | Billing, Payment, Invoice Management, Refund Management, Reporting & Analytics, Audit & Compliance. |
| Frequently Used Screens | Invoice Management, Payment Collection, Payment History, Refund Management, Outstanding Statement, Financial Dashboard. |
| KPIs | Collection rate, settlement accuracy, refund turnaround time, outstanding balance rate, reconciliation variance. |
| Success Metrics | Financial records remain accurate, payments reconcile successfully, and refunds follow policy. |
| Notifications Received | Payment confirmations, failed payments, refund requests, outstanding balance alerts, reconciliation exceptions. |
| Reports Used | Revenue Report, Payment Report, Refund Report, Outstanding Statement, Financial Dashboard. |
| Related Business Processes | Billing Management, Payment Management, Invoice Management, Refund Management, Reporting & Analytics. |
| Security Considerations | Requires strict authorization, separation of duties, and immutable financial records with complete audit trails. |
| Future Enhancements | Automated reconciliation, financial anomaly detection, and revenue forecasting support. |
| Persona Notes | This role directly affects revenue integrity and must be controlled with strong governance. |

---

# 10. Marketing Staff

| Field | Details |
|---|---|
| Persona Name | Marketing Staff |
| Purpose | Plan, configure, and monitor promotional campaigns and customer communications that drive acquisition, retention, and engagement. |
| Role Description | The marketing execution persona responsible for campaign targeting, delivery coordination, and performance review. |
| Business Goals | Increase customer acquisition, improve retention, promote offers, and measure marketing impact. |
| Primary Responsibilities | Create campaigns, select audiences, configure messages, submit for approval, monitor performance, and generate campaign reports. |
| Typical Daily Activities | Draft campaign content, refine audience segments, schedule delivery, review approvals, and analyze engagement data. |
| Pain Points | Approval delays, unclear audience definitions, fragmented channel performance, and difficulty proving campaign ROI. |
| Business Capabilities | Campaign Management, Audience Segmentation, Communication Planning, Marketing Analytics, Campaign Governance. |
| System Permissions | Campaign creation and configuration permissions, audience filtering access, and reporting access within scope. |
| Accessible Modules | Advertisement Campaign, Notification Management, Reporting & Analytics, Approval Workflow. |
| Frequently Used Screens | Campaign Management, Audience Selection, Campaign Scheduling, Delivery Tracking, Campaign Reports. |
| KPIs | Delivery rate, open rate, click-through rate, conversion rate, campaign ROI, customer response rate. |
| Success Metrics | Campaigns are approved, delivered, and measurable, with clear contribution to business outcomes. |
| Notifications Received | Approval updates, scheduled delivery status, failed deliveries, campaign completion notices. |
| Reports Used | Campaign Performance Report, Marketing Report, Conversion Summary, Audience Response Report. |
| Related Business Processes | Advertisement Campaign Flow, Notification Management, Approval Workflow, Reporting & Analytics. |
| Security Considerations | Campaign content and audience data must be protected, especially where customer communication preferences or personal data are involved. |
| Future Enhancements | AI-driven audience recommendations, campaign optimization support, and cross-channel attribution analytics. |
| Persona Notes | Marketing activity must be governed to prevent unapproved or non-compliant customer communications. |

---

# 11. Support Executive

| Field | Details |
|---|---|
| Persona Name | Support Executive |
| Purpose | Handle support tickets, investigate issues, communicate with users, and support timely issue resolution. |
| Role Description | The operational support persona responsible for ticket processing and customer or staff issue handling. |
| Business Goals | Resolve issues quickly, maintain service quality, follow SLA commitments, and preserve complete support records. |
| Primary Responsibilities | Accept tickets, update progress, request information, resolve issues, communicate with users, and support closure workflows. |
| Typical Daily Activities | Review assigned tickets, respond to customers, investigate issues, document findings, and update resolution status. |
| Pain Points | Incomplete ticket details, SLA pressure, repeated escalations, and cross-team dependencies. |
| Business Capabilities | Ticket Handling, Incident Management, SLA Monitoring, Customer Communication, Escalation Support, Support Analytics. |
| System Permissions | Ticket-specific view, update, comment, attach, resolve, and communicate permissions within assigned scope. |
| Accessible Modules | Support Ticket Management, Notification, Reporting & Analytics, Audit & Compliance. |
| Frequently Used Screens | Support Ticket Queue, Ticket Details, Ticket Comments, Escalation View, Support Dashboard. |
| KPIs | First response time, resolution time, SLA compliance, reopen rate, customer satisfaction, ticket throughput. |
| Success Metrics | Tickets are resolved efficiently, communication is timely, and historical issue records remain accurate. |
| Notifications Received | New assignments, escalations, SLA warnings, customer responses, closure or reopen events. |
| Reports Used | Support Summary Report, SLA Report, Ticket Aging Report, Resolution Report. |
| Related Business Processes | Support Ticket Management, Notification Management, Reporting & Analytics, Audit & Compliance. |
| Security Considerations | Access must be limited to assigned tickets and related business context, with internal notes protected from customers. |
| Future Enhancements | Intelligent ticket routing, AI-assisted suggested responses, and knowledge-base integration. |
| Persona Notes | This persona is customer-facing and must maintain high communication quality and traceability. |

---

# 12. Customer

| Field | Details |
|---|---|
| Persona Name | Customer |
| Purpose | Consume services offered by the Organization, including memberships, attendance, personal training, billing interactions, and communications. |
| Role Description | The external service consumer who interacts with the platform through front-office, digital, and communication touchpoints. |
| Business Goals | Access services easily, understand entitlements, complete payments, receive timely communication, and maintain a positive experience. |
| Primary Responsibilities | Maintain accurate information where required, follow membership rules, attend services, respond to notifications, and raise support issues when needed. |
| Typical Daily Activities | Check membership status, book or attend sessions, review notifications, make payments, and contact support if required. |
| Pain Points | Unclear entitlement status, delayed communication, difficult payment experiences, and friction during check-in or booking. |
| Business Capabilities | Service Consumption, Membership Participation, Attendance, Payment Completion, Communication Response, Support Interaction. |
| System Permissions | Limited self-service access to personal profile, membership, payment, notifications, and support history where enabled. |
| Accessible Modules | Customer Portal, Membership Views, Attendance Views, Payment Views, Notification Center, Support Ticket Submission. |
| Frequently Used Screens | Customer Dashboard, Membership Details, Attendance History, Payment History, Notifications, Support Request. |
| KPIs | Service usage frequency, attendance consistency, payment completion rate, engagement with notifications, support resolution satisfaction. |
| Success Metrics | Services are accessible, entitlements are clear, communication is timely, and support is responsive. |
| Notifications Received | Membership confirmations, renewal reminders, payment confirmations, attendance confirmations, schedule updates, support updates. |
| Reports Used | Customer History View, Membership Summary, Payment Receipt View, Attendance Summary, Support History. |
| Related Business Processes | Customer Registration & Management, Membership Purchase, Attendance Management, Billing Management, Payment Management, Support Ticket Management. |
| Security Considerations | Personal data, payment-related data, and access entitlements must be protected with strong privacy and identity controls. |
| Future Enhancements | Self-service profile management, mobile-first engagement, digital wallet support, and smart service recommendations. |
| Persona Notes | The Customer is the primary external consumer of platform value and should experience a simple, trustworthy service journey. |

---

# 13. Parent / Guardian (Future)

| Field | Details |
|---|---|
| Persona Name | Parent / Guardian (Future) |
| Purpose | Manage service access, payments, communication, and attendance-related responsibility for dependent customers such as children or minors. |
| Role Description | A future external persona that will represent a responsible adult linked to one or more dependent customers. |
| Business Goals | Monitor dependent service usage, authorize participation, receive communications, and manage financial responsibility where applicable. |
| Primary Responsibilities | Approve participation, review schedules, receive notifications, manage payments, and maintain guardian information. |
| Typical Daily Activities | Review child or dependent schedules, approve forms, monitor attendance, respond to alerts, and review payments. |
| Pain Points | Need for visibility across dependents, consent and authorization complexity, and multi-child management overhead. |
| Business Capabilities | Dependent Management, Consent Management, Communication Oversight, Payment Oversight, Attendance Visibility. |
| System Permissions | Future scoped access to dependent profiles, attendance, payments, and notifications with strict consent controls. |
| Accessible Modules | Future Guardian Portal, Dependent Profile Views, Notifications, Payment Views, Consent Management. |
| Frequently Used Screens | Dependent Dashboard, Consent Forms, Attendance Summary, Payment Overview, Notification Center. |
| KPIs | Consent completion rate, attendance visibility, payment compliance, message response rate. |
| Success Metrics | Guardian can oversee dependent participation safely and efficiently. |
| Notifications Received | Attendance alerts, payment reminders, consent requests, schedule changes, support updates. |
| Reports Used | Dependent Attendance Report, Consent Status Report, Payment Summary, Communication History. |
| Related Business Processes | Future Customer Relationship Enhancements, Attendance Management, Billing Management, Payment Management, Notification Management. |
| Security Considerations | Must enforce consent, age-based access rules, and strict separation between guardian and dependent records. |
| Future Enhancements | Multi-dependent dashboards, consent workflows, and guardian-specific mobile experience. |
| Persona Notes | This persona is not active in the current baseline but is included for future expansion into child-centric business models. |

---

# 14. External Auditor (Future)

| Field | Details |
|---|---|
| Persona Name | External Auditor (Future) |
| Purpose | Review business records, compliance evidence, and audit trails for external governance, statutory, or contractual assurance. |
| Role Description | A future read-only persona for independent review of controls, transactions, and compliance evidence. |
| Business Goals | Validate compliance, inspect records, review controls, and confirm historical integrity. |
| Primary Responsibilities | Review reports, inspect audit trails, verify records, and produce independent observations. |
| Typical Daily Activities | Examine compliance reports, review logs, inspect configuration history, and validate evidence samples. |
| Pain Points | Need for controlled access, evidence traceability, and limited but sufficient visibility. |
| Business Capabilities | Audit Review, Compliance Review, Evidence Validation, Historical Inspection. |
| System Permissions | Future read-only access to selected audit, reporting, and evidence repositories with export restrictions. |
| Accessible Modules | Future Auditor Portal, Audit & Compliance, Reporting & Analytics, Document Review. |
| Frequently Used Screens | Audit Logs, Compliance Reports, Configuration History, Evidence Register, Report Exports. |
| KPIs | Review coverage, evidence completeness, issue identification rate, compliance exception count. |
| Success Metrics | Auditor can independently verify records without compromising data integrity or tenant isolation. |
| Notifications Received | Future audit assignment notices, evidence availability alerts, compliance review requests. |
| Reports Used | Compliance Report, Audit Report, Configuration Change Report, Retention Report. |
| Related Business Processes | Audit & Compliance, Reporting & Analytics, Approval Workflow, Organization Governance. |
| Security Considerations | Must be read-only, time-bound, scope-limited, and fully audited with export control. |
| Future Enhancements | External auditor workspace, evidence packaging, and controlled attestations. |
| Persona Notes | This persona is reserved for future compliance and assurance scenarios. |

---

# 15. Third-Party Integration User (Future)

| Field | Details |
|---|---|
| Persona Name | Third-Party Integration User (Future) |
| Purpose | Represent an external system or partner actor that exchanges data with Digitize through approved integrations. |
| Role Description | A future technical-commercial persona for controlled external access through APIs or integration workflows. |
| Business Goals | Exchange trusted data, automate workflows, reduce manual effort, and maintain reliable integration behavior. |
| Primary Responsibilities | Send and receive approved data, authenticate integration requests, handle callbacks, and respect integration policies. |
| Typical Daily Activities | Push or consume service events, synchronize records, process webhooks, and monitor integration health. |
| Pain Points | Authentication failures, schema mismatches, retry handling, rate limits, and versioning changes. |
| Business Capabilities | Integration Access, Data Exchange, Webhook Handling, API Consumption, Sync Monitoring. |
| System Permissions | Future API-scoped permissions with token-based, least-privilege, and tenant-bound access. |
| Accessible Modules | Future Integration Console, API Gateway, Webhook Monitoring, Integration Audit. |
| Frequently Used Screens | Integration Setup, API Credentials, Webhook Logs, Sync Status, Error Queue. |
| KPIs | Sync success rate, API availability, error rate, latency, retry success rate. |
| Success Metrics | Integration operates reliably, securely, and with complete traceability. |
| Notifications Received | Integration failures, token expiry notices, webhook retries, sync completion events. |
| Reports Used | Integration Health Report, API Usage Report, Error Log Report, Sync Summary. |
| Related Business Processes | Future Integration Management, Notification, Audit & Compliance, Reporting & Analytics. |
| Security Considerations | Must use strong authentication, scoped access, tenant isolation, rate limiting, and complete API audit logs. |
| Future Enhancements | Partner integration hub, event streaming, and managed connector marketplace. |
| Persona Notes | This persona is not part of the current baseline but is essential for enterprise integration expansion. |

---

# 16. Persona Capability Matrix

| Capability | Platform Admin | Org Admin | Facility Manager | Site Admin | Reception Staff | Trainer | Finance Staff | Marketing Staff | Support Executive | Customer | Parent/Guardian | External Auditor | Integration User |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Platform Administration | Yes | No | No | No | No | No | No | No | No | No | No | No | No |
| Organization Governance | Yes | Yes | No | No | No | No | No | No | No | No | No | No | No |
| Facility Management | Yes | Yes | Yes | No | No | No | No | No | No | No | No | No | No |
| Site Management | Yes | Yes | Yes | Yes | No | No | No | No | No | No | No | No | No |
| Customer Management | No | Yes | No | No | Yes | No | No | No | No | Limited | Limited | No | No |
| Membership Management | No | Yes | No | No | Yes | No | No | No | No | Limited | Limited | No | No |
| Attendance Management | No | Yes | Yes | Yes | Yes | Yes | No | No | No | View Only | View Only | No | No |
| Activity & Batch Management | No | Yes | Yes | No | No | Yes | No | No | No | No | No | No | No |
| Personal Training | No | No | No | No | No | Yes | No | No | No | No | No | No | No |
| Billing & Payment | No | Yes | No | No | Yes | No | Yes | No | No | Limited | Limited | No | No |
| Campaigns | No | Yes | No | No | No | No | No | Yes | No | No | No | No | No |
| Support Tickets | No | Yes | No | No | Yes | No | No | No | Yes | Raise Only | Raise Only | No | No |
| Reporting & Analytics | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Limited | Limited | Read Only | Limited |
| Audit & Compliance | Yes | Yes | Read Only | Read Only | Read Only | Read Only | Read Only | Read Only | Read Only | No | No | Read Only | Read Only |

---

# 17. Persona Interaction Matrix

| Persona | Primary Interactions | Secondary Interactions |
|---|---|---|
| Platform Administrator | Organization Administrator, System, Audit, Reporting | Support Executive, Finance Staff |
| Organization Administrator | Platform Administrator, Facility Manager, Site Administrator, Reception Staff, Finance Staff | Trainer, Marketing Staff, Support Executive |
| Facility Manager | Organization Administrator, Site Administrator, Trainer, Reception Staff | Finance Staff, Support Executive |
| Site Administrator | Facility Manager, Reception Staff, Trainer, Customers | Organization Administrator |
| Reception Staff | Customers, Finance Staff, Trainers, Site Administrator | Support Executive, Organization Administrator |
| Trainer | Reception Staff, Customers, Facility Manager | Site Administrator |
| Finance Staff | Reception Staff, Organization Administrator, System | Support Executive, Platform Administrator |
| Marketing Staff | Organization Administrator, System, Customers | Support Executive, Reporting users |
| Support Executive | Customers, Reception Staff, Organization Administrator, Finance Staff | Platform Administrator |
| Customer | Reception Staff, Trainer, Support Executive, System notifications | Organization Administrator |
| Parent / Guardian (Future) | Customer, Reception Staff, Notification Service | Organization Administrator |
| External Auditor (Future) | Organization Administrator, Platform Administrator, Audit Service | Reporting users |
| Third-Party Integration User (Future) | System APIs, Notification events, Audit logs | Platform Administrator |

---

# 18. Persona Journey Mapping

## 18.1 Journey Overview

The following journey mapping summarizes the highest-value operating path for each persona.

## 18.2 Journey Paths

| Persona | Journey Summary |
|---|---|
| Platform Administrator | Configure platform, onboard organization, govern subscription and license models, monitor health, and review compliance. |
| Organization Administrator | Configure organization, manage facilities and sites, govern staff, approve changes, and monitor organizational performance. |
| Facility Manager | Operate facility, manage activities and batches, monitor capacity, coordinate resources, and review performance. |
| Site Administrator | Manage branch operations, local settings, and site readiness while enforcing inherited policy. |
| Reception Staff | Register customers, process memberships, record attendance, manage billing, and collect payments. |
| Trainer | Deliver sessions, record attendance, document progress, and manage customer development. |
| Finance Staff | Generate invoices, collect payments, manage refunds, reconcile transactions, and monitor receivables. |
| Marketing Staff | Build campaigns, target audiences, secure approvals, deliver communications, and analyze performance. |
| Support Executive | Receive tickets, investigate issues, communicate progress, resolve incidents, and close cases. |
| Customer | Register, purchase or renew services, attend sessions, receive notifications, pay bills, and request support. |
| Parent / Guardian (Future) | Oversee dependent participation, approvals, payments, and communication. |
| External Auditor (Future) | Review evidence, validate controls, inspect logs, and verify compliance. |
| Third-Party Integration User (Future) | Exchange data through APIs, monitor sync status, and maintain integration health. |

## 18.3 Journey Principles

- Journeys must reflect business hierarchy and role scope.
- Journey steps must remain auditable.
- Journey touchpoints should minimize friction for high-volume roles.
- Journey design must support future expansion without redesigning the core platform.

---

# 19. Persona Security Considerations

## 19.1 Access Control

- Access must be role-based, scope-based, and policy-driven.
- Platform-level privileges must be separated from tenant-level privileges.
- Customer access must remain isolated from staff access.

## 19.2 Auditability

- All persona-driven actions that affect business data must be auditable.
- Administrative and financial actions require stronger traceability.
- Security-related decisions must preserve historical evidence.

## 19.3 Data Isolation

- Personas must not access data belonging to other organizations.
- Site-scoped personas must not exceed assigned site boundaries.
- Future personas must be implemented with least privilege and tenant isolation.

## 19.4 Sensitive Operations

- Platform configuration, billing, refunds, approvals, and support investigations require additional control.
- Communication permissions must respect customer preferences and mandatory notification rules.
- Integration access must be limited by scope, token, and event type.

## 19.5 Future Personas

- Parent / Guardian access must be consent-aware.
- External Auditor access must be read-only and time-bound.
- Third-Party Integration User access must be API-scoped and monitored.

---

# 20. Summary

The User Personas document establishes the principal human and external system-facing personas that interact with the Digitize platform.

It defines role intent, operating scope, responsibilities, permissions, and security considerations in a consistent enterprise format that can be used across product analysis, functional design, UI/UX, development, testing, implementation, and support.

By standardizing persona definitions and aligning them to the enterprise business hierarchy, Digitize maintains a scalable, secure, and role-aware product foundation for current operations and future expansion.

**End of BA-05 - User Personas**
