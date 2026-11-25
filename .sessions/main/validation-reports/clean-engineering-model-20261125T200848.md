# Graph rule validation

**Generated:** 2026-11-25 20:08:49 UTC
**Project:** mm3e-online-holistic
**Action:** validate (graph JSON + AI rules)

**Graph sources:**
- `C:\dev\mm3e-online-holistic\.sessions\main\.context\checked-graphs\clean-engineering-model-20261125T200848\graph.json`

**The session's graph also held, and practice-wide rules compared against:**
- `.context`
- `story_tests/resolve-checks`

## Summary

**No graph rule ran on:** `combat/.context/combat-model.md`. The graph read no node from them, so only the AI rules judge them.
**AI rules in scope:** 35

## Rules

Each rule names where its text is kept, then any graph scanner hits (`**[graph rule]**`). The judgment is appended after the rules, in the shape the Validate action gives (`cdd_guidance/actions/validate/validate.md`, step 6). A hit marked `**CANDIDATE**` comes from a rule that requires a judge: its check only lists places to read, so read each and fail the rule only where the reading finds it broken.

### `vocabulary-traces-to-source`

Rule text: [clean_engineering/clean_engineering.md:18](C:\Users\jeffa\.cdd\runtime\cdd_guidance\practices\clean_engineering\clean_engineering.md#L18)

### `do-not-invent-terms`

Rule text: [clean_engineering/clean_engineering.md:19](C:\Users\jeffa\.cdd\runtime\cdd_guidance\practices\clean_engineering\clean_engineering.md#L19)

### `do-not-invent-parallel-object-models`

Rule text: [clean_engineering/clean_engineering.md:20](C:\Users\jeffa\.cdd\runtime\cdd_guidance\practices\clean_engineering\clean_engineering.md#L20)

### `model-modules-follow-the-partition`

Rule text: [clean_engineering/clean_engineering.md:236](C:\Users\jeffa\.cdd\runtime\cdd_guidance\practices\clean_engineering\clean_engineering.md#L236)

### `class-not-property-instance-or-subtype`

Rule text: [clean_engineering/clean_engineering.md:237](C:\Users\jeffa\.cdd\runtime\cdd_guidance\practices\clean_engineering\clean_engineering.md#L237)

### `keep-classes-single-responsibility`

Rule text: [clean_engineering/clean_engineering.md:238](C:\Users\jeffa\.cdd\runtime\cdd_guidance\practices\clean_engineering\clean_engineering.md#L238)

### `shape-classes-around-resources`

Rule text: [clean_engineering/clean_engineering.md:239](C:\Users\jeffa\.cdd\runtime\cdd_guidance\practices\clean_engineering\clean_engineering.md#L239)

### `put-logic-on-the-owning-resource`

Rule text: [clean_engineering/clean_engineering.md:240](C:\Users\jeffa\.cdd\runtime\cdd_guidance\practices\clean_engineering\clean_engineering.md#L240)

### `hide-inner-details`

Rule text: [clean_engineering/clean_engineering.md:241](C:\Users\jeffa\.cdd\runtime\cdd_guidance\practices\clean_engineering\clean_engineering.md#L241)

### `use-property-not-accessor`

Rule text: [clean_engineering/clean_engineering.md:242](C:\Users\jeffa\.cdd\runtime\cdd_guidance\practices\clean_engineering\clean_engineering.md#L242)

### `prefer-class-operations`

Rule text: [clean_engineering/clean_engineering.md:243](C:\Users\jeffa\.cdd\runtime\cdd_guidance\practices\clean_engineering\clean_engineering.md#L243)

### `use-explicit-dependencies`

Rule text: [clean_engineering/clean_engineering.md:244](C:\Users\jeffa\.cdd\runtime\cdd_guidance\practices\clean_engineering\clean_engineering.md#L244)

### `external-system-interface-is-one-way`

Rule text: [clean_engineering/clean_engineering.md:245](C:\Users\jeffa\.cdd\runtime\cdd_guidance\practices\clean_engineering\clean_engineering.md#L245)

### `keep-operations-single-responsibility`

Rule text: [clean_engineering/clean_engineering.md:249](C:\Users\jeffa\.cdd\runtime\cdd_guidance\practices\clean_engineering\clean_engineering.md#L249)

### `limit-operation-parameters`

Rule text: [clean_engineering/clean_engineering.md:250](C:\Users\jeffa\.cdd\runtime\cdd_guidance\practices\clean_engineering\clean_engineering.md#L250)

### `hold-state-on-the-object-not-in-parameters`

Rule text: [clean_engineering/clean_engineering.md:251](C:\Users\jeffa\.cdd\runtime\cdd_guidance\practices\clean_engineering\clean_engineering.md#L251)

### `avoid-vague-parameter-names`

Rule text: [clean_engineering/clean_engineering.md:252](C:\Users\jeffa\.cdd\runtime\cdd_guidance\practices\clean_engineering\clean_engineering.md#L252)

### `errors-out-of-existence`

Rule text: [clean_engineering/clean_engineering.md:253](C:\Users\jeffa\.cdd\runtime\cdd_guidance\practices\clean_engineering\clean_engineering.md#L253)

### `refuse-unreadable-input`

Rule text: [clean_engineering/clean_engineering.md:254](C:\Users\jeffa\.cdd\runtime\cdd_guidance\practices\clean_engineering\clean_engineering.md#L254)

### `state-change-returns-record-or-named-failure`

Rule text: [clean_engineering/clean_engineering.md:255](C:\Users\jeffa\.cdd\runtime\cdd_guidance\practices\clean_engineering\clean_engineering.md#L255)

### `domain-exception-carries-context`

Rule text: [clean_engineering/clean_engineering.md:256](C:\Users\jeffa\.cdd\runtime\cdd_guidance\practices\clean_engineering\clean_engineering.md#L256)

### `limit-comments`

Rule text: [clean_engineering/clean_engineering.md:257](C:\Users\jeffa\.cdd\runtime\cdd_guidance\practices\clean_engineering\clean_engineering.md#L257)

### `write-invariants`

Rule text: [clean_engineering/clean_engineering.md:261](C:\Users\jeffa\.cdd\runtime\cdd_guidance\practices\clean_engineering\clean_engineering.md#L261)

### `write-interactions`

Rule text: [clean_engineering/clean_engineering.md:262](C:\Users\jeffa\.cdd\runtime\cdd_guidance\practices\clean_engineering\clean_engineering.md#L262)

### `no-redundant-relationship-paths`

Rule text: [clean_engineering/clean_engineering.md:263](C:\Users\jeffa\.cdd\runtime\cdd_guidance\practices\clean_engineering\clean_engineering.md#L263)

### `use-intention-revealing-names`

Rule text: [clean_engineering/clean_engineering.md:267](C:\Users\jeffa\.cdd\runtime\cdd_guidance\practices\clean_engineering\clean_engineering.md#L267)

### `use-consistent-naming`

Rule text: [clean_engineering/clean_engineering.md:268](C:\Users\jeffa\.cdd\runtime\cdd_guidance\practices\clean_engineering\clean_engineering.md#L268)

### `eliminate-duplication`

Rule text: [clean_engineering/clean_engineering.md:269](C:\Users\jeffa\.cdd\runtime\cdd_guidance\practices\clean_engineering\clean_engineering.md#L269)

### `one-canonical-model-document`

Rule text: [clean_engineering/clean_engineering.md:270](C:\Users\jeffa\.cdd\runtime\cdd_guidance\practices\clean_engineering\clean_engineering.md#L270)

### `delete-unused-classes`

Rule text: [clean_engineering/clean_engineering.md:275](C:\Users\jeffa\.cdd\runtime\cdd_guidance\practices\clean_engineering\clean_engineering.md#L275)

### `delete-unused-operations`

Rule text: [clean_engineering/clean_engineering.md:276](C:\Users\jeffa\.cdd\runtime\cdd_guidance\practices\clean_engineering\clean_engineering.md#L276)

### `check-use-the-graph-cannot-see`

Rule text: [clean_engineering/clean_engineering.md:277](C:\Users\jeffa\.cdd\runtime\cdd_guidance\practices\clean_engineering\clean_engineering.md#L277)

### `make-module-only-operations-private`

Rule text: [clean_engineering/clean_engineering.md:278](C:\Users\jeffa\.cdd\runtime\cdd_guidance\practices\clean_engineering\clean_engineering.md#L278)

### `connect-disconnected-classes`

Rule text: [clean_engineering/clean_engineering.md:279](C:\Users\jeffa\.cdd\runtime\cdd_guidance\practices\clean_engineering\clean_engineering.md#L279)

### `merge-one-class-packages`

Rule text: [clean_engineering/clean_engineering.md:280](C:\Users\jeffa\.cdd\runtime\cdd_guidance\practices\clean_engineering\clean_engineering.md#L280)
