# Worked Design System: TaskFlow

## Scenario

**TaskFlow** is a small web application for personal task management — lists,
due dates, priorities, tags, and a calendar view. Two-person team (one
designer, one engineer), building the MVP over 12 weeks. At week three they
realize three components exist in four implementations each, the color palette
has drifted between screens, and the engineer spends the first hour of every
sprint reconciling visual inconsistencies. They decide to build a design
system — not a comprehensive one, just enough to keep the product coherent
through the MVP and beyond.

The full arc from audit to shipped system components is documented here.
Each step's artifact is shown with the reasoning that produced it. This file
is the companion to section 06 of SKILL.md; the workflow described there
is the one applied below.

---

## Step 1 — Audit the existing surface (Component Inventory)

The team runs a screen-by-screen audit using the method in
`references/component-inventory.md`. They enumerate every screen and dialog:

| Surface | Components |
|---|---|
| Task list | TaskCard, Checkbox, PriorityBadge, DueDateTag, SearchInput, AddButton, FilterDropdown |
| Task detail | TextInput, TextArea, Select (assignee), DatePicker, Button (save/cancel), TagChip, StatusSelect |
| Calendar view | CalendarGrid, DayCell, EventBadge, NavigationArrows |
| Settings | Toggle, TextInput, ColorPicker, RadioGroup, Button |
| Empty state | EmptyStateCard, CTAButton |
| Error state | ErrorBanner, RetryButton |

The tally sheet:

| Component | Count | Implementations | Divergence | Worst case |
|---|---|---|---|---|---|
| Button | 12 | 4 | 3 | Three button variants: one with rounded corners, one with sharp corners, one pill-shaped; two use different color systems |
| TextInput | 8 | 3 | 2 | Focus ring exists on one implementation, light gray border on another, no border at all on a third |
| Card | 6 | 3 | 3 | TaskCard sometimes clickable, sometimes not; padding varies by 12px across instances |
| Badge | 5 | 2 | 1 | PriorityBadge uses red/yellow/green; DueDateTag uses blue; colors differ from the primitives |
| Select/Dropdown | 4 | 2 | 2 | FilterDropdown has no keyboard handling; status Select on task detail does |
| Checkbox | 3 | 2 | 1 | One implementation uses native checkbox; one uses styled div with aria role |
| Toggle | 2 | 1 | 0 | Consistent |
| Dialog | 2 | 2 | 2 | One dialog is a full-screen modal; one is a small popover; both called "Dialog" |

**Divergence score summary:** Four components at divergence level 2 or higher
(Button, TextInput, Card, Dialog). These are the system's starting point.

---

## Step 2 — Build the token set

Using `references/design-tokens.md`, the team designs a three-tier token set
targeting the MVP's needs. They make three decisions before writing a single
value:

1. **One spacing scale, not per-component.** Every gap and padding resolves to
   a step on one 8-step scale: 4, 8, 12, 16, 24, 32, 48, 64. The 12px step
   exists because 8-to-16 is too large for button-to-icon gaps.
2. **Color primitives as OKLCH.** They define four hue ramps of 11 steps each
   (blue, red/error, green/success, yellow/warning), plus a neutral ramp of
   11 steps, all in OKLCH. This prevents the muddy mid-tones of RGB math and
   makes dark theme derivation mechanical — invert L, keep C and H.
3. **Semantic tokens smaller than primitives.** 36 semantic tokens versus 55
   primitive tokens. The semantic tier is deliberately smaller so engineers
   cannot accidentally use a primitive in a context that should change under
   theming.

**Primitive tokens (abbreviated):**

| Token | Value (light) | Value (dark) |
|---|---|---|
| blue-50 | oklch(0.967 0.029 255) | oklch(0.15 0.03 255) |
| blue-500 | oklch(0.52 0.19 260) | oklch(0.65 0.18 260) |
| gray-0 | oklch(1 0 0) | oklch(0.12 0 0) |
| gray-900 | oklch(0.12 0 0) | oklch(0.95 0 0) |
| space-4 | 4px | 4px |
| font-size-md | 16px | 16px |
| radius-sm | 4px | 4px |

**Semantic tokens (abbreviated):**

| Token | Resolves to (light) | Resolves to (dark) |
|---|---|---|
| color-bg-page | gray-0 | gray-900 |
| color-bg-surface | gray-50 | gray-800 |
| color-text-primary | gray-900 | gray-0 |
| color-text-secondary | gray-600 | gray-300 |
| color-border-input | gray-300 | gray-600 |
| color-focus-ring | blue-500 | blue-300 |
| color-bg-button-primary | blue-500 | blue-400 |
| space-inset-sm | space-8 | space-8 |
| radius-input | radius-sm | radius-sm |

Every semantic token has a dark-theme value declared at proposal time, not
added later.

---

## Step 3 — Component documentation: Button

Using `templates/component-doc-template.md` and the guidance from
`references/pattern-documentation.md`, the team documents their first and
most-divergent component.

**Anatomy:**

1. Container — maps visual bounds and background — prop `intent` — token `color-bg-button-primary`
2. Label — text content — prop `children` — token `color-text-on-primary`
3. Icon (optional) — leading affordance — prop `icon` — token `space-inline-icon`
4. Spinner (loading state) — replaces label — prop `loading` — token `color-spinner`

**Variants — allowed combinations:**

| | sm | md |
|---|---|---|
| primary | ✓ | ✓ |
| secondary | ✓ | ✓ |
| destructive | ✗ | ✓ |
| ghost | ✓ | ✓ |

The disallowed destructive-sm combination was a deliberate choice: destructive
actions at small size are too easy to trigger accidentally.

**States:**

| State | Visual | Trigger | Announcement |
|---|---|---|---|
| rest | filled/outlined bg | default | — |
| hover | bg darkens 10% L | pointer enters | — |
| focus-visible | color-focus-ring outline +2px | Tab / keyboard nav | — |
| active | bg darkens 20% L | pointer down / Enter | — |
| disabled | opacity 0.4, no pointer | disabled prop | aria-disabled="true" |
| loading | spinner replaces label | loading prop | aria-busy="true" |

**Do / Don't:**

1. **Do:** Use `intent="primary"` for the primary call to action on every surface.
   **Don't:** Use primary intent for two actions on the same surface — that is
   two primary calls to action, which is zero primary calls to action. Use one
   primary and the rest secondary or ghost.
2. **Do:** Use `intent="destructive"` for delete, remove, or irreversible actions.
   **Don't:** Use destructive intent for cancel or dismiss actions — cancel is
   not destructive; use secondary intent instead.
3. **Do:** Provide an `aria-label` when the button contains only an icon.
   **Don't:** Use a tooltip to communicate a icon-only button's purpose — labels
   are accessible; tooltips are pointer-access-only.

**A11y notes:** Pattern: button. Focus behavior: native `<button>` handles
focus. `aria-busy="true"` set when loading prop is true. Accessible name
source: children text, or aria-label if icon-only. Test: tab through a form
with two buttons — focus must stop on each and the button role must be
announced as "button" by NVDA.

---

## Step 4 — Component documentation: TextInput

**Anatomy:**

1. Container — wraps input and label — token `space-inset-sm`
2. Label — visible text above or beside — prop `label`
3. Control — the `<input>` element — prop `value`, `onChange`, `type`
4. Helper text — below input — prop `helperText`
5. Error text — replaces helper on validation fail — prop `error`
6. Leading/trailing affordance — optional icon slot — token `space-inline-icon`

**Variants:**

| | default | with-icon |
|---|---|---|
| sm | ✓ | ✓ |
| md | ✓ | ✓ |

**States:**

| State | Visual | Trigger | Announcement |
|---|---|---|---|
| rest | 1px color-border-input | default | label associated via for/id |
| focus | color-focus-ring outline +2px | Tab / click | — |
| hover | border darkens | pointer enters | — |
| disabled | bg gray-100, opacity 0.4 | disabled prop | aria-disabled |
| error | color-text-error border | error prop string set | aria-describedby points to error text |
| filled | value non-empty | user types | — |

**Do / Don't:**

1. **Do:** Use the `label` prop for visible labels.
   **Don't:** Use `placeholder` as the only label — placeholder disappears on
   input, fails 1.4.1 (use of color), and is inaccessible to screen readers
   in most browsers.
2. **Do:** Set the `error` prop with a user-facing message string.
   **Don't:** Change the border to red without setting `aria-describedby` to
   the error text — color-only error indication is invisible to screen reader
   users and fails WCAG 1.4.1.
3. **Do:** Use `type` appropriately (text, email, url, tel, number, password).
   **Don't:** Use `type="number"` for anything that is not an actual number
   (postal codes, phone numbers, IDs) — use `inputMode` instead for mobile
   keyboard optimization without the number-input spinbutton behavior.

**A11y notes:** Pattern: textbox. Label associated via `<label for>` or
`aria-labelledby`. Error text linked via `aria-describedby`. The input has
`aria-invalid="true"` set when error prop is a non-empty string. Focus flows
to the first invalid input when a form is submitted with errors.

---

## Step 5 — Component documentation: Card

**Anatomy:**

1. Container — bounds, bg, shadow — token `color-bg-surface`
2. Header (optional) — title, subtitle — prop `title`, `subtitle`
3. Body — content area — slot
4. Footer (optional) — action bar — slot
5. Badge (optional) — top-right indicator — prop `badge`

**Variants:**

| | default | interactive | bordered |
|---|---|---|---|
| padding-sm | ✓ | ✓ | ✓ |
| padding-md | ✓ | ✓ | ✓ |

interactive renders the container as `<button>` or `<a>` with appropriate
role, focus-visible indicator, and keyboard enter-to-activate.

**Do / Don't:**

1. **Do:** Use `interactive` when the whole card is clickable.
   **Don't:** Nest interactive elements (buttons, links) inside an interactive
   card — nested interactive elements trap keyboard users and create ambiguous
   click targets. Instead, make the card a container and place interactive
   elements inside without the interactive prop.
2. **Do:** Use bordered variant when a card sits on a surface that already has
   a background (sidebar, settings panel).
   **Don't:** Use shadow on a card that appears over another card — the shadow
   stacks and creates phantom depth. Prefer border for layered cards.

**A11y notes:** Pattern: interactive cards use `role="button"` or `<a>` with
`tabindex="0"`. Non-interactive cards are `role="region"` with
`aria-label` identifying what the card contains. Focus indicator is mandatory
on interactive variant — 3px offset outline at `color-focus-ring`.

---

## Step 6 — Theming: dark mode

Using `references/theming-architecture.md`, the team derives the dark theme
from the light theme by mechanical inversion: for every semantic color token,
luminance is inverted on the neutral ramp and hue constants shift slightly to
maintain perceptibility.

**Decisions:**

- Background surfaces flip: `color-bg-page` maps from gray-0 to gray-900.
  The luminance delta between surfaces is preserved (8-12%), so depth
  hierarchy remains legible without tinted backgrounds.
- Saturation is reduced 60% on large surfaces (page and surface backgrounds)
  to reduce eye fatigue. Blue-50 at 2.9% saturation becomes blue-80 (dark)
  at 1.2% saturation.
- Text contrast: all text tokens maintain >= 7:1 ratio against their intended
  background in dark mode. The team chooses AAA for body text as a standard,
  not an exception.

The dark theme is built and tested in parallel with the light theme — not as
a follow-up. Every semantic token that has no sensible dark counterpart
(color-primary-gradient, shadow on dark bg) is demoted to a component token,
and the component owns the exception.

---

## Step 7 — Governance setup

Before the system ships to production, the team establishes minimum governance
using `references/versioning-and-governance.md`:

**Tracks**:
- Fast track (patch): one reviewer, ships same day. For token value fixes,
  text corrections, example additions.
- Standard track (all new tokens, components, breaking changes): three
  reviewers (the system lead, a consuming-team member, and a design lead),
  three business day review window, change record required.

**Token governance**:
- New tokens require two documented consumption surfaces.
- Token value changes at the primitive tier are MAJOR version bumps.
- Deprecation: a token is deprecated for two MINOR releases before removal.

**Release cadence**: a minor release every two weeks, a major release every
quarter. The release is announced three days before ship so consumers can test
against the release candidate.

---

## Step 8 — First production surface

The team rebuilds the main task list surface — the most-visited screen — using
only system components. Measured outcomes:

| Metric | Pre-system | Post-system |
|---|---|---||---|
| Render time | 980 ms | 620 ms |
| CSS imports on page | 12 | 3 |
| Component files imported | 7 (all bespoke) | 5 (all system) |
| A11y violations (automated scan) | 14 | 0 |
| Time to add a new filter dropdown | ~4 hours | ~30 minutes (drop in existingSelect) |

The rebuild takes 4 days: 2 for token adoption and component wiring, ies for
the production surface. The team publishes these numbers as the case study
that other teams in the organization use to justify their own adoption.

---

## What these artifacts demonstrate

The TaskFlow worked example shows a full system build from a two-person team
with an aggressive timeline. The key takeaways:

- **Start with the audit.** The inventory told them which four components to
  build first, and the diverence scores prevented them from wasting time on
  components that already worked.
- **Build token before components.** The design system team designed the token
  set knowing which components it would serve (from the inventory), then
  documented components using those tokens. Components are specific instances
  of the system; tokens are the system.
- **Do not skip the dark theme.** Building both themes in parallel paid for
  its cost on the first release — no post-hoc dark-theme patch, no
  eleventh-hour contrast fixes, no engineers overriding component colors to
  make them visible.
- **Governance light.** Three rules and a two-sentence release process. Any
  system that imposes more than three procedural constraints in the first
  release is a system that will be bypassed.

The complete translation from this example to any other product is
straightforward: replace the surface nouns (TaskFlow → your product, task list
→ your core screen), replace the component names with your inventory findings,
and apply the same token architecture with your brand's colors. The structure
is the transferable part.