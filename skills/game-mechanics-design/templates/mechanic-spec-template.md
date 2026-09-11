# Mechanic Spec Template

Copy this file per mechanic. Delete this guidance block after filling it in.
The companion guide is `../references/mechanics-documentation.md`; the
machine-checkable contract is `../schemas/mechanic-spec.schema.json`. Target
one page of content; split into a parent spec plus children if it will not
fit.

```markdown
---
name: <hyphenated-mechanic-name>
version: 0.1
status: draft            # draft | ready-for-review | approved | in-development | live | deprecated
owner: <one accountable person or team>
last-updated: YYYY-MM-DD
related: [<other-spec-names>, <gdd-sections>]
---

## Summary
One sentence: what the player does, and what it produces. Example:
"Player marks a target; the next attack within 5 s homes to it and deals
bonus damage from behind."

## Inputs
What the mechanic reads at the moment it runs — player state, world state,
held items, timing. List explicitly; implicit inputs cause cross-mechanic
incidents.

## Rules
1. <Rule one — testable, no vague quantifiers.>
2. <Rule two.>
3. <Rule three.>
(Number every rule; QA turns each into test cases. If a rule needs another
document to be understood, inline it or split the mechanic.)

## Parameters
| name | default | range | owner |
| --- | --- | --- | --- |
| <param_one> | 5 | 2-10 | <owner> |
| <param_two> | 1.5s | 0.8-2.5s | <owner> |
(Every tunable number lives here — no magic constants in code or prose.)

## Interaction Map
Reads: <systems this mechanic reads from.>
Writes: <systems this mechanic changes.>
Triggered by: <events that start it.>
Interrupted by: <events that stop or override it.>
(Write "none" explicitly where a list is empty — empty is a testable claim.)

## Failure and Edge Cases
- At zero: <behavior>
- At max: <behavior>
- Simultaneous triggers: <behavior>
- Mid-animation/interrupted: <behavior>
- Tutorial/first-run save: <behavior>
(Undefined is not an answer; each line is a test case.)

## Player Experience Intent
One paragraph: what the player should feel, what decision this mechanic
exists to create, and what success looks like in observed behavior.

## Open Questions
- <Question> — owner: <name>, resolve by: <date>

## Playtest Plan
Question: "Will players <behavior> when <condition>?"
Method: <paper / greybox / build-with-telemetry>, n=<count>, by <date>.
```

Fill-in checklist before marking `ready-for-review`:

- [ ] Every rule testable as written; no "some/often/reasonable".
- [ ] Every parameter has default, range, owner.
- [ ] Interaction map lists both directions; empties stated as "none".
- [ ] Edge cases have stated behaviors, not ellipses.
- [ ] Open questions each have owner and deadline.
- [ ] Version bumped and last-updated touched.