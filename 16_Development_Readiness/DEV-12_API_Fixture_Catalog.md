# DEV-12 API Fixture Catalog

> Reusable API fixture catalog for local mocks, Flutter development, backend contract tests, and QA validation.

---

# Document Control

| Field | Value |
|---|---|
| Document ID | DEV-12 |
| Document Name | API Fixture Catalog |
| Folder | 16_Development_Readiness |
| Product | Digitize by OreeOn Technologies Pvt. Ltd. |
| Status | Design Draft |
| Owner | API / QA |
| Reviewers | Frontend, Backend, Testing |
| Version | 1.0 |
| Last Updated | 2026-07-24 |

---

# 1. Purpose

This catalog defines the initial fixture set required for frontend and backend development.

---

# 2. Fixture Naming

Fixtures shall use:

```text
<module>_<operation>_<scenario>.json
```

Examples:

```text
auth_login_success.json
organization_list_success.json
organization_create_validation_error.json
tenant_context_invalid.json
```

---

# 3. Common Headers Fixture

Required headers:

```json
{
  "authorization": "Bearer mock_access_token",
  "x-correlation-id": "corr-dev-001",
  "x-request-id": "req-dev-001",
  "x-organization-id": "org_dev_001",
  "x-facility-id": "fac_dev_001",
  "x-site-id": "site_dev_001"
}
```

---

# 4. First-Slice Fixture Catalog

| Fixture ID | File | Purpose | Consumer |
|---|---|---|---|
| FX-AUTH-001 | `auth_login_success.json` | Login success response | Flutter, API tests |
| FX-AUTH-002 | `auth_login_invalid_credentials.json` | Login error response | Flutter, API tests |
| FX-AUTH-003 | `auth_current_user_context.json` | Current user, roles, permissions, tenant access | Flutter |
| FX-ORG-001 | `organization_list_success.json` | Organization list with records | Flutter, API tests |
| FX-ORG-002 | `organization_list_empty.json` | Empty organization list | Flutter |
| FX-ORG-003 | `organization_create_request.json` | Create organization request | Backend tests |
| FX-ORG-004 | `organization_create_success.json` | Create organization success | Flutter, API tests |
| FX-ORG-005 | `organization_create_validation_error.json` | Validation error | Flutter, API tests |
| FX-FAC-001 | `facility_list_success.json` | Facility list | Flutter, API tests |
| FX-FAC-002 | `facility_create_success.json` | Facility create success | Flutter, API tests |
| FX-SITE-001 | `site_list_success.json` | Site list | Flutter, API tests |
| FX-SITE-002 | `site_create_success.json` | Site create success | Flutter, API tests |
| FX-ERR-001 | `error_unauthorized.json` | Unauthorized error | Flutter, API tests |
| FX-ERR-002 | `error_forbidden.json` | Forbidden error | Flutter, API tests |
| FX-ERR-003 | `error_tenant_context_invalid.json` | Invalid tenant context error | Flutter, API tests |
| FX-ERR-004 | `error_server_failure.json` | Server failure | Flutter, API tests |

---

# 5. Error Fixture Shape

```json
{
  "error_code": "TENANT_CONTEXT_INVALID",
  "message": "The selected tenant context is not valid for this user.",
  "details": [],
  "correlation_id": "corr-dev-001",
  "request_id": "req-dev-001"
}
```

---

# 6. Governance

- Fixtures shall be updated when API contracts change.
- Fixtures shall use synthetic data only.
- Fixtures shall not include real access tokens or secrets.
- Contract tests should reuse fixture shapes where practical.

---

# 7. First-Slice Request Fixture Details

## `organization_create_request.json`

```json
{
  "organization_name": "Blue Wave Swimming Academy",
  "organization_code": "BLUE_WAVE",
  "contact_email": "admin@example.test",
  "contact_phone": "+10000000000"
}
```

## `facility_create_request.json`

```json
{
  "organization_id": "org_dev_001",
  "facility_name": "Blue Wave Main Pool",
  "facility_type": "SWIMMING_POOL"
}
```

## `site_create_request.json`

```json
{
  "organization_id": "org_dev_001",
  "facility_id": "fac_dev_001",
  "site_name": "Blue Wave Downtown Site",
  "address_line": "Synthetic Address Line",
  "city": "Demo City"
}
```

---

# 8. First-Slice Response Fixture Details

## `auth_current_user_context.json`

```json
{
  "user_id": "usr_dev_001",
  "display_name": "Demo Platform Admin",
  "roles": ["platform_admin"],
  "permissions": [
    "organization.view",
    "organization.create",
    "organization.update",
    "facility.view",
    "facility.create",
    "site.view",
    "site.create"
  ],
  "tenant_access": [
    {
      "organization_id": "org_dev_001",
      "facility_ids": ["fac_dev_001"],
      "site_ids": ["site_dev_001"]
    }
  ]
}
```

## `facility_list_success.json`

```json
{
  "items": [
    {
      "facility_id": "fac_dev_001",
      "organization_id": "org_dev_001",
      "facility_name": "Blue Wave Main Pool",
      "facility_type": "SWIMMING_POOL",
      "facility_status": "ACTIVE"
    }
  ],
  "page": 1,
  "page_size": 20,
  "total_count": 1
}
```

---

# 9. Fixture Versioning

Fixtures shall include an implied API version based on folder path or file metadata.

Recommended structure:

```text
fixtures/
└── v1/
    ├── auth/
    ├── organization/
    ├── facility/
    ├── site/
    └── errors/
```

When API contracts change:

- Update fixture file.
- Update tests consuming the fixture.
- Note compatibility impact in API change log where applicable.
- Do not silently change fixture semantics.

---

# 10. Fixture Ownership Matrix

| Fixture Area | Owner | Reviewer |
|---|---|---|
| Auth fixtures | Backend / Security | Frontend / QA |
| Organization fixtures | Backend / API | Frontend / QA |
| Facility fixtures | Backend / API | Frontend / QA |
| Site fixtures | Backend / API | Frontend / QA |
| Error fixtures | API / QA | Frontend / Backend |
| Tenant context fixtures | Backend / Security | Frontend / QA |

