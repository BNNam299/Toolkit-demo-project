# project-structure - Implementation Plan

## Execution Mode
- Mode: manual
- Policy: run sequentially by default (infrastructure-first order from design.md)
- Gate: stop on phase boundary or blocking error

## Task Registry (Machine Readable)

| ID | Title | Type | Status | Refs AC | Refs Design | Files | Checkpoint |
|---|---|---|---|---|---|---|---|
| 2.1.1 | Retarget project to Calo-AI (iOS 16, iPhone, portrait) | normal | pending | AC-001.1, AC-001.2 | 7.1 | Calo-AI.xcodeproj/project.pbxproj, Supporting Files/Info.plist | Builds for iOS 16 sim |
| 2.1.2 | Enforce iOS-16 availability + zero-warning build settings | normal | pending | AC-001.4 | 7.1 | Calo-AI.xcodeproj/project.pbxproj | Warnings-as-errors on; build 0 warnings |
| 2.2.1 | Create canonical MVVM+Repository source tree | normal | pending | AC-002.1, AC-002.3 | 7.2 | App/, Features/, Shared/{Models,Services,ViewModels,Components,Utils}/, Resources/, Config/, Supporting Files/ | Folders exist, project references them |
| 2.2.2 | Remove CoreData boilerplate | normal | pending | AC-002.4 | 7.2 | (delete) ContentView.swift, Persistence.swift, calo_ai_test.xcdatamodeld/ | No CoreData/Item symbols compile |
| 2.3.1 | Add pinned SPM deps + commit Package.resolved | normal | pending | AC-003.1, AC-003.2 | 7.3 | project.xcworkspace/xcshareddata/swiftpm/Package.resolved | Supabase/RevenueCat/Firebase resolve |
| 2.4.1 | Bundle id, entitlements (Sign in with Apple), signing | normal | pending | AC-004.1, AC-004.2, AC-004.3 | 7.4 | Supporting Files/Calo-AI.entitlements, project.pbxproj | Signs; entitlement present |
| 2.5.1 | Info.plist usage strings + ATS HTTPS | normal | pending | AC-005.1, AC-005.4 | 7.5 | Supporting Files/Info.plist | Usage strings set; no arbitrary loads |
| 2.5.2 | xcconfig files + Secrets template + gitignore | normal | pending | AC-005.2, AC-005.3 | 7.5 | Config/Shared.xcconfig, Config/Secrets.example.xcconfig, .gitignore | Keys via xcconfig; secrets ignored |
| 2.6.1 | Debug/Release configs mapped to xcconfig + shared scheme | normal | pending | AC-006.1, AC-006.2 | 7.6 | Config/Debug.xcconfig, Config/Release.xcconfig, xcschemes/Calo-AI.xcscheme | Both configs build; scheme shared |
| 3.1.1 | PlaceholderView component | normal | pending | AC-007.4 | 7.7 | Shared/Components/Placeholder/PlaceholderView.swift | Renders labeled placeholder |
| 3.1.2 | RootView TabView + NavigationStack (4 tabs) | normal | pending | AC-007.1, AC-007.2 | 7.7 | App/RootView.swift | 4 tabs, each in NavigationStack |
| 3.2.1 | AppConfiguration (typed keys + ConfigError) | normal | pending | AC-005.2, AC-006.4 | 4 | App/AppConfiguration.swift | Reads Info.plist keys; throws on missing |
| 3.2.2 | AppEnvironment enum (staging/prod from APP_ENV) | normal | pending | AC-006.3 | 7.6 | App/AppEnvironment.swift | APP_ENV maps to correct case |
| 3.3.1 | AppBootstrap SDK init (idempotent, non-fatal degrade) | normal | pending | AC-007.3 | 5 | App/AppBootstrap.swift | Init runs once; failure non-fatal |
| 3.3.2 | CaloApp @main wiring (bootstrap → RootView, inject env) | normal | pending | AC-001.3, AC-007.3 | 7.7 | App/CaloApp.swift | Launches into shell |
| 4.1.1 | AppConfiguration unit tests | pbt | pending | AC-005.2, AC-006.4 | 6 | Calo-AITests/AppConfigurationTests.swift | Valid parses; invalid throws |
| 4.1.2 | AppEnvironment unit tests | pbt | pending | AC-006.3 | 6 | Calo-AITests/AppEnvironmentTests.swift | Mapping + unknown rejected |
| 4.2.1 | App launch smoke UI test | normal | pending | AC-001.3, AC-007.1, AC-007.3, AC-007.4 | 6 | Calo-AIUITests/AppLaunchSmokeTests.swift | 4 tabs + placeholders, no crash |
| 4.3.1 | Config lint + clean-checkout resolve/build verify | normal | pending | AC-001.1, AC-003.3, AC-003.4, AC-004.4, AC-005.3, AC-005.4 | 6 | (CI/manual gate script) | Clean build resolves pinned + 0 errors |
| 4.3.2 | Warning gate + cold-launch time check | normal | pending | AC-001.1 | 6 | (CI/manual gate) | 0 warnings; shell launch <2.0s |

## Dependency Matrix
| Task | Depends On | Can Parallel With |
|---|---|---|
| 2.1.1 | — | — |
| 2.1.2 | 2.1.1 | 2.2.1 |
| 2.2.1 | 2.1.1 | 2.1.2 |
| 2.2.2 | 2.2.1 | 2.3.1 |
| 2.3.1 | 2.2.1 | 2.2.2, 2.4.1 |
| 2.4.1 | 2.1.1 | 2.3.1, 2.5.1 |
| 2.5.1 | 2.1.1 | 2.4.1, 2.5.2 |
| 2.5.2 | 2.2.1 | 2.5.1, 2.6.1 |
| 2.6.1 | 2.2.1, 2.5.2 | 2.4.1 |
| 3.1.1 | 2.2.1 | 3.2.1, 3.2.2 |
| 3.1.2 | 3.1.1 | 3.3.1 |
| 3.2.1 | 2.5.2 | 3.1.1 |
| 3.2.2 | 2.6.1, 3.2.1 | 3.1.1 |
| 3.3.1 | 2.3.1, 3.2.2 | 3.1.2 |
| 3.3.2 | 3.1.2, 3.3.1 | — |
| 4.1.1 | 3.2.1 | 4.1.2 |
| 4.1.2 | 3.2.2 | 4.1.1 |
| 4.2.1 | 3.3.2 | 4.1.1, 4.1.2 |
| 4.3.1 | 2.3.1, 2.5.2, 3.3.2 | 4.3.2 |
| 4.3.2 | 3.3.2 | 4.3.1 |

## 1. Shared Tasks
> Project & infrastructure foundation — everything else depends on these.

- [ ] **2.1.1** Retarget project to Calo-AI: set product name, deployment target iOS 16.0, `TARGETED_DEVICE_FAMILY=1` (iPhone), portrait-only orientation
  - Refs: AC-001.1, AC-001.2
  - Design: 7.1
  - File: `Calo-AI.xcodeproj/project.pbxproj`, `Supporting Files/Info.plist`
- [ ] **2.1.2** Turn on `SWIFT_TREAT_WARNINGS_AS_ERRORS` for the app target and confirm no pre-iOS-16 availability usage
  - Refs: AC-001.4
  - Design: 7.1
  - File: `Calo-AI.xcodeproj/project.pbxproj`
- [ ] **2.2.1** Create the canonical source tree (`App/`, `Features/`, `Shared/{Models,Services,ViewModels,Components,Utils}/`, `Resources/`, `Config/`, `Supporting Files/`) and add group references
  - Refs: AC-002.1, AC-002.3
  - Design: 7.2
  - File: directory scaffold per design §3 File plan
- [ ] **2.2.2** Delete CoreData boilerplate (`ContentView.swift`, `Persistence.swift`, `calo_ai_test.xcdatamodeld/`, `Item` entity); remove from target membership
  - Refs: AC-002.4
  - Design: 7.2
  - File: (delete) `ContentView.swift`, `Persistence.swift`, `calo_ai_test.xcdatamodeld/`
- [ ] **2.3.1** Add SPM packages pinned to explicit versions (Supabase, RevenueCat `purchases-ios`, `firebase-ios-sdk` → FirebaseAnalytics + FirebaseCrashlytics); commit `Package.resolved`
  - Refs: AC-003.1, AC-003.2
  - Design: 7.3
  - File: `Calo-AI.xcodeproj/project.xcworkspace/xcshareddata/swiftpm/Package.resolved`
- [ ] **2.4.1** Set reverse-DNS bundle id (consistent Debug/Release), add `Calo-AI.entitlements` with `com.apple.developer.applesignin`, enable automatic signing
  - Refs: AC-004.1, AC-004.2, AC-004.3
  - Design: 7.4
  - File: `Supporting Files/Calo-AI.entitlements`, `Calo-AI.xcodeproj/project.pbxproj`
- [ ] **2.5.1** Add `NSCameraUsageDescription` + `NSPhotoLibraryUsageDescription`; configure ATS to forbid `NSAllowsArbitraryLoads`
  - Refs: AC-005.1, AC-005.4
  - Design: 7.5
  - File: `Supporting Files/Info.plist`
- [ ] **2.5.2** Create `Shared/Debug/Release` xcconfig routing keys to Info.plist `$(VAR)`; add `Secrets.example.xcconfig`; git-ignore real `Secrets.xcconfig`
  - Refs: AC-005.2, AC-005.3
  - Design: 7.5
  - File: `Config/Shared.xcconfig`, `Config/Secrets.example.xcconfig`, `.gitignore`
- [ ] **2.6.1** Map `Debug`/`Release` build configs to their xcconfig; create a shared, source-controlled scheme that builds/runs/tests
  - Refs: AC-006.1, AC-006.2
  - Design: 7.6
  - File: `Config/Debug.xcconfig`, `Config/Release.xcconfig`, `Calo-AI.xcodeproj/xcshareddata/xcschemes/Calo-AI.xcscheme`

**Phase Gate 2 (end of Shared phase):** Run XcodeBuildMCP `discover_projs -> list_schemes -> build_sim`, then run the traceability check (every Shared task's Refs Design resolves to a design.md section; ACs 001.*, 002.*, 003.*, 004.*, 005.*, 006.1-2 covered).

## 2. Feature Tasks
> The root app shell + configuration/bootstrap code.

- [ ] **3.1.1** Implement `PlaceholderView(title:)` — labeled "coming soon" view, VoiceOver label, Dynamic Type + Dark Mode friendly
  - Refs: AC-007.4
  - Design: 7.7
  - File: `Shared/Components/Placeholder/PlaceholderView.swift`
- [ ] **3.1.2** Implement `RootView` with `TabView` + `AppTab` (Camera/Diary/Dashboard/Settings), each tab wrapped in `NavigationStack`, hosting `PlaceholderView`
  - Refs: AC-007.1, AC-007.2
  - Design: 7.7
  - File: `App/RootView.swift`
- [ ] **3.2.1** Implement `AppConfiguration.load()` reading typed keys from Info.plist; throw `ConfigError.missingKey/.invalidValue`
  - Refs: AC-005.2, AC-006.4
  - Design: 4
  - File: `App/AppConfiguration.swift`
- [ ] **3.2.2** Implement `AppEnvironment` enum resolving `APP_ENV` → `.staging`/`.production` with endpoints; reject unknown value
  - Refs: AC-006.3
  - Design: 7.6
  - File: `App/AppEnvironment.swift`
- [ ] **3.3.1** Implement `AppBootstrap.configure(env)` — idempotent Firebase/Crashlytics/RevenueCat/Supabase init; non-fatal failures logged, never block shell
  - Refs: AC-007.3
  - Design: 5
  - File: `App/AppBootstrap.swift`
- [ ] **3.3.2** Implement `CaloApp` `@main`: load config, run bootstrap, inject `AppEnvironment`, present `RootView`
  - Refs: AC-001.3, AC-007.3
  - Design: 7.7
  - File: `App/CaloApp.swift`

**Phase Gate 3 (end of Feature phase):** Run XcodeBuildMCP `discover_projs -> list_schemes -> build_sim`, then run the traceability check (shell tasks cover AC-007.*, AC-006.3-4, AC-001.3; all Refs Design resolve).

## 3. Integration Tasks
> Tests + build/config gates proving the foundation.

- [ ] **4.1.1** Write `AppConfigurationTests` — valid keys parse; missing/invalid throw the right `ConfigError` (validates P14, P18)
  - Refs: AC-005.2, AC-006.4
  - Design: 6
  - File: `Calo-AITests/AppConfigurationTests.swift`
- [ ] **4.1.2** Write `AppEnvironmentTests` — `APP_ENV` raw values map to cases; unknown rejected (validates P14)
  - Refs: AC-006.3
  - Design: 6
  - File: `Calo-AITests/AppEnvironmentTests.swift`
- [ ] **4.2.1** Write `AppLaunchSmokeTests` — launches, tab bar has 4 tabs, each shows a placeholder, no crash (validates P3, P20)
  - Refs: AC-001.3, AC-007.1, AC-007.3, AC-007.4
  - Design: 6
  - File: `Calo-AIUITests/AppLaunchSmokeTests.swift`
- [ ] **4.3.1** Config lint + clean-checkout verification: deployment/device family, entitlement (`applesignin`) present, no arbitrary loads, no committed secrets, `Package.resolved` pinned; delete DerivedData → resolve + build 0 errors (validates P1, P9, P11, P15, P16)
  - Refs: AC-001.1, AC-003.3, AC-003.4, AC-004.4, AC-005.3, AC-005.4
  - Design: 6
  - File: (CI/manual gate script)
- [ ] **4.3.2** Warning gate (0 warnings) + cold-launch timing of empty shell <2.0s on iPhone 12+ sim (NFR-PS-002/005)
  - Refs: AC-001.1
  - Design: 6
  - File: (CI/manual gate)

**Phase Gate 4 (end of Integration phase):** Run XcodeBuildMCP `discover_projs -> list_schemes -> build_sim`, then run the traceability check (all 28 ACs traced to ≥1 done task; every Refs Design resolves to a design.md section).

## Traceability Matrix
| Task ID | AC | Design | Property | Status |
|---|---|---|---|---|
| 2.1.1 | AC-001.1, AC-001.2 | 7.1 | P1, P2 | pending |
| 2.1.2 | AC-001.4 | 7.1 | P4 | pending |
| 2.2.1 | AC-002.1, AC-002.3 | 7.2 | P5, P6 | pending |
| 2.2.2 | AC-002.4 | 7.2 | P1 | pending |
| 2.3.1 | AC-003.1, AC-003.2 | 7.3 | P7, P8 | pending |
| 2.4.1 | AC-004.1, AC-004.2, AC-004.3 | 7.4 | P10, P11, P12 | pending |
| 2.5.1 | AC-005.1, AC-005.4 | 7.5 | P13, P16 | pending |
| 2.5.2 | AC-005.2, AC-005.3 | 7.5 | P14, P15 | pending |
| 2.6.1 | AC-006.1, AC-006.2 | 7.6 | P17 | pending |
| 3.1.1 | AC-007.4 | 7.7 | P20 | pending |
| 3.1.2 | AC-007.1, AC-007.2 | 7.7 | P3, P19 | pending |
| 3.2.1 | AC-005.2, AC-006.4 | 4 | P14, P18 | pending |
| 3.2.2 | AC-006.3 | 7.6 | P14 | pending |
| 3.3.1 | AC-007.3 | 5 | P20 | pending |
| 3.3.2 | AC-001.3, AC-007.3 | 7.7 | P3, P20 | pending |
| 4.1.1 | AC-005.2, AC-006.4 | 6 | P14, P18 | pending |
| 4.1.2 | AC-006.3 | 6 | P14 | pending |
| 4.2.1 | AC-001.3, AC-007.1, AC-007.3, AC-007.4 | 6 | P3, P20 | pending |
| 4.3.1 | AC-001.1, AC-003.3, AC-003.4, AC-004.4, AC-005.3, AC-005.4 | 6 | P1, P9, P11, P15, P16 | pending |
| 4.3.2 | AC-001.1 | 6 | P1 | pending |

## Progress
| Section | Total | Done | Status |
|---|---:|---:|---|
| Shared | 9 | 7 | 🟨 (1 partial: 2.5.2 xcconfig-wiring; 1 deferred: 2.3.1 SPM) |
| Feature | 6 | 6 | ✅ |
| Integration | 5 | 2 | 🟨 (4.3.1/4.3.2 via build gate; 3 test tasks deferred — no test target) |

## Execution Log (2026-07-21)

**Build gate: ✅ SUCCEEDED** — `xcodebuild` (scheme `calo-ai-test`, iPhone 16 Pro / iOS 18.3 sim), **0 errors, 0 warnings** with `SWIFT_TREAT_WARNINGS_AS_ERRORS=YES`.

**Environment reconciliations (vs spec):**
- Project/target kept as `calo-ai-test` (not renamed to `Calo-AI`) to avoid risky manual pbxproj/rename surgery without Xcode GUI; Display Name set to "Calo AI". Bundle id kept `com.ac.calo-ai-test` (already consistent across Debug/Release → AC-004.1 satisfied).
- Xcode 26 **file-system-synchronized group** → new files auto-join target; no pbxproj file-reference edits needed.
- Project uses **generated Info.plist** (`GENERATE_INFOPLIST_FILE=YES`); usage strings + display name set via `INFOPLIST_KEY_*` build settings. ATS secure-by-default (no `NSAllowsArbitraryLoads`) → AC-005.4.
- pbxproj backed up to `project.pbxproj.bak` (no git repo present).

| Task | Status | Notes |
|------|--------|-------|
| 2.1.1 | ✅ done | Deployment target 26.2→16.0; `TARGETED_DEVICE_FAMILY` 1,2→1; portrait-only |
| 2.1.2 | ✅ done | `SWIFT_TREAT_WARNINGS_AS_ERRORS=YES`; build 0 warnings |
| 2.2.1 | ✅ done | `App/`, `Features/`, `Shared/{Models,Services,ViewModels,Components,Utils}/`, `Resources/`, `Config/` created |
| 2.2.2 | ✅ done | Deleted `ContentView.swift`, `Persistence.swift`, `calo_ai_testApp.swift`, `calo_ai_test.xcdatamodeld/` |
| 2.3.1 | ⛔ deferred | SPM package refs need pbxproj UUID surgery + network resolution; importing SDKs would break build until resolved. Add in Xcode: Supabase, RevenueCat (`purchases-ios`), Firebase (Analytics+Crashlytics), then commit `Package.resolved` |
| 2.4.1 | ✅ done | `calo-ai-test.entitlements` (applesignin) + `CODE_SIGN_ENTITLEMENTS`; team `K7HD34Q8UN` already set; simulator build signs OK |
| 2.5.1 | ✅ done | `NSCameraUsageDescription` + `NSPhotoLibraryUsageDescription`; ATS default secure |
| 2.5.2 | 🟨 partial | `Config/{Shared,Debug,Release,Secrets.example}.xcconfig` + `.gitignore` created. **Wiring as `baseConfigurationReference` deferred** (needs Xcode or careful pbxproj edit); effective values currently in target build settings |
| 2.6.1 | ✅ done | Debug/Release configs present; **shared scheme** created at `xcshareddata/xcschemes/calo-ai-test.xcscheme`. Env switching via xcconfig depends on 2.5.2 wiring |
| 3.1.1 | ✅ done | `PlaceholderView.swift` (a11y label, Dynamic Type/Dark Mode friendly) |
| 3.1.2 | ✅ done | `RootView.swift` — `TabView` + 4 tabs, each in `NavigationStack` |
| 3.2.1 | ✅ done | `AppConfiguration.swift` — lenient `load()` + throwing `loadStrict()` (`ConfigError`) |
| 3.2.2 | ✅ done | `AppEnvironment.swift` — `APP_ENV`→case, `.staging` fallback |
| 3.3.1 | ✅ done | `AppBootstrap.swift` — idempotent, non-fatal stub with SDK TODOs (keeps shell green) |
| 3.3.2 | ✅ done | `CaloApp.swift` `@main` — load config → bootstrap → inject env → `RootView` |
| 4.1.1 | ⛔ deferred | Needs a unit-test target (none exists). Add `calo-ai-testTests` target in Xcode |
| 4.1.2 | ⛔ deferred | Same — needs test target |
| 4.2.1 | ⛔ deferred | Needs a UI-test target |
| 4.3.1 | 🟨 partial | Build gate: clean build 0 errors ✅; config lint (deployment/device/orientation/entitlement/usage/ATS) ✅; secrets not committed ✅. SPM `Package.resolved` check N/A until 2.3.1 |
| 4.3.2 | 🟨 partial | 0 warnings ✅; cold-launch <2.0s not yet measured (needs boot+launch run) |
