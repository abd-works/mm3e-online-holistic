import re, sys
from pathlib import Path
src = Path("equipment/.context/equipment-domain-sketch.md").read_text(encoding="utf-8")
out = Path(".sessions/main/model-manifest/equipment-norm/equipment/.context/equipment-domain-sketch.md")
blocks = re.split(r"^(?=#{2,3} )", src, flags=re.M)
res = []
for b in blocks:
    head = b.split("\n", 1)[0]
    if head == "## Key Abstractions":
        continue
    if head.startswith("### ") and "#### Decisions made" in b:
        b = "## " + b[4:]
    elif head.startswith("### "):
        b = re.sub(r"^### (.*?) \*is a type of\* .*$", r"### \1", b, count=1, flags=re.M)
    b = b.replace("#### Domain Language", "#### Domain language")
    res.append(b)
out.write_text("".join(res), encoding="utf-8")
