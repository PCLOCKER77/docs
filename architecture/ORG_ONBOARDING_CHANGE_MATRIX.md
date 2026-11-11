# Change Matrix — Organization Onboarding / PA Boundary (DR-021)

Internal reconciliation for requirements-freeze delivery. Not a product API contract.

| Area | Existing behavior | Required behavior | Affected module | Action |
| --- | --- | --- | --- | --- |
| Org create status | Service sets `PENDING` | `PENDING` | `organization/service.py` | Keep |
| OA on create | Optional; PA-supplied password + `account_created` email | Provision OA; **no PA password**; env policy: local temp password / QA+Prod setup link | schemas + service + CredentialProvisioningPolicy | Change |
| Same-as-org-email | Absent | UI-only checkbox | Flutter form | Add |
| OA credential email | Temp password always | Local: temp via Mailpit; QA/Prod: setup link only | email templates + outbox | Change |
| Setup credentials UI | Password-reset confirm only | `/auth/setup-credentials` (token query) | Flutter auth | Add |
| Activation | PA-only `activate` always | Auto-ACTIVE if OA accepts T&C with no initial changes; else PA approve | service + extras | Change |
| T&C | Absent | Auditable accept record | onboarding extra + audit + metadata | Add |
| Initial-change review | Absent | Flag pending PA review; reject/resubmit | service + extras | Add |
| PENDING gate | Per-module ACTIVE checks (facility/identity/customer/membership) | One central lifecycle rule | `core/organization_lifecycle.py` | Add + wire |
| PA tenant update | Policy classifies UPDATE as TENANT_ADMIN; org service not enforced | Enforce tenant_mutation on org update for PA | organization + tenant_mutation | Wire |
| PA plaintext tenant data | Customer module exists; no crypto gate | Deny PA DEK / decrypt path | tenant_crypto foundation | Add foundation |
| Classification | Docs only | Reusable NORMAL/SENSITIVE/HIGHLY_SENSITIVE | `core/data_classification.py` | Add |
| Docs lifecycle | FR-ORG-007 PA always activates; BA-04 Draft | New OA/T&C conditional path | FR-03, BA-*, PF-01, API-02 | Update |
| API catalog | 228 + ORG-ARCHIVE/RESTORE extras | Still 228; add onboarding extras only | catalog.py | Extend extras |
| Archive/restore | Soft-delete; PA-only | Unchanged | organization | Preserve |
| AuthN/AuthZ | Frozen | Unchanged | auth modules | Do not touch |
| Flutter create | No OA section | OA section + same-as-email | organization form | Add |
| Flutter OA onboarding | Password-change only | Review + T&C + status | org + auth routing | Add |
| Flutter PA review | Activate button only | Pending review visibility + approve/reject | list/details/actions | Extend |

## Contradictions resolved

1. **Draft vs Pending** → Pending is authoritative (`business_status=PENDING`).
2. **PA always activates** → Replaced by DR-021 conditional activation.
3. **DB default ACTIVE** → App always writes PENDING on create; do not add unnecessary migration solely to change default in this slice (document only).
4. **Operator password on OA create** → Removed; environment policy selects temporary password (local) or setup link (QA/production).
