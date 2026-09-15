<!-- PROVENANCE — do build script sinh, KHÔNG sửa tay
nguồn      : ux-wireframe-builder.skill  →  references/wireframe-standards.md
nhập ngày  : 2026-08-09
trạng thái : chép nguyên văn, không tóm tắt, không diễn giải
cập nhật   : xuất lại file .skill từ Claude rồi chạy lại build script
-->

# Wireframe Standards — Chuẩn chất lượng & Quy ước vẽ

## 4 tiêu chí đánh giá một wireframe tốt (khung tham chiếu)

Wireframe tốt không phải bản vẽ đẹp — là bản vẽ **rõ ràng, có mục đích, dễ hiểu**.

### 1. Quy tắc 3 Không (lo-fi)
Giữ người xem tập trung vào bố cục và tính năng, không phân tâm bởi thẩm mỹ:
- **Không màu sắc**: trắng, đen, tông xám. Ngoại lệ duy nhất: **xanh dương** cho link/nút quan trọng.
- **Không hình ảnh thật**: ô ảnh = chữ nhật có gạch chéo (✕).
- **Không font cầu kỳ**: MỘT font hệ thống (Arial/Roboto/San Francisco), phân cấp bằng cỡ + độ đậm/nhạt.

### 2. Phân cấp trực quan
Nhìn vào biết ngay đâu là thông tin quan trọng nhất, không cần giải thích:
- **Vị trí**: theo luồng mắt tự nhiên trên-xuống, trái-sang-phải (mô hình chữ Z hoặc F).
- **Kích thước**: CTA chính to, rõ hơn nút phụ.

### 3. Đầy đủ cấu trúc dữ liệu & chức năng
Màn hình trả lời được: **"chứa những gì và làm được gì?"**
- Đủ các khối nội dung chính (thanh tìm kiếm, danh mục, bộ lọc, danh sách...).
- Vùng tương tác (nút, ô nhập) đặt hợp **công thái học** — vùng ngón tay cái dễ chạm trên điện thoại (nửa dưới màn hình cho hành động chính).

### 4. Annotations rõ ràng
Ghi chú ngắn bên cạnh giải thích logic: *"Nút này bấm vào mở pop-up chọn ngày"*. Wireframe không chú thích = stakeholder tự đoán = họp lại từ đầu.

## 4 bước xây dựng (Buổi 17)

1. **Xác định kích thước khung** — Lo-fi không cần chính xác tuyệt đối; Mid/Hi-fi bắt đầu từ chuẩn Desktop/Mobile (tham khảo kích thước mẫu Figma; mobile mặc định 390×844).
2. **Vẽ thành phần điều hướng trước** — Navigation Bar, Search Box, icon điều hướng (mũi tên, chevron) — bổ sung ý nghĩa liên kết giữa các khung.
3. **Vẽ thành phần lớn** — quy ước nét: **Header = nét đậm** · **Body text = nét mảnh** · **Hình ảnh = chữ nhật gạch chéo** · banner, khối lớn.
4. **Hoàn thiện chi tiết** — Dropdown, Button, Checkbox, Text Field; luồng nhiều khung cần **Progress Bar hoặc Dialog**; bổ sung **CTA** và các lựa chọn — chi tiết này giúp người khác hiểu ý tưởng.

## 6 lưu ý (Buổi 17)

1. **Tạo đầy đủ tương tác ở trang chính** — trang chính là điểm bắt đầu của rất nhiều trang phụ/chi tiết.
2. **Không dùng Lorem Ipsum** — ghi text thật thể hiện ý tưởng: tên cửa hàng, tiêu đề đoạn, nhãn CTA thật.
3. **Thực tế hóa thao tác** — chỉ vẽ thao tác có thể hiện thực hóa trên sản phẩm sau này.
4. **Ghi chú rõ ràng** — để các bên liên quan hiểu nhanh.
5. **Có cấu trúc phân cấp** — điều hướng, thành phần trong trang, nội dung.
6. **Sáng tạo nhiều giải pháp** — mỗi ý tưởng có nhiều solution, vẽ vài phương án rồi chọn theo mục tiêu.

## 3 mức fidelity

| Mức | Đặc điểm | Dùng khi |
|---|---|---|
| **Lo-fi** | Thô, giấy bút được, không cần kích thước chính xác | Khám phá nhanh, họp ý tưởng, đếm màn |
| **Mid-fi** | Công cụ số, chính xác chi tiết hơn | Bàn giao nội bộ, usability test sớm |
| **Hi-fi** | Hình ảnh/thông tin/màu/button tương đồng prototype nhưng KHÔNG tương tác | Duyệt stakeholder cuối trước Figma/dev |

## Quy ước render HTML/SVG (khi skill tự vẽ)

- Khung thiết bị đúng kích thước (mobile 390×844 mặc định), mỗi màn một khung, nhãn **mã màn khớp Screen Inventory** phía trên khung.
- Palette: nền trắng, khối xám `#E5E5E5`–`#9E9E9E`, viền `#616161`, chữ đen; xanh dương `#1E6FEB` CHỈ cho CTA chính/link.
- Font: một font hệ thống; phân cấp bằng size/weight (Header đậm 18-20, body 14, caption 12).
- Ảnh: `<div>` viền + hai đường chéo SVG (✕). Icon: hình khối đơn giản hoặc ký tự (☰ ⌕ ‹ ›), không icon set màu mè.
- Annotation: chú thích đánh số ①②③ neo cạnh phải khung hoặc dưới khung, mỗi chú thích một dòng logic ("① bấm mở bottom sheet chọn size").
- Trạng thái biến thể: render cạnh màn gốc, cùng mã + hậu tố (S03 / S03-empty / S03-error).
- Nhiều màn: sắp theo thứ tự flow, mũi tên → giữa các khung khi hữu ích.
- Xuất bàn giao: một file HTML chứa toàn bộ khung + bảng inventory + annotations; tuyệt đối giữ Quy tắc 3 Không kể cả khi user đòi "cho đẹp tí" — đẹp là việc của Figma, wireframe đẹp quá sẽ bị review như bản thiết kế thật.
