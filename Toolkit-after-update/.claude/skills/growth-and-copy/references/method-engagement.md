<!-- PROVENANCE — do build script sinh, KHÔNG sửa tay
nguồn      : ux-engagement-designer.skill  →  SKILL.md
nhập ngày  : 2026-08-09
trạng thái : chép nguyên văn, không tóm tắt, không diễn giải
cập nhật   : xuất lại file .skill từ Claude rồi chạy lại build script
-->

---
name: ux-engagement-designer
description: "Design motivation, retention, and interaction strategy using the team's behavior frameworks: PACT analysis, emotion levels/sources, BJ Fogg B=MAT (Motivation-Ability-Trigger with khơi mào/hướng dẫn/tín hiệu trigger types), the Hooked model (Trigger→Action→Variable Reward→Investment), and interaction-type selection (WYSIWYG/WUGIWUS, menu, form, touch gestures). Use whenever the user wants to: tăng retention/engagement, thiết kế streak/reward/gamification, tìm lý do 'user không bấm nút / không quay lại', thiết kế trigger hoặc notification strategy, phân tích PACT cho một tính năng, chọn dạng tương tác cho một chức năng, hoặc thiết kế habit loop cho app. Also trigger when prd-builder Section 2 (nguyên tắc sản phẩm) or engagement KPIs need behavioral grounding. Applies at IxD stage — after research, before/during UI design, and after launch when metrics stall."
---

# Engagement & Interaction Designer

Trả lời hai câu hỏi mà usability tốt không tự trả lời được: **tại sao user không hành động** (dù app đẹp, dễ dùng) và **làm sao giữ họ quay lại**. Mã hóa chuỗi tư duy 3 tầng của giáo trình:

> Tìm chỗ đau của người dùng, cho họ **thuốc giảm đau** *(tìm vấn đề)* → làm sao để họ mua thuốc của mình — **B=MAT** *(giải quyết vấn đề)* → sau khi mua, nâng chất lượng để họ dùng lâu dài — **Hooked** *(nâng cao chất lượng)*.

Lưu ý triết lý "thuốc giảm đau chứ không phải thuốc chữa": sản phẩm sống bằng việc tiếp tục giảm đau cho những điểm đau mới, không phải chữa dứt một lần rồi bị bỏ. Đây là logic retention của giáo trình — dùng nó khi thiết kế vòng lặp giá trị.

**Ranh giới đạo đức**: mọi cơ chế ở đây phải qua phin lọc nguyên tắc sản phẩm trong PRD (vd "tạo động lực nhưng không thao túng"). Trigger/reward vi phạm nguyên tắc → gắn cờ và đề xuất phương án khác, không lặng lẽ thiết kế.

## Workflow

### 1. Chẩn đoán trước, framework sau

Khi nhận đề bài ("retention thấp", "user không upgrade", "không ai bật notification"), xác định hành động cụ thể đang KHÔNG xảy ra, rồi chạy chẩn đoán **B=MAT** (Behavior = Motivation × Ability × Trigger, xảy ra đồng thời): thiếu 1 trong 3 thì hành động không diễn ra. Ví dụ gốc: cuộc gọi đến thành công cần chuông reo (Trigger) + muốn nghe (Motivation — số lạ thì không) + nghe được (Ability — đang lái xe thì không).

Hỏi theo thứ tự: user có BIẾT phải làm gì lúc đó không (Trigger)? → có LÀM ĐƯỢC dễ dàng không (Ability)? → có MUỐN không (Motivation)? Đọc `references/behavior-frameworks.md` để soi từng yếu tố (6 rào cản Ability, 3 cặp động cơ).

### 2. Ưu tiên đòn bẩy đúng

Nguyên tắc chốt của giáo trình: **động cơ rất khó tác động — chỉ có thể TÌM ra nó; khả năng thì làm cho DỄ HƠN được**. Vậy thứ tự đòn bẩy: (1) đơn giản hóa Ability (thời gian phù hợp, giảm gánh nặng tiền bạc/tinh thần, hợp thể chất, hợp môi trường xã hội, hợp thói quen) → (2) chọn đúng loại Trigger theo ma trận Motivation × Ability → (3) chỉ sau cùng mới nghĩ đến bơm Motivation bằng reward.

Ma trận trigger (chi tiết reference): Motivation thấp + Ability dễ → **khơi mào** · Motivation cao + Ability khó → **hướng dẫn** từng bước · Motivation cao + Ability dễ → chỉ cần **tín hiệu** (thậm chí họ tự tìm ra). Trigger bên trong (tự động trong tâm trí) là đích dài hạn — chỉ đạt được khi hành động đã thành thói quen.

### 3. Thiết kế vòng giữ chân — Hooked

Khi hành động đầu đã kích hoạt được, xây vòng **Trigger → Action → Variable Reward → Investment**:
- Trigger trong (điều user thực sự muốn) + trigger ngoài (giá trị họ thấy được từ sản phẩm).
- Action phải đơn giản — liên quan trực tiếp usability (đã ổn chưa? nối `ux-usability-evaluator` nếu chưa).
- Variable Reward chọn đúng loại trong 3 loại: **bộ lạc** (từ người khác — upvote/badge kiểu Reddit), **cuộc đi săn** (tìm kiếm thông tin/tài nguyên — kho pin Pinterest), **bản thân** (nội tại từ sự tài giỏi — streak/leaderboard Duolingo). Chọn loại khớp với cảm xúc xã hội/vật lý của persona, không rải cả ba.
- Investment: tích lũy giá trị (nội dung, dữ liệu, follow, danh tiếng, kỹ năng) để nạp trigger tiếp theo và tăng chi phí rời bỏ một cách chính đáng.

Map vòng này vào CJM: trigger đặt ở điểm chạm nào, reward trả ở khoảnh khắc nào, investment tích ở đâu.

### 4. Tầng cảm xúc

Dùng khung cảm xúc khi quyết định *thông điệp và thời điểm*: cảm xúc **vật lý** (giác quan — ấn tượng nhìn/chạm đầu tiên) vs **xã hội** (từ cộng đồng — phần thưởng xã hội có giá trị cảm xúc CAO HƠN phần thưởng tổ chức, theo so sánh trong giáo trình); 3 mức bền: **tức thì** (dễ đạt, dễ tắt) → **nghĩ tới tương lai** → **tương lai + hồi tưởng quá khứ** (bền nhất — thiết kế cho user có khoảnh khắc để nhớ lại). Tâm trạng ảnh hưởng quyết định: vui → quyết nhanh; buồn → theo thói quen, ngại đổi mới — ảnh hưởng đến việc đặt CTA nâng cấp ở đâu trong hành trình cảm xúc.

### 5. PACT & chọn dạng tương tác

Trước khi chốt cơ chế cho một tính năng, chạy phân tích **PACT** (People – Activities với 5 đặc điểm: thời gian/hợp tác/phức tạp/an toàn/bản chất nội dung – Context: tổ chức/xã hội/vật lý – Technology: đầu vào/đầu ra/nền tảng) và chọn dạng tương tác từ catalog (WYSIWYG vs WUGIWUS, menu selection, audio menu, form, WIMP, cử chỉ cảm ứng) — cả hai trong reference. Điểm giáo trình nhấn: tần suất dùng quyết định vị trí sắp xếp; tính liên tục phải được bảo toàn qua gián đoạn (auto-save, draft); phản hồi ~100ms cho thao tác tay-mắt, quá 5s là thất vọng.

### 6. Output

Bản "Engagement Strategy" ngắn: chẩn đoán B=MAT → đòn bẩy chọn + lý do → thiết kế trigger (loại, kênh, thời điểm, tần suất — đối chiếu ràng buộc notification trong PRD S9) → vòng Hooked với loại reward → chỉ số đo (nối KPI PRD S5: D1/D7/D30, số phiên/tuần) → cờ đạo đức nếu có.
