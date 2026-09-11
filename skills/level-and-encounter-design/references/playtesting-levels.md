# Playtesting Levels

*Methodology.*

## Overview

Playtesting levels has a very different shape to playtesting individual mechanics. Level tests need to capture spatial navigation, pacing, difficulty comprehension, and environmental story. This reference covers level-specific protocols.

## What Level Playtesting Tests

| **Question** | **Method** | **Time cost** |
|---|---|---|
| Can the player find the path? | Silent observation, start-to-exit | session time |
| Does the intended path match the actual path? | Overlay path traces on minimap | post-session |
| Does the difficulty rise as expected? | Count deaths per segment | session |
| Are the teach beats effective? | Observe first exposure to each skill needed | session |
| Does the environmental story land? | Asked after play: name 3 things from the environment | post-session |
| Is the flow comfortable? | Video of the session, event rate from heart | post-session |

## Level Playtest Protocol — Structured

### Before the test:

1. Confirm the build has stable restart from the entry.
2. Install telemetry to capture path, death (both xyz), health per check.
3. Brief the tester: "This is level.. Play as normal. Just play and exit."
4. Restrain yourself — do not mention the mechanics involved. The player must learn them on their own.
5. Settle the player on difficulty: "It's a fair level, you can die but we'll respawn at once."

### Activity During Test:

| **Observation** | **Record** |
|---|---|
| Pauses of more than 5 seconds | time+position |
| Multiple attempts of the same jump/section | count, location |
| Player's explicit exclamation | verbatim |
| Player's mouse/facing: what direction they look at when entering a new room | direction vs intended path |

### After test — debriefing session

1. "Which section was the hardest for you?" (Note correlation with real difficulty.)
2. "Did you ever feel lost?" (Precision: when exactly.)
3. "What was the moment you enjoyed the most?" (Cross with death frequency.)
4. "What do you think was the goal of the level?" (Test comprehension of mission narrative.)
5. "Did you see any interesting details in the environment?"

Then, without the player present, mark:

- Player path on the map.
- Pause / re-entry points.
- Death points (colored over heatmap base).
- Intended path is different from the player — measure how.

## Iteration Discipline

When running a level test:

1. **One iteration per change.** You change, send new build, test again. 2 changes cannot be proven if the improvement is the first or the second.
2. **Check the major issue.** You find critical trip-hazard(?); fix exactly that and test.
3. **Three times per change.** Try three players with the same version to remove personal performance outlier. The marginal improvement design matters.
4. **Save the build.** If a change makes to worse, you need to revert without a question.

## Level Playtest Focus Areas

### Wayfinding

- Does the player leave the path and not feel lost?
- Do they see the goal? At entry, a sightline to goal or at least a big part of pathway?
- Which was the moment area where the player looks left/right and didn-t know which of both?

### Extended clearments

Check:
- participation progress: did they get a signal within seconds
- distance compression: can they walk the path?

### Range and fun

- Did the player produce any of these: smile, humming, energy increase after each combat? If not, the section was h not fun.  
- Did they laugh when a dangerous moment passed? That's the joy of mastery.
- Were they bored? Did they check their phone? Did they look away?

## Test the Silent Mechanic Teaching

Testing that the level teaches mechanics without tutorial text:

- **First exposure:** Does the player use the mechanic by the second exposure/physical invitation?
- **Deploy in true scenario:** If they fail the second time, it is a death or a learn?
- **Use in combination:** In the final encounter, do they use the mechanic more effectively if it's required?

Count rate of success vs failure per mechanic exposure. If failure rate is over 30% in the third (practiced) exposure, redesign the teaching beats.

## Minimum Sample Set

A level's confidence:

- **Level pass:** 5 testers = poor confidence of path.
- **Difficulty curve:** 15 = moderately.  
- **Everything combined:** 30+ for release candidate.

For the iteration loop: 3 testers per revisiting issue is fine.

## Notes from real playtesting

- **Players do not go left.** Entry semantics: if a player enters and 2 doors are equally visible, the one to the left is more frequently taken than the right, by a margin. But that means the one main path should be left, or make the right one more noticeable.
- **The player was will always run forward.** They rarely look behind them. place surprises behind the player. Don't place transitions behind them.
- **Dead ends need easy-to-recognize orchestration.** A dead end looks like a dead end? If it's just a blank wall, they'll go back. If there's a chest, they'll stay. **Always have a micro-reward at a dead end.
- **90% of players won't look up.** Not sure if in 3D, in 2D, they look up as more likely, but it still low. Plan for it.