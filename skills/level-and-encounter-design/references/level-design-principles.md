# Level Design Principles

## Overview

Level design translates abstract game mechanics into spatial, temporal, and sensory experiences. A well-designed level teaches the player how to play, guides them through a curated sequence of choices and challenges, and produces moments of satisfaction on a predictable rhythmic schedule. This reference covers the four foundational principles: readability, affordance, flow, and gating.

## Readability — The Player Must Understand What They See

A player should know within one second what a space offers, what threatens them, and where they can go. Readability is the level designer's primary responsibility. If the player has to stop moving to understand the space, the level has failed.

**Techniques for readability:**

- **Sightline framing:** Use geometry and forced perspective to present one decision at a time. A corridor that opens into a cavern should reveal the key element (exit, enemy, treasure) before the player enters. The beam of light falling on the exit door is not decoration; it is information.
- **Color signing** — Use a small palette of environmental colors for sign function. Warm colors (yellow, orange) signal interactables, goals, and forward progress. Cool colors (blue, purple) signal hazard, mystery, or non-interactive backdrop. Red signals immediate threat. Consistency across the level matters more than verisimilitude.
- **Negative space and clutter discipline** — A room filled with decoration is noise. Every element should either support gameplay (cover, path, hazard) or frame a view of something that does. The rule: if you cannot justify an object's presence in a sentence, remove it.
- **Height and silhouette** — platform games and 3D action games rely on character silhouette against backgrounds. A player must be able to read a platform's leading edge, a pit's boundary, and a climbable surface within a glance. Floor paint contrast, railings, and edge highlighting are not polish; they are readability features.
- **Arrow fallacy** — do not use literal arrows to show where to go. If the level needs an arrow, the space is not readable. Fix the space first.

## Affordance — The Player Should See What They Can Do

An affordance is a property of an object or space that communicates how to use it without instruction. A door handle says pull; a button says press. A game level communicates affordances through shape, animation, context, and contrast against the background.

### affordance types in level design

| Affordance type | How it works | Game example |
|---|---|---|
| Every-day physical | An object behaves like its real-world counterpart | A crate you pull to reach a ledge, like a step stool |
| Stylised interaction | The object's game-world shape reveals its function | A glowing crystal that activates when touched |
| Contrast-based | The interactive object differs visually from its surroundings | A climbable wall has brighter handholds than unclimbable wall |
| Environment | The space itself suggests a path | A gap between buildings narrows where the player should jump |

### Rules for affordance:

1. A player should see a climbable surface *before* they need to climb it. If the solution appears at the same time as the problem, the player has no time to plan and will resort to trial-and-error.
2. Affordances must look deliberate. If a pipe could be a decoration or an interaction, it will be ignored. Colour, shape, or animation must distinguish interactive from decorative.
3. Every interaction must have a clear, safe way to practice before the cost of failure is high. The first rope slide in a level should be over a pit the player can survive falling into, or over water.
4. Destroy any affordance that the player no longer uses. A climbable ledge behind a locked door is confusing. It is a path they cannot take; it signals the wrong thing.

## Flow — The Rhythm of Attention, Tension, and Release

Flow is the checkout sheet rhythm the level produces in the player. Good flow alternates activity types, does not ask the player to maintain peak attention for longer than they can, and builds to a climax before releasing.

### The flow cycle in a level:

| Phase | Player action | Sensory role |
|---|---|---|
| Orientation | Look, parse, plan | Low tension; player is reading the space |
| Approach | Move toward a goal | Medium-low tension; anticipation |  
| Engagement | Resolve encounters/challenge | High tension; peak player effort |
| Resolution | Complete, collect, breathe | Tension releases; reward moment |
| Transition | Move to the next space | Re-orient; reset for the next phase |

A level should have 3-7 of these cycles depending on length. A 10-minute beginner level should have 4-5. Each cycle should feel different from the last. A dungeon should not have the same corridor then room pattern repeated; cycles need to differ in enemy composition, spatial shape, or pacing.

### Flow killers

- **Long halls with enemies** — a corridor that is also a gunfight narrows skill expression. The best move is deterministic (stay in cover, line is not long enough to flank). Keep combat open and transitions brief.
- **Unskippable exposition** — a player cannot demonstrate skill during a 10-second animation triggered in a flow trough. The pause degrades to frustration.
- **Same-same encounters** — fighting the same enemy composition three times in a row flattens the difficulty curve. Change the mix, the space, or the objective.

## Gating — The Player Must Earn Forward Progress

Gating is the mechanism that controls when a player may proceed. The obstacle gate defines the challenge and the condition gate allows the player past it. Gating cheats difficulty, pacing, and teaching.

### Gate types:

| **Gate type** | How does it work? | Effect on design |
|---|---|---|
| Key-and-lock | Player must obtain an item to unlock | Teaches item use; pace depends on how far the keys is from the lock |
| Skill gate | Player must demonstrate an ability | Validates learned ability; place skill gate after teaching the skill |
| Combat gate | Player must defeat all enemies | Ensures baseline combat difficulty; used for milestone progression |
| Key-and-door | Player must have collected N keys Total that exit | Provides exploration incentive; requires metric plate |
| Scripted gate | Level triggers the next section by condition | Controls pacing rhythm; blocks progress on story trigger |

### Gating design rules:

- Teach before gate. The player should have used the required skill or item at least once before encountering a gate that demands it.
- When possible, show the gate before the player can open it — a locked door they walk past, a gap they see before they can double-jump. This sets up an anticipation that pays off later.
- Never gate with a knowledge test. If the player must remember something from 10 minutes ago without any reminder, the gate is unfair.
- Provide a soft reset on the gate. If the player reaches a combat gate and has no health, there should be a way to get resources without a load-screen-frustration loop.

## Section Line Budget Check

This reference covers methodology and principles, role: methodology/rubric.