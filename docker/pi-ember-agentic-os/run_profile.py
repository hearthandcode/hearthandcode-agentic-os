#!/usr/bin/env python3
"""Run one installed Agentic OS profile as Pi's explicit system prompt."""

from __future__ import annotations

import os
import sys
from pathlib import Path

ALLOWED_PROFILES = {
    "pathfinder", "steward", "librarian", "waymaker",
    "maker", "critic", "herald", "archivist",
}
PI_AGENT_DIR = Path(os.environ.get("PI_CODING_AGENT_DIR", "/home/pi/.pi/agent"))


def main() -> None:
    if len(sys.argv) < 2 or sys.argv[1] not in ALLOWED_PROFILES:
        available = ", ".join(sorted(ALLOWED_PROFILES))
        raise SystemExit(f"usage: run_profile.py <profile> [pi arguments]; profiles: {available}")
    profile_name = sys.argv[1]
    profile_path = PI_AGENT_DIR / "agents" / f"{profile_name}.md"
    if not profile_path.is_file():
        raise SystemExit(f"profile is not installed: {profile_path}; run launcher install first")
    prompt = profile_path.read_text(encoding="utf-8")
    os.execvp("pi", ["pi", "--system-prompt", prompt, *sys.argv[2:]])


if __name__ == "__main__":
    main()
