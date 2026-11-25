## Language

*Power Economy* — Power Economy is the budgeting system at the heart of hero construction — it defines the total resources available, establishes what every trait category costs, and enforces the rule that a completed hero's expenditures must exactly equal the budget. Power level is the GM-controlled input that drives everything else: it sets the starting PP total (PL x 15), determines where the hard caps on trait pairs fall, and frames the general scope of what the hero can accomplish. Power points are the currency spent against those costs; basic trait costs are the fixed price list that converts design intentions into PP allocations. Starting power points is the budget amount that results from the GM's PL choice and that a finished hero must spend exactly. These four concepts form a closed accounting loop: PL determines budget, budget is allocated at fixed per-category costs, the sum must balance. The GM can vary the starting PP total up or down from the table, but the relationship between PL, budget, and costs always holds.

### power level

- Power level (PL) is the GM-set measure of overall hero effectiveness — primarily combat capability but also the general scope of tasks a character can accomplish on a routine basis.
- PL establishes the starting power point budget and governs hard caps on every paired trait combination (attack/effect, defenses, skill modifier).
- PL ranges from 1 (15 PP) to 20 (300 PP), with PL 10 being the default recommended starting point for most series.
- NPCs are not bound by PL limits; the GM assigns traits at desired ranks and derives effective PL from the character's highest relevant offensive/defensive pair.
- The GM sets PL for the entire series; individual heroes in the same series share the same PL ceiling.
- Sets the series-wide PP budget by formula (PL × 15) before any design choices are made.
- Governs hard caps on every paired trait combination: attack/effect, Dodge/Toughness, Parry/Toughness, Fortitude/Will, and skill modifier.
- Applies uniformly to all player characters in the same series; the GM cannot vary PL per hero.
- Does not constrain NPC traits — derives NPC effective PL retrospectively from the character's highest relevant offensive/defensive pair.
- Frames the general scope of what heroes of this series can accomplish on a routine basis.
- **Invariant:** no hero construction is valid without an established PL; the budget, all cap limits, and the skill modifier ceiling all derive from PL being set first.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_024.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_026.md`

### power points

- Power points (PP) are the currency of hero construction — every ability rank, defense rank, skill rank, advantage, and power effect is purchased with PP.
- Once spent on a trait, PP are locked to that trait and cannot be freely moved without GM permission or a specific power effect.
- PP are awarded by the GM at the end of adventures and spent between sessions to improve traits.
- The total spent PP must equal exactly the starting PP total; too many or too few signals a design error.
- Serves as the construction currency spent to acquire every trait, tracking each allocation at the applicable Basic Trait Costs rate.
- Locks spent PP to the chosen trait after allocation; redistribution requires GM permission or a specific power effect.
- Accumulates through GM adventure awards and is spent between sessions to improve hero traits using the same cost formulas as initial construction.
- **Invariant:** a completed hero's total spent PP must equal exactly the starting PP total; any discrepancy is a design error that must be corrected before GM approval.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_025.md`

### starting power points

- Starting power points is the initial PP budget available to build a new hero, determined by the series power level: PL x 15.
- The Starting Power Points table maps PL 1-20 to budgets of 15-300 PP in 15-point increments.
- The GM may vary the starting PP total up or down from the table value to suit the series.
- A completed hero's trait costs must sum exactly to the starting PP total.
- Derives from the GM's chosen PL via the fixed formula PL × 15, producing the exact budget that frames the entire hero design envelope.
- Constrains the total resources available for trait allocation; the sum of all trait costs must equal this value exactly.
- Permits GM adjustment up or down from the table value when series-specific balance requires it.
- **Invariant:** a completed hero's PP expenditure must equal starting PP; over- or under-spending by even one PP signals an incomplete design.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_024.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_026.md`

### basic trait costs

- Basic trait costs define the PP price for each trait category: abilities cost 2 PP per rank; defenses cost 1 PP per rank above the base provided by abilities; skills cost 1 PP per 2 total skill ranks; advantages cost 1 PP per advantage or advantage rank.
- Power costs follow the formula: ((base effect cost + extras minus flaws) x rank) + flat modifiers.
- These costs apply equally when building a hero from scratch and when spending earned PP to improve traits.
- Basic costs establish the economy constraint that ties the PP budget to trait choices.
- Converts design intentions into PP allocations via a fixed price schedule covering every trait category.
- Applies fixed rates: abilities at 2 PP/rank, defenses at 1 PP/rank, skills at 1 PP per 2 ranks, advantages at 1 PP/rank or per ranked advantage rank.
- Applies a formula-driven rate to powers: ((base effect cost + extras − flaws) × rank) + flat modifiers, with specific rates defined in the Powers chapter.
- Provides the accounting reference against which the PP total balance check is validated.
- **Invariant:** trait costs must be computed at the rates defined in the Basic Trait Costs table; no hero-specific pricing deviations are permitted outside power effects.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_023.md`

*Power Level Limits* — Power Level Limits is the constraint system that governs where and how players may allocate their PP. While Power Economy establishes the total budget and per-trait pricing, Power Level Limits imposes hard caps on the pairing of offensive, defensive, and skill traits — ensuring that no hero's single axis of capability exceeds what the series power level deems appropriate. There are five named limit pairs (attack & effect, Dodge & Toughness, Parry & Toughness, Fortitude & Will, and skill modifier) plus the trade-off concept that describes the legal design space within each limit pair. Because the limits apply to sums rather than individual ranks, a player may deliberately skew one side of a pair higher than the other so long as the total remains within 2xPL. The GM is the authority that monitors and approves combinations that swing asymmetrically beyond 50% disparity within a pair.

### trade-off

- A trade-off is the design choice to make one trait in a PL-limited pair higher than the other while keeping their sum within the 2xPL cap.
- Trade-offs let a player build a hero optimized for high attack skill and low damage output, or high Toughness with low Dodge/Parry, all within legal PL limits.
- The GM monitors wide asymmetries: a disparity greater than 50% between the paired traits is a balance concern meriting close review before approval.
- Trade-offs are self-limiting in practice — a hero with massive Toughness but no active defenses has a different but not necessarily overpowered risk profile.
- Permits individual paired traits to differ from each other within the constraint that their sum must not exceed 2 × PL.
- Enables design diversity: a hero can build a high-skill, lower-damage fighter, a raw-power brute with minimal attack finesse, or any balanced distribution between.
- Flags extreme imbalances — a disparity of more than 50% between traits in a pair — as a design concern for close GM scrutiny at approval.
- Does not change or relax the hard paired cap; trade-off operates entirely within the fixed ceiling.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_027.md`

### attack & effect limit

- The attack & effect limit specifies that a hero's total attack bonus plus the effect rank of that attack cannot exceed twice the series power level (2xPL).
- If a power effect allows a resistance check but requires no attack check, its effect rank alone cannot exceed PL.
- The limit applies to each attack individually — a hero may have multiple attacks that each independently respect the cap.
- Exceeding this cap during design requires reducing either the attack bonus or the effect rank until the sum is within 2xPL.
- Enforces that attack bonus + effect rank ≤ 2 × series PL for every attack that requires an attack roll.
- Enforces that effect rank alone ≤ PL when an effect allows a resistance check without requiring an attack roll.
- Validates each attack/effect pair independently: a hero with multiple attacks checks each combination against the cap separately.
- **Invariant:** no single attack may exceed the 2 × PL ceiling on its combined bonus and effect rank, regardless of trade-off distribution.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_026.md`

### Dodge & Toughness limit

- The Dodge & Toughness limit specifies that the sum of a hero's Dodge defense and Toughness defense cannot exceed twice the series power level (2xPL).
- Both Dodge (an active defense) and Toughness (a passive defense) count toward this paired cap.
- Trade-offs within this pair are legal: a hero may have very high Toughness and low Dodge (or vice versa) as long as the sum stays within 2xPL.
- Enforces that Dodge (purchased active defense) + Toughness (passive resistance) ≤ 2 × series PL.
- Governs the hero's resilience against ranged attacks and area-effect threats.
- Shares Toughness with the Parry & Toughness pair: any increase to Toughness simultaneously tightens both defense constraints.
- **Invariant:** the sum of Dodge and Toughness cannot exceed 2 × PL at design time or after any advancement spending.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_026.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_027.md`

### Parry & Toughness limit

- The Parry & Toughness limit specifies that the sum of a hero's Parry defense and Toughness defense cannot exceed twice the series power level (2xPL).
- Parry is the close-combat active defense equivalent of Dodge; it pairs with Toughness under the same cap structure.
- Trade-offs within this pair are legal by the same logic as the Dodge & Toughness pair.
- Enforces that Parry (active close-combat defense) + Toughness ≤ 2 × series PL.
- Governs close-combat resilience independently from the Dodge pair.
- Shares Toughness with the Dodge & Toughness pair: improving Toughness tightens both limit pairs simultaneously.
- **Invariant:** Parry + Toughness ≤ 2 × PL at all times, subject to the same trade-off flexibility as other limit pairs.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_026.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_027.md`

### Fortitude & Will limit

- The Fortitude & Will limit specifies that the sum of a hero's Fortitude defense and Will defense cannot exceed twice the series power level (2xPL).
- Both Fortitude and Will are resistance defenses (not active); they pair together under the same cap as the combat defense pairs.
- Trade-offs within this pair are legal: investing heavily in Fortitude at the expense of Will, or vice versa, is a valid design choice.
- Enforces that Fortitude + Will ≤ 2 × series PL.
- Governs the hero's capacity to resist physical and mental threats that bypass active defense: afflictions, ailments, mental influence.
- Operates independently from the combat defense pairs; Fortitude and Will are resistance defenses only, not active defenses.
- **Invariant:** Fortitude + Will ≤ 2 × PL at all times; trade-off applies within this pair just as with defense limit pairs.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_026.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_027.md`

### skill modifier limit

- The skill modifier limit specifies that a hero's total modifier with any single skill (ability rank + skill rank + advantage modifiers) cannot exceed PL + 10.
- This limit applies even to untrained skill modifiers (based solely on ability rank), so it effectively constrains how high any ability can usefully go for skill purposes.
- The cap is per skill, not per ability; a hero with high Agility may approach the limit on Acrobatics while having a lower modifier in another Agility-based skill if they lack ranks in it.
- Enforces that total skill modifier (ability rank + skill rank + advantage modifiers) ≤ PL + 10 for any single skill.
- Applies to untrained checks as well — since untrained use relies on ability rank alone, this effectively caps every ability rank as a side effect.
- Validates each of the 24 skills independently against the per-skill limit.
- **Invariant:** no constructed skill modifier may exceed PL + 10; this bound constrains all ability rank investments across the hero.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_026.md`

*Complication* — Complication is the narrative-challenge system that creates dramatic hooks for play while rewarding players for engaging with adversity rather than avoiding it. A complication is a structural narrative element — not a PP expenditure — that the GM uses to introduce challenges targeting specific vulnerabilities in a hero's story. Unlike the up-front-reward model of older game systems, complications pay out a hero point only when activated during play and engaged with by the player, making the reward proportional to the actual dramatic cost paid. Every hero requires at least two complications: one Motivation (the mandatory drive that defines why the hero acts heroically) and at least one other from a broad palette including enemy, secret, weakness, power loss, identity, responsibility, relationship, and many more. Complication interacts with the hero point boundary concept: when a complication fires, the hero point is generated and becomes available to the player. The Complication KA owns the classification, selection rules, activation conditions, and evolution rules for all narrative challenge types.

### complication

- A complication is a narrative flaw or challenge the GM introduces during play to test the hero; when the hero is affected by it, the player earns a hero point as compensation.
- Every hero must have at least two complications: one Motivation and at least one other.
- Complications use a pay-as-you-go reward model: the hero point is earned when the complication causes actual trouble, not at character creation.
- The GM may limit the total number of active complications per hero for narrative manageability; complications not activated during a session generate no reward.
- Complications can change over the course of a series: resolved complications are replaced with new ones as the hero's story evolves.
- Complications can arise from injuries, malfunctioning devices, or persistent distractions — anything that causes trouble and earns a hero point.
- Records a narrative liability that the GM can invoke during play to create genuine trouble for the hero and earn them a hero point.
- Requires at minimum a motivation; two or more total complications are strongly recommended.
- Can evolve over the course of the series as old conflicts resolve and new ones emerge; the GM may cap the number of active complications a hero holds simultaneously.
- **Invariant:** every hero must have at least one motivation complication; without it, the hero has no hero-point-earning mechanism tied to character drive.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_028.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_030.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_031.md`

### motivation

- Motivation is the mandatory complication that answers why the hero fights — what drives them to risk their life for others.
- Every hero must have exactly one Motivation complication (chosen as the required first complication).
- Common motivations include Acceptance, Doing Good, Greed, Justice, Patriotism, Recognition, Responsibility, and Thrills.
- A shared motivation can create an empathic bond in social encounters: with GM permission, circumstance bonuses apply to interaction checks with characters sharing the same motivation; opposing motivations may impose a penalty.
- Motivation can function as a descriptor for powers at the GM's option, enabling powers that detect or affect characters with a particular motivation.
- When motivation is the source of a hero's powers, losing faith in that motivation can trigger Power Loss.
- Conflicting motivations within a hero create dramatic roleplay hooks and may lead to motivation change over the series.
- Defines the primary ethical or personal drive that shapes how the hero approaches their role and resolves moral conflicts in play.
- Functions as a required complication that gives the hero a core character dimension the GM can invoke and the player must play through honestly.
- Can serve as a power descriptor at GM option, enabling emotion-sensitive powers to detect or affect the hero based on motivation alignment.
- Can be the triggering condition for a power loss complication when the motivation wavers or is actively undermined in play.
- **Invariant:** every hero must have exactly one motivation; a hero without a stated motivation is mechanically incomplete and cannot earn hero points through character-drive complications.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_029.md`

### enemy

- Enemy is a complication representing an adversary who actively tries to harm or thwart the hero.
- When the enemy appears and causes a particular problem (abduction of a loved one, laying a trap), the hero earns a hero point.
- The enmity may be one-sided or mutual — mutual enmity makes encounters more personally charged.
- An enemy-driven adventure is inherently more complicated for the hero, providing the GM a reliable narrative handle.
- Defines an adversarial figure who actively opposes the hero and whose interference in play generates hero points.
- Specifies the adversary's identity and the nature of the enmity — one-sided (adversary targets hero) or mutual (genuine rivalry acknowledged on both sides).
- Triggers a hero point only when the GM introduces the enemy in an adventure and the hero suffers specific harm or meaningful hardship as a result.
- Can represent individuals, rival heroes, criminal organizations, or government agencies — any persistent adversarial relationship with defined identity and nature.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_029.md`

### secret

- Secret is a complication representing something potentially damaging or embarrassing the hero is hiding — most commonly a secret identity, but also a secret weakness or dark past.
- Occasionally something or someone threatens to reveal the secret, activating the complication and earning the hero a hero point.
- A secret identity creates the dual-life challenge of protecting loved ones who don't know the truth while also hiding from enemies.
- Defines something potentially damaging or embarrassing that the hero actively conceals from the world.
- Most commonly the hero's true identity, but can be a dark past, a hidden weakness, or a morally compromising fact the hero cannot afford to have exposed.
- Triggers a hero point only when something or someone actively threatens to reveal the secret — not merely because the secret exists in the background.
- Can intersect with the identity complication when the secret being kept IS the dual identity itself.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_030.md`

### weakness

- Weakness is a complication representing a specific substance, energy, or condition that bypasses the hero's normally strong defenses or inflicts extra harm.
- Common weakness effects include adding degrees of effect, imposing an entirely different effect (Affliction, Damage, Weaken), or other outcomes agreed with the GM in advance.
- When the GM invokes the weakness against the hero, it activates as a complication earning a hero point.
- Examples of weakness triggers: silver for a werewolf-type hero, exotic materials or energies harmful only to that hero.
- Specifies a material, condition, or circumstance that overcomes the hero's normally strong defenses or inflicts unusual harm.
- Defines both the triggering substance/condition and the precise mechanical effect: increased damage degrees, affliction, specific power failure, or an alternate effect class.
- Requires negotiation with the GM at construction time so both the trigger and its effect are agreed before play begins.
- Triggers a hero point when the GM uses the weakness as an active complication during an adventure.
- **Invariant:** both the triggering condition and the mechanical effect must be specified at construction time; a vague weakness without agreed trigger and effect is not a valid complication.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_030.md`

### power loss

- Power Loss is a complication in which specific circumstances cause some or all of the hero's powers to fail, stop working, or be stripped away temporarily.
- Triggers for Power Loss include dependence on objects that can be stolen, environmental conditions (darkness, exotic radiation), or wavering motivation (when motivation is the power source).
- When the triggering condition occurs and the hero is adversely affected, the player earns a hero point.
- Defines specific circumstances under which the hero's powers fail entirely: a triggering substance, condition, location, or a direct undermining of the hero's motivation.
- Triggers a hero point only when the powers actually fail due to the defined trigger in play — proximity to the trigger alone does not earn the point.
- Can be linked to motivation: heroes who derive power from their convictions may suffer power loss when their motivation is genuinely undermined in play.
- Requires the trigger to be specific and defined at construction time; overly broad triggers require GM negotiation to avoid making the complication too easily activated.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_029.md`

### identity

- Identity is a complication representing the challenge of maintaining a secret or separate persona — hero name vs. civilian name.
- The dual-identity complication includes the risk of exposure, the juggling of two lives, and the transformation between personas.
- For heroes who physically transform between personas, additional complications can arise from controlling the transformation or from losing powers in the civilian form.
- Heroes who abandon their secret identity and live publicly face different complications: constant media attention, fan intrusion, and enemies able to track them easily.
- Defines the hero's approach to their dual existence: maintaining a secret civilian identity separate from the hero persona, or operating fully as a publicly known hero.
- Secret identity heroes actively manage two personas, must protect loved ones from knowing the truth, and risk exposure if the two worlds collide.
- Public identity heroes face no dual-life management complexity but lose the safety of anonymity; enemies, media, and fans can track their civilian life.
- Earns a hero point as a complication when the chosen identity approach creates genuine conflict, exposure risk, or personal cost during an adventure.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_034.md`

### responsibility

- Responsibility is a complication representing demands on the hero's time and attention: family obligations, professional duties, and similar ongoing commitments.
- When a responsibility creates conflict with the hero's heroic activities (missed obligations, loss of relationships or employment), it activates as a complication earning a hero point.
- Defines competing obligations — family duties, professional commitments, civic roles — that legitimately claim the hero's time in conflict with heroic duties.
- Creates complication opportunities when the responsibility is visibly neglected, placed at risk, or in direct tension with what the hero must do as a hero.
- Triggers a hero point only when the conflict is made manifest in play; the responsibility must actively interfere, not merely exist in the background.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_030.md`

### relationship

- Relationship is a complication representing the important people in a hero's life — friends, family, romantic partners — who can be a source of strength but also a source of danger.
- If loved ones don't know the hero's secret, they must be kept safely in the dark; if they do know, they become targets for the hero's enemies.
- When a relationship causes a specific problem (a loved one threatened, a friendship strained by the hero's double life), the complication activates.
- Defines key people in the hero's life whose safety and knowledge create emotional stakes and potential vulnerability.
- Generates different risk profiles depending on whether the person knows the hero's identity: an informed confidant becomes a danger target; an ignorant loved one requires the hero to maintain the deception.
- Creates hero-point opportunities when the relationship is directly threatened, exploited, or placed in conflict with heroic duties during an adventure.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_030.md`

*Hero Advancement* — Hero Advancement is the progression system that operates after initial character creation — it governs how the hero grows and improves over the course of a series. It has three parts: the regular earning and spending of PP awarded by the GM after completed adventures (hero advancement), the ratcheting up of the series PL ceiling once the accumulated PP exceeds the current PL's natural range (increasing power level), and the exceptional mechanism for moving already-spent PP from one trait to another when a narrative transformation event occurs (reallocating power points). Hero Advancement interacts directly with Power Economy (more PP enters the budget pool after each adventure) and Power Level Limits (raising PL expands the cap headroom, enabling investment in traits previously maxed). Complications earn hero points during play, but hero points do not enter the PP advancement pool — they are a distinct boundary concept owned by Check Resolution.

### hero advancement

- Hero advancement is the process of earning and spending PP awarded after each completed adventure to improve the hero's traits.
- The GM awards 1 PP per successfully completed one-session adventure; 2 PP for defeating especially powerful foes; 1 PP per session for multi-session adventures, plus a possible bonus.
- Players spend earned PP between adventures on new or improved traits following the same basic trait costs as during character creation.
- Once allocated, earned PP are locked to their traits unless a specific effect causes reallocation.
- The GM may vary advancement rates by awarding more or fewer PP per adventure, and may withhold the award for very poor hero performance.
- Awards PP at the end of adventures: typically 1 PP per completed single-session adventure, up to 2 PP for especially powerful or difficult challenges, and 1 PP per session for multi-session adventures with a possible end-of-arc bonus.
- Requires PP to be spent between sessions — not during play — on new or improved traits, using the same cost formulas and PL limits as initial construction.
- Allows unspent PP to accumulate so the hero can invest them after a PL increase on traits that were previously at the PL cap ceiling.
- Enables the GM to withhold the PP award when the heroes handled an adventure especially poorly.
- **Invariant:** all advancement spending obeys the current series PL limits; no earned PP can raise a trait above the current PL cap.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_034.md`

### increasing power level

- Increasing power level is the process by which the GM raises the series PL — typically by +1 — once the heroes have accumulated approximately 15 additional PP since the series started or since the last PL increase.
- After a PL increase, heroes can spend accumulated PP on traits that were previously capped at the old PL maximum.
- When PL increases, the GM should reevaluate NPC villains to keep them as appropriate challenges; some may be improved, while others are intentionally left behind as the heroes outgrow them.
- Triggers when heroes have accumulated approximately 15 additional PP since the series start or the last PL increase — mirroring the 15-PP interval used to set initial budgets.
- Raises the series PL by +1, expanding cap headroom on every paired limit simultaneously and unlocking spending on previously-maxed traits.
- Requires the GM to reevaluate NPC villain trait levels to maintain appropriate challenge; some adversaries are advanced, others intentionally left behind as the heroes outgrow them.
- Enables the introduction of new villains and challenges calibrated to the new PL level.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_034.md`

### reallocating power points

- Reallocating power points is the exceptional process of moving already-spent PP from one trait to another, changing the hero's trait profile within PL limits.
- Reallocation is normally prohibited; it requires either GM permission as a deliberate narrative event or a power effect (e.g., the transformed condition).
- In-fiction triggers for reallocation include exposure to transformational forces (intense radiation, mutagenic chemicals, cosmic power sources).
- Reallocation events should be rare unless their effects are intended to be temporary complications.
- Permits already-spent PP to move from one trait to another, changing the hero's trait profile within current PL limits.
- Normally prohibited after initial allocation; requires explicit GM permission as a deliberate narrative event, or activation of a specific power effect such as the transformed condition.
- Can result in the hero losing traits entirely and gaining wholly new ones — the most radical form of hero transformation.
- Should be rare unless the triggering power effect is designed to produce frequent or temporary transformations as part of the hero concept.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_027.md`

*Hero Identity* — Hero Identity is the narrative construction layer that answers who the hero is, not just what they can do. While Power Economy governs resource allocation and Power Level Limits sets mechanical constraints, Hero Identity defines the imaginative context: the archetype template a player selects or customizes as a starting point, the concept that drives the design before any PP is spent, the origin story that explains how the hero acquired powers and provides a descriptor tag, the background details (name, appearance, age, personality, goals) that make the hero a person rather than a stat block, and the costume that signals the hero's public persona. These terms are interdependent: the archetype structures the concept, the origin contextualizes both powers and background, and the costume materializes the identity visually. Hero Identity does not own mechanical trait rules — it owns the narrative elements that frame who the hero is and how they present themselves to the world.

### hero archetype

- A hero archetype is a ready-to-play, fully built PL 10 hero template that a player can adopt as-is or customize as a starting point.
- Archetypes cover a range of hero types (Crime Fighter, Martial Artist, Powerhouse, Warrior, etc.) and some offer an Options section with simple variant choices (different skill sets, alternate powers, vehicles).
- Even without a formal Options section, any archetype can be customized freely within PP budget, PL caps, and GM approval.
- Archetypes on pages 35-49 of the Handbook include some advantages printed in italics, indicating those come from Enhanced Advantage power effects rather than being purchased directly.
- Archetypes serve as inspiration and shortcut, not a constraint; players comfortable with design can change any trait.
- Provides a complete, tested PL 10 hero template that a player can adopt unchanged or use as a design starting point.
- Offers Options sections where defined, allowing simple variant choices across skills, advantages, or power sets within the archetype's theme.
- Can be freely modified beyond any Options section within PP budget, PL caps, and GM approval; the archetype is a starting point, not a constraint.
- Marks advantages sourced from Enhanced Advantage power effects with italics to distinguish purchased advantages from power-granted ones.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_022.md`

### hero concept

- Hero concept is the creative starting point for character design — the player's answer to what sort of hero they want to create before spending any PP.
- A concept covers basic abilities, powers, origin, and theme; it guides the 10-step design process.
- Players are encouraged to share the concept with the GM before starting design work and to consult fellow players to ensure the team composition makes sense.
- Inspiration for concepts can come from archetypes, comic books, television, or movies.
- Establishes the creative foundation for the entire design: what type of hero, what powers, what origin, what theme — before any PP is spent.
- Guides all subsequent construction steps: PP allocations, power selection, complication choices, and background details all flow from the concept.
- Must be shared with the GM before design begins to validate series fit, and ideally with fellow players to ensure team composition makes sense.
- Carries no PP cost and no mechanical rule; its role is to make the stat block coherent and the hero a deliberate creation rather than an arbitrary collection of traits.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_022.md`

### origin

- Origin describes how the hero acquired superpowers; it shapes background narrative and can serve as a power descriptor.
- Common origins: Accident (radiation, chemicals, energy exposure), Alien (member of a non-human species with inherent powers), Endowment (powers granted by an outside patron or force), Experiment (deliberate scientific or mystical transformation), Mutant (born with latent genetic potential that manifests under stress), Training (powers acquired through hard work, martial discipline, or magical study).
- Origins function as descriptors for powers: a mutant hero can be detected by mutant-detection powers; a mystic's powers may be affected by anti-magic; etc.
- The GM may restrict or require particular origins for the series setting.
- A hero's age is connected to origin: wartime heroes may have ancient origins; teenage heroes often have recent accident or mutant origins.
- Establishes how the hero acquired powers and provides the narrative provenance that explains abilities, background, and potential complications.
- Supported types: Accident, Alien, Endowment, Experiment, Mutant, and Training — each carrying different narrative implications for the hero's history and world relationships.
- Functions as a power descriptor when the GM applies it: a mutant hero can be targeted by mutant-detection powers; a mystic's abilities may be countered by anti-magic effects.
- Subject to GM restriction or mandate for the series setting; the GM may ban, require, or limit specific origins for story-consistency reasons.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_032.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_033.md`

### costume

- A costume is the hero's distinctive visual identity in their superhero role — typically a unique, colorful outfit emblazoned with a symbol or logo.
- Costumes can range from skin-tight spandex to military fatigues, body armor, suits of ancient or high-tech armor, or even ordinary street clothes.
- By comic-book convention, a hero's costume is immune to the hero's own powers (a flame-controlling hero does not incinerate their outfit) — this costs no PP.
- Costumes can be damaged or torn by attacks and external circumstances, unlike normal wear from the hero's powers.
- For heroes who maintain a secret identity, the costume is the key element of the alter-ego persona transition.
- Mechanical details of costumes as equipment (stats, gadgets) belong to the Gadgets & Gear module.
- Provides the hero's distinctive visual identity in their superhero role — the primary external marker distinguishing the hero persona from the civilian persona.
- Is immune by comic-book convention to wear from the hero's own powers (a fire controller does not incinerate their costume) — this immunity costs no PP.
- Can be damaged or destroyed by external attacks and environmental circumstances, unlike the immunity to power-caused wear.
- Serves as the key persona-transition marker for secret-identity heroes: donning or removing it signals the switch between civilian and hero roles.
- Mechanical details of costumes treated as equipment (armor values, gadgets) are defined in the Gadgets & Gear module, not this module.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_034.md`

### background

- Background encompasses the narrative details that make a hero more than a stat block: name (code name or real name), appearance (race, sex, ethnicity, distinctive features), personality, goals, and age.
- Background elements include the hero's name style (origin-based, powers-based, themed, titled, or simply a cool-sounding word), the hero's persona when not fighting crime, and long-term narrative goals.
- A hero's age influences trait choices: older characters tend toward higher skill ranks and lower physical ability ranks; younger heroes may have fewer skills but emerging raw ability.
- Background details inform which complications are most resonant and how the hero interacts with the social world.
- Encompasses the narrative details that make a hero a person with history rather than a stat block: name, appearance, age, personality, and goals.
- Name selection follows creative conventions (origin-based, power-based, themed, titled, aesthetic, or real name) that signal the hero's style and persona.
- Age shapes plausible trait choices: older heroes trend toward higher skill ranks and lower raw physical ability; younger heroes may have emerging raw capability with fewer trained skills.
- Goals beyond generic heroism provide story hooks, roleplaying depth, and natural sources for complications and character arcs.
- Background details directly inform which complications feel authentic and how the hero navigates the social world.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_031.md`

*Boundary terms*

### trait

- Owned by: Assign Abilities
- A trait is any mechanical element purchased with power points: ability rank, defense rank, skill rank, advantage, or power effect.
- Character Construction depends on the concept of trait as the unit of PP expenditure; the specific rules for each trait type are owned by the Assign Abilities, Manage Skills, Select Advantages, and Configure Powers modules.
- Basic trait costs (the PP prices per rank or unit) are defined within this module; the behavioral rules of individual traits live in their owning modules.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_024.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_025.md`

### hero point

- Owned by: Check Resolution
- A hero point is the reward earned when a complication is activated by the GM and the player goes along with it; it can be spent later to enhance rolls or other actions.
- Character Construction depends on hero points as the incentive mechanism that gives complications their pay-as-you-go value; the rules for spending and earning hero points live in the Check Resolution module.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_028.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_030.md`

### descriptor

- Owned by: Configure Powers
- A descriptor is a narrative tag attached to a power or trait that defines what it is and how it interacts with the world (e.g., "mutant," "mystic," "fire," "alien").
- Character Construction depends on descriptors because origins and motivations can serve as power descriptors, affecting detection and targeting of powers; the full rules for descriptors are owned by the Configure Powers module.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_029.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_033.md`
