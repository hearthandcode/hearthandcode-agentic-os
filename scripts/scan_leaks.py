#!/usr/bin/env python3
"""
hearthandcode-agentic-os leak scanner.
Scans every tracked file for forbidden content patterns and a maintainer-held
token list. Exits non-zero on any match.

Usage:
  python3 scripts/scan_leaks.py [--token-list TOKEN_FILE]

The token file defaults to .leak-scan-tokens.txt (gitignored, maintainer-held).
A placeholder example file ships as .leak-scan-tokens.example.txt.
"""

import argparse
import os
import re
import sys


# Always-active patterns from spec/0008
ALWAYS_ACTIVE_PATTERNS = [
    (r"/home/[a-z]", "home-directory path fragment"),
    (r"[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}", "email address"),
    (r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", "IP address"),
    (r"BEGIN [A-Z ]*PRIVATE KEY", "private key material"),
]


def load_token_list(path):
    """Load forbidden tokens from file, one per line. Ignores comments and blanks."""
    tokens = []
    if os.path.isfile(path):
        with open(path) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#"):
                    tokens.append(line)
    return tokens


def scan_file(filepath, patterns, token_list):
    """Scan a single file. Returns list of (line_number, match_text, pattern_name)."""
    findings = []
    try:
        with open(filepath, "r", errors="replace") as f:
            for i, line in enumerate(f, 1):
                # Check always-active patterns
                for pat, name in patterns:
                    m = re.search(pat, line, re.IGNORECASE)
                    if m:
                        findings.append((i, m.group().strip()[:80], f"always-active: {name}"))
                # Check token list
                for token in token_list:
                    if token.lower() in line.lower():
                        findings.append((i, line.strip()[:80], f"token-match: {token}"))
    except Exception:
        pass
    return findings


def main():
    parser = argparse.ArgumentParser(description="Leak scanner for hearthandcode-agentic-os")
    parser.add_argument("--token-list", default=".leak-scan-tokens.txt",
                        help="Path to forbidden-token list (default: .leak-scan-tokens.txt)")
    parser.add_argument("--git-log", action="store_true",
                        help="Also scan git commit messages")
    flags = parser.parse_args()

    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    token_list = load_token_list(os.path.join(repo_root, flags.token_list))

    # Walk repository files
    findings = []
    file_count = 0
    for root, dirs, files in os.walk(repo_root):
        # Skip .git, __pycache__, node_modules
        dirs[:] = [d for d in dirs if d not in (".git", "__pycache__", "node_modules")]
        for fn in files:
            if fn.endswith((".pyc", ".png", ".jpg", ".gif", ".ico")):
                continue
            fpath = os.path.join(root, fn)
            file_count += 1
            findings.extend(scan_file(fpath, ALWAYS_ACTIVE_PATTERNS, token_list))

    # Also scan git log messages if requested
    if flags.git_log:
        try:
            import subprocess
            result = subprocess.run(
                ["git", "log", "--oneline", "--format=%s%n%b"],
                capture_output=True, text=True, cwd=repo_root
            )
            for i, line in enumerate(result.stdout.split("\n"), 1):
                for pat, name in ALWAYS_ACTIVE_PATTERNS:
                    m = re.search(pat, line, re.IGNORECASE)
                    if m:
                        findings.append((f"git-log:{i}", m.group().strip()[:80], f"always-active: {name}"))
                for token in token_list:
                    if token.lower() in line.lower():
                        findings.append((f"git-log:{i}", line.strip()[:80], f"token-match: {token}"))
        except Exception:
            pass

    if findings:
        print(f"LEAKS FOUND ({len(findings)}):")
        for line_num, match, pat_name in findings:
            print(f"  {pat_name}: {line_num}: {match}")
        sys.exit(1)
    else:
        print(f"Clean: {file_count} files scanned, 0 leaks found.")
        sys.exit(0)


if __name__ == "__main__":
    main()