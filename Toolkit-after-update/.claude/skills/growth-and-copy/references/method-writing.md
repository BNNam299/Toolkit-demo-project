<!-- PROVENANCE — do build script sinh, KHÔNG sửa tay
nguồn      : ux-writing-review.skill  →  SKILL.md
nhập ngày  : 2026-08-09
trạng thái : chép nguyên văn, không tóm tắt, không diễn giải
cập nhật   : xuất lại file .skill từ Claude rồi chạy lại build script
-->

---
name: ux-writing-review
description: "Review, evaluate, and improve the words in a product interface — UI microcopy, button and CTA labels, onboarding and empty-state text, error and confirmation messages, tooltips, form labels, paywall and permission-request copy, notifications. Use whenever the user asks to refine, rewrite, critique, or 'make the copy better', asks whether wording is clear/on-brand/too long, wants button or headline options, wants an error or empty state written, wants terminology made consistent across screens, or shares mockups wanting the text (not layout) assessed. Also use to write microcopy from scratch for a described screen, localize tone, or build a content style guide. Trigger even without the words 'UX writing' or 'microcopy' — any request to judge or produce interface wording should use this skill so writing is evaluated against real content-design principles instead of ad-hoc taste. Do NOT use for long-form prose (articles, blog posts, essays) — this is for interface text."
---

# UX Writing Review

Evaluate and improve the words inside a product interface, grounded in content-design principles rather than personal taste. Interface copy has a job: help the user understand, decide, and act with the least friction. Every recommendation should serve that job and be defensible against a principle, not just "reads nicer."

## Core principle: copy is a UX decision, not decoration

A word change can change behavior — a button labeled "Continue" vs "Start free trial" produces different tap rates and different expectations. So treat wording like any design decision: know the user's goal at that moment, know what the copy must make them understand or do, and judge whether it does. When you can't see something (the flow it sits in, the brand voice, real click data), say so and scope the review to what you know.

## Workflow

1. **Inventory the copy.** List every string you're evaluating, grouped by screen and by type (headline, body, button/CTA, label, error, empty state, helper text, legal/permission). You can't improve what you haven't laid out. If reviewing a flow, capture the copy in reading order so you can see repetition and inconsistency across screens.

2. **Establish voice and context.** Identify (or ask): who is the user and what's their goal at this moment, what's the product's voice (playful? plain? authoritative?), the platform (iOS/Android/web conventions differ), and the emotional temperature (a payment error needs different words than a celebration). If a brand voice or style guide exists, evaluate against it; if not, note that you're applying general content-design norms.

3. **Run the evaluation passes.** Apply the checks in `references/principles.md` (the content-design heuristics: clarity, concision, usefulness, voice, consistency, accessibility of language) and `references/patterns.md` (type-specific rules for buttons, errors, empty states, permissions, paywalls, onboarding). Flag each issue with the principle it violates.

4. **Rewrite, don't just critique.** For every flagged issue, provide the improved wording — usually the recommended version plus one alternative when there's a real strategic choice (e.g. a plain vs. a hookier headline). Show the before and after so the change is visible. Never leave a criticism without a concrete replacement.

5. **Check the set as a whole.** Consistency is a system property: one term per concept across all screens, parallel structure in parallel elements (all buttons verb-first, or all noun phrases — pick one), a consistent numeric/format style, a consistent voice. A pass that fixes each string in isolation but leaves the set inconsistent has failed.

6. **Note what to validate with users/data.** UX writing quality is ultimately proven by comprehension and behavior, not opinion. Where a choice is genuinely uncertain (does this label read as expected? does this CTA convert?), say what method would settle it — a quick comprehension check, tree test / card sort for navigation labels, or funnel/CTR data on the live copy. See `references/validation.md`.

## Output format

- **Scope** — what copy was reviewed, which screens, what you knew about voice/context and what you didn't.
- **Issues and rewrites** — grouped by screen or by severity. Each: the current text, the problem (named principle), and the rewrite (recommended + optional alternative).
- **Consistency pass** — cross-screen findings: terminology, structure, tone, formatting.
- **Voice note** — is the copy in a consistent, appropriate voice; if a hook vs. plain choice exists, state the tradeoff and recommend.
- **Validate next** — the few things worth testing with real users or data rather than deciding by judgment.

Keep it prescriptive and specific. "Tighten this" is not feedback; "cut 'in order to' → 'to'; the sentence is 6 words shorter and reads at a glance" is.

## Honesty guardrails

- Don't invent brand voice. If you weren't given one, say you're applying general norms and that a brand guide could change specifics.
- Don't claim a rewrite will lift conversion as fact. Say it's expected to, and name what would confirm it.
- Keep the user's meaning. Don't "improve" copy into saying something the product doesn't do — accuracy first (a rewrite that promises a feature the app lacks is a failure, not a polish).
- Respect length constraints. Interface text lives in real containers; a witty label that overflows the button is wrong. Flag when a rewrite needs to fit a specific space.

## Method sources (for the user's own study)

The passes draw on established content-design references; point users here to go deeper. Claude cannot browse these live and evaluates from its own knowledge of these methods — the links are for the user's verification.

- Nielsen Norman Group — UX Writing Study Guide (nngroup.com/articles/ux-writing-study-guide/): structure, formatting, writing for scanning.
- UX Content Collective (uxcontent.com/what-is-ux-writing/): foundational definitions and the role of content in product design.
- User Interviews field guide and BBC GEL research methods: how to run comprehension studies, tree testing, and card sorting to test wording and navigation labels.
- Maze UX research tools guide: survey and behavior-analytics tools (Hotjar heatmaps, Mixpanel funnels) for finding where copy causes drop-off and measuring CTA performance.
