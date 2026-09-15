# paywall-display - Requirements

## Overview
`paywall-display` implements WF-006, the transparent Premium offer shown after the camera-capture scan-limit handoff (FR-010) or from Settings. It presents weekly, monthly, and annual pricing cards, the 7-day trial badge, benefits, plan selection, and the primary trial CTA. Trigger/quota enforcement remains owned by `camera-capture`; this spec owns only paywall presentation, selection, and the UI handoff into the subscription flow.

Pricing follows PRD §11: Weekly $2.99, Monthly $9.99, and Annual $39.99–$49.99 (localized StoreKit price may be shown), with a clearly disclosed 7-day trial and renewal terms. The experience must reinforce Calo AI's trust positioning and must not use dark patterns or violate App Store Guidelines 3.1.2c / 5.6.

## Evidence References
- **Market data from PRD:** PRD §1 positions Calo AI around transparent billing after Cal AI's paywall enforcement; PRD §1 product principles require visible price/cycle before trial, easy in-app cancellation, and no dark patterns. PRD §11 defines the freemium/Premium model, 7-day trial, and recommended weekly/monthly/annual pricing.
- **Source documents:** `.claude/specs/Calo-AI/Functional_Requirements.md` — FR-010 (paywall trigger handoff/display boundary), FR-021 (Premium trial offer), FR-022 (initiate trial); `.claude/specs/Calo-AI/Use_Cases.md` — UC-019 (view paywall), UC-020 (start 7-day trial); `.claude/specs/Calo-AI/Wireframes.md` — WF-006 (paywall); `.claude/specs/Calo-AI/Project_Implementation_Roadmap.md` — Phase 6 mapping and `Features/Paywall/` file plan.
- **Key KPIs:** PRD §12 tracks `paywall_viewed` and `trial_started`; PRD §2 targets 3–5% free-to-paid conversion without sacrificing transparent billing; FR-022 requires a 7-day trial, validated entitlement, and unlimited scans only after activation.

## Requirements

### Requirement 1 (REQ-001): Paywall Entry and Offer Display
**User Story:** As a free-tier user who reaches the paywall from scan limits or Settings, I want to see the complete Premium offer immediately, so that I can make an informed decision without searching for prices or terms.
**Source:** FR-010, FR-021, UC-019, WF-006

#### Acceptance Criteria
1. AC-001.1: WHEN the paywall is opened from the camera-capture handoff or Settings THEN THE SYSTEM SHALL present WF-006 without re-evaluating scan quota or changing subscription state.
2. AC-001.2: WHEN paywall entry is visible THEN THE SYSTEM SHALL make the price and billing cycle visible from paywall entry for weekly ($2.99/week), monthly ($9.99/month), and annual ($39.99–$49.99/year) offers, using the localized StoreKit/RevenueCat values when available.
3. AC-001.3: WHEN the offer is displayed THEN THE SYSTEM SHALL show the "7 days free" trial badge, the unlimited-scan benefit, and the remaining benefits before the trial CTA.
4. AC-001.4: IF RevenueCat offerings or pricing cannot be loaded THEN THE SYSTEM SHALL show a recoverable "Upgrade to Premium" state with retry/close actions and SHALL NOT show a blank paywall, invent a price, or crash.

### Requirement 2 (REQ-002): Plan Selection
**User Story:** As a user comparing Premium plans, I want to select exactly one billing cycle and see its complete terms, so that the CTA starts the plan I intentionally chose.
**Source:** FR-021, FR-022, UC-019, UC-020, WF-006

#### Acceptance Criteria
1. AC-002.1: WHEN the user taps a weekly, monthly, or annual pricing card THEN THE SYSTEM SHALL mark only that card as selected and expose the selected product to the trial action.
2. AC-002.2: WHILE a plan is selected THEN THE SYSTEM SHALL display that plan's localized price, billing cycle, trial length, and annual savings label when supplied by the offering.
3. AC-002.3: WHEN the user changes the selected plan THEN THE SYSTEM SHALL update the selected product and CTA terms before any purchase request is sent.
4. AC-002.4: IF a plan is unavailable, malformed, or missing a price/cycle THEN THE SYSTEM SHALL disable that plan's selection and show a specific availability message without starting a purchase.

### Requirement 3 (REQ-003): Start Seven-Day Trial Handoff
**User Story:** As an eligible user, I want the Start 7-day trial action to open Apple's purchase confirmation for my selected plan, so that I can activate Premium through the approved subscription flow.
**Source:** FR-022, FR-021, UC-020, WF-006

#### Acceptance Criteria
1. AC-003.1: WHEN an eligible user taps "Start 7-day trial" with a valid selected plan THEN THE SYSTEM SHALL call the injected `SubscriptionService` purchase contract and cause the StoreKit payment sheet to open through RevenueCat.
2. AC-003.2: WHEN StoreKit confirms the purchase and RevenueCat reports the Premium entitlement active THEN THE SYSTEM SHALL dismiss the paywall, show "Premium activated", and expose unlimited scans to the app.
3. AC-003.3: IF the user cancels or dismisses the StoreKit payment sheet THEN THE SYSTEM SHALL keep the user on the paywall with no charge, no entitlement activation, and a retryable CTA.
4. AC-003.4: IF receipt validation or network verification fails THEN THE SYSTEM SHALL show "Could not activate trial", keep Premium disabled until verification succeeds, and allow retry or later recovery without duplicating the purchase.

### Requirement 4 (REQ-004): Billing Transparency and Compliance
**User Story:** As a cautious subscriber, I want pricing, renewal, cancellation, and dismissal choices stated plainly, so that I can start a trial without surprise charges or manipulative interaction patterns.
**Source:** FR-021, FR-022, UC-019, UC-020, WF-006, PRD §1, PRD §11

#### Acceptance Criteria
1. AC-004.1: WHEN the user is about to start the trial THEN THE SYSTEM SHALL display the selected price plus billing cycle, the 7-day trial length, the post-trial renewal terms, and the in-app cancellation path BEFORE trial start.
2. AC-004.2: WHEN the paywall is shown THEN THE SYSTEM SHALL use no dark patterns: the price/cycle and trial terms SHALL remain visible, the dismiss/"Remind me later" action SHALL be available, and no deceptive countdown, hidden fee, or obstructive navigation SHALL be used.
3. AC-004.3: WHEN the user taps close, back, or "Remind me later" THEN THE SYSTEM SHALL dismiss the paywall without starting a purchase, changing entitlement, or removing access to the free tier.
4. AC-004.4: IF a required price, cycle, renewal term, or cancellation disclosure is unavailable THEN THE SYSTEM SHALL disable the trial CTA and show an explicit unavailable state rather than hiding the missing information.

## Non-Functional Requirements
- NFR-PW-001: Offer loading — With cached offerings, the complete paywall SHALL render within 500ms; with a network fetch, it SHALL show a loading state within 200ms and resolve within 2 seconds or expose the error state.
- NFR-PW-002: Price integrity — 100% of enabled pricing cards SHALL use the RevenueCat/StoreKit localized display price and billing period; the UI SHALL never synthesize or silently substitute a price.
- NFR-PW-003: Accessibility — All interactive controls SHALL be at least 44pt, support Dynamic Type, provide VoiceOver labels/value for plan, price, trial, and dismissal, and maintain text contrast of at least 4.5:1.
- NFR-PW-004: Purchase safety — No purchase call SHALL occur without an explicit CTA tap and a valid selected product; entitlement activation SHALL require a verified RevenueCat `CustomerInfo` result.
- NFR-PW-005: Platform/compliance — The feature SHALL support iOS 16+, use Apple's in-app purchase flow, and pass StoreKit sandbox checks for Guideline 3.1.2c / 5.6 disclosures before release.
