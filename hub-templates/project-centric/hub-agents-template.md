# AGENTS — Hub Governance and Orchestration Charter

## 01 — Purpose and Scope

Governance charter of the agentic hub. Occupies the hub root. First document an agent reads at session boot. Owns orchestration, governance (ACK protocol), provenance (decision ledger), and recovery.

## 02 — ACK Signature Protocol

Every human decision with an effect requires an ACK before execution.

Format: `ACK-{profile}-{sequence}-{8-char-hash}`

Kinds: effect, gate, route, archive, rollback, governance, objective

Lifecycle: GENERATED → PENDING → CONFIRMED → RECORDED or REJECTED → CLOSED

## 03 — Decision Ledger

`<hub-root>/08-ops/01-decision-ledger/README.md` — fenced YAML blocks, append-only, never edited.

## 04 — Directory Layout: Project-Centric

Work organized by project. Top-level folders group by function.

| Folder | Purpose |
|--------|---------|
| `01-projects/` | One subfolder per active project |
| `02-notes/` | Cross-project notes, reference, personal knowledge |
| `03-research/` | Sources, investigations, literature |
| `04-drafts/` | Cross-project scratch drafts and WIP |
| `05-templates/` | Reusable templates, scaffolds, schemas |
| `06-archive/` | Completed projects and closed work |
| `07-reference/` | Permanent reference materials and external sources |
| `08-ops/` | AGENTS.md copy, decision ledger, scripts, backups |

Each project subfolder in `01-projects/` follows its own NN-prefixed structure:
`NN-goal/`, `NN-research/`, `NN-plan/`, `NN-execute/`, `NN-review/`, `NN-deliver/`.

## 05 — Recovery

If AGENTS.md is missing, hub is inoperative. Restore via installer.

## 06 — Version 1.0.0 — Layout: project-centric