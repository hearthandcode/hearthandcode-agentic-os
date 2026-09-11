---
name: design-system-foundations
description: Use when you need to build, audit, extend, or migrate a design system — token architectures, component inventories, pattern documentation, theming, accessibility enforcement, adoption strategy, and governance. Load this skill when the task involves founding a new design system, auditing the coherence of an existing UI, or preparing a migration plan. Covers the full lifecycle from inventory to governance handoff.
---

# design-system-foundations

## 01 — Purpose

A design system is a set of named, governed, and documented decisions about the user interface: what the colors are, how spacing works, how components behave, and what rules cannot be broken. Without a system, every screen invents its own answers. With a system, a team of three produces a product that looks like one product, not three products sharing a database. The difference is not aesthetic — it is structural. A system reduces cognitive load for designers, eliminates reimplementation for engineers, and creates a shared vocabulary that product managers, QA, and stakeholders can use to describe what they see. The best design system is the one that makes the most common patterns boring — boring enough that the team can focus on the features that differentiate the product.

This skill equips you to build that system from the ground up. It does not assume an existing component library, a live Figma file, or a pre-approved color palette. It assumes you have a product — shipping or in design — and you need to make it coherent before it multiplies into inconsistency. The skill covers the full lifecycle: auditing what exists, designing the token architecture, documenting components, enforcing accessibility, establishing theming and versioning, planning adoption, and knowing when to stop. Each phase produces a concrete artifact that a colleague can review and a downstream team can consume. The artifacts are designed to be reviewed independently — the token file does not depend on the adoption plan being finished, and the component doc does not require the governance process to be decided.

The eight reference files, two templates, schema, and worked example in this skill directory are the canonical resources. The schema at `schemas/design-tokens.schema.json` provides machine-checkable validation for token proposals from any authoring tool or workflow — whether you write tokens by hand, generate them from a Figma plugin, or export from a design tool, the schema is the single gate. The templates give you a repeatable starting point for component docs and token specs — fill them in once per artifact rather than inventing a new structure each time. The worked example in `examples/worked-design-system.md` runs the full workflow on a small web application called TaskFlow, showing intermediate artifacts at every step so a new practitioner sees what each phase produces before they start their own.

This skill is a workbook. The reference files exist to be consulted in order during the workflow, not read cover-to-cover. The templates exist to be copied and filled in, one per component or token proposal. The schema exists to be run in CI. Use the skill the same way: start at section 04, follow the workflow, consult the references when a step needs depth, and produce the artifacts as you go. Each step's checkpoint question tells you whether you are done with that step before moving to the next.

Load this skill when the task begins with "build a design system," "audit our UI for consistency," "document our components," or "create a token set." Do not load it when the product already has a mature system and the task is adding a single component. This skill is for founding and governing, not for contributing to an existing system.

## 02 — When to Use / When Not to Use

### The four-question test

Before loading this skill, ask four questions. Each question filters a common category of misuse.

**Q1: Does the product have four or more surfaces?** Fewer than four surfaces means the product is too young to need a system. A single-page app with one screen and a dialog does not yet need tokens and governance. It needs design discipline, which is different — consistent naming, a limited palette, and a handful of hand-authored components. If the answer is "no," use the `product-design` skill to build coherent single-surface designs and return here when the fourth surface gets designed.

**Q2: Do multiple people build the UI?** A solo designer shipping from one Figma file does not need component inventory audits or governance bodies. If you are the only builder, keep the design decisions in your head until the second person arrives. A design system's value compounds with the number of people it coordinates. If the answer is "no," the cost of governance exceeds the benefit.

**Q3: Is there an observable inconsistency that affects reliability or team velocity?** If the product looks inconsistent but nobody notices or cares (aesthetic-only drift), the system solves a problem nobody feels. Wait until a consumer reports it, a bug links to visual drift, or an onboarding session reveals two buttons on the same screen with different corner radii. The divergence score, defined in `references/component-inventory.md`, is the measurement that converts the feeling of inconsistency into a number the team can act on.

**Q4: Can you allocate at least 50% of one person's time for four weeks?** A design system with no dedicated capacity ships nothing. Part-time contributions from people with full product delivery responsibilities produce partial documentation and ungoverned tokens. If capacity is less than that, produce only the token set and skip everything else — tokens alone provide more value than full documentation that goes out of date.

### Use this skill when

1. **You are founding a design system for a new or growing product.** The product has more than a handful of surfaces and you have already observed visual drift — buttons that do not match, spacing that varies from screen to screen, two colors that claim to be the same blue on different surfaces. Start with the component inventory in `references/component-inventory.md`. The inventory tells you which components exist, what divergence score each has, and where to start building. A product with 15–30 surfaces and three or more engineers is the typical trigger point. The inventory produces the first concrete artifact: a single table that a product manager, designer, and engineer can all agree describes reality.

2. **You are auditing an existing UI for coherence.** A stakeholder has said "this does not feel like one product" and you need evidence to drive a decision. The audit workflow in `references/component-inventory.md` produces a divergence score per component type, a surface coverage map that names which surfaces were and were not audited, a prioritized shortlist for the system team, and a divergence appendix with side-by-side screenshots of the worst three divergences — the artifact that convinces a skeptic because it is visual, not abstract. Run the audit before proposing anything — without evidence you are proposing solutions to an unmeasured problem.

3. **You need to design a token set from scratch.** You have decided to move from hard-coded values to a governed token architecture. The three-tier model (primitive, semantic, component) in `references/design-tokens.md` gives you the structure, naming conventions with a closed vocabulary of modifier terms, guidance on building scales for color, space, typography, radius, and motion, and theming hooks that require every semantic token to declare a dark counterpart at proposal time. Validate each proposal against `schemas/design-tokens.schema.json` before adding to the token file.

4. **You are writing component documentation for the first time.** `references/pattern-documentation.md` explains why most docs fail — they are written for the system team that built the component instead of the engineer or designer who consumes it. The `templates/component-doc-template.md` provides a skeleton with placeholders and guidance for each section; `references/accessibility-standards.md` provides the WCAG pattern registry and ARIA requirements to fill in the a11y section.

5. **You are planning a theme (dark mode, brand variant, high contrast).** `references/theming-architecture.md` covers the three-layer model of resolution (token → component → platform), the critical distinction between brand and mode themes, automated contrast sweeps that fail the build on violations, and the theme registry validated at build time to catch missing tokens in a single CI step.

6. **You need to establish a change governance process.** Once the system ships to more than one team, token drift is inevitable. `references/versioning-and-governance.md` provides the versioning scheme (MAJOR for breaking, MINOR for additive, PATCH for fixes), a two-track review process (fast with one reviewer and same-day approval for patches, standard with three reviewers and a three business-day window for everything else, plus an escalation path when a change is tabled twice), a deprecation policy requiring two MINOR releases with a named migration path, and governance body composition rules.

7. **You are planning adoption and need to convince skeptical teams.** `references/adoption-strategies.md` provides the three-phase model (foundation weeks 1–6, pull weeks 7–20, governance weeks 21+), the pull ratio metric (consumer requests fulfilled per system initiative, target 2:1 or higher), migration strategy with the "touch once, never revisit" rule, buy-in tactics that respond to the three most common skeptic arguments, and communication cadences (weekly status, monthly demo, quarterly review).

8. **You are teaching or onboarding someone to build a design system.** The skill's structure maps to a sprint series from audit to shipped component. Each step produces a concrete, reviewable artifact. The worked example in `examples/worked-design-system.md` provides a complete narrative that illustrates every phase decision with an intermediate artifact.

### Do not use this skill when

1. **You need a single component for an existing system that already has a contribution process.** That system's own governance rules take precedence over this skill's templates. Use the established process — contributing through the system's own path is faster and teaches you the system's conventions.

2. **You need a runnable UI library and already have the design decisions settled.** This skill produces design tokens, component documentation, and governance policies — not runtime code. Use the `typescript-frontend` skill to implement the components, or the `infrastructure` skill to set up Storybook. The handoff boundary is clear: this skill produces the decisions about how the UI should look and behave; other skills produce the code that realizes those decisions. A system without code is a specification; a system without specifications is a pile of components.

3. **You are doing a visual redesign that does not need structural governance.** A single-designer Figma file for a three-screen prototype does not need a design system. Use the `product-design` skill for the redesign, and return here only when more than one person builds from the result.

4. **You are evaluating design system tooling such as Storybook, Style Dictionary, or token transformers.** This skill provides methodology, not tool recommendations. Use the `infrastructure` skill for tooling evaluation and the `architecture-comparison` skill for platform selection.

5. **You are migrating an existing mature system to a different platform.** Use the `architecture-comparison` skill for platform options, then apply the governance layer from this skill for the migration process rather than the full workflow.

6. **You need CSS or runtime code.** This skill produces JSON tokens, YAML configuration, and Markdown documentation. Use the token files as input to the token-transformer or CSS-generator tool of your choice. The `infrastructure` skill has tool-specific guidance.

7. **You are debugging a single component's behavioral issue.** This skill governs the system, not individual component bugs. Use the component's own documentation and testing resources. Return to this skill when the fix becomes a systemic change — a new token, a deprecation, a component variant.

## 03 — Inputs and Outputs

### Inputs

- **The product surface.** A live or designed product with enough surfaces to establish patterns. Four surfaces is the minimum viable inventory size — fewer than that and you are speculating about which components you need. Include every route, every screen, and every dialog state, including empty, error, loading, and permission-denied states. An 80% inventory honestly labeled is better than a 100% one that silently skipped the settings pages because they were "not a priority."

- **Existing design artifacts.** Figma files, CSS declarations, Sketch files, or screenshots. Any record of existing visual decisions is an input to the inventory phase. Screenshots of the worst divergences are the most valuable artifacts because they convince skeptics that the system is needed — a side-by-side of two buttons that appear on the same screen but have different corner radii is worth a page of reasoning.

- **Accessibility requirements.** Your target WCAG level (A, AA, or AAA), platform regulatory requirements (Section 508, EN 301 549), and any regulatory obligations from customers or contracts. These determine what the token schema must enforce (contrast metadata on every semantic color token, focus indicator constraints on every interactive token) and what each component doc must cover (keyboard contracts, ARIA patterns, announcement sequences). If the target is AAA, plan for it from day one — retrofitting higher-contrast requirements later costs more than designing for it upfront.

- **Color and spacing constraints.** Brand color palette, typeface selections, logo usage rules. These define the primitive tier and bound the set the semantic tier works within. The system must mediate between brand guidelines and accessibility thresholds when a brand color fails a 4.5:1 contrast check.

- **Team context.** Who builds the system, who reviews changes, who adopts the components. Team size drives governance complexity — a two-person team needs one reviewer and same-day approval, while a thirty-person organization needs three reviewers and a three-day window. Start light: simpler governance that is followed beats comprehensive governance that is bypassed. Know the team's release authority: does the system team own its own package publish, or does every token change need a product-architecture review? Owning the publish step is the difference between a two-day release cycle and a two-week one.

- **Tooling constraints.** The target platform (web, React, React Native, plain CSS, design-to-code pipeline, Figma). These determine token output format, component scaffolding, and which parts of the schema are used. The token schema is platform-agnostic, but the output format (CSS custom properties, platform JS tokens) is not. Decide the format at the start rather than converting later.

- **Release cadence expectations.** How often the product ships determines how often the system must ship. If the product releases weekly, the system must release at least biweekly. A monthly product release cycle lets the system release monthly. The system's cadence must not be slower than the product's. If the system cannot keep pace, it becomes a bottleneck and teams start bypassing it.

- **Existing design tokens or style variables.** If the product already uses CSS custom properties, Sass variables, or a design tool token plugin, those are inputs to the token design phase. They indicate naming conventions the team is used to and values that may need migration. Do not discard them — map them to the three-tier model before retiring them.

- **Platform constraints.** Browser support matrix (which CSS features are available), performance targets (render budget, network budget), and device range (mobile, tablet, desktop, screen reader compatibility). These constrain both token values (no 3000-step color ramps on memory-constrained devices) and component behavior (no complex CSS animations on low-powered devices).

- **Governance appetite.** How much process the organization will tolerate. Measured as: how many reviewers, how many days of review window, how many layers of approval before a token can ship. A startup with two engineers and a designer needs a governance model that is three rules and one meeting per month. An enterprise with 50 engineers across 5 teams needs the full standard track with escalation paths. Start with the minimum the organization will accept — governance can always be tightened later.

### Outputs

- **Component inventory.** A per-component-type tally of surfaces, implementations, divergence scores, and a prioritized candidate list. Built from `references/component-inventory.md`. Includes a coverage check that names missed surfaces honestly. The inventory is the only artifact that describes the product as it actually exists — all other artifacts describe the system as it should be. Keep the inventory updated; when the product changes shape, the inventory is the first thing that gets stale.

- **Token set.** A three-tier architecture (primitives, semantic, component) validated against `schemas/design-tokens.schema.json` with defined values for all supported themes. Versioned independently from the product codebase. The token file is the single source of truth that CSS variable generation, design tools, and component APIs reference. The token file must have a CI gate: a commit that fails schema validation is rejected.

- **Component documentation.** One page per system component following `templates/component-doc-template.md` and `references/pattern-documentation.md`. Includes anatomy with prop and token mappings, variant combination tables with allowed combinations explicitly checked, state tables covering rest, hover, focus-visible, active, disabled, and loading with ARIA announcements for each, three to six Do/Don't pairs each grounded in a visible usability or accessibility reason, a11y notes for every component with ARIA patterns from `references/accessibility-standards.md`, the keyboard interaction table naming every key and its behavior, and copy-pasteable runnable examples for each variant axis.

- **Theme registry.** A single YAML or JSON file listing each theme, its type (brand vs. mode), its token reference, and the parent theme it extends. Validated at build time so every semantic token resolves to a value in all themes — a token that silently inherits an invisible value across a theme is a bug caught before shipping. The registry is the single source of truth for what themes exist and what inheritance chain each uses. It is versioned alongside the token file.

- **Governance process.** Documented: the versioning scheme, review tracks, deprecation policy, governance body composition, escalation path, and a first change record that establishes governance itself. Fits on two pages. A single page is better. If the governance process exceeds a two-page budget, it is too complex for the team it governs.

- **Adoption plan and case study.** A three-phase plan with measurable targets, first-adopter team identified, migration strategy with surface-by-surface priority and the "touch once, never revisit" rule, and a published first-adopter case study in the format of `references/system-case-studies.md` with pre- and post-system metrics. The case study must include at least three concrete numbers: render time (pre/post), component file count (pre/post), and a11y violations (pre/post). Numbers make the case; adjectives do not.

## 04 — Workflow

The following workflow produces a design system from an ungoverned product surface. Work through the steps in order; each step consumes the artifact produced by the previous one. The workflow assumes a mid-size product (30–60 surfaces) and a two- to four-person system team. Scale steps down for smaller teams by collapsing steps 4–6 into two weeks, or scale up by adding a governance review gate to each step (the `versioning-and-governance.md` reference provides the standard track process for each).

Durations and checkpoint questions at each step are calibrated for a first-time team. Experienced practitioners can tighten durations but should not skip the checkpoint questions — they are designed to catch the most common failures in each phase.

### Step 1: Audit the existing surface

Run a screen-by-screen component inventory using `references/component-inventory.md`. For each surface, enumerate every component instance and record its implementation, divergence from other instances of the same type, and any visual or behavioral anomalies. Include empty, error, and loading states — they are the most likely to have drifted because they are the least-visited screens and therefore the least-refactored. Work screen by screen, not component by component: component-first searching biases you toward what you already know and overlooks the third instance that nobody remembers adding.

The output is a tally sheet per component type with a divergence score: 0 (identical everywhere), 1 (cosmetic drift — spacing or color varies by a step), 2 (behavioral divergence — one instance has different states or focus behavior), or 3 (conflicting semantics — two different things called the same name). Attach a divergence appendix showing side-by-side screenshots of the three worst divergences. This appendix is the artifact that convinces skeptics because it is visual, not abstract.

Duration: one person-week per ~30 surfaces for the inventory plus divergence appendix. If the product has 60+ surfaces, split the audit across two people — each takes half the surfaces, and they cross-check each other's divergence scores. Calibration between auditors matters: one person's "divergence 1" is another's "divergence 2" without a shared example to calibrate against. Spend the first hour of the audit reviewing two surfaces together to align scoring before splitting.

**Governing reference:** `references/component-inventory.md`

**Checkpoint question:** Has the audit been run against every surface — including the empty, error, loading, and permission-denied states that are often silently skipped? Did you include empty surfaces like empty-state, error-state, loading-state, permission-denied? These are the highest-drift surfaces because they are the least-visited by the team and therefore the least-refactored. An audit that skips them describes the product as it should be, not as it is.

### Step 2: Prioritize the component shortlist

From the tally, compute a priority per component type using the formula from `references/component-inventory.md`: (Frequency + Divergence + Risk) − Effort. Define axes on a 1–5 scale and invert effort so expensive items score lower. Interactive and focus-managed components rank above static ones because they are harder to retrofit and fail bigger when broken. Choose five to eight candidates for the founding set. A typical shortlist includes at least one form component (text input, select, checkbox), one action component (button, link, toggle), and one overlay component (dialog, drawer, popover, toast). These three families cover the highest-frequency interactions across nearly every product.

Each shortlisted component gets a one-liner summary of the problem drawn from the divergence score. Do not skip this step: "Button has 12 instances, four implementations, score 3 — two colors, two corner radii, one implementation uses a `<div>` instead of `<button>`" gives the team direction and establishes the principle that the system exists to solve divergence, not to build the team's wishlist. Format each shortlist entry with the component name, divergence score, instance count, the single worst divergence, and the priority score — this table is the artifact the team reviews before any token or component work begins.

Duration: one day. The shortlist fits on one page.

**Governing reference:** `references/component-inventory.md`

**Checkpoint question:** Does your shortlist include at least one form component, one action component, and one overlay component? These three families cover the highest-frequency interactions in most products. If you have five buttons and no text inputs, you prioritized what you know instead of what the product needs. Cross-check the shortlist against the divergence appendix: are the three worst divergences represented in the shortlist? If not, the shortlist is prioritizing by familiarity rather than by impact.

### Step 3: Design the token set

Build a three-tier token architecture using `references/design-tokens.md`:

- **Primitives** as the full palette — every step of every scale, sized so theming has somewhere to go. Define them in the largest color space your production context supports (OKLCH preferred for perceptual uniformity). For every primitive, document whether it is consumed by a semantic token or exists as a future placeholder.
- **Semantic tokens** as role-named decisions the product makes: `color-bg-page`, `space-inset-md`, `radius-input`. Each semantic token resolves to a primitive token. The goal is that a theme change is a single-layer swap — re-pointing semantic tokens at different primitives and nothing else changes.
- **Component tokens** for genuine divergence: `card-shadow-focus`, `toast-inset-padding`. If a component token repeats a semantic token's value, delete it and use the semantic tier instead.

Define color ramps in OKLCH across four primary hue families (blue, red/error, green/success, yellow/warning) plus a neutral ramp of 11 steps each. The OKLCH space is preferred over sRGB because perceptual uniformity means that a 10% luminance change produces a visually uniform brightness change across all hues. sRGB's `lighten()` and `darken()` functions produce muddy mid-tones because they operate on a gamma-encoded space that does not match human perception. Each ramp uses step names 50, 100, 200, 300, 400, 500, 600, 700, 800, 900, and 950 (where 50 is the lightest and 950 is the darkest). The 11-step scale gives themes enough granularity to create depth without needing ad-hoc intermediate steps.

Build a geometric spacing scale from a base unit (4px conventional, 8px stricter) with 6–8 steps capped at the third power: 4, 8, 12, 16, 24, 32, 48, 64. The spacing scale uses a mixed geometric-arithmetic progression: steps double from 4→8 and from 8→16, then the intermediate 12px step is added for the specific gap between icons and labels where the doubling step (16px) is too large. From 16 onward, the scale doubles: 16→32→64. The cap at 64px is deliberate — anything larger is a layout concern (grid column, page margin) and should be handled by the application layout layer, not the component spacing layer.

Define a type scale at ratio 1.25 for product UI or 1.333 for editorial surfaces. Ratio 1.25 produces 5 steps: 14, 16, 20, 24, 32. This is compact enough that every step is used — a larger ratio (1.333, producing 12, 16, 21, 28, 37) works for editorial surfaces where text hierarchy carries more information. Choose your ratio based on the surface: product UI needs tight spacing and legibility at small sizes; editorial surfaces need visible hierarchy at large sizes.

Each token proposal uses `templates/token-spec-template.md` with: the name, rationale, two or more consumption surfaces, theme implications for every theme, a contrast check pair for every semantic foreground-background relationship, and the defined migration path. Validate each token against `schemas/design-tokens.schema.json` before committing.

Duration: one to two weeks for a token set of 30–50 primitives and 20–40 semantic tokens. This is the most architecturally important step — time spent here repays itself throughout the system's life.

**Governing reference:** `references/design-tokens.md`, `templates/token-spec-template.md`, `schemas/design-tokens.schema.json`. Validate every proposed token against the schema before adding it to the token file — the schema is the gate that prevents naming violations, missing theme values, and type errors. A proposal that passes schema validation is structurally valid; a proposal that fails it is rejected without human review, which saves the governance body's time for questions the schema cannot answer.

**Checkpoint question:** Does every semantic token have a dark theme value declared at proposal time? If not, the component that consumes it will fail under dark mode — demote it to a component token and let the component that needs it handle the theming exception.

### Step 4: Document the first component batch

Document the shortlist (from Step 2) using `templates/component-doc-template.md` following `references/pattern-documentation.md`. Each doc must include:

- **Summary** naming when it is appropriate and not appropriate for the component.
- **Anatomy** mapping each named part to a prop and a token.
- **Variant combination table** listing allowed combinations and explicitly marking disallowed ones.
- **State table** covering rest, hover, focus-visible, active, disabled, and loading with ARIA announcements.
- **Three to six Do/Don't pairs** each grounded in a usability or accessibility reason.
- **A11y notes** with ARIA pattern name, accessible name source, focus behavior, and one concrete verifiable test.
- **Keyboard interaction table** naming every key and its behavior.
- **Runnable examples** for each variant axis, copy-pasteable.

The variant combination table is the single most valuable line in the doc, because it converts "the design says so" into a rule a reviewer can enforce without repeating the conversation. The allowed-combination format from `references/pattern-documentation.md` shows the standard layout.

Duration: one to two days per component, depending on complexity. The first component (typically the Button) takes the longest because the team establishes the documentation conventions. Subsequent components are faster — the team copies the template, fills in the structure, and reviews against the established conventions.

**Governing references:** `references/pattern-documentation.md`, `templates/component-doc-template.md`, `references/accessibility-standards.md`

**Checkpoint question:** Can an engineer who has never seen the component ship a correct instance using only the doc and the component's source code? If not, the doc is not ready. Hand the doc to someone who was not on the team and watch them try to use it. Time how long they take. If they need to ask a question, the doc needs revision. If they complete the task in under two hours, the doc passes.

### Step 5: Apply accessibility requirements

Verify each doc against the checklist from `references/accessibility-standards.md`. Run automated contrast checks for every text-on-background pair that the components actually render — not every possible pair, but every pair that appears on at least one surface — tested across all themes. Verify the focus indicator passes at 3:1 ratio against the component's adjacent surface. Map each component to one of the listed ARIA patterns from the reference file.

Run all four testing layers at this step: automated lint (axe-core in CI, fail the build on any violation), keyboard audit (manual Tab, Shift+Tab, arrow keys, Enter, Escape, and Space traversal of every state), screen reader audit (NVDA or VoiceOver documenting the announcement sequence for each state), and a user test with 3–5 assistive technology users before the first MAJOR release.

Document the audit results in the component doc's a11y section: which tests passed, which were beyond scope, and the date of the last audit. The a11y section must be reviewed by the accessibility champion before the component ships. A component with an a11y section that has not been reviewed by the accessibility champion is not ready for release — the component doc is blocked regardless of how complete the implementation is.

Duration: two to three days per component for a first-time audit. The first a11y audit takes the longest because the team establishes the testing conventions and writes the component-specific YAML pair file for the contrast regression. After the first component, subsequent audits are faster — the pair file template exists, the keyboard audit checklist is established, and the screen reader test script can be reused.

**Governing reference:** `references/accessibility-standards.md`

**Checkpoint question:** Does every interactive component have a documented focus-visible state with a visible focus indicator at 3:1 minimum in all themes? If it uses hover-only affordances, it does not pass. If there is no focus-visible state documented, the component is not eligible for any claim of conformance.

### Step 6: Design theming architecture

Using `references/theming-architecture.md`, define the theme registry: one file listing each theme, its type (brand or mode), the theme it extends, and the token file it references. For mode themes (light, dark), derive values by luminance inversion (systematically swapping the luminance ladder) and saturation reduction (by 60–80% on large surfaces) for readability. For brand themes, define custom primitive palette overrides without adding new semantic tokens to the common set — brand-specific meaning stays inside the brand theme's override file.

Run a contrast sweep against every text-on-background pair rendered by at least one component in each theme. Fail the build on any WCAG 2.1 AA violation. CC exceptions cover only decorative elements and require written approval from the accessibility representative.

Test all four layers from the reference:
1. Contrast sweep per theme — every rendered pair, not every token pair.
2. Surface mapping — each component renders correctly in all themes.
3. Color meaning preservation — red means error in all themes; green means success.
4. Extensibility check — a new brand theme can be written by overriding no more than 40% of primitive values.

Duration: one week for the first two theme variants, plus one day per additional theme. The first theme pair (light + dark) is the most expensive because the team establishes the luminance inversion pattern and writes the contrast sweep YAML pair file. Subsequent themes reuse the pair file and only change token values — the test framework is built from the first pair.

**Governing reference:** `references/theming-architecture.md`

**Checkpoint question:** Does every semantic token resolve to a valid value in every theme you are shipping? If a theme silently inherits a value that produces invisible text or insufficient contrast, it is not ready to ship.

### Step 7: Establish governance

Using `references/versioning-and-governance.md`, define the versioning scheme: MAJOR for breaking (token removal, component API change, behavioral change), MINOR for additive (new components, new tokens, new themes, new variants), PATCH for fixes (value corrections, a11y patches that do not change the API, doc corrections). The version is independent of the product — the system's version is the system's contract.

Define two review tracks with these roles:

- **Fast track** — one reviewer from the system team, ships same day. For patches (color value fixes, typo corrections) and documentation-only changes. The fast track reviewer must confirm that the change is indeed a patch and has not slipped a behavior change into a patch release.
- **Standard track** — three reviewers: one system lead, one consuming team representative, one accessibility representative. Minimum three business days. For all MINOR and all MAJOR changes. Each produces a change record (a `.md` file in the system's `changelog/` directory) stating the change, the rationale, the affected files, and the migration path.

Define the deprecation policy: a token remains available for at least two MINOR releases (or one MAJOR) before removal. During deprecation, mark the item as deprecated, emit a build warning when referenced, and name the replacement. Require a migration path for every removal. The migration path must include a code example showing the before and after — a consumer reading the deprecation notice should be able to find-and-replace the old token with the new one without referencing any other documentation.

Write the first change record: "Establish governance process" as the system's first governance decision, with the date and authors.

Duration: two days.

**Governing reference:** `references/versioning-and-governance.md`

**Checkpoint question:** Does every consumer team know when the next release is, how to propose a new component, and what happens when a breaking change ships? A governance process that is not communicated will be bypassed. Have you published the release calendar and the intake request template to the consumer channel? If consumers cannot find the governance documents without asking, the process exists but nobody uses it.

### Step 8: Plan adoption

Using `references/adoption-strategies.md`, define a three-phase adoption plan. Identify the first-adopter team candidate before the token work begins — choose by enthusiasm, not by mandate. A volunteer team ships faster and produces a better case study. If no team volunteers, build the foundation phase with a small internal prototype (a single surface reimplemented by the system team alone) and present the case study as evidence before asking another team to adopt.

- **Foundation phase (weeks 1–6):** Tokens, two to three components, documentation, and one rebuilt production surface. The surface must be a real product surface used by real users — not a showcase page. A real surface produces real metrics (render time, a11y violations, CSS imports, team development time) that are credibly comparable to the pre-system state.
- **Pull phase (weeks 7–20):** Bi-weekly MINOR releases. Track two metrics — adoption rate (target 60%) and pull ratio (target 2:1). During this phase, the system team's primary goal is responsiveness to consuming team requests. Every component that ships should have a consuming team ready to use it in the same release cycle.
- **Governance phase (weeks 21+):** Governance body meets quarterly. Deprecation enforced. Adoption target: 80% of new surfaces.

Migration strategy: high-frequency, low-variance surfaces first (a table view with 50 rows using 3 component types is the easiest migration target), touch-once surfaces in redesign (if a surface is being rebuilt anyway, the migration cost is negligible), audit-before and measure-after for each (publish render time, file count, and a11y violations for every migrated surface as a case study appendix). Do not migrate a surface that works fine and is not being touched — the system's value improves over time without the migration cost, and forcing migration on a stable surface risks breaking something that nobody was asking to change.

Communication cadence: weekly status post (4–6 bullets in the consuming team channel covering what shipped, what is in review, what broke, what the system team needs to know — never longer), monthly demo (invite all consuming teams, show the latest components, share first-adopter results with concrete numbers, announce deprecations, serve food — the demo is the primary vehicle for building organizational consent), quarterly governance review with published minutes (adoption metrics, open issues, roadmap for the next quarter).

Duration: one to two days to draft the full plan.

**Governing reference:** `references/adoption-strategies.md`

**Checkpoint question:** Has the first-adopter team been identified, does it have dedicated capacity, and have you published pre-system metrics for a credible comparison? A first adopter without time does not ship — choose a different team.

### Step 9: Build the first-adopter surface

The first-adopter team rebuilds one production surface using only system tokens, components, and patterns. The surface must ship before the system is "complete" — treat week 6 as a hard deadline. Measure pre- and post: render time, CSS import count, component file count, a11y violations, and development time for one standard change (e.g., adding a new variant to the migrated surface). Every metric must be measured twice: once before migration and once after. A metric measured only once is a guess, not a data point.

Publish results as a case study following `references/system-case-studies.md` format: team context, timeline, what worked, what the team would do differently, specific numbers, and at least one direct quote from a team member about what the system did and did not improve.

The case study has three jobs: (1) convince other teams that the system reduces friction, (2) reveal what the system does not yet handle well, and (3) provide baseline metrics for future adoption phases. A case study without metrics is a story; one with metrics is a contract.

Duration: two to three weeks from tokens to a live surface with the shortlisted components. This duration assumes the first-adopter team has dedicated capacity and the shortlisted components are four to six in number. If the shortlist is larger or the team is shared with product delivery work, extend the duration but do not expand the shortlist — shipping a small surface on time is more valuable than shipping a large surface three weeks late.

**Governing reference:** `references/system-case-studies.md`

**Checkpoint question:** Did the first-adopter surface ship faster or more reliably than it would have without the system? If not, the system is adding friction and must be fixed before further adoption.

### Step 10: Iterate and govern

After the first-adopter surface ships, the governance processes from Step 7 become active. Run a MINOR release every two weeks. Track the pull ratio every cycle — if it drops below 1:1 for two consecutive releases, stop building new system capabilities and fulfill consumer requests exclusively until the ratio recovers above 2:1. Track the deprecation window for every token and component that entered the deprecation cycle — publish a deprecation calendar alongside the release schedule so consumers can plan their migration work.

Transition phases by metrics, not the calendar:
- Foundation → Pull: when the first adopter ships. Before this milestone, the system team operates without governance overhead — fast track only for every change.
- Pull → Governance: when the adoption rate passes 60%.
- Governance → System maturity: when the pull ratio stays above 2:1 for four consecutive releases without a dip below 1.5. At this point, the system has enough surface area and consumer trust that ungoverned growth would erode coherence. The governance body may begin delegating fast-track review authority to consuming team representatives.

Schedule quarterly governance meetings with published minutes. Revisit the token schema quarterly: delete tokens that have zero production usage in two or more releases. A palette that only grows and never shrinks becomes unusable within two years. Run a token count vs. surface count ratio on the same quarterly schedule — a ratio above 0.3 is a warning that tokens are growing faster than the product surface, and the surplus tokens should be audited for consolidation or deprecation.

**Governing references:** `references/versioning-and-governance.md`, `references/adoption-strategies.md`

**Checkpoint question (recurring):** Has the pull ratio been above 1:1 for two consecutive release cycles? If not, stop building new components and fulfill consumer requests first. Is the deprecation window for every active deprecation still within bounds? A deprecation that passes its removal date without action is a governance failure for the whole system.

## 05 — Rules and Quality Bar

1. **Audit before you design.** A system built without an inventory serves the interface the team imagines, not the one that exists. The divergence score is the most important number in the system's first month — it tells you where the pain is and where to start building.

2. **Tokens before components.** The token set must exist before the first component doc is written. Tokens are the shared vocabulary that makes a component library coherent rather than a pile of bespoke parts that happen to share a file.

3. **Semantic tier smaller than primitive tier.** If your semantic count matches your primitive count, the indirection layer has no value. A 1:1 mirror tier is cost without benefit. Primitives are the paint store; semantics are the painting.

4. **Every semantic token needs a dark value at proposal time.** A token that cannot declare a dark counterpart will produce invisible text when a dark theme ships or require a midnight emergency fix. The schema enforces this.

5. **Component docs are contracts, not novels.** One page per component, two pages hard limit. The doc must enable a new engineer to ship a correct instance in one afternoon using only the doc and the source code. If the doc requires the reader to open a second artifact (design file, specification document, email thread) to use the component, the doc is incomplete.

6. **Every interactive component must have a focus-visible indicator at 3:1 minimum contrast.** Pointer-only affordances exclude keyboard users and violate WCAG 2.1.3. This is verified by automated checks in CI. A component that passes pointer testing but fails keyboard testing does not ship.

7. **Do not number a release without a changelog.** The changelog is the contract between the system team and its consumers. Every change — PATCH, MINOR, MAJOR — must be logged before the release ships.

8. **First-adopter surface ships before the system is complete.** A system not proven on a real surface is a plan, not a product. The first adopter must ship by week 6 and its metrics must be published.

9. **New tokens require two documented consumption surfaces.** A one-surface token is too narrow — use a component override instead. The two-surface rule prevents token set growth for edge cases.

10. **Governance grows with adoption, not before it.** Apply governance when adoption passes 60%, not on day one. Premature governance creates friction without the scale to benefit from it.

11. **Deprecate only with a migration path.** Removing a token or component without naming the replacement and removal version is abandonment. Every deprecation enters the changelog.

12. **Measure adoption by imports, not by appearance.** If it does not import from the system package, it is not system adoption. Imports do not lie.

13. **Reject any token proposal that fails contrast check at proposal time.** A token that does not meet WCAG AA when proposed will not meet it at ship time. A written accessibility exception from the governance body is the only escape.

14. **Build dark theme in parallel with light — not as a follow-up.** A theme that launches six months late erodes trust because it breaks when the light tokens change. Ship both from the first MAJOR. Dark mode is not a feature — it is an accessibility requirement that the WCAG 2.1 guidelines treat as an affordance, not an option.

15. **The component doc a11y section is a checklist, not an essay.** Name the ARIA pattern, accessible name source, focus behavior, and one verifiable test. Every item must be testable right now. A writable assertion that can be automated is worth ten paragraphs of explanation. If a rule cannot be tested, it does not belong in the doc.

16. **No system survives its first encounter with a real deadline untouched.** Therefore: prioritize tokens and first surface over full documentation; a11y baseline over ideal API; working governance over future-proof coverage. Ship what you can verify, iterate what you cannot.

17. **Do not version a release without verifying all themes.** Every theme must pass contrast for all its rendered pairs before the release label is stamped. Schema check takes one minute; contrast check takes five. The release does not ship without both. A theme that fails contrast check is a breaking change for users who rely on that theme — ship it as a patch fix in the same release cycle rather than waiting for the next minor.

18. **Consumer team requests weigh more than system team preferences.** The pull ratio rule (2:1) ensures the system ships twice as many consumer-requested features as self-initiated features. This keeps the system responsive. A system team that ignores this rule builds features nobody uses and burns the budget on internal priorities — the pull ratio is the metric that prevents that.

## 06 — Worked Example: TaskFlow

The following example traces the full workflow applied to **TaskFlow**, a fictitious small web application for personal task management. TaskFlow has two team members, a twelve-week MVP timeline, and discovers at week three that three components have four implementations each. The complete artifact set is documented in `examples/worked-design-system.md`. This section summarizes the arc and provides detail on key design decisions that are transferable to other products. The worked example should be read alongside the examples directory — the examples file contains every intermediate artifact referenced here, while this section explains the reasoning behind each decision.

### Context

TaskFlow ships across 8 surfaces: a task list (the primary surface), a task detail view, calendar view, settings panel, empty state, error state, loading state, and a quick-add dialog. In week three, a visual audit reveals 12 button instances across 4 implementations with divergence score 3 — the highest in the product. A clickable button uses 4px, 12px, and 16px radius implementations across different screens. Primary actions use three different blue values that were established at different points in the product's history and never reconciled. One button is a `<div>` with a click handler and lacks all the accessibility behavior of native `<button>` — no enter-to-activate, no focus indicator, no role. The team decides to systemize with 9 weeks remaining before the MVP deadline.

### Audit and shortlist

The inventory following `references/component-inventory.md` produces a tally table across all 8 surfaces. The audit reveals 8 candidate component types: Button, TextInput, Card, Badge, Select, Checkbox, Toggle, and Dialog. Four have divergence scores of 2 or higher: Button at 3 (conflicting semantics — 4 implementations that call themselves the same name but behave differently), TextInput at 2 (behavioral drift on focus — focus ring exists on one, missing on another, shadow border on a third), Card at 3 (sometimes clickable, sometimes not — the name serves two jobs: an interactive navigation target and a static info container), and Dialog at 2 (full-screen modal vs small popover, both called "Dialog" in code). The team shortlists these four plus Badge and Select as low-effort additions with high-frequency usage. Priority scores from the formula: Button 14, Dialog 13, TextInput 11, Card 10, Badge 7, Select 6.

### Token design decisions

Using `references/design-tokens.md`, the team designs 56 primitives and 38 semantic tokens with both light and dark values from day one.

**Color architecture:** Four OKLCH hue ramps at 11 steps each — blue (brand primary), red (error and destructive), green (success and completion), yellow (warning and caution). Each ramp is constructed with luminance steps that cluster more tightly on the near-white end (50–200) and spread wider in the mid-tones (300–700) for text contrast, where perception is most sensitive to luminance differences. This non-uniform spacing is deliberate: the near-white steps differentiate subtle surface backgrounds, while the mid-tone steps need visible contrast jumps for text readability.

**Spacing scale design:** An 8-step geometric scale: 4, 8, 12, 16, 24, 32, 48, 64. The 12px step has a one-line justification: "The gap between button label and icon is too large at 16px and too tight at 8px." All other gaps and paddings resolve to one of these values — no exceptions. The scale is capped at 64px; anything larger is a layout concern, not a spacing token. The team documents the justification for every scale step at proposal time so future designers know why 12px exists and do not add 14px or 20px.

**Type system:** A 5-step scale at ratio 1.25: font-size-sm (14px — small labels, captions, metadata), font-size-md (16px — body text, form values), font-size-lg (20px — section headings), font-size-xl (24px — subheads), font-size-2xl (32px — page titles). Each size pairs with a line-height ratio (1.5 for body, 1.25 for headings) and a font-weight slot (400 for body, 500 for emphasized body, 700 for headings). The line-height values are calculated per size, not uniform: 14px text gets 1.5 (21px), while 32px text gets 1.25 (40px), because small text needs proportionally more leading for readability.

**Radius:** 3 steps: sm (4px), md (8px), full (9999px for pills and circles). The team deliberately does not add xl (16px) — the product has no use for it, and adding it preemptively would create a design target that would eventually need to be used somewhere.

**Shadows:** 3 elevation levels: low (cards — close to the surface), medium (popovers, tooltips — lifted off), high (modals, drawers — float above everything). Each shadow token stores the full `box-shadow` declaration rather than individual offset values, because developers consistently misconfigure shadow colors when assembling them from primitive parts.

### Component documentation: Button

The team documents Button as the first component following `templates/component-doc-template.md` and `references/pattern-documentation.md`.

**Anatomy:** Container (prop `intent`, token `color-bg-button-primary`), Label (prop `children`, token `color-text-on-primary`), Icon optional (prop `icon`, token `space-inline-icon`), Spinner loading state (prop `loading`, token `color-spinner`). The spinner replaces the label entirely when loading is true — it does not stack with the label.

**Variant combination table — explicitly disallowed combination documented:**

|             | sm | md |
|------------|----|-----|
| primary    | ✓  | ✓   |
| secondary  | ✓  | ✓   |
| destructive| ✗  | ✓   |
| ghost      | ✓  | ✓   |

The destructive-sm disallow is deliberate: "Small destructive buttons are too close to other actions for safe accidental activation. At md, the user must travel farther to commit — 48px minimum touch target. Do not create a destructive-sm variant without an accessibility review." The disallow is documented with a reason in the variant table, not just a symbol. This converts the design decision into an enforceable rule.

**Width variant added:** `full` (100% width of parent) and `inline` (shrink-wrap). The `full` variant sets `width: 100%`; the `inline` variant is the default.

**State behavior table:**

| State          | Visual change                             | Trigger              | ARIA announcement                |
|---------------|-------------------------------------------|----------------------|----------------------------------|
| rest          | filled bg per intent color                | default              | —                                |
| hover         | bg lightens or darkens 10% L              | pointer enters       | —                                |
| focus-visible | 2px offset outline at color-focus-ring    | Tab / keyboard nav   | —                                |
| active        | bg darkened 15% L                         | pointer down / Enter | —                                |
| disabled      | opacity 0.4, cursor not-allowed           | disabled prop        | aria-disabled="true"             |
| loading       | spinner replaces label, width preserved   | loading prop         | aria-busy="true", button disabled |

The width preservation during loading state is a specific architectural decision: when loading is true, a hidden container matching the longest label string prevents layout shift in a row of buttons where one enters the loading state. This is documented in the state notes.

**Keyboard interactions:**

| Key          | Action                     |
|-------------|----------------------------|
| Tab         | Focus enters               |
| Enter/Space | Activate the action        |
| Shift+Tab   | Focus leaves               |

### Component documentation: TextInput

TextInput has divergence score 2. The team reconciles the three implementations into one consistent interface.

**Anatomy:** Container → Label → Input → Helper text (error text replaces helper on validation failure) → Leading/trailing affordance. The label is always visible — visible label is a non-negotiable accessibility requirement.

**Variant axes:** size (sm, md) and element (default, with-icon). Both sizes preserve the visible label — sm shrinks the input control but keeps the label at body reading size.

**State table:**

| State    | Visual                                | Trigger              | ARIA announcement                                 |
|---------|----------------------------------------|----------------------|---------------------------------------------------|
| rest    | 1px border at color-border-input       | default              | label associated via for/id                       |
| hover   | border darkens 1 step                  | pointer enters       | —                                                 |
| focus   | color-focus-ring outline at 2px offset | Tab / click          | —                                                 |
| disabled| bg gray-100, opacity 0.4, no focus ring| disabled prop        | aria-disabled, not `<input disabled>` — remaining focusable for assistive tech context |
| error   | border color-text-error, aria-invalid  | error prop string    | aria-describedby points to error text element ID  |
| filled  | value non-empty                        | user types           | —                                                 |

**Do/Don't pairs:**

1. **Do:** Use the `label` prop for a visible label. **Don't:** Use `placeholder` as the only label — placeholder disappears on input, fails WCAG 1.4.1, and is inaccessible to screen readers in most browsers.
2. **Do:** Set `error` prop with a user-facing string. **Don't:** Change border to red without setting `aria-describedby` to the error text — color-only error indication is invisible to screen reader users.
3. **Do:** Use `type` appropriately (text, email, url, tel). **Don't:** Use `type="number"` for postal codes, IDs, or phone numbers — use `inputMode="numeric"` for mobile keyboard optimization without the spin-button behavior.

**A11y notes:** Pattern: textbox. Label associated via `<label for>` or `aria-labelledby`. Error text linked via `aria-describedby`. The input has `aria-invalid="true"` set when error prop is a non-empty string. Focus flows to the first invalid input when a form is submitted with errors.

### Component documentation: Card

Card has divergence score 3 — the product uses "Card" for two distinct jobs: a static container (metadata block) and a clickable navigation target (task list items). The team distinguishes them with `variant="default"` and `variant="interactive"`.

**Anatomy:** Container (box-shadow, rounded, bg) → Header (title + optional subtitle) → Body (slot content) → Footer (optional actions). The interactive variant renders as `<button>` or `<a>` — never a `<div>` with `onClick`, because a `<div>` has no default enter-to-activate behavior and no accessible role without explicit assignment.

**Do/Don't pairs:**

1. **Do:** Use `interactive` when clicking the whole card triggers navigation or an action. **Don't:** Nest buttons inside an interactive card — nested interactive elements trap keyboard users and create ambiguous click targets.
2. **Do:** Use `bordered` variant for cards on a background surface (sidebar, settings). **Don't:** Stack shadow cards — stacked shadow creates unintended depth.
3. **Do:** Keep content semantic: `<h2>` or `<h3>` for the title, `<p>` for the body. **Don't:** Use div-soup inside cards — use proper semantic structure.

### Governance setup

Before shipping the first production surface, the team defines minimum governance from `references/versioning-and-governance.md`:
- **Tracks:** Fast track (one reviewer, same day) for patches and docs. Standard track (three reviewers, three days) for new tokens, components, and breaking changes.
- **Deprecation:** Two MINOR releases notice with migration path.
- **Release cadence:** Bi-weekly MINOR, quarterly MAJOR.

### First-adopter surface

The team rebuilds the main task list surface with measurable outcomes:

| Metric                          | Pre-system | Post-system |
|--------------------------------|------------|-------------|
| Render time                    | 980ms      | 620ms       |
| CSS imports on surface         | 12         | 3           |
| Component files imported       | 7          | 5           |
| A11y violations (automated)    | 14         | 0           |
| Time to add new filter dropdown| ~4 hours   | ~30 minutes |
| Time to add new component variant| ~3 hours   | ~15 minutes |

The rebuild takes 4 days. The team publishes these numbers as the case study. The pattern scales: a two-person team with a 9-week runway and a clear shortlist produces a working system that reduces render times by 37%, eliminates a11y violations, and cuts CSS imports by 75%.

### What the example proves

A two-person team with five components and eight weeks produces a measurable, working system. Key patterns: start with inventory, tokens before components, both themes from day one, governance light, publish real metrics. The TaskFlow pattern is transferable to any web product: replace the surface nouns (task list → your core screen) and component names with your own audit findings, and the same structure applies. The specific numbers (render time, a11y violations, CSS imports) are the template for any case study — publish the same metrics for your own first-adopter surface so the next team can compare their expected benefit against a real result.

## 07 — Development Workflow

Building a design system means establishing a rhythm, not completing a checklist. The development workflow below integrates token design, component implementation, and documentation into a single sustainable loop.

### The development loop: Token → Component → Doc → Verify → Release

Each cycle produces one or two release-ready components:

1. **Propose tokens.** Before writing any component code, propose the tokens the component needs using `templates/token-spec-template.md`. Token proposals are validated against `schemas/design-tokens.schema.json` and the governance track. A new component must not introduce tokens that are not defined at the schema layer.

2. **Implement the component.** Build the component per its documented anatomy and variant spec, referencing tokens as CSS custom properties. Component code is at the bottom; token values are at the top. The component must never embed a hard-coded color or spacing value.

3. **Write the doc.** Use `templates/component-doc-template.md` following `references/pattern-documentation.md`. Document the public API: props, slots, events, style hooks, and keyboard contract.

4. **Verify accessibility.** Run automated a11y tests (axe-core or equivalent in the component test suite), keyboard-only traversal, and screen-reader tests. Document the verification.

5. **Review.** Submit for governance review (standard track for new components, fast track for patches). Every review references a changelog entry.

6. **Release.** Ship in the next MINOR release per the schedule. The component is tagged with the release version in the changelog, the doc frontmatter, and the component's source file header. Each release produces a git tag, a published npm package, and a documentation site update — all three must exist for the release to be considered complete.

### Daily development rhythm

Each day in a design system build cycle follows a rhythm that balances production work with maintenance:

- **Morning check** (15 min): Review consumer channel for intake requests, bug reports, and questions. Respond or triage before starting the day's feature work. This prevents a day of building from being interrupted by a question that could have been answered in two minutes.
- **Feature block** (3–4 hours): The day's primary work — tokens, component implementation, documentation, or testing. No meetings, no channel notifications. Use this block for the token-propose → component-build → doc-write → verify loop.
- **Afternoon review** (60–90 min): Code review of a PR from another team member, governance review of a change record, or doc review of a component that is under governance review. The review is done before 4pm so the author can process feedback before the end of the day.
- **End-of-day** (15 min): Update the release branch's changelog if anything was merged. Update the consumer channel status post. Close out any stale review requests.

This rhythm applies during the foundation and pull phases. During the governance phase, the feature block shrinks to make room for governance meetings and intake triage.

### Estimate sizing

Before starting work, each component or token proposal gets a size estimate in the intake process. The size determines how the work fits into a release cycle:

| Size | Time | What it covers | Governance track |
|------|------|---------------|------------------|
| XS | 0–2 hours | Doc fix, existing token reconfiguration, schema correction | Fast track |
| S | 2–8 hours | New variant of existing component (e.g., new intent for Button) | Standard track |
| M | 1–3 days | New component within the shortlist, full doc, a11y review | Standard track |
| L | 3–5 days | New component outside the shortlist, full governance approval | Standard + governance |
| XL | 5+ days | Displaces other work — needs governance body approval for reprioritization | Governance decision |

The size brackets serve as a communications tool: when a consumer requests a component, the system team replies with the size estimate and the expected release window. A consumer who knows their request is an L knows it competes with other work and may make the business case to the governance body. A consumer who gets an XS knows it will ship in the next release without negotiation.

This loop repeats every release cycle (two weeks). During the pull phase, the system team times ahead of consumer requests while maintaining the pull ratio.

### Branching strategy

The system codebase and tokens live on independent branches from the product codebase:
- **main** — stable release branch. Tokens and components here have passed governance, doc checks, and a11y audits. Merging to `main` requires: passing CI (all 4 pipeline stages), completed handoff checklist, and governance body sign-off for any MINOR or MAJOR change. PATCH changes on `main` require only CI pass and one system-team reviewer.
- **feature/...** — individual component or token development. Branched from `main`, merged back via PR. Each feature branch must include: the component implementation (if applicable), the component doc (if applicable), any new tokens (validated against the schema), and the component's Do/Don't pairs (reviewed by at least one person outside the system team). A feature branch that fails CI on three consecutive pushes is escalated to the system lead.
- **release/** — release candidate branch. All features for the release are merged here. The branch runs full CI: contrast sweep against all themes, visual regression against all stored baselines, a11y axe-core scan of every component variant. CI on the release branch must pass before the governance body considers tagging. A release branch that fails CI for more than three days triggers a postmortem — why did failing code reach the release branch?
- **hotfix/** — for PATCH releases. Bypasses governance (fast track only), merges directly to main. A hotfix must include: the fix itself, a one-sentence justification for why it could not wait for the next release cycle, and a changelog entry. Hotfixes are reviewed by the system lead within 24 hours.

The branching strategy enforces a quality gate: code moves from left (feature) to right (main, release) only through CI-verified gates. A bypass (committing directly to main) triggers an escalation.

### Component development checklist

Before a component enters the release branch:

- [ ] Token set defined and validated against schema.
- [ ] Component consumes no hard-coded values — all visuals reference tokens.
- [ ] Component has named part mapping for theme overrides.
- [ ] Do/Don't pairs written and reviewed by at least one person outside the system team.
- [ ] A11y checklist complete and signed off.
- [ ] Focus indicator verified (focus-visible) at 3:1 against adjacent background.
- [ ] Keyboard contract documented per `references/accessibility-standards.md`.
- [ ] All themes verified visually and with automated screenshot diff.
- [ ] Component doc reviewed and assigned an owner (a role, not a person).

## 08 — Quality Assurance and Testing

A design system that is not tested is not trustworthy. Each component and token must pass through multiple layers of rigor, with cost increasing from left to right. Every release must pass at least the first three layers.

### Layer 1 — Schema validation

`schemas/design-tokens.schema.json` runs against the token file at every commit. The schema catches: invalid token names (naming rules from `references/design-tokens.md`), missing data values (token must reference an existing primitive), undefined scale steps (a value outside the declared scale), and malformed dark-theme declarations (missing, incomplete, or referencing a non-existent primitive). A failing token blocks the PR.

Integrate via a `pnpm validate-tokens` hook in pre-commit or as a PR gate. Output is a plain-text list of problems, each with the token name and the rule violated. Each violation names the specific line in the token file so the author can fix without running the schema tool.

### Layer 2 — Contrast regression

A contrast check against every rendered foreground-background pair in each theme. Pairs are defined by a YAML mapping file that lists which token pairs are actually rendered by each component: `foreground-token: background-token`. Writing this file is a one-time cost during component creation — for each state of each variant, list the text-on-background pairs that appear. The regression check is fully automated after that. The YAML file looks like:

```yaml
button:
  primary:
    rest:
      - foreground: color-text-on-primary
        background: color-bg-button-primary
    hover:
      - foreground: color-text-on-primary
        background: color-bg-button-primary-hover
    disabled:
      - foreground: color-text-disabled
        background: color-bg-button-primary-disabled
```

Fail the build on any WCAG 2.1 AA violation: 4.5:1 for normal text, 3:1 for large text (18px+ bold or 24px+ regular). For AAA targets, run a separate check with AAA thresholds and tag the results as advisory rather than blocking — AAA on every text pair is rare and should be a governance decision, not an absolute rule.

### Layer 3 — Visual regression tests

Automated screenshot diffing per component, per theme, per variant, per state. A canonical set covers 1–2 states per component — not every state because 70+ components × 10 states × 2 themes = 1400 screenshots is uneconomical. Choose the most complex state (loading, error, or interactive) and the default rest state for each component. Each test asks: does the component under theme X look like its spec screenshot? A diff failure must be reviewed and either corrected (if the spec is wrong) or accepted as a new baseline. Use a tool that supports approval workflows — a human reviews each diff and approves or rejects it.

Integrate via Storybook with Chromatic, Loki, or Percy. Run on every MINOR release. Storing baselines in the repository alongside component code prevents drift between repo state and test expectations. If the team uses Figma, the spec screenshots come from the design file at a known version; the visual regression compares the rendered component against the Figma-sourced baseline, not against a previous render pass. This catches design-to-implementation drift as well as code-to-code drift.

### Layer 4 — Integration regression

A small set of integration tests derived from the first-adopter surface. The main task list (from the worked example in Section 06) serves as the canonical test case — it uses all system component types in one view. Compare rendered output against a known-good baseline image per release. If the integration regression fails, it means a component change broke the composition use case, even if every component passed its individual visual regression. Keep this test set small — three to five views maximum — because each one is expensive to maintain. Rotate the test views each quarter to match the surfaces that have changed most. The integration test set is agreed upon by the governance body and updated quarterly.

### Layer 5 — Component unit tests

Every component variant must have a unit test that verifies:
- **Rendering:** Each variant renders the expected DOM structure. Test the default variant, one non-default variant per axis, and the disabled state.
- **Props:** Each prop produces the expected behavior. Test the prop's default value, an explicit value, and an invalid value (the component should fall back to default, not crash).
- **Events:** Each emitted event fires with the correct payload and at the correct time.
- **Edge cases:** The component handles empty children, null props, and unexpected types without throwing. Use a test helper that wraps the component in a theme provider to ensure token resolution works in the test environment.
- **Accessibility:** Automated a11y checks run on every variant using axe-core in the test runner. A component with a11y violations in its unit tests does not pass review.

Unit tests are run on every PR push and must pass before merge. A component with failing unit tests is not included in the release. The unit test suite is the first gate in the CI pipeline — it runs before visual regression, before integration tests, before the contrast sweep — because failing unit tests indicate a fundamental implementation error that makes higher-level tests uninformative.

### Layer 6 — Manual a11y audit

At each MAJOR release, complete the full a11y checklist for all components: tab order, focus indicators, label presence, roles, state announcements, and keyboard interaction. This is the slowest layer and justifies investment in automation of the earlier layers. Document each finding with the component name, state, and the fix or exception. The manual a11y audit is the last layer before the release candidate is tagged — if it fails, the release must be delayed until every finding is resolved or acknowledged with a documented exception approved by the accessibility champion.

### Layer 7 — Screen reader user tests

Before each MAJOR release, test with 3–5 participants who rely on assistive technology (NVDA, JAWS on Windows; VoiceOver on macOS). Test 5 key flows entirely by screen reader. Document the announcement sequence and confirm: does the screen reader communicate every state change? Can a user complete the flow without vision? This is the most expensive layer and catches the most subtle bugs — missing announcements, incorrect focus order, ambiguous roles.

### Layer 8 — Adoption measurement

Monthly, count system imports in product telemetry: CSS imports and component file usage per surface. Surface-level granularity is important — a per-file count masks the situation where one page uses 10 system components and another uses none. Use this for the adoption rate and pull ratio calculations. If adoption drops or plateaus, survey the consuming teams to learn why. Common reasons for plateau: the system does not cover the components the team needs, the documentation is stale, or the governance process is too slow. Each reason has a different corrective move — skipping the diagnosis wastes time on the wrong fix.

Publish the adoption numbers on a dashboard visible to all consuming teams. The dashboard shows: adoption rate (percentage of new surfaces using system components, trend line over the last 6 releases), pull ratio (consumer requests fulfilled per system initiative, trend line), and the top-5 most-requested components not yet built. Transparency converts the metrics from a management report into a team tool that every consumer can use to prioritize their own migration.

The dashboard is updated monthly by the governance coordinator and is the first item on the monthly demo agenda. A consumer team that sees their requested component climbing toward the top of the most-requested list knows the system team is processing their intake, even if the component has not shipped yet. A consumer team that sees adoption trending down knows to ask why and expects an honest answer in the demo.

## 09 — Tools & Integrations

Design systems survive when their outputs connect to the tools that consume them. The following tool types integrate with different system outputs.

### Token transformers

The token file is authored in one validated JSON format. To consume it as CSS custom properties, JS module, Tailwind config, Android Compose constants, or Swift constants, use a transformer:

- **Style Dictionary** (Amazon): reads JSON token files following its format, transforms to CSS, SCSS, JS, iOS, and Android. Works with any schema-compliant file. The system exports a Style Dictionary config that maps token categories to output formats.
- **Token transformer plugins** via Figma: exports Figma variable definitions to the system's JSON token format. Import path is system schema → Figma variables → design.

The system's contribution is the format specification and schema — the transformer is a thin plugin layer. Do not couple the system to a single transformer. If Style Dictionary becomes unavailable, the token file is still readable and convertible using another tool.

### Component inspection and documentation

- **Storybook** — standard environment for component development: rendering examples, a11y addons (axe-core storybook addon, accessibility panel), interactive variant controls via controls addon, theme switching via global decorator. Storybook stories should derive from the component doc's examples — one story per variant axis, one composite story showing all states. The Storybook configuration must include: (1) a theme decorator that wraps every story in each theme and renders a theme-name label, (2) an a11y addon that runs axe-core checks on every story render, and (3) a docs addon that renders the component doc alongside the component preview. Do not use Storybook as the source of truth for component behavior — the doc is the source; Storybook is the visual test harness.
- **Vite / TypeScript** — component builds. Token resolution should be runtime: the CSS variable is set at the application level via a theme class or attribute (`data-theme="dark"` on `<html>`), and the component uses `var(--token-name)` in its styles. Avoid compile-time token resolution for CSS — runtime variables are the only way to switch themes without recompiling and the only way to support user-preference media queries like `prefers-color-scheme`. The component must never import a token value directly; it imports a token module that resolves the CSS variable name to the runtime value. This separation of concerns means tokens can change without rebuilding components.

### Design integration

- **Figma** — the system's schema and Figma variable definitions should use the same data format. The validated token file is the source of truth; export to Figma's token plugin format using a CI step that runs `npx token-transformer tokens.json figma-tokens.json` on every merged PR. When Figma design updates with new token values, re-import into the codebase by parsing the Figma token export and validating it against the schema — never accept unvalidated Figma values directly. The re-import process must: (1) read the Figma token file, (2) validate every value against the schema, (3) compute a diff against the current token file, and (4) output a PR with the diff for human review.
- **Design-to-code handoff** — component doc examples serve as the reference for visual appearance. Designers check rendered component pages on the system's documentation site, not CSS files, to confirm implementation matches intent. The documentation site renders the same Storybook stories that the visual regression uses, ensuring parity between what engineers see in the test harness and what designers approve. Screenshots from the visual regression layer (Layer 3) serve as the handoff artifact — when a visual regression passes, the component matches the design.

### CI/CD pipeline

The full CI pipeline for a design system package runs on every PR and every merge to `main`. It is the enforcement layer for every rule in this skill — if a rule cannot be checked by CI, it will be violated:

1. **Lint** — schema validation against the token file: naming rules (using a regex check from `references/design-tokens.md`), no dangling tokens (every primitive consumed by at least one semantic, every semantic consumed by at least one component), no duplicate definitions, all primitives reachable from at least one theme. A failing lint produces a plain-text report with the exact line number and the rule violated.
2. **Test** — a11y tests via axe-core on every component variant rendered in every theme, visual diff against stored baselines (Layer 3), contrast sweep (Layer 2) against the YAML pair file, component unit tests that verify each variant produces the expected DOM structure, and keyboard navigation tests that Tab through each component and verify that every interactive stop receives focus and every expected key activates the correct behavior.
3. **Build** — compile tokens to CSS, JS, and platform output formats using the transformer of choice. The build output must be deterministic — running the same token file through the same transformer on different machines must produce identical output. Run the build twice and compare checksums to verify.
4. **Validate** — build components from the compiled output tokens to confirm no compile-time drift. If the build output changes between the source-token build and the compiled-token build, the transformer has a bug or the token schema does not match the transformer input. Either way, the pipeline fails.

The pipeline answers three questions: Do the tokens parse? Do the components build? Does the composition work across all themes? A pipeline that passes all four stages produces a release artifact that can be published directly. A pipeline failure at any stage blocks the release until the issue is resolved and re-verified.

### Version management

Tag each release with a git tag `v<MAJOR>.<MINOR>.<PATCH>`. Publish via npm or equivalent. Each release ships: the package itself (compiled tokens, components, and documentation), a changelog (a Markdown file in the repository root listing every change since the last release, organized by MAJOR/MINOR/PATCH with change-record links), a migration guide (if any behavior changed — what changed, why, how to update, and which version the migration was introduced in), and the diff of the token file against the previous release — a token-level visualization that shows exactly which values changed without reading the changelog.

The governance body determines the version label — not the CI pipeline. CI runs the tests and confirms they pass; the governance body decides whether the sum of changes is MAJOR, MINOR, or PATCH. A change that looks like a PATCH (a color value fix) might be MAJOR if it changes the system's brand appearance in a way that ripples through a consumer's marketing materials. The governance body weighs that impact. The decision is documented in the changelog and in the governance meeting minutes.

## 10 — Integration with Development Process

### System-package relationship

- The system package is a peer dependency in the product's project, not a direct dependency. This prevents version conflicts when multiple products consume different system versions.
- The product never imports tokens directly from the style layer — it imports the system package. This abstraction prevents lock-in to a specific rendering layer (CSS vs CSS-in-JS vs design tool).
- The system package exports: one CSS file (`system/tokens.css`) containing all token values for all themes, one component module per component, and a `components.js` re-export file for convenience imports.

### Intake process

When a product team needs a component or token, the intake process is the interface between the system and its consumers. A frictionless intake process determines whether consumers wait for the system or build their own workaround:

1. Product team posts a request in the system channel with the use case, the two surfaces the token or component would serve, and the business impact of not having it. Requests without a use case are returned immediately — this prevents the system team from spending time on hypotheticals.
2. System team estimates effort within 48 hours: 0–2 hours (doc fix, existing token reconfiguration, or token already exists and just needs discovery), 2–8 hours (new variant of an existing component — new size, new intent, new state), 1–5 days (new component within the shortlist — documented, prototyped, tested), or >5 days (new component that displaces other work or is outside the current shortlist — needs governance body approval for reprioritization).
3. System team either fulfills within existing capacity or routes to the next release's planning. The pull ratio determines which requests take priority — if the system team has shipped three self-initiated features for every consumer-requested feature in the last two releases, the pull ratio is 0.33, and the next three requests are fulfilled before any new self-initiated work begins.
4. The requester receives weekly status updates on their request — "in review," "in implementation," "blocked on X," "scheduled for release v1.4." A request that receives two consecutive weekly updates with no status change triggers a escalation. The system lead reviews the blockage and decides whether to reprioritize or close the request.

During the pull phase, the system team ships 2–3 components per release. Requests that accumulate beyond a two-release window are escalated in the monthly demo. If a request has been waiting longer than four weeks, the requester is invited to the demo to present their use case directly to the governance body.

### Deprecation notification process

When a token or component enters deprecation, the notification process follows a defined sequence:

1. **Announcement in the governance meeting.** The deprecation is discussed and approved by the governance body. The change record is drafted with the deprecation version, the removal version, and the migration path.
2. **Build warning.** The system package emits a console warning when a deprecated item is imported. The warning includes: the deprecated item name, the deprecation version, the planned removal version, and the recommended replacement. The warning is logged in development and testing environments only — never in production.
3. **Deprecation file.** A file named `DEPRECATIONS-<version>.md` is created in the system repository root. It lists every deprecated item in this release with its deprecation version, removal version, replacement, and a code example showing the migration.
4. **Consumer notification.** The deprecation is announced in the system channel, in the monthly demo, and in the release notes. The announcement links to the deprecation file.
5. **Removal.** After the deprecation window expires (two MINOR releases or one MAJOR), the deprecated item is removed. The removal is documented in the changelog with the same migration path from the deprecation file.

The deprecation notification process is the consumer's earliest warning that a change is coming. Skipping any step in the sequence erodes trust — if a consumer discovers that a component they depend on was removed without notice, they will stop adopting new system versions.

### Handoff checklist

At the end of each MINOR release, the system team runs through a verification checklist. A release that fails any item is not published until the gap is resolved:

- [ ] Token files committed to `main` and validated against `schemas/design-tokens.schema.json`. The validation output is included in the release branch's artifact.
- [ ] Component docs committed to the documentation site and current for every component in this release. The "last reviewed" date in each doc's frontmatter matches or postdates the release date.
- [ ] Changelog written in the `changelog/` directory. The changelog lists every change since the last release, organized by MAJOR, MINOR, PATCH, each with a link to the change record. If a change record is missing, the changelog entry for that change is incomplete and the release is blocked.
- [ ] Migration guide written for any changed tokens. The guide names: the old token/value, the new token/value, which version the change was introduced, which version the old token will be removed, and a before/after code example showing the migration.
- [ ] All themes verified — build passes, visual regression tests (Layer 3) pass for every component in every theme, contrast sweep (Layer 2) passes for every rendered pair in every theme, and the theme registry validates that every semantic token resolves to a defined value in every theme without implicit inheritance.
- [ ] Release notes sent to the consumer channel. The notes are 5-10 bullet points: what shipped, what changed, what is deprecated, what the team needs to know about the upgrade. Consumer teams must acknowledge receipt within two business days.
- [ ] Each new component assigned an owner — a role (primary engineer, primary designer), not a person who might leave the team. The owner is responsible for doc freshness, bug reports, and deprecation decisions for that component.

The handoff checklist is the last gate before a release reaches consumers. It cannot be skipped for any reason — not for pressure, not for a deadline. A release that ships without passing the handoff checklist will be reverted.

### Roles and responsibilities

A functioning design system team has defined roles even when individuals wear multiple hats. On a two-person team, one person may be the token steward and component engineer while the other is the documentation lead and accessibility champion — but each role's responsibilities are explicit:

- **Token steward** — owns the token file, schema validity, theme registration, and token governance. Approves every new token proposal. The token steward is the single person who can say "this belongs at the component layer, not the semantic layer" and be heard. This role must include at least one person with a design background who can evaluate whether a proposed token color encodes the intended meaning across all themes.
- **Component engineer** — implements components, owns component CSS, tests, and token resolution patterns. Reviews every component PR for hard-coded values and missing state styles. The component engineer runs the visual regression suite and approves baseline changes.
- **Documentation lead** — writes and reviews component docs using `templates/component-doc-template.md`. Owns the Do/Don't pairs, the a11y notes, and the examples. Reviews every component PR from a documentation-consumer perspective: can a new engineer who has never seen the component use it from the doc alone?
- **Accessibility champion** — reviews every component for ARIA patterns, keyboard contracts, color contrast, and screen-reader announcements. Runs the manual a11y audit before each MAJOR release. The a11y champion must be part of the governance body and can block a release on a11y grounds alone.
- **Governance coordinator** — schedules governance meetings, publishes the agenda and minutes, tracks the change backlog, and manages the release workflow. This is often a rotating role that gives consuming team members exposure to the governance process.
- **Consumer liaison** — the rotating member from a consuming team during Phase 2. Responsible for bringing production pressure into the system and taking system discipline back to their team. The liaison's term is one release cycle (two weeks).

Each role has a backup person assigned at all times. Role vacancies (someone leaves the team) trigger a succession notification within the governance body. A role unfilled for more than two weeks is escalated to the system lead, who may pause non-critical work until the role is filled.

### Meeting cadence and artifacts

- **Weekly sync (30 min):** System team + rotating consumer liaison. Review in-progress work, blockers, and the next release scope. Artifact: a one-paragraph update posted to the consumer channel within one hour of the meeting end.
- **Bi-weekly governance (1 hour):** Governance body. Approve/reject change records, review adoption metrics, decide release readiness. Artifact: published minutes within 24 hours. Minutes include: items discussed, decisions made, rationale for each decision, and action items with owners.
- **Monthly demo (45 min):** Open to all consuming teams. Show the latest components, announce deprecations, share adoption metrics. Artifact: recording and slide deck posted to the system documentation site.
- **Quarterly review (2 hours):** Governance body + one representative per consuming team. Review the roadmap for the next quarter, adoption and quality metrics from the past quarter, and any governance process changes. Artifact: published roadmap document with committed items and stretch goals.

## 11 — Additional Anti-Patterns

Beyond the per-reference anti-patterns and the failure modes below, watch for these systemic anti-patterns driven by team dynamics rather than technical missteps.

### The "library" mindset

**Pattern:** The system team treats every component in the codebase as a candidate for the system registry, adding it regardless of usage frequency, divorce from the inventory.

**Why it fails:** The system grows to 200+ components, documentation falls behind, and no consumer knows what is available or how any two components relate. The system becomes a junkyard.

**Corrective:** Measure "documentation completeness per component." Do not add a component that is not fully documented. Prune any component without production usage in three releases.

### The "kitchen sink" token set

**Pattern:** Every designer asks for a custom shade, and the token set accumulates 300+ primitive steps because nobody says no.

**Why it fails:** 300+ tokens are never audited, the file becomes heavy, and theme derivation is impossible because every value encodes a specific design decision. Contrast checking takes hours.

**Corrective:** Apply the two-surface rule to primitives too. If a color step is not consumed by at least two semantic tokens, drop it. Trim quarterly at the governance review.

### The "premature stabilization" component

**Pattern:** The system team ships a component as "stable" with a note that "the API may change in the next major version."

**Why it fails:** Consumers adopt the stable tag, rely on the v1 API, and the removal becomes a forced migration costing as much as building the system from scratch.

**Corrective:** Ships as `experimental` with a clear tag in docs and import path. Experimental components are not semantically versioned. Stable is for components that have passed three releases without an API change.

### The "token as escape hatch" anti-pattern

**Pattern:** Every component override is exposed as a named token in the token file, so anyone can change any part of any component from the token layer.

**Why it fails:** The token file now contains component-specific overrides that behave like semantic tokens. The token count balloons, and the boundary between the system and the component is erased.

**Corrective:** Component overrides live in the component's implementation, not in the token file. The token file holds only primitives and semantic tokens. A component consumes semantic tokens and applies local overrides — those overrides are not system tokens.

### The "design-by-fiat" token architecture

**Pattern:** The system team designs the entire token set without consulting any consuming team, then presents it as a done deal.

**Why it fails:** The tokens do not match real component usage. Consuming teams spend more time writing overrides than they save from the system. They bypass the system within a month.

**Corrective:** Include at least one consuming team member in token design (Step 3). Let them propose the first five tokens. The system team generalizes and validates — it does not invent in isolation.

### The "version devaluation" anti-pattern

**Pattern:** Every change, including typo fixes and deprecation removals, triggers a MAJOR version bump. The MAJOR number climbs to 37, and consumers stop updating.

**Why it fails:** Version numbers lose semantic meaning. Consumers cannot tell which updates are safe and which require migration. They pin to old versions.

**Corrective:** Reserve MAJOR for actual breaking changes. If the version climbs too fast, revisit the governance definition of "breaking" — token value changes that do not change the visual appearance are PATCH, not MAJOR.

## 12 — Failure Modes and Recovery

### Failure 1: The component backlog

**Early signal:** Team accepts every request from consuming teams, backlog exceeds 30 items, nothing ships for two consecutive releases.

**Corrective move:** Close all open requests. Pause intake for one release cycle. Reopen requiring two documented consumption surfaces and a business-impact statement. Process FIFO with a two-week response deadline.

**Prevention:** Set a maximum backlog size (recommended: 12 items). When hit, no new intake until two items ship. Review and close stale items weekly — anything untouched for two months is dropped without notification.

### Failure 2: Token sprawl

**Early signal:** Semantic token count exceeds primitives. Proposals arrive for single-use cases. Quarterly audit shows 30% growth while product surface grew 10%.

**Corrective move:** Freeze all token proposals for one release. Audit every token for production usage. Deprecate unused tokens with a two-release notice. Publish a token count graph.

**Prevention:** Enforce the two-surface rule. Run quarterly token count vs surface count. A ratio above 0.3 is a warning; above 0.5 is a freeze.

### Failure 3: Docs nobody reads

**Early signal:** Same question asked three times in one week in the consumer channel — and the answer is in the doc.

**Corrective move:** Flag all out-of-date docs (check the "last reviewed" date). Rewrite the top-three most-asked-about components, focusing on the questions being asked. Publish a doc changelog to make updates visible.

**Prevention:** Doc review is required before component ships to stable. Rotate reviewers across teams to catch blind spots.

### Failure 4: Dark theme fails contrast

**Early signal:** Dark theme added late. Consumer reports blue text on dark background is illegible. Contrast sweep was never run.

**Corrective move:** Run contrast sweep immediately against all rendered pairs. Adjust dark primitives or add dark semantic overrides. Ship as MAJOR fix (it changes visual appearance).

**Prevention:** Build both themes from day one. CI checks contrast on every commit.

### Failure 5: Governance bypass

**Early signal:** A consuming team duplicates a system component outside governance, arguing the system "does not quite fit."

**Corrective move:** Do not force removal of the duplicate. Audit why the system did not fit — specific feature gap, performance issue, or documentation mismatch. If valid, add variant or fix. Publish the finding.

**Prevention:** Make governance low-friction. Track bypass rate as a metric. Rising rate means the process or the component is wrong.

### Failure 6: First-adopter surface never ships

**Early signal:** Foundation phase extends past week 8. The team keeps building "just one more" component.

**Corrective move:** Stop building. Ship whatever exists — even if only tokens and two components. Migrate one small surface (not the main one, any surface). Publish metrics even if modest.

**Prevention:** Hard deadline at week 6. Everything else is lower priority than the first ship.

### Failure 7: Pull ratio below 1:1

**Early signal:** The system team ships features nobody asked for. Consumer teams respond with silence or complaints.

**Corrective move:** Stop all system-initiated work for two releases. Fulfill consumer requests exclusively.

**Prevention:** Track pull ratio from the pull phase month one. Below 1.5 for two consecutive releases triggers a pause and consumer survey.

### Failure 8: Schema drift

**Early signal:** A token passes schema validation but produces unexpected output values. The schema and token file have been updated independently on different branches.

**Corrective move:** Validate schema against token output. Fix mismatches. Add CI validation that runs both directions: tokens validate against schema AND schema validates against published token files.

**Prevention:** CI validation from day one, before the first proposal. PR blocked on failure.

### Failure 9: The big-bang migration

**Early signal:** A team decides to "adopt the design system by rewriting the entire product in a month."

**Corrective move:** Roll back. Revert to pre-migration state. Migrate surface by surface following the adoption plan — never more than one surface per week.

**Prevention:** Use the three-phase model from `references/adoption-strategies.md`. Never plan a migration that spans more than one surface at a time.

### Failure 10: Tool lock-in

**Early signal:** The token file can only be read by one proprietary tool. If the tool breaks, the tokens cannot be extracted.

**Corrective move:** Convert the token file to a plain JSON format matching the system schema. Rebuild the pipeline from that format, treating the old tool as an optional output.

**Prevention:** Keep the token file in a plain, version-agnostic format (JSON + schema). Export to tool-specific formats from that source — never the reverse.

### Failure 11: The abandoned changelog

**Early signal:** Release v1.4 has no changelog entry. Release v1.5 describes a change that was actually shipped in v1.4. Consumers cannot tell what changed.

**Corrective move:** Reconstruct the changelog from git history. Publish the corrected version. Add CI check that a release branch without a corresponding changelog entry cannot be merged.

**Prevention:** Do not merge a release without a changelog entry. CI blocks merges to `main` or `release/` without a corresponding changelog file.

### Failure 12: Rotating teams, static docs

**Early signal:** New team members join the system team. The docs they are supposed to maintain are assigned to people who left six months ago.

**Corrective move:** Audit every component doc for last-reviewed date and assigned owner (role). Reassign unowned docs. Flag docs with last-reviewed older than two releases.

**Prevention:** Assign owners by role, not by person. At every governance meeting, review the doc ownership map.

## 13 — Supporting Files Index

| File | Role | When to Read / Use |
|---|---|---|
| `references/design-tokens.md` | Token architecture: tiers, naming, scales, theming hooks, anti-patterns | Designing or extending the token set (Step 3) |
| `references/component-inventory.md` | Audit methodology: surface enumeration, tally, grouping, prioritization | Running the initial audit (Step 1, Step 2) |
| `references/pattern-documentation.md` | Component doc writing guide: anatomy, variants, states, Do/Don't, a11y | Writing or reviewing component docs (Step 4) |
| `references/theming-architecture.md` | Theme layers: brand vs mode variants, contrast enforcement, registry | Designing themes (Step 6) |
| `references/accessibility-standards.md` | WCAG mapping, ARIA patterns, focus indicators, keyboard contracts | Applying a11y requirements (Step 5) |
| `references/versioning-and-governance.md` | Versioning scheme, change review, deprecation policy, governance body | Establishing change management (Step 7) |
| `references/adoption-strategies.md` | Three-phase adoption model, migration strategy, buy-in tactics, comms | Planning adoption (Step 8) |
| `references/system-case-studies.md` | Two verified case studies and five transferable patterns | Citing evidence for adoption (Step 9) |
| `templates/token-spec-template.md` | Fill-in skeleton for token proposals with guidance per section | Proposing a new token (Step 3) |
| `templates/component-doc-template.md` | Fill-in skeleton for component docs with guidance per section | Writing a new component doc (Step 4) |
| `schemas/design-tokens.schema.json` | Draft 2020-12 JSON Schema for validating token spec documents | Token validation; CI integration (Step 3, Layer 1) |
| `examples/worked-design-system.md` | Complete TaskFlow worked example with intermediate artifacts for every step | Teaching material; companion to Section 06 |

### About the reference files

Each reference file is designed to be read in the context of the workflow step that calls for it. The references are not meant to be read cover-to-cover — they are depth layers that the workflow steps pull from when the step's duration or complexity warrants a deeper investigation. When you encounter a "Governing reference" callout in a workflow step, that is the moment to open the reference file and read it through.

### Reading paths

**For a first-time reader building their first system:** Start with `references/component-inventory.md` (audit) → `references/design-tokens.md` (tokens) → `references/pattern-documentation.md` (docs) → `examples/worked-design-system.md` (full narrative). This follows the workflow sequence from Step 1 through Step 6. Read the worked example all the way through once before starting your own audit — seeing the full arc before starting prevents the common mistake of over-scoping the first token set.

**For an experienced practitioner joining mid-cycle:** Start with `references/versioning-and-governance.md` (process) → `references/theming-architecture.md` (architecture) → `templates/component-doc-template.md` (standard format). Then pick up the current phase from Section 04. The workflow steps in Section 04 contain the checkpoint questions that reveal whether the phase you are joining is on track — read the current phase's checkpoint first, then the phase's artifacts.

**For an adoption skeptic:** Start with `references/system-case-studies.md` (evidence that it works with concrete numbers) → `references/adoption-strategies.md` (metrics and timeline) → the TaskFlow metrics in `examples/worked-design-system.md` (measurable proof).

**For the team setting up CI:** Start with `schemas/design-tokens.schema.json` → `references/versioning-and-governance.md` (release process) → Section 08 of this skill (QA layers) to configure the full testing pipeline. Run the schema validator against the token file first — everything else depends on tokens being parseable.

**For scaling to multiple brands and platforms:** Start with `references/theming-architecture.md` (theming layer model) → `references/design-tokens.md` (brand token structure) → `references/versioning-and-governance.md` (cross-brand governance). Then move to Section 06 of this skill (the TaskFlow worked example shows how brands scale in practice) before planning your first multi-brand theme registry.

**For a post-launch retrospective:** Read all 12 Failure Modes in Section 12 and check which signals your system is showing. Then read the anti-patterns in Section 11 and Section 02. The most common post-launch failure is Failure 2 (token sprawl) and Failure 5 (governance bypass) — if you see either signal, the corrective moves are in Section 12.

**For a new team member onboarding to an existing system:** Start with `examples/worked-design-system.md` (the full narrative) → Section 04 (workflow steps) → the component doc for the component you are assigned to. The worked example gives you the conceptual model; the workflow steps give you the process; the component doc gives you your task.

**For an audit of an existing system:** Start with Section 08 (QA layers) to find what is actually tested → `references/accessibility-standards.md` (the checklist to run) → `references/versioning-and-governance.md` (whether changes are governed at all). An audit that starts with the token file finds the drift; an audit that starts with the QA layers finds the causes.