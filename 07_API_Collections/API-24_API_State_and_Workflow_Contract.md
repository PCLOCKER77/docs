> **Status:** Frozen — 2026-07-26 — 2026-07-26

# API-24 API State and Workflow Contract

**Document ID:** API-24  
**Document Name:** API State and Workflow Contract  
**Company:** OreeOn Technologies Pvt. Ltd.  
**Product:** Digitize  
**Document Type:** API Workflow Governance Documentation  
**Backend Technology:** FastAPI  
**Authentication:** JWT  
**API Version:** v1  
**Document Version:** 0.1  
**Status:** Design Draft  
**Owner:** API Architecture / Product Architecture  
**Reviewer:** Solution Architecture / Business Analysis / UI/UX / Backend Engineering / QA  
**Dependencies:** API-00, API-02 to API-14, API-16, API-19, API-22, API-23  
**Last Updated:** July 2026

---

# 1. Document Metadata

| Attribute | Value |
|---|---|
| Document ID | API-24 |
| Document Name | API State and Workflow Contract |
| Output File | API-24_API_State_and_Workflow_Contract.md |
| API Version | v1 |
| Document Version | 0.1 |
| Status | Design Draft |
| Governing Standard | API-00_API_Collection_Standards.md |

---

# 2. Purpose

This document centralizes lifecycle states, allowed API actions, forbidden actions, business conditions, required permissions, resulting states, audit events, notification events, and UI action visibility rules.

It gives UI/UX and frontend teams a state-driven contract for buttons, menus, workflows, confirmations, disabled states, and next actions.

---

# 3. Scope

In scope:

- Organization lifecycle.
- Facility and Site lifecycle.
- User lifecycle.
- Customer lifecycle.
- Membership lifecycle.
- Attendance lifecycle.
- Invoice, payment, and refund lifecycle.
- Subscription and license lifecycle.
- Campaign and notification lifecycle.
- Ticket lifecycle.
- Report/export lifecycle.
- Generic workflow action rules for UI visibility.

Out of scope:

- Business process diagrams already owned by BA-04.
- Database state machine implementation.
- UI visual design.
- Workflow engine source code.

---

# 4. State Contract Principles

| Principle | Standard |
|---|---|
| Explicit states | UI and API shall use known lifecycle states |
| API authoritative | Backend validates every state transition |
| UI state-aware | UI actions shall follow allowed actions |
| Auditable | Lifecycle transitions create audit evidence |
| Permission-bound | Every transition requires permission |
| Idempotent where needed | Retry-prone actions require idempotency |
| No hidden transitions | Automated transitions shall be documented |

---

# 5. State Table Template

| Current State | Allowed API Action | Forbidden Actions | Required Permission | Business Conditions | Resulting State | UI Visibility | Audit Event | Notification |
|---|---|---|---|---|---|---|---|---|
| STATE | Action | Actions | `permission.code` | Conditions | NEXT_STATE | Show/Hide/Disable | EVENT | Notification |

---

# 6. Organization Lifecycle

| Current State | Allowed API Action | Forbidden Actions | Required Permission | Business Conditions | Resulting State | UI Visibility | Audit Event | Notification |
|---|---|---|---|---|---|---|---|---|
| DRAFT | Create/update profile | Suspend/archive | `tenant.organization.create` | Platform user authorized | DRAFT | Show setup actions | ORGANIZATION_CREATED | Optional |
| DRAFT | Activate | Suspend/archive | `tenant.organization.activate` | Required profile/config complete | ACTIVE | Show activate | ORGANIZATION_ACTIVATED | Organization activated |
| ACTIVE | Update/suspend | Create duplicate | `tenant.organization.update` | Tenant scope valid | ACTIVE/SUSPENDED | Show allowed actions | ORGANIZATION_UPDATED | Optional |
| SUSPENDED | Reactivate/archive | Normal operations | `tenant.organization.activate` | Suspension reason resolved | ACTIVE/ARCHIVED | Show reactivate/archive | ORGANIZATION_REACTIVATED | Reactivation |
| ARCHIVED | View history | Activate/update | `tenant.organization.view` | Read-only access | ARCHIVED | Hide mutations | ORGANIZATION_VIEWED | None |

---

# 7. Facility and Site Lifecycle

| Current State | Allowed API Action | Forbidden Actions | Required Permission | Business Conditions | Resulting State | UI Visibility | Audit Event | Notification |
|---|---|---|---|---|---|---|---|---|
| DRAFT | Update/activate | Suspend/archive | `facility.manage` / `site.manage` | Parent Organization active | ACTIVE | Show activate | FACILITY_ACTIVATED / SITE_ACTIVATED | Optional |
| ACTIVE | Update/suspend/archive | Create duplicate | `facility.manage` / `site.manage` | Scope valid | ACTIVE/SUSPENDED/ARCHIVED | Show permitted | FACILITY_UPDATED / SITE_UPDATED | Optional |
| SUSPENDED | Reactivate/archive | Attendance/billing operations | `facility.lifecycle.manage` | Reason resolved | ACTIVE/ARCHIVED | Show reactivate/archive | FACILITY_REACTIVATED / SITE_REACTIVATED | Optional |
| ARCHIVED | View history | Operational actions | `facility.view` / `site.view` | Read-only | ARCHIVED | Hide mutations | FACILITY_VIEWED / SITE_VIEWED | None |

---

# 8. User Lifecycle

| Current State | Allowed API Action | Forbidden Actions | Required Permission | Business Conditions | Resulting State | UI Visibility | Audit Event | Notification |
|---|---|---|---|---|---|---|---|---|
| INVITED | Activate/resend invite | Login if not activated | `user.activate` | Credential setup complete | ACTIVE | Show activate/resend | USER_ACTIVATED | Staff account activated |
| ACTIVE | Suspend/reset/deactivate | Invite duplicate | `user.manage` | Role/scope valid | SUSPENDED/DEACTIVATED | Show actions by role | USER_SUSPENDED | Staff notice |
| SUSPENDED | Reactivate/deactivate | Normal login | `user.manage` | Suspension reason resolved | ACTIVE/DEACTIVATED | Show reactivate | USER_REACTIVATED | Staff notice |
| DEACTIVATED | View history | Login/reactivate unless policy allows | `user.view` | Historical access | DEACTIVATED | Hide mutations | USER_VIEWED | None |

---

# 9. Customer Lifecycle

| Current State | Allowed API Action | Forbidden Actions | Required Permission | Business Conditions | Resulting State | UI Visibility | Audit Event | Notification |
|---|---|---|---|---|---|---|---|---|
| DRAFT | Register/complete profile | Suspend/archive | `customer.create` | Required profile fields | ACTIVE | Show complete registration | CUSTOMER_REGISTERED | Welcome optional |
| ACTIVE | Update/transfer/suspend/archive | Register duplicate | `customer.update` | Scope valid | ACTIVE/SUSPENDED/ARCHIVED | Show permitted | CUSTOMER_UPDATED | Optional |
| SUSPENDED | Reactivate/archive | Attendance/membership purchase unless allowed | `customer.lifecycle.manage` | Reason resolved | ACTIVE/ARCHIVED | Show reactivate/archive | CUSTOMER_REACTIVATED | Reactivation |
| ARCHIVED | View history | Update/attendance/purchase | `customer.history.view` | Read-only | ARCHIVED | Hide mutations | CUSTOMER_HISTORY_VIEWED | None |

---

# 10. Membership Lifecycle

| Current State | Allowed API Action | Forbidden Actions | Required Permission | Business Conditions | Resulting State | UI Visibility | Audit Event | Notification |
|---|---|---|---|---|---|---|---|---|
| DRAFT | Activate/cancel | Freeze/resume/renew | `membership.activate` | Payment condition satisfied | ACTIVE/CANCELLED | Show activate/cancel | MEMBERSHIP_ACTIVATED | Membership activated |
| PENDING_PAYMENT | Activate/cancel | Attendance/freeze | `membership.activate` | Payment confirmed | ACTIVE/CANCELLED | Show payment/activate | MEMBERSHIP_ACTIVATED | Payment confirmation |
| ACTIVE | Renew/upgrade/downgrade/freeze/cancel | Activate duplicate | `membership.manage` | Plan rules satisfied | ACTIVE/FROZEN/CANCELLED | Show lifecycle actions | MEMBERSHIP_UPDATED | Lifecycle notification |
| FROZEN | Resume/cancel | Freeze duplicate/attendance | `membership.resume` | Freeze period valid | ACTIVE/CANCELLED | Show resume/cancel | MEMBERSHIP_RESUMED | Resume notification |
| EXPIRED | Renew/view history | Freeze/resume/attendance | `membership.renew` | Renewal allowed | ACTIVE/EXPIRED | Show renew | MEMBERSHIP_RENEWED | Renewal |
| CANCELLED | View history | Activate/freeze/resume | `membership.history.view` | Read-only | CANCELLED | Hide mutations | MEMBERSHIP_HISTORY_VIEWED | None |

---

# 11. Attendance Lifecycle

| Current State | Allowed API Action | Forbidden Actions | Required Permission | Business Conditions | Resulting State | UI Visibility | Audit Event | Notification |
|---|---|---|---|---|---|---|---|---|
| NOT_RECORDED | Check-in | Check-out/cancel | `attendance.checkIn` | Eligibility/capacity valid | CHECKED_IN | Show check-in | ATTENDANCE_CHECKED_IN | Attendance recorded |
| CHECKED_IN | Check-out/update/cancel | Duplicate check-in | `attendance.checkOut` | Active attendance exists | CHECKED_OUT/CANCELLED | Show checkout/cancel | ATTENDANCE_CHECKED_OUT | Optional |
| CHECKED_OUT | Update/audit | Check-out duplicate | `attendance.update` | Correction allowed | CORRECTED/CHECKED_OUT | Show correction if permitted | ATTENDANCE_UPDATED | Optional |
| CANCELLED | View audit | Update/check-out | `attendance.audit.view` | Read-only | CANCELLED | Hide mutations | ATTENDANCE_CANCELLED | Optional |

---

# 12. Invoice Lifecycle

| Current State | Allowed API Action | Forbidden Actions | Required Permission | Business Conditions | Resulting State | UI Visibility | Audit Event | Notification |
|---|---|---|---|---|---|---|---|---|
| DRAFT | Add items/finalize/cancel | Pay | `billing.manage` | Charges/taxes valid | ISSUED/CANCELLED | Show finalize/cancel | INVOICE_GENERATED | Optional |
| ISSUED | Collect payment/cancel/adjust | Finalize duplicate | `payment.collect` | Balance due | PARTIALLY_PAID/PAID/CANCELLED | Show payment | PAYMENT_COLLECTED | Receipt |
| PARTIALLY_PAID | Collect payment/refund where allowed | Cancel without policy | `payment.collect` | Balance remains | PAID/REFUNDED | Show payment/refund | PAYMENT_COLLECTED | Receipt |
| PAID | Refund/credit note/view | Cancel | `refund.process` | Refund policy allows | REFUNDED/PARTIALLY_REFUNDED/PAID | Show refund if permitted | REFUND_PROCESSED | Refund notice |
| CANCELLED | View history | Pay/refund | `billing.view` | Read-only | CANCELLED | Hide mutations | INVOICE_CANCELLED | Optional |

---

# 13. Payment and Refund Lifecycle

| Current State | Allowed API Action | Forbidden Actions | Required Permission | Business Conditions | Resulting State | UI Visibility | Audit Event | Notification |
|---|---|---|---|---|---|---|---|---|
| INITIATED | Verify/cancel | Receipt before success | `payment.verify` | Provider reference exists | SUCCESS/FAILED/CANCELLED | Show verifying | PAYMENT_VERIFIED | Optional |
| SUCCESS | Receipt/refund/reconcile | Cancel | `receipt.generate` | Settlement rules | RECEIPTED/REFUNDED | Show receipt/refund | RECEIPT_GENERATED | Receipt |
| FAILED | Retry payment | Receipt/refund | `payment.collect` | Retry allowed | INITIATED/FAILED | Show retry | PAYMENT_FAILED | Failure notice |
| REFUND_REQUESTED | Verify refund | Duplicate refund | `refund.process` | Provider accepted | REFUNDED/REFUND_FAILED | Show refund status | REFUND_PROCESSED | Refund notice |
| REFUNDED | View/reconcile | Refund duplicate | `payment.view` | Read-only | REFUNDED | Hide mutation | REFUND_VIEWED | None |

---

# 14. Subscription and License Lifecycle

| Current State | Allowed API Action | Forbidden Actions | Required Permission | Business Conditions | Resulting State | UI Visibility | Audit Event | Notification |
|---|---|---|---|---|---|---|---|---|
| DRAFT | Activate/cancel | Renew/suspend | `subscription.activate` | Payment/license terms valid | ACTIVE/CANCELLED | Show activate/cancel | SUBSCRIPTION_ACTIVATED | Activation |
| ACTIVE | Renew/upgrade/downgrade/suspend/cancel | Activate duplicate | `subscription.manage` | Term rules valid | ACTIVE/SUSPENDED/CANCELLED | Show lifecycle actions | SUBSCRIPTION_UPDATED | Optional |
| SUSPENDED | Reactivate/cancel | Feature access | `subscription.activate` | Reason resolved | ACTIVE/CANCELLED | Show reactivate | SUBSCRIPTION_REACTIVATED | Reactivation |
| EXPIRED | Renew/view | Feature access | `subscription.renew` | Renewal allowed | ACTIVE/EXPIRED | Show renew | SUBSCRIPTION_RENEWED | Renewal |
| LICENSE_ACTIVE | Suspend/renew/modify capabilities | Generate duplicate | `license.manage` | Subscription active | LICENSE_SUSPENDED/LICENSE_ACTIVE | Show license actions | LICENSE_UPDATED | Optional |
| LICENSE_SUSPENDED | Activate/cancel | Feature access | `license.activate` | Subscription allows | LICENSE_ACTIVE/CANCELLED | Show reactivate | LICENSE_ACTIVATED | Optional |

---

# 15. Campaign Lifecycle

| Current State | Allowed API Action | Forbidden Actions | Required Permission | Business Conditions | Resulting State | UI Visibility | Audit Event | Notification |
|---|---|---|---|---|---|---|---|---|
| DRAFT | Configure/submit/cancel | Launch | `campaign.manage` | Required fields complete | SUBMITTED/CANCELLED | Show submit | CAMPAIGN_UPDATED | Optional |
| SUBMITTED | Approve/reject | Launch before approval | `campaign.approve` | Approver authorized | APPROVED/REJECTED | Show approve/reject | CAMPAIGN_APPROVED | Approval notice |
| APPROVED | Schedule/launch/cancel | Edit restricted fields | `campaign.schedule` | Audience/consent valid | SCHEDULED/LAUNCHED/CANCELLED | Show schedule/launch | CAMPAIGN_SCHEDULED | Optional |
| SCHEDULED | Launch/pause/cancel | Approve duplicate | `campaign.launch` | Schedule reached or manual launch | LAUNCHED/PAUSED/CANCELLED | Show pause/cancel | CAMPAIGN_LAUNCHED | Launch |
| LAUNCHED | Pause/complete/cancel | Edit audience | `campaign.manage` | Delivery state valid | PAUSED/COMPLETED/CANCELLED | Show pause/complete | CAMPAIGN_COMPLETED | Completion |

---

# 16. Support Ticket Lifecycle

| Current State | Allowed API Action | Forbidden Actions | Required Permission | Business Conditions | Resulting State | UI Visibility | Audit Event | Notification |
|---|---|---|---|---|---|---|---|---|
| OPEN | Classify/assign/priority/accept | Close without resolution | `support.manage` | Ticket valid | CLASSIFIED/ASSIGNED/ACCEPTED | Show triage actions | SUPPORT_TICKET_UPDATED | Assignment |
| ACCEPTED | Progress/request info/escalate/resolve | Reopen | `support.update` | Assigned user/team | IN_PROGRESS/INFO_REQUESTED/ESCALATED/RESOLVED | Show work actions | SUPPORT_TICKET_PROGRESS_UPDATED | Optional |
| INFO_REQUESTED | Add info/progress/resolve | Close | `support.update` | Info received | IN_PROGRESS/RESOLVED | Show info controls | SUPPORT_INFO_REQUESTED | Request |
| RESOLVED | Close/reopen | Resolve duplicate | `support.close` | Customer/internal confirmation | CLOSED/REOPENED | Show close/reopen | SUPPORT_TICKET_RESOLVED | Resolution |
| CLOSED | Reopen/view | Progress/resolve | `support.reopen` | Reopen window/policy valid | REOPENED/CLOSED | Show reopen if allowed | SUPPORT_TICKET_REOPENED | Reopen |

---

# 17. Report and Export Lifecycle

| Current State | Allowed API Action | Forbidden Actions | Required Permission | Business Conditions | Resulting State | UI Visibility | Audit Event | Notification |
|---|---|---|---|---|---|---|---|---|
| REQUESTED | Poll/cancel | Download | `report.view` | Job accepted | RUNNING/CANCELLED | Show pending | REPORT_EXECUTION_REQUESTED | Optional |
| RUNNING | Poll/cancel | Duplicate export | `report.view` | Job active | COMPLETED/FAILED/CANCELLED | Show progress | REPORT_EXECUTION_UPDATED | Optional |
| COMPLETED | Download/export archive | Execute duplicate optional | `report.export` | Export permission | DOWNLOADED/COMPLETED | Show download | REPORT_EXPORT_REQUESTED | Export ready |
| FAILED | Retry/view error | Download | `report.view` | Retry allowed | REQUESTED/FAILED | Show retry | REPORT_EXECUTION_FAILED | Failure |
| CANCELLED | View | Poll/download | `report.view` | Read-only | CANCELLED | Hide mutation | REPORT_EXECUTION_CANCELLED | Optional |

---

# 18. UI Action Visibility Rules

| Rule | Standard |
|---|---|
| State unavailable | Hide action |
| Permission missing | Hide or disable action according to UX pattern |
| Business condition missing | Disable with safe reason where helpful |
| Destructive/lifecycle action | Confirm before submit |
| Retryable failure | Show retry only if API-19 retryable |
| Concurrency conflict | Ask user to refresh/review |
| Pending async state | Show progress, disable duplicate submit |

---

# 19. Test Mapping

| Workflow Area | API-16 Scenario |
|---|---|
| Lifecycle success | API-16-LIFE-001 to API-16-LIFE-010 |
| Forbidden action | API-16-AZ-001, API-16-LIFE |
| State conflict | API-16-VAL-004 or module conflict |
| Idempotent action | API-16-IDEMP |
| Concurrency state | API-16-CON |
| Audit state transition | API-16-AUD |
| Notification | API-16-NOT |

---

# 20. Governance Controls

- New lifecycle states require Product, API Architecture, and QA review.
- UI/UX shall use this document for screen action availability.
- Backend shall enforce state transitions regardless of UI behavior.
- API-20 changes are required for new states or changed transitions.
- API-23 access matrix shall be updated when state actions change.

---

# 21. Assumptions and Constraints

- State names are design baseline values and may be refined before Frozen status.
- Some automated jobs may transition state without user action.
- Exact notification templates are governed by API-10.
- Exact audit event persistence is governed by API-13 and DB mappings.

---

# 22. Acceptance Criteria

This document is acceptable when UI/UX and frontend teams can determine which actions are visible, disabled, or forbidden for major Digitize resources based on state, permission, business condition, resulting state, audit, and notification behavior.

---

# 23. Summary

API-24 centralizes state and workflow contracts for Digitize APIs. It prevents UI workflows from diverging from backend lifecycle rules.
