"""Pull the language of one module out of its domain-language / key-abstractions / domain-sketch chain.

Usage: python extract_terms.py <module>   (run from the project root)

Prints, per class grouping (the ``## Key Abstraction`` headings of the latest stage), each term (``### term`` that
carries a ``#### Domain [Ll]anguage`` block) with its language bullets, sketch bullets and source chunks, as a starting
point for ``{module}/.context/{module}-model.md``. Verbatim source extracts (chapter dumps) are dropped; they live in
``.context/sources/``. Terms the latest stage lost are taken from the earlier stages and listed under "(not grouped)".
"""
import re
import io
import sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
module = sys.argv[1]
ctx = Path(module) / ".context"
stages = [ctx / f"{module}-domain-sketch.md", ctx / f"{module}-key-abstractions.md", ctx / f"{module}-domain-language.md"]


def parse(path):
    groups, order, group = {}, [], "(not grouped)"
    text = path.read_text(encoding="utf-8") if path.exists() else ""
    blocks = re.split(r"^(?=#{2,3} )", text, flags=re.M)
    for b in blocks:
        head = b.split("\n", 1)[0]
        if head.startswith("## ") and not re.match(r"## (Module|CHAPTER|Domain logic)", head):
            group = head[3:].strip()
            continue
        if not head.startswith("### ") or not re.search("#### Domain [Ll]anguage", b):
            continue
        term = head[4:].strip()
        lang = re.search(r"#### Domain [Ll]anguage\n(.*?)(?=\n####|\Z)", b, re.S)
        sk = re.search(r"#### Domain Sketch\n(.*?)(?=\n####|\Z)", b, re.S)
        srcs = sorted(set(re.findall(r"Source: (\S+)", b)))
        groups.setdefault(group, {})[term] = (
            [l for l in (lang[1] if lang else "").splitlines() if l.strip().startswith("-") or l.startswith("  ")],
            [l for l in (sk[1] if sk else "").splitlines() if l.strip().startswith("-")],
            srcs,
        )
        if term not in order:
            order.append(term)
    return groups, order


latest, seen = parse(stages[0])
known = {t for g in latest.values() for t in g}
for older in stages[1:]:
    g, _ = parse(older)
    for grp, terms in g.items():
        for t, v in terms.items():
            if t not in known:
                latest.setdefault("(not grouped)", {})[t] = v
                known.add(t)

for grp, terms in latest.items():
    print(f"\n## GROUP: {grp}")
    for t, (lang, sk, srcs) in terms.items():
        print(f"\n### {t}")
        for l in lang:
            print(l)
        for l in sk:
            print(l.replace("- Invariant:", "- **Invariant:**"))
        if srcs:
            print("- Sources: " + ", ".join(f"`{s}`" for s in srcs))
