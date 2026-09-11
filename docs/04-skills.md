# Skills

Skills are the expertise layer of the system — self-contained packages of
knowledge, each organized as a 512-line SKILL.md charter plus eight reference
files and optional templates, schemas, and examples.

Unlike profiles, which define *how* an agent operates (its scope, principles,
and workflow), skills define *what* an agent knows (the domain-specific
techniques, patterns, and procedures it can draw on).

---

## Skill anatomy

Every skill directory (`skills/<name>/`) contains:

| Path | What it is |
|---|---|
| `SKILL.md` | The charter (504-520 substantive lines). 8 sections: Purpose, When to Use, Inputs/Outputs, Workflow, Rules/Quality, Worked Example, Failure Modes, Supporting Files Index. |
| `references/` | Exactly 8 reference files (40-200 lines each). Each is a standalone document — a checklist, methodology guide, rubric, pattern catalog, glossary, or metrics guide. |
| `templates/` | Templates that define output shapes (only when listed in the skill manifest). |
| `schemas/` | JSON schemas or structured definitions (only when listed). |
| `examples/` | Extended example artifacts (only when listed). |

## The 16 skills

### Game design (3 skills)

| Skill | What it covers | Key reference files |
|---|---|---|
| **game-mechanics-design** | Core loops, action economies, progression curves, skill trees, metagame layers | Core loop canvas, action catalog template, progression curve walkthrough, tuning checklist, verb taxonomy, lock-and-key patterns, reward scheduling reference, comparative analysis guide |
| **level-and-encounter-design** | Encounter composition, pacing, difficulty curves, spatial narrative, trap and puzzle design | Encounter canvas, pacing spreadsheet, difficulty curve worksheet, environmental storytelling guide, puzzle design patterns, trap taxonomy, playtesting checklist, boss design patterns |
| **game-economy-balancing** | Resource economies, currencies, inflation control, market simulation, balancing across game modes | Economy model template, currency taxonomy, balancing mathematics reference, tuning workflow, simulation guide, sink/source catalog, player psychology reference, live-ops adjustment guide |

### Software development & architecture (3 skills)

| Skill | What it covers | Key reference files |
|---|---|---|
| **software-architecture-design** | Architecture decisions, module boundaries, API design, data flow, technology selection | ADR template, architecture decision canvas, modularity patterns, API contract rubric, quality attribute scenario guide, tech stack evaluation matrix, data flow diagram patterns, migration strategy guide |
| **code-review** | Review workflows, checklist-based verification, communication, security and performance scanning | Code review checklist, security review guide, performance review guide, review feedback templates, severity classification guide, author's guide (how to request review), code review workflow, metrics and tracking guide |
| **testing-strategy** | Test pyramids, coverage boundaries, test design, automation strategy, quality metrics | Test strategy template, test case design patterns, coverage boundary guide, test automation decision matrix, quality metrics reference, risk-based testing guide, test environment strategy, test documentation templates |

### Creative work (2 skills)

| Skill | What it covers | Key reference files |
|---|---|---|
| **story-and-narrative-design** | Narrative structure, character arcs, worldbuilding, dialogue, theme, pacing | Narrative structure guide, character arc worksheet, worldbuilding template, dialogue beat sheet, theme development matrix, pacing calculator, scene outline template, revision checklist |
| **brainstorming-and-ideation** | Divergent and convergent thinking, ideation methods, concept evaluation, group facilitation | Ideation methods catalog, SCAMPER reference, concept evaluation matrix, facilitation guide, warmup exercise catalog, idea capture template, constraints guide, cross-domain inspiration catalog |

### Marketing (2 skills)

| Skill | What it covers | Key reference files |
|---|---|---|
| **marketing-strategy** | Market analysis, positioning, messaging, channel strategy, campaign planning | Market analysis framework, positioning canvas, messaging hierarchy template, channel strategy guide, campaign planning worksheet, competitive analysis template, content strategy guide, KPI and measurement framework |
| **copywriting-and-messaging** | Brand voice, persuasion techniques, format-specific writing, editing, headlines | Brand voice worksheet, persuasion techniques catalog, format reference library, editing checklist, headline patterns, call-to-action guide, tone adjustment guide, A/B testing framework |

### Business management (2 skills)

| Skill | What it covers | Key reference files |
|---|---|---|
| **business-planning** | Business models, financial planning, market sizing, competitive strategy, pitch preparation | Business model canvas companion, financial projection template, market sizing guide, competitive analysis framework, pitch deck outline, milestone planning worksheet, risk assessment matrix, investor outreach guide |
| **operations-and-process-design** | Process mapping, workflow design, SOP creation, metrics, continuous improvement | Process mapping guide, SOP template, operational metrics catalog, workflow design patterns, continuous improvement framework, SLA design guide, escalation path patterns, operations review cadence |

### Social media management (2 skills)

| Skill | What it covers | Key reference files |
|---|---|---|
| **social-media-strategy** | Platform selection, content mix, posting cadence, audience analysis, growth tactics | Platform comparison guide, content pillar template, posting cadence calculator, audience analysis worksheet, growth tactics catalog, engagement metric guide, crisis communication workflow, analytics review process |
| **content-calendar-planning** | Calendar structure, scheduling strategy, deadline management, cross-platform coordination | Calendar template, scheduling strategy guide, deadline management process, cross-platform coordination guide, content scoring rubric, theme-planning worksheet, workflow automation guide, quarterly retrospective process |

### UI design (2 skills)

| Skill | What it covers | Key reference files |
|---|---|---|
| **ui-design-critique** | Critique frameworks, visual evaluation, accessibility review, interaction analysis, feedback communication | Critique framework reference, visual evaluation checklist, accessibility review guide, interaction patterns reference, feedback communication guide, heuristic evaluation reference, design principle catalog, critique session facilitation guide |
| **design-system-foundations** | Design token architecture, component taxonomy, documentation, governance, adoption, testing | Design token specification, component taxonomy guide, documentation template, governance model canvas, adoption strategy guide, testing strategy reference, versioning and changelog guide, migration pattern catalog |

---

## Writing your own skill

To author a new skill:

1. **Study the contract** in `spec/0006-skill-charter-contract.yaml`. Every
   skill must follow this anatomy exactly.
2. **Find the roster** in `spec/0005-skill-roster.yaml` to see the full
   manifest requirements for your domain.
3. **Create the directory** `skills/<your-skill-name>/` with:
   - `SKILL.md` (504-520 substantive lines, 8 sections)
   - `references/` (exactly 8 files, 40-200 lines each)
   - Supporting files only if listed in an updated manifest
4. **Follow the quality bar:** The workflow section must be executable by a
   competent practitioner without any other document. The worked example uses
   a specific named scenario. Every file in the directory is referenced in
   SKILL.md and vice versa.
5. **Run the verifier:** `python3 scripts/verify_repo.py --shape` validates
   every skill against the contracts.

See `docs/06-extending.md` for the full extender's guide and submission
checklist.

## Loading skills

Skills are loaded by your agent harness. Their frontmatter descriptions lead
with the trigger situation so a router knows when to load them. You can
also load a skill explicitly to get its full charter into context.

Each skill's `references/` files are meant to be consulted individually —
the workflow in SKILL.md names which reference to use at each step.