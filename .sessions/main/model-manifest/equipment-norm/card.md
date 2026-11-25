# equipment

- **Purpose:** give a hero the gear behind their concept — removable devices paid in power points, mundane equipment, weapons, armor, vehicles and headquarters paid in equipment points, inventions built on the fly, and constructs — so each item grants exactly what it was paid for and is lost and recovered by its own rules.
- **Seam (terms):** Device, Equipment, EquipmentAdvantage, AlternateEquipment, Invention, Weapon, Armor, Vehicle, Headquarters, Construct
- **Dependencies (one-way):** power (power effect, Removable flaw), character-construction (power points, power level), ability (Strength, absent ability), skill (Technology skill, Expertise: Magic), advantage (Minion advantage), combat (hero point)

## Constraint

Callers buy equipment, weapons, armor, vehicles and headquarters only through the Equipment advantage's equipment point pool, and devices only with power points; an item whose benefits exceed real-world technology is a device, never equipment. Power effect mechanics, power points and the Technology skill are used here, not redefined.

## **Device**

+ Device(powerEffects: list[PowerEffect], removability: Removability)
	// must carry Removable or Easily Removable as a flaw; a power without that flaw is not a device
	// its power points stay spent on the character's sheet when it is lost, so the character can always replace it
------
+ << association >> powerEffects: list[PowerEffect]
+ removability: Removability
	// Easily Removable applies only to items that are small, loosely carried or designed for quick removal
+ isIndestructible: Boolean
	// only a device already carrying Removable or Easily Removable can be Indestructible
+ descriptor: DeviceDescriptor
+ isInOwnersPossession: Boolean
----
+ remove(): Device
	// all its power effects are suspended together the moment it leaves the owner's possession
+ recover(): Device
	// all its power effects are restored together when the owner recovers it
+ useTemporarily(character: Character): Device
	// one scene or adventure without paying power points; the GM may require a hero point
	-> heroPoints.spend
+ replace(): Device
	// an Indestructible device is never permanently eliminated

## **Equipment**

+ Equipment(cost: Integer)
	// benefits must stay within real-world technology; an item whose benefits exceed the ceiling is a device
------
+ cost: Integer
+ bonus: Integer
	// applies only if it is the highest equipment bonus of its type in effect; equipment bonuses never stack
+ isAvailable: Boolean
----
+ declareLost(): Equipment
	// destroyed, lost or failed as a complication; no power points are recovered
+ performStunt(): Equipment
	// equipment never benefits from extra effort; a hero point is the only way
	-> heroPoints.spend
+ produceOnHand(): Equipment
	// on-hand equipment lasts one scene after a hero point is spent, when the GM finds it plausible
	-> heroPoints.spend

## **EquipmentAdvantage**

+ EquipmentAdvantage(ranks: Integer)
	// the pool is never exceeded; a purchase that would overspend it is refused
------
+ equipmentPoints: Integer
+ << aggregation >> items: list[Equipment]
----
+ buy(item: Equipment): EquipmentAdvantage
	// a vehicle or headquarters power effect costs one-fifth its normal power-point cost in equipment points

## **AlternateEquipment**

+ AlternateEquipment(items: list[Equipment])
	// only one item is active at a time; selecting a new item deactivates the previous one
------
+ << aggregation >> items: list[Equipment]
+ << association >> activeItem: Equipment
+ cost: Integer
	// full price of the most expensive item plus 1 equipment point per additional item
----
+ activate(item: Equipment): AlternateEquipment
+ addForScene(item: Equipment): AlternateEquipment
	// a hero-point stunt adds the item for one scene only
	-> heroPoints.spend

## **Invention**

+ Invention(device: Device, method: InventionMethod)
	// both the design and construction checks are made before the device is available; only jury-rigging skips design
	// an invented device lasts one scene; reuse costs a hero point, permanent use costs power points
------
+ << composition >> device: Device
+ method: InventionMethod
	// inventing and jury-rigging use the Technology skill; a ritual uses Expertise: Magic
+ isJuryRigged: Boolean
----
+ design(): Invention
	// GM rolls secretly, DC 10 + point cost, 1 hour per point; 3+ degrees of failure looks correct but will not work
	-> technologySkill.check
+ construct(): Invention
	// DC 10 + point cost, 4 hours per point; each time rank reduced is −5 on the check
	-> technologySkill.check
+ juryRig(): Invention
	// spend a hero point, skip design, 1 round per point, construction DC +5, never a routine check
	-> heroPoints.spend
	-> technologySkill.check
+ reuse(): Invention
	-> heroPoints.spend

## **Weapon** : Equipment

+ Weapon(category: WeaponCategory, effect: PowerEffect, criticalThreatRange: Integer, cost: Integer)
	// carries exactly four traits: category, effect, critical threat range and cost
------
+ category: WeaponCategory
+ << association >> effect: PowerEffect
+ criticalThreatRange: Integer
+ isStrengthBased: Boolean
+ toughness: Integer
+ accessories: list[WeaponAccessory]
	// each accessory is bought separately at 1 equipment point, never bundled into the base cost
----
+ damage(wielderStrength: Integer): Integer
	// a Strength-based weapon adds the wielder's Strength rank to its Damage rank
	// breaks when the wielder exerts Strength greater than its Toughness
+ extendCriticalRange(): Weapon
	// 1 equipment point per +1 critical threat range

## **Armor** : Equipment

+ Armor(protection: Integer)
	// Toughness from armor never exceeds the series power level
------
+ protection: Integer
	// equipment armor bonuses never stack; only the highest applies
+ isLimitedToBallistic: Boolean

## **Vehicle** : Equipment

+ Vehicle(size: VehicleSize, speed: Integer)
	// standard amenities cost nothing
	// several movement modes pay full cost for the most expensive; the others are Alternate Effects
------
+ size: VehicleSize
	// base Strength, Toughness and Defense come from the size category and are never reduced below it
+ strength: Integer
+ speed: Integer
+ defense: Integer
+ toughness: Integer
+ << composition >> features: list[VehicleFeature]
	// a power-effect feature costs one-fifth its normal cost and stays within series power level limits
----
+ addFeature(feature: VehicleFeature): Vehicle
+ shareCost(owners: list[Character]): Vehicle

## **Headquarters** : Equipment

+ Headquarters(size: HeadquartersSize, toughness: Integer)
	// a destroyed headquarters can be rebuilt with the same equipment points; they are never lost with it
------
+ size: HeadquartersSize
	// starts at Small for no points; 1 point per step up, 1 point back per step below Small
+ toughness: Integer
	// starts at 6; 1 point per +2
+ powerLevel: Integer
+ << composition >> features: list[HeadquartersFeature]
	// each feature costs 1 equipment point; a power-effect feature never exceeds twice the headquarters power level
----
+ addFeature(feature: HeadquartersFeature): Headquarters
+ rebuild(): Headquarters
+ shareCost(owners: list[Character]): Headquarters

## **Construct**

+ Construct(abilities: Abilities)
	// has no Stamina and lacks either Intellect and Presence (automaton) or Strength and Agility (immobile intellect)
	// immune to Fortitude-resisted effects unless the effect works on objects
------
+ << association >> abilities: Abilities
+ kind: ConstructKind
+ lastOrder: Order
----
+ command(order: Order): Construct
	// a move action for the owner; without new orders it follows the last order given
+ repair(): Construct
	// never recovers on its own; repaired with the Technology skill
	-> technologySkill.check
