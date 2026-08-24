#!/usr/bin/env python3
"""Keep CLAUDE.md and AGENTS.md identical wherever they live as a pair.

Usage:
  python3 sync_pair.py [--check] [--from claude|agents] PATH [PATH ...]

Each PATH is a directory containing the pair (or expected to). Default
action: make them identical, newer file wins. --from forces the direction.
--check reports without writing (exit 1 on any mismatch). Stdlib only;
Windows/macOS/Linux.
"""
import argparse
import shutil
import sys
from pathlib import Path


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("paths", nargs="+", type=Path)
    ap.add_argument("--check", action="store_true", help="report only; exit 1 on mismatch")
    ap.add_argument("--from", dest="source", choices=["claude", "agents"],
                    help="force direction instead of newest-wins")
    args = ap.parse_args()

    mismatches = 0
    for d in args.paths:
        d = d.expanduser()
        c, a = d / "CLAUDE.md", d / "AGENTS.md"
        if not c.exists() and not a.exists():
            print(f"{d}: neither CLAUDE.md nor AGENTS.md exists — skipped")
            continue
        if c.exists() != a.exists() and not args.source:
            # A lone file is a valid single-harness location (e.g. ~/.codex
            # holds only AGENTS.md). Pass --from to create the twin.
            lone = c if c.exists() else a
            print(f"{d}: only {lone.name} present — ok (single-harness)")
            continue
        if c.exists() and a.exists() and c.samefile(a):
            print(f"{d}: in sync (linked)")
            continue
        if c.exists() and a.exists() and c.read_bytes() == a.read_bytes():
            print(f"{d}: in sync")
            continue
        mismatches += 1
        if args.check:
            missing = "AGENTS.md missing" if not a.exists() else (
                      "CLAUDE.md missing" if not c.exists() else "contents differ")
            print(f"{d}: OUT OF SYNC ({missing})")
            continue
        if args.source == "claude":
            src, dst = c, a
        elif args.source == "agents":
            src, dst = a, c
        elif not a.exists() or (c.exists() and c.stat().st_mtime >= a.stat().st_mtime):
            src, dst = c, a
        else:
            src, dst = a, c
        if not src.exists():
            print(f"{d}: source {src.name} missing — cannot sync", file=sys.stderr)
            continue
        shutil.copyfile(src, dst)
        print(f"{d}: {src.name} -> {dst.name}")
    return 1 if (args.check and mismatches) else 0


if __name__ == "__main__":
    sys.exit(main())
