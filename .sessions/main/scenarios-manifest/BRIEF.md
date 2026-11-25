# Brief: turn acceptance criteria into CDD scenario files

Project root: `C:\dev\mm3e-online-holistic`. You convert one module's acceptance criteria (AC) into Given/When/Then
scenario markdown files, one file per story, at the exact paths a manifest gives. The AC files will be deleted after
this work, so everything they say that is behaviour must land in a scenario. Do not edit any other file.

## Inputs

- **Manifest** `.sessions/main/scenarios-manifest/{epic}.json`: one entry per story on the map, with `story` (the exact
  story name on the map, actor removed), `actor` (Player / GM / System), `path` (where to write), `map_path`.
- **Acceptance criteria** `{module}/.context/{module}-acceptance-criteria.md`: numbered WHEN/THEN/AND criteria per
  story, with domain terms and source evidence.
- **Context** you may read for values and meaning: `{module}/.context/{module}-domain-language.md`,
  `-domain-sketch.md`, `-key-abstractions.md`, `module-context.md`, `.context/consolidation-notes.md`, and the rules
  chunks the AC cite (`.context/sources/rules/HeroesHandbook-rules__chunk_NNN.md`). Read the AC in full first.
- **Pilot to copy the shape from**: `story_tests/resolve-checks/make-check/make-trait-check/make_trait_check_story.test.md`.

## Matching AC to stories

AC story headings may differ a little from the map (wording drift, merged or split stories, a different epic
grouping). Match each AC story to the manifest story it describes. Two map stories were renamed: "Balance on
Precarious Surface" is now **Keep Balance on Precarious Surface**, and "Transition Incapacitated Target to Dying" is
now **Move Incapacitated Target to Dying**. When one AC story covers several map stories, split its criteria between
them. When an AC story matches no map story, put its criteria on the closest map story only if it truly belongs there;
otherwise report it (see Report). Never add a story to the map and never invent a file path: write only the paths in
the manifest.

## File format (follow exactly)

```
## Story: <story name exactly as in the manifest>

**Story type:** user        (system when actor is System; user for Player and GM)

### Domain terms

- ++<term>++ — <plain gloss, from the AC/domain language>

### Evidence

| Source | Note |
|--------|------|
| `.context/sources/rules/HeroesHandbook-rules__chunk_035.md` | <what it says that matters> |

### Examples              (only when a scenario uses concrete values; one table per concept)

#### <concept>

| <concept> | example | <field> | <field> |
| --- | --- | --- | --- |
| <concept> | <example name> | <value> | <value> |

### Behaviors

#### Scenario: <outcome-oriented name>

*Given* <state the system checks, aggregate root first>  
  *And* <more state>  
*When* the **<Actor>** <domain intent, not a UI gesture>  
*Then* <observable result>  
  *And* <further result of the same When>  
  *But* <a record that is absent / an action not taken>
```

Every step line ends with two spaces. `*And*`/`*But*` lines are indented two spaces. Domain terms in steps are written
`++term++` and concrete values `*value*`. Do not link terms (no domain model exists yet).

## Rules the scenarios must meet

- **One AC criterion → one scenario** as a rule of thumb. A WHEN becomes the *When*; its THEN/AND become *Then*/*And*.
  Turn the condition hidden in a WHEN ("when the rank is above the cap") into a *Given*.
- **At most 7 scenarios per story.** Where criteria are one mechanic over many values, use one
  `#### Scenario Outline:` with `{field}` placeholders and an Examples table (a table only when more than 2 rows).
- **Main flow first**, then variations, then refusals and error cases.
- **Edge and error cases**: where the AC or the source states what happens (a cap, a floor, a refusal, a prerequisite
  missing, a repeated action), write it as an ordinary scenario. Do not invent outcomes the source does not state, and
  keep no list or table of "cases considered".
- **Given** only the state the rule reads. **When** holds the one operation under test, named as the actor's intent
  ("the Player sets the Strength rank"), never "clicks". **Then** states only what that When produced and what a person
  or the system can observe (a value, a refusal with its reason, a changed condition) — never "the next screen is".
- **System stories**: the *When* is the request or event arriving at the system ("When an ability rank changes"),
  the *Then* is what the system answers or changes.
- **Values come from the AC and the cited chunks** (ranks, costs, DCs, ±2/±5, PL limits). Put them in Examples.
  If a criterion needs a value no source gives, write the intended steps and add a line under the scenario:
  `> Evidence missing: <what is missing>`.
- Keep the AC's evidence: every chunk or doc an AC criterion cites goes into the Evidence table (path from the project root).
- Plain English throughout; no code identifiers.

A manifest story with no AC criteria at all gets **no file** (it is waiting for its scenarios). Do not write one.

## Report (your final message, keep it short)

1. Number of files written, and the list of manifest stories left without a file.
2. AC stories or criteria you could not place on any map story: AC heading + one line on what it covers.
3. Any criterion you dropped and why (should be none).
