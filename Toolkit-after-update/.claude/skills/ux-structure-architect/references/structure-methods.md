<!-- PROVENANCE — do build script sinh, KHÔNG sửa tay
nguồn      : ux-flow-architect.skill  →  references/structure-methods.md
nhập ngày  : 2026-08-09
trạng thái : chép nguyên văn, không tóm tắt, không diễn giải
cập nhật   : xuất lại file .skill từ Claude rồi chạy lại build script
-->

# Structure Methods — Chi tiết & Template

## Task Analysis — ba tầng

| Tầng | Định nghĩa | Ghi nhớ |
|---|---|---|
| **Mục đích** | Trạng thái user muốn đạt, kết quả cuối cùng khi dùng sản phẩm | Thường trở thành **chức năng hệ thống**; một sản phẩm chứa nhiều mục đích (app Alarm: đặt báo thức mới / bật-tắt cái đã có / đổi giờ) |
| **Nhiệm vụ** | Hoạt động cần thiết để đạt mục đích — điều user nghĩ hoặc làm | Một mục đích → nhiều nhiệm vụ nhỏ; có nhiều cách nhiệm vụ khác nhau cho cùng mục đích |
| **Hành động** | Bước cụ thể tác động lên sản phẩm; mức nhỏ nhất, không cần giải quyết vấn đề | Xác định được hành động = hình dung được tương tác trên UI; cùng nhiệm vụ có nhiều cách hành động (thanh cuộn vs bàn phím số) |

Ví dụ chuẩn: Mục đích = Cài đặt hẹn giờ → Nhiệm vụ "Thiết lập giờ" → Hành động "Nhập số vào ô thời gian / kéo thanh cuộn".

**HTA (Hierarchical)**: phân cấp cây từ mục đích xuống nhiệm vụ xuống hành động — dùng khi cần bức tranh đầy đủ một chức năng.
**CTA (Cognitive)**: đi theo nhận thức trong đầu user, phân tích một nhiệm vụ nhỏ trong mục đích lớn, tập trung vào hành động — dùng khi tối ưu một bước cụ thể hoặc bước có gánh nặng nhận thức.

### Scenario (kịch bản tương tác)

Mô tả chuỗi hành động/sự kiện của user trên sản phẩm + phản hồi của hệ thống; một nhiệm vụ có thể thực hiện nhiều cách do điều kiện khác nhau. Cách chạy: viết tình huống (Debbie đặt phòng khách sạn vừa túi tiền, review tốt) → chia bước (tìm web → xem giá & đánh giá → xem chi tiết → chọn và đặt) → brainstorm nhóm trên từng bước bằng 3 loại thẻ:

- **Design Ideas** — cần thiết kế giao diện ra sao để họ thực hiện bước này?
- **Questions** — tình huống nào có thể xảy ra? thiết kế có khắc phục được không?
- **Comments & Considerations** — làm hay không làm; cân nhắc gì?

## Information Architecture

### Mô hình hóa đối tượng
1. User tương tác với **đối tượng** thông tin nào? (từ nghiên cứu: mục tiêu → nhiệm vụ → đối tượng)
2. Đối tượng có **thuộc tính** gì? (bài tin: tiêu đề, tóm tắt, cmt, thời gian, tác giả; trang chi tiết: nội dung đầy đủ, bài liên quan, ý kiến...)
3. **Quan hệ** giữa các đối tượng?
Nội dung có cấu trúc (phân tích được thuộc tính) vs không cấu trúc — cố phân rã thông tin thành đơn vị nhỏ.

### 7 dạng phân loại nội dung
Thời gian · Sự kiện · Alphabet · Địa lý · Định dạng nội dung · Nhiệm vụ (web nội bộ theo bộ phận) · Nhóm đối tượng (chia user thành nhóm nhỏ).

### 5 kiến trúc
| Kiến trúc | Đặc điểm | Dùng khi |
|---|---|---|
| **Phân cấp (cây)** | 1 gốc phân nhánh | Web/app nhiều tầng nội dung |
| **Tuyến tính** | Trang tuần tự lần lượt | Onboarding, wizard — phổ biến trên mobile |
| **Chuyên mục + Database** | Cây + các chuyên mục có content biểu diễn giống nhau (Store nam/Store nữ) | Catalog, thương mại |
| **Hub** | Trang trung tâm CHỈ chứa đường dẫn (không dữ liệu, không nav) | App phân quyền — chọn vai trò rồi vào giao diện riêng |
| **Tab** | Biến thể cây, các trang ưu tiên ngang nhau, chuyển nhanh; tab đang mở trở thành "trang gốc" khi quay lại | Mobile app chủ đạo |

Giá trị của sơ đồ: rà thiếu nội dung trước khi thiết kế/bàn giao dev · mỗi ô = 1 trang → đếm màn hình → **ước tính kinh phí báo giá** · tên ô = tiêu đề trang trong thiết kế · Navigation = IA thể hiện ra ngoài.

## User Story & Story Mapping

**Cấu trúc**: `Là [người dùng như thế nào], tôi [mong muốn] để [mục tiêu]`.
Ví dụ chuẩn: "Là một đại diện bán hàng, tôi muốn nhận lời nhắc tự động về các cuộc gọi và email tiếp theo để tôi có thể tiếp tục tương tác với khách hàng tiềm năng và cải thiện tỷ lệ chuyển đổi."

4 điểm giữ chuẩn: tập trung **vai trò** cụ thể · nổi bật **"lý do"** (không chỉ hành động mà cả vì sao) · **một câu** duy nhất, tránh dài dòng · ngôn ngữ **hướng hành động** ("xem", "tạo", "nhận").

**Story vs Journey Map**: CJM = toàn bộ trải nghiệm, tìm pain và vùng cải thiện, góc nhìn toàn diện; Story = yêu cầu rõ và khả thi cho MỘT tính năng, ưu tiên tính năng, chống feature bloat. Story là tập con của CJM — mỗi stage CJM sinh ra các story của stage đó.

**Story Mapping 4 bước** (featuremap.co hoặc bảng markdown):
1. **Khung**: What (giải quyết vấn đề gì / xây gì) · Who (cho ai) · Why (lợi ích cho user, team, lợi nhuận ròng).
2. **Xương sống**: các bước cấp cao nhất của hành trình. Ví dụ mua nhạc: Đăng ký → Tìm kiếm (thể loại/năm/nghệ sĩ/album) → Xem/nghe → Nhập thanh toán → Mua → Tải xuống → Tương tác xã hội/đánh giá. Backbone = luồng mang **giá trị chính** cho user.
3. **Chia thẻ & nhóm** dưới từng bước (bước "Tìm kiếm" → thẻ: tìm bản nhạc / nghệ sĩ / album / trong thể loại / theo năm). Mỗi thẻ liên hệ mục tiêu người dùng.
4. **Ưu tiên** theo hàng ngang: hàng trên cùng = bắt buộc cho release đầu. Duy trì bản đồ như tài liệu sống.

### Template Story Map (markdown)
```markdown
| Backbone → | Bước 1 | Bước 2 | Bước 3 |
|---|---|---|---|
| **P0 (MVP)** | story... | story... | story... |
| **P1** | | | |
| **P2** | | | |
```

## User Flows

**Ký hiệu**: ⬭ bắt đầu/kết thúc · ◇ quyết định · ▭ trang/màn hình/hành động · → điều hướng · ▢ ghi chú.

**8 quy tắc**:
1. **Tên tự mô tả** cho từng bước.
2. **Luồng một chiều**.
3. **Một mục tiêu mỗi luồng** — không chen ngang khi user đang cố hoàn thành nhiệm vụ; không đặt họ vào tình huống phân tâm. Nhiều mục tiêu → tách luồng.
4. **Luôn có key chú giải** (tròn = bắt đầu, chữ nhật = màn hình, thoi = quyết định...).
5. **Điểm bắt đầu rõ ràng**; nhiều điểm bắt đầu → chỉ định rõ hoặc tách thành các luồng khác nhau.
6. **Nhãn ngắn rõ**: "Màn hình đăng nhập" (màn hình) / "Đăng nhập hoặc Đăng ký" (quyết định); tránh "Đăng nhập nếu đã có tài khoản hoặc đăng ký nếu chưa có".
7. **Hạn chế màu** — tốt nhất không dùng; nếu dùng phải mô tả rõ (đỏ = quyết định, xanh = màn hình...).
8. **Giải pháp rõ ràng** — luồng hoàn tất khi đạt mục tiêu; bắt buộc qua màn chính sách → đồng ý → mới đăng ký thành công, không để lửng.

Bắt đầu: phác lại luồng của đối thủ trước → luồng đơn giản của mình → thay khối bằng wireframe/prototype khi chín.

### Template flow (text + mermaid)
```markdown
## Luồng: <tên tự mô tả — một mục tiêu>
Persona: · Điểm bắt đầu: · Mục tiêu/điều kiện hoàn tất:
1. [Màn hình] ...
2. [Hành động] ...
3. ◇ [Quyết định] ...? → Có: bước 4 / Không: bước 2b
...
Kết thúc: <trạng thái đạt mục tiêu>
Luồng lỗi liên quan: <offline / permission denied / payment fail / empty state>
```

## Sitemap & Wireframe

- **Sitemap**: chạy Card Sorting trước (cụm trên = cụm chức năng, dưới = sắp theo chức năng) → vẽ theo kiến trúc đã chọn.
- **Wireframe** 3 mức: **Lo-fi** (giấy bút, thô, chưa cần kích thước chính xác) · **Mid** (công cụ số, chính xác hơn) · **Hi-fi** (hình ảnh/thông tin/màu/button tương đồng prototype nhưng KHÔNG tương tác).
- 4 bước: (1) xác định kích thước khung (Mid/Hi: chuẩn Desktop/Mobile, tham khảo kích thước mẫu Figma) → (2) vẽ thành phần điều hướng trước (Navigation Bar, Search Box, icon mũi tên/chevron) để giữ liên kết giữa các khung → (3) vẽ thành phần lớn (Header nét đậm, body text nét mảnh, hình ảnh = chữ nhật gạch chéo, banner) → (4) hoàn thiện chi tiết (Dropdown, Button, Checkbox, Text Field; Progress Bar/Dialog cho luồng nhiều khung; CTA và các lựa chọn).
- 6 lưu ý: đầy đủ tương tác ở trang chính (điểm bắt đầu của các trang phụ) · KHÔNG Lorem Ipsum — ghi text thật thể hiện ý tưởng · thực tế hóa thao tác (chỉ vẽ cái hiện thực hóa được) · ghi chú rõ ràng cho stakeholder · có cấu trúc phân cấp · sáng tạo nhiều giải pháp rồi chọn theo mục tiêu.
- **Đếm số màn hình từ flow, estimate thời gian thiết kế, và vẽ wireframe thực tế** → dùng skill `ux-wireframe-builder` (Happy Path + Decision States + Data States).
