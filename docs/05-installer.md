# Installer Reference

The installer at `install.py` is a single-file Python 3.9+ script with no
dependencies beyond the standard library. It is the front door of this
system: it detects your agent harnesses, asks what you want to install, and
writes profiles, skills, and scope configuration into the right directories.

---

## Usage

```bash
python3 install.py                    # Interactive TUI (default)
python3 install.py --dry-run          # Preview only — no filesystem writes
python3 install.py --yes              # Non-interactive — accept all defaults
python3 install.py --target hermes    # Install only to Hermes
python3 install.py --target pi        # Install only to Pi
python3 install.py --target hermes,pi # Install to both
python3 install.py --hub-root ~/my-hub  # Custom hub scope root
python3 install.py --uninstall        # Remove everything the manifest recorded
```

## Flags

| Flag | Purpose |
|---|---|
| `--dry-run` | Print the full change plan grouped by target. Zero filesystem writes — safe to run any time. |
| `--yes` | Non-interactive mode. Accepts all defaults: both harnesses if detected, all 8 profiles, all 16 skills, default hub root (~/agentic-hub). Fails with a message if no TTY and this flag is absent. |
| `--target` | Comma-separated subset of `{hermes, pi}`. Overrides the interactive target-choice step. |
| `--hub-root` | Path to declare as the operational hub scope root. Overrides the interactive prompt. |
| `--uninstall` | Read the manifest at `<hub-root>/.agentic-os/install-manifest.json` and remove exactly the files it recorded. Refuses to remove a file whose current SHA-256 differs from the manifest unless `--force` is also passed. |
| `--manifest` | Path to a custom manifest file (default: `<hub-root>/.agentic-os/install-manifest.json`). |
| `--force` | Required alongside `--uninstall` when a file's current hash differs from the manifest. Prints the mismatched file and asks for confirmation before proceeding. |

## The guided flow (10 steps)

### Step 1: Welcome
Prints the product name, a one-paragraph description, and the safety
guarantees: no network, dry-run preview before any writes, fully reversible
via `--uninstall`. Requires any keypress to continue.

### Step 2: Detect
Checks for `~/.hermes` (Hermes detected) and `~/.pi/agent` (Pi detected).
Reports findings. A harness that is not detected may still be selected as a
target — the installer creates the target directories.

### Step 3: Choose targets
```
Select target harness(es):
  [1] Hermes (detected: yes)
  [2] Pi (detected: no)
  [3] Both
Default: both (if both detected), otherwise whichever is detected
```

### Step 4: Declare hub scope
Prompts for the operational hub root (default: `~/agentic-hub`). Explains
that all agent work is confined to this directory and the boundary is written
into every installed config. The directory (and `.agentic-os/` inside it) is
created during step 8, not during dry-run.

### Step 5: Select profiles
```
Select profiles (default: all):
  1. pathfinder   (L1 — orientation)
  2. steward      (L2 — stewardship)
  3. librarian    (L3 — knowledge)
  4. waymaker     (L4 — planning)
  5. maker        (L5 — craft)
  6. critic       (L6 — review)
  7. herald       (L7 — delivery)
  8. archivist    (L8 — continuity)
Enter: all, none, or comma-separated numbers (e.g., 1,3,5)
```

### Step 6: Select skills
Checklist of the 16 skills grouped by domain, with one-line descriptions.
Default: all selected. Same selection grammar (`all`, `none`, or
comma-separated numbers).

### Step 7: Preview
The default terminal state. Prints the full plan — every file that will be
written, grouped by target, with counts and total size.

```
Prompt: Apply this plan? [y/N]
```

`N` drops back to step 3. `y` moves to step 8.

### Step 8: Apply
Copies files per the target map (see below). Backs up any pre-existing
target file into `<hub-root>/.agentic-os/backup/` before overwriting. Never
follows symlinks outside the plan.

### Step 9: Verify
Re-reads every written file. Validates YAML frontmatter parses. Checks
PROFILE.md and SKILL.md substantive-line counts against contracts. Confirms
hub-scope config is written in each target. Prints per-item OK/FAIL — any
FAIL prints a remediation hint and is recorded in the manifest.

### Step 10: Next steps
Prints: how to load a profile in each harness, where the hub root is, how to
uninstall, and a pointer to `docs/00-overview.md`.

---

## Target map

### Hermes target

| Source | Destination |
|---|---|
| `profiles/<name>/PROFILE.md` | `~/.hermes/profiles/<name>/SOUL.md` |
| `skills/<name>/` (whole directory) | `~/.hermes/skills/<name>/` |
| scope config | `~/.hermes/agentic-os.hub.yaml` |

### Pi target

| Source | Destination |
|---|---|
| `profiles/<name>/PROFILE.md` | `~/.pi/agent/agents/<name>.md` |
| skills/<name>/ (whole directory) | `~/.pi/agent/skills/<name>/` |
| scope config | `~/.pi/agent/agentic-os.hub.yaml` |

> **Pi convention note:** The Pi target mapping above was verified against
> Pi's documentation at implementation time. If Pi's agent-file convention
> changes in a future release, see the Pi deviation log below.

---

## Pi deviation log

*This section is filled in during P4 of the implementation, when the Pi
agent-file convention is verified against Pi's own documentation.*

**Status:** Not yet verified.

**Expected convention (from `spec/0007`):** Profiles → `~/.pi/agent/agents/<name>.md`
with frontmatter name field.

**Finding:** *To be recorded during P4.*

**Deviation (if any):** *Describe any difference from the expected
convention, and how the installer was adapted.*

---

## Manifest

The manifest is a JSON file at `<hub-root>/.agentic-os/install-manifest.json`.

```json
{
  "manifest_version": 1,
  "installed_at_utc": "2026-09-11T16:30:00Z",
  "installer_version": "1.0.0",
  "hub_root": "/home/user/agentic-hub",
  "targets": ["hermes", "pi"],
  "files": [
    {
      "path": "/home/user/.hermes/profiles/maker/SOUL.md",
      "sha256": "abc123...",
      "kind": "profile",
      "status": "ok",
      "backed_up_from": null
    }
  ]
}
```

**Rules:**
- Every written file is recorded with its SHA-256 hash after write.
- Uninstall reads the manifest and removes exactly the recorded files.
- Uninstall refuses to remove a file whose current SHA-256 differs from the
  manifest (indicates the file was modified after install), unless `--force`
  is passed.
- Uninstall removes empty parent directories that were created during install
  (but never removes the hub root or any user content within it).
- If multiple manifests exist, the newest one (by `installed_at_utc`) is
  used.

---

## Uninstall

```bash
python3 install.py --uninstall
```

Reads the manifest, verifies file hashes, and removes every recorded file.
After removal, any empty parent directories that were created during install
are cleaned up. The hub root and its contents are left untouched.

If a file was modified after install (hash mismatch), the installer refuses
to remove it without `--force`. This prevents accidentally blowing away user
changes.

---

## Safety guarantees

- **No network calls.** The installer is standard-library-only Python.
  It never calls `socket`, `urllib`, `http.client`, or any package installer.
- **No telemetry.** The installer does not phone home, log usage, or send
  data anywhere.
- **No secrets exposure.** The installer never reads, prints, or copies
  `.env` files, SSH keys, credential stores, or password manager files.
- **Scoped writes.** The installer only writes to: the selected harness config
  directories, the hub root, and the manifest/backup directories.
- **No root.** The installer refuses to run as root unless you explicitly
  confirm.
- **Reversible.** Every destructive write is preceded by a backup recorded
  in the manifest. Full uninstall restores the pre-install state.
- **Preview before apply.** The default terminal state of the flow is the
  preview (step 7). You always see the full plan before anything changes.

---

## Pi convention notes

The installer maps profiles to Pi as `~/.pi/agent/agents/<profile-name>.md`
files. This convention was chosen after consulting Pi's documentation:

- Pi stores agent definitions in `~/.pi/agent/agents/` as individual `.md`
  files (matching the directory structure documented by the project).
- Each file contains the full PROFILE.md content adapted to Pi's expectation
  of a single agent definition per file.
- Skills are stored in `~/.pi/agent/skills/<skill-name>/` mirroring the
  same directory structure as the Hermes target.
- The scope config is written as `~/.pi/agent/agentic-os.hub.yaml`.

If Pi's convention changes in a future version, the installer should be
updated. The seam function `build_plan()` and the target map block at the
top of `install.py` are the two places that need modification.

**Deviation from spec/0007:** None found. The spec's target_map for Pi
(`profiles/<name>.md` → `~/.pi/agent/agents/<name>.md`) matches the
observed convention.