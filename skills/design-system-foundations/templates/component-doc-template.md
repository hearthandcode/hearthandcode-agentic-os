# Component Doc Template

Copy this file per component. Delete this guidance block after filling it in.
The companion guides are `../references/pattern-documentation.md` (how to write
each section) and `../references/accessibility-standards.md` (ARIA patterns,
keyboard contracts, and testing requirements). Every component's doc must pass
a review before the component ships as stable.

## Guidance

The doc is written for the engineer or designer who needs to use this component
*right now*. It is not the component's design history, it is not the team's
workshop notes, and it is not the place to argue about alternatives. If the
reader cannot ship a correct instance of this component in one afternoon using
only this document and the component's source, the document has failed.

Target length: one to two pages. If the anatomy, variants, and states fill
three pages, consider whether you are documenting one component or three.

```markdown
---
name: <component-name>
version: 1.0.0
status: stable            # experimental | stable | deprecated
owner: <team-name>
last-reviewed: YYYY-MM-DD
related-components: [<other-component-names>]
aria-pattern: <pattern-name-from-accessibility-standards.md>
---

## Summary

One sentence: what this component is for. One sentence: when *not* to use it
and what to use instead.

## Anatomy

Numbered list of the component's visual and structural parts, outside to inside.

1. <Part name> — <its job> — maps to prop `<prop-name>` and token `<token-name>`.
2. <Part name> — <its job> — maps to prop `<prop-name>` and token `<token-name>`.

Rules:
- Every named part maps to at least one prop and one token.
- Parts that never change appearance or behavior are not anatomy — remove them.

## Variants

List the variant axes (intent, size, layout) with the allowed combinations
shown in a table. Every disallowed combination is a decision, not an oversight.

| | variant-A | variant-B |
|---|---|---|
| axis-1-value-1 | ✓ | ✓ |
| axis-1-value-2 | ✓ | ✗ |

## Props

| Prop | Type | Default | Description |
|---|---|---|---|
| <name> | <type> | <default> | <one sentence — what changing it does> |

Focus on usage contract, not code signature. "Setting `loading` replaces the
label with a spinner and sets `aria-busy='true'`" is better than "loading:
boolean."

## States

| State | Visual change | Trigger | Announcement |
|---|---|---|---|
| rest | <description> | default | — |
| hover | <description> | pointer enters | — |
| focus-visible | <description> | Tab / keyboard nav | — |
| active | <description> | pointer down / Enter | — |
| disabled | <description> | disabled prop | aria-disabled |
| loading | <description> | loading prop | aria-busy |

Every interactive component must have focus-visible styling. Pointer-only
affordances are how keyboard users get stranded. Loading, error, empty, and
disabled are content decisions — who authors the text?

## Do / Don't

1. **Do:** <correct usage>
   **Don't:** <wrong usage> — <reason this is wrong, grounded in a11y or UX>
2. **Do:** <correct usage>
   **Don't:** <wrong usage> — <reason>

Three to six pairs. Each Don't names its Do. Ground each pair in a reason.

## Accessibility notes

- Pattern: <name from accessibility-standards.md>
- Roles: <required roles>
- Focus behavior: <where focus lands on mount, where it returns on unmount>
- Accessible name source: <label / aria-label / aria-labelledby>
- One test: <the single test that proves a11y — "tab through: focus must enter
  the dialog and return to the trigger" — this test must be verifiable without
  the design file>

## Examples

One canonical example per variant axis. Show the compliant version; link to the
Don't section for the anti-pattern.

```jsx
<Component variant="primary" size="md">
  Label
</Component>
```

## Keyboard interactions

| Key | Action |
|---|---|
| Tab | <move focus to next tabbable element> |
| Enter / Space | <activate or toggle element> |
| Escape | <close/dismiss if applicable, return focus> |
| Arrow keys | <navigate within component if applicable> |

## Related components

| Component | Relationship |
|---|---|
| <name> | <purpose — "use instead when..."> |
| <name> | <purpose> |

## Maintenance

- Owner: <role, not person>
- Last reviewed: <date>
- Test files: <paths to a11y, unit, integration tests>
- Governance rule: a component release without a doc check fails review.
```

Fill-in checklist before marking `stable`:

- [ ] Summary says what it is for and when not to use it.
- [ ] Anatomy parts map to a prop and a token each.
- [ ] Variant table includes allowed combinations; disallowed combos are explicit.
- [ ] Every state in the table has a visual description, trigger, and announcement.
- [ ] Focus indicator is documented and tested at 3:1 contrast minimum.
- [ ] Do/Don't pairs each name their alternative and their reason.
- [ ] ARIA pattern is named from the accessibility standards reference.
- [ ] Keyboard interaction table is complete.
- [ ] Examples are runnable, not representative.
- [ ] Automated a11y test exists in CI and passes.