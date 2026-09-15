# settings-management - Requirements

## Overview
`settings-management` là spec của Phase 8 (Account & Settings). Nó dựng phần Settings (WF-007 settings portion) cho app Calo AI: nhóm preferences (đơn vị metric/imperial, theme system/light/dark), notifications opt-in, privacy/data export & delete (PRD §9 yêu cầu user được export và xoá dữ liệu), app info (version, privacy policy link, terms link), và link sang subscription settings + account profile. Spec lưu local preferences trong `PreferencesStore` (UserDefaults wrapper) và dùng `DataClient.exportUserData()` / `deleteUserData()` cho quyền riêng tư. Spec KHÔNG quản lý subscription (đó là `subscription-settings`) và KHÔNG quản lý profile editing (đó là `account-management`).

## Evidence References
- **Market data from PRD:** Privacy policy phải cho phép user export và xoá toàn bộ dữ liệu (PRD §9) — đây là yêu cầu bắt buộc pháp lý và App Store Health & Fitness data guidelines. Free/premium không phụ thuộc vào notifications (PRD §9) — opt-in, không bật mặc định. Việc cho phép tuỳ chọn đơn vị metric/imperial là điểm UX cơ bản cho app Health/Fitness mass-market (cạnh tranh với MyFitnessPal/YAZIO đều có).
- **Source documents:**
  - `.claude/specs/Calo-AI/Functional_Requirements.md` — FR-018 (height/weight units metric/imperial, BR-018.3); phần preferences chưa có FR riêng trong MVP nên suy ra từ PRD §9 + Use_Cases; privacy/export/delete lấy từ PRD §9
  - `.claude/specs/Calo-AI/Use_Cases.md` — UC-022 (quản lý subscription — phần settings links), UC-023 (restore — settings entry)
  - `.claude/specs/Calo-AI/Wireframes.md` — WF-014 (Settings — phần settings list), WF-015 (Share Progress — settings entry)
  - `.claude/specs/Calo-AI/PRD.md` §9 (privacy/export/delete, opt-in notifications, units context)
- **Key KPIs / measurable targets:** Preferences persistence <100ms (UserDefaults write); export job returns download URL <10s; delete confirmation hard to bypass (typed-name confirm).

## Requirements

### Requirement 1 (REQ-001): Preferences (Units & Theme)
**User Story:** As a user, I want to choose my preferred unit system (metric/imperial) and app theme (system/light/dark), so that the app matches my locale and visual preference.
**Source:** FR-018 (BR-018.3 unit conversion); PRD §9 (units context); UC-022 (settings portion); WF-014

#### Acceptance Criteria
1. AC-001.1: WHEN the user opens Settings THEN THE SYSTEM SHALL display two preference rows: "Units" (metric/imperial segmented control) and "Theme" (system/light/dark segmented control), each reflecting the value currently persisted in `PreferencesStore`.
2. AC-001.2: WHEN the user changes Units or Theme THEN THE SYSTEM SHALL persist the new value via `PreferencesStore.set(_:forKey:)` within 100ms and apply the change immediately (theme switches the color scheme; units toggle the displayed unit suffix on profile/height/weight fields in `account-management`).
3. AC-001.3: WHEN the user reopens the app THEN THE SYSTEM SHALL restore the persisted Units and Theme values on next launch.
4. AC-001.4: IF `PreferencesStore` write fails (e.g., disk full) THEN THE SYSTEM SHALL surface a recoverable error via `ErrorHandler` and revert the UI to the previously persisted value.

### Requirement 2 (REQ-002): Notifications Opt-In
**User Story:** As a user, I want to opt in to notifications (daily meal-log reminder), so that I am not spammed by default and only get reminders if I want them.
**Source:** PRD §9 (opt-in, not default-on, max 1/day); UC-022; WF-014

#### Acceptance Criteria
1. AC-002.1: WHEN the user opens Settings THEN THE SYSTEM SHALL display a "Notifications" row with a toggle, defaulting to OFF (opt-in), and a caption "Daily meal-log reminder" (PRD §9 ≤1/day).
2. AC-002.2: WHEN the user flips the toggle to ON THEN THE SYSTEM SHALL request notification authorization via `UNUserNotificationCenter.requestAuthorization(options: [.alert, .badge, .sound])` and SHALL only persist `notificationsEnabled = true` if authorization is granted.
3. AC-002.3: WHEN the user flips the toggle to OFF THEN THE SYSTEM SHALL persist `notificationsEnabled = false`, disable scheduled local notifications, and SHALL NOT call `UNUserNotificationCenter.requestAuthorization`.
4. AC-002.4: IF the user denies system authorization THEN THE SYSTEM SHALL keep `notificationsEnabled = false`, show a one-line hint "Enable in iOS Settings > Calo AI > Notifications" with a deep-link button, and SHALL NOT retry the prompt automatically.

### Requirement 3 (REQ-003): Privacy — Export & Delete User Data
**User Story:** As a user, I want to export all my data and delete my account/data, so that I control my personal information per privacy law.
**Source:** PRD §9 (required: Privacy Policy + user can export and delete all data + clear consent); UC-022; WF-014

#### Acceptance Criteria
1. AC-003.1: WHEN the user taps "Export my data" THEN THE SYSTEM SHALL call `DataClient.exportUserData()` and present a system share sheet (`UIActivityViewController`) with the generated JSON file containing the user's profile, meal logs, and preferences; on success, show a toast "Export ready".
2. AC-003.2: WHEN the user taps "Delete my data" THEN THE SYSTEM SHALL show a destructive confirmation modal (WF-018 style) with copy "Delete all your data? This permanently removes your profile, logs, and preferences. This cannot be undone." and require the user to type "DELETE" to enable the destructive button.
3. AC-003.3: WHEN the user confirms with the typed keyword AND taps "Delete" THEN THE SYSTEM SHALL call `DataClient.deleteUserData()` (Supabase RPC), clear `PreferencesStore`, clear `OfflineSyncService` user cache, and sign the user out via `AuthService.logout()`.
4. AC-003.4: IF `exportUserData()` or `deleteUserData()` fails THEN THE SYSTEM SHALL surface the error via `ErrorHandler` and SHALL NOT mark the operation as complete.
5. AC-003.5: AFTER successful delete THEN THE SYSTEM SHALL navigate the user to the Sign in screen; on subsequent sign-in (even with the same Apple ID), the previous data SHALL NOT be present.

### Requirement 4 (REQ-004): App Info & Links
**User Story:** As a user, I want to see the app version, privacy policy, and terms of service from Settings, so that I can review what the app does with my data.
**Source:** PRD §9 (Privacy Policy required); UC-022; WF-014

#### Acceptance Criteria
1. AC-004.1: WHEN the user opens Settings THEN THE SYSTEM SHALL display an "About" section with three rows: "App version" (read-only `CFBundleShortVersionString` + `CFBundleVersion`), "Privacy policy" (opens `https://caloai.app/privacy` in SFSafariViewController), and "Terms of service" (opens `https://caloai.app/terms` in SFSafariViewController).
2. AC-004.2: WHEN the user taps "Privacy policy" or "Terms of service" THEN THE SYSTEM SHALL open the URL in an in-app `SFSafariViewController` (no external app switch) so the user can return to Settings via the standard close button.
3. AC-004.3: IF the URL fails to load THEN THE SYSTEM SHALL show a recoverable error via `ErrorHandler` with a Retry button.
4. AC-004.4: WHEN the user taps "Account profile" or "Subscription" links THEN THE SYSTEM SHALL navigate to the corresponding section (`account-management` for profile; `subscription-settings` for subscription) within the Settings tab via `NavigationStack` push.

## Non-Functional Requirements
- NFR-SM-001: Preferences persistence — preference writes SHALL complete <100ms (UserDefaults sync write).
- NFR-SM-002: Export latency — `DataClient.exportUserData()` SHALL return a downloadable file URL within 10s on a healthy network; longer surfaces `ErrorHandler` recoverable banner.
- NFR-SM-003: Delete guardrail — destructive "Delete" button SHALL require typed keyword ("DELETE") to enable, matching WF-018 destructive pattern; no single-tap delete.
- NFR-SM-004: Auth gating — Settings SHALL be reachable only when `AuthService.sessionValid() == true`; otherwise route to Sign in (same NFR-004 used by account-management).
- NFR-SM-005: Notifications compliance — Notifications SHALL be opt-in (default OFF); `requestAuthorization` SHALL NOT be called on app launch or any silent event; max one prompt per user-decided toggle ON (PRD §9).
- NFR-SM-006: Privacy UX — Export and Delete actions SHALL be in a dedicated "Privacy" section, visually separated from low-stakes preferences, with destructive styling on Delete.
- NFR-SM-007: Accessibility — All Settings rows SHALL meet WCAG 2.1 AA (NFR-009): tap targets ≥44×44pt, VoiceOver labels, Dynamic Type; toggles expose state via `accessibilityValue`.
