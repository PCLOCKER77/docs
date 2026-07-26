# DEV-08 Mock API and Fixture Strategy

> Mock API, local fixture, contract-test fixture, and Flutter mock-mode strategy for Digitize.

---

# Document Control

| Field | Value |
|---|---|
| Document ID | DEV-08 |
| Document Name | Mock API and Fixture Strategy |
| Folder | 16_Development_Readiness |
| Product | Digitize by OreeOn Technologies Pvt. Ltd. |
| Status | Design Draft |
| Owner | API / QA / Frontend Engineering |
| Reviewers | Backend, UI/UX, Testing, DevOps |
| Version | 1.0 |
| Last Updated | 2026-07-24 |

---

# 1. Purpose

This document defines how frontend and backend teams shall use mock APIs and fixtures before all backend endpoints are complete.

---

# 2. Mocking Principles

Mocks shall:

- Follow approved API contracts.
- Use realistic but synthetic data.
- Include success and error responses.
- Include tenant context headers.
- Avoid real customer data.
- Avoid becoming the source of truth.
- Be replaced by real API integration as endpoints become available.

---

# 3. Fixture Locations

Recommended fixture locations:

```text
backend/tests/fixtures/
frontend/test/fixtures/
frontend/assets/mock/
docs/16_Development_Readiness/DEV-12_API_Fixture_Catalog.md
```

---

# 4. Mock API Modes

| Mode | Usage |
|---|---|
| Static Fixture Mode | Flutter UI development without backend |
| Local Backend Mode | Flutter calls local FastAPI |
| Contract Test Mode | Backend validates request/response against fixtures |
| Error Simulation Mode | UI validates API error, timeout, restricted, empty, and validation states |

---

# 5. Required First-Slice Fixtures

Fixtures shall exist for:

- Login success.
- Login failure.
- Current user context.
- Authorized organization list.
- Empty organization list.
- Organization create success.
- Organization validation error.
- Facility list.
- Facility create success.
- Site list.
- Site create success.
- Unauthorized error.
- Tenant context error.
- Server error.

---

# 6. Error Fixture Baseline

Error fixtures shall include:

- `error_code`.
- `message`.
- `details`.
- `correlation_id`.
- `request_id`.

Frontend shall display safe user-facing messages and preserve diagnostic IDs where useful.

---

# 7. Governance

- Fixture changes shall be reviewed when API contracts change.
- Fixture data shall remain synthetic.
- Mock-only fields shall not appear in production DTOs.
- Fixtures shall be reused by tests where practical.

---

# 8. Mock Server Strategy

The project may support two mock modes:

| Mock Mode | Description | Owner |
|---|---|---|
| Flutter Fixture Mode | Flutter reads local JSON fixtures without backend dependency | Frontend |
| FastAPI Mock Endpoint Mode | FastAPI exposes temporary mock-backed endpoints before full persistence is implemented | Backend / API |

Mock endpoints shall be disabled outside local development unless explicitly approved.

---

# 9. Fixture Directory Structure

```text
frontend/
└── test/
    └── fixtures/
        ├── auth/
        ├── organization/
        ├── facility/
        ├── site/
        └── errors/

backend/
└── tests/
    └── fixtures/
        ├── requests/
        ├── responses/
        └── errors/
```

---

# 10. Sample Success Fixture

```json
{
  "organization_id": "org_dev_001",
  "organization_name": "Blue Wave Swimming Academy",
  "organization_code": "BLUE_WAVE",
  "organization_status": "ACTIVE",
  "created_at": "2026-07-24T00:00:00Z",
  "updated_at": "2026-07-24T00:00:00Z"
}
```

---

# 11. Sample List Fixture

```json
{
  "items": [
    {
      "organization_id": "org_dev_001",
      "organization_name": "Blue Wave Swimming Academy",
      "organization_code": "BLUE_WAVE",
      "organization_status": "ACTIVE"
    }
  ],
  "page": 1,
  "page_size": 20,
  "total_count": 1
}
```

---

# 12. Mock Data Rules

Mock data shall:

- Use clearly synthetic names.
- Avoid real phone numbers, emails, tax IDs, or addresses.
- Use stable IDs for repeatable tests.
- Include tenant hierarchy fields where required.
- Include both active and inactive lifecycle states where relevant.
- Include edge cases such as long names and missing optional fields.

---

# 13. Error Scenario Coverage

| Scenario | Fixture |
|---|---|
| Missing required field | `organization_create_validation_error.json` |
| Duplicate code | `organization_duplicate_code_error.json` |
| Unauthorized | `error_unauthorized.json` |
| Forbidden | `error_forbidden.json` |
| Invalid tenant context | `error_tenant_context_invalid.json` |
| Backend unavailable | `error_server_failure.json` |
| Timeout | Simulated by mock client delay |

---

# 14. Fixture Review Checklist

- Fixture matches API field naming.
- Fixture includes request and correlation IDs where error response requires them.
- Fixture data is synthetic.
- Fixture is used by at least one test or mock path.
- Fixture does not introduce undocumented fields.
- Fixture status aligns with API version.

