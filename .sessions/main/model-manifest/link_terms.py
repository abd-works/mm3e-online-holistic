"""Link each ++domain term++ in the scenario markdown to its heading in the module models.

Usage (from the project root): python link_terms.py [--write]

A term owned by a class links to that class's card heading (``## **Class**``), the heading the knowledge graph reads the
class from, so the step is joined to the class. A module-level term links to its own ``### term`` heading. A term no
model defines stays unlinked. Without --write, prints what would change.
"""
import os
import re
import sys
from pathlib import Path

sys.path.insert(0, r"C:\dev\abd-cdd-class-language")
from harness.markdown.markdown import heading_anchor  # noqa: E402

ROOT = Path.cwd()
MODULES = ["ability", "advantage", "character-construction", "check-resolution", "combat", "equipment", "power", "skill"]
EPIC_MODULE = {
    "resolve-checks": "check-resolution", "construct-hero": "character-construction", "assign-abilities": "ability",
    "manage-skills": "skill", "select-advantages": "advantage", "configure-power-effects": "power",
    "apply-power-modifiers": "power", "organize-power-sets": "power", "equip-hero": "equipment", "conduct-combat": "combat",
}
LP = lambda p: "\\\\?\\" + str(Path(p).resolve())


def norm(text):
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)          # an existing link's words
    text = re.sub(r"[*`_]", "", text).strip().lower()
    return re.sub(r"\s+", " ", text)


def variants(text):
    """The keys a heading is found by: as written, without a parenthetical, the parenthetical alone, singular."""
    base = norm(text)
    keys = {base} | {part.strip() for part in base.split("/") if part.strip()}
    m = re.match(r"^(.*?)\s*\((.*?)\)\s*$", base)
    if m:
        keys |= {m[1].strip(), m[2].strip()}
    keys |= {k[:-1] for k in list(keys) if k.endswith("s") and len(k) > 4}
    return {k for k in keys if k}


def camel_words(name):
    return re.sub(r"(?<=[a-z])(?=[A-Z])", " ", name).lower()


index = {}  # module -> key -> (anchor, kind)
for module in MODULES:
    path = ROOT / module / ".context" / f"{module}-model.md"
    keys, current = {}, None
    for line in path.read_text(encoding="utf-8").splitlines():
        card = re.match(r"^##\s+(\*\*([^*]+)\*\*.*)$", line)
        if card:
            current = heading_anchor(card[1].strip())
            for k in variants(card[2]) | variants(camel_words(card[2])):
                keys.setdefault(k, (current, "class"))
            continue
        if re.match(r"^#\s", line):
            current = None
            continue
        term = re.match(r"^###\s+(.+)$", line)
        if term:
            anchor = current or heading_anchor(term[1].strip())
            kind = "class" if current else "term"
            for k in variants(term[1]):
                keys.setdefault(k, (anchor, kind))
    index[module] = keys

TERM = re.compile(r"\+\+(?!\[)([^+\n]+?)\+\+")


def owner(term, own):
    for module in [own] + [m for m in MODULES if m != own]:
        for k in variants(term):
            if k in index[module]:
                return module, index[module][k]
    return None


write = "--write" in sys.argv
stats = {"files": 0, "linked": 0, "graph": 0, "unlinked": {}}
for f in sorted(ROOT.joinpath("story_tests").rglob("*_story.test.md")):
    own = EPIC_MODULE[f.relative_to(ROOT / "story_tests").parts[0]]
    text = open(LP(f), encoding="utf-8").read()
    head, sep, rest = text.partition("### Examples")
    if not sep:
        head, sep, rest = text.partition("### Behaviors")
    tail_examples = ""

    def repl(m):
        term = m[1].strip()
        found = owner(term, own)
        if not found:
            stats["unlinked"][term.lower()] = stats["unlinked"].get(term.lower(), 0) + 1
            return m[0]
        module, (anchor, kind) = found
        rel = os.path.relpath(ROOT / module / ".context" / f"{module}-model.md", f.parent).replace("\\", "/")
        stats["linked"] += 1
        stats["graph"] += kind == "class"
        return f"++[{term}]({rel}#{anchor})++"

    # Link in the domain-terms list and in the steps; leave example tables as they are.
    parts = re.split(r"(?m)^(### Examples\n.*?)(?=^### Behaviors)", text, flags=re.S)
    new = "".join(p if p.startswith("### Examples") else TERM.sub(repl, p) for p in parts)
    if new != text:
        stats["files"] += 1
        if write:
            open(LP(f), "w", encoding="utf-8").write(new)

print(f"files changed: {stats['files']}, links: {stats['linked']} (to a class heading: {stats['graph']})")
top = sorted(stats["unlinked"].items(), key=lambda kv: -kv[1])
print(f"terms left unlinked: {len(top)} distinct, {sum(v for _, v in top)} uses; most used:")
for term, n in top[:40]:
    print(f"  {n:4}  {term}")
