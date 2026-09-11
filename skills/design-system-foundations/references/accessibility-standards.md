# Accessibility Standards: WCAG Application, Pattern Registry, and Testing

A design system that does not encode accessibility into its components, tokens, and documentation does not ship accessible products — it ships the *opportunity* to build them correctly, which is not the same thing. This reference maps WCAG 2.1 AA requirements to design system deliverables so compliance is built in rather than bolted on after the contrast audit fails.

## WCAG principle mapping for design systems

Each WCAG principle maps to one or more design system artifacts. If an artifact does not exist, the principle is not enforced.

| Principle | Requirement | System artifact that enforces it |
|---|---|---|
| Perceivable 1.4.3 Contrast (minimum) | Text and images of text have 4.5:1 ratio (3:1 for large) | Token schema must require `contrast-ratio` metadata on every text-on-background token pair; build-time check |
| Operable 2.1.1 Keyboard | All functionality from a keyboard | Component doc must specify focus order, visible focus indicator, and which interactive elements are tabbable vs. arrow-navigable |
| Operable 2.4.3 Focus Order | Focus order preserves meaning | Component template includes a "focus flow" section that enumerates tab stops and their ordering relationship |
| Understandable 3.3.2 Labels or Instructions | Labels or instructions when input requires user input | Form-field component doc must document `aria-label`, `aria-labelledby`, visible label, and placeholder-as-label prohibition |
| Robust 4.1.2 Name, Role, Value | All UI components have correct name, role, value | Component schema requires role, accessible name source, and value type per interactive element |

## Required ARIA patterns per component family

Not every component needs a bespoke ARIA pattern. Most map to one of the seven ARIA authoring practices patterns below. Document the pattern name in the component doc and reference this table; do not repeat the pattern's rules in the component doc.

| Component family | ARIA pattern | Key requirement |
|---|---|---|
| Button, Link, IconButton | `button` role | Role is implicit for `<button>`; explicit role required for div/span-based buttons. `aria-pressed` for toggle buttons |
| Text Input, Select, Textarea | `textbox` / `combobox` / `listbox` | Associating `<label>` programmatically; `aria-describedby` for error messages; `aria-invalid` on validation failure |
| Dialog, Drawer | `dialog` / `alertdialog` | Focus trap on open; focus returns to trigger on close; `aria-labelledby` references the title; `aria-modal="true"` |
| Checkbox, Radio, Switch | `checkbox` / `radio` / `switch` | `aria-checked` for custom styled inputs; `aria-disabled` not `disabled` for visually disabled but focusable items |
| Tab panel | `tablist` / `tab` / `tabpanel` | `aria-selected` on active tab; `aria-controls` points to the panel; `aria-orientation` if vertical tabs |
| Navigation (nav, breadcrumb, pagination) | `navigation` landmark + `aria-label` | Distinct label per nav region on the same page ("Main", "Breadcrumb", "Pagination"); `aria-current="page"` on current item |
| Tooltip | No standard ARIA role | Use `aria-describedby` on the trigger; tooltip content is described, not named; no interactive elements inside |
| Toast, Banner | `status` / `alert` role | `role="status"` for non-critical info; `role="alert"` for time-sensitive; `aria-live="polite"` vs. `aria-live="assertive"` |

## Color and contrast in components

Every semantic color token the system defines has an associated contrast role — foreground on which background. The token schema (see `schemas/design-tokens.schema.json`) enforces that each color token declares its intended use pair. The build step validates:

- All `color-text-*` tokens against `color-bg-*` and `color-surface-*` tokens
- All `color-border-*` tokens against adjacent background tokens
- Focus indicators against their adjacent background at 3:1 minimum
- Interactive state transitions preserve contrast (hover, focus, active, disabled)

A token that fails validation cannot ship. The system provides two override mechanisms for cases where constrained surfaces (data visualization, branding headers) must operate at lower contrast: (1) the component accepts an explicit `a11y-contrast-mode` prop that switches to an AA-compliant variant, and (2) the design system governance process accepts written exceptions in `versioning-and-governance.md`.

## Focus indicators

Every interactive component must have a visible focus indicator at 3:1 contrast against its adjacent background. The indicator must be:

- At least 2px thick (CSS `outline-width` or box-shadow faux outline)
- Visible in all states (hover does not suppress focus-visible)
- Present on the interactive element itself, not on a parent — unless the parent is the interactive region (e.g., a card that is a link)
- Focus-visible applied, not focus — focus-visible shows the ring only when the user navigates by keyboard, not on click

Component templates include the focus-visible rule as an `outline` or `box-shadow` token reference, keyed to a semantic token. The default: `color-focus-ring` (which resolves to a high-contrast blue or, in dark mode, a light cyan or white).

## Keyboard interaction contracts

Document per component family the keyboard contract it accepts and provides. A contract includes:

- **Tabbable elements.** Which children of this component receive tab focus and in what order.
- **Arrow navigation.** When arrow keys navigate within the component (radio group, tab list, combobox) instead of moving focus away.
- **Dismissal.** Escape or other key closes the component (dialog, dropdown, popover). Document what happens to focus after dismissal.
- **Shortcut keys.** Reserved or configurable key combinations; document what they do and how to discover them without reading the doc.

Testing: every keyboard contract has an automated test. Link the test file in the component doc. A contract without a test is a promise the component does not keep.

## Testing protocol

Four testing layers, from cheapest to most expensive:

1. **Automated lint** — axe-core or similar run in CI on every component rendering. Catches missing roles, missing labels, insufficient contrast, and focus order violations. Fail the build on any violation.
2. **Keyboard audit** — manual traverse of every component state using Tab, Shift+Tab, arrow keys, Enter, Escape, and Space. Document focus order, visible indicator at every stop, and whether special key handling works. Checklist in the component doc.
3. **Screen reader audit** — NVDA on Windows or VoiceOver on macOS. Test each component and each state with the primary screen reader for the target platform. Document the announcement sequence and confirm it communicates state changes (disabled, loading, expanded).
4. **User test with assistive technology** — 3-5 participants who rely on assistive technology, testing key flows. Budget for this in the system's release cycle; it is required before any major version bump.

## Documentation checklist for component authors

Every component doc must answer, before it leaves review:

- [ ] Which ARIA pattern does this component implement? Reference by name.
- [ ] What is the accessible name source (label, aria-label, aria-labelledby)?
- [ ] Where does focus land on mount (if applicable)?
- [ ] Where does focus return on unmount (if applicable)?
- [ ] How is disabled state communicated (aria-disabled, reduced opacity, both)?
- [ ] Does every state change produce an appropriate announcement (aria-live region or role change)?
- [ ] Is the focus indicator visible at 3:1 against the component's adjacent surface in every theme?
- [ ] Does the component have automated a11y tests in CI?
- [ ] Does the component have a keyboard audit checklist completed for this release version?

A doc with any unchecked answer fails review until the gap is closed or a written accessibility exception is filed using the process in `versioning-and-governance.md`.