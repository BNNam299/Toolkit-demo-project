# project-structure — Requirements

**Spec ID**: `project-structure` · **Phase**: 1 · **Type**: `infra` · **Priority**: 1
**Depends on**: — (spec đầu tiên) · **Blocks**: `shared-foundations` → toàn bộ 25 spec còn lại
**Duration**: 1 ngày · **Snapshot**: 2.4 / 2026-08-07
**Project docs**: [`../carplay-ai/_INDEX.md`](../carplay-ai/_INDEX.md)

---

## Overview

Dựng bộ khung dự án Xcode cho Carbina: cây thư mục theo `ios-architecture`, **hai target tách biệt** (app iOS và widget extension), App Group làm kênh giao tiếp duy nhất giữa chúng, và cấu hình build/bảo mật ở mức project.

Spec này **không viết một dòng logic nghiệp vụ nào**. Nó tồn tại để mọi spec sau có chỗ đặt code đúng chỗ, và để bốn ràng buộc kỹ thuật quan trọng nhất của dự án được cưỡng chế **ở tầng cấu hình** thay vì trông chờ vào kỷ luật của người viết code: ngưỡng bộ nhớ widget extension, ngưỡng phiên bản iOS, cấm secret trong bundle, và cấm cảnh báo build.

> **Ghi chú về truy vết — đọc trước khi review.** Trong `Project_Implementation_Roadmap.md`, spec này có `covers: {fr: [], uc: [], wf: []}`: nó **không phủ FR, UC hay WF nào**. Đó là đúng — đây là spec hạ tầng, không có bề mặt người dùng.
> Vì vậy trường **Source** của mỗi requirement dưới đây trỏ tới các **NFR** cụ thể trong `Functional_Requirements.md` §3 — những NFR mà acceptance criteria của chúng thuần build/config và **chỉ spec này thoả được** (NFR-007, NFR-010, NFR-013, NFR-021, NFR-022, NFR-024). Mỗi requirement cũng ghi thêm dòng **Enables** liệt kê FR mà nó *mở đường* nhưng **không** thực thi, kèm tên spec thực thi thật.
> Cách ghi Source này là **infra-spec carve-out chính thức** của `gate-requirements`, không phải sai lệch: khi roadmap registry khai một spec với `covers` rỗng thì Source được phép trỏ các NFR ở `Functional_Requirements.md` §3, kèm dòng **Enables (không thực thi)**. Xem `spec-creation-contract` §Infra-spec carve-out; `validate_traceability.py` tự cưỡng chế bằng cách đọc `spec-state.json` → registry, và ghi phần nới lỏng ra warning để còn kiểm lại được.
> Lý do có carve-out: gán một FR không liên quan vào spec hạ tầng chính là kiểu "laundering" mà `gate-wireframes` và `gate-roadmap` cấm. Ghi rõ quan hệ thật tốt hơn thoả câu chữ bằng một tham chiếu sai. Ngược lại, requirement **không có Source nào** vẫn là lỗi chặn, kể cả với spec hạ tầng.

---

## Evidence References

- **Market data from PRD**: Đối thủ dẫn đầu `myCar` đạt ~$700K/tháng và DAU 103K, nhưng **78% review gần nhất là 1★** và **D30 chỉ 4,0%**. Hai nguyên nhân complaint lớn nhất: paywall cứng, và **widget không render đúng trên màn hình xe thật** (cắt chữ trên Jeep Wrangler 2022 màn 8", không hiện trên xe đời 2026, Ram Rebel, Audi). Cả cluster "carplay"/"car play" bị Apple gỡ **42–52%**. *(PRD §4, §13 R-08, R-11)*
- **Vì sao dữ liệu đó dẫn tới spec hạ tầng này**: complaint kỹ thuật số 1 của đối thủ là lỗi render widget, và một trong hai nguyên nhân gốc là **widget extension bị hệ thống thu hồi vì vượt ngưỡng bộ nhớ** — biểu hiện ra ngoài giống hệt lỗi layout. Ngăn chuyện đó bắt đầu từ **tách target và cấm widget extension liên kết framework nặng**, tức là từ file cấu hình project, không phải từ code. *(`Project_Overview.md` §8 rủi ro thực thi A; `FR_widget.md` BR-029.3)*
- **Key KPIs bị spec này ảnh hưởng** *(PRD §12, `Project_Overview.md` §6.1)*:
  | KPI | Mục tiêu | Liên hệ với spec này |
  |---|---|---|
  | **Widget Render Success Rate** | ≥ 90% (T3) · ≥ 95% (T6) | Ngưỡng bộ nhớ widget extension được đặt ở tầng target/entitlements |
  | **Crash-Free Sessions** | ≥ 99,2% (T3) · ≥ 99,5% (T6) | Deployment target + kiểm tra khả dụng API là điều kiện để không crash trên iOS 16.4–17.3 |
  | **Recent 1★ Ratio** | < 20% (T3) · < 15% (T6) | Gián tiếp: mọi lỗi render đều đổ về đây |
- **Source documents**:
  - `carplay-ai/Functional_Requirements.md` §3.1–3.2 — NFR-007, NFR-010, NFR-013, NFR-021, NFR-022, NFR-024
  - `carplay-ai/Project_Overview.md` §3.1 (tech stack), §3.2 (sơ đồ kiến trúc), §3.3 Quyết định 1 (hai ngưỡng iOS), Quyết định 2 (ba runtime một lớp domain), Quyết định 7 (cây thư mục), §8 rủi ro thực thi A
  - `carplay-ai/Project_Implementation_Roadmap.md` §Project Structure, §Phase Timeline P1, §File Breakdown P1
  - `.claude/skills/ios-architecture/SKILL.md` — Structure Compliance Gate
  - `carplay-ai/PRD.md` §9 (ma trận nền tảng, quyền riêng tư & bảo mật), §13 (R-08, R-11)

---

## Requirements

### REQ-001: Cây thư mục chuẩn theo ios-architecture

**User Story:** Với vai trò iOS developer, tôi muốn mọi file mới có **đúng một** vị trí hiển nhiên trong cây thư mục, để 25 spec phía sau không phải tranh luận chỗ đặt file và Structure Compliance Gate chạy được tự động.

**Source**: [NFR-024 *(build hygiene — cấu trúc là điều kiện để rà soát tự động)* · `ios-architecture` Structure Compliance Gate · `Project_Overview.md` §3.3 Quyết định 7]
**Enables (không thực thi):** toàn bộ 26 spec còn lại — mỗi spec đặt file theo cây này. Thực thi thật nằm ở từng spec.

#### Acceptance Criteria

1. **AC-001.1** — WHEN spec này hoàn thành THEN THE SYSTEM SHALL có sẵn các thư mục gốc `App/`, `Core/`, `Features/`, `CarbinaWidget/`, `shared/`, `Resources/`, `Tests/` trong repo.
2. **AC-001.2** — WHEN thư mục `Core/` được tạo THEN THE SYSTEM SHALL chứa đúng 8 thư mục con: `CarPlay/`, `ML/`, `Audio/`, `Entitlement/`, `Analytics/`, `Persistence/`, `Extensions/`, `Utilities/`.
3. **AC-001.3** — WHEN thư mục `Features/` được tạo THEN THE SYSTEM SHALL chứa đúng 9 feature module: `Onboarding/`, `Home/`, `SoundLibrary/`, `WidgetBuilder/`, `VoiceGreeting/`, `Paywall/`, `Settings/`, `Diagnostics/`, `CarPlayDashboard/`.
4. **AC-001.4** — WHEN một feature module được tạo THEN THE SYSTEM SHALL chứa các thư mục con `Views/`, `ViewModels/`, `Models/`, `Services/` — trừ `Home/` và `VoiceGreeting/` và `Paywall/` và `Settings/` và `Diagnostics/` và `CarPlayDashboard/` chỉ cần thư mục con mà roadmap §Project Structure liệt kê cho chúng.
5. **AC-001.5** — WHEN thư mục `shared/` được tạo THEN THE SYSTEM SHALL chứa `Components/` (với 6 thư mục con `Buttons/`, `Cards/`, `Rows/`, `Inputs/`, `Feedback/`, `CarPlay/`), `Styles/`, `Modifiers/`.
6. **AC-001.6** — WHEN thư mục `Resources/` được tạo THEN THE SYSTEM SHALL chứa `Assets.xcassets/`, `Sounds/`, `VehicleImages/`, `GreetingVariants/`, và ba thư mục localization `en.lproj/`, `es.lproj/`, `pt-BR.lproj/`.
7. **AC-001.7** — WHEN thư mục `Tests/` được tạo THEN THE SYSTEM SHALL chứa `CoreTests/`, `CarPlayLayoutTests/`, `FeatureTests/`.
8. **AC-001.8** — IF một thư mục trong cây trên rỗng sau khi spec hoàn thành THEN THE SYSTEM SHALL vẫn giữ nó trong repo bằng một file giữ chỗ (`.gitkeep`), để cây có mặt đầy đủ trước khi spec sau bắt đầu.
9. **AC-001.9** — WHEN cây thư mục được rà soát THEN THE SYSTEM SHALL **không** chứa thư mục nào ngoài danh sách ở roadmap §Project Structure.

#### States & Edge Cases
- **Loading:** N/A — thao tác tạo cây thư mục là đồng bộ, không có trạng thái chờ mà người dùng hay agent quan sát được.
- **Empty:** AC-001.8 — thư mục rỗng được giữ bằng `.gitkeep` thay vì biến mất khỏi repo.
- **Error / failure:** AC-001.9 — cây có thư mục lạ là trạng thái lỗi và phải bị chặn ở review.
- **Offline / stale:** N/A — thao tác cục bộ, không phụ thuộc mạng.
- **Permission-denied:** N/A — không có quyền hệ thống nào liên quan tới việc tạo cây thư mục.

#### Validation Rules
N/A — no user input. Requirement này không nhận đầu vào từ người dùng; đầu vào là bảng thư mục cố định ở roadmap §Project Structure.

#### Wireframe Affordance Coverage
N/A — infra spec, `covers.wf = []`. Spec này **không sở hữu màn hình nào**; 30/30 WF đã được sở hữu bởi 19 spec loại `feature` khác (xem roadmap §Feature→Screen Mapping). Không có affordance nào bị bỏ rơi ở đây.

---

### REQ-002: Hai target tách biệt với ràng buộc phụ thuộc một chiều

**User Story:** Với vai trò iOS developer, tôi muốn widget extension là một target riêng **không** liên kết được framework nặng, để nó không bao giờ vượt ngưỡng bộ nhớ và bị hệ thống thu hồi — vì lỗi đó biểu hiện ra ngoài giống hệt lỗi layout và sẽ làm chẩn đoán R-11 sai hướng.

**Source**: [**NFR-007** (AC-NFR-007.1 ≤ 25MB · AC-NFR-007.4 widget không nạp Core ML, không gọi mạng) · **NFR-022** (AC-NFR-022.1 không crash trên iOS 16.4–17.3) · `Project_Overview.md` §3.3 Quyết định 2]
**Enables (không thực thi):** FR-029 *(render widget — `widget-render`)*, FR-030 *(giảm cấp layout — `widget-render`)*

#### Acceptance Criteria

1. **AC-002.1** — WHEN Xcode project được tạo THEN THE SYSTEM SHALL có đúng hai target sản phẩm: `Carbina` (iOS app) và `CarbinaWidget` (widget extension).
2. **AC-002.2** — WHEN target `CarbinaWidget` được cấu hình THEN THE SYSTEM SHALL **không** liên kết `CoreML`, `AVFoundation`, `EventKit`, `CoreLocation`, hay bất kỳ framework mạng nào.
3. **AC-002.3** — WHEN target `CarbinaWidget` được cấu hình THEN THE SYSTEM SHALL chỉ liên kết `WidgetKit`, `SwiftUI` và các file thuộc `Core/CarPlay/` và `shared/Styles/`.
4. **AC-002.4** — IF một file thuộc `Core/ML/`, `Core/Audio/`, `Core/Analytics/`, hoặc `Core/Entitlement/` được thêm vào membership của target `CarbinaWidget` THEN THE SYSTEM SHALL coi đó là lỗi cấu hình chặn merge.
5. **AC-002.5** — WHEN cả hai target được build THEN THE SYSTEM SHALL dùng chung một Deployment Target là **iOS 16.4**.
6. **AC-002.6** — WHEN target `Carbina` được cấu hình THEN THE SYSTEM SHALL khai báo `CPTemplateApplicationSceneSessionRoleApplication` trong `Info.plist` để CarPlay scene khởi tạo được.
7. **AC-002.7** — WHEN thiết bị tối thiểu được khai báo trên App Store Connect THEN THE SYSTEM SHALL là **iPhone 12** trở lên (yêu cầu Apple Neural Engine).
8. **AC-002.8** — WHERE một API chỉ có từ iOS 17.4 được dùng THE SYSTEM SHALL bọc nó trong kiểm tra khả dụng `if #available(iOS 17.4, *)`.

#### States & Edge Cases
- **Loading:** N/A — cấu hình target là thuộc tính tĩnh của project file, không có trạng thái chờ.
- **Empty:** N/A — không có tập dữ liệu nào có thể rỗng ở requirement này.
- **Error / failure:** AC-002.4 — file sai target membership là trạng thái lỗi chặn merge.
- **Offline / stale:** N/A — cấu hình build cục bộ.
- **Permission-denied:** N/A — không có quyền hệ thống liên quan.

#### Validation Rules
N/A — no user input. Đầu vào là bảng cấu hình target, không phải dữ liệu người dùng nhập.

#### Wireframe Affordance Coverage
N/A — infra spec, không sở hữu màn hình. WF-017 (CarPlay Widget) mà target này *chạy* thuộc spec `widget-render`.

---

### REQ-003: App Group là kênh giao tiếp duy nhất giữa hai target

**User Story:** Với vai trò iOS developer, tôi muốn app và widget extension chỉ trao đổi dữ liệu qua **một** App Group container, để không tồn tại đường đi thứ hai mà spec sau vô tình tạo ra rồi gây lệch dữ liệu giữa hai bề mặt.

**Source**: [**NFR-007** (AC-NFR-007.2 ảnh ≤ 2MB trong container) · **NFR-010** (AC-NFR-010.2 Data Protection cho file) · `Project_Overview.md` §3.2 "Widget extension là một tiến trình riêng"]
**Enables (không thực thi):** FR-022 *(lưu cấu hình widget vào App Group — `widget-builder`)*, FR-013 *(gán sound ghi App Group — `sound-library`)*, FR-061 *(theme dùng chung — `settings-presentation`)*

#### Acceptance Criteria

1. **AC-003.1** — WHEN cả hai target được cấu hình THEN THE SYSTEM SHALL bật capability App Group với **cùng một identifier** `group.app.carbina.shared` trên cả hai.
2. **AC-003.2** — WHEN App Group được bật THEN THE SYSTEM SHALL khai báo identifier đó trong **cả hai** file `.entitlements` (`App/Carbina.entitlements` và `CarbinaWidget/CarbinaWidget.entitlements`).
3. **AC-003.3** — WHEN spec này hoàn thành THEN THE SYSTEM SHALL chứng minh container đọc và ghi được **từ cả hai target** bằng một lần ghi từ app rồi đọc lại từ widget extension.
4. **AC-003.4** — WHEN file được tạo trong App Group container THEN THE SYSTEM SHALL đặt thuộc tính Data Protection tối thiểu `NSFileProtectionCompleteUntilFirstUserAuthentication`.
5. **AC-003.5** — IF một cơ chế chia sẻ dữ liệu khác giữa hai target được thêm (`UserDefaults` chuẩn, Keychain sharing, Darwin notification cho dữ liệu, file ngoài container) THEN THE SYSTEM SHALL coi đó là lỗi kiến trúc chặn merge.
6. **AC-003.6** — WHEN App Group identifier được đặt THEN THE SYSTEM SHALL khớp chính xác giữa hai entitlements file và cấu hình trên Apple Developer portal — lệch một ký tự làm widget đọc container rỗng mà **không** báo lỗi.

#### States & Edge Cases
- **Loading:** N/A — truy cập container là đồng bộ ở tầng cấu hình.
- **Empty:** AC-003.3 — container rỗng ở thời điểm spec này kết thúc là **trạng thái đúng và mong đợi**; dữ liệu thật do spec sau ghi vào.
- **Error / failure:** AC-003.6 — identifier lệch dẫn tới container rỗng **im lặng**; đây là chế độ thất bại nguy hiểm nhất của requirement này vì nó không phát ra lỗi.
- **Offline / stale:** N/A — App Group là lưu trữ cục bộ, không phụ thuộc mạng.
- **Permission-denied:** N/A — App Group không cần người dùng cấp quyền; nó là capability ở tầng ký ứng dụng.

#### Validation Rules
N/A — no user input.

#### Wireframe Affordance Coverage
N/A — infra spec, không sở hữu màn hình.

---

### REQ-004: Cấu hình build không cho lọt cảnh báo

**User Story:** Với vai trò iOS developer, tôi muốn cảnh báo build làm hỏng build ngay từ ngày đầu, để dự án không tích lũy một đống cảnh báo rồi tới lúc submit mới phải dọn — và để điều kiện "0 cảnh báo Xcode" của cổng phát hành không bao giờ trở thành việc lớn.

**Source**: [**NFR-024** (AC-NFR-024.1 coverage ≥ 80% cho `Core/` · AC-NFR-024.2 **0 cảnh báo Xcode, chặn submission**)]
**Enables (không thực thi):** không FR nào — đây là ràng buộc chất lượng áp lên mọi spec.

#### Acceptance Criteria

1. **AC-004.1** — WHEN cấu hình build được thiết lập THEN THE SYSTEM SHALL bật `SWIFT_TREAT_WARNINGS_AS_ERRORS = YES` cho cấu hình Release.
2. **AC-004.2** — WHEN cấu hình build được thiết lập THEN THE SYSTEM SHALL bật `GCC_TREAT_WARNINGS_AS_ERRORS = YES` cho cấu hình Release.
3. **AC-004.3** — WHEN project được build ở cả Debug và Release THEN THE SYSTEM SHALL hoàn thành với **0 cảnh báo**.
4. **AC-004.4** — WHEN scheme test được cấu hình THEN THE SYSTEM SHALL bật thu thập code coverage, giới hạn phạm vi đo ở target chứa `Core/`.
5. **AC-004.5** — WHEN Swift language version được đặt THEN THE SYSTEM SHALL dùng chế độ nghiêm ngặt nhất mà toolchain hiện tại hỗ trợ và **không** tắt bất kỳ cảnh báo an toàn nào (`strict concurrency` ở mức tối thiểu `targeted`).
6. **AC-004.6** — IF một cảnh báo được tắt bằng pragma hoặc build setting THEN THE SYSTEM SHALL kèm một dòng chú thích nêu lý do ngay tại chỗ tắt.

#### States & Edge Cases
- **Loading:** N/A — cấu hình build là tĩnh.
- **Empty:** N/A.
- **Error / failure:** AC-004.3 — build có cảnh báo là trạng thái thất bại; Release build sẽ **dừng** vì AC-004.1/.2.
- **Offline / stale:** N/A — build cục bộ.
- **Permission-denied:** N/A.

#### Validation Rules
N/A — no user input.

#### Wireframe Affordance Coverage
N/A — infra spec, không sở hữu màn hình.

---

### REQ-005: Cấu hình bảo mật ở tầng project

**User Story:** Với vai trò người dùng quan tâm quyền riêng tư, tôi muốn app không mang theo secret nào trong gói cài và không mở ngoại lệ mạng nào, để cam kết "dữ liệu không rời thiết bị" của app có nền tảng kỹ thuật chứ không chỉ là một câu trong onboarding.

**Source**: [**NFR-010** (AC-NFR-010.2 Data Protection · AC-NFR-010.3 **không API key plaintext trong bundle**) · **NFR-013** (AC-NFR-013.1 TLS ≥ 1.2 · AC-NFR-013.2 **không `NSAllowsArbitraryLoads`, không exception domain**)]
**Enables (không thực thi):** FR-066 *(telemetry không PII — `telemetry-core`)*, FR-057 *(xoá dữ liệu on-device — `privacy-data`)*

#### Acceptance Criteria

1. **AC-005.1** — WHEN `Info.plist` của cả hai target được rà soát THEN THE SYSTEM SHALL **không** chứa khoá `NSAllowsArbitraryLoads`.
2. **AC-005.2** — WHEN `Info.plist` của cả hai target được rà soát THEN THE SYSTEM SHALL **không** chứa bất kỳ exception domain nào trong `NSAppTransportSecurity`.
3. **AC-005.3** — WHEN bundle sản phẩm được rà soát trước mỗi lần submit THEN THE SYSTEM SHALL **không** chứa API key, secret, hay token ở dạng plaintext trong `Info.plist`, tệp cấu hình, hay hằng số trong mã.
4. **AC-005.4** — WHEN capability của target `Carbina` được cấu hình THEN THE SYSTEM SHALL bật Data Protection ở mức tối thiểu `NSFileProtectionCompleteUntilFirstUserAuthentication`.
5. **AC-005.5** — WHEN `Info.plist` khai báo chuỗi mô tả quyền THEN THE SYSTEM SHALL cung cấp `NSLocationWhenInUseUsageDescription`, `NSCalendarsUsageDescription`, `NSPhotoLibraryUsageDescription`, và mỗi chuỗi SHALL nêu **lý do cụ thể** thay vì câu chung như "để cải thiện trải nghiệm".
6. **AC-005.6** — IF một khoá quyền được khai báo trong `Info.plist` mà app **không** thực sự dùng THEN THE SYSTEM SHALL gỡ khoá đó — khai quyền thừa là rủi ro bị App Review từ chối (R-02).
7. **AC-005.7** — WHEN target `CarbinaWidget` được rà soát THEN THE SYSTEM SHALL **không** khai báo bất kỳ chuỗi mô tả quyền nào, vì widget extension không yêu cầu quyền nào.

#### States & Edge Cases
- **Loading:** N/A — cấu hình tĩnh.
- **Empty:** AC-005.7 — danh sách quyền của widget extension **rỗng là trạng thái đúng**, không phải thiếu sót.
- **Error / failure:** AC-005.3 — phát hiện secret plaintext là **lỗi chặn phát hành**, không phải cảnh báo.
- **Offline / stale:** N/A.
- **Permission-denied:** AC-005.5 — chuỗi mô tả quyền là thứ người dùng đọc **trước khi** từ chối; chất lượng chuỗi này quyết định tỉ lệ cấp quyền. Hành vi sau khi bị từ chối thuộc FR-008 (`onboarding-flow`), **không** thuộc spec này.

#### Validation Rules
N/A — no user input. *(Chuỗi mô tả quyền là nội dung do đội viết, không phải đầu vào runtime.)*

#### Wireframe Affordance Coverage
N/A — infra spec, không sở hữu màn hình. Màn hình hiển thị lý do quyền là WF-005 và WF-022, thuộc spec `onboarding-flow`.

---

### REQ-006: Hạ tầng test cho ràng buộc layout CarPlay

**User Story:** Với vai trò QA, tôi muốn test target dành riêng cho layout CarPlay tồn tại **trước khi** một dòng layout nào được viết, để ràng buộc "không hằng số kích thước màn hình xe" có nơi được kiểm tự động thay vì phụ thuộc vào việc ai đó nhớ rà tay.

**Source**: [**NFR-021** (AC-NFR-021.1 **0 hằng số kích thước màn hình xe** trong code layout) · **NFR-024** (AC-NFR-024.3 property-based test với **mọi** cặp (width, height) hợp lệ)]
**Enables (không thực thi):** FR-029, FR-030 *(`widget-render` — spec đó viết nội dung test; spec này chỉ dựng chỗ cho nó)*

#### Acceptance Criteria

1. **AC-006.1** — WHEN spec này hoàn thành THEN THE SYSTEM SHALL có ba test target/bundle tương ứng `Tests/CoreTests/`, `Tests/CarPlayLayoutTests/`, `Tests/FeatureTests/`.
2. **AC-006.2** — WHEN `Tests/CarPlayLayoutTests/` được tạo THEN THE SYSTEM SHALL chứa file `LayoutPropertyTests.swift` với ba hàm test rỗng đã đặt tên: `testNoOverflowForAnyBounds()`, `testTextNeverBelow16pt()`, `testNoHardcodedSizeConstants()`.
3. **AC-006.3** — WHEN ba hàm test đó tồn tại ở dạng rỗng THEN THE SYSTEM SHALL đánh dấu chúng `XCTSkip` kèm lý do `"chờ widget-render (Phase 3)"` — để suite xanh mà **không** giả vờ đã kiểm gì.
4. **AC-006.4** — WHEN test scheme được cấu hình THEN THE SYSTEM SHALL chạy được cả ba bundle bằng một lệnh duy nhất.
5. **AC-006.5** — WHEN thư viện property-based testing được thêm THEN THE SYSTEM SHALL dùng **SwiftCheck ≥ 0.12.0** qua SPM (theo `.claude/shared/PBT_GUIDE.md`) và khai báo nó **chỉ** cho test target, không cho target sản phẩm.
6. **AC-006.6** — IF một test target liên kết vào target `CarbinaWidget` THEN THE SYSTEM SHALL coi đó là lỗi cấu hình — test không được làm tăng kích thước widget extension.

#### States & Edge Cases
- **Loading:** N/A.
- **Empty:** AC-006.3 — test rỗng là trạng thái đúng ở Phase 1; điều quan trọng là chúng **bị skip có lý do**, không phải pass giả.
- **Error / failure:** AC-006.6 — test target liên kết sai là lỗi cấu hình chặn merge.
- **Offline / stale:** N/A — trừ khi thư viện PBT lấy qua SPM; khi đó cần mạng **một lần** lúc resolve dependency, và bản resolve được commit (`Package.resolved`) để build sau đó không cần mạng.
- **Permission-denied:** N/A.

#### Validation Rules
N/A — no user input.

#### Wireframe Affordance Coverage
N/A — infra spec, không sở hữu màn hình.

---

## Non-Functional Requirements

NFR của spec này là **ràng buộc lên chính quá trình dựng khung**, phân biệt với 24 NFR sản phẩm ở `Functional_Requirements.md` §3 (những cái đó là *nguồn* của các requirement trên).

- **NFR-PS-001 · Build performance:** Clean build của cả hai target hoàn thành trong **< 90 giây** trên máy dev chuẩn (Apple Silicon, 16GB). Nếu vượt ngưỡng này ngay khi project còn rỗng thì cấu hình đang có vấn đề.
- **NFR-PS-002 · Reproducibility:** Clone repo mới và build thành công **không cần thao tác thủ công nào** ngoài `open Carbina.xcodeproj`. Số bước thiết lập thủ công = **0**.
- **NFR-PS-003 · Security:** Số secret/API key dạng plaintext trong repo và trong bundle = **0**, kiểm bằng rà soát trước mỗi lần submit *(AC-005.3)*.
- **NFR-PS-004 · Reliability:** Widget extension khởi tạo được trong **< 200ms** với cấu hình rỗng, và mức bộ nhớ ở trạng thái rỗng **≤ 5MB** — tức còn ≥ 20MB dư địa cho ngân sách 25MB của NFR-007.
- **NFR-PS-005 · Maintainability:** Số thư mục nằm ngoài cây đã định = **0** *(AC-001.9)*. Structure Compliance Gate của `ios-architecture` chạy sạch.
- **NFR-PS-006 · Accessibility:** N/A ở spec này — **không có bề mặt người dùng nào** được tạo. Ràng buộc accessibility (VoiceOver, Dynamic Type, tương phản ≥ 4,5:1, target ≥ 44pt) áp dụng từ `shared-foundations` trở đi, nơi component đầu tiên xuất hiện. Ghi lại ở đây để chứng minh đã cân nhắc chứ không bỏ sót.
- **NFR-PS-007 · Privacy / PII:** N/A ở spec này — không xử lý dữ liệu người dùng nào. Nền tảng cho cam kết privacy nằm ở REQ-005 (Data Protection, ATS, không secret).
- **NFR-PS-008 · Offline:** Build và test chạy được **không cần mạng** sau lần resolve dependency đầu tiên; `Package.resolved` được commit *(xem REQ-006 States)*.
