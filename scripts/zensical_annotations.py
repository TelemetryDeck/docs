"""Convert Zensical build warnings into GitHub annotations.

Usage: python3 scripts/zensical_annotations.py build.log
"""
import re
import sys

log = re.sub(r"\x1b\[[0-9;]*m", "", open(sys.argv[1]).read())
for msg, path, line, col in re.findall(r"Warning: (.+)\n\s*╭─\[ (\S+):(\d+):(\d+) \]", log):
    src = f"docs/{path}"
    try:
        target = re.match(r'[^)\s"]*', open(src).read().splitlines()[int(line) - 1][int(col) - 1:]).group()
    except (OSError, IndexError):
        target = ""
    print(f"::error file={src},line={line},col={col},title=Zensical: {msg}::{msg}: {target}")
