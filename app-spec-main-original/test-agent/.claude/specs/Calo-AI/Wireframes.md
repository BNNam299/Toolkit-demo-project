# Calo AI - Bản Thiết Kế Giao Diện (Wireframes)

**Phiên bản**: 1.0  
**Ngày**: 2026-07-21  
**Tác giả**: Đại lý Nghiên cứu AI  
**Chế độ**: Các Bản Thiết Kế MVP  
**Trạng thái**: Giai đoạn 1 — Các màn hình cốt lõi (WF-001 đến WF-008)

---

## 1. Giới Thiệu

### 1.1 Mục Đích

Tài liệu này định nghĩa **giao diện người dùng** (bố cục UI, thành phần, tương tác) cho tất cả các màn hình trong Calo AI MVP. Mỗi wireframe có liên kết truy nguyên tới Functional_Requirements.md (FR) và Use_Cases.md (UC).

### 1.2 Nguyên Tắc Thiết Kế

- **Đơn Giản**: Giao diện sạch sẽ, không lộn xộn, một chức năng chính trên mỗi màn hình
- **Nhất Quán**: Thiết kế thống nhất, tái sử dụng component, các mẫu điều hướng nhất quán
- **Hỗ Trợ Tiếp Cận**: Hỗ trợ VoiceOver, Dynamic Type, WCAG 2.1 AA
- **iOS Gốc**: Tuân theo Apple Human Interface Guidelines, các thành phần SwiftUI

### 1.3 Hệ Thống Thiết Kế

**Kiểu Chữ**:
- **Display (Lớn)**: SF Pro, 32pt, semibold (tiêu đề)
- **Tiêu Đề**: SF Pro, 28pt, semibold (tiêu đề phần)
- **Headline**: SF Pro, 24pt, semibold (tiêu đề màn hình)
- **Nội Dung**: SF Pro, 16pt, regular (văn bản chính)
- **Nội Dung Nhỏ**: SF Pro, 14pt, regular (văn bản phụ)
- **Chú Thích**: SF Pro, 12pt, regular (văn bản trợ giúp)

**Bảng Màu** (các màu hệ thống iOS + tùy chỉnh):
- Chính (Hành Động): #007AFF (xanh iOS) — nút, liên kết, điểm nhấn
- Phụ: #5AC8FA (xanh nhạt) — CTA phụ
- Thành Công: #34C759 (xanh lá iOS) — trạng thái tích cực, tiến độ
- Cảnh Báo: #FF9500 (cam iOS) — trạng thái cảnh báo
- Lỗi: #FF3B30 (đỏ iOS) — lỗi, hành động tàn phá
- Nền: #FFFFFF (sáng) / #000000 (chế độ tối)
- Văn Bản Chính: #000000 (sáng) / #FFFFFF (tối)
- Văn Bản Phụ: #666666 (sáng) / #CCCCCC (tối)
- Đường Phân Cách: #E5E5EA (sáng) / #333333 (tối)

**Khoảng Cách** (lưới 8pt):
- XS: 4pt | SM: 8pt | MD: 16pt | LG: 24pt | XL: 32pt | XXL: 48pt

**Bán Kính Góc**:
- SM: 4pt (tinh tế, đầu vào biểu mẫu)
- MD: 8pt (thẻ, modal)
- LG: 12pt (nút nổi bật)
- XL: 16pt (hình đại diện bo tròn)
- Toàn Bộ: 9999pt (hình tròn)

### 1.4 Tham Chiếu Bên Ngoài & Dự Phòng

| Tham Chiếu Bên Ngoài | Nếu Có Sẵn | Dự Phòng Nếu Thiếu |
|---|---|---|
| `ios-components` skill | Sử dụng định nghĩa thành phần | Dùng danh sách thành phần nội tuyến §4 |
| `ios-ui-ux` skill | Dùng hướng dẫn UX | Dùng §5–§7 ở đây |
| `mcp-figma` | Trích token từ Figma | Dùng ASCII wireframes + §1.3 |
| `DESIGN_TOKEN_[name].json` | Dùng giá trị token | Dùng đường dẫn token §1.3 |
| Figma file | Liên kết file | Đánh dấu "(chưa tạo)"; wireframes ở đây có thẩm quyền |

**Mô Hình Điều Hướng iOS** (tái sử dụng):
- **Tab (Chính)**: 3 tab dưới: Camera | Nhật Ký | Tài Khoản (49pt)
- **Modal/Sheet**: Paywall, Xác nhận, Chỉnh sửa (ở giữa hoặc bottom)

---

## 2. Danh Sách Màn Hình

### 2.1 Các Màn Hình Bắt Buộc (Cho tất cả dự án)

| ID Màn Hình | Tên Màn Hình | Ưu Tiên | FR Liên Quan | UC Liên Quan | Kiến Trúc | Trạng Thái |
|-----------|------------|--------|-----------|------------|---------|---------|
| WF-001 | Splash | Cao | — | — | Tiêu Thụ | Bản Nháp |
| WF-008 | Onboarding (Nhiều bước) | Cao | FR-018, FR-019, FR-020 | UC-016, UC-017, UC-018 | Hành Động | Bản Nháp |
| WF-006 | Paywall / Đăng Ký | Cao | FR-021, FR-022, FR-023 | UC-019, UC-020 | Hành Động | Bản Nháp |

### 2.2 Các Màn Hình Cốt Lõi MVP (17 tổng cộng)

| ID Màn Hình | Tên Màn Hình | Ưu Tiên | FR Liên Quan | UC Liên Quan | Kiến Trúc | Mật Độ |
|-----------|------------|--------|-----------|------------|---------|--------|
| WF-002 | Camera (Chụp Ảnh) | Cao | FR-001, FR-002, FR-009 | UC-001, UC-002, UC-009 | Hành Động | Dày Đặc |
| WF-003 | Xác Nhận (Chỉnh Sửa Nguyên Liệu) | Cao | FR-003, FR-004, FR-005, FR-006, FR-007, FR-008 | UC-003, UC-004, UC-005, UC-006, UC-007, UC-008 | Hành Động | Dày Đặc |
| WF-004 | Nhật Ký (Bản Ghi Hàng Ngày) | Cao | FR-012, FR-013, FR-014, FR-015, FR-016, FR-017 | UC-011, UC-012, UC-013, UC-014, UC-015 | Tiêu Thụ | Dày Đặc |
| WF-005 | Bảng Điều Khiển (Thông Tin Chi Tiết Tuần) | Trung Bình | FR-014 | UC-013 | Tiêu Thụ | Vừa |
| WF-007 | Cài Đặt / Tài Khoản | Trung Bình | FR-024, FR-025, FR-026 | UC-021, UC-022, UC-023 | Quản Lý | Vừa |
| WF-009 | Yêu Cầu Quyền | Cao | FR-001 AF | UC-001 AF | Hành Động | Nhẹ |
| WF-010 | Trạng Thái Tải AI | Cao | FR-003 | UC-003 | Tiêu Thụ | Nhẹ |
| WF-013 | Modal Chỉnh Sửa Bản Ghi | Trung Bình | FR-015, FR-016 | UC-014 | Hành Động | Vừa |
| WF-014 | Modal Xác Nhận Xoá | Trung Bình | FR-017 | UC-015 | Hành Động | Nhẹ |
| WF-018 | Modal Huỷ Đăng Ký | Trung Bình | FR-024 | UC-021 | Hành Động | Nhẹ |

**Phạm Vi Màn Hình**:
- Tổng cộng màn hình MVP: 17 (3 bắt buộc + 14 bổ sung)
- Ưu tiên cao: 10 màn hình
- Ưu tiên trung bình: 7 màn hình
- Tất cả FR ưu tiên cao có ≥1 màn hình ✓
- Tất cả FR ưu tiên trung bình có ≥1 màn hình ✓

---

## 2 bis. Phân Loại Màn Hình

### Gán Kiến Trúc

| ID WF | Tên Màn Hình | Kiến Trúc Chính | Mật Độ Tương Tác | Hành Vi Chính |
|-------|------------|------|------|------|
| WF-001 | Splash | Tiêu Thụ | Nhẹ | Tự động loại bỏ (2s), logo thương hiệu, spinner tải |
| WF-002 | Camera | Hành Động | Dày Đặc | Live preview, nút chụp, bộ chọn thư viện ảnh, xử lý quyền |
| WF-003 | Xác Nhận | Hành Động | Dày Đặc | Danh sách nguyên liệu (checkboxes), bộ chọn khẩu phần, hiển thị macro, lưu/thử lại |
| WF-004 | Nhật Ký | Tiêu Thụ | Dày Đặc | Danh sách bữa ăn, thanh tiến độ, tổng cộng hàng ngày, vuốt để chỉnh sửa/xoá |
| WF-005 | Bảng Điều Khiển | Tiêu Thụ | Vừa | Biểu đồ tuần, phân tích macro, thống kê trung bình, xuất/chia sẻ |
| WF-006 | Paywall | Hành Động | Vừa | Đề nghị dùng thử, các tầng giá, danh sách lợi ích, nút mua |
| WF-007 | Cài Đặt | Quản Lý | Vừa | Thông tin hồ sơ, trạng thái đăng ký, thanh toán, tùy chọn tài khoản |
| WF-008 | Onboarding | Hành Động | Nhẹ | Biểu mẫu nhiều bước (chiều cao/cân nặng, mức hoạt động, xác nhận mục tiêu) |
| WF-009 | Quyền | Hành Động | Nhẹ | Hộp thoại quyền iOS gốc, liên kết cài đặt dự phòng |
| WF-010 | Tải AI | Tiêu Thụ | Nhẹ | Hoạt ảnh spinner, văn bản "Đang phân tích...", tùy chọn hủy |
| WF-013 | Modal Chỉnh Sửa | Hành Động | Vừa | Biểu mẫu đã điền sẵn, danh sách nguyên liệu, nút lưu/hủy |
| WF-014 | Modal Xoá | Hành Động | Nhẹ | Tin nhắn cảnh báo, nút xác nhận/hủy |
| WF-018 | Modal Huỷ | Hành Động | Nhẹ | Tin nhắn xác nhận, nút tiếp tục/hủy |

---

## 3. Các Đặc Tả Màn Hình Cốt Lõi

### WF-001: Màn Hình Splash

**Kiến Trúc**: Tiêu Thụ | **Ưu Tiên**: Cao | **FR Liên Quan**: — | **UC Liên Quan**: —

**Mục Đích**: Màn hình khởi động ứng dụng; hiển thị thương hiệu, khởi tạo trạng thái ứng dụng (xác thực, đồng bộ dữ liệu)

**Bố Cục**:
- Vùng A (Anh Hùng): Logo thương hiệu (ở giữa, 120x120pt) + tên ứng dụng "Calo"
- Vùng B (Engagement): Spinner tải (hoạt ảnh, không xác định)
- Vùng C (Khám Phá): —
- Vùng D (Tiện Ích): —

**Thành Phần**:
- Hình ảnh logo (UIImage hoặc SF Symbol)
- Chỉ báo tải (SwiftUI ProgressView, kiểu tròn)
- Văn bản tên ứng dụng (SF Pro, 28pt, semibold)

**Tương Tác**:
- Tự động loại bỏ sau 2 giây (hoặc khi trạng thái ứng dụng sẵn sàng)
- Không yêu cầu hành động của người dùng
- Màn hình tiếp theo: WF-008 (Onboarding) nếu người dùng mới, WF-002 (Camera) nếu đã quay lại

**Trạng Thái**:
- Tải: Spinner hiển thị, văn bản "Đang khởi tạo..."
- Hoàn Tất: Loại bỏ bằng hoạt ảnh mờ dần

**Hỗ Trợ Tiếp Cận**:
- Logo có nhãn tiếp cận: "Calo AI"
- Spinner tải được công bố: "Đang tải, vui lòng chờ"

---

### WF-002: Màn Hình Camera

**Kiến Trúc**: Hành Động | **Ưu Tiên**: Cao | **FR Liên Quan**: FR-001, FR-002, FR-009 | **UC Liên Quan**: UC-001, UC-002, UC-009

**Mục Đích**: Giao diện chụp ảnh; điểm vào vòng lặp cốt lõi

**Bố Cục**:
- Vùng A (Anh Hùng): Toàn màn hình xem trước camera trực tiếp (bỏ qua vùng an toàn cho xem trước)
- Vùng B (Engagement): Nút chụp tròn lớn (dưới giữa, đường kính 70pt)
- Vùng C (Khám Phá): Huy hiệu số scan (trên cùng bên phải: "2/3 scans" hoặc "Không giới hạn"), thẻ Mẹo (có thể thu gọn)
- Vùng D (Tiện Ích): Biểu tượng thư viện ảnh (trên cùng bên trái), Biểu tượng Cài đặt (trên cùng bên phải), nút back (nếu modal)

**Thành Phần**:
- AVCaptureView (bao bọc SwiftUI) hoặc UIViewControllerRepresentable
- Nút chụp tròn lớn (tròn, màu chính)
- Biểu tượng thư viện ảnh (SF Symbol: "photo.on.rectangle")
- Huy hiệu số scan (tròn, có số)
- Biểu tượng Cài đặt (SF Symbol: "gear")
- Văn bản Mẹo (tùy chọn, bên dưới xem trước): "Góc từ trên xuống cho kết quả tốt nhất"

**Tương Tác**:
- Nhấn nút chụp → Chụp ảnh (FR-002) → Hiển thị xem trước với "Dùng ảnh này" / "Chụp lại"
- Nhấn thư viện ảnh → PHPickerViewController → Chọn ảnh → Hiển thị xem trước
- Nhấn Cài đặt → Mở Xem Cài đặt (WF-007)
- Huy hiệu số scan → Nhấn để hiển thị mẹo "Không giới hạn với Premium"

**Trạng Thái**:
- Ban đầu: Xem trước trực tiếp, nút chụp sẵn sàng, không gợi ý (người dùng quay lại)
- Lần đầu: Văn bản gợi ý hiển thị ở trên nút chụp
- Giới hạn gần (2/3): Huy hiệu số scan được tô sáng vàng
- Vượt giới hạn (3/3): Nút chụp bị vô hiệu hóa, lớp phủ "Nâng cấp"
- Quyền bị từ chối: Hiển thị trạng thái lỗi "Cần quyền camera"

**Hỗ Trợ Tiếp Cận**:
- Nút chụp: "Chụp ảnh" (voiceover)
- Thư viện ảnh: "Chọn từ thư viện"
- Huy hiệu số scan: "2 trong 3 lượt scan đã dùng hôm nay"

---

### WF-003: Màn Hình Xác Nhận (Chỉnh Sửa Nguyên Liệu)

**Kiến Trúc**: Hành Động | **Ưu Tiên**: Cao | **FR Liên Quan**: FR-003-008 | **UC Liên Quan**: UC-003-008

**Mục Đích**: Xác minh và chỉnh sửa nguyên liệu được phát hiện bởi AI trước khi lưu

**Bố Cục**:
- Vùng A (Anh Hùng): Hình ảnh bữa ăn (xem trước nhỏ, 100x100pt, trên cùng bên trái) + Tên bữa ăn + Tổng calo (lớn, 32pt)
- Vùng B (Engagement): Danh sách nguyên liệu (có thể cuộn, mỗi mục: checkbox + tên + bộ chọn khẩu phần + calo)
- Vùng C (Khám Phá): Phân tích Macro (thanh nội tuyến: Protein X% | Carbs Y% | Fat Z%)
- Vùng D (Tiện Ích): Nút "+ Thêm nguyên liệu", Nút "Xác Nhận & Lưu" (dưới, toàn chiều rộng), liên kết "Chụp lại"

**Thành Phần**:
- Xem ảnh (xem trước bữa ăn)
- Nhãn (tên bữa ăn, SF Pro 24pt)
- Hiển thị số lớn (tổng calo, SF Pro 32pt, đậm)
- Danh sách nguyên liệu (ô tuỳ chỉnh):
  - Checkbox (chuyển đổi)
  - Tên nguyên liệu (nhãn)
  - Bộ chọn khẩu phần (nút: Nhỏ / Vừa / Lớn)
  - Hiển thị Calo/gram (văn bản phụ)
- Thanh Macro (3 phân đoạn, mã hóa màu)
- Trường nhập văn bản (ẩn theo mặc định, "+ Thêm" mở rộng)
- Nút "Xác Nhận & Lưu" (chính, toàn chiều rộng, chiều cao 48pt)

**Tương Tác**:
- Nhấn checkbox → Chuyển đổi nguyên liệu, tính lại macro (thời gian thực, <200ms)
- Nhấn nút khẩu phần → Thay đổi bội số (0.75x / 1.0x / 1.25x), tính lại (FR-006)
- Nhấn tên nguyên liệu → Modal chỉnh sửa mở (không phải trên màn hình xác nhận, xảy ra tại WF-013)
- Nhấn "+ Thêm nguyên liệu" → Trường nhập mở rộng, các gợi ý tự hoàn thành xuất hiện
- Cuộn danh sách → Cuộn mượt, không nảy
- Nhấn "Xác Nhận & Lưu" → Xác thực (≥1 nguyên liệu, tổng > 0) → Lưu log → Điều hướng đến WF-004
- Nhấn "Chụp lại" → Quay lại WF-002 (loại bỏ hiện tại)

**Trạng Thái**:
- Độ tin cậy cao (>80%): Không có cảnh báo
- Độ tin cậy thấp (<70%): Thanh cảnh báo vàng "Không chắc chắn. Vui lòng xác minh bên dưới."
- Tất cả nguyên liệu không được chọn: Nút Lưu bị vô hiệu hóa, gợi ý "Chọn ít nhất một nguyên liệu"
- Tổng trống: Nút Lưu bị vô hiệu hóa, gợi ý "Tổng phải > 0"

**Hỗ Trợ Tiếp Cận**:
- Checkbox: "Mì ống, được chọn, 200 calo"
- Nút khẩu phần: "Kích cỡ khẩu phần: Vừa, hiện được chọn"
- Thanh Macro: "Protein 25%, Carbs 45%, Fat 30%"
- Nút Lưu: "Xác nhận và lưu log bữa ăn"

---

### WF-004: Màn Hình Nhật Ký (Log Hàng Ngày)

**Kiến Trúc**: Tiêu Thụ | **Ưu Tiên**: Cao | **FR Liên Quan**: FR-012-017 | **UC Liên Quan**: UC-011-015

**Mục Đích**: Xem log bữa ăn hàng ngày và tiến trình so với mục tiêu

**Bố Cục**:
- Vùng A (Anh Hùng): Thanh tiến độ (trên cùng, toàn chiều rộng) với nhãn "1800 / 2000 cal", mã hóa màu
- Vùng B (Engagement): Danh sách bữa ăn (có thể cuộn) — mỗi mục: Tên bữa ăn + calo + giờ + vuốt để chỉnh sửa/xoá
- Vùng C (Khám Phá): Chuyển đổi "Xem tuần" (dưới cùng, chuyển sang WF-005), Thẻ "Bảng Điều Khiển" (có thể mở rộng)
- Vùng D (Tiện Ích): Bộ chọn ngày (trên cùng), chuyển đổi xem ngày/tuần (nút), chia sẻ tiến độ (biểu tượng)

**Thành Phần**:
- Thanh tiến độ (phân đoạn, màu: xanh ≤100%, vàng 100-110%, đỏ >110%)
- Nhãn tiến độ (ví dụ: "1800 / 2000")
- Danh sách các mục bữa ăn (ô tuỳ chỉnh):
  - Tên bữa ăn (nhãn, 16pt)
  - Calo (phụ, 14pt)
  - Giờ (tuỳ chọn, văn bản xám)
  - Hành động vuốt (Nút Chỉnh sửa / Xoá, ẩn cho đến khi vuốt)
- Nút chuyển đổi "Xem tuần"
- Thẻ Bảng Điều Khiển (xem trước mini, thống kê hàng tuần)
- Nút Chia sẻ (biểu tượng, trên cùng bên phải)
- Bộ chọn ngày (tuỳ chọn, nếu người dùng nhấn ngày)

**Tương Tác**:
- Vuốt trái trên bữa ăn → Nút Chỉnh sửa & Xoá xuất hiện (FR-015, FR-017)
- Nhấn Chỉnh sửa → Mở WF-013 (Modal chỉnh sửa)
- Nhấn Xoá → Hiển thị WF-014 (Xác nhận xoá)
- Nhấn "Xem tuần" → Chuyển sang WF-005 (hoặc chuyển đổi nội tuyến trên cùng một màn hình)
- Nhấn biểu tượng chia sẻ → Chia sẻ tiến độ (tờ rơi OS)
- Kéo để làm mới → Làm mới danh sách bữa ăn từ Supabase
- Nhấn tiêu đề ngày → Mở bộ chọn ngày để xem các ngày khác

**Trạng Thái**:
- Trống (không có bữa ăn): Trạng thái trống "Chưa ghi log bữa ăn nào. Nhấn Camera để thêm." với CTA Camera
- Có bữa ăn: Danh sách đầy đủ, thanh tiến độ nổi bật
- Gần mục tiêu (90-110%): Thanh tiến độ vàng, tin nhắn tùy chọn
- Vượt mục tiêu (>110%): Thanh tiến độ đỏ, tin nhắn "Bạn đã vượt quá mục tiêu của mình"
- Ngoại tuyến: Biểu ngữ "Lần đồng bộ cuối cùng 5 phút trước"

**Hỗ Trợ Tiếp Cận**:
- Thanh tiến độ: "Tiến độ: 1800 trên 2000 calo, 90 phần trăm"
- Mục bữa ăn: "Mì ống, 600 calo, 12:30 PM"
- Vuốt: "Vuốt trái để chỉnh sửa hoặc xoá"
- Chuyển đổi tuần: "Chuyển sang xem tuần"

---

### WF-005: Màn Hình Bảng Điều Khiển (Insight Hàng Tuần)

**Kiến Trúc**: Tiêu Thụ | **Ưu Tiên**: Trung bình | **FR Liên Quan**: FR-014 | **UC Liên Quan**: UC-013

**Mục Đích**: Xem tóm tắt hàng tuần và xu hướng

**Bố Cục**:
- Vùng A (Anh Hùng): Thẻ tóm tắt hàng tuần — "Tổng hàng tuần: 12.950 cal" + "Trung bình: 1.850/ngày"
- Vùng B (Engagement): Biểu đồ cột (7 cột, Thứ Hai-Chủ Nhật, chiều cao = tổng hàng ngày, mã hóa màu theo trạng thái mục tiêu)
- Vùng C (Khám Phá): Biểu đồ tròn phân tích Macro (Protein 25%, Carbs 45%, Fat 30%) + văn bản insight ("Tuyệt vời, 2% dưới mục tiêu tuần này")
- Vùng D (Tiện Ích): Nút Xuất / Chia sẻ (dưới cùng), quay lại Hàng ngày (nút chuyển đổi)

**Thành Phần**:
- Thẻ tóm tắt (văn bản lớn, 2 số liệu chính)
- Biểu đồ cột (7 cột, nhập vào hoạt ảnh)
- Biểu đồ tròn (3 phân đoạn, mã hóa màu)
- Văn bản insight (1-2 câu về hiệu suất)
- Nút Xuất (biểu tượng, dưới cùng bên trái)
- Nút Chia sẻ (biểu tượng, dưới cùng bên phải)

**Tương Tác**:
- Nhấn cột trong biểu đồ → Hiển thị bữa ăn hàng ngày cho ngày đó (mở rộng)
- Nhấn "Xem hàng ngày" → Quay lại WF-004
- Nhấn Xuất → Tải CSV hoặc PDF
- Nhấn Chia sẻ → Tờ rơi OS

**Trạng Thái**:
- Tuần đầu tiên (không có dữ liệu): Trạng thái trống "Ghi log bữa ăn để xem xu hướng hàng tuần"
- Đúng tiến độ: Chỉ báo xanh, tin nhắn khuyến khích
- Vượt trung bình: Chỉ báo màu cam, tin nhắn cảnh báo

**Hỗ Trợ Tiếp Cận**:
- Biểu đồ: "Biểu đồ hàng tuần, Thứ Hai 1800 calo, Thứ Ba 1950..."
- Nút Xuất: "Xuất tuần dưới dạng CSV"

---

### WF-006: Màn Hình Paywall (Đề Nghị Subscription)

**Kiến Trúc**: Hành Động | **Ưu Tiên**: Cao | **FR Liên Quan**: FR-021, FR-022, FR-023 | **UC Liên Quan**: UC-019, UC-020

**Mục Đích**: Trình bày bản dùng thử Premium và các tùy chọn giá

**Bố Cục**:
- Vùng A (Anh Hùng): Tiêu đề "Mở khóa Scan Không Giới Hạn" + huy hiệu "Miễn phí 7 ngày"
- Vùng B (Engagement): Tùy chọn giá (2 thẻ: Hàng tháng $9.99/tháng | Hàng năm $39.99/năm với "TIẾT KIỆM 30%")
- Vùng C (Khám Phá): Danh sách lợi ích (✓ Scan không giới hạn, ✓ AI Coach sắp có, ✓ Theo dõi GLP-1 sắp có)
- Vùng D (Tiện Ích): Nút "Bắt đầu dùng thử 7 ngày" (chính, toàn chiều rộng), liên kết "Nhắc tôi sau"

**Thành Phần**:
- Tiêu đề (SF Pro, 32pt, đậm)
- Huy hiệu "Miễn phí 7 ngày" (tròn, nền xanh)
- Thẻ giá 1: Nhãn "$9.99/tháng" + biểu tượng
- Thẻ giá 2: Nhãn "$39.99/năm" + huy hiệu "TIẾT KIỆM 30%"
- Danh sách lợi ích (các dấu đầu dòng, dấu kiểm SF Symbol)
- Nút CTA (màu chính, "Bắt đầu dùng thử 7 ngày")
- Liên kết phụ ("Nhắc tôi sau", văn bản xám)

**Tương Tác**:
- Nhấn thẻ giá → Chọn gói (đường viền tô sáng)
- Nhấn "Bắt đầu dùng thử 7 ngày" → Mở bảng thanh toán StoreKit → Hoàn tất mua (FR-022)
- Nhấn "Nhắc tôi sau" → Đóng modal, quay lại Camera/Diary
- Nhấn back → Đóng modal

**Trạng Thái**:
- Ban đầu: Hàng tháng được chọn theo mặc định
- Người dùng đã dùng thử: Nút "Kích hoạt lại Premium" thay vào đó
- Đã là Premium: Nút "Quản lý subscription"

**Hỗ Trợ Tiếp Cận**:
- Tiêu đề: "Mở khóa scan không giới hạn"
- Thẻ: "Gói hàng tháng, 9 đô la 99 xu mỗi tháng, hiện được chọn"
- Nút: "Bắt đầu dùng thử miễn phí 7 ngày"

---

### WF-007: Màn Hình Cài Đặt (Tài Khoản)

**Kiến Trúc**: Quản Lý | **Ưu Tiên**: Trung bình | **FR Liên Quan**: FR-024, FR-025, FR-026 | **UC Liên Quan**: UC-021, UC-022, UC-023

**Mục Đích**: Xem tài khoản, subscription, và cài đặt

**Bố Cục**:
- Vùng A (Anh Hùng): Tên người dùng / Avatar (trên cùng, phần hồ sơ)
- Vùng B (Engagement): Phần trạng thái đăng ký — "Subscription của bạn: Premium, gia hạn 25 Tháng Một" với các nút (Quản lý / Huỷ / Khôi phục)
- Vùng C (Khám Phá): Các phần Cài đặt — Hồ sơ, Thông báo, Quyền riêng tư, Về, Trợ giúp
- Vùng D (Tiện Ích): Nút "Đăng xuất" (dưới cùng, đỏ/tước quyền)

**Thành Phần**:
- Phần hồ sơ (avatar + tên + email)
- Thẻ subscription (trạng thái + ngày gia hạn + các nút hành động)
- Danh sách Cài đặt (các ô xem bảng):
  - Hồ sơ → Chỉnh sửa tên, email, mục tiêu
  - Thông báo → Bật/tắt
  - Quyền riêng tư → Liên kết chính sách dữ liệu
  - Về → Phiên bản, pháp lý
  - Trợ giúp → Câu hỏi thường gặp, liên hệ
- Nút Đăng xuất (kiểu tước quyền, đỏ)

**Tương Tác**:
- Nhấn avatar → Modal chỉnh sửa hồ sơ (thay đổi tên, mục tiêu)
- Nhấn "Quản lý subscription" → Mở trang subscriptions App Store (liên kết sâu)
- Nhấn "Huỷ" → Hiển thị WF-018 (xác nhận) → Xử lý hủy (FR-024)
- Nhấn "Khôi phục purchase" → Gọi khôi phục StoreKit (FR-026)
- Tap settings cells → Navigate to sub-screens
- Tap "Log out" → Confirmation → Clear auth → Return to WF-001

**States**:
- Premium: Show renewal date, Manage/Cancel/Restore options
- Free tier: Show "Upgrade to Premium" button
- No subscription: Show "Restore purchases" option

**Accessibility**:
- Subscription: "Premium subscription, renews January 25"
- Manage button: "Manage your premium subscription"

---

### WF-008: Onboarding (Biểu Mẫu Nhiều Bước)

**Kiến Trúc**: Hành Động | **Ưu Tiên**: Cao | **FR Liên Quan**: FR-018, FR-019, FR-020 | **UC Liên Quan**: UC-016, UC-017, UC-018

**Mục Đích**: Thu thập dữ liệu hồ sơ người dùng (chiều cao, cân nặng, mục tiêu, hoạt động) để tính mục tiêu calo

**Bố Cục** (biểu mẫu 3 bước):

**Bước 1: Chiều Cao & Cân Nặng**
- Vùng A: Tiêu đề "Hồ Sơ Của Bạn"
- Vùng B: Nhập chiều cao (số + bộ chọn đơn vị cm/in) + Nhập cân nặng + Bộ chọn mục tiêu (nút: Giảm / Duy trì / Tăng)
- Vùng D: Nút "Tiếp Theo"

**Bước 2: Mức Hoạt Động**
- Vùng A: Tiêu đề "Bạn hoạt động bao nhiêu?"
- Vùng B: 4 nút radio (Ít hoạt động / Nhẹ / Trung bình / Rất tích cực) kèm mô tả
- Vùng D: Nút "Tiếp Theo"

**Bước 3: Xác Nhận Mục Tiêu**
- Vùng A: Tiêu đề "Mục tiêu hàng ngày của bạn"
- Vùng B: Hiển thị calo lớn (ví dụ: "2000 kcal") + giải thích công thức
- Vùng D: Nút "Sẵn sàng bắt đầu"

**Thành Phần** (tất cả bước):
- Trường nhập văn bản (SF Pro, 16pt, có viền)
- Bộ chọn đơn vị (điều khiển phân đoạn: cm / in, kg / lb)
- Nút radio (tròn, chọn đơn)
- Nút (Tiếp Theo, Back, Sẵn sàng)
- Chỉ báo tiến độ (Bước 1/3, 2/3, 3/3)

**Tương Tác**:
- Bước 1: Nhập chiều cao/cân nặng, chọn mục tiêu, nhấn Tiếp Theo → Xác thực (chiều cao 120-220, cân nặng 30-300) → Tiến tới Bước 2
- Bước 2: Chọn mức hoạt động, nhấn Tiếp Theo → Tiến tới Bước 3
- Bước 3: Xem lại mục tiêu được tính, nhấn "Sẵn sàng bắt đầu" → Lưu hồ sơ → Loại bỏ onboarding → Điều hướng đến WF-002 (Camera)
- Nút Back trên bất kỳ bước nào → Quay lại bước trước
- Nút Skip (tùy chọn, trên Bước 1) → Bỏ qua ứng dụng chính với mục tiêu mặc định

**Trạng Thái**:
- Biểu mẫu không hợp lệ: Nút Tiếp Theo bị vô hiệu hóa, tin nhắn lỗi
- Biểu mẫu hợp lệ: Nút Tiếp Theo được bật
- Tính toán mục tiêu: Hiển thị spinner trên Bước 3

**Hỗ Trợ Tiếp Cận**:
- Chiều cao: "Nhập chiều cao, 168 cm"
- Hoạt động: "Ít hoạt động, ít hoặc không tập luyện"
- Mục tiêu: "Mục tiêu hàng ngày của bạn là 2000 calo, được tính bằng công thức Mifflin-St Jeor"

---

### WF-009: Modal Yêu Cầu Quyền

**Kiến Trúc**: Hành Động | **Ưu Tiên**: Cao | **FR Liên Quan**: FR-001 | **UC Liên Quan**: UC-001

**Mục Đích**: Yêu cầu quyền camera từ hệ thống iOS (modal/dialog gốc)

**Bố Cục**:
- Vùng A (Anh Hùng): Tiêu đề "Calo AI muốn truy cập Camera của bạn"
- Vùng B (Engagement): Mô tả "Để chụp ảnh bữa ăn, ứng dụng cần quyền truy cập camera."
- Vùng D (Tiện Ích): 2 nút: "Cho Phép" (xanh), "Không Cho Phép" (xám)

**Thành Phần**:
- Tiêu đề (SF Pro 16pt, semibold)
- Mô tả (SF Pro 14pt, regular)
- Nút Cho Phép (Primary, #007AFF)
- Nút Không Cho Phép (Secondary, xám)

**Tương Tác**:
- Nhấn "Cho Phép" → Camera permission granted, camera screen appears
- Nhấn "Không Cho Phép" → Permission denied, show error state on WF-002

**Trạng Thái**:
- System dialog (iOS native UIAlertController hoặc permission alert)
- Không thể dismiss bằng tap backdrop (yêu cầu hành động rõ ràng)

**Hỗ Trợ Tiếp Cận**:
- Tiêu đề: "Calo AI muốn truy cập Camera"
- Nút Cho Phép: "Grant camera access"

---

### WF-010: Modal Trạng Thái Tải AI

**Kiến Trúc**: Tiêu Thụ | **Ưu Tiên**: Cao | **FR Liên Quan**: FR-003 | **UC Liên Quan**: UC-003

**Mục Đích**: Hiển thị trạng thái xử lý khi AI phân tích ảnh (overlay loading)

**Bố Cục**:
- Vùng A (Anh Hùng): Spinner hoạt ảnh (tròn, 60x60pt)
- Vùng B (Engagement): Văn bản "Đang phân tích bữa ăn..." (SF Pro 16pt)
- Vùng D (Tiện Ích): Nút "Huỷ" (optional, nếu user muốn dừng)

**Thành Phần**:
- ProgressView (circular, animated)
- Text "Đang phân tích..." (SF Pro 16pt)
- Cancel button (nếu có timeout >5s)

**Tương Tác**:
- Display: Khi ảnh được gửi tới AI API
- Auto-dismiss: Khi kết quả nhận được (max 15 giây timeout)
- Nhấn Huỷ → Quay lại WF-002, discard current photo

**Trạng Thái**:
- Processing (0-100% progress, hoặc indeterminate)
- Timeout (>15s) → Show error "Phân tích quá lâu, thử lại"

**Hỗ Trợ Tiếp Cận**:
- Spinner: "Loading, analyzing meal, please wait"
- Text: "Processing image"

---

### WF-011: Modal Kết Quả Lỗi / Thử Lại

**Kiến Trúc**: Hành Động | **Ưu Tiên**: Cao | **FR Liên Quan**: FR-003 | **UC Liên Quan**: UC-003 AF

**Mục Đích**: Hiển thị khi AI không nhận diện được thức ăn hoặc lỗi xảy ra

**Bố Cục**:
- Vùng A (Anh Hùng): Biểu tượng lỗi (SF Symbol "exclamationmark.circle", đỏ)
- Vùng B (Engagement): Tiêu đề "Không thể nhận diện" + Mô tả "Ảnh quá mờ hoặc không phải thực phẩm. Thử lại với góc khác?"
- Vùng D (Tiện Ích): 2 nút: "Thử Lại" (Primary), "Quay Lại" (Secondary)

**Thành Phần**:
- Error icon (SF Symbol, 60x60pt, #FF3B30)
- Tiêu đề (SF Pro 18pt, semibold)
- Mô tả (SF Pro 14pt, regular)
- Nút Thử Lại (Primary)
- Nút Quay Lại (Secondary)

**Tương Tác**:
- Nhấn Thử Lại → Quay lại WF-002 (camera), không mất lượt scan
- Nhấn Quay Lại → Quay lại Diary hoặc Camera

**Trạng Thái**:
- Error: Confidence < 30%, no ingredients detected
- Timeout: AI API call exceeded timeout

**Hỗ Trợ Tiếp Cận**:
- Icon: "Error"
- Title: "Could not recognize meal"
- Buttons: "Retry" or "Go Back"

---

### WF-012: Modal Thành Phần Không Tìm Thấy (Gợi Ý Nhập Thủ Công)

**Kiến Trúc**: Hành Động | **Ưu Tiên**: Trung bình | **FR Liên Quan**: FR-005 | **UC Liên Quan**: UC-005

**Mục Đích**: Hiển thị khi người dùng muốn thêm nguyên liệu không có trong danh sách đề xuất

**Bố Cục**:
- Vùng A (Anh Hùng): Biểu tượng tìm kiếm (SF Symbol "magnifyingglass", xám)
- Vùng B (Engagement): Văn bản "Thành phần không tìm thấy" + Gợi ý "Nhập tên thành phần hoặc chọn từ danh sách gợi ý"
- Zone B2: Danh sách gợi ý (autocomplete hoặc danh sách nước dùng)
- Vùng D (Tiện Ích): Trường nhập + Nút "Thêm" (Primary)

**Thành Phần**:
- Search icon (SF Symbol, 48x48pt, xám)
- Text "Thành phần không tìm thấy"
- Text input field (SF Pro 16pt)
- List of suggestions (hoặc empty state)
- Button "Add" (Primary)

**Tương Tác**:
- User types ingredient name
- Suggestions appear (filtered from common ingredients list)
- Nhấn suggestion → Pre-fill input + tap Add
- Nhấn Add → Add new ingredient to list, recalculate macros

**Trạng Thái**:
- Empty input: Add button disabled
- Has input: Add button enabled
- Loading suggestions: Show spinner

**Hỗ Trợ Tiếp Cận**:
- Icon: "Search"
- Input: "Enter ingredient name"
- Suggestions list: "Autocomplete suggestions"

---

### WF-013: Modal Chỉnh Sửa Bản Ghi (Edit Meal)

**Kiến Trúc**: Hành Động | **Ưu Tiên**: Trung bình | **FR Liên Quan**: FR-015, FR-016 | **UC Liên Quan**: UC-014

**Mục Đích**: Modal cho phép chỉnh sửa bữa ăn đã lưu (được gọi từ Diary screen vuốt Edit)

**Bố Cục**:
- Vùng A (Anh Hùng): Tiêu đề "Chỉnh Sửa Bữa Ăn"
- Vùng B (Engagement): Form (tương tự WF-003 Confirmation): danh sách nguyên liệu, checkbox, bộ chọn khẩu phần, macro bar
- Vùng D (Tiện Ích): Nút "Lưu" (Primary), "Huỷ" (Secondary), "Xoá Bữa Ăn" (Destructive link)

**Thành Phần**:
- Header title (SF Pro 18pt, semibold)
- Close button (X, top-right)
- Ingredient list (như WF-003)
- Macro breakdown bar
- "Save" button (Primary, full-width)
- "Cancel" button (Secondary)
- "Delete" link (destructive, red, bottom)

**Tương Tác**:
- Chỉnh sửa nguyên liệu (add/remove/portion change)
- Nhấn Save → Validate → Update meal in Supabase → Close modal → Refresh WF-004 list
- Nhấn Cancel → Close modal, discard changes
- Nhấn Delete → Show WF-014 (Delete confirmation)

**Trạng Thái**:
- Loaded: Hiển thị dữ liệu hiện tại
- Edited: Save button highlighted
- Saving: Show spinner

**Hỗ Trợ Tiếp Cận**:
- Title: "Edit meal"
- Save button: "Save changes to meal"
- Delete link: "Delete this meal"

---

### WF-014: Modal Xác Nhận Xoá

**Kiến Trúc**: Hành Động | **Ưu Tiên**: Trung bình | **FR Liên Quan**: FR-017 | **UC Liên Quan**: UC-015

**Mục Đích**: Xác nhận trước khi xoá bữa ăn (destructive action)

**Bố Cục**:
- Vùng A (Anh Hùng): Biểu tượng cảnh báo (SF Symbol "exclamationmark.triangle", cam)
- Vùng B (Engagement): Tiêu đề "Xoá Bữa Ăn?" + Mô tả "Hành động này không thể hoàn tác."
- Vùng D (Tiện Ích): 2 nút: "Xoá" (Destructive, đỏ), "Huỷ" (Secondary)

**Thành Phần**:
- Warning icon (SF Symbol, 48x48pt, #FF9500)
- Tiêu đề (SF Pro 16pt, semibold)
- Mô tả (SF Pro 14pt, regular)
- "Delete" button (Destructive, red)
- "Cancel" button (Secondary, gray)

**Tương Tác**:
- Nhấn "Xoá" → Delete meal from DB → Close modal → Refresh WF-004 → Show toast "Bữa ăn đã bị xoá"
- Nhấn "Huỷ" → Close modal, keep meal

**Trạng Thái**:
- Confirmation: Waiting for user choice
- Deleting: Show spinner

**Hỗ Trợ Tiếp Cận**:
- Icon: "Warning"
- Title: "Delete meal?"
- Delete button: "Delete this meal permanently"

---

### WF-015: Modal Chia Sẻ Tiến Độ

**Kiến Trúc**: Hành Động | **Ưu Tiên**: Trung bình | **FR Liên Quan**: — | **UC Liên Quan**: —

**Mục Đích**: Chia sẻ tiến độ hàng ngày/tuần qua OS share sheet

**Bố Cục**:
- Vùng A (Anh Hùng): Tiêu đề "Chia Sẻ Tiến Độ"
- Vùng B (Engagement): Xem trước text chia sẻ (ví dụ: "Tôi đã ăn 1850 calo hôm nay! 📊")
- Vùng D (Tiện Ích): Nút "Chia Sẻ" (Primary), "Huỷ" (Secondary)

**Thành Phần**:
- Tiêu đề (SF Pro 18pt)
- Text preview (SF Pro 14pt, regular, tối đa 2 dòng)
- "Share" button (Primary)
- "Cancel" button (Secondary)

**Tương Tác**:
- Nhấn "Chia Sẻ" → Open UIActivityViewController → User chooses app (Messages, Twitter, etc.)
- Nhấn "Huỷ" → Close modal

**Trạng Thái**:
- Preview: Show formatted text
- Sharing: App selection sheet (iOS native)

**Hỗ Trợ Tiếp Cận**:
- Title: "Share progress"
- Share button: "Share to social media or messages"

---

### WF-016: Modal Chỉnh Sửa Hồ Sơ

**Kiến Trúc**: Hành Động | **Ưu Tiên**: Trung bình | **FR Liên Quan**: — | **UC Liên Quan**: —

**Mục Đích**: Chỉnh sửa thông tin hồ sơ (từ WF-007 Settings, nhấn avatar)

**Bố Cục**:
- Vùng A (Anh Hùng): Avatar + Tên người dùng
- Vùng B (Engagement): Form (3 trường): Tên, Email (read-only), Mục tiêu calo (editable)
- Vùng D (Tiện Ích): Nút "Lưu" (Primary), "Huỷ" (Secondary)

**Thành Phần**:
- Avatar (tròn, 80x80pt)
- Text input: Name (SF Pro 16pt)
- Text display: Email (SF Pro 14pt, gray, read-only)
- Number input: Goal calories (SF Pro 16pt)
- "Save" button (Primary, full-width)
- "Cancel" button (Secondary)

**Tương Tác**:
- Edit name, goal
- Nhấn Save → Validate → Update Supabase → Close modal → Refresh WF-007
- Nhấn Cancel → Close modal

**Trạng Thái**:
- Loaded: Hiển thị dữ liệu hiện tại
- Edited: Save button enabled
- Saving: Show spinner

**Hỗ Trợ Tiếp Cận**:
- Avatar: "Profile picture"
- Name field: "Edit name"
- Goal field: "Edit daily calorie goal"

---

### WF-017: Modal Thay Đổi Mục Tiêu

**Kiến Trúc**: Hành Động | **Ưu Tiên**: Trung bình | **FR Liên Quan**: — | **UC Liên Quan**: —

**Mục Đích**: Thay đổi mục tiêu calo hàng ngày (từ WF-007 hoặc WF-005 Dashboard)

**Bố Cục**:
- Vùng A (Anh Hùng): Tiêu đề "Thay Đổi Mục Tiêu"
- Vùng B (Engagement): Current goal display + Input mục tiêu mới (number field) + Công thức tính (Mifflin-St Jeor)
- Vùng D (Tiện Ích): Nút "Cập Nhật" (Primary), "Huỷ" (Secondary)

**Thành Phần**:
- Tiêu đề (SF Pro 18pt)
- Current goal display (SF Pro 16pt)
- Number input: New goal (SF Pro 16pt, placeholder "e.g., 2000")
- Formula note (SF Pro 12pt, gray)
- "Update" button (Primary)
- "Cancel" button (Secondary)

**Tương Tác**:
- Input new goal value
- Nhấn Update → Validate (>0, <10000) → Save to DB → Close modal → Refresh UI
- Nhấn Cancel → Close modal

**Trạng Thái**:
- Input empty: Update button disabled
- Input valid: Update button enabled

**Hỗ Trợ Tiếp Cận**:
- Input: "Enter new daily calorie goal"
- Update button: "Update goal"

---

### WF-018: Modal Huỷ Đăng Ký

**Kiến Trúc**: Hành Động | **Ưu Tiên**: Trung bình | **FR Liên Quan**: FR-024 | **UC Liên Quan**: UC-021

**Mục Đích**: Xác nhận huỷ subscription (từ WF-007 Settings, nhấn Cancel)

**Bố Cục**:
- Vùng A (Anh Hùng): Biểu tượng cảnh báo (SF Symbol "exclamationmark.circle", cam)
- Vùng B (Engagement): Tiêu đề "Huỷ Subscription?" + Mô tả "Bạn sẽ mất quyền truy cập Scan Không Giới Hạn. Khoá được giữ cho đến hết chu kỳ hiện tại (Jan 25)."
- Vùng D (Tiện Ích): 2 nút: "Tiếp Tục Huỷ" (Destructive), "Giữ Subscription" (Primary)

**Thành Phần**:
- Warning icon (SF Symbol, 48x48pt, #FF9500)
- Tiêu đề (SF Pro 16pt, semibold)
- Mô tả (SF Pro 14pt, regular)
- Renewal date info (SF Pro 12pt, gray)
- "Continue Cancellation" button (Destructive, red)
- "Keep Subscription" button (Primary, blue)

**Tương Tác**:
- Nhấn "Tiếp Tục Huỷ" → Call StoreKit API to cancel → Close modal → Show toast "Subscription đã bị huỷ"
- Nhấn "Giữ Subscription" → Close modal

**Trạng Thái**:
- Confirmation: Waiting for user choice
- Cancelling: Show spinner

**Hỗ Trợ Tiếp Cận**:
- Icon: "Warning"
- Title: "Cancel subscription?"
- Destructive button: "Confirm cancellation"

---

## 4. Thành Phần Chung

### 4.1 Điều Hướng

- **Tab Bar**: 49pt chiều cao, 3-4 tab, icon (SF Symbol) + label, badge tùy chọn
- **Navigation Stack**: Nút Back iOS chuẩn, title ở giữa
- **Search Bar**: SF Pro 16pt, icon tìm kiếm, nút huỷ
- **Back Button**: SF Symbol "chevron.left", hoặc custom action

### 4.2 Thành Phần Giao Diện Cốt Lõi

- **Nút (Chính)**: SF Pro, 16pt, semibold, padding 12pt (dọc), nền #007AFF, văn bản trắng, chiều cao 48pt
- **Nút (Phụ)**: Kiểu viền, viền #007AFF, văn bản #007AFF, nền trong suốt
- **Nút (Tước Quyền)**: Nền #FF3B30, văn bản trắng
- **Nhập Văn Bản**: SF Pro, 16pt, viền dưới 1pt #E5E5EA, padding 12pt, dynamic type hỗ trợ
- **Điều Khiển Phân Đoạn**: 2-4 tùy chọn, tô sáng viền dưới, animation smooth
- **Checkbox**: 20x20pt, tô đầy #007AFF khi được chọn
- **Huy Hiệu**: Tròn, 24x24pt, số ở giữa, nền #FF3B30

### 4.3 Thành Phần Phản Hồi

- **Thanh Tiến Độ**: Chiều cao 4pt, tô đầy hoạt ảnh, mã hóa màu (xanh ≤100%, vàng 100-110%, đỏ >110%)
- **Thẻ**: Nền #FFFFFF, bóng tinh tế, padding 16pt, bán kính góc 8pt
- **Mục Danh Sách**: Toàn chiều rộng, padding 12pt (dọc), 16pt (ngang), viền dưới chia
- **Lớp Phủ Modal**: Đen bán trong suốt (alpha 0.4)
- **Toast/Alert**: Văn bản trắng, nền tối (#1C1C1C), corner radius 8pt, tự động loại bỏ sau 3 giây

---

## 5. Thiết Kế Responsive & Bố Cục

### 5.1 Hỗ Trợ Thiết Bị

- iPhone 12-13 Mini: 390pt (bố cục thường xuyên)
- iPhone 14 Pro: 393pt (bố cục thường xuyên)
- iPhone 14 Pro Max: 430pt (padding điều chỉnh nhẹ)
- iPad: KHÔNG HỖ TRỢ (chỉ iOS cho MVP)

### 5.2 Định Hướng

- Chỉ hỗ trợ Portrait (dọc)
- Landscape: Không bắt buộc cho MVP, xem xét Post-MVP

### 5.3 Bố Cục Thích Ứng

**Vùng An Toàn**:
- Trên: Thanh trạng thái + notch (nếu có)
- Dưới: Chỉ báo trang chủ (34pt trên hầu hết iPhone)
- Padding nội dung: 16pt trái/phải trên tất cả thiết bị

---

## 6. Hỗ Trợ Tiếp Cận (WCAG 2.1 AA)

### 6.1 VoiceOver

- Tất cả nút, nhập liệu có `.accessibilityLabel()` và `.accessibilityHint()`
- Thứ tự lọc: từ trái sang phải, từ trên xuống dưới
- Sử dụng `.accessibilityElement(children: .combine)` cho nhóm liên quan

### 6.2 Dynamic Type

- Hỗ trợ Text Size từ Small (~75%) đến Accessibility (>200%)
- SF Pro sizing: scaled, không fixed pt values
- Line height tự động điều chỉnh

### 6.3 Tương Phản Màu

- Text: ≥4.5:1 tương phản (WCAG AAA)
- UI components: ≥3:1 tương phản (WCAG AA)
- Không dùng màu duy nhất để truyền thông tin (mô tả cũng cần có)

### 6.4 Mục Tiêu Chạm

- Min 44x44pt cho interactive elements (iOS tiêu chuẩn)
- Padding tối thiểu 8pt giữa các mục
- Điều khiển slider: Tối thiểu 44pt chiều rộng

---

## 7. Chế Độ Tối & Chủ Đề

**Điều Chỉnh Màu**:
- Tất cả giá trị màu tự động điều chỉnh thông qua SwiftUI @Environment(.colorScheme)
- Nền: #FFFFFF (sáng) → #000000 (tối)
- Văn bản: #000000 (sáng) → #FFFFFF (tối)
- Thẻ: #FFFFFF (sáng) → #1C1C1C (tối)
- Chia: #E5E5EA (sáng) → #333333 (tối)

**Kiểm Tra**: Tất cả màn hình được xác minh trong cả chế độ Sáng và Tối

---

## 8. Design Assets

### 8.1 Biểu Tượng

- Dùng SF Symbol (hệ thống iOS, miễn phí tiếp cận)
- Các biểu tượng chính: camera, photo.on.rectangle, gear, trash, plus, checkmark, xmark
- Kích cỡ: 16pt (nhỏ), 24pt (trung bình), 32pt (lớn)
- Màu: Tuân theo hệ thống (màu chính, màu phụ, xám)

### 8.2 Hình Ảnh

- Ảnh bữa ăn: JPG/PNG, tối đa 10MB, tỷ lệ khung hình thay đổi
- Placeholder/skeleton: Gradient xám (bắt đầu từ #E5E5EA)
- Logo thương hiệu: SVG hoặc PDF tuy chọn (không yêu cầu raster)
- Avatar người dùng: Tròn, corner radius 9999pt, 48x48pt-64x64pt

### 8.3 Hoạt Ảnh

- Auto-dismiss splash: Fade-out 0.3s, delay 1.7s
- Spinner tải: Rotation 360°, duration 1s, loop vô hạn
- Transition sheet: Slide-up 0.3s, spring (damping 0.8)
- List swipe: Reveal buttons, duration 0.2s
- Progress bar fill: Linear, duration 0.5s, animation curve ease-in-out

### 8.4 Tập Tin SwiftUI Style

- Colors: Sử dụng `Asset.xcassets` cho các màu có tên (primaryColor, successColor, v.v.)
- Font: SF Pro scale dùng `Font.system()` không hardcode size
- Spacing: Token 8pt grid (4, 8, 16, 24, 32, 48pt)
- Corner radius: Token scale (4, 8, 12, 16pt hoặc .circle)
- Shadow: Predefined `.shadow()` modifiers với opacity-consistent

---

## 9. Tích Hợp Figma

**Figma File Status**: Chưa tạo (wireframes ở đây là authoritative, được sync vào Figma sau)

**Kế hoạch Tích Hợp**:
1. Export ASCII wireframes từ §3 vào Figma (via Code Connect hoặc manual component setup)
2. Tạo component library trong Figma với design system tokens từ §1.3
3. Map SwiftUI components từ ios-components skill vào Figma components
4. Setup Code Connect để sync Figma components ↔ SwiftUI source

**Framelink MCP** (nếu có sẵn):
- Sử dụng để trích design tokens từ Figma
- Fallback: Dùng token values từ §1.3 (hardcoded here)

---

## 10. Tham Chiếu

- **Functional_Requirements.md** (v1.0, 2026-07-21): Ánh xạ FR→Màn hình
- **Use_Cases.md** (v1.0, 2026-07-21): Ánh xạ UC→Màn hình, task flows
- **Project_Overview.md** (v1.0, 2026-07-21): Kiến trúc, nguyên tắc thiết kế
- **Apple Human Interface Guidelines**: https://developer.apple.com/design/human-interface-guidelines/

---

**Phiên bản**: 1.0  
**Cập nhật lần cuối**: 2026-07-21  
**Trạng thái**: ✅ Phase 1 & 2 Hoàn Thành — Tất Cả 17 MVP Screens (WF-001 đến WF-018)  

**Screen Count Breakdown**:
- Core Screens: 5 (WF-001 Splash, WF-008 Onboarding, WF-006 Paywall, WF-002 Camera, WF-004 Diary)
- Additional Consumption: 2 (WF-003 Confirmation, WF-005 Dashboard)
- Settings/Account: 1 (WF-007 Settings)
- Modals/Overlays Phase 1: 3 (WF-009 Permission, WF-010 Loading, WF-011 Error)
- Modals/Overlays Phase 2: 5 (WF-012 Add Ingredient, WF-013 Edit, WF-014 Delete, WF-015 Share, WF-016-017-018 Settings Modals)

**Hành động tiếp theo**: 
1. Chạy Quality Gate (gate-wireframes) 
2. Tiến tới Step 6: UX_Flows.md
