> **Status:** Frozen — 2026-07-26 — 2026-07-26

# API-25 API Mocking and Sandbox Strategy

**Document ID:** API-25  
**Document Name:** API Mocking and Sandbox Strategy  
**Company:** OreeOn Technologies Pvt. Ltd.  
**Product:** Digitize  
**Document Type:** API Testing and Consumer Enablement Documentation  
**Backend Technology:** FastAPI  
**Authentication:** JWT / Mock Auth / Sandbox Auth  
**API Version:** v1  
**Document Version:** 0.1  
**Status:** Design Draft  
**Owner:** API Architecture / QA / DevOps  
**Reviewer:** Solution Architecture / Frontend Architecture / UI/UX / Backend Engineering / Security Architecture  
**Dependencies:** API-00 to API-24, API-26  
**Last Updated:** July 2026

---

# 1. Document Metadata

| Attribute | Value |
|---|---|
| Document ID | API-25 |
| Document Name | API Mocking and Sandbox Strategy |
| Output File | API-25_API_Mocking_and_Sandbox_Strategy.md |
| API Version | v1 |
| Document Version | 0.1 |
| Status | Design Draft |
| Governing Standard | API-00_API_Collection_Standards.md |

---

# 2. Purpose

This document defines how Digitize APIs shall be mocked and sandboxed so UI/UX, frontend, QA, integration, and implementation teams can work before every backend endpoint is complete.

It establishes mock response standards, sandbox restrictions, seed data ownership, simulation rules, synchronization with API contracts, and consumer readiness expectations.

---

# 3. Scope

In scope:

- Mock server approach.
- Mock response standards.
- Success, validation, authorization, empty-state, pagination, slow-response, async, payment, and webhook simulations.
- Sandbox environment usage and restrictions.
- Test tenant and seed data ownership.
- Mock data privacy rules.
- Contract synchronization with API-21 OpenAPI and Postman blueprint.

Out of scope:

- Actual mock server implementation code.
- Production data cloning.
- Real payment capture.
- Real provider webhook secrets.
- UI prototype tooling selection.

---

# 4. Mocking Principles

| Principle | Standard |
|---|---|
| Contract-aligned | Mock responses shall follow API-00 and API module contracts |
| Realistic enough | Mock data shall represent real workflows and edge cases |
| Safe data | Mock data shall be synthetic and non-sensitive |
| Scenario-driven | Mocks shall support API-16 scenarios |
| State-aware | Mock workflows shall follow API-24 states |
| Permission-aware | Mock responses shall support API-23 role/scope behavior |
| Synchronized | Mocks shall be updated when API contracts change |

---

# 5. Mock Server Options

| Option | Usage | Notes |
|---|---|---|
| Postman Mock Server | Quick consumer testing | Good for early UI and API examples |
| OpenAPI Mock Server | Contract-derived mocks | Preferred after API-21 artifact exists |
| Backend Stub Service | Stateful workflow simulation | Useful for complex lifecycle flows |
| Local Frontend Fixtures | Screen-level prototyping | Must stay aligned with API examples |
| Sandbox Backend | Integrated non-production environment | Preferred for end-to-end validation |

---

# 6. Mock Response Envelope

All mock responses shall use API-00 envelopes.

Success example:

```json
{
  "success": true,
  "data": {
    "customer_id": "00000000-0000-4000-8000-000000000001",
    "customer_status": "ACTIVE"
  },
  "metadata": {
    "correlation_id": "00000000-0000-4000-8000-000000000099",
    "timestamp": "2026-07-24T10:30:00Z"
  }
}
```

Error example:

```json
{
  "success": false,
  "error": {
    "error_code": "CUSTOMER_VALIDATION_001",
    "category": "VALIDATION",
    "message": "Customer request validation failed.",
    "retryable": false
  },
  "metadata": {
    "correlation_id": "00000000-0000-4000-8000-000000000099",
    "timestamp": "2026-07-24T10:30:00Z"
  }
}
```

---

# 7. Required Mock Scenarios

| Scenario | Required |
|---|---|
| Happy path success | Yes |
| Validation error | Yes |
| Authorization error | Yes |
| Cross-tenant denial | Yes for tenant APIs |
| Empty list | Yes for list endpoints |
| Pagination first page | Yes for list endpoints |
| Pagination last page | Yes for list endpoints |
| Search no result | Yes for search endpoints |
| Slow response | Yes for high-latency UX |
| Async pending | Yes for async endpoints |
| Async completed | Yes for async endpoints |
| Async failed | Yes for async endpoints |
| Payment success | Yes for payment flows |
| Payment failure | Yes for payment flows |
| Webhook callback simulation | Yes for integration flows |

---

# 8. Mock Data Profiles

| Profile | Purpose |
|---|---|
| `admin_full_access` | Platform and Organization admin screens |
| `facility_manager` | Facility-scoped operations |
| `reception_staff` | Customer, membership, attendance, walk-in workflows |
| `finance_staff` | Billing, payment, refund, reconciliation screens |
| `trainer_assigned` | Assigned trainer schedules and notes |
| `support_user` | Support tickets and support reporting |
| `auditor_read_only` | Audit, compliance, export views |
| `unauthorized_scope` | Cross-tenant negative tests |

---

# 9. Test Tenant Data

Sandbox and mock data shall include:

- Two Organizations.
- At least two Facilities under one Organization.
- At least two Sites under one Facility.
- Active and inactive customers.
- Active, pending-payment, frozen, expired, and cancelled memberships.
- Checked-in and checked-out attendance records.
- Draft, issued, paid, refunded, and cancelled invoices.
- Successful and failed payment attempts.
- Active and suspended subscriptions/licenses.
- Draft, approved, scheduled, launched, paused, and completed campaigns.
- Open, assigned, escalated, resolved, closed, and reopened support tickets.
- Audit events and report export examples.

---

# 10. Empty State Standards

Empty responses shall use valid success envelopes and pagination metadata where applicable.

Example:

```json
{
  "success": true,
  "data": [],
  "metadata": {
    "pagination": {
      "page": 1,
      "page_size": 20,
      "total_items": 0
    }
  }
}
```

UI/UX shall design empty states using these mock responses.

---

# 11. Pagination Mock Standards

Mocks shall support:

- First page.
- Middle page.
- Last page.
- Empty page.
- Maximum page size.
- Cursor response where required.
- Invalid pagination error.

---

# 12. Slow-response Simulation

| Response Type | Simulated Delay |
|---|---|
| Normal read | 300 to 800 ms |
| Search | 500 to 1200 ms |
| Report request | Immediate `202 Accepted` |
| Report completion | 3 to 10 seconds in mock |
| Payment verification | 2 to 8 seconds in mock |
| Webhook delivery | Async state update |

Slow-response simulations help validate loading, disabled, cancellation, and retry states.

---

# 13. Payment Simulation

Payment mocks shall include:

- Online payment initiated.
- Online payment success.
- Online payment failed.
- Online payment pending.
- Offline payment recorded.
- Receipt generated.
- Refund requested.
- Refund success.
- Refund failed.
- Reconciliation completed.

No mock shall contain real card numbers, CVV, bank credentials, or production provider references.

---

# 14. Webhook Simulation

Webhook mocks shall include:

- Valid signed callback.
- Invalid signature.
- Replay event.
- Expired timestamp.
- Delivery success.
- Delivery retry.
- Dead-letter terminal failure.

Mock webhook signatures may use deterministic fake secrets in non-production only.

---

# 15. Async Operation Simulation

Async mocks shall include:

| State | UI Purpose |
|---|---|
| ACCEPTED | Initial async request accepted |
| PENDING | Waiting for processing |
| RUNNING | Active processing |
| COMPLETED | Result available |
| FAILED | Safe failure shown |
| CANCELLED | User/system cancellation |

---

# 16. Sandbox Restrictions

Sandbox shall not:

- Use production credentials.
- Store real payment card data.
- Send real customer notifications unless approved.
- Expose production tenant data.
- Accept unapproved external callbacks.
- Represent itself as production.

Sandbox may:

- Use synthetic tenant data.
- Simulate payment and notification providers.
- Support partner demos.
- Support frontend and QA validation.

---

# 17. Seed Data Ownership

| Data Area | Owner |
|---|---|
| Tenant hierarchy | QA / Implementation |
| Users and roles | Security Architecture / QA |
| Customers and memberships | Product / QA |
| Attendance and walk-ins | QA |
| Training and batches | Product / QA |
| Billing and payments | Commercial Architecture / QA |
| Notifications and campaigns | Product / QA |
| Reports and audit | QA / Data Architecture |

---

# 18. Mock Data Privacy

- Use synthetic names, phone numbers, emails, and addresses.
- Avoid real customer records.
- Avoid real payment references.
- Avoid secrets.
- Clearly mark demo accounts and tenant data.
- Reset sandbox data on approved schedule.

---

# 19. Contract Synchronization

Mocks shall be updated when:

- API-21 OpenAPI schemas change.
- API endpoint request/response changes.
- API-19 error codes change.
- API-24 state transitions change.
- API-23 access rules change.
- API-20 records a relevant change.

---

# 20. UI/UX Usage

UI/UX may use mocks to validate:

- Navigation and screen states.
- Form validation behavior.
- Loading and empty states.
- Permission-based action visibility.
- State-based workflows.
- Error banners and field errors.
- Async report/export progress.
- Payment success/failure flows.

---

# 21. QA Usage

QA may use mocks for:

- Early test case authoring.
- Contract assertions before backend completion.
- Negative-path coverage.
- Regression fixtures.
- Demo data verification.
- Environment validation.

---

# 22. Acceptance Criteria

This document is acceptable when frontend, UI/UX, QA, and backend teams can create mock and sandbox behavior that remains aligned with API contracts, error codes, access rules, state workflows, and release readiness.

---

# 23. Summary

API-25 enables parallel UI, frontend, QA, and backend work by defining a safe, governed mocking and sandbox strategy for Digitize APIs.
