"""Convert a lychee JSON report into GitHub annotations and a job summary.

Usage: python3 scripts/lychee_annotations.py lychee/out.json
Exits with 1 if the report has broken links.
"""
import json
import os
import re
import sys
from pathlib import Path

report = json.load(open(sys.argv[1]))
site = Path("site").resolve()
rows = set()
theme = {}  # broken links not found in any source file, for example in the theme


def source_for(html):
    # site/a/b/index.html -> docs/a/b.md or docs/a/b/index.md
    page = Path(html).resolve().relative_to(site).parent
    for cand in (Path("docs") / f"{page}.md", Path("docs") / page / "index.md"):
        if cand.is_file():
            return cand
    return None


def find_line(src, url):
    # Search the source for the end of the broken path, for example "tql/filters".
    path = re.sub(r"^file://" + re.escape(str(site)), "", url).split("#")[0].rstrip("/")
    lines = src.read_text().splitlines()
    for tail in ("/".join(path.split("/")[-2:]), path.split("/")[-1]):
        pattern = re.compile(rf'[(/"]{re.escape(tail)}(\.md)?[/)#"]')
        for no, line in enumerate(lines, 1):
            if tail and pattern.search(line):
                return no
    return None


for html, errors in report["error_map"].items():
    src = source_for(html)
    for err in errors:
        url = err["url"].replace(f"file://{site}", "")
        line = find_line(src, err["url"]) if src else None
        if line:
            rows.add((f"{src}:{line}", url))
        else:
            theme.setdefault(url, set()).add(html)

# GitHub shows at most 10 error annotations per step. The summary has the full list.
for loc, url in sorted(rows):
    src, line = loc.rsplit(":", 1)
    print(f"::error file={src},line={line},title=Broken link::{url}")
for url, pages in sorted(theme.items()):
    print(f"::error title=Broken link::{url} (on {len(pages)} pages, not in a source file)")
    rows.add((f"{len(pages)} pages (theme or config)", url))

summary = os.environ.get("GITHUB_STEP_SUMMARY")
if summary:
    with open(summary, "a") as out:
        out.write(f"## Link check\n\n{len(rows)} broken links.\n\n")
        if rows:
            out.write("| Source | Broken link |\n|---|---|\n")
            out.writelines(f"| `{s}` | `{u}` |\n" for s, u in sorted(rows))

sys.exit(1 if rows else 0)
