# Encounter Design Patterns

*Pattern catalog.*

## Overview

An encounter is a contained unit of gameplay — a combat, a puzzle, a gauntlet, or a negotiation. Encounters form the building blocks of level pacing. This reference catalogs four fundamental encounter patterns, each with its anatomy, design rules, and failure modes.

## 1 — Arena

A closed space where enemies spawn or are present upon entry. The player cannot leave until conditions are met (all enemies dead, timer expired, or button pressed).

### Anatomy

1. **Door closes behind:** The player enters; the exit locks or spawns behind them.
2. **Reveal delay:** A brief pause before enemies to let the player evaluate the space.
3. **Enemy placement:** Ranged on high ground, melee in front, flanks on opposite sides.
4. **Resources:** Health, ammo, or cover items available at the start or after first core kill.
5. **Exit condition:** All enemies defeated, or a puzzle solved.

### Design rules

- The arena must have at least 3 pieces of cover that block line-of-sight from at least 2 directions.
- A new enemy type should not appear first in an arena. The player should have met each type in a corridor/hallway first.
- Waves (if used) must escalate: wave 1 introduces the enemy type, wave 2 increases count, wave 3 introduces a new type or new behavior.
- After the arena, the player needs a physical exit that feels earned (doors opening, cutscene, animation).
- If the player can backtrack after the fight, include a shortcut door they unlock from inside so they do not need to cross the arena again.

### Failure modes

| **Failure** | **Signal** | **Fix** |
|---|---|---|
| Arena too small for the number of ranged enemies | Player dies without visible cover | Increase room diameter by 20%. Add a central pillar. |
| Arena too large | Player spends most of the time navigating, not fighting | Cut arena size by 25% or add more enemies on the path. |
| No cover-variation | Player camps the same Pillar for all waves | Add destructible cover that forces repositioning. |
| Ambush read-notice | Player never sees one of the exits when entering | Add one shot seeds (a visible enemy on the balcony) before the door closes. |

## 2 — Gauntlet

The player must move through a dangerous corridor or sequence while in combat or under time pressure. Gauntlets are the most kinetic encounter type — the pause is built into the movement.

### Anatomy

- **Corridor width:** The space is 2-4 player-widths across — wide enough to evade, narrow enough that enemies are unavoidable.
- **Threat density:** One threat per 3-5 seconds of run time. If the gauntlet is 30 seconds long, the player should encounter 6-10 threats.
- **Exit staging:** The end of the gauntlet is either a locked door that opens when the gauntlet ends, or a pit-climb-ladder.
- **Fail state:** The player is returned to the gauntlet's entry checkpoint, but the gauntlet is then in its cleared or fastest state.

### Design rules

- All threats must be visible from the start position. No blind threat.
- Repetition pattern: first threat is simple (floor fire), second is same with time pressure (floor fire + closing door behind), third adds a new axis (enemy shooting from above while floor fire exists).
- The player should always have at least two valid moves.
- Gauntlets without a checkpoint are 'time/learn wall' and should not be placed in the first half of a game.
- The player must know when the fight ends — a clear-terminal space (large safe room or checkpoint) visible from at least 10 metres before.

### Common mistakes

- No reward at the end: defeating a gauntlet requires emotional payoff — a vista, a new weapon, a cutscene.
- Ambush in the middle: if the player expects a clear run and is attacked at 30 seconds, they will learn to slow crawl. Better to mark.
- Gauntlet length exceeds 1.5 minutes of sprint: the run becomes a trudge.

## 3 — Puzzle-Lock

The player must solve a spatial, logic, or item-puzzle to open the path forward. The puzzle-lock is the only pattern where combat is secondary or absent.

### Anatomy

- **Lock:** Some barrier — a door, a force field, an energy bridge — that cannot be crossed by skill alone.
- **Key:** The solution, which can be a physical object, a combination of actions, or a timing sequence.
- **Distraction:** The puzzle should not be harder than the skill check the player just passed. A difficult combat before a simple puzzle creates balance; a simple combat for a complex puzzle frustrates.
- **Solution space:** There must be more than one way to solve or multiple spaces to test hypothesis. The player should be able to incorrect several times without resetting.

### Design rules

- The player must be able to see the lock before they can see the key points. Anticipation.
- At least one test: the player can see all elements of the puzzle from within the puzzle space.
- Failure does not kill the player — it returns them to the puzzle's starting state, but the world must cooperate each time quickly.
- If the puzzle has a combat element, the combat must not be avoidable by solving the puzzle. Not optional fights still.
- The puzzle must be solvable within 45 seconds by a player who understands its rules. Over 2 minutes is a plateau break and should be avoided in a tutorial level.

### Common forms

- **Rotary connection:** The player aligns elements on axes.
- **Weight system:** The player creates a bridge with objects in a sequence.
- **Environmental trigger:** Player stands on a pressure plate, companion activates a thing across the room, player runs to the door.
- **Light/path:** Refraction, reflection, or dark-echo.

## 4 — Boss Structure

Boss encounters are the climax. The player uses all learned skills to fight a single, powerful enemy that may evolve during the fight over multiple stages or patterns.

### Anatomy

- **Room:** spacious enough to manoeuvre, ring close enough to allow an engage-disengage rhythm. Typically 2-4x a standard arena.
- **Boss:** Single entity, move set with 3-5 distinct attacks. Each attack has a telegraph (wind-up animation or light/audio cue) of 0.5–1.0 seconds.
- **Phases:** Boss changes behavior at health thresholds (if it's a boss) — new attacks, new speed, new adds.
- **Arena change:** At each transition, the arena may also change: floor moves, hazards appear, advantage shifts.
- **Recovery zone:** After each phase the player gets 3-5 seconds to heal, reposition and plan.

### Design rules

- The player must be exposed to at least one instance of each boss attack BEFORE the context in which it is dangerous.
- Minions or adds must not appear after the boss's third-of-life. The final phase is pure player-vs-boss.
- Boss health should not be the only source of difficulty. If the boss is a bullet sponge that takes 10 minutes to whittle down, the encounter fails.
- The player must visually see their progress on the boss: boss armor cracks, the boss moves slower, boss changes form.
- Idle indicates: the boss should have mid/low activity phase (50% of battle) and storms activity phase (50%). Both phases at the control of the player.
- If the player dies and reset, the boss should have no puzzle-gate: it should be the boss arena and nothing else.
- Add a signal preview 1 minute before the boss space — a corpse with the right weapon, a note warning, a visual that the room ahead is special.

### Classic variants

| Variant | Description | Examples |
|---|---|---|
| Classic Boss | Single enemy with 3-phase pattern | Dark Souls Belfry Gargoyles |
| Extreme | Adds add spawn, more adding; last phase is wide | Hades |
| Puzzle Boss | The boss cannot be damaged by the normal weapon; use environment | Shadow of the Colossus |
| Reactive boss | Boss changes based on the player's behavior | Demon's Soul's Phalanx |