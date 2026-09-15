# project-structure - Requirements

## Overview
`project-structure` là spec hạ tầng nền tảng (Phase 1) của Calo AI. Mục tiêu là thiết lập một dự án Xcode chuẩn hoá, biên dịch được và chạy được trên simulator, với cây thư mục theo MVVM + Repository, quản lý dependency (SPM), cấu hình build/scheme theo môi trường, code signing + entitlements (Sign in with Apple), và một app shell điều hướng (TabView + NavigationStack) thay thế boilerplate CoreData mặc định. Spec này KHÔNG triển khai tính năng nghiệp vụ nào — nó là nền tảng bắt buộc mà toàn bộ 26 FR / 18 WF của MVP dựa lên (blocks: `shared-foundations` và tất cả spec downstream).

## Evidence References
- **Market data from PRD:** Ngành Health & Fitness đạt IAP 4.5 tỷ USD (2025, +13% YoY) và AI-photo logging là "vé vào cửa" bắt buộc (PRD §1, §4) → cần nền tảng iOS gọn, ra MVP nhanh (~13 ngày theo Roadmap) để chiếm khoảng trống niềm tin do khủng hoảng Cal AI (gỡ app 2026-04, rò rỉ 3.2 triệu bản ghi 2026-03).
- **Source documents:**
  - `.claude/specs/Calo-AI/PRD.md` §9 (Ràng buộc Sản phẩm và Kỹ thuật: iOS 16+, SwiftUI, MVVM, NavigationStack, dependencies AI Vision/RevenueCat/Firebase/Superwall, bảo mật backend có auth)
  - `.claude/specs/Calo-AI/Project_Overview.md` §3.1–§3.3 (Technology Stack, folder layout `App/ → Core/ → Features/`, architectural decisions)
  - `.claude/specs/Calo-AI/Project_Implementation_Roadmap.md` — Project Structure section (directory scaffold, files: `Calo-AI.xcodeproj`, `Config.xcconfig`, `Podfile`/SPM) và Phase 1 (Entry: None; Exit: "Build succeeds, simulator runs")
  - `.claude/specs/Calo-AI/Functional_Requirements.md` §3 (NFR-001, NFR-004, NFR-005, NFR-011, NFR-012, NFR-015, NFR-019)
- **Key KPIs (từ PRD §5 / Overview §6.1):** Crash-free sessions ≥99.5% (cần Crashlytics từ ngày đầu — NFR-015); Analytics đo funnel/conversion (Firebase — NFR-019); Cold launch <2.0s (nền tảng build tối ưu — NFR-001).

## Requirements

### Requirement 1 (REQ-001): Xcode Project & Deployment Target
**User Story:** As an iOS developer, I want a standardized Xcode project configured for iOS 16+ on iPhone that builds and runs on the simulator, so that all downstream feature specs have a compilable foundation.
**Source:** NFR-011 (iOS 16+), NFR-012 (iPhone 12+/A14), Roadmap Phase 1 (Exit: "Build succeeds, simulator runs"); enables FR-001–FR-026

#### Acceptance Criteria
1. AC-001.1: WHEN the project is opened in Xcode and built for an iOS Simulator THEN THE SYSTEM SHALL compile successfully with zero build errors.
2. AC-001.2: THE SYSTEM SHALL set the iOS Deployment Target to 16.0 and device family to iPhone-only (portrait orientation).
3. AC-001.3: WHEN the app is launched on a booted iOS 16 simulator THEN THE SYSTEM SHALL display the root shell without crashing.
4. AC-001.4: IF any source file references an API unavailable on iOS 16 or requiring A15+ only THEN THE SYSTEM SHALL fail the build (no silent runtime-only breakage), surfacing the availability error at compile time.

### Requirement 2 (REQ-002): MVVM + Repository Directory Scaffold
**User Story:** As an iOS developer, I want the source tree organized into App / Features / Shared / Resources following MVVM + Repository conventions, so that every feature spec knows exactly where its files belong.
**Source:** Project_Overview §3.1 (MVVM + Repository, naming conventions), Roadmap "Project Structure" (directory tree); enables `shared-foundations` and all Feature specs

#### Acceptance Criteria
1. AC-002.1: THE SYSTEM SHALL provide the directory scaffold: `App/`, `Features/`, `Shared/` (with `Models/`, `Services/`, `ViewModels/`, `Components/`, `Utils/`), `Resources/`, and `Supporting Files/`.
2. AC-002.2: THE SYSTEM SHALL contain the app entry point under `App/` (e.g. `CaloApp.swift`) that replaces the default CoreData boilerplate template.
3. AC-002.3: WHEN a developer adds a feature THEN THE SYSTEM SHALL support the layout `Features/<Feature>/Views|ViewModels|Services|Models/` without restructuring existing folders.
4. AC-002.4: IF the legacy template files (`ContentView.swift`, `Persistence.swift`, CoreData `.xcdatamodeld`, `Item` entity) remain THEN THE SYSTEM SHALL remove or replace them so no unused CoreData boilerplate ships in the target.

### Requirement 3 (REQ-003): Dependency Management
**User Story:** As an iOS developer, I want third-party SDKs declared via Swift Package Manager with pinned versions, so that builds are reproducible and the core integrations are wired from the start.
**Source:** PRD §9 (Tích hợp Bên thứ ba: RevenueCat, Firebase, Superwall, AI Vision), Overview §3.1 (Dịch vụ Bên thứ ba), NFR-015 (Crashlytics), NFR-019 (Analytics)

#### Acceptance Criteria
1. AC-003.1: THE SYSTEM SHALL declare dependencies through Swift Package Manager (SPM) with each package pinned to an explicit version (exact or up-to-next-major), not `branch`/`main`.
2. AC-003.2: THE SYSTEM SHALL include the foundational SDKs required for MVP: Supabase (backend), RevenueCat (billing), and Firebase (Analytics + Crashlytics).
3. AC-003.3: WHEN the project is built after a clean checkout and package resolution THEN THE SYSTEM SHALL resolve all packages successfully and compile.
4. AC-003.4: IF a required SDK cannot be resolved (network/version conflict) THEN THE SYSTEM SHALL surface the dependency-resolution error at build time rather than falling back to an unpinned version.

### Requirement 4 (REQ-004): Code Signing, Bundle Identity & Entitlements
**User Story:** As an iOS developer, I want a stable bundle identifier, signing configuration, and the capabilities MVP needs, so that authentication and device features work on real devices and pass App Store review.
**Source:** NFR-004 (Apple ID auth), FR-001 (camera access), PRD §9 (Authentication: Sign in with Apple bắt buộc); enables `authentication`

#### Acceptance Criteria
1. AC-004.1: THE SYSTEM SHALL define a unique reverse-DNS bundle identifier applied consistently across Debug and Release configurations.
2. AC-004.2: THE SYSTEM SHALL enable the "Sign in with Apple" capability in the app entitlements.
3. AC-004.3: THE SYSTEM SHALL configure automatic code signing for a development team so the app installs on a simulator and (when a team is set) a device.
4. AC-004.4: IF the "Sign in with Apple" entitlement is missing THEN THE SYSTEM SHALL fail the entitlement validation at build/sign time (prerequisite for `authentication` spec).

### Requirement 5 (REQ-005): App Configuration, Usage Descriptions & Secrets Handling
**User Story:** As an iOS developer, I want Info.plist usage strings and environment configuration set up with no secrets committed to source, so that the app requests permissions correctly and API keys stay out of the binary/repo.
**Source:** FR-001 (camera permission), PRD §9 (Quyền riêng tư và Bảo mật; audit backend), NFR-005 (TLS/secure transport)

#### Acceptance Criteria
1. AC-005.1: THE SYSTEM SHALL declare `NSCameraUsageDescription` (and `NSPhotoLibraryUsageDescription`) in Info.plist with a human-readable, App-Store-compliant purpose string.
2. AC-005.2: THE SYSTEM SHALL read environment-specific values (API base URLs, third-party keys) from `.xcconfig` build settings, not hardcoded literals in source.
3. AC-005.3: WHEN the repository is inspected THEN THE SYSTEM SHALL contain no committed production secrets (keys are injected via xcconfig/CI or a git-ignored config file).
4. AC-005.4: IF App Transport Security is configured THEN THE SYSTEM SHALL require secure (HTTPS/TLS) connections and SHALL NOT enable `NSAllowsArbitraryLoads`.

### Requirement 6 (REQ-006): Build Configurations & Schemes per Environment
**User Story:** As an iOS developer, I want Debug/Release build configurations and a shared scheme with environment separation, so that development, staging, and production can be built and analytics/billing point at the right backend.
**Source:** Roadmap Phase 1 (build config), NFR-013 (backend scale/staging isolation), Overview §5 Phase 1 (build configs); enables analytics/billing environment routing

#### Acceptance Criteria
1. AC-006.1: THE SYSTEM SHALL define at least `Debug` and `Release` build configurations with distinct settings (e.g. optimization, logging).
2. AC-006.2: THE SYSTEM SHALL provide a shared, source-controlled scheme that builds, runs, and tests the app target.
3. AC-006.3: WHEN building in `Debug` vs `Release` THEN THE SYSTEM SHALL select the corresponding environment configuration (e.g. staging vs production endpoint) via xcconfig.
4. AC-006.4: IF a build configuration is missing its required environment values THEN THE SYSTEM SHALL fail the build with a clear diagnostic rather than shipping empty/placeholder endpoints.

### Requirement 7 (REQ-007): Root App Shell & Navigation Container
**User Story:** As a user, I want the app to open into its main tabbed shell, so that I can reach the core areas (Camera, Diary, Dashboard, Settings) once features are implemented.
**Source:** PRD §9 (Navigation: NavigationStack với tab chính Camera/Nhật ký/Tiến trình/Cài đặt), Overview §3.1 (Navigation), Roadmap WF navigation; enables WF-002/WF-004/WF-005/WF-007 hosting

#### Acceptance Criteria
1. AC-007.1: THE SYSTEM SHALL provide a root SwiftUI shell using a `TabView` with tab slots for Camera, Diary, Dashboard, and Settings.
2. AC-007.2: THE SYSTEM SHALL wrap navigable tabs in `NavigationStack` (iOS 16 native), with no third-party navigation dependency.
3. AC-007.3: WHEN the app launches THEN THE SYSTEM SHALL show the shell with placeholder destinations that build and render for tabs whose features are not yet implemented.
4. AC-007.4: IF a tab's feature module is not yet built THEN THE SYSTEM SHALL display a clearly-labeled placeholder view rather than crashing or showing the CoreData list.

## Non-Functional Requirements
- NFR-PS-001: Buildability — A clean checkout SHALL build and launch on an iOS 16 simulator in a single `xcodebuild`/Xcode run with 0 errors. (Supports NFR-011, NFR-012)
- NFR-PS-002: Launch Foundation — The empty shell cold-launch SHALL complete in < 2.0s on iPhone 12+ simulator, establishing headroom for the NFR-001 target (<2.0s app launch).
- NFR-PS-003: Reliability Tooling — Firebase Crashlytics SHALL be initialized at app startup so crash-free-session tracking (target ≥99.5%, NFR-015) is available from the first build.
- NFR-PS-004: Analytics Tooling — Firebase Analytics SHALL be initialized so core funnel events (NFR-019) can be emitted by downstream features without further SDK setup.
- NFR-PS-005: Warning Hygiene — The project SHALL build with zero compiler warnings at baseline (treat-warnings-as-errors recommended for the app target) to keep the foundation clean for downstream specs.
- NFR-PS-006: Reproducibility — Dependency versions SHALL be pinned and the resolved `Package.resolved` committed so CI and all developers build identical package graphs.
