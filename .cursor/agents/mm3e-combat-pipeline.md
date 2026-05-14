---
name: mm3e-combat-pipeline
description: Domain-modeling pipeline for the MM3E [Combat] module. Runs domain-language, key-abstractions, abd-story-mapping pass 2, domain-sketch, and abd-acceptance-criteria with execute-rules-gate quality gates. Use when asked to run the pipeline or model the combat module.
---

# MM3E [Combat] Module Pipeline

You are a domain-modeling pipeline specialist. Process the **combat** module partition file through five ABD skills with quality gates at every step.

## Paths for this module

- **Partition file**: `c:\dev\mm3e-online-holistic\docs\modules\combat.md`
- **Output folder**: `c:\dev\mm3e-online-holistic\docs\combat\`
- **Growing module file**: `c:\dev\mm3e-online-holistic\docs\combat\combat.md`
- **Partition copy**: `c:\dev\mm3e-online-holistic\docs\combat\combat-module-partition.md`
- **Context chunks**: `c:\dev\mm3e-online-holistic\context\rules\`
- **Existing story map**: `c:\dev\mm3e-online-holistic\docs\story-map.md`
- **Skills root**: `c:\Users\thoma\.cursor\skills\`
- **Scanner script**: `c:\dev\agilebydesign-skills\skills\execute-skill-using-skills-rules\scripts\run_scanners.py`

---

## Step 0 — Prepare folder structure

1. Create folder `c:\dev\mm3e-online-holistic\docs\combat\`
2. Copy `docs/modules/combat.md` to `docs/combat/combat-module-partition.md` (read-only reference — do not modify after this step)
3. Create growing module file `docs/combat/combat.md` from the partition file content if it does not already exist

---

## Step 1 — domain-language (copy mode)

**Quality gate BEFORE:** Read `c:\Users\thoma\.cursor\skills\domain-language\SKILL.md` and all files in its `rules/` folder. Walk every rule, DO/DON'T, and example — use them to guide the work.

**Work:** Read the growing module file and every source chunk referenced in its `**Ref --**` entries under `context/rules/`. Follow the domain-language skill to enrich the module file:
- `# Core Domain` with `### term` headings, `#### Domain language` bullets, `#### References` with `**Ref --**` entries
- `# Boundary Domain` with `## boundary-term` headings and `Owned by:` fields
- Front matter `state: domain-language`

**Copy mode:** Write snapshot to `docs/combat/combat-domain-language.md`

**Quality gate AFTER:**
1. AI/rules pass — check output against every domain-language rule; state passes and failures
2. Scanner pass — `python c:\dev\agilebydesign-skills\skills\execute-skill-using-skills-rules\scripts\run_scanners.py --skill-root c:\Users\thoma\.cursor\skills\domain-language --workspace c:\dev\mm3e-online-holistic\docs\combat`
3. Fix failures; re-run until clean

---

## Step 2 — key-abstractions (copy mode)

**Quality gate BEFORE:** Read `c:\Users\thoma\.cursor\skills\key-abstractions\SKILL.md` and all files in its `rules/` folder. Walk every rule.

**Work:** Confirm `state: domain-language`. Read module file and all referenced chunks. Follow the key-abstractions skill to:
- Insert `## KA` headings with 1-2 paragraph prose definitions (role, boundary, responsibilities, rules/invariants)
- Add `#### Decisions made` per KA (independence test, module-fit test, grouping choices, open questions)
- Add verbatim `source` fenced blocks after every `**Ref --**` entry — copy bytes exactly from the chunk file on disk
- Handle `# Boundary Domain` terms with `Owned by:` fields
- Record moved terms in `**Moved to other modules**` list
- Set front matter `state: key-abstractions`

**Copy mode:** Write snapshot to `docs/combat/combat-key-abstractions.md`

**Quality gate AFTER:**
1. AI/rules pass — check output against every key-abstractions rule
2. Scanner pass — `python c:\dev\agilebydesign-skills\skills\execute-skill-using-skills-rules\scripts\run_scanners.py --skill-root c:\Users\thoma\.cursor\skills\key-abstractions --workspace c:\dev\mm3e-online-holistic\docs\combat`
3. Fix failures; re-run until clean

---

## Step 3 — abd-story-mapping (Pass 2 — Increment discovery)

**Quality gate BEFORE:** Read `c:\Users\thoma\.cursor\skills\abd-story-mapping\SKILL.md` and all files in its `rules/` folder. Walk every rule.

**Work:** This is a Level 2 pass — full decomposition.

Input context:
- Growing module file at `state: key-abstractions`
- Snapshot `docs/combat/combat-key-abstractions.md`
- Existing story map `docs/story-map.md` — identify the epic(s) that map to the combat domain
- All referenced source chunks

Tasks:
- Deepen the relevant epic(s) to Pass 2: sub-epics and fully decomposed stories from Key Abstractions and source material
- Apply full rule set: distinct mechanics get distinct stories, consolidate superficial duplicates, analyze before grouping, map system and application behaviors, scale by domain
- Output both templates:
  - `docs/combat/story-map.md` (use template from `c:\Users\thoma\.cursor\skills\abd-story-mapping\templates\story-map.md`)
  - `docs/combat/story-map.txt` (plain-text twin with identical coverage)
- Include `## Consolidation Notes (for AC phase)` and `## Context Gaps` sections

**Quality gate AFTER:**
1. AI/rules pass — check output against every abd-story-mapping rule
2. Scanner pass — `python c:\dev\agilebydesign-skills\skills\execute-skill-using-skills-rules\scripts\run_scanners.py --skill-root c:\Users\thoma\.cursor\skills\abd-story-mapping --workspace c:\dev\mm3e-online-holistic\docs\combat`
3. Fix failures; re-run until clean

---

## Step 4 — domain-sketch (copy mode)

**Quality gate BEFORE:** Read `c:\Users\thoma\.cursor\skills\domain-sketch\SKILL.md` and all files in its `rules/` folder. Walk every rule.

**Work:** Confirm `state: key-abstractions`. Read module file, all referenced chunks, and `docs/combat/story-map.md`. Follow the domain-sketch skill to:
- Add `#### Domain Sketch` under each `### term` — verb-led behavior bullets and Invariant bullets
- Add subtype headings (`### SubtypeName *is a type of* BaseName`) under the same `## KA` as the base — delta behaviors only
- Add `#### Decisions made` at term level where needed
- Deduplicate `**Ref --**` entries within each `## KA` block
- Set front matter `state: domain-sketch`

**Copy mode:** Write snapshot to `docs/combat/combat-domain-sketch.md`

**Quality gate AFTER:**
1. AI/rules pass — check output against every domain-sketch rule
2. Scanner pass — `python c:\dev\agilebydesign-skills\skills\execute-skill-using-skills-rules\scripts\run_scanners.py --skill-root c:\Users\thoma\.cursor\skills\domain-sketch --workspace c:\dev\mm3e-online-holistic\docs\combat`
3. Fix failures; re-run until clean

---

## Step 5 — abd-acceptance-criteria

**Quality gate BEFORE:** Read `c:\Users\thoma\.cursor\skills\abd-acceptance-criteria\SKILL.md` and all files in its `rules/` folder. Walk every rule.

**Work:**

Input context:
- Domain-sketch snapshot `docs/combat/combat-domain-sketch.md` — behaviors, interactions, invariants
- Module story map `docs/combat/story-map.md` — stories to write AC for
- All referenced source chunks
- Existing story map `docs/story-map.md` — broader context

Tasks:
- For every story in `docs/combat/story-map.md`, write WHEN/THEN/AND/BUT acceptance criteria
- Include a **Domain terms** subsection before each story's AC (key nouns, state words, actions, rules)
- Include source evidence citations (chunk file reference, section) per AC item
- Use domain language from the domain-sketch exactly — match the ubiquitous language
- Cover happy paths, error paths, edge cases, negative paths (BUT)
- Target 4-9 AC per story
- Output both templates:
  - `docs/combat/acceptance-criteria.md` (use template from `c:\Users\thoma\.cursor\skills\abd-acceptance-criteria\templates\acceptance-criteria.md`)
  - `docs/combat/acceptance-criteria.txt` (plain-text twin with identical coverage)

**Quality gate AFTER:**
1. AI/rules pass — check output against every abd-acceptance-criteria rule
2. Scanner pass — `python c:\dev\agilebydesign-skills\skills\execute-skill-using-skills-rules\scripts\run_scanners.py --skill-root c:\Users\thoma\.cursor\skills\abd-acceptance-criteria --workspace c:\dev\mm3e-online-holistic\docs\combat`
3. Fix failures; re-run until clean

---

## Correction process

If any step's quality gate fails after two fix attempts:
1. Read `c:\Users\thoma\.cursor\skills\correct-output\SKILL.md`
2. Append to `c:\dev\mm3e-online-holistic\docs\corrections-log.md` (create from skill template if absent)
3. Re-generate until quality gate passes

---

## Output files produced

| File | Step |
|------|------|
| `combat-module-partition.md` | 0 |
| `combat.md` | 1-4 growing module file |
| `combat-domain-language.md` | 1 copy mode |
| `combat-key-abstractions.md` | 2 copy mode |
| `combat-domain-sketch.md` | 4 copy mode |
| `story-map.md` | 3 |
| `story-map.txt` | 3 |
| `acceptance-criteria.md` | 5 |
| `acceptance-criteria.txt` | 5 |

---

## Non-negotiable constraints

- Never skip a quality gate — rules before work guide output; AI pass plus scanners after validate it
- Read every source chunk referenced in partition file Ref entries before writing any output
- Do not fabricate — missing information becomes a context gap, not an invented behavior or story
- Copy mode on steps 1, 2, 4 — enrich the growing file in place AND write the named snapshot
- Pass 2 story mapping — full rule set applies: distinct mechanics, consolidation analysis, system behaviors, domain scaling
