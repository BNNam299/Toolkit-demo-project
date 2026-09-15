# onboarding-form - Requirements

## Overview
`onboarding-form` là spec thứ hai của Phase 7 (Onboarding & Auth). Nó dựng màn hình Onboarding 3 bước (WF-008): **Bước 1** thu thập chiều cao / cân nặng / giới tính / tuổi + mục tiêu cân nặng (giảm / duy trì / tăng) + tốc độ; **Bước 2** chọn mức hoạt động (Sedentary / Light / Moderate / Very Active); **Bước 3** hiển thị mục tiêu calo hàng ngày được tính bằng công thức **Mifflin-St Jeor** — BMR theo giới tính × multiplier theo hoạt động ± adjustment theo mục tiêu — sau đó lưu vào `User` model + persist qua `DataClient`. Spec dùng `User` model từ `shared-foundations`, tái sử dụng `CaloButton` / `ErrorHandler`, và nhận `User` đã có id/email/name từ `authentication` (sign-in thành công). KHÔNG bao gồm Splash / Sign in (`authentication`), Camera (`camera-capture`), Diary (`diary-logging`).

## Evidence References
- **Market data from PRD:** Mifflin-St Jeor là công thức BMR được chấp nhận rộng rãi nhất (PRD §9 — chính xác hơn Harris-Benedict ~5% cho non-obese), giúp cá nhân hoá mục tiêu calo — yếu tố then chốt để onboarding completion >80% (PRD §12). UX multi-step giữ friction thấp (PRD §11 — MyFitnessPal onboarding 7 bước gây bất mãn). Free-tier 3-scan/ngày yêu cầu `calorieTarget` chính xác để progress bar meaningful.
- **Source documents:**
  - `.claude/specs/Calo-AI/Functional_Requirements.md` — FR-018 (profile + BR-018.1 height 120–220, BR-018.2 weight 30–300, BR-018.3 unit conversion, VR-018.1/2/3 validation, ERR-018.1/2/3), FR-019 (activity level + BR-019.1 multipliers 1.375/1.55/1.725/1.9, VR-019.1, ERR-019.1), FR-020 (TDEE display + BR-020.1 Mifflin-St Jeor, BR-020.2 ±500 kcal deficit/surplus = 0.5 lb/week, BR-020.3 goal range 1000–3500, VR-020.1, ERR-020.1)
  - `.claude/specs/Calo-AI/Use_Cases.md` — UC-016 (Nhập thông tin cơ bản), UC-017 (Chọn mức hoạt động), UC-018 (Xem mục tiêu calo)
  - `.claude/specs/Calo-AI/Wireframes.md` — WF-008 (Onboarding multi-step form, 3 steps)
  - `.claude/specs/Calo-AI/shared-foundations/design.md` — `User` model (`height` 120–220 cm, `weight` 30–300 kg, `goal` enum, `activityLevel` enum, `calorieTarget`, `onboardingComplete`); `DataClienting` (CRUD persistence)
- **Key KPIs / measurable targets:** Onboarding completion rate ≥80% (PRD §12); step transition ≤200ms; Mifflin-St Jeor computation <100ms; goal always within safety bounds [1000, 3500] kcal (BR-020.3).

## Requirements

### Requirement 1 (REQ-001): Basic Info Collection (Height / Weight / Sex / Age) + Weight Goal
**User Story:** As a new user, I want to enter my height, weight, sex, age, and weight goal (lose / maintain / gain with rate), so that the app can personalize my daily calorie goal.
**Source:** FR-018, FR-020 (goal adjustment), UC-016, WF-008 (step 1)

#### Acceptance Criteria
1. AC-001.1: WHEN the user reaches step 1 THEN THE SYSTEM SHALL display numeric input fields for height (cm, default unit), weight (kg, default unit), age (years), sex (male / female / other), and a goal selector with three options (Lose / Maintain / Gain) plus a target-rate stepper (−1, −0.5, 0, +0.5, +1 lb/week) that adjusts per the chosen goal.
2. AC-001.2: WHEN the user submits step 1 with valid inputs (height 100–250 cm, weight 30–300 kg, age 13–100, sex selected, goal selected, rate within ±1 lb/week) THEN THE SYSTEM SHALL enable "Next", persist the inputs to the in-progress `UserProfileDraft`, and allow advancing to step 2.
3. AC-001.3: IF any input is out of range THEN THE SYSTEM SHALL display an inline error message (e.g., "Height must be between 100 and 250 cm", "Weight must be between 30 and 300 kg") and block the "Next" button.
4. AC-001.4: IF any required field is missing (empty height/weight/age, no sex, no goal) THEN THE SYSTEM SHALL display "Please complete all fields" and block the "Next" button.

### Requirement 2 (REQ-002): Activity Level Selection
**User Story:** As a new user, I want to pick how active I am, so that my calorie goal reflects my real energy expenditure.
**Source:** FR-019, UC-017, WF-008 (step 2)

#### Acceptance Criteria
1. AC-002.1: WHEN the user reaches step 2 THEN THE SYSTEM SHALL display four radio options — Sedentary ("Little or no exercise"), Light ("Exercise 1–3 days/week"), Moderate ("Exercise 3–5 days/week"), Very Active ("Exercise 6–7 days/week") — each with its description, exactly one selectable at a time.
2. AC-002.2: WHEN the user selects an activity level THEN THE SYSTEM SHALL enable "Next" and store the selection on the in-progress `UserProfileDraft`, mapped internally to the TDEE multiplier (Sedentary 1.375, Light 1.55, Moderate 1.725, Very Active 1.9) per BR-019.1.
3. AC-002.3: WHEN the user taps "Back" on step 2 THEN THE SYSTEM SHALL return to step 1 with previously-entered values pre-filled and unchanged; advancing again restores step 2's prior selection if any.
4. AC-002.4: IF the user reaches step 2 without selecting THEN THE SYSTEM SHALL keep "Next" disabled and show "Please select activity level".

### Requirement 3 (REQ-003): Weight Goal Selection (Lose / Maintain / Gain) & Rate Mapping
**User Story:** As a new user, I want my chosen weight-goal direction and rate translated to a calorie adjustment, so that my goal reflects how fast I want to change weight.
**Source:** FR-018 (goal enum), FR-020 (BR-020.2 deficit/surplus), UC-016, WF-008 (step 1)

#### Acceptance Criteria
1. AC-003.1: WHEN the user selects "Lose" THEN THE SYSTEM SHALL show a rate stepper allowing −0.25 to −1 lb/week in 0.25 increments and map each 0.5 lb/week to a 500 kcal daily deficit (e.g., −1 lb/week → −1000 kcal/day), clamped to safe bounds.
2. AC-003.2: WHEN the user selects "Maintain" THEN THE SYSTEM SHALL hide the rate stepper and set the daily calorie adjustment to 0 kcal.
3. AC-003.3: WHEN the user selects "Gain" THEN THE SYSTEM SHALL show a rate stepper allowing +0.25 to +1 lb/week in 0.25 increments and map each 0.5 lb/week to a 500 kcal daily surplus (e.g., +1 lb/week → +1000 kcal/day), clamped to safe bounds.
4. AC-003.4: IF the user switches between Lose / Maintain / Gain THEN THE SYSTEM SHALL recompute the daily adjustment immediately and keep `UserProfileDraft.goal` consistent with the visible selection; switching to/from Maintain SHALL show/hide the rate stepper accordingly.

### Requirement 4 (REQ-004): TDEE Computation (Mifflin-St Jeor) & Goal Display
**User Story:** As a new user, I want to see my personalized daily calorie goal computed transparently from my profile, so that I understand and trust the number before I start logging.
**Source:** FR-020, UC-018, WF-008 (step 3)

#### Acceptance Criteria
1. AC-004.1: WHEN step 3 is reached THEN THE SYSTEM SHALL compute BMR using Mifflin-St Jeor: `BMR = 10·weight(kg) + 6.25·height(cm) − 5·age(y) + s` where `s = +5` (male), `+1` (other), or `−161` (female) per BR-020.1.
2. AC-004.2: WHEN BMR is computed THEN THE SYSTEM SHALL compute TDEE = BMR × activity_multiplier (Sedentary 1.375, Light 1.55, Moderate 1.725, Very Active 1.9) and then apply the Lose/Maintain/Gain adjustment to produce a candidate daily goal.
3. AC-004.3: WHEN the candidate goal is outside the safety bounds 1000–3500 kcal THEN THE SYSTEM SHALL clamp to the nearest bound AND display a non-blocking warning ("Goal adjusted to safety bounds"); the displayed and persisted goal SHALL always lie in [1000, 3500] per BR-020.3.
4. AC-004.4: WHEN the user taps "Ready to start logging" THEN THE SYSTEM SHALL persist the completed `User` (height/weight/sex/age/goal/activityLevel/calorieTarget/onboardingComplete=true) via `DataClient.update(_:)` and route to RootView (Camera tab).
5. AC-004.5: IF persistence fails (network, server error) THEN THE SYSTEM SHALL surface a recoverable error via `ErrorHandler` with a "Retry" action; the user SHALL NOT be left mid-onboarding with unsaved data — re-tapping "Ready to start logging" SHALL re-attempt the save with the same in-progress `UserProfileDraft`.

## Non-Functional Requirements
- NFR-OB-001: Step transition latency — Moving between onboarding steps SHALL complete within 200ms (per UX rule from PRD §12). Measured: tap "Next" → next step first frame.
- NFR-OB-002: TDEE compute latency — Mifflin-St Jeor + multiplier + adjustment + clamp SHALL execute in <100ms per `TDEECalculator.calculate(...)` call. Measured: deterministic pure function over `UserProfileDraft`.
- NFR-OB-003: Goal safety bounds — The final calorie goal SHALL always be clamped to [1000, 3500] kcal (BR-020.3) regardless of inputs; the displayed goal SHALL match the persisted value bit-for-bit.
- NFR-OB-004: Validation completeness — Every required field SHALL be validated client-side before advancing; no empty or out-of-range `User` fields SHALL reach `DataClient`.
- NFR-OB-005: Persistence durability — `onboardingComplete=true` SHALL be written atomically with `calorieTarget` and all profile fields; a partial write SHALL NOT leave the user stuck mid-onboarding (NFR-006 keychain + DataClient atomicity).
- NFR-OB-006: Unit conversion — All values SHALL be stored in metric (cm / kg / years) regardless of input unit; the UI MAY toggle cm/in and kg/lb as a display-only concern, but the stored value SHALL be metric (BR-018.3).