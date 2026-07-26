# CS-01 Subscription & Licensing Strategy

**Document ID:** CS-01

**Document Name:** Subscription & Licensing Strategy

**Company:** OreeOn Technologies Pvt. Ltd.

**Product:** Digitize

**Document Type:** Commercial Strategy

**Version:** 1.0

**Status:** Approved

**Prepared By:** Product Strategy & Commercial Architecture Team

**Owner:** Product Management & Business Leadership

**Reviewer:** CTO

**Last Updated:** July 2026

---

# Table of Contents

1. Document Information
2. Purpose
3. Executive Summary
4. Commercial Philosophy
5. Commercial Architecture
6. Subscription Model
7. Licensing Model
8. Subscription Plans
9. Site Licensing
10. Subscription Lifecycle
11. License Lifecycle
12. Subscription Operations
13. Plan Upgrade & Downgrade
14. Renewal Strategy
15. Suspension & Grace Period
16. Trial Strategy
17. Enterprise Licensing
18. Future Commercial Expansion
19. Business Rules Summary
20. Document References
21. Revision History

---

# 1. Purpose

The purpose of this document is to define the commercial subscription and licensing strategy for **Digitize**, the Software-as-a-Service (SaaS) platform developed by **OreeOn**.

This document establishes the principles, commercial structure, licensing model, subscription lifecycle, and governance rules that determine how organizations access, license, and consume the Digitize platform.

It serves as the single source of truth for all subscription and licensing decisions across the platform.

The strategy defined in this document provides consistency for product management, engineering, finance, customer success, sales, implementation partners, and future stakeholders.

Commercial pricing values are intentionally excluded from this document and are maintained separately in **CS-02 – Pricing Strategy**.

---

# 2. Executive Summary

Digitize is offered as a multi-tenant SaaS platform that enables organizations to digitize and manage activity and recreation businesses through a configurable operating platform.

The commercial model is designed around the operational structure of customer businesses rather than technical metrics such as user count, database usage, or transaction volume.

The primary commercial unit of the platform is the **Facility**.

Each subscribed Facility receives access to Digitize through a subscription plan that defines the business capabilities available to that Facility.

Facilities may operate one or more Sites. The commercial treatment of Sites is defined independently from the Facility subscription to allow organizations to expand geographically without fundamentally changing their subscription model.

The subscription strategy has been designed to satisfy the following objectives:

* Simplicity for customers.
* Predictable recurring revenue.
* Scalability across industries.
* Support for organizations of different sizes.
* Clear separation between subscriptions, licenses, pricing, and future commercial offerings.
* Flexibility for future commercial evolution.

This document defines the commercial framework that all downstream business and technical documentation must follow.

---

# 3. Commercial Philosophy

The commercial strategy for Digitize is guided by principles intended to balance customer value, business sustainability, and long-term product scalability.

## 3.1 Business-Centric Commercial Model

Digitize is licensed according to how customers operate their businesses rather than how heavily they use the software.

Customers purchase access based on business operations, not technical consumption.

The platform intentionally avoids licensing models based on:

* Number of registered customers.
* Number of memberships.
* Number of employees.
* Number of trainers.
* Attendance volume.
* Invoice count.
* Database size.
* API requests.

This approach encourages customers to grow their businesses without fear of incurring unpredictable licensing costs.

---

## 3.2 Scalable Growth

The subscription model must grow alongside customer businesses.

Organizations should be able to expand their operations by:

* Adding new Facilities.
* Expanding to additional Sites.
* Upgrading subscription plans.
* Purchasing additional commercial capabilities.
* Transitioning to enterprise agreements.

The commercial model should never require architectural redesign as customers grow.

---

## 3.3 Simplicity

Customers should easily understand:

* What they are purchasing.
* Why they are purchasing it.
* How they can expand.
* What happens during renewal.
* How upgrades work.

Commercial complexity should remain internal to OreeOn and not create confusion for customers.

---

## 3.4 Fairness

Commercial charges should reflect genuine business value.

Organizations should pay for the operational value they receive rather than arbitrary software limitations.

The commercial strategy seeks to establish long-term customer relationships by ensuring pricing remains transparent, predictable, and aligned with business growth.

---

## 3.5 Future Flexibility

The commercial architecture must support future expansion without requiring major changes to the underlying subscription framework.

Future capabilities may include:

* Premium capability packs.
* Industry-specific offerings.
* Enterprise licensing.
* Marketplace services.
* AI-powered modules.
* Partner programs.

The subscription architecture should accommodate these future offerings while maintaining backward compatibility wherever possible.

---

# 4. Commercial Architecture

The commercial architecture defines the relationship between the company, product, customer organizations, subscriptions, and licenses.

```text
OreeOn (Company)
        │
        ▼
Digitize (Product)
        │
        ▼
Organization
        │
        ▼
Facility
        │
        ▼
Subscription
        │
        ▼
License
        │
        ▼
Operational Access
```

Each layer has a distinct commercial responsibility.

---

## 4.1 Company

**OreeOn** is the legal entity responsible for developing, operating, licensing, supporting, and commercially managing the Digitize platform.

OreeOn owns all commercial agreements, subscription contracts, licensing policies, and customer relationships.

---

## 4.2 Product

**Digitize** is the SaaS platform offered by OreeOn.

Digitize delivers configurable business management capabilities to organizations operating activity and recreation businesses.

The product is licensed according to the commercial rules defined in this strategy.

---

## 4.3 Organization

An Organization represents the legal customer entering into a commercial relationship with OreeOn.

An Organization may own one or more Facilities.

The Organization itself is not the subscription unit.

Instead, it acts as the contractual entity responsible for subscription ownership, billing, payment, and overall account administration.

---

## 4.4 Facility

A Facility represents an operational business unit within an Organization.

Examples include:

* Swimming Pool
* Gym
* Yoga Centre
* Dance Studio
* Football Academy
* Badminton Centre

Each Facility operates independently from a commercial perspective.

Every subscribed Facility has its own subscription, licensing status, operational configuration, and commercial lifecycle.

The Facility is the primary commercial unit of the Digitize platform.

---

## 4.5 Site

A Site represents a physical operating location belonging to a Facility.

Examples:

**Facility:** Swimming Pool

Sites:

* HSR Layout
* Jayanagar
* Whitefield

A Site extends the operational footprint of a Facility but does not represent an independent business type.

**Version 1.0 Commercial Assumption**

For Version 1.0 of the commercial strategy:

* By default, every Facility subscription includes one (1) Site.
* The underlying platform supports multiple Sites per Facility.
* Additional Sites may be enabled through commercial Site Add-ons.
* This is a commercial packaging policy only and does not restrict the platform architecture.

This assumption is subject to future commercial review without affecting the underlying subscription architecture.

---

## 4.6 Subscription

A Subscription represents the commercial agreement granting a Facility access to Digitize for a defined billing period.

A subscription determines:

* Commercial plan.
* Subscription validity.
* Enabled business capabilities.
* Billing cycle.
* Renewal eligibility.
* Commercial status.

Subscriptions are discussed in detail in Section 6 of this document.

---

## 4.7 License

A License is the operational authorization generated from an active subscription.

A valid License enables the subscribed Facility to access and use the Digitize platform according to the rights defined by its subscription.

Licenses are system-controlled and exist to enforce commercial entitlements rather than define commercial agreements.

Further details are provided in Section 7.

---

# 5. Subscription Model

## 5.1 Overview

The subscription model defines the commercial relationship between an Organization and OreeOn for the use of the Digitize platform.

Digitize follows a **Facility-Based Subscription Model**, where each subscribed Facility receives access to the platform through an active subscription.

The subscription represents the commercial agreement between the customer and OreeOn and determines the services, capabilities, and commercial rights available during the subscription period.

A subscription is independent of the technical implementation used to enforce access.

---

## 5.2 Commercial Subscription Hierarchy

The subscription hierarchy is designed to mirror how organizations operate their businesses.

```text
Organization
      │
      ▼
Facility
      │
      ▼
Subscription Plan
      │
      ▼
License
      │
      ▼
Platform Access
```

Each subscribed Facility maintains its own commercial identity while remaining under the same Organization.

---

## 5.3 Subscription Unit

The primary subscription unit within Digitize is the **Facility**.

Examples:

| Organization       | Facility      | Subscription |
| ------------------ | ------------- | ------------ |
| ABC Sports Pvt Ltd | Swimming Pool | Required     |
| ABC Sports Pvt Ltd | Gym           | Required     |
| ABC Sports Pvt Ltd | Yoga Centre   | Required     |

Each Facility operates independently from a commercial perspective.

A Facility may subscribe to a different commercial plan based on its operational requirements.

---

## 5.4 Subscription Ownership

Subscriptions are owned by the Organization but allocated to individual Facilities.

Responsibilities include:

### Organization

* Commercial agreement with OreeOn.
* Billing responsibility.
* Payment responsibility.
* Subscription ownership.

### Facility

* Operational usage.
* License consumption.
* Business configuration.
* Daily platform operations.

This separation enables centralized commercial management while allowing Facilities to operate independently.

---

## 5.5 Subscription Characteristics

Every subscription contains the following information:

* Subscription Identifier
* Organization
* Facility
* Subscription Plan
* Subscription Status
* Billing Cycle
* Activation Date
* Expiry Date
* Renewal Status
* License Information
* Commercial History

Additional commercial metadata may be introduced in future versions without changing the subscription architecture.

---

## 5.6 Subscription Scope

A subscription grants access only to the subscribed Facility.

It does not automatically activate:

* Other Facilities.
* Other Organizations.
* Additional Products.
* Future Premium Services.

Each commercial entitlement must be explicitly licensed.

---

# 6. Licensing Model

## 6.1 Purpose

While a Subscription represents the commercial agreement, a License represents the operational permission granted by the platform.

The distinction between these concepts is intentional.

| Subscription        | License                |
| ------------------- | ---------------------- |
| Commercial Contract | Operational Permission |
| Managed by Business | Managed by System      |
| Billing & Renewals  | Platform Access        |
| Customer Agreement  | Access Enforcement     |

This separation provides flexibility for future licensing models without altering commercial agreements.

---

## 6.2 License Generation

A License is automatically generated when:

* A subscription becomes active.
* Commercial validation succeeds.
* Required business information is complete.
* Initial payment conditions are satisfied (where applicable).

The generated License authorizes platform access according to the subscribed plan.

---

## 6.3 License Scope

Each License is associated with exactly one subscribed Facility.

A License determines:

* Platform access.
* Enabled capabilities.
* Subscription validity.
* Operational status.
* Commercial entitlement.

A License cannot be shared across Facilities.

---

## 6.4 License States

Every License exists in one of the following operational states.

| Status    | Description                |
| --------- | -------------------------- |
| Pending   | Awaiting activation.       |
| Active    | Fully operational.         |
| Suspended | Temporarily disabled.      |
| Expired   | Subscription period ended. |
| Cancelled | Permanently terminated.    |

Additional operational states may be introduced as the licensing framework evolves.

---

## 6.5 License Validation

Every authenticated platform request requiring protected functionality must validate the License.

Validation includes:

* License status.
* Subscription validity.
* Commercial entitlement.
* Plan capabilities.
* Operational restrictions.

License validation ensures only authorized Facilities access subscribed functionality.

---

# 7. Subscription Plans

## 7.1 Overview

Digitize offers standardized subscription plans that support organizations at different stages of business maturity.

Subscription plans are designed around **business capabilities**, not customer volume.

This approach encourages customer growth while maintaining predictable commercial relationships.

Version 1.0 defines four commercial plans.

* Launch
* Grow
* Scale
* Enterprise

Future plans may be introduced without affecting existing subscriptions.

---

## 7.2 Launch Plan

The Launch plan is intended for organizations beginning their digital transformation journey.

Typical characteristics:

* Essential operational capabilities.
* Core membership management.
* Attendance management.
* Billing and invoicing.
* Standard reporting.
* Basic operational dashboards.

The Launch plan focuses on establishing a digital operational foundation.

---

## 7.3 Grow Plan

The Grow plan supports organizations that have established stable operations and require enhanced business capabilities.

Typical enhancements include:

* Advanced reporting.
* Enhanced dashboards.
* Advertisement management.
* Extended operational controls.
* Additional configuration options.
* Improved business insights.

The Grow plan enables organizations to optimize operational efficiency while preparing for future expansion.

---

## 7.4 Scale Plan

The Scale plan targets mature organizations with more sophisticated operational and management requirements.

Potential capabilities include:

* Advanced analytics.
* Executive dashboards.
* API integrations.
* Enhanced security.
* Advanced workflow configuration.
* Operational automation.

The Scale plan supports organizations focused on operational excellence and business scalability.

---

## 7.5 Enterprise Plan

The Enterprise plan is designed for organizations requiring enterprise governance, centralized administration, and premium commercial services.

Typical enterprise capabilities may include:

* Enterprise administration.
* Multi-Facility governance.
* Consolidated reporting.
* Priority support.
* Enterprise integrations.
* Dedicated commercial agreements.

Enterprise offerings may include customized commercial arrangements while remaining aligned with the core subscription architecture.

---

## 7.6 Plan Evolution

Subscription plans will evolve over time as Digitize introduces new capabilities.

Plan evolution should follow these principles:

* Preserve backward compatibility where practical.
* Avoid disrupting existing customers.
* Introduce value through additional capabilities.
* Maintain clear differentiation between plans.

Changes to plan composition shall be managed through version-controlled commercial strategy updates.

---

# 8. Site Licensing

## 8.1 Purpose

A Site represents a physical operating location belonging to a subscribed Facility.

Sites exist to support organizations operating from multiple geographic locations while maintaining a single business identity for the Facility.

Examples:

**Facility:** Swimming Pool

Sites:

* HSR Layout
* Jayanagar
* Whitefield

The Site model enables business expansion without creating separate commercial entities.

---

## 8.2 Commercial Principle

The commercial subscription is always associated with the **Facility**.

Sites inherit their commercial entitlement from the subscribed Facility.

A Site never owns an independent subscription.

---

## 8.3 Version 1.0 Commercial Assumption

For Version 1.0 of the commercial strategy:

* By default, every Facility subscription includes one (1) Site.
* The underlying platform supports multiple Sites per Facility.
* Additional Sites are enabled through commercial Site Add-ons.
* Site Add-ons inherit the parent Facility’s subscription plan and enabled capabilities.
* Site Add-ons are billed together with the parent Facility subscription and may be prorated during mid-cycle activation.
* This is a commercial packaging policy only and does not restrict the platform architecture.

These assumptions are subject to future commercial review without changing the core subscription architecture.

---

## 8.4 Site Characteristics

Every Site maintains operational information such as:

* Site Identifier
* Facility Association
* Site Name
* Physical Address
* Operational Status
* Business Hours
* Staff Assignment
* Local Configuration
* Operational Reports

Commercial ownership always remains with the parent Facility.

---

## 8.5 Site Independence

Although Sites share the same subscription, each Site operates independently from an operational perspective.

Each Site may maintain:

* Independent staff.
* Independent attendance.
* Independent customers (where applicable).
* Independent trainer schedules.
* Independent operational reports.
* Independent business timings.

This enables organizations to operate multiple locations while maintaining centralized commercial management.

---

# 9. Subscription Lifecycle

## 9.1 Overview

Every subscription progresses through a controlled lifecycle from creation until termination.

The lifecycle ensures predictable commercial operations while protecting platform integrity.

---

## 9.2 Subscription Lifecycle Flow

```text
Draft
   │
   ▼
Pending Activation
   │
   ▼
Active
   │
   ├──────────────┐
   ▼              │
Renewed           │
   │              │
   ▼              │
Active            │
                  │
        Suspended │
             │    │
             ▼    │
          Reactivated
             │
             ▼
           Active
             │
             ▼
           Expired
             │
             ▼
         Terminated
```

---

## 9.3 Draft

The subscription record has been created but is not yet commercially valid.

Typical characteristics:

* No platform access.
* No active License.
* Configuration may still be modified.
* Awaiting commercial completion.

---

## 9.4 Pending Activation

The subscription has been submitted for activation.

Typical activities include:

* Commercial validation.
* Payment verification.
* Business verification.
* License preparation.

The Facility remains inaccessible until activation is completed.

---

## 9.5 Active

The subscription becomes fully operational.

Characteristics include:

* License generated.
* Facility activated.
* Platform access granted.
* Commercial validity established.
* Operational activities permitted.

This is the normal operating state.

---

## 9.6 Renewed

Renewal extends the subscription into a new commercial period without interrupting business operations.

Renewals should preserve:

* Subscription history.
* Facility configuration.
* Business data.
* Operational continuity.

A renewed subscription continues under the applicable commercial terms.

---

## 9.7 Suspended

A subscription may be temporarily suspended due to operational or commercial reasons.

Examples:

* Payment failure.
* Administrative suspension.
* Compliance review.
* Customer request.

During suspension:

* Platform access may be restricted.
* Operational data remains preserved.
* No business data is deleted.

---

## 9.8 Expired

An expired subscription indicates that the commercial validity period has ended.

Characteristics:

* License expires.
* Platform access is disabled.
* Business data is retained according to data retention policies.
* Renewal remains possible during the applicable retention period.

---

## 9.9 Terminated

Termination permanently concludes the commercial relationship for the subscribed Facility.

Termination may occur due to:

* Customer cancellation.
* Permanent closure.
* Contract termination.
* Administrative decision.

Historical commercial records remain available for audit purposes.

---

# 10. License Lifecycle

## 10.1 Overview

The License Lifecycle governs the operational authorization used by Digitize to enforce subscription entitlements.

Unlike subscriptions, licenses are system-generated and lifecycle events are automatically managed by the platform.

---

## 10.2 License Lifecycle Flow

```text
Generated
    │
    ▼
Activated
    │
    ▼
Operational
    │
    ├──────────────┐
    ▼              │
Suspended          │
    │              │
    ▼              │
Reactivated        │
    │              │
    ▼              │
Operational        │
                   │
               Expired
                   │
                   ▼
              Archived
```

---

## 10.3 Generated

The platform generates a License immediately after a subscription satisfies all activation requirements.

The generated License remains inactive until formal activation.

---

## 10.4 Activated

An activated License authorizes the subscribed Facility to access Digitize according to its subscribed commercial plan.

Activation occurs automatically after successful commercial validation.

---

## 10.5 Operational

The License is fully active.

The Facility can perform all operations permitted by its subscription plan.

Every protected platform request validates the operational License before processing.

---

## 10.6 Suspended

A License may be suspended when:

* Subscription payments fail.
* The associated subscription is suspended.
* Administrative action requires temporary restriction.
* Security concerns are identified.

License suspension immediately affects platform access but does not remove customer data.

---

## 10.7 Reactivated

Once suspension conditions are resolved, the License returns to operational status without requiring data restoration or platform reconfiguration.

---

## 10.8 Expired

When the associated subscription expires, the License automatically expires.

Expired Licenses cannot authorize platform operations.

---

## 10.9 Archived

Expired or terminated Licenses are archived for historical, financial, compliance, and audit purposes.

Archived Licenses are never reused or reassigned.

---

# 11. Subscription Operations

## 11.1 Purpose

Subscription Operations define the commercial processes responsible for managing subscriptions throughout their operational lifecycle.

These processes ensure that every subscription is administered consistently from activation until termination while maintaining commercial accuracy, operational continuity, and customer satisfaction.

Subscription operations are executed by authorized platform administrators and automated platform services according to the commercial policies defined by OreeOn.

---

## 11.2 Core Subscription Operations

The platform shall support the following subscription operations:

* Create Subscription
* Activate Subscription
* Modify Subscription
* Upgrade Subscription
* Downgrade Subscription
* Renew Subscription
* Suspend Subscription
* Reactivate Subscription
* Cancel Subscription
* Expire Subscription
* Archive Subscription

Each operation shall be fully auditable.

---

## 11.3 Operational Principles

Subscription operations shall follow these principles:

* Every operation must be traceable.
* Commercial history shall never be deleted.
* Changes shall not impact historical invoices.
* Active business data shall always be preserved.
* Subscription changes shall respect licensing policies.
* All operations shall be recorded in the audit log.

---

# 12. Plan Upgrade & Downgrade Strategy

## 12.1 Overview

Organizations may change their subscription plan as their business requirements evolve.

The platform shall support both upgrades and downgrades while ensuring commercial integrity and uninterrupted business operations.

---

# 12.2 Upgrade Strategy

An upgrade occurs when a Facility transitions to a subscription plan that provides additional commercial capabilities.

Example:

```text
Launch
      │
      ▼
Grow
      │
      ▼
Scale
      │
      ▼
Enterprise
```

Typical upgrade reasons include:

* Business expansion.
* Need for additional features.
* Additional Sites.
* Enterprise governance.
* Advanced reporting.
* Integration requirements.

---

## 12.3 Upgrade Principles

Subscription upgrades shall follow these principles:

* Upgrades should not interrupt business operations.
* Existing business data shall remain intact.
* New capabilities become available immediately after successful activation.
* Previous invoices remain unchanged.
* Upgrade history shall be retained permanently.
* Any pricing adjustments are prorated to the effective upgrade date.

Commercial pricing adjustments are defined in CS-02 – Pricing Strategy.

---

## 12.4 Downgrade Strategy

Organizations may reduce their subscription plan when advanced capabilities are no longer required.

Example:

```text
Enterprise
        │
        ▼
Scale
        │
        ▼
Grow
        │
        ▼
Launch
```

Downgrades are commercial events and must preserve historical operational data.

---

## 12.5 Downgrade Principles

Downgrades shall follow these principles:

* Existing business data shall never be deleted.
* Features unavailable in the downgraded plan become inaccessible.
* Historical reports remain preserved.
* Commercial history remains unchanged.
* Customers shall receive advance notification before downgrade takes effect.
* Downgrades are normally scheduled for the next renewal cycle to avoid mid-cycle capability disruption.
* If an immediate downgrade is requested, the effective date and any proration calculations must be approved by commercial policy.

Downgrades should normally become effective at the next renewal cycle unless explicitly approved by commercial policy.

---

# 13. Renewal Strategy

## 13.1 Purpose

Subscription renewal extends commercial access for an additional subscription period.

Renewal is intended to preserve uninterrupted business operations while maintaining an ongoing commercial relationship between the customer and OreeOn.

---

## 13.2 Renewal Methods

Version 1.0 supports the following renewal methods:

### Manual Renewal

The Organization initiates the renewal process.

---

### Assisted Renewal

Renewal is coordinated by OreeOn's commercial or customer success team.

---

### Automatic Renewal

Automatic renewal is supported when the customer has provided a valid payment method and consent for recurring billing.
* Automatic renewals are subject to commercial governance and may be enabled only for applicable plans and regions.
* Customers may opt out of automatic renewal at any time prior to the renewal date.

---

## 13.3 Renewal Principles

Renewals shall:

* Preserve all business data.
* Preserve Facility configuration.
* Preserve customer information.
* Preserve operational continuity.
* Extend License validity.
* Create a complete commercial audit trail.

No operational reconfiguration shall be required following a successful renewal.

---

## 13.4 Renewal Notifications

The platform shall support configurable renewal reminders.

Typical notification schedule:

* 30 days before expiry.
* 15 days before expiry.
* 7 days before expiry.
* 3 days before expiry.
* Expiry day.
* Grace period reminders (if applicable).

Notification templates are managed independently from the subscription engine.

---

# 14. Suspension & Grace Period

## 14.1 Suspension

Subscription suspension is a temporary commercial restriction applied to a subscribed Facility.

Typical reasons include:

* Payment overdue.
* Administrative review.
* Customer request.
* Compliance investigation.

Suspension temporarily restricts operational access while preserving all business information.

---

## 14.2 Suspension Principles

During suspension:

* Business data remains preserved.
* Customer information remains preserved.
* Historical invoices remain accessible.
* Platform access is restricted according to suspension policy.
* Commercial obligations remain unchanged.

---

## 14.3 Grace Period

Following subscription expiry, OreeOn provides a configurable Grace Period before permanent service interruption.

Version 1.0 recommends a default Grace Period of fourteen (14) days, subject to commercial agreement.

The duration may vary according to:

* Subscription plan.
* Commercial agreement.
* Organization type.
* Regional business policy.

Specific durations are maintained outside this document.

---

## 14.4 Grace Period Behaviour

During the Grace Period:

* Business data remains available.
* Renewal is permitted.
* Commercial reminders continue.
* Operational restrictions may apply according to policy.

Upon successful renewal, normal operations resume without data loss.

---

# 15. Trial Strategy

## 15.1 Purpose

A Trial Subscription allows prospective customers to evaluate Digitize before entering into a commercial subscription agreement.

Trials support customer acquisition while demonstrating platform capabilities.

---

## 15.2 Trial Principles

Trial subscriptions shall:

* Operate independently from commercial subscriptions.
* Have a predefined validity period.
* Convert into commercial subscriptions without data migration.
* Preserve all customer-entered information during conversion.

---

## 15.3 Trial Capabilities

Version 1.0 allows Business Leadership to configure:

* Trial availability.
* Trial duration.
* Available capabilities.
* Conversion eligibility.
* Trial limitations.

These policies are intentionally configurable to support future commercial strategies.

---

## 15.4 Trial Conversion

When a trial converts into a paid subscription:

* Business data is retained.
* Customer data is retained.
* Operational configuration is preserved.
* A commercial subscription is created.
* A production License is generated.
* Commercial history begins from the subscription activation date.

No manual migration should be required.

---

# 16. Enterprise Licensing

## 16.1 Purpose

Enterprise Licensing is designed for organizations that require centralized governance, advanced operational capabilities, premium support, and customized commercial agreements.

Enterprise Licensing extends the standard commercial model without introducing a separate product or independent platform.

All Enterprise customers continue to operate on the Digitize platform developed by OreeOn.

---

## 16.2 Enterprise Philosophy

Enterprise Licensing follows these principles:

* Single configurable platform.
* Centralized commercial agreement.
* Standardized subscription governance.
* Flexible commercial packaging.
* Long-term customer partnership.

Enterprise Licensing enhances commercial flexibility while preserving platform consistency.

---

## 16.3 Enterprise Characteristics

Enterprise agreements may include:

* Multiple subscribed Facilities.
* Large numbers of operational Sites.
* Organization-wide administration.
* Centralized reporting.
* Executive dashboards.
* Enterprise integrations.
* Dedicated onboarding.
* Priority customer support.
* Custom Service Level Agreements (SLAs).
* Named Customer Success Manager.

Enterprise offerings are defined through commercial agreements while remaining compatible with the core subscription architecture.

---

## 16.4 Enterprise Subscription Governance

Enterprise Organizations continue to operate using Facility-based subscriptions.

However, OreeOn may manage these subscriptions through a consolidated Enterprise Agreement for commercial simplicity.

Characteristics include:

* Centralized billing.
* Consolidated invoicing.
* Unified renewal cycle.
* Enterprise reporting.
* Commercial account management.
* Volume-based commercial agreements (where applicable).

This approach preserves the integrity of the subscription model while simplifying administration for large customers.

---

## 16.5 Enterprise Licensing Principles

Enterprise Licensing shall:

* Remain compatible with the standard subscription model.
* Preserve Facility-level operational independence.
* Support organization-wide governance.
* Avoid creating separate licensing architectures.
* Maintain backward compatibility wherever practical.

---

# 17. Future Commercial Expansion

## 17.1 Purpose

The commercial architecture has been intentionally designed to support future business growth without requiring structural redesign.

Future commercial offerings should extend the existing subscription model rather than replace it.

---

## 17.2 Capability Packs

Future versions of Digitize may introduce optional Capability Packs.

Examples include:

* Artificial Intelligence (AI) Pack.
* Advanced Analytics Pack.
* WhatsApp Automation Pack.
* Public API Pack.
* Payroll Pack.
* Marketing Automation Pack.
* Marketplace Pack.
* Premium Reporting Pack.

Capability Packs provide additional business value while remaining independent of the base subscription plan.

---

## 17.3 Industry-Specific Packages

As Digitize expands beyond swimming pools, OreeOn may introduce industry-specific commercial packages for supported Facility Types.

Examples include:

* Gym Operations Package.
* Yoga Studio Package.
* Dance Academy Package.
* Football Academy Package.
* Indoor Sports Package.

These packages will build upon the common platform and leverage the same commercial architecture.

---

## 17.4 Partner & Channel Programs

Future commercial strategies may include:

* Implementation Partners.
* Technology Partners.
* Franchise Programs.
* Reseller Programs.
* Referral Programs.

These initiatives will extend the commercial reach of Digitize without altering its licensing framework.

---

## 17.5 Commercial Evolution Principles

Future commercial enhancements shall:

* Preserve customer investments.
* Maintain backward compatibility where practical.
* Minimize disruption during upgrades.
* Align with the long-term Product Vision.
* Be governed through version-controlled Commercial Strategy documents.

---

# 18. Business Rules Summary

The following business rules define the baseline commercial behaviour for Version 1.0.

| Rule ID   | Business Rule                                                                                              |
| --------- | ---------------------------------------------------------------------------------------------------------- |
| CS-BR-001 | OreeOn is the legal company responsible for the Digitize platform.                                         |
| CS-BR-002 | Digitize is the SaaS product offered by OreeOn.                                                            |
| CS-BR-003 | An Organization is the contracting customer.                                                               |
| CS-BR-004 | A Facility is the primary subscription unit.                                                               |
| CS-BR-005 | Every subscribed Facility requires an active subscription.                                                 |
| CS-BR-006 | Every active subscription generates a License.                                                             |
| CS-BR-007 | A License authorizes operational access to the platform.                                                   |
| CS-BR-008 | Sites inherit the commercial entitlement of their parent Facility.                                         |
| CS-BR-009 | Sites do not own independent subscriptions.                                                                |
| CS-BR-010 | Subscription Plans define available business capabilities.                                                 |
| CS-BR-011 | Subscription Plans do not limit customer growth by user count, membership count, or transaction volume.    |
| CS-BR-012 | Subscription changes shall preserve business data and historical commercial records.                       |
| CS-BR-013 | Commercial pricing is governed by CS-02 – Pricing Strategy.                                                |
| CS-BR-014 | Billing behaviour is governed by CS-03 – Billing & Invoicing Strategy.                                     |
| CS-BR-015 | Promotional offers are governed by CS-04 – Discount & Promotion Policy.                                    |
| CS-BR-016 | Future commercial enhancements shall extend the existing subscription architecture rather than replace it. |

These rules form the baseline commercial governance for Digitize Version 1.0.

---

# 19. Document References

The Subscription & Licensing Strategy is part of the Commercial Strategy documentation set and shall be read in conjunction with the following documents.

### Product Foundation

* PF-01 – Product Glossary
* PF-02 – Domain Model
* PF-03 – Product Vision
* PF-04 – Business Model
* PF-05 – Product Evolution & Release Strategy

### Commercial Strategy

* CS-02 – Pricing Strategy
* CS-03 – Billing & Invoicing Strategy
* CS-04 – Discount & Promotion Policy

### Business Analysis

* BA-01 – Business Requirements Document (BRD)
* BA-02 – Business Rules
* BA-03 – Business Process Catalog
* BA-04 – Business Flows
* BA-05 – User Personas
* BA-06 – User Journeys
* BA-07 – Stakeholder Matrix
* BA-08 – Requirement Traceability Matrix

### Functional Documentation

* Functional Requirements Specification (FRS)
* System Architecture Document (SAD)
* Database Design
* API Specifications
* UI/UX Design
* Test Strategy

---

# 20. Revision History

| Version | Date      | Author                                          | Description                                                                                         |
| ------- | --------- | ----------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| 1.0     | July 2026 | Product Strategy & Commercial Architecture Team | Initial release of the Subscription & Licensing Strategy based on the Version 1.0 commercial model. |

---

# End of Document