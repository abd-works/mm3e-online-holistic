## Language

*Device* — A Device is the central concept of powered, character-owned gear in MM3E — the bridge between the character's power point investment and a physical item that can be taken away. It owns the definition of what makes an item a device (it is a power with the Removable or Easily Removable flaw applied), the rules for temporary use without power-point cost, and the recovery rules when a device is lost. Device interacts with the Equipment advantage (which it contrasts with), with the Removable and Indestructible modifiers (which govern its vulnerability), and with inventing and jury-rigging (which produce temporary devices). The invariant that defines a Device is that it must always be traceable to a power effect paying power points; an item with no power-point cost is not a device — it is equipment.

### device

- A device is an item providing a power effect or set of effects; mechanically it is a power with the Removable or Easily Removable flaw applied.
- Devices may originate from advanced science, magic, alien technology, or psychic power; all work identically in game terms regardless of origin or descriptor.
- A device is a permanent part of the character's trait set — the character pays power points for it; if lost or destroyed the character can replace it.
- Unlike mundane equipment, devices grant effects beyond normal technology and are only ever taken away temporarily.
- Characters may temporarily use a device for a single scene or adventure without paying power points; continuing use requires purchasing the device as a regular power.
- The GM may require a hero point to temporarily use a device belonging to another character.
- Records the character's power-point payment at cost reduced by the Removable or Easily Removable flaw ratio.
- Grants its power effects to the owner whenever the owner has possession of the device.
- Suspends all its power effects immediately when removed from the owner's possession.
- Restores all its power effects immediately when the owner recovers the device.
- Permits a non-owner to use the device for one scene without transferring power points.
- Permits the character to replace a permanently lost device because the power points remain spent on the character's sheet.
- **Invariant:** must carry either Removable or Easily Removable as a flaw; a power without that flaw is not a device.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_158.md`

### Removable

- Removable is a flaw applied to powers that are external to the character, making the power dependent on an item that can be taken away.
- Applying Removable reduces the power's point cost to reflect the vulnerability of losing access.
- When the device is taken away the character loses those powers until the item is recovered.
- Devices are defined as powers with the Removable or Easily Removable flaw; without one of these flaws the power is internal, not a device.
- Reduces the point cost of its host power by the Removable flaw's cost-reduction ratio.
- Flags the device as one that opponents can physically take from the character during play.
- Triggers power-loss for the host power when the device is removed from the character's possession.
- Triggers power-restoration when the character recovers the device.
- **Invariant:** cannot be applied to a power that has no physical item form; internalized powers cannot carry this flaw.

### Easily Removable

- Easily Removable is a more severe form of the Removable flaw — the device can be stripped away even more readily.
- The greater vulnerability to loss is reflected in a larger point-cost reduction compared to standard Removable.
- Items that are easily grabbed, small, or designed so opponents can quickly take them qualify for Easily Removable.
- Reduces the point cost of its host power by a larger ratio than standard Removable.
- Flags the device as one that opponents can strip away with minimal effort or contest.
- Applies the same power-loss and power-restoration triggers as Removable, with a faster stripping threshold.
- **Invariant:** applies only to items that are small, loosely carried, or designed for quick removal; bulky or worn gear qualifies for standard Removable instead.

### Indestructible

- Indestructible is a modifier applied to a Removable or Easily Removable device indicating the item cannot be permanently destroyed.
- An Indestructible device can still be taken away but cannot be eliminated through destruction.
- Applying Indestructible costs additional points (reducing the benefit of the Removable flaw) because the item is less vulnerable overall.
- Reduces the flaw-based cost discount on the device it modifies by the Indestructible surcharge.
- Prevents the device from being permanently eliminated from play through any destructive means.
- Allows the device to be taken but guarantees the character can always recover it eventually.
- **Invariant:** can only be applied to a device that already carries Removable or Easily Removable; cannot make an equipment item indestructible.

### battlesuit

- A battlesuit (power armor) is an advanced suit of technological or magical armor granting the wearer power effects structured as a Removable device.
- Common battlesuit powers: Protection (possibly Impervious or Sustained), attack effects (Damage, often as Alternate Effects), Immunity to environmental hazards, movement (Flight, Leaping, Swimming), Senses (darkvision, radio, infrared, GPS, time sense), and Enhanced Strength.
- The battlesuit is the prototypical device: integral to the character's concept, powers the wearer beyond mundane capability, only ever taken away temporarily.
- Bundles Protection, Damage, movement, and Senses effects into a single Removable device instance.
- Loses all bundled powers simultaneously when removed from the wearer.
- Accepts Alternate Effect structures for multiple attack modes under one device cost.
- **Invariant:** all powers listed on the battlesuit are lost together when the battlesuit is away — no selective availability.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_159.md`

### costume

- A costume may be made of unusual materials (super-science or magic) giving it a Protection effect beyond ordinary clothing.
- Costumes may serve as the source of a hero's powers (e.g., a battlesuit is a specialized powered costume).
- Comic book costumes are conventionally immune to the wearer's own powers; this is a descriptor costing no points.
- Grants Protection from its material (device-grade, stacks with non-equipment Protection bonuses) when purchased as a device.
- Applies the no-cost immunity-to-own-powers descriptor to all costumes by default in standard play.
- May serve as the physical housing for any other device effect the character carries.
- **Invariant:** the immunity-to-own-powers descriptor costs nothing and is assumed unless the GM rules otherwise.

### enhanced equipment

- Enhanced equipment is normal equipment given special properties through magic or super-science, crossing from equipment into the device category.
- Examples: magical weapons with greater Damage bonuses, magical armor with greater Protection, equipment using super-alloys or bulletproof cloth.
- The line from equipment to device is crossed when item properties exceed what the real world can produce.
- Exceeds the real-world technology ceiling in at least one property to qualify as a device.
- Acquires device status at the point its properties become impossible without magic or super-science.
- Carries the same Removable (or Easily Removable) flaw structure as any other device once it qualifies.
- **Invariant:** the crossing point is the real-world technology ceiling; items on the mundane side remain equipment regardless of rarity or cost.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_160.md`

*Equipment* — The Equipment KA governs the acquisition and use of mundane items in the game. It owns the concept of an equipment point pool derived from the Equipment advantage, the rules for what qualifies as adventuring equipment (and therefore requires payment), and the constraints on equipment's effectiveness relative to devices and powers. Equipment interacts with Device (it is the contrasting concept: mundane vs. powered) and with the Weapon, Armor, Vehicle, and Headquarters KAs (which define what can be purchased as equipment). The fundamental invariant is that equipment is bounded by real-world technology; anything exceeding that boundary becomes a device.

### equipment

- Equipment covers mundane items — ordinary real-world things — that supplement a character's traits without granting powers per se.
- Equipment is acquired using equipment points from the Equipment advantage; each piece has a point cost.
- Equipment is limited to technology commonly available in the setting; the GM decides what qualifies.
- Equipment bonuses do not stack with each other or with other bonus types; only the highest bonus applies.
- Equipment cannot benefit from extra effort; a hero point must be spent instead for equipment stunts.
- Equipment is subject to damage, malfunction, and loss; the GM may declare it fails as a complication.
- Grants benefits as equipment-type bonuses up to the real-world technology ceiling.
- Applies its bonus only if it is the highest equipment bonus of its type currently in effect.
- Becomes unavailable when destroyed, lost, or declared a complication by the GM with no power-point recovery.
- Cannot be used with extra effort; a hero point is the only way to perform an equipment stunt.
- **Invariant:** benefits must remain within real-world technology; any item whose benefits exceed the ceiling is a device, not equipment.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_162.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_164.md`

### Equipment advantage

- The Equipment advantage is the character trait that grants equipment points for purchasing items.
- Characters pay each item's point cost from their equipment points and can thereafter own and use that item.
- An item's cost is based on its effects and features, just as a power's cost is based on effect rank and modifiers.
- Maintains the character's equipment point pool; the pool size equals the advantage's benefit level.
- Validates each item purchase against the remaining pool balance before allowing it.
- **Invariant:** the pool cannot be exceeded; purchases that would overspend the pool are not allowed.

### equipment point

- An equipment point is the unit of currency for purchasing items via the Equipment advantage; the pool size is determined by ranks in the advantage.
- Every piece of equipment has a point cost; the character pays it and can thereafter own and use the item.
- Equipment points are distinct from power points: equipment points buy mundane gear and vehicles; power points buy devices and character traits.
- Functions as the unit of exchange for all equipment purchases (gear, vehicles, headquarters).
- Decrements the character's equipment pool when spent; the pool does not regenerate outside advancement.
- Converts vehicle and headquarters power effects to one-fifth their normal power-point cost for purchasing purposes.
- **Invariant:** vehicle and HQ power effects always cost one-fifth the normal amount in equipment points regardless of effect type.

### Alternate Equipment

- Alternate Equipment is an array of items usable only one at a time, analogous to Alternate Effect for powers.
- Cost: full price for the most expensive item, 1 equipment point per additional item of equal or lesser cost.
- The utility belt is the classic example: a collection of tools and weapons available situationally but not simultaneously.
- Spending a hero point allows temporarily adding an item to the array for one scene.
- Activates exactly one item from its array at any given time; deactivates all others simultaneously.
- Charges full price for the most expensive item in the array and 1 point per additional item.
- Allows a hero-point stunt to add a non-array item for one scene without adding it permanently.
- **Invariant:** only one array item can be active at a time; selecting a new item deactivates the previous one.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_163.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_166.md`

### on-hand equipment

- On-hand equipment allows a character to spend a hero point to have a particular item available in a scene without having planned ahead.
- It functions as an equipment power stunt for one scene; the GM decides whether having the item is plausible given the situation.
- The same rule applies to vehicles and replacement items.
- Produces a specific item for one scene after the character spends a hero point.
- Leaves the plausibility determination entirely to the GM; no rules enforce when this is possible.
- Applies to vehicles and replacement items under the same hero-point stunt rule.
- **Invariant:** on-hand equipment is always one-scene; continued use requires purchasing the item through normal means.

*Invention* — Invention is the system that allows characters to create temporary devices on the fly, bypassing the normal power-point acquisition process at the cost of time, skill, and sometimes luck. It owns the design-and-construction workflow (two sequential Technology checks with time requirements scaled to power-point cost), the jury-rigging emergency shortcut (skip design, spend a hero point, compress construction to rounds at higher DC), and the ritual variant (same workflow but using Expertise: Magic for characters with the Ritualist advantage). Invention interacts with Device (invented items are temporary devices), with the Technology skill and Expertise: Magic skill (the check mechanics), and with the hero point economy (the currency for jury-rigging and reuse). The invariant is that invented and jury-rigged devices are temporary — they last one scene; permanent use requires spending power points.

### inventing

- Inventing is the process by which a character with the Inventor advantage creates a temporary device for single-adventure use.
- Requires two sequential checks: Design Check (Technology, DC 10 + point cost, 1 hour/pp) then Construction Check (Technology, DC 10 + point cost, 4 hours/pp).
- Both checks may be routine checks; reducing work time incurs a -5 penalty per -1 time rank reduction.
- The GM makes the design check secretly; 3+ degrees of failure means the design appears correct but won't function.
- A completed invention lasts one scene; reuse costs a hero point or the character spends power points to make it permanent.
- Magical inventions use Expertise: Magic instead of Technology for both checks.
- Executes a two-check workflow: GM makes design check in secret, then player makes construction check.
- Scales both check DCs and time requirements proportionally to the device's power-point cost.
- Allows time reduction by accepting a -5 check penalty per time rank reduced.
- Delivers a working device usable for one scene; permits hero-point reuse or permanent purchase.
- **Invariant:** both checks must be made before the device is available; only jury-rigging can skip the design phase.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_160.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_161.md`

### jury-rigging

- Jury-rigging is an emergency inventing technique that produces a working device immediately by spending a hero point.
- The design check is skipped; construction time compresses to 1 round per power point of cost; the construction DC increases by +5.
- Cannot use routine check when jury-rigging; the check must be rolled.
- A jury-rigged device functions for one scene; each additional use costs one hero point with no further checks.
- Replaces the full inventing workflow by spending a hero point and skipping the design phase.
- Compresses construction time to one round per power point of cost.
- Applies a +5 DC penalty to the construction check.
- Blocks the routine-check option; the construction check must be rolled under pressure.
- **Invariant:** jury-rigged devices last one scene; extension requires another hero point each time.

### ritual

- A ritual is a magical version of inventing available to characters with the Ritualist advantage; uses Expertise: Magic for all checks.
- Research phase: 4 hours per power point of cost; performance phase: 10 minutes per power point.
- Failing the research check makes the ritual unusable; 3+ degrees of failure may result in a mishap.
- Jury-rigging a ritual: spend a hero point, skip research, perform in rounds equal to cost, DC 15 + cost; works for one scene.
- Substitutes Expertise: Magic for Technology in both the design (research) and construction (performance) checks.
- Applies the same DC formula (10 + pp cost) for research and performance checks.
- Triggers a potential mishap at 3+ degrees of failure on the research check.
- Converts to jury-rig mode at the cost of one hero point, compressing to rounds per point at DC 15 + cost.
- **Invariant:** 3+ degrees of failure on research prevents the ritual from being performed and may cause adverse consequences.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_162.md`

*Weapon* — The Weapon KA owns the equipment-grade offensive tools available to heroes and villains: melee weapons (hand-held close combat weapons with Strength-based Damage), ranged weapons (thrown and projectile weapons spanning simple pistols to rocket launchers), grenades (thrown area-effect weapons), and explosives (placed area-damage devices). It interacts with the Equipment KA (weapons are purchased with equipment points) and the Device KA (magical or super-scientific weapons are devices, not equipment). Weapons each carry four traits: category, effect, critical threat range, and point cost; this structure is uniform across melee, ranged, grenade, and explosive types.

### melee weapon

- A melee weapon is a hand-held close-combat weapon, typically with Strength-based Damage adding the wielder's Strength rank to the weapon's damage rank.
- Ordinary melee weapons break if the wielder's Strength exceeds the weapon's Toughness (4 for wood, 7-8 for metal).
- Categories: simple (brass knuckles, club, knife, pepper spray, stun gun), archaic (battleaxe, sword, spear, warhammer), exotic (chain Reach 2 + Improved Grab/Trip; chainsaw non-Strength; nunchaku; whip Reach 3 + Improved Grab/Trip).
- Critical threat range can be extended by 1 for 1 equipment point (same cost as Improved Critical advantage).
- Adds the wielder's Strength rank to its Damage rank for all Strength-based variants.
- Breaks when the wielder exerts Strength greater than the weapon's Toughness rating.
- Assigns one of three categories (simple, archaic, exotic) that determines which mechanical properties the weapon may have.
- Allows critical threat range extension at 1 equipment point per +1 range (up to Improved Critical advantage value).
- **Invariant:** each melee weapon carries exactly four traits — category, effect, critical range, and cost — none are optional.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_167.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_168.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_169.md`

### ranged weapon

- Ranged weapons include thrown weapons (Strength-based Damage) and projectile weapons (not Strength-based): bows, crossbows, guns, energy weapons.
- Categories: Projectile Weapons, Energy Weapons (blasters, taser), Heavy Weapons (flamethrower, grenade launcher, rocket launcher), Thrown Weapons (bolos, boomerang, javelin, shuriken).
- Shuriken are thrown but not Strength-based (too light); boomerangs return to the thrower's hand next round (descriptor, not a power).
- Weapon accessories (laser sight, stun ammo, suppressor, targeting scope) cost 1 equipment point each.
- Applies Damage independently of the wielder's Strength for projectile and energy weapons.
- Adds the wielder's Strength rank to Damage for thrown weapons (Strength-based thrown category).
- Returns to the wielder's hand on the next round for boomerangs as a descriptor with no power cost.
- Accepts optional accessories at 1 equipment point each that modify attack or damage properties.
- **Invariant:** accessories are purchased separately at 1 point each and are never bundled into the weapon's base cost.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_170.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_171.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_172.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_173.md`

### grenade

- A grenade is a thrown area-effect weapon affecting all targets within a burst or cloud area; targets beat a Dodge DC to halve or avoid effects.
- Types: fragmentation (Burst Area Damage 5, DC 15), smoke (Cloud Area Concealment Attack), flash-bang (Burst Area Dazzle 4), sleep gas (Cloud Area Affliction — fatigued/exhausted/asleep), tear gas (Cloud Area Affliction — dazed/vision-impaired, stunned/vision-disabled, incapacitated).
- Delivers its effect to all targets in the burst or cloud area simultaneously on a successful throw.
- Requires each affected target to beat the Dodge DC to halve or avoid the effect.
- Maintains cloud area effects for multiple rounds until the cloud disperses.
- **Invariant:** grenades are thrown weapons; they use the same throw rules and range penalties as other thrown items.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_175.md`

### explosive

- An explosive is a non-thrown area-damage device placed or delivered by other means.
- Types: dynamite (Burst Area Damage 5 per stick) and plastic explosive (Burst Area Damage 10 per 1-lb block); each doubling of quantity increases Damage rank by 1.
- Explosives have a Dodge DC that targets beat to halve damage from the burst area.
- Requires placement or delivery rather than throwing to deploy.
- Scales its Damage rank upward by 1 for each doubling of quantity used.
- Applies the same Burst Area Dodge-for-half mechanic as grenades but is not a thrown weapon.
- **Invariant:** each doubling of explosive material increases Damage rank by exactly 1; the scaling is logarithmic, not linear.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_174.md`

*Armor and Defense* — The Armor and Defense KA owns the protective gear that characters wear or carry — armors (which add a Protection bonus to Toughness) and shields (which grant active defense bonuses to Dodge and Parry). It also owns the Toughness bonus concept, which is the mechanical output of armor: a stacking-restricted bonus to Toughness. This KA interacts with the Device KA (super-shields and battlesuits are device versions of shield and armor concepts), with the Vehicle KA (vehicles can have armor features), and with the power level rules (Toughness from equipment cannot exceed power level).

### armor

- Armor provides a Protection effect, granting a bonus to Toughness to resist damage.
- Categories: archaic (leather Prot 1, chain-mail Prot 3, plate-mail Prot 5, full-plate Prot 6), modern (undercover shirt Prot 2 Limited/Ballistic/Subtle; bulletproof vest Prot 4 Limited/Ballistic/Subtle).
- Equipment armor bonuses do not stack with other armor or Protection bonuses; only the highest applies.
- Toughness from armor cannot exceed the series' power level limit.
- Provides a Protection bonus to Toughness counted as an equipment-type bonus.
- Restricts modern armor's Protection to ballistic damage via the Limited modifier.
- Applies its bonus only if it is the single highest equipment Toughness bonus currently in effect.
- **Invariant:** equipment armor bonuses never stack — only the highest applies regardless of how many armors are worn.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_175.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_177.md`

### shield

- A shield grants active defense bonuses (Enhanced Dodge and Parry) functioning as mobile cover rather than passive Protection.
- Sizes: small (+1 active defenses, 2 points), medium (+2 active defenses, 4 points), large (+3 active defenses, 6 points).
- Super-shields are device versions; their Protection stacks with other effects (not equipment-based) and can be Impervious or Sustained.
- A super-shield can be an Alternate Effect weapon (Damage, Strength-based or Ranged) — offensive and defensive modes cannot be active simultaneously.
- Provides Enhanced Dodge and Enhanced Parry as active defense bonuses (mobile cover mechanic).
- In device (super-shield) form, provides Protection that stacks with non-equipment bonuses.
- Supports an Alternate Effect attack mode; offensive and defensive modes are mutually exclusive.
- **Invariant:** a shield's active defense bonus cannot be used while the shield is deployed as an Alternate Effect offensive weapon.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_176.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_178.md`

### Toughness bonus

- The Toughness bonus is the bonus to Toughness granted by the Protection effect from armor or similar sources.
- Equipment-sourced Toughness bonuses do not stack with each other or with non-equipment bonuses; only the highest applies.
- Device-based Protection (battlesuits, super-shields) stacks with other effects because it is not an equipment bonus.
- Toughness, even when granted by armor, is capped by the series' power level.
- Distinguishes between equipment-type and device-type Toughness bonuses for stacking purposes.
- Caps at the series power level regardless of the combined total from any source.
- Allows device-based Protection to stack on top of equipment armor Protection (they are different bonus types).
- **Invariant:** equipment Toughness bonuses never stack with each other; device Toughness bonuses follow normal stacking rules and are separately PL-capped.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_164.md`

*Vehicle* — The Vehicle KA owns transportation devices acquired as equipment. It governs the five-trait model (Size, Strength, Speed, Defense, Toughness) through which vehicles are purchased and upgraded, the size-based stat derivation table, and the full menu of vehicle features. Vehicle interacts with the Equipment KA (vehicles cost equipment points), the Device KA (vehicles can have power effects), and the Headquarters KA (both use shared/alternative ownership patterns). The invariant is that a vehicle's standard amenities cost nothing and that vehicles with multiple movement modes must pay full cost for the most expensive, acquiring others as Alternate Effects.

### vehicle

- A vehicle is a transportation device acquired as equipment with five traits purchased at equipment point cost: Size, Strength, Speed, Defense, and Toughness.
- Base cost is the Speed movement effect; other traits, features, and powers cost additional points.
- Vehicles with multiple movement modes pay full cost for the most expensive and acquire others as Alternate Effects.
- Teams may pool equipment points to share a vehicle, dividing cost as they see fit.
- Alternate Vehicles: pay full cost for the most expensive, 1 point per additional vehicle of equal or lesser cost.
- Sets base trait values for Strength, Toughness, and Defense from its size category.
- Charges the full cost of the most expensive movement mode; additional movement modes are Alternate Effects.
- Permits a team to divide equipment point cost among members in any agreed proportion.
- Allows a hero-point stunt to produce a non-primary vehicle for one scene.
- **Invariant:** standard amenities (seating, seatbelts, radio, headlights, climate control) are included at no additional point cost.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_178.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_179.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_181.md`

### vehicle size

- Vehicle size is measured in categories from Medium (default) upward: Large, Huge, Gargantuan, Colossal, Awesome.
- Size determines base Strength, Toughness, and Defense values (Awesome: Str 20/Tgh 15/Def -12; Medium: Str 0/Tgh 5/Def 0).
- Larger vehicles have greater Strength and Toughness but a Defense penalty (easier to hit); penalty can be bought off at 1 point per -1 removed.
- Each size increase costs 1 equipment point.
- Determines the vehicle's baseline Strength, Toughness, and Defense from a fixed category table.
- Applies a Defense penalty for vehicles larger than Medium; larger vehicles are easier to target.
- Allows the Defense penalty to be bought off at 1 equipment point per -1 penalty removed.
- **Invariant:** baseline Strength, Toughness, and Defense values per size category are fixed; they may be improved above baseline but not reduced below it.

### vehicle feature

- Vehicle features are optional extras each costing 1 equipment point; standard features include Alarm (Technology DC 20), Caltrops dispenser, Hidden Compartments (Perception DC 20), Navigation System (+5 navigation), Oil Slick (DC 15 Vehicles check), Remote Control.
- Some features are power effects: Armor (Protection), Cloaking Device (Concealment 4 or 8 points), Immunity (environmental hazards), Smokescreen (Cloud Area Concealment Attack, 12 points), Weapons (Damage effects).
- Vehicle power effects cost one-fifth normal power-point cost, paid in equipment points.
- Charges one equipment point per feature for standard non-power features.
- Charges one-fifth normal power-point cost for power-effect features (converted to equipment points).
- Allows any appropriate power effect as a vehicle feature within the converted cost structure.
- **Invariant:** vehicle power effect ranks may not exceed limits derived from the series power level.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_180.md`

*Headquarters* — The Headquarters KA owns fixed bases of operation — from underground caves to orbiting satellites — acquired as equipment. It governs the two primary traits (Size and Toughness) and the menu of features that define a base's capabilities. Headquarters interacts with the Vehicle KA (both share the shared/alternate ownership pattern and feature-based customization), with the Equipment KA (all costs are equipment points), and with the Construct KA (HQ computers may be AI constructs). The invariant is that a headquarters power level caps the strength of power-effect features at twice the PL, and that a destroyed headquarters can always be rebuilt using the same equipment points.

### headquarters

- A headquarters is a base of operations purchased as equipment with equipment points.
- Teams may pool equipment points to share a headquarters; cost is divided as members see fit.
- Alternate Headquarters: pay full cost for the most expensive, 1 point per additional HQ of equal or lesser cost.
- If destroyed, the owner may rebuild it with the same features or build a new one using the same equipment points.
- The HQ power level governs certain feature strengths; for player characters it equals the series power level.
- Starts at Small size for zero points; each size step up costs one additional equipment point.
- Maintains a feature menu that defines the base's capabilities; each feature costs one point.
- Permits a team to divide equipment point cost among members in any agreed proportion.
- Can be rebuilt after destruction using the same equipment points; the character never permanently loses those points with the structure.
- **Invariant:** if destroyed, the character may rebuild to the same specifications or choose different features; the equipment points are retained.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_186.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_187.md`

### headquarters size

- HQ size categories range from Fine/Miniscule (-4 points) upward through Tiny, Small (default, 0 points), Medium, Large, Huge, Gargantuan, Colossal, Awesome.
- Starting size is Small (house-sized); each size increase costs 1 point; reducing below Small grants 1 extra point per step.
- Colossal is city-block-sized; Awesome is small-town-scale.
- Sets the physical scale of the base from house-sized Small to small-town Awesome.
- Charges 1 point per size increase; grants 1 reclaimed point per step below Small.
- **Invariant:** base Toughness starts at 6 for zero points; increasing Toughness costs 1 point per +2.

### headquarters feature

- Each feature costs 1 equipment point; features with power effects cannot exceed twice the HQ power level.
- Feature list includes: Combat Simulator, Communications, Computer, Concealed (DC+10 to find), Defense System (up to 2x HQ PL), Deathtraps, Dimensional Portal, Dock, Dual Size, Fire Prevention System (Nullify Fire 5), Garage, Gym, Hangar, Holding Cells (Nullify at HQ PL or +50% Toughness), Infirmary, Isolated, Laboratory, Library, Living Space, Personnel, Power System, Sealed, Secret, Security System (DC 20 +5/application, max DC 40), Self-repairing, Temporal Limbo, Workshop.
- Self-repairing taken twice allows the HQ to rebuild within a week if destroyed.
- Caps any power-effect feature rank at twice the HQ power level.
- Sets Defense System attack bonus exactly equal to the HQ power level.
- Increments Security System DC by +5 per additional security application to a maximum of DC 40.
- Charges 1 equipment point per feature regardless of complexity for non-power features.
- **Invariant:** standard structural amenities (doors, windows, power outlets, utilities) are included at no cost and are never charged as features.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_188.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_189.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_190.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_191.md`

*Construct* — The Construct KA owns nonliving beings capable of independent action — robots, androids, animated golems, zombies — acquired via the Minion advantage rather than as equipment. It governs the special build rules that make constructs distinct from living characters: no Stamina (cannot recover, must be repaired), immunity to Fortitude effects unless working on objects, and the mandatory absence of one ability pair (either Intellect+Presence for automatons, or Strength+Agility for immobile intellects). It interacts with the Equipment KA (constructs are explicitly not equipment), with the Device KA (constructs are not devices), and with the Headquarters KA (HQ AI computers are a construct variant).

### construct

- A construct is a nonliving being (robot, android, golem, zombie) capable of action; treated as a Minion, not equipment or a device.
- Constructs are created like other characters but have no Stamina (do not recover — must be repaired) and are immune to Fortitude-resisted effects unless the effect works on objects.
- Constructs lack either (a) Intellect and Presence — automatons, immune to Will and interaction effects — or (b) Strength and Agility — immobile intellects that cannot perform physical actions.
- Loss of three abilities (-30 points) plus Immunity to Fortitude effects (+30 points) nets to zero extra cost.
- Constructs can have skills, advantages, and power effects like other characters but cannot take those requiring absent abilities.
- Owner commands a construct as a move action; in the absence of new orders the construct follows the last order given.
- Builds using the Minion advantage rules as a full character, not as equipment or a device.
- Forces the absence of one ability pair (Intellect + Presence for automatons, or Strength + Agility for immobile intellects).
- Grants immunity to all Fortitude-resisted effects unless the effect specifically targets objects.
- Must be repaired using the Technology skill after taking damage; never recovers naturally.
- Executes the owner's most recent order when no new command has been given.
- **Invariant:** loss of three ability ranks (-30 pp) plus Immunity to Fortitude effects (+30 pp) nets to exactly zero extra cost; constructs are not more expensive than living characters.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_194.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_195.md`

### animated object

- An animated object is a construct variant in which a normally inanimate object (golem, magically-animated skeleton, enchanted armor) has been given the capacity for action through magic.
- As a construct it has no Stamina, does not recover from damage, and is immune to Fortitude-resisted effects.
- Animated objects are typically automatons — lacking Intellect and Presence — that obey literal commands without creativity or initiative.
- Executes orders literally without improvisation or creativity (automaton behavior default).
- Cannot interpret ambiguous commands; does only exactly what it is literally told.
- **Invariant:** has no Intellect or Presence ranks; is immune to Will effects and interaction skills.

### robot

- A robot is a construct variant driven by technology (armored robots, androids, mechanical drones).
- Robots with Intellect and Presence ranks can interpret orders and improvise; may be intelligent but non-sentient (Intellect without Presence) or fully self-aware.
- Robots without Strength and Agility ranks are immobile intellects (AI computers) capable only of directing other constructs.
- Robots do not recover from damage; they must be repaired using the Technology skill.
- Ranges in intelligence from simple automaton to full artificial sentience depending on purchased ability ranks.
- In immobile-intellect form (no Strength or Agility), can direct other constructs but cannot perform physical actions.
- Requires the Technology skill for all repair after damage; the skill user's check result determines repair extent.
- **Invariant:** same no-Stamina, Immunity to Fortitude, and no-recovery rules from the construct base apply to all robot variants without exception.

*Boundary terms*

### power effect

- Equipment and devices are built using power effects (Damage, Protection, Features, Affliction, etc.) with their standard costs.
- Device power effects cost the same as non-device powers but are reduced by the Removable or Easily Removable flaw.
- Vehicle and headquarters power effects cost one-fifth normal because they are paid in equipment points.
- This module defines that vehicle and HQ power effects cost one-fifth of the normal power-point amount when converted to equipment points.
- The Powers module owns the power effect definitions (Damage, Protection, Affliction, Concealment, etc.) and their standard costs, DCs, and saving throws.
- This module enforces: when a vehicle or HQ includes a power effect feature, the equipment point cost = normal power cost ÷ 5; the Powers module enforces the effect's in-play mechanics (resistance checks, area calculations, durations).
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_158.md`

### power points

- Devices (powers with Removable flaws) are paid for with power points reduced by the Removable discount.
- A character who permanently loses a Removable device may reallocate those power points.
- Constructs are created as characters using power points in the normal creation pool.
- This module defines the Removable flaw discount applied when a device is purchased: the power's point cost is reduced by the flaw ratio.
- Character Construction owns the total power-point budget and the rules for spending and tracking power points.
- This module enforces: device pp cost = power base cost minus Removable/Easily Removable reduction; if permanently lost, those pp remain spent on the sheet (character retains them and can replace the device).
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_158.md`

### Strength

- Melee weapon damage is typically Strength-based: the wielder's Strength rank adds to the weapon's Damage rank.
- Weapon breakage occurs when the wielder's Strength exceeds the weapon's Toughness.
- A vehicle's Strength determines carrying capacity and can be increased above the size-based default for 1 point per rank.
- The Abilities module defines the Strength trait, its rank range, and how it contributes to checks and damage.
- This module defines the melee weapon Strength-based Damage formula (weapon Damage rank + wielder Strength rank) and the weapon breakage rule (wielder Strength > weapon Toughness → break on use).
- This module also defines the vehicle Strength trait (carrying capacity) and its upgrade cost (1 point per +1 rank above size default); the Abilities module enforces the Strength rules in all other contexts.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_167.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_178.md`

### Technology skill

- Technology is used for both the design and construction checks in inventing.
- Technology checks are also used to repair damaged equipment and constructs, and to bypass vehicle alarms and security systems.
- The Skills module defines the Technology skill and the general rules for how skill checks work (modifier, DC, degrees of success).
- This module defines the inventing workflow that depends on Technology: Design DC = 10 + pp cost (1 hr/pp); Construction DC = 10 + pp cost (4 hr/pp); routine checks allowed; time reduction at -5 per rank.
- This module also enforces Technology as the repair skill for constructs and damaged equipment, and the skill used to bypass alarm systems (DC 20 base for most vehicle and HQ security).
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_160.md`

### Minion advantage

- Constructs are acquired via the Minion advantage (or summoned via the Summon power effect); they are full characters, not equipment-point purchases.
- The Minion advantage is distinct from the Equipment advantage.
- The Advantages module defines the Minion advantage and the rules for what a minion may do and how it is acquired.
- This module defines the construct — the specific kind of minion produced when the Minion advantage is used to create a nonliving being.
- This module enforces the construct-specific traits (no Stamina, one ability pair absent, Immunity to Fortitude) that apply to minions of construct type; the Advantages module enforces the general minion rules (loyalty, command, minion defeat).
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_194.md`
