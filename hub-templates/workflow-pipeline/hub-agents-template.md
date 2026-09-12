# AGENTS — Hub Governance and Orchestration Charter

## ORCHESTRATE: This document governs all agents and profiles operating inside this hub. It is read at session boot and every profile references it by path. It never moves, never renames, and is never modified without an ACK decision recorded in the ledger.

## 01 — Purpose and Scope

This is the permanent governance charter of the agentic hub. It occupies the hub root and is the first document an agent reads. Every profile loads it as top-level context.

It owns four things:
1. **Orchestration** — active objectives, routing topology, directory structure.
2. **Governance** — how decisions are made (ACK protocol).
3. **Provenance** — decision ledger, chain of consent.
4. **Recovery** — cold-start reader learns hub state.

## 02 — ACK Signature Protocol

Every human decision that produces an effect requires an ACK before execution.

Format: `ACK-{profile}-{sequence}-{8-char-hash}`

Kinds: effect, gate, route, archive, rollback, governance, objective

Lifecycle: GENERATED → PENDING → CONFIRMED → RECORDED or REJECTED → CLOSED

## 03 — Decision Ledger

Location: `<hub-root>/08-ops/01-decision-ledger/README.md`

Each entry is a fenced YAML block with id, kind, timestamp, profile, action, status, human response.

Invariants: no entry is ever deleted or edited; corrections are new entries.

## 04 — Directory Layout: Workflow-Pipeline

Work is tracked by stage. Each NN-prefixed folder maps to a workflow step.

| Folder | Purpose |
|--------|---------|
| `01-inbox/` | Raw intake, uncategorized ideas, incoming requests |
| `02-scoped/` | Tasks with a route recommendation and scope boundary |
| `03-in-progress/` | Active work being executed by any profile |
| `04-review/` | Work waiting for review or quality check |
| `05-done/` | Completed, verified, and signed-off work |
| `06-archive/` | Closed seasons, finished projects, historical artifacts |
| `07-reference/` | Permanent reference, templates, research store |
| `08-ops/` | AGENTS.md copy, decision ledger, scripts, backups |

### Rules of engagement

- A profile may READ from any directory without an ACK.
- A profile may WRITE only to a directory appropriate to the work's stage.
- Moving work across stages requires an ACK or route kind.
- A profile may not create or delete a folder without an ACK.

## 05 — Alternate Layouts

Available: layer-mirror, project-centric, topical-indexed.

## 06 — Recovery

If AGENTS.md is missing, hub is inoperative. Restore via installer.

## 07 — Version 1.0.0 — Layout: workflow-pipeline