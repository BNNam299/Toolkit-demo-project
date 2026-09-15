<!-- PROVENANCE — do build script sinh, KHÔNG sửa tay
nguồn      : onboarding-scenario-selector.skill  →  references/scenarios.md
nhập ngày  : 2026-08-09
trạng thái : chép nguyên văn, không tóm tắt, không diễn giải
cập nhật   : xuất lại file .skill từ Claude rồi chạy lại build script
-->

# Bộ 8 kịch bản Onboarding + Paywall — Chi tiết đầy đủ

Nguồn: tài liệu team "Hướng dẫn tạo các kịch bản Onboarding và Paywall cho Mobile App".
Mỗi kịch bản gồm: mô tả, app phù hợp, khi nào KHÔNG dùng, app trong portfolio nên cân nhắc, target, request cho Product/Design/Dev, events bắt buộc, kill rule, wireframe luồng.

---

## KB1 — Direct Outcome Paywall

Bán sớm bằng outcome rõ ràng sau 2-3 màn onboarding ngắn.

**App phù hợp:** intent đầu vào mạnh, pain rõ, user hiểu việc cần làm trước khi mở app. App không cần output visual phức tạp trước khi user quyết định trial. User thường đến từ keyword/creative rất trực tiếp hoặc tình huống cần giải quyết ngay.

**Không phù hợp khi:** user cần nhìn thấy kết quả thật mới tin; app có nguy cơ bị xem là bait-and-switch; D1 cancel/refund đang cao.

**Portfolio nên cân nhắc:** SmartClean AI (traffic "clean storage/duplicate photos"), PDF Scanner (export/OCR), TV Remote (điều khiển ngay), WiFinder (tìm/kết nối WiFi), GPS Map Camera (timestamp ngay), Email AI (unified inbox/AI reply nhanh).

**Target:** Install → Paywall View >70% · Paywall View → Trial 4-8% · D1 cancel <25-30%.

**Request Product/Design/Dev:** Onboarding 2-3 màn, mỗi màn chỉ 1 message. Paywall có headline outcome, 3 benefit bullets, 2-3 plan, CTA trial rõ. Không đưa câu hỏi profiling dài.

**Events bắt buộc:** `onboarding_start`, `onboarding_screen_view`, `paywall_view{placement:onboarding_end}`, `trial_start`, `premium_activation`.

**Kill rule:** tắt nếu trial tăng nhưng D1 cancel >35%, refund tăng, hoặc review nhắc bị ép mua.

**Wireframe luồng:**
```
Splash [Logo, Loading..., no ad trước ONB]
→ Welcome [Solve your problem in seconds] [Continue]
→ Benefit [✓ Fast result ✓ Safe action ✓ Save time] [Continue]
→ Paywall [Unlock full access, 3 benefits, plan cards] [Start trial]
→ Activation [Premium unlocked, Do first action now] [Start]
```

---

## KB2 — Aha Before Paywall / Result Unlock

Cho user thấy preview/partial result trước khi khóa full output bằng paywall.

**App phù hợp:** value mạnh nhất là kết quả nhìn thấy được: ảnh before/after, AI output, scan preview, phân tích kết quả, dung lượng có thể giải phóng. User không tin text promise, nhưng sẽ trial khi thấy app tạo được kết quả liên quan đến dữ liệu thật của họ.

**Không phù hợp khi:** cost mỗi preview quá cao mà chưa có cơ chế giới hạn; output hiện tại chưa đủ đẹp/ổn định.

**Portfolio nên cân nhắc:** HomeMagic AI Interior, FacePlus, AI Photo Maker/MagicArt, AR Drawing, PDFPro Scanner, SmartClean AI scan storage, Calora AI food scan, Horoscope/Tarot nếu có reading preview cá nhân hóa.

**Target:** First result view >35-50% · Result → Trial >8-12% · Trial-to-paid >30%.

**Request Product/Design/Dev:** cho 1 preview low-res/blur/watermark. Gate: Save HD, Export, Regenerate, More styles, Batch, Full reading, Detailed plan. Paywall xuất hiện khi user chạm CTA có intent cao.

**Events bắt buộc:** `input_success`, `generate_start`, `generate_success`, `result_view`, `result_cta_click`, `paywall_view{trigger:save_hd/regenerate}`, `trial_start`.

**Kill rule:** tắt nếu user complain "pay before result", result fail rate >5%, hoặc output làm trial thấp hơn direct variant.

**Wireframe luồng:**
```
Welcome [Create your result from your input] [Continue]
→ Input [Upload / Scan, Choose style/type] [Generate]
→ Loading [Analyzing... Creating preview... Progress 72%]
→ Preview [Low-res result] [Save HD] [More styles] [Unlock]
→ Paywall [Unlock full result, HD + unlimited] [Start trial]
```

---

## KB3 — Personalized Intent Paywall

Dùng 1 câu hỏi intent để đổi headline, benefit và visual của paywall.

**App phù hợp:** app có nhiều use case, nhiều persona, nhiều lý do mua. Nếu cùng một paywall đang phải bán cho user rất khác nhau, personalization thường tăng relevance và trial.

**Không phù hợp khi:** app chỉ có 1 use case rất rõ, hoặc traffic chưa đủ lớn để đọc từng segment.

**Portfolio nên cân nhắc:** HomeMagic theo room/goal/style; Cleaner theo photos/videos/junk; AI Tutor theo speaking/job/travel/exam; Calora theo lose/gain/maintain; Quran theo read/prayer/qibla/azkar; Horoscope theo love/career/family; Email AI theo all inbox/reply/grammar/signature.

**Target:** Paywall View → Trial +15-30% · intent question drop <20%.

**Request Product/Design/Dev:** chỉ hỏi 1 câu trong onboarding, 3-5 lựa chọn, có skip. Mapping paywall headline + first benefit theo answer. Event answer bắt buộc gửi vào paywall property.

**Events bắt buộc:** `onboarding_answer{question_id,answer_value}`, `paywall_view{intent_segment}`, `trial_start{intent_segment}`.

**Kill rule:** tắt nếu drop tại intent screen >20% hoặc personalization không tạo uplift sau đủ sample.

**Wireframe luồng:**
```
Welcome [What do you want to improve today?] [Continue]
→ Intent [Choose goal: (·)A (·)B (·)C] [Skip]
→ Value [Personalized benefit for A/B/C] [Continue]
→ Paywall [Headline = intent, Benefits = intent, Visual = intent] [Trial]
```

---

## KB4 — Progress Loading + Value Build

Biến thời gian loading/setup thành màn tăng trust và perceived value.

**App phù hợp:** app có AI generation, scan, analyze, backup, import dữ liệu hoặc xử lý cần vài giây. User đang chờ nên attention cao; nếu loading trống, user thấy chậm. Nếu loading có step cụ thể, user cảm thấy app đang làm việc thật.

**Không phù hợp khi:** loading giả quá dài, claim vượt quá khả năng product, hoặc app cần action tức thì không nên delay.

**Portfolio nên cân nhắc:** HomeMagic, AI Photo, FacePlus, AR Drawing photo-to-sketch, SmartClean scan, PDF scan/OCR, Calora food analysis, Horoscope personalized reading, AI Tutor level analysis.

**Target:** Loading completion >85% · Paywall CVR +10-20% · generate fail <3-5%.

**Request Product/Design/Dev:** loading 5-12s có 3-4 step. Step phải khớp task thật. Nếu lỗi, không show paywall ngay sau lỗi; cần retry hoặc free compensation.

**Events bắt buộc:** `loading_start`, `loading_step_view`, `loading_complete`, `generate_time`, `generate_fail`, `paywall_view_after_loading`.

**Kill rule:** tắt nếu loading drop >15%, session time giảm, hoặc support/review nói app fake loading.

**Wireframe luồng:**
```
Input done [Your request is ready] [Start]
→ Loading 1 [Analyzing... ▓▓▓▓░░░░ Step 1/4]
→ Loading 2 [Matching... ▓▓▓▓▓▓░░ Step 3/4]
→ Paywall/Preview [Result is ready, Unlock full access] [Trial]
```

---

## KB5 — Trial-first Risk-free Paywall

Paywall tập trung vào dùng thử, giảm cảm giác rủi ro cho traffic broad/social.

**App phù hợp:** user low/mid intent, đến từ Meta/TikTok/Google broad, chưa có nhu cầu đủ rõ hoặc còn sợ subscription. App cần thời gian để user trải nghiệm value nhiều lần trước khi paid.

**Không phù hợp khi:** trial cancel đang rất cao, app chỉ có one-time use, hoặc giá sau trial gây sốc.

**Portfolio nên cân nhắc:** AI Tutor, Calora, Quran, Horoscope/Tarot, HomeMagic từ social creative, AI Photo từ viral creative, Cleaner ở market trial thấp, Email AI với user chưa có pain mạnh.

**Target:** Paywall View → Trial +20-40% · Trial-to-paid không dưới 25% · D1 cancel <30-35%.

**Request Product/Design/Dev:** CTA "Start 3-day free trial" hoặc "Try free today". Có timeline trial: Today unlock, Day 2 reminder, Day 3 renew. Legal clarity gần CTA.

**Events bắt buộc:** `paywall_view{offer:trial_first}`, `trial_start`, `activation_checklist_start`, `activation_complete`, `trial_cancel`.

**Kill rule:** tắt nếu trial-to-paid giảm dưới 25% hoặc D1 cancel tăng >35%.

**Wireframe luồng:**
```
Value [Try premium with no risk, Cancel anytime]
→ Paywall [3-day free trial, Today: full access, Then: price] [Start trial]
→ Activation [Trial started, Complete first win] [Use premium]
```

---

## KB6 — No Trial / Direct Purchase for High Intent

Loại trial ở segment intent cao để tăng D0 cash và giảm cancel noise.

**App phù hợp:** user đến từ keyword/creative có nhu cầu gấp, app giải quyết việc ngay, giá thấp/weekly hợp lý, và lịch sử trial cancel cao vì user dùng xong rồi hủy. CHỈ nên apply theo source/geo/keyword, không rollout global.

**Không phù hợp khi:** app cần thời gian chứng minh value, app có giá cao, hoặc traffic broad/social.

**Portfolio nên cân nhắc:** PDF export/OCR từ ASA keyword, Cleaner one-tap clean từ keyword "storage full", TV Remote urgent intent, GPS Map Camera work-use, Scanner urgent document, một số gói credit AI output nếu user đã thấy preview.

**Target:** D0 revenue/install tăng · refund <5-8% · purchase success >25-35% tùy giá.

**Request Product/Design/Dev:** A/B by source: Trial vs No trial. No-trial paywall cần price clarity mạnh, refund guardrail sát, không dùng urgency fake.

**Events bắt buộc:** `paywall_view{offer:no_trial,source}`, `purchase_sheet_open`, `purchase_success`, `refund`.

**Kill rule:** tắt nếu refund/review xấu tăng hoặc D7 net revenue không vượt trial variant.

**Wireframe luồng:**
```
Intent hit [You need this now, Unlock to continue] [Continue]
→ Paywall [Unlock premium, Weekly/Monthly, no trial] [Continue]
→ Purchase [Store sheet → Success → First action]
```

---

## KB7 — Downsell After Close

Khi user close paywall, show offer mềm hơn hoặc plan ngắn hơn với frequency cap.

**App phù hợp:** Paywall View cao nhưng Trial/Purchase thấp. User có thể không ghét app mà chỉ chưa sẵn sàng với gói chính, giá cao hoặc commitment dài. Dùng tốt cho market nhạy giá hoặc paywall annual-first.

**Không phù hợp khi:** app đã có review xấu về spam popup, hoặc paywall close là do product chưa có value chứ không phải giá/commitment.

**Portfolio nên cân nhắc:** HomeMagic annual-first, AI Photo/Face premium, Calora annual plan, Quran subscription, Horoscope/Tarot, Cleaner ở price-sensitive geo, Email AI, AI Tutor.

**Target:** Incremental trial/purchase +5-15% · không tăng rage close/review xấu.

**Request Product/Design/Dev:** chỉ show 1 lần/session, tối đa 2 lần/tuần. Downsell có thể là monthly/weekly, cheaper intro, hoặc "try 3 days". Không lặp popup ngay lập tức nhiều lần.

**Events bắt buộc:** `paywall_close`, `downsell_view`, `downsell_accept`, `downsell_decline`, `trial_start{source:downsell}`.

**Kill rule:** tắt nếu close rate tăng, session length giảm, hoặc complaint về spam/price tăng.

**Wireframe luồng:**
```
Main paywall [Annual highlighted] [Start trial] [X]
→ Close intent [Wait... Not ready? Try smaller plan]
→ Downsell [Start smaller, Weekly/Monthly] [Continue] [No thanks]
```

---

## KB8 — Permission-led Setup Paywall

Đưa permission/setup vào đúng thời điểm để user hiểu vì sao cần quyền trước khi thấy paywall.

**App phù hợp:** app cần quyền nhạy cảm như ảnh, camera, location, notification, contacts, email account, calendar, file access. Nếu xin quyền quá sớm, user deny rồi không còn trải nghiệm value; nếu xin sau khi giải thích outcome, acceptance tăng và paywall không bị nghi ngờ.

**Không phù hợp khi:** app không có permission friction hoặc permission không ảnh hưởng core value đầu tiên.

**Portfolio nên cân nhắc:** SmartClean AI cần Photos; HomeMagic/AI Photo/Face/AR Drawing cần Photos/Camera; GPS Map Camera cần Location/Camera; WiFinder cần Location; Email AI cần account permission; Quran/Calora cần notification; Scanner cần camera/files.

**Target:** Permission accept +15-30% · Aha reach tăng · Paywall view không giảm.

**Request Product/Design/Dev:** màn pre-permission giải thích benefit trước system permission. Nếu deny, có fallback demo/sample để vẫn dẫn user tới value/paywall nhẹ.

**Events bắt buộc:** `pre_permission_view`, `permission_prompt`, `permission_accept`, `permission_deny`, `fallback_demo_view`, `paywall_view`.

**Kill rule:** tắt nếu permission screen drop >20% hoặc deny users không có fallback.

**Wireframe luồng:**
```
Intent [What do you want? (·)Option A] [Continue]
→ Pre-permission [Allow access to create your result] [Allow]
→ System dialog [iOS permission: Allow / Deny]
→ Fallback/Aha [Nếu allow: real data · Nếu deny: sample demo] [Continue]
→ Paywall [Unlock full use] [Trial]
```

---

## Quy trình nghiên cứu thị trường theo quốc gia

Khi cần làm paywall cho một thị trường cụ thể (ví dụ: Cleaner AI cho Brazil):

1. Lên **AppStoreSpy** tìm Top 5 đối thủ cùng dòng tại quốc gia đó
2. Vào **Sensor Tower Pro** tìm 5 app tại quốc gia: gói giá IAP nào đang bán, offer nào tốt nhất, nội dung IAP/màn paywall của 5 app
3. Cho AI học bộ dữ liệu (gói giá + paywall) → sinh ra các màn paywall bản địa hóa cho quốc gia đó
4. Mỗi quốc gia sinh đủ **8 kịch bản onboarding** theo mẫu trên để đội UA có kho biến thể test

Ghi nhớ: nghiên cứu đối thủ quyết định GIÁ + OFFER; chẩn đoán app/traffic quyết định KỊCH BẢN LUỒNG. Hai việc độc lập, làm cả hai.
