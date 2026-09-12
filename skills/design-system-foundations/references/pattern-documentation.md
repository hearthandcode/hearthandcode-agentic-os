# Pattern Documentation: Component Docs People Use

Component documentation fails in two ways: written for the system team instead of the consumer, or written once and never updated. A doc that a new engineer cannot use to ship a correct button in one afternoon — without asking anyone — has failed, no matter how thorough it looks. This file is the guide for filling in the component-doc template (see `templates/component-doc-template.md`); it explains what each section is for and the judgment calls inside each.

## The audience contract

Write for the engineer or designer who arrives needing to build or use this component *today*. That reader needs, in order: what it is for and when not to use it, what it looks like and what its parts are, how to make it behave, what will bite them, and what rules they may not break. They do not need the history, the rejected alternatives, or the token table for a component they are not touching.

## Anatomy

The anatomy section names the parts, top to bottom or outside in, so people can talk about the component without pointing at screens: for a text input — container, label, control, helper text, error text, optional leading/trailing affordance. Rules that make anatomy earn its place:

- **Every named part must matter to at least one decision.** If a part never changes appearance or behavior, it is decoration in the doc, not anatomy.
- **Map each part to its token or prop.** The label maps to a prop (`label`), an a11y contract (`<label for>`), and a token (`color-text-secondary`). A part without a mapping is a part someone will break.
- **Show the anatomy as an ordered list, not a diagram alone.** Diagrams rot in repos; a numbered part list survives.

## Variants and props

Document the variant axes, not just the variants. For a button: intent (`primary / secondary / destructive`), size (`sm / md`), and state (rest, hover, focus-visible, active, disabled, loading). For each axis, say which combinations are allowed — the allowed-combination table is the single most valuable line in the doc, because it converts "the design says so" into a rule a reviewer can enforce:

|  | sm | md |
|---|---|---|
| primary | ✓ | ✓ |
| secondary | ✓ | ✓ |
| destructive | ✗ | ✓ |

Props get: name, type, default, and one sentence on what changing it does. Do not copy the code signature; write the *usage* contract — "setting `loading` replaces the label with a spinner and sets `aria-busy`."

## States

Interactivity is a contract between the component and the keyboard, the pointer, and assistive technology. Document, per state: the visual change, what triggers it, and what it announces. If hover styling exists, focus-visible styling must exist too — pointer-only affordances are how keyboard users get stranded. Loading, empty, error, and disabled are *states with content decisions*, not afterthoughts: who authors the loading text? Is the disabled reason exposed to screen readers? If the doc cannot answer, the component is not done.

## Do / Don't

Do/Don't pairs are the highest-leverage lines in the doc and the most-copied section when people write new docs. Rules for writing them:

- **Each Don't names its Do.** "Don't use a Dialog for a destructive confirmation" is useless without "use a Dialog with the destructive intent and an explicit cancel."
- **Ground each pair in a reason.** "Don't nest buttons inside cards that are also clickable — nested interactive elements trap keyboard users and make the click target ambiguous" teaches the rule, not just the taste.
- **Three to six pairs.** Fewer and the doc is toothless; more and the pairs repeat the states section.

Good pairs for common components: Button (don't use intent to mean priority *and* tone), Text Input (don't use placeholder as the only label), Card (don't nest interactive elements in an interactive card), Dialog (don't stack dialogs), Toast (don't put the only copy of required actions in a toast, don't rely on auto-dismiss for critical info).

## Accessibility notes

The a11y section is a checklist, not an essay: name the required ARIA pattern (from `accessibility-standards.md`), the roles that must exist, the focus behavior, and the one test that proves it — "tab through the form: focus must move into the dialog on open and return to the trigger on close." Every line must be verifiable without the design file. Lines you cannot verify are lines you will silently drop during review.

## Examples

One canonical example per variant axis, full-width and copy-pasteable. Examples are the most-visited section; make them runnable rather than representative. If the component has a compliance trap (e.g., a form field whose label must stay visible while the user types), the example shows the compliant version and the doc links to the Don't explaining why.

## Maintenance

Docs die when their owner leaves. Give every component doc: an owner (a role, not a person), a "last reviewed" date, and a rule from `versioning-and-governance.md` that a component release without a doc check fails review. The doc's job is to be the component's contract — and contracts that silently rot are worse than none, because they get cited with confidence.

## The review checklist

Before a component doc ships, a reviewer confirms each item in one pass. Every line is checkable from the doc alone — if a check needs the design file or a meeting, the doc has already failed:

1. A reader can identify the component's job and its two nearest disqualifications ("use X instead when…") from the first two sections.
2. Every named anatomical part maps to at least one token, prop, or ARIA attribute.
3. The allowed-combination table covers every variant axis, and at least one cell is deliberately forbidden.
4. Every interactive state documents its trigger, its visual change, and what assistive technology announces.
5. Focus-visible styling exists anywhere hover styling does.
6. Loading, empty, error, and disabled content decisions name an author, not a hope.
7. Each Don't pairs with its Do and states the reason; there are three to six pairs.
8. The a11y section names the ARIA pattern, the required roles, and one test verifiable without the design file.
9. Every behavioral claim carries a version anchor; the doc states its owner (a role) and its last-reviewed date.
10. The canonical example is copy-pasteable and demonstrates the compliance trap, if the component has one.

## Writing the allowed-combination table

The combination table is where component design actually happens, so it deserves its own method. Build it in this order:

1. **List the axes** — intent, size, density, tone, whatever the component genuinely varies along. Two axes are typical; four is a smell that the component is doing several jobs.
2. **Fill in the legal cells first.** Start from what the product demonstrably uses, not from what a matrix could express. Every cell nobody uses is a maintenance promise nobody made.
3. **Decide the forbidden cells explicitly, with reasons.** A destructive small button exists in the mockups because a designer needed to fit it somewhere; the table is the place to say no and record why ("destructive actions need a full-width confirmation path").
4. **Enforce the table in code.** A prop-type union or runtime assertion that encodes the table converts documentation into the guardrail reviewers actually rely on.

A table that arrives at review with every cell marked ✓ was not designed; it was transcribed. Send it back and ask which combinations the team is willing to support for the component's lifetime.

## Documentation debt triage

Docs rot on a schedule whether or not anyone touches them. Triage the backlog by behavior risk rather than by age:

| Signal | Risk | Action |
| --- | --- | --- |
| Component changed since last doc review | High | Re-verify every behavioral claim; update version anchors |
| Consumers ask questions the doc answers | High | The answers are buried or misordered — restructure, do not append |
| Screenshots drift from current rendering | Medium | Regenerate; visual drift erodes trust in every claim |
| Stale links or renamed tokens | Low | Batch-fix in a patch release with other doc corrections |

A doc older than two release cycles without a review is automatically suspect: schedule its re-verification even if no change fired the signal, because silent drift is the failure mode that never announces itself.

## Anti-patterns

- **The gallery with no rules.** Twenty screenshots, zero statements about when each applies. A gallery is a mood board; docs are a contract.
- **The novel.** Six pages of history and philosophy before the anatomy. If a reader cannot use the component from the first screen, the doc has failed.
- **The unversioned doc.** "This component changed in the last release" with no version number — the reader cannot tell if their installed version behaves this way. Every behavioral claim needs a version anchor.