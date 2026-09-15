<!-- PROVENANCE — do build script sinh, KHÔNG sửa tay
nguồn      : prd-builder.skill  →  references/research-playbook.md
nhập ngày  : 2026-08-09
trạng thái : chép nguyên văn, không tóm tắt, không diễn giải
cập nhật   : xuất lại file .skill từ Claude rồi chạy lại build script
-->

# Research Playbook — Multi-Angle Evidence Gathering

The PRD's credibility rests on its research. This playbook defines repeatable "plays". Before any play: check whether web search is available. With it, gather live data. Without it, produce knowledge-cutoff-dated analysis, say so plainly, and tag items `[RESEARCH: verify with live data]`.

**Two invariants (from the template's own methodology note):**
1. Apple/Google do not publish DAU, retention, sessions, engagement, IAP revenue, or RPD. Any such figure is an inference → write "(ước tính)" + the inference basis. Purpose is **so sánh tương đối để ra quyết định sản phẩm**, not financial forecasting.
2. Every external fact lands in `research_log.md` first: `| date | fact | source | confidence |`. The PRD cites from the log.

## Play 1 — Competitor Matrix (Ma trận Đối thủ)

1. **Enumerate**: 5-8 apps across the spectrum — category leaders, focused newcomers with traction, and 1-2 indirect competitors (different category, same user time/money). Sources: App Store/Google Play search + category charts, "best X apps" listicles, Reddit threads asking for recommendations.
2. **Archetype**: cluster them into 3-5 mô thức (the template's Tổng quan expects archetypes A-E, e.g., "tất cả trong một nhưng rối" vs "cao cấp nhưng hẹp"). The archetypes, not the individual apps, reveal the gap.
3. **Standard matrix columns** (keep consistent across all rows):
   `App | Mô thức | Lượt tải/ratings công bố | Giá (weekly/annual) | Free tier | Tính năng đinh | Điểm mạnh | Điểm yếu | Cập nhật gần nhất`
4. **Bảng 1 (Thị trường & Thương mại)**: downloads/installs claimed, rating count & average, price points, subscription model, estimated revenue tier (ước tính — basis: rating volume × category conversion norms).
5. **Bảng 2 (Sản phẩm & Kỹ thuật)**: platform coverage, offline support, account requirement, onboarding length (steps to value), notification behavior, app size, min OS.
6. **Phụ lục IAP/release**: exact IAP SKUs and prices from store listings, release cadence (dates of last 5 updates → updates/month), storefront notes (featured placements, seasonal events).

**Inference bases you may use for ước tính** (state which one): rating count as download proxy (typical 0.5-2% of downloads leave ratings, category-dependent); rank-to-download curves; claimed figures in press/store descriptions; team size from LinkedIn; update cadence as investment signal.

## Play 2 — Review Mining (Insight từ Review)

The highest-value play per hour spent. Feeds S4 insights, S3 pain points, S6 scope, S8 onboarding-length target.

1. For the top 3-4 competitors, read 1-star/2-star reviews AND 5-star reviews (recent first, ~20-30 each if searchable; otherwise aggregate reports and Reddit complaint threads).
2. Bucket into the template's three lists:
   - **Điều người dùng yêu thích** — what to preserve/match (table stakes).
   - **Phàn nàn phổ biến** — recurring, cross-app complaints are the opportunity list. Quote or closely paraphrase; real user language beats abstraction ("app bắt đăng nhập mới đọc được" > "friction trong onboarding").
   - **Khoảng trống cơ hội** — needs no competitor serves, visible when the same wish appears in reviews of multiple apps.
3. Cross-check S3: does each persona pain point appear in real review language? Pain points with zero outside signal get flagged `⚠ Giả định cần kiểm chứng`.

## Play 3 — Market Sizing (Market Size Framing)

The template deliberately uses **category-download framing**, not TAM dollars: "các sản phẩm dẫn đầu ghi nhận 20M-700M lượt tải/cài đặt cùng lượng đánh giá lớn, cho thấy nhu cầu bền vững". Follow that style:

1. Sum/observe download scale of the top 3-5 category apps (claimed figures, store rating counts as floor).
2. Note trajectory: are new entrants still gaining installs? (proof the category isn't sealed)
3. Note geography/language splits if relevant to positioning (e.g., localization gaps = entry wedge).
4. One sentence, evidence-first, no "$X billion by 2030" consultant numbers unless the PO explicitly wants them — and then labeled with the source and its methodology.

## Play 4 — Pricing Benchmark (Cơ sở Định giá)

1. From Play 1's IAP appendix, build the anchor set: weekly and annual price of each competitor, trial length, intro offers.
2. Identify the gravity point (template example: "mức neo tập trung quanh $59.99/năm").
3. Recommend a range, positioned deliberately: at-anchor (parity), under-anchor (conversion play — but not so low it signals low quality; the template warns about "tín hiệu chất lượng thấp"), or above-anchor (requires a premium story the S4 matrix supports).
4. Sanity-check trial length against time-to-value from S8 (trial must contain ≥2 value moments).

## Play 5 — Why-Now Analysis (Tại sao là lúc này)

Strong why-now = ≥1 of these, with evidence:
- **Behavior shift**: usage pattern newly mainstream (cite adoption signal).
- **Technology unlock**: something recently became cheap/possible (on-device AI, new OS API, ASR quality...).
- **Competitive signal**: new focused entrants gaining traction fast = demand outrunning incumbents (template: "các đối thủ mới cho thấy nhu cầu rõ ràng với các phân khúc tập trung hơn").
- **Distribution window**: store policy change, new surface (widgets, lock screen), platform featuring appetite.
- **Gap persistence**: the archetype spectrum from Play 1 shows an unoccupied middle (template: "khoảng trống giữa nhóm 'tất cả trong một nhưng rối' và nhóm 'cao cấp nhưng hẹp'").

Test: would this statement have been equally true 3 years ago? If yes, it's not a why-now.

## Play 6 — KPI Benchmarks

For S5 targets, gather category norms: D1/D7/D30 retention ranges, trial-start and trial→paid conversion norms for the model chosen in S10, typical rating trajectories. Sources: published industry benchmark reports (Adjust, AppsFlyer, RevenueCat state-of-subscription — name which), public postmortems, founder threads. Every target row in the KPI table cites its benchmark or is marked "(giả định — hiệu chỉnh sau 4 tuần)".

## Presenting research to the PO

- Lead with the decision the research informs, then the evidence — never a data dump.
- Mark confidence per claim: ✅ verified (primary source) · ~ ước tính (basis stated) · ⚠ weak signal.
- Disagreements between sources are findings, not noise — surface them.
- After each play, propose the 2-3 sentences that should enter the PRD, and let the PO react before committing.
