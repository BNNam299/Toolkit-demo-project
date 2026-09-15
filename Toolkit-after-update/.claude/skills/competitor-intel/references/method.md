<!-- PROVENANCE — do build script sinh, KHÔNG sửa tay
nguồn      : app-opportunity-scout.skill  →  SKILL.md
nhập ngày  : 2026-08-09
trạng thái : chép nguyên văn, không tóm tắt, không diễn giải
cập nhật   : xuất lại file .skill từ Claude rồi chạy lại build script
-->

---
name: app-opportunity-scout
description: "Discover, score, and validate mobile app opportunities BEFORE writing a PRD — using the team's discovery pipeline: need zones → problem mining (App Store/Google Play reviews, Reddit, keyword tools, Google Trends, TikTok) → need clusters → Need Score (≥25/35) and weighted Opportunity Score → real-demand vs surface-trend filter → app concepts (For [user] who…) → 3-layer competition check → fake-door validation. Use whenever the user asks: nên làm app gì, tìm ý tưởng app mới, dòng app nào sắp tăng trưởng, nghiên cứu thị trường/từ khóa/đối thủ cho một category, chấm điểm ý tưởng app, validate ý tưởng trước khi build, phân tích review đối thủ để tìm cơ hội, 'category X còn cơ hội không', hoặc săn pain points / nỗi đau người dùng trên Reddit và cộng đồng (tìm subreddit để nằm vùng, 'is there an app for', 'somebody make this'). Also trigger when prd-builder is invoked but no validated concept exists yet — opportunity research comes first. Outputs a ranked opportunity table feeding prd-builder."
---

# App Opportunity Scout — Tìm dòng app đáng phát triển

Nguyên tắc gốc của quy trình: **không cố "nghĩ ra app hay"** — xây hệ thống liên tục thu thập, nhóm và đánh giá những vấn đề người dùng đã thể hiện bằng lời nói và hành vi. Và không đoán category nào sắp tăng, mà tìm **vấn đề đang tăng nhanh hơn số giải pháp tốt hiện có**.

Câu hỏi khởi đầu đúng không phải "nên làm app thuộc category nào?" mà là: **"Nhóm người nào đang gặp một vấn đề lặp lại, đủ khó chịu, và hiện vẫn giải quyết bằng cách thủ công hoặc bằng một sản phẩm chưa tốt?"**

Chuỗi khám phá: Tín hiệu thị trường → Lời phàn nàn thực tế → Nhóm nhu cầu → Vấn đề cụ thể → Cơ hội sản phẩm → Ý tưởng app.

**Vị trí pipeline**: đứng TRƯỚC `prd-builder` (concept thắng cuộc → Section 1/4/10 của PRD); dùng chung kỹ thuật review mining với research-playbook của prd-builder nhưng ở tầm quét-thị-trường thay vì một-sản-phẩm. Khi cần phỏng vấn user thật để đào sâu một cluster → `ux-research-planner`.

## Workflow

### 0. Xác định điểm vào

Người dùng skill đang ở đâu? (a) *Chưa có gì* → bắt đầu từ Bước 1 chọn vùng nhu cầu. (b) *Có sẵn category/ý tưởng mơ hồ* ("làm app AI drawing được không?") → nhảy vào Bước 2-3 mining quanh ý tưởng đó, nhưng ép mở rộng thành cluster thay vì validate một ý duy nhất. (c) *Có danh sách ý tưởng cần chọn* → Bước 5 chấm điểm. (d) *Đã chọn, cần kiểm chứng* → Bước 7-8. Luôn nói rõ đang ở bước nào của chuỗi.

Nếu web search khả dụng: dùng để lấy dữ liệu review, thảo luận, trend thực. Nếu không: chạy quy trình trên kiến thức nền + dữ liệu user cung cấp, và **dán nhãn [ƯỚC LƯỢNG] cho mọi con số không có nguồn** — quy tắc estimate-labeling giống prd-builder.

### 1. Chọn 3-5 vùng nhu cầu (không chọn ngành ngay)

Dùng bản đồ 10 vùng trong `references/mining-playbook.md` (Quản lý cuộc sống, Tiền bạc, Sức khỏe, Tinh thần, Gia đình, Học tập, Sáng tạo, Thiết bị số, Công việc, Giải trí). Ưu tiên vùng team có lợi thế sẵn — với team này: utility/device cleaning, drawing & creative learning, remote control, subscription & mobile onboarding, AI-assisted features. Lợi thế sẵn có giảm rủi ro build lẫn marketing.

### 2. Problem mining — đào "nỗi đau thô"

Chưa nghĩ solution. Chỉ thu thập **câu nói thực tế** của user từ 5 nguồn (chi tiết cụm từ mồi trong reference): review 1-3 sao App Store/Play (app top + app đang tăng-nhưng-nhiều-complaint), Reddit/Facebook/Discord, Google Keyword Planner + autocomplete, Google Trends (nhớ caveat: chỉ số 0-100 tương đối, không phải volume tuyệt đối), TikTok/YouTube (comment giá trị hơn video). Với Reddit — nguồn giàu nhất cho ý tưởng từ con số 0 — đọc `references/reddit-hunting.md`: 3 bộ từ khóa săn nỗi đau (ức chế công cụ hiện tại / nhu cầu chưa đáp ứng / quy trình thủ công), subreddit chiến lược (r/somebodymakethis, r/findanapp, r/SideProject…), và công thức niche-down `site:reddit.com/r/<ngách> "<từ khóa>"`. Chỉ tiêu tối thiểu khi làm nghiêm túc: 100 reviews + 30 thảo luận + 30 search suggestion + 20 video comment.

Song song, dựng **nhóm từ khóa vấn đề theo 5 hướng** (Vấn đề / Kết quả mong muốn / Tính năng / Đối tượng-bối cảnh / Cách giải quyết thay thế) — không nghiên cứu từ quá rộng như "cleaner", "drawing" vì không lộ intent. Đo mỗi từ khóa theo 3 khung thời gian 90 ngày / 12 tháng / 5 năm.

### 3. Ghi nhận theo format thống nhất

Mỗi vấn đề = một dòng theo format 10 trường (User / Situation / Problem / Current workaround / Frequency / Severity / Existing solution / Complaint / Desired outcome / Evidence). Kỷ luật quan trọng nhất: **tách "user nói gì" ≠ "user thực sự cần gì"** — "tôi cần nút xóa tất cả email" có nhu cầu sâu là "giảm inbox clutter mà không sợ xóa nhầm email quan trọng". Concept phải giải nhu cầu sâu, không copy feature được yêu cầu.

### 4. Gom thành need clusters

Thu đủ ~100-200 complaint → nhóm lại (kỹ thuật giống Affinity Diagram của `ux-persona-journey`). Cluster tốt: nhiều vấn đề liên quan · nhiều nhóm người cùng gặp · mở rộng được thành nhiều feature · outcome rõ · không sống nhờ một trend rất ngắn.

### 5. Chấm điểm hai tầng

Đọc `references/scoring-validation.md` cho bảng đầy đủ:
- **Need Score** (lọc cluster): 7 tiêu chí × 1-5 (Frequency, Severity, Search Demand, Existing Workaround, Monetization, Retention, Team Fit) — giữ cluster **≥ 25/35**.
- **Opportunity Score** (xếp hạng ý tưởng/concept): điểm 1-5 × trọng số — Nhu cầu tăng 25% + Kiếm tiền 20% + Khoảng trống cạnh tranh 20% + Retention 15% + Lợi thế phân phối 10% + Lợi thế build 10%.

Kèm bộ lọc **demand thật vs trend bề mặt** (bảng đối chiếu trong reference) — một spike Google Trends không phải bằng chứng nhu cầu thương mại. Tín hiệu mạnh nhất cần săn: user đang dùng spreadsheet/workaround phức tạp, trả tiền nhiều công cụ cho một việc, **"ghét sản phẩm nhưng vẫn phải dùng"**.

### 6. Cluster → concepts

Mỗi cluster sinh **3+ concept** theo cấu trúc: *For [user] who struggles with [problem] in [context], the app helps [outcome] by [unique mechanism]*. Không chọn concept đầu tiên; một cluster tốt cho được 5-10 concept. Tránh bẫy "hot category máy móc": "AI Cleaner" là chiến lược yếu — "dọn hàng nghìn email quảng cáo theo từng sender" là chiến lược tốt, vì AI là mechanism chứ không phải value proposition.

### 7. Kiểm tra cạnh tranh 3 lớp

Lớp 1: có app giải trực tiếp không? ("không có đối thủ" KHÔNG tự động là tín hiệu tốt — có thể không có nhu cầu). Lớp 2: giải pháp thay thế phi-app (Gmail filter, xóa thủ công, *không làm gì cả*). Lớp 3: đối thủ đang bỏ sót segment nào (quá pro cho user phổ thông, thiếu quốc gia, quá đắt, thiếu privacy, chỉ giải một phần workflow) — **cơ hội thường nằm ở segment bị bỏ quên, không phải category mới**. Với mỗi cụm, phân tích 10-20 app theo checklist định lượng trong reference (xu hướng download/doanh thu 3-6-12 tháng, tốc độ tăng review, thay đổi paywall/screenshot, phân loại complaint) — thị trường tốt có NHIỀU app cùng tăng, không phải một app độc chiếm.

### 8. Validate bằng fake-door trước khi viết PRD

Với 3 concept/cluster tốt nhất: landing page kiểu App Store + icon + 3 screenshot mô phỏng + 2-3 ad creative + CTA (waitlist/early access) → chạy ad nhỏ CÙNG audience, CÙNG ngân sách → so sánh CTR, landing conversion, cost per lead, chất lượng comment, feature clicks. So concept với nhau, không so với benchmark cố định. Đây là **dùng marketing làm research**. Concept thắng → mở `prd-builder`.

### 9. Output chuẩn

Luôn kết bằng **bảng cơ hội xếp hạng** (format trong reference: Need cluster / User / Vấn đề / Evidence / Demand / Gap / Monetization / Concept) + phân loại 5 nhóm hành động: (1) nhu cầu cao + còn khoảng trống → test ngay; (2) nhu cầu cao + cạnh tranh cao → cần khác biệt mạnh; (3) nhu cầu thấp + kiếm tiền tốt → niche; (4) chỉ tăng do trend → theo dõi; (5) download cao + retention thấp → tránh. Kèm sprint plan phù hợp (14 ngày đầy đủ hoặc 7 ngày rút gọn — cả hai trong reference) nếu user muốn tự chạy.

## Nguyên tắc chất lượng

- Mỗi ô Evidence phải đếm được (số review, số thread) — không viết "nhiều người phàn nàn".
- Điểm số minh họa ≠ điểm thật: mọi bảng chấm chưa có dữ liệu nghiên cứu phải ghi chú "cần thay bằng số liệu thực".
- Không kết luận cơ hội từ một nguồn đơn lẻ; demand thật = nhiều tín hiệu độc lập cùng chiều.
- CPC cao = doanh nghiệp sẵn trả tiền cho keyword, KHÔNG tự động = app consumer sẽ thành công.
