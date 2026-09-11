# Worked Example: Cavern Run — Introductory Level

*Companion artifact to the worked example in SKILL.md section 06. This file extends the same scenario with full detail.*
This document is intended to be studied alongside SKILL.md by loading it whenever you need reference-level detail on a problem of similar complexity.

## Scenario

**Game:** Cavern Run — a 2D side-scrolling platform action game. The setting is an abandoned mining complex. The game teaches three mechanics sequentially in the first level: grappling hook, stealth (moving through shadows without being seen), and explosive barrels (carrying, placing, and detonating a barrel to destroy a blocked passage). The level must teach all three **without any tutorial text** and run approximately 10 minutes.

## Spatial Map

### Level layout (ASCII sketch)

```
[START] ---A--- [GRAPPLE POINT 1]
                 |   /
                 |  /  
                 [PIT]   ← fall here = safe drops to lower platform (soft reset)
                 |
                 B (first rest beat — shadow pool)
                 |
                [STEALTH CORRIDOR]
                 |  |
                Guard 1 → |   Guard 2 (patrolling)
                 |  |
                 C (shadow-moss refuge)
                 |
                [BARREL ROOM]  ← Collect barrel here
                 |
                 |
                (gauntlet shoot) — traps + guards
                 |
                 |
                 |
                 |
              [BROKEN BRIDGE — place barrel → boom → open path]
                 |
                 |
                 |
              [SHORT ASCENT → FINAL WALL → escape]
```

### Linear summary: six named zones

| Zone | ID | Shape | Purpose |
|---|---|---|---|
| Entry Cave | `z01-entry` | Flat 120px corridor, two ?-blocks teaching jumping | Pull the player right, scramble these first block contest. Silence the environment tense but neutral. |
| Grapple Bay | `z02-grapple` | Pit × 2, one rope endpoint above pit, both visible from entry. The grapple target is: a light-framed wall beyond the pit. Test: pull. | Teach **Grapple**. The first grapple point is a horizontal-tension test (grab rock, swing over pit). Pit below is 1-damage. |
| Shadow Pool | `z03-shadow` | Dark corner, ambience. Player landing in it loses all light. Reverb; then light shows: shadows are safety. Learn --- → the dark is safer than the light. | Teach **Stealth concept**: The shade in the deep is undetectable. Test: the guards walk in light and patrol the path. The shaded path is not covered. |
| Stealth Corridor | `z04-corridor` | Patrol of 2 guards moving left/right. Guarantee ahead lights and guard zones visible more than 5 seconds before the guard position. The shadow path is above the guard level, but it requires a grapple swing at the end. | Combine **Grapple + Stealth**: Use shadow to approach, then grapple to exit. |
| Barrel Room | `z05-barrel` | A room with three guarded bomb barrels. Two guards patrol. The barrel is explosive: pick it up, walk slowly. | Teach **Explosive Barrel** (carry-and-place, environment interaction). 
| Gauntlet Throw | Z06 gauntlet g  | The player carries barrel across a trap corridor. 2 traps: boulder roll (timed), press-type floor. At the end, a collapsed wall shaped like a doorframe: the barrel fits. Place and booby-trap. | Combine all: stealth past guards? grapple out of danger? barrel as final. |
| Final ascent | Z07 exit | A small climb; nothing attacks. The exit door opens titled cinematic. player slides down outside. | Payoff: scenic look-back. |

## Beat-by-Beat Sequence (timed)

### = Timings are approximate for a first-time player. This is "core walk" — not speedrun. =

| Second | Location | Player does | Mechanical lesson | Notes |
|---|---|---|---|---|
| 0-15 | Entry cave | Walk right. Jump off first rock. Hit brick block? In the ?-block is a coin. | Walk, jump/Jump-things above you. | No enemy yet. Only ground. |
| 15-25 | Entry, second half | A single harmless bat flows left to right: crossing the path. | Jump over / walk past. | First creature. Non-lethal. |
| 25-40 | Edge of Grappling Bay | The player reaches a pit that is 2.5 blocks wide, which is just jumpable but they land. | This pit is teaches _ go to want more range. | On the other side, the rope/ mechanism is rendered and stationary. The player can read "this moves"  
| 40-55 | Button hook trial | The player grapples to the other side for the first time. | Grapple action: into a reaction that brings you across?  
| -- death recovery | Pit under Grappling Bay 1 | A pit that leaves the player on 1HP. This does not kill the player a second time; it teaches safe. They come back | Pitfall = 1 damage, respawn on half-second. |
| 55-85 | Grapple Sequence Continued | Two more grapple points — each requiring timing a swing over a short gap. The second has a small hazard (drips mis-approximation). | The speed constraint makes the player edge-case with grapple. |
| 85-100 | The drop into shadow pool | The player drops through a soft fall into a dark pool. | Orientation | Entrance to stealth --- no enemies in the pool. The player is safe but the atmosphere says those are not safe. |
| 100-130 | Stealth corridor intro | One guard patrolling left/right. The guard has a light beam that sweeps. The shadow pool is at 1/3 of the corridor length. The guard cannot see the player if they are crouching in the pool. | The player learns that the dark is safe. | The guard cycles: 1: look right /or left (shines full). The shadow spot is 2-block wide. Pass. |  
| 130-160 | Stealth corridor — 2 guards | Both guards, time synchronization: one moves one direction, one moves the other. The player-time threat for any player: wait + move between pools. | The player now alternates between shadow patches. | This is about timing. The player may die once or twice. Every death they spawn at the start of the corridor. |
| 160-185 | Barrel room reveal | Guard 1: in the center. Two barrels. Guard. Player needs to carry a barrel, but if carrying the player is slower. | The player is taught: the barrel can be used as a tool. | The guard is a armored enemy. No kill by typical hit? The barrel explosion kills the guard. |
| 185-220 | Barrel craft/combat | Player learns: barrel explosion vs enemy, barrel moved to gate. | | |
| 220-260 | Barrel gauntlet (begin) | The player must carry the barrel through a gauntlet corridor.  | **Combination:**  hold barrel. | The player may decide to set down barrel to grapple up to skip one trap. First deck of teach. |
| 260-300 | Bridge destruction | Place barrel → fuse → boom → bridge solved.    | Full-cycle use | |
| 300-330 | Final climb + exit | Platforms + crystals. The player climbs to exit. | No challenge. Wind-down. | |

## Encounter Design

### Grapple Introduction (z02)
**Pattern:** Gauntlet variant — wall-to-wall grapple.
- **Enemies:** none.
- **Threat:** pitfall (1 damage).
- **Structure:** Three grapple points (stepping stone difficulty: short horizontal, medium swing, high-level with fall.
- **Skill test barrier:** must use grapple mid-air twice consecutively in the third.

### Stealth Corridor (z04)
**Type:** Gauntlet (sneak).
- **Enemies:** 1-2 guache Guards (cannot be killed, alerted triggers fail).
- **Threat:</b> detection, reset to start.
- **Structure:** 5 shadow pool covers, 1 guard patrol per pool. Paired drill.
- **Fail condition:** alerted guard shout → combat too full for the player? (low damage but can't beat them). The player respawns on entry.

### Barrel handling zone (z05)
| Training pattern | One |
|---|---|
| Type of encounter: arena | |
| Enemies: 2 guard-level guards + 1 barrel giant? | |
| Threat: medium (guards strong) | |
| Structure: one barrel in the room writ large. The player must use the barrel. | |

### Gauntlet + barrel escort (z06)
**Pattern:** gauntlet with pinch.
- **Enemies:** 2, but barrel required.
- **Failure:** barrel hits damage → re-carried. Elbow damage.
- **Exit:** broken bridge.

### Final climb (z07)
**Pattern:** environment, exit.
- **Enemies:** none.

## Difficulty Curve

```

Intensity
10 ●
9  ●
8  ●  ●   ●
7●  ●  ●    ●
6●      ●    ●   ●
5●        ●      ●
4●               ●
3●               ●
2●   rest   rest   rest
1●────┬────┬────┬────┬────┬────┬
   1  2  3  4  5  6  7  8  9  10
                minutes
```

- **Minutes 0-2:** low. Four jumps, walking, getting used to the controls.
- **Minutes 2-4:** Corridor/ platforms (medium). Rest: shadow pool.
- **Minutes 4-5:** Stealth (medium climax): 2 guards timing challenge. Rest: corridor end.
- **Minutes 5-6:** Barrel (define pick up, threat, enemy count). Rest: short.
- **Minutes 6-8:** Gauntlet carrying barrel. Medium. Rest: end of bridge — short.
- **Minutes 8-9:** Bridge destruction satisfaction. Final climb: low.
- **Minute ~9:** The sequence 1-3 above repeats with new mechanic adding gate.

## Teach

### Grapple Teaching Sequence:

1. **Environmental:** The first grapple point is visible (a large hook) while the player is still standing on safe ground. They have time to orient.
2. **Use Prompt:** The hook is directly over the first gap. The player has to: press a button to grapple. Success. They see the rope swing across.
3. **Repetition w. Variable:** The next point is a longer swing. Then a higher one.
4. **Combination:** In the stealth corridor, the player must grapple out of shadow onto a hidden point, while guard is under them.  

### Stealth Teaching Sequence:

1. **Soft entry:** The player's last point of safety (shadow pool) is full visual change in atmospheric (lighting shift, particle density). The pool has no enemy; the player can just stand in darkness.
2. **Press observation:** The guard patrol has a visible highlighted path (lamp line). The player sees: in dark — guard's path not match.
3. **First execution:** Guard faces away. The player gets from first shadow point to second during guard turn.
4. **Combination (guard + grapple):** The player must wait until guard times, grapple to lead while guard is still turning.

### Explosive Barrel Teaching Sequence:

1. **Object recognition:** barrel has specific shape, glowing nodes (like powder). The player touches: pick up. Prompt to use action.
2. **Functional test:** barrel placed near the Guard → explosion two seconds → guard die.
3. **The path of barrel tear long corridor:** the tear across, avoid wall shots.
4. **Final use:** barrel at the bridge will explode, drop bridge and door opening. Player learns: barrel can unlock paths by damage.

## Telemetry goals

- Death per section: guess <2 in stealth, <1 in barrel zone.
- Time in stealth zone: 20-30 seconds normal.
- completion rate: >85% for first version.

## Post-iteration

After first playtest, the early drops were more common in the gauntlet than intended: 60% dead in the fire trap but all deaths there. Moved one scorch to the easier side: 25% dead then. Good.