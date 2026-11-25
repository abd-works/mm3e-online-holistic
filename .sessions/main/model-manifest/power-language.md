## Language

*Effect Framework* — The Effect Framework is the foundational architecture of every superhuman capability in the game. An **effect** is the atomic rules-defined unit: it names a capability, specifies its type (Attack, Control, Defense, General, Movement, Sensory), and ships with default action, range, duration, and cost per rank. A **power** is the player-facing wrapper a character acquires — one or more effects combined, named, and described using **descriptors** that determine what Nullify counters, what Immunity blocks, and how the fictional world reacts. **Power type** is the category label on every effect that tells the system which general rules apply. Together these three concepts answer the most important design question: what does this capability do and how is it categorized?

### effect

- An effect is the named, rules-defined game unit that produces a specific superheroic capability — the atomic building block from which all powers are constructed.
- Every effect has five fixed properties at acquisition: type, action, range, duration, and cost per rank.
- Effects are acquired in ranks; higher rank means greater scale, distance, or intensity.
- The effect's stat block defaults can be changed by applying extras and flaws.
- Players name their powers freely; the effect is the underlying mechanical structure the rules operate on.
- is the *atomic rules-defined unit* of superhuman capability — the named, typed, mechanically complete building block
- carries five fixed properties: type, action, range, duration, and cost per rank — all set at acquisition
- is acquired in ranks; higher rank means greater scale, intensity, reach, or effect magnitude
- exposes its default stat block to the modifier system; extras and flaws alter those defaults
- **Invariant:** every effect has exactly one type, one action, one range, one duration, and one cost per rank at any point in time
- Collaborates with: Modifier (extras/flaws change its properties and cost), Effect Cost (calculates its price), Power (groups one or more effects into a named capability)
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_082.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_083.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_084.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_087.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_088.md`

### power

- A power is the player-facing, named combination of one or more effects that appears on a character sheet.
- Powers cost power points equal to the sum of each included effect's (cost per rank × rank) plus any flat modifiers.
- Powers must have at least one descriptor; descriptors are assigned at acquisition.
- The GM approves all powers before play; powers interact with settings, plots, and genre conventions.
- is the *player-facing named capability* that appears on a character sheet — the fiction label wrapping one or more effects
- acquires one or more effects, each paying its own cost; total power cost = sum of all effect costs
- carries at least one descriptor; the descriptor is not optional
- is approved by the GM before play; the GM may veto or modify powers for series appropriateness
- **Invariant:** every power must contain at least one effect and at least one descriptor
- Collaborates with: effect (its mechanical content), descriptor (its thematic identity), power point (its economic cost in Character Construction)
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_082.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_083.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_155.md`

### power type

- Power type is the category label assigned to each effect: Attack, Control, Defense, General, Movement, Sensory.
- Attack type effects require an attack check and allow targets a resistance check.
- Defense type effects are passive or reactive; most are permanent.
- Control type effects manipulate the environment, objects, or characters.
- General type effects provide utility, enhancement, or transformation.
- Movement type effects grant locomotion modes.
- Sensory type effects grant, enhance, or alter perception capabilities.
- is the *category label* on every effect that governs which general rules apply
- classifies each effect into exactly one of six categories: Attack, Control, Defense, General, Movement, Sensory
- determines whether an effect requires an attack check, allows a resistance check, is activated as free action, or is permanent
- **Invariant:** every effect belongs to exactly one power type; a power type cannot be changed by modifiers
- Collaborates with: effect (carries the type label), modifier (extras can sometimes change apparent type behavior but not the official type)
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_084.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_087.md`

### descriptor

- A descriptor is a free label attached to a power that identifies its nature, medium, source, or results in thematic and mechanical terms.
- Descriptors cost no power points; they are assigned at acquisition and may not be changed without GM approval.
- Descriptors determine what Nullify counters, what Immunity blocks, and how narrative effects interact with the power.
- At minimum every power must have at least one descriptor.
- is a free *thematic label* on a power that connects it to the game fiction and mechanical interaction systems
- costs no power points — it is purely a label attached at acquisition
- governs what Nullify can counter and what Immunity can block
- supports GM rulings on descriptor interactions in play
- **Invariant:** every power must have at least one descriptor; descriptors may not be changed without GM approval
- Collaborates with: Nullify (uses descriptor to target), Immunity (uses descriptor to define coverage), GM (final arbitrator of descriptor interactions)
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_155.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_156.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_157.md`

### origin descriptor

- An origin descriptor identifies how a character came to have their powers — the narrative source of the character's abilities.
- Common origin descriptors: Accidental, Bestowed, Invented, Mutant, Training.
- Origin descriptors rarely have direct mechanical effects but govern narrative interactions.
- is a *descriptor subtype* that identifies how the character came to have their powers
- covers origin categories: Accidental, Bestowed, Invented, Mutant, Training
- typically applies to the character's entire power set rather than individual powers
- **Invariant:** origin descriptor rarely has direct mechanical effects; it is primarily a narrative and GM-ruling tool
- Collaborates with: descriptor (its parent concept), power set (the scope it typically covers)
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_155.md`

### source descriptor

- A source descriptor identifies the energy or force that a power draws upon to function.
- Common source descriptors: Biological, Cosmic, Divine, Extradimensional, Magical, Moral, Psionic, Technological.
- Source descriptors have mechanical significance: Nullify targeting "magical effects" counters all powers with a Magical source.
- is a *descriptor subtype* that identifies the energy or force a power draws upon to function
- covers source categories: Biological, Cosmic, Divine, Extradimensional, Magical, Moral, Psionic, Technological
- has direct mechanical significance — Nullify targeting 'magical effects' counters all powers with Magical source
- a power can have multiple source descriptors if it draws on more than one source
- **Invariant:** source descriptor determines Nullify and Immunity interactions more directly than origin descriptor
- Collaborates with: descriptor (its parent concept), Nullify (primary mechanical consumer), Immunity (secondary consumer)
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_155.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_156.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_157.md`

*Effect Cost* — The Effect Cost abstraction owns the pricing model that converts a raw effect into power points spent on the character sheet. **Base cost** is the printed starting value per rank for each specific effect — it represents the inherent worth of the capability at rank 1. **Cost per rank** is the modified rate after extras raise it and flaws lower it, and it is the key figure used in the multiplication: cost per rank × rank = the bulk of the power's price. **Flat modifier** is the final adjustment applied to the total (not the per-rank figure), used for extras and flaws that have fixed-point values rather than rank-scaled ones.

### base cost

- Base cost is the unmodified power-point cost per rank for an effect as printed in the rules.
- Base costs vary: 1 pp/rank for simple effects (Damage), up to 7 pp/rank for versatile effects (Variable).
- Modifier math starts from base cost: extras add to it, flaws subtract from it.
- is the *unmodified power-point cost per rank* as printed in the rules for a specific effect
- is immutable — set at effect design time and cannot be changed by play or by modifiers
- seeds the modifier math: cost per rank = base cost + extras − flaws
- **Invariant:** base cost is always a positive integer ≥ 1 for every defined effect
- Collaborates with: effect (carries its base cost), modifier (adjusts from this baseline), cost per rank (derived value)
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_083.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_087.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_140.md`

### cost per rank

- Cost per rank = base cost + (sum of per-rank extras) − (sum of per-rank flaws).
- Must be at minimum 1 pp/rank regardless of flaws applied.
- Total effect cost = (cost per rank × ranks) + flat modifiers.
- is the *final modified cost per rank* paid for each rank of an effect after all modifier math is complete
- is computed as: base cost + (sum of per-rank extras) − (sum of per-rank flaws)
- drives the bulk of total power cost: effect cost = (cost per rank × ranks) + flat modifiers
- **Invariant:** cost per rank cannot drop below 1 pp/rank regardless of flaws applied
- Collaborates with: base cost (starting value), extra/flaw (modifiers applied), flat modifier (post-multiplication), rank (the multiplier)
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_083.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_140.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_141.md`

### flat modifier

- A flat modifier is applied to the final total cost of a power (after cost per rank × rank) — a fixed-point adjustment, not rank-scaled.
- Flat extras add points to the total; flat flaws subtract points.
- Flat modifiers apply after cost per rank is calculated; they can push total cost below the per-rank floor.
- is a *fixed-point price adjustment* applied to the final total cost after per-rank cost × rank is computed
- adds (flat extra) or subtracts (flat flaw) a set number of points from the total, regardless of rank
- is applied last in the cost formula: (cost per rank × rank) + flat extras − flat flaws
- **Invariant:** flat modifiers cannot reduce total power cost below 1 power point
- Collaborates with: extra (flat extras add to total), flaw (flat flaws subtract), cost per rank (applied after multiplication)
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_140.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_141.md`

*Modifier* — A Modifier is any rule element attached to an effect that changes how it works and adjusts its price. **Extras** make effects more capable — they can expand action type, extend range, increase duration, add properties, or improve the effect in other ways; each per-rank extra raises cost per rank, while each flat extra adds a fixed amount to the total. **Flaws** make effects less capable — they restrict applicability, reduce action type, narrow range, or impose conditions; per-rank flaws reduce cost per rank, flat flaws reduce the total. The specific modifiers — **Accurate**, **Area**, **Multiattack**, **Penetrating** (extras) and **Activation**, **Check Required**, **Limited**, **Removable** (flaws) — are the most commonly encountered and have their own rules sections.

### extra

- An extra enhances an effect beyond its default behavior — broadens action type, extends range, adds properties.
- Per-rank extras add their value (usually +1) to base cost to raise cost per rank.
- Flat extras add a fixed point amount to the final total cost.
- Any effect can receive any extra as long as the effect doesn't already have that property.
- is a *modifier that enhances an effect* — it broadens, extends, or improves the effect beyond its defaults
- is either per-rank (adds to cost per rank) or flat (adds to the final total cost)
- must grant a genuine improvement; cosmetic changes are descriptors, not extras
- **Invariant:** an effect cannot receive an extra for a property it already has (e.g., cannot apply Ranged extra to an already-Ranged effect)
- Collaborates with: effect (is applied to an effect), base cost (raises it to produce cost per rank), flat modifier (for flat-value extras)
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_140.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_141.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_142.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_144.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_145.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_146.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_147.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_148.md`

### flaw

- A flaw limits an effect below its default behavior — restricts action type, reduces range, narrows applicability, or imposes conditions.
- Per-rank flaws subtract their value (usually −1) from base cost to lower cost per rank.
- Cost per rank cannot drop below 1 pp/rank no matter how many flaws are applied.
- Flaws must represent genuine limitations — the effect must actually be restricted about half or more of the time.
- is a *modifier that limits an effect* — it restricts, narrows, or conditions the effect below its defaults
- is either per-rank (reduces cost per rank) or flat (reduces the final total cost)
- must represent a genuine limitation reducing utility by approximately half or more; cosmetic restrictions are descriptors
- **Invariant:** flaws cannot reduce cost per rank below 1 pp/rank; total cost cannot drop below 1 pp
- Collaborates with: effect (is applied to an effect), base cost (reduces it to produce cost per rank), flat modifier (for flat-value flaws)
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_140.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_141.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_149.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_150.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_151.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_152.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_153.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_154.md`

### Accurate

- Accurate is a flat extra; cost 1 flat point per +2 attack bonus (1 point per rank of bonus).
- Improves attack check rolls with that specific effect only.
- The attack bonus from Accurate cannot push total attack bonus beyond PL × 2.
- is a *flat extra* that adds +2 per rank to attack checks made with the specific effect
- costs 1 flat point per rank of accuracy bonus (i.e., 1 pp for +2, 2 pp for +4, etc.)
- applies only to the specific effect it is purchased for
- **Invariant:** the attack bonus from Accurate cannot push total attack bonus beyond PL × 2
- Collaborates with: attack check (the thing improved), PL limits (the cap), flat modifier (the cost mechanism)
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_087.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_141.md`

### Area

- Area is a per-rank extra; cost +1 per rank.
- Removes the need for an attack check; targets in the area make a Dodge resistance check (DC 10 + effect rank).
- Area shapes: Burst, Cloud, Cone, Cylinder, Line, Perception, Shapeable.
- Success on the Dodge check reduces effect rank by half.
- is a *per-rank extra* that removes the attack check requirement and instead affects all targets in a defined area
- allows targets a Dodge resistance check (DC 10 + effect rank) to avoid the effect (success = half rank effect)
- offers shapes: Burst, Cloud, Cone, Cylinder, Line, Perception, Shapeable
- costs +1 per rank; each additional rank of Area increases the area dimensions
- **Invariant:** Area effects cannot exclude specific targets within the area without the Selective extra
- Collaborates with: Dodge (the resistance check), area shape (the dimension of coverage), effect rank (sets DC and area size), Selective extra (for target exclusion)
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_087.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_142.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_143.md`

### Multiattack

- Multiattack is a per-rank extra; cost +1 per rank.
- Against a single target: +2 to effect DC at 2 degrees of attack success, +5 at 3+ degrees.
- Against multiple targets: one attack roll with penalty equal to number of targets; each target whose Dodge is exceeded is hit.
- is a *per-rank extra* that allows an effect to hit multiple targets or strike a single target multiple times
- against a single target: +2 to effect DC at 2 degrees of attack success; +5 at 3+ degrees
- against multiple targets: one attack roll with penalty equal to number of targets; each target whose Dodge is exceeded is hit
- costs +1 per rank
- **Invariant:** Multiattack has two distinct modes (single-target boost vs. multi-target spray); the character chooses each time they use the effect
- Collaborates with: attack check (the roll used for both modes), Dodge (the defense of each target in spray mode), DC (increased in single-target mode)
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_146.md`

### Penetrating

- Penetrating is a flat extra; cost 1 flat point per rank of Penetrating.
- Overcomes Impervious resistance to degree equal to the Penetrating rank.
- Target with Impervious Toughness must resist damage rank equal to Penetrating rank even if normally blocked.
- is a *flat extra* that allows an effect to bypass Impervious resistance
- costs 1 flat point per rank of Penetrating; overcomes Impervious to degree equal to Penetrating rank
- forces targets with Impervious Toughness to resist damage rank equal to the Penetrating rank
- **Invariant:** Penetrating only bypasses Impervious; it does not increase the attack's DC or rank
- Collaborates with: Impervious extra (what it bypasses), Toughness (the resistance still applied), flat modifier (the cost mechanism)
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_141.md`

### Activation

- Activation is a flat flaw; cost −1 (move action activation) or −2 (standard action activation).
- Applies to the entire power — all effects require the activation first.
- If Nullified or deactivated, the character must spend the activation action again.
- is a *flat flaw* that requires the character to spend an action activating the power before any effects become available
- costs −1 (move action) or −2 (standard action) from the power's total cost
- applies to the entire power — all effects within the power require the activation
- requires reactivation after being Nullified or deactivated
- **Invariant:** Activation applies to the whole power, not individual effects within it
- Collaborates with: flat modifier (the cost mechanism), Nullify (the deactivation trigger), the entire power (all effects affected)
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_149.md`

### Check Required

- Check Required is a flat flaw; cost −1 per rank of the effect.
- Must succeed on a skill or ability check (DC 10 + extra ranks) before the effect activates.
- Natural 1 always fails; on success, gain 1 effective rank per point exceeding the DC.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_150.md`

### Limited

- Limited is a per-rank flaw; cost −1 per rank.
- Effect works only under certain circumstances, against certain targets, or in certain conditions.
- Limitation must reduce utility to approximately half or less; GM determines qualification.
- is a *per-rank flaw* that restricts an effect to function only under certain circumstances, against certain targets, or in certain conditions
- costs −1 per rank
- requires the limitation to genuinely reduce utility to approximately half or less; GM determines qualification
- is distinct from complications — complications trigger narrative events with hero point rewards; Limited reduces mechanical cost
- **Invariant:** Limited must be a genuine mechanical restriction, not a cosmetic or flavor restriction
- Collaborates with: per-rank flaw (the cost mechanism), GM approval (required to qualify), circumstance (the limiting condition)
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_140.md`

### Removable

- Removable is a flat flaw; cost −1 per 5 points of final power cost (or −2 if easily removable).
- Represents a power built into a device that can be taken from the character.
- The device can be taken when the character is both stunned and defenseless, or via disarm/grab.
- Removable applies to the entire power.
- is a *flat flaw* that represents a power built into an item that can be physically taken from the character
- costs −1 per 5 points of final power cost (or −2 if easily removable)
- allows the item to be taken when the character is both stunned and defenseless, or via a disarm/grab
- applies to the entire power — all effects are unavailable if the item is taken
- allows the item itself to be damaged using object damage rules; Toughness = character's PL
- **Invariant:** Removable applies to the whole power, not individual effects
- Collaborates with: flat modifier (the cost mechanism), stunned+defenseless conditions (the vulnerability window), item Toughness (= PL), object damage rules
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_153.md`

*Attack Effect* — An Attack Effect is any power effect whose primary purpose is to cause direct harm, impose conditions, or otherwise damage or disable an opponent through a direct confrontation requiring an attack check and allowing a resistance check. The Attack Effect KA groups together the six core effects that define offensive superhuman power: **Affliction** (condition imposition), **Blast** (ranged energy damage), **Damage** (melee harm), **Deflect** (defensive interception), **Nullify** (power suppression), and **Weaken** (trait reduction).

### Affliction

- Type Attack, action Standard, range Close, duration Instant, resistance Fortitude or Will (chosen at acquisition), cost 1 per rank.
- Three conditions chosen at acquisition for degrees 1, 2, and 3; each progressively worse.
- Target makes resistance check at end of each of their turns; success removes one degree.
- Third-degree recovery requires a full minute (or outside aid) after the Affliction is no longer active.
- is an *Attack effect* that imposes progressively worsening conditions on a target who fails a resistance check
- requires an attack check before the target makes a resistance check (Fortitude or Will — chosen at acquisition)
- applies conditions based on degree of failure: first degree applies condition 1, second adds condition 2, third adds condition 3
- allows the target to make a resistance check at end of each of their turns; success removes one degree (from worst)
- enforces special recovery for third degree: full minute (or outside aid) after the Affliction ends
- **Invariant:** exactly three conditions must be specified at acquisition, in degree order; each must be progressively worse
- Collaborates with: resistance check (Fort or Will), condition (the output applied), attack check (prerequisite)
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_087.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_089.md`

### Blast (Damage, Ranged)

- Blast is Damage with the Ranged extra applied; not a separate effect type.
- Stat block with Ranged: type Attack, action Standard, range Ranged, duration Instant, resistance Toughness, cost 2 per rank.
- Requires a ranged attack check vs. target's Dodge; on a hit, target makes Toughness check vs. DC 15 + effect rank.
- Base Damage (1 pp/rank) + Ranged extra (1 pp/rank) = 2 pp/rank for Blast.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_090.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_097.md`

### Damage

- Type Attack, action Standard, range Close, duration Instant, resistance Toughness, cost 1 per rank.
- DC of the Toughness check = 15 + Damage rank.
- Four degrees of failure: minor penalty → dazed and penalized → staggered and penalized → incapacitated (then dying → dead).
- Damage stacks with Strength for unarmed attacks.
- is the *foundational Attack effect* for direct physical harm at close range
- sets resistance check DC = 15 + effect rank against target's Toughness
- applies damage conditions in four degrees: minor penalty → dazed and penalized → staggered and penalized → incapacitated
- stacks with character's Strength for unarmed attacks
- **Invariant:** Damage has Close range by default; it requires the Ranged extra to become Blast
- Collaborates with: Toughness (the resistance), DC (15 + rank), Strength (stacks for unarmed), damage condition (the output)
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_097.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_098.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_099.md`

### Deflect

- Type Defense, action Standard (or Reaction with extra), range Ranged, duration Instant, cost 1 per rank.
- Uses Deflect rank as defense check instead of normal active defense; can protect other characters in range.
- Medium and long range penalties apply to Deflect attempts at distance.
- is a *Defense effect* that intercepts incoming ranged attacks for the user or nearby allies
- substitutes its rank (plus modifiers) for the normal active defense value of the protected target
- applies range penalties for medium and long range interceptions
- **Invariant:** Deflect intercepts attacks; it does not prevent the attack from being made — it substitutes the defense roll
- Collaborates with: active defense (Dodge/Parry — replaced by Deflect rank), range penalties (medium/long apply), attack check (what it is countering)
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_087.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_088.md`

### Nullify

- Type Attack, action Standard, range Ranged, duration Instant, cost 1 per rank.
- Ranged attack check required; on hit, opposed check of target's effect rank (or Will) vs. Nullify rank.
- Success counters (turns off) the targeted effect; target can re-activate on their next action.
- Targets effects by descriptor; Broad or Simultaneous extras can affect multiple effects.
- is an *Attack effect* that suppresses other power effects matching a chosen descriptor
- requires a ranged attack check, then an opposed check: Nullify rank vs. target effect rank (or Will, whichever is higher)
- on success, the targeted effect is countered (turned off); the target can reactivate on their next action
- targets effects by descriptor; Broad and Simultaneous extras expand targeting scope
- **Invariant:** Nullify suppresses; it does not destroy or permanently remove effects
- Collaborates with: descriptor (the targeting criterion), ranged attack check, opposed check, Will (alternate resistance), sustained vs permanent effects (reactivation rules differ)
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_125.md`

### Weaken

- Type Attack, action Standard, range Close, duration Instant, resistance Fortitude or Will, cost 1 per rank.
- On failed resistance check: target's specified trait reduced by degree of failure, up to Weaken rank.
- Weaken is cumulative — multiple applications stack up to the effect rank maximum.
- Targets recover at 1 point of the reduced trait per round.
- is an *Attack effect* that temporarily reduces a specific trait of the target
- applies reduction equal to degree of failure on the resistance check, up to the Weaken rank maximum
- is cumulative — multiple Weaken applications on the same trait stack up to the rank maximum
- allows targets to recover at 1 point of the reduced trait per round (automatic, no action)
- **Invariant:** Weaken is cumulative to rank maximum; beyond rank maximum, additional Weaken has no further effect
- Collaborates with: resistance check (Fort or Will), degree of failure (determines reduction amount), target trait (chosen at acquisition), recovery (1 per round automatic)
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_139.md`

*Defense Effect* — A Defense Effect is any power effect whose primary purpose is to protect the character from harm, prevent death, or provide ongoing resistance. The four Defense Effects in this module — **Immortality**, **Immunity**, **Protection**, and **Regeneration** — each address a different aspect of survivability: Prevention (Protection raises the Toughness bar before harm arrives), Nullification (Immunity makes specific threats automatically irrelevant), Recovery (Regeneration heals damage after it is taken), and Resurrection (Immortality reverses death itself).

### Immortality

- Type Defense, action None, range Personal, duration Permanent, cost 2 per rank.
- Recovery time after death = time rank (19 − Immortality rank); at rank 20, recover each action round.
- Does not prevent death — only enables return afterward.
- is a *Defense effect* that allows the character to return from death after a time period determined by rank
- calculates recovery time as time rank (19 − Immortality rank); at rank 20, recovers each action round
- does not prevent death — it only enables post-death return
- is permanent and always active; cannot be turned off
- **Invariant:** Immortality only triggers after death; it has no effect before death occurs
- Collaborates with: death (the trigger), time rank (the recovery schedule), permanent duration
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_111.md`

### Immunity

- Type Defense, action None, range Personal, duration Permanent, cost 1 per rank.
- Rank cost scales by scope: narrow immunity = 1 rank; Life Support = 10 ranks; all Fortitude effects = 30 ranks.
- Provides complete protection against the specified effect set with no check required.
- Partial immunity (half effect) costs half the full rank.
- is a *Defense effect* that grants automatic success on resistance checks against a specified effect set
- scales cost by scope: 1 rank for narrow immunity, up to 80 ranks for all Toughness effects
- provides complete protection against the covered set with no check required
- offers partial immunity (half effect) for half the full rank cost
- is permanent and always active; cannot be deactivated
- **Invariant:** Immunity works against the specified descriptor/effect set only; it has no effect outside that set
- Collaborates with: descriptor (the matching criterion), resistance check (bypassed), partial immunity (the half-cost variant)
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_112.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_113.md`

### Protection

- Type Defense, action None, range Personal, duration Permanent, cost 1 per rank.
- +1 Toughness per rank; stacks with Stamina-derived Toughness.
- Permanent and always active; cannot be deactivated and cannot benefit from extra effort.
- is a *Defense effect* that adds directly to the character's Toughness defense
- provides +1 Toughness per rank; stacks with Stamina-derived Toughness and Impervious
- is permanent and always active — cannot be deactivated and cannot benefit from extra effort
- **Invariant:** Protection is always on; there is no version that can be turned off without a flaw
- Collaborates with: Toughness (the defense it enhances), Stamina (stacks with), Impervious extra (can be combined with)
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_126.md`

### Regeneration

- Type Defense, action None, range Personal, duration Permanent, cost 1 per rank.
- Recovery phases: Toughness penalties removed at rank × minutes rate, then damage conditions at rank × minutes rate.
- Permanent and always active; cannot be deactivated.
- is a *Defense effect* that progressively removes damage conditions over time
- recovers in two phases: first removes Toughness penalties at rank per minute, then removes damage conditions at rank per minute from most severe
- is permanent and always active — cannot be deactivated
- **Invariant:** Regeneration cannot affect conditions that have not occurred naturally — it only repairs existing damage
- Collaborates with: damage conditions (the target of recovery), Toughness penalty (the first-phase target), permanent duration
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_127.md`

*Mobility Effect* — A Mobility Effect is any power effect that grants, enhances, or alters a character's locomotion — how they move through the world. The seven Mobility Effects cover the complete space of extraordinary movement: **Burrowing** (underground), **Flight** (air), **Leaping** (ballistic arcs), **Movement** (special modes), **Speed** (ground velocity), **Swimming** (water), and **Teleport** (instantaneous relocation). Each grants a distinct mode with distinct speed, mechanics, and environmental interactions.

### Burrowing

- Type Movement, action Free, range Personal, duration Sustained, cost 1 per rank.
- Speed through soil = Burrowing rank − 5; clay/packed earth −1, solid rock −2.
- Character chooses whether tunnel is permanent or collapses.
- is a *Movement effect* that grants the ability to move through earth, soil, clay, or rock
- calculates speed rank as Burrowing rank − 5; applies terrain penalties (clay −1, solid rock −2)
- lets the character choose on each use whether the tunnel is permanent or collapses behind them
- **Invariant:** Burrowing does not grant underwater breathing or any other survival capability
- Collaborates with: Movement (its type), speed rank (the output), terrain type (penalty input)
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_091.md`

### Flight

- Type Movement, action Free, range Personal, duration Sustained, cost 2 per rank.
- Flight speed rank = effect rank; hovering available by default.
- Activating is free action; moving requires a move action. Sustained — if unable to maintain, character falls.
- is a *Movement effect* that grants the ability to fly at a speed rank equal to the effect rank
- provides hovering capability by default — the character can remain stationary in midair
- activates as a free action; moving while airborne requires a move action as normal
- is sustained — the character falls if they cannot maintain it
- **Invariant:** Flight does not grant additional protection from the fall if the effect ends mid-air
- Collaborates with: speed rank (the output), sustained duration (the maintenance requirement), move action (required for actual movement)
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_106.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_107.md`

### Leaping

- Type Movement, action Free, range Personal, duration Instant, cost 1 per rank.
- Jump distance rank = Leaping rank − 2; no damage from landing within maximum distance.
- Cannot change direction mid-air; follows a ballistic arc.
- is a *Movement effect* that extends jumping distance to superhuman scales
- calculates jump distance rank = Leaping rank − 2 on the distance table
- prevents fall damage when landing within maximum jump distance
- follows a ballistic arc — the character cannot change direction mid-air
- **Invariant:** Leaping has Instant duration — it does not sustain; each jump is a discrete action
- Collaborates with: distance rank (the jump reach), Instant duration (discrete per-jump activation)
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_116.md`

### Movement

- Type Movement, action Free, range Personal, duration Sustained, cost 2 per rank.
- Each rank grants one special movement mode: Dimension Travel, Environmental Adaptation, Permeate, Safe Fall, Slithering, Space Travel, Sure-Footed, Swinging, Time Travel, Trackless, Wall-Crawling, Water-Walking.
- Each mode operates according to its own specific sub-rules.
- is a *Movement effect* that grants one special movement mode per rank from a defined list
- offers modes: Dimension Travel, Environmental Adaptation, Permeate, Safe Fall, Slithering, Space Travel, Sure-Footed, Swinging, Time Travel, Trackless, Wall-Crawling, Water-Walking
- activates as free action; requires a move action for actual movement (as all movement effects)
- is sustained; losing it ends the movement mode until reactivated
- **Invariant:** each rank grants exactly one mode; modes are independent — multiple modes require multiple ranks
- Collaborates with: movement mode (the specific capability acquired), sustained duration, GM (for Dimension/Time Travel interactions with setting)
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_087.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_123.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_124.md`

### Speed

- Type Movement, action Free, range Personal, duration Sustained, cost 1 per rank.
- Ground speed rank = effect rank; improves all ground-speed-based movement.
- Does not grant flight, swimming, or other non-ground movement.
- is a *Movement effect* that increases ground movement speed
- sets ground speed rank = effect rank; improves all speed-based ground movement actions
- does not grant flight, aquatic movement, or any non-ground mode
- **Invariant:** Speed only enhances ground movement; each other movement mode requires its own effect
- Collaborates with: speed rank (the output), ground movement (the only context it improves), move action (required for actual movement)
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_088.md`

### Swimming

- Type Movement, action Free, range Personal, duration Sustained, cost 1 per rank.
- Water speed rank = effect rank − 2; routine Athletics (Swimming) checks are automatic.
- Does not grant underwater breathing.
- is a *Movement effect* that grants enhanced aquatic movement speed
- sets water speed rank = effect rank − 2 on the speed table
- makes routine Athletics (Swimming) checks automatic — no roll required
- does not grant underwater breathing capability
- **Invariant:** Swimming does not prevent suffocation underwater; Immunity (Suffocation) must be purchased separately
- Collaborates with: speed rank (the aquatic output), Athletics (Swimming) check (made automatic), Immunity (for breathing)
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_136.md`

### Teleport

- Type Movement, action Move, range Rank range, duration Instant, cost 2 per rank.
- Destination must be well-known or accurately sensed; blind teleporting risks error.
- Character retains velocity from before the teleport; instant arrival, no transit time.
- is a *Movement effect* that provides instantaneous point-to-point relocation
- requires the destination to be either well-known or accurately sensed; unperceived destinations risk teleport error
- preserves the character's velocity from before the teleport (momentum is conserved)
- carries mass rank 0 additional mass by default (Mass extra extends this)
- **Invariant:** Teleport is Instant — there is no transit, no passage through intervening space
- Collaborates with: perception (for destination targeting), mass rank (for carrying capacity), Instant duration
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_088.md`

*Sensory Effect* — A Sensory Effect is any power effect that grants, enhances, or fools perception — the ability to collect information about the world or deny that ability to others. The six Sensory Effects cover information gathering (**Communication**, **Comprehend**, **Mind Reading**, **Remote Sensing**, **Senses**) and information denial (**Concealment**). These effects define the superhuman informational layer — who knows what, who can communicate with whom, and who can be perceived.

### Communication

- Type Sensory, action Free, range Rank range, duration Sustained, cost 4 per rank.
- Communicate over distance via a chosen sense type medium; language-dependent by default.
- Point-to-point communication to a known location or person.
- is a *Sensory effect* that sends and receives information over distance via a chosen sense type medium
- determines range by effect rank on the distance table; operates as point-to-point by default
- requires a shared language between sender and receiver; language-dependent unless modified
- **Invariant:** Communication requires a chosen sense type medium at acquisition; this cannot be changed without GM approval
- Collaborates with: sense type (the medium), range (determined by rank), language (a prerequisite for exchange)
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_092.md`

### Comprehend

- Type Sensory, action None, range Personal, duration Permanent, cost 2 per rank.
- Each rank = one communication type: Animals, Languages, Machines, Objects, Plants, Spirits.
- Always active — requires no action to use.
- is a *Sensory effect* that grants understanding of and ability to communicate with otherwise inaccessible beings or languages
- allocates each rank to exactly one communication type at acquisition: Animals, Languages, Machines, Objects, Plants, Spirits
- is permanent — always active, requires no action to invoke
- **Invariant:** each rank covers exactly one communication type; types do not stack within one rank
- Collaborates with: sense type (implicit), communication type (the chosen category per rank)
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_093.md`

### Concealment

- Type Sensory, action Free, range Personal, duration Sustained, cost 2 per rank.
- Grants total concealment from a specific sense type; Visual costs 2 ranks per visual sense.
- Cannot conceal from tactile sense.
- Activated as free action; sustained — dropping concentration ends it.
- is a *Sensory effect* that makes the character undetectable to one specific sense type
- grants total concealment — characters relying on that sense cannot perceive the character at all
- costs 2 ranks per visual sense type; costs 1 rank for most other sense types
- is activated as a free action; must be sustained — lapses if concentration is broken
- **Invariant:** concealment from tactile (touch) sense is not possible
- Collaborates with: sense type (the sense being blocked), Senses (a target's sensing capability), attack check (attackers relying on concealed sense are effectively blind)
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_094.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_095.md`

### Mind Reading

- Type Sensory, action Standard, range Perception, duration Sustained, cost 2 per rank.
- Opposed effect check vs. target's Will; 4 degrees: surface thoughts, personal thoughts, memories, subconscious.
- Target makes Will check at end of their turns; success breaks contact.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_117.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_118.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_119.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_120.md`

### Remote Sensing

- Type Sensory, action Free, range Rank range, duration Sustained, cost 1–5 per rank based on sense types.
- Displaces senses to another location; normal senses suppressed while active.
- Character is vulnerable while active (active defenses halved).
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_088.md`

### Senses

- Type Sensory, action None, range Personal, duration Permanent, cost 1 per rank.
- Each rank buys one enhancement from a large menu: Accurate, Acute, Analytical, Awareness, Communication Link, Counters Concealment, Counters Illusion, Danger Sense, Darkvision, Detect, Direction Sense, Distance Sense, Extended, Infravision, Low-Light Vision, Microscopic Vision, Penetrates Concealment, Postcognition, Precognition, Radio, Radius, Ranged, Rapid, Time Sense, Tracking, Ultra-Hearing, Ultravision.
- Permanent — purchased enhancements are always active.
- is a *Sensory effect* that acts as the catch-all for any sensory enhancement not covered by a dedicated effect
- allocates each rank to one enhancement from a large menu of options
- is permanent — all purchased enhancements are always active
- covers enhancements including Accurate, Acute, Analytical, Awareness, Communication Link, Counters Concealment, Counters Illusion, Danger Sense, Darkvision, Detect, Direction Sense, Distance Sense, Extended, Infravision, Low-Light Vision, Microscopic Vision, Penetrates Concealment, Postcognition, Precognition, Radio, Radius, Ranged, Rapid, Time Sense, Tracking, Ultra-Hearing, Ultravision
- **Invariant:** each rank of Senses provides exactly one enhancement from the defined list
- Collaborates with: sense type (the sense being enhanced), permanent duration, Concealment (countered by Counters Concealment enhancement)
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_085.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_128.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_129.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_130.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_131.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_132.md`

*Control and General Effect* — The Control and General Effect KA encompasses all effects that do not fit cleanly into Attack, Defense, Mobility, or Sensory categories — effects that manipulate the environment, transform matter, summon beings, provide utility, or enhance physical form. This is intentionally a broad KA; the domain is large (16 terms) and these effects share the common pattern of being useful in non-combat contexts even when they have combat applications. **Create**, **Environment**, **Illusion**, **Luck Control**, **Move Object**, **Summon**, and **Transform** are Control type; **Elongation**, **Enhanced Trait**, **Feature**, **Growth**, **Healing**, **Insubstantial**, **Quickness**, **Shrinking**, and **Variable** are General type.

### Create

- Type Control, action Standard, range Ranged, duration Sustained, cost 2 per rank.
- Max volume = effect rank on volume table; created objects have Toughness = effect rank.
- Objects vanish if unmaintained; character can spend PP equal to rank for permanence.
- is a *Control effect* that forms solid physical objects with Toughness and volume derived from effect rank
- sets created object Toughness = effect rank; sets max volume from effect rank on volume table
- sustains the object — objects vanish when the effect is not maintained; character can spend PP = rank for permanence
- can trap, block, or restrain targets; restraining uses effect rank as effective Strength
- **Invariant:** created objects are solid and physical — they have Toughness and can be damaged and destroyed
- Collaborates with: rank (sets volume and Toughness), PP spending (for permanence), grab/restrain (combat application)
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_087.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_096.md`

### Elongation

- Type General, action Free, range Personal, duration Sustained, cost 1 per rank.
- Reach extends to size rank + effect rank; +1 to grab checks per rank.
- is a *General effect* that extends the character's body or limbs to reach distant targets
- sets reach = size rank + effect rank on the distance table
- grants +1 to grab check rolls per rank due to improved leverage
- **Invariant:** Elongation does not grant enhanced Strength, Toughness, or any other physical enhancement beyond reach
- Collaborates with: size rank (contributes to total reach), grab check (the combat application of reach)
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_087.md`

### Enhanced Trait

- Type General, action Free, range Personal, duration Sustained, cost equal to base cost of trait per rank.
- Increases an existing trait by rank; subject to PL limits.
- Sustained — drops if character cannot maintain.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_101.md`

### Environment

- Type Control, action Standard, range Rank range, duration Sustained, cost 1–2 per rank.
- Alters environmental conditions (Cold, Heat, Light, Visibility, Movement impede) in a radius area.
- Multiple environment effects can be stacked on one Environment effect.
- is a *Control effect* that alters environmental conditions in a radius area
- offers selectable changes: Cold, Heat, Light, Visibility impairment, Movement impede
- determines radius from effect rank on the area table; additional environmental changes cost additional ranks
- **Invariant:** Environment does not directly damage targets — it creates hazardous or difficult conditions
- Collaborates with: effect rank (sets radius), environmental conditions (the changes made), movement speed (impede reduces it)
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_102.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_103.md`

### Feature

- Type General, action None, range Personal, duration Permanent, cost 1 per rank (each rank = one Feature).
- Provides one minor ability per rank with a concrete game effect; distinct from free descriptors.
- is a *General effect* where each rank purchases one minor, permanently active game capability
- requires each Feature to have a concrete game-mechanical effect approved by the GM
- is distinct from descriptors — descriptors are free flavor; Features cost PP and provide real benefits
- **Invariant:** each rank equals exactly one Feature with exactly one minor game effect
- Collaborates with: GM approval (required for each Feature definition), descriptor (conceptually adjacent but mechanically distinct)
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_104.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_105.md`

### Growth

- Type General, action Free, range Personal, duration Sustained, cost 2 per rank.
- Per rank: +1 Strength, +1 Stamina, +1 mass rank, −1 Stealth; size category changes per 4 ranks.
- Per 2 ranks: −1 Dodge, −1 Parry, +1 Intimidation. Per 8 ranks: +1 Speed.
- is a *General effect* that increases the character's size rank, gaining physical power at the cost of defenses and concealment
- applies per-rank bonuses: +1 Strength, +1 Stamina, +1 mass rank, −1 Stealth
- applies per-2-rank changes: −1 Dodge, −1 Parry, +1 Intimidation
- applies per-8-rank bonus: +1 Speed
- is sustained; returning to normal is a free action
- **Invariant:** Growth is sustained — if disrupted, the character immediately returns to normal size
- Collaborates with: size rank (the change driver), Strength/Stamina/Dodge/Parry/Stealth (the traits modified), sustained duration
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_087.md`

### Healing

- Type General, action Standard, range Close, duration Instant, cost 2 per rank.
- DC 10 check; each degree of success removes one damage condition from most severe.
- Cannot be used on same target more than once per scene; doesn't work on targets unable to recover naturally.
- is a *General effect* that removes damage conditions from a willing target
- makes a check vs. DC 10; each degree of success removes one condition from most severe
- stabilizes a dying character as part of its effect
- cannot be used on the same target more than once per scene
- does not function on targets incapable of natural recovery (constructs, undead — unless modified)
- **Invariant:** Healing removes conditions in order from most severe to least; it cannot skip conditions
- Collaborates with: damage conditions (the output), stabilize (dying target special case), scene (the reuse boundary)
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_108.md`

### Illusion

- Type Control, action Standard, range Perception, duration Sustained, cost 1–5 per rank by sense types.
- Insight check DC 10 + rank to detect; no physical substance — cannot cause real damage.
- Maintaining and altering illusion = free action each turn.
- is a *Control effect* that creates false sensory impressions for targets in perception range
- costs 1–5 pp/rank depending on number of sense types covered; each additional sense type adds 1 pp/rank
- allows an Insight check (DC 10 + rank) to detect the illusion — success reveals falsehood but does not remove it
- has no physical substance — cannot block movement, cause damage, or provide cover
- is maintained and altered as a free action each turn
- **Invariant:** Illusions cannot cause actual harm or provide real physical barriers
- Collaborates with: sense type (the dimension of the illusion), Insight check (the detection mechanism), sustained duration
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_109.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_110.md`

### Insubstantial

- Type General, action Free, range Personal, duration Sustained, cost 5 per rank (4 ranks total).
- Four forms: rank 1 Fluid, rank 2 Gaseous, rank 3 Energy, rank 4 Incorporeal.
- Switch between available forms as a free action.
- is a *General effect* with 4 progressive forms representing decreasing physicality
- form 1 (Fluid): liquid-like; form 2 (Gaseous): gas-like; form 3 (Energy): energy-like; form 4 (Incorporeal): immaterial
- allows switching between available forms as a free action
- form 4 (Incorporeal) allows passing through solid matter and ignoring most physical effects
- is sustained; returning to normal is a free action
- **Invariant:** higher rank forms include all lower rank capabilities; you must purchase ranks in order
- Collaborates with: descriptor (defines the fiction of each form), sustained duration, Affects Insubstantial extra (for others to affect an Insubstantial character)
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_114.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_115.md`

### Luck Control

- Type Control, action Reaction, range Perception, duration Instant, cost 3 per rank.
- Each rank grants one capability involving hero points (spend for another, transfer, negate, or force re-roll).
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_087.md`

### Move Object

- Type Control, action Standard, range Ranged, duration Sustained, cost 2 per rank.
- Effective Strength = rank for lifting/moving; cannot directly damage a target.
- Can make disarm, grab, or trip maneuvers at range; target resists with Strength check vs. effect rank.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_122.md`

### Quickness

- Type General, action Free, range Personal, duration Sustained, cost 1 per rank.
- Each rank reduces time rank of routine tasks by 1; does not affect non-routine tasks or movement.
- is a *General effect* that accelerates completion of routine tasks
- reduces the time rank of routine tasks by 1 per rank; at high ranks, hours become minutes, minutes become seconds
- does not affect non-routine tasks (those requiring checks) or movement speed
- **Invariant:** Quickness only applies to routine tasks; any task requiring a roll is not affected
- Collaborates with: time rank (the reduction target), routine check (the scope of tasks affected)
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_088.md`

### Shrinking

- Type General, action Free, range Personal, duration Sustained, cost 2 per rank.
- Per 4 ranks: −1 size category. Per rank: +1 Stealth. Per 2 ranks: +1 active defenses, −1 Speed.
- Reduces Strength (for size-based purposes) and Intimidation.
- is a *General effect* that decreases the character's size rank, improving defenses and stealth at cost of Strength and reach
- applies per-4-rank size category reduction
- applies per-rank bonuses: +1 Stealth; per-2-rank changes: +1 Dodge, +1 Parry, −1 Speed, −1 Intimidation
- reduces Strength for size-based purposes per size category reduction
- **Invariant:** Shrinking is sustained — returning to normal is a free action
- Collaborates with: size rank (the change driver), Dodge/Parry/Stealth/Speed (the traits modified), sustained duration
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_133.md`

### Summon

- Type Control, action Standard, range Close, duration Sustained, cost 2 per rank.
- Minion has power points = rank × 15; minion PL ≤ effect rank.
- Dazed when summoned (standard action first turn); directing = move action. Disappears if incapacitated.
- is a *Control effect* that calls an independently acting minion
- defines minion as having power points = effect rank × 15 and power level ≤ effect rank
- applies dazed condition to the minion on arrival (standard action only on first turn)
- directs the minion with a move action each turn; minion otherwise follows last instructions
- dismisses the minion if it is incapacitated; the summoner can re-summon later
- **Invariant:** minion PL cannot exceed the Summon effect rank; minion PP is fixed at rank × 15
- Collaborates with: effect rank (sets minion PP and PL cap), dazed condition (on arrival), move action (directing cost), incapacitated condition (dismissal trigger)
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_134.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_135.md`

### Transform

- Type Control, action Standard, range Close, duration Sustained, cost 2–5 per rank by scope.
- Cost by breadth: 2 pp narrow → up to 5 pp anything-to-anything; max mass = rank − 6 on mass table.
- Inanimate objects don't resist; living targets make Fortitude check. Sustained = reversible.
- is a *Control effect* that changes one type of object into another type at close range
- scales cost by scope: 2 pp/rank (narrow: one substance to one), up to 5 pp/rank (broad: anything to anything)
- determines transformable mass from effect rank on the mass table (rank − 6)
- allows inanimate objects to be transformed without resistance; living targets make Fortitude checks
- is sustained — transformation reverts when the effect ends unless the Continuous extra is applied
- **Invariant:** Transform requires a defined target type and result type at acquisition (or defined scope for broad transforms)
- Collaborates with: effect rank (sets mass limit), Fortitude (living target resistance), sustained duration (reversibility), Continuous extra (permanence)
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_121.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_137.md`

### Variable

- Type General, action Standard, range Personal, duration Sustained, cost 7 per rank.
- Pool size = rank × 5 power points; allocate to any effects of appropriate type/descriptor.
- Subject to PL limits; resetting requires not maintaining the effect.
- is a *General effect* that provides a pool of power points the character can allocate to any effects of a defined type or descriptor
- sets pool size = effect rank × 5 power points; any effects of the defined type can be built from this pool
- reallocates the pool as a standard action; all effects built from the pool are subject to PL limits
- resets the pool if the effect is not maintained (all active allocated effects end)
- **Invariant:** the pool size is exactly rank × 5; Variable-built effects cannot exceed PL limits
- Collaborates with: effect rank (sets pool size), PP pool (the allocatable resource), PL limits (the constraint on built effects), sustained duration
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_138.md`

*Power Array* — The Power Array abstraction defines how groups of Alternate Effects are organized into a shared cost pool that allows one set of power points to fund multiple effect options, used exclusively. An **Array** is the collection itself — the container that makes the mutual-exclusivity rule apply and the cost pool meaningful. An **Alternate Effect** is a variant effect added to an Array for a flat 1-point cost each, subject to the rule that its total cost cannot exceed the primary effect's total cost. A **Dynamic Alternate Effect** is a special variant that can share power points with other Dynamic effects and operate simultaneously at reduced effectiveness, at the cost of 2 flat points per dynamic alternate (and 1 point to make the base dynamic).

### Array

- A collection of Alternate Effects sharing a cost pool; all mutually exclusive — only one active at a time.
- Switching between effects = free action once per turn.
- If any effect is disabled/Nullified/drained, all effects in the Array are equally affected.
- is the *container concept* for a collection of Alternate Effects that share a cost pool under mutual exclusivity
- enforces the rule: only one effect in the Array can be active at a time (for non-Dynamic effects)
- propagates disable state: if any effect in the Array is Nullified or disabled, all are equally affected
- allows switching between effects as a free action once per turn
- **Invariant:** an Array requires at least one base effect and at least one Alternate Effect to be meaningful
- Collaborates with: Alternate Effect (the variants it contains), Dynamic Alternate Effect (the simultaneous variant), Nullify (the propagation trigger), free action (the switch mechanism)
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_141.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_143.md`

### Alternate Effect

- Flat extra; cost 1 point per Alternate Effect added to an Array.
- Total cost of the alternate cannot exceed the total cost of the primary (base) effect.
- Permanent effects cannot be Alternate Effects; only one active at a time.
- is a *variant effect in a Power Array* that can substitute for the primary effect at flat cost
- costs 1 flat point per Alternate Effect added to the Array
- must have a total cost (all extras, flaws, ranks included) ≤ the primary effect's total cost
- cannot be a permanent effect — permanent effects cannot be switched in/out
- **Invariant:** only one Alternate Effect (or the primary) can be active at a time
- Collaborates with: Array (the container), flat modifier (the cost mechanism), primary effect (the cost ceiling), mutual exclusivity rule
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_141.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_143.md`

### Dynamic Alternate Effect

- Flat extra; base effect costs 1 extra point to become dynamic; each Dynamic Alternate costs 2 flat points.
- Dynamic effects can share power points and operate simultaneously at reduced effectiveness.
- Character reallocates points among Dynamic effects once per turn as a free action.
- is a *variant of Alternate Effect* that can share power points with other Dynamic effects and operate simultaneously at reduced effectiveness
- costs 2 flat points per Dynamic Alternate Effect (the base effect costs 1 extra point to become dynamic)
- allows point reallocation among Dynamic effects once per turn as a free action
- operates at reduced effectiveness when sharing — combined allocation cannot exceed the Array pool total
- **Invariant:** Dynamic effects CAN operate simultaneously; standard Alternate Effects cannot
- Collaborates with: Array (the container), power points (shared resource), free action (reallocation mechanism), pool size (upper limit)
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_143.md`

*Boundary terms* — Terms this module uses but another module owns.

### power point

- Owned by: Character Construction
- The currency spent to acquire effects, traits, advantages, and skills.
- Power point budget is set by power level (PL × 15 at creation).
- This module uses power point costs as outputs; the budget and economy are Character Construction concerns.

### rank

- Owned by: Character Construction
- The numeric level of an effect, ability, skill, or other trait.
- Effects are acquired in ranks and scale with rank; the Power module uses rank in cost formulas and effect resolution.

### resistance check

- Owned by: Check Resolution
- The check made by a target to resist a power effect; typically DC 10 + effect rank.
- Every attack-type effect in this module specifies which resistance check applies (Toughness, Fortitude, Will, Dodge).

### Toughness

- Owned by: Combat
- Defense used to resist Damage effects; derived from Stamina + Protection ranks + other bonuses.
- Referenced by Damage, Blast, and similar effects as the resistance check target.

### Fortitude

- Owned by: Combat
- Defense used to resist Affliction and Weaken effects targeting physical resilience.

### Will

- Owned by: Combat
- Defense used to resist mental Affliction, Mind Reading, and Will-targeted Weaken.

### Dodge

- Owned by: Combat
- Defense used to avoid ranged attacks and Area effect saves (DC 10 + effect rank for half).
