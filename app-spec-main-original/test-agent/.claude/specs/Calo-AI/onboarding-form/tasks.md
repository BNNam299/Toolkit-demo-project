# onboarding-form - Implementation Plan

## Execution Mode
- Mode: manual
- Policy: run sequentially by default (UI-first order from design.md)
- Gate: stop on phase boundary or blocking error

## Task Registry (Machine Readable)

| ID | Title | Type | Status | Refs AC | Refs Design | Files | Checkpoint |
|---|---|---|---|---|---|---|---|
| 2.1.1 | UserProfileDraft + Sex + WeightGoal + ActivityLevel enums | normal | pending | AC-001.2, AC-001.3, AC-001.4, AC-002.2, AC-002.4, AC-003.1, AC-003.2, AC-003.3 | 4 | Features/Onboarding/Models/UserProfileDraft.swift, Features/Onboarding/Models/Sex.swift, Features/Onboarding/Models/WeightGoal.swift, Features/Onboarding/Models/ActivityLevel.swift | Enums + draft + validate() |
| 2.1.2 | TDEECalculator (Mifflin-St Jeor + multiplier + adjustment + clamp) | normal | pending | AC-002.2, AC-003.1, AC-003.2, AC-003.3, AC-004.1, AC-004.2, AC-004.3 | 4, 7.4 | Features/Onboarding/Utils/TDEECalculator.swift | Pure function; clamp bounds |
| 3.1.1 | OnboardingViewModel (step machine, validation, save, retry) | normal | pending | AC-001.2, AC-002.3, AC-003.4, AC-004.4, AC-004.5 | 7.1, 7.2, 7.3, 7.4 | Features/Onboarding/ViewModels/OnboardingViewModel.swift | Step transitions + save/retry |
| 3.2.1 | OnboardingStepBasicInfoView (Step 1) | normal | pending | AC-001.1, AC-001.2, AC-001.3, AC-001.4, AC-003.1, AC-003.2, AC-003.3, AC-003.4 | 7.1, 7.3 | Features/Onboarding/Views/OnboardingStepBasicInfoView.swift | Inputs + goal + rate; inline errors |
| 3.2.2 | OnboardingStepActivityView (Step 2) | normal | pending | AC-002.1, AC-002.2, AC-002.4 | 7.2 | Features/Onboarding/Views/OnboardingStepActivityView.swift | 4 radios + descriptions |
| 3.2.3 | OnboardingStepGoalConfirmView (Step 3) + clamp warning | normal | pending | AC-004.1, AC-004.2, AC-004.3, AC-004.4, AC-004.5 | 7.4 | Features/Onboarding/Views/OnboardingStepGoalConfirmView.swift | Big goal + formula + Ready button |
| 3.3.1 | OnboardingProgressIndicator (1/3, 2/3, 3/3) | normal | pending | AC-001.1, AC-002.1, AC-004.4 | 7.1, 7.2, 7.4 | Features/Onboarding/Views/OnboardingProgressIndicator.swift | Segmented progress chip |
| 3.4.1 | OnboardingView assembly (NavigationStack container) | normal | pending | AC-001.1, AC-002.1, AC-004.4, AC-004.5 | 8 | Features/Onboarding/Views/OnboardingView.swift | 3-step container with back/next |
| 3.5.1 | Wire OnboardingView into RootView as `.onboarding` route | normal | pending | AC-004.4 | 8 | App/RootView.swift | Auth success → OnboardingView → MainTabView |
| 4.1.1 | UserProfileDraft + enums tests | pbt | pending | AC-001.2, AC-001.3, AC-001.4, AC-002.2, AC-002.4, AC-003.1, AC-003.2, AC-003.3, AC-003.4 | 6 | calo-ai-testTests/UserProfileDraftTests.swift | Validation + enums + rate mapping |
| 4.1.2 | TDEECalculator tests | pbt | pending | AC-004.1, AC-004.2, AC-004.3 | 6 | calo-ai-testTests/TDEECalculatorTests.swift | Mifflin-St Jeor + clamp |
| 4.1.3 | OnboardingViewModel tests (fake DataClienting) | pbt | pending | AC-002.3, AC-004.4, AC-004.5 | 6 | calo-ai-testTests/OnboardingViewModelTests.swift | Step transitions + save/retry |
| 4.2.1 | Build + integration gate | normal | pending | AC-001.1, AC-002.1, AC-004.4 | 6 | (build gate) | build_sim green; 3-step flow end-to-end |

## Dependency Matrix
| Task | Depends On | Can Parallel With |
|---|---|---|
| 2.1.1 | — | 2.1.2 |
| 2.1.2 | 2.1.1 | — |
| 3.1.1 | 2.1.1, 2.1.2 | 3.2.1, 3.2.2 |
| 3.2.1 | 2.1.1, 3.1.1 | 3.2.2, 3.3.1 |
| 3.2.2 | 2.1.1, 3.1.1 | 3.2.1, 3.3.1 |
| 3.2.3 | 2.1.2, 3.1.1 | 3.3.1 |
| 3.3.1 | — | 3.2.1, 3.2.2, 3.2.3 |
| 3.4.1 | 3.1.1, 3.2.1, 3.2.2, 3.2.3, 3.3.1 | — |
| 3.5.1 | 3.4.1 | — |
| 4.1.1 | 2.1.1 | 4.1.2, 4.1.3 |
| 4.1.2 | 2.1.1, 2.1.2 | 4.1.1, 4.1.3 |
| 4.1.3 | 3.1.1, 4.1.1, 4.1.2 | — |
| 4.2.1 | 3.5.1, 4.1.1, 4.1.2, 4.1.3 | — |

## 1. Shared Tasks
> Pure models + utility the ViewModel and views depend on.

- [ ] **2.1.1** `UserProfileDraft` (in-progress struct with `validate(step:) -> AppError?`) + `Sex` enum (`bmrConstant: +5/-161/+1`) + `WeightGoal` enum (`dailyAdjustmentKcal(rateLbPerWeek:)`) + `ActivityLevel` enum (`multiplier: 1.375/1.55/1.725/1.9`)
  - Refs: AC-001.2, AC-001.3, AC-001.4, AC-002.2, AC-002.4, AC-003.1, AC-003.2, AC-003.3
  - Design: 4
  - File: `Features/Onboarding/Models/UserProfileDraft.swift`, `Features/Onboarding/Models/Sex.swift`, `Features/Onboarding/Models/WeightGoal.swift`, `Features/Onboarding/Models/ActivityLevel.swift`
- [ ] **2.1.2** `TDEECalculator.calculate(draft:)` pure function — Mifflin-St Jeor BMR (`10W + 6.25H − 5A + s.bmrConstant`), TDEE = BMR × activity_multiplier, rawGoal = TDEE + adjustment, clampedGoal ∈ [1000, 3500], `wasClamped` flag, `formulaBreakdown` string
  - Refs: AC-002.2, AC-003.1, AC-003.2, AC-003.3, AC-004.1, AC-004.2, AC-004.3
  - Design: 4, 7.4
  - File: `Features/Onboarding/Utils/TDEECalculator.swift`

**Phase Gate 2 (end of Shared phase):** Run XcodeBuildMCP `discover_projs -> list_schemes -> build_sim`, then traceability check (AC-001.2/3/4, AC-002.2/4, AC-003.1/2/3, AC-004.1/2/3 covered; Refs Design resolve).

## 2. Feature Tasks
> ViewModel + step views + progress indicator + assembly.

- [ ] **3.1.1** `OnboardingViewModel` (`@MainActor ObservableObject`; `@Published currentStep: Step`, `draft: UserProfileDraft`; `next()`, `back()`, `setBasicInfo(...)`, `setGoal(...)`, `setActivity(...)`, `save()` with `DataClienting.update(User)` + retry; deps: `DataClienting`, `ErrorPresenting` injected)
  - Refs: AC-001.2, AC-002.3, AC-003.4, AC-004.4, AC-004.5
  - Design: 7.1, 7.2, 7.3, 7.4
  - File: `Features/Onboarding/ViewModels/OnboardingViewModel.swift`
- [ ] **3.2.1** `OnboardingStepBasicInfoView` — numeric inputs (height/weight/age) + sex segmented + goal radio + rate stepper (hidden for Maintain); inline validation messages; "Next" `CaloButton` gated by `validate(step: .basicInfo)`
  - Refs: AC-001.1, AC-001.2, AC-001.3, AC-001.4, AC-003.1, AC-003.2, AC-003.3, AC-003.4
  - Design: 7.1, 7.3
  - File: `Features/Onboarding/Views/OnboardingStepBasicInfoView.swift`
- [ ] **3.2.2** `OnboardingStepActivityView` — 4 radio rows with descriptions; single-select; "Next" `CaloButton` gated by `validate(step: .activity)`
  - Refs: AC-002.1, AC-002.2, AC-002.4
  - Design: 7.2
  - File: `Features/Onboarding/Views/OnboardingStepActivityView.swift`
- [ ] **3.2.3** `OnboardingStepGoalConfirmView` — big calorie number + formula breakdown + clamp warning chip when `wasClamped==true` + "Ready to start logging" `CaloButton` triggering `save()`
  - Refs: AC-004.1, AC-004.2, AC-004.3, AC-004.4, AC-004.5
  - Design: 7.4
  - File: `Features/Onboarding/Views/OnboardingStepGoalConfirmView.swift`
- [ ] **3.3.1** `OnboardingProgressIndicator` — "Step X of 3" + segmented bar; updates with `currentStep`
  - Refs: AC-001.1, AC-002.1, AC-004.4
  - Design: 7.1, 7.2, 7.4
  - File: `Features/Onboarding/Views/OnboardingProgressIndicator.swift`
- [ ] **3.4.1** `OnboardingView` assembly — `NavigationStack` host with progress indicator + current step view + Back/Next `CaloButton`s; step machine driven by `OnboardingViewModel`
  - Refs: AC-001.1, AC-002.1, AC-004.4, AC-004.5
  - Design: 8
  - File: `Features/Onboarding/Views/OnboardingView.swift`

**Phase Gate 3 (end of Feature phase):** Run XcodeBuildMCP `discover_projs -> list_schemes -> build_sim`, then traceability check (all 17 ACs covered; Refs Design resolve).

## 3. Integration Tasks
> Wiring + unit tests + build gate.

- [ ] **3.5.1** Wire `OnboardingView` into `RootView` as the destination for `AuthCoordinator.route == .onboarding`; route to `MainTabView` on `save()` success
  - Refs: AC-004.4
  - Design: 8
  - File: `App/RootView.swift`
- [ ] **4.1.1** `UserProfileDraftTests` + `SexEnumTests` + `WeightGoalEnumTests` + `ActivityLevelEnumTests` — validation accept/reject; `bmrConstant`; multipliers; rate mapping; show/hide stepper on goal switch
  - Refs: AC-001.2, AC-001.3, AC-001.4, AC-002.2, AC-002.4, AC-003.1, AC-003.2, AC-003.3, AC-003.4
  - Design: 6
  - File: `calo-ai-testTests/UserProfileDraftTests.swift`
- [ ] **4.1.2** `TDEECalculatorTests` — Mifflin-St Jeor on representative inputs (male 30y 80kg 180cm Moderate); clamp below 1000 and above 3500; `wasClamped` flag
  - Refs: AC-004.1, AC-004.2, AC-004.3
  - Design: 6
  - File: `calo-ai-testTests/TDEECalculatorTests.swift`
- [ ] **4.1.3** `OnboardingViewModelTests` (fake `DataClienting`) — step transitions; validation gating; `save()` success → `update(User)` with `onboardingComplete=true` + `calorieTarget==clampedGoal`; failure → draft intact + retry re-attempts same args
  - Refs: AC-002.3, AC-004.4, AC-004.5
  - Design: 6
  - File: `calo-ai-testTests/OnboardingViewModelTests.swift`
- [ ] **4.2.1** Build + integration gate: `build_sim` green; 3-step onboarding flow renders; Mifflin-St Jeor formula visible in step 3; clamp warning fires on extreme inputs; save + route to Camera tab
  - Refs: AC-001.1, AC-002.1, AC-004.4
  - Design: 6
  - File: (build gate)

**Phase Gate 4 (end of Integration phase):** Run XcodeBuildMCP `discover_projs -> list_schemes -> build_sim` (+ `test_sim`), then traceability check (all 17 ACs traced to ≥1 done task; every Refs Design resolves).

## Traceability Matrix
| Task ID | AC | Design | Property | Status |
|---|---|---|---|---|
| 2.1.1 | AC-001.2, AC-001.3, AC-001.4, AC-002.2, AC-002.4, AC-003.1, AC-003.2, AC-003.3 | 4 | P1, P2, P4, P5 | pending |
| 2.1.2 | AC-002.2, AC-003.1, AC-003.2, AC-003.3, AC-004.1, AC-004.2, AC-004.3 | 4, 7.4 | P3, P4, P5, P7 | pending |
| 3.1.1 | AC-001.2, AC-002.3, AC-003.4, AC-004.4, AC-004.5 | 7.1, 7.2, 7.3, 7.4 | P6, P9, P10, P11 | pending |
| 3.2.1 | AC-001.1, AC-001.2, AC-001.3, AC-001.4, AC-003.1, AC-003.2, AC-003.3, AC-003.4 | 7.1, 7.3 | P1, P6 | pending |
| 3.2.2 | AC-002.1, AC-002.2, AC-002.4 | 7.2 | P2 | pending |
| 3.2.3 | AC-004.1, AC-004.2, AC-004.3, AC-004.4, AC-004.5 | 7.4 | P7, P8, P10, P11 | pending |
| 3.3.1 | AC-001.1, AC-002.1, AC-004.4 | 7.1, 7.2, 7.4 | — | pending |
| 3.4.1 | AC-001.1, AC-002.1, AC-004.4, AC-004.5 | 8 | P9 | pending |
| 3.5.1 | AC-004.4 | 8 | P10, P11 | pending |
| 4.1.1 | AC-001.2, AC-001.3, AC-001.4, AC-002.2, AC-002.4, AC-003.1, AC-003.2, AC-003.3, AC-003.4 | 6 | P1, P2, P4, P5, P6 | pending |
| 4.1.2 | AC-004.1, AC-004.2, AC-004.3 | 6 | P3, P7, P8 | pending |
| 4.1.3 | AC-002.3, AC-004.4, AC-004.5 | 6 | P9, P10, P11, P12 | pending |
| 4.2.1 | AC-001.1, AC-002.1, AC-004.4 | 6 | P10, P11 | pending |

## Progress
| Section | Total | Done | Status |
|---|---:|---:|---|
| Shared | 2 | 0 | ⬜ |
| Feature | 7 | 0 | ⬜ |
| Integration | 5 | 0 | ⬜ |