# Game Design Doc Template

Section template for a game design document. A GDD is not a novel — it is
the smallest document that lets a stranger on the team make a correct
decision without asking. Write each section to be readable independently;
most readers arrive by link, not by cover page. Keep the whole doc under
30 pages by moving mechanic detail into per-mechanic spec files
(`mechanic-spec-template.md`) and linking them.

Per-section guidance first, skeleton at the bottom.

## Section guidance

**Elevator pitch.** Two sentences: player fantasy plus the differentiating
mechanic. If the second sentence could describe three other games, the
differentiator is not on the page yet.

**Experience goals.** Three to five statements of what the player should
feel and be able to do, written as observable targets ("players narrate
their heist plan before executing it"), not adjectives ("exciting"). Every
later design argument is settled against this section; write it first and
revise it rarely.

**Audience and platform.** Who plays this (genre familiarity, session
length, input), and on what. Session length drives loop design more than
genre does; state it here.

**Core loop.** The one-sentence loop with its decision point, plus the
30-minute session arc (open, rise, peak, bank). See
`../references/core-loop-design.md` for the method. If the loop needs a
paragraph to explain, it is two loops.

**Pillars.** Three to four pillars — short names for the qualities the
game must protect (e.g., "every death teaches," "the city remembers").
Pillars are used as review criteria; name them memorably and keep them to
a handful.

**Mechanics overview.** One table: mechanic name, family (action/system/
progression/social), one-line description, link to its mechanic spec. The
GDD holds the map, not the detail; the detail lives in the spec files.

**Content architecture.** What the game is made of and how much: regions,
act structure, enemy families, item tiers. This is where scope becomes
visible; keep the unit counts honest and dated.

**Progression and economy summary.** Which currencies exist, what they
buy, and the intended pacing (time-to-first-upgrade, session count to
first completion). Deep modeling belongs to the economy discipline; the
GDD records the shape and the promises.

**UI and controls summary.** Input map, the verbs' controls, the key
screens. One page maximum; the mechanics' feel lives in their specs.

**Risks and open questions.** Top design risks with the test planned for
each, plus dated open questions with owners. This section is the agenda
for every design review; if it is empty, the GDD is being maintained as
documentation, not as a tool.

**Milestones and playtest plan.** Which questions get answered by which
prototype at which milestone, and who tests. Review cadence included.

## GDD skeleton

```markdown
---
name: <game-name-gdd>
version: 0.1
status: draft
owner: <design-lead>
last-updated: YYYY-MM-DD
mechanic_specs: [<linked spec files>]
---

# <Game Name> — Design Document

## 1. Elevator Pitch
<Fantasy in one sentence. Differentiating mechanic in the next.>

## 2. Experience Goals
1. <Observable, feel-oriented goal>
2. <Goal>
3. <Goal>

## 3. Audience and Platform
<Who plays; genre familiarity; session length; platform and input.>

## 4. Core Loop
<One-sentence loop with decision point.>
<30-minute session arc: open → rise → peak → bank.>

## 5. Design Pillars
1. <Pillar — memorable name, one-line meaning>
2. <Pillar>
3. <Pillar>

## 6. Mechanics Overview
| Mechanic | Family | One-line description | Spec |
| --- | --- | --- | --- |
| <name> | <action/system/progression/social> | <line> | <link> |

## 7. Content Architecture
<What the game is made of, with unit counts and the date they were counted.>

## 8. Progression and Economy Summary
<Currencies; what they buy; intended pacing numbers.>

## 9. UI and Controls Summary
<Input map; verb controls; key screens.>

## 10. Risks and Open Questions
| Risk / Question | Test planned | Owner | By |
| --- | --- | --- | --- |
| <one-line> | <how it gets answered> | <who> | <date> |

## 11. Milestones and Playtest Plan
<Milestone → question answered → who tests → date.>

## Appendix A — Glossary
<Term — definition. Only terms the team actually uses.>
```

Maintenance rules: the GDD changes by revision at design review, not by
silent edit; every version bump updates Risks and the mechanics table;
superseded sections move to an appendix dated by version rather than
vanishing — decisions need ghosts, or they get relitigated.