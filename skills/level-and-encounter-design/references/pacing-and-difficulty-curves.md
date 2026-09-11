# Pacing and Difficulty Curves

## Overview

Pacing is the manipulation of time, tension, and variety across a level or game. Difficulty curves plot challenge intensity over player progression. A well-tuned curve keeps the player within their competence-zone without plateau or spike. This reference covers how to design both.

## The Shape of a Difficulty Curve

Difficulty curves have consistent shape across games of every genre. The classic curve alternates ramp-plateau-ramp, with rest beats between peaks. The first-time player should feel challenged but not overwhelmed; the veteran should feel rewarded for mastery.

### Lesson from the masters:

- **Super Mario 1-1** — the difficulty does not increase by adding more enemies. It increases by adding fewer safety pauses between decisions, and by placing hazards in a pattern that the player must now time their movement through instead of walking straight through.
- **Halo: Combat Evolved** — the first 30 seconds have no enemies at all. The entire first encounter is a solo fight against Grunts, and Elites are introduced with a single Elite in a space the player can retreat from. The final encounter has 4 Elites, Hunters, and Jackals in a small room.
- **Half-Life 2** — the airboat sequence: the difficulty curve is a series of 3-4-minute segments with increasing intensity (a bridge, a bridge under attack, a bridge collapsing) followed by a calm moment in a safe house. Walk speed is the rest beat.

## Measuring Difficulty

| **Method** | **What it measures** | **How to use it** |
|---|---|---|
| Player death rate (DPM) | Deaths per minute per player | Baseline; if deaths > 0.5 per minute at the start of a level, recalibrate |
| Time-to-cover ratio | Seconds in cover vs seconds in movement | In cover >50% of the level means the encounters are riskier than necessary |
| Health attrition | Player health consumed at supply-spawn used | If the player consumes all health available, the difficulty peaks too high |
| Pause frequency | Player stops for >2 seconds without threat | Indicates confusion or analysis pause — both break flow |

## Building a Difficulty Curve

### Step 1 — Establish the baseline

The first encounter must be **trivially safe**. A single enemy that doesn't converge, a wide safe zone, time to learn controls. The player needs to know what "easy" feels like to know that the later fight is "medium."

### Step 2 — Map your ramp

Divide the level into quarters of time. Each quarter should feel noticeably harder than the last:

| Quarter | Feeling | Player expectations |
|---|---|---|
| 1 | Exploration, low risk | Threats are scarce; the player feels competent |
| 2 | Increasing danger | 2x threat density; enemies are aware of the player |
| 3 | The player is tested | Enemies combo; new enemy types; resources are scarce |
| 4 | Climax, all-in | Maximum challenge; final boss/escape uses all skills |

### Step 3 — Place rest beats

After every 2-3 minutes of increasing intensity, insert a rest beat: a safe room, an item cache, a story beat, an open space without enemies, a view point. The rest beat should be visible from the end of the hard sequence so the player knows the stress is temporary.

**Rest beat types:**
- Safe zone — no enemies, refill checkpoint.
- Story beat — dialogue, note, or diorama that does not need player input.
- Exploratory section — the player navigates a non-lethal puzzle or a simple space with multiple routes.
- Metroidvania-reset — the player sees a new ability-gated path, creating anticipation and planning the return.

### Step 4 — Design the climax

The final beat of the level must use every skill the level taught. No new mechanics in the final fight. The player must be able to say, before the fight: "I know how to win this. But it'll be hard". Doing this correctly is the climax design.

### Failure curves:

| **Failure pattern** | **Curve shape** | **Problem** |
|---|---|---|
| Flat line | No increases in difficulty | Player is bored by min 3 |
| Wall | Sharp jump after a low point | Player cannot proceed without skill-decay grinding |
| Sawtooth | Spikes, then falls below previous | Player optimizes for the spike and the rest is trivial |
| Diverging | Difficulty continues later after climax | Player has no rest; maxes out at fight-and-relief rhythm |
| Grim Elbow | Too difficult after first 10%, | The player who survives first moment is and from then everything is scaled to them; new failers remains underwhelmed |

## Designing Rest Beats — Why They Matter

The human attention span for continuous high-alert performance is roughly 5 minutes. After that, performance drops. Rest beats let the player:

1. Replenish health and resources (physical relief).
2. Let the cognitive load of the last encounter settle (mental relief).
3. Build emotional anticipation for the next encounter (positive tension).
4. Validate the previous combat's outcome (completion signal).

**The rest beat time formula:**

- Short rest: 15-30 seconds (single health pickup, short animation, quick dialogue).
- Medium rest: 30-90 seconds (small safe room, exploration choice, scavenger a corpse).
- Long rest: 2-5 minutes (safe hub, shop, save point, story sequence).

The average of a short + medium rest should be placed every 3-5 minutes of active play. A 10-minute level needs two rest beats.

## The Intensity Arc

Intensity is moment-to-moment engagement, not just difficulty. An argument that goes up to 10 then stays at 10 is a loud, not an arc. You need ebbs.

### Typical 10-minute intensity arc:

Minute   0-1: Welcome valley (very high — orientation, curiosity, low risk)
Minute  1-3: Ramp to combat (middle intensity, first encounter)
Minute  3-4: Rest beat
Minute  3-6: Medium high (second encounter, new enemy type)
Minute  5-7: Complex task (multi-type enemies, skill check)
Minute  7-8: Rest and preparation
Minute  8-10: Climax (all skills, high density)
Minute 10: Resolution and quiet

## Checklist

Before finalizing any level's difficulty curve:

- [ ] Is the first encounter easier than the last?
- [ ] Are there at least 2 rest beats in a 10-minute level?
- [ ] Will a player who never stops running die? (If yes, reduce density or increase rest.)
- [ ] Can a player take 3 damage without having to restart?
- [ ] Is the hardest encounter before the climax a warm-up for the climax?
- [ ] Does the final encounter re-ask about the skill taught in the tutorial?
- [ ] Do at least three elements of variety (enemy type, burial/firing, support type) used in the climax?
- [ ] Resource spawning: can the player walk into the climax with at least 70% of core resource?
- [ ] Would resetting from the end of the level be painful enough to need checkpoints?