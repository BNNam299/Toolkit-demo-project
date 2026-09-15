# testing-integration - Implementation Plan

## Execution Mode
- Mode: manual
- Policy: run sequentially by default (test harness first, then E2E flows, then coverage gate, then metadata + crash gate)
- Gate: stop on phase boundary or blocking error

## Task Registry (Machine Readable)

| ID | Title | Type | Status | Refs AC | Refs Design | Files | Checkpoint |
|---|---|---|---|---|---|---|---|
| 2.1.1 | CrashMonitor module + ErrorHandler extension | normal | pending | AC-005.1, AC-005.3 | 7.5 | Tools/CrashMonitor/CrashlyticsVerifier.swift, Shared/Services/ErrorHandler.swift | recordNonFatal forwards to Crashlytics |
| 2.1.2 | URLProtocol test stubs (AIVision/Supabase/RC/PhotosPicker) | normal | pending | AC-001.3, AC-001.5, AC-002.1, AC-002.5 | 7.1, 7.2 | Calo-AIUITests/Stubs/*.swift | No real network in tests |
| 2.1.3 | StoreKit Configuration.storekit + RC products | normal | pending | AC-002.1, AC-002.2, AC-002.4 | 7.2 | Calo-AIUITests/Configuration.storekit | 3 products, test_sign ready |
| 3.1.1 | CoreLoopE2ETests (permission grant → capture → AI mock → confirmation → save → diary) | pbt | pending | AC-001.1, AC-001.2, AC-001.4, AC-001.5 | 7.1 | Calo-AIUITests/CoreLoop/CoreLoopE2ETests.swift | <10s, quota +1 on Save |
| 3.2.1 | SubscriptionFlowTests (paywall → trial → active) | pbt | pending | AC-002.1, AC-002.2, AC-002.5 | 7.2 | Calo-AIUITests/Subscription/SubscriptionFlowTests.swift | trial_end = start + 7d |
| 3.2.2 | RestorePurchaseTests (2nd Apple ID) | pbt | pending | AC-002.3 | 7.2 | Calo-AIUITests/Subscription/RestorePurchaseTests.swift | Premium restored, no dup trial |
| 3.2.3 | CancelFlowTests (WF-018 + App Store deep-link) | pbt | pending | AC-002.4 | 7.2 | Calo-AIUITests/Subscription/CancelFlowTests.swift | Deep-link to apps.apple.com |
| 3.3.1 | AppInitSmokeTests extension (Firebase + Crashlytics init assert) | normal | pending | AC-005.1 | 7.5 | Calo-AIUITests/AppInitSmokeTests.swift | verifyInit() true |
| 4.1.1 | coverage-gate.sh + thresholds + new-untested-file detector | normal | pending | AC-003.1, AC-003.2, AC-003.4 | 7.3 | scripts/coverage-gate.sh, config/coverage.thresholds.json | Fails build if <60% |
| 4.1.2 | generate_coverage_maps.sh + per-spec Coverage/*.md | normal | pending | AC-003.3 | 7.3 | scripts/generate_coverage_maps.sh, Tests/Coverage/<Spec>.md | Map per spec regenerated |
| 4.2.1 | AppStoreMetadata yaml + AppStoreMetadataParser | normal | pending | AC-004.1 | 7.4 | StoreMetadata/app-store-metadata.yaml, Tools/Metadata/AppStoreMetadataParser.swift | Schema validates |
| 4.2.2 | Screenshot set for 6.7"/6.1"/5.5"/iPad + build_screenshot_set.sh | normal | pending | AC-004.2 | 7.4 | StoreMetadata/screenshots/, scripts/build_screenshot_set.sh | ≥3 per device class |
| 4.2.3 | PrivacyNutritionLabel.md + PrivacyPolicy.md | normal | pending | AC-004.3, AC-004.4 | 7.4 | StoreMetadata/PrivacyNutritionLabel.md, StoreMetadata/PrivacyPolicy.md | Apple categories declared |
| 4.2.4 | appstore_readiness_check.sh + release_signoff_check.sh | normal | pending | AC-004.5, AC-005.4 | 7.4, 7.5 | scripts/appstore_readiness_check.sh, scripts/release_signoff_check.sh | Both exit 0 on ready |
| 4.3.1 | CrashlyticsReportParser + beta Crashlytics export pipeline | normal | pending | AC-005.2 | 7.5 | Tools/CrashMonitor/CrashlyticsReportParser.swift, StoreMetadata/CrashlyticsReport.md | Sessions/crash-free parsed |
| 4.4.1 | Build + test_sim + readiness gate | normal | pending | AC-001.1, AC-002.1, AC-004.5 | 6 | (build gate) | All scripts green |

## Dependency Matrix
| Task | Depends On | Can Parallel With |
|---|---|---|
| 2.1.1 | — | 2.1.2, 2.1.3 |
| 2.1.2 | — | 2.1.1, 2.1.3 |
| 2.1.3 | — | 2.1.1, 2.1.2 |
| 3.1.1 | 2.1.1, 2.1.2 | 3.2.1, 3.2.2, 3.2.3, 3.3.1 |
| 3.2.1 | 2.1.2, 2.1.3 | 3.1.1, 3.2.2, 3.2.3, 3.3.1 |
| 3.2.2 | 2.1.2, 2.1.3 | 3.1.1, 3.2.1, 3.2.3, 3.3.1 |
| 3.2.3 | 2.1.2, 2.1.3 | 3.1.1, 3.2.1, 3.2.2, 3.3.1 |
| 3.3.1 | 2.1.1 | 3.1.1, 3.2.1, 3.2.2, 3.2.3 |
| 4.1.1 | — | 4.1.2, 4.2.*, 4.3.1 |
| 4.1.2 | 4.1.1 | 4.2.*, 4.3.1 |
| 4.2.1 | — | 4.1.*, 4.2.2, 4.2.3, 4.3.1 |
| 4.2.2 | 4.2.1 | 4.1.*, 4.2.3, 4.3.1 |
| 4.2.3 | 4.2.1 | 4.1.*, 4.2.2, 4.3.1 |
| 4.2.4 | 4.2.1, 4.2.2, 4.2.3 | 4.3.1 |
| 4.3.1 | 2.1.1 | 4.1.*, 4.2.* |
| 4.4.1 | 3.*, 4.* | — |

## 1. Shared Tasks
> Test harness foundations reused by every E2E suite and the crash monitor.

- [ ] **2.1.1** `CrashlyticsVerifier` (`Tools/CrashMonitor/`) + `recordNonFatal(_:)` extension on shared-foundations `ErrorHandler`; expose `verifyInit()` that asserts `FirebaseApp.configure()` ran and Crashlytics collection is enabled
  - Refs: AC-005.1, AC-005.3
  - Design: 7.5
  - File: `Tools/CrashMonitor/CrashlyticsVerifier.swift`, `Shared/Services/ErrorHandler.swift`
- [ ] **2.1.2** `URLProtocol` stubs (`AIVisionStub`, `SupabaseStub`, `RCStub`, `PhotosPickerStub`) — register via `URLSessionConfiguration.ephemeral.protocolClasses` so all suites run without real network/photo library
  - Refs: AC-001.3, AC-001.5, AC-002.1, AC-002.5
  - Design: 7.1, 7.2
  - File: `Calo-AIUITests/Stubs/AIVisionStub.swift`, `SupabaseStub.swift`, `RCStub.swift`, `PhotosPickerStub.swift`
- [ ] **2.1.3** `Configuration.storekit` with weekly/monthly/annual products in the Calo AI subscription group; wire to `Calo-AIUITests` scheme (`-STOREKIT_CONFIGURATION` arg)
  - Refs: AC-002.1, AC-002.2, AC-002.4
  - Design: 7.2
  - File: `Calo-AIUITests/Configuration.storekit`

**Phase Gate 2 (end of Shared phase):** Run XcodeBuildMCP `discover_projs -> list_schemes -> build_sim`, then traceability check (AC-001.3, AC-002.1, AC-005.1, AC-005.3 covered; stubs compile; Refs Design resolve).

## 2. Feature Tasks
> XCUITest flows for the two product-critical paths and the smoke test.

- [ ] **3.1.1** `CoreLoopE2ETests` — drive Camera permission grant → shutter (or `PhotosPickerStub`) → `AIVisionStub` returns meal JSON → Confirmation toggle ingredient + change portion .medium→.large → Save → assert diary entry shows correct totals and `ScanQuotaService.used` incremented by 1; negative branch: permission denied → no Save, no AI call; assert <10s
  - Refs: AC-001.1, AC-001.2, AC-001.4, AC-001.5
  - Design: 7.1
  - File: `Calo-AIUITests/CoreLoop/CoreLoopE2ETests.swift`
- [ ] **3.2.1** `SubscriptionFlowTests` — paywall (WF-006) → assert both monthly+annual price+cycle visible → tap annual → StoreKit sheet (`test_sign`) → confirm → assert `SubscriptionState.trialing`, `trial_end = start + 7d`, scan badge "Unlimited"; cancel-sheet branch: no mutation, no `subscription_started` event gap
  - Refs: AC-002.1, AC-002.2, AC-002.5
  - Design: 7.2
  - File: `Calo-AIUITests/Subscription/SubscriptionFlowTests.swift`
- [ ] **3.2.2** `RestorePurchaseTests` — log in with second sandbox Apple ID that has a prior Premium receipt → Settings → "Restore purchases" → assert `SubscriptionState` matches receipt, no duplicate trial grant
  - Refs: AC-002.3
  - Design: 7.2
  - File: `Calo-AIUITests/Subscription/RestorePurchaseTests.swift`
- [ ] **3.2.3** `CancelFlowTests` — active subscription → Settings → Cancel → WF-018 modal → "Continue cancel" → assert deep-link URL host = `apps.apple.com` → return to app → `SubscriptionState.pendingCancellation`
  - Refs: AC-002.4
  - Design: 7.2
  - File: `Calo-AIUITests/Subscription/CancelFlowTests.swift`
- [ ] **3.3.1** `AppInitSmokeTests` extension — assert `CrashlyticsVerifier.verifyInit()` returns true after launch (FirebaseApp configured + Crashlytics collection enabled)
  - Refs: AC-005.1
  - Design: 7.5
  - File: `Calo-AIUITests/AppInitSmokeTests.swift`

**Phase Gate 3 (end of Feature phase):** Run XcodeBuildMCP `discover_projs -> list_schemes -> build_sim -> test_sim`, then traceability check (AC-001.*, AC-002.*, AC-005.1 covered; XCUITests green; Refs Design resolve).

## 3. Integration Tasks
> Coverage gate, App Store readiness artifacts, and release sign-off scripts.

- [ ] **4.1.1** `coverage-gate.sh` parses `xccov` JSON; enforces ≥60% on `Shared/Services/**` ∪ `Shared/Models/**` ∪ `Features/<F>/{ViewModels,Services}/**`; new-untested-file detector (diff vs prior baseline); `config/coverage.thresholds.json` for tuning
  - Refs: AC-003.1, AC-003.2, AC-003.4
  - Design: 7.3
  - File: `scripts/coverage-gate.sh`, `config/coverage.thresholds.json`
- [ ] **4.1.2** `generate_coverage_maps.sh` — produces `Tests/Coverage/<Spec>.md` for every spec (camera-capture, ai-recognition, shared-foundations, …, settings-management) with ViewModel/Service, % cov, untested functions + justifications; run after every `test_sim`
  - Refs: AC-003.3
  - Design: 7.3
  - File: `scripts/generate_coverage_maps.sh`, `Tests/Coverage/<Spec>.md`
- [ ] **4.2.1** `app-store-metadata.yaml` (name, subtitle, primary+secondary category, keywords ≤100 chars, support/marketing/privacy URLs, descriptionEN, descriptionVI, whatsNew, version) + `AppStoreMetadataParser` (Swift, schema validation)
  - Refs: AC-004.1
  - Design: 7.4
  - File: `StoreMetadata/app-store-metadata.yaml`, `Tools/Metadata/AppStoreMetadataParser.swift`
- [ ] **4.2.2** Screenshot set `StoreMetadata/screenshots/<DeviceClass>-<ScreenName>-<Locale>.png` for 6.7" (iPhone 14 Pro Max), 6.1" (iPhone 14), 5.5" (iPhone 8 Plus), iPad 12.9" — ≥3 per device class; `build_screenshot_set.sh` to copy/build from Figma source
  - Refs: AC-004.2
  - Design: 7.4
  - File: `StoreMetadata/screenshots/`, `scripts/build_screenshot_set.sh`
- [ ] **4.2.3** `PrivacyNutritionLabel.md` per Apple categories (Photos/Food Images, Health & Fitness, Identifiers, Usage Data, Diagnostics — all `Linked to User`, `Not Used for Tracking`; explicit "Data Not Collected" entries) + `PrivacyPolicy.md` (data collected, retention 7-day image auto-delete, user export+delete, 30-day GDPR/CCPA SLA per Overview §8)
  - Refs: AC-004.3, AC-004.4
  - Design: 7.4
  - File: `StoreMetadata/PrivacyNutritionLabel.md`, `StoreMetadata/PrivacyPolicy.md`
- [ ] **4.2.4** `appstore_readiness_check.sh` (metadata yaml + ≥3 screenshots per device class + Privacy Nutrition Label + Privacy Policy all present + yaml schema valid) + `release_signoff_check.sh` (reads `CrashlyticsReport.md` crash-free ≥99% or 99–99.5% with explicit sign-off in `ReleaseSignOff.md`)
  - Refs: AC-004.5, AC-005.4
  - Design: 7.4, 7.5
  - File: `scripts/appstore_readiness_check.sh`, `scripts/release_signoff_check.sh`
- [ ] **4.3.1** `CrashlyticsReportParser` consumes the Firebase Crashlytics export JSON and writes `CrashlyticsReport.md` (windowStart/End, totalSessions, crashCount, crashFreeRate, top-3 signatures with stack traces); `ReleaseSignOff.md` template with PO + iOS Lead + QA fields
  - Refs: AC-005.2
  - Design: 7.5
  - File: `Tools/CrashMonitor/CrashlyticsReportParser.swift`, `StoreMetadata/CrashlyticsReport.md`, `StoreMetadata/ReleaseSignOff.md`
- [ ] **4.4.1** Build + integration gate: `build_sim` green; `test_sim` runs all suites (unit + UI); `coverage-gate.sh` passes (≥60%); `appstore_readiness_check.sh` passes; `release_signoff_check.sh` placeholder passes (with sign-off note)
  - Refs: AC-001.1, AC-002.1, AC-004.5
  - Design: 6
  - File: (build gate)

**Phase Gate 4 (end of Integration phase):** Run XcodeBuildMCP `discover_projs -> list_schemes -> build_sim -> test_sim`, then run `coverage-gate.sh` + `appstore_readiness_check.sh` + `release_signoff_check.sh`; traceability check (all 23 ACs traced to ≥1 done task; every Refs Design resolves).

## Traceability Matrix
| Task ID | AC | Design | Property | Status |
|---|---|---|---|---|
| 2.1.1 | AC-005.1, AC-005.3 | 7.5 | P10, P11 | pending |
| 2.1.2 | AC-001.3, AC-001.5, AC-002.1, AC-002.5 | 7.1, 7.2 | P3, P6 | pending |
| 2.1.3 | AC-002.1, AC-002.2, AC-002.4 | 7.2 | P4 | pending |
| 3.1.1 | AC-001.1, AC-001.2, AC-001.4, AC-001.5 | 7.1 | P1, P2, P3 | pending |
| 3.2.1 | AC-002.1, AC-002.2, AC-002.5 | 7.2 | P4, P6 | pending |
| 3.2.2 | AC-002.3 | 7.2 | P5 | pending |
| 3.2.3 | AC-002.4 | 7.2 | P6 | pending |
| 3.3.1 | AC-005.1 | 7.5 | P10 | pending |
| 4.1.1 | AC-003.1, AC-003.2, AC-003.4 | 7.3 | P7, P8 | pending |
| 4.1.2 | AC-003.3 | 7.3 | P7 | pending |
| 4.2.1 | AC-004.1 | 7.4 | P9 | pending |
| 4.2.2 | AC-004.2 | 7.4 | P9 | pending |
| 4.2.3 | AC-004.3, AC-004.4 | 7.4 | P9 | pending |
| 4.2.4 | AC-004.5, AC-005.4 | 7.4, 7.5 | P9, P11 | pending |
| 4.3.1 | AC-005.2 | 7.5 | P11 | pending |
| 4.4.1 | AC-001.1, AC-002.1, AC-004.5 | 6 | P1, P4, P9 | pending |

## Progress
| Section | Total | Done | Status |
|---|---:|---:|---|
| Shared | 3 | 0 | ⬜ |
| Feature | 5 | 0 | ⬜ |
| Integration | 8 | 0 | ⬜ |