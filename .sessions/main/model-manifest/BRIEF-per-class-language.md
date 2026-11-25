# Brief: move a model's language onto its classes

Project root: `C:\dev\mm3e-online-holistic`. Each `{module}/.context/{module}-model.md` currently has one consolidated
`## Language` section at the top (class-grouping paragraphs `*Grouping* — …` and `### term` entries with `-` bullets),
then `---`, the module card `# {module}` (Purpose / Seam / Dependencies), `## Constraint`, and the class cards
`## **ClassName**`. CDD's template now puts language **on each class**: you restructure the file so there is no
`## Language` section and every term sits on the card of the class that owns it. Change nothing else: keep every
bullet's wording, every class member, invariant and interaction exactly as they are. Edit only your module's model file.

## Target shape

```
# {module}

### {module-level term — only for a term no class of this module owns, see below}

- …

- **Purpose:** …
- **Seam (terms):** …
- **Dependencies (one-way):** …

## Constraint

…

## **ClassName**

*ClassName* is {definition paragraph — from the grouping paragraph that described this class, or the class's own
term bullets; one or two sentences: the job a caller hires it for, then what it holds and does}.

### {term this class owns}

- {its bullets, unchanged, including **Invariant:** and Sources: lines}

### {next term this class owns}

- …

+ ClassName(param: Type)
	// …
------
…
```

## Which class owns a term

- The class whose state or behaviour the term names: the class itself (`ability` → Ability), a property
  (`ability rank` → Ability, `defense class` → Defense), a state (`absent ability`, `debilitated` → Ability), or an
  instance of it (`Strength (STR)` → Ability; `Dodge` → Defense; `Acrobatics` → Skill or its subtype).
- A subtype's own terms go on the subtype's card (`## **InteractionSkill** : Skill`).
- A grouping paragraph that described a class becomes that class's definition paragraph (reword only enough to open
  with `*ClassName* is`). A grouping paragraph that matches no class is kept as a module-level paragraph under `# {module}`.
- **Boundary terms** (a `*Boundary terms*` grouping, or a term with an `Owned by:` line naming another module): they are
  defined in the owning module, so they are **not** repeated here. Delete them only if the owning module's model file
  (`{owner}/.context/{owner}-model.md`) already has that term (search it, case-insensitive). If it does not, keep the
  term as a module-level `### term` under `# {module}`.
- A term no class of this module owns and that is not a boundary term (e.g. a rule or a procedure the classes don't
  model yet) is kept as a module-level `### term` under `# {module}`, before the Purpose line.

## Hard rules (the reader depends on them)

- Above a class's `+ Constructor(` line, no line may start with `+`, and no language bullet may start with
  `- ` immediately followed by `name(` with no space (e.g. `- _foo(`). Every language bullet starts with `- ` and
  normal prose. Definition paragraphs start with `*ClassName*`.
- A class card with no constructor line (a `//` note in its place) keeps that note **after** its language.
- Do not use bold `**…**` in any `###` term heading (bold headings are read as classes).
- Remove the `## Language` heading and the `---` that separated it from the card.

## Check before you finish

1. **No term lost:** count `### ` term headings in the file before you start, and count them after plus the boundary
   terms you deleted (each one you deleted must be found in its owner's model). Report the numbers.
2. **The reader reads it:** run with CDD's fixed reader (in the worktree), from any folder:
   ```
   cd C:\dev\abd-cdd-class-language
   python -c "import sys;sys.path.insert(0,'.');from cdd_guidance.practices.clean_engineering.model.markdown.markdown_class_model import MarkdownCleanEngineeringModel as M;t=open(r'C:/dev/mm3e-online-holistic/{module}/.context/{module}-model.md',encoding='utf-8').read();m=M().parse(t,'x');[print(mod.name,[(c.name,len(c.operations),len(c.properties),len(c.intent)) for c in mod.classes]) for mod in m.modules]"
   ```
   It must print one module `{module}` with the same classes and the same operation/property counts as before your
   change (run it once before you start to get them), and every class must have a non-zero intent length.

## Report (short)

Classes with their terms count; module-level terms kept (and why); boundary terms deleted (with the owner file that
defines each); the before/after term counts and member counts.
