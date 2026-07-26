# Decision Log

> **Document ID:** PM-01  
> **Document Name:** Decision Log  
> **Version:** 1.0  
> **Status:** Approved  
> **Owner:** Product Team  
> **Last Updated:** July 2026

---

# 1. Purpose

The Decision Log records significant product, business, architectural, and governance decisions made during the lifecycle of Digitize by OreeOn Technologies Pvt. Ltd.

Its purpose is to preserve the reasoning behind important decisions so that future team members, stakeholders, and implementation teams understand not only *what* was decided, but *why* it was decided.

This document is intended to eliminate repeated discussions, reduce ambiguity, and provide historical traceability for all major product decisions.

---

# 2. Scope

This document includes:

- Business decisions
- Product decisions
- Architecture decisions
- User role decisions
- Commercial decisions
- Platform strategy decisions
- Governance decisions

This document does **not** include:

- Technical implementation details
- Development tasks
- Sprint planning
- Bug fixes
- Minor UI changes

---

# 3. Decision Process

Every major decision should follow the same process.

```text
Problem
      ↓
Analysis
      ↓
Options Considered
      ↓
Final Decision
      ↓
Reason
      ↓
Impact
```

Only approved decisions should be added to this document.

---

# 4. Decision Register

---

## DEC-001

### Title

Platform Strategy

### Decision

Digitize by OreeOn Technologies Pvt. Ltd. will be developed as a configurable SaaS platform rather than a software product dedicated to a single business type.

### Reason

The long-term business vision is to support multiple activity and recreation businesses using a common technology platform.

### Impact

Future facility types can be introduced through configuration rather than rebuilding the application.

---

## DEC-002

### Title

Initial Market Focus

### Decision

Phase 1 will focus exclusively on Swimming Pool Management.

### Reason

Swimming pools provide a well-defined operational model that allows validation of the platform before expanding into additional facility types.

### Impact

All Phase 1 documentation and development will prioritize swimming pools while ensuring future extensibility.

---

## DEC-003

### Title

Business Hierarchy

### Decision

The platform hierarchy is defined as:

```text
Platform
    ↓
Organization
    ↓
Facility
    ↓
Site
```

### Reason

An organization represents the legal business.

A facility represents the business type.

A site represents the operational location.

This hierarchy supports organizations operating multiple facilities and multiple locations.

### Impact

All future documentation, database design, APIs, and UI must follow this hierarchy.

---

## DEC-004

### Title

Facility Ownership

### Decision

One Organization may own multiple Facilities.

### Reason

Future business expansion requires organizations to manage different activity businesses under one account.

Example:

- Swimming Pool
- Gym
- Yoga Centre

### Impact

The platform supports multi-facility organizations without architectural changes.

---

## DEC-005

### Title

Site Ownership

### Decision

Each Facility may operate multiple Sites.

### Reason

Business operations are location-specific.

Each site may have different staff, operating hours, memberships, pricing, and customer base.

### Impact

Operational management becomes site-specific while maintaining centralized organizational governance.

---

## DEC-006

### Title

User Roles

### Decision

The platform will initially support:

- Platform Admin
- Organization Admin
- Site Admin
- Staff
- Customer

### Reason

This hierarchy simplifies governance and avoids unnecessary management layers.

### Impact

The Manager role is removed from the initial product scope.

**Action:** Update the Role & Permission Matrix (FRS) and all RBAC-related API and UI specifications to remove "Manager". Owner: Solution Architect. Target: Update FR and API artifacts before FR freeze.

---

## DEC-007

### Title

Approval Workflow

### Decision

Site Admins cannot directly publish business configuration changes.

All configuration changes require Organization Admin approval.

### Reason

Organizations require centralized governance to ensure consistency across sites.

### Impact

Approval workflows become a core platform capability.

---

## DEC-008

### Title

Dynamic User Interface

### Decision

The application interface will be generated based on Facility Type.

### Reason

Different businesses require different operational modules.

Examples:

- Swimming Pool
- Gym
- Yoga Centre
- Dance Studio

### Impact

The platform can support multiple industries without maintaining separate applications.

---

## DEC-009

### Title

Subscription Strategy

### Decision

Subscriptions will be licensed at the Facility level during Phase 1.

### Reason

Facilities operating under the same organization may have different operational requirements and commercial needs.

### Impact

Each facility may independently subscribe to the platform.

---

## DEC-010

### Title

Platform Capabilities

### Decision

Platform functionality will be controlled through configurable platform capabilities.

### Reason

Different subscription plans should enable different features without changing the application.

### Impact

Future commercial models become configuration-driven.

---

## DEC-011

### Title

Documentation Standard

### Decision

Markdown is the official documentation format.

Mermaid is the standard diagram format.

Draw.io will be used only where Mermaid is insufficient.

### Reason

Text-based documentation is version-controlled, maintainable, and developer-friendly.

### Impact

All future documentation follows the same standard.

---

## DEC-012

### Title

Documentation Governance

### Decision

Every document will have:

- Unique Document ID
- Version
- Status
- Owner
- Purpose
- Scope

### Reason

Consistent documentation improves maintainability and review.

### Impact

All documentation follows the same structure.

---

## DEC-013

### Title

Technical Baseline Governance

### Decision

Product-level business decisions shall be maintained in this Decision Log (PM-01).

Technology-specific implementation decisions shall be maintained as individual Decision Records under the `99_Decision_Records` folder.

### Reason

Separating business governance from technology governance keeps this document focused while allowing technical decisions to evolve independently.

### Impact

Business documentation references PM-01 for product decisions, while engineering teams reference the approved Decision Records for technology baselines.

---

# 5. Future Decisions

Future architectural and business decisions should be appended to this document.

Existing decisions must never be deleted.

If a decision changes, a new decision record should reference the previous one and explain the reason for the update.

---

# 6. Guiding Principles

All decisions should align with the following principles:

- Business First
- Configuration Over Customization
- Scalability by Design
- Single Source of Truth
- Future Ready
- Operational Simplicity
- Enterprise Governance

---

# 7. Approval

| Role | Responsibility |
|------|----------------|
| Product Owner | Reviews business decisions |
| Solution Architect | Reviews architecture decisions |
| CTO | Approves technical and product decisions |


## Approval Thresholds
Approval is determined by the documented impact level for the change. Impact levels and required approvers are defined below.

| Impact Level | Criteria / Examples | Required Approvals |
|--------------|---------------------|--------------------|
| Low | Minor UI text, help copy, non-functional editorial updates, documentation-only changes | Product Owner |
| Medium | Functional behavior changes that do not modify architecture or core data models, API contract extensions (backward-compatible), pricing changes < 10% | Product Owner + Solution Architect |
| High | Architecture changes, database schema or core data model changes, breaking API contract changes, pricing or commercial model changes >= 10%, security or regulatory-impacting changes | Product Owner + CTO + Founders |

All approvals must reference the associated `CR-` and any related `DR-` or `DOC-GAP-` IDs. When impact assessment is ambiguous, escalate to Product Owner + Solution Architect for an impact determination prior to approval routing.

---

# 8. Revision History

| Version | Date | Description |
|----------|------|-------------|
| 1.0 | July 2026 | Initial Decision Log |