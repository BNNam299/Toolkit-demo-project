# authentication - Requirements

## Overview
`authentication` là spec đầu tiên của Phase 7 (Onboarding & Auth). Nó dựng màn hình Splash (WF-001) với luồng **Sign in with Apple**: người dùng mới → Sign in → onboarding (`onboarding-form`); người dùng quay lại → phục hồi session từ Keychain → RootView; người dùng đăng xuất từ Settings (WF-007) → re-auth. Spec này wires UI lên `AuthServicing` / `AppleAuthService` đã define trong `shared-foundations`; `ASAuthorizationAppleIDProvider` là framework Apple — không cần SPM. KHÔNG bao gồm camera permission (WF-009 dialog thuộc `camera-capture`), onboarding form (`onboarding-form`), paywall (`paywall-display`), hay subscription management.

## Evidence References
- **Market data from PRD:** Sign in with Apple là yêu cầu bắt buộc của App Store (Guideline 5.1.1) khi app cung cấp third-party / social login, đồng thời giảm friction onboarding so với email/password (PRD §9). Tốc độ first-launch-to-app là KPI chính (NFR-001 <2s) — phục hồi session nhanh từ Keychain tránh nhân lại friction đăng nhập mỗi lần mở app.
- **Source documents:**
  - `.claude/specs/Calo-AI/Functional_Requirements.md` — NFR-004 (User Authentication: Apple ID sign-in required; no unauthenticated access), NFR-006 (Data encryption at-rest for tokens via Keychain)
  - `.claude/specs/Calo-AI/Use_Cases.md` — UC-001 (Mở Camera — first-launch variant: Authentication entry)
  - `.claude/specs/Calo-AI/Wireframes.md` — WF-001 (Splash), WF-007 (Settings → sign-out trigger), WF-009 (Permission re-prompt / re-auth gate)
  - `.claude/specs/Calo-AI/shared-foundations/design.md` — `AuthServicing` protocol + `AppleAuthService` (Sign in with Apple + Keychain token storage)
- **Key KPIs / measurable targets:** Splash-to-ready ≤2s cho returning user với valid token (NFR-001); Sign in with Apple sheet presented ≤1s after Splash trên first-launch (UX); 100% data access chỉ khi `sessionValid()==true` (NFR-004).

## Requirements

### Requirement 1 (REQ-001): First-Launch Sign In with Apple
**User Story:** As a new user, I want to sign in with Apple once at first launch and land in onboarding, so that I can start setting up my profile with a single tap instead of filling out forms.
**Source:** NFR-004, UC-001 (first-launch variant), WF-001, WF-009

#### Acceptance Criteria
1. AC-001.1: WHEN the app launches for the first time (no token in Keychain) THEN THE SYSTEM SHALL display Splash (WF-001) for ≤2 seconds and present the Sign in with Apple sheet (`ASAuthorizationAppleIDProvider`).
2. AC-001.2: WHEN the user completes Sign in with Apple successfully THEN THE SYSTEM SHALL persist the resulting identity token + user id in Keychain and route to the onboarding flow (`onboarding-form`, WF-008).
3. AC-001.3: IF the user cancels the Sign in with Apple sheet THEN THE SYSTEM SHALL keep the user on the auth screen with a clear "Sign in with Apple" button and SHALL NOT proceed to onboarding or RootView.
4. AC-001.4: IF Sign in with Apple fails (network or credential error) THEN THE SYSTEM SHALL surface a recoverable error via `ErrorHandler` with a "Try again" action and SHALL NOT silently succeed.

### Requirement 2 (REQ-002): Session Restoration on Launch
**User Story:** As a returning user, I want to land directly in the app without re-authenticating each time, so that I can keep logging meals with zero friction.
**Source:** NFR-004, NFR-006, UC-001 (returning variant), WF-001

#### Acceptance Criteria
1. AC-002.1: WHEN the app launches and a valid identity token exists in Keychain THEN THE SYSTEM SHALL restore the `User` from the token claims and route to RootView (Camera tab) without prompting for sign-in.
2. AC-002.2: WHEN the Keychain token is expired THEN THE SYSTEM SHALL route to the Sign in with Apple flow (REQ-001) and SHALL NOT block the app on a stale session.
3. AC-002.3: IF the Keychain token is missing or corrupt (cannot be decoded) THEN THE SYSTEM SHALL treat the user as signed-out and present the Sign in with Apple sheet.
4. AC-002.4: WHEN the restored `User.onboardingComplete==true` THEN THE SYSTEM SHALL bypass onboarding and route to RootView; IF `onboardingComplete==false` THEN THE SYSTEM SHALL route to `onboarding-form` (WF-008).

### Requirement 3 (REQ-003): Sign Out & Re-Authentication
**User Story:** As a user, I want to sign out from Settings and be able to sign back in with the same Apple ID, so that I can protect my data on a shared device or switch accounts safely.
**Source:** NFR-004, NFR-006, UC-001 (re-auth variant), WF-007, WF-009

#### Acceptance Criteria
1. AC-003.1: WHEN the user taps "Sign out" in Settings (WF-007) THEN THE SYSTEM SHALL present a confirmation modal (SignOutConfirmModal) before clearing the session and SHALL NOT clear the session on the first tap.
2. AC-003.2: WHEN the user confirms sign-out THEN THE SYSTEM SHALL clear the Keychain token and the in-memory `User`, then route back to the Splash auth screen.
3. AC-003.3: WHEN the user re-authenticates with the same Apple ID after sign-out THEN THE SYSTEM SHALL restore the same `User.id` (no duplicate account creation); a different Apple ID SHALL yield a fresh `User.id`.
4. AC-003.4: IF the Keychain clear fails (e.g., secure enclave unavailable) THEN THE SYSTEM SHALL surface a recoverable error via `ErrorHandler` and offer a "Retry" action; the user SHALL NOT be left in an inconsistent signed-in state where the UI says signed-out but Keychain still holds a token.

## Non-Functional Requirements
- NFR-AUTH-001: Splash-to-ready latency — The system SHALL complete splash + session check + route decision within 2 seconds on iPhone 12+ (NFR-001). Measured: cold-start app launch to first frame of chosen route.
- NFR-AUTH-002: Sign in with Apple latency — The Sign in with Apple sheet SHALL be presented within 1 second after Splash dismissal on first-launch. Measured: splash fade-complete → sheet first frame.
- NFR-AUTH-003: Token storage — The identity token SHALL be stored in Keychain with `kSecAttrAccessibleAfterFirstUnlockThisDeviceOnly`; no token bytes SHALL appear in UserDefaults, plist, console logs, or analytics (NFR-006).
- NFR-AUTH-004: Unauthenticated access — All `DataClient` calls SHALL fail-fast with `AppError.unauthenticated` when `sessionValid()==false`; no meal log or profile read SHALL succeed anonymously (NFR-004).
- NFR-AUTH-005: Cancellation safety — When Sign in with Apple is cancelled, no partial token SHALL be written to Keychain; the prior session (if any) SHALL remain intact (NFR-006).