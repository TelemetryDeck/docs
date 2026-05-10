"""Generate llms.txt, llms-full.txt, and ship raw .md sources alongside the
rendered HTML so coding agents and LLMs can consume the documentation.

Run after `zensical build`. Reads:
  - zensical.toml  (for site metadata and navigation)
  - docs/         (source markdown)

Writes into the existing site/ directory:
  - site/<path>.md     for every source page (preserves directory layout)
  - site/llms.txt      structured index per https://llmstxt.org
  - site/llms-full.txt all page content concatenated for one-shot consumption
"""

from __future__ import annotations

import re
import shutil
import sys
import tomllib
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = ROOT / "zensical.toml"
DOCS_DIR = ROOT / "docs"
SITE_DIR = ROOT / "site"
STATIC_WEB_APP_CONFIG = ROOT / "staticwebapp.config.json"
DEFAULT_SITE_URL = "https://docs.telemetrydeck.com"

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


@dataclass
class Page:
    rel_path: str
    title: str
    description: str


def load_config() -> dict:
    with CONFIG_PATH.open("rb") as f:
        return tomllib.load(f)


def parse_frontmatter(text: str) -> tuple[dict, str]:
    """Extract YAML-ish frontmatter without pulling in PyYAML.

    Only top-level scalar key/value pairs are read — that is all we need
    (title, description, lead). Lists and nested maps are skipped.
    """
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}, text
    data: dict[str, str] = {}
    current_key: str | None = None
    for line in match.group(1).splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line.startswith(" ") or line.startswith("\t"):
            current_key = None
            continue
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        current_key = key
        data[key] = value
    body = text[match.end():]
    return data, body


def page_for(rel_path: str, fallback: str | None = None) -> Page | None:
    src = DOCS_DIR / rel_path
    if not src.is_file():
        print(f"warning: missing source page {rel_path}", file=sys.stderr)
        return None
    text = src.read_text(encoding="utf-8")
    fm, _ = parse_frontmatter(text)
    title = fm.get("title") or fallback or fallback_title(rel_path)
    description = fm.get("description") or fm.get("lead", "")
    return Page(rel_path=rel_path, title=title, description=description)


def fallback_title(rel_path: str) -> str:
    stem = Path(rel_path).stem
    if stem == "index":
        stem = Path(rel_path).parent.name or "Home"
    return stem.replace("-", " ").replace("_", " ").title()


def md_url(rel_path: str, base_url: str) -> str:
    return f"{base_url.rstrip('/')}/{rel_path}"


def copy_source_markdown(rel_paths: Iterable[str]) -> int:
    count = 0
    for rel_path in rel_paths:
        src = DOCS_DIR / rel_path
        dst = SITE_DIR / rel_path
        if not src.is_file():
            continue
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
        count += 1
    return count


def collect_nav_pages(
    nav: list, prefix: tuple[str, ...] = ()
) -> list[tuple[tuple[str, ...], str, str]]:
    """Walk the nav structure and yield (section_path, page_rel_path, label) tuples."""
    pages: list[tuple[tuple[str, ...], str, str]] = []
    for entry in nav:
        if not isinstance(entry, dict) or len(entry) != 1:
            continue
        label, value = next(iter(entry.items()))
        if isinstance(value, str):
            pages.append((prefix, value, label))
        elif isinstance(value, list):
            pages.extend(collect_nav_pages(value, prefix + (label,)))
    return pages


def all_source_pages() -> list[str]:
    return sorted(
        str(p.relative_to(DOCS_DIR)).replace("\\", "/")
        for p in DOCS_DIR.rglob("*.md")
    )


def render_llms_txt(config: dict, base_url: str) -> str:
    project = config.get("project", {})
    site_name = project.get("site_name", "Documentation")
    site_description = project.get("site_description", "")
    nav = project.get("nav", [])

    nav_pages = collect_nav_pages(nav)
    seen: set[str] = set()

    lines: list[str] = [f"# {site_name}", ""]
    if site_description:
        lines += [f"> {site_description}", ""]
    lines += [
        "Every documentation page is also available as Markdown by visiting",
        "the same URL with a `.md` suffix (for example `/articles/insights.md`).",
        "A single concatenated copy of all pages lives at `/llms-full.txt`.",
        "",
    ]

    sections: dict[tuple[str, ...], list[Page]] = {}
    for section_path, rel_path, label in nav_pages:
        if rel_path in seen:
            continue
        seen.add(rel_path)
        page = page_for(rel_path, fallback=label)
        if page is None:
            continue
        sections.setdefault(section_path, []).append(page)

    for section_path, pages in sections.items():
        heading = " / ".join(section_path) if section_path else "Overview"
        lines.append(f"## {heading}")
        lines.append("")
        for page in pages:
            url = md_url(page.rel_path, base_url)
            entry = f"- [{page.title}]({url})"
            if page.description:
                entry += f": {page.description}"
            lines.append(entry)
        lines.append("")

    extras = sorted(
        rel_path for rel_path in all_source_pages() if rel_path not in seen
    )
    if extras:
        lines.append("## Optional")
        lines.append("")
        for rel_path in extras:
            page = page_for(rel_path)
            if page is None:
                continue
            url = md_url(rel_path, base_url)
            entry = f"- [{page.title}]({url})"
            if page.description:
                entry += f": {page.description}"
            lines.append(entry)
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def render_llms_full_txt(config: dict, base_url: str) -> str:
    project = config.get("project", {})
    site_name = project.get("site_name", "Documentation")

    parts: list[str] = [
        f"# {site_name} (full text)",
        "",
        "Concatenated source for every documentation page. Pages are separated",
        "by horizontal rules and labelled with their canonical URL.",
        "",
    ]

    for rel_path in all_source_pages():
        page = page_for(rel_path)
        if page is None:
            continue
        url = md_url(rel_path, base_url)
        text = (DOCS_DIR / rel_path).read_text(encoding="utf-8")
        parts += [
            "---",
            "",
            f"# {page.title}",
            "",
            f"Source: {url}",
            "",
            text.rstrip(),
            "",
        ]

    return "\n".join(parts).rstrip() + "\n"


def main() -> int:
    if not SITE_DIR.is_dir():
        print(f"error: site directory not found at {SITE_DIR}", file=sys.stderr)
        print("run `zensical build` before this script", file=sys.stderr)
        return 1

    config = load_config()
    site_url = config.get("project", {}).get("site_url") or DEFAULT_SITE_URL
    base_url = site_url.rstrip("/")

    rel_paths = all_source_pages()
    copied = copy_source_markdown(rel_paths)
    print(f"copied {copied} markdown sources into {SITE_DIR}")

    if STATIC_WEB_APP_CONFIG.is_file():
        shutil.copy2(STATIC_WEB_APP_CONFIG, SITE_DIR / STATIC_WEB_APP_CONFIG.name)
        print(f"copied {STATIC_WEB_APP_CONFIG.name} into {SITE_DIR}")

    llms_txt = render_llms_txt(config, base_url)
    (SITE_DIR / "llms.txt").write_text(llms_txt, encoding="utf-8")
    print(f"wrote {SITE_DIR / 'llms.txt'}")

    llms_full_txt = render_llms_full_txt(config, base_url)
    (SITE_DIR / "llms-full.txt").write_text(llms_full_txt, encoding="utf-8")
    print(f"wrote {SITE_DIR / 'llms-full.txt'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
