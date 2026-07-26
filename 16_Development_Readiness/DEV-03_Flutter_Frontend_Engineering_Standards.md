# DEV-03 Flutter Frontend Engineering Standards

> Flutter frontend implementation standards for Digitize web, Android, and iOS.

---

# Document Control

| Field | Value |
|---|---|
| Document ID | DEV-03 |
| Document Name | Flutter Frontend Engineering Standards |
| Folder | 16_Development_Readiness |
| Product | Digitize by OreeOn Technologies Pvt. Ltd. |
| Status | Design Draft |
| Owner | Frontend Engineering |
| Reviewers | UI/UX, Backend, API, QA, Security, DevOps |
| Version | 1.0 |
| Last Updated | 2026-07-24 |

---

# 1. Purpose

This document defines how Flutter frontend code shall be structured and governed.

---

# 2. Framework Baseline

Frontend implementation shall use Flutter and Dart per `DR-015_Flutter_Hybrid_Frontend_Baseline.md`.

Targets:

- Web.
- Android.
- iOS.

---

# 3. Architecture Standard

Flutter code shall separate:

- App bootstrap.
- Routing and navigation.
- Feature modules.
- API clients.
- DTOs.
- State management.
- UI components.
- Design tokens.
- Validation.
- Platform-specific adapters.

Feature modules should own their screens, local state, validators, and feature-specific widgets.

---

# 4. API Consumption

Flutter shall consume approved REST APIs only through a controlled API client layer.

API clients shall:

- Add authorization tokens where available.
- Add tenant context headers where required.
- Add correlation or request identifiers where supported.
- Map API errors to user-safe UI states.
- Avoid embedding backend business rules.
- Keep DTOs separate from UI view models.

---

# 5. Auth and Tenant Context

Frontend shall support:

- Login.
- Session restore.
- Logout.
- Token refresh where approved.
- Organization, Facility, and Site context display.
- Role-aware navigation.
- Permission-aware actions.

The backend remains the enforcement authority for authorization and tenant isolation.

---

# 6. State and UX Standards

Every async screen shall support:

- Loading.
- Empty.
- Success.
- Validation error.
- Authorization denied.
- Server error.
- Retry.
- Offline or degraded connectivity where applicable.

Forms shall show field-level validation and preserve user-entered data where safe.

---

# 7. Testing

Flutter testing shall include:

- Unit tests for validators and mappers.
- Widget tests for critical components.
- Feature tests for key screens.
- Integration tests for first vertical slice flows.
- Web, Android, and iOS smoke validation before release candidates.

---

# 8. Release Readiness

Flutter release readiness requires:

- API base URL configured per environment.
- No hardcoded secrets.
- No debug-only endpoints in release builds.
- Platform permissions reviewed.
- Accessibility and responsive behavior checked.
- Error states verified.

---

# 9. State Management Standard

The Flutter app shall use a consistent state-management approach selected during scaffold setup.

State management shall support:

- Async API state.
- Form state.
- Auth/session state.
- Tenant context state.
- Permission state.
- Local mock mode state.

Until a package is selected, feature code shall isolate state behind controllers or notifiers so implementation can evolve without rewriting UI widgets.

---

# 10. Routing Standard

Routes shall:

- Use stable route names.
- Separate public and authenticated routes.
- Support route guards.
- Support restricted-state handling.
- Preserve tenant context where route parameters depend on Organization, Facility, or Site.
- Avoid deep links that bypass backend authorization.

---

# 11. API Client Standard

The API client shall provide:

- Base URL per environment.
- Auth token injection.
- Tenant header injection.
- Correlation/request ID support.
- Timeout handling.
- Error mapping.
- JSON serialization/deserialization.
- Mock fixture mode.

Widgets shall not construct raw HTTP requests directly.

---

# 12. Platform-Specific Rules

| Platform | Rule |
|---|---|
| Web | Validate responsive layouts, browser refresh behavior, and URL routing |
| Android | Validate back navigation, permissions, keyboard behavior, and touch targets |
| iOS | Validate safe areas, navigation gestures, permissions, and form behavior |

---

# 13. Flutter Quality Gates

Before a frontend PR is mergeable:

- Code is formatted.
- Static analysis passes.
- Critical widget tests pass.
- No hardcoded secrets or production URLs exist.
- Shared components are reused where applicable.
- Screen states match DEV-07.

