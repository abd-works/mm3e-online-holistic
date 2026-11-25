"""Scratch: character-construction variant of compose_language.py (its sketch uses '#### Domain Language',
plain-line sketch bullets, and source fences containing '##' headings)."""
import io, re, sys
from pathlib import Path
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
module = "character-construction"
ctx = Path(module) / ".context"

def parse(path):
    groups, group, boundary = {}, "(not grouped)", False
    intro = {}
    owned = {}
    lines = path.read_text(encoding="utf-8").splitlines()
    fence = False; term = None; section = None; pending_intro = None
    for ln in lines:
        if ln.startswith("```"):
            fence = not fence; continue
        if fence:
            if term and section == "refs":
                pass
            continue
        if ln.startswith("# "):
            boundary = ln.strip() == "# Boundary Domain"; term = None; section = None; continue
        if ln.startswith("## ") and not re.match(r"## (Module|CHAPTER|Domain logic)", ln):
            group = ln[3:].strip(); term = None; section = None; pending_intro = group
            if boundary:
                term = group; groups.setdefault("Boundary terms", {})[term] = [[], [], []]
                g = "Boundary terms"
            else:
                groups.setdefault(group, {})
            continue
        if ln.startswith("### "):
            term = ln[4:].strip(); section = None; pending_intro = None
            if not boundary:
                groups.setdefault(group, {})[term] = [[], [], []]
            continue
        if ln.startswith("#### "):
            h = ln[5:].strip().lower()
            section = {"domain language": "lang", "domain sketch": "sketch", "references": "refs"}.get(h)
            pending_intro = None if h.startswith("decisions") else pending_intro
            continue
        if pending_intro and ln.strip() and not boundary:
            if pending_intro not in intro:
                intro[pending_intro] = ln.strip()
            pending_intro = None; continue
        if boundary and term and ln.startswith("Owned by:"):
            owned[term] = ln.strip(); continue
        g = "Boundary terms" if boundary else group
        if not term or term not in groups.get(g, {}):
            continue
        rec = groups[g][term]
        if section == "lang" and (ln.strip().startswith("-") or ln.startswith("  ")) and ln.strip():
            rec[0].append(ln)
        elif section == "sketch" and ln.strip() and ln.strip() != "---":
            s = ln.strip()
            if not s.startswith("-"):
                s = "- " + s
            rec[1].append(s.replace("- Invariant:", "- **Invariant:**"))
        elif section == "refs":
            m = re.match(r"Source: (\S+)", ln)
            if m and m[1] not in rec[2]:
                rec[2].append(m[1])
    # drop headings without language (chapter-dump ### lines)
    for g in list(groups):
        groups[g] = {t: v for t, v in groups[g].items() if v[0]}
    return groups, intro, owned

latest, intro, owned = parse(ctx / f"{module}-domain-sketch.md")
known = {t.lower() for g in latest.values() for t in g}
for st in ("key-abstractions", "domain-language"):
    g2, _, _ = parse(ctx / f"{module}-{st}.md")
    for grp, terms in g2.items():
        for t, v in terms.items():
            for gg in latest.values():
                for tt, vv in gg.items():
                    if tt.lower() == t.lower() and not vv[2]:
                        vv[2].extend(v[2])
            if t.lower() not in known:
                latest.setdefault("(not grouped)", {})[t] = v; known.add(t.lower())
                print("NOT GROUPED:", grp, "/", t, file=sys.stderr)
out = ["## Language", ""]
order = [g for g in latest if g not in ("Boundary terms", "(not grouped)")] + [g for g in ("(not grouped)", "Boundary terms") if g in latest]
for grp in order:
    terms = latest[grp]
    if not terms:
        print("EMPTY GROUP:", grp, file=sys.stderr); continue
    out += [f"*{grp}* — {intro[grp]}" if grp in intro else f"*{grp}*", ""]
    for t, (lang, sk, srcs) in terms.items():
        out += [f"### {t}", ""]
        if t in owned:
            out.append(f"- {owned[t]}")
        out += lang + sk
        if srcs:
            out.append("- Sources: " + ", ".join(f"`{s}`" for s in sorted(srcs)))
        out.append("")
Path(sys.argv[1]).write_text("\n".join(out), encoding="utf-8")
print(sum(len(v) for v in latest.values()), "terms", {g: len(v) for g, v in latest.items()})
