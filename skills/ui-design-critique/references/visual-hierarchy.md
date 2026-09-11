# Visual Hierarchy

Methodology for reading how a screen directs attention: where the eye lands, in what order, and whether that order serves the task. Hierarchy failures are the most common root cause behind "this screen feels off but I cannot say why."

## What hierarchy does

Every screen broadcasts an order of importance whether the designer chose one or not. The user's eye lands somewhere first, scans a predictable path second, and only then reads. Hierarchy is the deliberate arrangement of size, weight, color, position, and space so that the eye's path matches the task's order: orientation first, primary content second, primary action third, machinery last.

A screen has working hierarchy when a user can answer three questions within seconds of arrival:

1. Where am I? (orientation — page or step identity)
2. What is the main thing here? (the primary content or number)
3. What do I do next? (the primary action or a clear path)

If any answer takes effort, note which one and what is competing with it — that is the finding's raw material.

## The first-fixation test

The core diagnostic, run on every screen in a critique:

1. Look at the screen for three seconds, then look away. Write down what you remember — that is what the screen made primary.
2. Compare the remembered element against the screen's goal sentence (see `references/critique-principles.md`).
3. If the remembered element is not the goal-critical element, hierarchy has failed, and the finding writes itself: "the promo banner out-shouts the checkout CTA."

Record the fixation, not the intention. "The designer wanted X emphasized" is irrelevant; the test records what the screen actually emphasizes. If you cannot look away honestly (you have seen the screen too many times), hand it to someone uninvolved for ten seconds, or judge by the lever inventory below: add up what every tool of emphasis is doing, and the winner of the first fixation is usually arithmetic.

## Mapping attention order

For each screen, list the attention order as the design delivers it, then the order the task needs. The gaps are findings.

- Delivered: promo banner → hero image → order summary → CTA.
- Required: order summary → CTA → promo banner.
- Gap: the two task-critical elements rank third and fourth.

Rank attention honestly: first fixation, second, third. Most screens reveal their true order in the top three positions; below that, detail rarely lands on a first pass.

## The emphasis budget

Emphasis is a finite resource. Every element that shouts devalues every other shouting element.

- One primary focal point per screen — the single thing that must be seen or clicked.
- At most two secondary emphases: a key number, a warning, a status.
- Everything else is body weight. If five elements are bold, colored, and boxed, the screen has zero hierarchy, not five.

Budget violations are findings even when each element is individually defensible: "four competing calls to action share the same fill and size; keep one primary and demote the rest to text links (button hierarchy — see `references/interaction-patterns.md`)."

Budgets also apply across a flow. A five-screen flow where every screen has a different primary action color, weight, and position teaches the user nothing transferable; consistency across screens is part of the same budget.

## Tools of hierarchy, in order of strength

1. **Position** — top-left (in reading-order cultures) and center read first; bottom-right reads last.
2. **Size** — the strongest lever; a 2x area difference reads instantly. Use steps, not tweaks: a 15% size difference reads as a mistake.
3. **Weight and color** — bold and saturated pull the eye; reserve the most saturated color for the primary action.
4. **Whitespace** — space isolates and elevates. A crowded primary action is a contradicted primary action.
5. **Imagery** — faces and high-contrast images out-pull any text element; place them deliberately or they win the first fixation by accident.

Changing several levers at once multiplies emphasis. A large, bold, saturated, isolated element is nearly impossible to demote without a redesign — flag it as a structural finding, not a styling tweak.

## Scanning patterns

- **F-pattern (text-heavy pages):** users read the first lines fully, then progressively less down the page. Front-load the point; the right edge of mid-page is a dead zone.
- **Z-pattern (sparse screens, short forms):** the eye sweeps top-left to top-right, diagonally to bottom-left, across to bottom-right. Reserve the terminal corner for the primary action or the brand mark, not decoration.
- **Mobile top-to-bottom:** single-column scanning collapses to a straight line downward under the thumb. The bottom third of the viewport is prime action territory; the top third is orientation territory.

Do not design against these patterns; place the critical content inside them. A checkout CTA at the visual dead center of a scrolling mobile page fights the pattern and loses.

## Hierarchy on scroll

Above the fold is where hierarchy is decided, but scrolled content still needs an order:

- The first viewport should answer the three arrival questions completely; a CTA visible but its consequence (the total, the terms) below the fold is a hierarchy finding.
- Repeating the primary action in a sticky bar beats asking users to remember where it was.
- Section transitions need spatial rhythm: when every scroll stop looks identical, the user loses position sense; vary group spacing deliberately (see `references/layout-and-spacing.md`).

## Common hierarchy failures

- Everything emphasized, so nothing is (the budget is blown).
- The loudest element is decorative — hero art, promo banner — while the task element whispers.
- Symmetry misused: the primary action and a cancel link given equal size and weight.
- Low-priority content placed top-center, where it hijacks the first fixation.
- Numbers users scan for — totals, balances, counts — styled as caption text.
- A second "primary" button introduced for a secondary action (express checkout, upgrade prompts) competing with the real one.

## The fix ladder

Propose hierarchy fixes in the cheapest effective order; each rung is a smaller change than the next:

1. **Move** — reposition the competing element (free; no visual language change).
2. **Space** — add separation around the primary element (a margin change).
3. **Demark** — demote the competitor: lighter weight, neutral color, smaller size (a token change).
4. **Restyle** — promote the task element: weight, color, size step (still within the existing system).
5. **Restructure** — only when no styling arrangement can close the gap: merge screens, remove the competing module, redesign the layout.

A report that jumps to restructure while demark would do is over-prescribing; a report that demarks when the whole module must go is under-prescribing. Say which rung your fix sits on.

## Hierarchy review method

1. Write or read the screen's goal sentence.
2. Run the first-fixation test; record the delivered order in three positions.
3. Write the required order from the task's perspective.
4. List the gaps as candidate findings with evidence: which element, which position, what out-shouts what.
5. Check the emphasis budget; count the focal points.
6. Propose fixes via the fix ladder, naming the rung; reserve "restructure" for when position and emphasis alone cannot close the gap.
