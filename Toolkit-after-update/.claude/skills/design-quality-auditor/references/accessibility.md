<!-- PROVENANCE — do build script sinh, KHÔNG sửa tay
nguồn      : ux-design-review.skill  →  references/accessibility.md
nhập ngày  : 2026-08-09
trạng thái : chép nguyên văn, không tóm tắt, không diễn giải
cập nhật   : xuất lại file .skill từ Claude rồi chạy lại build script
-->

# Accessibility baseline checks

Run these on every examined screen. Surface violations as findings (usually Moderate, but Critical if they block use for a group of users). These derive from WCAG 2.1 AA and the platform HIGs.

## Color contrast
Text must meet WCAG AA: 4.5:1 for normal text, 3:1 for large text (≥18px bold or ≥24px regular) and for meaningful UI components/icons. Check: light-gray text on white; colored text on colored fills; low-contrast placeholder or caption text. Flag any text that looks faint against its background.

## Tap-target size
Interactive targets should be at least 44×44pt (iOS HIG) / 48×48dp (Material). Check: small icon buttons, close buttons, list-row chevrons, tightly packed controls. Flag targets that look smaller or too close together to hit reliably.

## Text scaling / truncation
Layouts should tolerate larger system font sizes without clipping or overlap. Check: fixed-height text containers, single-line labels that would truncate, dense number rows. Flag anything that would break with Dynamic Type / large font settings.

## Screen-reader affordances
Every meaningful control needs an accessible label; icon-only buttons especially. Decorative images should be ignorable. Check: icon-only actions with no text, images conveying information with no alternative. (You often can't verify labels from a static design — note it as "verify in build" rather than asserting.)

## Color as the only signal
Never rely on color alone to convey state or meaning — pair it with text, icon, or shape. Check: status shown only by color; a selected state distinguished only by hue. Flag these.

## Motion / animation
Heavy auto-playing motion should respect reduced-motion preferences and not be the only way to convey information. Check: onboarding that forces watching animations; essential info shown only in motion.

## How to report
Accessibility findings fold into the review as their own group under Findings, or (if the user asks) as a scored criterion. When you can't verify something from a static frame (e.g. screen-reader labels, actual contrast ratios without exact hex values), say "verify in build" rather than passing or failing it — honesty about what a static review can and can't confirm is part of the method.
