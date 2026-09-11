# Accessibility Review

Checklist for the accessibility pass of any critique. Accessibility findings are severity-anchored: a screen that blocks assistive-technology users from completing the core task is a P0 by definition (see `references/critique-principles.md` for the severity scale). This file covers the essentials a practitioner can verify by inspection; it is not a substitute for a full audit or for testing with real assistive technology.

The references here are to WCAG 2.1/2.2 success criteria (SC). They are stable public standards; cite the numbers exactly as given below.

## Contrast (the audit's overlap with color)

- **SC 1.4.3 Contrast (Minimum):** 4.5:1 for normal text, 3:1 for large text (24px+, or 19px+ bold). Compute, do not eyeball. Full method in `references/color-and-contrast.md`.
- **SC 1.4.11 Non-text Contrast:** 3:1 for UI component boundaries, icons that carry meaning, and focus indicators.
- **SC 1.4.1 Use of Color:** color is never the only signal for state, required fields, or chart series.
- **SC 1.4.12 Text Spacing:** no loss of content or function when users increase line/letter/paragraph spacing (quick check: set 1.5x line height, 2x paragraph spacing and look for clipping).

## Keyboard access

The keyboard pass finds the failures screen readers inherit, because if it is not focusable, it is not operable.

- **SC 2.1.1 Keyboard:** every action reachable by keyboard — links, buttons, form fields, custom widgets, modals, media controls. No keyboard-only traps (SC 2.1.2: focus can always leave a component, modals return focus on close).
- Tab order follows visual/logical reading order. A tab order that jumps from the header to a mid-page promo before the primary form is a finding.
- Focus is always visible (SC 2.4.7): a visible indicator on every focused element, meeting the 3:1 non-text contrast floor. `outline: none` with no replacement is a finding on sight.
- Custom components (tabs, accordions, dropdowns, modals) implement the expected keys: arrow keys move between tabs/options, Enter/Space activate, Escape closes modals (pattern behavior in `references/interaction-patterns.md`).
- No hover-only reveals: any content shown on hover must also appear on focus (SC 1.4.13 Content on Hover or Focus).
- Skip navigation exists on long pages so keyboard users can pass repeated header content (SC 2.4.1 Bypass Blocks).

## Forms and labels

- Every input has a visible, persistent label associated programmatically (`<label for>` or equivalent). Placeholder-only labeling is a finding twice over (contrast and label persistence).
- **SC 3.3.1 Error Identification:** errors are described in text to the user, not just colored borders or icons.
- **SC 3.3.2 Labels or Instructions:** required fields and formats are stated in text ("Card number (16 digits)") — an asterisk with no legend does not satisfy it.
- **SC 3.3.3 Error Suggestion:** error messages recommend the correction where known ("ZIP must be 5 digits — you entered 4").
- **SC 3.3.4 Error Prevention (Legal, Financial, Data):** for irreversible or financial submissions — a checkout's place-order button, a delete — one of: reversible submission, reviewed-and-confirmed step, or validated input. This is why review steps and confirm dialogs matter on payment screens.
- Autocomplete attributes on personal-data fields (`name`, `email`, `street-address`, `cc-number`) per SC 1.3.5 Identify Input Purpose.

## Screen reader basics

You can find most blockers without a screen reader, but the label/role/value pass needs one. Verify by inspection first, then flag what needs AT verification:

- Every image has appropriate alt text: meaningful images describe their content and purpose; decorative images are explicitly hidden (`alt=""`); images of text are avoided (SC 1.4.5). "Image" or the filename as alt text is a finding.
- Buttons and links have discernible text — icon-only buttons need accessible names ("Remove item from cart", not an unlabeled X). Links say where they go, not "click here" (SC 2.4.4 Link Purpose).
- **Name, Role, Value:** custom widgets expose name, role, and value to assistive technology (SC 4.1.2). A styled `<div>` acting as a button is a finding; a `<button>` with styles is not.
- Headings form an outline (`h1`–`h6`, no skipped levels) so screen-reader users can navigate by structure (SC 1.3.1 Info and Relationships; SC 2.4.6 Headings and Labels).
- Status messages are announced without moving focus (SC 4.1.3 Status Messages) — toasts and inline "saved" confirmations need the right semantics.
- Reading order matches visual order; CSS reordering that scrambles the DOM sequence is a finding.
- Page has a descriptive title and landmarks (`main`, `nav`) so AT users can orient (SC 2.4.2 Page Titled).

## Vision beyond contrast

- **SC 1.4.4 Resize Text:** content survives 200% zoom without loss of function — no clipped columns, no hidden CTAs.
- **SC 1.4.10 Reflow:** at 320px width, no two-dimensional scrolling for single-column content.
- **SC 1.3.4 Orientation:** content does not lock to portrait or landscape.
- **SC 2.3.3 Animation from Interactions** and `prefers-reduced-motion`: motion honors the setting; parallax and large auto-playing movement get an off switch.
- **SC 2.5.8 Target Size (Minimum) (2.2):** targets at least 24x24 CSS px (the older, stricter 44/48px guidance remains best practice — see `references/layout-and-spacing.md`).

## Screen-reader spot checks

When you have a build (not just static screens), run this five-minute pass with the platform's built-in reader (VoiceOver, Narrator, TalkBack):

1. Navigate by headings: does the outline match the page's structure?
2. Tab through the primary path: does every control announce name and role? Does focus visibly move?
3. Submit the form empty: is the error announced?
4. Open and close the modal: is focus trapped inside and returned on close?
5. Trigger a toast: is it announced?

Record which checks you could run versus which need a real AT session — honesty about verification depth is part of evidence discipline (see `references/critique-principles.md`).

## What the pass cannot certify

- Full conformance requires assistive-technology testing across platform combinations, automated scans, and user testing — outside this skill's scope.
- Treat this checklist as a *screening* pass: it finds the common blockers and the citation-backed requirements, and it tells the team exactly what a professional audit will still need to cover.

## Accessibility checklist summary

Run in this order; each unchecked item is a candidate finding:

1. Contrast: text pairs, component boundaries, focus indicators.
2. Keyboard: complete reachability, visible focus, no traps, logical order, skip link.
3. Forms: labels, error text, suggestions, error prevention on financial/legal submits.
4. Alt text and accessible names: images, icon buttons, link purpose.
5. Structure: heading outline, landmarks, page title, reading order.
6. Reflow: 200% zoom and 320px width survival; orientation freedom.
7. Motion: reduced-motion honored; hover-only content also on focus.
8. Status: messages announced; modals trap and restore focus.