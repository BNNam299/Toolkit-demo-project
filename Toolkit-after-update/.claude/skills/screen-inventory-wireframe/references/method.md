<!-- PROVENANCE — do build script sinh, KHÔNG sửa tay
nguồn      : ux-wireframe-builder.skill  →  SKILL.md
nhập ngày  : 2026-08-09
trạng thái : chép nguyên văn, không tóm tắt, không diễn giải
cập nhật   : xuất lại file .skill từ Claude rồi chạy lại build script
-->

---
name: ux-wireframe-builder
description: "Turn user flows into a complete screen inventory, a design-time estimate, and actual lo-fi/mid-fi wireframes. Use whenever the user wants to: đếm/tính số màn hình cần thiết kế từ user flow, estimate thời gian thiết kế wireframe, liệt kê các trường hợp/trạng thái màn hình (empty/loading/error/edge cases), vẽ wireframe, tạo mockup lo-fi, chuẩn bị bàn giao màn hình cho dev, hoặc báo giá dựa trên số màn hình. Also trigger for 'app này cần bao nhiêu màn hình', 'vẽ wireframe cho flow này', 'còn thiếu trạng thái nào chưa thiết kế'. Sits after ux-flow-architect (consumes its user flows and IA), before hi-fi design in Figma; wireframes it produces feed ux-usability-evaluator for early testing."
---

# Wireframe Builder — Đếm màn hình, Estimate, và Vẽ

Ba việc, đúng thứ tự: (1) từ user flow **liệt kê gần đúng nhất mọi trường hợp** để ra screen inventory đầy đủ, (2) từ inventory ra **estimate thời gian** có cơ sở, (3) vẽ wireframe đạt chuẩn. Công thức gốc của khung tham chiếu:

> **Tổng số màn hình = Màn hình luồng chính (Happy Path) + Màn hình rẽ nhánh (Decision States) + Màn hình trạng thái dữ liệu (Data States)**

Sai lầm đắt nhất khi báo giá là chỉ đếm hình chữ nhật trên luồng chính — mỗi hình thoi nhân bản màn hình theo số kết quả, và mỗi màn hình cốt lõi kéo theo 1-2 màn trạng thái. Ví dụ chuẩn: luồng "Mua hàng nhanh" tưởng 3 bước → thực tế 4 màn (Chi tiết SP → Nhập thông tin & thanh toán → ◇ kiểm tra → Thành công / Lỗi thanh toán), chưa tính trạng thái.

**Vị trí pipeline**: nhận user flows + IA từ `ux-flow-architect` (hoặc từ Figma/tài liệu user đưa); inventory + estimate đổ vào báo giá và sprint plan; wireframe xuất ra đưa vào `ux-usability-evaluator` (đúng thời điểm test "khi có wireframe hoặc lo-fi prototype") rồi mới sang Figma hi-fi.

## Workflow

### 1. Chuẩn hóa đầu vào

Yêu cầu user flow ở dạng đọc được (bước đánh số, sơ đồ, hoặc mô tả). Xác nhận ký hiệu: **chữ nhật = màn hình** · **thoi = quyết định/ngã rẽ (Đúng/Sai, Thành công/Thất bại)** · **mũi tên = thao tác dẫn màn này sang màn khác**. Nếu flow chưa có, chuyển sang `ux-flow-architect` làm flow trước — đếm màn hình từ flow mơ hồ là đếm sai.

### 2. Đếm màn hình — quét 3 lớp + 1 lớp phụ

Đọc `references/screen-counting.md` và chạy đúng trình tự:

1. **Lớp Happy Path**: đếm chữ nhật trên đường ngắn nhất không lỗi.
2. **Lớp Decision States**: với TỪNG hình thoi, liệt kê đủ mọi kết quả có thể (không chỉ 2 nhánh vẽ sẵn — đăng nhập có ít nhất 4: đúng / sai / chưa kích hoạt→OTP / quên mật khẩu). Mỗi kết quả cần UI riêng = +1 màn hoặc +1 biến thể.
3. **Lớp Data States**: với từng màn hình cốt lõi, quét checklist trạng thái trong reference (Empty / Loading / Error / Offline / Partial / First-run / Permission / Paywall...). Quy tắc gốc: mỗi màn cốt lõi cộng thêm **1-2 màn trạng thái** tối thiểu.
4. **Lớp phụ — thành phần chồng (overlay)**: modal, bottom sheet, dialog, toast — không phải màn hình đầy đủ nhưng vẫn phải thiết kế; đếm riêng với trọng số 0.25-0.5.

Với mỗi trạng thái, quyết định **màn riêng hay biến thể/annotation** theo bảng quy tắc trong reference — đây là chỗ inventory phình ảo hoặc thiếu thật nếu làm cẩu thả.

Output bắt buộc: **bảng Screen Inventory** (mã màn · tên · loại: core/branch/state/overlay · độ phức tạp Đ/T/P · nguồn gốc từ bước flow nào · ghi chú). Trình bày cho user duyệt TRƯỚC khi estimate — inventory là hợp đồng, estimate chỉ là phép nhân.

### 3. Estimate thời gian

Dùng mô hình trong `references/screen-counting.md` mục "Estimation": giờ cơ sở theo độ phức tạp (Đơn giản/Trung bình/Phức tạp) × hệ số fidelity (Lo-fi 1× · Mid 1.5-2× · Hi-fi 3-4×) × trọng số loại màn (state variant 0.3-0.5×, overlay 0.25-0.5×) + buffer review 20-30% + phí khởi động hệ thống (component nền, grid) tính một lần. Xuất bảng estimate kèm 3 con số: **lạc quan / thực tế / dự phòng**, và ghi rõ giả định (số vòng review, fidelity, tool). Không bao giờ đưa một con số duy nhất không kèm giả định.

### 4. Vẽ wireframe

Chỉ vẽ sau khi inventory được duyệt. Chuẩn chất lượng trong `references/wireframe-standards.md` — tóm tắt bất di bất dịch:

- **Quy tắc 3 Không** (lo-fi): không màu (trắng-đen-xám; xanh dương duy nhất cho link/CTA quan trọng) · không ảnh thật (chữ nhật gạch chéo ✕) · không font cầu kỳ (một font hệ thống, phân cấp bằng cỡ/độ đậm).
- **Phân cấp trực quan**: nhìn vào biết ngay cái gì quan trọng nhất — vị trí theo luồng mắt Z/F, CTA chính to rõ hơn nút phụ.
- **Đầy đủ cấu trúc & chức năng**: màn hình trả lời được "chứa gì và làm được gì"; vùng tương tác đặt hợp công thái học (vùng ngón cái trên mobile).
- **Annotations**: mỗi vùng tương tác có ghi chú logic ngắn ("nút này bấm mở pop-up chọn ngày").
- Quy ước nét từ giáo trình: Header **nét đậm**, body text **nét mảnh**, ảnh = **chữ nhật gạch chéo**; vẽ điều hướng trước (nav bar, search, chevron) rồi thành phần lớn rồi chi tiết (dropdown, button, checkbox, field, progress bar/dialog cho luồng nhiều khung, CTA).
- **Không Lorem Ipsum** — ghi text thật thể hiện ý tưởng (tên cửa hàng, tiêu đề, nhãn CTA thật). Thao tác vẽ ra phải hiện thực hóa được trên sản phẩm thật.

Cách render: mặc định tạo wireframe HTML/SVG xem ngay trong chat (mỗi màn một khung đúng kích thước thiết bị, mobile 390×844 trừ khi user chỉ định khác), trang chính vẽ đầy đủ tương tác vì nó là điểm xuất phát của các trang phụ. Nhiều màn thì render theo flow order, kèm nhãn mã màn khớp inventory. User cần file bàn giao → xuất HTML một trang chứa toàn bộ màn + bảng inventory + annotation.

### 5. Bàn giao & khép vòng

- Đối chiếu ngược: mỗi màn trong inventory xuất hiện trong ≥1 flow; mỗi bước flow có màn tương ứng; trạng thái nào quyết định "để sau" phải ghi rõ trong inventory (không được biến mất im lặng).
- Đề xuất chạy `ux-usability-evaluator` chế độ chuyên gia trên wireframe trước khi sang Figma.
- Số màn hình + estimate đổ vào PRD: Full mode có Section 10 "Danh sách Màn hình" (`# | Tên | Mô tả | Ưu tiên | Phụ thuộc`) — inventory của skill này chính là bản nở đầy đủ của bảng đó (thêm Decision/Data States); đồng bộ hai chiều và dùng làm cơ sở báo giá. Nhắc user cập nhật nếu đang có PRD mở.
