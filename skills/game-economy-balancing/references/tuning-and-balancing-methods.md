# Tuning and Balancing Methods

Checklist for the iterative calibration of economy parameters before and after
launch. Use this file when a model fails a quality gate and you need to know
which lever to pull, how far, and how to verify the change worked. The goal of
tuning is not to find the perfect number — it is to move from a failing number
to a passing number with the smallest possible change.

## 1. The Delta Method

Every tuning move follows the same three steps:

1. **Measure the delta.** How far is the current value from the target?
   Compute the gap as a percentage of the target. A sink ratio of 0.61 against
   a target of 0.85 has a delta of 28%, but you will not close it in one move.
2. **Select the smallest effective lever.** Start with the least risky
   adjustment. Reducing a faucet rate by 5% is less risky than removing a
   faucet entirely. Adding a new sink is less risky than changing a
   fundamental conversion rate.
3. **Verify with a single-variable test.** Change exactly one lever, re-run
   the 28-day model, and measure the new outcome. If the move did not change
   the outcome, the lever does not work — do not pull it harder, find a
   different lever.

## 2. The Lever Table

| Lever | Effect | Impact | Risk |
|-------|--------|--------|------|
| Reduce faucet rate | Less currency enters | Mild | Low — easily reversible |
| Increase sink cost | More currency exits per purchase | Mild | Low — players notice |
| Add new aspirational sink | New drain with no progression penalty | Moderate | Low — purely additive |
| Add new bounded faucet | More currency enters, controlled | Mild | Low — capped by design |
| Reduce sink cost | Players spend less, accumulate | Mild | Low — players happy |
| Cap unbounded faucet | Prevent infinite injection | Moderate | Medium — skilled players feel nerfed |
| Remove a faucet | Stop a source entirely | High | High — anger if faucet is popular |
| Change conversion rate | Alters cross-currency balance | Systemic | High — cascading effects |

Start with the mildest lever that could plausibly close the delta. Only
escalate if the mild lever proves insufficient.

## 3. The 10% Rule

No single lever may change by more than 10% per tuning cycle. Multiple levers
may change in one cycle, but each is individually capped at 10%. Rationale:
a 10% change is noticeable to the model but usually invisible to the player.
A 20% change is noticeable to both. By capping individual moves, you prevent
over-correction and give yourself room to tune in the opposite direction next
cycle if you went too far.

## 4. Tuning Sequence

When a currency fails a quality gate, apply this sequence:

1. Reduce the largest unbounded faucet by 5-10%.
2. If still out of range, increase the cost of the most-used sink by 5-10%.
3. If still out of range, add a new aspirational sink.
4. If still out of range after three cycles, the architecture is wrong —
   revisit currency roles and sink types from the fundamentals.

Do not skip to step 4 because steps 1-3 are slow. Slow tuning is survivable;
a rebuilt architecture that ships untested is not.

## 5. Post-Launch Tuning Cadence

| Phase | Frequency | Player Expectation |
|-------|-----------|-------------------|
| Alpha / Beta | Weekly | Changes expected, low attachment |
| Launch | Biweekly to monthly | Respond to feedback visibly |
| Stabilization | Monthly | Gradual improvements |
| Mature | As needed, small changes | No surprises |

Ship tuning changes with patch notes that name the changed parameter, its old
value, its new value, and the reason for the change. Players tolerate
adjustments when they understand the logic.