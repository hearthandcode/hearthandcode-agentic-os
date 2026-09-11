# Color and Contrast

Rubric for judging palette, contrast ratios, and semantic color use. Color is the most subjective-looking discipline in UI critique, which is exactly why it needs numbers: contrast ratios and role discipline turn "the gray looks muddy" into findings a team can act on.

## Palette roles

Judge color by what each color is *for*, not by whether the hues are pretty. A healthy product palette has named roles, and every use of color maps to one:

- **Primary / brand:** the identity color, used sparingly for the brand presence and the single primary action.
- **Action:** interactive affordances — buttons, links, focus rings. One action color family, used consistently.
- **Feedback:** success (green family), warning (amber family), error (red family). Feedback colors never double as decoration.
- **Neutrals:** the grays that carry text, borders, and surfaces — typically a ramp of 8–12 steps from near-black to near-white.

Audit method: list every distinct color on the screen and assign it a role. Colors with no role (a decorative teal on a payment screen) and roles with competing colors (two different blues for links) are findings. A common structural finding: the palette has 14 colors where 9 roles exist, because neutrals were chosen ad-hoc per screen instead of as a ramp.

## Contrast ratios

Contrast is measurable and regulated. WCAG (see `references/accessibility-review.md` for the full checklist) sets the floor:

| Ratio | Applies to | WCAG criterion |
| --- | --- | --- |
| 4.5:1 | Normal text (under 24px, or under 19px bold) | 1.4.3 Contrast (Minimum) |
| 3:1 | Large text (24px+, or 19px+ bold) | 1.4.3 Contrast (Minimum) |
| 3:1 | UI components and graphical objects (input borders, icons, focus indicators) | 1.4.11 Non-text Contrast |
| 7:1 / 4.5:1 | Enhanced, treat as aspiration: normal text 7:1, large text 4.5:1 | 1.4.6 Contrast (Enhanced) — AAA |

Compute ratios from hex values; do not eyeball. The classic borderline failures are everywhere in real products:

- Gray placeholder text at #9CA3AF on white: ~2.5:1 — fails 4.5:1 for normal text.
- A yellow warning banner with white text: often 1.6–2.1:1 — fails catastrophically.
- Light gray borders (#E5E7EB on white: ~1.4:1) around text inputs — below the 3:1 component minimum, so the input's boundary is invisible to low-vision users.
- Focus indicators styled as a subtle shadow — effectively invisible against the component minimum.

Placeholder text is held to the same 4.5:1 standard as any text; "it's supposed to look subtle" is not an exemption, it is a design problem to solve with patterns (see `references/interaction-patterns.md`), not with low contrast.

## Contrast audit method

1. Extract every text/background pair and component boundary from the screen.
2. Compute the ratio for each (any WCAG contrast calculator, or the relative-luminance formula).
3. List failures with the pair, the computed ratio, the required ratio, and the criterion number.
4. Check the *disabled* state: disabled controls are exempt from 1.4.3, but users still need to tell disabled from enabled — note when the only difference is a contrast drop.
5. Check hover and focus states; they inherit the same floors and are skipped more often than base states.

Report format: "Placeholder 'Enter phone number' renders at #9CA3AF on #FFFFFF (2.5:1) — fails WCAG 1.4.3's 4.5:1 minimum; darken to a 4.5:1-passing neutral or use a floating label."

## Semantic color

Semantic color is where palettes earn or lose trust. The color must agree with the meaning everywhere in the product.

- **Red = destructive or error.** Never a promotion, never a "hot deal" price, never a decorative accent — or the real error state loses its meaning. A red "Save" button adjacent to red error text is a finding even if both are individually defensible.
- **Green = success or confirmation.** A green order-confirmation banner should share its family with inline "saved" feedback, not with a "go bargain hunting" CTA.
- **Amber/yellow = caution** requiring acknowledgment, not ambient decoration.
- **Blue/purple links:** once a product uses blue for links, any other blue text reads as clickable. Stripped links that still look like links are findings (see `references/interaction-patterns.md` on affordances).

Consistency checks across screens, not just within one:

- Error text uses the same red and the same styling pattern on every screen.
- Primary buttons keep one color; "the CTA is blue on step 2 and green on step 4" is a coherence finding.
- Badge and status colors map 1:1 to statuses — two statuses sharing one color defeats the system.

## Color and meaning beyond hue

Never let color alone carry meaning (WCAG 1.4.1 Use of Color): error text needs an icon or a text prefix, not just red; required fields need a marker, not just an asterisk color; chart series need labels or patterns, not just distinct hues. Colorblind users — roughly 1 in 12 men for red-green deficiency — read these screens every day.

Check icon-only and status elements under three simulations (any colorblindness simulator): protanopia, deuteranopia, tritanopia. If two states become indistinguishable, the finding is "state relies on hue alone."

## Color proportions

A working screen's palette follows a rough weight distribution — approximately 60% neutral surfaces and text, 30% secondary neutrals and imagery, at most 10% accent (the action color). Screens that invert this — large saturated fields of brand color on task surfaces — spend the action color's attention budget on decoration, and the primary action stops reading as primary. This proportion rule is the color-side sibling of the emphasis budget in `references/visual-hierarchy.md`.

## Dark mode considerations

When a dark theme exists, audit it as a first-class palette, not an inversion:

- Elevation via lighter surfaces (dark mode convention) rather than drop shadows, which disappear on dark backgrounds.
- Saturation restrained: fully saturated brand colors vibrate on dark backgrounds; desaturated tints read better.
- Contrast requirements do not relax: white-on-dark text still needs 4.5:1; pure white on pure black causes halation for astigmatic users — prefer off-white (#E5E7EB range) on near-black.
- Audit dark mode with the same extraction method; a dark theme that was auto-inverted almost always fails semantic color (the "warning amber" becomes unreadable mud) and neutral ramps (grays that assume a white surface).

## Color rubric summary

1. Every color maps to a named role; no role has two competing colors.
2. All text pairs meet 4.5:1 (normal) or 3:1 (large) per WCAG 1.4.3.
3. Component boundaries and focus indicators meet 3:1 per WCAG 1.4.11.
4. Semantic colors are consistent across screens and never reused against their meaning.
5. No meaning is carried by hue alone (WCAG 1.4.1).
6. Disabled states remain distinguishable from enabled ones.
7. Dark mode (if present) passes the same floors as a first-class palette.