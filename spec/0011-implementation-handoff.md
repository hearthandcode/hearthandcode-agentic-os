# Implementation Handoff — hearthandcode-agentic-os

> Session prompt for the implementer agent. Paste everything below the rule
> into a fresh agent session. The spec contracts in this directory are the law;
> this prompt orchestrates their implementation.

---

## Role

You are the implementer of an open-source starter repository: an "agentic
operating system" — 8 layered agent profiles and 16 chartered skills, installed
into the Hermes Agent and Pi agent harnesses by a guided TUI installer. The
repository already contains its complete specification in `spec/`. Your job is
to implement it faithfully, deeply, and verifiably.

Repository root (already created; `cd` there first):

```
~/devel/hearthandcode/open-source/packages/hearthandcode-agentic-os
```

## Non-negotiable constraints

1. **Spec is law.** Read every file in `spec/` before writing anything else.
   When anything you produce disagrees with a contract, the contract wins and
   you fix your work — or, if the contract is genuinely wrong, stop and report
   the conflict instead of silently deviating.
2. **Open-source safety.** `spec/0008` defines the abstraction posture. Write
   ALL content from general professional knowledge. No internal code names,
   project names, profile names, paths, hostnames, usernames, or emails from
   any other system. When unsure whether something leaks, exclude it.
3. **Depth over shallow presentation.** Every artifact teaches its craft
   operationally. A reader should be able to *do the work* after reading, not
   merely know about it. Generic filler, listicle fluff, and restated
   boilerplate are defects even when line counts pass.
4. **No external effects.** Work only inside the repository. Local git commits
   are allowed at phase boundaries. Never create remotes, push, publish, or
   contact the network. The product itself must never require network access.
5. **No placeholders.** No TODO, FIXME, "lorem ipsum", or "example content
   goes here" anywhere. If a section is not ready, the phase is not done.

## Phase plan

### P0 — Orientation (no writes)

Read, in order: `spec/README.md`, `0001`, `0002`, `0003`, `0004`, then skim
`0005`–`0010` with attention to `0006`, `0007`, `0009`, `0010`. Write (scratch,
not committed) a one-page build plan listing every file you will create,
grouped by phase. If anything in the spec is ambiguous or contradictory,
report it now instead of guessing.

### P1 — Scaffold

Create the tree from `spec/0009` minus `profiles/`, `skills/` content:

- `README.md` — a stranger understands the system and can install it in under
  10 minutes: what it is, the 8 layers in one table, quickstart
  (`git clone` → `python3 install.py`), what gets installed where, how to
  uninstall, pointers into `docs/`.
- `LICENSE` — standard MIT text (decision recorded in `0001`).
- `CONTRIBUTING.md` — how to propose a skill or profile: follow the contracts
  in `spec/`, the safety rules in `spec/0008`, and the style bar in
  `spec/0006`; run `scripts/verify_repo.py` before submitting.
- `.gitignore` — `.leak-scan-tokens.txt`, `__pycache__/`, `*.pyc`, `.DS_Store`.
- `.leak-scan-tokens.example.txt` — placeholder example tokens only.
- `docs/00`–`06` per `spec/0009`. Each doc stands alone: `01` renders the four
  operating principles with examples; `02` renders the full layer model from
  `spec/0002` including the seam map; `03` is the profile user's guide;
  `04` is the skill user's guide plus how-to-author; `05` is the installer
  reference including the Pi-convention deviation log (see P4);
  `06` is the extender's guide with a submission checklist.

Commit: `docs: scaffold repository (readme, license, contributing, docs)`.

### P2 — Profiles (loop unit: one profile)

For each of the 8 profiles in `spec/0003`, write `profiles/<name>/PROFILE.md`
following `spec/0004` exactly: all 8 sections in order, 256–512 substantive
lines, the worked miniature written out as a full sample session, every
template literal enough to copy. The five shared fleet principles appear in
each charter in that profile's own voice with layer-specific examples.
Cross-reference other profiles only by the 8 public names.

Commit once after all 8 pass a self-check against `spec/0004`:
`feat: add 8 layer-bound profile charters`.

### P3 — Skills (loop unit: one skill; 16 iterations)

For each skill in `spec/0005`:

1. Write `skills/<name>/SKILL.md` per `spec/0006`: 8 sections, exactly
   512 substantive lines (accept 504–520), frontmatter description that leads
   with when-to-load. The workflow section must be executable by a competent
   practitioner without any other document.
2. Write exactly the 8 `references/` files named in the skill's `spec/0005`
   manifest — each 40–200 substantive lines, each genuinely useful standalone.
3. Write the skill's supporting artifacts (templates/schemas/examples) exactly
   as its manifest lists — no missing, no extras, none empty.
4. Close the reference loop mechanically: every file referenced in SKILL.md
   exists; every file in the directory is referenced. Then record the skill
   complete in your build ledger before starting the next.

Write from professional craft knowledge: real techniques, real trade-offs,
real numbers where numbers help (e.g., contrast ratios, cadence math, curve
shapes). The worked example in every SKILL.md uses a specific named scenario —
a named fictional product, game, business, or campaign — and shows
intermediate artifacts, not just outcomes.

Retry limit per skill: 2 per failure class, then record the blocker and move
on; never pad to pass. Commit per domain group (7 commits) with messages
`feat: add <domain> skills (<names>)`.

### P4 — Installer + scripts

- `install.py` per `spec/0007`: stdlib-only, the 10-step guided flow, the
  documented flags, the mandatory function seams with their signatures, the
  manifest + backup + uninstall semantics, and every listed safety rule.
  **Pi seam:** verify Pi's agent-file convention against Pi's own
  documentation before writing the Pi target; record what you found (and any
  deviation from `spec/0007`) in `docs/05-installer.md`.
- `scripts/verify_repo.py` implementing the shape checks and installer static
  checks from `spec/0010` (AST import walk, seam signatures, line counting per
  the `spec/0006` counting rule, roster diff against `spec/0005`, reference
  closure, frontmatter validation).
- `scripts/scan_leaks.py` implementing `spec/0008`: token list +
  always-active patterns, `file:line:pattern` output, non-zero exit on match.

Commit: `feat: add installer, verifier, and leak scanner`.

### P5 — Verification (everything in `spec/0010`)

Run, in order, capturing evidence for each:

1. `python3 scripts/verify_repo.py --shape`
2. `python3 scripts/verify_repo.py --installer`
3. `python3 scripts/scan_leaks.py` (with a real maintainer token list if one is
   provided to you; otherwise the example list plus always-active patterns —
   record which in the report)
4. The dry-run matrix: for each cell (hermes / pi / both), redirect `HOME` to a
   fresh scratch directory, run the installer non-interactively, hash the tree
   before and after, assert the target map, verify the manifest hashes, run
   uninstall, and assert the scratch HOME is byte-identical to its pre-install
   state.
5. Fresh-reader check: read `README.md`, one full `SKILL.md`, and one full
   `PROFILE.md` as a stranger; record notes.

Failure protocol per `spec/0010`: fix the class, audit all siblings for the
same flaw, max 3 cycles per failure class, then stop and report.

Commit fixes with `fix:` messages; final commit `chore: verification pass
clean`.

### P6 — Handoff report (your final message)

Report: every check run with its command and result; the profile and skill
inventories with substantive-line counts; the dry-run matrix outcomes
including uninstall round-trips; the Pi-convention finding; any spec conflicts
surfaced; any blockers from P3; an honest list of what is thin and would
benefit from a future pass. Confirm explicitly that no remote was created and
nothing was published.

## First action

`cd ~/devel/hearthandcode/open-source/packages/hearthandcode-agentic-os` and
read `spec/README.md` then every contract in numeric order. Begin P0.
