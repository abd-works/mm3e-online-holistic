---

# combat

- **Purpose:** run a conflict: who acts when and with which actions, whether an attack hits, and what damage, hazards and recovery do to its target.
- **Seam (terms):** Initiative, Turn, AttackCheck, Maneuver, TeamAttack, ResistanceCheck, ToughnessResistance, Hazard, InanimateObject, HeroPoints, ExtraEffort
- **Dependencies (one-way):** ability (Defense: Dodge, Parry, Fortitude, Toughness; Ability: Strength), check-resolution (condition), power (power effect, Alternate Effect), advantage (advantage: Improved Initiative, Improved Critical), character-construction (power level)

## Constraint

Callers act in a conflict only through a character's turn, and conditions are imposed by asking check-resolution to apply them; combat decides when a condition is imposed, never what it does. Defense ranks are read from ability, never set here.

## **Initiative**

+ Initiative(characters: list[Character])
	// every character in a conflict has exactly one initiative position; it persists across rounds unless delay or ready moves it
	// every declared action occurs within a round
------
+ << composition >> turns: list[Turn]
+ round: Integer
	// advances only once every character in the order has completed their turn
+ isSurpriseRound: Boolean
	// surprised characters do not act in the surprise round and are stunned and vulnerable until it ends; the others get a standard action and free actions only
----
+ rollInitiative(): Initiative
	// d20 + initiative modifier, counting down from highest; ties go to highest Dodge, then Agility, then Awareness; the GM may roll once for a group of minions
	-> defenses.initiative
+ join(character: Character): Initiative
	// a character entering after the conflict began rolls initiative and acts at that place in the existing order
+ moveSlot(turn: Turn): Initiative
	// a delayed or readied turn takes the slot where it acted
+ advanceRound(): Initiative

## **Turn**

+ Turn(character: Character, initiative: Initiative)
	// a character has exactly one turn per round; extra effort adds an action within it, never a second turn
	// opens by ending "until the start of your next turn" effects; closes by ending "until the end of your turn" effects, then making resistance checks against ongoing effects
------
+ << association >> initiative: Initiative
+ standardActions: Integer
	// one per turn; extra effort grants one more; consumed at declaration with no refund
+ moveActions: Integer
	// one per turn, or two when the standard action is exchanged for a move; a move is not split around the standard action
+ hasActed: Boolean
+ readiedAction: ActionType
	// only one at a time; lost if the next initiative comes up before its trigger fires
+ hasRecovered: Boolean
	// recover is usable once per conflict
----
+ start(): Turn
+ takeStandardAction(): Turn
+ exchangeStandardForMove(): Turn
+ takeMoveAction(): Turn
+ takeFreeAction(): Turn
	// free actions happen only on the character's own turn
+ react(): Turn
	// only when circumstances trigger it; never uses the standard, move or free action budget
+ delay(): Turn
	// refused after any action this turn or when the character cannot act; the turn is lost if not taken before the same position comes up next round
	-> initiative.moveSlot
+ ready(action: ActionType, trigger: Trigger): Turn
	// a standard action; the readied action fires as a reaction when the trigger occurs
	-> initiative.moveSlot
+ recover(): Turn
	// takes the whole turn; removes the worst damage condition or fatigue, or makes one more resistance check against an ongoing effect; +2 to active defenses until the start of the next turn
	-> toughnessResistance.removeCondition
	-> resistanceCheck.resolve
+ end(): Turn
	-> resistanceCheck.resolve

## **AttackCheck**

+ AttackCheck(range: AttackRange, attackBonus: Integer, defense: Defense)
	// a natural 1 always misses; a natural 20 always hits
	// area and perception-range attacks make no attack check: they affect the target automatically and can never be critical hits
------
+ << association >> defense: Defense
	// close attacks target Parry, ranged attacks target Dodge
+ range: AttackRange
	// a close attack needs the target within reach; a ranged attack takes −2 at medium range, −5 at long range, and cannot target beyond long range
+ attackBonus: Integer
	// Fighting or Dexterity plus Close or Ranged Combat ranks and circumstance modifiers; a maneuver trade-off never takes it below +0
+ concealment: ConcealmentLevel
	// partial −2, total −5
+ cover: CoverLevel
	// partial −2, total −5; complete cover prevents targeting, and the attacker may target the cover instead
+ isHit: Boolean
+ isCriticalHit: Boolean
	// needs both a natural 20 and a total at or above the defense class; a minion never scores one against a non-minion
----
+ aim(): AttackCheck
	// +5 for a close attack or a ranged attack at close range, +2 at greater range; the attacker is vulnerable while aiming, and any action other than the attack cancels the bonus
	-> condition.apply
+ charge(): AttackCheck
	// moves the speed rank in a straight line toward the target, then a close attack at −2
+ resolve(): AttackCheck
	// d20 + attack bonus against the defense class (active defense + 10); vulnerable halves the active defense, defenseless makes it 0 and allows a routine check
	-> defense.defenseClass
+ chooseCriticalEffect(effect: CriticalEffect): AttackCheck
	// Increased Effect (+5 resistance DC), Added Effect, or Alternate Effect (a power stunt with no fatigue); Increased Effect against a minion gives the worst degree

## **Maneuver**

+ Maneuver(name: ManeuverName, attackCheck: AttackCheck)
	// a maneuver is a standard action, and the GM decides whether circumstances permit it
------
+ << association >> attackCheck: AttackCheck
+ name: ManeuverName
	// defend, disarm, grab, trip, feint or slam attack
+ holdDegree: Integer
	// grab: one degree restrains the target, two or more bind it; improving a hold adds degrees, losing frees the target
----
+ resolve(): Maneuver
	// disarm: −2 close or −5 ranged, then damage rank against Strength; trip: −2 against Parry, then Acrobatics or Athletics opposed; grab: the target resists with the better of Strength or Dodge; feint: Deception against the better of Deception or Insight, leaving the target vulnerable to the next attack; defend: an opposed active defense against each attack until the next turn, a roll of 10 or lower counting as 10; slam attack: damage is the greater of speed rank or damage rank + 1, and the attacker resists half of it
	-> attackCheck.resolve
	-> condition.apply
+ counter(): Maneuver
	// counter-disarm or counter-trip, as a reaction, only when the attacker loses the opposed check, never when the attack misses
+ maintainHold(): Maneuver
	// a free action each turn; missing it releases the target; the attacker is hindered and vulnerable while holding
	-> condition.apply

## **TeamAttack**

+ TeamAttack(attacks: list[AttackCheck])
	// every contributing attack shares the effect type and resistance defense and is within 5 ranks of the others
	// all participants delay to the slowest attacker's initiative
------
+ << aggregation >> attacks: list[AttackCheck]
+ effectRank: Integer
	// the largest effect rank is the base; each hit adds +2 for one degree or +5 for three or more; misses add nothing
----
+ combine(): TeamAttack
	-> attackCheck.resolve

## **ResistanceCheck**

+ ResistanceCheck(defense: Defense, difficulty: Integer)
	// not an action; it never uses the action allotment
	// a minion that fails suffers the worst degree whatever the actual degree of failure
------
+ << association >> defense: Defense
+ difficulty: Integer
	// effect rank + 10
+ degreesOfFailure: Integer
+ isOngoing: Boolean
	// success against an ongoing effect ends it and removes all its conditions
----
+ resolve(): ResistanceCheck
	// d20 + defense against the difficulty; each degree of failure imposes a worse outcome
	-> condition.apply

## **ToughnessResistance**

+ ToughnessResistance(toughness: Defense)
	// every failure adds a cumulative −1 penalty, across all hits and attackers, until the character recovers
------
+ << association >> toughness: Defense
+ penalty: Integer
+ damageCondition: DamageCondition
	// incapacitated, then dying on another failure, then dead on another; incapacitated means no actions, defense class 10, and attackers may use routine checks
----
+ resist(damageRank: Integer): ToughnessResistance
	// d20 + Toughness against damage rank + 15; one degree −1, two dazed, three staggered (already staggered counts as four), four incapacitated
	-> condition.apply
+ removeCondition(): ToughnessResistance
	// a living target removes one damage condition per minute of rest, worst first

## **Hazard**

+ Hazard(name: HazardName, rank: Integer)
	// an Immunity effect against the hazard type negates it completely
------
+ name: HazardName
	// falling, suffocation, heat, cold, starvation, thirst, vacuum, poison, disease or radiation
+ rank: Integer
	// falling damage is 4 + 2 × distance rank, never above 16
+ initiativeRank: Integer
----
+ fireResistanceCheck(): ResistanceCheck
	// usually Fortitude against 10 + rank; repeated failures escalate fatigued, exhausted, incapacitated, dying; a suffocating character cannot stabilize until able to breathe
	-> resistanceCheck.resolve

## **InanimateObject**

+ InanimateObject(materialToughness: Integer)
	// never recovers by itself; it must be repaired
------
+ materialToughness: Integer
	// the material's rank at about one inch, +1 per doubling of thickness and −1 per halving
+ isBroken: Boolean
+ isDestroyed: Boolean
----
+ resist(damageRank: Integer): InanimateObject
	// defenseless by definition and open to finishing attacks; dazed and staggered do nothing; two degrees of failure break it, three or more destroy it
+ repair(): InanimateObject

## **HeroPoints**

+ HeroPoints()
	// a session starts with 1; unspent points never carry over
------
+ count: Integer
----
+ spend(use: HeroPointUse): HeroPoints
	// a reaction that takes no time, as often in one turn as points are held; an Improve Roll re-roll of 1–10 adds 10
+ earn(): HeroPoints
+ resetForSession(): HeroPoints

## **ExtraEffort**

+ ExtraEffort(turn: Turn)
	// once per turn; its benefits are not limited by power level
------
+ << association >> turn: Turn
+ fatigue: FatigueLevel
	// escalates each use: fatigued, exhausted, incapacitated
----
+ declare(benefit: ExtraEffortBenefit): ExtraEffort
	// a free action; the fatigue lands at the start of the following turn
+ powerStunt(power: Power): ExtraEffort
	// a temporary Alternate Effect of a power the hero already has, for the scene at most; never based on a permanent effect
+ removeFatigue(): ExtraEffort
	// a hero point spent at the start of the following turn removes the fatigue
	-> heroPoints.spend
