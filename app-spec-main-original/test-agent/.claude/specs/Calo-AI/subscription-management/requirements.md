# subscription-management - Requirements

## Overview
`subscription-management` implements the subscription lifecycle behind WF-006 and WF-018: RevenueCat-backed entitlement state, the 7-day trial badge, status display in Settings, restore purchases, and an in-app cancellation flow. It consumes the paywall's selected-plan purchase contract, observes RevenueCat `CustomerInfo`, and maps StoreKit/App Store state into a stable UI model.

Cancellation is intentionally transparent and self-serve. The app presents WF-018, then uses StoreKit's `showManageSubscriptions` UI so the user can cancel without contacting support; the user retains Premium until the App Store expiration date. Restore is idempotent and supports a new device or reinstall using the same Apple ID.

## Evidence References
- **Market data from PRD:** PRD §1 positions trust and transparent billing against Cal AI's paywall scandal; PRD §11 promises a 7-day trial, easy in-app cancellation, and standard StoreKit restore. PRD §1 product principles prohibit dark patterns and require transparent price/cycle disclosure.
- **Source documents:** `.claude/specs/Calo-AI/Functional_Requirements.md` — FR-023 (subscription verification/activation), FR-024 (cancel subscription), FR-025 (manage status/options), FR-026 (restore purchase); `.claude/specs/Calo-AI/Use_Cases.md` — UC-020 (trial confirmation), UC-021 (cancel), UC-022 (manage), UC-023 (restore); `.claude/specs/Calo-AI/Wireframes.md` — WF-006 (paywall/trial context), WF-018 (cancel confirmation modal), with Settings host behavior documented in WF-007; `.claude/specs/Calo-AI/Project_Implementation_Roadmap.md` — Phase 6 `Features/Subscription/` file plan.
- **Key KPIs:** PRD §12 tracks `trial_started`, `subscription_started`, and `subscription_cancelled`; FR-023 requires verified entitlement and unlimited scans only after activation; FR-025 requires fresh RevenueCat status; FR-026 requires idempotent restore and explicit no-purchase/network errors.

## Requirements

### Requirement 1 (REQ-001): Subscription Status Display
**User Story:** As a user viewing Settings, I want to know whether I am free, in trial, Premium, cancelled-pending-expiry, or expired, so that I understand my access and renewal state.
**Source:** FR-025, UC-022, WF-006, WF-018

#### Acceptance Criteria
1. AC-001.1: WHEN the user opens the subscription area from Settings THEN THE SYSTEM SHALL display a status card with one of Free, Trial, Premium, Cancellation pending, or Expired.
2. AC-001.2: WHEN the user has an active or trial entitlement THEN THE SYSTEM SHALL display the plan, localized billing cycle/price, renewal or trial-end date, and current scan access.
3. AC-001.3: WHEN RevenueCat emits an updated `CustomerInfo` THEN THE SYSTEM SHALL reconcile the status card and scan entitlement without requiring the user to restart the app.
4. AC-001.4: IF the status cannot be refreshed THEN THE SYSTEM SHALL show the last known status with a stale indicator and a Refresh action, and SHALL NOT claim Premium from an unverified response.

### Requirement 2 (REQ-002): Trial Entitlement and Seven-Day Badge
**User Story:** As a user who starts a trial from the paywall, I want the app to confirm the trial state and duration, so that I know when Premium begins and ends.
**Source:** FR-023, FR-025, UC-020, UC-022, WF-006

#### Acceptance Criteria
1. AC-002.1: WHEN RevenueCat returns a verified active trial entitlement after the paywall purchase THEN THE SYSTEM SHALL mark the user as Trial/Premium and expose unlimited scans.
2. AC-002.2: WHILE the trial is active THEN THE SYSTEM SHALL show a "7 days free" trial badge and the trial end/renewal date in the paywall confirmation or subscription status view.
3. AC-002.3: WHEN the trial expires without an active renewal THEN THE SYSTEM SHALL map the user to Free/Expired, remove unlimited scan access, and show the upgrade path.
4. AC-002.4: IF `CustomerInfo` is missing, invalid, or inconsistent with the purchase result THEN THE SYSTEM SHALL keep Premium disabled, surface a verification error, and allow a safe refresh or restore retry.

### Requirement 3 (REQ-003): In-App Cancellation Flow
**User Story:** As a current subscriber, I want to cancel without contacting support, while keeping access through the paid period, so that I remain in control of billing.
**Source:** FR-024, FR-025, UC-021, UC-022, WF-018

#### Acceptance Criteria
1. AC-003.1: WHEN a Premium or Trial user taps Cancel subscription THEN THE SYSTEM SHALL present WF-018 with the loss-of-unlimited-scans warning, expiration/renewal date when known, "Continue cancellation", and "Keep subscription" actions.
2. AC-003.2: WHEN the user taps "Keep subscription" THEN THE SYSTEM SHALL dismiss WF-018 without changing the App Store subscription or entitlement.
3. AC-003.3: WHEN the user confirms cancellation THEN THE SYSTEM SHALL present Apple's in-app StoreKit `showManageSubscriptions` UI and SHALL NOT require a support contact or claim cancellation before App Store confirmation.
4. AC-003.4: WHEN StoreKit reports cancellation scheduled at renewal THEN THE SYSTEM SHALL show "Premium expires on the verified expiration date", retain Premium through that date, and update the status to Cancellation pending.
5. AC-003.5: IF the StoreKit manage-subscriptions UI cannot be presented or the result cannot be refreshed THEN THE SYSTEM SHALL show a recoverable error and the system Settings/App Store path, without falsely marking the subscription cancelled.

### Requirement 4 (REQ-004): Restore Purchases
**User Story:** As a returning subscriber on a new device or reinstall, I want to restore my purchase with the same Apple ID, so that I regain Premium without being charged again.
**Source:** FR-026, FR-025, UC-023, UC-022, WF-006, WF-018

#### Acceptance Criteria
1. AC-004.1: WHEN the user taps Restore purchases THEN THE SYSTEM SHALL call the injected `SubscriptionService` restore contract, query RevenueCat/App Store purchase history, and show progress.
2. AC-004.2: IF a matching active or trial subscription is found THEN THE SYSTEM SHALL update `CustomerInfo`, activate the matching Premium/trial state, and show "Premium restored" without a new charge.
3. AC-004.3: IF no matching purchase is found THEN THE SYSTEM SHALL show "No previous purchases" and leave the current entitlement unchanged.
4. AC-004.4: IF restore fails because of network, StoreKit, or Apple ID mismatch THEN THE SYSTEM SHALL show the specific recoverable error and a retry action, and SHALL NOT grant unverified Premium.

### Requirement 5 (REQ-005): Manage Subscription Actions
**User Story:** As a user managing my subscription, I want actions appropriate to my current state, so that I can change, restore, or cancel from one clear place.
**Source:** FR-025, FR-024, FR-026, UC-022, UC-021, UC-023, WF-006, WF-018

#### Acceptance Criteria
1. AC-005.1: WHEN the subscription status card is visible THEN THE SYSTEM SHALL show Manage/change, Restore purchases, and Cancel actions for an active subscription, with Upgrade/Restore actions for a free or expired state.
2. AC-005.2: WHEN the user taps Manage/change plan THEN THE SYSTEM SHALL present Apple's StoreKit `showManageSubscriptions` UI and refresh `CustomerInfo` when the user returns.
3. AC-005.3: WHEN the user taps Restore purchases from any eligible state THEN THE SYSTEM SHALL use the same idempotent restore flow and update the status card from the resulting entitlement.
4. AC-005.4: IF no active subscription exists THEN THE SYSTEM SHALL hide or disable cancellation, explain why it is unavailable, and SHALL NOT present a misleading cancellation confirmation.

## Non-Functional Requirements
- NFR-SM-001: Status freshness — On app launch, Settings entry, and foreground return, the service SHALL request/receive fresh RevenueCat `CustomerInfo` within 2 seconds when online; cached status SHALL be labeled stale when unavailable.
- NFR-SM-002: Listener reliability — A `CustomerInfo` update SHALL reach the ViewModel/status card within 500ms on the main actor and shall not require relaunch.
- NFR-SM-003: Restore safety — Repeated restore requests SHALL be idempotent, create zero new charges, and grant Premium only from a verified entitlement.
- NFR-SM-004: Cancellation safety — The app SHALL never represent cancellation as immediate access removal; pending cancellation SHALL preserve access through the App Store expiration date.
- NFR-SM-005: Accessibility — Status, dates, badges, and actions SHALL support Dynamic Type, VoiceOver labels/value, 44pt minimum controls, and text contrast of at least 4.5:1.
- NFR-SM-006: Privacy and platform — Subscription identifiers, receipts, and `CustomerInfo` SHALL not be logged as raw sensitive data; the feature SHALL support iOS 16+, RevenueCat `purchases-ios`, and StoreKit sandbox verification.
