# Economy Modeling

Methodology for building spreadsheet models and Monte Carlo simulations that
predict economy behavior before players enter the system. Use this file when
translating a design into numbers, stress-testing assumptions, or diagnosing
why a model and live data disagree. A model that cannot be wrong (because it
has no testable predictions) is not a model — it is wishful thinking.

## 1. The Static Spreadsheet Model

The simplest and most important modeling tool. Every column per currency per
persona: starting supply, daily faucet events (by type, amount, rate), daily
sink events (by cost, frequency), daily net flow, running balance. Cover at
least 28 days of simulated play.

**Column layout:**

| Day | Faucet A | Faucet B | Total Faucet | Sink A | Sink B | Total Sink | Net Flow | Running Balance |
|-----|----------|----------|-------------|--------|--------|-----------|---------|----------------|
| 1   | 200      | 50       | 250         | 100    | 50     | 150       | +100    | 100             |
| 2   | 200      | 50       | 250         | 120    | 50     | 170       | +80     | 180             |

Every cell must reference input parameters, not hardcode numbers. Changing a
single faucet rate should recalculate the entire 28-day projection. A model
where you must edit 28 cells to change one rate is not a model — it is a
record of manual arithmetic.

**Critical detail: persona time corrections.** A casual player does not play
every day. Multiply total-days by 1.4 for casual, 1.15 for midcore, 1.0 for
hardcore to account for skipped days. Without this correction, the model
claims casual players reach milestones faster than they do in practice.

## 2. The Monte Carlo Simulation

Run 1000 iterations of the model. In each iteration, randomize persona
assignment (weighted by estimated player distribution), randomize daily
activity choices (not every player optimizes every day), and track:

- Time-to-endgame
- Endgame wealth
- Cumulative purchase spend
- Deadlock events (days where the player cannot afford minimum required action)

**Three quality gates:**
1. Deadlock rate across all personas ≤ 5% at day 14.
2. Currency supply variance across runs ≤ 15% coefficient of variation.
3. No persona segment with zero liquidity for more than two consecutive days.

The Monte Carlo reveals failure modes that the static model cannot see. A
static model shows the average path; the Monte Carlo shows which fraction of
players are on paths that end in frustration.

## 3. Sink Ratio and Inflation Calculations

**Sink ratio:** total sinks consumed / total faucets generated, per currency,
measured over the 28-day simulation. Target: 0.85-1.10. Below 0.85 means
inflationary (more enters than leaves). Above 1.10 means deflationary
(currency too scarce). Calculate per currency — never aggregate across
currencies.

**Inflation rate:** (total faucets − total sinks) / total liquid supply, per
week. Healthy range: 1-3% per week. Caution: 4-6%. Escalation: above 6%.

**Wealth gap:** top 10% average wealth divided by median wealth. Below 3.5 is
healthy. 3.5-5.0 triggers intervention. Above 5.0 requires a model rebuild.

## 4. Common Model Errors

**Single persona fallacy.** Modeling only the designer's own play style. Always
model at least three personas. A model that works for the hardcore player but
starves the casual is not a working model.

**Deterministic-only trap.** Static models miss edge cases. Always pair a
static model with a Monte Carlo. The static model validates averages; the
Monte Carlo validates tails.

**Aggregate blindness.** A sink ratio of 1.0 across all currencies sounds
healthy, but one currency could be at 0.3 (runaway inflation) while another
is at 1.7 (starvation). Calculate every metric per currency.

**Forgotten skip days.** Casual players miss days. A model that assumes
perfect daily attendance overestimates casual wealth by 30-40%.

## 5. Backtesting

After launch, compare model predictions against live data. Any metric that
diverges more than 25% from the projection within 14 days triggers a mandatory
model re-review. The model is wrong until proven right. This is not failure —
it is the normal cycle of model refinement. The models that survive are the
ones that get updated.