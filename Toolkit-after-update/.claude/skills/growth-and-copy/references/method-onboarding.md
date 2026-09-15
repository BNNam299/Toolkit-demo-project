<!-- PROVENANCE — do build script sinh, KHÔNG sửa tay
nguồn      : onboarding-scenario-selector.skill  →  SKILL.md
nhập ngày  : 2026-08-09
trạng thái : chép nguyên văn, không tóm tắt, không diễn giải
cập nhật   : xuất lại file .skill từ Claude rồi chạy lại build script
-->

---
name: onboarding-scenario-selector
description: "Chọn và thiết kế kịch bản Onboarding + Paywall cho mobile app theo bộ 8 kịch bản chuẩn của team (Direct Outcome, Aha Before Paywall, Personalized Intent, Progress Loading, Trial-first, No Trial High Intent, Downsell After Close, Permission-led Setup). Dùng skill này BẤT CỨ KHI NÀO user hỏi về onboarding hoặc paywall của mobile app - nên dùng kịch bản onboard nào, thiết kế luồng onboarding/paywall, tăng trial/purchase conversion, chọn chiến lược monetization đầu phễu, làm paywall cho một thị trường/quốc gia cụ thể, so sánh trial vs no-trial, xử lý paywall close rate cao, hay xin permission trong onboarding. Cũng trigger khi user nhắc KB1-KB8, kịch bản onboard, luồng ONB, IAP paywall, aha moment, downsell, hard/soft paywall, hoặc đưa metric phễu (install to paywall, trial start, D1 cancel, refund) và hỏi nên đổi gì. Skill sẽ hỏi các câu chẩn đoán cần thiết rồi gợi ý kịch bản kèm target, event tracking và kill rule."
---

# Onboarding Scenario Selector

Chọn đúng kịch bản Onboarding + Paywall trong bộ 8 kịch bản chuẩn, dựa trên đặc điểm app, nguồn traffic và tình trạng metric hiện tại. Chi tiết đầy đủ từng kịch bản (fit/anti-fit, target, request cho Product/Design/Dev, events, kill rule, wireframe) nằm trong `references/scenarios.md` — đọc file đó trước khi viết recommendation cuối.

## Bộ 8 kịch bản (tóm tắt nhận diện)

| Mã | Tên | Bán bằng gì | Dấu hiệu chọn nhanh |
|---|---|---|---|
| KB1 | Direct Outcome Paywall | Lời hứa outcome, bán sớm sau 2-3 màn | Intent đầu vào mạnh, pain rõ, không cần thấy kết quả visual |
| KB2 | Aha Before Paywall / Result Unlock | Preview/partial result thật, gate phần full | Value là kết quả nhìn thấy được (before/after, AI output, scan) |
| KB3 | Personalized Intent Paywall | 1 câu hỏi intent → đổi headline/benefit paywall | App nhiều use case, nhiều persona, một paywall bán cho nhiều kiểu user |
| KB4 | Progress Loading + Value Build | Biến loading thật thành màn build trust | Có AI generation/scan/analyze mất vài giây |
| KB5 | Trial-first Risk-free | Giảm cảm giác rủi ro, timeline trial | Traffic broad/social, intent thấp, user sợ subscription |
| KB6 | No Trial / Direct Purchase | Mua thẳng, không trial | Intent rất cao theo keyword/source, trial cancel lịch sử cao |
| KB7 | Downsell After Close | Offer mềm hơn khi user đóng paywall | Paywall view cao nhưng trial thấp, market nhạy giá |
| KB8 | Permission-led Setup | Pre-permission đúng lúc trước paywall | App cần quyền nhạy cảm (Photos, Camera, Location, Notification...) |

Lưu ý: các kịch bản KHÔNG loại trừ nhau. Tổ hợp phổ biến: KB2+KB4 (aha có loading thật), KB2+KB8 (aha cần permission), KB5+KB7 (trial-first kèm downsell), KB3+bất kỳ (personalization là lớp phủ). Recommendation tốt thường là 1 kịch bản xương sống + 1-2 lớp bổ trợ.

## Workflow

### Bước 0 — Khai thác ngữ cảnh trước khi hỏi

Đọc lại hội thoại và mọi tài liệu user đã đưa. KHÔNG hỏi lại những gì đã trả lời được:
- App thuộc dòng gì, output có visual không (app AI ảnh/interior → gần như chắc chắn dính KB2)
- Traffic đến từ đâu (đã nhắc ASA keyword? TikTok creative?)
- Metric nào đang được nêu (D1 cancel cao? paywall close nhiều?)
- Thị trường/quốc gia mục tiêu

### Bước 1 — Hỏi chẩn đoán (tối đa 2 vòng, dùng multiple choice nếu có tool)

Vòng 1 — ba câu cốt lõi, chỉ hỏi câu chưa có đáp án từ ngữ cảnh:

1. **Value proof**: User có cần NHÌN THẤY kết quả thật mới tin không, hay lời hứa outcome là đủ?
   (Kết quả visual: before/after, ảnh AI, scan preview / Outcome utility: clean xong, connect xong, export xong / Không chắc)
2. **Traffic intent**: Nguồn install chính và độ rõ của nhu cầu?
   (Keyword/ASA intent cao, cần giải quyết ngay / Broad social Meta-TikTok, intent thấp / Trộn lẫn hoặc chưa chạy UA)
3. **Tình trạng hiện tại**: Đang thiết kế mới từ đầu, hay đang tối ưu flow có sẵn? Nếu tối ưu: metric nào đang xấu?
   (Mới từ đầu / Paywall view cao nhưng trial thấp / Trial nhiều nhưng cancel-refund cao / Drop trước khi tới paywall)

Vòng 2 — hỏi bổ sung CHỈ khi liên quan đến nhánh đã lộ ra:
- App có bước xử lý mất vài giây thật không (AI generate, scan, analyze)? → quyết định lớp KB4
- App cần permission nhạy cảm trước khi tạo được value đầu tiên không? → quyết định lớp KB8
- App có nhiều use case/persona rõ rệt không? Traffic đủ lớn để đọc từng segment? → quyết định lớp KB3
- Giá và thị trường: geo nhạy giá? gói chính là weekly hay annual? → ảnh hưởng KB6/KB7
- Lịch sử trial: trial-to-paid và D1 cancel bao nhiêu? → chọn giữa KB5 và KB6

KHÔNG hỏi quá 3 câu một lượt. Nếu user trả lời "không biết", chọn nhánh an toàn hơn và ghi rõ giả định trong recommendation.

### Bước 2 — Logic chọn kịch bản

Đi theo thứ tự loại trừ:

1. **Value cần được nhìn thấy** (app visual/AI output) → xương sống là **KB2**. Loại KB1 (nguy cơ bait-and-switch, D1 cancel cao). Kiểm tra thêm: có loading thật → cộng **KB4**; cần Photos/Camera trước aha → cộng **KB8**.
2. **Value là outcome utility + intent cao** → xương sống **KB1**. Nếu lịch sử trial cancel rất cao vì "dùng xong rồi hủy" và giá weekly hợp lý → cân nhắc **KB6** nhưng CHỈ theo source/geo/keyword, không rollout global.
3. **Traffic broad/social, intent thấp** → xương sống **KB5** (trial-first, timeline 3 ngày, legal sát CTA). Gói an toàn đi kèm: **KB7** làm lưới đỡ khi close.
4. **Đang tối ưu flow có sẵn**:
   - Paywall view cao, trial thấp → thêm **KB7**; nếu nghi paywall không relevant với từng kiểu user → thêm **KB3**.
   - Trial nhiều, cancel/refund cao → xem lại kịch bản gốc có đang là KB1 ép sớm không; cân nhắc chuyển KB2 hoặc test KB6 theo segment intent cao.
   - Drop trước paywall → soi từng màn onboarding; nếu drop tại permission → **KB8**; nếu onboarding dài do profiling → cắt về đúng 1 câu intent (KB3) hoặc 2-3 màn (KB1).
5. **Nhiều persona/use case** → phủ lớp **KB3** lên xương sống bất kể là gì (chỉ 1 câu hỏi, 3-5 lựa chọn, có skip).

Nguyên tắc va chạm: KB1 và KB2 không đứng chung một flow (một bên bán trước kết quả, một bên bán sau). KB6 không đi với KB5. KB7 đi được với mọi kịch bản có nút close.

### Bước 3 — Viết recommendation

Đọc `references/scenarios.md` phần các kịch bản được chọn, rồi trả lời theo cấu trúc:

1. **Kịch bản đề xuất**: xương sống + lớp bổ trợ, một câu lý do cho mỗi lựa chọn, nêu rõ giả định nếu có
2. **Vì sao không phải các kịch bản gần kề** (1-2 kịch bản bị loại sát nút, mỗi cái một câu — giúp team không tranh cãi lại từ đầu)
3. **Luồng màn đề xuất** (wireframe dạng text theo mẫu trong references)
4. **Target số** để đánh giá thành công (lấy đúng ngưỡng trong references)
5. **Event tracking bắt buộc** (liệt kê đúng tên event)
6. **Kill rule** — điều kiện tắt kịch bản
7. **Đề xuất A/B** nếu có 2 kịch bản cạnh tranh nhau (ví dụ KB5 vs KB6: A/B theo source)

### Nghiên cứu thị trường (khi user hỏi "làm paywall cho quốc gia X")

Quy trình chuẩn của team, hướng dẫn user theo thứ tự:
1. Lên **AppStoreSpy** tìm Top 5 đối thủ cùng dòng tại quốc gia đó
2. Vào **Sensor Tower Pro** lấy thông tin 5 app: gói giá IAP đang bán, offer tốt nhất, nội dung màn paywall
3. Tổng hợp cho AI học (bảng gói giá + screenshot paywall) → sinh paywall bản địa hóa
4. Vẫn chạy workflow chẩn đoán ở trên để chọn kịch bản onboarding — nghiên cứu đối thủ quyết định GIÁ và OFFER, còn kịch bản quyết định LUỒNG

Mỗi quốc gia sinh đủ 8 biến thể kịch bản theo mẫu để đội UA có kho test.

## Lưu ý chất lượng

- Không gợi ý urgency giả, fake loading, hay giấu giá sau trial — mọi kịch bản trong bộ đều có kill rule gắn với review xấu và refund; recommendation vi phạm mấy điều này là tự kích hoạt kill rule của chính nó.
- Mọi recommendation phải kèm target số và kill rule, không đưa kịch bản chay.
- Nếu user đưa metric thật, đối chiếu ngay với ngưỡng target/kill rule trong references thay vì nhận định cảm tính.
- Kịch bản chọn ra ảnh hưởng thiết kế màn: khi user chuyển sang viết nội dung/wireframe cho từng màn, tiếp tục dùng các skill UX (ux-writing-review, ux-wireframe-builder, ux-engagement-designer) — skill này chỉ quyết định CHIẾN LƯỢC luồng.
