# Brief: turn a module's domain-language chain into its Clean Engineering model file

Project root: `C:\dev\mm3e-online-holistic`. Each module folder `{module}/.context/` holds one document at three
stages: `{module}-domain-language.md` (language only), `{module}-key-abstractions.md` (adds the class groupings, the
`## Key Abstraction` headings) and `{module}-domain-sketch.md` (adds `#### Domain Sketch` bullets: what each thing
holds, does and must keep true). You write the single canonical model document **`{module}/.context/{module}-model.md`**
from that chain. It is a Clean Engineering *model* that is deliberately incomplete: full language, a module card, and
class skeletons for the main classes only. Do not delete or edit the three stage files or any other file; the caller
removes them after checking your result.

## Copy the pilot

`ability/.context/ability-model.md` is the finished pilot. Match its shape exactly:

1. **`## Language`** — generate it, do not hand-type it:
   `python .sessions/main/model-manifest/compose_language.py {module} .sessions/main/model-manifest/{module}-language.md`
   (run from the project root). It writes each grouping as `*Grouping* — paragraph`, then every term as `### term`
   with its language bullets, sketch bullets (`**Invariant:**` marked) and `Sources:` chunks. Check its output reads
   cleanly; if a grouping heading is junk (e.g. a sentence picked up from a chapter dump, or "Key Abstractions" used as
   a wrapper), fix that heading by hand in your copy. Terms listed under "(not grouped)" came from earlier stages only:
   put each under the grouping it belongs to.
2. **`---` then `# {module}`** — the module card, as in the pilot:
   `- **Purpose:**` (the job a caller hires the module for, one sentence, from `module-context.md` Scope),
   `- **Seam (terms):**` (the class names you model), `- **Dependencies (one-way):**` (other modules this one uses,
   from the sketch's Boundary terms / "Owned by:" lines, e.g. `character-construction (power point, power level)`).
   Module names are the folder names: ability, advantage, character-construction, check-resolution, combat, equipment,
   power, skill.
3. **`## Constraint`** — one or two sentences: what callers must or must not do at this seam.
4. **Class skeletons** — one `## **ClassName**` block per main class (bold name is required, the graph reads only bold
   headings), in the pilot's compact form:
   ```
   ## **ClassName**

   + ClassName(param: Type)
   	// invariant (must / never / always / before / after about its own state)
   ------
   + << composition >> part: Type
   + << association >> other: Type
   + plainProperty: Type
   	// invariant about this property, only when one exists
   ----
   + operationName(param: Type): ReturnType
   	// rule that holds when it runs
   	-> collaborator.operation
   ```
   (Indent comments and interactions with a TAB.)

## Which classes, and how much

- One class per key abstraction that has its own identity, state and behaviour; add a collection class only when the
  sources treat the group as a thing (e.g. Abilities = the eight abilities). Aim for roughly 3–8 classes per module.
- Apply `class-not-property-instance-or-subtype`: named variants that differ only by data are **instances** or a
  property (Strength is an Ability with name Strength, not a class); a state is a property (`isDebilitated`); write a
  subtype only when the variant changes what the thing does.
- Properties and operations come **only** from the sketch bullets, language and invariants already in the chain —
  verbs the source names (set, buy, apply, resolve, recover…). Keep it incomplete: a class may have just a constructor
  and two or three members. Do not invent mechanics, names or values the chain does not state.
- Invariants come from the chain's `Invariant:` bullets, placed on the class/property/operation they constrain.
- Interactions (`-> collaborator.operation`) only where the chain says this thing asks another to act; a collaborator
  in another module is named by the module's term (e.g. `-> powerPoints.spend`).
- Names: classes PascalCase from the domain noun (`vocabulary-traces-to-source`), members camelCase, no abbreviations,
  no Manager/Service/Helper classes.

## check-resolution is different

`check-resolution/.context/` has no domain-language chain; it already has a typed model
(`check-resolution-object-model.md`) plus `check-resolution-ubiquitous-language.md` and `check-resolution-crc.md`.
For it: build `check-resolution-model.md` with `## Language` from the ubiquitous-language file (one `### term` per term,
bullets, sources), the module card + Constraint, and class blocks converted from the object model into the pilot's
format (`## **ClassName**` headings, `+`/`-` members, `------`/`----` separators, `//` invariants, `->` interactions,
`<< composition >>`/`<< aggregation >>`/`<< association >>` on properties). Keep every class, property, operation,
invariant and interaction the object model has — that one is not incomplete. Do not touch the CRC, class diagram or
other files. There is no `module-context.md` for check-resolution: take Purpose from the object model's Scope line and
say so in your report.

## Check before you finish

Parse your file with CDD's own reader and report what it read:

```
cd C:\dev\abd-context-driven-delivery
python -c "import sys;sys.path.insert(0,'.');from cdd_guidance.practices.clean_engineering.model.markdown.markdown_class_model import MarkdownCleanEngineeringModel as M;t=open(r'C:/dev/mm3e-online-holistic/{module}/.context/{module}-model.md',encoding='utf-8').read();m=M().parse(t,'x');[print(mod.name,[(c.name,len(c.operations),len(c.properties)) for c in mod.classes]) for mod in m.modules]"
```

It must print one module named `{module}` with your classes. Fix the file until it does.

## Report (short)

1. Classes written, each with its member counts (from the parse check).
2. Any term or grouping you could not place, and any heading you fixed by hand.
3. Anything in the chain you left out of the classes on purpose (keep it in the Language section either way).
