# subscription-settings - Requirements

## Overview
`subscription-settings` là spec của Phase 8 (Account & Settings). Nó dựng phần Subscription trong Settings (WF-014 subscription portion + WF-018 cancel modal): hiển thị trạng thái subscription hiện tại (Free / Trial X ngày còn lại / Premium với ngày gia hạn), cho phép quản lý qua StoreKit (cancel, restore purchases), xem ngày thanh toán. Spec tái sử dụng `SubscriptionService` từ `subscription-management` (đã có startTrial/cancelSubscription/restorePurchases/getStatus) và subscribe vào `CustomerInfo` publisher để cập nhật UI real-time. Spec KHÔNG bao gồm paywall (đó là `paywall-display`) và KHÔNG bao gồm việc khởi tạo trial (đó là `subscription-management`).

## Evidence References
- **Market data from PRD:** Premium tier có cancel dễ trong app, không yêu cầu support contact (PRD §11) — đây là lợi thế cạnh tranh chính so với Cal AI (đã từng bị Apple reject vì Guideline 3.1.2c/5.6 — buộc user phải liên hệ support để huỷ). Restore purchases chuẩn StoreKit là bắt buộc theo App Store guideline.
- **Source documents:**
  - `.claude/specs/Calo-AI/Functional_Requirements.md` — FR-024 (cancel subscription; BR-024.1/2/3, ERR-024.1/2, AC-024.1..4), FR-025 (manage subscription; BR-025.1/2, VR-025.1, ERR-025.1, AC-025.1..3), FR-026 (restore purchases; BR-026.1/2, VR-026.1, ERR-026.1/2/3, AC-026.1..3)
  - `.claude/specs/Calo-AI/Use_Cases.md` — UC-021 (huỷ subscription), UC-022 (quản lý subscription), UC-023 (restore purchase)
  - `.claude/specs/Calo-AI/Wireframes.md` — WF-014 (Settings — subscription section), WF-015 (Share — settings entry), WF-018 (Cancel Subscription confirm modal)
  - `.claude/specs/Calo-AI/PRD.md` §11 (Premium huỷ dễ trong app, restore chuẩn StoreKit)
- **Key KPIs / measurable targets:** Subscription status rendered within 1s of `SubscriptionService.CustomerInfo` publishing; restore query completes within 10s; cancel flow goes through App Store (no support contact).

## Requirements

### Requirement 1 (REQ-001): Subscription Status Display
**User Story:** As a user, I want to see my current subscription status (Free / Trial X days left / Premium with renewal date) in Settings, so that I know exactly where I stand on Premium.
**Source:** FR-024, FR-025; UC-022; WF-014

#### Acceptance Criteria
1. AC-001.1: WHEN the user opens Settings THEN THE SYSTEM SHALL display a Subscription section showing one of three states: "Free — Upgrade to Premium", "Trial — X days left" (with the countdown derived from `trialEndDate`), or "Premium — renews [renewal_date]" (with the date formatted in the user's locale).
2. AC-001.2: WHEN `SubscriptionService.CustomerInfo` publishes a change (renewal date updated, trial expired, billing cycle rolled over) THEN THE SYSTEM SHALL refresh the status row within 1 second.
3. AC-001.3: WHILE the status is loading THEN THE SYSTEM SHALL show a skeleton row and SHALL NOT show stale text from a previous session.
4. AC-001.4: IF fetching the status fails THEN THE SYSTEM SHALL show a recoverable error via `ErrorHandler` with a Retry button, AND SHALL keep the last known status visible if present.

### Requirement 2 (REQ-002): Manage / Cancel Subscription
**User Story:** As a Premium subscriber, I want to cancel my subscription from Settings in the app (no support contact), so that I retain trust that billing is transparent and reversible.
**Source:** FR-024 (BR-024.1/2/3, ERR-024.1/2); FR-025 (BR-025.1/2); UC-021; WF-018

#### Acceptance Criteria
1. AC-002.1: WHEN the user is on Free tier THEN THE SYSTEM SHALL display an "Upgrade to Premium" `CaloButton` (primary) that navigates to the paywall (`paywall-display` route). The "Cancel" and "Manage" buttons SHALL NOT be visible.
2. AC-002.2: WHEN the user is on Premium (active or trial) THEN THE SYSTEM SHALL display three actions: "Manage" (opens App Store subscription management via deep-link `itms-apps://apps.apple.com/account/subscriptions`), "Restore purchases" (handled by REQ-003), and "Cancel" (opens the cancel confirm modal WF-018).
3. AC-002.3: WHEN the user taps "Cancel" THEN THE SYSTEM SHALL present the WF-018 confirmation modal: "Cancel Premium? You'll lose unlimited scans. Your access continues until [renewal_date]." with "Keep subscription" (primary) and "Continue cancellation" (destructive) buttons.
4. AC-002.4: WHEN the user confirms cancellation ("Continue cancellation") THEN THE SYSTEM SHALL call `SubscriptionService.cancelSubscription()` and on success show a toast "Premium expires on [renewal_date]" and update the status to "Premium — expires [renewal_date]".
5. AC-002.5: IF `cancelSubscription()` fails OR the App Store cannot be reached THEN THE SYSTEM SHALL show a recoverable error via `ErrorHandler` with copy "Please cancel from Settings > [App Name] > Manage Subscriptions" (matching ERR-024.2) and SHALL keep the user subscribed.
6. AC-002.6: IF the user taps "Keep subscription" THEN THE SYSTEM SHALL dismiss the cancel modal without calling `cancelSubscription()`.

### Requirement 3 (REQ-003): Restore Purchases
**User Story:** As a user who switched devices or reinstalled the app, I want to restore my previous subscription from Settings, so that I keep my Premium access without contacting support.
**Source:** FR-026 (BR-026.1/2, VR-026.1, ERR-026.1/2/3); UC-023; WF-014

#### Acceptance Criteria
1. AC-003.1: WHEN the user taps "Restore purchases" THEN THE SYSTEM SHALL call `SubscriptionService.restorePurchases()` and show a loading indicator on the button while in flight.
2. AC-003.2: IF the restore finds a previous subscription for the current Apple ID THEN THE SYSTEM SHALL update `CustomerInfo` (Premium activated), show toast "Premium restored", and refresh the status row within 1 second.
3. AC-003.3: IF the restore finds no previous purchases THEN THE SYSTEM SHALL show "No previous purchases for this Apple ID" (matching ERR-026.1) inline and SHALL NOT show an error banner.
4. AC-003.4: IF the restore call fails (network / App Store unavailable) THEN THE SYSTEM SHALL show a recoverable error via `ErrorHandler` with copy "Could not connect to App Store. Try again later." (matching ERR-026.2) and keep the Restore button enabled for retry.
5. AC-003.5: WHERE the current Apple ID differs from the original purchase Apple ID THEN THE SYSTEM SHALL show "Use the same Apple ID as your original purchase" (matching ERR-026.3) inline.

## Non-Functional Requirements
- NFR-SS-001: Status freshness — UI shall reflect `CustomerInfo` updates within 1s of publisher emission (live subscription state).
- NFR-SS-002: Cancel transparency — Per PRD §11, cancel flow MUST complete entirely in-app (no support contact); if App Store is unreachable, the fallback copy directs the user to App Store Subscriptions (Apple-mandated path).
- NFR-SS-003: Restore compliance — Restore purchases MUST be available regardless of subscription state (per Apple StoreKit guideline); it SHALL be a separate, always-visible action in the Subscription section.
- NFR-SS-004: Trial countdown — "Trial — X days left" SHALL be calculated from `trialEndDate` rounded down (calendar days, local timezone); at 0 days remaining, the row transitions to Free state.
- NFR-SS-005: Auth gating — Subscription Settings SHALL be reachable only when `AuthService.sessionValid() == true`; otherwise route to Sign in.
- NFR-SS-006: Service reuse — The spec MUST NOT re-implement StoreKit / RevenueCat logic; it only consumes `SubscriptionService` from `subscription-management`. No new SPM dependency.
- NFR-SS-007: Accessibility — All Subscription section actions SHALL meet WCAG 2.1 AA (NFR-009): tap targets ≥44×44pt, VoiceOver labels (e.g., "Premium subscription, renews January 25"), Dynamic Type.
