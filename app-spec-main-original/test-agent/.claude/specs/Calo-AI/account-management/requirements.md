# account-management - Requirements

## Overview
`account-management` là spec của Phase 8 (Account & Settings). Nó dựng màn hình Account (WF-007 Profile view) với hai modal: Edit Profile (WF-016) cho phép chỉnh sửa thông tin cơ bản (height, weight, activity level) và Change Goal (WF-017) cho phép chỉnh mục tiêu calo hằng ngày, cùng nút Sign Out để clear session. Spec đọc/ghi `User` qua `UserRepository` (DataClient + Supabase RLS), bám sát validation rules BR-018/VR-018/BR-020/VR-020. Spec KHÔNG quản lý subscription status (đó là `subscription-settings`), KHÔNG bao gồm preferences/privacy (đó là `settings-management`), và KHÔNG bao gồm onboarding lần đầu (đó là `onboarding-form`).

## Evidence References
- **Market data from PRD:** Privacy policy yêu cầu user phải được quản lý và xoá dữ liệu của mình (PRD §9) — account screen là entry point cho cả Edit Profile lẫn Sign Out, do đó phải có khả năng đọc/ghi `User` an toàn. Việc cho phép chỉnh mục tiêu calo mà không cần re-onboarding giữ chân người dùng khi cân nặng/mục tiêu thay đổi — đây là điểm khác biệt so với Cal AI (đã từng bị phàn nàn vì không thể chỉnh goal).
- **Source documents:**
  - `.claude/specs/Calo-AI/Functional_Requirements.md` — FR-018 (profile fields + VR-018.1/2/3 + BR-018.1/2/3), FR-020 (goal range 1000–3500 + VR-020.1 + BR-020.3); quản lý subscription được tách sang FR-024/025 (thuộc `subscription-settings`)
  - `.claude/specs/Calo-AI/Use_Cases.md` — UC-021 (huỷ sub), UC-022 (quản lý sub/profile), UC-023 (restore) — phần profile-only
  - `.claude/specs/Calo-AI/Wireframes.md` — WF-003 (Profile view), WF-016 (Edit Profile modal), WF-017 (Change Goal modal)
  - `.claude/specs/Calo-AI/PRD.md` §9 (privacy/export — Sign Out clear session, account là entry point)
- **Key KPIs / measurable targets:** Edit Profile save <2s (mirror BR-002.3 image-preview budget để cảm giác "nhanh"); Change Goal validation inline tức thì; Sign Out clear session <1s.

## Requirements

### Requirement 1 (REQ-001): View Profile
**User Story:** As a user, I want to see my profile (name, height, weight, activity level, daily calorie goal) when I open the Account screen, so that I can review what Calo AI knows about me.
**Source:** FR-018, FR-020; UC-022 (profile portion); WF-003

#### Acceptance Criteria
1. AC-001.1: WHEN the user opens the Account tab THEN THE SYSTEM SHALL display the profile card with name, height (cm), weight (kg), activity level, and current daily calorie goal sourced from `AuthService.getUser()`.
2. AC-001.2: WHILE the profile is loading THEN THE SYSTEM SHALL show a loading state (skeleton/spinner) and SHALL NOT show stale empty fields.
3. AC-001.3: IF the profile fails to load (network/server error) THEN THE SYSTEM SHALL show a recoverable error via `ErrorHandler` with a Retry button and SHALL keep the previous profile data if present.
4. AC-001.4: IF the user is not signed in (`AuthService.sessionValid() == false`) THEN THE SYSTEM SHALL route to the Sign in screen instead of showing the Account screen.

### Requirement 2 (REQ-002): Edit Profile (Height, Weight, Activity Level)
**User Story:** As a user, I want to edit my basic profile info (height, weight, activity level) from a modal, so that my calorie target stays accurate as my body or habits change.
**Source:** FR-018 (BR-018.1/2/3, VR-018.1/2/3); UC-022; WF-016

#### Acceptance Criteria
1. AC-002.1: WHEN the user taps "Edit profile" on the Account screen THEN THE SYSTEM SHALL open the Edit Profile modal (WF-016) pre-filled with the current `User` values.
2. AC-002.2: WHEN the user changes height, weight, or activity level AND taps Save THEN THE SYSTEM SHALL validate against the ranges height∈[120,220] cm (VR-018.1) and weight∈[30,300] kg (VR-018.2), and SHALL require activity level selected (VR-018.3).
3. AC-002.3: WHEN validation passes THEN THE SYSTEM SHALL persist the update via `UserRepository.update()` (DataClient → Supabase, RLS-scoped) within 2 seconds and SHALL close the modal, returning to a refreshed Account screen.
4. AC-002.4: IF validation fails (out-of-range or missing activity) THEN THE SYSTEM SHALL show an inline message ("Height must be between 120 and 220 cm" / "Weight must be between 30 and 300 kg" / "Please select activity level") and SHALL NOT close the modal or call `update()`.
5. AC-002.5: IF the save call fails THEN THE SYSTEM SHALL surface the error via `ErrorHandler`, keep the modal open, and preserve the user's typed values for retry.

### Requirement 3 (REQ-003): Change Daily Calorie Goal
**User Story:** As a user, I want to change my daily calorie goal directly from the Account screen, so that I can adjust my plan without re-running onboarding.
**Source:** FR-020 (BR-020.3, VR-020.1); UC-022; WF-017

#### Acceptance Criteria
1. AC-003.1: WHEN the user taps "Change goal" on the Account screen THEN THE SYSTEM SHALL open the Change Goal modal (WF-017) showing the current `User.calorieTarget` and the Mifflin-St Jeor formula explanation.
2. AC-003.2: WHEN the user enters a new goal value AND taps Update THEN THE SYSTEM SHALL validate the value is in the safe range 1000–3500 kcal (BR-020.3, VR-020.1) and SHALL reject zero, negative, non-integer, or out-of-range values.
3. AC-003.3: WHEN the new goal is valid THEN THE SYSTEM SHALL persist it via `UserRepository.update()` and SHALL refresh the Diary progress bar (`FR-014` consumer) within the next view appearance.
4. AC-003.4: IF the entered goal is outside [1000, 3500] THEN THE SYSTEM SHALL show "Goal must be between 1000 and 3500 kcal" inline and SHALL NOT persist.
5. AC-003.5: IF the update fails THEN THE SYSTEM SHALL surface the error via `ErrorHandler` and SHALL keep the modal open with the user's input preserved for retry.

### Requirement 4 (REQ-004): Sign Out
**User Story:** As a user, I want to sign out from the Account screen, so that I can clear my session and stop syncing data to my account.
**Source:** PRD §9 (privacy — user controls data); UC-022 (sign-out portion); WF-007

#### Acceptance Criteria
1. AC-004.1: WHEN the user taps "Sign out" on the Account screen THEN THE SYSTEM SHALL show a confirmation: "Sign out? You'll need to sign in again with Apple." with Cancel/Sign out buttons.
2. AC-004.2: WHEN the user confirms sign out THEN THE SYSTEM SHALL call `AuthService.logout()` to clear the Keychain JWT and reset `AppEnvironment` user state, and SHALL navigate to the Sign in screen within 1 second.
3. AC-004.3: IF the user taps Cancel THEN THE SYSTEM SHALL dismiss the confirmation and leave the Account screen unchanged.
4. AC-004.4: IF `AuthService.logout()` fails THEN THE SYSTEM SHALL surface the error via `ErrorHandler`, keep the user signed in, and SHALL NOT navigate away.
5. AC-004.5: AFTER sign out completes THEN THE SYSTEM SHALL clear any locally cached user-scoped data from `OfflineSyncService` so a subsequent signed-in user on the same device cannot read it.

## Non-Functional Requirements
- NFR-AM-001: Profile read latency — Account screen shall render the profile card <1s after `AuthService.getUser()` returns on a warm cache (NFR-001 budget for screen-to-content render).
- NFR-AM-002: Profile edit save latency — Edit Profile / Change Goal save round-trip shall complete <2s on a healthy network; longer surfaces `ErrorHandler` recoverable banner.
- NFR-AM-003: Sign-out latency — Sign-out flow shall complete (logout + navigation) <1s.
- NFR-AM-004: Validation strictness — All `User` field validations SHALL match `User.validate()` rules from `shared-foundations` (height∈[120,220], weight∈[30,300], goal∈[1000,3500], activityLevel required); the spec MUST NOT introduce duplicate or divergent validation.
- NFR-AM-005: Auth gating — Account screen SHALL be reachable only when `AuthService.sessionValid() == true`; otherwise route to Sign in (NFR-004).
- NFR-AM-006: Session/data hygiene — Sign out SHALL clear Keychain token (AuthService) and user-scoped cache (OfflineSyncService); subsequent reads SHALL require fresh sign-in.
- NFR-AM-007: Accessibility — All Account-screen actions SHALL meet WCAG 2.1 AA (NFR-009): tap targets ≥44×44pt, VoiceOver labels on Edit/Save/Cancel/Sign out, Dynamic Type support.
