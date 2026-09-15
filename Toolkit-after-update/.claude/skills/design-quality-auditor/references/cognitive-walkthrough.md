<!-- PROVENANCE — do build script sinh, KHÔNG sửa tay
nguồn      : ux-design-review.skill  →  references/cognitive-walkthrough.md
nhập ngày  : 2026-08-09
trạng thái : chép nguyên văn, không tóm tắt, không diễn giải
cập nhật   : xuất lại file .skill từ Claude rồi chạy lại build script
-->

# Cognitive Walkthrough — task-based flow evaluation

Where heuristics inspect screens against principles, a cognitive walkthrough inspects a *task* against how a real (often first-time) user thinks. You step through a specific goal action-by-action, asking at each step whether the user would know what to do and understand what happened. It's the best method for catching learnability and flow problems that a static screen-by-screen heuristic pass misses — especially drop-off in onboarding and funnels.

Source for self-study: NN/G "Evaluate Interface Learnability with Cognitive Walkthroughs" and the LogRocket guide (which includes a 1–5 scoring template).

## Setup

1. **Define the user.** Who are they, what do they already know? First-time users are the usual focus since learnability is what walkthroughs test best.
2. **Pick concrete tasks.** Not "explore the app" but specific goals: "clean up storage for the first time", "log a meal by photo", "start the free trial". Pick the tasks that matter for the product's success (for a subscription app, reaching the paywall and understanding the offer is a task).
3. **List the correct action sequence.** Write the exact steps the user must take to complete each task. Each step is one action (tap this, choose that).

## The four questions (ask at every step)

For each action in the sequence, ask:

1. **Will the user try to achieve the right effect?** Do they know this sub-goal is needed — is it obvious this step is part of reaching their goal?
2. **Will the user notice the correct action is available?** Is the control visible and discoverable — not hidden, not off-screen, not disguised?
3. **Will the user associate the correct action with the effect they want?** Does the label/icon make it clear this control does what they need? (A "Continue" button that actually starts a trial fails here — the label doesn't match the effect.)
4. **After the action, will the user see progress toward the goal?** Is there feedback confirming they did the right thing and can continue?

A "no" or "maybe" to any question at any step is a finding — record the step, which question failed, and why.

## Scoring (1–5 per step, optional but useful)

For a quantified walkthrough, rate each step's ease on a 1–5 scale (5 = user sails through, 1 = user is stuck or likely to abandon). Steps scoring 1–2 are Critical or Moderate findings. Averaging across the task gives a learnability signal you can track across design iterations. This pairs well with real funnel data — a step that scores low in the walkthrough AND shows a high drop-off in analytics is a confirmed problem, not a hypothesis.

## When to use it in a review

- The product has a multi-step flow (onboarding, checkout, first-run) — walkthrough is more revealing than heuristics here.
- There's drop-off data pointing at a specific step — walk that step to find *why*.
- A task spans several screens where the heuristic (per-screen) pass can't see the seams.

Feed walkthrough findings into both the "Usability & heuristics" and "Conversion / goal effectiveness" criteria in scoring.md — flow friction hurts both. Note in the review which tasks you walked and for which user type, so the scope is honest.
