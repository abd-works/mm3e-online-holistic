
---

# ability

- **Purpose:** hold a hero's eight ability ranks and the five defenses and initiative derived from them, so every check, defense and cost reads one current rank.
- **Seam (terms):** Ability, Abilities, Defense, Defenses
- **Dependencies (one-way):** character-construction (power point, power level), power (enhanced trait), check-resolution (condition)

## Constraint

Callers change a rank only through the ability that owns it; derived defenses and initiative are read, never set. Power points are spent and limits enforced by character-construction, not here.

## **Ability**

+ Ability(name: AbilityName, rank: Integer)
	// rank never goes below −5 through a player's choice; below −5 is reached only by an outside effect, and the ability is then debilitated
	// a rank change reaches every trait derived from this ability in the same operation
------
+ name: AbilityName
+ category: AbilityCategory
+ rank: Integer
+ enhancedRank: Integer
	// the enhanced portion is nullified apart from the natural portion; nullifying it never touches the natural rank
+ isAbsent: Boolean
	// an absent ability has no rank; it cannot be weakened or debilitated
+ isDebilitated: Boolean
----
+ setRank(rank: Integer): Ability
	// costs 2 power points per rank raised and refunds 2 per rank lowered
	-> powerPoints.spend
+ designateEnhanced(ranks: Integer): Ability
+ markAbsent(): Ability
	// needs Gamemaster permission for a hero; grants 10 power points
	-> powerPoints.grant
+ reduceByEffect(ranks: Integer): Ability
	// past −5 the ability is debilitated and further reduction is refused
	-> condition.apply

## **Abilities**

+ Abilities(abilities: list[Ability])
	// holds exactly the eight abilities: Strength, Stamina, Agility, Dexterity, Fighting, Intellect, Awareness, Presence
	// when Awareness is absent, Presence is absent too
------
+ << composition >> abilities: list[Ability]
----
+ ability(name: AbilityName): Ability

## **Defense**

+ Defense(name: DefenseName, ability: Ability)
	// the base rank always equals the current rank of its ability
------
+ << association >> ability: Ability
+ name: DefenseName
+ purchasedRanks: Integer
	// Toughness cannot be raised above its Stamina base with power points
+ rank: Integer
+ defenseClass: Integer
	// always rank + 10
+ isActive: Boolean
	// Dodge and Parry are active defenses; Fortitude, Toughness and Will are passive
----
+ buyRanks(ranks: Integer): Defense
	// 1 power point per rank above the base, within power level limits
	-> powerPoints.spend

## **Defenses**

+ Defenses(abilities: Abilities)
	// one defense each for Dodge (Agility), Parry (Fighting), Fortitude (Stamina), Toughness (Stamina) and Will (Awareness)
------
+ << composition >> defenses: list[Defense]
+ << association >> abilities: Abilities
+ initiative: Integer
	// Agility rank plus Improved Initiative and power bonuses; with Agility absent the Agility part is 0
----
+ defense(name: DefenseName): Defense
