## Language

*Advantage* — An advantage is the named, purchasable capability unit of the Advantage module. It owns the identity of what an advantage is, how much it costs, how it scales through ranks, and what distinguishes ranked from non-ranked advantages. Every specific advantage is an instance of this concept. It collaborates with the Character Construction module (power points fund purchases) and interacts with all four category concepts, but does not own combat resolution, skill checks, or hero point mechanics. An advantage must always cost exactly 1 power point per rank; must always belong to exactly one of the four categories; and a non-ranked advantage must never appear with a rank number greater than 1.

### advantage

- An advantage is a special ability or rule-breaking capability beyond the reach of ordinary characters, purchased with power points at character creation or advancement.
- Advantages allow heroes to do things most characters cannot, or to do ordinary things significantly better.
- Each advantage is categorized as Combat, Fortune, General, or Skill based on the domain of activity it affects.
- Advantages cost 1 power point per rank; those with no ranks are acquired once at effective rank 1.
- Each advantage's description states the benefit it provides and whether the advantage can be acquired in ranks.
- accepts cost of exactly 1 power point per rank during character creation or advancement
- belongs to exactly one of the four categories (Combat, Fortune, General, Skill) fixed at definition time
- allows the holder to do something most characters cannot do, or to do something ordinary significantly better
- scales through rank when the advantage is Ranked; a non-ranked advantage is acquired once at effective rank 1
- publishes its benefit description and whether additional ranks are available
- **Invariant:** cost is always exactly 1 power point per rank.
- **Invariant:** a non-ranked advantage is always at effective rank 1.
- **Invariant:** category membership is fixed and always exactly one of the four categories.
- **Invariant:** the benefit must never grant an effect equivalent to a power costing more than 1 point.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_065.md`

### advantage rank

- Ranked advantages may be purchased multiple times, each purchase adding one rank that increases or extends the advantage's effect.
- Rank is noted by a number after the advantage name (e.g., "Defensive Roll 2" for two ranks).
- Non-ranked advantages are acquired only once; they do not scale with repeated purchase.
- If a maximum number of ranks exists, it is listed in parentheses in the advantage's heading (e.g., "Ranked (2)").
- Advantage cost equals 1 power point per rank, matching the cost formula for abilities and skills.
- records itself as a number after the advantage name (e.g., "Defensive Roll 2" for two ranks)
- scales the advantage's effect upward with each rank purchased
- enforces a published maximum rank when the advantage heading specifies one (e.g., "Ranked (2)")
- prevents purchase of additional ranks beyond the stated maximum
- for non-ranked advantages, holds fixed at effective rank 1 and cannot increase
- **Invariant:** rank cannot exceed the maximum stated in the advantage's heading when a cap is listed.
- **Invariant:** a non-ranked advantage is always rank 1.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_065.md`

*Advantage Category* — An advantage category is the classification label that groups every advantage into one of four domain areas: Combat, Fortune, General, and Skill. The category owns the boundary of what kind of activity the advantage affects. The four category terms collectively define the taxonomy; each specific advantage belongs to exactly one category and that membership is fixed at definition time. Categories do not have ranks and are not purchased; they are structural tags. An advantage must always belong to exactly one category; no advantage may belong to two categories simultaneously.

### combat advantage

- Combat advantages modify how combat maneuvers are performed or provide bonuses during fighting.
- A combat advantage typically creates a trade-off (e.g., sacrificing attack bonus for effect bonus) or removes a penalty from a specific combat action.
- The full list includes: Accurate Attack, All-out Attack, Chokehold, Close Attack, Defensive Attack, Defensive Roll, Evasion, Fast Grab, Favored Environment, Grabbing Finesse, Improved Aim, Improved Critical, Improved Defense, Improved Disarm, Improved Grab, Improved Hold, Improved Initiative, Improved Smash, Improved Trip, Improvised Weapon, Move-by Action, Power Attack, Precise Attack, Prone Fighting, Quick Draw, Ranged Attack, Redirect, Set-up, Takedown, Throwing Mastery, Uncanny Dodge, Weapon Bind, Weapon Break.
- Combat advantages can be combined to represent fighting styles such as martial arts disciplines or superhero combat techniques.
- classifies each member advantage as affecting combat — establishing the domain boundary for this category
- modifies maneuver terms (attack bonus, active defenses, effect modifier, critical range) rather than skill use or hero point spending
- combines with other combat advantages at the character level to form coherent fighting styles (e.g., martial arts disciplines)
- **Invariant:** a combat advantage always modifies a combat maneuver mechanic.
- **Invariant:** it never requires a hero point to activate.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_065.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_067.md`

### fortune advantage

- Fortune advantages require spending a hero point to activate; they enhance or modify the use of hero points.
- Fortune advantages include: Beginner's Luck, Inspire, Leadership, Luck, Seize Initiative, and Ultimate Effort.
- Each fortune advantage defines what the hero point purchase achieves (e.g., temporary skill ranks, an inspiration bonus, a removed condition, a die re-roll, initiative priority, or a guaranteed roll of 20).
- classifies each member advantage as requiring a hero point spend to activate its effect
- defines the specific outcome that the hero point purchase achieves (re-roll, group bonus, condition removal, or temporary skill ranks)
- Luck is an exception: it functions like a hero point re-roll but draws from a separate per-session pool rather than consuming an actual hero point
- **Invariant:** each fortune advantage defines a hero-point-activated effect.
- **Invariant:** hero point benefits in this category ignore power level limits.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_065.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_068.md`

### general advantage

- General advantages provide special abilities or passive bonuses not covered by combat, fortune, or skill categories.
- General advantages include: Assessment, Benefit, Diehard, Eidetic Memory, Equipment, Extraordinary Effort, Fearless, Great Endurance, Instant Up, Interpose, Minion, Second Chance, Sidekick, Teamwork, and Trance.
- General advantages often grant immunity effects, passive bonuses to specific checks, or access to additional character resources (Equipment, Minion, Sidekick).
- classifies each member advantage as falling outside the three more specific categories
- grants passive bonuses (e.g., Great Endurance), immunity effects (e.g., Fearless), resource access (Equipment, Minion, Sidekick), or narrative perquisites (Benefit)
- takes effect passively, at character creation, or through explicit character management — never through combat maneuver declaration or hero point spending
- **Invariant:** a general advantage never requires a combat maneuver declaration or a hero point expenditure to take effect.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_065.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_068.md`

### skill advantage

- Skill advantages grant bonuses, modifications, or new capabilities tied to the use of skills.
- Skill advantages include: Agile Feint, Animal Empathy, Artificer, Attractive, Connected, Contacts, Daze, Fascinate, Favored Foe, Hide in Plain Sight, Improvised Tools, Inventor, Jack-of-all-trades, Languages, Ritualist, Skill Mastery, Startle, Taunt, Tracking, and Well-informed.
- Skill advantages often allow a skill to be used in unusual circumstances, substitute one skill for another, or remove penalties for using a skill without proper tools or training.
- classifies each member advantage as affecting skill use rather than combat maneuvers, hero points, or general character resources
- removes training requirements (Jack-of-all-trades), enables pressure-free routine checks (Skill Mastery), or grants circumstance bonuses against specific targets (Favored Foe)
- applies its effect through the skill system — not by modifying attack checks directly or activating through hero point spending
- **Invariant:** a skill advantage always affects the application of skill rules and does not directly modify attack check mechanics or activate through hero point spending.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_065.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_069.md`

*Attack Trade-off* — An Attack Trade-off is a combat advantage that implements the core maneuver trade-off mechanic: the character voluntarily reduces one combat stat by up to 5 to add the same number (up to 5) to another combat stat for that attack. The four Attack Trade-off advantages form a symmetric group covering all four trade-off directions: Accurate Attack trades effect for accuracy; All-out Attack trades defense for accuracy; Defensive Attack trades accuracy for defense; Power Attack trades accuracy for effect. This KA owns the mechanic of deliberately exchanging one combat value for another and enforces the rule that neither the penalty nor the bonus may exceed 5. It interacts with the attack check and active defense (both owned by Combat) but does not own their resolution. The trade-off must always be symmetric: the penalty applied must equal the bonus received, and neither may exceed 5.

### Accurate Attack

- Accurate Attack is a combat advantage that enables a trade-off between effect modifier and attack bonus during an accurate attack maneuver.
- The player may take a penalty of up to -5 on the attack's effect modifier and add that same number (up to +5) to the attack bonus.
- Accurate Attack is used when the character needs to ensure they hit at the cost of dealing less damage or a weaker effect.
- declares a penalty of up to −5 on the effect modifier before the attack roll is made
- applies the same value as a bonus to the attack check for that attack (up to +5)
- enforces that penalty and bonus are equal in magnitude and neither exceeds 5
- resolves only during an accurate attack maneuver — declaration must happen before the attack roll
- **Invariant:** penalty taken must equal bonus gained.
- **Invariant:** neither the penalty nor the bonus may exceed 5.
- **Invariant:** declaration must precede the attack roll.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_066.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_067.md`

### All-out Attack

- All-out Attack is a combat advantage that enables a trade-off between active defenses and attack bonus during an all-out attack maneuver.
- The player may take a penalty of up to -5 on active defenses (Dodge and Parry) and add that same number (up to +5) to the attack bonus.
- All-out Attack suits characters who prioritize landing hits over maintaining their own defenses.
- declares a penalty of up to −5 on both active defenses (Dodge and Parry) before the attack roll
- applies the same value as a bonus to the attack check for that attack (up to +5)
- enforces that penalty and bonus are equal in magnitude and neither exceeds 5
- resolves only during an all-out attack maneuver — declaration must happen before the attack roll
- **Invariant:** penalty and bonus are equal.
- **Invariant:** neither exceeds 5.
- **Invariant:** both Dodge and Parry take the full penalty together.
- **Invariant:** declaration precedes the attack roll.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_066.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_067.md`

### Defensive Attack

- Defensive Attack is a combat advantage that enables a trade-off between attack bonus and active defenses during a defensive attack maneuver.
- The player may take a penalty of up to -5 on the attack bonus and add that same number (up to +5) to both active defenses (Dodge and Parry).
- Defensive Attack is the inverse of All-out Attack: sacrificing offensive power for increased defensive capability.
- declares a penalty of up to −5 on the attack check before the roll
- applies the same value as a bonus to both active defenses (Dodge and Parry) for the round (up to +5)
- enforces that penalty and bonus are equal in magnitude and neither exceeds 5
- resolves only during a defensive attack maneuver — declaration must happen before the attack roll
- **Invariant:** penalty must equal bonus.
- **Invariant:** neither exceeds 5.
- **Invariant:** both Dodge and Parry receive the full bonus as a pair.
- **Invariant:** declaration precedes the attack roll.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_067.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_071.md`

### Power Attack

- Power Attack is a combat advantage that enables a trade-off between attack bonus and effect bonus during a power attack maneuver.
- The player may take a penalty of up to -5 on the attack bonus and add that same number (up to +5) to the attack's effect bonus.
- Power Attack is the inverse of Accurate Attack: sacrificing accuracy for increased damage or effect potency.
- declares a penalty of up to −5 on the attack check before the roll
- applies the same value as a bonus to the effect modifier of the attack (up to +5)
- enforces that penalty and bonus are equal in magnitude and neither exceeds 5
- resolves only during a power attack maneuver — declaration must happen before the attack roll
- **Invariant:** penalty must equal bonus.
- **Invariant:** neither exceeds 5.
- **Invariant:** declaration precedes the attack roll.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_067.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_078.md`

*Combat Enhancement* — A Combat Enhancement is a combat advantage that provides a direct bonus to a specific combat parameter without requiring a trade-off against another stat. These advantages increase combat effectiveness unconditionally when their triggering condition is met. Improved Initiative grants +4 per rank to initiative checks; Improved Critical expands the critical threat range by 1 per rank; Ranged Attack and Close Attack each grant +1 per rank to their respective attack checks (both capped by power level); Favored Environment provides a per-round +2 circumstance bonus to attack or defense that is not power-level-capped. This KA interacts with the attack check and initiative systems owned by Combat, and with the power level cap owned by Character Construction.

### Improved Initiative

- Improved Initiative is a ranked combat advantage that grants a +4 bonus to initiative checks per rank.
- Initiative determines the order of acting in combat; Improved Initiative allows the character to act earlier in the turn order.
- Each rank stacks for a cumulative +4 per rank (e.g., Improved Initiative 2 gives +8 to initiative checks).
- adds +4 per rank to every initiative check without requiring any activation or declaration
- stacks cumulatively: Improved Initiative 2 grants +8, rank 3 grants +12, and so on
- applies automatically to every initiative check for as long as the advantage is held
- **Invariant:** bonus is exactly +4 per rank and applies to all initiative checks without exception.
- **Invariant:** no per-round declaration is needed.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_067.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_075.md`

### Improved Critical

- Improved Critical is a ranked combat advantage that increases the critical threat range with a specific attack by 1 per rank.
- Base critical threat is natural 20; Improved Critical 1 extends this to natural 19-20; maximum threat range of 16-20 with 4 ranks.
- Only a natural 20 is an automatic hit; an attack that misses is not a critical hit even if the roll falls in the threat range.
- Each rank applies to a different attack or increases the threat range of an existing attack by one more.
- The chosen attack type is specified when the advantage is acquired.
- records the specified attack type at acquisition time — the advantage is bound to that attack type
- extends the critical threat range by 1 per rank: base natural 20; rank 1 = 19–20; rank 4 = 16–20 (maximum)
- validates that a roll in the threat range that misses is not treated as a critical hit
- applies automatically to every attack of the specified type — no per-attack declaration required
- **Invariant:** maximum threat range is 16–20 (4 ranks).
- **Invariant:** only natural 20 is an automatic hit.
- **Invariant:** an attack that misses is never a critical hit even within the threat range.
- **Invariant:** advantage is bound to one specified attack type per rank.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_067.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_074.md`

### Ranged Attack

- Ranged Attack is a ranked combat advantage that grants +1 to ranged attack checks per rank.
- The total attack bonus from Ranged Attack is still limited by the series power level.
- Ranged Attack suits characters with broad ranged combat skill across multiple attack types; for a specific ranged attack type, the Ranged Combat skill is preferred.
- adds +1 per rank to all ranged attack checks without targeting a specific attack type
- applies passively to every ranged attack — no declaration or activation required
- remains subject to the series power level cap on total attack bonus
- **Invariant:** total attack bonus including Ranged Attack is always subject to power level cap.
- **Invariant:** bonus applies to all ranged attacks without exception.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_067.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_078.md`

### Close Attack

- Close Attack is a ranked combat advantage that grants +1 to close attack checks per rank.
- The total attack bonus from Close Attack is still limited by the series power level.
- Close Attack suits characters with broad close combat skill (both armed and unarmed); for a specific close attack type, the Close Combat skill is preferred.
- adds +1 per rank to all close attack checks (armed and unarmed) without targeting a specific attack type
- applies passively to every close attack — no declaration or activation required
- remains subject to the series power level cap on total attack bonus
- **Invariant:** total attack bonus including Close Attack is always subject to power level cap.
- **Invariant:** bonus applies to all close attacks without exception.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_067.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_070.md`

### Favored Environment

- Favored Environment is a combat advantage tied to a specific environment (e.g., air, underwater, space, extreme heat, jungles) where the character excels.
- While in the favored environment, the character gains a +2 circumstance bonus to either attack checks or active defenses; the choice is made at the start of each round.
- The +2 circumstance bonus from Favored Environment is not affected by power level limits.
- Examples of favored environments include in the air, underwater, in space, in extreme heat or cold, and in jungles or woodlands.
- recognizes when the character is in their favored environment (air, underwater, space, extreme heat, jungle, etc.)
- requires the character to choose at the start of each round whether the +2 applies to attack checks or to both active defenses
- holds the chosen allocation fixed until the start of the character's next round
- applies passively while in the environment — no action required beyond the round-start allocation choice
- **Invariant:** the +2 bonus is not affected by power level limits.
- **Invariant:** the allocation choice must be made at round start and applies for the full round.
- **Invariant:** the advantage has no effect outside the designated environment.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_067.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_073.md`

*Fortune Activation* — Fortune Activation groups the advantages that use the hero point as their primary activation resource. Each advantage in this KA requires spending a hero point (or operates in the same hero-point economy) to produce a benefit for the character or their allies. The KA owns the interaction between the hero point resource and advantage activation: it defines what happens when a hero point is spent, when the benefit expires, and what restrictions apply. Fortune Activation interacts with the hero point boundary term (owned by Character Construction) but does not define how hero points are earned or reset. All Fortune Activation advantages are categorized as Fortune type. Luck is included here despite not requiring an explicit hero point spend because it mirrors the hero-point re-roll mechanic at a rank-limited rate and belongs to the Fortune type.

### Luck

- Luck is a ranked fortune advantage (maximum rank = half series power level, rounded down) that allows the character to re-roll a die once per round, including adding 10 to re-rolls of 10 or less.
- The character can use Luck a number of times per game session equal to their Luck rank.
- Luck functions like spending a hero point for a re-roll but does not actually cost a hero point.
- Luck ranks refresh when hero points reset at the start of an adventure.
- The GM may adjust the maximum rank limit depending on the series.
- tracks remaining uses for the session; each use consumes one rank from the pool (not a hero point)
- re-rolls one die roll once per round, adding 10 to any re-roll result of 10 or less — same mechanic as a hero point re-roll
- limits session uses to the character's current Luck rank — when the pool is empty, Luck cannot be used
- refreshes the full pool when hero points reset at the start of a new adventure
- **Invariant:** maximum rank is half the series power level rounded down.
- **Invariant:** cannot exceed once per round.
- **Invariant:** pool is empty after rank uses that session.
- **Invariant:** pool refreshes only at adventure start.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_068.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_077.md`

### Inspire

- Inspire is a ranked fortune advantage (maximum rank 5) that grants allies a circumstance bonus to all checks.
- Once per scene, the character spends a hero point and takes a standard action; allies who can interact with the character gain +1 per Inspire rank on all checks until the start of the character's next round.
- The maximum inspiration bonus is +5 (at rank 5); the character themselves does not receive the bonus.
- The inspiration bonus ignores power level limits, like other hero point uses.
- Multiple uses of Inspire do not stack; only the highest bonus applies.
- requires spending a hero point and taking a standard action to activate
- grants +1 per Inspire rank on all checks to all allies who can interact with the activating character, until start of that character's next round
- excludes the activating character — only allies receive the bonus
- enforces a maximum bonus of +5 (Inspire rank is capped at 5)
- **Invariant:** bonus ignores power level limits.
- **Invariant:** the activating character does not receive the bonus.
- **Invariant:** multiple Inspire activations do not stack — only the highest applies.
- **Invariant:** bonus expires at the start of the activating character's next round.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_068.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_076.md`

### Leadership

- Leadership is a fortune advantage that allows the character to remove a condition from an ally.
- As a standard action, the character spends a hero point to remove one of the following conditions from an ally with whom they can interact: dazed, fatigued, or stunned.
- Leadership reflects the character's ability to reassure and lend courage, snapping allies out of debilitating conditions through presence and direction.
- requires spending a hero point and taking a standard action to activate
- selects one ally within interaction range as the target
- removes exactly one of three eligible conditions from that ally: dazed, fatigued, or stunned
- **Invariant:** only the three eligible conditions (dazed, fatigued, stunned) can be removed.
- **Invariant:** the ally must be within interaction range.
- **Invariant:** exactly one condition is removed per activation.
- **Invariant:** no other conditions are eligible.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_068.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_076.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_077.md`

### Beginner's Luck

- Beginner's Luck is a fortune advantage that grants temporary skill ranks by spending a hero point.
- By spending a hero point, the character gains effective 5 ranks in one chosen skill they currently have at 4 or fewer ranks, including skills with no ranks or skills that normally cannot be used untrained.
- The temporary 5 ranks last for the duration of the scene and grant their normal benefits.
- The skill chosen can be any qualifying skill, giving unpracticed characters a brief surge of luck-based proficiency.
- requires spending a hero point to activate; no additional action cost beyond the hero point spend
- selects one skill the character currently has at 4 or fewer ranks (including skills with 0 ranks and normally untrained-restricted skills)
- grants effective rank 5 in that skill for the duration of the current scene
- expires at the end of the scene — temporary ranks do not carry over
- **Invariant:** applies only to skills currently at 4 or fewer ranks.
- **Invariant:** grants exactly effective rank 5 (not +5 to existing rank).
- **Invariant:** lasts exactly for the scene.
- **Invariant:** expires when the scene ends.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_068.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_069.md`

*Character Resource* — A Character Resource is a general advantage that grants the character access to an external asset that exists outside the character's own body but is owned and managed by them. Equipment grants 5 gear points per rank to spend on weapons, armor, vehicles, and headquarters. Minion grants an independent follower with (rank x 15) power points. Sidekick grants a full NPC partner with (rank x 5) power points. Benefit grants a contextual fringe benefit of agreed narrative and mechanical significance. This KA owns the rule that resources are funded by power points and ranks, that they do not earn points autonomously, and that they can be lost, destroyed, or superseded. Character Resources must never duplicate effects purchasable as individual powers at equivalent point cost; they represent access to things, not innate abilities.

### Equipment

- Equipment is a ranked general advantage that grants 5 equipment points per rank to spend on weapons, armor, vehicles, headquarters, and other gear.
- Equipment points purchase gear as defined in the Gadgets & Gear chapter.
- Many heroes rely on Equipment in combination with skills and other advantages as their primary source of power.
- Equipment is not a power; it is subject to the physical world (it can be lost, stolen, or destroyed).
- grants 5 equipment points per rank, accumulating linearly across ranks (rank 3 = 15 equipment points)
- allocates those points to weapons, armor, vehicles, headquarters, and other gear as defined by equipment rules
- treats all purchased gear as physical objects subject to the rules of the physical world — equipment can be lost, stolen, or destroyed
- does not interact with power level limits — equipment is not a power effect
- **Invariant:** equipment points are always 5 per rank.
- **Invariant:** equipment is always subject to loss/theft/destruction.
- **Invariant:** Equipment is never treated as a power effect.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_068.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_071.md`

### Minion

- Minion is a ranked general advantage that grants the character a follower with a power point total of (rank x 15).
- Minions are independent characters subject to normal power level limits; they cannot have minions of their own.
- Minions capable of independent thought are automatically helpful toward their owner; they follow normal minion rules (page 245).
- Minions do not earn power points independently; the character must spend earned power points to increase Minion rank and improve the minion's point total and traits.
- Lost minions are replaced between adventures at the Gamemaster's discretion.
- Minions do not have hero points.
- builds the minion with a power point total of exactly (rank × 15) subject to normal series power level limits
- prevents the minion from having minions of its own
- grants the minion an automatically helpful attitude toward its owner when the minion is capable of independent thought
- requires the character to spend earned power points to increase Minion rank and improve the minion's point total and traits
- replaces a lost minion between adventures at the Gamemaster's discretion — not in-scene
- **Invariant:** minion point total is always exactly rank × 15.
- **Invariant:** minion never has hero points.
- **Invariant:** minion cannot have its own minions.
- **Invariant:** lost minions are replaced between adventures only.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_068.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_077.md`

### Sidekick

- Sidekick is a ranked general advantage that grants the character a partner/aide built with (rank x 5) power points, subject to series power level.
- A sidekick's power point total must be less than the character's own total.
- Sidekicks are NPCs but are automatically helpful and loyal; the GM normally allows the player to control their sidekick.
- Sidekicks are not minions: they are full-fledged characters not subject to minion rules.
- Sidekicks do not earn power points; the character spends earned points to increase Sidekick rank, granting 5 additional power points per rank increase.
- The character can spend hero points on the sidekick's behalf with the usual benefits; sidekicks themselves do not have hero points.
- builds the sidekick with a power point total of exactly (rank × 5), subject to series power level
- requires the sidekick's total power points to always remain less than the character's own total
- allows the character to spend hero points on the sidekick's behalf with normal hero point benefits
- requires the character to spend earned power points to increase Sidekick rank, adding 5 power points per rank increase
- does not apply minion rules to the sidekick — the sidekick is a full character under shared GM/player control
- **Invariant:** sidekick total must always be less than owner's total.
- **Invariant:** sidekick has no hero points of its own.
- **Invariant:** sidekick is never subject to minion rules.
- **Invariant:** hero points spent on the sidekick's behalf come from the owner's pool.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_068.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_079.md`

### Benefit

- Benefit is a ranked general advantage representing a significant perquisite or fringe benefit agreed between the player and the GM.
- The benefit should not exceed the value of any other advantage or a power effect costing 1 point; it must be significant enough to justify at least 1 power point.
- Sample benefits include: Alternate Identity, Ambidexterity, Cipher, Diplomatic Immunity, Security Clearance, Status, and Wealth.
- Benefits can be taken in ranks for improved levels of the same benefit.
- Routine professional credentials (e.g., law or medicine licenses) do not qualify; they are considered training and have no significant game effect.
- The GM is the final arbiter of what constitutes a Benefit in the series.
- negotiates the specific benefit with the GM before finalizing — both sides must agree on what the benefit represents
- validates that the benefit does not exceed the value of any other advantage or a 1-point power effect
- validates that the benefit is significant enough to justify at least 1 power point cost
- allows multiple ranks for escalating versions of the same benefit
- rejects routine professional credentials — a law or medicine license has no significant game effect and never qualifies
- **Invariant:** GM has final approval authority.
- **Invariant:** benefit value ceiling is any other advantage or a 1-point power effect.
- **Invariant:** routine credentials never qualify.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_068.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_069.md`

*Skill Enhancement* — A Skill Enhancement is a skill advantage that modifies the scope, reliability, or reach of a character's skill use without being tied to a specific single skill instance. Skill Mastery makes one chosen skill reliable under pressure. Jack-of-all-trades makes every skill accessible without training (while still requiring tools). Favored Foe applies a +2 circumstance bonus across four skill checks when facing a specific opponent type. All three are classified as Skill advantages and interact with the Skill module's check system, but they do not define the skills themselves. Skill Enhancement advantages are not power-level-capped. Each must operate on a defined scope: one chosen skill (Skill Mastery), all skills universally (Jack-of-all-trades), or all checks against a specific foe type (Favored Foe).

### Skill Mastery

- Skill Mastery is a skill advantage that allows the character to make routine checks with one chosen skill even under pressure.
- Normally, routine checks cannot be made under pressure; Skill Mastery removes that restriction for the chosen skill.
- Skill Mastery does not allow routine checks with skills that categorically do not permit routine checks regardless of conditions.
- The advantage may be taken multiple times, each time applying to a different skill.
- removes the restriction that routine checks cannot be made under pressure, but only for the designated skill
- records the chosen skill at acquisition — each instance applies to a different skill
- does not enable routine checks for skills that categorically prohibit routine checks regardless of conditions
- can be acquired multiple times, each time selecting a different qualifying skill
- **Invariant:** applies only to the specifically designated skill.
- **Invariant:** does not override categorical prohibitions on routine checks.
- **Invariant:** designated skill is fixed at acquisition.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_069.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_080.md`

### Jack of all Trades

- Jack-of-all-trades is a skill advantage that allows the character to use any skill untrained, including skills and aspects of skills that normally cannot be used without training.
- The character must still have proper tools if a skill requires them; Jack-of-all-trades removes the training barrier only, not the tool requirement.
- This advantage is broadly applicable across all skill domains, making the character a versatile generalist.
- removes the restriction that certain skills or skill aspects require training before they can be used
- maintains tool requirements — if a skill requires tools, those tools are still needed even with this advantage
- applies passively and globally — no per-skill or per-check activation required
- **Invariant:** tool requirements still apply and are never waived by this advantage.
- **Invariant:** training restriction is fully removed for all skills.
- **Invariant:** no activation is required.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_069.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_076.md`

### Favored Foe

- Favored Foe is a skill advantage granting +2 circumstance bonus to Deception, Intimidation, Insight, and Perception checks against a specific type of opponent.
- The opponent type is specified when the advantage is acquired and can be a creature type (aliens, animals, undead, etc.) or a profession (soldiers, Yakuza, etc.) approved by the GM.
- Broad categories such as "humans" or "villains" are not permitted as favored foes.
- The +2 circumstance bonus from Favored Foe is not limited by power level.
- records the favored foe type at acquisition: a creature type (aliens, animals, constructs, mutants, undead) or a profession (soldiers, police, Yakuza) approved by the GM
- enforces that the type is not excessively broad — categories like "humans" or "villains" are not permitted
- grants +2 circumstance bonus to Deception, Intimidation, Insight, and Perception checks when those checks involve the favored foe
- does not apply to checks against targets that are not of the favored foe type
- **Invariant:** +2 bonus is not subject to power level limits.
- **Invariant:** foe type must be specific enough to receive GM approval.
- **Invariant:** bonus applies to exactly the four listed skills.
- **Invariant:** does not apply outside qualifying interactions with the favored foe.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_069.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_073.md`

*Boundary terms* — Terms this module uses but does not define; each is owned by another module and appears here only as advantages read or spend it.

### hero point

- Hero points are a game resource spent to activate fortune advantages (Inspire, Leadership, Beginner's Luck, Seize Initiative, Ultimate Effort), enhance Luck re-rolls, and fund Sidekick actions.
- Fortune advantages define their effects in terms of spending a hero point as the activation cost.
- Hero points reset at the start of each adventure, which also refreshes Luck ranks.
- consumed by fortune advantages (Inspire, Leadership, Beginner's Luck) as the activation cost for their effects
- proxied by Luck for re-roll effects — Luck draws from its own per-session pool rather than consuming an actual hero point
- bypasses power level limits when funding Inspire's bonus — a property of hero point benefits generally
- **Invariant:** hero points are owned by Character Construction.
- **Invariant:** this module consumes them but never generates or refreshes them.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_068.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_077.md`

### power point

- Power points are the resource spent to purchase advantage ranks at character creation and advancement; the cost is 1 power point per rank.
- Power points also fund Minion and Sidekick improvements: the character spends earned power points to increase their rank in these advantages.
- funds advantage acquisition at 1 power point per rank for all advantages in this module
- funds rank increases for Minion and Sidekick out of the character's earned power points pool
- **Invariant:** power points are owned by Character Construction.
- **Invariant:** this module spends them but never generates them.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_065.md`

### power level

- Power level is the series cap that limits total attack bonus and active defense values, including those gained from ranked combat advantages such as Close Attack and Ranged Attack.
- Luck's maximum rank is capped at half the series power level (rounded down).
- Power level limits do not apply to circumstance bonuses from Favored Environment or Favored Foe.
- caps total attack bonus (including bonuses from Ranged Attack and Close Attack advantages) at the series power level
- limits Luck's maximum rank to half the series power level (rounded down)
- does not cap circumstance bonuses from Favored Environment or Favored Foe — those explicitly ignore power level limits
- **Invariant:** power level cap applies to attack bonuses from ranked attack advantages.
- **Invariant:** Luck rank cap is always half PL rounded down.
- **Invariant:** circumstance bonuses from Favored Environment and Favored Foe are always exempt from the cap.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_070.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_077.md`

### attack check

- Attack checks are the rolls used during combat maneuvers; combat advantages modify their bonuses or penalties.
- Accurate Attack, All-out Attack, Power Attack, and Defensive Attack all apply adjustments directly to the attack check modifier.
- Close Attack and Ranged Attack each add a flat bonus to the relevant type of attack check.
- receives bonus adjustments from Ranged Attack (+1/rank) and Close Attack (+1/rank), both subject to power level cap
- receives penalty or bonus adjustments during trade-off maneuvers: Accurate Attack, All-out Attack, Defensive Attack, Power Attack each apply −N or +N to the attack check
- receives optional +2 circumstance bonus from Favored Environment when the player chooses attack allocation at round start
- **Invariant:** attack checks are owned by Combat.
- **Invariant:** this module modifies their bonus values through advantage rules but does not resolve the check.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_067.md`

### active defense

- Active defenses (Dodge and Parry) are the defenses adjusted by combat advantage trade-offs: All-out Attack reduces them, Defensive Attack raises them.
- Defensive Roll adds bonus Toughness as an active defense that is lost when the character is vulnerable or defenseless.
- Favored Environment's +2 bonus can optionally apply to active defenses rather than attack.
- receives penalty adjustments from All-out Attack (−N to both Dodge and Parry, symmetric with attack bonus)
- receives bonus adjustments from Defensive Attack (+N to both Dodge and Parry, symmetric with attack penalty)
- receives optional +2 circumstance bonus from Favored Environment when the player chooses defense allocation at round start
- **Invariant:** active defenses are owned by Combat.
- **Invariant:** this module modifies them through advantage rules but does not resolve defense checks.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_071.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_073.md`

### extra effort

- Extra effort is a general mechanic allowing characters to push beyond their normal limits; Extraordinary Effort modifies how extra effort works, granting two benefits instead of one at the cost of doubled fatigue.
- Spending a hero point at the start of the following turn reduces the cost of extraordinary effort from exhausted to merely fatigued.
- doubles the normal benefits of extra effort (two benefits instead of one, including stacking the same type twice)
- doubles the fatigue cost (character becomes exhausted instead of fatigued, starting the turn after)
- prevents use when already exhausted
- allows reduction of the doubled fatigue cost back to normal (fatigued) by spending a hero point at the start of the following turn
- **Invariant:** extra effort mechanics are owned by Combat.
- **Invariant:** Extraordinary Effort modifies benefit count and fatigue cost but not what benefits are available.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_072.md`
