#!/usr/bin/env python3
"""ACK signature generator for the agentic hub decision protocol.

Usage:
  python3 ack.py generate maker 007 "Write file: 05-craft/whitepaper.md"
  # Output: ACK-maker-007-4f9e2b

Outputs an ACK string and optionally the YAML ledger entry.
"""

import hashlib
import sys
import time
from datetime import datetime


def generate(profile: str, seq: int, description: str,
             timestamp: float = 0.0, session_hour: str = "") -> str:
    if timestamp <= 0:
        timestamp = time.time()
    if not session_hour:
        session_hour = datetime.utcfromtimestamp(timestamp).strftime("%Y-%m-%dT%H:00:00Z")
    raw = f"{profile}-{seq:03d}-{timestamp}-{session_hour}-{description}"
    h = hashlib.sha256(raw.encode()).hexdigest()[:8]
    return f"ACK-{profile}-{seq:03d}-{h}"


def parse(ack_str: str) -> dict:
    parts = ack_str.split("-", 3)
    if len(parts) != 4 or parts[0] != "ACK":
        raise ValueError(f"Invalid ACK format: {ack_str}")
    return {"profile": parts[1], "sequence": int(parts[2]), "hash": parts[3]}


def ledger_entry(ack_str: str, kind: str, action: str,
                 status: str = "CONFIRMED") -> str:
    return (f"---ack\nid: {ack_str}\nkind: {kind}\nsession: "
            f"{datetime.utcnow().isoformat()}Z\naction: {action!r}\nstatus: {status}\n---\n")


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python3 ack.py <profile> <sequence> \"<description>\" [--entry <kind>]", file=sys.stderr)
        sys.exit(1)
    profile = sys.argv[1]
    seq_s = sys.argv[2]
    if not seq_s.isdigit():
        print(f"Sequence must be integer: {seq_s}", file=sys.stderr)
        sys.exit(1)
    seq = int(seq_s)
    desc = sys.argv[3]
    ack = generate(profile, seq, desc)
    if "--ledger" in sys.argv:
        idx = sys.argv.index("--ledger")
        kind = sys.argv[idx + 1] if idx + 1 < len(sys.argv) else "effect"
        print(ack)
        print(ledger_entry(ack, kind, desc))
    else:
        print(ack)