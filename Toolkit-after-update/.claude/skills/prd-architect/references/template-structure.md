<!-- PROVENANCE — do build script sinh, KHÔNG sửa tay
nguồn      : prd-builder.skill  →  references/template-structure.md
nhập ngày  : 2026-08-09
trạng thái : chép nguyên văn, không tóm tắt, không diễn giải
cập nhật   : xuất lại file .skill từ Claude rồi chạy lại build script
-->

# Template Structure — Section-by-Section Guide

This maps the team's PRD template exactly. For each section: purpose, question bank (pick 2-4 per turn, never all), quality bar (the line between filler and useful), failure modes, and dependencies.

## Contents
- [Entry-point routing](#entry-point-routing)
- [Dependency map](#dependency-map)
- [S0. Meta, Stakeholders, Version History, Links](#s0)
- [S1. Tóm tắt Điều hành (Executive Summary)](#s1)
- [S2. Mục tiêu và Bối cảnh](#s2)
- [S3. Vấn đề Người dùng và Đối tượng Mục tiêu](#s3)
- [S4. Phân tích Cạnh tranh](#s4)
- [S5. Tầm nhìn và Mục tiêu Sản phẩm](#s5)
- [S6. Phạm vi (Scope)](#s6)
- [S7. Yêu cầu và Tính năng](#s7)
- [S8. Luồng Người dùng](#s8)
- [S9. Ràng buộc Mobile](#s9)
- [S10. Kiếm tiền (Monetization)](#s10)
- [Full mode: các section mở rộng (theo mẫu chuẩn ScreenTimeControl)](#full-mode)
- [Meeting Notes](#meeting-notes)

## Entry-point routing

| Signal from intake | Start at | Then usually |
|---|---|---|
| Vague idea, strong user hunch | S3 Personas | S1 problem statement → S4 |
| "Category is proven, we enter it" (studio model) | S4 Competitive | S10 Monetization → S3 → S6 |
| Hard deadline / fixed team capacity | S6 Scope (backward) | S7 → S3 to validate scope serves someone |
| Monetization-first bet | S10 + S4 together | S3 → S6 |
| Vision memo already exists | S1 formalize | S3 + S4 to validate downward |
| Rebuild/pivot of existing product | S4 (incl. own product as competitor) | S3 current-journey → S6 |

S9 (Mobile Constraints) is best done late — after S6/S7 exist — but pull individual items early if they gate scope (e.g., offline requirement changes architecture and MVP size). S5 KPI is best right after S1 Success Criteria while the same thinking is warm.

## Dependency map

After committing a section, check the arrows pointing OUT of it:

- **S1 Success Criteria → S5 KPI**: KPIs must be the measurable form of the same criteria. No orphan KPIs, no unmeasured criteria.
- **S1 Target Market → S3 Personas**: primary users named in S1 must exist as a persona.
- **S3 Personas → S7 Features → S8 Flows**: every MVP feature maps to ≥1 persona need; the main flow serves the primary persona's core need end-to-end.
- **S4 Matrix → S1 Why Now / S4 Differentiation / S10 Pricing**: "why now" cites the gap the matrix shows; differentiation claims are absent-or-weak in competitors' columns; price sits justified against anchors.
- **S6 Scope → S5 KPI**: the in-scope set must plausibly move the 6-month KPIs. If not, either scope or KPI is wrong.
- **S6 Out-of-scope → S7 Post-MVP**: out-of-scope items with future intent appear in Post-MVP; permanent exclusions don't.
- **S9 Performance/Offline → S7 Feature table**: constraints that affect specific features get noted in those features' rows.
- **S10 Free vs Premium split → S3 Pain points**: the free tier must fully solve the entry pain; premium sells depth, not relief from artificial crippling.

<a name="s0"></a>
## S0. Meta, Stakeholders, Version History, Important Links

Fast, mostly clerical — do it in setup or whenever names are known. Don't spend brainstorm energy here.

- **Meta**: Version starts 1.0 (or 0.x while drafting), Mode = "Lite PRD" per template default, Status = "Bản nháp để PO rà soát" until sign-off.
- **Stakeholders table**: template has 11 fixed roles (PM, PO, Developer, UI/UX, Data Analytic, BE, AI, Graphic, ASO, Tester, Marketing/UA). Keep all rows even if unstaffed — mark `_TBD_`. Ask only: "ai đã được assign?" Roles' responsibilities are pre-written in the skeleton; edit only if this project differs.
- **Important Links**: UI/UX (Figma), Diagram, Api, Monet. Add rows as links appear during the project (research sheet, tracking doc). A PRD that links out is healthier than one that inlines everything.
- **Version History**: one row now ("Tạo file PRD"); add a row per substantive change thereafter.

<a name="s1"></a>
## S1. Tóm tắt Điều hành

**Tư duy phát biểu vấn đề (pattern tốt từ PRD Cal AI)**: mỗi vấn đề viết thành chuỗi nhân-quả *cơ chế → hệ quả đo được* — "app truyền thống bắt search món + nhập khẩu phần → user phải hành động nhiều → drop-off nhanh". Tối đa 3 vấn đề lớn, đánh số. **Giải pháp phải map 1-1 với từng vấn đề** (vấn đề 1 → cơ chế giải 1…) — nếu một vấn đề không có lời giải tương ứng, hoặc cắt vấn đề hoặc thừa nhận trong Câu hỏi Mở. Định vị viết dạng mũi tên from→to ("tool đếm calories → AI hỗ trợ ăn uống & tạo thói quen"). Khung thị trường nên reframe theo kinh tế retention: **market size không nằm ở số người tải mà ở số người stick & trả tiền dài hạn** — số downloads của đối thủ chỉ chứng minh nhu cầu tồn tại.

**Purpose**: the 60-second read for anyone deciding whether to fund/join. Written last-or-iteratively, readable first. It compresses S3, S4, S5 — expect to revisit it after those solidify.

**Subsections**: Phát biểu Vấn đề · Giải pháp · Tại sao là lúc này · Thị trường Mục tiêu (Primary Users / Positioning / Market Size Framing / Market Trend) · Tiêu chí Thành công.

**Question bank**:
- Nếu chỉ được nói 2 câu với CEO về lý do làm sản phẩm này, bạn nói gì?
- Vấn đề này gây đau ở đâu: mất thời gian, mất tiền, mất động lực, hay không làm được việc X?
- Tại sao bây giờ mà không phải 2 năm trước / 2 năm nữa? (công nghệ mới? hành vi mới? đối thủ để lộ khoảng trống? chính sách store thay đổi?)
- Positioning một dòng: "Dành cho [ai], [sản phẩm] là [category] giúp [giá trị], khác với [đối thủ] ở chỗ [khác biệt]."
- Thành công sau 6 tháng trông như thế nào — nói bằng con số nếu được, bằng trạng thái nếu chưa?

**Quality bar**:
- Problem statement names WHO hurts and WHEN — not "người dùng gặp khó khăn khi..." but a specific person in a specific moment.
- "Tại sao là lúc này" cites ≥1 external signal (download scale of category, new entrant traction, visible gap) — the template's example cites "700M+ lượt tải" category proof.
- Success criteria are qualitative-but-checkable at this level (e.g., "đạt retention giai đoạn đầu mạnh trước khi mở rộng"; exact numbers live in S5).

**Failure modes**: solution described before problem; "why now" that was equally true five years ago; market size copied from a consulting deck ($X billion TAM) instead of category-download framing the template prefers.

**Feeds**: S5 KPI, S3 personas. **Fed by**: S4 matrix (why-now evidence), S3 (problem language).

<a name="s2"></a>
## S2. Mục tiêu và Bối cảnh

**Subsections**: Mục tiêu Sản phẩm · Liên kết với Mục tiêu Kinh doanh · Nguyên tắc Sản phẩm.

**Question bank**:
- Mục tiêu sản phẩm một đoạn: ra mắt cái gì, cho ai, đến trạng thái nào?
- Công ty cần gì từ dự án này: doanh thu mới, học một category, tận dụng traffic sẵn có, lấp portfolio? (đây là "liên kết mục tiêu kinh doanh")
- 3-5 nguyên tắc sẽ dùng để phân xử tranh cãi thiết kế sau này? Mỗi nguyên tắc phải LOẠI BỎ được một lựa chọn hợp lý — nếu không loại được gì thì nó là khẩu hiệu, không phải nguyên tắc.

**Quality bar**: Nguyên tắc tốt có dạng "ưu tiên A hơn B" (template mẫu: "Ưu tiên sử dụng hằng ngày hơn là độ phức tạp chuyên sâu", "Tạo động lực nhưng không thao túng"). Test each principle: name a plausible feature it would kill. If the PO can't, sharpen it.

**Failure modes**: principles that are values-poster material ("chất lượng là trên hết"); business goals that are just product goals restated.

<a name="s3"></a>
## S3. Vấn đề Người dùng và Đối tượng Mục tiêu

**Subsections**: Persona Chính / Thứ cấp / Thứ ba (each: Profile, Context, Pain Points, Need) · Hành trình Người dùng Hiện tại · Hành trình Người dùng Mong muốn.

**Question bank**:
- Hình dung 1 người cụ thể sẽ mở app này tuần 3 lần — họ bao nhiêu tuổi, đang ở đâu lúc mở app, mở để làm gì?
- Hiện tại (không có app) họ giải quyết việc này bằng gì? Chỗ nào trong cách đó làm họ bực?
- Pain nào là pain "trả tiền được" và pain nào chỉ là phiền nhẹ?
- Persona thứ cấp khác persona chính ở nhu cầu gì — hay chỉ khác demography? (nếu chỉ khác tuổi thì gộp lại)
- Hành trình hiện tại: đi từng bước từ trigger → hành động → kết quả → cảm xúc. Bước nào gãy?
- Hành trình mong muốn: cũng các bước đó, app thay đổi bước nào? (KHÔNG phải danh sách tính năng — là trải nghiệm)

**Quality bar**:
- Each persona has a NEED phrased as an outcome ("một thói quen hằng ngày nhanh, có hướng dẫn, giảm mệt mỏi ra quyết định"), not a feature ("cần tính năng nhắc nhở").
- Personas differ by need/context, not just age bands.
- Journeys are step sequences with an explicit break point (current) and an explicit changed step (desired). If web research is possible, review mining (see research playbook) grounds pain points in real store-review language.

**Failure modes**: 3 personas that are one persona in 3 age costumes; desired journey that's a feature list; pain points the PO invented in the meeting room with zero outside signal.

**Feeds**: S7 (every feature cites a persona need), S8 (main flow = primary persona's desired journey), S10 (free tier must clear the entry pain).

<a name="s4"></a>
## S4. Phân tích Cạnh tranh

The heaviest research section — usually multiple research passes. Read `research-playbook.md` plays 1-3 before starting.

**Archetype theo CƠ CHẾ giải pháp** (pattern chuẩn từ PRD Cal AI): phân nhóm đối thủ theo cách họ giải vấn đề chứ không theo quy mô — vd thị trường calorie: *Camera-first (nhanh)* / *AI Coach (hướng dẫn)* / *Database (truyền thống)*. Mỗi archetype ghi: điểm mạnh của cơ chế, điểm cơ chế đó bỏ rơi user nào. Sản phẩm mình thường thắng bằng cách lai hai cơ chế hoặc phục vụ segment bị cơ chế thống trị bỏ rơi. Bảng giá đối thủ chuẩn 3 cột `Weekly | Monthly | Yearly` kèm link chính thức từng app; ô không có gói ghi "—".

**Subsections**: Tổng quan Thị trường (competitor archetypes A-E) · Lưu ý phương pháp luận (KEEP the estimate-labeling note — it's in the skeleton, don't delete) · Ma trận Đối thủ · Key Takeaways for PO · Bảng 1: Chỉ số Thị trường & Thương mại · Bảng 2: Chỉ số Sản phẩm & Kỹ thuật · Phụ lục IAP/release/storefront · Diễn giải nhanh cho chiến lược · Insight từ Review (yêu thích / phàn nàn / khoảng trống) · Khác biệt hóa của Chúng ta.

**Question bank**:
- Kể tên 5-8 app người dùng sẽ so sánh với chúng ta (kể cả app "không phải đối thủ trực tiếp" nhưng chiếm cùng thời gian).
- Trong đó cái nào là "tất cả trong một nhưng rối", cái nào là "cao cấp nhưng hẹp"? (template frames the market as archetypes — find this product's version of that spectrum)
- Chúng ta thắng bằng gì mà đối thủ KHÓ copy trong 6 tháng? (nếu dễ copy, đó là feature, không phải khác biệt hóa)

**Quality bar**:
- Matrix has consistent columns across competitors (see playbook for the standard column set) and every estimated number carries "(ước tính)" + basis.
- **Quy tắc "Không công bố"** (chuẩn từ mẫu ScreenTimeControl): Ghi chú Phương pháp luận nêu rõ thứ tự nguồn (quan sát trực tiếp App Store trong tháng cụ thể → website chính thức đối thủ → public market report bổ trợ) và phân hai lớp dữ liệu — rating, giá, phiên bản, app size, iOS minimum, update cadence, privacy labels là *quan sát trực tiếp*; còn DAU, revenue, retention, RPD **chỉ điền khi có tín hiệu công khai rõ, nếu không giữ nhãn "Không công bố" thay vì suy đoán**. Không phải số nào cũng được phép ước tính.
- Key takeaways are decisions-shaped ("vì X nên chúng ta nên Y"), not observations ("app A có nhiều lượt tải").
- Review insights quote or closely paraphrase real complaints — the "phàn nàn phổ biến" list is gold for S3 pain points and S6 scope.
- "Khác biệt hóa" has ≤3 items. Four+ differentiators means none.

**Failure modes**: matrix as trivia (columns nobody will use to decide anything); ignoring indirect competitors; differentiation = "đẹp hơn, nhanh hơn, rẻ hơn" (every loser says this).

<a name="s5"></a>
## S5. Tầm nhìn và Mục tiêu Sản phẩm

**Subsections**: Tuyên bố Tầm nhìn · Mục tiêu & KPI trong 6 tháng (table).

**Question bank**:
- Tầm nhìn 1 câu, dạng "Trở thành [X] [tính từ đo được] nhất để [outcome]" — template mẫu: "đơn giản nhất để xây dựng thói quen hằng ngày bền vững".
- Với từng tiêu chí thành công ở S1: con số cụ thể sau 6 tháng là bao nhiêu? Dựa trên benchmark nào?

**KPI table columns**: `Mục tiêu | KPI | Target 6 tháng | Cách đo | Baseline/Benchmark`. Typical mobile-app KPI set: D1/D7/D30 retention, trial-start rate, trial→paid conversion, crash-free sessions, store rating, DAU or WAU. Pull benchmark ranges from S4 research; when no benchmark exists, mark target "(giả định — hiệu chỉnh sau 4 tuần)".

**Quality bar**: every KPI has a measurement method the Data Analytic role can actually implement (this template's team has a dedicated DA stakeholder — the KPI table is their contract). Targets trace to a benchmark or are flagged as calibration guesses.

**Failure modes**: vanity metrics (cumulative downloads with no retention pair); targets copied from a different category's benchmarks; KPIs no one is assigned to track.

<a name="s6"></a>
## S6. Phạm vi và Những gì nằm ngoài Phạm vi

**Subsections**: Phạm vi MVP (In Scope) · Rõ ràng nằm ngoài Phạm vi MVP · Lý do.

**Question bank**:
- MVP phải chứng minh điều gì? (một câu — template mẫu: "MVP cần chứng minh retention...") Mọi thứ không phục vụ câu đó là out.
- Với từng item in-scope: nếu bỏ nó, MVP còn chứng minh được điều trên không? Nếu còn → chuyển sang out.
- Liệt kê những thứ mọi người SẼ HỎI tại sao không có — chủ động đưa vào out-of-scope kèm lý do, đỡ tranh cãi lại mỗi sprint.

**Quality bar**:
- In-scope list is 5-8 items max for a Lite PRD; each phrased as a capability, not a screen.
- Out-of-scope list is explicit and slightly uncomfortable (if nothing painful is out, scope wasn't cut).
- "Lý do" ties scope to the proof goal in one short paragraph.

**Failure modes**: out-of-scope list that's only obviously-absurd items; scope that grew during the meeting that was called to cut it; no single proof statement.

**Feeds**: S7 feature table (in-scope items decompose into features), S5 (scope must be able to move KPIs).

<a name="s7"></a>
## S7. Yêu cầu và Tính năng

**Subsections**: Bảng Tính năng MVP (table) · Gợi ý viết Acceptance Criteria · Sau MVP (Backlog định hướng) · Nhóm tính năng theo giai đoạn (Phase 2 / Phase 3).

**Feature table columns**: `# | Tính năng | Mô tả ngắn | Persona/Need phục vụ | Ưu tiên (P0/P1/P2) | Ghi chú ràng buộc`. P0 = MVP fails without it; P1 = MVP ships without it if forced; P2 = fast-follow candidate.

**Acceptance Criteria (chuẩn từ mẫu)**: hành vi phải **đo được trên thiết bị thật**, không chỉ logic nội bộ; luồng lỗi permission / subscription / cơ chế thoát khẩn cấp là **bắt buộc có AC**; feature premium phải hiển thị rõ trong onboarding VÀ settings. User story chi tiết để ở sheet ngoài, link trong Important Links.

**Question bank**:
- Decompose each in-scope capability: những gì user làm được (kể được thành hành động), không phải những gì hệ thống có.
- Với từng feature: persona nào, need nào? (không trả lời được → cắt hoặc quay lại S3)
- Ràng buộc nào từ S9 chạm feature này? (offline? sync conflict? notification opt-in?)

**Quality bar**: descriptions are outcome-level ("user tiếp tục nghe từ vị trí cũ") not implementation-level ("lưu timestamp vào UserDefaults"). Implementation details belong in linked docs (Important Links), not here — this is the alignment layer, engineers own the how. Post-MVP list exists and pulls from S6 out-of-scope items that have future intent.

**Failure modes**: feature table that's a screen inventory; P0 on everything; requirements written as UI prescriptions that handcuff the designer.

<a name="s8"></a>
## S8. Luồng Người dùng

**Subsections**: Luồng Chính · Luồng Phục hồi / Lỗi · Luồng Phụ (mỗi tính năng chính một luồng ngắn) · **Luồng Onboarding Chi tiết** (với app subscription, đây là cỗ máy conversion — viết như một sản phẩm con).

**Onboarding Chi tiết (chuẩn từ mẫu ScreenTimeControl)** — khi sản phẩm sống nhờ onboarding→paywall, S8 phải có:
- **Spec từng màn onboarding** theo format 5 trường: *Mục tiêu màn hình* (vd "xác định một mục tiêu chính để cá nhân hóa preset, copy, và weekly review") · *Câu hỏi chính* hiển thị cho user · *Lựa chọn* (đáp án cụ thể) · *Microcopy* trấn an ("Bạn vẫn có thể chỉnh lại mục tiêu này sau") · *Dữ liệu cần thu* (lựa chọn, thời gian ra quyết định, tỷ lệ bỏ ở bước này).
- **Nội dung cần cá nhân hóa**: những gì các màn sau (preset, copy, paywall, weekly review) đổi theo câu trả lời onboarding.
- **Các điểm rơi rụng cần theo dõi**: liệt kê theo hành vi ("bỏ app ngay sau intro", "từ chối permission vì lo privacy", "hoàn tất onboarding nhưng không có hành động giá trị nào trong 24h đầu").
- **Event track riêng cho onboarding**: chuỗi snake_case đủ để dựng funnel (onboarding_started → goal_selected → …_permission_prompted/granted/denied → onboarding_preview_viewed → onboarding_completed).
- **Câu hỏi onboarding hỏi người dùng** và **câu hỏi mở còn lại** tách riêng để không lẫn quyết định đã chốt với điều chưa chốt.

**Bảng "Rules & Công thức theo màn"** (pattern tốt từ PRD Cal AI — lớp còn thiếu giữa flow và engineering): sau các luồng, thêm bảng `Màn | Mô tả/hành động | Rule` chứa hành vi tất định mà dev/QA test được: timeout cụ thể ("màn loading timeout 15s"), công thức tính hiển thị nguyên văn ("Net Calories = Calories Consumed − Calories Burned"), hành vi cạnh tranh trạng thái ("user edit liên tục → lấy kết quả edit gần nhất"), rule hiệu năng gắn màn ("mở app → vào thẳng camera <5s sau splash"), rule hiển thị ("ngày được chọn in đậm, luôn hiển thị đủ 7 ngày chứa ngày đó"). Mỗi rule là một câu đo được — đây chính là nguồn viết Acceptance Criteria ở S7.

**Đánh dấu AI touchpoints**: mọi điểm trong luồng gọi AI được tag và đánh số ("AI Generate 1/2", "AI Insight 1"). Với TỪNG touchpoint, PRD phải trả lời: latency chấp nhận được + hành vi khi chậm (timeout → gì?), hành vi khi AI SAI (user sửa được không? sửa xong dữ liệu downstream cập nhật thế nào?), và chi phí/lượt có bị quota free-tier chặn không (nối S10). App AI mà không có luồng "AI trả kết quả sai" là chưa đạt — chính review đối thủ ("sai với món phức tạp → mất niềm tin") chứng minh đây là pain số một.

**Question bank**:
- Đi từ lần mở app ĐẦU TIÊN của persona chính: từng bước đến "aha moment" đầu tiên. Bao nhiêu bước? Bước nào bỏ được?
- Phiên quay lại hằng ngày trông thế nào? (thường quan trọng hơn first-run cho retention)
- Điều gì xảy ra khi: mất mạng giữa chừng, hết trial, sync conflict, user từ chối notification permission, thanh toán fail? Mỗi tình huống: user thấy gì và đường quay lại là gì?

**Quality bar**: flows are numbered step sequences (`1. User mở app → 2. ...`) with decision points marked; the main flow reaches value in ≤ the step count competitors need (check S4 review complaints about onboarding length). Recovery flows cover ít nhất: offline, permission-denied, payment-fail, và empty/first-run state. Text sequences are fine; if the PO wants diagrams, link the Figma/Miro board in Important Links rather than embedding ASCII art.

**Failure modes**: happy path only; flows that assume permissions granted; "recovery" section that just says "hiện thông báo lỗi".

<a name="s9"></a>
## S9. Ràng buộc Sản phẩm dành riêng cho Mobile

**Subsections**: Ma trận Nền tảng · Mục tiêu Hiệu năng và Độ tin cậy · Offline và Đồng bộ · Thông báo · Khả năng Trợ năng · Quyền riêng tư và Bảo mật · Mức độ Sẵn sàng Phát hành.

This section has strong defaults in the skeleton (from the team's standard: cold launch <2.0s, screen render <1.0s cached, API p95 <800ms, crash-free ≥99.5%, 44pt touch targets, Dynamic Type, VoiceOver, opt-in daily reminders max 1/day, re-engagement only after 3+ days inactive, in-app account deletion if accounts exist). Workflow: walk the defaults with the PO and ADJUST rather than brainstorm from blank.

**Question bank (only where defaults may not fit)**:
- Platform: iOS trước hay cả hai? Min version? iPad? Landscape?
- Có nội dung nào phải xin bản quyền/legal review trước khi ship? (template flags content licensing)
- Offline: những gì bắt buộc dùng được offline? Sync conflict giải quyết kiểu gì (latest-write-wins hay server-authoritative)? — template default: user content = latest-write-wins; progress/streak = server quyết để chống lạm dụng.
- Dữ liệu cá nhân tối thiểu là gì cho app này? Đăng nhập bắt buộc hay optional?

**Quality bar**: every number is a testable gate the Tester role can verify pre-launch; the "Mức độ Sẵn sàng Phát hành" list names concrete QA coverage (offline mode, reminder opt-in, subscription + restore purchases).

<a name="s10"></a>
## S10. Kiếm tiền

**Subsections**: Mô hình Doanh thu · Gói Miễn phí · Gói Premium · Khuyến nghị Định giá · Cơ sở Định giá.

**Question bank**:
- Mô hình: freemium+subscription (team default), paid, ads, hybrid? Tại sao mô hình này khớp hành vi sử dụng của persona chính?
- Ranh giới free/premium: free phải đủ để user THÀNH THÓI QUEN (không thì không có ai để convert); premium bán chiều sâu gì?
- Neo giá của đối thủ (từ S4 Phụ lục IAP): weekly và annual của từng đối thủ?
- Trial bao nhiêu ngày? (team default 3 ngày — hợp với app thói quen, đủ 2-3 phiên giá trị)

**Quality bar**:
- Free tier is listed feature-by-feature; each premium feature answers "vì sao đáng tiền" in one clause.
- Pricing gives ranges anchored to the S4 appendix (template pattern: "mức neo của đối thủ quanh $59.99/năm → gia nhập bằng hoặc thấp hơn"), states weekly AND annual, and articulates the basis in prose.
- Consistency check with S2 principles (e.g., "giá trị subscription mang tính bổ sung, không ép buộc" forbids paywalling the core habit loop).

**Failure modes**: free tier so crippled the app can't demonstrate value; pricing picked by gut with no anchor; premium list that's just "mọi thứ nhiều hơn".

**Pattern hybrid ads-to-extend** (từ PRD Cal AI): free tier có quota tính năng AI đắt tiền ("2 lượt scan/ngày") + xem ads để mở thêm lượt — vừa chặn chi phí AI, vừa tạo đường doanh thu phụ, vừa giữ đường trải nghiệm giá trị cho user chưa trả. Khi dùng pattern này, quality bar: **quota là số chính xác kèm chu kỳ reset** ("2 lượt/ngày, reset 0h" — không viết "2-3 lần"), ghi rõ số lượt ads-extend tối đa, và đối chiếu chi phí AI/lượt ở Cấu trúc Chi phí.

## Anti-patterns từ PRD thực tế (skill PHẢI chặn — mục tiêu: đầu ra vượt mẫu)

Rút từ việc mổ xẻ các PRD đã hoàn thành của team. Khi viết hoặc review PRD, quét danh sách này; vi phạm nào cũng chặn ở Cổng Chất lượng:

1. **Section rỗng đội lốt hoàn thành** — heading "Giải pháp" tồn tại nhưng không có nội dung, người đọc lướt tưởng đã viết. Sweep trước export: mọi heading phải có nội dung hoặc bị xóa/đánh dấu _TBD_.
2. **Bảng quan trọng dạng ảnh chụp sheet** ("Click the image to view the sheet") — Ma trận đối thủ, KPI, Bảng tính năng dán ảnh: không tìm kiếm được, không diff được, chết khi sheet nguồn đổi, export hỏng. Quy tắc: bảng quyết định (matrix, KPI, feature, pricing) phải là bảng thật trong tài liệu; sheet ngoài chỉ là nguồn dữ liệu, link ở Important Links.
3. **Flow chỉ có ảnh diagram** — không có chuỗi bước đánh số dạng text thì ux-wireframe-builder không đếm được màn hình và không ai review được nhánh thiếu. Ảnh là minh họa, text là hợp đồng.
4. **Bullet-fragment thay câu** — chuỗi bullet một-hai từ lồng nhau ("User: / Có thể sẵn sàng trả…") làm mất chủ ngữ và mập mờ ai khẳng định gì. Mỗi nhận định là câu hoàn chỉnh.
5. **Số không nguồn** — "20k-700k lượt tải" trơ trọi không nhãn (ước tính? nguồn? ngày?). Mọi số vào Bảng Bằng chứng hoặc mang nhãn (ước tính)/(Không công bố).
6. **Persona không đạt chuẩn 6 tiêu chí** — persona chỉ là dải tuổi + danh sách mối quan tâm, không tên, không bối cảnh, không viết từ góc nhìn persona. Persona trong PRD phải đạt chuẩn `ux-persona-journey` (6 tiêu chí) hoặc dán nhãn [GIẢ ĐỊNH] chờ nghiên cứu.
7. **Embed chết** — "[This type of content is unavailable...]" cho wireframe. Nội dung không nhúng được thì để link + một dòng mô tả nội dung link.
8. **App camera/AI thiếu luồng permission và luồng AI-thất-bại** — xin quyền camera/photo nằm ngay luồng chính mà không có nhánh từ chối; không có hành vi khi AI sai/chậm.

<a name="full-mode"></a>
## Full mode: các section mở rộng (theo mẫu chuẩn ScreenTimeControl, 16 section)

Ở Full mode, thứ tự sample chuẩn: S1-S9 như trên → **10. Danh sách Màn hình** → 11. Kiếm tiền (nội dung như S10 ở trên) → **12. Chỉ số Thành công và Analytics** → **13. Giả định, Phụ thuộc, Rủi ro** → **14. Câu hỏi Mở** → **15. Điều phối Triển khai** → **16. Phụ lục**. Lite mode có thể bỏ 12-15 và rút gọn 16.

### Danh sách Màn hình
Bảng `# | Tên màn hình | Mô tả | Ưu tiên (P0/P1) | Phụ thuộc` — mô tả một dòng ("Màn hình can thiệp trước khi mở app"), phụ thuộc ghi hệ thống/permission ("Screen Time permission", "Rule engine", "Billing"). Đây là cầu nối trực tiếp sang `ux-wireframe-builder`: danh sách này là Happy-Path inventory sơ khởi; wireframe-builder sẽ nở nó ra với Decision/Data States. Quality bar: mỗi màn khớp ≥1 luồng ở S8, và các màn bắt buộc của app freemium (Paywall với restore purchase, Permission Setup) phải có mặt.

### Chỉ số Thành công và Analytics
Subsections: Định nghĩa KPI (công thức đo, không chỉ tên) · **Sự kiện Cốt lõi** · Dashboard cần theo dõi. Event taxonomy là bảng `Event | Trigger | Mục đích` với tên snake_case; mục đích gắn vào tầng phân tích (DAU/session, funnel conversion, core behavior, activation, engagement, habit loop, product efficacy, monetization funnel, revenue, quality, stability). Quality bar: mỗi KPI ở S5 có ít nhất một event đo được nó; luôn có error_occurred + crash_occurred; event onboarding tách riêng ở S8.

### Giả định, Phụ thuộc, Rủi ro
Giả định chính (những gì tin là đúng nhưng chưa kiểm chứng — mỗi cái nối tới cách kiểm chứng) · Phụ thuộc (API hệ điều hành, entitlement, dịch vụ bên thứ ba, quyết định pending) · Rủi ro + Hướng Giảm thiểu (bảng: rủi ro / xác suất / tác động / mitigation). Failure mode: rủi ro chung chung ("cạnh tranh cao") không kèm mitigation cụ thể.

### Câu hỏi Mở
Danh sách những điều PO chưa quyết — mỗi câu hỏi ghi ai quyết và deadline nếu có. Đây là nơi status board [DRAFT] items trỏ về.

### Điều phối Triển khai
Các mốc đề xuất (milestone gắn tuần/tháng) · Timeline trực quan (tùy chọn — bảng hoặc link). Nối với PRD dependency: milestone đầu thường là "PRD sign-off + design kickoff".

### Phụ lục (governance — điểm mạnh nhất của mẫu)
- **Nguồn Nghiên cứu**: URL đánh số, dùng lại được cho Bảng Bằng chứng.
- **Thuật ngữ**: chỉ những từ mà stakeholder không phải PM có thể hiểu sai.
- **Nhật ký Thay đổi**: khớp Version History đầu file.
- **Bảng Bằng chứng**: `Nhận định | Source URL | Date | Độ tin cậy (High/Med/Low)` — mọi nhận định định lượng trong PRD (screen time trung bình, market size, CAGR…) phải có một dòng ở đây. Market report public mặc định Low trừ khi có nguồn thứ hai xác nhận.
- **Cổng Chất lượng PRD** — checklist Pass/Fail trước khi bàn giao, 5 cổng: **Core-8 Completeness** (8 section lõi S1-S8 đủ và không placeholder) · **Evidence Quality** (mọi số có nhãn nguồn/ước tính/Không công bố) · **Mobile-Specific Coverage** (S9 đủ offline/notification/a11y/privacy/release readiness) · **Scope Clarity** (in/out/lý do rõ, MVP khớp story map P0) · **Metrics Readiness** (KPI ↔ event đối chiếu được). Cổng nào Fail → ghi vào Vướng mắc.
- **Vướng mắc**: những gì còn thiếu và VÌ SAO (vd "chưa có nguồn công khai đáng tin cho DAU/revenue của 5 đối thủ", "persona dựa trên review + market inference, chưa có user interview trực tiếp").
- **Điều chỉnh Bắt buộc**: việc phải làm nếu muốn nâng PRD lên mức sâu hơn; nếu baseline đã đủ, ghi rõ "đủ điều kiện chuyển bước tiếp theo nếu PO chấp thuận".
- **Tóm tắt Bàn giao**: file đã cập nhật · chế độ (Lite/Standard/Full/Strict) · số đối thủ đã phân tích · số nguồn đã rà · số giả định đang mở · hành động tiếp theo được khuyến nghị.

<a name="meeting-notes"></a>
## Meeting Notes

Template ends with dated meeting blocks (`**Meeting DD-MM-YYYY**` + Thành phần + decisions). Append one per review meeting. Decisions recorded here that change the PRD also get a Version History row — the notes are the why, the history is the what.
