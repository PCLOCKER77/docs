# PF-02 Domain Model

**Document ID:** PF-02
**Document Name:** Domain Model
**Product:** Digitize by OreeOn Technologies Pvt. Ltd.
**Document Type:** Product Foundation
**Version:** 1.0
**Status:** Approved
**Owner:** Product Management
**Reviewer:** CTO
**Prepared By:** Product & Architecture Team
**Last Updated:** July 2026

---

# 1. Purpose

The purpose of this document is to define the business domain model for the Digitize by OreeOn Technologies Pvt. Ltd. platform.

The Domain Model provides a conceptual representation of the business by identifying the core business domains, their relationships, ownership, responsibilities, and interactions. It establishes a common understanding of how the platform is organized from a business perspective before any technical implementation is considered.

This document serves as the bridge between the **Product Glossary (PF-01)** and the subsequent functional and technical documentation, including the Business Requirements Document (BRD), Functional Requirements Specification (FRS), System Architecture, Database Design, API Specifications, and User Interface Design.

The Domain Model intentionally avoids implementation details such as database tables, APIs, or programming concepts. Instead, it focuses on business objects, their relationships, and the rules that govern them.

---

# 2. Scope

This document covers the complete business domain of the Digitize by OreeOn Technologies Pvt. Ltd. platform.

It defines:

* Core business domains.
* Business hierarchy.
* Domain ownership.
* Domain relationships.
* Business aggregates.
* Domain boundaries.
* Domain events.
* High-level lifecycle models.
* Future domain extensibility.

The document applies to the entire platform, regardless of the Facility Type being managed.

The following Facility Types are within the scope of this domain model:

* Swimming Pools
* Gyms
* Yoga Centres
* Dance Studios
* Badminton Academies
* Football Academies
* Martial Arts Centres
* Indoor Sports Facilities
* Tennis Academies
* Cricket Academies
* Adventure Parks
* Kids Activity Centres
* Wellness Centres

Future Facility Types shall follow the same domain architecture without requiring changes to the core business model.

The following topics are outside the scope of this document:

* User interface design.
* Database schema.
* API definitions.
* Security implementation.
* Technology stack.
* Deployment architecture.
* Infrastructure design.
* Test cases.

These subjects are addressed in their respective documents.

---

# 3. Intended Audience

This document is intended for all stakeholders involved in the planning, design, development, implementation, and maintenance of the Digitize by OreeOn platform.

The primary audience includes:

### Product Management

To understand how business concepts are organized and governed across the platform.

### Business Analysts

To derive detailed business requirements and operational workflows.

### Solution Architects

To establish architectural boundaries and translate the business domain into system architecture.

### Software Engineers

To understand business ownership, relationships, and responsibilities before implementing application logic.

### Database Designers

To design an enterprise data model aligned with business concepts.

### UI/UX Designers

To understand how business domains influence navigation, workflows, and screen organization.

### Quality Assurance Engineers

To validate business scenarios against the intended domain behavior.

### Implementation and Support Teams

To understand the operational structure of customer organizations and facilities during onboarding, deployment, and customer support.

---

# 4. Domain Overview

Digitize by OreeOn Technologies Pvt. Ltd. is a configurable Software-as-a-Service (SaaS) platform designed to digitalize the operations of activity and recreation businesses.

Instead of being developed for a single industry, the platform provides a unified business foundation capable of supporting multiple Facility Types through configuration rather than customization.

The business domain is organized into a hierarchical structure that separates organizational governance from operational execution.

At the highest level, the platform manages Organizations. Each Organization owns one or more Facilities that represent different business types. Every Facility may operate through one or more physical Sites where day-to-day operations are performed.

Business configuration is centrally managed by the Organization, while operational activities are executed independently at each Site under controlled governance.

This separation enables organizations to maintain consistent business policies while allowing individual Sites to efficiently manage their daily operations.

The platform is designed around reusable business concepts rather than industry-specific implementations. As a result, new Facility Types can be introduced by defining their activities, operational rules, and platform capabilities without redesigning the underlying business architecture.

This approach provides long-term scalability and positions Digitize by OreeOn Technologies Pvt. Ltd. as a unified operating platform for the activity and recreation industry.

---

# 5. Domain Objectives

The Domain Model has been designed to achieve the following objectives:

## 5.1 Establish a Common Business Language

Provide a consistent vocabulary for business, product, engineering, and implementation teams by referencing the terminology defined in the Product Glossary.

---

## 5.2 Standardize Business Structure

Define a consistent hierarchy for Organizations, Facilities, Sites, users, customers, and operational activities across all supported business domains.

---

## 5.3 Separate Governance from Operations

Ensure that business configuration remains centrally governed while operational execution is delegated to individual Sites through clearly defined responsibilities and approval workflows.

---

## 5.4 Enable Platform Configurability

Support multiple Facility Types through configurable business rules, operational workflows, and platform capabilities instead of separate applications.

---

## 5.5 Support Future Growth

Provide a domain architecture capable of supporting new Facility Types, additional business capabilities, enterprise licensing models, and future platform expansion without redesigning the core business model.

---

## 5.6 Provide a Foundation for Subsequent Documentation

Serve as the authoritative business architecture reference for:

* Business Requirements Document (BRD)
* Functional Requirements Specification (FRS)
* System Architecture Document (SAD)
* Database Design (ERD)
* API Specifications
* User Interface Specifications
* Test Documentation

---
# 6. Business Domain Hierarchy

The Digitize by OreeOn Technologies Pvt. Ltd. platform follows a hierarchical domain architecture that separates business ownership, business configuration, operational execution, and platform governance.

Each level in the hierarchy has a clearly defined responsibility and ownership. This separation enables the platform to support organizations of different sizes while maintaining centralized governance and decentralized operations.

The business hierarchy is designed to be independent of any specific Facility Type, allowing the platform to support multiple industries through configuration rather than custom development.

---

## 6.1 Domain Hierarchy Overview

The platform is organized into the following business hierarchy:

```text
Digitize by OreeOn Technologies Pvt. Ltd. Platform
│
├── Organization
│
├── Facility
│   │
│   ├── Site
│   │   │
│   │   ├── Staff
│   │   ├── Customer
│   │   ├── Activities
│   │   ├── Membership Plans
│   │   ├── Memberships
│   │   ├── Sessions
│   │   ├── Attendance
│   │   ├── Billing
│   │   └── Daily Operations
│   │
│   └── Additional Sites
│
└── Additional Facilities
```

Each level of the hierarchy builds upon the level above it while maintaining clear ownership and operational boundaries.

---

# 6.2 Hierarchy Levels

## Platform

The Platform represents the SaaS solution provided by Digitize by OreeOn Technologies Pvt. Ltd.

It is responsible for:

* Platform Administration
* Organization Management
* Subscription Management
* License Management
* Platform Security
* Global Configuration
* Platform Monitoring

The Platform is owned and operated by OreeOn Technologies Pvt. Ltd.

---

## Organization

An Organization represents a customer using the Digitize by OreeOn Technologies Pvt. Ltd. platform.

The Organization defines the business entity that owns and manages one or more Facilities.

Responsibilities include:

* Business Governance
* Organization Policies
* Facility Management
* User Administration
* Subscription Ownership
* Business Reporting
* Approval Management

Every Organization has exactly one Organization Administrator responsible for business governance.

---

## Facility

A Facility represents a business vertical operated by an Organization.

Examples include:

* Swimming Pool
* Gym
* Yoga Centre
* Dance Studio
* Badminton Academy
* Football Academy

The Facility defines:

* Business Configuration
* Activities
* Membership Plans
* Pricing
* Business Rules
* Operational Policies

A Facility may operate through multiple Sites.

---

## Site

A Site represents the physical operating location of a Facility.

Each Site performs the day-to-day business operations while following the business configuration defined by the Facility.

Typical responsibilities include:

* Customer Operations
* Membership Execution
* Attendance
* Billing
* Staff Operations
* Daily Reporting

Each Site is managed by one or more Site Administrators.

---

## Operational Layer

The Operational Layer represents the day-to-day business activities performed at a Site.

It includes:

* Customer Registration
* Membership Sales
* Walk-in Visits
* Activity Scheduling
* Session Management
* Attendance
* Billing
* Payments
* Notifications

This layer generates the operational data consumed by reporting and analytics.

---

# 6.3 Hierarchical Relationships

The following relationships govern the business hierarchy.

| Parent       | Child           | Relationship                                |
| ------------ | --------------- | ------------------------------------------- |
| Platform     | Organization    | One Platform manages many Organizations     |
| Organization | Facility        | One Organization owns many Facilities       |
| Facility     | Site            | One Facility operates through many Sites    |
| Site         | Staff           | One Site manages many Staff Members         |
| Site         | Customer        | One Site serves many Customers              |
| Facility     | Activity        | One Facility offers many Activities         |
| Facility     | Membership Plan | One Facility defines many Membership Plans  |
| Customer     | Membership      | One Customer may own many Memberships       |
| Activity     | Session         | One Activity may contain many Sessions      |
| Session      | Attendance      | One Session records many Attendance entries |

These relationships are conceptual and will later be translated into the logical data model and database design.

---

# 6.4 Business Ownership Hierarchy

Ownership within the platform follows a strict hierarchical structure.

| Business Object | Owned By     |
| --------------- | ------------ |
| Platform        | OreeOn       |
| Organization    | Platform     |
| Facility        | Organization |
| Site            | Facility     |
| Activity        | Facility     |
| Membership Plan | Facility     |
| Customer        | Organization |
| Membership      | Customer     |
| Session         | Activity     |
| Attendance      | Site         |
| Invoice         | Organization |
| Payment         | Organization |
| Subscription    | Organization |
| License         | Platform     |

Ownership determines business accountability and governance throughout the platform.

---

# 6.5 Governance Hierarchy

The platform separates governance responsibilities from operational responsibilities.

| Level        | Primary Responsibility |
| ------------ | ---------------------- |
| Platform     | Platform Governance    |
| Organization | Business Governance    |
| Facility     | Business Configuration |
| Site         | Operational Management |
| Staff        | Operational Execution  |
| Customer     | Service Consumption    |

This separation allows centralized control while enabling individual Sites to operate independently within approved business rules.

---

# 7. Domain Architecture Principles

The Domain Architecture Principles define the fundamental rules governing the structure and behavior of the Digitize by OreeOn business domain.

These principles ensure consistency across all Facility Types and provide the foundation for future platform evolution.

---

## 7.1 Configuration Before Customization

Business requirements shall be satisfied through configurable business rules wherever possible.

The platform should avoid customer-specific software customization in favor of reusable configuration.

---

## 7.2 Single Platform Architecture

Digitize by OreeOn shall operate as a single configurable platform capable of supporting multiple Facility Types.

New business domains shall be introduced through configuration rather than separate applications.

---

## 7.3 Business Hierarchy

Every business object shall exist within the established hierarchy:

Platform → Organization → Facility → Site → Operations

No operational data shall exist outside this hierarchy.

---

## 7.4 Centralized Governance

Business configuration shall be controlled by the Organization.

Examples include:

* Membership Plans
* Pricing
* Activities
* Business Rules
* Operating Policies

Configuration changes shall follow the approved governance process.

---

## 7.5 Decentralized Operations

Sites shall independently perform day-to-day operational activities including:

* Customer Registration
* Membership Sales
* Attendance
* Billing
* Payments
* Session Execution

Operational autonomy shall not override Organization governance.

---

## 7.6 Approval-Driven Configuration

Business configuration proposed by Site Administrators shall require Organization Administrator approval before becoming effective.

No Site shall directly modify approved business configurations.

---

## 7.7 License-Based Capabilities

Platform functionality shall be controlled through Licenses.

Licenses determine which Platform Capabilities are available to a Facility.

Examples include:

* Advertisement Campaigns
* Personal Training
* Batch Management
* Advanced Reports
* Future AI Capabilities

---

## 7.8 Dynamic User Experience

The user interface shall adapt according to:

* Facility Type
* Enabled Platform Capabilities
* User Role
* Business Configuration

This enables a single application to provide different user experiences for different business domains.

---

## 7.9 Domain Independence

Core business concepts shall remain independent of implementation technologies.

Business domains shall not depend on:

* Database Design
* API Design
* Programming Language
* User Interface Framework

This principle ensures long-term maintainability and technology flexibility.

---

## 7.10 Future Extensibility

The domain architecture shall support future expansion without requiring redesign of the core business model.

Examples include:

* New Facility Types
* New Platform Capabilities
* Additional Licensing Models
* Enterprise Features
* Third-Party Integrations
* AI Services

Future enhancements should extend the domain rather than replace existing concepts.

---

# 8. Core Domain Model

## 8.1 Introduction

The Core Domain Model represents the fundamental business structure of the Digitize by OreeOn platform.

It identifies the primary business domains (also referred to as **Domain Aggregates**) that collectively define how the platform operates. Each aggregate encapsulates a cohesive set of business responsibilities, ensuring that related business concepts remain together while maintaining clear boundaries with other domains.

The Core Domain Model serves as the conceptual foundation for:

* Business Requirements (BRD)
* Functional Requirements (FRS)
* System Architecture
* Database Design (ERD)
* API Design
* User Interface Design

The model intentionally remains technology-independent and focuses solely on business architecture.

---

# 8.2 Core Domain Overview

The Digitize by OreeOn platform is organized into the following primary business domains.

```text
                           Digitize by OreeOn
                                     │
     ┌───────────────────────────────┼───────────────────────────────┐
     │                               │                               │
Organization Domain         Subscription Domain            Platform Administration
     │                               │
     │                               │
Facility Domain              License Domain
     │
     │
Site Domain
     │
 ┌───┼──────────────────────────────────────────────────────────────┐
 │   │             │             │            │          │          │
Customer      Activity      Membership   Billing   Marketing   Notification
Domain         Domain         Domain      Domain      Domain        Domain
```

Each domain is responsible for a specific area of the business and communicates with other domains through well-defined business relationships.

---

# 8.3 Organization Domain

## Purpose

The Organization Domain represents the highest business entity within the customer hierarchy.

It is responsible for business ownership, governance, policy management, subscriptions, reporting, and overall operational control.

---

## Primary Responsibilities

* Organization Registration
* Organization Administration
* Business Governance
* Facility Ownership
* Subscription Ownership
* Organization Users
* Enterprise Reporting
* Approval Governance

---

## Aggregate Root

**Organization**

---

## Primary Business Objects

* Organization
* Organization Admin
* Subscription
* Business Policies

---

## Owned Domains

* Facility Domain
* Subscription Domain

---

## Business Rules

* An Organization owns one or more Facilities.
* Every Organization has at least one Organization Administrator.
* Organization policies apply across all Facilities.
* Organization dashboards provide consolidated reporting across all Sites.

---

# 8.4 Facility Domain

## Purpose

The Facility Domain represents an individual business operated by an Organization.

A Facility defines the operational identity, business configuration, pricing, activities, and services offered to customers.

Examples include:

* Swimming Pool
* Gym
* Yoga Centre
* Dance Studio
* Badminton Academy

---

## Primary Responsibilities

* Business Configuration
* Activity Management
* Membership Plan Management
* Pricing Rules
* Operating Policies
* Site Management

---

## Aggregate Root

**Facility**

---

## Primary Business Objects

* Facility
* Facility Type
* Activities
* Membership Plans
* Business Rules

---

## Owned Domains

* Site Domain
* Activity Domain
* Membership Domain

---

## Business Rules

* A Facility belongs to exactly one Organization.
* A Facility may operate through multiple Sites.
* Business configuration is shared across all Sites unless explicitly configured otherwise in future platform versions.
* Operational execution occurs only at the Site level.

---

# 8.5 Site Domain

## Purpose

The Site Domain represents the physical operating location where business activities are executed.

The Site performs operational functions while adhering to the business configuration defined by the Facility.

---

## Primary Responsibilities

* Customer Operations
* Membership Execution
* Attendance
* Billing
* Session Management
* Staff Management
* Daily Reporting

---

## Aggregate Root

**Site**

---

## Primary Business Objects

* Site
* Site Admin
* Staff

---

## Owned Domains

* Customer Domain
* Billing Domain
* Attendance Domain

---

## Business Rules

* Every Site belongs to one Facility.
* A Site cannot modify business configuration directly.
* Configuration changes require Organization Admin approval.
* Daily operational activities are executed independently at each Site.

---

# 8.6 Customer Domain

## Purpose

The Customer Domain manages the complete customer lifecycle from registration through service consumption.

It maintains customer identity, memberships, participation history, attendance, and engagement across the platform.

---

## Primary Responsibilities

* Customer Registration
* Customer Profile Management
* Membership Ownership
* Activity Participation
* Attendance History
* Communication History

---

## Aggregate Root

**Customer**

---

## Primary Business Objects

* Customer
* Membership
* Attendance History

---

## Business Rules

* A Customer belongs to an Organization.
* A Customer Aggregate exists only within a single Organization (tenant).
* The same individual may have independent Customer Aggregates in different Organizations because Organizations are isolated tenants.
* Customers may hold multiple active Memberships.
* Customer history is never deleted.
* Customer identity remains consistent across Facilities within the Organization.

---

# 8.7 Activity Domain

## Purpose

The Activity Domain defines the services delivered by a Facility.

Activities represent the operational offerings made available to customers.

Examples include:

Swimming

* Public Swimming
* Coaching
* Summer Camp

Gym

* Fitness Training
* Personal Training

Yoga

* Yoga Class
* Meditation Session

---

## Primary Responsibilities

* Activity Management
* Session Planning
* Batch Management
* Trainer Assignment
* Capacity Management

---

## Aggregate Root

**Activity**

---

## Primary Business Objects

* Activity
* Session
* Batch/Class

---

## Business Rules

* Activities belong to one Facility.
* Activities may have multiple Sessions.
* Capacity rules are configurable.
* Activities follow Facility business policies.

---

# 8.8 Membership Domain

## Purpose

The Membership Domain manages the commercial relationship between customers and the Facility.

It governs membership plans, purchases, renewals, validity, and access rights.

---

## Primary Responsibilities

* Membership Plan Management
* Membership Purchase
* Renewals
* Expiry
* Membership Validation

---

## Aggregate Root

**Membership Plan**

---

## Primary Business Objects

* Membership Plan
* Membership

---

## Business Rules

* A Membership references one Membership Plan.
* Customers may own multiple active Memberships.
* Membership activation follows successful payment.
* Membership validity is enforced during attendance.

---

# 8.9 Billing Domain

## Purpose

The Billing Domain manages financial transactions between customers and the Facility.

It records invoices, payments, taxes, discounts, and financial history.

---

## Primary Responsibilities

* Invoice Generation
* Payment Processing
* Financial Records
* Tax Calculation
* Receipts
* Refund Support (Future)

---

## Aggregate Root

**Invoice**

---

## Primary Business Objects

* Invoice
* Payment

---

## Business Rules

* Every Payment references an Invoice.
* Financial records are immutable.
* Billing follows organizational policies.
* Payment confirmation may activate Memberships.

---

# 8.10 Subscription Domain

## Purpose

The Subscription Domain manages the commercial relationship between the Organization and Digitize by OreeOn.

It controls subscription plans, renewals, billing periods, and commercial agreements.

---

## Primary Responsibilities

* Subscription Management
* Renewal
* Plan Assignment
* Commercial Billing

---

## Aggregate Root

**Subscription**

---

## Primary Business Objects

* Subscription
* Subscription Plan

---

## Business Rules

* Every Subscription belongs to one Organization.
* Subscription controls commercial entitlement.
* Licenses operationalize subscribed capabilities.

---

# 8.11 License Domain

## Purpose

The License Domain governs operational entitlements assigned to Facilities.

Licenses determine which Platform Capabilities are available for use.

---

## Primary Responsibilities

* License Assignment
* Capability Management
* License Validation
* Feature Availability

---

## Aggregate Root

**License**

---

## Primary Business Objects

* License
* Platform Capability

---

## Business Rules

* Every License belongs to one Subscription.
* Every Facility must have an active License.
* Capabilities are enabled through Licenses.
* License expiration affects Facility access according to subscription policy.

---

# 8.12 Marketing Domain

## Purpose

The Marketing Domain enables Organizations to promote Facilities, Membership Plans, Activities, and events through integrated campaigns.

---

## Primary Responsibilities

* Campaign Creation
* Campaign Scheduling
* Audience Targeting
* Campaign Analytics

---

## Aggregate Root

**Advertisement Campaign**

---

## Primary Business Objects

* Advertisement Campaign
* Target Audience

---

## Business Rules

* Campaigns require Organization Admin approval.
* Campaigns are measurable.
* Campaign history is retained.

---

# 8.13 Notification Domain

## Purpose

The Notification Domain manages communication between the platform, Organizations, Staff, and Customers.

---

## Primary Responsibilities

* Event Notifications
* Payment Notifications
* Membership Alerts
* Approval Notifications
* Marketing Communications

---

## Aggregate Root

**Notification**

---

## Primary Business Objects

* Notification
* Notification Template
* Delivery Channel

---

## Business Rules

* Notifications may be automated or manual.
* Delivery history is retained.
* Multiple delivery channels may be supported.

---

# 8.14 Approval Domain

## Purpose

The Approval Domain governs controlled business changes within the platform.

It ensures that operational flexibility is balanced with centralized governance.

---

## Primary Responsibilities

* Approval Requests
* Review Process
* Decision Recording
* Audit Trail

---

## Aggregate Root

**Approval Request**

---

## Primary Business Objects

* Approval Request
* Approval Decision
* Review Comments

---

## Business Rules

* Site Admins submit Approval Requests.
* Organization Admins approve or reject requests.
* Approved changes become effective only after approval.
* Every approval decision is permanently auditable.

---

# Domain Dependency Summary

The domains collaborate through defined business relationships while preserving clear ownership boundaries.

```text
Organization
    │
    ├── Subscription
    │      │
    │      └── License
    │
    └── Facility
           │
           ├── Site
           │     ├── Customer
           │     ├── Billing
           │     ├── Notification
           │     └── Approval
           │
           ├── Activity
           │      ├── Session
           │      └── Batch/Class
           │
           ├── Membership
           │
           └── Marketing
```

The Domain Dependency Summary illustrates how the major business domains collaborate while maintaining clear ownership, governance, and operational boundaries. These relationships provide the conceptual blueprint for the Business Requirements Document, Functional Requirements Specification, System Architecture, Database Design, and API Specifications.

---

# 9. Domain Relationships

## 9.1 Overview

The Domain Relationships describe how the core business domains interact while maintaining clear ownership, responsibilities, and business boundaries.

Each domain has a defined purpose and communicates with other domains through established business relationships rather than direct dependencies.

This approach promotes scalability, maintainability, and separation of concerns across the Digitize by OreeOn platform.

---

# 9.2 High-Level Domain Relationships

```text
                               Platform
                                   │
                    ┌──────────────┴──────────────┐
                    │                             │
             Organization Domain         Platform Administration
                    │
         ┌──────────┴──────────┐
         │                     │
 Subscription Domain     Facility Domain
         │                     │
         │               ┌─────┴─────┐
         │               │           │
    License Domain   Site Domain   Activity Domain
                          │             │
               ┌──────────┼─────────────┘
               │          │
         Customer Domain  Membership Domain
               │          │
               └─────┬────┘
                     │
               Billing Domain
                     │
        ┌────────────┴────────────┐
        │                         │
 Marketing Domain        Notification Domain
                     │
              Approval Domain
```

The relationships above represent business interaction and ownership rather than implementation dependencies.

---

# 9.3 Primary Domain Relationships

| Parent Domain | Child Domain | Relationship             |
| ------------- | ------------ | ------------------------ |
| Platform      | Organization | Hosts Organizations      |
| Organization  | Subscription | Owns Subscription        |
| Subscription  | License      | Generates Licenses       |
| Organization  | Facility     | Owns Facilities          |
| Facility      | Site         | Operates through Sites   |
| Facility      | Activity     | Defines Activities       |
| Facility      | Membership   | Defines Membership Plans |
| Site          | Customer     | Serves Customers         |
| Customer      | Membership   | Purchases Memberships    |
| Membership    | Billing      | Generates Invoices       |
| Activity      | Session      | Schedules Sessions       |
| Session       | Attendance   | Records Attendance       |
| Site          | Marketing    | Executes Campaigns       |
| Site          | Approval     | Raises Approval Requests |
| Platform      | Notification | Delivers Notifications   |

---

# 9.4 Business Relationship Principles

The following principles govern domain interactions.

### Ownership

Every business object has a single business owner.

Ownership determines accountability, governance, and lifecycle management.

---

### Association

Business domains may collaborate without transferring ownership.

Example:

Customer Domain interacts with Billing Domain.

Customer does not own Billing.

Billing serves Customer.

---

### Aggregation

A parent domain groups multiple related business objects.

Example

Facility

contains

* Activities
* Membership Plans
* Sites

without becoming dependent on operational execution.

---

### Dependency

Domains depend on business outcomes rather than implementation.

Example

Membership activation depends on successful Payment.

The Membership Domain does not process payments.

The Billing Domain performs payment processing.

---

# 9.5 Cross-Domain Interactions

## Customer Purchase Journey

```text
Customer Domain
        │
        ▼
Membership Domain
        │
        ▼
Billing Domain
        │
        ▼
Notification Domain
```

Flow

Customer

↓

Purchases Membership

↓

Invoice Generated

↓

Payment Completed

↓

Membership Activated

↓

Confirmation Notification

---

## Attendance Journey

```text
Customer Domain
        │
        ▼
Membership Domain
        │
        ▼
Activity Domain
        │
        ▼
Attendance
```

Flow

Customer

↓

Membership Validation

↓

Session Validation

↓

Attendance Recorded

---

## Business Configuration Journey

```text
Site Domain
      │
      ▼
Approval Domain
      │
      ▼
Organization Domain
      │
      ▼
Facility Domain
```

Flow

Site Admin

↓

Configuration Request

↓

Organization Approval

↓

Facility Updated

↓

Site Uses New Configuration

---

# 9.6 Domain Communication Rules

The following communication rules apply throughout the platform.

### Rule 1

Organization governs.

Sites execute.

---

### Rule 2

Facilities define business.

Sites perform business.

---

### Rule 3

Customers consume services.

Staff deliver services.

---

### Rule 4

Billing validates commercial transactions.

Membership validates business access.

---

### Rule 5

Licenses enable capabilities.

Subscriptions authorize licensing.

---

### Rule 6

Notifications communicate business events.

Notifications never change business state.

---

### Rule 7

Approval Requests control business configuration.

Operational transactions never require approval.

---

# 10. Domain Ownership

## 10.1 Overview

Domain Ownership defines who owns, governs, manages, and operates each business domain.

Ownership is assigned at the business level and remains independent of technical implementation.

---

# 10.2 Domain Ownership Matrix

| Domain       | Business Owner          | Managed By         | Operated By  |
| ------------ | ----------------------- | ------------------ | ------------ |
| Platform     | OreeOn                  | Platform Admin     | Platform     |
| Organization | Organization            | Organization Admin | Organization |
| Subscription | Organization            | Platform           | Platform     |
| License      | Platform                | Platform           | Platform     |
| Facility     | Organization            | Organization Admin | Organization |
| Site         | Facility                | Organization Admin | Site Admin   |
| Customer     | Organization            | Site Admin         | Staff        |
| Activity     | Facility                | Organization Admin | Site Admin   |
| Membership   | Facility                | Organization Admin | Staff        |
| Billing      | Organization            | Site Admin         | Staff        |
| Marketing    | Organization            | Organization Admin | Site Admin   |
| Notification | Platform / Organization | Platform           | Platform     |
| Approval     | Organization            | Organization Admin | Platform     |

---

# 10.3 Ownership Responsibilities

## Platform

Responsible for:

* SaaS Operations
* Subscription Management
* Licensing
* Security
* Platform Availability

---

## Organization

Responsible for:

* Business Governance
* Facilities
* Business Policies
* Organization Users

---

## Facility

Responsible for:

* Business Configuration
* Membership Plans
* Activities
* Pricing
* Operational Standards

---

## Site

Responsible for:

* Daily Operations
* Customer Services
* Attendance
* Billing
* Staff Management

---

## Staff

Responsible for:

* Customer Registration
* Membership Sales
* Attendance Recording
* Payment Collection
* Customer Assistance

---

# 10.4 Ownership Principles

* Every domain has one business owner.
* Governance flows from Organization to Site.
* Operational authority never overrides business governance.
* Ownership is permanent unless explicitly transferred through business processes.
* Business responsibility must always be traceable.

---

# 11. Domain Lifecycles

## 11.1 Overview

Every core business domain progresses through a defined lifecycle.

Lifecycle states establish consistency across business operations and provide predictable behavior throughout the platform.

---

# 11.2 Organization Lifecycle

```text
Registered
      │
      ▼
Verified
      │
      ▼
Subscribed
      │
      ▼
Operational
      │
      ▼
Suspended
      │
      ▼
Archived
```

---

## Business Events

* Organization Created
* Subscription Purchased
* Facilities Created
* Organization Activated
* Subscription Expired

---

# 11.3 Facility Lifecycle

```text
Created
     │
     ▼
Configured
     │
     ▼
Licensed
     │
     ▼
Operational
     │
     ▼
Inactive
     │
     ▼
Archived
```

---

## Business Events

* Facility Created
* License Assigned
* Configuration Completed
* Facility Activated

---

# 11.4 Site Lifecycle

```text
Created
     │
     ▼
Configured
     │
     ▼
Operational
     │
     ▼
Inactive
     │
     ▼
Closed
```

---

## Business Events

* Site Created
* Staff Assigned
* Site Activated
* Site Closed

---

# 11.5 Customer Lifecycle

```text
Registered
      │
      ▼
Verified
      │
      ▼
Active
      │
      ▼
Inactive
```

---

## Business Events

* Customer Registered
* Membership Purchased
* Attendance Recorded
* Membership Renewed

---

# 11.6 Membership Lifecycle

```text
Created
     │
     ▼
Purchased
     │
     ▼
Active
     │
     ▼
Expired
     │
     ▼
Renewed
```

---

## Business Events

* Membership Purchased
* Membership Activated
* Membership Expired
* Membership Renewed

---

# 11.7 Subscription Lifecycle

```text
Draft
   │
   ▼
Purchased
   │
   ▼
Active
   │
   ▼
Renewed
   │
   ▼
Expired
   │
   ▼
Cancelled
```

---

## Business Events

* Subscription Purchased
* Subscription Renewed
* License Generated
* Subscription Expired

---

# 11.8 Approval Request Lifecycle

```text
Draft
   │
   ▼
Submitted
   │
   ▼
Under Review
   │
   ├─────────────┐
   ▼             ▼
Approved     Rejected
   │
   ▼
Implemented
   │
   ▼
Closed
```

---

## Business Events

* Request Submitted
* Review Started
* Request Approved
* Request Rejected
* Configuration Updated

---

# 11.9 Lifecycle Principles

The following principles apply across all business domains.

* Every lifecycle begins with creation or registration.
* State transitions occur only through valid business events.
* Lifecycle history is retained for audit purposes.
* Historical records are never physically deleted.
* Business events trigger notifications, reporting, and audit logging.
* Lifecycle transitions are governed by business rules defined in the Functional Requirements Specification.

---

# 12. Business Aggregates

## 12.1 Overview

Business Aggregates are logical groupings of closely related business entities that collectively represent a specific business capability.

Each aggregate has a single **Aggregate Root**, which acts as the entry point for all business operations within that aggregate. This approach ensures consistency, maintains clear ownership boundaries, and prevents unrelated domains from directly modifying business data.

The aggregate model adopted by Digitize by OreeOn aligns with Domain-Driven Design (DDD) principles while remaining simple enough for product, business, and engineering teams to understand.

---

# 12.2 Organization Aggregate

## Aggregate Root

**Organization**

### Business Objects

* Organization
* Organization Admin
* Organization Policies
* Organization Settings

### Responsibilities

* Business ownership
* Governance
* Organization administration
* Facility ownership
* Subscription ownership
* Enterprise reporting

### Owned Aggregates

* Facility Aggregate
* Subscription Aggregate

---

# 12.3 Facility Aggregate

## Aggregate Root

**Facility**

### Business Objects

* Facility
* Facility Type
* Activity
* Membership Plan
* Business Configuration
* Pricing Rules

### Responsibilities

* Business configuration
* Operational policies
* Service catalog
* Pricing strategy
* Business standards

### Owned Aggregates

* Site Aggregate
* Activity Aggregate
* Membership Aggregate

---

# 12.4 Site Aggregate

## Aggregate Root

**Site**

### Business Objects

* Site
* Site Admin
* Staff

### Responsibilities

* Daily operations
* Customer servicing
* Membership execution
* Billing operations
* Attendance management
* Local reporting

### Owned Aggregates

* Customer Aggregate
* Billing Aggregate

---

# 12.5 Customer Aggregate

## Aggregate Root

**Customer**

### Business Objects

* Customer
* Customer Profile
* Membership
* Attendance History

### Responsibilities

* Customer lifecycle
* Membership ownership
* Service utilization
* Customer history

---

# 12.6 Activity Aggregate

## Aggregate Root

**Activity**

### Business Objects

* Activity
* Session
* Batch/Class

### Responsibilities

* Service scheduling
* Trainer allocation
* Capacity management
* Operational planning

---

# 12.7 Membership Aggregate

## Aggregate Root

**Membership Plan**

### Business Objects

* Membership Plan
* Membership

### Responsibilities

* Membership definition
* Membership purchase
* Renewals
* Validity
* Customer access

---

# 12.8 Billing Aggregate

## Aggregate Root

**Invoice**

### Business Objects

* Invoice
* Payment

### Responsibilities

* Financial transactions
* Customer billing
* Tax calculation
* Receipts
* Financial history

---

# 12.9 Subscription Aggregate

## Aggregate Root

**Subscription**

### Business Objects

* Subscription
* License

### Responsibilities

* Commercial agreement
* License generation
* Capability entitlement
* Subscription lifecycle

---

# 12.10 Marketing Aggregate

## Aggregate Root

**Advertisement Campaign**

### Business Objects

* Advertisement Campaign
* Target Audience

### Responsibilities

* Marketing campaigns
* Customer engagement
* Promotional activities
* Campaign analytics

---

# 12.11 Notification Aggregate

## Aggregate Root

**Notification**

### Business Objects

* Notification
* Notification Template
* Delivery Channel

### Responsibilities

* Business communication
* Customer communication
* Event notifications
* Marketing notifications

---

# 12.12 Approval Aggregate

## Aggregate Root

**Approval Request**

### Business Objects

* Approval Request
* Approval Decision
* Review Comments

### Responsibilities

* Governance
* Business approvals
* Configuration control
* Audit trail

---

# 13. Domain Boundaries

## 13.1 Overview

Domain Boundaries define the limits of responsibility for each business domain.

Each domain owns its business rules, lifecycle, and data, while interacting with other domains only through defined business relationships.

This separation reduces complexity, improves maintainability, and supports future scalability.

---

# 13.2 Bounded Contexts

| Business Domain         | Primary Responsibility   |
| ----------------------- | ------------------------ |
| Platform Administration | SaaS platform management |
| Organization Management | Organization governance  |
| Subscription Management | Commercial subscriptions |
| License Management      | Platform capabilities    |
| Facility Management     | Business configuration   |
| Site Operations         | Daily operations         |
| Customer Management     | Customer lifecycle       |
| Activity Management     | Activities and sessions  |
| Membership Management   | Membership lifecycle     |
| Billing Management      | Financial operations     |
| Marketing Management    | Campaign management      |
| Notification Management | Business communications  |
| Approval Management     | Governance workflows     |

Each bounded context owns its business logic and exposes services to other contexts without sharing internal implementation.

---

# 13.3 Boundary Principles

The following principles govern all domain boundaries:

* Each domain has a single business purpose.
* Each domain owns its business rules.
* Cross-domain communication occurs through business events.
* Domains remain loosely coupled.
* Business ownership is clearly defined.
* Changes within one domain should have minimal impact on others.

---

# 14. Domain Events

## 14.1 Overview

A Domain Event represents a significant business occurrence that has happened within the platform.

Domain Events communicate completed business actions between domains and enable automation, notifications, reporting, auditing, and future integrations.

Events describe **what has happened**, not **what should happen**.

---

# 14.2 Organization Events

* Organization Registered
* Organization Verified
* Subscription Purchased
* Organization Activated
* Organization Suspended

---

# 14.3 Facility Events

* Facility Created
* Facility Configured
* License Assigned
* Facility Activated
* Facility Archived

---

# 14.4 Site Events

* Site Created
* Site Activated
* Site Closed
* Staff Assigned

---

# 14.5 Customer Events

* Customer Registered
* Customer Verified
* Customer Updated
* Customer Deactivated

---

# 14.6 Membership Events

* Membership Plan Created
* Membership Purchased
* Membership Activated
* Membership Renewed
* Membership Expired
* Membership Cancelled

---

# 14.7 Billing Events

* Invoice Generated
* Payment Received
* Payment Failed
* Receipt Generated

---

# 14.8 Activity Events

* Activity Created
* Session Scheduled
* Session Started
* Session Completed
* Attendance Recorded

---

# 14.9 Marketing Events

* Campaign Created
* Campaign Approved
* Campaign Published
* Campaign Completed

---

# 14.10 Approval Events

* Approval Submitted
* Approval Reviewed
* Approval Approved
* Approval Rejected
* Configuration Applied

---

# 14.11 Notification Events

* Notification Generated
* Notification Delivered
* Notification Failed

---

# 14.12 Event Principles

* Every event represents a completed business action.
* Events are immutable once recorded.
* Events trigger downstream business processes.
* Events are retained for auditing and reporting.
* Future platform integrations should consume events instead of directly accessing business data where appropriate.

---

# 15. Future Domain Expansion

The Domain Model has been designed with long-term scalability as a primary objective.

Future business growth should be achieved by extending existing domains rather than redesigning the platform architecture.

---

## 15.1 Future Facility Types

The platform is designed to support additional Facility Types, including but not limited to:

* Swimming Pools
* Gyms
* Yoga Centres
* Dance Studios
* Badminton Academies
* Football Academies
* Cricket Academies
* Tennis Academies
* Martial Arts Centres
* Indoor Sports Facilities
* Wellness Centres
* Adventure Parks
* Kids Activity Centres

Each new Facility Type will reuse the existing Organization, Facility, Site, Customer, Membership, Billing, and Notification domains while introducing only the configuration and activities specific to that business.

---

## 15.2 Future Platform Capabilities

The platform architecture supports future capabilities such as:

* Artificial Intelligence (AI)
* Predictive Analytics
* Business Intelligence Dashboards
* Marketplace Integration
* Accounting Integrations
* Payroll Management
* Public APIs
* IoT Device Integration
* Mobile Ecosystem
* Enterprise Multi-Facility Management
* Multi-Organization Groups

These capabilities will extend existing domains without requiring changes to the core business architecture.

---

## 15.3 Domain Evolution Principles

Future enhancements shall follow these principles:

* Preserve existing business concepts.
* Extend through configuration rather than customization.
* Maintain clear domain ownership.
* Avoid introducing cross-domain dependencies.
* Ensure backward compatibility wherever possible.
* Keep the core platform technology-agnostic.

These principles ensure that Digitize by OreeOn can evolve into a comprehensive operating platform for the activity and recreation industry while maintaining a stable and maintainable domain architecture.

---

# 16. Revision History

| Version | Date      | Author                      | Description                                                 |
| ------- | --------- | --------------------------- | ----------------------------------------------------------- |
| 1.0     | July 2026 | Product & Architecture Team | Initial release of the Domain Model for Digitize by OreeOn. |

---

# End of Document

The Domain Model is the conceptual blueprint for the Digitize by OreeOn platform. It establishes the business architecture, ownership model, domain relationships, aggregates, boundaries, and business events that guide all subsequent documentation and implementation.

This document should be used as the primary business architecture reference for the Business Requirements Document (BRD), Functional Requirements Specification (FRS), System Architecture Document (SAD), Database Design (ERD), API Specifications, User Interface Specifications, and Quality Assurance artefacts.
