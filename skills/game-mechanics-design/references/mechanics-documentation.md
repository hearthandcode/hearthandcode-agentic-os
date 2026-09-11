# Mechanics Documentation

A template guide for writing mechanic specifications that other people can
build, test, or review from — without a meeting. The unit of documentation
is the **mechanic spec**: one page of frontmatter plus focused sections.
The companion template is `../templates/mechanic-spec-template.md` and its
machine-checkable twin is `../schemas/mechanic-spec.schema.json`.

## 1. The bar a spec must clear

A mechanic spec is buildable when a competent implementer can:

- state what the mechanic does and does not cover (boundaries),
- implement the rules without asking a designer what a word means,
- find the numbers or the plan for producing them,
- know how the mechanic will be judged, and by what test.

If any of those four fail, the document is a design sketch, not a spec.
Specs are also read by QA (to write test plans), by producers (to estimate),
and by future-you (to remember why). Write for all four readers.

## 2. Frontmatter fields

Keep frontmatter small and factual — everything else lives in sections.

- **name:** the mechanic's proper name, hyphenated if multi-word. Names are
  load-bearing: the spec, tasks, test plans, and telemetry will all use it.
- **version:** increments on every content change. If version numbers drift
  from the text, nothing else in the doc is trustworthy.
- **status:** one of `draft | ready-for-review | approved | in-development
  | live | deprecated`. Reviewers trust status; make status changes loud.
- **owner:** one accountable name or role. Committees cannot own a mechanic.
- **last-updated:** ISO date. Update it whenever version increments.
- **related:** pointers to the systems this mechanic touches (other spec
  names, GDD sections). Related links make implicit dependencies explicit.

## 3. Section-by-section guidance

**Inputs.** What the player and the systems provide when the mechanic runs.
Be concrete: "the held tool, the target tile, the player's current stamina."
Inputs you cannot name are usually a second mechanic wearing a trench coat.

**Rules.** Numbered, testable statements of the mechanic's logic. Each rule
must be independently falsifiable — QA should be able to turn any rule into
a test case without interpretation. Prefer "gain 1 charge per kill, max 3"
over "gains charges from combat." Ban any word you would not accept in a
test case: some, often, near, reasonable, about.

**Parameters.** Every tunable number in one table: name, default, range,
owner. A number without a range is untested; a table without owners is
unmaintained. Parameters are the contract between design and balance work —
when a later tuning pass changes a value, it changes it here, with a note.

**Interaction map.** Two short lists: what this mechanic touches (systems
it reads or writes), and what touches it (systems that alter its inputs).
This is the section that prevents the "nobody knew the shield regen
interacted with the difficulty curve" incident. If the list is empty, say
so explicitly — empty is a claim, and a testable one.

**Failure and edge cases.** What happens at zero, at max, at negative, at
simultaneous, mid-animation, offline, in a tutorial save. Each edge case
needs a stated behavior; "undefined" is a bug in the spec, not an answer.
Edge cases discovered during implementation get added here, not to a chat.

**Player experience intent.** One paragraph: what the player should feel and
what decisions the mechanic should produce. This is the section reviewers
use to judge "correct but wrong" implementations, and the section that
survives when the numbers change.

**Open questions.** Explicit unknowns with an owner and a deadline. An open
question without a deadline is a decision made by delay.

**Playtest plan.** What will be observed, with how many players, by when.
Even a paper prototype needs this line; it is what converts the spec from
opinion to experiment. `../references/playtesting-methods.md` governs the
method.

## 4. The one-page rule and when to break it

Aim for one page of content (roughly 40-60 lines). The one-page constraint
is a forcing function: if the rules section cannot fit, the mechanic is
usually two mechanics, and splitting them is the real work. When a spec
must exceed a page — sprawling systems, platform-dependent rules — split
into a parent spec that defines the shared rules and child specs for each
variant, linked through `related`.

## 5. Spec hygiene checklist

- Every rule is testable as written (a QA reader can make a test case).
- Every parameter has default, range, and owner.
- Every edge case named in review has been merged into the doc, or argued
  down in writing.
- The version incremented and the date updated on this edit.
- No rule references another document for its core meaning ("see the combat
  rework" is not a rule).
- No dead content: parameters removed from the design are removed from the
  table, not left to rot.
- A reader who has never heard of the project can say what the mechanic
  does after 90 seconds with the doc.

## 6. Common documentation failures

- **The noun soup:** the spec names 9 systems without defining any.
  Fix: define terms in a glossary block at the top of Rules, or rename.
- **The vibes rule:** "feels weighty and impactful." Fix: translate to
  observable targets (hit-stop ms, knockback distance) or move to the
  experience-intent paragraph where it can be judged rather than enforced.
- **The hidden parameter:** numbers that live only in code. Fix: every
  tunable number appears in Parameters; a build step may generate the
  code constants from the spec table.
- **The orphaned edge case:** someone asked "what if two players grab the
  same pickup," the designer nodded, nobody wrote it down. Fix: edge cases
  land in the doc the same day, or the spec status drops back to draft.
- **The evergreen draft:** status `draft` for three months. Fix: drafts
  older than two review cycles get killed or promoted; a permanent draft
  is a decision dodged.

## 7. A worked fragment

A trimmed spec for a hypothetical gadget, at the right size:

```markdown
---
name: tether-bomb
version: 0.3
status: ready-for-review
owner: combat-design
last-updated: 2026-09-11
related: [grapple-system, hazard-fields]
---

## Rules
1. Player attaches tether to a surface or enemy within 12 m.
2. Tether pulls player toward the anchor for 1.2 s unless interrupted.
3. On attach to an enemy, the enemy is stunned for 0.8 s.

## Parameters
| name | default | range | owner |
| --- | --- | --- | --- |
| tether_range | 12 | 8-16 | combat-design |
| pull_duration | 1.2 | 0.8-1.6 | combat-design |
| stun_duration | 0.8 | 0.4-1.2 | combat-design |
```

Note what the fragment does: names its boundaries, keeps rules testable,
tables its numbers. The full structure — inputs, interaction map, edge
cases, experience intent — is what the template adds.