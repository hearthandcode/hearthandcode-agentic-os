# Economy Model: [Game Name]

Fill in the bracketed fields with your game's data. Use this template as your
output document after completing the workflow in SKILL.md section 04. Every
section maps to one or more workflow steps. Guidance blocks (blockquotes) help
you fill each section — remove them from the final document.

> **Guidance:** Start with the game title, version, and status. Version follows
> semantic versioning: bump major when architecture changes, minor when
> parameters change, patch for corrections.

## Version

- **Version:** 0.1.0
- **Status:** Draft
- **Date:** [date]
- **Author:** [name / team]

## 1. Game Profile

> Define the game that owns this economy. Be specific about genre, target player,
> and monetization model — these anchor every downstream parameter.

| Field | Value |
|-------|-------|
| Game title | [name] |
| Genre | [e.g., midcore crafting RPG] |
| Platform(s) | [PC / mobile / console] |
| Target player | [Casual / Midcore / Hardcore / Mixed] |
| Monetization model | [F2P / Premium / Subscription / Battle Pass / Hybrid] |
| Hours to endgame (median persona) | [N hours] |

## 2. Currency Architecture

> List every currency and resource in the game. Each occupies exactly one axis
> (vertical progression, horizontal expression, content gating, friction
> recovery). If two currencies share an axis, merge them.

| Symbol | Name | Type | Axis | Faucet Sources | Sink Uses | Storage |
|--------|------|------|------|----------------|-----------|---------|
| [SYM] | [Name] | [primary_soft / secondary_soft / premium / reputation / seasonal] | [axis] | [list] | [list] | [uncapped / hard cap / soft cap] |
| [SYM2] | [Name2] | ... | ... | ... | ... | ... |

### Conversion Rules

> Every cross-currency path must be documented: direction, rate, caps. Block
> any path that violates premium purity.

| From | To | Rate | Direction | Cap | Notes |
|------|----|------|-----------|-----|-------|
| [C1] | [C2] | [N:1] | [one-way / bidirectional] | [daily cap / none] | [rationale] |

## 3. Personas

> Define at least three personas. Each needs a time budget, play style, session
> count, and spending behavior. The default set is Casual (1h/day), Midcore
> (2.5h/day), Hardcore (5h/day). Add Whale when monetization relies on
> high-dollar purchases.

| Persona | Hours/Day | Sessions/Day | Active Ratio | Spend Ratio | Play Style |
|---------|-----------|-------------|-------------|-------------|------------|
| Casual | 1.0 | 1 | 70% | 50% | [description] |
| Midcore | 2.5 | 2 | 80% | 70% | [description] |
| Hardcore | 5.0 | 3 | 85% | 90% | [description] |
| [Whale] | [N] | [N] | [N%] | [N%] | [description] |

## 4. Faucet Inventory

> Every source of every currency. Tag each faucet with its type (unbounded,
> bounded, skill) and its rate per hour. Faucets with no explicit rate are
> not faucets — they are holes.

| Activity | Currency | Faucet Type | Rate/Hour | Bound | Conditions |
|----------|----------|-------------|-----------|-------|------------|
| [Activity] | [SYM] | [unbounded / bounded / skill] | [N] | [daily cap / none] | [when available] |

## 5. Sink Inventory

> Every drain on every currency. Tag each sink with its type (procedural,
> aspirational, social, friction). Every currency needs at least three sinks
> across at least two different sink types.

| Activity | Currency | Sink Type | Cost | Frequency | Conditions |
|----------|----------|-----------|------|-----------|------------|
| [Sink] | [SYM] | [procedural / aspirational / social / friction] | [N] | [per session / per day / one-time] | [when available] |

## 6. Progression Curve

> Choose one curve model per currency. Compute time-to-milestone for each
> persona using the daily faucet rate and the milestone cost. Include the
> skip-day correction (1.4x for casual, 1.15x for midcore, 1.0x for hardcore).

| Milestone | Currency | Cost | Curve | Casual Time | Midcore Time | Hardcore Time |
|-----------|----------|------|-------|-------------|--------------|---------------|
| First Upgrade | [SYM] | [N] | [linear / quadratic / exponential / logarithmic] | [N h] | [N h] | [N h] |
| Mid Gate | [SYM] | [N] | ... | [N h] | [N h] | [N h] |
| Endcap | [SYM] | [N] | ... | [N h] | [N h] | [N h] |

## 7. 28-Day Balance Sheet Simulation

> Per-persona daily balance projection. Include day-1 through day-28 running
> balance, total faucets, total sinks, and net flow. Calculate sink ratio and
> inflation rate per currency per week.

**Persona:** [Casual]

| Day | Total Faucet ([SYM]) | Total Sink ([SYM]) | Net Flow | Running Balance | Sink Ratio |
|-----|----------------------|--------------------|----------|----------------|------------|
| 1   | [N] | [N] | [+/-N] | [N] | [N] |
| 7   | [N] | [N] | [+/-N] | [N] | [N] |
| 14  | [N] | [N] | [+/-N] | [N] | [N] |
| 21  | [N] | [N] | [+/-N] | [N] | [N] |
| 28  | [N] | [N] | [+/-N] | [N] | [N] |

> Repeat the same table for Midcore and Hardcore personas. Copy and paste.

## 8. Diagnostics

> Compute all diagnostic metrics from the simulation data. Compare against
| target ranges.

| Metric | Target Range | Casual | Midcore | Hardcore | Status |
|--------|-------------|--------|---------|----------|--------|
| Sink ratio (28d) | 0.85-1.20 | [N] | [N] | [N] | [Pass / Fail] |
| Inflation rate (weekly avg) | 1-6% | [N] | [N] | [N] | [Pass / Fail] |
| Wealth gap | <3.5x | [N] | [N] | [N] | [Pass / Fail] |
| Endgame time ratio (casual/hardcore) | <2.0x | [N] | — | — | [Pass / Fail] |
| First upgrade time | <60 min | [N] | [N] | [N] | [Pass / Fail] |
| Premium purity | No power | — | — | — | [Pass / Fail] |

## 9. Monte Carlo Results

> 1000-iteration simulation results. Report the three gates.

| Gate | Threshold | Result | Status |
|------|-----------|--------|--------|
| Deadlock rate at day 14 | ≤5% | [N%] | [Pass / Fail] |
| Currency supply CV | ≤15% | [N%] | [Pass / Fail] |
| Zero liquidity days | ≤2 consecutive | [N] | [Pass / Fail] |

## 10. Ethics Review

> Score every purchase flow against the dark pattern checklist from
> references/monetization-ethics.md. Document each finding.

| Purchase Flow | Dark Patterns Found | Mitigation | Status |
|--------------|-------------------|------------|--------|
| [Flow name] | [list] | [actions taken] | [Clean / Flagged / Redesigned] |

## 11. Tuning History

> Document every tuning change: which lever, old value, new value, delta,
> outcome. Append to this table after every cycle.

| Date | Lever | Old Value | New Value | Delta | Reason | Outcome |
|------|-------|-----------|-----------|-------|--------|---------|
| [date] | [parameter] | [N] | [N] | [+/-N%] | [why] | [measured effect] |

## 12. Live Dashboard Specification

> Define dashboard metrics and alert thresholds per references/live-economy-monitoring.md.

| Metric | Calculation | Healthy Range | Alert (Caution) | Alert (Escalation) | Response |
|--------|------------|--------------|-----------------|-------------------|----------|
| [Name] | [formula] | [range] | [range] | [range] | [action] |

## 13. Risk Register

> Map every failure mode from references/economy-case-studies.md to a
| projected scenario in this design.

| Failure Mode | Analogous Scenario | Trigger Signal | Preventative Measure |
|-------------|-------------------|---------------|---------------------|
| [From case studies] | [specific scenario] | [metric + threshold] | [design element] |

## 14. Known Issues

- [Issue 1 — description and planned resolution]
- [Issue 2 — description and planned resolution]

---

*Generated with the game-economy-balancing skill. Schema validation recommended
before distribution.*