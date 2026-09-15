# Digitize Mobile Store & Platform Compliance Audit

**Audit date:** 13 September 2026  
**Status:** Architecture gate — **not** a store submission package  
**Code changes in this task:** none (documentation only)  
**Architecture freeze:** `ACCESS_MOBILE_COMMERCE_ARCHITECTURE_FREEZE.md` / DR-019 v2.0 — **FROZEN**. Store submission remains **NOT READY**.

---

## 1. Executive Summary

Digitize is a multi-tenant SaaS platform for activity and recreation businesses (organization → facility → site). The Flutter client and FastAPI backend already implement staff login, tenant administration (API-01–API-04), and Digitize SaaS subscription/license (API-09). **The product is not store-submittable today.** That is expected at this stage.

The highest-risk gaps are **not** missing camera permissions or analytics SDKs. They are:

1. **Account deletion** is not available in the app or on a public web resource, while the product already creates persistent user and customer records.
2. **No Privacy Policy, Terms, support URL, or in-app legal surfaces** exist in the repository.
3. **Who the Phase-1 operational app is for is frozen:** Organization Admin, Site Admin, and Staff. Platform Admin uses a **separate** application. Customer mobile is **Phase 2**. That freeze drives Sign in with Apple (not required for first-party staff login), IAP vs physical-service payments, kids/family policy, and deletion personas. Remaining store work is **implementation**, not architecture ambiguity.
4. **SaaS billing (Organization → Digitize/OreeOn)** and **facility commerce (Customer → Facility)** are **frozen** as separate commercial boundaries (API-09 vs API-05/API-08). Google Play lists **gym memberships** as physical services that **must not** use Play Billing. Apple 3.1.3(e) requires **non-IAP** methods for services consumed outside the app. Digitize SaaS must not be purchased in the operational mobile app. Staff may collect **facility** payments where already defined; that is not SaaS checkout.
5. **Minors:** Guardian Relationship is **future-ready**; detailed UX is **deferred**. `date_of_birth` is stored. Kids activity centers remain an intended vertical. Do not treat the Phase-1 operational app as a children’s consumer product.

**Architecture decisions (personas, roles, commerce split, Customer ≠ Participant, Platform Admin access): FROZEN.**  
**Store submission readiness: NOT READY** (privacy policy, in-app+web deletion, production IDs/signing, reviewer demo, Data Safety / App Privacy).  
**Recommended next gate:** API-05 Membership Plan **contract review** (do not implement in the access freeze). Must respect facility-commerce-only, no Manager role, no customer-mobile assumption.

---

## 2. Audit Scope

In scope: Apple App Store Review, Apple account deletion and App Privacy, Google Play User Data / Data Safety / account deletion / Payments / target API, plus repository evidence in `digitize-services/`, `digitize-ui/`, `database/`, `docs/`.

Out of scope (per gate): implementing APIs, Membership Plan, payments, Sign in with Apple, store SDKs, schema changes, auth redesign.

Sources were official Apple and Google pages accessed **13 September 2026**. URLs are in §28.

---

## 3. Repository Baseline

### Product

- Hierarchy: Platform → Organization → Facility → Site. Unchanged.
- Intended verticals include gyms, swim schools, kids activity centers, sports academies, etc. (`docs` product narrative; customer DOB already in schema).

### APIs

- Numbered inventory: **228** operations, collections **API-01 … API-14**.
- Live verticals: API-01, API-02, API-03, API-04, API-09 (partial). Authentication is a frozen extra collection (`AUTH_CONTRACT_FREEZE.md`).
- Runtime identity: `operation_id` (semantic). `catalog_id` (`API-02-015`) is product metadata only. **Not reopened in this audit.**
- API-05 Membership Plan is **not started** (Flutter `unavailable_membership_plan_repository.dart`; membership HTTP paths return 404).

### Authentication (implemented)

| Capability | Evidence | Store relevance |
| --- | --- | --- |
| Password login | `POST /api/v1/auth/login` | Account-based app |
| Refresh cookie + JWT | `POST /api/v1/auth/refresh` | Session |
| Logout | `POST /api/v1/auth/logout` | Required hygiene; not deletion |
| Password recovery | `POST /api/v1/auth/password-reset` (+ confirm) | Account recovery |
| MFA / SSO / social | Explicitly **out of scope** in freeze | Sign in with Apple **not triggered today** |
| Self-service registration | **Not present** | Creation is admin/staff-driven |
| Staff create | API-03 `identity_staff_accounts_create` | Account creation in product |
| Customer register | API-04 `customers_create` (staff registers customer) | Personal data; not necessarily an app login |

Flutter routes: `/login`, password-reset, dashboard/org/facility. No register, no delete-account, no privacy link (`digitize-ui/lib/features/authentication/routes/auth_routes.dart`).

### Mobile project

| Item | Value | Evidence |
| --- | --- | --- |
| Flutter package | `digitize_flutter` 1.0.0+1 | `digitize-ui/pubspec.yaml` |
| Android applicationId | `com.example.digitize_flutter` | `android/app/build.gradle.kts` |
| iOS bundle id | `com.example.digitizeFlutter` | `ios/Runner.xcodeproj/project.pbxproj` |
| Display name | Digitize Flutter / digitize_flutter | Info.plist / AndroidManifest |
| min/target/compile SDK | Inherited from Flutter Gradle plugin (not pinned) | `minSdk = flutter.minSdkVersion` |
| Release signing | **Debug keystore** | `signingConfig = signingConfigs.getByName("debug")` |
| Android permissions | `INTERNET` only | `AndroidManifest.xml` |
| iOS privacy strings | **None** (no camera/location/tracking keys) | `Info.plist` |
| Entitlements / Associated Domains / Push / SIWA | **None found** | no `.entitlements`, no `PrivacyInfo.xcprivacy` |
| Deep links | Launcher intent only | Manifest |
| Analytics / crash / ads / FCM / maps / IAP SDKs | **Not in pubspec** | `pubspec.yaml` |
| Token storage | `flutter_secure_storage` | pubspec |
| Production data mode | `kReleaseMode` → remote APIs | `lib/main.dart` |

### Personal data already in the domain

Customer (`customer.customer`): name, optional DOB, gender_code, email, phone, JSON profile_payload, facility/site FKs, `deleted_at`. Emergency contacts. Document **metadata** (`storage_reference`). Consent rows (`customer_consent`). History.

Identity (`identity.user_account`): login_identifier, display_name, password_hash, account_status, user_type, MFA flag (unused), sessions (auth module), `deleted_at`.

Commercial: subscription/license (API-09 live). Invoice/payment **models exist** (`billing` module); facility payment APIs are catalogued (API-08) **not live**.

Notifications: API-10 catalogued, **not implemented**. No APNs/FCM.

---

## 4. Apple App Store Assessment

**Guideline 2.1 — App Completeness:** Login-gated staff app will need a **demo account** and reachable functionality. No `APP_REVIEW_ENVIRONMENT` exists.

**Guideline 5.1.1(i) — Privacy Policy:** Required in App Store Connect **and inside the app**. Repository has **no** privacy policy URL or in-app link.

**Guideline 5.1.1(v) — Account deletion:** If the app supports account creation, deletion must be **initiated in the app**, remove the account and associated personal data (except legal retention), not mere deactivation. Support-only (email/phone) is insufficient except highly regulated industries (5.1.1(ix)). Digitize has **logout and staff deactivate / customer archive**, not in-app account deletion.

**Guideline 4.8 — Login Services:** Applies only if a **third-party/social login** is used for the **primary** account. Current contract is **first-party password only**. Sign in with Apple is **NOT APPLICABLE today**. Adding Google Sign-In later **would** trigger 4.8.

**Guideline 3.1.1 vs 3.1.3(e):** Digital goods/features consumed in-app → IAP. Physical goods/services consumed **outside** the app → **must not** use IAP (Apple Pay or cards instead). Facility memberships, class fees, walk-in admissions, and PT sessions consumed at a site are **outside-the-app services**. Digitize **SaaS licenses** that unlock **software** in the app are digital and, if sold **in** the iOS app, typically **IAP**.

**Kids (1.3 / Kids Category / 5.4):** No Kids Category, no COPPA flow. DOB is stored. Guardian Relationship is future-ready; detailed UX is **deferred**. **Implementation remaining** before kids-center go-live; architecture does not treat Customer as the child Participant by default.

**Permissions:** No sensitive iOS usage strings. Do not add location merely because facilities have addresses.

**Reviewer notes:** No screenshot set, age rating questionnaire, or demo org documented for stores.

---

## 5. Google Play Assessment

**User Data policy:** Privacy policy in-app and in Play Console. Account creation in-app requires **in-app deletion** **and** an **external web URL** in Play Console. Freezing/deactivating is not deletion. Retention must be disclosed.

**Current Digitize:** Staff accounts are created via API-03 (not a consumer “Sign up” screen). Play still treats apps that **allow account creation** (including in-product creation) as in scope once users have app accounts. A **staff-only** app that never creates accounts on-device may argue “no in-app account creation,” but reviewers often still expect deletion for logged-in app accounts. **Treat in-app + web deletion as required before Play submission** unless legal confirms the staff-only exception and Play Console Data Safety answers match.

**Data Safety form:** Not started. Must declare collected data, sharing, deletion mechanism, security practices.

**Payments:** Play Billing **required** for digital in-app purchases (including **cloud software/services** and many **subscription** examples). Play Billing **must not** be used when payment is primarily for **physical services** — policy examples include **gym memberships**, transportation, live-event tickets. Facility recreation memberships and admissions should use **non-Play** processors (cards, UPI, etc.). SaaS billed **inside** the Android app as “unlock Digitize software” is the dangerous mix.

**Target API:** New apps/updates must target **API 36** from **31 August 2026** (mobile). Current Gradle defers to Flutter. Re-check `flutter.targetSdkVersion` at first Play upload.

**Families / Designed for Families / COPPA:** Not declared. Risk if the app is used by children or markets to kids.

**Permissions:** INTERNET only. No unused CAMERA/LOCATION declared — **PASS** for current binary.

---

## 6. Cross-Platform Requirements

| Topic | Apple | Google | Digitize |
| --- | --- | --- | --- |
| Privacy policy | In-app + metadata | In-app + Console | **GAP** |
| Account deletion | In-app initiate | In-app **and** web URL | **GAP** |
| Deactivation ≠ deletion | Yes | Yes | Archive/deactivate exist; deletion productized **GAP** |
| Demo account | 2.1 | App access | **GAP** |
| Third-party login | 4.8 SIWA equivalent | No SIWA analogue | N/A until social login |
| Physical recreation fees | 3.1.3(e) non-IAP | Gym memberships excluded from Play Billing | Align API-05/08 **before** implementation |
| SaaS software fees in-app | Likely IAP | Likely Play Billing | Keep on **web billing portal** unless IAP is chosen |
| Tracking / ATT | If tracking | Ads ID / Data Safety | No ads SDK — N/A |
| Encryption / TLS | ATS default | User Data | Backend HTTPS assumed; no ATS exceptions in Info.plist |

---

## 7. Authentication & Account Lifecycle

### A. Can a user create an account?

- **End user in Flutter:** No self-registration UI.
- **Staff:** Yes, via API-03 (admin). Operator CLI `set-staff-password`.
- **Customer record:** Yes, staff `customers_create`. This is a **facility customer profile**, not proven to be an `identity.user_account` login. Customer-as-app-user is **DECISION REQUIRED**.

### B–D. Delete / request delete / in-app?

**No.** No delete-account API, Flutter screen, or public web form. Staff **deactivate** (`identity_users_deactivate`) and customer **archive** (`customers_archive` sets `deleted_at`) are **operator** lifecycle, not store self-service deletion.

### E. Does deletion remove associated personal data?

Not specified. Soft-delete columns exist (`deleted_at` on user_account and customer). Financial/audit tables are designed to **retain** (`API-00`: DELETE shall not physically remove data subject to audit/financial/legal retention).

### F. Legitimate retention?

**DECISION REQUIRED.** Docs require retention conceptually (`docs/06_Database_Design`, API-00) but **no approved retention periods** (`TEST-03` freeze note: Legal must provide durations).

### G. Personas

| Persona | App login today | Deletion today | Store implication |
| --- | --- | --- | --- |
| Platform Admin | Yes (staff auth) | Operator only | In-app delete or documented exception |
| Organization Admin / Facility staff / Receptionist / Trainer | Staff identity | Deactivate ≠ delete | Same |
| Customer | Profile in DB; **no customer auth vertical** | Archive by staff | If they later log in, full deletion UX |
| Parent/Guardian | Not a first-class account | N/A | Future |
| Participant / minor | May be the **customer row** (DOB) | Archive | Must not require a child Apple/Google account |

### H. Business records

Invoices, attendance, subscriptions, licenses, and audit events should **survive** as organizational records with **anonymized** personal fields where law allows. Hard-delete of the whole tenant graph is **incorrect** for commerce and tax.

**Logout exists. Password reset exists. Account linking / social / MFA do not.**

---

## 8. Privacy & Personal Data

Only fields **present or clearly planned** in repo/docs.

| Category | Collected? | Stored? | Why (inferred from schema/API) | Access | Third party | Retention | Deletion | Consent |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Name | Yes (staff display_name; customer first/last) | Yes | Identity / facility ops | Tenant-scoped APIs | None in app SDKs | DECISION REQUIRED | Soft-delete columns; no DSAR API | Not user-consented in app |
| Email / login_identifier | Yes | Yes | Auth + customer contact | Staff + system | Password reset may email (implementation TBD) | DECISION REQUIRED | GAP | GAP |
| Phone | Customer primary_phone; emergency phone | Yes | Contact | Staff | None seen | DECISION REQUIRED | GAP | GAP |
| Address | Org/facility/site business address; emergency `address_payload` | Yes | Operations — **not** device location | Staff | None | Org lifetime | N/A for facility address | N/A |
| Date of birth | Customer optional | Yes | Age / programs | Staff | None | DECISION REQUIRED | GAP | GAP |
| Gender | `gender_code` optional | Yes | Profile | Staff | None | DECISION REQUIRED | GAP | GAP |
| Profile photo | Not a dedicated column; `profile_payload` JSON | Possible | Unspecified | — | No image_picker | — | — | Do not add camera until needed |
| Emergency contact | Yes | `customer_contact` | Safety | Staff | None | Often retain with attendance | GAP | GAP |
| Guardian | **Deferred** | Contacts only | Docs | — | — | — | — | **DECISION** |
| Membership | Planned API-05 | Tables planned | Facility commerce | — | — | Financial | — | — |
| Attendance | Planned API-06 | Planned | Operations | — | — | Often legal/safety | — | — |
| Training | Planned API-07 | Planned | Operations | — | — | DECISION REQUIRED | — | — |
| Payment / invoice | Models + API-08 catalog | Planned | Facility commerce | — | Future PSP | **Legal retain** | Anonymize payer, keep amounts | — |
| SaaS subscription/license | API-09 live | Yes | Digitize billing | Platform/org | None in Flutter | Commercial | Org-level | Contract |
| Device / IP | Possible in access logs | Logging middleware | Security | Operators | None | DECISION REQUIRED | Log retention GAP | Legitimate interest? |
| Auth / sessions | Yes | JWT + refresh cookie + DB sessions | Auth | User + server | None | Session lifetime | Logout revokes | N/A |
| Push token | No | No | — | — | — | — | — | — |
| Device GPS | **No** | No | — | — | — | — | — | Do not request |
| Camera/photos | **No** | Document metadata only | KYC/docs planned | Staff | Object storage planned | DECISION REQUIRED | GAP | GAP |
| Support tickets | API-12 catalog | Not live | Support | — | — | DECISION REQUIRED | — | — |
| Notifications | API-10 catalog | Not live | Comms | — | Future ESP/SMS/FCM | — | Prefs planned API-10-024 | **Separate marketing vs transactional** |
| Analytics / crash | **No SDK** | None in client | — | — | — | — | — | Keep empty until chosen |
| Advertising | **None** | None | — | — | — | — | — | FUTURE |

`customer_consent` exists (`consent_type`, `consent_status`, `channel_type`) but **no frozen catalog of consent types** wired to store disclosures.

---

## 9. Account Deletion & Data Retention

### Store rules (both platforms)

- In-app path, easy to find.
- Not “deactivate only.”
- Disclose legal retention.
- Google additionally requires a **web** deletion URL.

### Recommended design (do not implement in this task)

**Customer (if they ever have an app account or even if deletion is of the customer profile they control):**

1. Re-authenticate.
2. Confirm consequences (memberships, outstanding invoices, class bookings).
3. Cancel or transfer **facility** commercial relationships per policy (cannot silently void tax invoices).
4. Set account/customer to a terminal **DELETED** / anonymized state.
5. Anonymize PII: names → `Deleted User {uuid}`, clear email/phone/DOB/photo/documents bytes, unlink push tokens.
6. Retain invoices, attendance facts, and audit rows with **tokenized** subject id for fraud/tax.
7. Staff-operated `customers_archive` is **not** a substitute for self-service if the customer is an app user.

**Organization staff user:**

1. Block deletion if they are the **last Organization Admin** (transfer ownership first).
2. Revoke sessions, disable login, anonymize staff profile.
3. Keep audit/attribution as “former staff {hash}.”
4. Do not delete the organization.

**Organization Admin:**

Same, plus mandatory **successor admin**. If they also own the legal entity, this may be a **contract cancellation** (API-09) rather than a store “delete my game account” flow.

**Platform Admin:** Operator-only; not a consumer store persona.

### Retention matrix (periods = DECISION REQUIRED unless noted)

| Data | Business | Legal/financial | On user deletion |
| --- | --- | --- | --- |
| Auth credentials | Until account end | Security logs | Hash destroy; sessions revoke |
| User / staff profile | Employment/ops | Labor/tax possible | Anonymize |
| Customer profile | Facility CRM | Possible | Anonymize or staff-retain if org still needs the **participant record** under a different lawful basis — **DECIDE** |
| Membership / attendance | Ops | Often retain | Keep events, strip PII |
| Invoices / payments / refunds | Accounting | **Typically retain** | Keep; mask payer |
| Audit logs | Security | Often retain | Immutable; minimize PII going forward |
| Support | Ops | DECISION REQUIRED | Anonymize thread |
| Notifications / tokens | Ops | Short | Delete tokens |
| Analytics / crash | N/A today | — | If added, vendor DPA + deletion |
| Uploaded files | KYC/ops | DECISION REQUIRED | Delete object storage |
| Organization records | SaaS tenant | Contract | **Not** deleted because one staff left |

---

## 10. Payments & Commerce

### Domain A — Digitize SaaS (API-09)

Organization pays OrieOn/Digitize for **software license**. Live APIs manage subscription/license **lifecycle**, not a card checkout in Flutter. **No** StoreKit / Play Billing SDK.

**Recommendation (frozen for Phase-1 operational app):** keep SaaS checkout on a **web billing portal** (and/or sales-assisted) so the mobile app **manages** entitlement (license validate-login already exists) without selling digital goods in-app. Confirm with counsel; US storefront steering rules (3.1.1(a)) are evolving.

### Domain B — Facility/customer commerce (API-05, API-08, walk-in, PT)

Customer pays the **facility** for membership, admission, classes, camps, PT — **physical recreation services consumed at a site**.

**Apple 3.1.3(e):** use **non-IAP** (cards, Apple Pay as payment method, etc.).  
**Google Payments §3:** **do not** use Play Billing for gym memberships / physical services.

**Do not** implement Stripe/Razorpay/IAP in this gate. When API-05/08 start, encode **processor = facility PSP**, never Play Billing, unless a SKU is truly digital-only (e.g. in-app video course with no on-site service) — that hybrid SKU is **DECISION REQUIRED**.

Current Flutter: no payment UI. Backend billing models exist; routes not live.

---

## 11. Subscriptions

| | Digitize SaaS | Customer facility membership |
| --- | --- | --- |
| Collection | API-09 | API-05 (not started) |
| Payer | Organization | Customer |
| Payee | Digitize | Facility |
| Store billing | Digital software risk | Physical service — **not** store billing |
| Catalog warning | Explicit in numbered notes | “Do not use commercial.subscription_plan” |

**PASS (architecture intent).** **P0 risk if API-05 reuses commercial.subscription or StoreKit.** Keep the freeze.

---

## 12. Children / Minors

**Evidence:** `date_of_birth` on customer; age validation in `CustomerService._validate_date_of_birth`; emergency contacts; **no** Customer-to-Customer guardian FK (deferred in API-04 preimplementation). Consent table unstructured.

**Product intent** includes kids centers and academies.

**Required decisions (architecture frozen; implementation deferred):** Can a child be a **participant only** (parent/guardian holds the commercial Customer record)? Minimum age for an independent login? Parental consent capture? Photos of minors? Marketing to children (should be **off**)? Designed for Families / Kids Category (usually **no** for a staff ops app).

**Do not** put the child on Sign in with Apple as the primary account.

---

## 13. Permissions

| Permission | Declared? | Used in Dart? | Needed now? | If denied |
| --- | --- | --- | --- | --- |
| Internet | Android yes | Yes (Dio/http) | Required | App cannot call API |
| Camera / Photos / Mic | No | No | No | — |
| Location (any) | No | No | **Do not add** for addresses | — |
| Bluetooth / Contacts / Calendar / Health | No | No | No | — |
| Notifications | No | No | Only when push ships | Optional recommended |
| Tracking (ATT) | No | No | No ads | — |
| Biometrics | No | No | Optional later | Fallback password |

**PASS** for unused-permission risk. QR attendance later: prefer **optional** camera with a purpose string, feature works via manual code entry.

---

## 14. Notifications

API-10 planned (system/manual/schedule/deliver, preferences). **Not implemented.** No FCM/APNs.

When built: transactional (booking, payment, staff alerts) vs marketing (campaigns API-10). Marketing needs **consent** and easy opt-out (store + spam law). Preferences endpoint already catalogued (`notification_preferences_update`).

---

## 15. Analytics & Third-Party SDKs

| SDK | Purpose | Data | Required? | Privacy |
| --- | --- | --- | --- | --- |
| Flutter SDK | UI | None beyond OS | Yes | Disclose nothing extra |
| flutter_riverpod, go_router, dio, http, intl, flex_color_scheme, font_awesome, flutter_svg, flutter_animate, cupertino_icons | App logic/UI | No telemetry in packages as used | Yes | Low |
| flutter_secure_storage | Tokens | Credentials on device | Yes | Local; not tracking |
| CocoaPods Flutter pods | Native embed | Standard | Yes | Review Privacy Manifests at submit time |
| Firebase / Crashlytics / GA / Facebook / AppsFlyer / OneSignal / Stripe / RevenueCat / maps | — | — | **Not present** | Do not add casually |

**PASS** for current binary. **FUTURE:** any crash/analytics SDK requires Apple Nutrition Labels, Google Data Safety, and possibly Privacy Manifests.

CocoaPods stats disabled in `Podfile` (`COCOAPODS_DISABLE_STATS`).

---

## 16. Android Configuration

- `namespace` / `applicationId`: `com.example.digitize_flutter` — **must change** before Play (example IDs are not a production brand).
- SDKs: Flutter-managed; **verify target 35/36** at upload time (Google policy 31 Aug 2026 → API 36 for new submissions).
- Release uses **debug signing** — **cannot** ship.
- `usesCleartextTraffic` not enabled in main manifest (good default).
- Main activity `exported=true` with LAUNCHER (normal).
- No backup rules customized (`allowBackup` default true) — review before storing more PII on device.
- No App Links.
- Debug/profile manifests: INTERNET for tooling.

---

## 17. iOS Configuration

- Bundle ID `com.example.digitizeFlutter` — change before App Store Connect.
- Deployment target **13.0** in pbxproj; Podfile platform line commented.
- No usage descriptions, no ATS exceptions, no associated domains, no push capability, no Sign in with Apple capability.
- Display name “Digitize Flutter” — productize before screenshots.

---

## 18. App Review / Reviewer Access

Login is required for meaningful UI. Production mode talks to a real API (`kReleaseMode`).

**Future `APP_REVIEW_ENVIRONMENT` (design only):**

- Seeded **demo organization**, facility, site, staff login, sample customers.
- License valid (`licenses_validate_login` path).
- No production tenant PII.
- Credentials in App Review notes / Play Console App access.
- If payments exist, sandbox PSP — **not** production charges.
- Mock data source must **never** ship in store builds (already separated).

Without this: **Guideline 2.1 / Play app access** rejection risk.

---

## 19. Store Metadata

Needed later, all **missing** as product decisions:

App name, short/full description, keywords, screenshots (phone/tablet), age rating, content rights, privacy URL, terms URL, support URL, **account deletion URL** (Play), Data Safety / App Privacy answers, reviewer notes.

Age rating: a staff ops app with customer DOB is not automatically 4+; kids-center marketing can force higher scrutiny.

---

## 20. Terms / Privacy / Legal Surfaces

Repository search found **no** Privacy Policy, Terms of Service, Cookie Policy, Refund Policy, DPA, or in-app legal links.

**Eventually required:** Privacy Policy (both stores + in-app), Terms, support contact, deletion instructions (Play web page), refund policy if selling, processor DPA if PSPs/email/SMS added. **Do not draft legal text in engineering.**

---

## 21. API & Database Architecture Impact

| Capability | Current | Before MVP | Before mobile store | Before production |
| --- | --- | --- | --- | --- |
| Account deletion API | None | Design | **Required** if app has accounts | Required |
| Web deletion page | None | — | **Google required** | Required |
| Data export (DSAR) | `reporting.data_exports` model unused for users | Future | Strongly advised | Production/GDPR |
| Anonymization job | Soft delete only | Design with API-04/05 | Required with deletion | Required |
| Consent types | Table, no product enum | Before marketing/push | Data Safety | Production |
| Notification prefs | Catalog API-10-024 | With notifications | With notifications | — |
| Guardian | Deferred | **Before kids vertical** | If child data in app | Kids vertical |
| Retention schedule | DECISION REQUIRED | Legal | Store disclosure | Production |
| Payment records | Models; APIs not live | API-08 design | If in-app pay | Accounting |
| Account status | ACTIVE/deactivate/archive | Map DELETED vs ARCHIVED | Store deletion | Production |

**Do not** start API-05 until deletion vs archive vs anonymize vs “participant remains for the facility” is decided.

---

## 22. Findings

### FINDING: No in-app account deletion

Status: **GAP**  
Priority: **P0** (store submission); **P1** (architecture before API-05)  
Platform: Both  
Requirement: Apple 5.1.1(v) and Google User Data account deletion.  
Current Digitize State: Login, logout, password reset, staff deactivate, customer archive. No self-service delete.  
Repository Evidence: `AUTH_CONTRACT_FREEZE.md`; no delete routes in `authentication/routes.py`; Flutter `auth_routes.dart`.  
Risk: App Review / Play rejection; GDPR/CCPA complaints.  
Required Change: Deletion API + Flutter settings entry + anonymization pipeline; Google web URL.  
Affected Domain: Identity, customer, membership, billing, audit.  
When Required: Before first store binary that issues accounts.  
Source: https://developer.apple.com/support/offering-account-deletion-in-your-app/ · https://support.google.com/googleplay/android-developer/answer/10144311

### FINDING: No Privacy Policy or in-app legal link

Status: **GAP**  
Priority: **P0** before submission  
Platform: Both  
Requirement: Apple 5.1.1(i); Google User Data.  
Current Digitize State: No policy documents or URLs in repo.  
Repository Evidence: repo-wide search for “privacy policy” / “terms of service” — no product hits.  
Risk: Automatic metadata rejection.  
Required Change: Legal-authored policy; in-app link; store metadata.  
Affected Domain: Flutter settings, store listing.  
When Required: Before store listing.  
Source: https://developer.apple.com/app-store/review/guidelines/ · https://support.google.com/googleplay/android-developer/answer/10144311

### FINDING: No Google Play web deletion resource

Status: **GAP**  
Priority: **P0** before Play  
Platform: Google  
Requirement: In-app **and** web deletion URL in Play Console.  
Current Digitize State: No public website deletion flow in repo.  
Repository Evidence: No support/marketing site in this repository.  
Risk: Play Data Safety / User Data rejection.  
Required Change: Hosted deletion request page.  
Affected Domain: Web + identity.  
When Required: Play submission.  
Source: https://support.google.com/googleplay/android-developer/answer/13327111

### FINDING: Staff deactivate / customer archive ≠ store deletion

Status: **PARTIAL**  
Priority: **P1**  
Platform: Both  
Requirement: Deactivation is insufficient.  
Current Digitize State: `identity_users_deactivate`, `customers_archive` (`deleted_at`).  
Repository Evidence: `customer/service.py` archive; API-03 deactivate.  
Risk: Shipping “delete” that only freezes login.  
Required Change: Distinct DELETED/anonymized state and UX copy.  
Affected Domain: Identity, customer.  
When Required: With deletion design.  
Source: Apple account-deletion Q&A; Google User Data (freezing insufficient).

### FINDING: App persona (frozen)

Status: **FROZEN** (architecture) / remaining store UX still GAP  
Priority: **P1** for store binary; not an open product-architecture question  
Platform: Both  
Requirement: Drives 4.8, kids, payments, deletion personas, 2.1 demo.  
Current Digitize State: Phase-1 operational application = Organization Admin, Site Admin, Staff. Platform Admin = separate app. Customer mobile = Phase 2. Flutter today is org/facility operations; customer APIs are staff-facing.  
Repository Evidence: `ACCESS_MOBILE_COMMERCE_ARCHITECTURE_FREEZE.md`; `app_shell.dart`; no customer login feature.  
Risk: Building API-05 as if customers were mobile users without deletion/guardian.  
Required Change: **None for persona architecture.** API-05 contract review must not assume customer mobile.  
Affected Domain: All mobile.  
When Required: Architecture done; customer-app auth remains Phase 2.  
Source: DR-019 v2.0; Apple 5.1.1(v), 4.8; Google User Data.

### FINDING: SaaS vs facility commerce billing channels

Status: **FROZEN** (architecture) / **PARTIAL** (no checkout implemented)  
Priority: **P1** for API-05 implementation  
Platform: Both  
Requirement: IAP/Play Billing for in-app digital; non-store billing for physical recreation.  
Current Digitize State: Organization → Digitize/OreeOn (API-09). Customer → Facility (API-05/08). No checkout in app. No staff-mobile SaaS purchasing.  
Repository Evidence: Freeze §4; `catalog.py` API-09 vs API-05 notes; Google gym membership exclusion.  
Risk: Wrong SDK on Membership Plan.  
Required Change: API-05/08 design: facility PSP only; SaaS off operational mobile.  
Affected Domain: Billing, membership, Flutter.  
When Required: Before API-05/08 implementation.  
Source: https://developer.apple.com/app-store/review/guidelines/ §3.1.3(e) · https://support.google.com/googleplay/android-developer/answer/9858738

### FINDING: Minors / guardian model deferred while DOB is live

Status: **GAP** relative to kids vertical; **PARTIAL** for generic adults  
Priority: **P1** before kids centers  
Platform: Both (COPPA/Kids/Families if applicable)  
Requirement: Parental consent, no unnecessary child accounts.  
Current Digitize State: DOB stored; guardian FK deferred.  
Repository Evidence: `customer.py` `date_of_birth`; `API_04_CUSTOMER_PREIMPLEMENTATION.md`.  
Risk: Unlawful child data processing; Families policy.  
Required Change: Participant-without-account + guardian consent design.  
Affected Domain: Customer, membership, notifications.  
When Required: Before kids-center production.  
Source: Apple Guideline 1.3 / Kids Category; Google Families / Designed for Families (Play Console Help).

### FINDING: No App Review demo environment

Status: **GAP**  
Priority: **P1** before first review  
Platform: Both  
Requirement: Reviewer must exercise core features.  
Current Digitize State: Auth required; no documented demo tenant.  
Repository Evidence: Frozen auth; production remote mode in `main.dart`.  
Risk: 2.1 incomplete app.  
Required Change: `APP_REVIEW_ENVIRONMENT` seed + notes.  
Affected Domain: Ops, identity, license.  
When Required: First submission.  
Source: https://developer.apple.com/app-store/review/guidelines/ §2.1

### FINDING: Example application IDs and debug release signing

Status: **GAP**  
Priority: **P1**  
Platform: Both  
Requirement: Unique production IDs; release signing.  
Current Digitize State: `com.example.*`; debug signingConfig.  
Repository Evidence: `android/app/build.gradle.kts`; `project.pbxproj`.  
Risk: Cannot publish; impersonation confusion.  
Required Change: Production IDs, upload key, Apple certs.  
Affected Domain: Mobile release.  
When Required: First submission.  
Source: Play / App Store Connect technical requirements.

### FINDING: Data Safety / App Privacy forms unprepared

Status: **GAP**  
Priority: **P1**  
Platform: Both  
Requirement: Accurate declarations matching the binary.  
Current Digitize State: No form drafts; data categories exist in DB.  
Repository Evidence: Customer/identity schemas vs empty SDK list.  
Risk: False “no data collected” vs backend PII.  
Required Change: Mapping in §18 of this doc → legal + store ops.  
Affected Domain: Store listing.  
When Required: Listing creation.  
Source: https://developer.apple.com/app-store/app-privacy-details/ · https://support.google.com/googleplay/android-developer/answer/10787469

### FINDING: Sign in with Apple not required today

Status: **NOT APPLICABLE**  
Priority: **P3** unless social login is added  
Platform: Apple  
Requirement: 4.8 if third-party login is primary.  
Current Digitize State: Password `login_identifier` only.  
Repository Evidence: `AUTH_CONTRACT_FREEZE.md` SSO deferred.  
Risk: Adding Google Sign-In without SIWA.  
Required Change: None now; freeze “no social login in v1 mobile.”  
Affected Domain: Auth.  
When Required: If SSO product decision changes.  
Source: https://developer.apple.com/app-store/review/guidelines/ §4.8

### FINDING: No device location or unused sensitive permissions

Status: **PASS**  
Priority: **P3** (keep it that way)  
Platform: Both  
Requirement: Justify every permission.  
Current Digitize State: INTERNET only.  
Repository Evidence: Manifest, Info.plist, pubspec.  
Risk: Future feature adding GPS “because sites have addresses.”  
Required Change: Policy: business address ≠ device location.  
Affected Domain: Flutter.  
When Required: Ongoing.  
Source: Apple 5.1.1 / 5.1.4; Google Permissions / Location.

### FINDING: No analytics/ads/push SDKs

Status: **PASS** (current)  
Priority: **P3** / **FUTURE**  
Platform: Both  
Requirement: Disclose SDKs; ATT if tracking.  
Current Digitize State: None.  
Repository Evidence: `pubspec.yaml`.  
Risk: Adding Firebase “by default.”  
Required Change: SDK review gate.  
Affected Domain: Mobile.  
When Required: Before adding.  
Source: Apple privacy; Google Data Safety.

### FINDING: Notification consent not implemented

Status: **FUTURE REQUIREMENT**  
Priority: **P2** with API-10  
Platform: Both  
Requirement: Optional permission; marketing consent.  
Current Digitize State: Catalog only.  
Repository Evidence: `operations.py` API-10.  
Risk: Spam / ATT confusion if push used for ads.  
Required Change: Prefs + OS permission when shipping push.  
Affected Domain: Communication.  
When Required: Before push.  
Source: Apple 4.0 / notifications; Google notifications.

### FINDING: Retention periods unspecified

Status: **DECISION REQUIRED**  
Priority: **P2**  
Platform: Both (disclosure) + law  
Requirement: Privacy policy must explain retention/deletion.  
Current Digitize State: Principles only.  
Repository Evidence: `TEST-03` awaiting Legal; API-00 no physical delete for financial data.  
Risk: Cannot write a truthful policy.  
Required Change: Legal schedule.  
Affected Domain: All data.  
When Required: Before privacy policy.  
Source: Apple 5.1.1(i); Google User Data.

### FINDING: Customer document metadata without upload UX

Status: **PARTIAL**  
Priority: **P2**  
Platform: Both  
Requirement: Photo library / camera purpose strings if used.  
Current Digitize State: `storage_reference` metadata API; no Flutter picker.  
Repository Evidence: `customer_document.py`; no `image_picker`.  
Risk: Adding camera without purpose string.  
Required Change: Optional permission + disclosure when files ship.  
Affected Domain: Customer.  
When Required: Document feature.  
Source: Apple permission purpose strings.

### FINDING: Advertising only hypothetical

Status: **FUTURE REQUIREMENT**  
Priority: **P3**  
Platform: Both  
Requirement: ATT, ads ID, Families if kids.  
Current Digitize State: None.  
Repository Evidence: No ads packages.  
Risk: Personalized ads in a kids-adjacent product.  
Required Change: Separate B2B promo vs third-party tracking.  
Affected Domain: Campaigns.  
When Required: If ads productized.  
Source: Apple 3.1.4 / tracking; Google Ads.

### FINDING: Target API inherited, not pinned

Status: **PARTIAL**  
Priority: **P2** at upload (calendar: API 36 by 31 Aug 2026)  
Platform: Google  
Requirement: Play target API policy.  
Current Digitize State: `targetSdk = flutter.targetSdkVersion`.  
Repository Evidence: `android/app/build.gradle.kts`.  
Risk: Upload blocked if Flutter lags.  
Required Change: Verify at release; upgrade Flutter if needed then.  
Affected Domain: Android.  
When Required: Play upload.  
Source: https://support.google.com/googleplay/android-developer/answer/11926878

### FINDING: Secure token storage present; default env is mock in tests only

Status: **PASS** with caveat  
Priority: **P2** (ops)  
Platform: Both  
Requirement: Don’t leak tokens; don’t ship mocks.  
Current Digitize State: `flutter_secure_storage`; `kReleaseMode` → production remote. Provider default remains development for tests.  
Repository Evidence: `main.dart`, `app_environment.dart`.  
Risk: Mis-built flavors.  
Required Change: Release checklist.  
Affected Domain: Flutter.  
When Required: Production.  
Source: Google User Data security; Apple 2.1 accuracy.

---

## 23. Required Product Decisions

Distinguish **frozen architecture** from **deferred implementation** and **store-submission blockers**. Do not treat frozen items as unresolved merely because wording changed.

| ID | Decision | Status |
| --- | --- | --- |
| DEC-STORE-001 | Account deletion model (anonymize vs hard delete vs org-retained records). Lifecycle **direction** frozen: Active, Suspended, Deactivated, Deletion Requested, Deleted/Anonymized. Suspend ≠ delete. | Architecture direction **FROZEN**; **implementation deferred**. **Store blocker.** |
| DEC-STORE-002 | Customer vs Participant vs app-user. Customer ≠ Participant. Customer is not `identity.user_account` in Phase 1. | **FROZEN** |
| DEC-STORE-003 | Parent/guardian and minors. Guardian Relationship future-ready; detailed UX deferred. | Architecture **FROZEN** as future-ready; **implementation deferred**. Kids-center go-live still needs consent UX. |
| DEC-STORE-004 | SaaS = Organization → Digitize/OreeOn (not staff-mobile checkout). Facility commerce = Customer → Facility (non-store billing for physical recreation). | **FROZEN**. Checkout implementation deferred. |
| DEC-STORE-005 | Social login: none in v1 (recommended) | Unchanged recommendation; not contradicted |
| DEC-STORE-006 | Notification / marketing consent | **Deferred** (API-10) |
| DEC-STORE-007 | Data retention schedule (Legal) | **Deferred** (legal copy) |
| DEC-STORE-008 | Analytics/crash SDK: none until named vendor + DPA | Unchanged |
| DEC-STORE-009 | Phase-1 operational app: Organization Admin, Site Admin, Staff. Platform Admin: separate app. Customer mobile: Phase 2. Manager: not a role. | **FROZEN** |
| DEC-STORE-010 | Production bundle/application IDs and display name | **Store blocker** (implementation) |
| DEC-STORE-011 | Age rating / Kids Category: **not** Kids Category unless designed for children | Unchanged guidance; Phase-1 app is operational, not Kids Category |
| DEC-STORE-012 | Reviewer demo tenant ownership | **Store blocker** (implementation) |

### Frozen decisions

Hierarchy; four roles; Platform Admin platform-wide access; Phase-1 operational personas; Customer mobile Phase 2; Customer ≠ Participant; SaaS vs facility commerce; account-lifecycle **states**; 228 inventory; semantic `operation_id`.

### Deferred implementation

Deletion/anonymization APIs and UX; Platform Admin product UI; customer mobile; guardian UX; live facility checkout; privacy-policy copy; retention durations.

### Store-submission blockers

Privacy policy; in-app + web deletion; production IDs/signing; reviewer demo; Data Safety / App Privacy forms.

### API-05 constraints

Membership Plan is Customer → Facility commerce only. No Manager role. No customer-mobile assumption. No SaaS IAP. No inventory expansion in this gate.

---

## 24. Required Architecture Changes

| Domain | Current | Future | APIs | Database | Flutter | Priority | Defer? |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Identity | Deactivate | Self-service delete + anonymize + last-admin guard | New auth/identity ops (not API-05) | `user_account` status; jobs | Settings → Delete account | P0 submit / P1 now | Not past first store binary |
| Customer | Archive | Distinguish archive vs user-requested erase; optional unlink from login | Customer + future customer-auth | `customer`, contacts, documents | Only if customer app | P1 | Not past kids/customer login |
| Membership | Not started | Physical-service PSP; no StoreKit/Play Billing | API-05/08 | membership + commercial | Pay wall | P1 | **Do not implement until API-05 contract review respects freeze** |
| SaaS | API-09 lifecycle | Keep checkout off-mobile | API-09 | commercial.subscription | Entitlement only | P1 | Web billing OK |
| Consent | Raw table | Typed consents + withdrawal | Customer / notifications | `customer_consent` | Legal + toggles | P2 | Until marketing/push |
| Guardian | Deferred | Parent account + child participant | Customer | New FKs | Customer app | P1 kids | Until kids vertical |
| Review | None | Demo seed | Ops | Seed data | None | P1 | Until submit |
| Store IDs | example.* | Production IDs + signing | None | None | Gradle/Xcode | P1 | Until submit |
| Push | None | Optional permission + prefs | API-10 | tokens | OS permission | P2 | Until notifications |
| Export | Unused model | DSAR export | Reports | `data_exports` | Request UI | P2 | GDPR/production |

**Do not implement these in this task.**

---

## 25. Recommended Implementation Order

1. **Architecture freeze (done):** DEC-STORE-009 (personas/roles), DEC-STORE-004 (billing channels), DEC-STORE-002 (Customer ≠ Participant). Deletion **states** frozen; deletion **implementation** still open (DEC-STORE-001).
2. **Next:** API-05 Membership Plan **contract review** (not implementation in the access freeze).
3. Legal: privacy policy + retention schedule (DEC-STORE-007).
4. Identity: deletion/anonymization design (still no store SDK).
5. `APP_REVIEW_ENVIRONMENT` seed plan.
6. Production app IDs and signing (release engineering).
7. Only then: Membership Plan **implementation** with **facility PSP**, notifications, optional camera for QR, optional analytics.

---

## 26. Compliance Requirements Matrix

| Requirement ID | Platform | Policy Area | Requirement | Applies? | Current Implementation | Repository Evidence | Risk | Required Architectural Change | Required Product Decision | Priority | Status | Source URL |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| APPLE-001 | Apple | Privacy | Privacy policy in app + metadata | Yes | None | No policy files | Rejection | In-app link | Legal URL | P0 | GAP | https://developer.apple.com/app-store/review/guidelines/ |
| APPLE-002 | Apple | Account | In-app account deletion 5.1.1(v) | Yes if accounts | Logout/deactivate only | Auth freeze; no delete API | Rejection | Deletion + anonymize | DEC-STORE-001 | P0 | GAP | https://developer.apple.com/support/offering-account-deletion-in-your-app/ |
| APPLE-003 | Apple | Payments | IAP for digital in-app; 3.1.3(e) for off-app services | Yes | No IAP; API-09/05 split | catalog.py | Wrong billing | Keep SaaS off-app; facility non-IAP | DEC-STORE-004 | P1 | PARTIAL | https://developer.apple.com/app-store/review/guidelines/ |
| APPLE-004 | Apple | Login | 4.8 Sign in with Apple if social primary | Not today | Password only | AUTH_CONTRACT_FREEZE | Future | None unless SSO | DEC-STORE-005 | P3 | NOT APPLICABLE | https://developer.apple.com/app-store/review/guidelines/ |
| APPLE-005 | Apple | Review | Demo account / complete app 2.1 | Yes | No demo env | main.dart login gate | Rejection | Review seed | DEC-STORE-012 | P1 | GAP | https://developer.apple.com/app-store/review/guidelines/ |
| APPLE-006 | Apple | Privacy | App Privacy nutrition labels | Yes at listing | Unprepared | Schemas vs no form | Inaccuracy | Data map | Legal | P1 | GAP | https://developer.apple.com/app-store/app-privacy-details/ |
| APPLE-007 | Apple | Kids | Kids Category / 1.3 | If kids product | DOB; no guardian UX | customer.py | Legal | Guardian UX when kids vertical | DEC-STORE-003 | P1 | DEFERRED | https://developer.apple.com/app-store/review/guidelines/ |
| APPLE-008 | Apple | Permissions | Purpose strings | When used | None needed | Info.plist | Future | Don’t add unused | — | P3 | PASS | https://developer.apple.com/documentation/uikit/protecting-the-user-s-privacy |
| GOOGLE-001 | Google | User Data | Privacy policy | Yes | None | Same | Rejection | Same as APPLE-001 | Legal | P0 | GAP | https://support.google.com/googleplay/android-developer/answer/10144311 |
| GOOGLE-002 | Google | Account | In-app + **web** deletion | Yes at Play | None | Same | Rejection | Web + in-app | DEC-STORE-001 | P0 | GAP | https://support.google.com/googleplay/android-developer/answer/13327111 |
| GOOGLE-003 | Google | Data Safety | Form + deletion questions | Yes at listing | None | — | Rejection | Process | Legal | P1 | GAP | https://support.google.com/googleplay/android-developer/answer/10787469 |
| GOOGLE-004 | Google | Payments | Play Billing for digital; **not** for gym memberships / physical services | Yes | No Play Billing | catalog API-05/08/09 | Wrong SDK | Facility PSP | DEC-STORE-004 | P1 | PARTIAL | https://support.google.com/googleplay/android-developer/answer/9858738 |
| GOOGLE-005 | Google | Technical | Target API 35 now; **36** from 31 Aug 2026 for new updates | At upload | Flutter-inherited | build.gradle.kts | Upload block | Verify SDK | — | P2 | PARTIAL | https://support.google.com/googleplay/android-developer/answer/11926878 |
| GOOGLE-006 | Google | Permissions | Declare only used | Yes | INTERNET | Manifest | Low | Keep clean | — | P3 | PASS | https://support.google.com/googleplay/android-developer/answer/9888170 |
| CROSS-001 | Both | Auth | First-party login OK | Yes | Implemented | auth routes | Low | — | DEC-STORE-005 | P3 | PASS | AUTH_CONTRACT_FREEZE.md |
| CROSS-002 | Both | Commerce | Split SaaS vs facility | Yes | Frozen + inventory split | freeze + catalog | High if merged | Respect in API-05 | DEC-STORE-004 | P1 | FROZEN | This audit |
| CROSS-003 | Both | Retention | Disclose periods | Yes | Unspecified | TEST-03 | Policy lie | Legal matrix | DEC-STORE-007 | P2 | DECISION REQUIRED | Privacy policies |
| CROSS-004 | Both | SDKs | Minimize processors | Yes | Few Flutter pkgs | pubspec.yaml | Low now | SDK gate | DEC-STORE-008 | P3 | PASS | Data Safety / Nutrition |
| CROSS-005 | Both | Identity | Production package IDs + signing | Yes | example + debug sign | Gradle / pbxproj | Cannot ship | Release eng | DEC-STORE-010 | P1 | GAP | Store consoles |
| CROSS-006 | Both | Location | Device GPS ≠ address | If tempted | Not used | Manifest | Review | Ban GPS for addresses | — | P3 | PASS | Apple 5.1.4 |

---

## 27. Release Gate

```text
MOBILE STORE & PLATFORM COMPLIANCE GATE

Status:
FAIL (store binary)

Architecture (access / personas / commerce):
FROZEN — see ACCESS_MOBILE_COMMERCE_ARCHITECTURE_FREEZE.md

P0 findings:
4
(APPLE-001/GOOGLE-001 privacy policy; APPLE-002 deletion; GOOGLE-002 web deletion;
combined legal-surface gap counted in findings APPLE-001, APPLE-002, GOOGLE-002,
and FINDING privacy)

P1 findings:
store blockers remain (review env, example IDs/signing, Data Safety/App Privacy,
archive≠delete). Persona and SaaS-vs-facility commerce are no longer unresolved.

P2 findings:
5
(retention, notifications, documents/camera later, target API verify,
token/release hygiene)

P3 findings:
5
(SIWA N/A, location PASS, SDK PASS, ads FUTURE, permission PASS)

Architecture blockers (open product questions):
0 for personas, Platform Admin access, Site Admin vs Manager, Customer mobile
phase, Customer vs Participant, SaaS vs facility commerce.

Deferred implementation:
deletion/anonymize, guardian UX, Platform Admin product UI, customer mobile,
live facility checkout, privacy copy.

Store-submission blockers:
Privacy policy, deletion (in-app+web), production IDs/signing, reviewer demo,
accurate Data Safety/App Privacy.

Product decisions DEC-STORE-001 … 012:
Reconciled — not duplicated. Frozen vs deferred vs store blocker as in §23.

Store submission readiness:
NOT READY

Architecture-before-API-05:
READY FOR CONTRACT REVIEW — freeze is written. Do not implement API-05 in the
access/mobile/commerce documentation gate.
```

---

## 28. Sources

Accessed **13 September 2026**:

- Apple App Review Guidelines — https://developer.apple.com/app-store/review/guidelines/
- Apple: Offering account deletion in your app — https://developer.apple.com/support/offering-account-deletion-in-your-app/
- Apple News: Account deletion requirement — https://developer.apple.com/news/?id=12m75xbj
- Apple App Privacy details — https://developer.apple.com/app-store/app-privacy-details/
- Google Play User Data — https://support.google.com/googleplay/android-developer/answer/10144311
- Google Play account deletion — https://support.google.com/googleplay/android-developer/answer/13327111
- Google Play Data Safety — https://support.google.com/googleplay/android-developer/answer/10787469
- Google Play Payments — https://support.google.com/googleplay/android-developer/answer/9858738
- Understanding Play Payments — https://support.google.com/googleplay/android-developer/answer/10281818
- Google Play target API levels — https://support.google.com/googleplay/android-developer/answer/11926878

Internal evidence (not store policy): `docs/architecture/AUTH_CONTRACT_FREEZE.md`, `docs/architecture/API_04_CUSTOMER_PREIMPLEMENTATION.md`, `docs/07_API_Collections/API-00_API_Collection_Standards.md`, `digitize-services/app/api/contracts/catalog.py`, `digitize-services/app/modules/customer/models/customer.py`, `digitize-ui/pubspec.yaml`, Android/iOS project files listed above.
