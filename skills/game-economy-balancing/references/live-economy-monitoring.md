# Live Economy Monitoring

Metrics guide for tracking economy health in live operations. Use this file when
setting up a dashboard for a launched game, diagnosing a live imbalance from
telemetry, or designing alert thresholds before launch. Monitoring is not
optional — an economy without telemetry is a plane flying in fog.

## 1. The Seven Essential Metrics

These seven metrics catch every major failure mode. Track them daily from day
one of launch.

**Total currency supply per type.** Raw count of every currency in circulation.
Alert if growth exceeds 20% week-over-week. Catches hyperinflation before it
affects player-facing prices.

**Daily sink ratio.** Sinks consumed divided by faucets generated, per currency,
measured daily and averaged weekly. Target: 0.85-1.20. This is the single
leading indicator of economy health — when it moves, something is wrong.

**Wealth gap.** Top 10% average divided by median. Measured weekly.
Above 3.5 triggers a diagnostic; above 5 triggers an escalation and model
rebuild.

**First upgrade time.** Actual time for a new player persona to make their
first meaningful purchase. Compare against the model projection. If real time
exceeds the model by more than 25%, the economy is tighter than designed and
casual players are being pushed out.

**Currency velocity.** Transaction volume divided by total supply. Low velocity
combined with high supply means hoarding — players have currency but nothing
to spend it on. This is the signal for adding aspirational sinks.

**F2P path viability.** Percentage of premium-only items that are reachable
through free play within 2x the paid time cost. If this drops below 80%,
the F2P path has eroded in practice even if it exists in design.

**Revenue per active user ($/DAU or $/MAU).** Sudden drops mean engagement or
conversion problems. Sudden spikes often mean players feel forced to spend —
investigate before celebrating.

## 2. Dashboard Architecture

The live dashboard should update daily (real-time within one hour):

1. Currency supply time-series (7d, 30d, all-time) for each primary currency.
2. Daily faucet vs. sink bar chart (today vs. 7-day average).
3. Active player segments by wealth tier.
4. Item price tracker with moving average.
5. Wealth concentration: top 100 players' share of total supply.
6. Faucet composition: currency creation by source.
7. Sink decomposition: where currency was consumed.

## 3. Alert Thresholds

| Alert Level | Condition | Response |
|-------------|-----------|----------|
| Info | Any metric 10-20% outside target range | Log, monitor |
| Caution | Any metric 20-33% outside target range | Open diagnostic cycle |
| Escalation | Any metric >33% outside target range | Emergency tuning cycle |
| Critical | Wealth gap >5.0 or deadlock rate >5% | Full model rebuild |

## 4. Anomaly Signals

Hyperinflation: total supply increases 10x in 2 weeks. Response: immediately
cap the largest unbounded faucet and inject a sink event.

Deflation: sink ratio >1.30 for two consecutive weeks. Response: add a
time-limited login faucet boost and reduce the most-visible sink cost by 10%.

Botting / farming: the top 1% of earners accounts for more than 40% of total
daily faucet. Response: investigate account behavior; if confirmed botting,
implement per-account faucet caps.

Market cornering (player-driven economies): a single player or guild controls
>30% of a traded good's weekly volume. Response: set NPC price floor and
per-account storage cap on the good.

## 5. Post-Patch Monitoring

| Phase | Duration | Activity |
|-------|----------|----------|
| Stabilization | 24-48 hours | Monitor core metrics hourly |
| Triage | Day 3-7 | Adjust as needed, one lever at a time |
| Settlement | Day 7-14 | Let economy reach new equilibrium |
| Long-term | Day 14+ | Watch for emergent imbalance |

Document every post-patch adjustment: the lever, the old value, the new value,
the measured effect after 72 hours.