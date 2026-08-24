#!/usr/bin/env python3
"""Mechanical wiki checker. Run manually or from flows/audit.md — never
wired to hooks, CI, or schedules.

Checks: frontmatter validity, unresolved [[wikilinks]], orphan pages,
index.md coverage, provenance tags on factual bullets, stale drafts,
log.md entry format. Reports; changes nothing. Exit 0 always, unless
--strict (then 1 if any findings). Stdlib only; Windows/macOS/Linux.

Usage:
  python3 wiki_lint.py WIKI_PATH [--provenance {facts,all,off}]
                                 [--stale-days N] [--strict]
"""
import argparse
import re
import sys
from datetime import date, timedelta
from pathlib import Path

FM_REQUIRED = ("type", "title", "status", "created", "updated")
STATUSES = {"draft", "stable", "superseded"}
LINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]")
PROV_RE = re.compile(r"(—|--)\s*(conv:|file:|verified:|exp:|\[\[)")
LOG_RE = re.compile(r"^## \[\d{4}-\d{2}-\d{2}\] \S+ \| .+")
DATE_RE = re.compile(r"\d{4}-\d{2}-\d{2}")
# Sections whose bullets are treated as factual claims in "facts" mode.
FACTY = {"facts", "findings", "results", "key facts", "lessons", "gotchas"}


def parse_frontmatter(text):
    if not text.startswith("---"):
        return None, text
    end = text.find("\n---", 3)
    if end == -1:
        return None, text
    fm = {}
    for line in text[3:end].splitlines():
        m = re.match(r"^(\w[\w-]*):\s*(.*)$", line)
        if m:
            val = m.group(2).strip()
            if val.startswith("[") and val.endswith("]"):
                inner = val[1:-1].strip()
                fm[m.group(1)] = [x.strip().strip("'\"")
                                  for x in inner.split(",") if x.strip()] if inner else []
            else:
                fm[m.group(1)] = val.strip("'\"")
    return fm, text[end + 4:]


def strip_link(target):
    return target.strip().lower()


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("wiki", type=Path)
    ap.add_argument("--provenance", choices=["facts", "all", "off"], default="facts",
                    help="which bullets must carry provenance tags (default: facts sections)")
    ap.add_argument("--stale-days", type=int, default=30)
    ap.add_argument("--strict", action="store_true")
    args = ap.parse_args()
    wiki = args.wiki.expanduser().resolve()
    pages_dir = wiki / "wiki"
    if not pages_dir.is_dir():
        sys.exit(f"{pages_dir} is not a directory — is {wiki} a wiki?")

    findings = []          # (category, message)
    def add(cat, msg):
        findings.append((cat, msg))

    pages = {}             # stem -> (path, fm, body)
    resolve = {}           # lowercased name/alias/title -> stem
    for p in sorted(pages_dir.glob("*.md")):
        fm, body = parse_frontmatter(p.read_text(encoding="utf-8"))
        pages[p.stem] = (p, fm, body)
        resolve[p.stem.lower()] = p.stem
        if fm:
            if fm.get("title"):
                resolve.setdefault(str(fm["title"]).lower(), p.stem)
            for a in (fm.get("aliases") or []):
                resolve.setdefault(a.lower(), p.stem)

    index_text = (wiki / "index.md").read_text(encoding="utf-8") if (wiki / "index.md").exists() else ""
    index_links = {strip_link(m) for m in LINK_RE.findall(index_text)}

    inbound = {stem: 0 for stem in pages}
    today = date.today()

    for stem, (p, fm, body) in pages.items():
        rel = f"wiki/{p.name}"
        # frontmatter
        if fm is None:
            add("frontmatter", f"{rel}: no frontmatter block")
        else:
            for k in FM_REQUIRED:
                if k not in fm or fm[k] == "":
                    add("frontmatter", f"{rel}: missing `{k}`")
            if fm.get("status") and fm["status"] not in STATUSES:
                add("frontmatter", f"{rel}: status `{fm['status']}` not in {sorted(STATUSES)}")
            if fm.get("type") and not p.name.startswith(str(fm["type"]) + "-"):
                add("frontmatter", f"{rel}: filename doesn't start with `{fm['type']}-`")
            # stale drafts
            if fm.get("status") == "draft":
                m = DATE_RE.search(str(fm.get("updated", "")))
                if m:
                    y, mo, d = map(int, m.group(0).split("-"))
                    if (today - date(y, mo, d)) > timedelta(days=args.stale_days):
                        add("stale-draft", f"{rel}: draft untouched since {m.group(0)}")
        # links
        for target in LINK_RE.findall(body or ""):
            t = strip_link(target)
            if t in resolve:
                if resolve[t] != stem:
                    inbound[resolve[t]] += 1
            else:
                add("unresolved-link", f"{rel}: [[{target.strip()}]] resolves to no page")
        # provenance — join wrapped bullets into logical bullets first
        if args.provenance != "off":
            in_facty = False
            bullet = None  # (joined_text, applies)
            def flush():
                nonlocal bullet
                if bullet:
                    text, applies = bullet
                    if applies and not PROV_RE.search(text) and not LINK_RE.search(text):
                        add("provenance", f"{rel}: untagged bullet: {text.strip()[:70]}")
                bullet = None
            for line in (body or "").splitlines():
                h = re.match(r"^#{2,}\s+(.*)$", line)
                if h:
                    flush()
                    in_facty = h.group(1).strip().lower() in FACTY
                    continue
                if re.match(r"^\s*[-*]\s+\S", line):
                    flush()
                    bullet = (line, args.provenance == "all" or in_facty)
                elif bullet and line.strip() and not line.lstrip().startswith(("#", ">", "|", "```")):
                    bullet = (bullet[0] + " " + line.strip(), bullet[1])
                else:
                    flush()
            flush()

    # orphans & index coverage
    for stem in pages:
        if inbound[stem] == 0 and stem.lower() not in index_links:
            add("orphan", f"wiki/{stem}.md: no inbound links and not in index.md")
        if stem.lower() not in index_links:
            add("index", f"wiki/{stem}.md: not listed in index.md")
    for t in index_links:
        if t not in resolve:
            add("index", f"index.md: [[{t}]] points at no page")

    # log format
    log = wiki / "log.md"
    if log.exists():
        for i, line in enumerate(log.read_text(encoding="utf-8").splitlines(), 1):
            if line.startswith("## ") and not LOG_RE.match(line):
                add("log", f"log.md:{i}: entry doesn't match `## [YYYY-MM-DD] kind | text`")

    # report
    if not findings:
        print(f"clean: {len(pages)} pages, no findings")
        return 0
    by_cat = {}
    for cat, msg in findings:
        by_cat.setdefault(cat, []).append(msg)
    for cat in sorted(by_cat):
        print(f"\n[{cat}] {len(by_cat[cat])}")
        for msg in by_cat[cat]:
            print(f"  {msg}")
    print(f"\n{len(findings)} finding(s) across {len(pages)} page(s)")
    return 1 if args.strict else 0


if __name__ == "__main__":
    sys.exit(main())
