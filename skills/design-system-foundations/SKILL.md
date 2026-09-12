---
name: design-system-foundations
description: Use when you need to build, audit, extend, or migrate a design system — token architectures, component inventories, pattern documentation, theming, accessibility enforcement, adoption strategy, and governance. Load this skill when the task involves founding a new design system, auditing the coherence of an existing UI, or preparing a migration plan. Covers the full lifecycle from inventory to governance handoff.
---

# design-system-foundations

## 01 — Purpose

A design system is a set of named, governed, and documented decisions
about the user interface: what the colors are, how spacing works, how
components behave, and what rules cannot be broken. Without a system,
every screen invents its own answers. With a system, a team of three
produces a product that looks like one product, not three products
sharing a database. The difference is not aesthetic — it is structural.

The skill owns three outcomes:

1. A measured inventory and a defensible starting point: which
   components exist, how far each type has diverged, and which five to
   eight are worth systematizing first — with side-by-side evidence a
   skeptic can inspect rather than a feeling you have to argue for.
2. A governed token and documentation foundation: a three-tier token
   set that validates against a schema in CI, component docs a newcomer
   can execute from without asking anyone, and accessibility
   requirements enforced as automated checks rather than good
   intentions.
3. An adoption and governance plan that survives contact with shipping:
   phased targets, a pull-ratio metric, a deprecation policy, and a
   first-adopter surface whose before-and-after numbers prove the system
   reduces real work instead of adding ceremony.

The cost side is real: a founding run consumes two to four person-months
before the first adopted surface ships, and the return arrives as
eliminated reimplementation — measured, not assumed. Teams that cannot
commit the capacity should run the reduced path rather than a diluted
full run, and teams that cannot measure the return should not start
until they can. Everything here exists to make the investment
verifiable: divergence scores before, pre/post metrics at the first
surface, and pull ratio thereafter.

The directory provides twelve artifacts, each referenced by name at its
point of use in the workflow: eight references, two templates, the
schema at `schemas/design-tokens.schema.json` (the machine-checkable
contract every token proposal must pass), and the worked example in
`examples/worked-design-system.md` — a full run on TaskFlow, a small web
app, with intermediate artifacts at every step.

Three boundaries keep this skill honest about what it is not. It is not
a brand identity exercise: naming the brand and choosing typefaces
precede the system. It is not a frontend implementation guide: it
produces decisions, and your framework skill produces the code. It is
not a tool evaluation: it names tool categories, never products.

## 02 — When to Use / When Not to Use

Use this skill when founding, auditing, extending, or governing an
interface that more than one person builds across many surfaces. The
questions filter common misuses.

**Q1: Does the product have four or more surfaces?** Fewer than four
means too young for tokens and governance — build by hand until the
fourth surface arrives.

**Q2: Do multiple people build the UI?** A solo designer shipping from
one file needs no audits or governance bodies — a system's value
compounds with the people it coordinates.

**Q3: Is there inconsistency that affects velocity?** If nobody notices
the drift, the system solves a problem nobody feels. Wait until a bug
links to drift or onboarding reveals two buttons with different radii.

**Q4: Can you name the first-adopter surface?** If no team will pilot
the system, the run produces artifacts nobody uses. One adopted surface
beats a complete set that ships nothing.

### Use this skill when

1. Founding a design system for a product with drift — mismatched
   buttons, two blues claiming one color. Start with
   `references/component-inventory.md`.
2. Auditing an existing UI for coherence — divergence scores, a
   coverage map, shortlist, side-by-side appendix.
3. Designing a token set — `references/design-tokens.md` gives tiers,
   naming, scales, extraction.
4. Writing component docs — `references/pattern-documentation.md` plus
   `templates/component-doc-template.md` produce docs a newcomer
   executes from.
5. Planning a theme — `references/theming-architecture.md` covers
   resolution, registry, contrast sweeps.
6. Establishing change governance — `references/versioning-and-governance.md`
   provides versioning, review tracks, deprecation.
7. Planning adoption — `references/adoption-strategies.md` answers the
   skeptic arguments with numbers.
8. Adding a CI gate for UI decisions — schema, contrast sweep, and
   divergence audit convert taste into checks.
9. Inheriting a system someone else built — the audit doubles as an
   assessment.
10. Weighing whether a system is worth it — the case studies include
    the failures.

### Do not use this skill when

1. A single component in a system that already has a contribution
   process — that governance takes precedence.
2. A runnable UI library with decisions settled — this skill produces
   decisions and policy, not runtime code.
3. A visual redesign with no governance needs — a single-designer,
   three-screen prototype needs no system.
4. Evaluating tooling — the skill names categories, never products.
5. Migrating a mature system to another platform — apply only the
   governance layer.
6. CSS or JavaScript from this skill — outputs are JSON and Markdown,
   inputs to your build tooling.
7. Debugging one component's behavior — return when the fix becomes
   systemic.
8. Naming a brand or choosing typefaces — brand identity precedes the
   system.

Gray zone: one new component in a young system with tokens but no
process. A new variant axis or token makes it system work (Steps 3–5);
composing existing tokens only needs the doc template.

## 03 — Inputs and Outputs

Each input changes a decision; each output is reviewable by someone who
did not run it. A run hands off at any step boundary — state lives in
the artifacts.

### Inputs

- The product surface: four or more surfaces — routes, screens, dialogs,
  distinct states (empty, error, loading). The audit is only as good as
  its coverage.
- Existing artifacts: stylesheets, design files, screenshots. Messy is
  fine; missing artifacts mean measuring rendered output — slower,
  adequate.
- Accessibility requirements: target WCAG level (AA default), legal or
  contractual commitments.
- Color and spacing constraints: brand palette, base spacing unit,
  existing scales worth preserving.
- Team context: who builds, who consumes, release cadence, governance
  appetite, and a named accessibility authority — a role with standing
  to block.
- Divergence evidence (optional but decisive): worst-case pairs side by
  side. Skeptics are settled by evidence, not taste.

Two anti-inputs arrive often and are refused. A competitor's design
system: importing its token names imports decisions made for different
constraints — use case studies for patterns, your own audit for values.
An unfinished design file: start from what shipped; label artifacts
provisional if the product is pre-ship.

### Outputs

- Component inventory: divergence scores, coverage map, worst-case
  appendix, a prioritized shortlist of five to eight types.
- Token set: primitives and semantics with per-theme values, validated
  against `schemas/design-tokens.schema.json`, plus proposal records in
  the shape of `templates/token-spec-template.md`.
- Component documents in the shape of `templates/component-doc-template.md`:
  anatomy, variants, states, do/don't pairs, a11y checklist.
- Theme registry and contrast sweeps for every theme pair.
- Governance process: versioning, review tracks, deprecation policy, in
  two pages or fewer.
- Adoption plan and case study: three phases with targets, the
  first-adopter surface, migration priorities, pre/post numbers.
- A decision log: every contested call — the forbidden cell, the
  refused step, the exception and its expiry.

Two outputs determine success, and neither is expected: the
first-adopter surface shipped — everything else is preparation — and the
decision log (a run that cannot explain its contested calls produced
files, not a system).

### Shape notes

Token proposals follow `templates/token-spec-template.md`; component
docs follow `templates/component-doc-template.md`. Both validate
mechanically — tokens against the schema, docs against the checklist in
`references/pattern-documentation.md`. A token proposal is a one-page
argument retired into the decision log; a component doc is a living
contract. The schema is the only artifact validated, not reviewed.

## 04 — Workflow

The workflow produces a design system from an ungoverned product
surface. Work the steps in order; each consumes the previous step's
artifact. It assumes a mid-size product (30–60 surfaces) and a two- to
four-person team. At 4–15 surfaces run steps 1–3 and 8–9; above 100,
prove the system inside one team before cross-team rollout. Steps 4–5
run concurrently — the a11y checklist applies per doc, not at the end.

Two standing practices apply. Artifact before meeting: every checkpoint
is answered by pointing at an artifact. The shortlist is the contract:
after Step 2, scope changes go through governance (Step 7).

### Step 1: Audit the existing surface

Enumerate every surface, tally every component instance, and score
divergence per type using `references/component-inventory.md`. Produce
tally sheets, the coverage map, the worst-case appendix, and the 5–8
type shortlist scored by frequency, divergence, blast radius.

**Governing reference:** `references/component-inventory.md`

**Checkpoint:** Can a skeptic who disagrees with the conclusions agree
with the numbers? A score resting on memory is incomplete.

### Step 2: Prioritize the shortlist

Score each candidate: priority = frequency × divergence ÷ effort. Keep
5–8; publish the formula, not just the ranking. Record exclusions and
reasons — exclusions re-litigated monthly signal a shortlist never
written down.

**Checkpoint:** Does every excluded component have a recorded reason?
If two people disagree on one, fix the criteria.

### Step 3: Design the token set

Build the three-tier architecture using `references/design-tokens.md`:
primitives as the full palette, semantics named by role, component
tokens only for genuine divergence. OKLCH ramps across brand, error,
success, warning plus neutrals, 11 steps each; spacing from a base unit
with 6–8 steps capped at 64; a type scale at ratio 1.25.

Unless greenfield, the token set is a convergence of values the audit
found — run the extraction pass first, designing only what the harvest
cannot supply. Set the convergence budget before mapping old values.

Each proposal uses `templates/token-spec-template.md` and validates
against `schemas/design-tokens.schema.json`. Every semantic declares a
dark value at proposal time.

**Governing references:** `references/design-tokens.md`,
`templates/token-spec-template.md`, `schemas/design-tokens.schema.json`

**Checkpoint:** Does every semantic token have a dark value? If not,
demote it.

### Step 4: Document the first component batch

Write docs for the top three shortlisted components using
`templates/component-doc-template.md` and `references/pattern-documentation.md`.
Each doc: anatomy mapped to props and tokens, the allowed-combination
table with forbidden cells and reasons, a state table with per-state
ARIA, three to six do/don't pairs, one example per axis. Test with an
outside reader — every question is a doc defect.

**Governing references:** `references/pattern-documentation.md`,
`templates/component-doc-template.md`

**Checkpoint:** Did an engineer who never touched the component ship a
correct button from the doc alone? If they needed the design file, the
doc is incomplete.

### Step 5: Apply accessibility requirements

Apply `references/accessibility-standards.md` per component: WCAG
criteria mapped to doc obligations, the ARIA pattern, focus behavior,
the four testing layers. The accessibility authority signs each a11y
section.

**Governing reference:** `references/accessibility-standards.md`

**Checkpoint:** Does every interactive component have a keyboard path
and a visible focus indicator, verified by test?

### Step 6: Design theming architecture

Define theme types (brand versus mode — different axes, different
resolution), the registry validated at build time, and the contrast
sweep that fails the build on violations, per
`references/theming-architecture.md`.

**Governing reference:** `references/theming-architecture.md`

**Checkpoint:** Can you enumerate every theme and its resolution order
in one paragraph, with no token inheriting an invisible value?

### Step 7: Establish governance

Adopt the versioning scheme, two-track review, and deprecation runbook
from `references/versioning-and-governance.md`, sized to current
adoption — one reviewer now, the standard track at 60% adoption. The
first change record establishes governance itself.

**Governing reference:** `references/versioning-and-governance.md`

**Checkpoint:** Do consumers know when the next release is, how to
propose a change, and what happens when a breaking change ships?

### Step 8: Plan adoption

Using `references/adoption-strategies.md`, define the three-phase plan
(foundation, pull, governance) and identify the first-adopter team —
chosen by enthusiasm, not mandate. Score first-adopter candidates
against all five criteria (frequently visited, volunteered,
representative, bounded, measurable) and reject any candidate that fails
boundedness regardless of visibility. Track adoption rate (target 60% in
pull) and pull ratio (target 2:1).

**Governing reference:** `references/adoption-strategies.md`

**Checkpoint:** Is the first adopter identified, with dedicated capacity
and pre-system metrics published? A first adopter without time does not
ship — choose a different team.

### Step 9: Build the first-adopter surface

The team rebuilds one production surface using only system tokens,
components, and patterns, shipping before the system is complete — week
6 is a hard deadline. Measure pre and post: render time, CSS import
count, a11y violations, time to make one standard change. Publish as a
case study per `references/system-case-studies.md`, including what did
not improve.

**Governing references:** `references/system-case-studies.md`,
`references/adoption-strategies.md`

**Checkpoint:** Are the before-and-after numbers published, including
the worse ones? A case study with only favorable numbers convinces no
one.

### Step 10: Iterate and govern

Run the system as a product: MINOR releases on cadence, change
governance handling the incoming flow, the deprecation runbook for
anything retired. Pull ratio and adoption rate reviewed every release;
below 1.5 pull for two releases, stop self-initiated work.

**Governing reference:** `references/versioning-and-governance.md`

**Checkpoint:** Is the changelog current, and does every deprecated item
have a named replacement and removal version?

### Step 11: Wire the quality gates

Make the rules mechanical: token validation against
`schemas/design-tokens.schema.json` in CI, the contrast sweep per theme,
the quarterly divergence re-audit, and the doc review checklist for
component changes. A gate that reports without blocking is a dashboard,
not a gate.

**Governing references:** `schemas/design-tokens.schema.json`,
`references/pattern-documentation.md`

**Checkpoint:** Does a failing gate block the merge, or only report?
Wire the block or delete the check.

### Step 12: Run the operating rhythm

Sustain with a rhythm, not heroics: daily consumer-channel triage, a
weekly status post of four to six bullets, a monthly demo with
first-adopter numbers, a quarterly governance review with published
minutes and governance-health metrics.

**Governing references:** `references/adoption-strategies.md`,
`references/versioning-and-governance.md`

**Checkpoint:** Did every open consumer request get a response inside
one cadence — even when the answer was "not yet"? Silence is how pull
dies.

## 05 — Rules and Quality Bar

1. Audit before you design: a system built without an inventory serves
   the interface the team imagines, not the one that exists.
2. Tokens before components: the token set exists before the first
   component doc. Tokens are the vocabulary that makes a library
   coherent rather than a pile of bespoke parts.
3. Keep the semantic tier smaller than the primitive tier: a 1:1 mirror
   tier is indirection with no change of meaning.
4. Every semantic token declares a dark value at proposal time: a token
   without one produces invisible text when dark mode ships. The schema
   enforces this.
5. Component docs are contracts, not novels: one page per component, two
   hard limit. Using the component must not require opening a second
   artifact.
6. Every interactive component has a focus-visible indicator at 3:1
   minimum: pointer-only affordances exclude keyboard users. Verified in
   CI, not in review.
- No release without a changelog: it is the contract between the
    system team and its consumers.
9. New tokens require two documented consumption surfaces: a one-surface
   token is too narrow — use a component override.
10. Governance grows with adoption, not before it: the standard track
    applies at 60% adoption, not day one.
11. Deprecate only with a migration path: removal without a named
    replacement and removal version is abandonment.
12. Measure adoption by imports: renames and copied values do not
    count. Imports do not lie.
13. Reject token proposals that fail contrast at proposal time: a token
    that misses WCAG AA when proposed will not meet it at ship.
14. Build dark theme in parallel with light: a late theme erodes trust
    and breaks when light tokens change.
15. The a11y section is a checklist, not an essay: ARIA pattern, name
    source, focus behavior, one verifiable test.
16. Consumer requests outweigh system-team preferences: the pull ratio
    keeps the system shipping what the product needs.
17. Forbidden cells are decisions, not omissions: every disallowed
    combination carries a written reason.
18. One escape value earns a fix; three earn a scale step: three
    independent 13px paddings mean the scale is missing a step.
19. Exceptions are dated and expire automatically: an exception without
    an expiry is a policy change made quietly.
20. The inventory is re-run, not archived: a founding audit never
    repeated measures a product that no longer exists.

The review bar in one line: an auditor holding only this skill's
references could reconstruct every decision — why this token exists, why
this combination is forbidden, why this deprecation window — from the
artifacts alone. The rubric checklists in `references/component-inventory.md`
(audit), `references/pattern-documentation.md` (docs), and
`references/versioning-and-governance.md` (governance health) are the
working instruments for this bar.

## 06 — Worked Example: TaskFlow

This section compresses the full run in `examples/worked-design-system.md`,
which carries every artifact. TaskFlow: a small web app for personal
task management, two team members, a twelve-week timeline, and a
week-three discovery that key components have four implementations
each.

### Context and audit

TaskFlow ships across 8 surfaces: task list, task detail, calendar
view, settings, empty/error/loading states, a quick-add dialog. The
week-three audit reveals 12 button instances across 4 implementations —
divergence 3, the product's worst. Radii vary across 4, 12, and 16px;
primary actions use three different blues; one "button" is a `<div>`
with a click handler — no enter-to-activate, no focus ring, no role.

The tally, in the format `references/component-inventory.md` prescribes,
with one row per surface:

| Surface | Instances | Implementation | Divergence notes | Score |
|---|---|---|---|---|
| Task list | 4 | `Button.css` v1 + inline | two radii; two primary blues | 3 |
| Task detail | 3 | `Button.css` v1 | consistent internally | 2 |
| Quick-add | 3 | `button.module.css` + 1 `<div onClick>` | no role, no focus ring | 3 |
| Settings | 2 | `button.module.css` | radius 4px — a third radius | 2 |
| Empty/error/loading | 4 | inline styles | hover missing; one `<a>` without href | 3 |

Eight candidate types are scored; four hit 2 or higher (Button 3, Card
3 — sometimes clickable, sometimes not; TextInput 2, Dialog 2). The
shortlist adds Badge and Select as low-effort, high-frequency adds.
Priority: Button 14, Dialog 13, TextInput 11, Card 10, Badge 7, Select
6. The appendix's three screenshot pairs did more to convince the
skeptical engineer than any argument. The coverage map records two
exclusions: onboarding (redesign scheduled) and the admin console
(another team's surface).

### Token design decisions

Following Step 3, the team designs 56 primitives and 38 semantic
tokens with light and dark values from day one. Every semantic named
its two consumption surfaces at proposal time — the discipline keeping
the tier from mirroring the primitives six months in.

- Color: four OKLCH ramps at 11 steps, plus neutrals. Steps cluster
  near white (50–200) for subtle surfaces and spread wider in mid-tones
  (300–700) where contrast lives.
- Spacing: 4, 8, 12, 16, 24, 32, 48, 64. The 12px step carries a
  recorded justification ("button label to icon"), so nobody adds 14
  later.
- Type: five steps at ratio 1.25 — 14px labels through 32px page
  titles — each with line-height and weight slot.
- Radius: 3 steps (sm 4, md 8, full) — xl is deliberately omitted
  because nothing uses it.
- Shadows: 3 elevation levels, each storing the full `box-shadow`
  declaration rather than parts.

The audit found 34 grays; the convergence budget kept 11, each mapped
to its nearest survivor. Two contested mappings — a settings-page gray
between two survivors — resolved by repointing styles at the semantic
tier, not expanding the ramp.

One proposal, in the shape of `templates/token-spec-template.md`:

- Name: `color-bg-button-primary` (semantic tier).
- Resolves to: `blue-600` (light), `blue-500` (dark).
- Rationale: the primary action background — Button today, Select's
  confirm variant shortlisted; two surfaces named.
- Contrast pair: against `color-text-on-primary`, 4.6:1 (AA).
- Migration: replaces `#2f6fed` and `#2563eb`, both found in the audit.

### Component documentation: Button

Documented first because it establishes conventions. Anatomy:
container (`intent`, `color-bg-button-primary`), label (`children`,
`color-text-on-primary`), optional icon, spinner (`loading` — replaces
the label; a hidden sizer preserves width). Combination table: intent ×
size, `destructive-sm` explicitly forbidden — "small destructive
buttons sit too close to other actions for safe accidental activation."
States: rest, hover, focus-visible (2px outline at
`color-focus-ring`), active, disabled (`aria-disabled`, opacity 0.4),
loading (`aria-busy`). Keyboard: Tab in, Enter/Space activates,
Shift+Tab out.

The doc's do/don't pairs:

1. Do: use `intent` for the action's consequence. Don't: use it to mean
   emphasis — three primary buttons on one screen is a hierarchy
   failure the token set cannot fix.
2. Do: disable with `aria-disabled` and stay focusable. Don't: use the
   HTML `disabled` attribute on a button that explains why — the native
   attribute removes focus and silences the explanation.
3. Do: keep labels verb-first ("Save task"). Don't: label a destructive
   action only "OK" — the label must survive being read out of context.

The pass hit one recurring issue: the first TextInput draft documented
the error state as "border changes to `color-border-error`" and nothing
else. The a11y review flagged it — color-only indication is invisible
to screen readers — producing the `aria-describedby` requirement now in
the doc. The ARIA column is a requirement to satisfy before the doc
ships, not a description of what already works.

### Governance and the first-adopter surface

Before shipping, the team defines minimum governance: fast track for
patches and docs, standard track for tokens and components, two-MINOR
deprecation notices with migration paths, biweekly releases. The first
change record — "Establish governance process" — is the first governed
decision.

Then the task-list surface is rebuilt in 4 days on system components
(with render time 980→620ms, CSS imports 12→3, a11y violations 14→0,
and time to add a filter dropdown ~4h→~30min).

The quick-add dialog was deferred when its `<div onClick>` button
turned out to be load-bearing for an undocumented drag-and-drop
interaction; the team shipped the list rather than delay and documented
the remaining two bespoke calendar components for a follow-up pass.

**The run's timeline:** Week 1 audit (shortlist of 6), Weeks 2–3 tokens
(56 primitives, 38 semantics, CI validation), Weeks 4–5 docs (Button
and TextInput pass reader test), Week 6 theming and governance (registry,
contrast sweep green), Weeks 7–9 first surface (task list rebuilt).
Spent buffer on the deferred dialog and re-running the audit; Button
score fell from 3 to 1 — the first number showing the system working.

Four judgment calls carry the transferable lesson. The shortlist was
cut from eight to six when the timeline compressed. The 12px
step was added only after three independent one-offs appeared in the
audit — the escape-value rule absorbing a proven need. The case
study published the calendar view's failure — only-wins case
studies earn no trust from the teams being asked to adopt next.

## 07 — Failure Modes and Recovery

### Failure 1: The component backlog

**Signal:** requests outpace fulfillment; the backlog ages past 200
items; teams route around the system to hit deadlines. **Correction:**
close items weekly, ship the top five by impact, say "no, and here is a
workaround" as often as "yes." **Prevention:** the pull ratio from Step
8, every release.

### Failure 2: Token sprawl

**Signal:** the token file grows every sprint; names like
`color-blue-600-semantic` appear. **Correction:** the quarterly audit
from `references/design-tokens.md` — least-referenced tokens reviewed
for removal, mirror renames collapsed. **Prevention:** the two-surface
rule and the "which token do we remove?" question.


### Failure 3: Documentation rot

**Signal:** a doc's review date predates the last release; screenshots
show components that no longer exist. **Correction:** triage by
behavior risk per `references/pattern-documentation.md`; re-verify
high-risk docs. **Prevention:** owner roles and review dates, checked
at governance meetings.

### Failure 4

**Signal:** the first screen-reader test happens after launch; focus
indicators exist for hover only. **Correction:** run the four testing
layers on every shipped component, fix keyboard traps first, add the
automated layers to CI. **Prevention:** Steps 4–5 concurrent.

### Failure 5: Governance bypass

**Signal:** a team duplicates a component outside governance, arguing
the system "does not quite fit." **Correction:** audit why — feature
gap, performance, doc mismatch — fix the cause or absorb as a variant.
**Prevention:** low friction; track the bypass rate.

### Failure 6: The first-adopter surface never ships

**Signal:** foundation extends past week 8; "one more" component before
any real surface. **Correction:** stop building, ship what exists,
migrate one small surface, publish the numbers. **Prevention:** the
week-6 deadline.

### Failure 7: Pull ratio below 1:1

**Signal:** the team ships features nobody asked for; requests dry up.
**Correction:** stop self-initiated work for two releases; fulfill
requests exclusively. **Prevention:** track pull ratio from month one.

### Failure 8: The big-bang migration

**Signal:** a plan to "adopt the system everywhere" in one push; the
migration guide precedes the first migrated surface. **Correction:**
roll back and migrate surface by surface, one per week at most.
**Prevention:** the three-phase model in `references/adoption-strategies.md`;
a single-date plan is the smell.

Three patterns run through these failures. Missing proof — declared
done before a real surface adopted it (6, 8). Metrics gap — invisible
until expensive (1, 2, 7). Trust debt — each burns the credibility the
next adoption phase needs (3, 5). When a new failure appears, classify
it: ship the proof, publish the number, or repay the trust.

## 08 — Supporting Files Index

| File | Role | Used in |
|---|---|---|
| `references/component-inventory.md` | Audit methodology: enumeration, tally, divergence scoring, prioritization | 02, 04 (Steps 1–2) |
| `references/design-tokens.md` | Token tiers, naming, scales, extraction, audit checklist | 01, 04 (Step 3), 05 |
| `references/pattern-documentation.md` | Component doc guide: anatomy, combinations, states, review checklist | 02, 04 (Steps 4, 11), 05 |
| `references/theming-architecture.md` | Theme types, registry, contrast enforcement, extensibility | 04 (Steps 6, 11) |
| `references/accessibility-standards.md` | WCAG mapping, ARIA patterns, four testing layers | 04 (Step 5) |
| `references/versioning-and-governance.md` | Versioning, review tracks, deprecation runbook, governance metrics | 02, 04 (Steps 7, 10), 05 |
| `references/adoption-strategies.md` | Phase model, pull ratio, first-adopter selection, stall diagnosis | 02, 04 (Steps 8–9), 07 |
| `references/system-case-studies.md` | Two successes, one failure, pattern-transfer questions | 02, 04 (Step 9), 06 |
| `templates/token-spec-template.md` | Per-token proposal skeleton with guidance | 03, 04 (Step 3), 06 |
| `templates/component-doc-template.md` | Component document skeleton with guidance | 03, 04 (Step 4) |
| `schemas/design-tokens.schema.json` | Machine-checkable token contract for CI | 01, 03, 04 (Steps 3, 11) |
| `examples/worked-design-system.md` | Complete TaskFlow artifacts, audit to case study | 06 |

Reading paths: a first-time builder reads `references/component-inventory.md`,
`references/design-tokens.md`, and `examples/worked-design-system.md`
before Step 1. Joining mid-cycle: `references/versioning-and-governance.md`
plus the current phase's steps in 04. A skeptic:
`references/system-case-studies.md`, then `references/adoption-strategies.md`,
then the TaskFlow metrics. Wiring CI: `schemas/design-tokens.schema.json`,
Step 11, `references/accessibility-standards.md`. Failure signals: 07
first, then the named reference.

Maintenance follows two rules. The byte-for-byte rule: the table lists
exactly the files present, and a commit adding or removing a file
updates the table in the same change — an index that lags reality is
worse than none, because it is cited with confidence. The used-in rule:
every file is cited from at least one numbered section, and every
section that says "reference" names a real file from this table. A file
that cannot name the section using it is a file to delete, not a file
to keep in case.
