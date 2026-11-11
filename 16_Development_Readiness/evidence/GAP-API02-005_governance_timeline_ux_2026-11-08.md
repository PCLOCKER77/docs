# GAP-API02-005 — Governance timeline UX depth

**Date:** 2026-11-08  
**API:** Extra `GET /api/v1/organizations/{organization_id}/governance-timeline` (PA governance)

## Implemented

- Split summary (`organizationGovernanceSummaryProvider`) from paginated timeline section.
- `OrganizationGovernanceTimelineSection`: loading, error/retry, **Load more events** (`page` / `page_size`).
- Lifecycle actions bump `governanceTimelineRefreshProvider` to remount timeline after suspend/activate.

## Tests

`flutter test test/features/organization/organization_governance_panel_test.dart` → **2 passed**

## Status

**Implemented (Flutter TESTED)** — backend contract unchanged; no new permissions.
