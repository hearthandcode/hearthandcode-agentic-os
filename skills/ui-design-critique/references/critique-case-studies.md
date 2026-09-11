# Critique Case Studies

Three complete screens critiqued end to end, showing how the methodology in the other references converts raw observation into scored findings. All products and numbers are fictional. Each case shows: the goal, the first-fixation reading, the findings with evidence, and the after state. Use these as calibration for your own severity calls.

## Case 1 — "Meridian Bank" transfer screen (mobile)

**Goal sentence:** A checking customer can send money to a saved payee in under a minute, confident the amount and recipient are right.

**First-fixation test:** What lands first is the "Move your money" marketing headline, set at display size in brand teal. The transfer form sits below in small gray type. The required order (form → confirm button → promo) is inverted: the screen emphasizes a marketing message on a task screen.

**Raw notes (before cleaning):**

- Banner huge, form tiny — why is marketing on the transfer screen?
- Typed "12.345" — Continue tapped — red box at top, field itself unmarked
- Amount digits wobble next to the balance line
- Four grays playing "surface" (#F5F5F5, #F6F6F6, #FAFAFA, #EEE)
- Colors feel a bit corporate? (preference — discarded, no principle)

Merged: the four-grays note stays one finding with four evidence points; the "colors feel corporate" note dies as taste.

**Findings (scored):**

1. **P1 — Promo headline out-shouts the form.** Evidence: 40px teal headline vs. 14px gray form labels; first fixation on the banner. Principle: emphasis budget, one primary focal point (`references/visual-hierarchy.md`). Fix (rung: demark): demote the banner to a 16px text line above the form.
2. **P1 — Amount errors surface only after tapping Continue, far from the field.** Evidence: submitting "12.345" produces a red summary box at the top; the field itself shows no state. Principle: validate on blur, near the field (`references/interaction-patterns.md`). Fix (rung: restyle): validate on blur, place the error under the field, state the format ("Amounts to 2 decimal places").
3. **P2 — Amount uses proportional figures.** Evidence: "1,000.00" digits wobble in width; amounts hard to compare with the balance line. Principle: tabular figures for number columns (`references/typography-basics.md`). Fix: enable tabular numerals for all money values.
4. **P2 — Neutrals drift.** Evidence: four grays play "surface" on one screen. Principle: single neutral ramp, named roles (`references/color-and-contrast.md`). Fix: collapse to two surface tokens.

**After:** Banner reduced to one 16px line; amount field validates on blur with an inline, actionable error; money values use tabular figures; two surface grays remain. Their (fictional) usability test moved median transfer time from 54s to 38s. The point: each fix traced to a named principle, so the redesign could be measured against the same goals it was judged by.

## Case 2 — "Hearthside Goods" product listing page (desktop e-commerce)

**Goal sentence:** A gift shopper scanning 24 products can compare and shortlist items without opening each one.

**First-fixation test:** Equal visual weight everywhere: all 24 product cards identical in emphasis, titles 15px, prices 15px, no hover state. Nothing is primary — but a listing page's job *is* uniform scanning, so uniformity is correct here; the failure is elsewhere.

**Raw notes (before cleaning):**

- Nothing pops (preference? no — tested against goal: scanning wants uniformity; not a finding)
- Card 7's title wraps to three lines; its price sits lower than neighbors
- Rating only appears on hover — keyboard user never sees it
- Two blues: product links #2563EB, "See more" links #3B82F6
- Cards feel puffy inside (40px padding) but tight between (12px gutters)
- Grid gap inconsistent (later measured: 12px between rows, 24px between columns — intentional masonry? no: sloppiness)

Merged: "puffy inside / tight between" and the grid-gap note are one spacing finding with two measurements.

**Findings (scored):**

1. **P2 — Key compare data lives only on the hover state.** Evidence: material and rating appear in a hover overlay; keyboard users never see it and touch users get nothing. Principle: no hover-only reveals (SC 1.4.13, `references/accessibility-review.md`; behavior catalog in `references/interaction-patterns.md`). Fix: show rating on the card; move material to a filter facet.
2. **P1 — Grid misalignment.** Evidence: card 7's title wraps to three lines and its price sits 6px lower than neighbors; rows don't share a baseline. Principle: baseline alignment and one left edge (`references/layout-and-spacing.md`). Fix: clamp titles to two lines with an ellipsis, reserve the space, align prices by row.
3. **P2 — Two blues.** Evidence: product links #2563EB, "See more" links #3B82F6 — indistinguishable roles. Principle: one action color family per role (`references/color-and-contrast.md`). Fix: make "See more" a neutral text link with a chevron.
4. **P3 — Density mismatch.** Evidence: 40px padding in cards, 12px gutters — internal padding exceeds the inter-card gap, so boundaries read as arbitrary. Principle: internal padding should not exceed the inter-card gap (`references/layout-and-spacing.md`). Fix: 16px internal padding, 24px gutters.

**Severity note:** the alignment issue outranks the color split because it breaks scanning for *every* user on *every* row, while the two-blues issue costs only a little confidence in link affordance. Same "P-level-adjacent" issues; impact decides.

## Case 3 — "OrbitDesk" settings page (desktop SaaS)

**Goal sentence:** An account admin can find and change a workspace setting in under two minutes without reading documentation.

**First-fixation test:** A 60-item accordion list of settings with equal visual weight, 10px row spacing, no search, and a "Save" button that appears only after scrolling past the last item. Uniformity here *is* a failure — unlike Case 2 — because the task is find-one-setting, not scan-and-compare. Match the pattern to the task, never the reverse.

**Raw notes (before cleaning):**

- 60 items, no grouping, no search
- Edit three fields, click a nav item to billing — edits gone, no warning
- Save button only at the very bottom
- Section rhythm random (32px then 16px between sections)
- Checkbox labels read like legal text (kept as a finding only for the two labels under 60 characters — the rest is content, not UI)

**Findings (scored):**

1. **P0 — Unsaved-changes loss.** Evidence: navigating to a different settings section discards edits silently; no warning, no draft. Principle: never lose user data on navigation (`references/interaction-patterns.md`); error prevention (SC 3.3.4, `references/accessibility-review.md`). Fix: persist per-section drafts, or confirm before navigating away with unsaved edits.
2. **P1 — No navigation structure.** Evidence: 60 accordions in one column, no categories, no search; finding "invoice email" requires scanning all 60 rows. Principle: density and information architecture must match the task (`references/layout-and-spacing.md`). Fix: group into 5–7 categories with a left nav and a search box.
3. **P2 — Save discoverability.** Evidence: Save sits at the list's very bottom, off-screen during editing. Principle: the primary action stays reachable (see `references/visual-hierarchy.md`). Fix: sticky save bar that appears when the form is dirty.
4. **P3 — Inconsistent section rhythm.** Evidence: section headings sometimes 32px from prior content, sometimes 16px. Principle: semantic spacing roles (`references/layout-and-spacing.md`). Fix: section gap 32px everywhere.

**What was deliberately not a finding:** the legal-style label copy and the accordion pattern itself. The goal was findability; grouping and search solve it; converting 60 accordions to a full settings page redesign would fail the fix ladder (see `references/visual-hierarchy.md`) — a bigger change than the evidence demands.

## Calibration takeaways

- The P0 in Case 3 is a behavior failure, not a visual one — the screen looks fine in a screenshot. Flow critiques that skip interaction probing (submit, navigate away, double-tap) miss their most severe findings.
- Case 2 shows uniformity *passing* the hierarchy test: match the pattern to the task before calling it a failure.
- Raw-note lists always contain taste ("colors feel corporate") and duplicates; the cleaning pass in `references/critique-principles.md` is where 5 notes become 4 findings.
- Every finding above cites its reference file and, where relevant, names its fix-ladder rung. That is the standard for this skill's reports: no orphan judgments.
- Fictional numbers (54s, 60 items, 24 cards) make evidence concrete; real critiques substitute their measured values.