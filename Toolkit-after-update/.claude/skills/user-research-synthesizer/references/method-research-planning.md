<!-- PROVENANCE — do build script sinh, KHÔNG sửa tay
nguồn      : ux-research-planner.skill  →  SKILL.md
nhập ngày  : 2026-08-09
trạng thái : chép nguyên văn, không tóm tắt, không diễn giải
cập nhật   : xuất lại file .skill từ Claude rồi chạy lại build script
-->

---
name: ux-research-planner
description: "Plan and execute UX research and requirements gathering (thu thập yêu cầu, nghiên cứu người dùng) using the team's 5-step research planning framework and quantitative/qualitative method catalog. Use whenever the user wants to: xác định yêu cầu người dùng, lập kế hoạch UX research, viết kịch bản phỏng vấn, tạo survey/bảng hỏi, chọn phương pháp nghiên cứu (định lượng vs định tính), phân loại người dùng, chuẩn bị card sorting/tree testing/focus group, hoặc đo ROI của nghiên cứu. Also trigger when a PRD or design decision needs user evidence before proceeding — e.g. 'mình chưa biết user có cần tính năng này không', 'cần validate giả định này'. Sits at the Empathize stage, before persona/journey work (ux-persona-journey) and feeds prd-builder Section 3."
---

# UX Research Planner

Biến câu hỏi mơ hồ ("người dùng có cần X không?") thành một kế hoạch nghiên cứu chạy được, đúng phương pháp, và ra dữ liệu dùng được cho Persona/PRD. Skill này mã hóa framework của team: lập kế hoạch 5 bước, catalog phương pháp định lượng/định tính, và triết lý "hiểu người dùng trong sự liên kết với vấn đề của doanh nghiệp".

**Vị trí trong pipeline**: Trước Empathize → dữ liệu đổ vào `ux-persona-journey` (Empathy Map, Persona, CJM) và `prd-builder` Section 3. Nghiên cứu nâng cấp sản phẩm cũ thì chạy song song với review mining của prd-builder.

## Workflow

### 1. Làm rõ 2 phía yêu cầu trước khi chọn phương pháp

Luôn bắt đầu bằng 2 câu hỏi gốc của framework:
- **Cái BẠN (doanh nghiệp) muốn trên sản phẩm là gì?** → Business goals quy về 2 loại: **Make more money / Save more money**. Ép người dùng skill nói rõ mục tiêu doanh nghiệp bằng con số nếu có.
- **Cái NGƯỜI DÙNG muốn là gì?** → Nhớ nguyên tắc: người dùng không nói ra được cái họ muốn ("e ăn gì cũng được... thế ăn cơm nhé? Không") — nghiên cứu tồn tại để tìm cái họ KHÔNG nói ra.

Sau đó phân loại người dùng theo 6 nhóm của framework và gán mức độ quan trọng — đọc `references/methods-catalog.md` mục "Phân loại người dùng". Nghiên cứu nhắm sai nhóm là nghiên cứu bỏ đi.

### 2. Xác định loại yêu cầu cần làm rõ

Từ mục tiêu, đánh dấu những nhóm yêu cầu cần evidence (5 nhóm chuẩn của team): **chức năng** (hệ thống cần làm gì), **dữ liệu** (người dùng cần thông tin gì), **môi trường** (vật lý/xã hội/tổ chức/kỹ thuật), **kỹ năng & khả năng người dùng**, **suy nghĩ & tâm lý** (nhóm quan trọng nhất với trải nghiệm). Mỗi nhóm chưa rõ = một mục tiêu nghiên cứu.

### 3. Lập kế hoạch theo 5 bước chuẩn

Đi đúng thứ tự, viết thành văn bản kế hoạch:

1. **Mục đích nghiên cứu** — gồm B1 (đối tượng người dùng: họ là ai, nhóm nào quan trọng) + B2 (mục tiêu nghiên cứu). Với sản phẩm MỚI: mục tiêu về chức năng / nội dung / hành vi người dùng. Với NÂNG CẤP: đánh giá bản cũ tìm vấn đề tồn tại + xác định cái mới. Nếu tự vạch chức năng để khảo sát → bắt buộc nghiên cứu ứng dụng liên quan trước, rồi mới hỏi người dùng muốn thêm/bớt gì.
2. **Phương thức nghiên cứu** — chọn từ catalog định lượng/định tính theo cây quyết định trong `references/methods-catalog.md`. Không chọn method trước khi có mục tiêu — đây là lỗi phổ biến nhất.
3. **Đối tượng tham gia** — đúng phạm vi người dùng mục tiêu; không phỏng vấn bừa, không spam link survey.
4. **Địa điểm** — bắt buộc với phỏng vấn/quan sát. Phỏng vấn cho kết quả tốt nhất khi sắp xếp được vào lúc người dùng ĐANG sử dụng sản phẩm.
5. **Kịch bản** — viết script cụ thể cho phương pháp đã chọn (câu hỏi phỏng vấn, bảng hỏi, task list cho card sorting/tree testing...).

Output: file `research_plan.md` theo template ở cuối `references/methods-catalog.md`, kèm script sẵn chạy.

### 4. Viết câu hỏi đạt chuẩn

Khi soạn kịch bản, giữ 3 tiêu chí câu hỏi định tính tốt của team: **kết thúc mở** (cho họ nói ý riêng), **nói đơn giản** (không biệt ngữ), **cung cấp thông tin cần thiết** (câu không phục vụ nghiên cứu → bỏ). Với survey: **hạn chế câu hỏi dẫn dắt** — tránh biến dữ liệu thành ý kiến chủ quan của chính mình. Mỗi câu hỏi phải trả lời được: "kết quả thu về giúp mình giải quyết được gì?"

### 5. Kết hợp định tính + định lượng

Mặc định đề xuất mixed-methods theo mẫu Samsung TV của giáo trình: **định tính trước để tìm insight rộng** (quan sát/ethnography phát hiện "TV bị tắt cả ngày → là đồ nội thất") → **định lượng sau để chứng minh bằng số** (CSAT, Likert xác nhận thiết kế mới). Định lượng cho kết quả tập trung-hẹp; định tính cho toàn cảnh-rộng — trình bày cho stakeholder theo đúng cặp này.

### 6. Đo hiệu quả nghiên cứu (khi bị hỏi "nghiên cứu làm gì cho tốn tiền")

ROI = 100% × Net Return / Cost of Investment. Net Return gồm: giảm chi phí sửa vấn đề phát hiện muộn, giảm chi phí CSKH, tăng doanh số, giảm churn sau khi sửa điểm chạm, tăng NPS, tránh tổn hại thương hiệu. Cost gồm: lương team, chi phí tuyển + incentive người tham gia, công cụ. Dùng khung này để bảo vệ ngân sách nghiên cứu trước PM.

## Nguyên tắc giữ chất lượng

- Mỗi finding ghi rõ nguồn (phương pháp, ngày, số người) — dữ liệu từ nghiên cứu tài liệu/thứ cấp chỉ mang tính **dự đoán**, phải dán nhãn như vậy.
- Quan sát tự nhiên: không đặt nhiều câu hỏi, luôn ghi sổ tay — output là ghi chú thô, không phải kết luận.
- Nhóm mục tiêu chỉ đề xuất khi có người dẫn dắt đủ nghệ thuật; nếu không, đổi sang phỏng vấn 1-1.
- Đề tài nhạy cảm (tài chính, sức khỏe) → luôn one-on-one, không focus group.
- Kết quả nghiên cứu đổ về đâu: cập nhật `research_log.md` của dự án (nếu đang dùng prd-builder) và bàn giao dữ liệu thô cho bước tổng hợp persona.
