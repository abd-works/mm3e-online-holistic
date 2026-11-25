# Graph rule validation

**Generated:** 2026-11-25 18:55:48 UTC
**Project:** mm3e-online-holistic
**Action:** validate (graph JSON + AI rules)

**Graph sources:**
- `C:\dev\mm3e-online-holistic\.sessions\main\.context\checked-graphs\stories-story-map-20261125T185547\graph.json`

**The session's graph also held, and practice-wide rules compared against:**
- `story_tests/resolve-checks`

## Summary

**Total graph violations:** 3
**Rules with graph hits:** 1
**Candidates for the judge to read:** 23. A rule that requires a judge listed each; none is a violation until the judge reads it and fails it.
**AI rules in scope:** 12

## Rules

Each rule names where its text is kept, then any graph scanner hits (`**[graph rule]**`). The judgment is appended after the rules, in the shape the Validate action gives (`cdd_guidance/actions/validate/validate.md`, step 6). A hit marked `**CANDIDATE**` comes from a rule that requires a judge: its check only lists places to read, so read each and fail the rule only where the reading finds it broken.

### `vocabulary-traces-to-domain-source`

Rule text: [stories/stories.md:24](C:\Users\jeffa\.cdd\runtime\cdd_guidance\practices\stories\stories.md#L24)

### `read-all-source-context-in-full`

Rule text: [stories/stories.md:25](C:\Users\jeffa\.cdd\runtime\cdd_guidance\practices\stories\stories.md#L25)

### `do-not-invent-requirements`

Rule text: [stories/stories.md:26](C:\Users\jeffa\.cdd\runtime\cdd_guidance\practices\stories\stories.md#L26)

### `verb-noun-format`

Rule text: [stories/stories.md:83](C:\Users\jeffa\.cdd\runtime\cdd_guidance\practices\stories\stories.md#L83)

**Graph violations:** 3

- [X] **ERROR** **[graph rule]** - [.context/story-map.md](C:\dev\mm3e-online-holistic\.context\story-map.md#L63): SubEpic `Advance Hero`: SubEpic 'Advance Hero': name should start with a verb (got nominalisation).
- [X] **ERROR** **[graph rule]** - [.context/story-map.md](C:\dev\mm3e-online-holistic\.context\story-map.md#L108): SubEpic `Influence Target with Intimidation`: SubEpic 'Influence Target with Intimidation': name should start with a verb (got nominalisation).
- [X] **ERROR** **[graph rule]** - [.context/story-map.md](C:\dev\mm3e-online-holistic\.context\story-map.md#L112): SubEpic `Influence Target with Persuasion`: SubEpic 'Influence Target with Persuasion': name should start with a verb (got nominalisation).

### `story-name-captures-system-mechanic`

Rule text: [stories/stories.md:84](C:\Users\jeffa\.cdd\runtime\cdd_guidance\practices\stories\stories.md#L84)

**Candidates for the judge to read:** 14

- [?] **CANDIDATE** **[graph rule]** - [.context/story-map.md](C:\dev\mm3e-online-holistic\.context\story-map.md#L17): Story `Perform Routine Check`: Story 'Perform Routine Check' opens with a generic verb; judge from its context whether it hides the system mechanic (e.g. 'Submit Order').
- [?] **CANDIDATE** **[graph rule]** - [.context/story-map.md](C:\dev\mm3e-online-holistic\.context\story-map.md#L123): Story `Perform Acrobatic Maneuver`: Story 'Perform Acrobatic Maneuver' opens with a generic verb; judge from its context whether it hides the system mechanic (e.g. 'Submit Order').
- [?] **CANDIDATE** **[graph rule]** - [.context/story-map.md](C:\dev\mm3e-online-holistic\.context\story-map.md#L143): Story `Perform Legerdemain with Sleight of Hand`: Story 'Perform Legerdemain with Sleight of Hand' opens with a generic verb; judge from its context whether it hides the system mechanic (e.g. 'Submit Order').
- [?] **CANDIDATE** **[graph rule]** - [.context/story-map.md](C:\dev\mm3e-online-holistic\.context\story-map.md#L151): Story `Perform Jury-Rig Repair`: Story 'Perform Jury-Rig Repair' opens with a generic verb; judge from its context whether it hides the system mechanic (e.g. 'Submit Order').
- [?] **CANDIDATE** **[graph rule]** - [.context/story-map.md](C:\dev\mm3e-online-holistic\.context\story-map.md#L183): Story `Execute Attack Trade-Off Maneuver (accurate, all-out, defensive, power)`: Story 'Execute Attack Trade-Off Maneuver (accurate, all-out, defensive, power)' opens with a generic verb; judge from its context whether it hides the system mechanic (e.g. 'Submit Order').
- [?] **CANDIDATE** **[graph rule]** - [.context/story-map.md](C:\dev\mm3e-online-holistic\.context\story-map.md#L450): Story `Perform Magical Ritual`: Story 'Perform Magical Ritual' opens with a generic verb; judge from its context whether it hides the system mechanic (e.g. 'Submit Order').
- [?] **CANDIDATE** **[graph rule]** - [.context/story-map.md](C:\dev\mm3e-online-holistic\.context\story-map.md#L503): Story `Execute Last Order When No New Command Given`: Story 'Execute Last Order When No New Command Given' opens with a generic verb; judge from its context whether it hides the system mechanic (e.g. 'Submit Order').
- [?] **CANDIDATE** **[graph rule]** - [.context/story-map.md](C:\dev\mm3e-online-holistic\.context\story-map.md#L536): Story `Execute Charge Attack with Penalty`: Story 'Execute Charge Attack with Penalty' opens with a generic verb; judge from its context whether it hides the system mechanic (e.g. 'Submit Order').
- [?] **CANDIDATE** **[graph rule]** - [.context/story-map.md](C:\dev\mm3e-online-holistic\.context\story-map.md#L537): Story `Execute Slam Attack During Charge`: Story 'Execute Slam Attack During Charge' opens with a generic verb; judge from its context whether it hides the system mechanic (e.g. 'Submit Order').
- [?] **CANDIDATE** **[graph rule]** - [.context/story-map.md](C:\dev\mm3e-online-holistic\.context\story-map.md#L541): Story `Execute Feint with Deception Check`: Story 'Execute Feint with Deception Check' opens with a generic verb; judge from its context whether it hides the system mechanic (e.g. 'Submit Order').
- [?] **CANDIDATE** **[graph rule]** - [.context/story-map.md](C:\dev\mm3e-online-holistic\.context\story-map.md#L543): Story `Execute Grab Attempt`: Story 'Execute Grab Attempt' opens with a generic verb; judge from its context whether it hides the system mechanic (e.g. 'Submit Order').
- [?] **CANDIDATE** **[graph rule]** - [.context/story-map.md](C:\dev\mm3e-online-holistic\.context\story-map.md#L550): Story `Execute Disarm Attempt`: Story 'Execute Disarm Attempt' opens with a generic verb; judge from its context whether it hides the system mechanic (e.g. 'Submit Order').
- [?] **CANDIDATE** **[graph rule]** - [.context/story-map.md](C:\dev\mm3e-online-holistic\.context\story-map.md#L554): Story `Execute Trip Attempt`: Story 'Execute Trip Attempt' opens with a generic verb; judge from its context whether it hides the system mechanic (e.g. 'Submit Order').
- [?] **CANDIDATE** **[graph rule]** - [.context/story-map.md](C:\dev\mm3e-online-holistic\.context\story-map.md#L572): Story `Execute Team Attack with Coordinated Attackers`: Story 'Execute Team Attack with Coordinated Attackers' opens with a generic verb; judge from its context whether it hides the system mechanic (e.g. 'Submit Order').

### `child-count-fits-layer`

Rule text: [stories/stories.md:85](C:\Users\jeffa\.cdd\runtime\cdd_guidance\practices\stories\stories.md#L85)

### `story-scenarios-at-most-seven`

Rule text: [stories/stories.md:86](C:\Users\jeffa\.cdd\runtime\cdd_guidance\practices\stories\stories.md#L86)

### `branch-on-mechanical-uniqueness`

Rule text: [stories/stories.md:87](C:\Users\jeffa\.cdd\runtime\cdd_guidance\practices\stories\stories.md#L87)

**Candidates for the judge to read:** 9

- [?] **CANDIDATE** **[graph rule]** - [.context/story-map.md](C:\dev\mm3e-online-holistic\.context\story-map.md#L135): SubEpic `Use Combat Skills`: Stories under 'Use Combat Skills' share the same verb 'add'; split by distinct mechanics or merge.
- [?] **CANDIDATE** **[graph rule]** - [.context/story-map.md](C:\dev\mm3e-online-holistic\.context\story-map.md#L185): SubEpic `Apply Passive Combat Bonus`: Stories under 'Apply Passive Combat Bonus' share the same verb 'apply'; split by distinct mechanics or merge.
- [?] **CANDIDATE** **[graph rule]** - [.context/story-map.md](C:\dev\mm3e-online-holistic\.context\story-map.md#L228): SubEpic `Select Attack Effect`: Stories under 'Select Attack Effect' share the same verb 'select'; split by distinct mechanics or merge.
- [?] **CANDIDATE** **[graph rule]** - [.context/story-map.md](C:\dev\mm3e-online-holistic\.context\story-map.md#L253): SubEpic `Select Mobility Effect`: Stories under 'Select Mobility Effect' share the same verb 'select'; split by distinct mechanics or merge.
- [?] **CANDIDATE** **[graph rule]** - [.context/story-map.md](C:\dev\mm3e-online-holistic\.context\story-map.md#L267): SubEpic `Select Sensory Effect`: Stories under 'Select Sensory Effect' share the same verb 'select'; split by distinct mechanics or merge.
- [?] **CANDIDATE** **[graph rule]** - [.context/story-map.md](C:\dev\mm3e-online-holistic\.context\story-map.md#L281): SubEpic `Select Control Effect`: Stories under 'Select Control Effect' share the same verb 'select'; split by distinct mechanics or merge.
- [?] **CANDIDATE** **[graph rule]** - [.context/story-map.md](C:\dev\mm3e-online-holistic\.context\story-map.md#L299): SubEpic `Select General Effect`: Stories under 'Select General Effect' share the same verb 'select'; split by distinct mechanics or merge.
- [?] **CANDIDATE** **[graph rule]** - [.context/story-map.md](C:\dev\mm3e-online-holistic\.context\story-map.md#L331): SubEpic `Choose Flat Modifiers`: Stories under 'Choose Flat Modifiers' share the same verb 'apply'; split by distinct mechanics or merge.
- [?] **CANDIDATE** **[graph rule]** - [.context/story-map.md](C:\dev\mm3e-online-holistic\.context\story-map.md#L477): SubEpic `Add Headquarters Features`: Stories under 'Add Headquarters Features' share the same verb 'add'; split by distinct mechanics or merge.

### `right-size-story-nodes`

Rule text: [stories/stories.md:88](C:\Users\jeffa\.cdd\runtime\cdd_guidance\practices\stories\stories.md#L88)

### `behaviours-not-build-tasks`

Rule text: [stories/stories.md:89](C:\Users\jeffa\.cdd\runtime\cdd_guidance\practices\stories\stories.md#L89)

### `kebab-case-paths`

Rule text: [stories/stories.md:90](C:\Users\jeffa\.cdd\runtime\cdd_guidance\practices\stories\stories.md#L90)

### `story-map-links-to-markdown`

Rule text: [stories/stories.md:91](C:\Users\jeffa\.cdd\runtime\cdd_guidance\practices\stories\stories.md#L91)
