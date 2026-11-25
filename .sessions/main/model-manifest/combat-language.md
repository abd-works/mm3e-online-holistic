## Language

*Turn Structure* — Turn Structure is the time-and-sequence framework that governs who acts when and what they can do. The action round is the six-second unit of in-game time; initiative determines the order within each round; and a character's turn is the slot in that order where they act. Turn Structure owns the full action economy: the allotment of one standard and one move action per turn (or two move actions), the unlimited but GM-arbitrated free actions, and the reactive right to spend reactions whenever circumstances demand. Delay and Ready extend the framework temporally — Delay defers a turn to a later slot while Ready prepays a future reaction — enabling characters to coordinate and respond across the initiative sequence. Turn Structure interacts with all other KAs: Attack Resolution and Combat Maneuvers consume standard actions; tactical choices (Delay, Ready, Defend) consume actions to create positional or temporal advantages. The invariant is that no character may act outside their turn except via free actions and reactions, and no action can exceed its defined cost without an explicit extra effort or other modifier.

### initiative

- Initiative determines the order in which characters take their turns during a conflict.
- Base initiative modifier equals the character's Agility rank; advantages (e.g., Improved Initiative) and powers can modify it further.
- At the start of a conflict each character rolls d20 + initiative modifier; the turn order counts down from highest result to lowest.
- Ties are broken first by highest Dodge bonus, then highest Agility, then highest Awareness; if still tied, tied players each roll a die with the highest going first.
- The GM may roll a single initiative check for an entire group of minions, giving them all the same result.
- Characters who enter a conflict after it begins roll initiative when they join and act when their turn comes up in the existing order.
- Computes the conflict's turn order as a descending list from highest result to lowest at the start of each conflict.
- Inserts newly-arriving characters into the existing order at the result they roll when they join.
- **Invariant:** Every character in a conflict has exactly one initiative position; that position persists across rounds unless modified by delay or ready.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_196.md`

### action round

- An action round (round) is a six-second segment of in-game time used when turn order and action economy matter.
- During a round each character involved takes one turn — that character's opportunity to act.
- A round represents approximately one page of a comic book — just long enough for the group to each do one thing.
- Rounds structure conflicts, challenges, and any situation where sequence and action limits are important.
- Advances to the next round once every character in the initiative order has completed their turn.
- Serves as the atomic time unit against which effect durations ("until start of your next turn", "until end of your turn") are measured.
- **Invariant:** Every declared action occurs within a round — no action is resolved outside the round structure.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_016.md`

### turn

- A turn is a character's portion of an action round — the window in which that character declares and resolves their actions.
- When a character's turn begins, effects that last "until the start of your next turn" end.
- When a character's turn ends, effects that last "until the end of your turn" end and required resistance checks for ongoing effects are made.
- A character informs the GM when their turn is finished so the next character in initiative order may act.
- Opens by cleaning up "start of turn" expiring effects, then accepts action declarations.
- Closes by cleaning up "end of turn" expiring effects, then fires mandatory ongoing-effect resistance checks.
- Provides the temporal frame within which free actions are valid — free actions cannot occur outside a character's own turn.
- **Invariant:** A character has exactly one turn per round (extra effort can add one more action within the same turn, not a second turn).
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_197.md`

### standard action

- A standard action allows a character to do something meaningful: attack, use a skill, activate a power or advantage, or perform a similar task.
- Each character is limited to one standard action per turn.
- A standard action may be exchanged for an additional move action (two move actions instead of one standard + one move).
- Special actions (aim, charge, defend, disarm, grab, feint, recover, ready, trip) are standard actions.
- Permits one of: attack check, skill check, power activation, or any named special action (the Combat Maneuvers KA lists these).
- Consumed at declaration; no refund for a failed action.
- **Invariant:** Only one standard action per turn; extra effort can grant one additional standard action.

### move action

- A move action allows a character to move up to their speed rank or perform an equivalent activity (draw/stow an item, stand up, pick up an object).
- In a normal turn a character gets one standard action and one move action; the move may come before or after the standard action.
- A standard action may be exchanged for an additional move action, enabling two move actions in one turn.
- Actions cannot normally be split — a character may not move part of their speed, take a standard action, then move the remainder.
- A DC 15 Athletics check as a free action can increase ground speed rank by +1 for one round on one or more degrees of success.
- Covers both physical displacement (moving up to speed rank) and equivalent physical tasks (drawing a weapon, standing from prone).
- May be taken before or after the standard action, but not split around it.
- **Invariant:** Only one move action per turn unless the standard action is exchanged for a second move action.

### free action

- A free action consumes so little time it is considered to take no real time over the span of a round.
- A character may perform as many free actions per turn as the GM considers reasonable.
- Examples: dropping an object, dropping prone, speaking a sentence or two, ceasing to concentrate on a power, maintaining a grab.
- Free actions are a conscious choice made on the character's own turn; they cannot occur when it is not the character's turn (reactions serve that role).
- Executes alongside any other action without consuming standard or move action budget.
- **Invariant:** Free actions only occur on the character's own turn; off-turn interventions use the reaction mechanism instead.

### reaction

- A reaction is a response to something else happening during the round; it can occur even when it is not the character's turn.
- Reactions take no significant time and do not count against the character's normal action allotment.
- A character can react as often as circumstances dictate, but only when circumstances dictate.
- Spending a hero point is a reaction.
- Examples: taking a readied action when triggered, counter-disarming after losing a melee disarm, firing a netline after declaring a ready.
- Fires outside the character's own turn in response to a triggering event.
- Does not consume or replace the character's standard, move, or free action budget.
- **Invariant:** Reactions fire only when circumstances trigger them; they cannot be voluntarily taken at any time like free actions.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_017.md`

### delay

- Delay is a no-action choice to defer one's entire turn to later in the initiative order.
- A character cannot delay after having already taken an action on their turn, or if unable to take actions.
- After any other character acts, the delayed character may choose to act; their initiative slot moves to where they acted.
- If the trigger never fires before the character's original initiative comes up next round, the delayed turn is lost and initiative stays put.
- Beneficial effects that last until end of turn expire when the character delays; harmful effects persist until after the character acts.
- Removes the character from the current initiative slot and holds them in reserve for later activation.
- Transfers the initiative position to the point of insertion when the character chooses to act.
- **Invariant:** Cannot delay after any action has been taken on the current turn, and cannot delay if unable to take actions.
- **Invariant:** The delayed turn is lost if not taken before the same initiative position arrives in the next round.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_211.md`

### ready

- Ready is a standard action that prepares a single standard, move, or free action to trigger on a specified future condition.
- The character declares the action and triggering circumstances; the readied action fires as a reaction when conditions are met.
- When the readied action fires, the character's initiative slot moves to where they acted.
- If the trigger does not occur before the character's next initiative, the readied action is lost; the same action may be readied again.
- Packages an action with a trigger condition for deferred execution as a reaction.
- Shifts the character's initiative position to the point where the readied action fires.
- **Invariant:** Only one readied action at a time; the character may ready the same action again on a subsequent turn if the trigger never fired.
- **Invariant:** The readied action is automatically lost if the character's next initiative comes up without the trigger firing.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_213.md`

*Attack Resolution* — Attack Resolution is the sequence that determines whether an attack lands and with what force. The attack check is the gatekeeper — rolling d20 + attack bonus against the target's defense class to produce a hit or miss; a natural 20 extends to a potential critical hit while a natural 1 always misses. Defense class is calculated from the applicable active defense (Parry for close, Dodge for ranged) plus 10, and is modified by conditions, concealment, and cover. The attack bonus aggregates Fighting or Dexterity, skill ranks, and circumstance modifiers (including maneuver trade-offs). Close and ranged attacks are the two fundamental attack types that differ by range and which defense they target. Critical hits extend the resolution: when a natural 20 produces a total that beats the defense class, the attacker chooses from three amplified outcomes. Aim and charge are action-phase modifiers that feed into the attack check. Attack Resolution owns the rules that determine whether an attack connects; it does not own damage outcomes (those belong to Damage and Resistance) or the conditions imposed by effects (owned by Check Resolution).

### attack check

- An attack check determines whether an attack hits: d20 + attack bonus vs. target's defense class; equal or exceeding means a hit.
- A natural 20 on the d20 always hits regardless of defense and may be a critical hit.
- A natural 1 on the d20 always misses regardless of the total.
- Area and perception-range effects do not require attack checks; they automatically affect the target or area and cannot score critical hits or misses.
- Produces a binary hit/miss result that gates all further resolution (damage, conditions, effects).
- Extends to a critical hit determination when the d20 result is exactly 20.
- **Invariant:** d20 result of 1 always misses; d20 result of 20 always hits regardless of totals.
- **Invariant:** Area and perception-range attacks bypass this check entirely — no attack bonus, no defense class comparison.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_016.md`

### attack bonus

- The attack bonus is the modifier added to the d20 roll when making an attack check.
- For most characters it is based on Fighting (close attacks) or Dexterity (ranged attacks) plus applicable Close Combat or Ranged Combat skill ranks plus circumstance modifiers.
- Maneuvers (Accurate Attack, All-out Attack, Defensive Attack, Power Attack) can temporarily shift the attack bonus in exchange for other trade-offs.
- Conditions and tactical circumstances (aim bonus, charge penalty, concealment, cover) apply as circumstance modifiers.
- Aggregates all static and circumstance modifiers into a single value added to d20 for the attack check.
- Shifts temporarily when a maneuver trade-off is declared before the attack check.
- **Invariant:** Cannot be reduced below +0 by maneuver penalties (all maneuvers have this floor constraint).
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_214.md`

### defense class

- The defense class is the difficulty number an attack check must equal or exceed to hit: Defense Class = defense rank + 10.
- Close attacks target Parry; ranged attacks target Dodge; certain attacks may target other defenses.
- Vulnerable halves active defense ranks (round up); defenseless reduces active defense ranks to 0 making the base DC just 10.
- Attackers may make attack checks against defenseless targets as routine checks (auto-hit with bonus ≥ 0).
- Represents the minimum attack check result required to hit a specific character with a specific attack type.
- Recalculates dynamically when active defense ranks change (vulnerable, defenseless conditions).
- **Invariant:** Defense Class = active defense rank + 10; applies independently per attack type (close vs. ranged).
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_208.md`

### close attack

- A close attack targets a character within physical reach (by touch or melee weapon) and is checked against the target's Parry defense.
- Strength-based damage (unarmed, melee weapons) is close range by default.
- Close attacks can score critical hits; many maneuvers (charge, trip, disarm, grab) are close attacks.
- Selects Parry as the target defense, making Fighting rank the primary attack modifier.
- Enables all physical contact maneuvers (grab, trip, disarm, slam); ranged attacks cannot trigger these maneuvers.
- **Invariant:** Target must be within physical reach; attacks beyond reach require a ranged attack type.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_206.md`

### ranged attack

- A ranged attack targets a character at a distance and is checked against the target's Dodge defense.
- Short range (rank × 25 ft): no penalty; medium (rank × 50 ft): −2 circumstance; long (rank × 100 ft): −5 circumstance; beyond long range the target is out of range and cannot be attacked.
- Perception-range attacks automatically hit without an attack check and cannot score critical hits or misses.
- Modifiers affecting the attack check (including maneuvers) do not apply to area or perception effects.
- Selects Dodge as the target defense; applies distance modifiers based on range bands.
- Degrades accuracy at medium and long range through circumstance penalties to the attack check.
- **Invariant:** Cannot target beyond long range (rank × 100 ft); targets outside this range are simply out of range.
- **Invariant:** Perception-range attacks bypass this entire check — they automatically affect targets with no attack roll.

### critical hit

- A critical hit occurs when the attack check rolls a natural 20 and the total also equals or exceeds the target's defense class.
- A natural 20 that does not beat the defense class is still a hit but not a critical hit.
- On a critical hit the attacker chooses one of three effects: Increased Effect (+5 resistance DC), Added Effect (bonus rank-0 secondary effect), or Alternate Effect (temporary power stunt at no fatigue cost).
- Against a minion, Increased Effect bypasses the resistance check entirely — the minion automatically receives the worst degree.
- Improved Critical advantage extends the threat range below natural 20; auto-hit only occurs on a natural 20.
- Area and perception effects cannot score critical hits.
- Extends a natural-20 hit into one of three amplified outcome options chosen by the attacker.
- Applies the Increased Effect option against minions with an instant-defeat bypass rule.
- **Invariant:** Confirmation requires both natural 20 AND total ≥ defense class; missing the defense class on a natural 20 is a normal hit only.
- **Invariant:** Area and perception-range attacks can never produce critical hits.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_203.md`

### aim

- Aim is a standard action that lines up a subsequent attack, granting a circumstance bonus on the following attack check.
- Close attack or ranged attack at close range: +5 circumstance bonus; ranged attack at greater distance: +2 circumstance bonus.
- The attacker is vulnerable while aiming.
- A free action maintains aim before making the attack; losing the ability to maintain aim cancels the bonus.
- The very next action after aiming must be the attack; any other action cancels the aim bonus.
- Trades the current turn's standard action for a circumstance bonus to the immediately following attack check.
- Applies vulnerable condition to the aiming character from the moment aim is declared until the attack is made.
- **Invariant:** The aim bonus is lost if any action other than the declared attack occurs next.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_210.md`

### charge

- Charge is a standard action: the attacker moves their speed rank in a straight line toward a target, then makes a close attack at the end of movement with a −2 circumstance penalty.
- Combined with a move action, the attacker can move up to twice their speed rank before attacking.
- Charge enables the slam attack maneuver.
- Combines movement and a close attack into a single standard action at a −2 attack check penalty.
- Extends movement range when combined with a move action (up to 2× speed rank total).
- Enables the slam attack variant when the attacker chooses to use momentum as the damage source.
- **Invariant:** Movement must be in a relatively straight line toward the target; cannot charge a target not in line-of-movement.

*Damage and Resistance* — Damage and Resistance is the system that determines the consequence of a landed attack and the pathway from unharmed through degradation to incapacitation, dying, and death. The Damage effect is the primary weapon of combat — when a hit is scored the target makes a Toughness resistance check against a DC of damage rank + 15. Degrees of failure accumulate penalties and impose conditions: a single miss begins a cumulative −1 Toughness penalty; two degrees add dazed; three degrees add staggered; four degrees incapacitate. The incapacitated state exposes the target to the dying sequence, and another failure while dying kills. Toughness resistance is the specific check that governs this, distinct from the generic resistance check used for other effects (Affliction, ongoing hazards). Recovery undoes this progression — living targets heal one damage condition per minute of rest, and the Recover action accelerates this in-conflict. The recovery check is the per-turn automatic roll that ends ongoing effects. This KA owns the damage progression from hit to death and the full recovery arc back to normal.

### resistance check

- A resistance check resists a power effect or hazard: d20 + defense bonus vs. resistance DC (typically effect rank + 10).
- Resistance checks are not actions — they represent involuntary responses and do not consume action allotment.
- Resistance checks may be graded: different degrees of failure impose progressively worse outcomes.
- Ongoing effects require a resistance check at the end of each of the target's turns; success ends the effect and removes conditions.
- The Recover action grants an additional resistance check against an ongoing effect beyond the normal end-of-turn check.
- Fires automatically at end of each turn for ongoing effects without requiring any action.
- Grades its result by degree of failure to determine which condition or penalty is imposed.
- **Invariant:** d20 + defense bonus vs. effect rank + 10 (Damage uses effect rank + 15).
- **Invariant:** Success on the resistance check against an ongoing effect ends that effect and removes all its conditions.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_016.md`

### damage

- Damage is a power effect applied by a successful attack; the target makes a Toughness resistance check against DC = damage rank + 15.
- Failure degrees: one degree → −1 cumulative Toughness penalty; two degrees → dazed + −1 penalty; three degrees → staggered + −1 penalty (if already staggered, apply fourth degree); four degrees → incapacitated.
- Toughness check penalties from repeated failures are cumulative across all hits.
- An incapacitated target that fails another Toughness check becomes dying; a dying target that fails becomes dead.
- Strength provides a built-in close-range Damage effect; Strength-based weapons add Strength rank + Damage rank together.
- Accumulates a −1 penalty on every Toughness resistance check, regardless of degree of failure.
- Escalates character state through a four-degree chain: penalty only → dazed → staggered → incapacitated.
- Chains further into dying and then dead when the incapacitated character continues to receive damage.
- **Invariant:** Damage resistance DC is always damage rank + 15.
- **Invariant:** Cumulative penalty persists until the character recovers; it stacks across all attackers.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_203.md`

### Toughness resistance

- Toughness resistance is the specific resistance check against a Damage effect: d20 + Toughness rank vs. damage rank + 15.
- Every failure imposes a −1 cumulative circumstance penalty to all future Toughness resistance checks for that character.
- The penalty stacks across multiple hits and across different attackers within a scene.
- Impervious Toughness ignores Damage effects below a threshold rank equal to half the Impervious rank.
- Living targets recover Toughness penalties by removing one damage condition per minute of rest.
- Specializes the resistance check for Damage effects with a higher DC formula (rank + 15 instead of rank + 10).
- Tracks a running cumulative penalty that degrades future Toughness checks until the character recovers.
- **Invariant:** Penalty is cumulative — each failure adds another −1 regardless of degree.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_216.md`

### dying

- Dying is the near-death state entered when an incapacitated character suffers further Toughness failure, or when certain hazards reach their final stage.
- A dying character who fails another Toughness resistance check against damage dies.
- A dying character cannot stabilize from suffocation or vacuum until able to breathe/reach normal atmosphere.
- Death of major characters requires an active second effort; accidental single-roll death is near-impossible for main characters.
- Minions can be killed outright when a player declares intent to kill and the attack succeeds.
- Lasting injuries and death are handled as complications for narrative continuity.
- Sits at the terminal end of the damage escalation chain: incapacitated → dying → dead.
- Blocks self-stabilization when the cause (lack of air, vacuum) persists.
- Protects major characters from accidental death by requiring a second active harmful action after incapacitation.
- **Invariant:** Another Toughness resistance failure while dying results in death.

### incapacitated

- Incapacitated is the condition imposed by four degrees of failure on a Toughness resistance check (defenseless + stunned + unaware; character typically falls prone).
- An incapacitated target that fails another Toughness resistance check transitions to dying.
- Incapacitation can also result from suffocation, vacuum exposure, or other hazard escalation.
- While incapacitated the character cannot act (stunned) and has no active defenses (defenseless).
- Combines three conditions simultaneously: defenseless (no active defense), stunned (no actions), and unaware.
- Serves as the gateway state that, on further damage, leads to dying.
- Can be reached by damage (4 degrees failure) or by hazards (suffocation, vacuum).
- **Invariant:** While incapacitated: cannot act, defense class = 10, attackers may use routine checks.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_202.md`

### recovery check

- A recovery check is a resistance check made to end an ongoing condition or effect; it is not an action.
- At the end of each of the character's turns, a resistance check is automatically made against any ongoing effect.
- The Recover action (standard action, once per conflict) grants an additional resistance check beyond the normal end-of-turn check.
- Natural recovery: living targets remove one damage condition per minute of rest, working from the worst condition back toward normal.
- Healing and Regeneration effects can speed this process.
- Fires automatically at the end of each turn as part of the turn's closing sequence.
- Produces a binary result: success removes the ongoing effect and all its conditions; failure keeps them.
- Complements the once-per-conflict Recover action which grants one additional check on top of the automatic one.
- **Invariant:** Automatic recovery check costs no action; the Recover action grants an extra check at the cost of the full standard action for that turn.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_207.md`

### recover

- Recover is a standard action requiring the character's entire turn; usable only once per conflict.
- On recovery: remove the highest current level of damage or fatigue; alternatively make an additional resistance check against one ongoing effect (beyond the normal end-of-turn check).
- Recovery also grants +2 to active defenses until the start of the character's next turn.
- Remaining damage, fatigue, or effects after using recover must heal normally (rest or outside assistance).
- Removes the worst current damage condition or fatigue level in a single standard-action turn.
- Grants a defensive bonus (+2 active defenses) until start of next turn as a secondary benefit.
- **Invariant:** Once per conflict — the once-per-conflict limit cannot be reset during a scene.

*Combat Maneuvers* — Combat Maneuvers are the specialized standard-action tactics that produce outcomes beyond a simple hit — disabling, restraining, toppling, misdirecting, or buffeting opponents. Each maneuver modifies the standard attack resolution sequence with a specific check chain: disarm and trip each use an attack check followed by an opposed secondary check; grab uses an attack check followed by a resistance check; feint replaces the attack check with a skill check to impose a condition; slam attack modifies the damage formula of a charge; and defend replaces an attack with a defensive opposed roll. Maneuvers are optional additions to declared actions; the GM decides if circumstances permit a given maneuver. None of the maneuvers directly deal Toughness damage by themselves (except slam attack, which adds a damage bonus); their primary purpose is to impose conditions (prone, restrained, bound, vulnerable) or change the tactical situation. Combat Maneuvers depend on Attack Resolution for the initial hit determination and on Damage and Resistance for damage outcomes when applicable.

### defend

- Defend is a standard action: the character focuses on avoiding attacks rather than attacking.
- The defender makes an opposed check of their active defense (Parry or Dodge) vs. each attack made on them until the start of their next turn.
- Any defend roll result of 10 or lower is treated as 10 (same as hero point re-roll floor), ensuring a minimum effective result of 11.
- An attacker must equal or exceed the defender's opposed check result — not merely the normal defense class.
- Replaces the standard attack with an active defense roll that supersedes the normal static defense class.
- Applies a floor of 10 to all defend rolls, guaranteeing the defender at least a result of 11 against every attack.
- **Invariant:** Attacker must match the defender's opposed result, not just the base Defense Class = defense + 10.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_211.md`

### disarm

- Disarm is a standard action to knock an item out of an opponent's grasp.
- Attack check vs. the defender: −2 penalty for close disarm; −5 for ranged disarm.
- If the attack hits: opposed check of attack's damage rank vs. defender's Strength; win → defender drops the item.
- An unarmed disarm success allows grabbing the dropped item as a free action.
- If the attacker used a melee weapon and loses the opposed check, the defender may immediately counter-disarm as a reaction.
- Executes a two-check sequence: attack check (to hit) then opposed damage vs. Strength (to disarm).
- Differentiates between unarmed and weapon disarms in both penalties and counter-disarm exposure.
- **Invariant:** −2 close penalty, −5 ranged penalty applied before the attack check.

### grab

- Grab is a standard action to seize and restrain a target: attack check vs. target; on a hit the target resists with the better of Strength or Dodge vs. attacker's Strength or grab effect rank.
- One degree of success: target is restrained (immobile and vulnerable).
- Two or more degrees: target is bound (defenseless, immobile, and impaired).
- The attacker is hindered and vulnerable while maintaining the grab; maintaining is a free action each turn.
- After the grab is established, the attacker may take a standard action to inflict Strength damage on the grabbed target on subsequent turns.
- An existing hold can be improved with another grab action; cumulative degrees of success but losing frees the target.
- The attacker may drag a restrained or bound target: target resists with Strength vs. attacker's Strength; failure means target moves with attacker.
- A grabbed target may attempt to escape as a move action.
- Runs an attack check then a resistance check to determine hold degree: restrained (1 degree) or bound (2+ degrees).
- Imposes a reciprocal cost: the attacker is hindered and vulnerable while the hold is maintained.
- Enables follow-on damage and dragging as separate subsequent actions after the grab is established.
- **Invariant:** Maintaining the hold requires a free action each turn; missing the free action releases the target automatically.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_212.md`

### trip

- Trip is a standard action (close attack vs. target's Parry at −2 circumstance penalty) to knock a target prone.
- If the attack hits: opposed check of Acrobatics or Athletics (better of each) between attacker and defender.
- Attacker wins → defender falls prone in an adjacent area of the attacker's choice.
- Attacker loses → defender may immediately attempt to counter-trip; if that fails, the attempt ends.
- Runs a two-check sequence: attack check (−2 vs. Parry) then opposed Acrobatics/Athletics.
- Produces the prone condition on the target, creating tactical disadvantage.
- **Invariant:** Counter-trip triggers only when the attacker LOSES the opposed check, not when they miss the initial attack.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_214.md`

### feint

- Feint is a standard action using Deception to mislead an opponent in combat.
- The feinting character makes a Deception check opposed by the better of the target's Deception or Insight.
- Success leaves the target vulnerable against the feinter's next attack until the end of the feinter's next round.
- Replaces the attack check with a skill check (Deception) to produce the vulnerable condition rather than damage.
- Imposes vulnerable for a limited duration (until end of feinter's next round), enabling a follow-up attack at increased effectiveness.
- **Invariant:** Feint produces vulnerable on the target, not damage; it is always used to set up a subsequent attack.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_215.md`

### slam attack

- Slam attack is a maneuver used during a charge, trading personal risk for greater damage.
- Damage rank = max(speed rank, normal damage rank + 1); add +1 more if the attacker moved their full speed before charging.
- The GM may cap base slam damage at the series power level before circumstance modifiers.
- The attacker must make a Toughness resistance check against half the slam attack's damage rank (rounded down).
- Appropriate Immunity effects protect the attacker from slam damage they inflict.
- Replaces the normal damage rank calculation with a speed-based or boosted formula during charge.
- Imposes a reciprocal Toughness check on the attacker at half the damage rank.
- **Invariant:** Attacker always risks half the slam damage to themselves; Immunity can negate this.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_216.md`

*Tactical Environment* — Tactical Environment encompasses the contextual factors that modify combat outcomes without being actions themselves: concealment, cover, surprise, minion rules, and the mechanics for combining attackers (team attack, combined attack). Concealment and cover are passive modifiers applied by the GM based on the scene — both impose circumstance penalties to attack checks, with the important distinction that concealment impairs perception while cover impairs attack trajectory. Surprise reshapes the opening of a conflict, granting the non-surprised side an action window and making the surprised side vulnerable. Minions are a scaling device — the GM uses them to model hordes of weaker opposition with simplified rules that accelerate combat. Team attack and combined attack give multiple combatants a cooperative option to overcome targets whose individual resistance would be too high to crack. Tactical Environment interacts primarily with Attack Resolution (all modifiers flow into attack checks or defense class) and with Damage and Resistance (minion defeat, combined attack damage output).

### concealment

- Concealment applies when an attacker cannot clearly perceive their target with an accurate sense.
- Partial concealment (dim lighting, foliage, fog, smoke): −2 circumstance penalty to attack checks.
- Total concealment (complete darkness, heavy smoke): −5 circumstance penalty; attacker must know or guess the approximate area to target at all.
- Concealment is caused by conditions that obstruct perception — not physical obstructions that block attacks (those provide cover).
- Senses countering concealment (e.g., Counters Concealment: Darkness) remove the penalty for the corresponding condition.
- Applies a circumstance penalty to attack checks based on how well the attacker can perceive the target.
- Can be nullified by specific sense effects (Counters Concealment) that remove the perceptual obstruction.
- **Invariant:** Partial = −2, Total = −5; area and perception-range attacks bypass concealment penalties entirely.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_207.md`

### cover

- Cover applies when a target is behind a physical obstruction that could block or deflect an attack.
- Partial cover (roughly half the target behind obstruction): −2 circumstance penalty to attack checks.
- Total cover (three-quarters or more behind obstruction): −5 circumstance penalty to attack checks.
- Complete cover (target fully behind obstruction): cannot attack the target directly; may target the cover itself.
- Cover grants a circumstance bonus to Dodge resistance checks against area effects equal to its attack penalty, measured from the effect's origin.
- Applies a circumstance penalty to attack checks based on physical obstruction of the attack path.
- Grants a bonus to Dodge area-effect resistance checks equal to the cover penalty — the same obstruction that blocks attacks also deflects area effects.
- **Invariant:** Complete cover prevents targeting entirely; the attacker may instead target the obstruction.
- **Invariant:** Cover bonus to area-effect Dodge checks only applies when the cover is between the target and the effect's origin.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_208.md`

### surprise

- Surprise occurs when one or more characters begin a conflict unaware — typically from failing a Perception or similar check.
- If any characters are surprised, the conflict opens with a surprise round; all characters roll initiative normally.
- Surprised characters do not act during the surprise round; they are stunned and vulnerable until the end of the surprise round.
- Non-surprised characters during the surprise round are limited to a standard action and free actions (may exchange standard for a move action).
- Surprise attacks can occur mid-conflict via stealth, concealment, or unusual maneuvers; the target is vulnerable.
- Opens a special restricted round (surprise round) at the start of a conflict when any participants are surprised.
- Applies stunned + vulnerable to surprised characters for the duration of the surprise round.
- Limits non-surprised characters to standard + free actions in the surprise round (no full round).
- **Invariant:** Surprised characters cannot act during the surprise round; they recover to normal at the start of the first regular round.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_196.md`

### team attack

- Team attack allows multiple attackers to combine their efforts to overwhelm a single target's resistance.
- All attacks must share the same effect type and resistance defense, and be within 5 ranks of each other.
- Participants must all delay to the same initiative slot (the slowest attacker's position).
- Each attacker makes their own attack check; effects not requiring attack checks automatically count as one degree of success.
- The main attack uses the largest effect rank; each additional attack that hits contributes: 1 degree → +2 circumstance bonus to main rank; 3+ degrees → +5 bonus.
- Misses in a team attack have no effect and impose no penalties.
- Coordinates multiple attackers at the same initiative point to combine compatible attack effects.
- Scales the combined effect rank upward based on how many contributing attacks land.
- **Invariant:** Contributing attacks must share the same effect type, resistance defense, and be within 5 ranks.
- **Invariant:** Misses contribute nothing; only hits add to the combined result.

### combined attack

- Combined attack is the general pattern of multiple combatants coordinating compatible attacks against a single target (the team attack mechanic).
- Contributing attacks must share the same effect type and resistance defense and be within 5 ranks of each other before they can be combined.
- The result is a single composite effect rank boosted by the combined contributions of all participating hits.
- Describes the coordination pattern that produces a single composite effect rank from multiple compatible attacks.
- Enforces the compatibility constraint (same effect + resistance + within 5 ranks) before allowing combination.
- **Invariant:** The largest individual effect rank is the base; additional contributing hits add circumstance bonuses (not more base ranks).

### minion

- A minion is a minor character subject to special rules making them easier to defeat than full characters.
- Minions cannot score critical hits against non-minions.
- Non-minions may make attack checks against minions as routine checks (guaranteed hit with attack bonus ≥ 0).
- If a minion fails any resistance check, they suffer the worst degree of the effect regardless of actual degree of failure.
- Certain advantages (e.g., Takedown) are specifically more effective against or designed for use against minions.
- The GM may roll a single initiative check for an entire minion group.
- Simplifies resolution by compressing all resistance failures to the worst possible outcome.
- Enables routine-check attacks against them, removing attack randomness when facing masses of minions.
- **Invariant:** Any resistance failure → worst degree (e.g., any Toughness failure → incapacitated).
- **Invariant:** Minions cannot produce critical hits against non-minions regardless of die result.

*Hazards and Objects* — Hazards and Objects covers the non-combat-opponent sources of harm in the game world. Hazards are environmental dangers — falling, suffocation, heat, cold, vacuum, poison, disease, radiation — each governed by a Fortitude (or other) resistance check sequence that escalates conditions from fatigued through dying. Falling has its own damage formula (4 + 2× distance rank, capped at 16). Suffocation uses a breath-holding timer then a per-round Fortitude check. Damaging objects extends the combat system to inanimate targets: objects have Material Toughness values, cannot be dazed or staggered, and require either finishing attacks or repair. This KA interacts with Damage and Resistance (damage rank, Toughness check) and with Tactical Environment (hazards can affect the entire environment). The module owns the combat-facing rules for how hazards work in play.

### hazard

- Hazards are environmental dangers that harm characters independently of opponent attacks.
- Each hazard uses a resistance check (typically Fortitude) with DC = 10 + rank or a fixed DC; repeated failures escalate: fatigued → exhausted → incapacitated → dying.
- Hazard types include heat/cold, starvation/thirst, suffocation, vacuum, poison, disease, radiation, and falling.
- Immunity effects can negate specific hazard types entirely.
- Hazards may have their own initiative ranks in timed scenarios.
- Represents an environmental threat that fires resistance checks on a schedule independent of attacker turns.
- Escalates character conditions predictably from fatigued through dying on repeated failures.
- Can participate in initiative (with its own rank) in timed scenarios.
- **Invariant:** Immunity effect completely negates the corresponding hazard type.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_199.md`

### falling

- Falling inflicts damage rank = 4 + (2 × distance rank fallen), capped at rank 16.
- Characters with Acrobatics can fall greater distances without injury.
- Falling onto a dangerous surface may inflict additional damage at the GM's discretion.
- Catching a falling character or object requires a Dexterity check (DC 5); the catcher subtracts their Strength rank from falling damage rank — both catcher and caught suffer any remaining damage.
- A power (Flight, Move Object) may substitute its rank for Strength when catching, at the GM's discretion.
- Translates fall distance into damage rank via a fixed formula and applies it as a Toughness check.
- Provides a catching intervention path (Dexterity DC 5) that partially absorbs damage for both the catcher and the falling target.
- **Invariant:** Maximum falling damage rank is 16 regardless of distance rank.

### suffocation

- Characters may hold their breath for 10 rounds + (2 × Stamina rank) rounds before needing to check.
- After the limit, Fortitude check (DC 10, +1 per previous success) each round; failure → incapacitated.
- The following round after failure, the character becomes dying and cannot stabilize until able to breathe.
- Holding breath in vacuum additionally risks lung damage: Fortitude DC 15 (+1 per round); success causes loss of one Stamina rank; failure begins suffocation.
- Immunity to Suffocation removes this hazard entirely.
- Provides a grace period (breath-holding limit) before the Fortitude check sequence begins.
- Blocks stabilization from dying while the cause (no breathable atmosphere) persists.
- **Invariant:** Cannot stabilize while suffocating; removing the cause is the prerequisite for recovery.

### damaging objects

- Objects (targets lacking a Stamina rank) take damage similarly to characters but dazed and staggered results have no practical effect on inanimate targets.
- Inanimate objects are defenseless by definition and subject to finishing attacks: attacker may choose a routine check (auto-hit) or roll normally (auto-crit on any hit for +5 DC).
- Attacking an object held or worn by a character is a smash action (attack vs. character's defense at −5 if held; damage applied to the object).
- Two degrees of failure on the object's Toughness check causes a break; three or more degrees destroys the object.
- Objects cannot recover on their own — they must be repaired (Technology skill).
- Applies the damage system to inanimate targets with a defenseless-by-definition rule that simplifies resolution.
- Maps Toughness failure degrees to physical states: 2 degrees → break, 3+ degrees → destroyed.
- **Invariant:** Objects cannot self-recover; they require external repair via Technology skill.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_206.md`

### Material Toughness

- Material Toughness is the Toughness rank of a common material at approximately one inch (distance rank −7) of thickness.
- Each doubling of thickness adds +1 Toughness; each halving subtracts −1.
- Example ranks: paper/soil 0, glass/ice/rope 1, wood 3, stone 5, iron 7, reinforced concrete 8, steel 9, titanium 15, super-alloys 20+.
- Equipment has Toughness based on its material; devices have base Toughness = total power points ÷ 5 (round down, minimum 1).
- Provides a reference table mapping material type and thickness to a Toughness rank for use in object damage calculations.
- Scales linearly with thickness (±1 per doubling/halving).
- **Invariant:** The listed ranks apply at approximately one inch; thickness scaling is applied before any circumstance modifier.

*Hero Resources* — Hero Resources are the meta-level economy that gives heroes the ability to transcend normal limits. Hero points are a narrative currency earned through complications and heroic play, spent as reactions to re-roll dice, edit scenes, gain temporary advantages, get inspiration, counter effects, or instantly recover conditions. Extra effort is a within-turn free action that sacrifices the next turn's condition to gain a power boost now — an additional action, a skill bonus, a temporary power rank increase, or a power stunt. Power stunt is the specific extra effort option that instantiates a temporary Alternate Effect of an existing power. All three work together: hero points are the safety net that removes extra effort's fatigue cost, and power stunt is extra effort's most tactically complex option. Hero Resources are not bounded by power level — their effects can exceed what normal powers allow — and they apply as a layer on top of all other combat mechanics, never replacing them.

### hero point

- Players begin each game session with 1 hero point; unspent hero points do not carry over between sessions.
- Spending a hero point is a reaction (takes no time); a player may spend as many as they have in one turn.
- Improve Roll: re-roll any die roll before GM announces outcome; take the better; on a re-roll result of 1–10, add 10 (re-roll always yields 11–20).
- Edit Scene: add or change a scene detail with GM approval; cannot undo events that have already occurred.
- Heroic Feat: gain one rank of an advantage (except fortune advantages) until end of next turn; prerequisites must be met.
- Inspiration: receive a hint, clue, or direction from the GM.
- Instant Counter: attempt to counter an effect used against the hero as a reaction.
- Recover: immediately remove a dazed, fatigued, or stunned condition; or convert exhausted to fatigued.
- Heroes earn additional hero points from complications, acts of heroism, and roleplaying.
- Spends as a reaction (zero action cost) providing one of eight distinct rescue or amplification effects.
- Re-roll floor rule ensures no re-roll produces below 11, making hero point rolls statistically favorable.
- **Invariant:** Unspent hero points reset to 1 at the start of each new session — never carry over.
- **Invariant:** May be spent multiple times in one turn (limited only by number held).
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_019.md`

### extra effort

- Extra effort is a free action declared by the player, limited to once per turn.
- Choose one benefit: additional standard action; +2 circumstance bonus on one check (or upgrade existing +2 to +5); +1 rank to a power effect until start of next turn; power stunt (temporary Alternate Effect for the scene); additional resistance check against an ongoing effect; retry a failed effect; +1 speed rank until next turn; +1 Strength rank until next turn.
- Extra effort benefits are not limited by power level.
- Cost: at the start of the immediately following turn, the hero becomes fatigued; fatigued → exhausted on subsequent use; exhausted → incapacitated.
- Spending a hero point at the start of the following turn removes the fatigue cost entirely.
- Trades next-turn condition degradation for an immediate within-turn benefit chosen from eight options.
- Deferred cost fires at the start of the NEXT turn — not immediately — giving the hero a full benefit turn before the penalty.
- **Invariant:** Once per turn; fatigue escalates each time (normal → fatigued → exhausted → incapacitated).
- **Invariant:** Benefits are not limited by power level — extra effort can temporarily exceed PL caps.

### power stunt

- A power stunt uses extra effort to temporarily gain an Alternate Effect of one of the hero's existing powers.
- The stunt lasts until the end of the scene or until the effect's normal duration expires, whichever comes first.
- Permanent effects cannot be used as the basis for a power stunt.
- A power stunt gained via a critical hit's Alternate Effect option costs no fatigue.
- Instantiates a temporary Alternate Effect of an existing power for the duration of the scene.
- Costs extra effort's deferred fatigue unless obtained via critical hit's Alternate Effect option.
- **Invariant:** The base power must already exist on the character's sheet.
- **Invariant:** Permanent effects cannot be used as the basis; scene-duration cap applies.
