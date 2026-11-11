# Campaign hybrid WhatsApp delivery architecture

Product direction (frozen): Digitize supports **manual/external**, **Digitize-managed WhatsApp**, and **organization-owned WhatsApp** delivery. Campaign definition stays independent of provider implementation.

## Stage 1 (implemented — Flutter)

- **API-10-001…012** wired via `RemoteCampaignRepository`.
- **No list/get campaign** in the 228 inventory → device-local campaign index (`CampaignLocalIndex`) plus **open by UUID** and report/performance refresh.
- **Manual/external**: Share on WhatsApp (`wa.me/?text=`), copy message, copy report JSON export (no customer PII in export).
- **Launch disabled** for manual delivery mode (API-10-007 would enqueue real notification work).

## Stage 2 — Digitize-managed WhatsApp (not implemented)

Dependencies before enabling automated launch in UI:

| Area | Dependency |
|------|------------|
| Account ownership | Approved contract for Digitize WABA credentials, rotation, and org billing boundary |
| Provider abstraction | Extend backend delivery routing beyond env-scoped `WHATSAPP_PROVIDER`; org-scoped execution history |
| Templates | Approved template catalog + campaign `template_id` UX (API-10-013) |
| Consent | Enforce WhatsApp marketing consent on campaign launch (today: customer consent records exist; campaign launch does not filter) |
| Callbacks | Webhook registration + delivery status correlation to `CampaignExecution` / metrics |
| Flutter | Enable `CampaignDeliveryMethod.digitizeManagedWhatsApp` launch path after backend readiness |

Do **not** simulate delivery success in QA without provider verification.

## Stage 3 — Organization-owned WhatsApp (not implemented)

Dependencies:

| Area | Dependency |
|------|------------|
| Onboarding | OAuth / token storage / webhook registration contracts (not in 228 inventory) |
| Isolation | Per-organization credential vault; never expose secrets to Flutter or generic API responses |
| Identity | Organization-specific sending phone / WABA ID |
| Templates | Org-scoped template availability |
| Execution | Independent tracking from Digitize-managed sends |

Record in GAP register until contracts exist.

## Consent

- **Data**: `customer.customer_consent` (+ API-10 preference work in Phase 10 docs).
- **Gap**: Campaign audience API validates org membership only, not marketing consent.
- **UI**: Warnings and eligibility counts from customer consent payloads when audience is selected manually.

## Commercial

WhatsApp / campaign message charges remain **out of scope** for standard SaaS subscription unless an approved commercial policy links them.
