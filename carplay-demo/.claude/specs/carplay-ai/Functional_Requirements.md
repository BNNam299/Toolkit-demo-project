# Carbina: Car Dashboard & Widgets — Functional Requirements

**Document Version**: 2.4
**Snapshot Date**: 2026-08-07 (đồng bộ với PRD v2.4 · Project_Overview v2.4 · Use_Cases v2.4)
**Ngày tạo file**: 2026-08-17
**Status**: Draft — chờ PO review
**Dependencies**: [`PRD.md`](./PRD.md) v2.4 · [`Project_Overview.md`](./Project_Overview.md) v2.4 · [`Use_Cases.md`](./Use_Cases.md) v2.4

> **File này là INDEX.** Theo quy tắc **Sub-Spec Splitting** của `project-docs-contract` (nhóm FR > 5 requirement phải tách file riêng), toàn bộ 7 nhóm FR đều vượt ngưỡng nên nội dung chi tiết nằm ở 7 file `FR_*.md`. File này giữ: §1 giới thiệu · §2 index + ma trận truy vết · §2 bis Component Behavior Matrix · §2 ter Context-Dependent Behaviors · §3 NFR · §4 tổng hợp. **ID là duy nhất trên toàn bộ các file** — `FR-029` là `FR-029` bất kể nằm ở file nào.

---

## 1. Introduction

### 1.1 Purpose

Tài liệu này đặc tả **hệ thống phải làm gì**, nối nhu cầu người dùng (`Use_Cases.md`) với thiết kế kỹ thuật (`spec-design` ở giai đoạn thi công). Mỗi FR truy vết về ít nhất một UC; mỗi UC được phủ bởi ít nhất một FR. Đây là hợp đồng truy vết trung tâm của cả bộ tài liệu.

Tài liệu này **không** quyết định layout (thuộc `Wireframes.md`), **không** quyết định đường điều hướng (thuộc `UX_Flows.md`), và **không** quyết định kiến trúc triển khai (thuộc `Project_Overview.md` §3).

### 1.2 Scope

- **66 FR** phủ 36 UC (`FR-001` → `FR-066`). Ngưỡng sàn theo scale Medium là 15–35; mục tiêu chất lượng sản phẩm theo `project-docs-contract` là 50–100 ⇒ 66 nằm trong dải mục tiêu.
- **24 NFR** (`NFR-001` → `NFR-024`) phủ Performance · Security · Usability · Reliability · Compatibility · Scalability · Quality.
- **166 AC** được **mang nguyên văn** từ `Use_Cases.md` §2, **không đánh số lại và không viết lại câu**.
- Phạm vi thi công: **FR-001 → FR-062 và FR-066** thuộc MVP 1. **FR-063** thuộc MVP 2. **FR-064, FR-065** thuộc MVP 3.
- **F11 (Crash Reporting)** của PRD §7 không có UC vì không có bề mặt người dùng — nó được phủ bằng **NFR-017** và **NFR-018**, đúng như đã ghi trước ở `Use_Cases.md` §1.2.

### 1.3 Document Conventions

- **FR-XXX**: Functional Requirement (tuần tự FR-001 → FR-066)
- **NFR-XXX**: Non-Functional Requirement (NFR-001 → NFR-024)
- **BR-XXX.Y**: Business Rule của FR-XXX — điều kiện **hệ thống phải cưỡng chế**
- **VR-XXX.Y**: Validation Rule của FR-XXX — quy tắc kiểm tra dữ liệu vào
- **ERR-XXX.Y**: Error Scenario của FR-XXX — dẫn xuất 1:1 từ một `AF-xxx.y` của UC nguồn
- **AC-XXX.Y**: Acceptance Criterion — **mang nguyên từ `Use_Cases.md`**, giữ đúng số của UC gốc (AC gắn với UC, không gắn với FR)
- **Priority**: High (MVP, chặn phát hành) / Medium (MVP nhưng cắt được qua Scope Decision Record) / Low (post-MVP)
- **Status**: Planned / In Progress / Completed / Deferred — toàn bộ hiện ở `Planned`
- **Ký hiệu bề mặt**: 📱 iPhone · 🚗 CarPlay. Mọi FR có 🚗 chịu ràng buộc "người dùng đang lái": không modal, không nhập liệu, tối đa một chạm.

> **Về số của AC**: `AC-015.7` là criterion thứ 7 của **UC-015**, và nó xuất hiện trong **FR-029** (FR dẫn xuất từ UC-015). Số của AC **không** khớp số của FR — đó là chủ ý, để AC luôn truy được về UC gốc dù FR có được tách hay gộp.

---

## 2. Functional Requirements

### 2.0 Index sub-spec

| Sub-spec | Nhóm | FR | UC nguồn | Số FR |
|---|---|---|---|---|
| [`FR_onboarding.md`](./FR_onboarding.md) | Onboarding & Thiết Lập Xe | FR-001 → FR-009 | UC-001 → UC-005 | 9 |
| [`FR_sound.md`](./FR_sound.md) | Âm Thanh Lên/Xuống Xe | FR-010 → FR-020 | UC-006 → UC-011 | 11 |
| [`FR_widget.md`](./FR_widget.md) | Widget CarPlay & Tương Thích | FR-021 → FR-032 | UC-012 → UC-017 | 12 |
| [`FR_voice_dashboard.md`](./FR_voice_dashboard.md) | Giọng Chào AI & Dashboard Ngữ Cảnh | FR-033 → FR-042 | UC-018 → UC-023 | 10 |
| [`FR_monetization.md`](./FR_monetization.md) | Gói Free, Paywall & Thanh Toán | FR-043 → FR-054 | UC-024 → UC-030 | 12 |
| [`FR_settings_privacy.md`](./FR_settings_privacy.md) | Ngôn Ngữ, Quyền Riêng Tư, Phản Hồi & Telemetry | FR-055 → FR-062, FR-066 | UC-004, UC-017, UC-026, UC-029, UC-031 → UC-033, UC-036 | 9 |
| [`FR_postmvp.md`](./FR_postmvp.md) | Post-MVP | FR-063 → FR-065 | UC-034, UC-035 | 3 |

**Tổng: 66 FR.**

### 2.1 Ma trận truy vết UC → FR

Mọi UC ở `Use_Cases.md` §2 đều có ≥ 1 FR. Không có UC nào không được phủ; không có FR nào không có UC nguồn.

| UC | UC Name | FR phủ UC này | Số FR |
|---|---|---|---|
| UC-001 | Hoàn tất onboarding trong 5 bước | FR-001, FR-002, FR-003, FR-009 | 4 |
| UC-002 | Chọn xe của mình | FR-004, FR-005 | 2 |
| UC-003 | Báo xe không có trong thư viện | FR-006 | 1 |
| UC-004 | Cấp quyền sau khi hiểu rõ lý do | FR-007, FR-062 | 2 |
| UC-005 | Dùng app dù đã từ chối mọi quyền | FR-008 | 1 |
| UC-006 | Nghe thử âm thanh trước khi chọn | FR-010, FR-011, FR-012 | 3 |
| UC-007 | Gán âm thanh cho sự kiện Connect | FR-013 | 1 |
| UC-008 | Gán âm thanh cho Disconnect và Arrive | FR-014 | 1 |
| UC-009 | Điều chỉnh âm lượng sound độc lập | FR-015 | 1 |
| UC-010 | Nghe sound khi lên xe không bị nhạc lấn | FR-016, FR-017, FR-018 | 3 |
| UC-011 | Nghe sound xuống xe đúng lúc tắt máy | FR-019, FR-020 | 2 |
| UC-012 | Tạo widget đầu tiên | FR-021, FR-022, FR-023, FR-024 | 4 |
| UC-013 | Xem trước widget theo tỉ lệ màn hình xe | FR-025, FR-026 | 2 |
| UC-014 | Chọn ảnh xe hoặc ảnh cá nhân | FR-027, FR-028 | 2 |
| UC-015 | Xem widget hoạt động trên màn hình xe | FR-029, FR-030 | 2 |
| UC-016 | Phục hồi khi widget không render được | FR-031 | 1 |
| UC-017 | Chẩn đoán tương thích và gửi báo cáo | FR-032, FR-066 | 2 |
| UC-018 | Bật hoặc tắt hoàn toàn giọng chào | FR-033 | 1 |
| UC-019 | Chọn nguồn ngữ cảnh cho giọng chào | FR-034, FR-035 | 2 |
| UC-020 | Nghe thử giọng chào trước khi lên xe | FR-036 | 1 |
| UC-021 | Nghe giọng chào cá nhân hóa khi lên xe | FR-037, FR-038, FR-039 | 3 |
| UC-022 | Xem dashboard tự sắp xếp theo ngữ cảnh | FR-040, FR-041 | 2 |
| UC-023 | Chạm thẻ gợi ý trên dashboard | FR-042 | 1 |
| UC-024 | Dùng gói Free để tự xác nhận app chạy | FR-043, FR-044, FR-045 | 3 |
| UC-025 | Xem bảng giá minh bạch | FR-046, FR-047 | 2 |
| UC-026 | Xác nhận giá cuối trước khi trả tiền | FR-048, FR-049, FR-050, FR-066 | 4 |
| UC-027 | Bắt đầu trial 7 ngày | FR-051 | 1 |
| UC-028 | Nhận nhắc trước khi hết trial | FR-052 | 1 |
| UC-029 | Quản lý hoặc huỷ đăng ký | FR-053, FR-066 | 2 |
| UC-030 | Mua gói Lifetime một lần | FR-054 | 1 |
| UC-031 | Đổi ngôn ngữ app | FR-055, FR-056, FR-061 | 3 |
| UC-032 | Xoá toàn bộ dữ liệu on-device | FR-057, FR-058, FR-066 | 3 |
| UC-033 | Gửi đánh giá hoặc phản hồi | FR-059, FR-060 | 2 |
| UC-036 | Đổi theme của app | FR-061 | 1 |
| UC-034 | Gọi nhanh liên hệ từ màn hình xe *(MVP 2)* | FR-063 | 1 |
| UC-035 | Đồng bộ cấu hình qua cloud *(MVP 3)* | FR-064, FR-065 | 2 |

**Forward check**: 36/36 UC có ≥ 1 FR ⇒ **Pass**.
**Backward check**: 66/66 FR có trường `Source UC` hợp lệ ⇒ **Pass** (chi tiết ở §4.3).

### 2.2 Ma trận truy vết Secondary Action → FR

Nhóm dễ bị rơi nhất khi chuyển sang wireframe là **hành động phụ** trong `Use_Cases.md` §4 (Layer 2/3/4). Bảng này chứng minh từng hành động phụ đều có FR hoặc bước Processing kèm AC — không có hành động nào chỉ tồn tại trong mô tả màn hình.

| Hành động phụ (nguồn: UC §4) | Màn hình | Được phủ bởi |
|---|---|---|
| Phục hồi giao dịch | WF-002 Layer 4, WF-010 Layer 4, WF-025 Layer 4 | **FR-003** (trong onboarding) · **FR-053** (từ paywall và sheet đăng ký) |
| Bỏ qua một bước onboarding / "Chọn sau" | WF-003 Layer 4, WF-004 Layer 4 | **FR-002** Processing 4 · **FR-013** BR-013.2 |
| "Không tìm thấy xe của tôi" | WF-003 Layer 4 | **FR-006** |
| Tìm kiếm hãng/model | WF-003 Layer 2 | **FR-004** Processing 2, VR-004.1 |
| Đổi xe sau khi đã chọn | WF-006 Layer 2 | **FR-004** Processing 6 (AF-002.2) |
| "Tìm hiểu thêm" về một quyền | WF-005 Layer 2 | **FR-007** Processing 3 |
| "Bỏ qua tất cả" quyền | WF-005 Layer 4 | **FR-007** BR-007.3 · **FR-008** |
| Lối vào cấp quyền từ Settings | WF-012 Layer 3 | **FR-062** |
| Nghe thử inline trong danh sách | WF-007 Layer 2 | **FR-011** |
| Chuyển preset trước/sau trong sheet | WF-020 Layer 3 | **FR-012** Processing 3 |
| Chọn "Không dùng" cho một sự kiện sound | WF-007 Layer 2 | **FR-013** BR-013.2 · **FR-014** BR-014.1 |
| Nút âm lượng ở thanh trên thư viện | WF-007 Layer 4 | **FR-015** Processing 1 |
| Điều chỉnh âm lượng trong sheet nghe thử | WF-020 Layer 2 | **FR-015** Processing 2 |
| Đổi widget nhanh từ thẻ Home | WF-006 Layer 2 | **FR-021** Processing 6 |
| Đổi loại widget / ảnh ngay trong preview | WF-023 Layer 4 | **FR-025** Processing 5 (AF-013.2) |
| Duyệt ảnh xe theo model (không cần quyền ảnh) | WF-024 Layer 3 | **FR-027** Processing 2 |
| Xoay ảnh, đặt lại khung crop | WF-024 Layer 2 | **FR-027** Processing 4 |
| Bật/tắt lớp thông tin widget trong preview | WF-023 Layer 2 | **FR-026** Processing 4 |
| Chuyển dark/light trong preview | WF-023 Layer 3 | **FR-025** Processing 4 |
| Sao chép dữ liệu chẩn đoán | WF-014 Layer 4 | **FR-032** Processing 6 |
| Xoá lịch sử chẩn đoán | WF-014 Layer 4 | **FR-032** Processing 7 |
| Bỏ tick một mục dữ liệu trước khi gửi báo cáo | WF-028 Layer 2 | **FR-032** Processing 5, VR-032.2 |
| Thêm ghi chú vào báo cáo | WF-028 Layer 2 | **FR-032** VR-032.1 |
| Xem giá trị thật từng trường dữ liệu | WF-028 Layer 3 | **FR-032** Processing 4 |
| Nghe thử giọng chào | WF-009 Layer 2 | **FR-036** |
| Xem ví dụ câu chào của từng nguồn | WF-009 Layer 3 | **FR-034** Processing 2 |
| Công tắc chính giọng chào | WF-009 Layer 4 / WF-009 Zone D | **FR-033** |
| So sánh các gói | WF-010 Layer 3 | **FR-046** Processing 4 |
| "Tiếp tục dùng gói Free" | WF-010 Layer 4 | **FR-045** BR-045.3 |
| Xem điều khoản / chính sách hoàn tiền | WF-011 Layer 4, WF-010 Zone D | **FR-048** Processing 5 |
| Xem tính năng đang có của gói hiện tại | WF-025 Layer 3 | **FR-053** Processing 3 |
| Huỷ đăng ký | WF-025 Layer 2, WF-013 Zone B | **FR-053** |
| "Nhắc sau" | WF-013 Zone B | **FR-052** BR-052.2 |
| Đổi theme | WF-012 Layer 2 | **FR-061** |
| Chọn ngôn ngữ / "Theo hệ thống" | WF-012 Layer 2, WF-026 | **FR-055** |
| Xoá dữ liệu học | WF-012 Layer 4, WF-029 | **FR-057** |
| "Xoá cả cấu hình" (lựa chọn thứ hai) | WF-029 Zone D | **FR-058** |
| "Đánh giá Carbina" trong Settings | WF-012 Layer 3 | **FR-059** Processing 5 |
| Chọn mức hài lòng trên overlay | WF-030 Layer 4 | **FR-059** |
| Kênh phản hồi khi không hài lòng | WF-030 → WF-028 | **FR-060** |
| "Hoàn tác" trên toast | WF-030 Layer 2 | **FR-058** ERR-058.2 |
| Kéo xuống làm mới trạng thái Home | WF-006 (SF-001) | **FR-009** Processing 5 |
| Xem "cái gì được đồng bộ / không" | WF-015 Layer 3 | **FR-064** Processing 3 |
| Đăng xuất | WF-015 Layer 2 | **FR-064** Processing 5 |
| Xoá tài khoản và dữ liệu cloud | WF-015 Layer 4 | **FR-065** |

**Kết quả**: 45/45 hành động phụ đã liệt kê ở `Use_Cases.md` §4 đều có FR hoặc bước Processing kèm AC ⇒ **không có hành động nào bị rơi**.

---

## 2 bis. Component Behavior Matrix

Dẫn xuất 1:1 từ `Use_Cases.md` §2 bis (47 dòng biểu đạt). Mỗi dòng ở đây trả lời: **component nào**, **dữ liệu vào nào**, **validation nào**, **kết quả nào** — khác nhau ra sao giữa các màn hình.

> Chiều khác biệt chi phối là **bề mặt**: component trên 📱 được nhập liệu và mở modal; component trên 🚗 chỉ được hiển thị hoặc nhận đúng một chạm. Mọi dòng 🚗 vì thế luôn có validation "không nhập liệu" và output "không mở modal".

| FR ID | Component | Screen (WF) | Context | Behavior Difference |
|---|---|---|---|---|
| FR-001 | `BtnPrimary` "Bắt đầu" | WF-002 | Onboarding tuyến tính | Nút full-width, một đường ra duy nhất; kèm `ProgressBar` 1/4. Input: không. Output: chuyển WF-003 |
| FR-001 | `CardTile` "Hoàn tất thiết lập" | WF-006 | Bỏ dở onboarding | Thẻ nhắc thụ động, **bỏ qua được**; không chặn Home. Input: bước đang dở. Output: nhảy vào đúng bước đó |
| FR-003 | `LinkRow` "Phục hồi giao dịch" | WF-002 | Cài lại sau khi từng mua | Chỉ hiện khi StoreKit báo có giao dịch cũ; ẩn hoàn toàn nếu không có (không hiện nút vô hiệu) |
| FR-003 | `BtnSecondary` "Phục hồi giao dịch" | WF-010, WF-025 | Người dùng chủ động | Luôn hiện, **ngang hàng với các bậc giá**, không ẩn trong menu con |
| FR-004 | `PickerCascade` 3 tầng | WF-003 | Chọn xe lần đầu | Hãng → model → năm, mỗi tầng ghim lại thành hàng 44pt. Input: chuỗi tìm kiếm + 3 lựa chọn. VR: tìm kiếm khớp cả tên viết tắt |
| FR-004 | `CardTile` xe hiện tại | WF-006 | Đổi xe | Thẻ chỉ-đọc hiện hãng/model/năm + ảnh; chạm mở lại WF-003 với xe hiện tại ghim đầu. Không cho sửa tại chỗ |
| FR-006 | `SheetForm` 3 ô | WF-021 | Xe thiếu trong thư viện | Ba `TextField` tự do, không validate theo danh sách. Output: request xếp hàng on-device nếu offline |
| FR-006 | `LinkRow` cuối danh sách | WF-003 | Mọi tầng của picker | Chỉ là một dòng chữ, không chiếm chỗ; xuất hiện ở **cả ba tầng** để người dùng bỏ cuộc ở đâu cũng có đường ra |
| FR-007 | `PermissionCard` × 2 | WF-005 | Onboarding bước 4 | Thẻ tổng quan mỗi quyền: lý do 1 dòng + ví dụ + trạng thái. Mật độ thấp để quyết nhanh |
| FR-007 | `SheetExplainer` | WF-022 | Chạm "Tìm hiểu thêm" | Nội dung dài: 2 ví dụ (có/không có quyền) + link chính sách. Mật độ cao, dành cho người đọc kỹ |
| FR-008 | `StaticNotice` mời cấp quyền | WF-006 | Mọi quyền bị từ chối | **Một** dòng tĩnh, không popup, không nhắc lại theo phiên. BR: tối đa 1 lời mời/màn hình |
| FR-008 | `InlineExplainer` | WF-009 | Xem cài đặt giọng chào | Giải thích tại đúng tính năng bị ảnh hưởng, kèm lối vào cấp quyền — thuyết phục hơn mà không lặp lại |
| FR-011 | `CompactRow` + waveform | WF-007 | Duyệt danh sách | Chạm dòng là phát inline; waveform chạy theo audio thật. Không mở sheet, không rời vị trí cuộn |
| FR-012 | `SheetPlayer` | WF-020 | Nghe kỹ một preset | Sheet tập trung: waveform lớn + slider âm lượng + bộ chọn sự kiện + nút áp dụng |
| FR-012 | `AutoPlayOnAppear` | WF-004 | Bước 3 onboarding | Tự phát preset đầu tiên **một lần** khi vào màn; người dùng không cần biết bấm đâu |
| FR-013 | `BtnPrimary` nhãn động | WF-007 | Gán cho sự kiện đang chọn | Nhãn đổi theo sự kiện: "Dùng cho lúc lên xe" / "…xuống xe" / "…tới nơi". Output: ghi App Group |
| FR-013 | `BtnInline` trong sheet | WF-020 | Đang nghe kỹ | Áp dụng ngay tại khoảnh khắc nghe thấy; sheet tự đóng sau khi gán |
| FR-014 | `SegmentedControl` 3 sự kiện | WF-007 | Cấu hình nhiều sự kiện | Đổi sự kiện **giữ nguyên vị trí cuộn** danh sách; chỉ nhãn nút và dấu "đang dùng" đổi |
| FR-014 | `CompactRow` tóm tắt | WF-006 | Kiểm tra cấu hình | Một dòng hiện cả ba sự kiện đã gán; chỉ đọc |
| FR-015 | `SliderControl` bền vững | WF-012 | Cấu hình nguội | Lưu ngay khi nhả tay, không có nút Lưu. VR: 0 → hiện chữ "đang tắt" |
| FR-015 | `SliderControl` inline | WF-020 | Đang nghe thử | Cùng control, khác **thời điểm**: có phản hồi âm thanh tức thì ≤ 300ms |
| FR-015 | `IconButton` âm lượng | WF-007 | Đang duyệt thư viện | Chỉ là **lối vào**, không phải nơi điều chỉnh — mật độ tối thiểu |
| FR-016 | (không có component) | WF-016 🚗 | Lên xe | Hành vi âm thanh nền, **không có UI**. Validation: không nhập liệu. Output: không mở modal |
| FR-016 | `SheetPlayer` có ducking thật | WF-020 📱 | Nghe thử trước khi ra xe | Cặp "nghe trước / diễn ra thật": bản nghe thử áp dụng **đúng** logic ducking của lúc chạy thật |
| FR-019 | (không có component) | WF-016 🚗 | Tắt máy | Hành vi nền; cửa sổ phát ≤ 1s sau tín hiệu ngắt kết nối |
| FR-019 | `CompactRow` tab Disconnect | WF-007 📱 | Cấu hình trước | Nơi duy nhất người dùng tác động được tới hành vi này |
| FR-021 | `BtnPrimary` "Lưu widget" | WF-008 | Tạo/sửa widget | Luồng đầy đủ; nhãn đổi thành "Lưu thay đổi" nếu đã có widget |
| FR-021 | `CardTile` widget hiện tại | WF-006 | Đổi nhanh | 2 chạm là đổi xong; thẻ lớn nhất trên Home vì là thứ người dùng quan tâm nhất |
| FR-021 | `BtnInline` trong preview | WF-023 | Thấy preview lệch | Sửa **tại nơi phát hiện vấn đề**, không quay về đầu luồng |
| FR-023 | `LimitNotice` + `BtnUpgrade` | WF-008 | Free đã dùng hết 1 widget | Cho **đổi** widget hiện có; nút "Thêm widget thứ hai" mới dẫn WF-010. Không xoá widget đang có |
| FR-024 | `VersionNotice` | WF-008 | iOS < 17.4 | Nêu rõ yêu cầu iOS 17.4+, **vẫn cho cấu hình và lưu**; không giả vờ widget đang chạy |
| FR-025 | `ModalRatioViewer` | WF-023 | Kiểm nhiều tỉ lệ | Vuốt ngang qua các tỉ lệ, khung đổi kích thước bằng spring damping cao; nhãn nói rõ thật/ước lượng |
| FR-025 | `InlinePreview` nhỏ | WF-008 | Đang cấu hình | Xác nhận thoáng qua ở một tỉ lệ; không có điều hướng tỉ lệ |
| FR-025 | `CompactRow` kích thước thật | WF-014 | Sau khi đã cắm xe | Cùng thông tin, khác **độ chắc chắn**: số thật thay cho ước lượng |
| FR-027 | `SheetImagePicker` + crop | WF-024 | Chọn ảnh | Khung crop theo tỉ lệ màn hình xe; vùng bị cắt làm tối. VR: cảnh báo độ phân giải thấp |
| FR-027 | `ImageSlot` | WF-008 | Đang cấu hình | Chỉ là điểm khởi phát, một ô; không có logic crop |
| FR-029 | `WidgetSurface` | WF-017 🚗 | Trên xe | Chỉ hiển thị; không tương tác ở MVP 1. Layout tính từ scene bounds tại runtime |
| FR-029 | `ModalRatioViewer` | WF-023 📱 | Trước khi ra xe | Cùng nội dung, khác **quyền tương tác**: trên iPhone sửa được, trên xe chỉ nhìn |
| FR-031 | `FallbackNotice` | WF-019 🚗 | Render thất bại | Chỉ đọc, **không CTA** — người dùng đang lái. Không bao giờ để lại vùng trắng |
| FR-031 | `WarningRow` | WF-006 📱 | Mở app sau chuyến lỗi | Có hành động (dẫn WF-014) vì người dùng đã đỗ xe; tự xoá khi render kế tiếp thành công |
| FR-032 | `DiagnosticTable` | WF-014 | Tra cứu chủ động | Bảng dữ liệu kỹ thuật, mở rộng từng dòng được |
| FR-032 | `SheetDataDisclosure` | WF-028 | Gửi báo cáo | Liệt kê **từng mục** dữ liệu + giá trị thật + tick chọn; tách khỏi nơi tra cứu để người dùng thấy rõ gì rời máy |
| FR-032 | `CompactText` hướng dẫn | WF-019 🚗 | Lỗi trên xe | Chỉ là con trỏ sang iPhone, không phải nơi làm việc |
| FR-033 | `ToggleMain` | WF-009 | Bật/tắt giọng chào | Công tắc thật, đổi trạng thái hệ thống |
| FR-033 | `StatusRow` | WF-006 | Xem tổng quan | Chỉ báo trạng thái, **không bấm được để tắt** — tránh tắt nhầm từ Home |
| FR-034 | `ToggleRow` × 4 + ví dụ | WF-009 | Cấu hình nguồn | Mỗi nguồn 1 toggle + 1 ví dụ câu chào + trạng thái quyền |
| FR-035 | `ToggleRow` bị chặn | WF-009 | Nguồn thiếu quyền | Toggle **nảy về tắt** + nhãn "cần quyền" + nút hành động; không có trạng thái bật-mà-không-chạy |
| FR-036 | `BtnPrimary` "Nghe thử" | WF-009 | Xác minh tính năng | Sinh câu chào từ ngữ cảnh thật; chữ hiện đồng thời với âm thanh |
| FR-036 | `BtnUpgrade` | WF-010 | Người dùng Free | Nghe thử **đầy đủ**, nhưng nút sau đó là "Mở khoá" thay vì "Áp dụng" |
| FR-037 | (không có component) | WF-016 🚗 | Lên xe | Hành vi nền, ≤ 2s sau connect |
| FR-037 | `BtnPrimary` "Nghe thử" | WF-009 📱 | Trước khi ra xe | Cặp "nghe trước / diễn ra thật" — cơ chế chống R-10 và R-13 |
| FR-040 | `CardStack` tự sắp xếp | WF-016 🚗 | Dashboard đầy đủ | Thẻ đổi thứ tự bằng **crossfade tại chỗ**, không chuyển động vị trí; throttle 1 lần/30s |
| FR-041 | `CardStack` cơ bản | WF-018 🚗 | Gói Free | Cùng màn hình, ít thẻ hơn và không cá nhân hóa — **cấu hình Free đã chốt**, không phải bản làm mờ |
| FR-042 | `CardAction` 1 chạm | WF-016 🚗 | Chạm thẻ | Hành động bắt đầu ≤ 1s; touch target ≥ 44pt; lỗi báo **trên thẻ**, không modal |
| FR-042 | `CardLocked` | WF-018 🚗 | Thẻ Premium | Trạng thái khoá nói bằng chữ; **không mở paywall trên màn hình xe** |
| FR-044 | `StatusBadge` gói hiện tại | WF-006 | Hub trạng thái | Nói "bạn đang có gì" |
| FR-044 | `LockLabel` trên preset | WF-007 | Duyệt thư viện | Nói "bạn chưa có gì" — nửa còn lại của cùng thông điệp, đặt ở nơi khác |
| FR-044 | `StaticNotice` | WF-018 🚗 | Đang lái, gói Free | Biểu đạt yếu nhất có thể: một dòng, không popup, không chắn — an toàn > conversion |
| FR-045 | `PaywallFull` | WF-010 | Chạm tính năng khoá | Trang giá đầy đủ, Zone A nói về **đúng tính năng vừa chạm** |
| FR-045 | `LinkRow` "Nâng cấp" | WF-012 | Tự tìm trong Settings | Không có tính thúc đẩy, chỉ là lối vào thường trực |
| FR-046 | `PriceTierCard` × 4 | WF-010 | Xem bảng giá | 4 thẻ gồm cả Free đang dùng; giá cuối bằng tiền tệ địa phương từ StoreKit |
| FR-048 | `ConfirmPanel` | WF-011 | Trước giao dịch | **Đúng một vị trí duy nhất**; Layer Discovery cố ý trống để không gây phân tán |
| FR-051 | `StatusBadge` "Trial còn N ngày" | WF-006 | Trial đang chạy | Chỉ báo liên tục, mật độ tối thiểu; kèm ngày trừ tiền, không đếm ngược gây áp lực |
| FR-051 | `CompactRow` trạng thái trial | WF-012 | Tra cứu chi tiết | Đủ số liệu chính xác cho người muốn kiểm kỹ |
| FR-052 | `TrialReminderPanel` | WF-013 | Ngày 6 và 7 | 3 nút **ngang hàng thị giác** gồm cả "Huỷ trial" |
| FR-053 | `SheetSubscription` | WF-025 | Quản lý đăng ký | Nơi thao tác: trạng thái + huỷ + phục hồi |
| FR-053 | `CompactRow` có trạng thái | WF-012 | Xem Settings | Trạng thái hiện **ngay trên dòng**, không cần mở sheet |
| FR-053 | `AlertConfirm` | WF-027 | Chạm huỷ | Một câu hỏi duy nhất, nêu rõ ngày hết quyền; không có gì khác gây phân tán |
| FR-054 | `PriceTierCard` Lifetime | WF-010 | Chọn Lifetime | Trong cùng bảng 4 bậc |
| FR-054 | `ConfirmPanel` không gia hạn | WF-011 | Xác nhận Lifetime | Khác các bậc khác ở chỗ **loại bỏ** thông tin gia hạn — sự thiếu vắng đó là thông điệp |
| FR-055 | `SheetLanguagePicker` | WF-026 | Chọn ngôn ngữ | Chọn là áp dụng ngay, không có nút Lưu |
| FR-055 | `CompactRow` ngôn ngữ | WF-012 | Xem Settings | Hiện giá trị hiện tại mà không cần mở sheet |
| FR-057 | `AlertDestructive` | WF-029 | Xác nhận xoá | Điểm chặn không bỏ qua được; nêu rõ mất gì **và giữ gì** |
| FR-057 | `LinkRow` quyền riêng tư | WF-012 | Xem Settings | Nơi đọc hiểu trước khi quyết định |
| FR-059 | `ToastOverlay` biến thể mời đánh giá | WF-030 | Sau chuỗi tích cực | Hệ thống chọn thời điểm; đóng bằng một chạm; không chặn tác vụ |
| FR-059 | `LinkRow` "Đánh giá Carbina" | WF-012 | Tự tìm | Luôn có sẵn, không có timing |
| FR-060 | `SheetDataDisclosure` | WF-028 | Chọn "không hài lòng" | Cùng sheet với FR-032 nhưng **Zone C được nhấn mạnh** — ở ngữ cảnh này lời người dùng quan trọng hơn số liệu |
| FR-063 | `CardAction` liên hệ | WF-016 🚗 | *MVP 2* — đang lái | 1 chạm để gọi; tối đa 5 favorite |
| FR-064 | `ToggleRow` đồng bộ | WF-015 | *MVP 3* — cấu hình | Nơi thao tác |
| FR-064 | `LinkRow` "Tài khoản" | WF-012 | *MVP 3* — Settings | Chỉ là lối vào; **không hiện ở MVP 1** |

**Kiểm tra**: 82 dòng biểu đạt, phủ toàn bộ 47 dòng của `Use_Cases.md` §2 bis (một số dòng UC được tách thành nhiều dòng FR khi cùng biểu đạt liên quan tới nhiều FR). **FR chỉ có một màn hình duy nhất không xuất hiện ở đây** theo đúng quy tắc: FR-002, FR-005, FR-009, FR-010, FR-017, FR-018, FR-020, FR-022, FR-026, FR-028, FR-030, FR-038, FR-039, FR-043, FR-047, FR-049, FR-050, FR-056, FR-058, FR-061, FR-062, FR-065, FR-066.

---

## 2 ter. Context-Dependent Behaviors

Dẫn xuất từ **Context Variations** của từng UC ở `Use_Cases.md` §2 và **State Variations** ở §4. Mọi FR ưu tiên **High** có ≥ 2 dòng. Mỗi dòng nêu **hành vi cụ thể** — thành phần nào đổi, bước nào đổi, dữ liệu nào đổi — không dùng ngôn từ chung như "trải nghiệm tốt hơn".

| FR ID | Context | Trigger | Behavior Change |
|---|---|---|---|
| FR-001 Điều phối onboarding | First Visit | Cài mới, chưa có cấu hình | Hiện WF-002 với `ProgressBar` 1/4; **không** render WF-010 ở bất kỳ bước nào |
| FR-001 | Returning | Cài lại, StoreKit báo có giao dịch cũ | Thêm `LinkRow` "Phục hồi giao dịch" dưới nút chính; nếu phục hồi OK thì bỏ nhãn khoá ở WF-004 |
| FR-001 | Power User | Bỏ qua mọi bước xin quyền | Hoàn tất trong ~40s; chuyển thẳng WF-006 với trạng thái quyền = từ chối |
| FR-002 Lưu/phục hồi tiến trình | Error (ngắt giữa luồng) | App bị kill hoặc người dùng thoát ở bước N | Lần mở kế tiếp vào **đúng bước N**, giữ mọi lựa chọn đã làm; không quay về WF-002 |
| FR-002 | Returning | Đã hoàn tất onboarding trước đó | WF-001 định tuyến thẳng WF-006; không đọc lại state onboarding |
| FR-004 Thư viện xe | First Visit | Chưa chọn xe | Danh sách hãng sắp theo **mức phổ biến ở storefront hiện tại**, không theo thứ tự chữ cái; Zone A chưa có ảnh |
| FR-004 | Returning | Đã có xe, mở lại để đổi | Xe hiện tại **ghim đầu danh sách** và đánh dấu; ảnh xe hiện ngay ở Zone A |
| FR-004 | Power User | Xe nội địa / tên viết tắt | Tìm kiếm khớp cả tên viết tắt và tên nội địa; không validate cứng theo danh sách |
| FR-004 | Offline | Không có mạng | Tìm kiếm vẫn chạy ≤ 200ms vì thư viện đóng gói sẵn on-device; không có trạng thái tải |
| FR-005 Ảnh xe cho widget | Error (thiếu asset) | Model không có ảnh trong bộ asset | Dùng ảnh silhouette theo phân khúc (sedan/SUV/pickup) và **nói rõ đang dùng ảnh chung**; ghi nhận thiếu asset |
| FR-005 | Returning | Đã cắm xe, biết kích thước màn hình | Chọn biến thể ảnh có độ phân giải khớp kích thước thật thay vì biến thể lớn nhất |
| FR-007 Trình bày lý do quyền | First Visit | Chưa hỏi quyền nào | Cả hai `PermissionCard` ở trạng thái "Chưa hỏi"; nút "Tiếp tục" **đã bấm được** |
| FR-007 | Returning | Quyền đã bị từ chối trước đó | Nút "Cho phép" đổi thành "Mở Cài đặt" (iOS không cho hỏi lại lần hai) |
| FR-007 | Power User | Cấp Vị trí ở mức "Khi dùng app" | Nêu rõ tuyến đường chỉ học được khi app đang mở; **không** im lặng để người dùng tưởng đã đủ |
| FR-008 Suy giảm theo quyền | Error (từ chối toàn bộ) | Cả Vị trí và Lịch bị từ chối | Widget + sound + dashboard cơ bản vẫn đầy đủ; giọng chào rơi về biến thể chỉ theo giờ; mục Arrive bị vô hiệu kèm lý do |
| FR-008 | Power User (một phần) | Cấp Lịch, từ chối Vị trí | Giọng chào dùng lịch; dashboard **không** có thẻ gợi ý điểm đến; sound Arrive vẫn vô hiệu |
| FR-008 | Returning | Cấp quyền muộn | Ngữ cảnh mới có hiệu lực từ **lần `carplay_connected` kế tiếp**, không cần khởi động lại app |
| FR-009 Splash & định tuyến | First Visit | Chưa onboard | Hiện ≤ 1,5s rồi WF-002 |
| FR-009 | Returning | Đã onboard | Hiện ≤ 1,0s rồi WF-006; cấu hình đọc từ cache nên không có trạng thái tải |
| FR-009 | Error | Không đọc được cấu hình on-device | Vào WF-006 ở trạng thái mặc định an toàn kèm một dòng thông báo; **không** bắt onboard lại |
| FR-010 Danh mục sound | Free tier | Entitlement = Free | Đúng 3 preset mở, còn lại có `LockLabel` rõ ràng — **không ẩn** preset khoá |
| FR-010 | Premium | Entitlement = Premium/Lifetime | Toàn bộ ≥ 12 preset mở; `LockLabel` biến mất hoàn toàn |
| FR-011 Nghe thử inline | First Visit | Chưa nghe preset nào | Preset đã gán từ onboarding được ghim đầu; các nhóm khác mở để khuyến khích nghe thử |
| FR-011 | Power User | Chạm nhiều dòng liên tiếp | Dòng đang phát **dừng ngay** khi chạm dòng khác; không phát chồng, không cần chạm dừng |
| FR-011 | Error | Phiên audio bị chiếm (đang có cuộc gọi) | Dòng hiện lý do cụ thể tại chỗ, giữ icon tĩnh; **không** hiện waveform khi không có tiếng |
| FR-012 Nghe thử trong sheet | First Visit | Mở sheet lần đầu | Tự phát một lần khi sheet mở; người dùng không phải tìm nút play |
| FR-012 | Returning | Preset đang dùng | Nút chính hiện "Đang dùng" ở trạng thái đã chọn thay vì "Dùng sound này" |
| FR-012 | Power User | Đang phát nhạc từ app khác | Áp dụng **ducking thật** để bản nghe thử phản ánh đúng trải nghiệm trên xe |
| FR-013 Gán sound Connect | First Visit | Bỏ qua bước chọn sound | Hệ thống gán preset Free đầu tiên làm mặc định; không để trạng thái trống |
| FR-013 | Power User | Chọn "Không dùng" | Không phát sound lúc connect và **không** hiển thị nhắc nhở về việc này |
| FR-015 Âm lượng sound | First Visit | Chưa từng điều chỉnh | Dùng giá trị mặc định; slider **không** xuất hiện trong onboarding (giữ 5 bước) |
| FR-015 | Power User | Kéo về 0 | Hiện chữ "đang tắt" thay vì để trống; nhạc **không** bị đổi âm lượng |
| FR-015 | Error | Không phát được sound mẫu | Slider vẫn điều chỉnh và lưu được; hiện một dòng nói rõ không nghe thử được lúc này |
| FR-016 Phát sound Connect | First Visit 🚗 | Lần cắm xe đầu tiên | Đây là khoảnh khắc chứng minh giá trị; ghi `sound_played` kèm `output_route` để xác minh đúng loa xe |
| FR-016 | Returning 🚗 | Chuyến hằng ngày | Phát ≤ 1,5s, hoàn toàn không cần thao tác; xảy ra 2 lần/ngày |
| FR-016 | Power User 🚗 | Đang phát podcast | Duck xuống 20% rồi **phục hồi đúng vị trí và đúng mức** trước đó |
| FR-017 Nhường phiên audio | Error (cuộc gọi) 🚗 | Có cuộc gọi khi connect | **Bỏ hẳn lượt phát**; không ducking, không chèn tiếng, **không phát bù** sau khi cuộc gọi kết thúc |
| FR-017 | Error (chỉ dẫn dẫn đường) 🚗 | TTS dẫn đường đang phát | Nhường chỉ dẫn, phát sau khi kết thúc, **chờ tối đa 3s** rồi bỏ lượt |
| FR-018 Chống phát trùng | Power User 🚗 | Cắm lại dây trong 3s | Chỉ phát tối đa **1 lần**; lượt thứ hai bị bỏ |
| FR-018 | Error 🚗 | Kết nối chập chờn nhiều lần | Cửa sổ chống trùng áp dụng cho mỗi cặp connect/disconnect, không tích lũy nợ phát |
| FR-019 Phát sound Disconnect | Returning 🚗 | Tắt máy bình thường | Phát qua loa xe, lệch ≤ 1s so với tín hiệu ngắt kết nối |
| FR-019 | Power User 🚗 | Rút dây thay vì tắt máy | Coi là disconnect bình thường; cùng hành vi |
| FR-019 | Error 🚗 | Sound Arrive vừa phát trong 10s | **Bỏ** sound Disconnect để không phát 2 tiếng liền nhau |
| FR-020 Định tuyến loa xe | Error 🚗 | Phiên audio bị thu hồi trước khi phát được | **Bỏ lượt** và ghi lý do; **tuyệt đối không** phát bù qua loa iPhone |
| FR-020 | Power User 🚗 | Người dùng đang cắm tai nghe | Ghi `output_route` để phát hiện sai định tuyến; hành vi vẫn là ưu tiên loa xe |
| FR-021 Preset widget theo xe | First Visit | Chưa có widget | Hiện **≥ 3 preset gợi ý theo xe đã chọn**; tuyệt đối không có canvas rỗng |
| FR-021 | Returning | Đã có widget | Widget hiện tại nạp sẵn ở Zone A; nút chính đổi thành "Lưu thay đổi" |
| FR-021 | Power User | Premium, dùng ảnh cá nhân | Mở thêm loại widget ảnh cá nhân và counter; lối vào WF-024 nổi bật hơn |
| FR-022 Lưu vào App Group | Returning | Lưu thành công | Ghi ngay tại thời điểm lưu, **không chờ app vào background**; widget đọc được khi app ở background |
| FR-022 | Error | Ghi App Group thất bại | Nêu lỗi cụ thể + nút thử lại; **giữ bản nháp**, không mất cấu hình đang làm |
| FR-023 Giới hạn widget | Free tier | Đã dùng hết 1 widget | Cho **đổi** widget hiện có, nêu rõ giới hạn; nút "Thêm widget thứ hai" mới dẫn WF-010 |
| FR-023 | Premium | Entitlement = Premium/Lifetime | Không giới hạn số widget; `LimitNotice` biến mất |
| FR-023 | Returning (hạ cấp) | Trial hết, về Free với 3 widget | **Giữ nguyên** cả 3 cấu hình, chỉ 1 widget được kích hoạt; không xoá dữ liệu |
| FR-024 Ngưỡng iOS 17.4 | Error (iOS 16.4–17.3) | Thiết bị không hỗ trợ widget CarPlay | WF-008 nêu rõ yêu cầu iOS 17.4+, **vẫn cho cấu hình và lưu**; vùng widget trên xe hiện thông báo phiên bản, không crash |
| FR-024 | Returning (sau nâng cấp iOS) | Người dùng nâng lên 17.4+ | Widget đã cấu hình sẵn render ngay ở lần cắm kế tiếp, không cần cấu hình lại |
| FR-025 Preview theo tỉ lệ | First Visit | Chưa từng cắm xe | Dùng **≥ 4 tỉ lệ tham chiếu** và nhãn nói rõ đây là **ước lượng** |
| FR-025 | Returning | Đã cắm xe ≥ 1 lần | Tỉ lệ mặc định là **kích thước thật của xe người dùng**; nhãn nói rõ đây là số thật |
| FR-025 | Power User | Có 2 xe khác kích thước | Cho chọn giữa các kích thước **đã từng gặp**; kiểm được cả hai trước khi lưu |
| FR-026 Phát hiện vượt vùng | Error | Có phần tử vượt vùng an toàn | Chỉ rõ **phần tử nào** + đề xuất giảm bớt; **không** tự âm thầm cắt nội dung |
| FR-026 | Power User | Chữ dài hơn không gian | Co theo Dynamic Type rồi **truncate có ellipsis**, không cắt giữa chữ |
| FR-029 Render theo scene bounds | First Visit 🚗 | Lần cắm đầu tiên | Đọc bounds, tính layout, **lưu kích thước** để WF-023 dùng về sau; ghi `widget_render_ok` kèm kích thước |
| FR-029 | Returning 🚗 | Kích thước đã biết | Đường render ngắn hơn vì layout đã có tham số; kết quả giống hệt lần trước |
| FR-029 | Power User 🚗 | Kích thước chưa từng gặp | Vẫn render bình thường vì layout tính tại runtime, **không tra bảng xe**; ghi kích thước mới |
| FR-030 Giảm cấp layout | Error (vượt bounds) 🚗 | Không đủ chỗ cho mọi phần tử | Bỏ phần tử ưu tiên thấp nhất → co chữ → truncate; nếu vẫn thất bại thì chuyển FR-031 |
| FR-030 | Error (hết bộ nhớ) 🚗 | Widget extension bị hệ thống thu hồi | Chuyển FR-031 và ghi `failure_reason = memory` — **phân biệt rõ** với lỗi vượt bounds |
| FR-031 Fallback CarPlay | Error 🚗 | Render thất bại | Hiện `FallbackNotice` bằng chữ nêu rõ **vấn đề tương thích màn hình xe**; tuyệt đối không vùng trắng, không CTA |
| FR-031 | Error (bộ phận) 🚗 | Chỉ widget lỗi, dashboard vẫn được | **Chỉ vùng widget** bị thay bằng thông báo; WF-016 hoạt động đầy đủ |
| FR-031 | Returning | Lần render kế tiếp thành công | `WarningRow` trên WF-006 **tự xoá**; không để lại cảnh báo giả |
| FR-033 Bật/tắt giọng chào | First Visit | Sau onboarding | Bật theo mặc định kèm một dòng nói rõ có thể tắt bất cứ lúc nào |
| FR-033 | Returning | Tắt rồi bật lại | Cấu hình nguồn ngữ cảnh trước đó **được giữ nguyên**, không reset |
| FR-033 | Free tier | Entitlement = Free | Công tắc hiện trạng thái khoá; **nghe thử vẫn đầy đủ** (FR-036); nút mở khoá dẫn WF-010 |
| FR-036 Nghe thử giọng chào | First Visit | Chưa có quyền nào | Chỉ nguồn "giờ trong ngày" hoạt động, và điều đó được nói rõ ngay tại chỗ |
| FR-036 | Power User | Chạm "Nghe thử" ≥ 4 lần | Mỗi lần một câu khác; người dùng thấy đủ dải ≥ 4 biến thể ngữ cảnh |
| FR-036 | Error (TTS lỗi) | Không phát được âm thanh | **Vẫn hiện chữ** câu chào kèm lý do — nội dung vẫn kiểm chứng được dù âm thanh lỗi |
| FR-037 Phát giọng chào trên xe | First Visit 🚗 | Chưa đủ ngữ cảnh | Dùng biến thể chỉ theo giờ, và câu đó vẫn phải nghe tự nhiên — không nghe như bản rút gọn |
| FR-037 | Returning 🚗 | Đã dùng vài ngày | Ghép nhiều nguồn (giờ + thời tiết + lịch + tuyến quen); câu chào rõ ràng phong phú hơn |
| FR-037 | Error (cuộc gọi) 🚗 | Có cuộc gọi khi connect | Bỏ lượt phát, **không phát bù** |
| FR-037 | Free tier 🚗 | Entitlement = Free | **Không phát**; WF-018 nêu bằng một dòng chữ tĩnh, không popup |
| FR-038 Chống lặp & ràng buộc nội dung | Returning 🚗 | Câu vừa chọn giống lần trước | Chọn biến thể khác **trước khi phát** |
| FR-038 | Error (nội dung vi phạm) | Câu chào chứa tham chiếu bị cấm | Loại bỏ khỏi tập biến thể ở giai đoạn dựng dữ liệu; **không** có tên "Jarvis" hay tham chiếu Marvel/Disney (R-10) |
| FR-040 Sắp xếp dashboard | First Visit 🚗 | Chưa đủ dữ liệu học | Thứ tự mặc định + **một dòng nói rõ dashboard sẽ tự đổi sau vài chuyến**; không tuyên bố đã cá nhân hóa |
| FR-040 | Returning 🚗 | Đã học được thói quen | Thẻ hay dùng lên Zone A; thứ tự đổi theo giờ và tuyến đường; crossfade 0,4s, throttle 1 lần/30s |
| FR-040 | Power User (ngữ cảnh sai) 🚗 | Đi công tác, tuyến lạ | Người dùng **bỏ qua** thẻ → hạ trọng số; không cần vào Settings để sửa |
| FR-041 Dashboard theo entitlement | Free tier 🚗 | Entitlement = Free | Đúng cấu hình Free đã chốt: nhạc đang phát, thời tiết, 1 shortcut |
| FR-041 | Offline 🚗 | Mất mạng | Thẻ nhạc/thời tiết dùng cache và **ghi rõ thời điểm cập nhật**; thẻ shortcut vẫn hoạt động |
| FR-042 Chạm thẻ | Returning 🚗 | Chạm thẻ đúng | Hành động bắt đầu ≤ 1s; ghi `ai_recommendation_tapped` |
| FR-042 | Error 🚗 | Hành động thất bại (nguồn nhạc không sẵn sàng) | Thông báo gọn **trên thẻ** + hành động thay thế; **không modal**, các thẻ khác không bị ảnh hưởng |
| FR-042 | Free tier 🚗 | Thẻ thuộc Premium | Trạng thái khoá nói bằng chữ; **không mở paywall trên màn hình xe** |
| FR-043 EntitlementService | Error | Không đọc được entitlement | Mặc định về mức **Free và vẫn cho dùng**; không chặn, không hiện lỗi trên màn hình xe |
| FR-043 | Offline (Lifetime) | Mất mạng, đã mua Lifetime | Dùng bản cache đã xác thực; **không** hạ Lifetime xuống Free vì mất mạng |
| FR-044 Cấu hình gói Free | First Visit | Vừa onboard | 1 widget đầy đủ chức năng + 3 sound + dashboard cơ bản; không quảng cáo, không giới hạn thời gian |
| FR-044 | Returning | Dùng Free lâu dài | **Không** nhắc nâng cấp lặp lại theo phiên; tối đa 1 lời mời tĩnh/màn hình |
| FR-045 Chính sách paywall | First Visit | Lần mở app đầu tiên | **Không** hiển thị WF-010; kiểm chứng bằng `paywall_shown.days_since_install > 0` |
| FR-045 | Returning | Chạm tính năng khoá | Mở WF-010 với Zone A nói về **đúng tính năng vừa chạm**, không phải quảng cáo chung |
| FR-045 | Power User | Đã xem paywall trước đó | Nhấn mạnh bậc Yearly; **không** lặp lại cùng nội dung Zone A |
| FR-046 Trình bày bậc giá | Returning | Giá lấy được từ StoreKit | 4 bậc, giá cuối bằng tiền tệ địa phương; **không có bậc weekly** |
| FR-046 | Error | StoreKit không trả về giá | Hiện trạng thái tải rồi báo lỗi rõ ràng + nút thử lại; **chặn** đường sang WF-011 |
| FR-047 Cấm giá cache/hardcode | Error | Giá không đọc được | **Không** hiện giá cache, **không** hiện giá hardcode — trạng thái đúng là báo lỗi, không phải đoán |
| FR-047 | Power User | Đổi vùng App Store giữa lúc mua | Đọc lại giá từ StoreKit trước khi hiển thị WF-011 |
| FR-048 Điểm chặn xác nhận giá | First Visit | Bậc có trial | Hiện đủ 4 mốc: bắt đầu trial · hết trial · ngày trừ tiền · số tiền |
| FR-048 | Returning | Bậc Lifetime | **Không** hiện ngày gia hạn; nêu rõ "một lần, không tự động gia hạn" |
| FR-048 | Error | Người dùng huỷ ở dialog Apple | Về WF-011 **giữ lựa chọn**; không trả về WF-010, không hiện lại paywall |
| FR-049 Xử lý giao dịch StoreKit | Returning | Thanh toán thành công | Entitlement cập nhật; tính năng mở khóa ≤ 2s **không cần khởi động lại app** |
| FR-049 | Error | Thanh toán thất bại | Nêu nguyên nhân từ StoreKit + nút thử lại; giữ nguyên ở WF-011 |
| FR-050 Xác nhận giao dịch | Returning | Mua thành công | Gửi xác nhận giao dịch (email hoặc thông báo trong app) — biện pháp chống chargeback (R-12) |
| FR-050 | Error | Không gửi được xác nhận | Xếp hàng và gửi lại; **không** chặn việc mở khóa tính năng vì lý do này |
| FR-051 Quản lý trial | First Visit | Trial vừa bắt đầu | Badge "Trial còn N ngày" + ngày trừ tiền ở WF-006 Zone D; không đếm ngược gây áp lực |
| FR-051 | Power User | Huỷ ngày thứ 2 | Giữ Premium tới hết ngày 7; **mọi cấu hình widget/sound được giữ nguyên** sau khi về Free |
| FR-051 | Error | Đã từng dùng trial | **Không** hiển thị lại ưu đãi trial; nêu rõ là mua trực tiếp |

**Kiểm tra §2 ter**: 109 dòng, phủ 42/42 FR ưu tiên High với ≥ 2 dòng mỗi FR ⇒ **Pass**. Các FR ưu tiên Medium/Low có ngữ cảnh riêng được ghi trong chính sub-spec của chúng (mục **Error Handling** và **Business Rules**), không nhân bản lại ở đây.

---

## 3. Non-Functional Requirements

Mọi NFR dưới đây có **mục tiêu định lượng**. Nguồn số: `PRD.md` §9 (ràng buộc kỹ thuật) và `Project_Overview.md` §6.1 (chỉ số kỹ thuật). Không có NFR nào dùng từ "nhanh", "an toàn", "đáng tin cậy" mà không kèm con số.

### 3.1 Core NFRs (Required for all projects)

#### NFR-001: Performance — Cold Launch Time
**Priority**: High
**Requirement**: App phải trở nên tương tác được trong **< 2,0 giây** kể từ lúc chạm icon, trên thiết bị chuẩn iPhone 12, cold start.

**Measurement**: thời gian từ chạm icon đến khi WF-006 (hoặc WF-002) nhận được tương tác đầu tiên · đo trên iPhone 12, iOS 17.4 · app không còn trong bộ nhớ · Firebase Performance trace.

**Acceptance Criteria**:
- **AC-NFR-001.1**: WHEN người dùng chạm icon app THEN app trở nên tương tác được trong ≤ 2,0s trên iPhone 12.
- **AC-NFR-001.2**: WHEN đo trên toàn bộ thiết bị mục tiêu (iPhone 12 trở lên) THEN ≥ 95% lần khởi động đạt ngưỡng.
- **AC-NFR-001.3**: IF thời gian khởi động > 3,0s ở p95 THEN đây là điều kiện **chặn phát hành**.

---

#### NFR-002: Performance — Dashboard Load Time
**Priority**: High
**Requirement**: Dashboard trên iPhone (WF-006) và trên CarPlay (WF-016) phải hiển thị đủ nội dung trong **< 500ms** sau khi app vào foreground / scene active.

**Measurement**: trace tùy chỉnh từ `sceneDidBecomeActive` đến khi thẻ cuối cùng ở Zone B được vẽ · dùng dữ liệu cache, không tính thời gian gọi mạng.

**Acceptance Criteria**:
- **AC-NFR-002.1**: WHEN app vào foreground THEN WF-006 hiển thị đủ nội dung trong ≤ 500ms.
- **AC-NFR-002.2**: WHEN CarPlay scene active THEN WF-016 hiển thị đủ thẻ trong ≤ 500ms.
- **AC-NFR-002.3**: IF dữ liệu ngữ cảnh chưa sẵn sàng THEN hiển thị thứ tự thẻ mặc định trong ngưỡng trên thay vì chờ (liên quan FR-040).

---

#### NFR-003: Performance — Sound Playback Latency
**Priority**: High
**Requirement**: Sound Connect phải bắt đầu phát trong **≤ 1,5 giây** kể từ `carplay_connected`; sound Disconnect lệch **≤ 1 giây** so với tín hiệu ngắt kết nối.

**Measurement**: dấu thời gian giữa sự kiện hệ thống và callback bắt đầu phát của `AVAudioSession`, ghi trong `sound_played`.

**Acceptance Criteria**:
- **AC-NFR-003.1**: WHEN `carplay_connected` xảy ra THEN sound Connect bắt đầu phát trong ≤ 1,5s ở ≥ 95% phiên.
- **AC-NFR-003.2**: WHEN tín hiệu ngắt kết nối tới THEN sound Disconnect phát lệch ≤ 1,0s.
- **AC-NFR-003.3**: WHEN phiên audio không khả dụng THEN lượt phát bị bỏ **trong ≤ 100ms** thay vì treo chờ (liên quan FR-017, FR-020).

---

#### NFR-004: Performance — Voice Greeting Latency
**Priority**: High
**Requirement**: Giọng chào phải bắt đầu phát trong **≤ 2,0 giây** kể từ `carplay_connected`, gồm cả thời gian ContextEngine chọn biến thể.

**Measurement**: dấu thời gian ghi trong `voice_greeting_played` trừ dấu thời gian `carplay_connected`.

**Acceptance Criteria**:
- **AC-NFR-004.1**: WHEN `carplay_connected` xảy ra THEN giọng chào bắt đầu phát trong ≤ 2,0s ở ≥ 95% phiên.
- **AC-NFR-004.2**: IF độ trễ > 3,0s THEN coi là lỗi chức năng của FR-037, không phải suy giảm hiệu năng.
- **AC-NFR-004.3**: WHEN app chuẩn bị phiên CarPlay THEN mô hình Core ML được nạp sẵn (warm), **không** nạp lười tại thời điểm scene active.

---

#### NFR-005: Performance — On-Device Inference Time
**Priority**: High
**Requirement**: Mỗi lượt suy luận của ContextEngine (chọn biến thể câu chào, sắp thứ tự thẻ) hoàn tất trong **< 1,0 giây** trên Apple Neural Engine của iPhone 12.

**Measurement**: trace tùy chỉnh quanh lệnh gọi Core ML prediction, đo trên iPhone 12 và iPhone 15.

**Acceptance Criteria**:
- **AC-NFR-005.1**: WHEN ContextEngine được gọi THEN kết quả trả về trong ≤ 1,0s trên iPhone 12.
- **AC-NFR-005.2**: IF suy luận vượt 1,0s THEN hệ thống dùng kết quả mặc định và ghi nhận timeout, **không** chặn việc phát giọng chào.

---

#### NFR-006: Performance — App Memory Footprint
**Priority**: High
**Requirement**: App iPhone dùng **< 150MB** bộ nhớ ở trạng thái hoạt động bình thường, bao gồm toàn bộ framework và mô hình Core ML đã nạp.

**Measurement**: Xcode Instruments (Allocations), đo ở trạng thái WF-006 sau 5 phút dùng liên tục.

**Acceptance Criteria**:
- **AC-NFR-006.1**: WHEN app ở trạng thái hoạt động bình thường THEN bộ nhớ dùng ≤ 150MB.
- **AC-NFR-006.2**: WHEN mô hình Core ML được nạp THEN phần tăng thêm ≤ 40MB.

---

#### NFR-007: Performance — Widget Extension Memory Ceiling
**Priority**: High
**Requirement**: Widget extension phải chạy dưới ngưỡng bộ nhớ do hệ thống áp cho extension, với **mức dùng mục tiêu ≤ 25MB**; ảnh sau nén ghi vào App Group **≤ 2MB mỗi ảnh**.

**Measurement**: Instruments attach vào widget extension process; kiểm dung lượng file trong App Group container.

**Acceptance Criteria**:
- **AC-NFR-007.1**: WHEN widget render THEN bộ nhớ của extension ≤ 25MB.
- **AC-NFR-007.2**: WHEN ảnh được lưu cho widget THEN dung lượng sau nén ≤ 2MB.
- **AC-NFR-007.3**: WHEN widget extension bị hệ thống thu hồi vì bộ nhớ THEN hệ thống ghi `widget_render_failed` với `failure_reason = memory`, **phân biệt được** với lỗi vượt bounds (liên quan FR-030, rủi ro thực thi A ở `Project_Overview.md` §8).
- **AC-NFR-007.4**: WHEN widget extension chạy THEN nó **không** nạp mô hình Core ML và **không** thực hiện lệnh gọi mạng nào.

---

#### NFR-008: Performance — CarPlay Frame Rate
**Priority**: High
**Requirement**: Giao diện trên màn hình CarPlay giữ **60 FPS** khi cuộn và khi thẻ đổi thứ tự.

**Measurement**: Instruments (Core Animation FPS) trong phiên CarPlay simulator và trên 1 xe thật mỗi nhóm test matrix.

**Acceptance Criteria**:
- **AC-NFR-008.1**: WHEN người dùng cuộn WF-016 THEN frame rate ≥ 60 FPS ở ≥ 95% khung.
- **AC-NFR-008.2**: IF frame rate < 45 FPS THEN đây là điều kiện **chặn phát hành**.
- **AC-NFR-008.3**: WHEN thẻ đổi thứ tự (FR-040) THEN crossfade 0,4s **không** làm giảm frame rate xuống dưới 60 FPS.

---

#### NFR-009: Performance — Third-Party API Timeout
**Priority**: Medium
**Requirement**: Mọi lệnh gọi Spotify API timeout ở **2,0 giây** rồi chuyển sang nguồn cục bộ; không có lệnh gọi mạng nào trên đường xử lý sound hoặc giọng chào.

**Measurement**: cấu hình `URLSession` timeout; kiểm bằng test mạng chậm (Network Link Conditioner).

**Acceptance Criteria**:
- **AC-NFR-009.1**: WHEN Spotify API không phản hồi trong 2,0s THEN hệ thống chuyển sang nguồn nhạc cục bộ và ghi `error_occurred`.
- **AC-NFR-009.2**: WHEN kiến trúc được rà soát THEN F1 (sound), F2 (widget) và F3 (giọng chào) **không** phụ thuộc Spotify — sự cố Spotify không hạ tính năng cốt lõi.

---

#### NFR-010: Security — Data Protection at Rest
**Priority**: High
**Requirement**: Mọi dữ liệu nhạy cảm lưu trên thiết bị phải được bảo vệ: token trong **Keychain**, cơ sở dữ liệu SQLite và App Group container bật **iOS Data Protection** ở mức `NSFileProtectionCompleteUntilFirstUserAuthentication` trở lên. **Không có API key dạng plain-text trong bundle.**

**Implementation**: Keychain cho token · Data Protection cho file · không nhúng secret vào Info.plist hay source.

**Acceptance Criteria**:
- **AC-NFR-010.1**: WHEN token được lưu THEN nó nằm trong Keychain, không nằm trong `UserDefaults`.
- **AC-NFR-010.2**: WHEN file dữ liệu được tạo THEN thuộc tính Data Protection được đặt ở mức tối thiểu nêu trên.
- **AC-NFR-010.3**: WHEN bundle được rà soát trước submission THEN không tìm thấy API key hay secret dạng plain-text.

---

#### NFR-011: Security — No PII in Telemetry
**Priority**: High
**Requirement**: Không có dữ liệu định danh cá nhân trong bất kỳ event analytics hay báo cáo tương thích nào. Payload chỉ chứa: kích thước màn hình, phiên bản iOS, hãng/model xe đã chọn, loại widget, `failure_reason`, và ghi chú tuỳ chọn do người dùng tự gõ.

**Measurement**: rà soát schema 28 event ở `PRD.md` §12; kiểm payload thực tế qua Charles/Proxyman trước mỗi lần submit.

**Acceptance Criteria**:
- **AC-NFR-011.1**: WHEN bất kỳ event nào được gửi THEN payload **không** chứa user ID, email, số điện thoại, toạ độ GPS, hay nội dung lịch.
- **AC-NFR-011.2**: WHEN người dùng gửi báo cáo tương thích THEN WF-028 liệt kê **từng mục** dữ liệu sẽ gửi kèm giá trị thật (liên quan FR-032).
- **AC-NFR-011.3**: WHEN người dùng bỏ tick một mục THEN mục đó **không** nằm trong payload gửi đi.

---

#### NFR-012: Security — No Network Call in Context Pipeline
**Priority**: High
**Requirement**: Toàn bộ đường xử lý ngữ cảnh (đọc nguồn → suy luận Core ML → sinh câu chào → sắp thứ tự thẻ) chạy **hoàn toàn on-device**, với **0 lệnh gọi mạng**.

**Measurement**: rà soát mã đường xử lý + kiểm bằng chế độ máy bay: giọng chào và dashboard vẫn hoạt động đầy đủ.

**Acceptance Criteria**:
- **AC-NFR-012.1**: WHEN giọng chào được sinh THEN không có lệnh gọi mạng nào phát ra từ tiến trình đó.
- **AC-NFR-012.2**: WHEN thiết bị ở chế độ máy bay THEN FR-037 và FR-040 vẫn hoạt động đầy đủ.
- **AC-NFR-012.3**: WHEN dữ liệu hành vi được lưu THEN nó **không rời thiết bị** ở MVP 1 và MVP 2 (ở MVP 3, chỉ **cấu hình** được đồng bộ — xem FR-064).

---

#### NFR-013: Security — Transport Security
**Priority**: High
**Requirement**: Mọi kết nối ra ngoài (Firebase, App Store Server Notification endpoint, Spotify) dùng **TLS 1.2 trở lên**; App Transport Security bật, không có exception domain.

**Acceptance Criteria**:
- **AC-NFR-013.1**: WHEN dữ liệu được truyền THEN TLS ≥ 1.2 được dùng.
- **AC-NFR-013.2**: WHEN Info.plist được rà soát THEN không có `NSAllowsArbitraryLoads` hay exception domain nào.

---

### 3.2 Additional NFRs (Based on App Type)

Carbina là app **iOS + CarPlay, on-device ML, có IAP, đa ngôn ngữ, chạy trên phần cứng phân mảnh nặng**. Bốn nhóm dưới đây là hệ quả trực tiếp của bốn đặc tính đó.

#### Usability

#### NFR-014: Accessibility
**Priority**: High
**Requirement**: Hỗ trợ **VoiceOver** (mọi phần tử tương tác có nhãn và hint), **Dynamic Type** (mọi chữ co giãn theo cài đặt hệ thống), **High Contrast**, và điều hướng bằng nút trên CarPlay. Mọi touch target **≥ 44pt**. Chữ trên màn hình xe **≥ 16pt** ở kích thước mặc định.

**Measurement**: Accessibility Inspector (0 lỗi mức error) · kiểm thủ công VoiceOver trên 5 màn hình chính · đo touch target trên từng kích thước trong test matrix.

**Acceptance Criteria**:
- **AC-NFR-014.1**: WHEN Accessibility Inspector chạy trên WF-002, WF-006, WF-007, WF-008, WF-010 THEN 0 lỗi mức error.
- **AC-NFR-014.2**: WHEN người dùng đặt Dynamic Type ở mức lớn nhất THEN không có chữ nào bị cắt giữa chữ trên mọi màn hình iPhone; trên CarPlay áp dụng truncate có ellipsis (liên quan FR-026).
- **AC-NFR-014.3**: WHEN mọi phần tử tương tác được đo THEN touch target ≥ 44pt trên cả iPhone và CarPlay.
- **AC-NFR-014.4**: WHEN High Contrast bật THEN độ tương phản chữ trên ảnh widget đạt tối thiểu 4,5:1 ở cả dark và light mode.

---

#### NFR-015: Localization
**Priority**: High
**Requirement**: **EN + ES + PT-BR** đầy đủ trong MVP 1, bao gồm **nội dung giọng chào AI**, không chỉ chuỗi UI. Giá luôn hiển thị theo **tiền tệ địa phương của storefront**, độc lập với ngôn ngữ UI.

**Measurement**: đếm số khoá chưa dịch trong mỗi `Localizable` (phải = 0) · kiểm ≥ 4 biến thể câu chào tồn tại cho **cả ba** ngôn ngữ · kiểm giá trên 3 storefront (US, MX, BR).

**Acceptance Criteria**:
- **AC-NFR-015.1**: WHEN mỗi bộ ngôn ngữ được kiểm THEN số khoá chưa dịch = 0 cho cả ba ngôn ngữ.
- **AC-NFR-015.2**: WHEN ngôn ngữ là ES hoặc PT-BR THEN có ≥ 4 biến thể câu chào ngữ cảnh bằng đúng ngôn ngữ đó.
- **AC-NFR-015.3**: IF một chuỗi thiếu bản dịch THEN hệ thống rơi về English cho **đúng chuỗi đó**, không hiện khoá dịch thô (liên quan FR-056).
- **AC-NFR-015.4**: WHEN giá hiển thị THEN dùng định dạng tiền tệ của storefront hiện tại, không quy đổi thủ công.

---

#### NFR-016: Offline Capability
**Priority**: High
**Requirement**: App phải hoạt động đầy đủ ở các tính năng cốt lõi khi **không có mạng**: widget render, sound phát, giọng chào phát, dashboard hiển thị từ cache, thư viện xe tìm kiếm được.

**Measurement**: chạy toàn bộ 13 task flow của `Use_Cases.md` §5 ở chế độ máy bay; ghi nhận flow nào bị chặn.

**Acceptance Criteria**:
- **AC-NFR-016.1**: WHEN thiết bị không có mạng THEN FR-016, FR-019, FR-029, FR-037, FR-040 và FR-004 hoạt động đầy đủ.
- **AC-NFR-016.2**: WHEN thẻ dashboard dùng dữ liệu cache THEN thời điểm cập nhật cuối được hiển thị rõ (liên quan FR-041).
- **AC-NFR-016.3**: WHEN người dùng gửi yêu cầu thêm xe hoặc báo cáo tương thích khi offline THEN dữ liệu được xếp hàng on-device và gửi khi có mạng, xác nhận cho người dùng trong ≤ 500ms (liên quan FR-006, FR-032).
- **AC-NFR-016.4**: WHEN không có mạng THEN **không** màn hình nào của app hiển thị trạng thái lỗi toàn màn hình.

---

#### Reliability

#### NFR-017: Crash-Free Sessions
**Priority**: High
**Requirement**: **≥ 99,2%** phiên không crash ở tháng 3; **≥ 99,5%** ở tháng 6. Widget extension được tính riêng với cùng ngưỡng. *(Đây là NFR phủ **F11 — Crash Reporting** của PRD §7, tính năng không có bề mặt người dùng nên không có UC.)*

**Implementation**: Firebase Crashlytics tự động thu crash · upload dSYM cho mọi bản build · alert khi crash-free tụt dưới ngưỡng.

**Acceptance Criteria**:
- **AC-NFR-017.1**: WHEN đo trên toàn bộ phiên tháng 3 THEN crash-free ≥ 99,2%.
- **AC-NFR-017.2**: WHEN đo trên toàn bộ phiên tháng 6 THEN crash-free ≥ 99,5%.
- **AC-NFR-017.3**: IF crash-free trên TestFlight < 99,0% THEN đây là điều kiện **chặn phát hành**.
- **AC-NFR-017.4**: WHEN mỗi bản build được phát hành THEN dSYM đã được upload để stack trace đọc được.

---

#### NFR-018: Handled Error Rate
**Priority**: Medium
**Requirement**: Tỉ lệ lỗi đã xử lý (`error_occurred` / phiên) **< 0,5%** ở tháng 3 và **< 0,3%** ở tháng 6.

**Acceptance Criteria**:
- **AC-NFR-018.1**: WHEN đo theo tháng THEN tỉ lệ `error_occurred`/phiên đạt ngưỡng tương ứng.
- **AC-NFR-018.2**: WHEN một lỗi được xử lý THEN nó luôn kèm một đường phục hồi hiển thị cho người dùng — **không** có lỗi nào chỉ được ghi log rồi im lặng.

---

#### NFR-019: Widget Render Success Rate
**Priority**: High
**Requirement**: **≥ 90%** ở tháng 3 và **≥ 95%** ở tháng 6, tính bằng `widget_render_ok` / `carplay_connected`. Đây là **chỉ số kỹ thuật quan trọng nhất của dự án** (rủi ro R-11).

**Measurement**: Firebase dashboard theo ngày, chia nhóm theo `screen_width` × `screen_height`.

**Acceptance Criteria**:
- **AC-NFR-019.1**: WHEN đo theo tháng THEN tỉ lệ đạt ngưỡng tương ứng.
- **AC-NFR-019.2**: IF tỉ lệ tụt dưới 90% trong bất kỳ ngày nào THEN hệ thống phát cảnh báo tự động cho PM **trong ≤ 24 giờ** (liên quan FR-066).
- **AC-NFR-019.3**: IF cùng một cặp kích thước thất bại ≥ 3 lần THEN cặp đó được đánh dấu ưu tiên cao trong telemetry.

---

#### NFR-020: No Blank Surface on CarPlay
**Priority**: High
**Requirement**: **0 trường hợp** màn hình trắng hoặc vùng trắng không có nội dung trên bề mặt CarPlay, ở mọi nhánh lỗi.

**Measurement**: chạy toàn bộ ma trận lỗi (vượt bounds · hết bộ nhớ · thiếu entitlement · thiếu quyền · offline · iOS 17.3) trên từng kích thước trong test matrix và ghi nhận từng kết quả hiển thị.

**Acceptance Criteria**:
- **AC-NFR-020.1**: WHEN bất kỳ nhánh lỗi nào xảy ra trên CarPlay THEN màn hình luôn hiển thị nội dung chữ giải thích (liên quan FR-031).
- **AC-NFR-020.2**: WHEN chỉ widget lỗi THEN WF-016 vẫn hoạt động đầy đủ — không hạ toàn bộ bề mặt CarPlay.
- **AC-NFR-020.3**: WHEN ma trận lỗi được chạy hết THEN số trường hợp màn trắng = 0. Đây là điều kiện **chặn phát hành**.

---

#### Compatibility

#### NFR-021: CarPlay Screen Compatibility
**Priority**: High
**Requirement**: Layout tính từ `CPTemplateApplicationScene` bounds tại runtime; **không tồn tại hằng số kích thước màn hình xe nào trong code layout**. Test matrix bắt buộc: **≥ 4 kích thước màn hình CarPlay + ≥ 1 xe thật cho mỗi nhóm**.

**Measurement**: grep codebase tìm hằng số point trong đường layout CarPlay (kết quả phải rỗng) · biên bản test trên từng kích thước và từng xe thật.

**Acceptance Criteria**:
- **AC-NFR-021.1**: WHEN code layout CarPlay được rà soát THEN không tìm thấy hằng số kích thước màn hình xe nào. Đây là mục kiểm ở code review, không phải kiểm tại runtime.
- **AC-NFR-021.2**: WHEN test matrix được chạy THEN ≥ 4 kích thước + ≥ 1 xe thật mỗi nhóm đều pass, gồm nhóm màn 8" (đã ghi nhận lỗi ở đối thủ).
- **AC-NFR-021.3**: WHEN gặp kích thước chưa từng thấy THEN widget vẫn render đúng vì layout tính tại runtime, **không tra bảng xe** (liên quan FR-029).

---

#### NFR-022: iOS Version Support & Graceful Degradation
**Priority**: High
**Requirement**: Deployment target **iOS 16.4**; tính năng widget CarPlay yêu cầu **iOS 17.4+** và được bọc trong kiểm tra khả dụng. Người dùng iOS 16.4–17.3 dùng được sound, giọng chào, thư viện xe, dashboard cơ bản.

**Acceptance Criteria**:
- **AC-NFR-022.1**: WHEN app chạy trên iOS 16.4–17.3 THEN không có crash nào liên quan API chỉ có ở 17.4+.
- **AC-NFR-022.2**: WHEN người dùng ở iOS < 17.4 mở WF-008 THEN hệ thống nêu rõ yêu cầu iOS 17.4+ và **vẫn cho cấu hình và lưu** (liên quan FR-024).
- **AC-NFR-022.3**: WHEN người dùng nâng cấp lên iOS 17.4+ THEN widget đã cấu hình sẵn render ngay ở lần cắm kế tiếp, không cần cấu hình lại.
- **AC-NFR-022.4**: WHEN thiết bị không có Apple Neural Engine (dưới iPhone 12) THEN thiết bị đó **nằm ngoài danh sách hỗ trợ**; App Store minimum device được đặt tương ứng.

---

#### Scalability

#### NFR-023: Backend & Cost Ceiling
**Priority**: Medium
**Requirement**: MVP 1 **không có backend riêng**. Hạ tầng chỉ gồm Firebase (managed) và một endpoint nhận App Store Server Notification V2. Chi phí hạ tầng mục tiêu **≤ $100/tháng** ở quy mô 50.000 install và 12.500 DAU.

**Measurement**: hoá đơn Firebase theo tháng · số event/ngày so với hạn mức free tier.

**Acceptance Criteria**:
- **AC-NFR-023.1**: WHEN DAU đạt 12.500 THEN chi phí hạ tầng ≤ $100/tháng.
- **AC-NFR-023.2**: WHEN endpoint nhận notification hoàn tiền THEN nó xử lý được ≥ 100 notification/phút mà không mất dữ liệu.
- **AC-NFR-023.3**: WHEN Firebase gặp sự cố THEN app vẫn hoạt động đầy đủ ở mọi tính năng người dùng — mất telemetry **không** được hạ trải nghiệm.

> **Ghi chú về concurrent users**: MVP 1 không có yêu cầu người dùng đồng thời vì không có backend phục vụ người dùng. Yêu cầu này sẽ xuất hiện ở MVP 3 khi có cloud sync (FR-064) và **chưa được đặc tả** ở tài liệu này — đây là khoảng trống có ý thức, không phải bỏ sót.

---

#### Quality

#### NFR-024: Test Coverage & Build Hygiene
**Priority**: High
**Requirement**: **≥ 80%** test coverage cho tầng `Core/` (logic domain; tầng View không tính vào con số này). **0 cảnh báo Xcode** trước khi submit.

**Measurement**: Xcode code coverage giới hạn ở target `Core/` · build log.

**Acceptance Criteria**:
- **AC-NFR-024.1**: WHEN test suite chạy THEN coverage của `Core/` ≥ 80%.
- **AC-NFR-024.2**: WHEN build phát hành được tạo THEN số cảnh báo Xcode = 0. Đây là điều kiện **chặn submission**.
- **AC-NFR-024.3**: WHEN logic layout CarPlay được test THEN có property-based test kiểm rằng **với mọi cặp (width, height) trong dải hợp lệ**, không phần tử nào vượt bounds — đây là cách kiểm R-11 không phụ thuộc danh sách xe.

---

## 4. Requirements Summary

### 4.1 Functional Requirements by Priority

Cột **Module** dùng đúng cây thư mục ở `Project_Overview.md` §3.3 Quyết định 7, để `spec-design` ở giai đoạn thi công không phải suy diễn lại vị trí file.

| ID | Requirement | Priority | Module | Status |
|---|---|---|---|---|
| FR-001 | Điều phối luồng onboarding 5 bước | High | `Features/Onboarding` | Planned |
| FR-002 | Lưu và phục hồi tiến trình onboarding | High | `Features/Onboarding` | Planned |
| FR-003 | Phục hồi giao dịch trong onboarding | Medium | `Core/Entitlement` | Planned |
| FR-004 | Thư viện xe và tìm kiếm on-device | High | `Core/Persistence` | Planned |
| FR-005 | Gán ảnh xe và fallback silhouette | High | `Features/Onboarding` | Planned |
| FR-006 | Gửi yêu cầu thêm xe vào thư viện | Medium | `Features/Onboarding` | Planned |
| FR-007 | Trình bày lý do quyền và thu nhận quyết định | High | `Features/Onboarding` | Planned |
| FR-008 | Suy giảm chức năng theo trạng thái quyền | High | `Core/ML` · `Core/Audio` | Planned |
| FR-009 | Splash và định tuyến khởi động | High | `App` | Planned |
| FR-010 | Danh mục sound và phân tầng Free/Premium | High | `Features/SoundLibrary` | Planned |
| FR-011 | Nghe thử sound inline trong danh sách | High | `Features/SoundLibrary` | Planned |
| FR-012 | Nghe thử sound trong sheet chuyên dụng | High | `Features/SoundLibrary` | Planned |
| FR-013 | Gán sound cho sự kiện Connect | High | `Core/Audio` | Planned |
| FR-014 | Gán sound cho Disconnect và Arrive | Medium | `Core/Audio` | Planned |
| FR-015 | Âm lượng sound độc lập với nhạc | High | `Core/Audio` | Planned |
| FR-016 | Phát sound Connect kèm ducking | High | `Core/Audio` | Planned |
| FR-017 | Chính sách nhường phiên audio | High | `Core/Audio` | Planned |
| FR-018 | Chống phát trùng khi kết nối chập chờn | High | `Core/Audio` | Planned |
| FR-019 | Phát sound Disconnect đúng thời điểm tắt máy | High | `Core/Audio` | Planned |
| FR-020 | Định tuyến đầu ra loa xe và chính sách không phát bù | High | `Core/Audio` | Planned |
| FR-021 | Preset widget gợi ý theo xe đã chọn | High | `Features/WidgetBuilder` | Planned |
| FR-022 | Lưu cấu hình widget vào App Group | High | `Core/Persistence` | Planned |
| FR-023 | Giới hạn số widget theo entitlement | High | `Core/Entitlement` | Planned |
| FR-024 | Xử lý ngưỡng iOS 17.4 cho widget CarPlay | High | `Features/WidgetBuilder` | Planned |
| FR-025 | Preview widget theo tỉ lệ màn hình xe | High | `Features/WidgetBuilder` | Planned |
| FR-026 | Phát hiện và báo phần tử vượt vùng an toàn | High | `Core/CarPlay` | Planned |
| FR-027 | Chọn ảnh và crop theo tỉ lệ màn hình xe | Medium | `Features/WidgetBuilder` | Planned |
| FR-028 | Kiểm độ phân giải và nén ảnh widget | Medium | `Features/WidgetBuilder` | Planned |
| FR-029 | Render widget theo scene bounds tại runtime | High | `Core/CarPlay` · `CarbinaWidget` | Planned |
| FR-030 | Giảm cấp layout khi thiếu không gian | High | `Core/CarPlay` | Planned |
| FR-031 | Fallback CarPlay khi render thất bại | High | `Features/CarPlayDashboard` | Planned |
| FR-032 | Chẩn đoán tương thích và gửi báo cáo | Medium | `Features/Diagnostics` | Planned |
| FR-033 | Bật hoặc tắt hoàn toàn giọng chào | High | `Features/VoiceGreeting` | Planned |
| FR-034 | Quản lý nguồn ngữ cảnh của giọng chào | Medium | `Features/VoiceGreeting` | Planned |
| FR-035 | Chặn bật nguồn ngữ cảnh thiếu quyền | Medium | `Features/VoiceGreeting` | Planned |
| FR-036 | Nghe thử giọng chào sinh on-device | High | `Core/ML` · `Core/Audio` | Planned |
| FR-037 | Sinh và phát giọng chào khi lên xe | High | `Core/ML` · `Core/Audio` | Planned |
| FR-038 | Chống lặp câu chào và ràng buộc nội dung | High | `Core/ML` | Planned |
| FR-039 | Nội dung giọng chào theo ngôn ngữ | Medium | `Core/ML` · `Resources` | Planned |
| FR-040 | Sắp xếp thẻ dashboard theo ngữ cảnh on-device | High | `Core/ML` · `Features/CarPlayDashboard` | Planned |
| FR-041 | Cấu hình dashboard theo entitlement và trạng thái offline | High | `Features/CarPlayDashboard` | Planned |
| FR-042 | Thực thi hành động khi chạm thẻ dashboard | High | `Features/CarPlayDashboard` | Planned |
| FR-043 | EntitlementService là nguồn chân lý duy nhất | High | `Core/Entitlement` | Planned |
| FR-044 | Cấu hình gói Free vô thời hạn | High | `Core/Entitlement` | Planned |
| FR-045 | Chính sách hiển thị paywall | High | `Core/Entitlement` · `Features/Paywall` | Planned |
| FR-046 | Trình bày 4 bậc giá từ StoreKit | High | `Features/Paywall` | Planned |
| FR-047 | Cấm hiển thị giá cache hoặc giá hardcode | High | `Features/Paywall` | Planned |
| FR-048 | Màn xác nhận giá là điểm chặn duy nhất | High | `Features/Paywall` | Planned |
| FR-049 | Xử lý giao dịch StoreKit và mở khóa tính năng | High | `Core/Entitlement` | Planned |
| FR-050 | Gửi xác nhận giao dịch sau khi mua | High | `Core/Entitlement` | Planned |
| FR-051 | Quản lý trial 7 ngày và hiển thị đếm ngày | High | `Core/Entitlement` | Planned |
| FR-052 | Nhắc trước khi hết trial | Medium | `Features/Paywall` | Planned |
| FR-053 | Quản lý, huỷ đăng ký và phục hồi giao dịch | Medium | `Features/Paywall` · `Core/Entitlement` | Planned |
| FR-054 | Mua và phục hồi gói Lifetime | Medium | `Core/Entitlement` | Planned |
| FR-055 | Chọn ngôn ngữ và áp dụng tức thì | Medium | `Features/Settings` · `Resources` | Planned |
| FR-056 | Fallback khi thiếu bản dịch | Medium | `Resources` | Planned |
| FR-057 | Hiển thị và xoá dữ liệu học on-device | Medium | `Features/Settings` · `Core/Persistence` | Planned |
| FR-058 | Tách xoá dữ liệu học khỏi xoá cấu hình | Medium | `Core/Persistence` | Planned |
| FR-059 | Mời đánh giá có điều kiện và phân luồng | Medium | `Features/Settings` | Planned |
| FR-060 | Kênh phản hồi cho người không hài lòng | Medium | `Features/Diagnostics` | Planned |
| FR-061 | Đổi theme và áp dụng tức thì | Medium | `Features/Settings` | Planned |
| FR-062 | Lối vào trạng thái quyền từ Settings | Medium | `Features/Settings` | Planned |
| FR-063 | Contacts favorites và gọi một chạm *(MVP 2)* | Medium | `Features/CarPlayDashboard` | Deferred |
| FR-064 | Đăng nhập và đồng bộ cấu hình opt-in *(MVP 3)* | Low | `Features/Settings` | Deferred |
| FR-065 | Xoá tài khoản và dữ liệu cloud *(MVP 3)* | Low | `Features/Settings` | Deferred |
| FR-066 | Telemetry, sự kiện vận hành và cảnh báo | Medium | `Core/Analytics` | Planned |

**Tổng: 66 FR — 42 High · 22 Medium · 2 Low.** Kèm theo: **206 BR · 87 VR · 183 ERR · 166 AC** trải trên 7 sub-spec.
**Theo giai đoạn**: 63 FR thuộc MVP 1 (`Planned`) · 1 FR thuộc MVP 2 · 2 FR thuộc MVP 3 (`Deferred`).

**Bốn FR không được cắt trong mọi trường hợp** (nhắc lại từ `Use_Cases.md` §7.1, quy chiếu sang FR): **FR-008** (dùng được khi từ chối quyền) · **FR-031** (fallback khi render lỗi) · **FR-032** (chẩn đoán) · **FR-044** (gói Free). Cả bốn là lớp phòng vệ cho R-11, R-04, R-12 — cắt chúng là bỏ lớp phòng vệ, không phải tiết kiệm phạm vi.

### 4.2 Non-Functional Requirements by Category

| Category | Count | Priority Breakdown | NFR IDs |
|---|---|---|---|
| Performance | 9 | 8 High, 1 Medium | NFR-001 → NFR-009 |
| Security | 4 | 4 High | NFR-010 → NFR-013 |
| Usability | 3 | 3 High | NFR-014 (Accessibility) · NFR-015 (Localization) · NFR-016 (Offline) |
| Reliability | 4 | 3 High, 1 Medium | NFR-017 → NFR-020 |
| Compatibility | 2 | 2 High | NFR-021 (màn hình CarPlay) · NFR-022 (phiên bản iOS) |
| Scalability | 1 | 1 Medium | NFR-023 |
| Quality | 1 | 1 High | NFR-024 |
| **Tổng** | **24** | **20 High, 4 Medium** | NFR-001 → NFR-024 |

**Bảy NFR là điều kiện chặn phát hành**: NFR-001 (> 3,0s p95) · NFR-008 (< 45 FPS) · NFR-017 (crash-free TestFlight < 99,0%) · NFR-020 (bất kỳ trường hợp màn trắng nào trên CarPlay) · NFR-021 (test matrix chưa pass) · NFR-024 (còn cảnh báo Xcode) · và NFR-019 khi Widget Render Success Rate < 90% ở giai đoạn TestFlight.

**Ràng buộc NFR ↔ FR** (NFR nào ràng buộc FR nào — dùng cho `Project_Implementation_Roadmap.md` khi xếp phase):

| NFR | Ràng buộc các FR |
|---|---|
| NFR-003, NFR-009 | FR-016, FR-017, FR-018, FR-019, FR-020 |
| NFR-004, NFR-005, NFR-012 | FR-036, FR-037, FR-038, FR-040 |
| NFR-007, NFR-019, NFR-020, NFR-021 | FR-022, FR-026, FR-029, FR-030, FR-031, FR-032 |
| NFR-010, NFR-011 | FR-032, FR-057, FR-058, FR-066 |
| NFR-014 | FR-026, FR-029, FR-042, và mọi FR có bề mặt người dùng |
| NFR-015 | FR-039, FR-046, FR-055, FR-056 |
| NFR-016 | FR-004, FR-006, FR-016, FR-029, FR-032, FR-037, FR-040, FR-041 |
| NFR-022 | FR-024, FR-029 |
| NFR-023 | FR-050, FR-066 |
| NFR-024 | FR-026, FR-029, FR-030 |

### 4.3 Traceability Verification

Bốn phép kiểm bắt buộc của `project-docs-fr` Step 6, chạy sau khi viết xong toàn bộ FR:

| Phép kiểm | Cách kiểm | Kết quả |
|---|---|---|
| **1. Forward check** — mọi UC ở `Use_Cases.md` §2 xuất hiện trong trường `Source UC` của ≥ 1 FR | §2.1 liệt kê UC-001 → UC-036 kèm FR phủ từng UC | **36/36 Pass** — không UC nào bị bỏ |
| **2. Backward check** — mọi FR có `Source UC` hợp lệ trỏ tới UC tồn tại | Mỗi FR trong 7 sub-spec có trường `Source UC` ở đầu khối | **66/66 Pass** — không có FR mồ côi |
| **3. Context check** — mọi `ERR-xxx.y` tương ứng một `AF-xxx.y` của UC nguồn | Mỗi ERR trong sub-spec ghi rõ AF nguồn trong ngoặc | **Pass** — 110 AF của UC được phủ; các ERR bổ sung không đến từ AF đều được ghi nguồn là **State Variation** ở `Use_Cases.md` §4 hoặc **Recovery Path** ở §5 |
| **4. AC carry-forward check** — mọi `AC-xxx.y` trong FR trùng **nguyên văn** với AC trong UC | So từng câu AC giữa sub-spec và `Use_Cases.md` §2 | **166/166 Pass** — không câu nào bị viết lại. Ngoại lệ duy nhất được ghi nhận: **AC-036.1 → AC-036.3** ban đầu không tồn tại ở UC; thay vì để tầng FR tự nghĩ ra, **UC-036 đã được bổ sung vào `Use_Cases.md`** rồi FR-061 mang các AC đó sang (xem ghi chú ở cuối `FR_settings_privacy.md`) |

**Về nguyên tắc "không FR trùng lặp"**: không FR nào có thân là "giống FR-XXX". Hai chỗ dễ trùng nhất đã được phân biệt rõ:
- **FR-011 vs FR-012** (nghe thử inline vs nghe thử trong sheet): khác component, khác dữ liệu vào (FR-012 có mức âm lượng và bộ chọn sự kiện), khác kết quả (FR-011 không gán, FR-012 gán được).
- **FR-032 vs FR-060** (gửi báo cáo chẩn đoán vs kênh phản hồi khi không hài lòng): cùng dùng WF-028 nhưng khác điểm khởi phát, khác dữ liệu bắt buộc (FR-032 bắt buộc có kích thước màn hình; FR-060 bắt buộc có ghi chú của người dùng), và khác mục tiêu đo (FR-032 phục vụ NFR-019; FR-060 phục vụ KPI Recent 1★ Ratio).

**Về nguyên tắc "không hard-depend vào tham số chưa chốt"**: mọi giá trị mà FR/BR/AC/NFR phụ thuộc đều đã có Default trong `PRD.md` §14 — cấu hình gói Free (1 widget + 3 sound + dashboard cơ bản), độ dài trial (7 ngày), bậc giá ($4,99 / $29,99 / $49,99, không weekly), commission 15%, số kích thước phải test (≥ 4 + 1 xe thật/nhóm), framework ML (Core ML + Create ML), TTS (`AVSpeechSynthesizer`), ngôn ngữ MVP 1 (EN/ES/PT-BR), Contacts ở MVP 2, chỉ Apple Maps ở MVP 1. **Không có FR nào tự chọn giá trị mà PRD chưa chốt.**

Ba giá trị vẫn đang mở ở `PRD.md` §14 và **không** được FR nào phụ thuộc cứng: Coin IAP (FR-054 chỉ đặc tả Lifetime, Coin sẽ là FR mới ở MVP 2) · retention benchmark của đối thủ (chỉ ảnh hưởng mục tiêu KPI, không ảnh hưởng hành vi hệ thống) · trademark "Carbina" (không có FR nào phụ thuộc tên).

---

**Document Version**: 2.4
**Last Updated**: 2026-08-07 (snapshot bộ tài liệu; file tạo ngày 2026-08-17)
**Status**: Draft — chờ PO review
**Dependencies**: `PRD.md` v2.4 · `Project_Overview.md` v2.4 · `Use_Cases.md` v2.4
**Sub-specs**: `FR_onboarding.md` · `FR_sound.md` · `FR_widget.md` · `FR_voice_dashboard.md` · `FR_monetization.md` · `FR_settings_privacy.md` · `FR_postmvp.md`
**Bước kế tiếp**: `gate-fr` → phê duyệt → **Step 5: `Wireframes.md`** (30 màn hình WF-001 → WF-030, ràng buộc responsive của NFR-021 là điều kiện thiết kế bắt buộc cho mọi màn CarPlay)
