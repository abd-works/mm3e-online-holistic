*Boundary terms* — Terms combat uses but does not define; each is owned by another module.

### condition

- Owned by: Check Resolution
- Conditions (dazed, staggered, stunned, vulnerable, defenseless, incapacitated, dying, prone, hindered, impaired, etc.) are game-state modifiers imposed by combat outcomes, power effects, and hazards.
- Combat causes, references, and escalates conditions; their authoritative definitions and supersession chains live in Check Resolution.
- The dying and incapacitated conditions are triggered by Toughness resistance check outcomes defined in Combat, but their modifier bundles are owned by Check Resolution.
- Combat defines WHEN conditions are imposed (on specific damage degrees, on grab success, on trip success) but does NOT define WHAT the conditions do.
- The condition's modifier bundle (action restrictions, defense reductions, speed changes) is enforced by the consuming system at the point of use — Combat enforces action limits mid-turn; Check Resolution enforces check penalties on each check.
- **Invariant:** A condition's definition and supersession chain is owned by Check Resolution; Combat's role is trigger-only.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_017.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_203.md`

### Toughness

- Owned by: Character Construction
- Toughness is the physical resistance defense stat used as the basis for all Toughness resistance checks against Damage effects.
- Its rank is set during character construction; temporary −1 penalties from failed Toughness checks accumulate in combat and recover with rest.
- Character Construction defines the Toughness rank; Combat applies temporary penalties to that rank through the damage resistance check sequence.
- **Invariant:** Base Toughness rank is set at construction; combat only modifies via temporary cumulative penalties.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_203.md`

### Dodge

- Owned by: Character Construction
- Dodge is the active defense providing the defense class against ranged attacks (Dodge + 10).
- Combat halves Dodge rank (round up) when a character is vulnerable; reduces it to 0 when defenseless.
- Character Construction defines Dodge rank; Combat reads and temporarily modifies it when applying vulnerable or defenseless conditions.
- **Invariant:** Base Dodge is set at construction; Combat applies halving or zeroing only in response to specific conditions.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_208.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_209.md`

### Parry

- Owned by: Character Construction
- Parry is the active defense providing the defense class against close attacks (Parry + 10).
- Combat halves Parry rank (round up) when a character is vulnerable; reduces it to 0 when defenseless.
- Character Construction defines Parry rank; Combat reads and temporarily modifies it when applying vulnerable or defenseless conditions.
- **Invariant:** Base Parry is set at construction; Combat applies halving or zeroing only in response to specific conditions.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_208.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_209.md`

### Fortitude

- Owned by: Character Construction
- Fortitude is the physical resistance defense used for hazard checks (heat, cold, suffocation, disease, poison, vacuum, radiation) and ongoing physical effect resistance checks.
- Character Construction defines the Fortitude rank; Combat uses it as the resistance defense in all hazard check sequences and for physical ongoing effects.
- **Invariant:** Fortitude rank is set at construction; Combat does not modify the base rank.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_200.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_202.md`

### Strength

- Owned by: Character Construction
- Strength provides a built-in close-range Damage effect; its rank adds to Damage rank for Strength-based weapons.
- Strength is used in grab checks (attacker vs. target Strength or Dodge), disarm opposed checks (damage vs. Strength), trip opposed checks (Acrobatics/Athletics vs. Acrobatics/Athletics), and dragging during grab.
- Character Construction defines Strength rank; Combat uses it as both a Damage source and a check modifier in grab, disarm, drag, and falling-catch interactions.
- **Invariant:** Strength rank is defined at construction; extra effort can temporarily increase it by +1 rank.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_203.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_212.md`

### power effect

- Owned by: Power
- A power effect's rank determines the resistance DC (effect rank + 10 for most; Damage uses effect rank + 15).
- Combat resolves power effects when activated as attacks; area and perception-range effects bypass attack checks and automatically affect targets.
- The Power module defines each effect's rank, action, range, duration, and resistance type; Combat reads these properties to resolve the attack check (if any) and resistance check.
- **Invariant:** Effect rank + 10 is the standard resistance DC; Damage effects use effect rank + 15.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_202.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_209.md`

### advantage

- Owned by: Advantages
- Combat advantages (Improved Initiative, Improved Critical, Takedown, Move-by Action, etc.) modify combat mechanics; their definitions and prerequisites are owned by the Advantages module.
- Heroic Feat (a hero point spend) grants temporary access to one rank of an advantage for one turn.
- The Advantages module defines each advantage's prerequisites, rank costs, and behavioral descriptions; Combat applies the mechanical modifications those advantages specify (e.g., Improved Critical extends threat range, Takedown enables additional attacks on minion defeat).
- **Invariant:** Advantage definitions and prerequisites are read-only from Combat's perspective; only behavioral modifications are enforced here.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_020.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_196.md`

