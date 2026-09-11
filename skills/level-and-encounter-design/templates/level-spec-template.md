# Level Specification Template

Use this template to specify a single level before building. Fill every section to the required level of detail. The schema at `schemas/level-spec.schema.json` validates the YAML block at the top.

```yaml
# Level spec YAML header
name:                  # Unique level identifier
game:                  # Parent game/project
type:                  # tutorial, combat, puzzle, boss, hybrid
intended_duration:     # Minutes or session count
player_count:          # 1, 2-coop, 4-player
skills_taught:         # Comma-separated list of mechanics taught this level
difficulty_target:     # beginner, intermediate, advanced
```

## Elevator Pitch

One sentence: what is this level about, and what makes it special?

## Core Loops

What does the player do in 5-second, 30-second, and 5-minute loops?

| Loop scale | Activity | Teaching function |
|---|---|---|
| 5-second |  |  |
| 30-second |  |  |
| 5-minute |  |  |

## Spatial Summary

Diagram reference or textual description of the level's shape. Minimum elements:

- **Entry / Spawn point**
- **3-6 major zones** (named, 1-sentence each)
- **Gates** (key, skill, combat, puzzle)
- **Loops** (backtrack connections)
- **Chokepoints** (each with safety plan)

### Key Metrics per Zone

| Zone | Area | Threat density | Typical combat time | Rest beat |
|---|---|---|---|---|
| 1 |  |  |  |  |
| 2 |  |  |  |  |
| ... |  |  |  |  |

## Encounter List

| Encounter ID | Pattern type | Enemies | Room size | Special mechanics |
|---|---|---|---|---|
|  | arena/gauntlet/puzzle-lock/boss |  |  |  |
|  |  |  |  |  |

## Difficulty Curve

Plot the broad shape: low-medium-high-climax-rest pattern across the level. Sketch or describe the arc.

## Teach Sequence

How does the level teach each new mechanic, without text? Diagram by:

1. **First exposure:** a safe moment where the mechanic is shown.
2. **First use:** the player runs the mechanic at low pressure.
3. **Combined use:** the mechanic required together with previously learned.
4. **Mastered:** mechanic used as part of a more complex task.

## Environmental Story Notes

What is the story the environment tells? Three key dioramas or details.

## Telemetry Gating

Which metrics matter for this level specifically? (heatmap segments, death per enemy type, rest utilisation.)