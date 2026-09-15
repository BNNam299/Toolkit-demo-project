# project-structure — Implementation Plan

**Spec ID**: `project-structure` · **Phase**: 1 · **Type**: `infra` · **Duration**: 1 ngày
**Requirements**: [`requirements.md`](./requirements.md) — 6 REQ · 42 AC
**Design**: [`design.md`](./design.md) — 9 section · 6 feature block · 8 property · 14 failure mode
**Tổng task**: 37 *(Shared 8 · Feature 14 · Integration 15)* — trong đó **8 task `pbt`**

---

## Execution Mode

- **Mode**: `manual` *(theo `spec-state.json`)*
- **Policy**: chạy tuần tự theo thứ tự ID. Task song song **chỉ** khi Dependency Matrix cho phép tường minh.
- **Gate**: dừng ở biên phase hoặc ở lỗi chặn đầu tiên. Không tự promote sang phase sau khi phase gate fail.
- **Thứ tự thi công**: **logic-first** — theo chuỗi phụ thuộc kỹ thuật ở design §8.2, không theo số REQ. Cụ thể: project + target (7.1) → cây thư mục (7.2) → App Group (7.3) + Info.plist (7.4) → build settings (7.5) → test infra + property (7.6).
- **Ánh xạ phase → design**: Shared = design 7.1 + 7.2 · Feature = design 7.3 + 7.4 + 7.5 · Integration = design 7.6 + §6.4 + §8.3.
- **Ràng buộc riêng của spec này**: đây là spec **duy nhất** mà phase gate không chạy được ở trạng thái ban đầu — trước task 2.1.1 không có project để `build_sim`. Phase Gate 2 là lần đầu tiên gate chạy được thật.

---

## Task Registry (Machine Readable)

| ID | Title | Type | Status | Refs AC | Refs Design | Files | Checkpoint |
|---|---|---|---|---|---|---|---|
| 2.1.1 | Tạo `Carbina.xcodeproj` + 2 target, deployment target 16.4 cả hai cấu hình | normal | pending | AC-002.1, AC-002.5 | 7.1 | `Carbina.xcodeproj` | CP-1 |
| 2.1.2 | Viết 4 file Swift tối thiểu, thân rỗng, giới hạn import | normal | pending | AC-002.1 | 3.1 | `App/CarbinaApp.swift`, `App/AppDelegate.swift`, `App/CarPlaySceneDelegate.swift`, `CarbinaWidget/CarbinaWidgetBundle.swift` | CP-1 |
| 2.1.3 | Gỡ framework cấm khỏi `CarbinaWidget`, khoá membership widget | normal | pending | AC-002.2, AC-002.3, AC-002.4 | 7.1 | `Carbina.xcodeproj` | CP-1 |
| 2.1.4 | Xác nhận compiler chặn API 17.4 ở target 16.4; ghi quy ước `#available` | normal | pending | AC-002.8 | 7.1 | `App/CarPlaySceneDelegate.swift` | CP-1 |
| 2.1.5 | Khai scene manifest CarPlay + `UISceneDelegateClassName` | normal | pending | AC-002.6 | 7.1 | `App/Info.plist` | CP-1 |
| 2.2.1 | Tạo 73 thư mục theo bảng chuẩn | normal | pending | AC-001.1, AC-001.2, AC-001.3, AC-001.4, AC-001.5, AC-001.6, AC-001.7 | 4.1 | 73 thư mục | CP-1 |
| 2.2.2 | Thêm `.gitkeep` vào mọi thư mục rỗng | normal | pending | AC-001.8 | 7.2 | `**/.gitkeep` | CP-1 |
| 2.2.3 | Rà và gỡ thư mục ngoài bảng chuẩn | normal | pending | AC-001.9 | 7.2 | cây thư mục | CP-1 |
| 3.1.1 | Bật App Group cả 2 target, ghi identifier vào 2 entitlements | normal | pending | AC-003.1, AC-003.2 | 4.2 | `App/Carbina.entitlements`, `CarbinaWidget/CarbinaWidget.entitlements` | CP-2 |
| 3.1.2 | Đặt Data Protection `CompleteUntilFirstUserAuthentication` | normal | pending | AC-003.4, AC-005.4 | 4.2 | `App/Carbina.entitlements` | CP-2 |
| 3.1.3 | Thêm build phase inline `Verify App Group` so 4 điểm khai | normal | pending | AC-003.6 | 7.3 | `Carbina.xcodeproj` | CP-2 |
| 3.1.4 | Viết marker handshake `#if DEBUG`: app ghi, widget đọc | normal | pending | AC-003.3 | 4.5 | `App/CarbinaApp.swift`, `CarbinaWidget/CarbinaWidgetBundle.swift` | CP-2 |
| 3.1.5 | Rà không tồn tại kênh chia sẻ thứ hai giữa 2 target | normal | pending | AC-003.5 | 8.4 | `App/**`, `CarbinaWidget/**` | CP-2 |
| 3.2.1 | Viết `App/Info.plist`: gỡ mọi khoá ATS ngoại lệ | normal | pending | AC-005.1, AC-005.2 | 4.3 | `App/Info.plist` | CP-2 |
| 3.2.2 | Viết 3 chuỗi mô tả quyền theo bảng chốt | normal | pending | AC-005.5 | 4.3 | `App/Info.plist` | CP-2 |
| 3.2.3 | Rà gỡ khoá quyền thừa ở app target | normal | pending | AC-005.6 | 7.4 | `App/Info.plist` | CP-2 |
| 3.2.4 | Viết `CarbinaWidget/Info.plist`: 0 khoá quyền + extension point | normal | pending | AC-005.7 | 4.3 | `CarbinaWidget/Info.plist` | CP-2 |
| 3.3.1 | Bật `SWIFT`/`GCC_TREAT_WARNINGS_AS_ERRORS = YES` cho Release | normal | pending | AC-004.1, AC-004.2 | 4.4 | `Carbina.xcodeproj` | CP-3 |
| 3.3.2 | Đặt `SWIFT_STRICT_CONCURRENCY` ≥ `targeted` + `SWIFT_VERSION` cao nhất | normal | pending | AC-004.5 | 4.4 | `Carbina.xcodeproj` | CP-3 |
| 3.3.3 | Bật coverage trong scheme, phạm vi giới hạn ở target chứa `Core/` | normal | pending | AC-004.4 | 4.4 | `Carbina.xcodeproj` | CP-3 |
| 3.3.4 | Build Debug + Release, sửa về 0 cảnh báo | normal | pending | AC-004.3 | 7.5 | `Carbina.xcodeproj` | CP-3 |
| 3.3.5 | Ghi quy ước comment lý do tại mọi chỗ tắt cảnh báo | normal | pending | AC-004.6 | 7.5 | `Carbina.xcodeproj` | CP-3 |
| 4.1.1 | Tạo 3 test bundle + gán scheme chạy cả 3 bằng một lệnh | normal | pending | AC-006.1, AC-006.4 | 7.6 | `Tests/CoreTests/`, `Tests/CarPlayLayoutTests/`, `Tests/FeatureTests/`, `Carbina.xcodeproj` | CP-4 |
| 4.1.2 | Thêm SwiftCheck ≥ 0.12.0 chỉ cho test target; commit `Package.resolved` | normal | pending | AC-006.5 | 7.6 | `Package.resolved`, `Carbina.xcodeproj` | CP-4 |
| 4.1.3 | Xác nhận test target không liên kết `CarbinaWidget` | normal | pending | AC-006.6 | 7.6 | `Carbina.xcodeproj` | CP-4 |
| 4.1.4 | Viết skeleton `LayoutPropertyTests` 3 hàm đúng tên + `XCTSkip` có lý do | normal | pending | AC-006.2, AC-006.3 | 7.6 | `Tests/CarPlayLayoutTests/LayoutPropertyTests.swift` | CP-4 |
| 4.1.5 | Viết `FeatureTestsPlaceholder` với `XCTSkip` | normal | pending | AC-006.1, AC-006.3 | 7.6 | `Tests/FeatureTests/FeatureTestsPlaceholder.swift` | CP-4 |
| 4.2.1 | **P1** — cây thư mục, kiểm hai chiều | pbt | pending | AC-001.1, AC-001.2, AC-001.3, AC-001.4, AC-001.5, AC-001.6, AC-001.7, AC-001.8, AC-001.9 | 9 | `Tests/CoreTests/ProjectStructureTests.swift` | CP-4 |
| 4.2.2 | **P2** — identifier khớp 4 điểm + biến thể lệch phải fail | pbt | pending | AC-003.1, AC-003.2, AC-003.6 | 9 | `Tests/CoreTests/AppGroupContainerTests.swift` | CP-4 |
| 4.2.3 | **P3** — widget không liên kết framework/file cấm; test không liên kết widget | pbt | pending | AC-002.2, AC-002.3, AC-002.4, AC-006.6 | 9 | `Tests/CoreTests/TargetMembershipTests.swift` | CP-4 |
| 4.2.4 | **P4** — round-trip container byte-identical + Data Protection | pbt | pending | AC-003.3, AC-003.4, AC-005.4 | 9 | `Tests/CoreTests/AppGroupContainerTests.swift` | CP-4 |
| 4.2.5 | **P5** — deployment target 16.4 trên mọi (target × cấu hình) | pbt | pending | AC-002.5 | 9 | `Tests/CoreTests/ProjectStructureTests.swift` | CP-4 |
| 4.2.6 | **P6** — khoá ATS bị cấm vắng mặt ở cả 2 target | pbt | pending | AC-005.1, AC-005.2 | 9 | `Tests/CoreTests/ProjectStructureTests.swift` | CP-4 |
| 4.2.7 | **P7** — warnings-as-errors, concurrency, coverage, lý do tắt cảnh báo | pbt | pending | AC-004.1, AC-004.2, AC-004.4, AC-004.5, AC-004.6 | 9 | `Tests/CoreTests/ProjectStructureTests.swift` | CP-4 |
| 4.2.8 | **P8** — chuỗi quyền: tồn tại, không rỗng, không câu chung, không thừa | pbt | pending | AC-005.5, AC-005.6, AC-005.7 | 9 | `Tests/CoreTests/ProjectStructureTests.swift` | CP-4 |
| 4.3.1 | Chạy 6 bước xác minh tay, lưu bằng chứng từng bước | normal | pending | AC-002.1, AC-002.6, AC-002.7, AC-003.3, AC-004.3, AC-005.3, AC-006.4 | 6.4 | *(bằng chứng, không phải file mã)* | CP-4 |
| 4.3.2 | Ghi hợp đồng chuyển giao C1–C4 + 3 việc dọn dẹp cho `shared-foundations` | normal | pending | AC-003.5 | 8.3 | `spec-state.json` | CP-4 |

---

## Dependency Matrix

| Task | Depends On | Can Parallel With |
|---|---|---|
| 2.1.1 | — *(task đầu tiên của dự án)* | — |
| 2.1.2 | 2.1.1 | — |
| 2.1.3 | 2.1.1 | 2.1.4, 2.1.5, 2.2.1 |
| 2.1.4 | 2.1.2 | 2.1.3, 2.1.5, 2.2.1 |
| 2.1.5 | 2.1.2 | 2.1.3, 2.1.4, 2.2.1 |
| 2.2.1 | 2.1.1 | 2.1.3, 2.1.4, 2.1.5 |
| 2.2.2 | 2.2.1 | 2.1.3, 2.1.4, 2.1.5 |
| 2.2.3 | 2.2.1 | 2.1.3, 2.1.4, 2.1.5 |
| 3.1.1 | 2.1.1 | 3.2.1 |
| 3.1.2 | 3.1.1 | 3.2.1, 3.2.2 |
| 3.1.3 | 3.1.1, 3.1.4 | 3.2.3, 3.2.4 |
| 3.1.4 | 3.1.1, 2.1.2 | 3.2.1, 3.2.2 |
| 3.1.5 | 3.1.4 | 3.2.3, 3.2.4 |
| 3.2.1 | 2.1.5 | 3.1.1, 3.1.2, 3.1.4 |
| 3.2.2 | 3.2.1 | 3.1.1, 3.1.2, 3.1.4 |
| 3.2.3 | 3.2.2 | 3.1.3, 3.1.5 |
| 3.2.4 | 2.1.1 | 3.1.3, 3.1.5, 3.2.3 |
| 3.3.1 | 2.2.3, 3.1.3, 3.2.4 | — *(xem ghi chú §2 về vì sao không song song)* |
| 3.3.2 | 3.3.1 | 3.3.3 |
| 3.3.3 | 3.3.1 | 3.3.2 |
| 3.3.4 | 3.3.1, 3.3.2, 3.3.3 | — |
| 3.3.5 | 3.3.4 | — |
| 4.1.1 | 3.3.4 | — |
| 4.1.2 | 4.1.1 | — |
| 4.1.3 | 4.1.1 | 4.1.4, 4.1.5 |
| 4.1.4 | 4.1.2 | 4.1.5 |
| 4.1.5 | 4.1.1 | 4.1.3, 4.1.4 |
| 4.2.1 | 4.1.2, 2.2.2 | 4.2.2, 4.2.3, 4.2.5, 4.2.6, 4.2.7, 4.2.8 |
| 4.2.2 | 4.1.2, 3.1.3 | 4.2.1, 4.2.3, 4.2.5, 4.2.6, 4.2.7, 4.2.8 |
| 4.2.3 | 4.1.2, 4.1.3 | 4.2.1, 4.2.2, 4.2.5, 4.2.6, 4.2.7, 4.2.8 |
| 4.2.4 | 4.1.2, 3.1.4, 3.1.2 | 4.2.1, 4.2.2, 4.2.3, 4.2.5, 4.2.6, 4.2.7, 4.2.8 |
| 4.2.5 | 4.1.2, 2.1.1 | 4.2.1, 4.2.2, 4.2.3, 4.2.6, 4.2.7, 4.2.8 |
| 4.2.6 | 4.1.2, 3.2.1, 3.2.4 | 4.2.1, 4.2.2, 4.2.3, 4.2.5, 4.2.7, 4.2.8 |
| 4.2.7 | 4.1.2, 3.3.5 | 4.2.1, 4.2.2, 4.2.3, 4.2.5, 4.2.6, 4.2.8 |
| 4.2.8 | 4.1.2, 3.2.2, 3.2.3, 3.2.4 | 4.2.1, 4.2.2, 4.2.3, 4.2.5, 4.2.6, 4.2.7 |
| 4.3.1 | 4.1.4, 4.2.1, 4.2.2, 4.2.3, 4.2.4, 4.2.5, 4.2.6, 4.2.7, 4.2.8 | — |
| 4.3.2 | 4.3.1 | — |

**Ba ràng buộc thứ tự không được đảo, kèm lý do:**

1. **2.1.1 phải là task đầu tiên tuyệt đối.** Không có project thì không bật được capability, không gán được membership, không chạy được `build_sim`. Đây là task duy nhất trong cả 27 spec không có phase gate nào chạy được trước nó.
2. **3.3.1 (warnings-as-errors) phải sau 2.2.3, 3.1.3 và 3.2.4** — tức sau khi cây thư mục, build phase App Group và cả hai `Info.plist` đã xong. Lý do ở design §8.2: bật warnings-as-errors cùng lúc thêm build phase mới làm hai nguyên nhân fail trộn vào một output. Và bật trên project rỗng thì nợ cảnh báo = 0 *(design §2.4 Quyết định C)*.
3. **8 task `pbt` (4.2.x) đều phụ thuộc 4.1.2** — SwiftCheck phải resolve xong trước. Chúng chạy song song được với nhau, nhưng mỗi task còn phụ thuộc riêng vào task tạo ra tạo phẩm nó kiểm: 4.2.7 chờ 3.3.5, 4.2.8 chờ 3.2.2/3.2.3/3.2.4, v.v. Chạy PBT trước khi tạo phẩm tồn tại sẽ cho fail giả và làm mất niềm tin vào suite.

---

## 1. Shared Tasks

*Design §7.1 + §7.2 — nền mà 35 task còn lại của spec này và 26 spec sau đứng lên.*

- [ ] **2.1.1** Tạo `Carbina.xcodeproj` với 2 target `Carbina` (iOS app) + `CarbinaWidget` (widget extension); đặt `IPHONEOS_DEPLOYMENT_TARGET = 16.4` cho **cả hai target ở cả Debug và Release**
  - Refs: AC-002.1, AC-002.5
  - Design: 7.1
  - File: `Carbina.xcodeproj`
  - Lưu ý: **không** khai tay `MinimumOSVersion` trong plist — Xcode dẫn xuất từ build setting; hai nguồn sẽ lệch được *(design §4.6 quy tắc 1)*

- [ ] **2.1.2** Viết 4 file Swift tối thiểu với thân rỗng: `CarbinaApp` (`@main` + `WindowGroup` rỗng), `AppDelegate` (scene configuration), `CarPlaySceneDelegate` (`didConnect`/`didDisconnect` rỗng + `// TODO(widget-render)`), `CarbinaWidgetBundle` (`WidgetBundle` + 1 `Widget` placeholder)
  - Refs: AC-002.1
  - Design: 3.1
  - Files: `App/CarbinaApp.swift`, `App/AppDelegate.swift`, `App/CarPlaySceneDelegate.swift`, `CarbinaWidget/CarbinaWidgetBundle.swift`
  - Ràng buộc import: chỉ `SwiftUI`, `WidgetKit`, `CarPlay`, `UIKit`, `Foundation`. `CarbinaWidgetBundle.swift` **chỉ** `WidgetKit`, `SwiftUI`, `Foundation`

- [ ] **2.1.3** Gỡ mọi framework template Xcode tự liên kết vào `CarbinaWidget` (`AVFoundation` là cái hay bị sót nhất); khoá danh sách liên kết widget về `{WidgetKit, SwiftUI, Foundation}`; xác nhận không file nào thuộc `Core/ML`·`Core/Audio`·`Core/Analytics`·`Core/Entitlement` có membership widget
  - Refs: AC-002.2, AC-002.3, AC-002.4
  - Design: 7.1
  - File: `Carbina.xcodeproj`
  - **Phải làm ngay ở task này, không để sau**: nếu để `AVFoundation` nằm lại, `sound-playback-connect` (Phase 5) sẽ thấy nó có sẵn ở widget và tưởng là hợp lệ *(design §7.1)*

- [ ] **2.1.4** Xác nhận deployment target 16.4 làm compiler **chặn** API chỉ có từ 17.4; ghi quy ước `if #available(iOS 17.4, *)` kèm nhánh giảm cấp thành comment tại `CarPlaySceneDelegate` để `widget-render` thấy được
  - Refs: AC-002.8
  - Design: 7.1
  - File: `App/CarPlaySceneDelegate.swift`
  - Cấm: **không** nâng deployment target để "cho dễ" — sẽ phá hợp đồng C2 và cắt thị phần iOS 16.4–17.3 *(Overview §3.3 Quyết định 1)*

- [ ] **2.1.5** Khai `UIApplicationSceneManifest` → `CPTemplateApplicationSceneSessionRoleApplication` với `UISceneDelegateClassName = CarPlaySceneDelegate` trong `App/Info.plist`
  - Refs: AC-002.6
  - Design: 7.1
  - File: `App/Info.plist`
  - Chế độ thất bại im lặng *(ERR-PS-010)*: sai tên class → scene **không bao giờ** được tạo, không crash, không log. Tên trong plist là chuỗi, **không** đổi theo refactor tên Swift — kiểm tay ở 4.3.1

- [ ] **2.2.1** Tạo 73 thư mục theo bảng chuẩn design §4.1: 7 gốc + 8 `Core/` + 9 module `Features/` + 30 thư mục con feature + 3 `shared/` + 6 `Components/` + 7 `Resources/` + 3 `Tests/`
  - Refs: AC-001.1, AC-001.2, AC-001.3, AC-001.4, AC-001.5, AC-001.6, AC-001.7
  - Design: 4.1
  - Files: 73 thư mục
  - **Không** tạo trước `Services/` cho `Paywall/`, `Settings/`, `Diagnostics/`, `CarPlayDashboard/` — AC-001.9 cấm, và 4 thư mục đó sẽ được thêm khi roadmap được patch trước Phase 8 *(design §4.1 ghi chú)*

- [ ] **2.2.2** Thêm `.gitkeep` vào **mọi** thư mục rỗng
  - Refs: AC-001.8
  - Design: 7.2
  - Files: `**/.gitkeep`
  - Nghiệm thu thật: clone repo ra đường dẫn khác và xác nhận 73 thư mục còn đủ. Git không theo dõi thư mục rỗng, nên lỗi này **chỉ hiện ra sau clone** *(ERR-PS-009)*

- [ ] **2.2.3** Rà toàn cây, gỡ mọi thư mục không có trong bảng §4.1
  - Refs: AC-001.9
  - Design: 7.2
  - Files: cây thư mục

**Phase Gate 2 (end of Shared phase):** Run XcodeBuildMCP `discover_projs` → `list_schemes` → `build_sim`, then traceability check passes.
Điều kiện pass = **CP-1** của design §6.5: build thành công với target rỗng · `list_schemes` liệt kê đúng `Carbina` + `CarbinaWidget` · `python .claude/scripts/validate_traceability.py project-structure` PASSED. Không boot simulator ở gate này.

---

## 2. Feature Tasks

*Design §7.3 (App Group) + §7.4 (Info.plist) + §7.5 (build settings) — ba nhóm cấu hình, mỗi nhóm cưỡng chế một ràng buộc mà requirements không muốn phó cho kỷ luật người viết code.*

### 2.1 App Group — kênh giao tiếp duy nhất *(design 7.3)*

- [ ] **3.1.1** Bật capability App Group trên **cả hai** target với cùng identifier `group.app.carbina.shared`; ghi vào cả hai `.entitlements`
  - Refs: AC-003.1, AC-003.2
  - Design: 4.2
  - Files: `App/Carbina.entitlements`, `CarbinaWidget/CarbinaWidget.entitlements`
  - Mảng `com.apple.security.application-groups` phải có **đúng một** phần tử, **byte-identical** giữa hai file

- [ ] **3.1.2** Đặt `com.apple.developer.default-data-protection = NSFileProtectionCompleteUntilFirstUserAuthentication` cho target `Carbina`
  - Refs: AC-003.4, AC-005.4
  - Design: 4.2
  - File: `App/Carbina.entitlements`

- [ ] **3.1.3** Thêm build phase inline `Verify App Group` trong `project.pbxproj`: so 4 điểm khai identifier (2 entitlements + 2 literal Swift), **fail build** khi lệch, in ra cả 4 giá trị và đường dẫn từng chỗ
  - Refs: AC-003.6
  - Design: 7.3
  - File: `Carbina.xcodeproj`
  - Script sống **inline** trong `project.pbxproj`, **không** tạo file/thư mục mới — thư mục `Scripts/` sẽ vi phạm AC-001.9
  - Đây là điểm chặn duy nhất cho ERR-PS-001, chế độ thất bại nguy hiểm nhất của spec: identifier lệch → widget đọc container rỗng **không phát ra lỗi nào**

- [ ] **3.1.4** Viết marker handshake trong `#if DEBUG`: `CarbinaApp` ghi `handshake.bin` vào container, `CarbinaWidgetBundle` đọc và render nội dung trong widget placeholder
  - Refs: AC-003.3
  - Design: 4.5
  - Files: `App/CarbinaApp.swift`, `CarbinaWidget/CarbinaWidgetBundle.swift`
  - Tạo phẩm **tạm**: `shared-foundations` xoá cả marker và gom 2 literal vào `AppGroupBridge` *(design §8.3)*

- [ ] **3.1.5** Rà cả `App/**` và `CarbinaWidget/**`: không tồn tại kênh chia sẻ thứ hai — `UserDefaults` chuẩn, Keychain sharing, Darwin notification chở dữ liệu, hay file ngoài container
  - Refs: AC-003.5
  - Design: 8.4
  - Files: `App/**`, `CarbinaWidget/**`
  - Phát hiện kênh thứ hai = **lỗi kiến trúc chặn merge**, không có ngoại lệ ở MVP 1 *(ERR-PS-011)*

### 2.2 Info.plist — bảo mật vận chuyển và chuỗi quyền *(design 7.4)*

- [ ] **3.2.1** Viết `App/Info.plist`; gỡ mọi khoá ATS ngoại lệ do template sinh — `NSAllowsArbitraryLoads` và `NSExceptionDomains` phải **không tồn tại**
  - Refs: AC-005.1, AC-005.2
  - Design: 4.3
  - File: `App/Info.plist`
  - Kiểm **sự vắng mặt**, không kiểm giá trị `false`: khoá có mặt với `false` vẫn là tín hiệu ai đó đã chạm vào ATS *(design §9 P6)*

- [ ] **3.2.2** Viết 3 chuỗi mô tả quyền `NSLocationWhenInUseUsageDescription`, `NSCalendarsUsageDescription`, `NSPhotoLibraryUsageDescription` theo **bảng chốt** design §4.3
  - Refs: AC-005.5
  - Design: 4.3
  - File: `App/Info.plist`
  - Mỗi chuỗi phải nêu **tính năng cụ thể** + **hệ quả nếu từ chối**. Cấm cụm chung kiểu "to improve your experience". Bản dịch ES/PT-BR thuộc `settings-presentation`

- [ ] **3.2.3** Rà `App/Info.plist`: không tồn tại khoá `NS*UsageDescription` thứ tư
  - Refs: AC-005.6
  - Design: 7.4
  - File: `App/Info.plist`
  - Khai quyền thừa là rủi ro **R-02** (App Review từ chối). Ba khoá ở 3.2.2 được khai trước có chủ ý vì `onboarding-flow` cần; khoá thứ tư thì không *(design §7.4)*

- [ ] **3.2.4** Viết `CarbinaWidget/Info.plist`: **0 khoá mô tả quyền** + `NSExtension` → `NSExtensionPointIdentifier = com.apple.widgetkit-extension`
  - Refs: AC-005.7
  - Design: 4.3
  - File: `CarbinaWidget/Info.plist`
  - Danh sách quyền rỗng ở widget là **trạng thái đúng**, không phải thiếu sót

### 2.3 Build settings — cảnh báo không lọt được *(design 7.5)*

- [ ] **3.3.1** Bật `SWIFT_TREAT_WARNINGS_AS_ERRORS = YES` và `GCC_TREAT_WARNINGS_AS_ERRORS = YES` cho cấu hình **Release**
  - Refs: AC-004.1, AC-004.2
  - Design: 4.4
  - File: `Carbina.xcodeproj`
  - Chỉ Release, **không** Debug *(design §2.4 Quyết định B)*: bật ở Debug làm cảnh báo tạm chặn vòng sửa–chạy, và phản ứng tự nhiên sẽ là tắt cảnh báo — đúng thứ AC-004.6 muốn tránh

- [ ] **3.3.2** Đặt `SWIFT_STRICT_CONCURRENCY` tối thiểu `targeted` và `SWIFT_VERSION` = bản cao nhất toolchain hỗ trợ, cho cả Debug và Release
  - Refs: AC-004.5
  - Design: 4.4
  - File: `Carbina.xcodeproj`
  - Để `minimal` sẽ dồn toàn bộ cảnh báo data-race của `Core/ML` + `Core/Audio` sang Phase 5–7, đúng lúc áp lực lịch cao nhất *(design §7.5)*

- [ ] **3.3.3** Bật thu thập code coverage trong scheme, **giới hạn phạm vi đo** ở target chứa `Core/`
  - Refs: AC-004.4
  - Design: 4.4
  - File: `Carbina.xcodeproj`
  - Ngưỡng 80% của AC-NFR-024.1 **chưa đo được** ở phase này vì `Core/` rỗng; task này chỉ chịu trách nhiệm bật đúng phạm vi *(design §6.3)*

- [ ] **3.3.4** Build cả Debug **và** Release; sửa cho về **0 cảnh báo** ở cả hai
  - Refs: AC-004.3
  - Design: 7.5
  - File: `Carbina.xcodeproj`
  - Bật trên project rỗng nên nợ cảnh báo ban đầu = 0. Đây là trạng thái mọi spec sau phải giữ *(design §2.4 Quyết định C)*

- [ ] **3.3.5** Ghi quy ước: mọi chỗ tắt cảnh báo (build setting `*_WARNINGS = NO`, `#pragma`, `swiftlint:disable`) phải có comment nêu lý do **ngay tại chỗ tắt**
  - Refs: AC-004.6
  - Design: 7.5
  - File: `Carbina.xcodeproj`
  - P7 (task 4.2.7) là chỗ quy ước này được cưỡng chế tự động *(ERR-PS-012)*

**Phase Gate 3 (end of Feature phase):** Run XcodeBuildMCP `discover_projs` → `list_schemes` → `build_sim`, then traceability check passes.
Điều kiện pass = **CP-2 + CP-3** của design §6.5: build phase `Verify App Group` chạy và pass · `build_sim` **cả Debug và Release** với 0 cảnh báo · Release không dừng vì warnings-as-errors · `validate_traceability.py project-structure` PASSED. Không boot simulator ở gate này.

---

## 3. Integration Tasks

*Design §7.6 (test infra) + §9 (8 property) + §6.4 (6 bước xác minh tay) + §8.3 (chuyển giao). Đây là phase biến 5 nhóm cấu hình ở trên thành thứ **kiểm được tự động ở mọi phase gate của 26 spec sau**.*

### 3.1 Hạ tầng test *(design 7.6)*

- [ ] **4.1.1** Tạo 3 test bundle `CoreTests`, `CarPlayLayoutTests`, `FeatureTests`; cấu hình scheme chạy **cả ba bằng một lệnh duy nhất**
  - Refs: AC-006.1, AC-006.4
  - Design: 7.6
  - Files: `Tests/CoreTests/`, `Tests/CarPlayLayoutTests/`, `Tests/FeatureTests/`, `Carbina.xcodeproj`
  - Làm cả ba **ngay bây giờ** dù hai bundle sẽ rỗng nhiều tuần: sửa `.xcscheme` về sau dễ làm lệch giữa các máy *(design §2.4 Quyết định D)*

- [ ] **4.1.2** Thêm SwiftCheck ≥ 0.12.0 qua SPM, khai **chỉ** cho test target; commit `Package.resolved`
  - Refs: AC-006.5
  - Design: 7.6
  - Files: `Package.resolved`, `Carbina.xcodeproj`
  - Khai cho target sản phẩm → vào bundle phát hành; khai cho `CarbinaWidget` → ăn vào ngân sách 25MB *(AC-NFR-007.1)*
  - `Package.resolved` được commit để build sau đó **không cần mạng** *(NFR-PS-008)*; resolve cần mạng đúng một lần

- [ ] **4.1.3** Xác nhận không test target nào liên kết vào `CarbinaWidget`
  - Refs: AC-006.6
  - Design: 7.6
  - File: `Carbina.xcodeproj`
  - Test không được làm tăng kích thước widget extension — lỗi cấu hình chặn merge *(ERR-PS-002)*

- [ ] **4.1.4** Viết skeleton `LayoutPropertyTests.swift` với **đúng ba tên hàm**: `testNoOverflowForAnyBounds()`, `testTextNeverBelow16pt()`, `testNoHardcodedSizeConstants()`; mỗi hàm `XCTSkip("chờ widget-render (Phase 3)")`
  - Refs: AC-006.2, AC-006.3
  - Design: 7.6
  - File: `Tests/CarPlayLayoutTests/LayoutPropertyTests.swift`
  - Ba tên hàm là **hợp đồng** với `widget-render`, không phải gợi ý — đổi tên ở đây buộc Phase 3 phải đi tìm hoặc tạo hàm mới và để lại 3 hàm skip vĩnh viễn *(design §7.6)*
  - Nghiệm thu: chạy test thấy báo **skipped**, **không** phải passed *(ERR-PS-014 — passed = suite đang nói dối về độ phủ)*

- [ ] **4.1.5** Viết `FeatureTestsPlaceholder.swift` với 1 hàm `XCTSkip` có lý do, chỉ để bundle `FeatureTests` tồn tại
  - Refs: AC-006.1, AC-006.3
  - Design: 7.6
  - File: `Tests/FeatureTests/FeatureTestsPlaceholder.swift`

### 3.2 Property-based tests *(design 9)*

Tám property, tất cả trong `CoreTests`, đều **đọc tạo phẩm cấu hình thật** (`project.pbxproj`, `Info.plist`, `.entitlements`, hệ thống file) — không mock, vì đối tượng cần kiểm chính là cấu hình đó.

- [ ] **4.2.1** **P1 (Invariant)** — cây thư mục, kiểm **hai chiều**: mọi thư mục trong bảng §4.1 phải tồn tại, **và** mọi thư mục tồn tại dưới 7 gốc phải thuộc bảng; mọi thư mục rỗng có `.gitkeep`
  - Refs: AC-001.1, AC-001.2, AC-001.3, AC-001.4, AC-001.5, AC-001.6, AC-001.7, AC-001.8, AC-001.9
  - Design: 9
  - File: `Tests/CoreTests/ProjectStructureTests.swift`
  - Chiều thứ hai là chiều bắt thư mục lạ *(ERR-PS-008)* — test một chiều sẽ bỏ sót hoàn toàn
  - **Sẽ cần patch** khi roadmap thêm 4 `Services/` trước Phase 8, nếu không P1 fail đúng vào Phase 8 *(design §9.2)*

- [ ] **4.2.2** **P2 (Invariant)** — 4 điểm khai App Group identifier bằng nhau byte-identical và bằng `group.app.carbina.shared`; **và** với mọi biến thể lệch sinh bởi generator (bớt ký tự, đổi hoa/thường, thêm khoảng trắng, đổi dấu chấm) checker phải trả **fail**
  - Refs: AC-003.1, AC-003.2, AC-003.6
  - Design: 9
  - File: `Tests/CoreTests/AppGroupContainerTests.swift`
  - Nửa sau là phần quan trọng: nó chứng minh checker **không phải hàm luôn-true**

- [ ] **4.2.3** **P3 (Invariant)** — mọi framework trong tập cấm ∉ liên kết của `CarbinaWidget`; mọi file `Core/ML`·`Audio`·`Analytics`·`Entitlement` ∉ membership widget; mọi test target không liên kết widget; liên kết widget ⊆ `{WidgetKit, SwiftUI, Foundation}`
  - Refs: AC-002.2, AC-002.3, AC-002.4, AC-006.6
  - Design: 9
  - File: `Tests/CoreTests/TargetMembershipTests.swift`
  - Đây là property có **giá trị dài hạn cao nhất** của spec: nó bắt được ngày một spec Phase 7 vô tình thêm `CoreML` vào widget target — nguyên nhân gốc của rủi ro thực thi A *(design §9.2)*

- [ ] **4.2.4** **P4 (Round-trip)** — với **mọi** payload `Data` (rỗng, 1 byte, nhiều MB, nhị phân bất kỳ): ghi vào App Group container rồi đọc lại cho ra byte-identical; file kết quả có `FileProtectionType == .completeUntilFirstUserAuthentication`
  - Refs: AC-003.3, AC-003.4, AC-005.4
  - Design: 9
  - File: `Tests/CoreTests/AppGroupContainerTests.swift`
  - Giới hạn phải nhớ: test chạy trong **test host của app**, nên nó chứng minh container đọc/ghi được bằng identifier đó — **không** chứng minh tiến trình widget đọc được. Phần đó là bước tay ở 4.3.1 *(design §6.2)*

- [ ] **4.2.5** **P5 (Invariant)** — với mọi cặp (target × cấu hình): `IPHONEOS_DEPLOYMENT_TARGET == "16.4"`
  - Refs: AC-002.5
  - Design: 9
  - File: `Tests/CoreTests/ProjectStructureTests.swift`

- [ ] **4.2.6** **P6 (Invariant)** — với mọi cặp (target × khoá ∈ `{NSAllowsArbitraryLoads, NSExceptionDomains}`): khoá **không tồn tại**
  - Refs: AC-005.1, AC-005.2
  - Design: 9
  - File: `Tests/CoreTests/ProjectStructureTests.swift`

- [ ] **4.2.7** **P7 (Invariant)** — mọi target ở Release có cả hai warnings-as-errors = YES; mọi cấu hình có `SWIFT_STRICT_CONCURRENCY` ∈ `{targeted, complete}`; coverage bật đúng phạm vi; mọi chỗ tắt cảnh báo có comment lý do liền kề
  - Refs: AC-004.1, AC-004.2, AC-004.4, AC-004.5, AC-004.6
  - Design: 9
  - File: `Tests/CoreTests/ProjectStructureTests.swift`

- [ ] **4.2.8** **P8 (Invariant)** — 3 khoá quyền tồn tại ở `Carbina`, không rỗng, không khớp danh sách cụm chung bị cấm; không khoá `NS*UsageDescription` thứ tư ở `Carbina`; **0 khoá** ở `CarbinaWidget`; và với mọi chuỗi sinh thuộc lớp "câu chung"/rỗng, validator trả **fail**
  - Refs: AC-005.5, AC-005.6, AC-005.7
  - Design: 9
  - File: `Tests/CoreTests/ProjectStructureTests.swift`

### 3.3 Xác minh tay và chuyển giao *(design 6.4 + 8.3)*

- [ ] **4.3.1** Chạy **6 bước xác minh tay** của design §6.4 và **lưu bằng chứng từng bước**: (1) `list_schemes` thấy đúng 2 target · (2) `build_sim` Debug + Release 0 cảnh báo · (3) CarPlay simulator: `didConnect` gọi được **và** widget đọc được marker · (4) một lệnh chạy 3 bundle, `LayoutPropertyTests` báo **skipped** · (5) rà bundle 0 hit secret · (6) minimum device = **iPhone 12** trên App Store Connect
  - Refs: AC-002.1, AC-002.6, AC-002.7, AC-003.3, AC-004.3, AC-005.3, AC-006.4
  - Design: 6.4
  - Files: *(bằng chứng — ảnh/đoạn output, không phải file mã)*
  - Sáu AC này **không có đường kiểm tự động ở Phase 1** và **không được** đánh done bằng suy luận *(design §9.1)*
  - Bước 6 nằm **ngoài repo** nên dễ bị bỏ quên nhất trong cả spec; bước 3 là bước duy nhất chứng minh được `AC-003.3` đúng nghĩa "đọc lại từ widget extension"
  - Bước 5 phát hiện secret = **lỗi chặn phát hành**; khắc phục phải gồm **thu hồi key đã lộ**, không chỉ xoá khỏi commit mới *(ERR-PS-004)*

- [ ] **4.3.2** Ghi hợp đồng chuyển giao vào `spec-state.json`: 4 hợp đồng C1–C4 + **3 việc dọn dẹp bắt buộc** của `shared-foundations` (gom 2 literal vào `AppGroupBridge` · xoá marker `handshake.bin` · **giữ** build phase `Verify App Group` và cập nhật để so 3 điểm)
  - Refs: AC-003.5
  - Design: 8.3
  - File: `spec-state.json`
  - Điều kiện nghiệm thu của chuyển giao: sau `shared-foundations`, số điểm khai identifier giảm 4 → **3**. Nếu *tăng*, đó là hồi quy

**Phase Gate 4 (end of Integration phase):** Run XcodeBuildMCP `discover_projs` → `list_schemes` → `build_sim`, then traceability check passes.
Điều kiện pass = **CP-4 + Exit gate** của design §6.5: 3 bundle chạy bằng một lệnh · **8/8 property pass thật** · skeleton báo skipped không phải passed · 6 bước §6.4 có bằng chứng đầy đủ · `validate_traceability.py project-structure` PASSED · `validate_cross_spec.py carplay-ai` PASSED.
Khớp Exit Criteria Phase 1 của roadmap: *`xcodebuild` thành công 0 warning · App Group đọc/ghi được từ cả 2 target*.

---

## Traceability Matrix

| Task ID | AC | Design | Property | Status |
|---|---|---|---|---|
| 2.1.1 | AC-002.1, AC-002.5 | 7.1 | - | pending |
| 2.1.2 | AC-002.1 | 3.1 | - | pending |
| 2.1.3 | AC-002.2, AC-002.3, AC-002.4 | 7.1 | - | pending |
| 2.1.4 | AC-002.8 | 7.1 | - | pending |
| 2.1.5 | AC-002.6 | 7.1 | - | pending |
| 2.2.1 | AC-001.1, AC-001.2, AC-001.3, AC-001.4, AC-001.5, AC-001.6, AC-001.7 | 4.1 | - | pending |
| 2.2.2 | AC-001.8 | 7.2 | - | pending |
| 2.2.3 | AC-001.9 | 7.2 | - | pending |
| 3.1.1 | AC-003.1, AC-003.2 | 4.2 | - | pending |
| 3.1.2 | AC-003.4, AC-005.4 | 4.2 | - | pending |
| 3.1.3 | AC-003.6 | 7.3 | - | pending |
| 3.1.4 | AC-003.3 | 4.5 | - | pending |
| 3.1.5 | AC-003.5 | 8.4 | - | pending |
| 3.2.1 | AC-005.1, AC-005.2 | 4.3 | - | pending |
| 3.2.2 | AC-005.5 | 4.3 | - | pending |
| 3.2.3 | AC-005.6 | 7.4 | - | pending |
| 3.2.4 | AC-005.7 | 4.3 | - | pending |
| 3.3.1 | AC-004.1, AC-004.2 | 4.4 | - | pending |
| 3.3.2 | AC-004.5 | 4.4 | - | pending |
| 3.3.3 | AC-004.4 | 4.4 | - | pending |
| 3.3.4 | AC-004.3 | 7.5 | - | pending |
| 3.3.5 | AC-004.6 | 7.5 | - | pending |
| 4.1.1 | AC-006.1, AC-006.4 | 7.6 | - | pending |
| 4.1.2 | AC-006.5 | 7.6 | - | pending |
| 4.1.3 | AC-006.6 | 7.6 | - | pending |
| 4.1.4 | AC-006.2, AC-006.3 | 7.6 | - | pending |
| 4.1.5 | AC-006.1, AC-006.3 | 7.6 | - | pending |
| 4.2.1 | AC-001.1, AC-001.2, AC-001.3, AC-001.4, AC-001.5, AC-001.6, AC-001.7, AC-001.8, AC-001.9 | 9 | P1 | pending |
| 4.2.2 | AC-003.1, AC-003.2, AC-003.6 | 9 | P2 | pending |
| 4.2.3 | AC-002.2, AC-002.3, AC-002.4, AC-006.6 | 9 | P3 | pending |
| 4.2.4 | AC-003.3, AC-003.4, AC-005.4 | 9 | P4 | pending |
| 4.2.5 | AC-002.5 | 9 | P5 | pending |
| 4.2.6 | AC-005.1, AC-005.2 | 9 | P6 | pending |
| 4.2.7 | AC-004.1, AC-004.2, AC-004.4, AC-004.5, AC-004.6 | 9 | P7 | pending |
| 4.2.8 | AC-005.5, AC-005.6, AC-005.7 | 9 | P8 | pending |
| 4.3.1 | AC-002.1, AC-002.6, AC-002.7, AC-003.3, AC-004.3, AC-005.3, AC-006.4 | 6.4 | - | pending |
| 4.3.2 | AC-003.5 | 8.3 | - | pending |

**Kiểm tra độ phủ hai chiều:**

| Chiều | Kết quả |
|---|---|
| Mọi AC → có task | **42/42** — không AC nào ship mà không có task thực thi |
| Mọi property P# → có task `pbt` | **8/8** — P1→4.2.1 · P2→4.2.2 · P3→4.2.3 · P4→4.2.4 · P5→4.2.5 · P6→4.2.6 · P7→4.2.7 · P8→4.2.8 |
| Mọi task → có ≥1 AC | **37/37** |
| Mọi task → có đúng 1 design section tồn tại | **37/37** — dùng 16 section: `3.1`, `4.1`, `4.2`, `4.3`, `4.4`, `4.5`, `6.4`, `7.1`, `7.2`, `7.3`, `7.4`, `7.5`, `7.6`, `8.3`, `8.4`, `9` |
| AC được phủ **2 lần** (thực thi + property/xác minh) | 35/42 |
| AC chỉ phủ **1 lần** | 7 — AC-001.8 *(2.2.2, và P1 phủ)*, AC-002.7, AC-002.8, AC-005.3, AC-006.2, AC-006.5, AC-003.5 |

**Bảy AC chỉ có một đường phủ — chấp nhận có ý thức, không phải sót:** AC-002.7 *(App Store Connect, ngoài repo)*, AC-005.3 *(nhận dạng secret là heuristic, property sẽ pass giả)*, AC-002.8 *(chưa có API 17.4 nào được dùng ở Phase 1; compiler là điểm chặn thật)*, AC-006.2/AC-006.5 *(tạo phẩm một lần, kiểm bằng chính việc test chạy)*, AC-003.5 *(cần code review, không property-hoá được)*. Lý do đầy đủ ở design §9.1.

---

## Progress

| Section | Total | Done | Status |
|---|---:|---:|---|
| Shared | 8 | 0 | ⬜ |
| Feature | 14 | 0 | ⬜ |
| Integration | 15 | 0 | ⬜ |
| **Tổng** | **37** | **0** | ⬜ |

**Phân bố theo type:** `normal` 29 · `pbt` 8
**Phase gate:** 3 *(Gate 2 sau Shared · Gate 3 sau Feature · Gate 4 sau Integration + Exit gate)*
**Checkpoint:** CP-1 *(8 task)* · CP-2 *(9 task)* · CP-3 *(5 task)* · CP-4 *(15 task)*
