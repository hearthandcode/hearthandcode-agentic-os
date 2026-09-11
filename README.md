# hearthandcode-agentic-os

**Eight layered agent profiles. Sixteen chartered skills. One guided installer. Your own structured agent operating system.**

This is a starter system for anyone who wants a structured, principled way to work with AI agents (Hermes Agent, Pi, or both) without designing one from scratch. Instead of one generic helper, you get eight specialized profile roles — each scoped to one layer of work — and sixteen deep skill packages for game design, software architecture, creative work, marketing, business ops, social media, and UI design.

Every profile follows the same five operating principles:

- **Consent-and-effects** — The agent names what it will change and asks first.
- **Hub-scope confinement** — Work stays inside a declared directory root.
- **Claim labels** — Every factual claim is marked as source, evidence, guess, or unknown.
- **Pause-and-ask** — Under uncertainty, the agent pauses instead of guessing.
- **You own every decision** — The profile recommends; you decide.

---

## The 8 layers at a glance

| Layer | Profile | What it does |
|---|---|---|
| L1 Orientation | **pathfinder** | Scopes incoming work, maps the hub, routes tasks |
| L2 Stewardship | **steward** | Names effects before they happen, guards your agency |
| L3 Knowledge | **librarian** | Captures sources, labels claims, answers from notes |
| L4 Planning | **waymaker** | Decomposes goals into ordered steps with done-criteria |
| L5 Craft | **maker** | Executes build work — prose, code, designs |
| L6 Review | **critic** | Verifies work against its criteria, finds problems |
| L7 Delivery | **herald** | Formats and packages reviewed work for its audience |
| L8 Continuity | **archivist** | Keeps work resumable across sessions |

These are **conceptual neighborhoods**, not software daemons. You select the profile whose layer matches the work you're doing right now.

---

## Quickstart

```bash
git clone <repository-url>
cd hearthandcode-agentic-os
python3 install.py
```

The installer walks you through ten steps:

1. Welcome and safety guarantees
2. Detect which agent harnesses you have (Hermes Agent, Pi, or both)
3. Choose target harness(es)
4. Declare your hub scope root (default `~/agentic-hub`)
5. Select profiles (all 8 by default)
6. Select skills (all 16 by default)
7. Preview the full change plan
8. Apply (with automated backup of any existing files)
9. Verify every written file
10. Print next-step instructions

**What gets installed where:**

| Component | Hermes | Pi |
|---|---|---|
| Profiles | `~/.hermes/profiles/<name>/SOUL.md` | `~/.pi/agent/agents/<name>.md` |
| Skills | `~/.hermes/skills/<name>/` (whole directory) | `~/.pi/agent/skills/<name>/` (whole directory) |
| Scope config | `~/.hermes/agentic-os.hub.yaml` | `~/.pi/agent/agentic-os.hub.yaml` |

The installer creates a manifest at `<hub-root>/.agentic-os/install-manifest.json` recording every file it wrote, with SHA-256 hashes. This enables clean uninstall.

### Uninstall

```bash
python3 install.py --uninstall
```

Reads the manifest, removes every recorded file, and cleans empty parent directories. The hub root and your user content are left untouched.

### Dry-run preview

```bash
python3 install.py --dry-run
```

Prints the full change plan without touching the filesystem.

---

## After installation

- **Load a profile** in Hermes: set your profile to the desired name (e.g., `pathfinder`). Each profile's `SOUL.md` charter contains the when-to-use guidance in its recognition section.
- **Load a skill** in Hermes: skills are loaded by the skill management system. The `docs/` directory in this repository has the full documentation.
- **Your hub scope** is the directory you declared at install — all agent work is confined there.

---

## Documentation

| Doc | What it covers |
|---|---|
| `docs/00-overview.md` | One-page system overview and quickstart |
| `docs/01-operating-principles.md` | The four operating principles with examples |
| `docs/02-layer-model.md` | Full layer model with collaboration map |
| `docs/03-profiles.md` | Profile user's guide: when to use each, how to switch |
| `docs/04-skills.md` | Skill system: anatomy, the 16 skills, writing your own |
| `docs/05-installer.md` | Installer reference: flags, targets, manifest, uninstall |
| `docs/06-extending.md` | Extender's guide: adding profiles/skills + submission checklist |

---

## Contributing

See `CONTRIBUTING.md` for how to propose new skills or profiles.

## License

MIT — see `LICENSE`.