"""Write the ``## Language`` section of ``{module}-model.md`` from the domain-language/sketch chain.

Usage: python compose_language.py <module> <out_file>   (run from the project root)

Each class grouping of the latest stage becomes a class definition paragraph (``*Grouping* is ...``, taken from the
grouping's own opening paragraph in the sketch), followed by its terms as ``### term`` concept headings with their
language and sketch bullets. Boundary groupings (terms the module depends on but does not define) are listed last under
"Boundary terms". The class blocks of the model are written by hand after this section.
"""
import io
import re
import subprocess
import sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
module, out = sys.argv[1], Path(sys.argv[2])
sketch = (Path(module) / ".context" / f"{module}-domain-sketch.md").read_text(encoding="utf-8")
extract = subprocess.run([sys.executable, str(Path(__file__).with_name("extract_terms.py")), module],
                         capture_output=True, text=True, encoding="utf-8", check=True).stdout


def opening(group):
    m = re.search(rf"^## {re.escape(group)}\n+(.+?)\n", sketch, re.M)
    return m[1].strip() if m and not m[1].startswith("#") else ""


lines = ["## Language", ""]
for block in re.split(r"^## GROUP: ", extract, flags=re.M)[1:]:
    group, body = block.split("\n", 1)
    para = opening(group)
    if para:
        lines += [f"*{group}* — {para}", ""]
    else:
        lines += [f"*{group}*", ""]
    for term in re.split(r"^### ", body, flags=re.M)[1:]:
        name, bullets = term.split("\n", 1)
        bl = [b for b in bullets.strip().splitlines() if b.strip()]
        lines += [f"### {name.strip()}", ""] + bl + [""]
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text("\n".join(lines), encoding="utf-8")
print(out, len(lines), "lines")
