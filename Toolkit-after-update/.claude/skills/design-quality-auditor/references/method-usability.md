<!-- PROVENANCE — do build script sinh, KHÔNG sửa tay
nguồn      : ux-usability-evaluator.skill  →  SKILL.md
nhập ngày  : 2026-08-09
trạng thái : chép nguyên văn, không tóm tắt, không diễn giải
cập nhật   : xuất lại file .skill từ Claude rồi chạy lại build script
-->

---
name: ux-usability-evaluator
description: "Evaluate product usability using the team's 5-component framework (Learnability, Efficiency, Memorability, Errors, Satisfaction) with the 0-4 severity scoring scale — via expert evaluation (đánh giá chuyên gia) or moderated user testing (đánh giá của người dùng). Use whenever the user wants to: đánh giá khả năng sử dụng, chấm điểm usability một app/màn hình, tìm lỗi dự đoán/nhận biết/điều hướng, chạy usability testing với người dùng thật, viết kịch bản test, phân loại mức nghiêm trọng của lỗi UX, hoặc kiểm tra sản phẩm trước khi lên store. Also trigger for 'app này dùng có ổn không', 'review trải nghiệm app X', or when ux-design-review needs the team's own scoring methodology instead of generic heuristics. Works on live apps, prototypes, wireframes, and screenshots; applies before design, at wireframe/lo-fi, before wide launch, and after launch."
---

# Usability Evaluator — Framework 5 thành phần & thang 0-4

Đánh giá khả năng sử dụng theo đúng phương pháp của team, hai chế độ: **đánh giá chuyên gia** (chủ quan, dựa chuyên môn — nhanh, rẻ) và **đánh giá người dùng** (khách quan — cần user thật, dựa kịch bản mình xây). Định nghĩa gốc: *Usability là khả năng, mức độ sử dụng sản phẩm để đạt được mục tiêu do con người quy định trong một bối cảnh cụ thể* — và **UX = LOOK + FEEL + USABILITY**, nên skill này đo phần USABILITY, không thay thế đánh giá thẩm mỹ.

**Quan hệ với skill khác**: `ux-design-review` chấm theo Nielsen/Shneiderman (chuẩn quốc tế); skill này chấm theo framework nội bộ 5 thành phần + thang 0-4 — khi cần báo cáo cho team thì dùng skill này, cần đối chiếu chuẩn ngoài thì chạy cả hai và merge findings.

## Chế độ A — Đánh giá chuyên gia

### 1. Hiểu sản phẩm trước khi đánh giá

Bắt buộc theo trình tự giáo trình: hiểu sản phẩm → **xây kịch bản sử dụng** của người dùng trên sản phẩm → kiểm tra khả năng sử dụng DỰA TRÊN kịch bản đó. Kịch bản trả lời: **Who** (đối tượng dùng là ai) · **When** (khi nào dùng) · **Why** (dùng để làm gì) · **How** (nó mang lại cái gì). Có persona từ `ux-persona-journey` thì lấy làm Who; không có thì dựng nhanh và ghi chú là giả định.

### 2. Đi qua 5 thành phần với tiêu chí con

Đọc `references/usability-framework.md` cho định nghĩa đầy đủ + ví dụ chấm mẫu (case MyTV). Khung:

- **Learnability (Dễ dùng)** — khả năng **dự đoán** (đoán được kết quả hành động tương lai; đoán rồi phải đúng) + khả năng **nhận biết** (nhìn thấy và hiểu được; nút không được lẫn vào text). Tương tác ẩn chỉ chấp nhận được khi dựa trên kinh nghiệm sẵn có của user (thẻ flashcard lật được vì đời thực có).
- **Efficiency (Hiệu suất)** — 4 tiêu chí: **điều hướng** (bản đồ di chuyển rõ, đường ngắn nhất — liên quan trực tiếp IA) · **điều khiển** (cá nhân hóa, kiểm soát hiển thị) · **phản hồi** (rõ, nhất quán, nhanh, liên tục — biết thành công/lỗi để sang bước kế) · **hệ thống thông minh** (gợi ý, giảm thao tác).
- **Memorability (Ghi nhớ)** — **sự quen thuộc** (ngôn ngữ/biểu tượng quen; icon mới thì kèm chú thích lần đầu) + **tính nhất quán** trong hệ thống.
- **Errors (Lỗi)** — phân mức: **không nghiêm trọng** (tự sửa được) / **trung tính** (không hậu quả lớn nhưng phiền) / **nghiêm trọng** (kết quả xấu: mất file, xóa nhầm). Kiểm tra đủ 3 cơ chế khắc phục: **cảnh báo** (confirm trước rủi ro) · **tự bảo vệ** (auto-save, chặn file nguy hiểm) · **khả năng phục hồi** (thùng rác 15-30 ngày, undo).
- **Satisfaction (Thỏa mãn)** — tính **linh hoạt** (nhiều cách làm cho trình độ khác nhau; responsive theo nền tảng) + **phong cách thiết kế** hợp đối tượng + tương tác thân thiện, tránh thay đổi đột ngột gây gián đoạn. **Lưu ý gốc: Satisfaction phải có người dùng thật mới đánh giá được** — chế độ chuyên gia chỉ chấm 4 thành phần đầu, Satisfaction để chế độ B.

### 3. Chấm điểm thang 0-4 (giữ đúng ngữ nghĩa của team)

| Điểm | Nghĩa |
|---|---|
| **4** | OK, không phải sửa gì |
| **3** | Chưa tốt lắm — có thể sửa hoặc không |
| **2** | Vấn đề khá nghiêm trọng — cần phải sửa |
| **1** | Rất nghiêm trọng — bắt buộc sửa sớm |
| **0** | Bắt buộc sửa, không thì người dùng không dùng được |

Mỗi finding ghi: vị trí/màn hình → mô tả lỗi → **thuộc tiêu chí nào** (vd "lỗi khả năng dự đoán + điều hướng") → điểm → đề xuất sửa. Một lỗi có thể dính nhiều tiêu chí (case MyTV: bấm "Tất cả phim đề xuất" ra mục Phim lẻ = lỗi dự đoán + điều hướng, 0 điểm). Kết mỗi thành phần bằng cụm giải pháp như văn mẫu MyTV — giải pháp phải trả lời được cả câu "chức năng này tạo ra với mục đích gì" khi lỗi lộ ra thiết kế thiếu mục đích (đề xuất không có cá nhân hóa thì đề xuất để làm gì?).

## Chế độ B — Đánh giá người dùng (usability testing)

Khách quan: tìm **người dùng thực sự** của sản phẩm; buổi đánh giá dựa trên kịch bản do mình xây; có thể mời nhiều người để lấy dữ liệu phân tích. Quy trình trong `references/usability-framework.md` mục "User testing": chọn thời điểm (trước thiết kế / wireframe-lofi / trước launch rộng / sau launch) → tuyển đúng persona → viết task từ kịch bản Who-When-Why-How → **hạn chế chỉ dẫn mang tính định hướng** khi moderate → quan sát + ghi chép → tổng hợp findings theo cùng 5 thành phần + thang 0-4 để merge được với chế độ A → đo Satisfaction (thang hỏi sau phiên). Đo hiệu suất người dùng bằng chính 5 tiêu chí này (đúng ghi chú giáo trình: "khi user testing thì sử dụng 5 tiêu chí này").

## Báo cáo

```markdown
# Đánh giá Usability — <sản phẩm> · <ngày> · chế độ: chuyên gia/người dùng
## Kịch bản: Who / When / Why / How
## Findings
| # | Màn hình | Mô tả | Tiêu chí vi phạm | Điểm | Đề xuất |
## Tổng hợp theo thành phần (L/E/M/Err/S) + điểm trung bình
## Ưu tiên sửa: mọi mục 0-1 trước, 2 theo sprint, 3 backlog
```
Mục 0-2 nối sang bug tracker/PRD Version History; nếu sản phẩm chưa launch, đối chiếu danh sách QA trong PRD S9 (offline, reminders, subscription, restore purchases).
