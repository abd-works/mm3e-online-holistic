
---

# power

- **Purpose:** turn a player's named power into the effects, modifiers and descriptors the rules run on, and price it in power points from base cost, rank and modifier math.
- **Seam (terms):** Power, Effect, Modifier, Descriptor, Array, AlternateEffect
- **Dependencies (one-way):** character-construction (power point, rank), check-resolution (resistance check), combat (Toughness, Fortitude, Will, Dodge)

## Constraint

Callers build and change a power only through its effects, modifiers and arrays, and read its cost; they never set cost per rank or total cost directly. Power points are spent and power level limits enforced by character-construction, not here.

## **Power**

+ Power(name: String, effects: list[Effect], descriptors: list[Descriptor])
	// always holds at least one effect and at least one descriptor
	// is approved by the Gamemaster before play
------
+ name: String
+ << composition >> effects: list[Effect]
+ << composition >> descriptors: list[Descriptor]
+ << composition >> modifiers: list[Modifier]
	// Activation and Removable apply to the whole power, never to one effect in it
+ isApproved: Boolean
+ totalCost: Integer
	// always the sum of each effect's total cost plus the power's flat modifiers, and never below 1 power point
----
+ acquireEffect(effect: Effect): Power
	// each effect pays its own cost, whatever power it is grouped under
	-> powerPoints.spend
+ applyModifier(modifier: Modifier): Power
	// a flat flaw such as Activation or Removable lowers the total; the total never drops below 1
+ activate(): Power
	// with Activation, the activation action is spent before any effect is available, and again after the power is nullified or deactivated

## **Effect**

+ Effect(name: EffectName, powerType: PowerType, rank: Integer)
	// at any time it has exactly one power type, one action, one range, one duration and one cost per rank
	// its power type is never changed by a modifier
------
+ name: EffectName
+ powerType: PowerType
+ action: Action
+ range: Range
+ duration: Duration
+ resistance: DefenseName
+ rank: Integer
+ baseCost: Integer
	// set by the rules for the effect, always 1 or more, and never changed in play or by a modifier
+ << composition >> modifiers: list[Modifier]
+ costPerRank: Integer
	// always base cost plus per-rank extras minus per-rank flaws, and never below 1 power point per rank
+ totalCost: Integer
	// always cost per rank × rank, then flat extras added and flat flaws taken away
+ isActive: Boolean
----
+ applyModifier(modifier: Modifier): Effect
	// an extra is refused for a property the effect already has
+ counter(): Effect
	// countering suppresses the effect; it never destroys it, and the effect can be reactivated on its next action
	-> array.counter

## **Modifier**

+ Modifier(name: ModifierName, isExtra: Boolean, isFlat: Boolean, value: Integer)
	// an extra must grant a genuine improvement; a flaw must restrict the effect about half the time or more; a cosmetic change is a descriptor, not a modifier
------
+ name: ModifierName
+ isExtra: Boolean
+ isFlat: Boolean
	// a per-rank modifier changes cost per rank; a flat modifier changes the total after cost per rank × rank
+ value: Integer
+ appliesToWholePower: Boolean

## **Descriptor**

+ Descriptor(name: String, kind: DescriptorKind)
	// costs no power points and is never changed without Gamemaster approval
------
+ name: String
+ kind: DescriptorKind
	// origin descriptors rarely carry mechanics; source descriptors decide what Nullify counters and Immunity blocks

## **Array**

+ Array(primary: Effect, alternates: list[AlternateEffect])
	// holds a primary effect and at least one alternate effect
	// only one effect of the array is active at a time, except dynamic alternates sharing the array's points
------
+ << composition >> primary: Effect
+ << composition >> alternates: list[AlternateEffect]
+ activeEffect: Effect
----
+ switchTo(effect: Effect): Array
	// a free action, once per turn
+ counter(): Array
	// when any effect of the array is nullified or disabled, every effect of the array is affected the same way
+ reallocate(effect: Effect, points: Integer): Array
	// only among dynamic alternates, once per turn as a free action; the combined allocation never exceeds the array's points

## **AlternateEffect**

+ AlternateEffect(effect: Effect, isDynamic: Boolean)
	// its total cost never exceeds the primary effect's total cost
	// a permanent effect is never an alternate effect
------
+ << association >> effect: Effect
+ isDynamic: Boolean
+ flatCost: Integer
	// 1 point for an alternate effect, 2 for a dynamic alternate effect (and 1 more to make the primary dynamic)
