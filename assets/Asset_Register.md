# Asset Register

> Shared visual asset, icon, image, and Flutter asset registration baseline for Digitize by OreeOn Technologies Pvt. Ltd.

---

# Document Control

| Field | Value |
|---|---|
| Document ID | ASSET-01 |
| Document Name | Asset Register |
| Folder | docs/assets |
| Product | Digitize by OreeOn Technologies Pvt. Ltd. |
| Status | Design Draft |
| Owner | UI/UX Design / Frontend Engineering |
| Reviewers | Product, UI/UX, Frontend Engineering, Brand, Security |
| Version | 1.0 |
| Last Updated | 2026-07-24 |

---

# 1. Purpose

This register defines how icons, images, logos, illustrations, diagrams, and Flutter assets shall be named, owned, reviewed, and used.

It prevents undocumented visual assets, inconsistent icon usage, and unsafe asset storage.

---

# 2. Asset Categories

| Category | Usage |
|---|---|
| Brand Assets | Logo, app icon, favicon, splash assets |
| Navigation Icons | Primary module and sidebar icons |
| Action Icons | Create, edit, delete, save, search, filter, export, retry, refresh |
| Status Icons | Success, warning, error, info, pending, restricted |
| Empty State Images | Optional feature empty-state visuals |
| Documentation Diagrams | Architecture, flow, process, deployment, and data diagrams |
| Flutter Runtime Assets | Assets bundled in Flutter app |

---

# 3. Naming Rules

Assets shall use lowercase snake_case.

Examples:

```text
assets/icons/action/add.svg
assets/icons/status/warning.svg
assets/images/empty/customer_empty.png
assets/brand/app_icon.png
```

---

# 4. Flutter Asset Rules

Flutter runtime assets shall:

- Be declared in `frontend/pubspec.yaml`.
- Use stable paths.
- Avoid secret, customer, production, or environment-specific content.
- Include light/dark variants where required.
- Include density variants for app icons and launch assets where platform tooling requires them.

---

# 5. Initial Asset Register

| Asset ID | Asset Name | Category | Intended Path | Usage | Source | Status |
|---|---|---|---|---|---|---|
| AST-BRAND-001 | Digitize App Icon | Brand | `frontend/assets/brand/app_icon.png` | App icon for web, Android, iOS | Brand design | Planned |
| AST-BRAND-002 | Digitize Logo | Brand | `frontend/assets/brand/logo.svg` | App header, login, documentation | Brand design | Planned |
| AST-NAV-001 | Dashboard Icon | Navigation | `frontend/assets/icons/nav/dashboard.svg` | Dashboard navigation | Design system | Planned |
| AST-NAV-002 | Organization Icon | Navigation | `frontend/assets/icons/nav/organization.svg` | Organization module | Design system | Planned |
| AST-NAV-003 | Facility Icon | Navigation | `frontend/assets/icons/nav/facility.svg` | Facility module | Design system | Planned |
| AST-NAV-004 | Site Icon | Navigation | `frontend/assets/icons/nav/site.svg` | Site module | Design system | Planned |
| AST-ACT-001 | Add Icon | Action | `frontend/assets/icons/action/add.svg` | Create action | Design system | Planned |
| AST-ACT-002 | Edit Icon | Action | `frontend/assets/icons/action/edit.svg` | Edit action | Design system | Planned |
| AST-ACT-003 | Delete Icon | Action | `frontend/assets/icons/action/delete.svg` | Delete action | Design system | Planned |
| AST-ACT-004 | Search Icon | Action | `frontend/assets/icons/action/search.svg` | Search field/action | Design system | Planned |
| AST-ACT-005 | Filter Icon | Action | `frontend/assets/icons/action/filter.svg` | Filter action | Design system | Planned |
| AST-STS-001 | Success Icon | Status | `frontend/assets/icons/status/success.svg` | Success state | Design system | Planned |
| AST-STS-002 | Warning Icon | Status | `frontend/assets/icons/status/warning.svg` | Warning state | Design system | Planned |
| AST-STS-003 | Error Icon | Status | `frontend/assets/icons/status/error.svg` | Error state | Design system | Planned |
| AST-STS-004 | Restricted Icon | Status | `frontend/assets/icons/status/restricted.svg` | Permission denied state | Design system | Planned |

---

# 6. Governance

- Assets shall not be added without an owner.
- Brand assets require Product or Brand approval.
- Runtime assets require Frontend review.
- Sensitive screenshots shall not be committed.
- Production customer data shall not be used in assets.

---

# 7. Freeze Rule

This register may remain `Design Draft` until final brand assets are approved.

First vertical slice development may begin with planned assets if Flutter components define safe fallbacks.

---

# 8. Icon Usage Matrix

| UI Area | Preferred Icon Type | Notes |
|---|---|---|
| Primary Navigation | Outline navigation icon | Must remain recognizable at small size |
| Form Actions | Action icon plus label where space allows | Icon-only requires tooltip or semantic label |
| Destructive Actions | Destructive icon and confirmation dialog | Must use warning/destructive color treatment |
| Status Messages | Status icon plus text | Do not rely on color alone |
| Empty States | Optional illustration or simple status icon | Must not distract from primary action |
| Mobile Bottom/Drawer Navigation | Simple high-contrast icon | Must fit mobile tap targets |

---

# 9. Flutter Asset Declaration Example

```yaml
flutter:
  assets:
    - assets/brand/
    - assets/icons/nav/
    - assets/icons/action/
    - assets/icons/status/
    - assets/images/empty/
```

---

# 10. Asset Review Checklist

- Asset has an owner.
- Asset path follows naming rules.
- Asset is not sensitive.
- Runtime asset is declared in Flutter where required.
- Icon has accessible semantic usage.
- Brand asset has Product or Brand approval.
- Asset does not include production customer data.
- Image dimensions are appropriate for web and mobile use.

---

# 11. First Slice Asset Needs

| Need | Asset IDs |
|---|---|
| App shell brand | AST-BRAND-001, AST-BRAND-002 |
| Organization navigation | AST-NAV-002 |
| Facility navigation | AST-NAV-003 |
| Site navigation | AST-NAV-004 |
| Create/edit actions | AST-ACT-001, AST-ACT-002 |
| Search/filter list actions | AST-ACT-004, AST-ACT-005 |
| Status and error states | AST-STS-001, AST-STS-002, AST-STS-003, AST-STS-004 |

---

# 12. Fallback Rule

If final SVG or PNG assets are not available when first-slice development starts, Flutter may use built-in Material icons as temporary implementation placeholders.

Temporary icons shall be tracked and replaced before UI/UX freeze or production release readiness.
