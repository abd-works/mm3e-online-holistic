"""Scratch: compose the power Language section by hand-declared groupings (sketch uses #### terms)."""
import io, re, sys
from pathlib import Path
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
ctx = Path("power/.context")
sk = (ctx / "power-domain-sketch.md").read_text(encoding="utf-8")
dl = (ctx / "power-domain-language.md").read_text(encoding="utf-8")
GROUPS = ["Effect Framework", "Effect Cost", "Modifier", "Attack Effect", "Defense Effect", "Mobility Effect",
          "Sensory Effect", "Control and General Effect", "Power Array"]
SUB = {"Domain Sketch", "Domain Language", "References", "Decisions made"}

def strip_fences(text):
    out, inf = [], False
    for l in text.splitlines():
        if l.startswith("```"):
            inf = not inf; continue
        if not inf: out.append(l)
    return out

lines = strip_fences(sk.split("## Boundary Domain")[0])
groups, paras, order = {}, {}, []
group, term, sub = None, None, None
pending_para = None
for l in lines:
    m3 = re.match(r"^### (.+)$", l); m4 = re.match(r"^#### (.+)$", l)
    if m3:
        name = m3[1].strip()
        if name in GROUPS:
            group, term, sub = name, None, None; pending_para = name; groups.setdefault(name, {})
        else:
            sub = None if term is None else sub
        continue
    if m4:
        name = m4[1].strip()
        if name in SUB:
            sub = name
        else:
            term, sub = name, None; pending_para = None
            groups[group].setdefault(term, {"lang": [], "sketch": [], "src": set()})
            order.append(term)
        continue
    if l.startswith("## ") or l.startswith("# "):
        continue
    if pending_para and l.strip() and not l.startswith("#") and pending_para not in paras:
        paras[pending_para] = l.strip(); pending_para = None; continue
    if term:
        t = groups[group][term]
        s = re.match(r"Source: (\S+)", l)
        if s: t["src"].add(s[1])
        if sub == "Domain Language" and (l.strip().startswith("-") or l.startswith("  ")) and l.strip():
            t["lang"].append(l.rstrip())
        if sub == "Domain Sketch" and l.strip().startswith("-"):
            t["sketch"].append(l.rstrip())

# earlier-stage language (domain-language file) for fallback / missing terms
early = {}
for b in re.split(r"^(?=### )", dl.split("# Boundary Domain")[0], flags=re.M):
    h = b.split("\n", 1)[0]
    if not h.startswith("### "): continue
    name = h[4:].strip()
    lang = re.search(r"#### Domain Language\n(.*?)(?=\n####|\Z)", b, re.S)
    early[name] = ([x.rstrip() for x in (lang[1] if lang else "").splitlines() if x.strip().startswith("-")],
                   set(re.findall(r"Source: (\S+)", b)))
missing = [t for t in early if t not in order]
print("sketch terms", len(order), "early terms", len(early), "missing", missing, file=sys.stderr)

out = ["## Language", ""]
for g in GROUPS:
    out += [f"*{g}* — {paras.get(g, '')}", ""]
    for term, t in groups[g].items():
        lang = t["lang"] or early.get(term, ([], set()))[0]
        src = t["src"] | early.get(term, ([], set()))[1]
        out += [f"### {term}", ""] + lang
        out += [x.replace("- Invariant:", "- **Invariant:**") for x in t["sketch"]]
        if src: out.append("- Sources: " + ", ".join(f"`.context/{s.split('.context/')[-1]}`" if ".context/" in s else f"`{s}`" for s in sorted(src)))
        out.append("")
# boundary
bd = sk.split("## Boundary Domain")[1]
out += ["*Boundary terms* — Terms this module uses but another module owns.", ""]
for b in re.split(r"^### ", bd, flags=re.M)[1:]:
    name, body = b.split("\n", 1)
    bl = [x.rstrip() for x in body.splitlines() if x.strip()]
    owned = [x for x in bl if x.startswith("Owned by:")]
    rest = [x for x in bl if x.startswith("-")]
    out += [f"### {name.strip()}", ""] + [f"- {o}" for o in owned] + rest + [""]
Path(sys.argv[1]).write_text("\n".join(out), encoding="utf-8")
