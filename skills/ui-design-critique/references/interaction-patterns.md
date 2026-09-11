# Interaction Patterns

Pattern catalog for judging behavior: forms, navigation, feedback, empty states, and destructive-action confirmations. Visual critique asks whether things look right; this file asks whether things *behave* right. Most P0 and P1 findings in flow critiques come from broken or missing interaction patterns, not from visuals.

How to use the catalog: identify the pattern each screen implements, compare it against the canonical pattern below, and record deviations as findings with the deviation, the expected pattern, and the user consequence. A deviation that helps the user is a delight; one that confuses is a finding.

## Forms

Forms carry most transactional flows. The canonical rules:

- **Visible labels above fields.** Placeholder-as-label disappears on input, fails memory for multi-field forms, and typically ships with failing contrast. Floating labels are acceptable; placeholder-only is a finding.
- **One logical group per step.** Multi-step flows beat one mega-form, but each step must earn its split (shipping ≠ payment ≠ review). Splitting one address into two steps for visual reasons is a finding.
- **Input types match data:** `type="email"` gets email keyboards, `type="tel"` gets numeric phone pads, `inputmode="numeric"` for card and ZIP fields, `autocomplete` attributes (`cc-number`, `postal-code`, `name`) so browsers autofill. Missing autofill on known fields is a P1-level friction finding on mobile.
- **Validation timing:** validate on blur or after the user stops typing — never on every keystroke (mid-typing "invalid" errors), never only at submit (errors far from their fields). Inline error placement belongs with the field, stating what is wrong and how to fix it, in text — not just a red border.
- **Error recovery:** after a failed submit, focus the first errored field, preserve all entered data, and summarize the error count at the top for long forms. Losing data on back-navigation is a P0 in a checkout flow.
- **Never disable the primary button silently.** If the button is disabled until valid, the user needs to see *why*; otherwise keep it enabled and validate on tap.
- **Optional fields are marked, not mandatory ones** — or better, cut the optional fields; every field is a tax on completion.

## Navigation

- **Location awareness:** the user must know where they are — highlighted nav item, breadcrumb, step indicator, or page title. A multi-step flow without a step indicator ("Step 2 of 4") leaves users with no exit-cost model, which drives abandonment.
- **The escape hatch:** every non-terminal screen offers a visible way back or out. Back must never lose entered data in the same session (see Forms). Modals need an explicit close affordance plus Escape.
- **Consistent orientation:** nav placement, logo position, and cart access do not move between screens. "The back arrow is top-left on the cart and absent on the address screen" is a finding.
- **Primary path versus detours:** the flow's main path is continuously available; cross-sells, promos, and "you might also like" never occupy the primary action's slot or out-shout it (see `references/visual-hierarchy.md` on the emphasis budget).

## Feedback and status

Every user action gets an acknowledgment within about a second — the system's answer to "did that work?"

- **Loading:** buttons show progress during slow submits (spinner in the button, disabled state with a label change); screens show skeleton or progress for content loads. A silent 3-second wait after "Place order" reads as a crash and invites double-clicks.
- **Double-submit protection:** payment and submit actions are idempotent or visually locked during processing. Two charges from a double-tap is a P0.
- **Success:** confirmations state what happened and what happens next ("Order #4821 confirmed — receipt sent"). Silence after a completed action is a finding.
- **Errors:** human-readable, actionable, near the trigger. "Payment declined by your bank — try another card or contact them" beats "Error 402." System jargon, raw codes, and blame-the-user phrasing ("Invalid input!") are findings.
- **Toasts:** used for reversible confirmations, never for errors the user must act on (errors live inline, where they cannot time out), never stacking as the only record of a critical outcome.

## Empty states

Every list, feed, search, and dashboard has an empty state: first use, no results, cleared, or error.

- **First-use empty state** teaches and offers the next action ("No orders yet — start with our bestsellers"), never a bare zero.
- **No-results state** says what was searched and offers a widening action ("No results for 'shoe' — try 'footwear' or clear filters"). Dead-end empty states are findings.
- **Error empty state** distinguishes failure from emptiness — a blank screen that looks like "nothing here" when the request failed is a P1.
- Empty states are the cheapest place to carry brand voice; they are also the most commonly unshipped screen. Ask for them explicitly when the requester provides screens.

## Confirmation and destructive actions

- Irreversible actions (delete, cancel order, overwrite) get a confirmation naming the consequence and the object ("Delete draft 'Q3 plan'? This cannot be undone").
- Destructive buttons never take the confirmatory slot styling (primary/filled) — the safe action or explicit cancel is primary (see `references/color-and-contrast.md` on semantic color).
- Frequent low-stakes actions should not confirm; confirm-fatigue trains users to click through real warnings.

## Microinteractions

- Transitions animate state *change* (what moved, what appeared) at 150–300ms; decoration that merely delays is a finding.
- Motion respects the user's reduced-motion setting (`prefers-reduced-motion`) — see `references/accessibility-review.md`.
- Hover and focus states exist for every interactive element; a link with no hover state reads as dead text.
- State changes preserve context: if a filter change collapses the list the user was reading, the new state should restore scroll position or say why it cannot.

## Pattern audit method

1. Walk the flow as a user would; note the pattern each screen implements.
2. For each, compare against this catalog; list deviations with evidence.
3. Probe the unhappy paths explicitly: submit empty, submit invalid, lose network mid-submit, press back mid-form, double-click the primary action.
4. For each screen, also ask what is *missing*: no empty state, no loading state, no error state, no zero-data state. Absent patterns are findings too — the screenshot cannot show what was never designed.
5. Rate each deviation's severity by user consequence (per `references/critique-principles.md`), not by implementation difficulty.