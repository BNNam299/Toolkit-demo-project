---
name: project-docs-prd
description: Create PRD.md through interactive discovery and market research. Use when creating PRD, conducting market analysis, defining product strategy.
allowed-tools:
  - Read
  - Write
  - Edit
  - Grep
  - Glob
  - WebSearch
  - WebFetch
skills:
  - project-docs-lifecycle
  - project-docs-contract
  - project-docs-quality-gates
---


# Create PRD.md

## Objective

Create a PRD.md through interactive discovery and market research. Every claim must be backed by verifiable sources. No fabricated data.

## Default Output Language

- Default all user-facing output to **Vietnamese with full diacritics**.
- Write discovery questions, research synthesis, PRD content, evidence summaries, and handoff notes in **natural Vietnamese with diacritics**.
- Keep source URLs, product names, platform names, technical keywords, metric acronyms, and exact quoted text in their original form when needed.
- Do not default to ASCII-only Vietnamese unless the user explicitly requests it.
- If a template contains mixed English/Vietnamese labels, preserve the template structure but fill the content in **Vietnamese with diacritics** by default.

## Phase 1: Discovery

Ask the user these 5 questions. **Wait for all answers before proceeding.**

### Option A: User Knows Their Goals (Default)
If the user has clear answers, ask:

1. **Target users** who are they and what do they care about?
2. **Problem** what pain point are you solving?
3. **Core action** what is the one thing users must accomplish?
4. **Success metrics** how will you know this worked?
5. **Similar apps** what existing apps do you admire or compete with?

### Option B: User Needs AI-Assisted Discovery (Optional)
**If the user is unsure or hasn't defined their goals**, offer this option:

```
You mentioned you're not sure about the specifics. 
Would you like me to suggest a direction based on:
- Global market opportunities in [broad category if mentioned]
- High-potential IAP (In-App Purchase) business models
- Proven app categories with strong monetization

I can research and propose:
✓ Target user segments with highest LTV (Lifetime Value)
✓ Problem spaces with unmet demand
✓ Core actions that drive engagement + revenue
✓ Success metrics tied to IAP conversion
✓ Similar successful apps with strong monetization

Would you like me to proceed with AI-assisted discovery? [Yes/No]
```

**If user selects "Yes":**
1. Use `WebSearch` to identify high-opportunity app categories
2. Focus on: Global markets (US, EU, APAC), IAP-friendly niches
3. Propose 2-3 specific directions with:
   - Target user persona + demographics
   - Problem statement + market gap
   - Core action + engagement loop
   - IAP monetization strategy
   - 2-3 successful competitor examples
4. Present options and let user choose
5. **Then proceed to Phase 2** with the selected direction

**If user selects "No":**
- Ask them to clarify at least the broad category
- Or suggest postponing PRD creation until goals are clearer

### Discovery Rules
- **Option A**: Wait for user answers. Do not guess.
- **Option B**: Research first, propose options, let user choose.
- Do not skip ahead. The direction (user-defined or AI-proposed) drives everything that follows.

## Phase 2: Comprehensive Market Research

**Objective**: Gather rich competitive intelligence from minimum 10-20 distinct sources across multiple channels.
**Priority: use https://lite.duckduckgo.com/lite/
### Research Strategy (Parallel Execution)

Execute searches across ALL these channels. Do NOT stop at first results.

#### 2.1 Academic & Industry Reports (2-4 sources)
**Priority: Data from January 2025 to current month 2026**
- Use `WebSearch` with queries like:
  - `"[product category] market analysis 2025" OR "[product category] market analysis 2026" filetype:pdf`
  - `"[product category] trends 2025" OR "[product category] trends 2026" site:mcKinsey.com OR site:deloitte.com OR site:pwc.com`
  - `"[competitor name]" report 2025 OR 2026 site:statista.com`
  - `"mobile app trends [category]" after:2024-12-31`
- Target: Industry whitepapers, research reports, trend analyses
- **Filter**: ONLY use sources from 2025 to current month 2026; exclude older data unless absolutely necessary
- **Note publication dates**: Always record exact publication date in Evidence Table
- **Date validation**: Check PDF metadata or article date to confirm data is from 2025 or 2026

#### 2.2 News & Tech Blogs (3-5 sources)
**Priority: Data from January 2025 to current month 2026 ONLY**
- Use `WebSearch` with strict time filters:
  - `"[competitor] app review" site:techcrunch.com OR site:theverge.com after:2024-12-31`
  - `"[competitor] funding" OR "[competitor] launch" after:2024-12-31`
  - `"[problem space] startup" site:producthunt.com after:2024-12-31`
  - `"[category] apps comparison" after:2024-12-31`
  - `"[category] market trends" 2025 OR 2026`
- Use `WebFetch` on promising URLs
- **Date verification**: Check article publication date before using
- **Exclusion**: Reject articles from 2024 or earlier unless critical historical context
- **Note**: Articles must be dated between 2025-01-01 and current month 2026

#### 2.3 Market Intelligence Platforms (REQUIRED)

**Use these platforms to research the market and category before identifying competitors:**

**Public Intelligence Platforms** (REQUIRED - minimum 3 platforms):

| Platform | Data Available | Access Method | Recency |
|----------|---------------|---------------|---------|
| **Sensor Tower** | Blog posts, reports, market indices, download/revenue estimates, ad performance insights | `WebSearch`: `site:sensortower.com "[app name]" OR "[category] market" after:2024` | Reports from 2025-2026 |
| **AppMagic** | Public top charts, live store rankings, market research reports | `WebSearch`: `site:appmagic.com top charts "[category]" 2025` | Live rankings + 2025-2026 reports |
| **Apptopia** | Public top charts, trending pages, blog with data model explanations | `WebSearch`: `site:apptopia.com "[app name]" market data 2025` | Current data + 2025 analysis |
| **AppTweak** | ASO insights, keyword rankings, market intelligence | `WebSearch`: `site:apptweak.com "[category]" insights 2025 OR 2026` | Current rankings + trends |
| **data.ai** (formerly App Annie) | Market estimates via Sensor Tower acquisition | `WebSearch`: `site:data.ai OR site:appannie.com "[category]" report 2025` | 2025-2026 reports |

**Search Query Templates** (prioritize 2025-2026):
```
"[app name]" download estimates sensortower 2025
"[app name]" revenue data apptopia 2025
"[category] apps" market analysis appmagic 2025 OR 2026
"[competitor]" ranking app store "[country]" 2025
"[category]" mobile market report 2025 filetype:pdf
```

**Extract Metrics** (with data freshness indicators):
- Download estimates (ranges: 1K+, 10K+, 100K+, 1M+, 10M+) — **note: estimate date**
- Revenue estimates (if public) — **note: report publication date**
- Category rankings (Top 10, Top 50, Top 100) — **note: ranking date**
- User ratings (average, count) — **note: current as of [date]**
- Update frequency (last update date, version history)
- Featured status (Editor's Choice, Top Charts) — **note: observation date**

**Data Freshness Rule (STRICT)**:
- **Valid date range**: January 1, 2025 to current month 2026 only
- **App store data** (reviews, rankings, downloads): Real-time ✅ — always current
- **Third-party estimates** (Sensor Tower, AppMagic, Apptopia): Must be from 2025-2026 reports
- **News/Articles**: Must be dated 2025-2026; reject 2024 or earlier
- **Always include data collection date** in Evidence Table with format: `Collected: YYYY-MM-DD`

#### 2.4 Identify Top 5 Competitors

**After gathering market intelligence, identify exactly 5 competitors for deep research.**

1. From market research across all channels (Academic, News, Intelligence Platforms), identify the **TOP 5 competitors** in the category
2. For each competitor, find the **official iOS App Store link**:
   - Format: `https://apps.apple.com/app/[app-name]/id[app-id]`
   - Use WebSearch: `"[app name] site:apps.apple.com"` or `"[app name] app store link"`
3. Verify each link by visiting the App Store page
4. List all 5 competitors with their App Store links in your working notes

**Do NOT proceed to the next step until you have confirmed App Store links for all 5 competitors.**

#### 2.5 Deep Research Each Competitor

**For EACH of the 5 competitors**, perform the following research:

**Step A: App Store Analysis** (visit each App Store link):
- App description, features, screenshots, preview videos
- User reviews: analyze 20-30 most recent (mix of 1-star, 3-star, 5-star)
- Rating, download count, price
- Last update date, version history, supported devices
- Capture: `Collected: YYYY-MM-DD`

**Step B: Sensor Tower Deep Research** (WebSearch for EACH competitor):
```
"[app name]" sensortower 2025 OR 2026
"[app name]" revenue estimates 2025
"[app name]" download estimates 2025
"[app name]" user demographics 2025
site:sensortower.com "[app name]" 2025
```

**Step C: Additional Intelligence Platforms** (WebSearch):
```
"[app name]" site:appmagic.com 2025
"[app name]" site:apptopia.com 2025
"[app name]" top charts rankings 2025
```

**Extract for Competitor Matrix:**
| Data Point | Source | Notes |
|------------|--------|-------|
| App Name | App Store | Exact name as displayed |
| Link | App Store | Full URL to App Store page |
| Downloads | Sensor Tower / App Store | Range: 1K+, 10K+, 100K+, 1M+, 10M+ |
| Rating | App Store | Stars + number of ratings |
| Price | App Store | Current price or Free + IAP |
| Revenue | Sensor Tower | Monthly revenue estimates if available |
| Strengths | Reviews + Research | Top 3 most praised features |
| Weaknesses | Reviews + Research | Top 3 common complaints |

**Also extract for the Competitive Analysis section in the PRD template:**

1. **Bảng 1. Chỉ số Thị trường & Thương mại**
   - App name
   - App Store link
   - Downloads / user scale
   - Rating + rating count
   - DAU estimate
   - IAP revenue estimate
   - RPD estimate
   - Engagement time estimate
   - Sessions/day estimate
   - Retention D1/D7/D14/D30/D60 estimate
   - Pricing model
   - Top country / top countries

2. **Bảng 2. Chỉ số Sản phẩm & Kỹ thuật**
   - Main features
   - App size
   - Minimum iOS
   - Current version
   - Last update date
   - Age / longevity signals

3. **Phụ lục gọn: IAP, release và ghi chú storefront**
   - IAP product names and prices
   - First release date (if available)
   - Storefront / data caveats

4. **Narrative synthesis required after the tables**
   - Market overview
   - Methodology note
   - Strategic implications
   - Review insights
   - Our differentiation thesis

**Data Freshness Rule (STRICT)**:
- **Valid date range**: January 1, 2025 to current month 2026 only
- **App Store data**: Real-time ✅ — always current
- **Sensor Tower estimates**: Must be from 2025-2026 reports
- **Always include data collection date**: `Collected: YYYY-MM-DD`

#### 2.6 Community & Social Intelligence (3-5 sources)
**Priority: ONLY discussions from January 2025 to current month 2026**

**General Tech Communities**:
- **Reddit** (`site:reddit.com`):
  - Subreddits: r/ios, r/android, r/startups, r/SideProject, r/Entrepreneur, r/Marketing
  - Search: `"[app name]" OR "[competitor]" OR "[problem space]" after:2024-12-31`
  - **Strict filter**: Sort by "New" and only use posts from 2025-2026
  - Check post timestamp: must be between 2025-01-01 and current month 2026
  - Extract: pain points, feature requests, complaints, praise
  - **Reject**: Any posts from 2024 or earlier
  
- **Hacker News** (`site:news.ycombinator.com`):
  - Check "Ask HN" threads, "Show HN" launches
  - Search: `"[competitor]" OR "[category] app"`
  - **Filter by date**: Only stories from 2025-2026 (check "past" filter)

- **Product Hunt** (`producthunt.com`):
  - Search launches in relevant categories
  - **Filter by "Newest" for 2025-2026 launches ONLY**
  - Check launch date: must be between 2025-01-01 and current month 2026
  - Read comments for user reactions
  - Check "Upcoming" section for pre-launch competitors

**Game-Specific Communities** (if applicable):
- **TouchArcade** (`toucharcade.com`): iOS game reviews — filter by 2025-2026
- **Pocket Gamer** (`pocketgamer.com`): Mobile game news — filter by 2025-2026
- **Reddit gaming**: r/iOSGaming, r/AndroidGaming, r/gamedev — posts from 2025-2026 only
- **Discord**: Current active discussions (real-time, no date filter needed)

**Developer & Publisher Communities**:
- **Indie Hackers** (`indiehacker.com`): Search for 2025-2026 product stories ONLY
- **Dev.to** (`dev.to`): Recent articles from 2025-2026
- **Medium** (`medium.com`): Company blogs, announcements — 2025-2026 posts ONLY

**Social Media (if accessible)**:
- **Twitter/X**: Search for 2025-2026 complaints/praise
  - Query: `"[app name]" OR "[competitor]" since:2025-01-01 until:2026-12-31`
- **LinkedIn**: Company updates, product launches from 2025-2026
  - Check post date: must be within valid range

#### 2.7 User Reviews Deep-Dive (3-5 sources)
- Extract reviews from:
  - App Store (iOS): Read 1-star, 3-star, 5-star reviews
  - Google Play: Same analysis
  - G2 Crowd / Capterra (for B2B)
  - Trustpilot
- Use `WebSearch`: `"[app name]" "user review" "pros and cons"`

**Review Analysis Template**:
For each competitor, document:
- **Top 3 praises** (most mentioned positive points)
- **Top 3 complaints** (recurring negative feedback)
- **Feature requests** (what users want that doesn't exist)
- **Comparison mentions** (users comparing to other apps)

#### 2.8 Company & Product Research (2-3 sources)
- **Company websites**: About pages, blogs, press releases
- **LinkedIn**: Company size, funding announcements, key hires
- **Crunchbase**: Funding history, investor info
- **Pitchbook**: (if accessible) Valuation data

### Minimum Source Requirements

| Category | Minimum Sources | Priority Platforms |
|----------|-----------------|------------------|
| Academic/Industry Reports | 2 | McKinsey, Deloitte, Statista, industry whitepapers |
| News/Tech Articles | 3 | TechCrunch, The Verge, ArsTechnica, VentureBeat |
| App Store Data | 4 | **Sensor Tower**, **AppMagic**, **Apptopia**, AppTweak, direct store pages |
| Community Discussions | 3 | Reddit, Hacker News, Product Hunt, Discord (for games) |
| User Reviews | 3 | App Store, Google Play, G2/Capterra, Trustpilot |
| Company Intel | 3 | Crunchbase, LinkedIn, company blogs, press releases |
| **TOTAL** | **18** | |

**Stretch goal**: 25+ sources for comprehensive coverage.

**Data Quality Priority** (from highest to lowest reliability):
1. **Direct app store data** (iOS App Store, Google Play) - Primary source
2. **Established intelligence platforms** (Sensor Tower, AppMagic, Apptopia) - Industry standard
3. **Company official sources** (blogs, press releases, investor reports) - Verified by company
4. **Reputable tech media** (TechCrunch, The Verge) - Editorial oversight
5. **Community feedback** (Reddit, HN) - User sentiment, unverified claims
6. **Academic/Research** - Methodology-dependent

**Important**: When using third-party estimates (Sensor Tower, AppMagic, etc.), always note in Evidence Table that these are estimates, not official figures.

### Evidence Table

| Claim | Source Type | Source | URL | Date | Data Range |
|-------|-------------|--------|-----|------|------------|
| ... | [News/App Store/Community/etc] | ... | ... | ... | [2025-01 to 2026-XX] |

**Data Range Requirements:**
- **Acceptable**: January 1, 2025 to current month 2026
- **Exclusion**: Any data from 2024 or earlier (unless explicitly marked as "Historical Context")
- **Date format**: Use `YYYY-MM` or full `YYYY-MM-DD` for precision

**Every factual claim in the PRD must have a row here.** If you cannot find a source from 2025-2026, label the claim "unverified" and flag it for the user.

### Competitor Analysis Template

For each of **exactly 5** competitors, gather:

1. **App Store Link** (REQUIRED - verify before proceeding):
   - Full URL to iOS App Store page
   - Format: `https://apps.apple.com/app/[name]/id[number]`

2. **Product Overview**: Core features, positioning, pricing

3. **User Feedback Themes**: Top 3 praises, top 3 complaints

4. **Market Position**: Downloads estimate (Sensor Tower), rating, update recency

5. **Sensor Tower Data** (REQUIRED for each competitor):
   - Revenue estimates
   - Download trends
   - User demographics
   - Use WebSearch: `"[app name]" sensortower 2025`

6. **Differentiation**: What makes them unique

7. **Weaknesses**: Gaps you can exploit

Document in a Competitor Matrix before writing PRD.

## Phase 2.9: Intermediate Outputs Before Writing

Before writing the PRD, prepare these intermediate artifacts in working notes. Do not jump directly from raw research to final prose.

1. **Discovery Brief**
   - Target users
   - Problem statement
   - Core action
   - Success metrics
   - Similar apps / competitors

2. **Competitor Roster**
   - Exactly 5 competitors
   - Verified iOS App Store link for each

3. **Competitive Analysis Pack**
   - Competitor Matrix
   - `Bảng 1. Chỉ số Thị trường & Thương mại`
   - `Bảng 2. Chỉ số Sản phẩm & Kỹ thuật`
   - `Phụ lục gọn: IAP, release và ghi chú storefront`
   - `Diễn giải nhanh cho chiến lược sản phẩm`
   - `Insight Chính từ Review và Định vị của Đối thủ`
   - `Khác biệt hóa của Chúng ta`

4. **Product Direction Notes**
   - Product goal
   - Business alignment
   - Product principles
   - Vision statement
   - KPI draft for 3 months and 6 months

5. **Scope and Delivery Notes**
   - MVP in-scope list
   - Post-MVP list
   - Explicit out-of-scope list
   - Feature table draft
   - Main user flow draft
   - Screen inventory draft

6. **Risks and Unknowns Pack**
   - Assumptions
   - Dependencies
   - Risks + mitigations
   - Open questions with owner and decision deadline

7. **Evidence Table Draft**
   - Every factual claim that will appear in the PRD
   - Source type, source name, URL, date, and data range

If any of the items above are missing, incomplete, or weakly sourced, continue research before writing.

## Phase 3: Write PRD

Create the PRD at `.opencode/specs/[project-name]/PRD.md`.

Write the PRD in **Vietnamese with diacritics by default**, while preserving exact URLs, product names, and technical terms where necessary.

**You MUST read `.claude/doc-templates/PRD.md` first** and follow its section layout. Its `QUALITY-GATE-MANIFEST` block (at the end of the template) is the authoritative list of required sections — do NOT copy that manifest block into the output PRD.

### Required Opening Blocks

Before section `1. Tóm tắt Điều hành`, the PRD must include the metadata block and these 3 tables exactly in this order:

1. Metadata block:
   - `**Version**: ...`
   - `**Date**: ...`
   - `**Author**: ...`
   - `**Mode**: ...`
   - `**Status**: ...`
2. `## Các bên liên quan`
3. `## Lịch sử phiên bản`
4. `## Liên kết quan trọng`

Use the current table structure from `doc-templates/PRD.md`, including the Vietnamese column names:

- `Các bên liên quan`: `Vai trò | Tên | Trách nhiệm | Liên kết`
- `Lịch sử phiên bản`: `Ngày | Phiên bản | Nội dung | Tác giả`
- `Liên kết quan trọng`: `Nội dung | Liên kết`

### PRD Sections

The required sections (mục lớn + mục con) and required closing blocks are defined **only**
in the `QUALITY-GATE-MANIFEST` of `.claude/doc-templates/PRD.md` (single source of
truth). Reproduce every `required_major` and its `required_minor` from the template; do NOT
hard-code or re-list them here. `gate-prd` validates the produced PRD against that manifest.

The guidance below is only how to FILL each section with data (not the structure list):

### Section-to-Data Mapping Rules

- `Tóm tắt Điều hành`: derive from discovery + market timing + research-backed success framing
- `Mục tiêu và Bối cảnh`: derive from user goals, business intent, and product principles inferred from discovery
- `Vấn đề Người dùng và Đối tượng Mục tiêu`: derive from discovery, reviews, and community pain points
- `Phân tích Cạnh tranh`: must include the competitor matrix, both benchmark tables, storefront appendix, strategic implications, review insights, and differentiation
- `Tầm nhìn và Mục tiêu Sản phẩm`: must include 3-month and 6-month KPIs grounded in discovery and market context
- `Phạm vi và Những gì nằm ngoài Phạm vi`: derive from the core action, MVP constraints, and strategic focus
- `Yêu cầu và Tính năng`: turn the MVP scope into a feature table with user stories and acceptance criteria
- `Luồng Người dùng`: derive from the core action and key failure/recovery paths
- `Ràng buộc Sản phẩm và Kỹ thuật`: document platform, architecture, services, performance, offline/sync, notifications, accessibility, privacy, and release-readiness constraints
- `Danh sách Màn hình`: enumerate the minimum screens implied by the MVP scope and user flows
- `Kiếm tiền`: derive from pricing research, competitor IAP patterns, and the intended business model
- `Chỉ số Thành công và Analytics`: translate success metrics into KPI definitions, events, and dashboards
- `Giả định, Phụ thuộc, Rủi ro`: extract unknowns and execution constraints explicitly
- `Câu hỏi Mở`: list unresolved decisions that still need stakeholder alignment
- `Điều phối Triển khai`: summarize owner, stakeholders, milestones, and release window
- `Phụ lục` + `Bảng Bằng chứng`: every factual claim must be traceable to a source

Replace `[project-name]` with the actual project directory name.

## Phase 4: Quality Gate and Confirmation

1. Run the PRD quality gate: invoke `project-docs-quality-gates` with gate `gate-prd`
2. Fix any issues the gate raises
3. Follow `project-docs-lifecycle` to present the draft for user confirmation before marking complete

## Non-negotiable Rules

- **Ask discovery questions first.** No research before the user answers.
- **Wait for answers.** Do not guess or fill in answers yourself.
- **No invented data.** Every number, ranking, and market claim needs a real source. If you cannot find one, say so.
- **Resolve depended-upon open questions.** Any value in `§14 Câu hỏi Mở` that a downstream doc (BR/AC/NFR/FR) will reference (e.g. free scans/day, trial length, AI vendor, default photo storage) MUST be given a concrete **Default** with an explicit `(ASSUMPTION)` flag — never left blank. Leaving it open forces the executing agent to pick arbitrarily.
