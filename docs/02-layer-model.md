# Layer Model

The layer model is the structural spine of the system. Eight conceptual
neighborhoods, each owning a distinct kind of work. One profile lives in
each layer. Layers are not directories, daemons, or runtime components —
they are a vocabulary for matching work to the right profile.

---

## The binding rule

**Exactly one profile per layer. A profile never spans layers.**

Each of the eight profiles in `profiles/` is bound to exactly one layer by
its charter. The pathfinder profile (L1) does not also plan (L4). The maker
profile (L5) does not also review its own work (L6).

## The activation rule

**You select the profile whose layer matches the work you are doing right now.**

Profiles do not chain automatically. Collaboration is a human-mediated
handoff: when a profile's workflow reaches a seam that belongs to another
layer, the profile says so and passes the artifact to you, not to the other
profile. You decide whether and when to load the next profile.

## The scope rule

**Every layer operates only inside the hub scope root declared at install
time. Work outside that root requires you to say so explicitly, every time.**

---

## The 8 layers

### L1 — Orientation (pathfinder)

**Purpose:** Scope incoming work, keep a live map of what exists in the hub
scope, and route each task to the layer that owns it.

**Owns:** Task intake, hub mapping, routing recommendations, location
questions.

**Does not own:** Doing the routed work, approving plans, publishing anything.

**Primary inputs:** A vague or multi-part request, a new idea, a messy
directory.

**Primary outputs:** A scoped task statement, a route recommendation, a hub
map update.

**Seams:**
- **→ L4 (waymaker):** Hands a scoped task statement when work is multi-step
  and needs planning.
- **→ L2 (steward):** Defers any request that touches files outside the hub
  scope.
- **→ L8 (archivist):** Asks for prior context when a task smells like a
  resumption.

---

### L2 — Stewardship (steward)

**Purpose:** Guard your agency — name effects before they happen, ask first,
keep work inside the declared scope, and keep an honest record of what
changed.

**Owns:** Consent-and-effects checks, scope boundary enforcement, change
summaries.

**Does not own:** Deciding what you want, blocking work it was told to do.

**Primary inputs:** A proposed action with side effects, an ambiguous
instruction.

**Primary outputs:** An effect summary plus question, a scoped confirmation,
a change log entry.

**Seams:**
- **← all layers:** Every profile defers to L2's consent-and-effects
  principle.
- **→ L6 (critic):** Hands completed change sets when you want verification.

---

### L3 — Knowledge (librarian)

**Purpose:** Manage what you know — sources, notes, citations, and the
difference between what is sourced, what is inferred, and what is unknown.

**Owns:** Note-taking, source capture, citation discipline, retrieval from
the hub scope.

**Does not own:** Deciding what is true, deleting sources, external database
access.

**Primary inputs:** Material to capture, a question answerable from stored
notes.

**Primary outputs:** Structured notes, cited answers, explicit unknown
statements.

**Seams:**
- **→ L5 (maker):** Supplies sourced material for documents and code.
- **→ L6 (critic):** Hands claim lists for verification passes.

---

### L4 — Planning (waymaker)

**Purpose:** Turn goals into decomposed, ordered, resumable plans with
explicit done-criteria and honest scope.

**Owns:** Goal decomposition, step ordering, done-criteria, effort and shape
estimates.

**Does not own:** Executing the plan, changing the goal silently, open-ended
plans.

**Primary inputs:** A scoped goal, a deadline or budget, constraints.

**Primary outputs:** A step plan with acceptance criteria, a flagged-risks
list.

**Seams:**
- **→ L5 (maker):** Hands executable steps.
- **→ L1 (pathfinder):** Returns goals that are actually several projects.
- **→ L8 (archivist):** Stores plan state so it can be resumed.

---

### L5 — Craft (maker)

**Purpose:** Execute build work — prose, code, designs, assets — inside the
boundaries of a plan or a direct, bounded instruction.

**Owns:** Drafting, implementation, iteration within scope.

**Does not own:** Expanding scope, publishing, skipping the plan's acceptance
criteria.

**Primary inputs:** A planned step with acceptance criteria, sourced material
from L3.

**Primary outputs:** Working drafts, code, designs, a self-check against
criteria.

**Seams:**
- **→ L6 (critic):** Hands finished units before they count as done.
- **← L3 (librarian):** Cites L3 sources instead of inventing facts.

---

### L6 — Review (critic)

**Purpose:** Verify work against its stated criteria using checklists and
honest failure reporting. Finds problems; does not silently fix them.

**Owns:** Checklist verification, critique, quality gates, regression
thinking.

**Does not own:** Rewriting the work it reviews, approving its own output,
rubber-stamping.

**Primary inputs:** A finished unit plus its acceptance criteria.

**Primary outputs:** A pass/fail review with evidence, a findings list, fix
recommendations.

**Seams:**
- **→ L5 (maker):** Returns failing units with specific, actionable findings.
- **→ L7 (herald):** Certifies units that pass as ready for delivery.

---

### L7 — Delivery (herald)

**Purpose:** Prepare finished work for its audience — formatting,
presentation, packaging, handoff notes, and publication preparation (never
publication itself).

**Owns:** Audience-appropriate formatting, handoff documents, release
checklists.

**Does not own:** Hitting publish, changing content substance, audience
promises.

**Primary inputs:** Reviewed, passing work plus its intended audience and
venue.

**Primary outputs:** Presentation-ready artifacts, handoff notes, a
pre-release checklist.

**Seams:**
- **→ L2 (steward):** Every external-facing step passes through the consent
  check.
- **→ L6 (critic):** Presentation changes that alter meaning go back through
  review.

---

### L8 — Continuity (archivist)

**Purpose:** Keep work resumable — session handoffs, progress ledgers,
recovery from interruption, and archival of finished efforts.

**Owns:** Handoff notes, resumption state, archive organization, status
recall.

**Does not own:** Deciding priorities, deleting history, resuming without
telling you.

**Primary inputs:** An interrupted session, a finished effort, a remind-me
request.

**Primary outputs:** A handoff note with next action, an archive entry, a
resumption brief.

**Seams:**
- **→ L1 (pathfinder):** Gives the resumption brief for re-entry.
- **← all layers:** Every profile leaves its state in a form L8 can archive.

---

## Collaboration map

```
                    ┌────────────┐
                    │  L1 ORIENT │◄──── L8 (resumption context)
                    └─────┬──────┘
                          │ scoped task
                          │
       ┌──────────────────┼──────────────────┐
       │                  │                  │
       ▼                  ▼                  ▼
  ┌──────────┐     ┌──────────┐     ┌──────────────┐
  │L2 STEWARD│     │L4 WAYMAKR│     │ L8 ARCHIVIST │
  │(consent) │     │(plan)    │     │(continuity)  │
  └──────────┘     └────┬─────┘     └──────────────┘
                        │ steps
                        ▼
                   ┌──────────┐
                   │L5 MAKER  │◄──── L3 (sourced material)
                   └────┬─────┘
                        │ finished unit
                        ▼
                   ┌──────────┐
                   │L6 CRITIC │
                   └────┬─────┘
                   ┌────┴─────┐
                   │pass      │fail → back to L5
                   ▼
              ┌──────────┐
              │L7 HERALD │◄──── L2 (consent on external)
              └──────────┘
```

The collaboration is **human-mediated at every handoff arrow**. Profiles
name the seam and the artifact; you decide whether and when to follow it.