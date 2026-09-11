# Level Metrics and Telemetry

*Metrics/measurement guide.*

## Overview

Numerical measurement transforms level design from opinion-based iteration to data-informed refinement. This reference covers what to measure, how to collect data, and how to interpret the measurements. Telemetry is not a substitute for feel but a calibration tool.

## Core Metrics

### Completion and Progression

| **Metric** | **What it tells you** | **Target** |
|---|---|---|
| Level completion rate | Percentage from enter to exit | >85% for intro level, >65% for late-game |
| Per-segment completion rate | Percentage of that entered each segment | Drop-offs indicates pace or gating issues |
| Restart rate per segment | How many players restart after enter | > 20% per segment is a design flaw |
| Path divergence rate | How often the player takes a side path | Less than 5% means the path is invisible or unrewarding |

### Death Metrics

| **Metric** | **What it tells you** | **Target** |
|---|---|---|
| Death per minute | Overall difficulty | Under 0.5/min for tutorial; 0.3–0.8/min for core |
| Death heatmap | Spatial distribution of death | Clusters indicate choke sections and balance issues |
| Per-enemy death | Ratio of deaths per paper-type encounter | High specific death means one enemy isn't read |
| First-encounter completion rate | How many die at the start | Under 5% target for beginner levels |

### 3. Encounter Metrics

| **Metric** | **What it tells you** | **Target** |
|---|---|---|
| Time-to-kill per enemy | How long combat takes | Below 15 seconds for minions, 120s for mini-boss |
| Accuracy/panic-input rate | How often the player hits unintended | Above 20% panic rate suggests poor UX |
| Retreat rate | How often the player must back out to recover | >40% retreat suggests the encounter is over-tuned |
| Kill diversity | Did the player use different tools/weapons | Everything 1 kind of weapon: too easy, too unitary |

### 4. Movement Metrics

| **Metric** | **What it tells you** | **Target** |
|---|---|---|
| Path linearity score | Speeds that the player followed the intended path vs. wandered | High linearity is expected for tutorial; lower for exploration |
| Run-speed vs. walk-speed ratio | How often the player is sprinting | Very sprint ratio indicates rest beats are missing |
| Turn-around rate | How often the player reverses direction | >3 reversals mark ambiguity in path-finding |
| Pause frequency | Number of times the player stops for 2+ seconds | Metal or analysis phase: too many — too much |

## Interpreting Heatmaps

A death heatmap visualises the spatial distribution of death. Red zones = design failure or intended skill check.

### Death heatmap interpretation guide

| Pattern | Likely cause | Action |
|---|---|---|
| One tight red cluster at an exit | Enemy at door opening; alarm blind spot | Move 1 second of safe time into the room |
| Uniform red across level | The level is too hard | Reduce density or enemies health max |
| Spotless sections with no death | Player cannot die there; boring | Short fix mentioned |
| Red at final room over 40% | boss fight harsh but too high | Adjust the boss's phase 1 openings |
| Red only at full platform sections | Movement under-developed | Mark edges, slower moving hazards |

## Setting Up Telemetry

### Minimum Viable Telemetry per Level

System needed before playing any level after its first pass:

1. Level start and completion events (timestamp).
2. Death location (X, Y, Z) per death.
3. Resources used pre-death (health, ammo, mana).
4. Reserved path positions (2-second sample).
5. Kill count per enemy type.

### Analysis workflow

1. **Collect** minimal data from 5 core playtest runs.
2. **Visualize** as heatmap overlay on the minimap.
3. **Identify** two sections with highest death/to-ressurection ratio.
4. **Adjust** one variable at a time (enemy count, HP, weapon spacing).
5. **Retest** with same pool, measure delta.
6. **Flag** check for improvement or emergence of new problem.

## Final note

All measurements are compared to the player being good and the skill is correct, not to the test deck. Only after establishing that the system is correctly set up, iterate.