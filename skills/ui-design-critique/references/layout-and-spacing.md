# Layout and Spacing

Methodology for judging grids, spacing systems, density, and alignment. Layout findings are the highest-yield category in most critiques because spacing and alignment problems are measurable, cheap to fix, and visible to every user even when they cannot name what is wrong.

## The grid

A grid is the invisible set of columns and gutters that elements snap to. You rarely see it, but you feel its absence: elements that almost line up, ragged left edges, columns that wander as you scroll.

- **Columns:** 12 columns is the standard for responsive desktop; 4 or 6 for narrower layouts. On mobile, a single column with consistent margins is the grid.
- **Gutters:** the space between columns, typically 16–32px on desktop, 16px on mobile.
- **Margins:** the outer edge padding, typically 24–48px on desktop, 16–24px on mobile.
- **Snap discipline:** every element's left and right edge should land on a column or margin line. Half-aligned elements are findings even when nothing else about them is wrong.

When auditing: pick three horizontal reference lines (one per screen third) and check which elements' edges align. Misalignment across those three lines is evidence; "things look off" is not.

## Spacing systems

Professional layouts use a small spacing scale — one set of values, applied everywhere — instead of ad-hoc pixel choices.

- A working scale: 4, 8, 12, 16, 24, 32, 48, 64 (multiples of a 4px or 8px base unit).
- Audit by extracting the actual gaps: measure vertical space between sibling cards, between a label and its input, between sections. Values that appear once and appear nowhere else in the system are scale violations.
- The report should say it with numbers: "seven distinct values (8, 10, 14, 18, 24, 30, 40px) play the role of 'gap between form rows'; a 3-value scale (8, 16, 24) covers all cases."

### Semantic spacing roles

Spacing carries meaning through consistent roles. Name the roles, then check they are used consistently:

- **Tight (4–8px):** inside a component — label to input, icon to text.
- **Base (12–16px):** between sibling items in a group — list rows, form fields.
- **Group (24–32px):** between related groups — address block to delivery block.
- **Section (48–64px):** between major page areas — content to footer.

The strongest spacing findings are role violations: group-level space applied inside a component splits a unit apart, or tight space applied between groups crams unrelated things together. Proximity is the user's only grouping signal — the gestalt principle that near things belong together is doing real work here.

A second class of finding is token drift: the same role rendered at 14px here and 16px there because two screens were built at different times. Drift is what a spacing audit exists to catch, and it is invisible without extracting the values.

## Whitespace as structure

Whitespace is not empty; it delimits groups and creates rhythm.

- Text paragraphs breathe with 1.5–2x line-height in surrounding space terms; do not crush body copy against headings.
- Cards and panels need internal padding at least as large as the gap between neighboring cards, or the card boundary reads as arbitrary.
- Uniform whitespace everywhere is as bad as none: if all gaps are equal, hierarchy (see `references/visual-hierarchy.md`) has no spatial tool left. Vary the gap by role and the structure becomes visible without lines or boxes.
- Symmetry check: groups held together by proximity should not also be split by equal surrounding space. If a heading is equidistant from the section above and its own content below, proximity is broken and the heading appears to belong to the wrong block.

## Density

Density is the amount of information per screen area, and it must match the task.

- **Low density (generous spacing):** marketing pages, onboarding, confirmation screens — where reassurance and clarity beat throughput.
- **Medium density:** most product pages, settings, checkout steps.
- **High density (tight, compact rows):** data tables, dashboards, admin lists — where expert users scan many items.

Density findings are always relative to the task: a settings page with dashboard-density feels cramped and anxious; a data table with marketing whitespace wastes half the screen and buries the scan. Judge density by asking what the user does on the screen — read and decide, or scan and compare — not by how it looks in isolation.

## Alignment

Pick one alignment scheme per axis and enforce it.

- **Left-align text** by default; centered text is for standalone headings, hero statements, and empty-state messages only. Centered form labels and body paragraphs are findings.
- **Right-align numbers** in columns (prices, quantities, totals) so digits line up; keep the decimal point in one visual position with a tabular font feature where available (see `references/typography-basics.md`).
- **Baseline alignment:** the text baselines of side-by-side elements should match, not just their boxes. A button label floating 3px above its neighbor's label reads as sloppiness nobody can name.
- **Consistent edge:** one content left edge per screen. Indented exception blocks are fine; five different left edges are not.

## Touch targets and reachability

On touch interfaces, layout has a physical floor:

- Minimum 44x44pt (iOS HIG) / 48x48dp (Material) for interactive targets, with spacing between adjacent targets so a thumb cannot press two at once. (WCAG 2.2's floor is smaller — 24x24 — but the platform floors remain best practice; see `references/accessibility-review.md`.)
- Primary actions in the lower half of a mobile screen — the thumb zone; corners of the viewport are the worst positions.
- Destructive actions placed away from high-traffic targets and never adjacent to their safe counterpart (delete next to save invites mis-taps).

## Responsive behavior

Layout findings must hold at more than one width when both are in scope:

- Check the breakpoints the product ships: does the 12-column desktop layout collapse cleanly to the mobile single column, or does content reflow into dead zones?
- Grids that break at 768px (the tablet gap) produce orphan columns and stretched cards; note the width where each break happens.
- Text containers should reflow, not rescale: fixed-width content columns force horizontal scrolling on narrow viewports (see SC 1.4.10 Reflow in `references/accessibility-review.md`).

## Layout audit procedure

1. Identify the grid or infer it; check margin and gutter consistency.
2. Extract the spacing values in use; compare against a scale; count the distinct values per semantic role.
3. Check alignment: one left edge, right-aligned number columns, baseline-aligned side-by-side elements.
4. Run the three-line alignment check on each screen third.
5. Judge density against the task; flag screens whose density contradicts their job.
6. Verify touch-target sizes and thumb-zone placement on mobile.
7. Convert each deviation into evidence-based findings: value in pixels, element, location, and the scale or role it breaks (severity per `references/critique-principles.md`).