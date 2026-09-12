#!/usr/bin/env python3
"""Offline verification for the dedicated Pi-Ember Agentic OS harness."""

from __future__ import annotations

import hashlib
import json
import os
import socket
import sys
from pathlib import Path

SOURCE_ROOT = Path("/opt/hearthandcode-agentic-os")
PI_AGENT_DIR = Path(os.environ.get("PI_CODING_AGENT_DIR", "/home/pi/.pi/agent"))

PROFILE_NAMES = (
    "pathfinder", "steward", "librarian", "waymaker",
    "maker", "critic", "herald", "archivist",
)
SKILL_NAMES = (
    "game-mechanics-design", "level-and-encounter-design", "game-economy-balancing",
    "software-architecture-design", "code-review", "testing-strategy",
    "story-and-narrative-design", "brainstorming-and-ideation",
    "marketing-strategy", "copywriting-and-messaging",
    "business-planning", "operations-and-process-design",
    "social-media-strategy", "content-calendar-planning",
    "ui-design-critique", "design-system-foundations",
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def frontmatter(path: Path) -> dict[str, str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0] != "---":
        return {}
    fields: dict[str, str] = {}
    for line in lines[1:]:
        if line == "---":
            return fields
        if ":" in line and not line.startswith((" ", "\t")):
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip()
    return {}


def assert_file_matches(source: Path, destination: Path, label: str) -> None:
    if not destination.is_file():
        raise AssertionError(f"missing {label}: {destination}")
    if sha256(source) != sha256(destination):
        raise AssertionError(f"content mismatch for {label}: {destination}")


def check_profiles() -> None:
    for name in PROFILE_NAMES:
        source = SOURCE_ROOT / "profiles" / name / "PROFILE.md"
        destination = PI_AGENT_DIR / "agents" / f"{name}.md"
        assert_file_matches(source, destination, f"profile {name}")
        metadata = frontmatter(destination)
        if metadata.get("name") != name or not metadata.get("description"):
            raise AssertionError(f"profile {name} lacks Pi agent name/description frontmatter")


def check_skills() -> None:
    for name in SKILL_NAMES:
        source_dir = SOURCE_ROOT / "skills" / name
        destination_dir = PI_AGENT_DIR / "skills" / name
        source_files = sorted(path for path in source_dir.rglob("*") if path.is_file())
        destination_files = sorted(path for path in destination_dir.rglob("*") if path.is_file())
        source_relative = {path.relative_to(source_dir) for path in source_files}
        destination_relative = {path.relative_to(destination_dir) for path in destination_files}
        if source_relative != destination_relative:
            raise AssertionError(f"skill {name} file set differs from its source package")
        for relative in source_relative:
            assert_file_matches(source_dir / relative, destination_dir / relative, f"skill {name}/{relative}")
        metadata = frontmatter(destination_dir / "SKILL.md")
        if metadata.get("name") != name or not metadata.get("description"):
            raise AssertionError(f"skill {name} is not valid Pi Agent Skills metadata")


def check_manifest_and_scope() -> Path:
    scope_path = PI_AGENT_DIR / "agentic-os.hub.yaml"
    scope = scope_path.read_text(encoding="utf-8")
    hub_line = next((line for line in scope.splitlines() if line.startswith("hub_root:")), "")
    if not hub_line:
        raise AssertionError("Pi scope configuration has no hub_root")
    hub_root = Path(hub_line.split(":", 1)[1].strip())
    if not hub_root.is_absolute() or not hub_root.is_dir():
        raise AssertionError("Pi scope configuration does not name an existing absolute hub root")
    manifest_path = hub_root / ".agentic-os" / "install-manifest.json"
    if not manifest_path.is_file():
        raise AssertionError(f"missing install manifest: {manifest_path}")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if manifest.get("hub_root") != str(hub_root):
        raise AssertionError("manifest hub_root does not match Pi scope configuration")
    return hub_root


def check_offline_boundary() -> None:
    if os.environ.get("PI_OFFLINE") != "1":
        raise AssertionError("PI_OFFLINE is not enabled")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as probe:
        probe.settimeout(1)
        try:
            probe.connect(("1.1.1.1", 53))
        except OSError:
            return
    raise AssertionError("network connection unexpectedly succeeded; expected network_mode: none")


def main() -> None:
    check_profiles()
    check_skills()
    hub_root = check_manifest_and_scope()
    check_offline_boundary()
    print(f"PASS profiles=8 skills=16 files=source-identical scope={hub_root} network=blocked")


if __name__ == "__main__":
    try:
        main()
    except (AssertionError, OSError, ValueError, json.JSONDecodeError) as error:
        print(f"FAIL {error}", file=sys.stderr)
        raise SystemExit(1)
