<!-- PROVENANCE — do build script sinh, KHÔNG sửa tay
nguồn      : ux-design-review.skill  →  references/heuristics.md
nhập ngày  : 2026-08-09
trạng thái : chép nguyên văn, không tóm tắt, không diễn giải
cập nhật   : xuất lại file .skill từ Claude rồi chạy lại build script
-->

# Nielsen's 10 usability heuristics — evaluation checklist

Walk every examined screen through these. For each, the design either satisfies it, violates it, or the heuristic doesn't apply to that screen. Record concrete evidence — the specific element and what it does or fails to do. A finding without a pointed example ("the Home screen shows the same '5.37 GB' three times") is not usable feedback.

## 1. Visibility of system status
The design keeps users informed about what is going on, through timely feedback. Check: loading/scanning states, progress indicators, confirmation after an action, current-location cues in navigation. Violation example: a scan runs with no progress or result feedback; a tab bar that doesn't show which tab is active.

## 2. Match between system and the real world
Language, concepts, and imagery match the user's world, not internal jargon. Check: labels use user vocabulary; icons match their meaning; the flow follows a real-world logical order. Violation: a "cleaner" app whose first screen promotes something unrelated to cleaning; placeholder data that no real user would see (all rows identical).

## 3. User control and freedom
Users can undo, redo, cancel, and exit unwanted states — a clear "emergency exit." Check: back/cancel on every step; undo after destructive actions; no dead ends. Violation: a delete with no undo; a flow you can't back out of; a modal with no dismiss.

## 4. Consistency and standards
Same things look and are named the same way; platform conventions are followed. Check: one term per concept (not "Boost" here, "Clean" there, "Optimize" elsewhere for the same action); consistent icons (distinct icon per nav item); platform-standard patterns (iOS HIG / Material). Violation: three different labels for the same action; identical icons for different tabs.

## 5. Error prevention
The design prevents problems before they happen. Check: confirmation before irreversible/destructive actions; constraints that stop invalid input; sensible defaults. Violation: bulk-deleting photos with no confirmation dialog; no guard against deleting the wrong item.

## 6. Recognition rather than recall
Minimize memory load — make options, actions, and information visible. Check: users don't have to remember data across screens; relationships between numbers/elements are shown, not inferred. Violation: three unlabeled numbers whose relationship the user must deduce; hidden actions with no affordance.

## 7. Flexibility and efficiency of use
Accelerators for experienced users, without hindering novices. Check: shortcuts (one-tap actions, batch operations); personalization; the common path is fast. Strength example: a "Boost Now / one-tap clean" that shortcuts the whole flow.

## 8. Aesthetic and minimalist design
No irrelevant or rarely-needed information competing with the relevant. Check: each screen has a clear focus; no clutter; visual hierarchy guides the eye. Violation: overlapping elements; duplicated data blocks; competing CTAs with equal weight.

## 9. Help users recognize, diagnose, and recover from errors
Error messages in plain language, precisely stating the problem and suggesting a solution. Check: errors are human-readable; there's a recovery path (restore, retry). Violation: silent failure; no "recover deleted items" after a clean.

## 10. Help and documentation
Help is available where needed, concise, task-focused. Check: unfamiliar concepts are explained in-context (e.g. how "similar photos" differs from "duplicates"); onboarding conveys how to use core features; empty states guide the next action. Violation: two near-identical features with no explanation of the difference.

## How to use this pass
For each screen, produce a short list: heuristic number, satisfied/violated, evidence. Roll these up into the "Usability & heuristics" criterion score in `scoring.md` — many Critical violations across core screens pushes that score toward 40–55; a clean pass with only minor issues pushes it toward 80+.
