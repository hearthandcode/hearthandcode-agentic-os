---
purpose: >
  Hub governance charter — orchestrates the 8 profile layers, enforces the ACK
  signature protocol, maintains the decision ledger, and maps work to directories.
version: 1.0.0
layout: layer-mirror
hub_root: .
---

# AGENTS — Hub Governance and Orchestration Charter

## 01 — Purpose and Identity

This document is the permanent governance layer of the agentic hub. It sits at the
hub root and is never removed, replaced, or modified without an ACK-signed decision.
Every profile, every skill, and every agency follows the rules declared here when
operating inside the hub scope. It has four functions:

1. **Orchestration** — declare the active objectives, the routing topology, and the
   directory layout so every profile loads the same map.
2. **Governance** — define how decisions are made, signed, recorded, and enforced.
3. **Provenance** — host the decision ledger and maintain the chain of consent.
4. **Recovery** — answer the question "what was this hub doing and why" on re-entry.

## 02 — Layout Declaration

This hub uses the **layer-mirror** layout. Every top-level folder is bound to a
layer from the profile fleet. All work produced by a given profile must be placed
inside that profile's folder or in a child path inside it, unless an ACK-signed
exception has been granted.

### Top-level directory layout

| Folder | Layer | Profile binding | Purpose |
|--------|-------|----------------|---------|
| `01-orientation/` | L1 | pathfinder | Incoming work, hub maps, route recommendations |
| `02-stewardship/` | L2 | steward | Consent records, backups, change logs |
| `03-knowledge/` | L3 | librarian | Notes, sources, references, citation store |
| `04-planning/` | L4 | waymaker | Plans, decompositions, goal maps |
| `05-craft/` | L5 | maker | Drafts, code, designs, built artifacts |
| `06-review/` | L6 | critic | Review findings, quality checks, verdicts |
| `07-delivery/` | L7 | herald | Formatted output, release packages |
| `08-continuity/` | L8 | archivist | Handoff notes, session logs, archive |
| `09-ops/` | Layer 0 | AGENTS.md | Decision ledger, ACK registry, config |
| `10-archive/` | — | — | Finished and closed items |

Every subfolder inside a layer path inherits the binding of its parent. Profile
may travel: the maker also writes to `03-knowledge/` when using the librarian
material, but the canonical home of maker output is `05-craft/`.

## 02 — The ACK Signature Protocol

Every human decision that has an effect on the hub — writing, routing, moving, deleting,
approving, rejecting — requires an **ACK signature** to be recorded before the effect
executes. This is the heartbeat of the hub's transparency.

### Generating an ACK signature

When a profile determines that a human decision is needed:

```
ACK-{epoch-seconds}-{8-char-sha}-{action-slug}
```

Example: `ACK-1762879200-a1b2c3d4-approve-design-system`

The agent:
1. Detects the decision point (effect, route change, approval gate).
2. Generates the ACK string.
3. Presents it to the human: "ACK-1762879200-a1b2c3d4: Shall I proceed with [description]?"
4. The human responds yes/no (or more info).
5. If **yes**, the agent records the ACK in the decision ledger.
6. If **no**, the agent marks the ACK as `REJECT` in the ledger and stops.
7. The agent then executes (or does not execute) the effect.

### ACK signature generation rules

1. **Epoch seconds** = the current Unix timestamp when the ACK is generated, not
   when it's confirmed.
2. **Task hash** = first 8 hex characters of SHA-256(description + timestamp +
   hub_root).
3. **Action slug** = lowercase hyphenated, describes the pending effect and one
   action.
4. **Sequence** = incremented integer per session, reset per month.

Replay for the same task in the same session is the same ACK repeated.

### ACK lifecycle

1. GENERATED — agent creates the ACK, presents to user.
2. PENDING — user hasn't responded yet.
3. CONFIRMED — user said yes, ACK recorded in ledger.
4. REJECTED — user said no, ACK recorded as rejected.
5. EXPIRED — ACK was generated but not confirmed within session end.
6. SUPERSEDED — a later ACK supersedes this one.

## 03 — Decision Ledger

The decision ledger is `<hub-root>/09-ops/01-decision-ledger/README.md` (for
active entries) and archived monthly as `<hub-root>/09-ops/01-decision-ledger/YYYY-MM.md`.

Each ledger entry is a fenced YAML block:

```
---ack
id: ACK-1761234560-a1b2c3d4
timestamp: 2026-09-11T16:30:00Z
kind: effect
action: "Create file ~/agentic-hub/05-craft/whitepaper-v2.md"
profile: maker
status: confirmed
human response: yes
supersedes: null
superseded_by: null
requested_by: user
---
```

Ledger invariants:
- No entry is ever deleted or modified after writing.
- A correction ACK (status: corrected) may reference a prior ACK and the
  corrected version.
- The ledger file may be MOVED (to archive) but never overwritten.

### Decision types

| Kind | Examples | Requires ACK? |
|------|----------|---------------|
| Execution effect | Write, move, delete file | Yes |
| Routing decision | "Route this to maker" | Yes (when routing.execution.handoffs) |
| Approval gate | "Approve this design" | Yes |
| Scope change | "Work outside hub root" | Yes (ACK + entry steward) |
| Info sharing | "Hub map please" | On the
| Attention from hub | "Load this sunset" | No |
| Error recovery | "Roll back" | Yes |

## 04 — Routing Map

The profile routing topology is fixed by the layer model. Work flows through
the hub as follows:

```
User Request
  ↓
L1-pathfinder (orienteer) — scopes work, maps hub, recommends route
  ↓  (scoped task statement)
L4-waymaker — decomposes into plan with acceptance criteria
  ↓  (plan steps)
L5-maker — executes each bounded step
  ↓  (finished unit)
L6-critic — reviews against criteria
  ↓  pass / fail
L7-herald — formats and packages for audience
  ↓  (through L2 consent check for external)
L8-archivist — everything that is not external is archived with handoff
```

Each arrow passes a formal handoff artifact: the scoped task statement, the plan,
the work unit, the review finding, the delivery, the archive entry.

Profiles are loaded manually (or by the orchestrator AGENTS.md for automated
routing). The pathfinder (L1) provides route recommendations; it does not
execute routing.

## 05 — Session Lifecycle

Every session that touches the hub should follow:

1. **ACK boot** — load this AGENTS.md to restore the operational shape.
2. **Status check**: ask the archivist (or read `08-continuity/`) for active work.
3. **Claim**: state which work you're picking up and generate an ACK for
   that claim.
4. **Execute**: run the workflow.
5. **Ledger close**: record the session's ACKs at session end.
6. **Archive**: move in-progress handoff to `08-continuity/`.