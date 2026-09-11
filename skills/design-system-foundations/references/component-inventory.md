# Component Inventory: Auditing, Grouping, and Prioritizing

A component inventory is a census of the interface you actually have: every button, every card, every table, every modal, recorded with where it lives and how it varies. It is the foundation for every other design-system decision — you cannot consolidate what you have not counted, and you cannot prioritize what you have not priced. Teams that skip the inventory build a system for the interface they imagine; teams that do it build one for the interface that exists.

## The audit pass

Work screen by screen, not component by component. Component-by-component searching ("find all the buttons") biases you toward components you already know about and misses the weird third instance nobody remembers writing. Screen-first guarantees full coverage.

1. **List the surfaces.** Every route, every screen, every significant dialog state. Include states nobody thinks of: empty, error, loading, permission-denied. A surface list of 40 rows for a mid-size product is normal.
2. **For each surface, enumerate the components on it.** Walk the DOM or the design file top to bottom and name each component informally: "filter bar," "stat card," "row of action chips." Informal names are fine at this stage.
3. **For each component instance, record:** which surface, which variant or size, how it is implemented (shared component, page-local, duplicated markup), and anything visually odd. Screenshots live in the audit folder; the rows reference them.

Record instances, not types — five differently-styled card implementations are five rows, not one "Card" row. The divergence *is* the data.

## The tally sheet

A workable tally has one row per component type with columns: count, distinct implementations, worst divergence, and a note on the worst case. Divergence is scored on a 0-3 scale:

- **0** — identical everywhere.
- **1** — cosmetic drift: spacing or color varies within a step or two.
- **2** — behavioral drift: one instance has different states, focus behavior, or markup semantics.
- **3** — conflicting semantics: two things called "Card" that mean different things, or a "button" that is actually a link.

Behavioral divergence (2+) is what a system fixes; cosmetic drift is what it prevents.

## Grouping

Once tallied, group rows into families — the groups users would recognize, not the groups engineers would factor. Ask: which of these are trying to do the same job?

- **Forms:** text inputs, selects, checkboxes, radios, field wrappers, validation display.
- **Overlays:** dialogs, drawers, popovers, toasts, banners. Overlays group by behavior (blocking? dismissible? focus-managed?), not looks.
- **Containers:** cards, panels, table rows, list items. Grouped by content arrangement.
- **Feedback:** badges, banners, empty states, inline alerts.
- **Navigation:** nav bars, tabs, breadcrumbs, pagination, sidebars.

Two rules for grouping: group by *job*, and when in doubt, split. A "Card" that is sometimes a link, sometimes a form container, and sometimes a dashboard tile is three components wearing one name.

## Prioritizing

Score each candidate component on four axes, 1-5 each:

| Axis | 1 means | 5 means |
|---|---|---|
| **Frequency** | appears once | on most surfaces |
| **Divergence** | instances agree | implementations conflict |
| **Risk** | purely cosmetic if wrong | breaks flows if wrong |
| **Effort** (inverse) | huge build | trivial to build |

Compute a rough priority: `(Frequency + Divergence + Risk) − Effort`, and use the number to order a conversation, not to command one. Two judgment rules matter more than the formula:

- **Interactive and focus-managed components rank above static ones.** A Dialog or Toast — which owns focus, layering, and dismissal — is higher priority than a Card, even when the Card appears more often, because it is harder to fix later and fails users harder when wrong.
- **A component nobody can agree on the semantics of waits.** If the team argues about what "Card" means, the scoring is premature; settle semantics first, and score it lower until then.

A founding system for a small product usually lands at five to eight components: the text input (everything starts with a form), the button (every action goes through one), and the two or three containers and overlays that recur everywhere.

## What the inventory produces

- **`inventory.md`** — one row per component type: name, count, implementations, divergence score, example surfaces. This is the evidence base for the shortlist.
- **A divergence appendix** — for the worst three divergences, side-by-side screenshots and one line on why they differ. This is the artifact that convinces a skeptic the system is needed.
- **A coverage check** — surfaces audited / total surfaces, with the stragglers named. An 80% inventory honestly labeled beats a 100% one that silently skipped the settings pages.

Update the inventory when the product changes shape, and re-run the audit before each major system milestone — the census is only trustworthy on the day it is taken.