"""Check every ++[term](model.md#anchor)++ in the scenarios resolves to a heading, using CDD's own anchor resolver."""
import re
import sys
from pathlib import Path

sys.path.insert(0, r"C:\dev\abd-cdd-class-language")
from harness.markdown.markdown import MarkdownText  # noqa: E402

LP = lambda p: "\\\\?\\" + str(Path(p).resolve())
LINK = re.compile(r"\+\+\[[^\]]+\]\(([^)#]+\.md)#([^)]+)\)\+\+")
uses = {}
for f in Path("story_tests").rglob("*_story.test.md"):
    for m in LINK.finditer(open(LP(f), encoding="utf-8").read()):
        key = (str((f.parent / m[1]).resolve()), m[2])
        uses[key] = uses.get(key, 0) + 1
docs, bad, on_class, other = {}, [], 0, 0
for (target, anchor), n in uses.items():
    if target not in docs:
        text = open(target, encoding="utf-8").read()
        docs[target] = (MarkdownText(text), text.splitlines())
    md, lines = docs[target]
    found = md.anchored_lines(anchor)
    if found is None:
        bad.append((target, anchor, n))
        continue
    heading = next((lines[i] for i in (found[0], found[0] - 1) if 0 <= i < len(lines) and lines[i].startswith("#")), "")
    if heading.startswith("## **"):
        on_class += n
    else:
        other += n
print(f"distinct targets {len(uses)}, unresolved {len(bad)}, uses on a class heading {on_class}, on a term heading {other}")
for b in bad[:10]:
    print("  unresolved:", b)
