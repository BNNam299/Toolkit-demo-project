<!-- PROVENANCE — do build script sinh, KHÔNG sửa tay
nguồn      : ux-persona-journey.skill  →  SKILL.md
nhập ngày  : 2026-08-09
trạng thái : chép nguyên văn, không tóm tắt, không diễn giải
cập nhật   : xuất lại file .skill từ Claude rồi chạy lại build script
-->

---
name: ux-persona-journey
description: "Synthesize raw user research into Insight, Job-to-be-Done, Empathy Map, User Persona, and Customer Journey Map (CJM) using the team's Empathize/Define toolkit (5 Whys + Kipling's questions, Lotus Blossom, Fishbone, Affinity Diagram). Use whenever the user wants to: tạo persona, vẽ empathy map, xây customer journey map / user journey map, tìm insight từ dữ liệu phỏng vấn/khảo sát, xác định vấn đề (Define), đào root cause của một vấn đề UX, hoặc xác định Job to be Done. Also trigger right after research data arrives ('phỏng vấn xong rồi, giờ làm gì'), or when prd-builder Section 3 (personas, hành trình người dùng) needs proper grounding. Sits in Empathize→Define, after ux-research-planner, before ux-flow-architect."
---

# Persona & Journey Synthesizer

Chuyển dữ liệu nghiên cứu thô thành các artefact Define chuẩn: Insight → Job to be Done → Empathy Map → Persona → Customer Journey Map. Nguyên tắc lõi của giáo trình: **xác định và nêu ra được ĐÚNG vấn đề sẽ dẫn chúng ta đi đúng hướng** — mọi artefact ở đây tồn tại để phục vụ câu đó.

**Vị trí trong pipeline**: sau `ux-research-planner` (nhận dữ liệu thô), trước `ux-flow-architect` (persona + CJM là đầu vào của user story và flows). Persona hoàn chỉnh đổ thẳng vào `prd-builder` Section 3.

## Workflow

### 0. Kiểm tra đầu vào

Hỏi có dữ liệu nghiên cứu thật không (ghi chú phỏng vấn, survey, quan sát, analytics, review). Có → làm chuẩn. Không có → vẫn làm được nhưng mọi artefact dán nhãn **[GIẢ ĐỊNH]** và kết thúc bằng kế hoạch validate (đúng cách giáo trình dạy với CJM giả định: tự xây dưới góc nhìn Persona → nhờ người dùng thực xác thực → điều chỉnh).

### 1. Sắp xếp dữ liệu — Affinity Diagram

Trước khi tạo persona, gom toàn bộ quan sát/quote thành Affinity Diagram: mỗi dữ kiện một thẻ, nhóm theo quan hệ tự nhiên, đặt tên nhóm. Làm trong file văn bản dạng cây. Nhóm nào dày thẻ = tín hiệu mạnh.

### 2. Đào Insight — bộ công cụ đào sâu

Đọc `references/define-toolkit.md` trước khi chạy các kỹ thuật này. Insight = **sự thật ẩn giấu, khó phát hiện, có khả năng tác động đến hành vi và quyết định** của khách hàng — không phải quan sát bề mặt.

- **5 Whys** trước để tìm root cause (mỗi Why có thể ra nhiều nguyên nhân → đào tiếp từng nhánh), rồi **Kipling's questions** (What/Where/When/Who/How) để thu thập toàn diện quanh từng nguyên nhân — luôn bắt đầu chuỗi bằng Why và bám từ khóa vấn đề.
- Vấn đề nhiều nguyên nhân rối → **Fishbone** (mỗi đầu xương = 1 cause từ 5 Whys; nhánh xương = yếu tố Kipling) hoặc **Lotus Blossom** (vấn đề ở nhụy, yếu tố ở cánh; lấy cánh làm nhụy mới để đào tiếp).
- **Beginner's Mindset**: đặt mình vào người lần đầu tiếp cận để dự đoán trải nghiệm của họ.

### 3. Chuyển Insight → Job to be Done

Với mỗi insight mạnh, hỏi: **công việc thực sự khách hàng "thuê" sản phẩm để hoàn thành là gì?** (mua dao cắt giấy → JTBD là cắt tấm giấy to thành nhiều tấm nhỏ). Reframe: khách hàng không mua sản phẩm — họ **thuê** sản phẩm để xong việc của họ. JTBD này sau trở thành ngôn ngữ của tính năng trong PRD.

### 4. Empathy Map → Persona

Empathy Map dựa trên **người thật** từ dữ liệu (Says/Thinks/Does/Feels + Pains/Gains). Rồi đúc Persona — bản mô tả **hư cấu nhưng chân thực** đại diện một nhóm người dùng mục tiêu, là ánh xạ dữ liệu từ UX research.

Persona phục vụ 4 việc: xây đồng cảm · xác định vấn đề · tạo ý tưởng đúng tệp (Ideate) · làm tiêu chí tuyển người tham gia test (Test). Persona đạt chuẩn khi qua đủ **6 tiêu chí** trong `references/define-toolkit.md` (context, real behaviors, end-goals, viết từ persona's perspective, bối cảnh rõ, pain points rõ). Sau khi tạo Persona → tạo Empathy Map riêng cho Persona đó (đúng trình tự giáo trình).

Chống anti-pattern: nhiều persona chỉ khác tuổi = một persona — phân biệt bằng need/context hoặc gộp lại.

### 5. Customer Journey Map

Chọn hành trình theo 1 trong 3 chiến lược: **tiêu biểu** (ảnh hưởng nhiều người dùng nhất — e-commerce là flow mua hàng), **đang nhiều vấn đề** (đào pain), hoặc **theo thời gian** (sản phẩm banking/tiết kiệm). CJM tập trung trải nghiệm của **một** Persona.

Cấu trúc: trục dọc = điểm chạm theo thứ tự; trục ngang = thuộc tính từng điểm chạm — trải nghiệm khách hàng ở nửa trên, business ở nửa dưới. Mỗi điểm chạm ghi đủ 4 yếu tố user: **Hành động · Cảm xúc · Chướng ngại vật · Touchpoint**, cộng góc nhìn doanh nghiệp (mục tiêu, chỉ số, hệ thống). Giai đoạn khung: Trước mua (Awareness → Consideration → Decision) → Mua (Purchase → Use) → Sau mua (Advocacy → Giới thiệu). Hai điểm phải luôn nắm: **động lực mua hàng** và **khoảnh khắc của sự thật**.

5 biến thể CJM khi cần (bản đồ trải nghiệm / trạng thái hiện tại / trạng thái tương lai / cuộc sống hàng ngày / empathy map) — chọn theo mục đích, xem reference. CJM cũng có thể vẽ cho **hành trình của user trên dịch vụ tương đồng mà họ không hài lòng** để đánh giá cơ hội cho app mình.

### 6. Bàn giao

- Persona + hành trình hiện tại/mong muốn → `prd-builder` Section 3 (đúng format Profile/Context/Pain Points/Need).
- Pain points từ CJM → danh sách cơ hội, đối chiếu với review mining nếu có.
- Persona → tiêu chí tuyển participant cho `ux-usability-evaluator`.
- Mọi mục [GIẢ ĐỊNH] → sinh nhiệm vụ validate cho `ux-research-planner`.
