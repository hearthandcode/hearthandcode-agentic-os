# Extending the System

This repository is designed to be extended. You can add new profiles, new
skills, or improve existing ones — as long as you follow the contracts in
`spec/`. This guide explains the process and provides a submission checklist.

---

## Understanding the contracts

Every file in this repository is governed by a contract in `spec/`. Before
extending, you should understand the contracts that apply to your change:

| If you are changing | Governing contract(s) |
|---|---|
| A profile charter | `spec/0003` (roster), `spec/0004` (template/anatomy), `spec/0002` (layer model) |
| Adding a new profile | `spec/0003`, `spec/0004`, `spec/0002`, `spec/0009` (layout) |
| A skill charter | `spec/0005` (roster/manifest), `spec/0006` (anatomy/512-line rule) |
| Adding a new skill | `spec/0005`, `spec/0006`, `spec/0009` (layout) |
| The installer | `spec/0007` (behavior) |
| Scripts | `spec/0010` (verification), `spec/0008` (safety) |
| Any artifact | `spec/0008` (abstraction/safety), `spec/0001` (governance) |

---

## Adding a profile

### 1. Find the right layer

Profiles are bound to layers — exactly one profile per layer. If your new
profile would occupy a layer that already has a profile, you must first
amend the contracts in `spec/0002` and `spec/0003` (which requires a
maintainer discussion).

The eight existing layers (L1-L8) cover: orientation, stewardship, knowledge,
planning, craft, review, delivery, continuity. A new profile should fit
within one of these layers or propose a new layer.

### 2. Write the PROFILE.md

Follow `spec/0004-profile-charter-template.yaml` exactly:

- 8 sections in order: Recognition, Role and Operating Principles, Input
  Contract, Output Contract, Workflow, Worked Miniature, Boundaries and
  Failure Modes, Customization
- 256-512 substantive lines
- The worked miniature must be a realistic sample session
- All five shared fleet principles (consent-and-effects, hub-scope
  confinement, claim labels, pause-and-ask, you own every decision) appear
  in the profile's own voice with layer-specific examples
- Cross-references to other profiles use only the eight public profile names

### 3. Register the profile

Add the profile to `spec/0009-repository-layout.yaml` (the canonical tree)
and add an entry to `profiles/<name>/PROFILE.md`.

### 4. Run verification

```bash
python3 scripts/verify_repo.py --shape
```

---

## Adding a skill

### 1. Choose a domain

The 16 existing skills are organized across 7 domains: game design, software
development, creative work, marketing, business management, social media
management, and UI design. A new skill can join an existing domain or
establish a new one.

### 2. Write the SKILL.md

Follow `spec/0006-skill-charter-contract.yaml` exactly:

- 8 sections in order: Purpose, When to Use / When Not to Use, Inputs and
  Outputs, Workflow, Rules and Quality Bar, Worked Example, Failure Modes
  and Recovery, Supporting Files Index
- 504-520 substantive lines (target 512)
- The workflow section (8-16 steps) must be executable by a competent
  practitioner without any other document
- The worked example uses a specific named scenario (product, game, business,
  or campaign) — no placeholders — and shows intermediate artifacts

### 3. Write the reference files

Exactly 8 files in `references/`, each 40-200 substantive lines. Across
the 8 files, cover at least 4 of these roles:

- Methodology guide
- Checklist
- Rubric
- Pattern catalog
- Case study
- Glossary
- Template guide
- Metrics/measurement guide

### 4. Write supporting files

If your skill needs templates, schemas, or extended examples, add them in
the corresponding subdirectories. These must be listed in your skill's
manifest entry in `spec/0005`.

### 5. Close the reference loop

- Every file mentioned in SKILL.md exists in the skill directory
- Every file in the skill directory is mentioned in SKILL.md
- The Supporting Files Index table (section 08) matches the directory
  listing exactly

### 6. Verify

```bash
python3 scripts/verify_repo.py --shape
```

---

## Submission checklist

Before opening a pull request, check every item:

### Safety

- [ ] All content is written from general professional knowledge
- [ ] No internal code names, project names, hostnames, paths, usernames,
      emails, or personal identifiers from any private system
- [ ] No passage could only have been written by reading a private system
- [ ] `scripts/scan_leaks.py` exits clean against the repository
- [ ] Names pass two tests: a stranger learns the function from the name;
      an insider cannot reverse-engineer private structure from it

### Contract conformance

- [ ] Profile follows `spec/0004` anatomy (8 sections, correct order)
- [ ] Skill follows `spec/0006` anatomy (8 sections, correct order)
- [ ] Profile is 256-512 substantive lines (counting rule: total − blanks −
      frontmatter delimiters)
- [ ] Skill is 504-520 substantive lines (same counting rule)
- [ ] References directory holds exactly 8 files, 40-200 lines each
- [ ] Supporting directories match the manifest entry exactly (no missing,
      no extras, none empty)
- [ ] The tree matches what `spec/0009` expects

### Quality

- [ ] The workflow section is executable without any other document
- [ ] The worked example uses a specific named scenario (not placeholder or
      abstract)
- [ ] The worked example shows intermediate artifacts, not just the final one
- [ ] No TODO, FIXME, "lorem ipsum", or "example content goes here"
- [ ] Generic filler, listicle fluff, and restated boilerplate are absent
- [ ] A reader can do the work after reading, not merely know about it

### Mechanical

- [ ] Reference closure: every file in SKILL.md exists; every file in the
      directory is mentioned in SKILL.md
- [ ] The Supporting Files Index table matches the directory listing exactly
- [ ] `python3 scripts/verify_repo.py --shape` passes
- [ ] `python3 scripts/verify_repo.py --installer` passes (if installer
      files changed)
- [ ] `python3 scripts/scan_leaks.py` exits clean

---

## Modifying existing content

Improvements to existing profiles and skills are welcome as long as they:

- Maintain contract conformance (the improved version still passes `--shape`)
- Add depth, not padding (a longer file that just restates the same thing
  is worse than the original)
- Preserve the open-source safety posture (no leaks)
- Keep the worked examples grounded (if you replace a scenario, the new one
  must be equally specific)

## Modifying the contracts

The `spec/` directory is permanent maintainer documentation and ships with
the repo. Changing a contract requires a discussion with the maintainer.
The gate record in `spec/0001` notes that the current design was approved
as-is; amendments are tracked by updating the gate record and the affected
contracts.

If you find a genuine conflict or gap in the contracts, report it as an
issue rather than silently deviating in your implementation.