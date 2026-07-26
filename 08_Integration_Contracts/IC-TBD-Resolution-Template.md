IC Integration Contracts — TBD Resolution Template

Use this template to resolve `[TBD — Source mapping pending — see BE traceability mappings](docs/10_Backend_Engineering/BE-TRACEABILITY_MAPPINGS.md)` entries in IC documents and IC-15 traceability rows. Owners should fill the fields and commit the resolved values.

Document: <IC-XX Document Name>
Owner: <Team or Person>
Date: <YYYY-MM-DD>

1) Source mappings
- Business Requirement IDs (BA-xx):
- Functional Requirement IDs (FR-xx):
- API Document IDs and endpoints (API-xx, API-xx-001 etc):
- Database Table(s) (schema.table or DB-xx):
- Domain Event names (event.name):
- Audit Event IDs (API-13 or audit id):
- UI Workflow IDs (UI-xx or Screen IDs):
- Test Scenario IDs and evidence links (API_Test_Cases.md, Postman links, CI job):

2) Provider mappings (if applicable)
- Provider Name:
- Provider field mappings (provider_field -> Digitize_field):
- Callback signature algorithm and header:
- Required secrets/credential references (Vault path):
- Idempotency and duplicate key mapping:

3) Operational mappings
- Outbox / queue name:
- Dead-letter store reference:
- Reconciliation owner and cadence:
- Runbook link:

4) Security and compliance
- PII or PCI data classification and approved redaction approach:
- Secret rotation schedule or reference:
- Approval reference (ticket/decision record):

5) Acceptance
- Evidence artifacts (links to Postman, CI job, test results):
- Owner sign-off (name, role, date):

Notes:
- Do not invent API or DB IDs. Use authoritative sources from `docs/07_API_Collections` and `docs/06_Database_Design`.
- If a required mapping cannot be provided, state the reason and mitigation plan.
