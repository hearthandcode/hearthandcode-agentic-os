# Spatial Composition

*Methodology.*

## Overview

Spatial composition is the arrangement of geometry, sightlines, paths, and landmarks to produce a level that is navigable, interesting, and purposeful. The same rooms can be arranged to produce confusion or flow. This reference gives four concerns: sightlines, landmarks, loops, and chokepoints.

## Sightlines

A sightline is the line-of-sight a player has from a given position. Controlling sightlines controls *when and where* the player receives information and risk.

### Why sightlines matter

- Long sightlines in enemy-free space produce awe, anticipation, and planning.
- Long sightlines in combat produce vulnerability.
- Short sightlines produce surprise and uncertainty, but also frustration if over-used.
- The ratio of long-to-short sightlines in a level directly affects the level's mood.

### Sightline types

| **Type** | **Distance** | **Player feeling** |
|---|---|---|
| Vistas | >100 units (1st person), full room (top-down) | awe, orientation, goal sighting |
| Targeting | Top-down-card's combat distance | appropriate for combat decision |
| corridor | 2-3s of run time ahead | Forward progress tunnel vision |
| engage | Trigger or elevator | anticipation + pressure |
| block | Instant, <1s of distance | disoriented only for a moment, then path decision |

**Rule:** every major path junction should have a vista line to at least one destination. The player should never have to choose a path without seeing what it contains.

### Building sightlines

1. Mark every player position where they must decide which direction to go.
2. For each, sightline from that position to a significant element (door, tower, landmark, threat).
3. If no sightline exists, the player is asked to guess. Add a landmark or shorten the corridor length until a sightline exists.
4. Over long distances, add secondary landmarks to ensure the path signals do not disappear.

## Landmarks

A landmark is an object or geometry that is visible from a distance, is unique in silhouette and colour, and has a known role (start position, exit, treasure, boss). Landmarks are the north star of spatial navigation.

### Types of landmarks

- **Orientation landmark** — visible from the entire level, used to reorient after backtracking. Player should see it one: the entrance tower, the mountain peak above.
- **Goal landmark** — what the player is moving towards. Seen from the previous sightline but not earlier, to hint general direction.
- **Beat indicator** — a small landmark spaced every 10-20 seconds of run time; marks progression signposts.
- **Warp/teleport** — a landmark that is also a destination; the player character goes there.

### Landmark design rules

- A landmark should be visually distinct from geometry more than 40% of its silhouette should be against the sky or a clear background.
- Avoid identical landmark types in the same level. Two spires in a archipelago confuse hierarchy.
- Every landmark should become more visible as the player approaches it, not less.
- No landmark should be false — if a player can see a series of lights and it's not the exit, the signpost is lying.

## Loops

A loop is a path that connects two points in the level so the player returns to an earlier location from a different direction. Loops reduce backtracking time that is not disadvantage, and builds spatial comprehension.

### Loop benefits

1. **Enables tactical gameplay** — the player can retreat and reenter from a different angle.
2. **Produces spatial learning** — "I came in this path, and I'm out here is that that I saw. The level is connected." You skip the spatial learning faster.
3. **Reduces backtracking** — players feel that the level is large but actually they is small.
4. **Allows second-path** — the same space facilitates two different gameplay contexts.

### Loop types

| **Loop Type** | **Description** | **Example** |
|---|---|---|
| Return loop | Player completes a circuit; the last hallway opens into the first area | The first room of the dungeon revisit after turning a valve opens a door |
| Undo loop | Player activates a switch; a short elevator/teleporter brings them back to the still intact path | The bridge gate from behind after crossing |
| Hub loop | A central space is revisited from several sides; the center is a junction | Central plaza in a castle level |
| Overlook loop | An area overlooks the starting point. The player feels they have progress | Dark Souls Undead Burg: the bridge overlook back |

**Rule:** In a 10-minute level, have at least one loop. In a 30-minute level, have 2-4 loops. Without loops, the player perceives the level as a straight corridor.

## Chokepoints

A chokepoint is a point where a player must pass through a narrow passage — a door, a bridge, a tunnel — and has limited ability to manoeuvre or retreat. Chokepoints create intensity, make encounter placement predictable, and create pacing.

### Chokepoint types, good and bad

**Good chokepoints:**
- The narrow passage is brief (1-3 seconds of crossing time).
- The player can see the exit before entering.
- There is a alternate path to the same outcome (the gate is one pass among many).
- The chokepoint funnels players into a designed encounter space (gate to an arena).

**Bad chokepoints:**
- The chokepoint is the encounter (the player fights *in* the corridor).
- The chokepoint is a room check (do you have the resource to cross?).
- The player cannot see the far side.
- The chokepoint is the only path deeper, but requires a key no one told them about.

### Chokepoint safety rules

- A corridor designed as a combat corridor must be at least 3 player widths wide. Any less is a pure chokepoint channel — combat there is a box.
- Any chokepoint that restacks the player a lot has a 30-second death check (short auto-save before the chokepoint entry).
- The player must be able to successfully guess whether a chokepoint is a corridor or good about 70% of the time. If they never want to enter one, the space is defined predictable with traps.

## Composition Checklist

- [ ] Can I draw, from the entry, at least 3 major paths or sightlines?
- [ ] Does each major path have a landmark visible from the junction?
- [ ] Are there at least 2 rest spaces with loops?  
- [ ] Will the player return to any space they've seen before from a different route?
- [ ] Can a player retreat from any encounter without double-backing through 30 seconds of neutral space?
- [ ] Are chokepoints at least 3 player-widths and not where the only combat is?
- [ ] Is there one sightline that gives the player **the goal** at the start of the level?
- [ ] Would a player that run straight through the level ignoring combat find themselves stuck? (if yes, remove a chokepoint.)