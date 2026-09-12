#!/usr/bin/env python3
"""hearthandcode-agentic-os installer — guided TUI, stdlib-only, reversible."""

import argparse
import hashlib
import json
import os
import shutil
import sys
import textwrap
from datetime import datetime, timezone


# ── Constants ────────────────────────────────────────────────────────────────

INSTALLER_VERSION = "1.0.0"
HUB_SCOPE_FILENAME = "agentic-os.hub.yaml"
MANIFEST_FILENAME = "install-manifest.json"
REPO_ROOT = os.path.dirname(os.path.abspath(__file__))

PROFILES_DIR = os.path.join(REPO_ROOT, "profiles")
SKILLS_DIR = os.path.join(REPO_ROOT, "skills")

PROFILE_NAMES = [
    "pathfinder", "steward", "librarian", "waymaker",
    "maker", "critic", "herald", "archivist",
]

SKILL_NAMES = [
    "game-mechanics-design", "level-and-encounter-design", "game-economy-balancing",
    "software-architecture-design", "code-review", "testing-strategy",
    "story-and-narrative-design", "brainstorming-and-ideation",
    "marketing-strategy", "copywriting-and-messaging",
    "business-planning", "operations-and-process-design",
    "social-media-strategy", "content-calendar-planning",
    "ui-design-critique", "design-system-foundations",
]

SKILL_DOMAINS = {
    "game-design": ["game-mechanics-design", "level-and-encounter-design", "game-economy-balancing"],
    "software-development-and-architecture": ["software-architecture-design", "code-review", "testing-strategy"],
    "creative-work": ["story-and-narrative-design", "brainstorming-and-ideation"],
    "marketing": ["marketing-strategy", "copywriting-and-messaging"],
    "business-management": ["business-planning", "operations-and-process-design"],
    "social-media-management": ["social-media-strategy", "content-calendar-planning"],
    "ui-design": ["ui-design-critique", "design-system-foundations"],
}

PROFILE_ROLES = {
    "pathfinder": "L1 — Scope incoming work and route it",
    "steward": "L2 — Guard agency with consent-and-effects",
    "librarian": "L3 — Manage sources, notes, and knowledge",
    "waymaker": "L4 — Turn goals into ordered plans",
    "maker": "L5 — Execute prose, code, and design",
    "critic": "L6 — Verify work against criteria",
    "herald": "L7 — Format and prepare for delivery",
    "archivist": "L8 — Keep work resumable and archived",
}


# ── File Operations ──────────────────────────────────────────────────────────

# Hub layout directory structures (NN-prefixed folders)
HUB_LAYOUTS = {
    "layer-mirror": {
        "agents_template": "hub-templates/layer-mirror/hub-agents-template.md",
        "directories": [
            "01-orientation", "02-stewardship", "03-knowledge",
            "04-planning", "05-craft", "06-review",
            "07-delivery", "08-continuity",
            "09-ops/01-decision-ledger/archive",
            "09-ops/scripts", "09-ops/config",
            "10-archive",
        ],
        "extra_files": [
            ("09-ops/scripts/ack.py", "hub-templates/ack.py"),
        ],
    },
    "workflow-pipeline": {
        "agents_template": "hub-templates/workflow-pipeline/hub-agents-template.md",
        "directories": [
            "01-inbox", "02-scoped", "03-in-progress",
            "04-review", "05-done", "06-archive",
            "07-reference", "08-ops/01-decision-ledger/archive",
            "08-ops/scripts", "08-ops/config",
        ],
        "extra_files": [
            ("08-ops/scripts/ack.py", "hub-templates/ack.py"),
        ],
    },
    "project-centric": {
        "agents_template": "hub-templates/project-centric/hub-agents-template.md",
        "directories": [
            "01-projects", "02-notes", "03-research",
            "04-drafts", "05-templates", "06-archive",
            "07-reference", "08-ops/01-decision-ledger/archive",
            "08-ops/scripts", "08-ops/config",
        ],
        "extra_files": [
            ("08-ops/scripts/ack.py", "hub-templates/ack.py"),
        ],
    },
    "topical-indexed": {
        "agents_template": "hub-templates/topical-indexed/hub-agents-template.md",
        "directories": [
            "01-writing", "02-code", "03-design",
            "04-planning", "05-research", "06-archive",
            "07-templates", "08-meta/01-decision-ledger/archive",
            "08-meta/scripts", "08-meta/config",
        ],
        "extra_files": [
            ("08-meta/scripts/ack.py", "hub-templates/ack.py"),
        ],
    },
}
# Set of all source files from hub-templates/ that need to ship
HUB_TEMPLATE_SOURCES = set()
for cfg in HUB_LAYOUTS.values():
    HUB_TEMPLATE_SOURCES.add(cfg["agents_template"])
    for _, src in cfg["extra_files"]:
        HUB_TEMPLATE_SOURCES.add(src)

LAYOUT_NAMES = list(HUB_LAYOUTS.keys())

class FileOp:
    """A single file operation: copy source to dest with kind metadata."""
    __slots__ = ("source", "dest", "kind")

    def __init__(self, source, dest, kind):
        self.source = source
        self.dest = dest
        self.kind = kind


def sha256_file(path):
    """Return hex SHA-256 of file at path."""
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def copy_with_backup(source, dest, backup_dir):
    """Copy source to dest, backing up any existing dest first."""
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    backed_up = None
    if os.path.exists(dest):
        backup_path = os.path.join(backup_dir, os.path.relpath(dest, "/").replace("/", "_"))
        os.makedirs(os.path.dirname(backup_path), exist_ok=True)
        shutil.copy2(dest, backup_path)
        backed_up = dest
    shutil.copy2(source, dest)
    return backed_up


# ── Detection ────────────────────────────────────────────────────────────────

def detect_harnesses():
    """Detect which agent harnesses are installed."""
    hermes_dir = os.path.expanduser("~/.hermes")
    pi_dir = os.path.expanduser("~/.pi/agent")
    return {
        "hermes": os.path.isdir(hermes_dir),
        "pi": os.path.isdir(pi_dir),
    }


def choose_targets(detected, flags):
    """Return list of target harness names."""
    if flags.target:
        parts = [t.strip().lower() for t in flags.target.split(",")]
        valid = set()
        for p in parts:
            if p in ("hermes", "pi"):
                valid.add(p)
        return sorted(valid)
    print()
    print("Select installation target(s):")
    print("  [1] Hermes Agent")
    print("  [2] Pi agent")
    print("  [3] Both")
    default = "3"
    if not detected["hermes"] and not detected["pi"]:
        default = "3"
    elif detected["hermes"] and not detected["pi"]:
        default = "1"
    elif not detected["hermes"] and detected["pi"]:
        default = "2"
    choice = input(f"Choice [1-3] (default {default}): ").strip() or default
    if choice == "1":
        return ["hermes"]
    elif choice == "2":
        return ["pi"]
    else:
        return ["hermes", "pi"]


def declare_hub_root(flags):
    """Return absolute hub root path, validated."""
    if flags.hub_root:
        path = os.path.abspath(flags.hub_root)
    else:
        default = os.path.expanduser("~/agentic-hub")
        print()
        path_input = input(f"Hub scope root directory (default {default}): ").strip()
        path = os.path.abspath(path_input) if path_input else default

    path = os.path.abspath(path)
    if path == os.path.expanduser("~") or path == "/":
        print("ERROR: Hub root cannot be your home directory or the root filesystem.")
        sys.exit(1)
    parent = os.path.dirname(path)
    if parent and not os.access(parent, os.W_OK):
        print(f"ERROR: Parent directory {parent} is not writable.")
        sys.exit(1)
    return path


def select_components(roster, kind, flags):
    """Return list of selected component names from roster."""
    if flags.yes:
        return list(roster.keys())

    print()
    print(f"Select {kind} to install:")
    items = list(roster.items())
    for i, (name, desc) in enumerate(items, 1):
        print(f"  [{i}] {name}  — {desc}")

    raw = input("Enter comma-separated numbers, 'all', or 'none' (default all): ").strip().lower()
    if not raw or raw == "all":
        return list(roster.keys())
    if raw == "none":
        return []
    selected = []
    for part in raw.split(","):
        part = part.strip()
        if part.isdigit():
            idx = int(part) - 1
            if 0 <= idx < len(items):
                selected.append(items[idx][0])
    return selected


def build_plan(targets, hub_root, profiles, skills, hub_layout="layer-mirror"):
    """Build a list of FileOps for the installation. Includes hub directory structure."""
    plan = []

    # Add hub directory structure and AGENTS.md from template
    layout_cfg = HUB_LAYOUTS.get(hub_layout, HUB_LAYOUTS["layer-mirror"])
    # Create hub root directory itself
    plan.append(FileOp(None, hub_root, "hub-dir"))
    # AGENTS.md
    agents_src = os.path.join(REPO_ROOT, layout_cfg["agents_template"])
    agents_dst = os.path.join(hub_root, "AGENTS.md")
    if os.path.isfile(agents_src):
        plan.append(FileOp(agents_src, agents_dst, "hub-agents"))
    # Directories
    for rel_dir in layout_cfg["directories"]:
        dst = os.path.join(hub_root, rel_dir)
        plan.append(FileOp(None, dst, "hub-dir"))
    # Extra files (ack.py, etc.)
    for rel_dst, rel_src in layout_cfg["extra_files"]:
        extra_src = os.path.join(REPO_ROOT, rel_src)
        extra_dst = os.path.join(hub_root, rel_dst)
        if os.path.isfile(extra_src):
            plan.append(FileOp(extra_src, extra_dst, "hub-script"))
    # Add decision-ledger README.md stub
    ledger_root = [d for d in layout_cfg["directories"] if "decision-ledger" in d]
    if ledger_root:
        # Find the decision-ledger directory (parent of archive/)
        ledger_dir = os.path.dirname(ledger_root[0])
        ledger_path = os.path.join(hub_root, ledger_dir, "README.md")
        if not any(op.dest == ledger_path for op in plan):
            plan.append(FileOp(None, ledger_path, "hub-manifest"))

    for target in targets:
        if target == "hermes":
            base = os.path.expanduser("~/.hermes")
            for pname in profiles:
                src = os.path.join(PROFILES_DIR, pname, "PROFILE.md")
                dst = os.path.join(base, "profiles", pname, "SOUL.md")
                plan.append(FileOp(src, dst, "profile"))
            for sname in skills:
                skill_src = os.path.join(SKILLS_DIR, sname)
                if not os.path.isdir(skill_src):
                    continue
                skill_dst_base = os.path.join(base, "skills", sname)
                for root, dirs, files in os.walk(skill_src):
                    for fn in files:
                        src = os.path.join(root, fn)
                        rel = os.path.relpath(src, skill_src)
                        dst = os.path.join(skill_dst_base, rel)
                        plan.append(FileOp(src, dst, "skill"))
            scope_dst = os.path.join(base, HUB_SCOPE_FILENAME)
            plan.append(FileOp(None, scope_dst, "config"))

        elif target == "pi":
            base = os.path.expanduser("~/.pi/agent")
            for pname in profiles:
                src = os.path.join(PROFILES_DIR, pname, "PROFILE.md")
                dst = os.path.join(base, "agents", f"{pname}.md")
                plan.append(FileOp(src, dst, "profile"))
            for sname in skills:
                skill_src = os.path.join(SKILLS_DIR, sname)
                if not os.path.isdir(skill_src):
                    continue
                skill_dst_base = os.path.join(base, "skills", sname)
                for root, dirs, files in os.walk(skill_src):
                    for fn in files:
                        src = os.path.join(root, fn)
                        rel = os.path.relpath(src, skill_src)
                        dst = os.path.join(skill_dst_base, rel)
                        plan.append(FileOp(src, dst, "skill"))
            scope_dst = os.path.join(base, HUB_SCOPE_FILENAME)
            plan.append(FileOp(None, scope_dst, "config"))

    return plan


def preview_plan(plan):
    """Print the plan grouped by target."""
    groups = {}
    for op in plan:
        groups.setdefault(op.kind, []).append(op)

    total_size = 0
    counts = {}
    for op in plan:
        if op.source and os.path.isfile(op.source):
            total_size += os.path.getsize(op.source)
        counts[op.kind] = counts.get(op.kind, 0) + 1

    print()
    print("╔══════════════════════════════════════════╗")
    print("║         Installation Plan Preview        ║")
    print("╚══════════════════════════════════════════╝")
    for kind, ops in sorted(groups.items()):
        print(f"\n  {kind.upper()} ({len(ops)} files):")
        for op in ops[:5]:
            print(f"    → {op.dest}")
        if len(ops) > 5:
            print(f"    ... and {len(ops) - 5} more")
    print(f"\n  Total: {sum(counts.values())} files, ~{total_size // 1024} KB")
    print()


def apply_plan(plan, backup_dir):
    """Execute the plan, returning results list."""
    os.makedirs(backup_dir, exist_ok=True)
    results = []
    for op in plan:
        try:
            sha = None
            backed_up = None
            if op.source is None:
                # Hub directory or manifest stub
                if op.kind == "hub-dir":
                    os.makedirs(op.dest, exist_ok=True)
                    results.append({"path": op.dest, "sha256": None, "kind": op.kind, "status": "ok", "backed_up_from": None})
                    continue
                elif op.kind == "hub-manifest":
                    # Decision ledger README stub
                    os.makedirs(os.path.dirname(op.dest), exist_ok=True)
                    if not os.path.exists(op.dest):
                        with open(op.dest, "w") as f:
                            f.write("# Decision Ledger — Active\n\nAppend-only record of every ACK. One fenced YAML block per entry.\n")
                    sha = sha256_file(op.dest) if os.path.isfile(op.dest) else None
                else:
                    # config file — write inline content
                    os.makedirs(os.path.dirname(op.dest), exist_ok=True)
                    content = _scope_config_content(None)
                    if os.path.exists(op.dest):
                        backed_up = os.path.dirname(op.dest)
                    with open(op.dest, "w") as f:
                        f.write(content)
                    sha = sha256_file(op.dest)
            else:
                if not os.path.isfile(op.source):
                    continue
                backed_up = copy_with_backup(op.source, op.dest, backup_dir)
                sha = sha256_file(op.dest)

            results.append({
                "path": op.dest,
                "sha256": sha,
                "kind": op.kind,
                "status": "ok",
                "backed_up_from": backed_up,
            })
        except Exception as e:
            results.append({
                "path": op.dest,
                "sha256": None,
                "kind": op.kind,
                "status": "failed",
                "error": str(e),
            })
    return results


def _scope_config_content(hub_root):
    """Generate hub scope YAML content."""
    return textwrap.dedent(f"""\
        hub_root: {hub_root if hub_root else '<hub-root-placeholder>'}
        installed_by: hearthandcode-agentic-os installer
        version: {INSTALLER_VERSION}
        note: >
          Agent work is confined to hub_root. Profiles installed by this package
          reference this file; treat any write outside hub_root as requiring
          explicit user instruction.
        """)


# ── Verification ─────────────────────────────────────────────────────────────

def verify_install(results):
    """Run per-file verification checks."""
    print()
    print("Verification:")
    all_ok = True
    for r in results:
        status = "OK" if r["status"] == "ok" else "FAIL"
        if r["status"] != "ok":
            all_ok = False
        print(f"  [{status}] {r['path']}")
        if r.get("error"):
            print(f"         Error: {r['error']}")
            print("         Remediation: Check file permissions and available disk space.")
    return all_ok


def write_manifest(results, hub_root):
    """Write the installation manifest."""
    manifest = {
        "manifest_version": 1,
        "installed_at_utc": datetime.now(timezone.utc).isoformat(),
        "installer_version": INSTALLER_VERSION,
        "hub_root": hub_root,
        "files": results,
    }
    manifest_dir = os.path.join(hub_root, ".agentic-os")
    os.makedirs(manifest_dir, exist_ok=True)
    manifest_path = os.path.join(manifest_dir, MANIFEST_FILENAME)
    with open(manifest_path, "w") as f:
        json.dump(manifest, f, indent=2)
    return manifest_path


def uninstall(manifest_path, force=False):
    """Remove files recorded in manifest."""
    if not os.path.isfile(manifest_path):
        print(f"ERROR: Manifest not found at {manifest_path}")
        return {"removed": 0, "errors": []}

    with open(manifest_path) as f:
        manifest = json.load(f)

    removed = 0
    errors = []
    for entry in manifest.get("files", []):
        path = entry["path"]
        if not os.path.exists(path):
            continue
        if not force and entry.get("sha256"):
            current = sha256_file(path)
            if current != entry["sha256"]:
                errors.append(f"SKIPPED: {path} (sha256 mismatch — use --force to override)")
                continue
        try:
            os.remove(path)
            removed += 1
            # Remove empty parent directories
            parent = os.path.dirname(path)
            while parent and parent != "/":
                try:
                    if os.path.isdir(parent) and not os.listdir(parent):
                        os.rmdir(parent)
                    else:
                        break
                except OSError:
                    break
                parent = os.path.dirname(parent)
        except Exception as e:
            errors.append(f"ERROR removing {path}: {e}")

    return {"removed": removed, "errors": errors}


# ── The Guided Flow ──────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="hearthandcode-agentic-os installer — guided TUI, stdlib-only"
    )
    parser.add_argument("--dry-run", action="store_true",
                        help="Print full change plan and exit; never touches filesystem")
    parser.add_argument("--yes", action="store_true",
                        help="Non-interactive; accept all defaults")
    parser.add_argument("--target", type=str,
                        help="Comma subset of {hermes, pi}; overrides interactive target choice")
    parser.add_argument("--hub-root", type=str,
                        help="Path; overrides interactive hub-root prompt")
    parser.add_argument("--hub-layout", type=str, default=None,
                        choices=["layer-mirror", "workflow-pipeline", "project-centric", "topical-indexed"],
                        help="Hub directory layout template")
    parser.add_argument("--setup-docker", action="store_true",
                        help="Generate docker-compose.yaml for selected targets after install")
    parser.add_argument("--uninstall", action="store_true",
                        help="Remove exactly what the recorded manifest installed, then exit")
    parser.add_argument("--manifest", type=str,
                        help="Path to manifest file (default: <hub-root>/.agentic-os/install-manifest.json)")
    flags = parser.parse_args()

    # ── Step 0: Non-interactive handling ──
    if not sys.stdin.isatty() and not flags.yes:
        print("ERROR: Non-interactive terminal requires --yes or a specific flag.")
        print("Usage: python3 install.py --yes")
        sys.exit(1)

    if flags.uninstall:
        if flags.manifest:
            manifest_path = os.path.abspath(flags.manifest)
        else:
            # Try to find manifest in default locations
            for candidate in [
                os.path.expanduser("~/.hermes/agentic-os.hub.yaml"),
                os.path.expanduser("~/.pi/agent/agentic-os.hub.yaml"),
            ]:
                if os.path.isfile(candidate):
                    hub_root = os.path.dirname(candidate)
                    manifest_path = os.path.join(hub_root, ".agentic-os", MANIFEST_FILENAME)
                    break
            else:
                print("ERROR: No manifest found. Specify --manifest path.")
                sys.exit(1)
        result = uninstall(manifest_path, force=flags.yes)
        print(f"Uninstall complete: {result['removed']} files removed")
        for err in result.get("errors", []):
            print(f"  {err}")
        return

    # ── Step 1: Welcome ──
    if not flags.yes:
        print()
        print("╔══════════════════════════════════════════════════╗")
        print("║        hearthandcode-agentic-os  Installer      ║")
        print("╚══════════════════════════════════════════════════╝")
        print()
        print("This installer will set up eight layered agent profiles and")
        print("sixteen domain skills in your Hermes Agent or Pi agent harness.")
        print()
        print("Safety guarantees:")
        print("  • No network calls ever")
        print("  • Dry-run preview before any write")
        print("  • Fully reversible (backup + manifest + uninstall)")
        print()
        input("Press Enter to continue...")

    # ── Step 2: Detect harnesses ──
    detected = detect_harnesses()
    if not flags.yes:
        print()
        print("Detected harnesses:")
        print(f"  Hermes: {'✓' if detected['hermes'] else '—'}")
        print(f"  Pi:     {'✓' if detected['pi'] else '—'}")

    # ── Step 3: Choose targets ──
    targets = choose_targets(detected, flags)

    # ── Step 4: Declare hub root ──
    hub_root = declare_hub_root(flags)

    # ── Step 5: Select profiles ──
    profile_roster = PROFILE_NAMES
    profiles = select_components(
        {n: PROFILE_ROLES[n] for n in profile_roster},
        "profiles", flags
    )

    # ── Step 6: Select skills ──
    skill_roster = {s: SKILL_DOMAINS.get(
        next(d for d, names in SKILL_DOMAINS.items() if s in names), "other"
    ) for s in SKILL_NAMES}
    skills = select_components(
        {s: f"({skill_roster[s]})" for s in SKILL_NAMES},
        "skills", flags
    )

    # ── Step 6b: Choose hub layout ──
    LAYOUT_DESC = {
        "layer-mirror": "Default 8-layer model mirror (01-orientation..08-continuity)",
        "workflow-pipeline": "Task stage pipeline (01-inbox..05-done)",
        "project-centric": "Portfolio by project (01-projects..06-archive)",
        "topical-indexed": "Discipline groups (01-writing..05-research)",
    }
    layout = flags.hub_layout
    if not layout and not flags.yes:
        print("\n── Hub Layout Selection ──\n")
        print("Choose the directory structure for your hub root:")
        for i, name in enumerate(LAYOUT_NAMES, 1):
            print(f"  [{i}] {name}: {LAYOUT_DESC[name]}")
        print(f"  Default: {LAYOUT_NAMES[0]}")
        choice = input(f"Select layout [1-4] (default 1): ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(LAYOUT_NAMES):
            layout = LAYOUT_NAMES[int(choice) - 1]
        else:
            layout = LAYOUT_NAMES[0]
    elif not layout:
        layout = LAYOUT_NAMES[0]
    hub_layout = layout

    # ── Step 7: Preview ──
    plan = build_plan(targets, hub_root, profiles, skills, hub_layout)
    preview_plan(plan)

    if flags.dry_run:
        print("--dry-run: Plan printed above. No files were written.")
        return

    if not flags.yes:
        proceed = input("Apply this plan? [y/N]: ").strip().lower()
        if proceed != "y":
            print("Installation cancelled.")
            return

    # ── Step 8: Apply ──
    backup_dir = os.path.join(hub_root, ".agentic-os", "backup")
    results = apply_plan(plan, backup_dir)

    # Write scope config files (the config entries in the plan had hub_root=None)
    for target in targets:
        if target == "hermes":
            config_path = os.path.expanduser("~/.hermes/agentic-os.hub.yaml")
        else:
            config_path = os.path.expanduser("~/.pi/agent/agentic-os.hub.yaml")
        os.makedirs(os.path.dirname(config_path), exist_ok=True)
        with open(config_path, "w") as f:
            f.write(_scope_config_content(hub_root))
        results.append({
            "path": config_path,
            "sha256": sha256_file(config_path),
            "kind": "config",
            "status": "ok",
            "backed_up_from": None,
        })

    # ── Step 9: Verify ──
    all_ok = verify_install(results)

    # ── Write manifest ──
    manifest_path = write_manifest(results, hub_root)
    print(f"\nManifest written to: {manifest_path}")

    # ── Step 10: Next steps ──
    print()
    print("Installation complete!")
    print()
    install_locations = {
        "hermes": ("~/.hermes/profiles/", "~/.hermes/skills/"),
        "pi": ("~/.pi/agent/agents/", "~/.pi/agent/skills/"),
    }
    for target in targets:
        profiles_path, skills_path = install_locations[target]
        print(f"  {target.capitalize()} profiles installed to: {profiles_path}")
        print(f"  {target.capitalize()} skills installed to: {skills_path}")
        print()
    print(f"  Hub scope root: {hub_root}")
    print(f"  To load a profile: select the profile in your harness")
    print(f"  To uninstall: python3 install.py --uninstall")
    print(f"  Docs: docs/00-overview.md")
    print()

    if not all_ok:
        print("WARNING: Some files failed verification. Check the output above.")
        sys.exit(1)

    # ── Step 11: Generate Docker compose (optional) ──
    setup_docker = flags.setup_docker
    if not setup_docker and not flags.yes:
        try:
            resp = input("\nGenerate Docker Compose for these targets? [y/N]: ").strip().lower()
            setup_docker = resp == "y"
        except (EOFError, KeyboardInterrupt):
            setup_docker = False
    if setup_docker:
        _generate_docker_compose(targets, hub_root)


def _generate_docker_compose(targets, hub_root):
    """Write a docker-compose.yaml based on selected targets."""
    docker_dir = os.path.join(REPO_ROOT, "docker")
    os.makedirs(docker_dir, exist_ok=True)
    compose_path = os.path.join(docker_dir, "compose.yaml")

    services = {}
    volumes = {}

    for t in targets:
        svc = t.capitalize()
        config_vol = f"agentic-os-{t}-config"
        services[t] = {
            "build": {
                "context": str(REPO_ROOT),
                "dockerfile": f"docker/Dockerfile.{t}",
            },
            "container_name": f"agentic-os-{t}",
            "stdin_open": True,
            "tty": True,
            "volumes": [
                f"{config_vol}:/home/user/.{t}",
                f"agentic-os-hub:/home/user/agentic-hub",
            ],
        }
        volumes[config_vol] = {}

    volumes["agentic-os-hub"] = {}

    compose = {
        "version": "3.9",
        "services": services,
        "volumes": volumes,
    }

    # Write with human-readable YAML (no PyYAML dependency)
    lines = [
        "# compose.yaml — hearthandcode-agentic-os Docker Compose",
        f"# Generated by: install.py (targets: {', '.join(targets)})",
        "# Usage: docker compose -f docker/compose.yaml up",
        "",
        'version: "3.9"',
        "",
        "services:",
    ]
    for t in targets:
        svc = t.capitalize()
        lines.extend([
            f"  {t}:",
            f"    build:",
            f"      context: ..",
            f"      dockerfile: docker/Dockerfile.{t}",
            f"    container_name: agentic-os-{t}",
            f"    stdin_open: true",
            f"    tty: true",
            f"    volumes:",
            f"      - agentic-os-{t}-config:/home/user/.{t}",
            f"      - agentic-os-hub:/home/user/agentic-hub",
            "",
        ])
    lines.append("volumes:")
    for t in targets:
        lines.append(f"  agentic-os-{t}-config:")
    lines.append("  agentic-os-hub:")

    with open(compose_path, "w") as f:
        f.write("\n".join(lines) + "\n")

    print(f"\n  Docker Compose generated: {compose_path}")
    print(f"  Build: docker compose -f docker/compose.yaml build")
    print(f"  Run:   docker compose -f docker/compose.yaml up")


if __name__ == "__main__":
    main()