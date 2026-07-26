# Auth API Proposal (API-03) — Draft for Owner Confirmation

Status: Proposed (Product Design drafted) — please confirm with API owner/security owner.

Purpose
- Provide a concrete payload and error-code → UI mapping so frontend and QA can implement `UI-AUTH-001` without blocking.

1) Success response (sample)

POST /auth/login

Response 200

```json
{
  "access_token": "eyJ...",
  "token_type": "Bearer",
  "expires_in": 3600,
  "refresh_token": "def...",
  "user": {
    "id": "user_123",
    "display_name": "Jane Doe",
    "email": "jane@example.com",
    "roles": ["site_staff"],
    "tenants": [{"org_id":"org_1","facilities":["fac_1"]}]
  }
}
```

2) Common error codes and UI mapping (proposed)

| HTTP | Code / Field | UI outcome |
|---:|---|---|
| 401 | invalid_credentials | Banner: "Invalid username or password." Suggest password recovery link.
| 423 | account_locked | Banner: "Account locked. Contact support." Show support contact and correlation id.
| 403 | mfa_required | Show MFA step UI (OTP / push). Provide `mfa_token` from API to drive next call.
| 429 | rate_limited | Banner: "Too many attempts — please try again in X seconds." Use `Retry-After` header if present.
| 400 | validation_error | Highlight field-level messages using `errors[]` payload per-field.
| 5xx | server_error | Friendly banner: "Service temporarily unavailable. Try again later." Provide correlation id.

3) Headers and rate-limit semantics (proposed)

- `Retry-After`: seconds to wait when 429 returned.
- `X-RateLimit-Limit`: configured window max.
- `X-RateLimit-Remaining`: remaining in window.
- `X-Correlation-ID` (or `X-Request-ID`): include in UI support copy/paste.

4) MFA / SSO guidance (decision pending)

- Proposal: treat MFA as optional per-tenant. If `mfa_required`, API returns HTTP 403 with `mfa_required:true` and `mfa_token`. Frontend displays MFA step and calls `POST /auth/mfa/verify`.
- SSO: support redirect-based SSO for web; mobile receives ID token via deep link. Include return URL in `POST /auth/sso-init` if supported.

5) Idempotency and retries

- Login requests are not idempotent but safe to retry for network errors. Use exponential backoff on 429.

6) Request for API owner

- Please confirm or provide OpenAPI fragment for `POST /auth/login`, sample responses for 200/401/423/403/429/5xx, and the exact header names for rate-limiting and correlation.

---

Documented-by: Product Design
