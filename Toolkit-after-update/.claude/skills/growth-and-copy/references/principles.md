<!-- PROVENANCE — do build script sinh, KHÔNG sửa tay
nguồn      : ux-writing-review.skill  →  references/principles.md
nhập ngày  : 2026-08-09
trạng thái : chép nguyên văn, không tóm tắt, không diễn giải
cập nhật   : xuất lại file .skill từ Claude rồi chạy lại build script
-->

# Content-design principles — the evaluation passes

Run every string through these. Each is a lens; a string can pass some and fail others. Name the principle when you flag an issue so the feedback is defensible.

## 1. Clarity — will the user understand it immediately?
Plain words over jargon; concrete over abstract; the user's vocabulary, not the system's. No ambiguity about what will happen. Test: could a first-time, distracted user understand this on one read? Violation: "Eliminate redundant media assets" for "Delete duplicate photos"; a button that doesn't say what it does ("Submit" → "Send message").

## 2. Concision — is every word earning its place?
Cut filler ("in order to" → "to", "please note that" → nothing, "you are able to" → "you can"). Front-load the important word. Shorter is not always better, but longer must be justified by clarity. Test: can I cut a word without losing meaning? Violation: "We intend to provide transparency and protect your privacy" as permission-request filler nobody reads.

## 3. Usefulness — does the copy help the user act or decide?
Especially errors and empty states: don't just state a fact, give the next step. Tell people what they can do, not only what went wrong. Test: after reading, does the user know what to do next? Violation: "Something went wrong" with no recovery path; an empty state that says "No items" without "Add your first item".

## 4. Voice and tone — right personality, right moment
Voice is constant (the product's character); tone flexes with context (calm in errors, warm in wins). Match the emotional temperature: never cheerful about a failure, never jokey in a security or payment moment. Test: does this sound like the product, and is the tone right for what the user is feeling here? Violation: an exclamation-mark celebration on a screen where the user just lost data.

## 5. Consistency — one concept, one word; parallel things, parallel form
The same action uses the same label everywhere (not "Delete" / "Remove" / "Clear" for one action). Parallel elements share structure (all CTAs verb-first, or all noun phrases). Consistent capitalization (Title Case vs sentence case — pick one), consistent number/date/unit format. This is a system property — check across screens, not per string. Violation: "Boost" / "Clean" / "Optimize" for the same action on three screens.

## 6. Accessibility of language
Reading level appropriate to the audience (aim plain — many mature interfaces target ~grade 7–9 for broad consumer apps). Avoid idioms that don't translate/localize, culture-specific references, and words that assume ability ("see below", "just tap"). Expand or avoid unexplained acronyms. Write for screen readers: labels must make sense read aloud out of visual context. Test: does it work for a non-native speaker, a screen-reader user, a stressed user?

## 7. Accuracy and honesty
The copy must describe what the product actually does. Never write a label, benefit, or headline that promises a feature the product lacks or overstates what happens. This overlaps with trust and with app-store compliance. Test: is every claim true of the real product? Violation: onboarding copy promoting a capability the app doesn't ship.

## 8. Scannability and formatting
Users scan, not read. Front-load meaning; keep to one idea per sentence/line; use formatting (bolding a key number, short lines) to guide the eye — without over-formatting. Headlines carry the message even if the body is skipped. Test: if the user reads only the headline and the button, do they get the point?

## How to use
For each string, note which principles it satisfies and which it violates, with evidence. Roll violations into the issue list with severity: a clarity or accuracy failure on a critical action (a CTA, a permission, a payment) is high severity; a concision nit in a rarely-seen tooltip is low. An issue flagged by multiple principles (e.g. unclear AND inconsistent) is higher priority.
