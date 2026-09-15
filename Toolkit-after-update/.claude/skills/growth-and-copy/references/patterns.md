<!-- PROVENANCE — do build script sinh, KHÔNG sửa tay
nguồn      : ux-writing-review.skill  →  references/patterns.md
nhập ngày  : 2026-08-09
trạng thái : chép nguyên văn, không tóm tắt, không diễn giải
cập nhật   : xuất lại file .skill từ Claude rồi chạy lại build script
-->

# Type-specific microcopy patterns

Different interface elements have different jobs and different rules. Apply the right pattern to the right element.

## Buttons and CTAs
- Lead with a verb that names the outcome: "Start free trial", "Delete photos", "Save changes" — not "OK", "Submit", "Continue" when something more specific is possible.
- The label should match what happens next. A button that starts a paid trial should not say "Continue" — that hides the consequence and breaks trust (and the cognitive-walkthrough "does the label match the effect?" test).
- Keep it short enough to fit the container at large font sizes.
- Primary vs secondary: the primary action is specific and affirmative; the secondary (skip, not now, cancel) is quieter but still clear. Avoid guilt-tripping decline labels.

## Error messages
Three parts: what happened (plainly), why if useful, and what to do next. Blame the situation, not the user. No codes-only, no "invalid input" without saying what's valid. Keep tone calm and human. Example: not "Error 402" but "That card was declined. Try another card or contact your bank."

## Empty states
An empty state is an opportunity, not a dead end. Say what goes here and how to add the first one. Example: not "No meals logged" but "No meals yet — snap a photo to log your first one." Optionally motivate (why it's worth doing).

## Onboarding / benefit screens
- One idea per screen; headline carries it. Body supports, doesn't repeat the headline's verb.
- Speak to the user's benefit, not the feature mechanism — but stay accurate. "Free up gigabytes in one tap" (benefit) over "Runs a filesystem scan" (mechanism).
- End with momentum: the button moves them forward; progress indicators show how much is left (reduces drop-off).
- Don't front-load a low-value or off-theme screen; the first screen should match why they downloaded the app.

## Permission requests (pre-prompts)
- Ask in context, right before the value is needed, and say why in one line tied to a benefit: "Allow photo access so we can find duplicates to delete." 
- Don't bury the reason in legal filler. The user decides in a second — give the reason in that second.
- Provide an honest, low-friction decline ("Not now") without dark patterns.

## Paywalls / trial offers
- State the offer plainly: what's free, for how long, what happens after, how to cancel. Hiding the "then $X/week" erodes trust and invites refunds/bad reviews.
- The CTA names the actual action and its safety: "Start 3-day free trial" beats "Continue". If there's a trial, say it on the button.
- Show value adjacent to price (what they unlock), and make the recommended plan's saving concrete ("Save 88%" with the math evident).

## Notifications / system messages
- Lead with the useful content; the user sees a fragment. Front-load the who/what.
- No false urgency, no clickbait. Respect that this interrupts the user.

## Confirmations (destructive actions)
- Name the specific consequence and whether it's reversible: "Delete 12 photos? This can't be undone." The confirm button restates the action ("Delete"), not a generic "OK". Offer the safe way out as the easy default.

## Cross-cutting
- Numbers: format consistently, and prefer concrete numbers where they add credibility ("512 MB freed" over "space freed").
- Never repeat the same strong verb in a headline and its own body ("Delete… / …eliminate…"); vary or let the body describe the how.
