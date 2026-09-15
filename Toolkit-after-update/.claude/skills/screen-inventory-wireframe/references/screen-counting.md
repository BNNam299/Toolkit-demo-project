<!-- PROVENANCE — do build script sinh, KHÔNG sửa tay
nguồn      : ux-wireframe-builder.skill  →  references/screen-counting.md
nhập ngày  : 2026-08-09
trạng thái : chép nguyên văn, không tóm tắt, không diễn giải
cập nhật   : xuất lại file .skill từ Claude rồi chạy lại build script
-->

# Screen Counting & Estimation — Phương pháp đếm đủ trường hợp

## Công thức

**Tổng số màn hình = Happy Path + Decision States + Data States (+ Overlays × trọng số)**

Ký hiệu flow chuẩn: ▭ chữ nhật = màn hình tĩnh · ◇ thoi = quyết định/ngã rẽ logic của user hoặc hệ thống · → mũi tên = thao tác dẫn màn này sang màn khác.

## Lớp 1 — Happy Path

Đường ngắn nhất, mượt nhất, không lỗi. Đếm số chữ nhật. (Đăng nhập: Nhập thông tin → Bấm Đăng nhập → Trang chủ = **2 màn**: Đăng nhập, Trang chủ.)

## Lớp 2 — Decision States (mỗi hình thoi nhân bản màn hình)

Với TỪNG hình thoi, hỏi: "kết quả có thể xảy ra là những gì?" — liệt kê hết, không dừng ở 2 nhánh vẽ sẵn. Mẫu chuẩn (thoi "kiểm tra đăng nhập"):
- Nhánh 1: đúng → Trang chủ (đã đếm)
- Nhánh 2: sai → thông báo lỗi (biến thể trên màn Đăng nhập)
- Nhánh 3: tài khoản chưa kích hoạt → **+1 màn OTP xác thực**
- Nhánh 4: quên mật khẩu → **+luồng Lấy lại mật khẩu** (một luồng con — đếm đệ quy cả luồng đó)

Câu hỏi mồi để moi đủ nhánh từ user (hỏi theo từng thoi): *Ngoài thành công/thất bại, có trạng thái "đang chờ" không (pending, xử lý)? Có nhánh nào chuyển sang luồng khác không (quên MK, đăng ký mới)? Hệ thống từ chối vì lý do nghiệp vụ (hết hạn, bị khóa, vượt hạn mức)? Kết quả phụ thuộc loại user (free/premium, mới/cũ, đã KYC/chưa)?*

**Nhánh nào là màn riêng, nhánh nào là biến thể?** Xem bảng quy tắc ở dưới.

## Lớp 3 — Data States (mỗi màn cốt lõi × checklist trạng thái)

Quy tắc gốc: **mỗi màn hình cốt lõi cộng 1-2 màn trạng thái tối thiểu**. Quét checklist sau cho TỪNG màn cốt lõi — đây là danh sách "các trường hợp có thể xảy ra" để không sót:

| # | Trạng thái | Khi nào áp dụng | Thường là |
|---|---|---|---|
| 1 | **Empty** (trống) | Màn hiển thị dữ liệu user tạo/tích lũy (giỏ hàng, danh sách, lịch sử, feed) | Màn riêng (empty state có CTA dẫn hành động đầu) |
| 2 | **Loading** | Dữ liệu từ mạng/nặng | Biến thể (skeleton/spinner) — chỉ tách màn riêng nếu có onboarding-loading đặc thù |
| 3 | **Error kết nối** | Mọi màn phụ thuộc mạng | Màn/biến thể dùng CHUNG toàn app (đếm 1 lần) + biến thể riêng nếu màn có retry đặc thù |
| 4 | **Offline** | App có yêu cầu offline (đối chiếu PRD S9) | Biến thể theo màn: cái nào dùng được offline, cái nào chặn |
| 5 | **Partial/ít dữ liệu** | List 1 item vs nhiều vs chạm giới hạn | Thường annotation; tách biến thể nếu layout đổi |
| 6 | **First-run** | Lần đầu vào màn (coach mark, tooltip, tutorial) | Biến thể overlay |
| 7 | **Permission** | Cần notification/camera/location/photo | Mỗi permission: màn pre-prompt (giải thích trước khi xin) + biến thể bị từ chối |
| 8 | **Auth states** | Màn xem được cả khi chưa đăng nhập? | Biến thể logged-out (CTA đăng nhập) + phiên hết hạn |
| 9 | **Paywall/tier** | Free vs Premium thấy khác gì (đối chiếu PRD S10) | Màn paywall riêng + biến thể locked của màn tính năng premium |
| 10 | **Form validation** | Mọi form | Biến thể: lỗi từng field, disabled/enabled nút submit |
| 11 | **Payment outcomes** | Có thanh toán | Thành công / thất bại / pending / cancelled / restore purchases |
| 12 | **Destructive confirm** | Xóa, thoát không lưu, hủy đơn | Overlay confirm (cơ chế "cảnh báo" của usability framework) |
| 13 | **Notification entry** | Push/deep link dẫn thẳng vào màn giữa luồng | Kiểm tra màn đích đứng độc lập được không (thiếu context stack) |
| 14 | **Update/maintenance** | Force update, bảo trì server | 1-2 màn toàn app, đếm 1 lần |

Với app của team (mobile freemium): các mục 7, 9, 11 gần như luôn có — flag nếu user quên.

## Lớp phụ — Overlays

Modal, bottom sheet, dialog, action sheet, toast, snackbar: không phải màn đầy đủ nhưng vẫn thiết kế. Trọng số 0.25 (toast/confirm đơn giản) đến 0.5 (bottom sheet có form).

## Quy tắc màn riêng vs biến thể vs annotation

| Xử lý | Khi nào | Chi phí đếm |
|---|---|---|
| **Màn riêng** | Layout/cấu trúc khác hẳn màn gốc; user điều hướng ĐẾN nó (OTP, paywall, empty state có CTA) | 1× theo độ phức tạp |
| **Biến thể (state variant)** | Cùng layout, đổi nội dung vùng chính (loading skeleton, error inline, locked) | 0.3-0.5× màn gốc |
| **Annotation** | Thay đổi vi mô (toast, đổi nhãn nút, tooltip) | 0 màn — ghi chú trên wireframe gốc |

## Ví dụ chuẩn — "Mua hàng nhanh"

Flow: Chi tiết SP (bấm Mua ngay) → Nhập thông tin giao hàng & thanh toán → ◇ kiểm tra số dư/thẻ → Thành công / Thất bại.

- Happy Path: Chi tiết SP · Nhập thông tin & thanh toán · Xác nhận thành công = 3 màn
- Decision: thất bại → **màn 4**: lỗi thanh toán + gợi ý thử lại/đổi phương thức
- → **4 màn wireframe riêng biệt** bàn giao dev (từ luồng "tưởng 3 bước")
- Quét Data States tiếp: form validation trên màn 2 (biến thể), loading khi xử lý thanh toán (biến thể/overlay), pending nếu cổng thanh toán trả chậm (hỏi user — có thể +1), địa chỉ trống lần đầu mua (biến thể). Inventory thực tế: **4 màn + 3-4 biến thể + 1-2 overlay**.

## Template Screen Inventory

```markdown
| Mã | Màn hình | Loại (core/branch/state/overlay) | Gốc từ (bước flow / màn cha) | Độ phức tạp | Ghi chú |
|---|---|---|---|---|---|
| S01 | Chi tiết sản phẩm | core | Flow Mua §1 | T | |
| S01a | — loading skeleton | state | S01 | Đ | biến thể |
| S02 | Nhập giao hàng & TT | core | Flow Mua §2 | P | form nhiều field |
| ... |
**Tổng: X core · Y branch · Z state · W overlay → quy đổi N "màn chuẩn"**
```
Quy đổi màn chuẩn = core/branch 1× + state 0.4× + overlay 0.35× (điều chỉnh theo team).

## Estimation — mô hình tính giờ

### Giờ cơ sở theo độ phức tạp (cho MỘT màn chuẩn, lo-fi)

| Độ phức tạp | Định nghĩa | Lo-fi |
|---|---|---|
| **Đơn giản (Đ)** | ≤5 thành phần, layout chuẩn (splash, confirm, empty) | 0.5-1h |
| **Trung bình (T)** | List/detail thường, form ngắn, 6-12 thành phần | 1-2h |
| **Phức tạp (P)** | Dashboard, form dài đa bước, màn có logic điều kiện dày, data-viz | 2-4h |

### Hệ số nhân

- Fidelity: **Lo-fi 1× · Mid-fi 1.5-2× · Hi-fi 3-4×** (hi-fi thường nằm ở giai đoạn Figma, ngoài phạm vi skill nhưng đưa vào khi user cần báo giá trọn gói)
- Loại màn: state 0.3-0.5× · overlay 0.25-0.5× (đã quy đổi ở inventory thì bỏ qua)
- **Phí một lần**: dựng nền (grid, component điều hướng, ký hiệu chung) = 2-4h/dự án
- **Buffer review**: +20-30% cho 1-2 vòng sửa; mỗi vòng review thêm ngoài thỏa thuận +10%
- Người mới với domain/tool: ×1.2-1.5

### Công thức & cách trình bày

```
Giờ = Σ(màn chuẩn × giờ cơ sở theo độ phức tạp) × fidelity + phí nền
Estimate = Giờ × (1 + buffer)
```
Luôn trình 3 con số: **Lạc quan** (không buffer) / **Thực tế** (buffer 25%) / **Dự phòng** (buffer 40% — flow chưa chốt, stakeholder đông). Kèm khối "Giả định": fidelity, số vòng review, tool, những trạng thái đã loại khỏi phạm vi. Estimate không có giả định là estimate không phòng thủ được.

### Quy đổi lịch

Giờ thuần ÷ 5-6h thiết kế thực/ngày (không phải 8h) = số ngày công; cộng lệch lịch review với stakeholder khi ra timeline.
