---

# check-resolution

- **Purpose:** resolve any check a character makes (d20 roll plus trait rank and modifiers against a Difficulty Class, as routine, opposed or team checks) into success or failure with degrees, translate ranks to real-world measures, and track the basic and combined conditions imposed on a character.
- **Seam (terms):** Trait, MeasurementType, Measurement, Check, CheckResult, GradedCheckResult, DifficultyClass, OpposedCheck, RoutineCheck, TeamCheck, Condition, GameModifier, ConditionSource, ImposedCondition, ImposedConditions, CombinedCondition, AppliedEffect
- **Dependencies (one-way):** power (effect), character-construction (character)

## Constraint

Callers get an outcome only by resolving a Check (or AppliedEffect.resist for resistance) and never compare rolls or add ranks themselves; rank arithmetic goes through Measurement. Conditions are applied and removed only through a character's ImposedConditions so supersession and blocked-condition reveal always hold. Effect and Character are supplied by power and character-construction, not built here.

## **Trait** <<Entity>>

+ Trait(character: Character, purchasedRank: Integer)
+ Trait(character: Character, purchasedRank: Integer, circumstanceModifier: Integer)
	// two traits with the same rank on different characters are distinct
------
+ << association >> character: Character
+ traitName: String
+ purchasedRank: Integer
----
+ effectiveRank(): Integer
	// effectiveRank is always purchasedRank minus the sum of active game modifier amounts targeting this trait from the character's imposed conditions
	-> conditionPenalty
- conditionPenalty(): Integer
	// sum of game modifier amounts on active imposed conditions whose modifier applies to this trait's name; 0 when no active condition targets this trait
	-> character.imposedConditions.activeConditions
+ realWorldValue(type: MeasurementType): Number
	// values at higher ranks are approximate guidelines, not precise calculations
	-> measurement.lookup
+ addRank(other: Integer, type: MeasurementType): Integer
	// ranks are never added directly: convert to measures, add the measures, convert back to a rank
	-> measurement.lookup
	-> measurement.rankFor
+ performCheck(dc: DifficultyClass): CheckResult
	// creates and resolves a Check using this trait and the given DC
	-> check.resolve

## **MeasurementType** <<ValueObject>>

	// pre-defined constants; no constructor
------
+ MASS: Integer = 1
+ TIME: Integer = 2
+ DISTANCE: Integer = 3
+ VOLUME: Integer = 4

## **Measurement** <<Service>>

	// static operations only; no instance state and no constructor
------
----
+ lookup(rank: Integer, type: MeasurementType): Number
	// returns the real-world value for the rank in the given dimension; values at higher ranks are approximate guidelines
+ rankFor(measure: Number, type: MeasurementType): Integer
	// returns the rank whose real-world value is nearest to the measure in the given dimension
+ throwingDistanceRank(strengthRank: Integer, massRank: Integer): Integer
	// throwingDistanceRank = strengthRank − massRank via measure arithmetic
	-> lookup
	-> rankFor
+ travelDistanceRank(timeRank: Integer, speedRank: Integer): Integer
	// travelDistanceRank = timeRank + speedRank via measure arithmetic
	-> lookup
	-> rankFor
+ travelTimeRank(distanceRank: Integer, speedRank: Integer): Integer
	// travelTimeRank = distanceRank − speedRank via measure arithmetic
	-> lookup
	-> rankFor

## **Check** <<Entity>>

+ Check(trait: Trait, dc: DifficultyClass)
+ Check(trait: Trait, dc: DifficultyClass, circumstanceModifier: Integer)
	// each resolution is a distinct occurrence with its own outcome
	// the shape is always roll total against dc.value; subtypes vary only how the total or the DC is produced
------
+ << association >> trait: Trait
+ dc: DifficultyClass
+ circumstanceModifier: Integer
----
+ resolve(): CheckResult
	// total = trait effective rank + d20 roll + circumstance modifier; success when total ≥ dc.value; critical only when the roll is 20
	-> rollD20
	-> trait.effectiveRank
+ resolveGraded(): GradedCheckResult
	// same resolution as resolve, plus a degree computed from the margin; a critical adds one degree after the normal calculation; resultingCondition is left null for AppliedEffect.resist to fill
	-> resolve
	-> computeDegree
- rollD20(): Integer
	// a uniformly random integer from 1 to 20 inclusive
- computeDegree(margin: Integer, isCritical: Boolean, isSuccess: Boolean): Integer
	// base 1; +1 for each full 5 points of margin; maximum 4; a critical adds 1 after the normal calculation and can turn 1 degree of failure into 1 degree of success; always clamped to 1–4

## **CheckResult** <<ValueObject>>

+ CheckResult(rollTotal: Integer, dc: DifficultyClass, isSuccess: Boolean, margin: Integer, isCritical: Boolean)
------
+ rollTotal: Integer
+ dc: DifficultyClass
+ isSuccess: Boolean
	// success when rollTotal ≥ dc.value; failure when below
+ margin: Integer
+ isCritical: Boolean
	// true only when the raw d20 roll was exactly 20

## **GradedCheckResult** <<ValueObject>> : CheckResult

+ GradedCheckResult(rollTotal: Integer, dc: DifficultyClass, isSuccess: Boolean, margin: Integer, isCritical: Boolean, degree: Integer, resultingCondition: Condition)
------
+ degree: Integer
	// 1–4 combined with the inherited isSuccess; a critical raises the degree by one after the normal calculation
+ << association >> resultingCondition: Condition
	// the condition this degree of failure imposes, from the resisted effect's condition set; null when no condition maps to the degree or when isSuccess is true

## **DifficultyClass** <<ValueObject>>

+ DifficultyClass(value: Integer)
------
+ value: Integer
	// 0 ≤ value ≤ 40 on the standard benchmark scale; higher values are valid for exceptional circumstances

## **OpposedCheck** <<Entity>> : Check

+ OpposedCheck(trait: Trait, opponent: Character, isPassive: Boolean)
	// passive or active is fixed when the check is created
------
+ << association >> opponent: Character
+ isPassive: Boolean
----
+ resolve(): CheckResult
	// passive: DC = opponent's matching trait effective rank + 10 and the opponent does not roll; active: both roll and the higher total wins; a tie goes to resolveTie
	-> opponent.traitMatching
	-> check.resolve
	-> resolveTie
- resolveTie(activeResult: CheckResult, opposingResult: CheckResult): CheckResult
	// the higher trait effective rank wins; with equal ranks a new d20 decides (1–10 the active character wins, 11–20 the opposing character wins)

## **RoutineCheck** <<Entity>> : Check

+ RoutineCheck(trait: Trait, dc: DifficultyClass)
+ RoutineCheck(trait: Trait, dc: DifficultyClass, circumstanceModifier: Integer)
------
----
+ resolve(): CheckResult
	// substitutes 10 for the d20; trait rank and circumstance modifiers still apply; never critical; a routine total below the DC returns failure and the caller may make a standard Check instead
	-> trait.effectiveRank

## **TeamCheck** <<Entity>> : Check

+ TeamCheck(trait: Trait, dc: DifficultyClass, helpers: List<Character>)
------
+ << association >> helpers: List<Character>
----
+ resolve(): CheckResult
	// helpers roll the same trait against DC 10 first; their results give a circumstance modifier on the leader's check; only the leader's total decides the outcome
	-> computeHelperModifier
	-> check.resolve
- computeHelperModifier(): Integer
	// 1–2 helper successes give +2; 3 or more give +5; with no success, a helper failure gives −2; the net modifier applies once to the leader's check
	-> helper.traitMatching
	-> check.resolve

## **Condition** <<ValueObject>>

	// pre-defined instances: DAZED, STUNNED, IMPAIRED, DISABLED, VULNERABLE, DEFENSELESS, HINDERED, IMMOBILE, COMPELLED, CONTROLLED, WEAKENED, DEBILITATED, FATIGUED, TRANSFORMED, UNAWARE, NORMAL
	// two conditions with the same name are interchangeable
------
+ name: String
+ << composition >> gameModifier: GameModifier
+ << association >> supersedes: Condition
	// the supersession chain is navigable through Condition data; supersedes and supersededBy are properties, not a separate runtime object
+ << association >> supersededBy: Condition

## **GameModifier** <<ValueObject>>

+ GameModifier(appliesTo: String, amount: Integer)
------
+ appliesTo: String
	// names the trait this modifier targets; null or empty means it applies to all checks
+ amount: Integer
	// negative values impose a penalty; positive values grant a bonus

## **ConditionSource** <<ValueObject>>

+ ConditionSource(identity: String)
------
+ identity: String
	// imposed conditions sharing an identity follow same-source supersession rules; different identities follow different-source rules

## **ImposedCondition** <<Entity>>

+ ImposedCondition(condition: Condition, source: ConditionSource)
	// each application of a condition to a character from a source is a distinct occurrence
------
+ << association >> condition: Condition
+ source: ConditionSource
+ isActive: Boolean
	// only an active imposed condition applies its game modifier to the character
+ << association >> blockingCondition: ImposedCondition
	// set when a more severe condition from a different source parks this one inactive; null when active or unblocked
----
+ activate(): void
	// sets isActive to true and clears blockingCondition; called when the blocker is removed and this condition's source is still in effect
+ deactivate(blocker: ImposedCondition): void
	// sets isActive to false and records the blocker; called when a more severe condition from a different source supersedes this one

## **ImposedConditions** <<Entity>>

+ ImposedConditions()
	// owned by the character; it has no identity outside that character
------
+ << composition >> appliedConditions: List<ImposedCondition>
+ dyingSuccessCount: Integer
+ dyingFailureCount: Integer
----
+ activeConditions(): List<ImposedCondition>
	// returns only the imposed conditions whose isActive is true
+ applyCondition(condition: Condition, source: ConditionSource): void
	// same source, more severe: remove the less severe and add the new one active; same source, less severe: no change
	// different source, more severe: the new one is active and the existing one becomes inactive; different source, less severe: add the new one inactive
	-> findActiveBySameSource
	-> findActiveInSupersessionChain
	-> incomingSupersedes
	-> imposedCondition.deactivate
- incomingSupersedes(existing: ImposedCondition, incoming: Condition): Boolean
	// true when incoming.supersedes is the existing condition; false when the existing condition supersedes incoming
- findActiveBySameSource(source: ConditionSource): ImposedCondition
	// the first active imposed condition whose source identity matches; null if none
- findActiveInSupersessionChain(condition: Condition): ImposedCondition
	// any active imposed condition in the same supersession chain as the incoming condition; null if none
+ penaltyFor(trait: Trait): Integer
	// sum of game modifier amounts from active imposed conditions whose modifier targets the trait or all checks; all active conditions stack
	-> activeConditions
+ revealBlockedConditions(removedBlocker: ImposedCondition): void
	// when a blocker is removed, every condition it was blocking becomes active if its source is still in effect
	-> imposedCondition.activate
+ remove(imposed: ImposedCondition): void
	// removes the imposed condition; if it was a blocker, the conditions it blocked are revealed in the same call
	-> revealBlockedConditions
+ recordDyingFortitudeResult(result: GradedCheckResult): String
	// degrees of success and failure accumulate across rounds; 2 accumulated successes give STABILIZED, 3 accumulated failures give DEAD, otherwise ALIVE

## **CombinedCondition** <<ValueObject>>

	// pre-defined instances: STAGGERED, INCAPACITATED, DYING, EXHAUSTED, ASLEEP, BLIND, BOUND, DEAF, ENTRANCED, PARALYZED, PRONE, RESTRAINED, SURPRISED
------
+ name: String
+ << composition >> constituents: List<Condition>
	// each constituent may be superseded or resolved on its own while the combined condition's name persists

## **AppliedEffect** <<Entity>>

+ AppliedEffect(effect: Effect, character: Character)
	// links an effect to the conditions it imposed on a character and owns the ongoing-resistance lifecycle
------
+ << association >> effect: Effect
+ << association >> character: Character
+ isOngoing: Boolean
	// when false, every imposed condition this effect created has been removed from the character
+ << composition >> imposedConditions: List<ImposedCondition>
	// tracks every imposed condition this effect created on the character
----
+ resist(defenseTrait: Trait): GradedCheckResult
	// DC = 10 + effect rank; on success the effect ends and all its conditions are removed; on failure conditions persist and the effect's degree mapping may add more
	-> effect.effectDc
	-> check.resolveGraded
	-> effect.conditionFor
	-> end
	-> character.imposedConditions.applyCondition
	-> character.imposedConditions.findActiveBySameSource
+ end(): void
	// sets isOngoing to false and removes every imposed condition this effect created from the character's ImposedConditions
	-> character.imposedConditions.remove
