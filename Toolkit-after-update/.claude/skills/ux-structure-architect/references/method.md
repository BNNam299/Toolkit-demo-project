<!-- PROVENANCE — do build script sinh, KHÔNG sửa tay
nguồn      : ux-flow-architect.skill  →  SKILL.md
nhập ngày  : 2026-08-09
trạng thái : chép nguyên văn, không tóm tắt, không diễn giải
cập nhật   : xuất lại file .skill từ Claude rồi chạy lại build script
-->

---
name: ux-flow-architect
description: "Design the structural layer of a product: Information Architecture (kiến trúc thông tin), Task Analysis (phân tích nhiệm vụ: mục đích→nhiệm vụ→hành động, HTA/CTA), interaction Scenarios, User Stories & Story Mapping, User Flows, Sitemap, and Wireframe preparation. Use whenever the user wants to: sắp xếp thông tin/nội dung app, mô hình hóa đối tượng, vẽ sơ đồ kiến trúc thông tin, phân tích nhiệm vụ, viết user story, làm user story map, vẽ user flow / luồng người dùng, tạo sitemap, chuẩn bị wireframe, hoặc quyết định app có bao nhiêu màn hình. Also trigger when features exist but structure doesn't ('có danh sách tính năng rồi, sắp xếp màn hình thế nào'), or when prd-builder Section 7 (features) and Section 8 (user flows) need to be derived properly. Sits after persona/journey (ux-persona-journey), before UI design."
---

# Flow Architect — IA, Task Analysis, Story Map, User Flows

Tầng cấu trúc giữa "biết người dùng cần gì" và "vẽ giao diện": tổ chức thông tin, phân rã nhiệm vụ, viết story, vẽ luồng. Phép so sánh gốc của giáo trình: **IA xây bố cục thư viện (cấu trúc — danh mục và nhãn); User Flow là biển chỉ dẫn qua các giá sách (hành trình — các bước hoàn thành nhiệm vụ)**. IA cung cấp cấu trúc; flow áp cấu trúc đó vào cách user làm task đơn giản nhất có thể.

**Vị trí pipeline**: nhận Persona + CJM từ `ux-persona-journey` → output đổ vào `prd-builder` S7 (bảng tính năng) và S8 (luồng), rồi wireframe/Figma. Thứ tự nội bộ đúng giáo trình: **Task Analysis/IA → User Story → Story Map → User Flows → Sitemap → Wireframe** (flows nằm sau Persona + Story, TRƯỚC wireframe).

## Workflow

### 1. Phân tích nhiệm vụ — Mục đích → Nhiệm vụ → Hành động

Bắt đầu từ ý tưởng chứ không phải app có sẵn. Ba tầng, đọc chi tiết ở `references/structure-methods.md`:

- **Mục đích** = trạng thái/kết quả cuối user muốn khi dùng sản phẩm. Một sản phẩm chứa NHIỀU mục đích; mục đích thường trở thành **chức năng của hệ thống sau này** — đây chính là cầu nối sang bảng tính năng PRD.
- **Nhiệm vụ** = các hoạt động cần thiết để đạt mục đích; một mục đích có nhiều cách nhiệm vụ khác nhau.
- **Hành động** = bước cụ thể nhỏ nhất, không cần giải quyết vấn đề; xác định được hành động là hình dung được tương tác trên giao diện. Cùng một nhiệm vụ có thể có nhiều cách hành động (kéo thanh cuộn thay vì gõ số).

Trình bày dạng bảng `Mục đích | Nhiệm vụ | Hành động`. Chọn HTA (phân cấp toàn cục) hay CTA (đi theo nhận thức trong đầu user, phân tích một nhiệm vụ nhỏ trong mục đích lớn) theo reference.

Kèm **Scenario** cho các nhiệm vụ chính: mô tả chuỗi hành động + phản hồi hệ thống, chia bước; brainstorm mỗi bước bằng 3 loại thẻ của giáo trình — **Design Ideas** (thiết kế giao diện ra sao để họ tương tác), **Questions** (tình huống có thể xảy ra — thiết kế khắc phục được không?), **Comments & Considerations** (làm hay không làm, cân nhắc gì).

### 2. Kiến trúc thông tin

- **Mô hình hóa đối tượng**: xác định user tương tác với ĐỐI TƯỢNG thông tin nào → thuộc tính của từng đối tượng → quan hệ giữa các đối tượng. (VnExpress: đối tượng = bài tin; thuộc tính = tiêu đề, tóm tắt, số cmt, thời gian, tác giả...). Dữ liệu lấy từ nghiên cứu người dùng — muốn biết đối tượng thì phải biết mục tiêu/nhiệm vụ của họ.
- **Tổ chức phân loại nội dung**: chọn dạng sắp xếp (thời gian, sự kiện, alphabet, địa lý, định dạng, nhiệm vụ, nhóm đối tượng).
- **Sơ đồ kiến trúc thông tin**: chọn 1 trong 5 kiến trúc (phân cấp cây / tuyến tính / chuyên mục+database / hub / tab — mobile chuộng tuyến tính và tab; hub cho app phân quyền). Hai giá trị thực dụng của sơ đồ: (a) rà soát thiếu nội dung trước khi vẽ UI/bàn giao dev, (b) **mỗi ô = một trang → đếm được số màn hình → ước tính kinh phí/báo giá**. Tên các ô chính là tiêu đề trang trong bản thiết kế; Navigation là cách IA thể hiện ra bên ngoài.
- Cần validate IA với người dùng? → Card Sorting (tạo mới) / Tree Testing (đánh giá) qua `ux-research-planner`.

### 3. User Story & Story Mapping

Story đúng cấu trúc: **"Là … [người dùng như thế nào], tôi … [mong muốn] … để … [mục tiêu]"** — 4 điểm giữ chuẩn: rõ vai trò, nổi bật "lý do", một câu duy nhất, ngôn ngữ hướng hành động. User Story là **tập con của CJM**: journey map cho toàn cảnh và pain; story cho yêu cầu cụ thể của MỘT tính năng, chống phình tính năng.

Story Mapping 4 bước (chi tiết + ví dụ mua nhạc trong reference): khung What/Who/Why → **xương sống** (backbone = luồng hoạt động chính mang giá trị chính) → chia thẻ và nhóm dưới từng bước xương sống → **ưu tiên** theo hàng ngang (hàng 1 = release đầu). Hàng ưu tiên 1 phải khớp Phạm vi MVP trong PRD S6 — lệch là báo ngay.

### 4. User Flows — 8 quy tắc

Vẽ được ở bất kỳ giai đoạn thiết kế nào và giúp xác định IA. Ký hiệu chuẩn: tròn/chữ nhật bo = bắt đầu-kết thúc · thoi = quyết định · chữ nhật = trang/màn hình/hành động · mũi tên = điều hướng · vuông = ghi chú. Khi sang wireframe, chữ nhật được thay bằng trang thật.

Giữ đủ 8 quy tắc của giáo trình (chi tiết reference): tên tự mô tả · luồng một chiều · **một mục tiêu mỗi luồng** (không chen ngang khi user đang cố hoàn thành nhiệm vụ) · luôn có key chú giải · điểm bắt đầu rõ (nhiều điểm bắt đầu → tách luồng) · gán nhãn ngắn rõ · hạn chế màu (tốt nhất không màu; dùng thì phải chú giải) · **có giải pháp rõ ràng** (luồng phải hoàn tất khi đạt mục tiêu — không để trạng thái "đồng ý cũng được không cũng chẳng sao").

Bắt đầu từ nghiên cứu đối thủ: đi qua sản phẩm cạnh tranh và **phác thảo lại luồng của họ** trước khi vẽ luồng của mình. Xuất flows dạng danh sách bước đánh số + sơ đồ Mermaid khi hữu ích; luồng chính + luồng phục hồi/lỗi đổ vào PRD S8.

### 5. Sitemap → Wireframe

Sitemap: chạy Card Sorting trước để phân cụm chức năng. Wireframe: chọn độ chi tiết Lo-fi (giấy bút, chưa cần kích thước chính xác) / Mid / Hi-fi (tương đồng prototype nhưng không tương tác); các bước: xác định kích thước khung (Mid/Hi theo chuẩn thiết bị trong Figma) → vẽ thành phần điều hướng (nav bar, search box, icon điều hướng) trước để giữ liên kết giữa các khung. Skill này dừng ở spec wireframe — việc đánh giá thiết kế thuộc `ux-design-review`/`ux-usability-evaluator`.

## Kiểm tra chéo trước khi bàn giao

- Mỗi tính năng trong story map ↔ một Mục đích trong task analysis ↔ một Persona need. Đứt mạch nào → quay lại tầng đó.
- Mỗi màn hình trong IA xuất hiện trong ≥1 flow; màn hình mồ côi = thừa hoặc thiếu flow.
- Flow chính đến giá trị trong ≤ số bước đối thủ (nếu có dữ liệu từ prd-builder S4).
