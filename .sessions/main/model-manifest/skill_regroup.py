import re
from pathlib import Path
src = Path(".sessions/main/model-manifest/skill-language.md").read_text(encoding="utf-8")
paras, terms = {}, {}
for chunk in re.split(r"\n(?=### |\*[A-Z])", src):
    if chunk.startswith("### "):
        terms[chunk.split("\n",1)[0][4:].strip()] = chunk.strip()
    elif chunk.startswith("*"):
        g = chunk.split("*")[1]; paras[g] = chunk.strip()
order = [
 ("Skill", ["skill rank","skill check","skill modifier","trained only","Skill Mastery","circumstance modifier"]),
 ("Interaction Skill", ["interaction skill","Deception","Insight","Intimidation","Persuasion"]),
 ("Manipulation Skill", ["manipulation skill","Sleight of Hand","Technology","Treatment","Vehicles"]),
 ("Physical Skill", ["Acrobatics","Athletics","Stealth"]),
 ("Combat Skill", ["Close Combat","Ranged Combat"]),
 ("Knowledge & Awareness Skill", ["Expertise","Investigation","Perception"]),
]
used = [t for _, ts in order for t in ts]
assert sorted(used) == sorted(terms), (set(terms) ^ set(used))
out = ["## Language", ""]
for g, ts in order:
    out += [paras[g], ""]
    for t in ts:
        out += [terms[t], ""]
Path(".sessions/main/model-manifest/skill-language-grouped.md").write_text("\n".join(out), encoding="utf-8")
print(len(out))
