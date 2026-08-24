#!/usr/bin/env python3
"""Mechanical wiki checker. Run manually or from flows/audit.md — never
wired to hooks, CI, or schedules.

Checks: frontmatter validity, unresolved [[wikilinks]], orphan pages,
index.md coverage and size budget (entries are pointers, not summaries),
provenance tags on factual bullets, stale drafts, log.md entry format.
Text inside code fences and inline backticks is ignored everywhere — a
documented `[[link]]` is not a link. Reports; changes nothing. Exit 0
always, unless --strict (then 1 if any findings).
Stdlib only; Windows/macOS/Linux.

Usage:
  python3 wiki_lint.py WIKI_PATH [--provenance {facts,all,off}]
                                 [--stale-days N] [--log-since YYYY-MM-DD]
                                 [--index-budget CHARS] [--index-entry-max CHARS]
                                 [--strict]
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
FENCE_RE = re.compile(r"^(```|~~~).*?^\1\s*$", re.M | re.S)
INLINE_CODE_RE = re.compile(r"`[^`\n]*`")


def strip_code(text):
    """Remove fenced blocks and inline code spans — their contents are
    documentation, not links or claims."""
    return INLINE_CODE_RE.sub("", FENCE_RE.sub("", text or ""))
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
    ap.add_argument("--log-since", metavar="YYYY-MM-DD", default=None,
                    help="only check log.md entries dated on/after this "
                         "(adopted wikis: set to the adoption date)")
    ap.add_argument("--index-budget", type=int, default=30000,
                    help="warn when index.md exceeds this many chars (default 30000)")
    ap.add_argument("--index-entry-max", type=int, default=200,
                    help="warn when an index entry line exceeds this (default 200; "
                         "the format targets ~165)")
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
    index_links = {strip_link(m) for m in LINK_RE.findall(strip_code(index_text))}

    # index budget: entries are pointers, not summaries
    if index_text:
        if len(index_text) > args.index_budget:
            add("index-size", f"index.md: {len(index_text)} chars (budget "
                f"{args.index_budget}) — it is loaded every session; entries "
                f"drifting from pointers into summaries is the usual cause")
        for i, line in enumerate(index_text.splitlines(), 1):
            if line.lstrip().startswith("- ") and len(line) > args.index_entry_max:
                add("index-size", f"index.md:{i}: entry is {len(line)} chars "
                    f"(max {args.index_entry_max}) — move detail into the page")

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
        # links (code-stripped: documented [[links]] don't count)
        scan_body = strip_code(body)
        for target in LINK_RE.findall(scan_body):
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
            for line in scan_body.splitlines():
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
                if args.log_since:
                    m = DATE_RE.search(line)
                    if m and m.group(0) < args.log_since:
                        continue  # legacy entry, predates the adopted format
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
