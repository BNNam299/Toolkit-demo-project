<!-- PROVENANCE — do build script sinh, KHÔNG sửa tay
nguồn      : ux-design-review.skill  →  references/scoring.md
nhập ngày  : 2026-08-09
trạng thái : chép nguyên văn, không tóm tắt, không diễn giải
cập nhật   : xuất lại file .skill từ Claude rồi chạy lại build script
-->

# Scoring rubric, weights, and priority levels

## Score bands (apply to each criterion, 0–100)

- **90–100 — Excellent.** Follows standards thoroughly; no notable violations; polished and intentional. Rare.
- **75–89 — Good.** Solid, professional; a few minor issues that don't impede use.
- **60–74 — Fair.** Works but has several real problems; noticeable friction or inconsistency; clearly improvable without a rebuild.
- **40–59 — Weak.** Multiple significant violations that impede use or erode trust; needs focused rework.
- **20–39 — Poor.** Core problems across the board; fails common standards; substantial redesign needed.
- **0–19 — Broken.** Unusable or fundamentally flawed.

Score against the standard, not against other apps. Cite the evidence that puts a criterion in its band.

## The six criteria and default weights

| Criterion | Weight | What it measures |
|---|---|---|
| Usability & heuristics | 30% | Nielsen heuristics + platform conventions; error prevention, feedback, undo, confirmation |
| Visual design | 20% | Hierarchy, typography, color, spacing, consistency of the visual system; trustworthiness |
| Conversion / goal effectiveness | 20% | How well the design drives its primary goal (evidence-backed if funnel data exists) |
| Information architecture | 15% | Structure, navigation, labeling; does the story match the actual product |
| Content & consistency | 15% | Microcopy, terminology consistency, no placeholder/duplicated/broken text |

Accessibility is run as a baseline check (see `accessibility.md`) and its violations surface as findings. If the user wants it scored as its own weighted line, add it (typical 10–15%) and renormalize the others so the total is still 100%.

## Computing the total

Weighted average: total = Σ (criterion_score × weight). Always show the arithmetic so the number is auditable. Example:

```
Usability 50 × 0.30 = 15.0
Visual    75 × 0.20 = 15.0
Conversion 40 × 0.20 = 8.0
IA        55 × 0.15 = 8.25
Content   55 × 0.15 = 8.25
Total = 54.5 ≈ 55 / 100
```

Round the final total to a whole number. Present it on a 0–100 scale (clearer than 0–10 for weighted math).

## Adjusting weights to the product goal

State the change whenever you make it, and note the total moved because of reweighting, not a design change.

- **Subscription / commerce app** — Conversion 30%, Usability 25%, Visual 20%, IA 15%, Content 10%.
- **Enterprise / productivity tool** — Usability 35%, IA 25%, Content 15%, Visual 15%, Conversion 10%.
- **Brand / marketing site** — Visual 35%, Content 20%, Conversion 20%, Usability 15%, IA 10%.
- **General consumer app** — the defaults above.

## Priority levels for findings

Every finding gets a priority by user impact, not by how easy it is to fix.

Rate severity using the standard Nielsen/Maze model — three factors combined:
- **Frequency** — how often users hit it (rare vs. every session).
- **Impact** — how hard it is to overcome when hit (minor annoyance vs. task-blocking).
- **Persistence** — is it a one-time bump users learn around, or a repeated obstacle?

A finding flagged by more than one method (e.g. both Nielsen and Shneiderman, or a heuristic plus a low cognitive-walkthrough step score) generally rates at least one level higher, because independent methods converging on it is strong evidence.

Map the combined severity to three levels:

- **Critical** — high on all three: frequent, blocks or badly derails a task, persistent. Also: risks data loss or store rejection. Examples: placeholder data that looks like a bug; destructive action with no confirmation; promoting a feature the product doesn't have; a walkthrough step where a first-time user would abandon. Fix first.
- **Moderate** — creates friction or confusion but the user can still get through, or hits only some users/sessions. Examples: inconsistent terminology; a control in the wrong context; weak visual hierarchy; a step that scores 3/5 in the walkthrough.
- **Minor** — polish; low frequency and low impact. Examples: slightly off spacing; a label that could be tighter; a nice-to-have shortcut.

Order the report Critical → Moderate → Minor. Each finding names the problem (screen + element), the method/standard that flagged it, and the concrete fix.

## Confidence

State how much of the design you actually examined and how that limits the score. "Examined 1 of 7 screens visually; remaining scored from structure only — treat sub-scores as provisional." A score from partial material is a starting point, not a verdict, and the write-up must say so.
