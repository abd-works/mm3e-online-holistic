"""One-off: compose advantage ## Language from its sketch (Key Abstractions wrapper, #### terms)."""
import re, io, sys
from pathlib import Path
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
sk = Path("advantage/.context/advantage-domain-sketch.md").read_text(encoding="utf-8")
core, boundary = sk.split("\n# Boundary Domain", 1)
core = re.sub(r"```source.*?```", "", core, flags=re.S)
boundary = re.sub(r"```source.*?```", "", boundary, flags=re.S)
out = ["## Language", ""]

def term_block(name, body):
    lines = [f"### {name}", ""]
    # language: bullets before first ** or ####
    lang = re.split(r"\n(?=\*\*Ref|#### )", body, 1)[0]
    if lang.lstrip().startswith("#### Domain Language"):
        lang = lang.split("#### Domain Language", 1)[1]
    lb = [l for l in lang.splitlines() if l.strip().startswith("-")]
    m = re.search(r"#### Domain Language\n(.*?)(?=\n\*\*Ref|\n#### |\Z)", body, re.S)
    if m and not lb:
        lb = [l for l in m[1].splitlines() if l.strip().startswith("-")]
    s = re.search(r"#### Domain Sketch\n(.*?)(?=\n#### |\n---|\Z)", body, re.S)
    sb, inv = [], []
    if s:
        for l in s[1].splitlines():
            if l.strip().startswith("-"):
                sb.append(l)
            elif l.startswith("Invariant:"):
                inv += [p.strip().rstrip(".") for p in l[len("Invariant:"):].split(";") if p.strip()]
    srcs = sorted(set(re.findall(r"Source: (\S+)", body)))
    lines += lb + sb + [f"- **Invariant:** {i}." for i in inv]
    if srcs:
        lines.append("- Sources: " + ", ".join(f"`{x}`" for x in srcs))
    return lines + [""]

# sources must be read from the un-stripped text; reparse with original for Source lines
orig_core = sk.split("\n# Boundary Domain", 1)[0]
groups = re.split(r"\n(?=### [^\n]+\n\n[^\n]+\n\n#### Decisions made\n)", orig_core)[1:]
for g in groups:
    gname = g.split("\n", 1)[0][4:].strip()
    para = g.split("\n")[2].strip()
    out += [f"*{gname}* — {para}", ""]
    for t in re.split(r"\n(?=#### (?!Decisions made|Domain Sketch|Domain Language)[^\n]+\n)", g)[1:]:
        name, body = t.split("\n", 1)
        body = re.sub(r"```source.*?```", "", body, flags=re.S)
        out += term_block(name[5:].strip(), body)
out += ["*Boundary terms* — Terms this module uses but does not define; each is owned by another module and appears here only as advantages read or spend it.", ""]
for t in re.split(r"\n(?=## (?!CHAPTER)[^\n]+\n)", sk.split("\n# Boundary Domain", 1)[1])[1:]:
    name, body = t.split("\n", 1)
    body = re.sub(r"```source.*?```", "", body, flags=re.S)
    out += term_block(name[3:].strip(), body)
Path(sys.argv[1]).write_text("\n".join(out), encoding="utf-8")
print(len(out))
