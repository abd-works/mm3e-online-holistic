---

# skill

- **Purpose:** hold a hero's skill ranks and resolve every skill check (d20 + skill rank + ability modifier + circumstance modifiers against a DC), including the Trained Only gate and the interaction, manipulation and combat skill rules.
- **Seam (terms):** Skill, Skills, CircumstanceModifier, InteractionSkill, ManipulationSkill, CombatSkill
- **Dependencies (one-way):** ability (ability modifier), character-construction (power point, power level), check-resolution (degree of success, routine check, condition, team check), combat (attack check), power (power effect), advantage (Skill Mastery, Inventor)

## Constraint

Callers resolve skill use only through a skill's check, never by adding its parts themselves; ranks are bought through Skills. Power points are spent and the skill modifier limit (power level + 10) is enforced by character-construction at build time, not at check time.

## **Skill**

+ Skill(name: SkillName, ability: Ability, isTrainedOnly: Boolean)
	// Acrobatics, Athletics, Expertise, Insight, Investigation, Perception and Stealth are instances; interaction, manipulation and combat skills are instances of their subtypes
	// rank 0 is a valid untrained state, not an absent skill; the ability modifier still applies at rank 0
------
+ name: SkillName
+ area: String
	// Expertise names one field and each area is a separate skill with its own rank
+ << association >> ability: Ability
+ rank: Integer
+ isTrainedOnly: Boolean
+ isTrained: Boolean
	// true whenever rank is 1 or greater
+ modifier: Integer
	// always skill rank + ability modifier; the ability modifier is included even when rank is 0
+ routineResult: Integer
	// always modifier + 10
+ isMastered: Boolean
	// Skill Mastery names one skill; a mastered skill uses its routine result without rolling, even under stress, and never beyond the skill modifier limit
----
+ check(difficultyClass: Integer, circumstanceModifiers: list[CircumstanceModifier]): DegreeOfSuccess
	// a Trained Only skill at rank 0 fails automatically before any roll; no partial result is produced
	// a natural 20 raises the degree by one after the normal degree is found
	-> ability.rank
	-> degreeOfSuccess.resolve

## **Skills**

+ Skills(skills: list[Skill])
------
+ << composition >> skills: list[Skill]
----
+ skill(name: SkillName): Skill
+ buyRanks(ranks: Integer): Skills
	// 1 power point buys 2 skill ranks, split freely across any skills
	-> powerPoints.spend

## **CircumstanceModifier**

+ CircumstanceModifier(value: Integer, circumstance: String)
	// transient and situational; never changes the skill rank or the ability modifier
------
+ value: Integer
	// lacking required tools is always -5; a subject who cannot hear or understand an interaction is -5
+ circumstance: String

## **InteractionSkill**

+ InteractionSkill(name: SkillName, ability: Ability)
	// Deception, Intimidation and Persuasion are instances; Insight resists them
------
----
+ influence(subjects: list[Character], difficultyClass: Integer): DegreeOfSuccess
	// subject awareness, subject Intellect and Immunity are resolved before the check; a blocked check has no effect
	// -5 when the subject cannot hear or understand; -5 when the subject's Intellect is -5; refused when the subject lacks mental abilities or is immune
	// a group gets one result applied to every member; mindless subjects are unaffected
	-> powerEffect.grantsImmunity
	-> skill.check

## **ManipulationSkill**

+ ManipulationSkill(name: SkillName, ability: Ability, requiresTools: Boolean)
	// Sleight of Hand, Technology, Treatment and Vehicles are instances, all Trained Only
	// usable only with prehensile limbs and a Strength rank, or a suitable Precise power effect
------
+ requiresTools: Boolean
	// without required tools the check always takes -5
----
+ assist(teamCheck: TeamCheck): TeamCheck
	// a character without physical manipulation capability uses its ranks only to oversee or assist others
	-> teamCheck.assist

## **CombatSkill**

+ CombatSkill(name: SkillName, ability: Ability, weaponOrPower: String)
	// Close Combat (Fighting) and Ranged Combat (Dexterity) are instances, usable untrained
	// each instance covers exactly one weapon or power; the bonus never transfers to another attack
------
+ weaponOrPower: String
	// an array of powers counts as one power only at the Gamemaster's discretion
----
+ addToAttack(attackCheck: AttackCheck): AttackCheck
	// adds its rank to attack checks with its own weapon or power only; it never adds to any defense
	-> attackCheck.addBonus
