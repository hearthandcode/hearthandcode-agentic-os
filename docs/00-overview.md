# Overview

## What this is

hearthandcode-agentic-os is a structured agent operating system — eight
specialized agent profiles organized into conceptual layers, supported by
sixteen deep skill packages, all installed into your existing agent harness
(Hermes Agent, Pi, or both) by a guided TUI installer.

It is not a new software platform. It is a **configuration and charter system**
that gives each profile a clear scope, a contract for what it accepts and
delivers, and a set of operating principles that keep you in control.

## How the layers fit together

```
                    Incoming work (vague, multi-part, a new idea)
                              │
                    ┌─────────┴─────────┐
                    │  L1  pathfinder   │  Orientation — scope it, map it, route it
                    └─────────┬─────────┘
                              │ scoped task statement
                              │
          ┌───────────────────┼───────────────────┐
          │                   │                   │
   ┌──────┴──────┐   ┌───────┴───────┐   ┌───────┴──────┐
   │ L2 steward  │   │ L4 waymaker   │   │ L8 archivist │
   │ Stewardship │   │ Planning      │   │ Continuity   │
   └──────┬──────┘   └───────┬───────┘   └───────┬──────┘
          │                  │                    │
          │         ┌────────┴────────┐           │
          │         │  L5 maker      │           │
          │         │  Craft         │           │
          │         └────────┬────────┘           │
          │                  │                    │
          │         ┌────────┴────────┐           │
          │         │  L6 critic      │           │
          │         │  Review         │           │
          │         └────────┬────────┘           │
          │                  │                    │
          │         ┌────────┴────────┐           │
          │         │  L7 herald      │           │
          │         │  Delivery       │           │
          │         └────────┬────────┘           │
          │                  │                    │
          └──────────────────┼────────────────────┘
                             │
                    ┌────────┴────────┐
                    │  L3 librarian   │  Knowledge — sources & claims throughout
                    └─────────────────┘
```

Each layer has a clear seam: what it passes to the next layer and what it
expects back. Profiles are selected manually; collaboration is a
human-mediated handoff described in each profile's charter.

## Quickstart

```bash
git clone <repository-url>              # or unpack the release tarball
cd hearthandcode-agentic-os
python3 install.py                      # guided TUI — follow the prompts
```

The installer detects which harnesses you have, asks for your preferences, and
writes profiles, skills, and scope configuration into the right directories.
After installation:

- **In Hermes Agent:** switch profiles by setting your profile to the desired
  name (e.g., `maker` or `critic`). Skills are loaded automatically from
  `~/.hermes/skills/`.
- **In Pi:** profiles appear as agents in `~/.pi/agent/agents/` and skills in
  `~/.pi/agent/skills/`.

## What you need before starting

- Python 3.9 or later (standard library only — no pip dependencies)
- Hermes Agent (optional) — profiles install to `~/.hermes/`
- Pi agent (optional) — profiles install to `~/.pi/agent/`
- One or both harnesses; the installer works even if neither is detected

## Icons used in this documentation

Throughout the docs, these markers flag important distinctions:

- **🧭 Pathfinder** — orientation and routing
- **🛡️ Steward** — consent and boundaries
- **📚 Librarian** — knowledge and citations
- **🗺️ Waymaker** — planning and decomposition
- **🔧 Maker** — craft and execution
- **🔍 Critic** — review and verification
- **📯 Herald** — delivery and packaging
- **📦 Archivist** — continuity and resumption

## Related documents

| Document | What it covers |
|---|---|
| `01-operating-principles.md` | The four operating principles with concrete examples |
| `02-layer-model.md` | The 8 layers with their seams and collaboration map |
| `03-profiles.md` | When to use each profile, how to switch, how to customize |
| `04-skills.md` | The skill system, the 16 skills, writing your own |
| `05-installer.md` | Installer reference: all flags, targets, manifest format, uninstall |
| `06-extending.md` | Adding profiles and skills, the contracts to follow, submission checklist |