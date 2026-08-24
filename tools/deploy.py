#!/usr/bin/env python3
"""Deploy generated instruction sources from the wiki to their live locations.

The manifest (<wiki>/setup/manifest.json) maps sources to targets:

  { "files": [ { "source": "config/global.md",
                 "targets": ["~/.claude/CLAUDE.md", "~/.codex/AGENTS.md"] } ] }

Sources are wiki-relative; targets are absolute (~ allowed). The source is
canonical: `deploy` copies source -> targets, `check` reports drift without
writing (exit 1 if any), `diff` shows unified diffs. A drifted target
usually means a hand-edit worth folding back into the source — see
flows/tune.md.

Symlinked targets are a supported mode: a target that already resolves to
its source (symlink or hardlink) is reported `ok (linked)` and never
copied over — POSIX setups that deploy by symlink coexist with this tool.
Copy mode is the cross-platform path: Windows symlinks need Developer
Mode/admin, so on Windows prefer plain copies. Stdlib only;
Windows/macOS/Linux.

Usage:
  python3 deploy.py --wiki PATH {deploy|check|diff}
"""
import argparse
import difflib
import json
import shutil
import sys
from pathlib import Path


def load(wiki: Path):
    mf = wiki / "setup" / "manifest.json"
    if not mf.exists():
        sys.exit(f"no manifest at {mf}")
    data = json.loads(mf.read_text(encoding="utf-8"))
    for entry in data.get("files", []):
        src = wiki / entry["source"]
        for t in entry["targets"]:
            yield src, Path(t).expanduser()


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--wiki", required=True, type=Path)
    ap.add_argument("command", choices=["deploy", "check", "diff"])
    args = ap.parse_args()
    wiki = args.wiki.expanduser().resolve()

    drift = 0
    for src, dst in load(wiki):
        if not src.exists():
            print(f"MISSING SOURCE: {src}", file=sys.stderr)
            drift += 1
            continue
        if dst.exists() and src.samefile(dst):
            # symlink (or hardlink) to the source: identical by construction.
            print(f"ok (linked) {dst}")
            continue
        s = src.read_text(encoding="utf-8")
        d = dst.read_text(encoding="utf-8") if dst.exists() else None
        if args.command == "deploy":
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(src, dst)
            print(f"deployed {src.relative_to(wiki)} -> {dst}")
        elif s == d:
            print(f"ok       {dst}")
        else:
            drift += 1
            state = "ABSENT " if d is None else "DRIFTED"
            print(f"{state}  {dst}   (source: {src.relative_to(wiki)})")
            if args.command == "diff" and d is not None:
                sys.stdout.writelines(difflib.unified_diff(
                    d.splitlines(keepends=True), s.splitlines(keepends=True),
                    fromfile=str(dst), tofile=str(src)))
    if args.command != "deploy" and drift:
        print(f"\n{drift} target(s) out of sync — `deploy` to overwrite from "
              f"sources, or fold hand-edits back first (flows/tune.md).")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
