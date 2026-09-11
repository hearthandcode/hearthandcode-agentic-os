---
name: ui-design-critique
description: >
  Load this skill when you are reviewing or critiquing a user interface —
  screens, flows, screenshots, or a design file before build or before
  redesign — or when a team asks "is this UI good enough to ship" and the
  answer must become a prioritized, evidence-backed findings list rather than
  a stream of opinions. Also for redesign scoping, comparative reviews,
  post-launch friction triage, and design-system conformance spot-checks. It
  produces a severity-ranked critique report (P0 blocker to P3 polish) in
  which every finding carries evidence, the violated principle, and a
  concrete recommended fix. Understandable cold: no prior use of this
  repository is assumed.
---

# ui-design-critique

## 01 — Purpose

UI critique has a reputation problem: design reviews routinely degrade into taste
arguments ("I don't like the blue") that produce no decisions, no ownership, and no
fixes. A review that ends in opinions gets relitigated next meeting, the real
findings never get scheduled, and the team learns that design review is where an
hour goes to die. This skill imposes a method on the review of any user interface —
mobile or desktop, product or marketing, design file or running build — so the
output is a ranked list of defensible findings, each tied to a named principle and
a recommended fix, instead of a stream of impressions.

The method runs in three movements. First, establish the standard: what each screen
is for, for whom, and what success looks like — a finding is a measurement, and a
screen without a goal sentence cannot produce findings yet. Second, inspect: walk
the flow as a user would, probe the unhappy paths, then run six lenses per screen —
visual hierarchy, layout and spacing, typography, color and contrast, interaction
patterns, and accessibility. Third, convert: raw observations become findings in a
fixed four-part format (severity, evidence, principle, fix) defined in
`references/critique-principles.md`, and findings become a capped, severity-ranked
report built on `templates/critique-report-template.md`.

The pass scales by verification depth, not by skipping steps: a staging build gets
behavior findings verified; static exports get the same lenses with behavior
labeled "assumed — verify in build," and the report says which kind of run it was.
The reference files carry the doctrine while this file stays procedure. What
separates professional critique from taste is traceability — every judgment must
trace to the screen's goal, observable evidence, and a written principle — and
this skill teaches you to discard your own preferences rather than ship them.

**Three outcomes this skill owns:**

1. A prioritized critique report a team can execute: severity-ranked findings with
   evidence, principle, and fix — capped, ordered, honest about severity shape.
2. A walkthrough record that shows the work: goal captures, first-fixation
   readings, and the raw observation list, so the report survives re-review.
3. A severity call a team can trust: ranked by user impact alone, effort stated
   separately, no inflated blockers, distribution stated up front.

## 02 — When to Use / When Not to Use

### Use this skill when:

1. **A team asks "is this ready to hand to engineering?"**
   - Pre-ship design review of screens in a design file or staging build, with
     severities the team can schedule against.
2. **An existing flow underperforms and someone must say what is wrong.**
   - Redesign scoping: support tickets or drop-off analytics converted into
     twelve concrete problems with fixes, replacing "it feels confusing."
3. **You are comparing two interfaces.**
   - The same lenses applied to two flows produce comparable finding lists; the
     delta answers "why does theirs feel better?"
4. **A shipped feature generates complaints or abandonment.**
   - Post-launch friction triage: walk the flow, reproduce friction on the
     unhappy paths, separate real interaction failures from visual noise.
5. **New screens claim to follow the design system but may drift.**
   - Conformance spot-check: the audit methods in
     `references/layout-and-spacing.md` and `references/color-and-contrast.md`
     catch type-scale, spacing-token, and semantic-color drift with measured
     values.
6. **A designer asks for critique of portfolio or case-study work.**
   - The same method applies, with the goal sentence supplied by the designer's
     stated intent rather than by analytics.

### Do NOT use this skill when:

1. **You are generating a new design, not judging an existing one.**
   - Ideation and wireframing are creation work; use `design-system-foundations`
     when the question is "what should our system be?" rather than "does this
     screen conform and perform?"
2. **You are verifying implementation quality of shipped code.**
   - Whether the build matches the spec, tests are right, code is sound — that is
     engineering review. Use `code-review` or `testing-strategy`.
3. **You are tuning game feel, difficulty, or level structure.**
   - Game interfaces borrow from UI critique, but their core questions — pacing,
     challenge curves, readability at 60 frames per second — live elsewhere. Use
     `level-and-encounter-design`.
4. **A compliance-grade accessibility audit is requested.**
   - This skill runs an accessibility *pass* (essentials in
     `references/accessibility-review.md`), but AT testing sessions, conformance
     reports, and VPATs need dedicated tooling this skill does not provide.
5. **The requester wants inspiration, not findings.**
   - Moodboard-style feedback ("show me bold checkout pages") is research, not
     critique; use `brainstorming-and-ideation` — this skill produces the wrong
     artifact.
6. **The artifact is not an interface.**
   - Documents, emails, and slide decks need editorial review; lenses like
     contrast, touch targets, and focus order do not apply. Apply editorial
     judgment directly.

Boundary rule of thumb: if the deliverable is a *findings report about an existing
interface*, this is the skill. If the deliverable is a *new artifact*, a *codebase
verdict*, or a *compliance document*, it belongs elsewhere.

## 03 — Inputs and Outputs

### Inputs

You must have the first two before starting; the rest sharpen the critique but
cannot be invented later without asking:

- **The screens.** Design-file exports, screenshots, or a live or staging build.
  Statics are enough for the visual lenses; a build is required to verify behavior
  (validation timing, keyboard flow, double-submit protection).
- **The flow order and the goal.** Which screens belong to the task, in what
  sequence, for which user, serving what task. If unstated, ask in workflow step
  1 — critiquing a guessed flow critiques the wrong journey, and critiquing
  without a goal produces taste.
- **Constraints** (optional but valuable): platform requirements, brand systems
  that must stay, deadlines, dark-theme existence, prior research. Each changes
  severity calls and fix choices.
- **Scope boundaries.** Critiques that wander past scope spend credibility on
  screens nobody asked about.
- **For self-critique:** your own screens plus five minutes of honesty about
  which parts you are least sure of — state known weaknesses instead of letting
  review discover them.

### What good inputs look like

- Five screens or fewer per session reviews deeply in one sitting; larger flows
  review better split by sub-flow.
- A staging build converts "assumed" behavior findings into verified ones — the
  most severe findings in flow critiques live in behavior, not visuals.
- Real content (actual prices, product names) instead of lorem ipsum: fake
  content hides measure, truncation, and wrapping problems the lenses exist to
  find.

### Outputs

1. **A critique report** built on `templates/critique-report-template.md`:
   goal capture, what-works, findings ordered P0 → P3, open questions,
   assumptions, appendix. Every finding follows the four-part format defined in
   `references/critique-principles.md`. Twelve findings is the default cap for
   a five-screen flow.
2. **A walkthrough record:** per-screen goal sentences, first-fixation readings,
   and the raw observation list — kept in the report annex or session notes,
   because re-review always asks "what did you actually look at?"
3. **A severity distribution statement** ("2 P0, 5 P1, 4 P2, 1 P3") at the top of
   the report, so the reader sees the shape of the problem before reading any
   finding.
4. **A verbal findings summary** for synchronous reviews: the top three
   findings, each under thirty seconds, so the meeting starts with decisions.

The report is the only artifact the requester must receive; the walkthrough record
makes it defensible when challenged. For the full shape of a finished deliverable,
see `examples/worked-ui-critique.md`.

## 04 — Workflow

A complete critique has fifteen steps: 1-4 build the standard and the raw
material; 5-10 are the six lenses; 11-13 convert observations into a ranked
findings list; 14-15 deliver. Skipping the unhappy paths (step 4) to jump to
visual opinions is the most common way critiques go wrong. Each step names its
reference and a checkpoint question; in autonomous runs, replace each checkpoint
with a stated assumption recorded in the report's Assumptions section.

### Step 1 — Confirm intake and scope
**Reference:** `references/critique-principles.md`

- Collect screens, flow order, goal, user, and scope; ask now about anything
  missing. Note the input format (statics versus build): it caps what you may
  claim later. Write the out-of-scope line before looking at any screen.
- Checkpoint: "Flow to critique: [list]. What is out of scope? Build or
  statics?"

### Step 2 — Capture goals per screen
**Reference:** `references/critique-principles.md`

- Write the goal sentence for every screen: "This screen exists so that [user]
  can [task], and success looks like [outcome]" — the standard every finding is
  measured against. If the requester cannot state a goal, propose one and mark
  it as proposed.
- Checkpoint: "Is payment success 'paid without double-charge' — or also 'chose
  the cheapest option'? These produce different findings."

### Step 3 — Walk the flow as a user
**Reference:** `references/interaction-patterns.md`

- Move through every screen in order, doing the task, noting friction the moment
  you feel it — where you hesitated, what you hunted for, what you misread. This
  pass generates raw observations, not findings; resist scoring anything yet,
  and capture the walkthrough in the user's words, not the layer names.
- Checkpoint: "I hit friction at the promo-code field — intentional or legacy?"

### Step 4 — Probe the unhappy paths
**Reference:** `references/interaction-patterns.md`

- Submit empty forms and invalid data, double-tap the primary action, press
  back mid-form, trigger the error states and — on a build — drop the network
  mid-submit. The most severe findings in flow critiques nearly always come
  from this step (see the OrbitDesk case in
  `references/critique-case-studies.md`); when the inputs omit error and empty
  states, request them explicitly — a missing error state is a finding.
- Checkpoint: "May I submit a real test-mode payment on staging, or stop at the
  form's validation layer?"

### Step 5 — Run the first-fixation test per screen
**Reference:** `references/visual-hierarchy.md`

- Three seconds per screen; record what lands first, second, and third. Compare
  the delivered attention order against the order the task needs — divergence is
  the raw material for a hierarchy finding. Check the emphasis budget: one
  primary action per screen is the default.
- Checkpoint: "The promo banner wins first fixation on the cart — is the promo
  meant to outrank checkout?"

### Step 6 — Audit layout and spacing
**Reference:** `references/layout-and-spacing.md`

- Extract the spacing values in use, count distinct values per semantic role,
  check alignment and the grid, judge density, and verify mobile touch-target
  sizes against the reference's minimums. Numbers, not impressions: "five gaps
  between option cards" is evidence; "spacing feels loose" is not.
- Checkpoint: "I count five gaps between the option cards — is there a spacing
  token set to measure against?"

### Step 7 — Audit typography
**Reference:** `references/typography-basics.md`

- List every font size with the elements using it; check measure (line length in
  characters), leading, weights, and pairing consistency across screens. The
  size inventory almost always surprises the team — say the count out loud.
  Check truncation and wrapping with real content, not placeholder strings.
- Checkpoint: "Eleven font sizes on the payment screen — is there a type-scale
  document, or should one be built?"

### Step 8 — Audit color and contrast
**Reference:** `references/color-and-contrast.md`

- Extract every text/background pair and component boundary; compute contrast
  ratios; check semantic color consistency across screens; simulate
  colorblindness for status colors. Compute, never eyeball — borderline failures
  are invisible to the eye. Check color proportions too: accent overuse
  flattens the hierarchy the emphasis budget needs.
- Checkpoint: "Placeholders compute to 2.5:1 — darker placeholders, or drop
  placeholders in favor of labels?"

### Step 9 — Run the accessibility pass
**Reference:** `references/accessibility-review.md`

- Contrast floors, keyboard reachability and focus visibility, form labels and
  error patterns, alt text and accessible names, heading structure, reflow at
  200% zoom and 320px width; on a build, add the screen-reader spot check. Cite
  WCAG success criteria by number so findings become requirements.
- Checkpoint: "Keyboard findings now, AT session after build?"

### Step 10 — Check interaction patterns against the catalog
**Reference:** `references/interaction-patterns.md`

- Forms (labels, validation timing, autofill, error recovery), navigation
  (location awareness, escape hatches), feedback quality, empty states, and
  destructive-action confirmations. Also verify the happy path's quiet
  properties: input modes, autocomplete attributes, data preservation.
- Checkpoint: "The address screen loses data on back-navigation — bug to log
  separately, or a finding here?"

### Step 11 — Clean the raw list into findings
**Reference:** `references/critique-principles.md`

- Merge duplicates and same-root-cause observations; split bundled ones. For
  each survivor, write the four parts — severity, evidence, principle (tied to
  its reference file), fix. Discard anything that is preference rather than
  principle, and say what you discarded.
- Checkpoint: "I discarded the hero-illustration note — no principle supports
  it. Flag if you want style opinions anyway."

### Step 12 — Rate severity, honestly
**Reference:** `references/critique-principles.md`

- Assign P0 through P3 by user impact alone — never effort, never offense
  taken. A wrong P0 costs more credibility than a missing P3. Force-rank if P0
  plus P1 exceeds a third of the list; downgrade when unsure; state the
  distribution.
- Checkpoint: "Back-navigation data loss is P0. Agree?"

### Step 13 — Cap and prioritize
**Reference:** `references/critique-principles.md`

- Order by severity, then by breadth of impact, then cheap-fix-first within a
  severity. Cap the delivered list — 12 findings is the working default for a
  five-screen flow — and move the remainder to the appendix, severities intact.
  The cap is part of the definition of done.
- Checkpoint: "Finding 13 (spacing rhythm) is appendix material — accept, or
  swap for finding 9?"

### Step 14 — Assemble the report
**Reference:** `templates/critique-report-template.md`

- Fill the template: goal capture, what works, findings, open questions,
  assumptions, appendix. Lead with what works, using the same evidence
  discipline as the failures; put the severity distribution up top.
- Checkpoint: "Does the what-works section match what the team already knows,
  or is it news?"

### Step 15 — Deliver and offer follow-through
**Reference:** `references/critique-case-studies.md`

- Present the top three findings verbally first in synchronous settings. Offer
  the next moves: fix the P0s now, re-critique after fixes land, or fold the
  findings into the backlog with owners. A re-critique verifies rather than
  trusts; offer it explicitly.
- Checkpoint: "Want a re-critique after the P0 and P1 fixes land, so we verify
  rather than trust?"

Run steps 5 through 10 screen by screen, not lens by lens across the flow, so no
screen is left half-judged; steps 11 through 13 are where observations become a
report, and a forty-item raw dump is a backlog, not a critique.

## 05 — Rules and Quality Bar

How to use these rules: run the draft report against them before sending. A
violated rule with no rationale is a defect in the critique itself.

1. **Goals before taste.** No finding without a goal, a user, or a named
   principle behind it.
   - Craft: `references/critique-principles.md`.
   - Why: taste masquerading as critique destroys the report's authority.
2. **Every finding carries all four parts** — severity, evidence, principle,
   fix — or it does not ship.
   - Craft: `references/critique-principles.md`.
   - Why: a three-quarter finding hands its missing work to the reader.
3. **Evidence is checkable.** Name the element, its state, and a count or
   measurement: "11 font sizes," "2.5:1," "320px below the fold."
   - Craft: `references/layout-and-spacing.md`,
     `references/color-and-contrast.md`.
   - Why: checkable claims get fixed; vibes get debated.
4. **Severity measures user impact, never effort or offense.**
   - Craft: `references/critique-principles.md`.
   - Why: folding effort into severity misorders the backlog.
5. **Cap the delivered list; appendix the rest.** Twelve ranked findings is a
   decision instrument; forty is a backlog dump.
   - Craft: `references/critique-principles.md`.
   - Why: the cap forces the prioritization logic to actually run.
6. **Probe the unhappy paths before judging visuals.**
   - Craft: `references/interaction-patterns.md`.
   - Why: the P0s live in error and recovery states (OrbitDesk case, in
     `references/critique-case-studies.md`).
7. **Run the six lenses per screen, and name the lens in each finding.**
   - Craft: the five lens references, starting with
     `references/visual-hierarchy.md`.
   - Why: lens-hopping produces duplicates and missed screens; naming the lens
     keeps citations honest.
8. **Cite the reference file in every principle statement.**
   - Craft: all reference files.
   - Why: the reader can check the doctrine, not just the assertion.
9. **Compute contrast; never eyeball it.**
   - Craft: `references/color-and-contrast.md`.
   - Why: borderline failures (2.8:1, 3.2:1) are invisible to the eye and
     decisive under WCAG 1.4.3.
10. **State verification depth honestly.** Statics mean behavior findings are
    labeled "assumed — verify in build."
    - Craft: `references/critique-principles.md`.
    - Why: one overclaim costs the credibility of the eleven right ones.
11. **Lead with what works, with the same evidence discipline.**
    - Craft: `templates/critique-report-template.md`.
    - Why: what-works proves the reviewer is measuring, not campaigning.
12. **Kind phrasing is precision plus respect.** Critique artifacts, never
    people; observable language over judgment language; no sarcasm.
    - Craft: `references/critique-principles.md`.
    - Why: the phrasing rules exist because unheard findings fix nothing.
13. **Recommend one primary action per screen.**
    - Craft: `references/visual-hierarchy.md`.
    - Why: fixes that leave two competing primaries moved the problem.
14. **Cite WCAG success criteria by number.**
    - Craft: `references/accessibility-review.md`.
    - Why: the numbers turn style disputes into requirements.
15. **Discard your preferences out loud.** Say what you left out and why.
    - Craft: `references/critique-principles.md`.
    - Why: visible discard decisions teach the method.

## 06 — Worked Example

The scenario: **ShopSimple**, a small web shop's mobile checkout — cart →
shipping address → delivery options → payment → confirmation. Five screens,
390px viewport, static design exports plus a staging build. The requester is the
shop's owner-developer, asking "is my checkout costing me sales?" The
deliverable is a critique report with exactly 12 prioritized findings. The full
report is `examples/worked-ui-critique.md`; this section walks the reasoning.

### Steps 1-2 — Intake and goal capture

- Scope agreed up front: the five checkout screens only; account creation and
  the storefront are out of scope. Build access granted, so behavior findings
  may be asserted rather than assumed.
- Goal capture produced one sentence per screen — the standard for every
  finding: Cart, "review items, see an accurate total, move to checkout with
  confidence"; Shipping, "enter an address once, without errors or re-entry";
  Delivery, "pick an option understanding the cost and date tradeoff"; Payment,
  "pay without double-charges or confusion about the amount"; Confirmation,
  "know the order went through, what happens next, how to get help."
- The step-2 checkpoint sharpened the payment goal: success is "paid without
  double-charge," not "chose the cheapest option" — which is why the
  total-related findings later target trust, not merchandising.

### Steps 3-4 — Walkthrough notes and unhappy paths

Walking the flow as a customer produced raw notes (unfiltered; some later
discarded):

- Cart total says "subtotal $142.00" — where is the real total? (kept)
- Promo "Apply" sits above Checkout and looks equally important (kept)
- Back from the address screen: everything I typed is gone (kept — reproduced
  3 of 3 times on staging)
- ZIP field opens the alphabet keyboard (kept)
- Delivery options: three radios, prices in an accordion, no arrival dates (kept)
- Hero illustration style feels dated (discarded — preference, no principle)
- Double-tapped "Place order" during a silent 3-second wait → two confirmation
  numbers, #4821 and #4822 (kept — the flow's worst finding)
- Card error after submit: message at top, field unmarked, data preserved (kept)
- Trust-badge carousel pushes the order summary 320px down; the CTA is visible
  but the amount it commits to is below the fold (kept)
- Placeholders are light gray everywhere (kept — later computed to 2.5:1)
- Payment screen shows 11 font sizes; input radii differ per field, 12/8/16px
- Gaps between delivery option cards measure 10, 12, 14, 16, 18px (kept)
- Two different reds for errors on payment versus address screens (kept)

### Step 5 — First-fixation reads

- Cart: the promo pair wins fixation over the CTA, inverting the order the task
  needs. Delivery: the "Step 3 of 4" indicator reads first (good), then the
  option radios.
- Payment: the trust-badge carousel wins first fixation, "Place order" is
  second, and the total does not appear in the first three — the amount is what
  the tap commits to.

### Steps 6-10 — The six lenses (evidence condensed to measured facts)

- Hierarchy: promo "Apply" competes with the CTA (emphasis budget —
  `references/visual-hierarchy.md`); the summary sits below the fold on
  payment.
- Layout and spacing: five values playing one spacing role; three different
  input radii; density acceptable except the payment screen's detour modules.
- Typography: 11 sizes against a needed 6-role scale; measure and leading
  within range elsewhere.
- Color and contrast: placeholders at 2.5:1 fail WCAG 1.4.3; two error reds
  (#DC2626 vs. #B91C1C) split the semantic role.
- Interaction: data loss on back-navigation; double-submit possible on payment;
  subtotal-versus-total mismatch at decision points; missing autofill
  attributes and `inputmode`; validation only at submit, far from fields.
- Accessibility: the contrast floor; error identification by color and border
  only at the card field; placeholders standing in for labels (SC 3.3.2).

### Steps 11-12 — Cleaning and severity

- Fourteen raw notes minus one discarded preference, minus two merges (the
  placeholder notes were one finding; the ZIP keyboard note merged into the
  autofill finding) equals 12 findings.
- Severity assigned by impact alone: data loss and double-charge are P0 because
  they corrupt the core task; decision-critical information and error handling
  are P1; measurable-but-workable friction (contrast, type scale, spacing, fold
  position) is P2; semantic drift (the two reds) is P3.
- Distribution: 2 P0, 5 P1, 4 P2, 1 P3 — within the one-third rule for P0 plus
  P1 (7 of 12). The severity disputes settled themselves with the scale:
  "the two reds?" — P3; "the double-charge?" — the definition of P0.

### Steps 13-15 — Prioritization and delivery

- Ordered by severity, then breadth: the P0s first (findings 1-2), then the P1s
  that touch every customer (total opacity, autofill, delivery dates), then the
  narrower P1s (promo emphasis, card-validation timing), then P2s
  cheap-fix-first within severity, then the P3.
- The report in `examples/worked-ui-critique.md` adds what works (the step
  indicator, wired autocomplete on email, plain-language confirmation), open
  questions (international shipping; promo rules; dark theme), and assumptions
  (mobile-first audience; staging mirrors production).
- The 30-second verbal version delivered to the owner: "Your checkout can
  charge people twice, and it throws away their address if they glance back at
  the cart — fix those two today; the rest is a one-week list."
- Follow-through offered: a re-critique after the P0 and P1 fixes land, so the
  fixes are verified rather than trusted.

### What the example proves

- Both P0s came from step 4, not from any visual lens — the unhappiest path
  carried the report.
- Numbers made findings unarguable ("11 font sizes," "2.5:1," "3 of 3
  reproductions"); the cap kept the report a decision instrument, not a
  backlog; naming the step indicator protected the pattern most at risk of
  being redesigned away.

## 07 — Failure Modes and Recovery

1. **Taste creep.**
   - Early signal: draft findings that cite no principle and no goal ("the
     illustration style feels dated").
   - Corrective move: run the four-part test on every finding; discard the
     taste, or convert it into a consistency finding.
   - Prevention: rule 1 in §05, plus step 11's explicit discard pass.
   - Detection: findings in the final report with no principle citation.
2. **Severity inflation.**
   - Early signal: P0 plus P1 exceeding a third of the list; the word
     "critical" appearing on cosmetic items.
   - Corrective move: force-rank against the severity definitions; ask "what
     breaks if this ships unfixed?" until honest labels emerge.
   - Prevention: the one-third rule and downgrade-on-uncertainty in
     `references/critique-principles.md`.
   - Detection: severity distributions compared across your reports over time.
3. **Static-screen overreach.**
   - Early signal: confident behavioral findings ("double-submit is
     impossible") when only design exports were supplied.
   - Corrective move: relabel as "assumed — verify in build," or get build
     access before publishing.
   - Prevention: step 1 asks for build access up front; rule 10 pins
     verification honesty into the report.
   - Detection: behavior claims carrying neither a "verified" nor an "assumed"
     label.
4. **Raw-dump delivery.**
   - Early signal: the draft report has 30-40 undifferentiated items and no
     distribution statement.
   - Corrective move: run the merge-and-split pass (step 11), cap the
     delivered list, appendix the rest.
   - Prevention: treat the cap as part of the definition of done.
   - Detection: delivered-finding count checked against the cap at assembly.
5. **Lens skipping.**
   - Early signal: strong color and typography findings but nothing on error
     states, keyboard flow, or empty states.
   - Corrective move: re-run steps 4 and 9-10 per screen before publishing;
     request empty states and unhappy-path screens when the inputs omit them.
   - Prevention: the six-lens checklist in steps 5-10, run per screen.
   - Detection: a lens-by-screen coverage matrix; empty cells are findings
     against the critique itself.
6. **Evidence-free contrast claims.**
   - Early signal: "the gray is too light" with no computed ratio or hex pair.
   - Corrective move: extract the pairs and compute (rule 9); the number either
     confirms the finding or kills it.
   - Prevention: `references/color-and-contrast.md` makes computation the
     method, not an optional rigor step.
   - Detection: any contrast finding without a ratio in its evidence line.
7. **Scope drift.**
   - Early signal: findings accumulating about the storefront, account
     creation, or email templates during a checkout critique.
   - Corrective move: park them in an "out of scope — flagging only" note;
     never let them consume delivered-finding slots.
   - Prevention: the scope boundary captured in step 1 and restated in the
     report's goal-capture section.
   - Detection: appendix and delivered list audited against the agreed scope.
8. **Report lands, nothing changes.**
   - Early signal: acknowledged receipt, no decisions, no backlog items two
     weeks later.
   - Corrective move: deliver the 30-second verbal version (three findings,
     each with its fix) before or with the document.
   - Prevention: step 15's delivery format — the report supports the
     conversation; it is not a substitute for it.
   - Detection: a two-week follow-up check — which findings have owners?

## 08 — Supporting Files Index

Reading order: run §04 top to bottom, opening a reference when a step names it;
use the template when composing findings; read the worked example after your
first real critique. If you read only one file first, make it
`references/critique-principles.md`.

The eight references each carry one body of craft — method, hierarchy, layout,
typography, color, interaction, accessibility, applied cases — so SKILL.md stays
procedural rather than encyclopedic. The template defines the one output shape;
the example shows the full pass at realistic depth.

| File | Purpose | Used In |
| --- | --- | --- |
| `SKILL.md` | The skill itself: procedure, rules, worked example, and this index | all sections |
| `references/critique-principles.md` | Methodology: goals before taste, finding format, severity scale, kind phrasing, prioritization | §01, §02, §03, §04 Steps 1-2, 11-13; §05 Rules 1-2, 4-5, 10, 12, 15 |
| `references/visual-hierarchy.md` | Methodology: attention order, first-fixation test, emphasis budget, scanning patterns, fix ladder | §04 Step 5; §05 Rules 7, 13; §06 |
| `references/layout-and-spacing.md` | Methodology: grids, spacing systems, density, alignment, touch targets, responsive checks | §04 Step 6; §05 Rules 3, 7; §06 |
| `references/typography-basics.md` | Rubric: type scale, measure, leading, pairing, legibility | §04 Step 7; §05 Rule 7; §06 |
| `references/color-and-contrast.md` | Rubric: palette roles, contrast ratios, semantic color, color proportions, dark mode | §04 Step 8; §05 Rules 7, 9; §06 |
| `references/interaction-patterns.md` | Pattern catalog: forms, navigation, feedback, empty states, confirmations, microinteractions | §04 Steps 3-4, 10; §05 Rules 6-7; §06 |
| `references/accessibility-review.md` | Checklist: WCAG essentials, keyboard access, forms, screen-reader basics | §04 Step 9; §05 Rules 7, 14; §06 |
| `references/critique-case-studies.md` | Three calibration case studies: goal, first-fixation, findings, after state | §04 Steps 4, 15; §05 Rule 6; §06, §07 |
| `templates/critique-report-template.md` | Report scaffold: metadata, severity scale, finding format, section skeleton | §03, §04 Step 14; §05 Rule 11 |
| `examples/worked-ui-critique.md` | Extended worked example: the full ShopSimple report with all 12 findings | §03, §06 |

Maintenance contract:

- This table must match the skill directory exactly — the verification suite
  diffs it against reality.
- If you add a file, add a row and cite it at its point of use in §04.
- If a file is no longer used, remove the file and the row.

Cross-skill boundaries:

- Findings that reveal system-level gaps — an information architecture that
  cannot hold the flow, a design system that does not exist yet — are recorded
  here and handed to `design-system-foundations`; critique flags, foundations
  decides.
- Implementation-quality questions surfaced by a critique ("does the build
  match these screens?") belong to `code-review` and `testing-strategy`;
  critique judges the interface, review judges the code.
- Compliance-grade accessibility verification stays out of scope; this skill's
  pass finds and frames the findings a dedicated audit would confirm.