# Design Tokens: Tiers, Naming, and Scales

A design token is a named decision: this is the blue, this is the space between a label and its input. Tokens exist so that a thousand files stop hard-coding values. The craft is not inventing names — it is deciding how many tokens you need (fewer than you think), which layer each one lives at, and what happens when a value must change.

## The three tiers

Tokens come in three tiers, and the tier determines who may change a value and why.

**Tier 1 — Primitive (also called global or core).** Raw values with no opinion attached. `blue-600: #2563eb`, `space-4: 16px`, `font-weight-bold: 700`. Primitives are a complete palette: every step of every scale, including steps nothing currently uses. They are the paint store, not the painting.

**Tier 2 — Semantic (also called alias or system).** Named for their *job*, not their value. `color-bg-page`, `color-text-primary`, `color-border-input`, `space-inset-md`, `radius-input`. A semantic token references a primitive: `color-bg-page: {blue-50}`. This indirection is the whole point — to retheme, you repoint semantics at different primitives and nothing else changes.

**Tier 3 — Component.** Named for a specific component's part. `button-bg-primary`, `dialog-overlay-opacity`, `toast-border-width`. Use component tokens sparingly — they exist when a component genuinely diverges from the semantic layer (a destructive button, an overlay that must be translucent). If a component token just repeats a semantic token's value, delete it and use the semantic one.

The flow of reference is strictly downward: component → semantic → primitive. A primitive must never reference a semantic; a semantic must never reference a component. Cycles and upward references make theming impossible.

## Naming rules that survive contact with a real codebase

1. **Name semantic tokens by role, never by value.** `color-text-primary` survives a rebrand; `color-text-gray-800` does not. The moment a name contains a hex value, a color word, or a number from a scale, it is a primitive wearing a semantic costume.

2. **Order from general to specific, category first.** `color-text-disabled`, `color-bg-surface-raised`, `space-stack-paragraph`. The category prefix (`color`, `space`, `radius`, `shadow`, `font`) lets tools group and validate; the modifiers read as a path from broad to narrow.

3. **Use a closed vocabulary of modifiers.** Decide once what `primary / secondary / tertiary`, `default / hover / active / focus / disabled`, and `raised / flat / sunken` mean, then reuse those words everywhere. Every ad-hoc synonym (`active` vs `current`, `main` vs `primary`) is future ambiguity.

4. **Beware state in names.** `color-button-hover` bakes one interaction model into the token layer. If hover styling might later come from an overlay or a theme, prefer a component token *inside* the button implementation that maps `:hover` to a semantic token. Stateful names are acceptable for component tokens; avoid them in the semantic tier.

## Building the scales

**Color:** define one hue ramp of 9-11 steps per hue (50 through 900 plus a near-black), constructed so that adjacent steps have usable contrast relationships. Then define the neutrals ramp the same way. Derive tints and shades with a perceptual model (adjusting lightness in a uniform space such as OKLCH) rather than naive RGB math, which produces muddy mid-tones. You will use three or four steps per hue in practice; the full ramp exists so light/dark themes and states have somewhere to go.

**Spacing:** one base unit (4px is conventional; 8px is stricter) and a geometric or arithmetic progression: 4, 8, 12, 16, 24, 32, 48, 64. Cap the scale. A 19-step spacing scale is a failure to say no. Every layout gap, padding, and margin must resolve to a scale step; if a designer demands 18px, the answer is "pick 16 or 20," not "add 18."

**Typography:** define a type scale (ratio 1.2-1.25 for product UI, 1.333 for editorial) with named sizes (`font-size-sm` through `font-size-3xl`), a line-height rule per size (small text needs proportionally more leading), and 2-3 font-weight slots per family. Pair every size with its intended use in the docs — "the size for form labels" beats "16px" as documentation.

**Radius, shadows, motion:** small closed sets. Radius: 3-4 steps plus `full` for pills and circles. Shadows: 3 elevation levels plus an overlay/none. Motion durations: fast (100-150ms), base (200-300ms), slow (400-600ms) with one standard easing curve. These sets rarely grow; do not pre-inflate them.

## The token file's job

The token file is a contract, so it needs a schema (see `schemas/design-tokens.schema.json` in this skill). A schema buys you three things: linting catches `color-` tokens with numeric values before they ship; tooling can generate CSS variables, Swift, and Kotlin from one source; and diffs between versions become reviewable. Keep primitives and semantics in one file or two clearly separated files — separation by tier, not by team.

## Theming hooks

Every semantic token is a theme slot whether you intend it or not. Design them so a dark theme is a value swap: for each semantic token, know its dark-mode counterpart at the moment you name it. If a semantic token has no sensible dark value ("this gradient only works on white"), the token is really a component token — move it down a tier and let the component own the exception. Full theming architecture, including brand variants and contrast enforcement, is covered in `theming-architecture.md`.

## Extracting tokens from an existing UI

No team writes a token file on a blank page; the tokens already exist, uncounted and unnamed, in stylesheets and mockups. Extraction beats invention because the product's real needs are visible in what people already wrote:

1. **Harvest, then sort.** Sweep every stylesheet and design file for literal color, spacing, radius, and font values. Deduplicate with a tolerance (grays within a few percent of each other collapse to one). The raw count is usually 3-10x what the final set will be.
2. **Cluster before naming.** Group values by role — page backgrounds, borders, text, focus rings. A cluster that spans many distinct values is the strongest candidate for a semantic token, because it proves the job exists.
3. **Name the survivors by job.** Only after clustering. Names derived from values before clustering become obsolete at the first rebrand.
4. **Set a convergence budget.** If the harvest found 34 grays, decide now how many survive (6-9 in the neutral ramp). Values that miss the budget migrate to their nearest survivor, never "temporarily" kept.
5. **Ship with a deprecation shim.** Old names map to new tokens through generated aliases that log a warning, so product code can migrate gradually while grep-ability improves with every merged PR.

## The token audit checklist

Run before a major release, and quarterly regardless. Each "no" is a work item:

1. Every color used in product markup resolves to a token — grep for hex literals outside the token file; each hit is a leak.
2. Every semantic token's value matches its name (a `color-text-disabled` lighter than `color-text-secondary` needs a rename or a value change).
3. The semantic tier is smaller than the primitive tier, and no token references a token in a higher tier.
4. Every semantic token has a dark-theme counterpart value recorded, even if the theme ships later.
5. Contrast pairs are documented for every text/background combination actually used together.
6. The ten least-referenced tokens of the last quarter are listed for removal review.
7. The token file validates against `schemas/design-tokens.schema.json` in this skill, and the diff between the last two versions contains no unexplained value changes.

## Anti-patterns

- **The mirror tier.** A semantic layer that is a 1:1 rename of primitives (`color-blue-600-semantic`). Indirection with no change of meaning is cost without benefit; the semantic layer should be much smaller than the primitive layer.
- **One-off escape values.** `padding: 13px` in a stylesheet because the scale "didn't quite fit." Each escape is a leak; log it, fix the scale or the layout, and move on. Three escapes at the same value means the scale is missing a step.
- **Token sprawl by committee.** Anyone can propose a token, so everyone does. Gate new tokens behind the governance process in `versioning-and-governance.md`: state the use case, show the two places it will be used, or it does not enter the file.
