
## GROUP: Ability Score

### ability
- One of eight fundamental numeric traits that characterize a hero's physical or mental capabilities.
- Partitioned into physical abilities (STR, STA, AGL, DEX) and mental abilities (FGT, INT, AWE, PRE).
- Each above-average ability rank provides a bonus on related die rolls; below-average rank applies a penalty.
- The ability rank is added to (or subtracted from) die rolls for tasks related to that ability and to calculate derived values.
- Ability ranks can be bought up using power points, reduced below 0 for bonus power points, or altered by power effects during play.
- Some ability ranks — or portions of them — can be designated as Enhanced Traits (powers), which behave differently from natural ranks.
- Stores a signed integer rank that modifies related die rolls as a direct numeric bonus or penalty.
- Determines which skills and derived defense values it feeds into based on which of the eight named types it is.
- Changes value when the player spends power points (at creation or advancement) or when a power effect alters it.
- Propagates the rank change to all dependent traits in the same operation — skills update, defenses update, attack modifiers update.
- **Invariant:** rank can never drop below −5 through voluntary player adjustment; values below −5 indicate a debilitated state triggered only by external game effects.
- **Invariant:** if a rank changes, all dependent traits must update to reflect the new value in the same operation.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_035.md`

### ability rank
- Numeric value expressing the degree of an ability; starts at 0 (the baseline average for an adult human).
- Can go as low as −5 (truly terrible) and as high as 20 or beyond for cosmic beings and forces.
- Costs 2 power points per +1 rank when purchased; yields 2 bonus power points per −1 rank when reduced.
- Cannot be voluntarily lowered below −5; dropping below −5 due to an external effect triggers the debilitated state.
- Used directly as a modifier on die rolls and as the base for calculating derived defense values.
- Represents the current signed integer value of a specific ability, serving as both a direct modifier and a base for derived calculations.
- Tracks whether a rank is normal, enhanced, or a combination — each portion with distinct properties under the rules.
- Resolves the cost/refund formula when the player adjusts it: positive delta costs 2 pp per +1, negative delta refunds 2 pp per −1.
- **Invariant:** rank must remain in the range [−5, ∞) after voluntary player adjustments; the floor is enforced at purchase time.
- **Invariant:** the enhanced portion of a rank is tracked separately from the base portion so it can be selectively nullified without affecting the natural portion.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_035.md`

### Strength (STR)
- Measures sheer muscle power and the ability to apply physical force.
- Applies to: unarmed and strength-based attack damage; jump distance (Athletics check); weight lifting, carrying, and throwing; Athletics skill checks.
- Physical ability.
- Contributes its rank directly as damage bonus on unarmed and strength-based attacks.
- Feeds into jump-distance calculation as part of Athletics checks and into all Athletics skill checks for physical tasks.
- **Invariant:** when STR is debilitated, the hero collapses (defenseless, immobilized, stunned) — STR no longer contributes meaningful attack damage or Athletics bonuses while in the collapsed state.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_036.md`

### Stamina (STA)
- Measures health, endurance, and overall physical resilience.
- Applies to: Toughness defense (resisting damage); Fortitude defense (resisting effects on health); Stamina checks for health-related resistance and recovery when no specific defense applies.
- Physical ability.
- Contributes its rank as the base value for both Toughness and Fortitude defenses simultaneously — two derivations from one source.
- Provides the resistance modifier for any health-based check when a specific defense is not named.
- **Invariant:** when STA is debilitated, the hero enters the dying state with a −5 Fortitude penalty stacked on top of any existing penalties.
- **Invariant:** a creature with no Stamina has no Fortitude defense; the derivation has no source.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_036.md`

### Agility (AGL)
- Measures balance, grace, speed, and overall physical coordination.
- Applies to: Dodge defense (avoiding ranged attacks and hazards); initiative bonus (acting first in combat); Acrobatics and Stealth skill checks; Agility checks for coordination feats.
- Physical ability.
- Contributes its rank as the base value for Dodge defense and as the base component of the initiative modifier.
- Feeds into Acrobatics and Stealth skill checks as the primary modifier.
- **Invariant:** when AGL is debilitated, the hero collapses (defenseless, immobilized, stunned) — Dodge defense and initiative modifier both become non-functional.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_036.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_039.md`

### Dexterity (DEX)
- Measures hand-eye coordination, precision, and manual dexterity.
- Applies to: ranged attack checks; Sleight of Hand and Vehicles skill checks; Dexterity checks for fine control and precision tasks.
- Physical ability.
- Contributes its rank as the modifier for all ranged attack checks.
- Feeds into Sleight of Hand and Vehicles skill checks as the primary modifier.
- **Invariant:** when DEX is debilitated, the hero collapses (defenseless, immobilized, stunned) — ranged attack checks become impossible.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_036.md`

### Fighting (FGT)
- Measures close combat ability — hitting targets and evading counter-attacks in melee.
- Applies to: close attack checks; Parry defense (avoiding close attacks).
- Mental ability (grouped with INT, AWE, PRE as a mental ability in the core rules).
- Contributes its rank as the modifier for all close attack checks.
- Contributes its rank as the base value for Parry defense.
- **Invariant:** when FGT is debilitated, the hero is dazed and defenseless and cannot make close attacks.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_036.md`

### Intellect (INT)
- Covers reasoning ability and learning; a high rank correlates with knowledge and education.
- Applies to: Expertise, Investigation, Technology, and Treatment skill checks; Intellect checks for pure reasoning when no specific skill applies.
- Mental ability.
- Contributes its rank as the modifier for Expertise, Investigation, Technology, and Treatment skill checks.
- Provides the general reasoning modifier when no specific skill applies to a problem.
- **Invariant:** when INT is debilitated, the hero is unaware and remains so until the ability rank is restored to at least −5.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_036.md`

### Awareness (AWE)
- Covers common sense and intuition ("wisdom"), distinct from Intellect (reasoning).
- Applies to: Will defense (resisting mental attacks); Insight and Perception skill checks; Awareness checks for intuition when no specific skill applies.
- Mental ability.
- A creature with no Awareness is also treated as having no Presence; awareness and presence absence are linked.
- Contributes its rank as the base value for Will defense.
- Contributes its rank as the modifier for Insight and Perception skill checks.
- **Invariant:** when AWE is debilitated, the hero is unaware and remains so until the rank is restored to at least −5.
- **Invariant:** if AWE is absent, Presence is automatically absent too — the two abilities share an absence linkage defined in Ch3.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_036.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_038.md`

### Presence (PRE)
- Measures force of personality, persuasiveness, leadership ability, and attractiveness.
- Applies to: Deception, Intimidation, and Persuasion skill checks; Presence checks to influence others through force of personality.
- Mental ability.
- Contributes its rank as the modifier for Deception, Intimidation, and Persuasion skill checks.
- Provides the general force-of-personality modifier when no specific interaction skill applies.
- **Invariant:** when PRE is debilitated, the hero is unaware and remains so until the rank is restored to at least −5.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_036.md`

### enhanced ability
- An ability rank (or portion thereof) acquired as an Enhanced Trait (power) rather than as a natural rank.
- Can be nullified by the Nullify effect — normal (natural) ability ranks cannot be nullified.
- Can have power modifiers and be used for power stunts with extra effort — normal ranks cannot.
- Same cost as normal ability ranks: 2 power points per +1 rank.
- The player decides whether a rank is normal, enhanced, or a combination; both apply as modifier simultaneously.
- Tracks a subset of the total ability rank that is designated as power-based rather than natural.
- Contributes its rank to the total modifier in the same way as the natural portion (the sum applies to all die rolls and derivations).
- Can be temporarily removed by the Nullify effect, reducing the total ability modifier by the enhanced portion during nullification.
- Can receive power modifiers (extras and flaws) that alter its behavior, cost, or power stunt eligibility.
- **Invariant:** nullifying the enhanced portion does not affect the natural portion — each tracks its own rank independently.
- **Invariant:** the total ability modifier is always the sum of natural + enhanced rank; the two portions are additive.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_037.md`

## GROUP: Absent Ability

### absent ability
- A creature entirely lacking an ability has no rank for it, a state distinct from having rank −5.
- Automatically fails any check requiring the absent ability.
- Lacking an ability grants an additional 10 power points to spend elsewhere — more generous than the −5 floor.
- Heroes cannot lack an ability without Gamemaster permission, as absence has significant game effects.
- An absent ability cannot be weakened or debilitated — it simply is not present.
- Per-ability absence effects:
  - No Strength: incapable of exerting any physical force (incorporeal or immobile creature).
  - No Stamina: no physical body; suffers and recovers from damage as an inanimate object; immune to fatigue; no Fortitude defense.
  - No Dexterity: cannot manipulate objects; cannot make physical attacks.
  - No Agility: unable to move under own power; no Dodge defense.
  - No Fighting: incapable of any close attack.
  - No Intellect: automaton; immune to mental effects and interaction skills; no Will defense.
  - No Awareness: completely unaware; also has no Presence; immune to mental effects and interaction skills; treated as inanimate object.
  - No Presence: unable to interact; immune to interaction skills; no Will defense.
- Represents the complete non-existence of an ability — no rank to apply, no modifier to add, no defense to derive.
- Applies per-ability capability restrictions as permanent characteristics of the creature.
- Grants −10 power points at character-creation time as compensation, recorded at creation, not recalculated at runtime.
- Enforces automatic failure on all checks that would use the absent ability's modifier.
- **Invariant:** an absent ability cannot be weakened by the Weaken effect (no rank to weaken) or debilitated (no rank to drop below −5).
- **Invariant:** a hero character cannot have an absent ability without explicit GM authorization.
- **Invariant:** when Awareness is absent, Presence is automatically absent — the two are linked and cannot be independently absent.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_038.md`

## GROUP: Derived Defense

### Dodge
- Defense value based on Agility rank; covers reaction time, quickness, nimbleness, and coordination.
- Used to avoid ranged attacks and other hazards where reflexes and speed are important.
- Active defense: requires mobility and focus; halved (round up) when vulnerable; reduced to 0 when defenseless.
- Used as defense class (Dodge + 10) against ranged attacks.
- Used in Dodge resistance checks (e.g., reflexively avoid a triggered trap).
- Can be increased above the Agility base by spending 1 power point per rank, subject to power level limits.
- Derives its base value from the character's Agility rank at creation and recalculates whenever AGL changes.
- Acts as the primary defense against ranged attacks by supplying the Dodge defense class (Dodge + 10).
- Participates in Dodge resistance checks (defense + d20 vs effect DC) when the check is triggered.
- Degrades under condition effects: halved when vulnerable, zeroed when defenseless.
- Can be increased above the AGL base through power point investment, up to the power level cap.
- **Invariant:** Dodge cannot be negative; if AGL is absent, there is no Dodge defense.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_039.md`

### Parry
- Defense value based on Fighting rank; represents countering, ducking, or evading close attacks.
- Active defense: halved (round up) when vulnerable; reduced to 0 when defenseless.
- Used as defense class (Parry + 10) for close attacks.
- Can be increased above the Fighting base by spending 1 power point per rank, subject to power level limits.
- Derives its base value from the character's Fighting rank and recalculates whenever FGT changes.
- Acts as the primary defense against close attacks by supplying the Parry defense class (Parry + 10).
- Degrades under condition effects: halved when vulnerable, zeroed when defenseless (same degradation rule as Dodge).
- Can be increased above the FGT base through power point investment, up to the power level cap.
- **Invariant:** Parry cannot be negative; the minimum after any degradation is 0.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_039.md`

### Fortitude
- Defense value based on Stamina rank; measures health and resistance to threats like poison or disease.
- Incorporates constitution, ruggedness, metabolism, and immunity.
- Passive defense: always effective regardless of mobility restrictions.
- Used in Fortitude resistance checks against health-affecting effects (toxins, disease, dying).
- Can be increased above the Stamina base by spending 1 power point per rank.
- Creatures with no Stamina have no Fortitude defense.
- Derives its base value from the character's Stamina rank.
- Participates in resistance checks against health-affecting effects; used for the dying stabilization check (DC 15 per round).
- Passive defense: does not degrade under vulnerable or defenseless conditions.
- Can be increased above the STA base through power point investment.
- **Invariant:** creatures with no Stamina have no Fortitude defense — the derivation has no source.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_039.md`

### Toughness
- Defense value based on Stamina rank; measures resistance to direct damage and overall physical durability.
- Cannot be increased above the base Stamina rank by direct power point spending — only through advantages (e.g., Defensive Roll) and powers (e.g., Protection effect).
- This restriction reflects that greater-than-normal Toughness is virtually always a special ability.
- Used in Toughness resistance checks against damage.
- Derives its base value from the character's Stamina rank.
- Participates in resistance checks against damage — every attack that deals damage triggers a Toughness resistance check.
- Passive defense: does not degrade under vulnerable or defenseless conditions.
- **Invariant:** Toughness cannot be raised above the base Stamina rank through direct power point spending; only advantages and powers can exceed this base.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_039.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_040.md`

### Will
- Defense value based on Awareness rank; measures mental stability, level-headedness, determination, self-confidence, and willpower.
- Used to resist mental or spiritual attacks.
- Used as defense class (Will + 10) when an attack targets Will.
- Can be increased above the Awareness base by spending 1 power point per rank.
- Creatures with no Intellect or no Awareness/Presence have no Will defense.
- Derives its base value from the character's Awareness rank.
- Acts as both defense class (Will + 10) for mental attacks and resistance check base for effects that target mental stability.
- Passive defense: does not degrade under vulnerable or defenseless conditions.
- Can be increased above the AWE base through power point investment.
- **Invariant:** creatures with no Intellect or no Awareness/Presence have no Will defense.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_039.md`

### defense
- General term for the five defensive values (Dodge, Parry, Fortitude, Toughness, Will) used to resist or avoid effects.
- Each defense is based on a specific ability rank, modified by advantages and powers.
- Base defense rank equals the rank of the associated ability.
- Can be increased above base by spending 1 power point per rank, subject to power level limits (except Toughness).
- Serves two purposes: (1) defense class (defense + 10 = DC to affect a target with an attack); (2) resistance check (defense + d20 vs effect's DC).
- Active defenses (Dodge, Parry) require mobility and focus to be fully effective; passive defenses (Fortitude, Toughness, Will) are unaffected by mobility.
- Owns the base derivation rule: each defense's starting rank equals the associated ability rank, updated automatically when the ability changes.
- Applies the investment economy: player may spend 1 pp per +1 defense rank above base (except Toughness).
- Enforces the two-role contract for all five defenses: defense class for attack targeting (defense + 10 = DC) AND resistance check base (defense + d20 vs effect DC).
- Separates active (Dodge, Parry) from passive (Fortitude, Toughness, Will) for condition-effect interactions.
- **Invariant:** base defense rank always reflects the current ability rank; it updates in the same operation as the ability rank change.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_039.md`

### active defense
- Category of defense that requires mobility, focus, and reaction time to be fully effective.
- Comprises Dodge and Parry — the two ability-derived defenses that degrade under condition effects.
- When vulnerable: active defense ranks are halved (divide normal value by 2, round up).
- When defenseless: active defense ranks are reduced to 0.
- Contrasts with passive defenses (Fortitude, Toughness, Will), which are unaffected by mobility restrictions.
- Classifies Dodge and Parry as the defenses requiring ongoing engagement to be fully effective.
- Applies the halving rule (round up) to both Dodge and Parry simultaneously when the character is vulnerable.
- Applies the zeroing rule to both simultaneously when the character is defenseless.
- **Invariant:** active defense rank can never fall below 0 regardless of condition effects.
---

### defense class
- The difficulty class for a given attack to affect a target: defense rank + 10.
- Represents the target's "routine defense" (equivalent to a routine check).
- Primary defense class traits: Dodge (for ranged attacks), Parry (for close attacks), and Will (for mental attacks).
- An attack "targets" a defense when it uses that defense's class as its DC.
- Computes the attack's DC by adding 10 to the appropriate defense rank.
- Applied to Dodge (ranged attacks), Parry (close attacks), and Will (mental attacks) as the primary targeting defenses.
- Changes whenever the underlying defense rank changes — it is always current with the current ability rank.
- **Invariant:** defense class is always defense rank + 10; there are no other modifiers to the base formula at this level.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_040.md`

### initiative
- Derived combat-readiness value computed as: Agility rank + Advantages (Improved Initiative) + Power Modifiers.
- Determines action order at the start of a conflict: characters act from highest to lowest initiative modifier.
- Defined in Ch3 Abilities alongside the five defenses, grounding it in the ability module.
- Depends on the Agility ability rank for its base value; the Advantage and Power components are boundary contributions.
- Computes as the sum of AGL rank plus any Improved Initiative advantage bonus plus any power modifier.
- Updates automatically whenever the AGL rank changes, since AGL is the only ability-module-owned component.
- **Invariant:** if AGL is absent, the Agility component is 0; the initiative modifier equals only Advantage and Power contributions.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_040.md`

## GROUP: Debilitated Ability

### debilitated
- State reached when an ability rank drops below −5 for any reason (typically caused by a power effect).
- Ability ranks cannot be lowered any further once debilitated; this threshold is the floor for each ability.
- Per-ability debilitation effects:
  - STR, AGL, or DEX debilitated: hero collapses — defenseless, immobilized, and stunned (but still conscious and aware).
  - STA debilitated: hero is dying, with an additional −5 modifier on Fortitude checks to avoid death.
  - FGT debilitated: hero is dazed and defenseless; cannot make close attacks.
  - INT, AWE, or PRE debilitated: hero is unaware and remains so until the ability is restored to at least −5.
- Triggers when an ability rank is reduced below −5 by a game effect, applying the appropriate per-ability condition set immediately.
- Enforces the floor: blocks any further rank reduction once the debilitated threshold is reached for that ability.
- Tracks recovery: when the ability rank rises back to −5 or above (typically when the effect causing the reduction ends), the debilitated state clears and conditions are removed.
- **Invariant:** ability ranks cannot go lower than the debilitated threshold; the floor is absolute and cannot be overridden.
- **Invariant:** the specific conditions applied depend on which ability is debilitated — they are not interchangeable across the four groups.
- **Invariant:** recovery from debilitation requires the rank to reach at least −5; a rank of −6 or lower maintains the debilitated state.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_037.md`
