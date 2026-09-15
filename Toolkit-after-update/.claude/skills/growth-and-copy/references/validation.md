<!-- PROVENANCE — do build script sinh, KHÔNG sửa tay
nguồn      : ux-writing-review.skill  →  references/validation.md
nhập ngày  : 2026-08-09
trạng thái : chép nguyên văn, không tóm tắt, không diễn giải
cập nhật   : xuất lại file .skill từ Claude rồi chạy lại build script
-->

# Validating UX writing with users and data

Judgment gets you a strong draft; comprehension and behavior prove it. When a wording choice is genuinely uncertain — will users understand this label, will this CTA convert — recommend the method that would settle it rather than asserting. Below are the standard methods and when each applies.

## Qualitative — does it make sense to people?

**Comprehension / highlighter test.** Show the copy; ask users to say in their own words what it means, or highlight anything confusing. Fast way to catch jargon, ambiguity, and wrong assumptions. Best for: error messages, onboarding, permission reasons, anything a first-timer must understand.

**5-second test.** Show a screen for 5 seconds, then ask what it's about / what they'd do. Tests whether the headline and primary action carry the message when scanned. Best for: onboarding and landing screens.

**Usability testing (task-based).** Give a task, watch where wording causes hesitation or wrong turns. Pairs with a cognitive walkthrough — a step where the label doesn't match the user's goal shows up as a stumble. Best for: flows, forms, CTAs.

## Structural — do the labels match users' mental models?

**Tree testing.** Give users a task and a text-only menu tree; see if they find the right label. Tests navigation and menu wording without visual design as a crutch. Best for: nav labels, settings, IA.

**Card sorting.** Users group and name concepts; reveals the words and categories they expect. Best for: choosing terminology and grouping features.

## Quantitative — what do people actually do?

**Funnel analytics (e.g. Mixpanel).** Find the step where users drop or exit — points you at the screen (and often the copy) that's failing. Best for: locating problem copy at scale; confirming a hypothesized weak screen.

**Heatmaps / session replay (e.g. Hotjar).** See what users click, how far they read, where they hesitate; collect inline feedback on specific text. Best for: seeing whether a CTA or link is noticed and understood.

**A/B testing on CTA / headline.** Ship two wordings, compare tap-through or conversion. The definitive test for "which words convert better" — but needs traffic and a clean metric. Best for: high-traffic CTAs, paywall copy, headlines where a real business metric rides on the words.

## How to recommend in a review
Don't over-prescribe. Name validation only where the choice is genuinely uncertain or the stakes are high (a primary CTA, a paywall line, a permission prompt). For low-stakes copy, a judgment call is fine — say so. When live data already exists (the user gave you funnel/drop-off numbers), tie the copy recommendation to the specific step the data flags, so the change is targeted rather than cosmetic.
