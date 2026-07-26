# DEV-13 Flutter Component Implementation Map

> Design-system to Flutter component implementation map for Digitize.

---

# Document Control

| Field | Value |
|---|---|
| Document ID | DEV-13 |
| Document Name | Flutter Component Implementation Map |
| Folder | 16_Development_Readiness |
| Product | Digitize by OreeOn Technologies Pvt. Ltd. |
| Status | Design Draft |
| Owner | UI/UX Design / Frontend Engineering |
| Reviewers | Product, QA, Accessibility |
| Version | 1.0 |
| Last Updated | 2026-07-24 |

---

# 1. Purpose

This document maps UI/UX design-system concepts to Flutter components.

It gives frontend engineering a stable component baseline before screen implementation starts.

---

# 2. Component Naming Rules

Flutter components shall use clear `Digitize` or domain-neutral names where shared.

Examples:

```text
DigitizeButton
DigitizeTextField
DigitizeDataTable
TenantContextSelector
PermissionGuard
AsyncStateView
```

---

# 3. Core Component Map

| Component ID | Design Element | Flutter Component | Usage | Owner | First Slice Required |
|---|---|---|---|---|---|
| CMP-001 | App Shell | `DigitizeAppShell` | Main authenticated layout | Frontend | Yes |
| CMP-002 | Navigation Rail / Drawer | `DigitizeNavigation` | Web and mobile navigation | Frontend | Yes |
| CMP-003 | Primary Button | `DigitizeButton` | Main actions | Frontend | Yes |
| CMP-004 | Icon Button | `DigitizeIconButton` | Compact actions | Frontend | Yes |
| CMP-005 | Text Input | `DigitizeTextField` | Forms | Frontend | Yes |
| CMP-006 | Dropdown / Select | `DigitizeSelectField` | Tenant and form selection | Frontend | Yes |
| CMP-007 | Form Section | `DigitizeFormSection` | Grouped form content | Frontend | Yes |
| CMP-008 | Async State Wrapper | `AsyncStateView` | Loading, empty, error, success | Frontend | Yes |
| CMP-009 | Data List | `DigitizeListView` | Mobile/tablet list views | Frontend | Yes |
| CMP-010 | Data Table | `DigitizeDataTable` | Web tabular views | Frontend | Yes |
| CMP-011 | Status Badge | `DigitizeStatusBadge` | Lifecycle/status display | Frontend | Yes |
| CMP-012 | Tenant Context Selector | `TenantContextSelector` | Organization/Facility/Site context | Frontend | Yes |
| CMP-013 | Permission Guard | `PermissionGuard` | UI visibility and restricted state | Frontend | Yes |
| CMP-014 | Error Banner | `DigitizeErrorBanner` | Safe error display | Frontend | Yes |
| CMP-015 | Empty State | `DigitizeEmptyState` | Empty list or no data | Frontend | Yes |
| CMP-016 | Confirmation Dialog | `DigitizeConfirmDialog` | Risky action confirmation | Frontend | No |
| CMP-017 | Search Field | `DigitizeSearchField` | List search | Frontend | Yes |
| CMP-018 | Filter Bar | `DigitizeFilterBar` | List filters | Frontend | No |

---

# 4. Component Rules

Components shall:

- Support light and dark theme readiness where practical.
- Avoid hardcoded API behavior.
- Support accessibility labels.
- Use design tokens from `UX-04_Design_System.md`.
- Avoid clipping text on small screens.
- Expose predictable loading and disabled states.
- Be testable through widget tests.

---

# 5. First Slice Component Priority

Build first:

1. `DigitizeAppShell`
2. `DigitizeNavigation`
3. `DigitizeButton`
4. `DigitizeTextField`
5. `DigitizeSelectField`
6. `AsyncStateView`
7. `TenantContextSelector`
8. `PermissionGuard`
9. `DigitizeListView`
10. `DigitizeDataTable`

---

# 6. Governance

- Shared components shall not contain module-specific business rules.
- Feature-specific widgets shall live inside feature modules.
- Component changes require visual and behavior review.
- Accessibility regressions shall block release-readiness approval.

---

# 7. Component API Expectations

## `DigitizeButton`

Required properties:

- Label or icon.
- Variant: primary, secondary, destructive, ghost.
- Size: small, medium, large.
- Loading state.
- Disabled state.
- Tooltip or semantic label for icon-only buttons.

## `DigitizeTextField`

Required properties:

- Label.
- Value.
- Error text.
- Required indicator.
- Keyboard type.
- Obscure text support.
- Disabled/read-only state.
- Helper text.

## `AsyncStateView`

Required states:

- Loading.
- Empty.
- Error.
- Success content.
- Restricted.
- Retry callback.

## `PermissionGuard`

Required behavior:

- Show child when permission is present.
- Hide child where configured.
- Show restricted fallback where configured.
- Never replace backend authorization.

---

# 8. Design Token Mapping

| Token Area | Flutter Implementation |
|---|---|
| Color | `ColorScheme` and custom semantic colors |
| Typography | `TextTheme` |
| Spacing | Shared spacing constants |
| Radius | Shared radius constants |
| Elevation | Minimal elevation constants |
| Status Colors | Success, warning, error, info, pending, restricted |
| Breakpoints | Layout helper for mobile, tablet, desktop |

---

# 9. Accessibility Requirements

Components shall support:

- Semantic labels.
- Focus order.
- Keyboard navigation where applicable.
- Sufficient color contrast.
- Text scaling without clipping.
- Tap targets appropriate for mobile.
- Non-color-only status communication.

---

# 10. Component Test Map

| Component | Required Test |
|---|---|
| `DigitizeButton` | Disabled, loading, tap callback |
| `DigitizeTextField` | Error display, required state, read-only state |
| `DigitizeSelectField` | Options render, selection callback, validation |
| `AsyncStateView` | Loading, empty, error, success, retry |
| `TenantContextSelector` | Cascading selector behavior |
| `PermissionGuard` | Allowed, hidden, restricted behavior |
| `DigitizeDataTable` | Empty, rows render, action visibility |

---

# 11. First Slice Component Delivery Order

| Order | Component | Reason |
|---|---|---|
| 1 | Theme and tokens | Required by all components |
| 2 | `DigitizeButton` | Required for forms and actions |
| 3 | `DigitizeTextField` | Required for forms |
| 4 | `DigitizeSelectField` | Required for Facility type and tenant context |
| 5 | `AsyncStateView` | Required for API-driven screens |
| 6 | `DigitizeAppShell` | Required for authenticated app |
| 7 | `DigitizeNavigation` | Required for module navigation |
| 8 | `TenantContextSelector` | Required for tenant-aware flows |
| 9 | `PermissionGuard` | Required for permission-aware UI |
| 10 | List/table components | Required for Organization, Facility, Site screens |

