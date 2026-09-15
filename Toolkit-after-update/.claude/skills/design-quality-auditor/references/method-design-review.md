<!-- PROVENANCE — do build script sinh, KHÔNG sửa tay
nguồn      : ux-design-review.skill  →  SKILL.md
nhập ngày  : 2026-08-09
trạng thái : chép nguyên văn, không tóm tắt, không diễn giải
cập nhật   : xuất lại file .skill từ Claude rồi chạy lại build script
-->

---
name: ux-design-review
description: "Evaluate the UI/UX quality of a digital product design (mobile app, web app, or website) against established standards — Nielsen's 10 heuristics, Shneiderman's 8 Golden Rules, cognitive walkthroughs — plus the team's internal methodology: PACT context analysis and the 5-component usability framework (Learnability/Efficiency/Memorability/Errors/Satisfaction) with 0-4 scoring. Produces a scored, criteria-based review with severity-rated findings. Use whenever the user asks to evaluate, audit, critique, review, grade, or score a design's usability or UX: 'is this design good/usable', 'rate this UI', 'heuristic evaluation', 'UX audit', 'đánh giá thiết kế', 'chấm điểm app', 'review màn hình này', or shares Figma frames/screenshots wanting structured feedback. Also for comparing two designs, walking onboarding/checkout flows for drop-off, or pre-ship audit checklists. For moderated user testing with real participants, route to ux-usability-evaluator."
---

# UI/UX Design Review

Produce a rigorous, criteria-based evaluation of a product design, grounded in established usability standards rather than personal taste. The output is a weighted score plus specific, prioritized, actionable findings.

## Core principle: evidence over opinion

Every finding must point to something concrete in the design (a specific screen, element, label, or number) and name the standard it violates or satisfies. Never give a vague verdict like "looks clean" or "feels off." If you cannot see a screen, say so and scope the review to what you actually examined — do not guess at screens you haven't viewed, and do not invent metrics. A review's credibility comes from being honest about what was and wasn't assessed.

## Workflow

1. **Gather the material.** Identify what you're evaluating and get visual access. For Figma, use the design-context tool to pull each screen's structure AND screenshot — usability lives in the visual detail (hierarchy, spacing, contrast, tap targets), so reading structure alone is not enough. For screenshots, examine them directly. List which screens you actually saw; the review only covers those.

2. **Establish context.** Ask (or infer from the conversation) three things that change how you weight the review: the platform (iOS/Android/web — each has its own HIG conventions), the product's primary goal (task efficiency? conversion? engagement?), and whether real usage data exists (funnel/drop-off numbers). If conversion data exists, conversion becomes a heavily weighted, evidence-backed criterion; if not, note that the conversion score is inferred and lower-confidence.

   For redesigns or full-product audits, structure this step with **PACT** (the team's context framework — see `references/team-framework.md`): People (ai dùng, khả năng/hạn chế), Activities (5 đặc điểm: tần suất & tính liên tục & thời gian đáp ứng 100ms/5s, hợp tác, phức tạp, an toàn, bản chất nội dung), Context (tổ chức/xã hội/vật lý), Technology (đầu vào/đầu ra/nền tảng). A design can only be judged against its PACT — a flow that fails office workers may be right for gloved lab technicians.

3. **Run the evaluation passes.** Apply the standard methods below — they overlap on purpose, and an issue flagged by more than one framework is a strong, high-priority signal.
   - **Nielsen's 10 heuristics** (always) — walk every examined screen through them. See `references/heuristics.md`.
   - **Shneiderman's 8 Golden Rules** (always) — a second heuristic lens sharper on interaction mechanics (consistency, feedback, reversal, control, memory load). See `references/shneiderman.md`. Especially valuable for interaction-heavy screens: forms, multi-step flows, controls.
   - **Cognitive walkthrough** (when there's a multi-step flow or drop-off data) — step through specific tasks as a first-time user, asking the four questions at each action. See `references/cognitive-walkthrough.md`. This catches learnability and funnel problems the per-screen passes miss; it's the right tool when the product has onboarding, checkout, or a first-run flow, or when analytics point at a specific step.
   - **Team 5-component pass** (when the audience is the internal team, or the user asks for "đánh giá theo framework của team") — walk the screens through Learnability (dự đoán + nhận biết), Efficiency (điều hướng, điều khiển, phản hồi, hệ thống thông minh), Memorability (quen thuộc + nhất quán), Errors (3 mức + 3 cơ chế khắc phục). Satisfaction requires real users — mark it "cần user testing" and route to `ux-usability-evaluator` mode B. Score findings on the team's 0-4 scale; see `references/team-framework.md` for the full rubric, the severity mapping to Critical/Moderate/Minor, and the required Who-When-Why-How usage scenario that precedes the pass.
   Record concrete violations and strengths from each pass.

4. **Score the six criteria.** Rate each on 0–100, apply the weights, and compute the weighted total. See `references/scoring.md` for the rubric (what each band means), the default weights, and how to adjust weights to the product's goal. Show your arithmetic so the total is auditable. Feed all three passes into the scores: heuristic findings drive "Usability & heuristics"; walkthrough findings drive both "Usability" and "Conversion / goal effectiveness" (flow friction hurts both).

5. **Prioritize findings with a severity rating.** Group every finding into Critical / Moderate / Minor by user impact (see `references/scoring.md` for the severity scale, which follows the standard Nielsen/Maze severity model — frequency × impact × persistence). Critical = actively breaks trust or blocks a task. An issue flagged by two or more passes generally rates at least one level higher. Order the report so the reader fixes the highest-impact issues first.

6. **Present the review.** Follow the report structure below. Use the visualizer for the scorecard (a weighted-bar breakdown reads far better than prose). Keep the written findings specific and prescriptive — each should say what's wrong, which method/standard flagged it, why it matters, and what to do instead.

## Report structure

Always produce these sections, in this order:

1. **Scope** — one or two sentences: what was evaluated, which screens were examined, whether real usage data was available. Be explicit about gaps.
2. **Overall score** — the weighted total on a 0–100 scale, shown via the visualizer scorecard with each criterion's sub-score and weight. State the arithmetic.
3. **Criteria breakdown** — a short paragraph per criterion explaining *why* it earned its score, citing specific evidence.
4. **Findings by priority** — Critical, then Moderate, then Minor. Each finding: the concrete problem (screen + element), the standard it violates, and the recommended fix. Never use bullet-only verdicts without the "why" and the "fix."
5. **What's working** — genuine strengths, so the team knows what to preserve. A review that only criticizes is neither accurate nor useful.
6. **Confidence & next steps** — how reliable this score is given what you could see, and what would sharpen it (e.g. "screenshots of the remaining screens", "real funnel data").

## Evaluation methods and source references

The passes above draw on established, citable methods. Point users here to self-study or build their own internal audit checklists.

Nielsen's 10 usability heuristics — the field-standard principles (NN/G): the original article at nngroup.com/articles/ten-usability-heuristics/ and how to run an evaluation at nngroup.com/articles/how-to-conduct-a-heuristic-evaluation/.

Shneiderman's 8 Golden Rules — interaction-design principles (HCI): Shneiderman's own page at cs.umd.edu/users/ben/goldenrules.html and the Interaction Design Foundation write-up.

Cognitive walkthrough — task-based learnability method: NN/G's cognitive-walkthroughs article, and the LogRocket guide which includes a 1–5 scoring template.

Ready-made checklists and severity templates — Eleken's UX audit checklist (built on Nielsen's heuristics) and Maze's heuristic-evaluation guide with a free severity-rating template.

Claude cannot browse these live and evaluates from its own knowledge of these well-established methods; the links are for the user's own reference and verification.

## The six evaluation criteria

These are scored in step 4. Full rubric in `references/scoring.md`.

1. **Usability & heuristics** (default weight 30%) — how well the design follows Nielsen's heuristics and platform conventions; presence of error prevention, confirmation, undo, feedback.
2. **Visual design** (20%) — hierarchy, typography, color, spacing, consistency of the visual system; does it look intentional and trustworthy.
3. **Conversion / goal effectiveness** (20%) — how well the design drives its primary goal. Evidence-backed if funnel data exists; inferred and lower-confidence if not.
4. **Information architecture** (15%) — clarity of structure, navigation, labeling; does the product's story match what it actually does.
5. **Content & consistency** (15%) — microcopy quality, terminology consistency, absence of placeholder/duplicated/broken text.
6. **Accessibility** (baseline check, folded in) — contrast, tap-target size, text scaling, screen-reader affordances. See `references/accessibility.md`. Surface accessibility violations as findings; if the user wants accessibility scored as its own weighted criterion, add it and renormalize weights.

## Adapting weights

The defaults suit a general consumer app. Shift them to the product's goal and say you did: a commerce/subscription app pushes conversion higher; an enterprise tool pushes usability and IA higher; a brand/marketing site pushes visual design higher. Weights must sum to 100%. When you change them, show the new weights and note that the total shifted because of the reweighting, not because the design changed.

## Honesty guardrails

- Only score what you examined. If you saw one screen out of seven, the review covers one screen and the confidence is low — say so plainly.
- Never fabricate metrics. If there's no funnel data, the conversion criterion is inferred; label it.
- A score is relative and partly subjective. Present it as "where this is and what to fix," not an absolute verdict. Note how the total would move under different reasonable weightings.
- Cite the standard behind each finding so the user can verify it, not just trust you.

## Routing: this skill vs ux-usability-evaluator

Both evaluate usability; pick by audience and method, and say which you chose:

- **This skill (ux-design-review)** — scored audit against international standards (Nielsen/Shneiderman/walkthrough, weighted 0-100), optionally adding the team 5-component pass. Best for: external-facing reviews, comparing designs, pre-ship audits, "chấm điểm app này".
- **ux-usability-evaluator** — the team's native methodology end-to-end: Who-When-Why-How scenario → 5 components → 0-4 findings table, plus **moderated user testing with real users** (mode B). Best for: internal team reports in the team's format, and any evaluation requiring real participants (Satisfaction can only be measured there).
- Running both? Merge findings into one table; an issue flagged by both international heuristics and the team framework is top priority. Map scales via `references/team-framework.md`.
