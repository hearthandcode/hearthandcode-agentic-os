# Worked UI Critique — ShopSimple Checkout Flow

Extended worked example referenced by SKILL.md section 06. Product, screens, and numbers are fictional. The deliverable is the full critique report with exactly 12 prioritized findings for a mobile e-commerce checkout: cart → shipping address → delivery options → payment → confirmation.

## Metadata

- **Product:** ShopSimple — a small web shop's mobile checkout
- **Screens:** 5 (cart, shipping address, delivery options, payment, confirmation)
- **Source:** static design file exports plus a staging build (behavior verifiable)
- **Viewport:** 390px-wide mobile
- **Goal capture:**
  - Cart: "A returning customer can review and adjust items, see an accurate total, and move to checkout with confidence."
  - Shipping address: "The customer enters a shipping address once, without errors or re-entry."
  - Delivery options: "The customer picks a delivery option understanding the cost and date tradeoff."
  - Payment: "The customer pays with their preferred method without double-charges or confusion about the amount."
  - Confirmation: "The customer knows the order went through, what happens next, and how to get help."
- **Scope:** the five checkout screens only; account creation flows and the storefront are out of scope.
- **Finding distribution:** 2 P0, 5 P1, 4 P2, 1 P3 — 12 delivered.

## What works

- The step indicator ("Step 2 of 4") on the address and delivery screens sets exit-cost expectations — keep this pattern when redrawing (see `references/interaction-patterns.md`).
- Autocomplete is wired on the email field; mobile keyboards open the right one (SC 1.3.5 — see `references/accessibility-review.md`).
- The confirmation screen states the order number and next steps in plain language — the strongest screen in the flow.

## Findings

### 1. [P0] Back-navigation on the address screen erases everything the customer typed
- **Evidence:** Entering an address, tapping back to the cart to check a coupon, and returning to the address screen shows all fields empty. Staging build reproduced 3 of 3 times.
- **Principle:** Never lose user data in-session; error prevention (SC 3.3.4) (see `references/interaction-patterns.md`, `references/accessibility-review.md`).
- **Fix:** Persist address state per session; restore on return. Ship this before redesigning anything else.

### 2. [P0] Double-tap on "Place order" can submit twice
- **Evidence:** The button has no disabled or progress state while the payment request is in flight (a silent ~3s wait); a rapid double-tap in staging produced two order confirmations (#4821, #4822).
- **Principle:** Double-submit protection on financial actions; feedback within ~1s (see `references/interaction-patterns.md`).
- **Fix:** Disable the button and swap its label to "Placing order…" on first tap; make the endpoint idempotent.

### 3. [P1] The cart shows a subtotal, not the payable total
- **Evidence:** Cart lists "$142.00 subtotal" and a "Checkout" button; delivery cost and tax surface two screens later. No estimate appears earlier, so the number the customer budgets against is the wrong one.
- **Principle:** Feedback and status — decision-relevant truth belongs where the decision happens (see `references/interaction-patterns.md`).
- **Fix:** Show an estimated total on the cart ("Est. total $158.20 incl. standard delivery and tax"), restated accurately at each step.

### 4. [P1] Address fields lose browser autofill on the two fields customers most want it
- **Evidence:** Name and email have `autocomplete` attributes; street address and ZIP do not (plain `type="text"`, no `autocomplete="street-address"` / `"postal-code"`); ZIP opens the full alphabet keyboard because `inputmode` is missing.
- **Principle:** Input types and autofill match the data (see `references/interaction-patterns.md`).
- **Fix:** Add the attributes; use `inputmode="numeric"` on ZIP and card fields.

### 5. [P1] Delivery options hide prices and give no arrival dates
- **Evidence:** Three radios labeled "Standard," "Express," "Priority" — prices hidden inside a collapsed "details" accordion, no dates anywhere. The customer cannot make the cost/date tradeoff this screen exists for.
- **Principle:** No expand-only critical content (SC 1.4.13) (see `references/interaction-patterns.md`, `references/accessibility-review.md`).
- **Fix:** Show "Express — $9.90 — arrives Thu, Sep 17" as the radio label; the accordion holds only carrier fine print.

### 6. [P1] Promo-code "Apply" competes with the primary CTA
- **Evidence:** "Apply" and "Continue to payment" share fill color, size, and weight; the first-fixation test lands on the promo pair, not the CTA.
- **Principle:** Emphasis budget — one primary action per screen (see `references/visual-hierarchy.md`).
- **Fix:** Demote "Apply" to a text link; "Continue to payment" becomes the only filled button.

### 7. [P1] Card-number errors surface only after full submit, in a summary far from the field
- **Evidence:** Submitting a 15-digit card shows "There is 1 error on this page" at the top of the screen; the field itself is unmarked; entered data is preserved (correctly).
- **Principle:** Validate on blur, near the field, with a suggestion (SC 3.3.1, 3.3.3) (see `references/interaction-patterns.md`, `references/accessibility-review.md`).
- **Fix:** Validate format on blur ("Card number is 16 digits — this one has 15"), mark the field, move focus to it on submit failure.

### 8. [P2] Placeholder gray fails contrast on every form
- **Evidence:** Placeholders render #9CA3AF on #FFFFFF (2.5:1) — below the 4.5:1 minimum for normal text.
- **Principle:** WCAG 1.4.3 Contrast (Minimum) (see `references/color-and-contrast.md`).
- **Fix:** Darken placeholders to a 4.5:1-passing neutral, or replace them with persistent labels (which should exist anyway — see finding 12's sibling, the pattern fix in `references/interaction-patterns.md`).

### 9. [P2] Payment screen runs 11 font sizes and mixed corner radii
- **Evidence:** 11 distinct font sizes on one screen (a 6-role scale would do); card number field 12px radius, CVC 8px, "Place order" 16px.
- **Principle:** Type scale discipline; component consistency (see `references/typography-basics.md`, `references/layout-and-spacing.md`).
- **Fix:** Consolidate to a documented scale; one radius token for inputs, one for buttons.

### 10. [P2] Delivery options screen has five unrelated spacing values playing one role
- **Evidence:** Gaps between the three option cards measure 10, 12, 14, 16, and 18px — no rhythm, no system.
- **Principle:** One spacing scale; semantic spacing roles (see `references/layout-and-spacing.md`).
- **Fix:** Collapse to 8/16/24 tokens; option cards sit at 16px.

### 11. [P2] Order summary starts 320px down — below the fold on the payment screen
- **Evidence:** On a 390px viewport, the payable total requires scrolling past a trust-badge carousel and a "you might also like" module; the CTA is fully visible but the amount it commits to is not.
- **Principle:** The primary action and its critical context stay within the first viewport; the primary path beats detours (see `references/visual-hierarchy.md`).
- **Fix:** Put a compact total line ("Total $158.20") beside "Place order"; demote the cross-sell below the summary.

### 12. [P3] Two different reds for the same error role
- **Evidence:** The declined-card error on the payment screen uses #DC2626; the address form uses #B91C1C for the same error role.
- **Principle:** Semantic color consistency (see `references/color-and-contrast.md`).
- **Fix:** One error token for the product.

## Open questions

- Shipping cost calculation could not be verified for non-US addresses from the staging environment — verify in build before assuming finding 3's estimate approach holds internationally.
- Promo-code acceptance rules are undocumented; whether "Apply" should survive at all is a team decision (finding 6 assumes it does).
- Whether ShopSimple ships a dark theme was not specified; this critique covers the light theme only.

## Assumptions

- Audience is mobile-first shoppers; a desktop pass is out of scope this round.
- The staging build reflects production behavior for payments and validation timing.
- "Small web shop" means a small engineering team: fixes above are scoped for a 1–2 day pass, not a redesign program.
