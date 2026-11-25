# Graph rule validation

**Generated:** 2026-11-25 18:54:37 UTC
**Project:** mm3e-online-holistic
**Action:** validate (graph JSON + AI rules)

**Graph sources:**
- `C:\dev\mm3e-online-holistic\.sessions\main\.context\checked-graphs\stories-scenarios-20261125T185435\graph.json`

## Summary

**Total graph violations:** 18
**Rules with graph hits:** 2
**Candidates for the judge to read:** 16. A rule that requires a judge listed each; none is a violation until the judge reads it and fails it.
**AI rules in scope:** 24

## Rules

Each rule names where its text is kept, then any graph scanner hits (`**[graph rule]**`). The judgment is appended after the rules, in the shape the Validate action gives (`cdd_guidance/actions/validate/validate.md`, step 6). A hit marked `**CANDIDATE**` comes from a rule that requires a judge: its check only lists places to read, so read each and fail the rule only where the reading finds it broken.

### `vocabulary-traces-to-domain-source`

Rule text: [stories/stories.md:24](C:\Users\jeffa\.cdd\runtime\cdd_guidance\practices\stories\stories.md#L24)

### `read-all-source-context-in-full`

Rule text: [stories/stories.md:25](C:\Users\jeffa\.cdd\runtime\cdd_guidance\practices\stories\stories.md#L25)

### `do-not-invent-requirements`

Rule text: [stories/stories.md:26](C:\Users\jeffa\.cdd\runtime\cdd_guidance\practices\stories\stories.md#L26)

### `gwt-steps-trace-to-domain-operations`

Rule text: [stories/stories.md:167](C:\Users\jeffa\.cdd\runtime\cdd_guidance\practices\stories\stories.md#L167)

### `behavioral-and-system-observable-outcomes`

Rule text: [stories/stories.md:168](C:\Users\jeffa\.cdd\runtime\cdd_guidance\practices\stories\stories.md#L168)

### `explore-full-interaction-surface`

Rule text: [stories/stories.md:169](C:\Users\jeffa\.cdd\runtime\cdd_guidance\practices\stories\stories.md#L169)

### `edge-and-error-cases-have-scenarios`

Rule text: [stories/stories.md:170](C:\Users\jeffa\.cdd\runtime\cdd_guidance\practices\stories\stories.md#L170)

### `examples-trace-domain-model`

Rule text: [stories/stories.md:171](C:\Users\jeffa\.cdd\runtime\cdd_guidance\practices\stories\stories.md#L171)

### `reconcile-live-immediately`

Rule text: [stories/stories.md:172](C:\Users\jeffa\.cdd\runtime\cdd_guidance\practices\stories\stories.md#L172)

### `flagged-writes-intended-gwt`

Rule text: [stories/stories.md:173](C:\Users\jeffa\.cdd\runtime\cdd_guidance\practices\stories\stories.md#L173)

### `main-flow-first`

Rule text: [stories/stories.md:174](C:\Users\jeffa\.cdd\runtime\cdd_guidance\practices\stories\stories.md#L174)

### `scenarios-name-a-story-on-the-map`

Rule text: [stories/stories.md:175](C:\Users\jeffa\.cdd\runtime\cdd_guidance\practices\stories\stories.md#L175)

### `given-only-what-the-system-checks`

Rule text: [stories/stories.md:176](C:\Users\jeffa\.cdd\runtime\cdd_guidance\practices\stories\stories.md#L176)

### `given-names-complex-state-root-first`

Rule text: [stories/stories.md:177](C:\Users\jeffa\.cdd\runtime\cdd_guidance\practices\stories\stories.md#L177)

### `but-marks-missing-state`

Rule text: [stories/stories.md:178](C:\Users\jeffa\.cdd\runtime\cdd_guidance\practices\stories\stories.md#L178)

### `when-holds-the-operation`

Rule text: [stories/stories.md:179](C:\Users\jeffa\.cdd\runtime\cdd_guidance\practices\stories\stories.md#L179)

### `when-names-intent-not-interface-gesture`

Rule text: [stories/stories.md:180](C:\Users\jeffa\.cdd\runtime\cdd_guidance\practices\stories\stories.md#L180)

### `expressive-system-interactions`

Rule text: [stories/stories.md:181](C:\Users\jeffa\.cdd\runtime\cdd_guidance\practices\stories\stories.md#L181)

### `and-chaining`

Rule text: [stories/stories.md:182](C:\Users\jeffa\.cdd\runtime\cdd_guidance\practices\stories\stories.md#L182)

### `outline-requires-many-permutations`

Rule text: [stories/stories.md:183](C:\Users\jeffa\.cdd\runtime\cdd_guidance\practices\stories\stories.md#L183)

### `plain-english-gwt-steps`

Rule text: [stories/stories.md:184](C:\Users\jeffa\.cdd\runtime\cdd_guidance\practices\stories\stories.md#L184)

### `seed-prior-story-as-given`

Rule text: [stories/stories.md:185](C:\Users\jeffa\.cdd\runtime\cdd_guidance\practices\stories\stories.md#L185)

### `domain-terms-link-to-model`

Rule text: [stories/stories.md:186](C:\Users\jeffa\.cdd\runtime\cdd_guidance\practices\stories\stories.md#L186)

### `then-observes-an-example`

Rule text: [stories/stories.md:187](C:\Users\jeffa\.cdd\runtime\cdd_guidance\practices\stories\stories.md#L187)

### `branch-on-mechanical-uniqueness`

Rule text: [stories/stories.md:87](C:\Users\jeffa\.cdd\runtime\cdd_guidance\practices\stories\stories.md#L87)

**Candidates for the judge to read:** 2

- [?] **CANDIDATE** **[graph rule]** - [.context/story-map.md](C:\dev\mm3e-online-holistic\.context\story-map.md#L130): SubEpic `Use Combat Skills`: Stories under 'Use Combat Skills' share the same verb 'add'; split by distinct mechanics or merge.
- [?] **CANDIDATE** **[graph rule]** - [.context/story-map.md](C:\dev\mm3e-online-holistic\.context\story-map.md#L174): SubEpic `Apply Passive Combat Bonus`: Stories under 'Apply Passive Combat Bonus' share the same verb 'apply'; split by distinct mechanics or merge.

### `child-count-fits-layer`

Rule text: [stories/stories.md:85](C:\Users\jeffa\.cdd\runtime\cdd_guidance\practices\stories\stories.md#L85)

**Graph violations:** 15

- [X] **ERROR** **[graph rule]** - [.context/story-map.md](C:\dev\mm3e-online-holistic\.context\story-map.md#L28): Epic `Translate Rank to Measure`: epic 'Translate Rank to Measure': 2 stories (target 4-9)
- [X] **ERROR** **[graph rule]** - [.context/story-map.md](C:\dev\mm3e-online-holistic\.context\story-map.md#L102): SubEpic `Use Interaction Skills`: sub-epic 'Use Interaction Skills': 15 stories (target 2-9)
- [X] **ERROR** **[graph rule]** - [.context/story-map.md](C:\dev\mm3e-online-holistic\.context\story-map.md#L118): SubEpic `Use Physical Skills`: sub-epic 'Use Physical Skills': 11 stories (target 2-9)
- [X] **ERROR** **[graph rule]** - [.context/story-map.md](C:\dev\mm3e-online-holistic\.context\story-map.md#L133): SubEpic `Use Manipulation Skills`: sub-epic 'Use Manipulation Skills': 18 stories (target 2-9)
- [X] **ERROR** **[graph rule]** - [.context/story-map.md](C:\dev\mm3e-online-holistic\.context\story-map.md#L152): SubEpic `Use Knowledge and Awareness Skills`: sub-epic 'Use Knowledge and Awareness Skills': 10 stories (target 2-9)
- [X] **ERROR** **[graph rule]** - [.context/story-map.md](C:\dev\mm3e-online-holistic\.context\story-map.md#L214): Epic `Configure Powers`: epic 'Configure Powers': 10 children (target 2-9)
- [X] **ERROR** **[graph rule]** - [.context/story-map.md](C:\dev\mm3e-online-holistic\.context\story-map.md#L215): SubEpic `Configure Attack Effect`: sub-epic 'Configure Attack Effect': 12 stories (target 2-9)
- [X] **ERROR** **[graph rule]** - [.context/story-map.md](C:\dev\mm3e-online-holistic\.context\story-map.md#L238): SubEpic `Configure Mobility Effect`: sub-epic 'Configure Mobility Effect': 11 stories (target 2-9)
- [X] **ERROR** **[graph rule]** - [.context/story-map.md](C:\dev\mm3e-online-holistic\.context\story-map.md#L250): SubEpic `Configure Sensory Effect`: sub-epic 'Configure Sensory Effect': 11 stories (target 2-9)
- [X] **ERROR** **[graph rule]** - [.context/story-map.md](C:\dev\mm3e-online-holistic\.context\story-map.md#L262): SubEpic `Configure Control Effect`: sub-epic 'Configure Control Effect': 15 stories (target 2-9)
- [X] **ERROR** **[graph rule]** - [.context/story-map.md](C:\dev\mm3e-online-holistic\.context\story-map.md#L278): SubEpic `Configure General Effect`: sub-epic 'Configure General Effect': 15 stories (target 2-9)
- [X] **ERROR** **[graph rule]** - [.context/story-map.md](C:\dev\mm3e-online-holistic\.context\story-map.md#L294): SubEpic `Apply Per-Rank Modifiers`: sub-epic 'Apply Per-Rank Modifiers': 10 stories (target 2-9)
- [X] **ERROR** **[graph rule]** - [.context/story-map.md](C:\dev\mm3e-online-holistic\.context\story-map.md#L305): SubEpic `Apply Flat Modifiers`: sub-epic 'Apply Flat Modifiers': 12 stories (target 2-9)
- [X] **ERROR** **[graph rule]** - [.context/story-map.md](C:\dev\mm3e-online-holistic\.context\story-map.md#L450): SubEpic `Add Headquarters Features`: sub-epic 'Add Headquarters Features': 10 stories (target 2-9)
- [X] **ERROR** **[graph rule]** - [.context/story-map.md](C:\dev\mm3e-online-holistic\.context\story-map.md#L511): SubEpic `Perform Combat Maneuvers`: sub-epic 'Perform Combat Maneuvers': 14 stories (target 2-9)

### `story-name-captures-system-mechanic`

Rule text: [stories/stories.md:84](C:\Users\jeffa\.cdd\runtime\cdd_guidance\practices\stories\stories.md#L84)

**Candidates for the judge to read:** 14

- [?] **CANDIDATE** **[graph rule]** - [.context/story-map.md](C:\dev\mm3e-online-holistic\.context\story-map.md#L17): Story `Perform Routine Check`: Story 'Perform Routine Check' opens with a generic verb; judge from its context whether it hides the system mechanic (e.g. 'Submit Order').
- [?] **CANDIDATE** **[graph rule]** - [.context/story-map.md](C:\dev\mm3e-online-holistic\.context\story-map.md#L120): Story `Perform Acrobatic Maneuver`: Story 'Perform Acrobatic Maneuver' opens with a generic verb; judge from its context whether it hides the system mechanic (e.g. 'Submit Order').
- [?] **CANDIDATE** **[graph rule]** - [.context/story-map.md](C:\dev\mm3e-online-holistic\.context\story-map.md#L136): Story `Perform Legerdemain with Sleight of Hand`: Story 'Perform Legerdemain with Sleight of Hand' opens with a generic verb; judge from its context whether it hides the system mechanic (e.g. 'Submit Order').
- [?] **CANDIDATE** **[graph rule]** - [.context/story-map.md](C:\dev\mm3e-online-holistic\.context\story-map.md#L143): Story `Perform Jury-Rig Repair`: Story 'Perform Jury-Rig Repair' opens with a generic verb; judge from its context whether it hides the system mechanic (e.g. 'Submit Order').
- [?] **CANDIDATE** **[graph rule]** - [.context/story-map.md](C:\dev\mm3e-online-holistic\.context\story-map.md#L172): Story `Execute Attack Trade-Off Maneuver (accurate, all-out, defensive, power)`: Story 'Execute Attack Trade-Off Maneuver (accurate, all-out, defensive, power)' opens with a generic verb; judge from its context whether it hides the system mechanic (e.g. 'Submit Order').
- [?] **CANDIDATE** **[graph rule]** - [.context/story-map.md](C:\dev\mm3e-online-holistic\.context\story-map.md#L423): Story `Perform Magical Ritual`: Story 'Perform Magical Ritual' opens with a generic verb; judge from its context whether it hides the system mechanic (e.g. 'Submit Order').
- [?] **CANDIDATE** **[graph rule]** - [.context/story-map.md](C:\dev\mm3e-online-holistic\.context\story-map.md#L475): Story `Execute Last Order When No New Command Given`: Story 'Execute Last Order When No New Command Given' opens with a generic verb; judge from its context whether it hides the system mechanic (e.g. 'Submit Order').
- [?] **CANDIDATE** **[graph rule]** - [.context/story-map.md](C:\dev\mm3e-online-holistic\.context\story-map.md#L508): Story `Execute Charge Attack with Penalty`: Story 'Execute Charge Attack with Penalty' opens with a generic verb; judge from its context whether it hides the system mechanic (e.g. 'Submit Order').
- [?] **CANDIDATE** **[graph rule]** - [.context/story-map.md](C:\dev\mm3e-online-holistic\.context\story-map.md#L509): Story `Execute Slam Attack During Charge`: Story 'Execute Slam Attack During Charge' opens with a generic verb; judge from its context whether it hides the system mechanic (e.g. 'Submit Order').
- [?] **CANDIDATE** **[graph rule]** - [.context/story-map.md](C:\dev\mm3e-online-holistic\.context\story-map.md#L513): Story `Execute Grab Attempt`: Story 'Execute Grab Attempt' opens with a generic verb; judge from its context whether it hides the system mechanic (e.g. 'Submit Order').
- [?] **CANDIDATE** **[graph rule]** - [.context/story-map.md](C:\dev\mm3e-online-holistic\.context\story-map.md#L519): Story `Execute Disarm Attempt`: Story 'Execute Disarm Attempt' opens with a generic verb; judge from its context whether it hides the system mechanic (e.g. 'Submit Order').
- [?] **CANDIDATE** **[graph rule]** - [.context/story-map.md](C:\dev\mm3e-online-holistic\.context\story-map.md#L522): Story `Execute Trip Attempt`: Story 'Execute Trip Attempt' opens with a generic verb; judge from its context whether it hides the system mechanic (e.g. 'Submit Order').
- [?] **CANDIDATE** **[graph rule]** - [.context/story-map.md](C:\dev\mm3e-online-holistic\.context\story-map.md#L525): Story `Execute Feint with Deception Check`: Story 'Execute Feint with Deception Check' opens with a generic verb; judge from its context whether it hides the system mechanic (e.g. 'Submit Order').
- [?] **CANDIDATE** **[graph rule]** - [.context/story-map.md](C:\dev\mm3e-online-holistic\.context\story-map.md#L541): Story `Execute Team Attack with Coordinated Attackers`: Story 'Execute Team Attack with Coordinated Attackers' opens with a generic verb; judge from its context whether it hides the system mechanic (e.g. 'Submit Order').

### `verb-noun-format`

Rule text: [stories/stories.md:83](C:\Users\jeffa\.cdd\runtime\cdd_guidance\practices\stories\stories.md#L83)

**Graph violations:** 3

- [X] **ERROR** **[graph rule]** - [.context/story-map.md](C:\dev\mm3e-online-holistic\.context\story-map.md#L65): SubEpic `Advance Hero`: SubEpic 'Advance Hero': name should start with a verb (got nominalisation).
- [X] **ERROR** **[graph rule]** - [.context/story-map.md](C:\dev\mm3e-online-holistic\.context\story-map.md#L119): Story `Balance on Precarious Surface`: Story 'Balance on Precarious Surface': name should start with a verb (got nominalisation).
- [X] **ERROR** **[graph rule]** - [.context/story-map.md](C:\dev\mm3e-online-holistic\.context\story-map.md#L530): Story `Transition Incapacitated Target to Dying`: Story 'Transition Incapacitated Target to Dying': name should start with a verb (got nominalisation).
