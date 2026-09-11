# Worked Mechanic Design: Rune Upgrades for Deep Delve

The complete run behind SKILL.md section 06 — a roguelite "one more run"
upgrade mechanic taken from brief to signed-off spec and playtest plan.
Artifacts appear in the order the workflow produces them, trimmed to what
each stage actually emits.

## 1. The brief

> Deep Delve is a mining roguelite: short delves into a procedurally
> layered mine, banking ore at the surface to buy permanent kit. The
> current build fails the "one more run" test — playtesters finish a
> session and stop. Brief: design an upgrade mechanic that converts
> in-run performance into visible, build-defining power, so losing a run
> creates appetite for the next one.

Constraints: 15-25 minute delves; solo and duo co-op; the surface shop
already exists and must not be replaced; five-person team; no new enemy
types this quarter.

## 2. Step 1 — restate the brief as a measurable goal

Restated goal: after a delve ends (success or death), the player should be
able to name what they gained and what they will try next, and should
choose to start a new delve rather than quit. Observable targets:

- 60% of sessions end with an immediate re-entry ("one more run").
- Players can describe their last run's build in one sentence.
- No re-entry stalls longer than 20 seconds (no long unban kairos).

## 3. Step 2 — experience goals and motivation alignment

Experience goals (written before any mechanic): the run should tell a
story the player can retell ("I was a bomb miner that run"), failure
should bank something honest, and upgrades should change how the pickaxe
feels, not just its numbers.

Motivation alignment, checked against `../references/player-motivation-models.md`:

- SDT: the mechanic must feed **competence** (builds that reward skill)
  and **autonomy** (player-chosen shapes, not fixed trees). Relatedness
  is served in duo by shared rune detonations.
- Archetypes: Achievers (build completion), Explorers (rune synergies
  hidden in the mine), and Killers-in-co-op (deepest-depth bragging) all
  get a hook; Socializers get the duo share.
- Displacement check: the existing ore currency already rewards beelining
  veins. The new mechanic must reward *depth commitment* instead, or it
  will double the beeline problem. This constraint shapes everything after.

## 4. Step 3 — loop analysis

Current loops, per `../references/core-loop-design.md`:

- 30-second loop: scan, choose shaft or vein, dig, resolve. Decisions are
  real but shallow — the vein is almost always correct.
- 30-minute loop: delve → hazard bands → escape decision → surface shop →
  buy → redelve. The **bank phase exists but is flat**: purchases are
  linear stat bumps, so the post-escape minutes have no build story, and
  there is no peak. The missing "one more run" energy lives here.

Diagnosis: the loop does not need a new verb; it needs the bank phase to
produce identity. That is a **progression-family** job.

## 5. Step 4 — candidate generation

From `../references/mechanics-taxonomy.md`, three candidates from the
progression family, plus one family-flip:

1. **Rune Upgrades** (chosen): ore glyphs socketed mid-run that grant
   build-defining mods; lost on death but *converted* to insight currency.
2. Talent tree bought at the shop with ore — rejected: doubles the
   existing shop, slow burn, no in-run identity.
3. Prestige-depth multiplier — rejected as the whole answer: no per-run
   decisions, feels like a multiplier tax.
4. Family flip: a social mechanic (duo rune-sharing) — kept as a slice of
   candidate 1 rather than a standalone.

Candidate 1 wins because decisions happen *inside* the run (identity per
run), death conversion keeps failure honest, and it re-uses the ore the
loop already produces.

## 6. Step 5 — mechanic spec

Written with `../templates/mechanic-spec-template.md`, validated against
`../schemas/mechanic-spec.schema.json`:

```markdown
---
name: rune-upgrades
version: 0.2
status: approved
owner: core-design
last-updated: 2026-09-11
related: [surface-shop, hazard-bands, duo-rescue]
---

## Summary
During a delve the player sockets found runes into a 3-slot harness;
each rune grants a build-defining mod; on escape, socketed runes bank
as permanent shop credit, and on death they convert to insight at 40%.

## Inputs
Held harness (3 slots), rune drops from ore clusters and caches,
current hazard band, elapsed delve time, duo partner's harness.

## Rules
1. Runes drop only from clusters 8 m or deeper.
2. Socketing a rune takes 2 s and can be interrupted by damage.
3. Each slot accepts one rune; socketing over a rune destroys it.
4. Runes of the same family (seismic, pyro, logistic) grant a set
   bonus at 2 and at 3 of the same family.
5. On escape, banked runes convert to shop credit at listed value.
6. On death, socketed runes convert to insight at 40% of value.
7. Insight buys nothing but rune odds: next-run rune drop quality.
8. Duo: partners may swap runes at range 5 m; both receive the set
   bonus if their shared family count reaches 2 each.

## Parameters
| name | default | range | owner |
| --- | --- | --- | --- |
| socket_time | 2.0s | 1.0-3.0 | core-design |
| death_insight_rate | 0.40 | 0.25-0.60 | economy-design |
| drop_min_depth | 8 | 5-14 | core-design |
| set_bonus_value | 25% | 15-40% | core-design |

## Interaction Map
Reads: hazard-bands (drop depth gating), duo-rescue (range checks).
Writes: surface-shop (credit), run-loadout (mods).
Triggered by: cluster-break event, cache-open event.
Interrupted by: damage-interrupt, harness-full state.

## Failure and Edge Cases
- Harness full, better rune found: player must destroy one (rule 3);
  UI shows comparative mods side by side.
- Two players socket same cache: first socket wins; second sees
  already-opened state.
- Death mid-socket: socket completes before death check (be generous).
- Escape with zero runes: shop credit unchanged; insight untouched.

## Player Experience Intent
The player should feel their run becoming a *character*: by mid-delve
they can say "I'm going pyro this run." Death should sting but fund the
next attempt's ambition, so re-entry is a plan, not a reset.

## Playtest Plan
Question: "Will players re-enter a delve within 20 s of a death at
least once per session?"
Method: greybox-with-telemetry, n=5, by 2026-09-25.
```

## 7. Step 6 — prototype before production

Per `../references/prototyping-playbook.md`, the fastest-testable-thing
for the *decision* question was paper; the *feel* question needed greybox:

- **Paper (half a day):** 6×6 tile grid, rune cards in three families,
  a dig economy, two sessions with colleagues. Finding: with three slots
  and three families, players locked a family by the second socket and
  ignored the third slot's flexibility. Decision: set bonuses at 2 and 3
  (rule 4) so slot three is a real choice, not filler.
- **Greybox (three days):** cubes, unlit ore, debug mods, death and
  escape flows wired, telemetry on socket/escape/death events. Designer
  play for 30-minute loops, then five outside players.
- **Kill criteria (written before testing):** if fewer than 2 of 5
  players re-enter within 20 s of death, the conversion value is wrong
  or the loop after death is broken — fix before any content work.

## 8. Step 7 — first balance pass

Per `../references/balancing-fundamentals.md`:

- Lever chosen for the beeline problem: **availability** (rule 1, drops
  gated by depth) rather than a magnitude nerf to vein ore — it reshapes
  the strategy space without taxing the existing verb.
- Marginal value: family set bonuses (25%) were stacked against the
  existing shop's flat damage line; the shop line was re-expressed as a
  rune-credit price so both compete on one axis.
- Dominant-strategy check: all-pyro was dominant on paper (burst clears
  hazards best). Response: buff logistic's cache yield at 3-family so
  eco runs answer it, rather than nerfing pyro pre-launch.

## 9. Step 8 — playtest round one and triage

Per `../references/playtesting-methods.md`, five players, quiet
observation, telemetry on. Signals and triage:

- 4 of 5 re-entered within 20 s of death — primary target met.
- Two players destroyed a rune by accident (rule 3), then quit that run:
  **blocked** class. Fix: confirm-to-destroy with mod comparison.
- One player socketed nothing, "saving slots for something better":
  **distorted** class — the empty-harness tax was too cheap. Fix: slot
  one's set bonus counts only when non-empty; players now socket early.
- Complaints that death "still felt bad" with no behavioral drop:
  **polish** class — queue a death-conversion sting and a next-run
  preview card ("your insight: +1 pyro drop next run").

## 10. Step 9 — the decision record

One page, appended to the spec: what shipped, what the evidence was, and
the three retests owed (destroy-confirm, empty-slot incentive, death
sting). The spec version bumped to 0.3; the GDD mechanics table gained a
row linking to `rune-upgrades`.

## 11. What made this run work

- The diagnosis preceded the mechanic: the loop had a flat bank phase,
  so the fix was a progression mechanic, not a new verb.
- Motivation analysis produced a constraint (reward depth, not veins),
  not decoration — and the constraint shaped the drop rules.
- Paper before greybox saved the third slot from being filler for the
  cost of half a day.
- Kill criteria written before the playtest survived contact with the
  playtest; the fix that shipped was priced in levers, not lectures.
