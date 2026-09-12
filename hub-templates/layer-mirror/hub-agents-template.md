# AGENTS — Hub Governance and Orchestration Charter

## ORCHESTRATE: This document governs all agents and profiles operating inside this hub. It is read at session boot and every profile references it by path. It never moves, never renames, and is never modified without an ACK decision recorded in the ledger.

## 01 — Purpose and Scope

This is the permanent governance charter of the agentic hub. It occupies the hub root and is the first document an agent reads when joining a hub session. Every profile — from pathfinder (L1) through archivist (L8) — loads this document as its top-level context. Skills reference it for routing, consent, and provenance rules.

It owns four things:
1. **Orchestration** — the active objectives, routing topology, directory structure.
2. **Governance** — how decisions are made, how effects are authorized (ACK protocol).
3. **Provenance** — decision ledger, chain of consent across sessions.
4. **Recovery** — a cold-start reader can learn the hub's state and rules.

## 02 — ACK Signature Protocol

Every human decision that produces an effect requires an ACK before execution.

### Format

ACK per profile per sequence, with a SHA-256 hash:

`ACK-{profile}-{sequence}-{8-char-hash}`

Example: `ACK-maker-007-4f9e2b — Build API landing page code`

### ACK kinds

| Kind | Situation |
|------|-----------|
| `effect` | Write, delete, move any file inside hub scope |
| `gate` | Approve or reject a deliverable |
| `route` | Change a routing decision mid-session |
| `archive` | Close or archive a project |
| `rollback` | Undo a prior effect |
| `governance` | Change this AGENTS.md or the layout |
| `objective` | Declare a new session objective |

### ACK lifecycle

```
GENERATED → PENDING → CONFIRMED → RECORDED → CLOSED
                    → REJECTED  → RECORDED → CLOSED
                    → EXPIRED   → VOID
```

## 03 — Decision Ledger

Location: `<hub-root>/09-ops/01-decision-ledger/README.md`

Each decision is one fenced YAML block:

```yaml
---ack
id: ACK-maker-007-4f9e2b
kind: effect
session: 2026-09-11T16:30:00Z
profile: maker
action: "Write file: 05-craft/whitepaper-v2.md"
status: CONFIRMED
human response: yes
context: "Plan step 3 — integrate migration feedback"
---
```

Ledger invariants:
- No entry is ever deleted or edited after recording.
- Corrections are new entries with the identical id and status: corrected.
- The ledger file is read at session start by the archivist.
- Every ACK id is unique in the active ledger.

## 04 — Directory Layout

This is the layer-mirror layout. All folders carry a two-digit numbered prefix for sort-order mapping to workflow order.

| Folder | Layer | Profile | Purpose |
|--------|-------|---------|---------|
| `01-orientation/` | L1 | pathfinder | Incoming work, hub maps, route recommendations |
| `02-stewardship/` | L2 | steward | Consent records, backups, change logs |
| `03-knowledge/` | L3 | librarian | Notes, sources, references, citation store |
| `04-planning/` | L4 | waymaker | Plans, goal maps, acceptance criteria |
| `05-craft/` | L5 | maker | Drafts, code, designs, built artifacts |
| `06-review/` | L6 | critic | Review findings, quality checks, verdicts |
| `07-delivery/` | L7 | herald | Formatted output, release packages, handoff docs |
| `08-continuity/` | L8 | archivist | Handoffs, session logs, archive state |
| `09-ops/` | Layer 0 | AGENTS.md | Decision ledger, scripts, config |
| `10-archive/` | — | — | Completed and closed items |

All subfolders are numbered the same way: `NN-kebab-name/`.

### Rules of engagement

- A profile may READ from any directory without an ACK.
- A profile may WRITE only to its canonical directory, unless a writing delegation ACK exists.
- A profile may not create or delete a folder without an ACK.
- Every leaf deliverable path inherits the numbered prefix of its parent.

## 05 — Alternate Layouts

### Workflow-pipeline

`01-inbox/` → `02-scoped/` → `03-in-progress/` → `04-review/` → `05-done/` → `06-archive/` → `07-reference/` → `08-ops/`

### Project-centric

`01-projects/` → `02-notes/` → `03-research/` → `04-drafts/` → `05-templates/` → `06-archive/` → `07-reference/` → `08-ops/`

### Topical-indexed

`01-writing/` → `02-code/` → `03-design/` → `04-planning/` → `05-research/` → `06-archive/` → `07-templates/` → `08-meta/`

## 06 — Recovery

- If AGENTS.md is missing, the hub is inoperative. Restore via installer.
- If the ledger is missing or corrupted, agents refuse to execute effects until a manual ACK-INTEGRITY-001 is granted by the human.
- No effects execute without a valid AGENTS.md.

## 07 — Version

- Version: 1.0.0
- Layout: layer-mirror (default)
- Last modifiable: ACK of kind governance.