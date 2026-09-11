# Theming Architecture: Layers, Variants, and Enforcement

A design system that supports one brand on one platform is a pattern library. A system that supports multiple brands, light and dark modes, or platform-specific rendering is a theming architecture — and that architecture must be designed, not discovered, because retrofitting theme support into a flat token set costs roughly as much as building the system in the first place.

## The three layers

Every theme resolves through three layers, evaluated at render time.

**Layer 1 — Token resolution.** Semantic tokens are resolved against the active theme's primitive palette. This is a pure lookup: `color-bg-page` maps to `blue-50` in the light theme and to `gray-900` in the dark theme. No logic, no cascade. Every semantic token has a value in every theme, stored in a flat key-value map. A missing key is a bug caught at build time.

**Layer 2 — Component overrides.** A component may declare theme-specific overrides for a minority of its tokens. Overrides live inside the component's definition and use a `themes` key that maps theme name to token overrides. The rule: if more than 30% of a component's tokens need overrides per theme, the token architecture is wrong — push those values up into the semantic tier where they belong.

**Layer 3 — Platform adaptation.** Platform-specific values (hover styles on web vs. touch feedback on mobile, system font stacks per OS) are not theme overrides. They live in platform adapter files that map a canonical component interface to each platform's native rendering. Theme crosses it, but platform adapters are outside the theme layer entirely.

## Brand variants vs. mode variants

Two kinds of theme exist, and treating them the same way is an architectural error.

**Brand themes** (Product A, Product B, White Label) differ in personality — colors, fonts, corner radii. They are best expressed by swapping the primitive palette entirely: a different `blue-500` per brand. Brand themes are authored in full by the system team and versioned like code.

**Mode themes** (light, dark, high-contrast) differ in luminance and accessibility but not personality. They are best expressed as value overrides on the *same* primitive palette, authored by the accessibility team and governed by contrast rules. Dark mode must not change the system's type scale or spacing — if it does, the theme is leaking brand differentiation into a mode that should only adapt luminance.

## The theme registry

Every theme lives in a registry — a single file that lists every theme name, its type (brand/mode), its token file, and which other theme it extends. A minimal registry:

```yaml
themes:
  light:
    type: mode
    extends: null
    tokens: themes/light/tokens.json
  dark:
    type: mode
    extends: light
    tokens: themes/dark/tokens.json
  brand-acme:
    type: brand
    extends: light
    tokens: themes/brand-acme/tokens.json
```

Inheritance: a theme that extends another inherits all its tokens and may override any subset. An override must name the primitive it resolves to, not another semantic token — chain references make diffing themes impossible. The registry is validated at build time: every theme must have a value for every semantic token in the system schema, either defined or inherited.

## Contrast enforcement

Every theme, before it ships, must pass a contrast audit. Write a script that enumerates all text-on-background token pairs the system actually renders (not every possible combination) and checks WCAG 2.1 AA ratios (4.5:1 for normal text, 3:1 for large text). Fail the build on any violation. CC exceptions exist for decorative elements only, and must be approved in writing with an alternative accessible experience documented.

Three patterns for achieving dark-theme contrast that do not degrade readability:

1. **Invert the luminance ladder.** `gray-900` (near-black) in the light theme becomes `gray-100` (near-white) in the dark theme. The text-primary-background contrast ratio stays the same because both sides flipped on the same axis.
2. **Elevate surfaces for depth, not difference.** Dark theme surfaces are distinguished with subtle luminance deltas (8-12% steps) rather than the blue or gray tint many systems use. Tinted dark themes make color-critical UI (status badges, charts) hard to read by shifting the perceptual reference.
3. **Reduce saturation on large surfaces.** Dark theme backgrounds should be desaturated by 60-80% relative to their light counterpart. A fully saturated dark blue background is fatiguing at screen scale even at AA contrast.

## Theme testing

Four tests every theme must pass:

1. **Contrast sweep.** Automated ratio check on every used foreground-background pair in the theme — not every token pair, every pair actually rendered on at least one surface.
2. **Surface mapping.** Every component renders correctly with the theme applied. Automated screenshot diff across themes for a canonical set of component states.
3. **Color meaning preservation.** Red means error in all themes; green means success. A theme that maps success-green to a tone that reads as warning fails meaning preservation, even if contrast passes.
4. **Extensibility check.** A new brand theme can be written by overriding no more than 40% of primitive values. If the override ratio is higher, the token scale lacks neutral ground — too many primitives encode brand-specific meaning before the semantic layer has a chance.

## Anti-patterns

- **The cascade drift.** Tokens that pass through three or more intermediate variables before reaching a component (color-bg-primary → color-surface-raised → card-bg → card-surface). Each indirection adds a theming surface nobody can track. Collapse to two hops: semantic → primitive.
- **Theme as component prop.** A `theme` prop on every component that switches between hard-coded value sets. This duplicates the token layer, skips the registry, and makes each component own a theming edge case. The theme is resolved once, above the component tree; components never inspect which theme is active.
- **Dark mode as afterthought.** The dark theme has 60% of the tokens the light theme does, and missing tokens silently inherit values that produce invisible text on dark backgrounds. Ship both themes simultaneously from the start — a theme that launches six months late is a theme nobody trusts.
- **Brand-specific tokens in the common set.** A brand theme that needs new semantic tokens to express its identity is overridden — brand-specific tokens pollute the shared schema. If the brand needs `color-accent-brand-x`, it belongs in the brand theme's override file, not the system schema.