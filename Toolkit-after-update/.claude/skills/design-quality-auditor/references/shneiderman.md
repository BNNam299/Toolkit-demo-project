<!-- PROVENANCE — do build script sinh, KHÔNG sửa tay
nguồn      : ux-design-review.skill  →  references/shneiderman.md
nhập ngày  : 2026-08-09
trạng thái : chép nguyên văn, không tóm tắt, không diễn giải
cập nhật   : xuất lại file .skill từ Claude rồi chạy lại build script
-->

# Shneiderman's 8 Golden Rules of Interface Design

A second heuristic lens focused on human-computer interaction, complementary to Nielsen's. Where Nielsen's heuristics are broad usability principles, Shneiderman's rules are sharper about interaction mechanics — consistency, feedback loops, control, and reducing memory load. Use them alongside the Nielsen pass; they overlap deliberately, and a violation flagged by both frameworks is a strong signal.

Source for self-study: Shneiderman's own page (cs.umd.edu/users/ben/goldenrules.html) and the Interaction Design Foundation article. The rules below are the canonical set.

## 1. Strive for consistency
Consistent sequences of actions in similar situations; identical terminology in prompts, menus, and help; consistent color, layout, capitalization, fonts. Check: does the same action use the same label and control everywhere? Are destructive actions styled consistently? Violation example: three different labels ("Boost", "Clean", "Optimize") for the same clean action across screens.

## 2. Seek universal usability
Recognize diverse users — novices to experts, different ages, abilities, tech comfort. Provide accelerators for experts (shortcuts) and explanations for novices (hints, onboarding). Overlaps with accessibility. Check: is there a fast path for repeat users and a guided path for first-timers?

## 3. Offer informative feedback
For every user action, there should be system feedback — modest for frequent/minor actions, substantial for infrequent/major ones. Check: does tapping a control visibly respond? Does a long operation show progress? Does completing a task confirm it? Violation: a scan that runs with no progress indicator; a delete with no confirmation of what happened.

## 4. Design dialogs to yield closure
Sequences of actions should have a beginning, middle, and end, with informative feedback at completion — a sense of accomplishment and a signal to move on. Check: do multi-step flows (onboarding, checkout, logging a meal) end with a clear "done" state? Violation: a flow that just dumps the user back with no completion cue.

## 5. Prevent errors
Design so users can't make serious errors; gray out invalid options, don't allow invalid characters, require confirmation for consequential actions. On error, offer simple, constructive, specific recovery. Overlaps Nielsen #5. Check: confirmation before bulk-deleting photos; input constraints on numeric fields.

## 6. Permit easy reversal of actions
Actions should be reversible — undo. This relieves anxiety and encourages exploration since users know errors can be undone. Check: is there undo after deletion? Can the user back out of any step? Violation: irreversible clean with no "restore recently deleted".

## 7. Keep users in control (support internal locus of control)
Experienced users want to feel in charge; the system responds to their actions rather than surprising them. Avoid unexpected changes, tedious data entry, difficulty getting needed info. Check: no forced auto-actions; the user initiates, the system responds. Violation: onboarding that auto-plays videos with no skip; a paywall with no visible close.

## 8. Reduce short-term memory load
Humans hold limited information in working memory (~7 items). Keep displays simple, consolidate, provide recognition over recall, keep needed info visible across steps. Overlaps Nielsen #6. Check: does the user have to remember a value from a previous screen? Are related items grouped? Violation: three unlabeled numbers whose relationship must be inferred.

## How to use this pass
Run it after the Nielsen pass. Most findings will reinforce Nielsen findings (consistency, feedback, error prevention, memory load appear in both) — note when both frameworks flag the same issue, as that raises its priority. Shneiderman is especially strong for interaction-heavy screens (forms, multi-step flows, controls); Nielsen is broader. Feed both into the "Usability & heuristics" criterion score in scoring.md.
