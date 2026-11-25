# Graph rule validation

**Generated:** 2026-11-25 19:14:23 UTC
**Project:** mm3e-online-holistic
**Action:** validate (graph JSON + AI rules)

**Graph sources:**
- `C:\dev\mm3e-online-holistic\.sessions\main\.context\checked-graphs\stories-scenarios-20261125T191401\graph.json`

## Summary

**No graph rule violations.** All scanned graph rules passed.
**Candidates for the judge to read:** 27. A rule that requires a judge listed each; none is a violation until the judge reads it and fails it.
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

**Candidates for the judge to read:** 5

- [?] **CANDIDATE** **[graph rule]** - [story_tests/conduct-combat/perform-combat-maneuvers/grab-target/damage-grabbed-target-on-subsequent-turn/damage_grabbed_target_on_subsequent_turn_story.test.md](C:\dev\mm3e-online-holistic\story_tests\conduct-combat\perform-combat-maneuvers\grab-target\damage-grabbed-target-on-subsequent-turn\damage_grabbed_target_on_subsequent_turn_story.test.md#L43): Given `but *Villain* escaped before *Hero*'s turn`: But step should mark missing or absent state, not a consequence: "*Villain* escaped before *Hero*'s turn".
- [?] **CANDIDATE** **[graph rule]** - [story_tests/conduct-combat/use-hero-resources/spend-hero-point-for-heroic-feat-advantage/spend_hero_point_for_heroic_feat_advantage_story.test.md](C:\dev\mm3e-online-holistic\story_tests\conduct-combat\use-hero-resources\spend-hero-point-for-heroic-feat-advantage\spend_hero_point_for_heroic_feat_advantage_story.test.md#L43): Given `but *Hero* lacks the ++prerequisite++ for Improved Critical`: But step should mark missing or absent state, not a consequence: '*Hero* lacks the ++prerequisite++ for Improved Critical'.
- [?] **CANDIDATE** **[graph rule]** - [story_tests/conduct-combat/use-hero-resources/spend-hero-point-to-remove-extra-effort-fatigue/spend_hero_point_to_remove_extra_effort_fatigue_story.test.md](C:\dev\mm3e-online-holistic\story_tests\conduct-combat\use-hero-resources\spend-hero-point-to-remove-extra-effort-fatigue\spend_hero_point_to_remove_extra_effort_fatigue_story.test.md#L40): Given `but *Hero* has *0* ++hero point++`: But step should mark missing or absent state, not a consequence: '*Hero* has *0* ++hero point++'.
- [?] **CANDIDATE** **[graph rule]** - [story_tests/select-advantages/activate-fortune-advantage/apply-inspiration-bonus-ignoring-power-level-cap/apply_inspiration_bonus_ignoring_power_level_cap_story.test.md](C:\dev\mm3e-online-holistic\story_tests\select-advantages\activate-fortune-advantage\apply-inspiration-bonus-ignoring-power-level-cap\apply_inspiration_bonus_ignoring_power_level_cap_story.test.md#L44): Given `but the character has only a move action left this turn`: But step should mark missing or absent state, not a consequence: 'the character has only a move action left this turn'.
- [?] **CANDIDATE** **[graph rule]** - [story_tests/select-advantages/manage-character-resources/manage-sidekick/spend-hero-point-on-sidekick-s-behalf/spend_hero_point_on_sidekick_s_behalf_story.test.md](C:\dev\mm3e-online-holistic\story_tests\select-advantages\manage-character-resources\manage-sidekick\spend-hero-point-on-sidekick-s-behalf\spend_hero_point_on_sidekick_s_behalf_story.test.md#L38): Given `but the owner has *0* ++hero points++`: But step should mark missing or absent state, not a consequence: 'the owner has *0* ++hero points++'.

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

**Candidates for the judge to read:** 9

- [?] **CANDIDATE** **[graph rule]** - [.context/story-map.md](C:\dev\mm3e-online-holistic\.context\story-map.md#L136): SubEpic `Use Combat Skills`: Stories under 'Use Combat Skills' share the same verb 'add'; split by distinct mechanics or merge.
- [?] **CANDIDATE** **[graph rule]** - [.context/story-map.md](C:\dev\mm3e-online-holistic\.context\story-map.md#L186): SubEpic `Apply Passive Combat Bonus`: Stories under 'Apply Passive Combat Bonus' share the same verb 'apply'; split by distinct mechanics or merge.
- [?] **CANDIDATE** **[graph rule]** - [.context/story-map.md](C:\dev\mm3e-online-holistic\.context\story-map.md#L228): SubEpic `Select Attack Effect`: Stories under 'Select Attack Effect' share the same verb 'select'; split by distinct mechanics or merge.
- [?] **CANDIDATE** **[graph rule]** - [.context/story-map.md](C:\dev\mm3e-online-holistic\.context\story-map.md#L253): SubEpic `Select Mobility Effect`: Stories under 'Select Mobility Effect' share the same verb 'select'; split by distinct mechanics or merge.
- [?] **CANDIDATE** **[graph rule]** - [.context/story-map.md](C:\dev\mm3e-online-holistic\.context\story-map.md#L267): SubEpic `Select Sensory Effect`: Stories under 'Select Sensory Effect' share the same verb 'select'; split by distinct mechanics or merge.
- [?] **CANDIDATE** **[graph rule]** - [.context/story-map.md](C:\dev\mm3e-online-holistic\.context\story-map.md#L281): SubEpic `Select Control Effect`: Stories under 'Select Control Effect' share the same verb 'select'; split by distinct mechanics or merge.
- [?] **CANDIDATE** **[graph rule]** - [.context/story-map.md](C:\dev\mm3e-online-holistic\.context\story-map.md#L299): SubEpic `Select General Effect`: Stories under 'Select General Effect' share the same verb 'select'; split by distinct mechanics or merge.
- [?] **CANDIDATE** **[graph rule]** - [.context/story-map.md](C:\dev\mm3e-online-holistic\.context\story-map.md#L332): SubEpic `Choose Flat Modifiers`: Stories under 'Choose Flat Modifiers' share the same verb 'apply'; split by distinct mechanics or merge.
- [?] **CANDIDATE** **[graph rule]** - [.context/story-map.md](C:\dev\mm3e-online-holistic\.context\story-map.md#L480): SubEpic `Add Headquarters Features`: Stories under 'Add Headquarters Features' share the same verb 'add'; split by distinct mechanics or merge.

### `story-name-captures-system-mechanic`

Rule text: [stories/stories.md:84](C:\Users\jeffa\.cdd\runtime\cdd_guidance\practices\stories\stories.md#L84)

**Candidates for the judge to read:** 13

- [?] **CANDIDATE** **[graph rule]** - [.context/story-map.md](C:\dev\mm3e-online-holistic\.context\story-map.md#L17): Story `Perform Routine Check`: Story 'Perform Routine Check' opens with a generic verb; judge from its context whether it hides the system mechanic (e.g. 'Submit Order').
- [?] **CANDIDATE** **[graph rule]** - [.context/story-map.md](C:\dev\mm3e-online-holistic\.context\story-map.md#L124): Story `Perform Acrobatic Maneuver`: Story 'Perform Acrobatic Maneuver' opens with a generic verb; judge from its context whether it hides the system mechanic (e.g. 'Submit Order').
- [?] **CANDIDATE** **[graph rule]** - [.context/story-map.md](C:\dev\mm3e-online-holistic\.context\story-map.md#L144): Story `Perform Legerdemain with Sleight of Hand`: Story 'Perform Legerdemain with Sleight of Hand' opens with a generic verb; judge from its context whether it hides the system mechanic (e.g. 'Submit Order').
- [?] **CANDIDATE** **[graph rule]** - [.context/story-map.md](C:\dev\mm3e-online-holistic\.context\story-map.md#L152): Story `Perform Jury-Rig Repair`: Story 'Perform Jury-Rig Repair' opens with a generic verb; judge from its context whether it hides the system mechanic (e.g. 'Submit Order').
- [?] **CANDIDATE** **[graph rule]** - [.context/story-map.md](C:\dev\mm3e-online-holistic\.context\story-map.md#L453): Story `Perform Magical Ritual`: Story 'Perform Magical Ritual' opens with a generic verb; judge from its context whether it hides the system mechanic (e.g. 'Submit Order').
- [?] **CANDIDATE** **[graph rule]** - [.context/story-map.md](C:\dev\mm3e-online-holistic\.context\story-map.md#L506): Story `Execute Last Order When No New Command Given`: Story 'Execute Last Order When No New Command Given' opens with a generic verb; judge from its context whether it hides the system mechanic (e.g. 'Submit Order').
- [?] **CANDIDATE** **[graph rule]** - [.context/story-map.md](C:\dev\mm3e-online-holistic\.context\story-map.md#L539): Story `Execute Charge Attack with Penalty`: Story 'Execute Charge Attack with Penalty' opens with a generic verb; judge from its context whether it hides the system mechanic (e.g. 'Submit Order').
- [?] **CANDIDATE** **[graph rule]** - [.context/story-map.md](C:\dev\mm3e-online-holistic\.context\story-map.md#L540): Story `Execute Slam Attack During Charge`: Story 'Execute Slam Attack During Charge' opens with a generic verb; judge from its context whether it hides the system mechanic (e.g. 'Submit Order').
- [?] **CANDIDATE** **[graph rule]** - [.context/story-map.md](C:\dev\mm3e-online-holistic\.context\story-map.md#L544): Story `Execute Feint with Deception Check`: Story 'Execute Feint with Deception Check' opens with a generic verb; judge from its context whether it hides the system mechanic (e.g. 'Submit Order').
- [?] **CANDIDATE** **[graph rule]** - [.context/story-map.md](C:\dev\mm3e-online-holistic\.context\story-map.md#L546): Story `Execute Grab Attempt`: Story 'Execute Grab Attempt' opens with a generic verb; judge from its context whether it hides the system mechanic (e.g. 'Submit Order').
- [?] **CANDIDATE** **[graph rule]** - [.context/story-map.md](C:\dev\mm3e-online-holistic\.context\story-map.md#L553): Story `Execute Disarm Attempt`: Story 'Execute Disarm Attempt' opens with a generic verb; judge from its context whether it hides the system mechanic (e.g. 'Submit Order').
- [?] **CANDIDATE** **[graph rule]** - [.context/story-map.md](C:\dev\mm3e-online-holistic\.context\story-map.md#L557): Story `Execute Trip Attempt`: Story 'Execute Trip Attempt' opens with a generic verb; judge from its context whether it hides the system mechanic (e.g. 'Submit Order').
- [?] **CANDIDATE** **[graph rule]** - [.context/story-map.md](C:\dev\mm3e-online-holistic\.context\story-map.md#L575): Story `Execute Team Attack with Coordinated Attackers`: Story 'Execute Team Attack with Coordinated Attackers' opens with a generic verb; judge from its context whether it hides the system mechanic (e.g. 'Submit Order').

## Judgment — `story_tests`

No rule fails on the graph. The judged candidates were read:

- `but-marks-missing-state` — Pass. The five remaining candidates each mark state that is absent (*Villain* already escaped the grab, *Hero* lacks the Improved Critical prerequisite, *0* hero points twice, only a move action left), which is what *But* is for. 77 earlier candidates that used *But* for a consequence ("X stays 5") were changed to *And* before this run.
- `branch-on-mechanical-uniqueness` — see the story-map judgment (`stories-story-map-20261125T185547.md`): Use Combat Skills and Add Headquarters Features are recorded there as Fail; the Select … Effect, Apply Passive Combat Bonus and Choose Flat Modifiers groups hold distinct mechanics.
- `story-name-captures-system-mechanic` — Pass: each Perform/Execute story names its game mechanic in the noun.

Scope of the AI-judged rules: the scenario files were written by nine agents from the module acceptance criteria and the cited rules chunks, each with a scripted check of headings, story type, scenario count (≤ 7), step formatting and outline placeholders. This judgment spot-read files in every epic, not all 426. Where acceptance criteria and the rules text disagreed, the scenarios follow the rules text, and values no source gives carry a `> Evidence missing:` line (`flagged-writes-intended-gwt`).
