#!/usr/bin/env python3
"""
hearthandcode-agentic-os repository verifier.
Usage:
  python3 scripts/verify_repo.py --shape     # Check profiles, skills, references
  python3 scripts/verify_repo.py --installer # Static checks on install.py
"""

import argparse
import os
import sys
import json

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PROFILES_DIR = os.path.join(REPO_ROOT, "profiles")
SKILLS_DIR = os.path.join(REPO_ROOT, "skills")
INSTALLER = os.path.join(REPO_ROOT, "install.py")

EXPECTED_PROFILES = [
    "pathfinder", "steward", "librarian", "waymaker",
    "maker", "critic", "herald", "archivist",
]

EXPECTED_SKILLS = [
    "game-mechanics-design", "level-and-encounter-design", "game-economy-balancing",
    "software-architecture-design", "code-review", "testing-strategy",
    "story-and-narrative-design", "brainstorming-and-ideation",
    "marketing-strategy", "copywriting-and-messaging",
    "business-planning", "operations-and-process-design",
    "social-media-strategy", "content-calendar-planning",
    "ui-design-critique", "design-system-foundations",
]

# Per-skill reference manifest from 0005
SKILL_REFERENCES = {
    "game-mechanics-design": [
        "core-loop-design.md", "mechanics-taxonomy.md", "player-motivation-models.md",
        "prototyping-playbook.md", "mechanics-documentation.md", "balancing-fundamentals.md",
        "playtesting-methods.md", "mechanics-case-studies.md",
    ],
    "level-and-encounter-design": [
        "level-design-principles.md", "pacing-and-difficulty-curves.md", "encounter-design-patterns.md",
        "spatial-composition.md", "narrative-through-environment.md", "level-metrics-and-telemetry.md",
        "playtesting-levels.md", "level-case-studies.md",
    ],
    "game-economy-balancing": [
        "economy-design-fundamentals.md", "currencies-and-resources.md", "progression-systems.md",
        "monetization-ethics.md", "economy-modeling.md", "tuning-and-balancing-methods.md",
        "live-economy-monitoring.md", "economy-case-studies.md",
    ],
    "software-architecture-design": [
        "architecture-decision-records.md", "architecture-styles-catalog.md",
        "quality-attribute-scenarios.md", "component-decomposition.md",
        "api-design-principles.md", "data-modeling-basics.md",
        "architecture-review-checklist.md", "architecture-case-studies.md",
    ],
    "code-review": [
        "review-principles.md", "review-checklist.md", "security-review-basics.md",
        "performance-review-basics.md", "readability-and-style.md",
        "giving-and-receiving-feedback.md", "review-automation.md", "review-case-studies.md",
    ],
    "testing-strategy": [
        "testing-pyramid.md", "test-design-techniques.md", "unit-testing-patterns.md",
        "integration-testing-patterns.md", "property-and-fuzz-testing.md",
        "test-data-management.md", "ci-test-pipelines.md", "testing-case-studies.md",
    ],
    "story-and-narrative-design": [
        "story-structure-models.md", "character-design.md", "worldbuilding-methods.md",
        "dialogue-craft.md", "theme-and-motif.md", "narrative-outlining.md",
        "revision-and-editing.md", "story-case-studies.md",
    ],
    "brainstorming-and-ideation": [
        "ideation-principles.md", "divergence-techniques.md", "convergence-techniques.md",
        "constraint-based-creativity.md", "idea-evaluation-rubrics.md",
        "facilitation-guide.md", "ideation-capture-and-triage.md", "ideation-case-studies.md",
    ],
    "marketing-strategy": [
        "marketing-fundamentals.md", "positioning-and-differentiation.md", "audience-research.md",
        "messaging-frameworks.md", "channel-strategy.md", "campaign-planning.md",
        "marketing-metrics.md", "strategy-case-studies.md",
    ],
    "copywriting-and-messaging": [
        "copywriting-principles.md", "voice-and-tone.md", "headline-and-hook-craft.md",
        "long-form-vs-short-form.md", "conversion-copywriting.md",
        "editing-and-tightening.md", "a-b-testing-copy.md", "copy-case-studies.md",
    ],
    "business-planning": [
        "business-model-design.md", "market-analysis.md", "financial-planning-basics.md",
        "goal-setting-and-metrics.md", "risk-assessment.md", "lean-planning-methods.md",
        "stakeholder-communication.md", "planning-case-studies.md",
    ],
    "operations-and-process-design": [
        "process-mapping.md", "workflow-design.md", "sop-authoring.md",
        "capacity-planning.md", "quality-management-basics.md", "continuous-improvement.md",
        "tooling-and-automation.md", "operations-case-studies.md",
    ],
    "social-media-strategy": [
        "platform-landscape.md", "audience-and-community.md", "content-pillars.md",
        "engagement-strategy.md", "growth-and-reach.md", "social-listening.md",
        "crisis-management.md", "strategy-case-studies.md",
    ],
    "content-calendar-planning": [
        "calendar-fundamentals.md", "cadence-and-frequency.md", "content-mix-design.md",
        "seasonal-and-event-planning.md", "repurposing-frameworks.md",
        "scheduling-workflows.md", "performance-review-loop.md", "calendar-case-studies.md",
    ],
    "ui-design-critique": [
        "critique-principles.md", "visual-hierarchy.md", "layout-and-spacing.md",
        "typography-basics.md", "color-and-contrast.md", "interaction-patterns.md",
        "accessibility-review.md", "critique-case-studies.md",
    ],
    "design-system-foundations": [
        "design-tokens.md", "component-inventory.md", "pattern-documentation.md",
        "theming-architecture.md", "accessibility-standards.md",
        "versioning-and-governance.md", "adoption-strategies.md", "system-case-studies.md",
    ],
}

SKILL_SUPPORTING = {
    "game-mechanics-design": {"templates": 2, "schemas": 1, "examples": 1},
    "level-and-encounter-design": {"templates": 1, "schemas": 1, "examples": 1},
    "game-economy-balancing": {"templates": 1, "schemas": 1, "examples": 1},
    "software-architecture-design": {"templates": 2, "schemas": 1, "examples": 1},
    "code-review": {"templates": 1, "examples": 1},
    "testing-strategy": {"templates": 1, "examples": 1},
    "story-and-narrative-design": {"templates": 2, "examples": 1},
    "brainstorming-and-ideation": {"templates": 1, "examples": 1},
    "marketing-strategy": {"templates": 2, "examples": 1},
    "copywriting-and-messaging": {"templates": 1, "examples": 1},
    "business-planning": {"templates": 2, "examples": 1},
    "operations-and-process-design": {"templates": 2, "examples": 1},
    "social-media-strategy": {"templates": 1, "examples": 1},
    "content-calendar-planning": {"templates": 1, "examples": 1},
    "ui-design-critique": {"templates": 1, "examples": 1},
    "design-system-foundations": {"templates": 2, "schemas": 1, "examples": 1},
}


def count_substantive_lines(path):
    """Count substantive lines per spec/0006 rule."""
    with open(path) as f:
        lines = f.read().split("\n")
    total = len(lines)
    blank = sum(1 for l in lines if l.strip() == "")
    frontmatter = 0
    if lines and lines[0].strip() == "---":
        frontmatter += 1
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                frontmatter += 1
                break
    return total - blank - frontmatter


def check_shape():
    """Run all shape checks."""
    errors = []

    # ── Profile checks ──
    if not os.path.isdir(PROFILES_DIR):
        errors.append("profiles/ directory not found")

    profile_dirs = []
    if os.path.isdir(PROFILES_DIR):
        profile_dirs = sorted([
            d for d in os.listdir(PROFILES_DIR)
            if os.path.isdir(os.path.join(PROFILES_DIR, d))
        ])

    if len(profile_dirs) != 8:
        errors.append(f"Expected 8 profile directories, got {len(profile_dirs)}: {profile_dirs}")

    for expected in EXPECTED_PROFILES:
        if expected not in profile_dirs:
            errors.append(f"Missing profile directory: {expected}")

    for pname in profile_dirs:
        probepath = os.path.join(PROFILES_DIR, pname, "PROFILE.md")
        if not os.path.isfile(probepath):
            errors.append(f"Missing PROFILE.md in profiles/{pname}/")
            continue
        clines = count_substantive_lines(probepath)
        if clines < 256:
            errors.append(f"profiles/{pname}/PROFILE.md: {clines} substantive lines (min 256)")

        # Check frontmatter
        with open(probepath) as f:
            content = f.read()
        if "name:" not in content[:200]:
            errors.append(f"profiles/{pname}/PROFILE.md: missing 'name' in frontmatter")
        if "layer:" not in content[:200]:
            errors.append(f"profiles/{pname}/PROFILE.md: missing 'layer' in frontmatter")

        # Check 8 sections
        for section_num in range(1, 9):
            section_marker = f"## 0{section_num} "
            if section_marker not in content:
                errors.append(f"profiles/{pname}/PROFILE.md: missing section {section_num:02d}")

    # ── Skill checks ──
    if not os.path.isdir(SKILLS_DIR):
        errors.append("skills/ directory not found")

    skill_dirs = []
    if os.path.isdir(SKILLS_DIR):
        skill_dirs = sorted([
            d for d in os.listdir(SKILLS_DIR)
            if os.path.isdir(os.path.join(SKILLS_DIR, d))
        ])

    if len(skill_dirs) != 16:
        errors.append(f"Expected 16 skill directories, got {len(skill_dirs)}")

    for expected in EXPECTED_SKILLS:
        if expected not in skill_dirs:
            errors.append(f"Missing skill directory: {expected}")

    for sname in skill_dirs:
        skillpath = os.path.join(SKILLS_DIR, sname)
        skillmd = os.path.join(skillpath, "SKILL.md")
        if not os.path.isfile(skillmd):
            errors.append(f"Missing SKILL.md in skills/{sname}/")
            continue

        clines = count_substantive_lines(skillmd)
        if clines < 504 or clines > 520:
            errors.append(f"skills/{sname}/SKILL.md: {clines} substantive lines (target 504-520)")

        # Check frontmatter description
        with open(skillmd) as f:
            content = f.read()
        if "name:" not in content[:200]:
            errors.append(f"skills/{sname}/SKILL.md: missing 'name' in frontmatter")
        if "description:" not in content[:200]:
            errors.append(f"skills/{sname}/SKILL.md: missing 'description' in frontmatter")

        # Check 8 sections
        for section_num in range(1, 9):
            section_marker = f"## 0{section_num} "
            if section_marker not in content:
                errors.append(f"skills/{sname}/SKILL.md: missing section {section_num:02d}")

        # Check references manifest
        refdir = os.path.join(skillpath, "references")
        if sname in SKILL_REFERENCES:
            expected_refs = SKILL_REFERENCES[sname]
            actual_refs = []
            if os.path.isdir(refdir):
                actual_refs = sorted(os.listdir(refdir))
            if len(actual_refs) != 8:
                errors.append(f"skills/{sname}/references/: expected 8 files, got {len(actual_refs)}: {actual_refs}")
            for ref in expected_refs:
                if ref not in actual_refs:
                    errors.append(f"skills/{sname}/references/: missing {ref}")
            for ref in actual_refs:
                if ref not in expected_refs:
                    errors.append(f"skills/{sname}/references/: unexpected {ref}")

        # Check supporting dirs
        if sname in SKILL_SUPPORTING:
            for dirname, expected_count in SKILL_SUPPORTING[sname].items():
                dirpath = os.path.join(skillpath, dirname)
                actual_count = 0
                if os.path.isdir(dirpath):
                    actual_count = len([f for f in os.listdir(dirpath)
                                        if os.path.isfile(os.path.join(dirpath, f))])
                if actual_count != expected_count:
                    errors.append(
                        f"skills/{sname}/{dirname}/: expected {expected_count} files, got {actual_count}"
                    )

        # Bidirectional reference closure
        if os.path.isdir(refdir):
            all_skill_files = set()
            for root, dirs, files in os.walk(skillpath):
                for fn in files:
                    rel = os.path.relpath(os.path.join(root, fn), skillpath)
                    all_skill_files.add(rel)
            # Check every file in the skill directory is mentioned in SKILL.md
            for frel in all_skill_files:
                if frel == "SKILL.md":
                    continue
                if frel not in content:
                    errors.append(f"skills/{sname}/: file {frel} not referenced in SKILL.md")
            # Check Supporting Files Index table matches directory
            # (Table should list every file — light check for presence of table)

    return errors


def check_installer_static():
    """Static checks on install.py."""
    errors = []

    if not os.path.isfile(INSTALLER):
        errors.append("install.py not found")
        return errors

    with open(INSTALLER) as f:
        content = f.read()

    # Check no network imports
    network_imports = ["import socket", "import urllib", "from urllib", "import http",
                       "from http", "import requests", "from requests"]
    for imp in network_imports:
        if imp in content:
            errors.append(f"install.py contains network import: {imp}")

    # Check no subprocess package managers
    pkg_managers = ["pip install", "pip3 install", "conda install", "npm install"]
    for pm in pkg_managers:
        if pm in content:
            errors.append(f"install.py references package manager: {pm}")

    # Check mandatory function seams
    seams = [
        "def detect_harnesses",
        "def choose_targets",
        "def declare_hub_root",
        "def select_components",
        "def build_plan",
        "def preview_plan",
        "def apply_plan",
        "def verify_install",
        "def write_manifest",
        "def uninstall",
        "def main",
    ]
    for seam in seams:
        if seam not in content:
            errors.append(f"install.py missing function seam: {seam}")

    return errors


def main():
    parser = argparse.ArgumentParser(description="hearthandcode-agentic-os repository verifier")
    parser.add_argument("--shape", action="store_true", help="Run shape checks")
    parser.add_argument("--installer", action="store_true", help="Run installer static checks")
    flags = parser.parse_args()

    all_errors = []
    any_run = False

    if flags.shape:
        any_run = True
        print("Running shape checks...")
        all_errors.extend(check_shape())

    if flags.installer:
        any_run = True
        print("Running installer static checks...")
        all_errors.extend(check_installer_static())

    if not any_run:
        parser.print_help()
        sys.exit(1)

    if all_errors:
        print(f"\nFAILURES ({len(all_errors)}):")
        for err in all_errors:
            print(f"  ✗ {err}")
        sys.exit(1)
    else:
        print("\nAll checks passed.")
        sys.exit(0)


if __name__ == "__main__":
    main()