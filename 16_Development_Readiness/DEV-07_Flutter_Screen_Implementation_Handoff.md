# DEV-07 Flutter Screen Implementation Handoff

> Flutter route, screen, widget, API, state, permission, and validation handoff for implementation.

---

# Document Control

| Field | Value |
|---|---|
| Document ID | DEV-07 |
| Document Name | Flutter Screen Implementation Handoff |
| Folder | 16_Development_Readiness |
| Product | Digitize by OreeOn Technologies Pvt. Ltd. |
| Status | Design Draft |
| Owner | UI/UX Design / Frontend Engineering |
| Reviewers | Product, API, Backend, QA, Security |
| Version | 1.0 |
| Last Updated | 2026-07-24 |

---

# 1. Purpose

This document maps approved UI/UX screens to Flutter implementation artifacts.

It helps Flutter development start with clear route names, widget ownership, API dependencies, validation behavior, and screen states.

---

# 2. Screen Handoff Fields

Each screen handoff shall define:

- Screen ID.
- Screen name.
- Flutter route.
- Flutter page/widget name.
- Feature module.
- API calls.
- Form fields.
- Validation.
- Required permissions.
- Tenant context.
- Loading, empty, error, success, restricted, and offline states.
- Web, tablet, and mobile behavior.

---

# 3. First Slice Screen Map

| Screen ID | Screen Name | Flutter Route | Flutter Page | Module | API Dependency | Permission |
|---|---|---|---|---|---|---|
| UI-AUTH-001 | Login | `/login` | `LoginPage` | `auth` | API-03 | Public / unauthenticated |
| UI-HOME-001 | App Shell | `/` | `AppShellPage` | `app` | API-03, API-23 | Authenticated |
| UI-ORG-001 | Organization List | `/organizations` | `OrganizationListPage` | `organization` | API-02 | `organization.view` |
| UI-ORG-002 | Organization Detail | `/organizations/:organization_id` | `OrganizationDetailPage` | `organization` | API-02 | `organization.view` |
| UI-ORG-003 | Organization Form | `/organizations/new`, `/organizations/:organization_id/edit` | `OrganizationFormPage` | `organization` | API-02 | `organization.create`, `organization.update` |
| UI-FAC-001 | Facility List | `/organizations/:organization_id/facilities` | `FacilityListPage` | `facility` | API-02 | `facility.view` |
| UI-FAC-002 | Facility Form | `/organizations/:organization_id/facilities/new` | `FacilityFormPage` | `facility` | API-02 | `facility.create` |
| UI-SITE-001 | Site List | `/facilities/:facility_id/sites` | `SiteListPage` | `site` | API-02 | `site.view` |
| UI-SITE-002 | Site Form | `/facilities/:facility_id/sites/new` | `SiteFormPage` | `site` | API-02 | `site.create` |
| UI-CTX-001 | Tenant Context Selector | App shell embedded | `TenantContextSelector` | `tenant_context` | API-02, API-03 | Authenticated |

---

# 4. Required Screen States

Every first-slice data screen shall implement:

- Initial loading.
- Empty state.
- Loaded state.
- Validation error.
- API error.
- Unauthorized/restricted state.
- Retry state.
- Save-in-progress state.
- Save-success state.

---

# 5. Responsive Rules

Flutter screens shall support:

- Mobile single-column layout.
- Tablet two-column or adaptive layout where useful.
- Web layout with persistent navigation where space permits.
- Forms with scroll-safe behavior.
- No clipped buttons or hidden validation messages.

---

# 6. Handoff Governance

- Screen implementation shall consume `UX-05_UI_Screens.md`.
- Flutter routes shall not invent new product modules.
- API calls shall use approved API documents.
- Backend remains authorization authority.
- UI-hidden actions are convenience only, not security.

---

# 7. Detailed Route Configuration

| Route | Auth Required | Tenant Context Required | Supported Platforms | Default Layout |
|---|---|---|---|---|
| `/login` | No | No | Web, Android, iOS | Centered auth layout |
| `/` | Yes | Partial | Web, Android, iOS | App shell |
| `/organizations` | Yes | No | Web, Android, iOS | List layout |
| `/organizations/new` | Yes | No | Web, Android, iOS | Form layout |
| `/organizations/:organization_id` | Yes | Organization | Web, Android, iOS | Detail layout |
| `/organizations/:organization_id/edit` | Yes | Organization | Web, Android, iOS | Form layout |
| `/organizations/:organization_id/facilities` | Yes | Organization | Web, Android, iOS | List layout |
| `/organizations/:organization_id/facilities/new` | Yes | Organization | Web, Android, iOS | Form layout |
| `/facilities/:facility_id/sites` | Yes | Organization + Facility | Web, Android, iOS | List layout |
| `/facilities/:facility_id/sites/new` | Yes | Organization + Facility | Web, Android, iOS | Form layout |

---

# 8. Screen Field Handoff

## Organization Form

| Field | Type | Required | Editable | Validation | API Mapping |
|---|---|---|---|---|---|
| Organization Name | Text | Yes | Yes | 2 to 150 characters | `organization_name` |
| Organization Code | Text | Yes | Create only | Unique, uppercase-safe slug where approved | `organization_code` |
| Contact Email | Email | Conditional | Yes | Valid email where provided | `contact_email` |
| Contact Phone | Text | Optional | Yes | Region-safe phone format where provided | `contact_phone` |
| Status | Display | No | No | Backend controlled | `organization_status` |

## Facility Form

| Field | Type | Required | Editable | Validation | API Mapping |
|---|---|---|---|---|---|
| Facility Name | Text | Yes | Yes | 2 to 150 characters | `facility_name` |
| Facility Type | Select | Yes | Yes | Must be approved reference value | `facility_type` |
| Organization ID | Hidden/Context | Yes | No | Must match selected context | `organization_id` |
| Status | Display | No | No | Backend controlled | `facility_status` |

## Site Form

| Field | Type | Required | Editable | Validation | API Mapping |
|---|---|---|---|---|---|
| Site Name | Text | Yes | Yes | 2 to 150 characters | `site_name` |
| Facility ID | Hidden/Context | Yes | No | Must match selected context | `facility_id` |
| Address Line | Text | Conditional | Yes | Required if structured address enabled | `address_line` |
| City | Text | Optional | Yes | Text only | `city` |
| Status | Display | No | No | Backend controlled | `site_status` |

---

# 9. API Interaction Map

| Screen | Initial API Call | Submit API Call | Refresh Behavior |
|---|---|---|---|
| Organization List | List Organizations | Not Applicable | Pull-to-refresh/mobile, refresh button/web |
| Organization Detail | Get Organization | Not Applicable | Refresh detail on return from edit |
| Organization Form | Get Organization for edit only | Create or update Organization | Navigate to detail/list after success |
| Facility List | List Facilities by Organization | Not Applicable | Refresh after create |
| Facility Form | Reference values for Facility type | Create Facility | Navigate to Facility list |
| Site List | List Sites by Facility | Not Applicable | Refresh after create |
| Site Form | Optional reference values | Create Site | Navigate to Site list |

---

# 10. Navigation Behavior

- Login success routes to app shell.
- App shell defaults to dashboard or Organization List depending on role.
- Organization List opens Organization Detail.
- Organization Detail opens Facility List.
- Facility List opens Site List.
- Create actions open form routes.
- Cancel returns to previous list or detail route.
- Save success returns to list or detail based on calling route.

---

# 11. Error Handling Behavior

| Error Type | UI Behavior |
|---|---|
| Validation Error | Show field-level errors and summary where useful |
| Unauthorized | Redirect to login if session invalid |
| Forbidden | Show restricted state |
| Tenant Context Invalid | Show context error and prompt re-selection |
| Network Error | Show retry action |
| Server Error | Show safe message and diagnostic IDs |
| Timeout | Show retry action and preserve form input where safe |

---

# 12. Widget Test Expectations

| Widget/Page | Required Tests |
|---|---|
| `LoginPage` | Input validation, failed login, successful login navigation |
| `OrganizationListPage` | Loading, empty, error, loaded |
| `OrganizationFormPage` | Required validation, submit disabled, successful submit |
| `FacilityFormPage` | Facility type required, tenant context applied |
| `SiteFormPage` | Required validation, successful submit |
| `TenantContextSelector` | Cascading Organization to Facility to Site behavior |
| `PermissionGuard` | Allowed, hidden, and restricted states |

