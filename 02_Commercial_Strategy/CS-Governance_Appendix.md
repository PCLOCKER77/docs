# CS — Governance Appendix

**Purpose:**
This appendix provides approval workflows, governance templates, and auditable forms to support the commercial policies defined in CS-01–CS-04. Use these templates for pricing changes, promotional campaigns, discounts, enterprise offers, billing controls, and authoritative approvals.

## A. Roles & Responsibilities (Quick Reference)

- Platform Owner (OreeOn Technologies Pvt. Ltd. Exec): Final strategic approval for pricing policy changes and enterprise frameworks.
- Business Leadership: Proposes strategic pricing, approves large offers and enterprise agreements.
- Product Management: Author of change, ensures product alignment and impacts are documented.
- Finance: Validates financial impact, tax and revenue recognition implications; approves invoice formats and numbering.
- Sales / Commercial Operations: Proposes commercial offers, validates go-to-market feasibility.
- Marketing: Campaign owner for promotional activities and communications.
- Customer Success: Validates retention/renewal incentives and customer impact.
- Legal: Reviews contractual wording for enterprise offers and compliance exposures.
- Engineering: Implements configuration changes and ensures no embedded pricing logic; provides implementation estimate and rollback plan.
- Platform Admin / Billing Ops: Executes billing engine configuration and monitors live reconciliations.

## B. Pricing Change Approval Workflow

1. Initiation
   - Owner: Product Management / Business Leadership.
   - Deliverable: `Pricing Change Request` (PCR) using the Pricing Change Template below.
2. Impact Assessment
   - Finance prepares revenue, tax, and accounting impact assessment.
   - Product documents functional and UI impact; Engineering provides implementation estimate and risk assessment.
3. Review Forum
   - Cross-functional review meeting: Product, Finance, Sales, Legal (if required), Engineering, CS.
4. Approval
   - For minor changes (non-catalog, non-enterprise): Business Leadership + Finance.
   - For material changes (affects >5% of customer base or regional pricing): Business Leadership + Finance + Platform Owner.
5. Scheduling & Communication
   - Define effective date, customer communications, and transition policy.
6. Implementation
   - Engineering + Billing Ops perform configuration change; validate in staging; deploy according to change window.
7. Audit & Post-Implementation Review
   - Finance reconciles first billing run; Product performs acceptance and reports to governance forum.

## C. Promotion/Discount Approval Workflow

1. Campaign Request (Marketing / Sales)
2. Campaign Risk & Revenue Check (Finance)
3. Campaign Eligibility & Technical Feasibility (Product + Engineering)
4. Approval Levels
   - Small promotional discounts: up to 20% discount OR value up to 1,000 USD (or currency-equivalent): Marketing + Finance.
   - Medium promotional discounts: greater than 20% and up to 50% OR value between 1,001 USD and 10,000 USD: Marketing + Finance + Business Leadership.
   - Large promotional discounts or volume incentives: greater than 50% OR value above 10,000 USD: Business Leadership + Finance + Legal.
   - Campaign budget cap: campaigns with an estimated financial cap above 50,000 USD require Platform Owner notification and Business Leadership review.
5. Publish, Monitor, and Close
   - Campaign owner monitors KPIs; at close, Marketing publishes campaign analysis to governance.

## D. Enterprise Offer Approval Workflow

1. Sales generates `Enterprise Offer Brief` and submits to Business Leadership.
2. Finance performs revenue modeling and tax review.
3. Legal reviews contract terms and SLAs.
4. Final sign-off: Business Leadership + Finance + Legal + Platform Owner (for strategic deals).
5. Post-deal: Billing Ops and Engineering implement consolidated billing and enterprise configuration.

## E. Billing & Invoice Governance

- Invoice Numbering: Finance proposes format; Platform Owner approves. Implementation is configuration-only in Invoice Engine.
- Recommended invoice numbering format (Version 1.0 baseline): `DIG-YYYYMM[-REG]-#####`
   - Explanation: `DIG` = product prefix; `YYYYMM` = invoice year and month; optional `REG` = region/country code; `#####` = zero-padded sequential number per month (e.g., `DIG-202607-IND-00001`).
   - Finance to confirm region code mapping and sequential generation policy. Numbering must support uniqueness, sequential auditability, and regional regulatory requirements.
- Tax Configuration: Finance owns tax rule configuration and must approve any tax profile changes before go-live.
- Credit Notes / Refunds: Require Finance approval according to configured thresholds; refunds above Business Leadership threshold require Business Leadership sign-off.
- Failed Payment Recovery Policy: Billing Ops to operate within configured retry policy; suspensions must follow documented customer communications.

### E.1 Refund Approval Thresholds (recommended defaults)

- Refunds under 500 USD: Billing Ops may approve and process.
- Refunds from 500 USD up to 5,000 USD: Finance approval required.
- Refunds above 5,000 USD: Business Leadership + Finance approval required.

Finance shall publish currency-equivalent thresholds for all supported billing currencies and maintain exchange-rate governance.

## F. Templates (copy into the change request system)

### F.1 Pricing Change Request (PCR) — Template
- PCR ID:
- Requestor:
- Date:
- Summary of change:
- Rationale / business objective:
- Affected plans / regions / customers:
- Revenue impact estimate (Finance):
- Tax & accounting impact (Finance):
- Implementation effort estimate (Engineering):
- Rollback plan:
- Approval required:
  - Business Leadership (Y/N):
  - Finance (Y/N):
  - Legal (Y/N):
  - Platform Owner (Y/N):
- Effective date:
- Communication plan:

### F.2 Promotion Approval Form — Template
- Campaign ID:
- Campaign owner:
- Start / End dates:
- Objective / KPI:
- Eligible plans / customers:
- Discount or incentive details:
- Budget / financial cap:
- Approval signatures: Marketing / Finance / Business Leadership:

### F.3 Enterprise Offer Brief — Template
- Offer ID:
- Account (Organization):
- Offer owner (Sales):
- Executive summary:
- Commercial terms (billing cadence, discounts, effective period):
- SLA & support commitments:
- Implementation timeline:
- Financial model (multi-year revenue, payment terms):
- Legal considerations:
- Approval sign-off:

## G. Audit & Traceability Requirements

- All approvals must be recorded and archived.
- All change requests must include a unique request identifier and a link to supporting documents.
- Implementation events (config changes) must include timestamp, operator, and before/after snapshots.
- Financial events (first billing run post-change) must be reconciled and signed off by Finance.

## H. Implementation Notes

- Keep pricing, tax, invoice, and promotional data in configuration stores not in source code.
- Engineering changes must be reversible and accompanied by migration/rollback scripts where applicable.
- Schedule major commercial changes during low-traffic windows and provide pre/post validation scripts.

## I. Contact & Owners

- Product Management: product-team@oreeon.example
- Finance: finance@oreeon.example
- Legal: legal@oreeon.example
- Billing Ops: billing-ops@oreeon.example
- Platform Owner: ceo@oreeon.example

---

*End of Governance Appendix*
