# Build Plan — hearthandcode-agentic-os

## P0 complete — all 11 spec files read. No spec conflicts found.

This plan lists every file to create, grouped by phase. Each file is
referenced from the spec contracts that govern it.

---

## P1 — Scaffold (13 files)

| File | Source |
|---|---|
| README.md | 0009 tree, P1 spec |
| LICENSE | 0001 decision: MIT, 0009 tree |
| CONTRIBUTING.md | 0009 tree, P1 spec |
| .gitignore | 0009 tree, P1 spec |
| .leak-scan-tokens.example.txt | 0008, 0009 tree, P1 spec |
| docs/00-overview.md | 0009 tree, P1 spec |
| docs/01-operating-principles.md | 0009 tree, P1 spec — 4 principles with examples |
| docs/02-layer-model.md | 0009 tree, P1 spec — renders 0002 including seam map |
| docs/03-profiles.md | 0009 tree, P1 spec — profile user's guide |
| docs/04-skills.md | 0009 tree, P1 spec — skill user's guide + how-to-author |
| docs/05-installer.md | 0009 tree, P1 spec — installer reference, Pi deviation log |
| docs/06-extending.md | 0009 tree, P1 spec — extender's guide + submission checklist |

---

## P2 — Profiles (8 PROFILE.md files)

Each in `profiles/<name>/PROFILE.md`, following 0004 anatomy:

| # | Profile | Layer | Seeds from 0003 |
|---|---|---|---|
| 1 | pathfinder | L1 orientation | vague/multi-part → scoped+route |
| 2 | steward | L2 stewardship | proposed-action → consent |
| 3 | librarian | L3 knowledge | raw-material → structured-note |
| 4 | waymaker | L4 planning | scoped-goal → ordered-plan |
| 5 | maker | L5 craft | planned-step → working-draft |
| 6 | critic | L6 review | finished-unit → pass/fail |
| 7 | herald | L7 delivery | reviewed-work → package |
| 8 | archivist | L8 continuity | interrupted-work → resumption |

Each: 8 sections per 0004, 256-512 substantive lines, 5 fleet principles
in own voice, worked miniature as full sample session.

---

## P3 — Skills (16 skills, each with 10-14 files)

Each skill: `skills/<name>/` containing:
- SKILL.md (504-520 substantive lines, 8 sections per 0006)
- references/ (exactly 8 files, 40-200 lines each)
- templates/ (when listed in 0005)
- schemas/ (when listed in 0005)
- examples/ (when listed in 0005)

### Domain: game-design (3 skills)
1. **game-mechanics-design** — references(8) + templates(2) + schemas(1) + examples(1) = 14 files
2. **level-and-encounter-design** — references(8) + templates(1) + schemas(1) + examples(1) = 13 files
3. **game-economy-balancing** — references(8) + templates(1) + schemas(1) + examples(1) = 13 files

### Domain: software-development-and-architecture (3 skills)
4. **software-architecture-design** — references(8) + templates(2) + schemas(1) + examples(1) = 14 files
5. **code-review** — references(8) + templates(1) + examples(1) = 12 files
6. **testing-strategy** — references(8) + templates(1) + examples(1) = 12 files

### Domain: creative-work (2 skills)
7. **story-and-narrative-design** — references(8) + templates(2) + examples(1) = 13 files
8. **brainstorming-and-ideation** — references(8) + templates(1) + examples(1) = 12 files

### Domain: marketing (2 skills)
9. **marketing-strategy** — references(8) + templates(2) + examples(1) = 13 files
10. **copywriting-and-messaging** — references(8) + templates(1) + examples(1) = 12 files

### Domain: business-management (2 skills)
11. **business-planning** — references(8) + templates(2) + examples(1) = 13 files
12. **operations-and-process-design** — references(8) + templates(2) + examples(1) = 13 files

### Domain: social-media-management (2 skills)
13. **social-media-strategy** — references(8) + templates(1) + examples(1) = 12 files
14. **content-calendar-planning** — references(8) + templates(1) + examples(1) = 12 files

### Domain: ui-design (2 skills)
15. **ui-design-critique** — references(8) + templates(1) + examples(1) = 12 files
16. **design-system-foundations** — references(8) + templates(2) + schemas(1) + examples(1) = 14 files

### Total P3 files: 16 SKILL.md + 128 references + 23 templates + 4 schemas + 16 examples = ~187 files

---

## P4 — Installer + scripts (3 files)

| File | Source | Content |
|---|---|---|
| install.py | 0007 | TUI installer, 10 steps, stdlib only, 11 function seams |
| scripts/verify_repo.py | 0010 | --shape and --installer checks |
| scripts/scan_leaks.py | 0008 | Token list + always-active pattern scanner |

Pi seam: verify Pi agent convention before determining Pi target layout.
Record findings in docs/05-installer.md.

---

## P5 — Verification

1. `python3 scripts/verify_repo.py --shape`
2. `python3 scripts/verify_repo.py --installer`
3. `python3 scripts/scan_leaks.py`
4. Dry-run matrix (3 cells: hermes / pi / both)
5. Fresh-reader check

---

## P6 — Handoff report

Summary of all results, counts, blockers, and honest assessment.