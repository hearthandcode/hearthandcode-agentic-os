# Typography Basics

Rubric for judging type: scale, measure, leading, pairing, and legibility. Typography failures are silent — users blame themselves for misreading, or simply trust the interface less — which makes them high-value findings that no user complaint will ever surface.

## Type scale

A type scale is the set of allowed font sizes and their roles. Judge both the steps and the adherence.

- **Number of sizes:** 5–8 sizes covers almost any product (caption, body, body-strong, subtitle, heading levels 1–3, display). More than 10 distinct sizes on one screen is a finding on its own.
- **Consistent steps:** sizes should follow a ratio (1.25 "major third" and 1.333 "perfect fourth" are common) or a documented ladder. Random sizes (15, 17, 22, 26px) are scale violations.
- **Roles, not just sizes:** each size owns a role — body text, section heading, caption. The same role must use the same size everywhere. A "step title" at 18px on one screen and 16px on another is a finding even though both are readable.
- **Minimum sizes:** 16px for body text on the web (12px absolute floor, and only for legally constrained labels); nothing interactive below 16px on mobile, or iOS zooms the input on focus.

Audit method: list every font size on the screen with the elements using it. The raw count and the duplicates are the evidence — "11 sizes where 6 roles suffice" needs no further argument.

## Measure (line length)

Measure is the width of a text line, counted in characters.

- **Ideal: 45–75 characters** per line for body text; ~66 is the classic target.
- Under 45 reads choppy; over 75 the eye loses the return path to the next line and rereads.
- Full-viewport-width paragraphs are the most common violation on wide screens. Constrain body text with a max-width (roughly 600–720px at 16–18px) rather than trusting the grid to keep prose narrow.
- Tables, code, and data grids are exempt — they scan by cell, not by line.

Count characters, not pixels: measure a representative body paragraph by dividing its width by average character width, or count directly. Report the number: "body paragraphs run 110–130 characters across, past the 75-character ceiling."

## Leading (line height)

Leading is the vertical space between lines.

- **Body text: 1.4–1.6x** the font size. 1.2 is fine for large display headings only.
- Dense UI text (tables, labels) can drop to 1.2–1.3; long-form reading wants 1.6–1.8.
- Leading interacts with measure: long lines need more leading, short lines less. A 90-character line at 1.3 leading is doubly wrong.
- Headings with wrapped lines need leading near 1.1–1.25 so multi-line headings read as one unit.

## Weight and emphasis

- Use at most 2 weights in running interfaces (regular + one heavier); 3 when a light display face is genuinely needed. Every additional weight dilutes the emphasis system.
- Emphasis inside body text: weight or color, not underline (reserved for links) and not italics at small sizes.
- All-caps for anything longer than a short label is a legibility finding: word shapes vanish and reading speed drops. All-caps works for buttons, badges, and short overlines only.

## Font pairing

Pairing means choosing two (rarely three) typefaces with distinct, complementary roles.

- **One-family solutions are legitimate:** a variable family with a strong weight range often beats two families. Do not invent a pairing problem where role discipline would fix the screen.
- When two families are used, the split should be by role (display vs. body, headings vs. UI), not by screen. The same role must keep its face everywhere.
- Pair by contrast, not similarity: a geometric sans with a humanist serif reads as intentional; two humanist sans faces read as a rendering bug.
- Check the fallback stack: if the webfont fails, does the fallback preserve approximate metrics? A layout that jumps when the font loads is a real finding — users lose their place mid-sentence.

## Legibility

Legibility is the letter-level property: can a user decode glyphs quickly?

- **x-height:** prefer larger x-heights for UI text; tiny x-heights at small sizes are unreadable on low-DPI screens.
- **Letter spacing:** default tracking for body; slight positive tracking for all-caps labels; negative tracking only at display sizes.
- **Line height vs. touch:** tappable text rows need vertical padding — text set on a 16px line with 8px padding gives a usable target; text set edge to edge does not.
- **Numerals:** proportional figures wobble in running text, which is fine for prose; columns of numbers (prices, quantities, totals) need tabular figures so digits align down the column.
- **Anti-patterns:** justified text (rivers of white), long strings of digits in proportional figures, text over busy images without a scrim, and light gray-on-white "subtle" body copy (contrast is a color problem — see `references/color-and-contrast.md`).

## Accessibility floor for type

These overlap the full checklist in `references/accessibility-review.md`; apply them inside typography findings rather than deferring everything:

- Text resized to 200% via browser zoom must still be readable and not clipped (WCAG 1.4.4 Resize Text).
- No information conveyed by font size or weight alone — emphasis must pair with a second signal (the sibling logic of WCAG 1.4.1 Use of Color).
- Real text, not images of text, wherever possible (WCAG 1.4.5 Images of Text).

## Typography rubric summary

Score each screen against these checks; each failure is one finding with the count or measurement as evidence:

1. Size inventory: 5–8 sizes, documented scale, consistent roles.
2. Measure: body text 45–75 characters.
3. Leading: 1.4–1.6x body; tighter only for dense UI.
4. Weights: 2–3 maximum, applied by role.
5. Pairing: role-based, contrast-based, consistent across screens.
6. Body size floor: 16px web body; nothing interactive under 16px on mobile.
7. Caps discipline: short labels only.
8. Legibility killers: justification, proportional figures in columns, text over busy imagery.

When a screen fails several checks at once, report them as one consolidated typography finding with per-check evidence, not as eight separate findings — the cap on delivered findings (see `references/critique-principles.md`) applies to typography too.