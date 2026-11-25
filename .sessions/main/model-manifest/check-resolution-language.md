## Language

*Core Domain* — The d20 resolution mechanic this module owns: a trait's rank plus a d20 roll and modifiers measured against a Difficulty Class, the check variants (routine, opposed, resistance, team), degrees of success and failure, ranks and measures, hero points, extra effort and power stunts, the basic and combined conditions a character can suffer, reactions, and the people at the table (Gamemaster, player characters, non-player characters).

### Trait

- A trait is any quantifiable game characteristic a character possesses — abilities, skills, advantages, powers, and defenses are all traits.
- Every trait has a rank; rank is the single numeric measure of a trait's effectiveness.
- A check is always a check *of* a trait — "Strength check," "Acrobatics check," "Dodge resistance check" — there is no check without a trait supplying the modifier.
- The Measurements Table translates trait ranks into real-world values (mass, time, distance, volume); traits are what have ranks, so measurements are a property of traits.
- Defenses (Dodge, Parry, Fortitude, Toughness, Will) are traits derived from abilities; they supply the DC or the modifier for resistance and attack checks.
- Other modules (Ability, Skill, Power, Advantage) define *specific* traits; the abstract concept of what a trait is — a quantifiable characteristic with a rank — belongs here.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_008.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_009.md`

### d20

- The game uses a single twenty-sided die (d20) to resolve actions.
- "d20+2" means roll the die and add two; "d20−4" means roll and subtract four.
- The die can also express percentages in increments of 5% (multiply the face value by 5).
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_004.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_005.md`

### check

- A check is d20 + trait rank (plus any additional modifiers) vs a Difficulty Class (DC); equaling or exceeding the DC is success, below is failure.
- Whenever a character attempts something where the outcome is in doubt, it requires a check of an appropriate trait — ability, skill, power, etc.
- Additional modifiers come from circumstances, advantages, or power effects layered on top of the trait rank.
- A natural 20 on a check is a critical success: determine the degree normally, then increase it by one degree; this can turn a failure into a success.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_005.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_009.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_010.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_011.md`

### Difficulty Class (DC)

- The DC is a number set by the GM that a check result must equal or exceed to succeed.
- A standard difficulty scale runs from Very Easy (DC 0) through Nigh-Impossible (DC 40) in steps of 5.
- In some cases the DC is set by another character's trait (opposed checks) or by an effect's rank (resistance checks, typically 10 + effect rank).
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_005.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_010.md`

### opposed check

- An opposed check pits two characters' check results against each other; the higher result wins.
- On a tie, the character with the higher bonus wins; if bonuses are also equal, roll d20 — 1–10 one character wins, 11–20 the other.
- Routine opposition sets the DC as the opposing character's modifier + 10 (used when the opponent is not actively opposing, e.g. a guard not specifically looking).
- A comparison check compares ranks directly without rolling; the higher rank wins (no luck involved).
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_012.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_014.md`

### resistance check

- A resistance check is d20 + defense bonus vs the hazard's DC (typically 10 + effect rank).
- Resistance checks may be graded, with different outcomes at different degrees of success or failure.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_016.md`

### routine check

- A routine check substitutes a fixed result of 10 for the die roll; the GM decides when circumstances allow a routine check.
- A character with a +10 bonus achieves a routine result of 20, succeeding at DC 20 tasks without rolling.
- If a character's routine result is not sufficient for a task, the player may still roll; the task is by definition not routine for that character.
- Certain game traits change what tasks or situations count as "routine" for a character.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_010.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_011.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_014.md`

### degree of success

- A graded check counts each 5 full points above the DC as one additional degree of success; a bare success is one degree.
- Degrees of success range up to four (DC + 15 or higher).
- A natural 20 (critical success) increases the degree of success by one.
- Some checks specify specific results for each degree of success.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_010.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_013.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_015.md`

### degree of failure

- A graded check counts each 5 full points below the DC as one additional degree of failure; a bare failure is one degree.
- Degrees of failure range down to four (DC − 20 or lower), though more than two degrees of failure rarely matter in practice.
- Specific types of graded checks — notably resistance checks — give defined results for each degree of failure.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_013.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_015.md`

### modifier

- A modifier is a number added to or subtracted from a d20 roll before comparing to the DC.
- The primary modifier comes from the trait's rank; additional modifiers come from circumstances, advantages, or power effects.
- A minor circumstance modifier is ±2; a major circumstance modifier is ±5.
- Missing required tools imposes a −5 penalty; makeshift tools reduce this to −2.
- Circumstance modifiers apply to the check result (not the DC) for consistency.
- Team checks: one leader rolls normally; each helper checks the same trait against DC 10; helper success grants the leader a +2 or +5 circumstance bonus; helper failure can impose a −2 penalty.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_004.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_005.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_015.md`

### rank

- Every quantifiable trait has a rank — the single numeric value measuring that trait's effectiveness.
- Ranks can be negative; each lower rank halves the previous measurement.
- Ranks must not be added directly; convert to measures, add the measures, then convert back to a rank.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_008.md`

### measure

- The Measurements Table maps each rank to mass, time, distance, and volume on a roughly doubling scale.
- Distance Rank = Time Rank + Speed Rank; Time Rank = Distance Rank − Speed Rank; Throwing Distance Rank = Strength Rank − Mass Rank.
- Measurements are approximate, especially at higher ranks — guidelines, not precise values.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_007.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_008.md`

### hero point

- Players start each session with 1 hero point; unspent points do not carry over between sessions.
- Spending a hero point is a reaction (takes no time); a player can spend as many as they have.
- Improve Roll: re-roll any die roll and take the better result; on a 1–10 re-roll, add 10 (so the re-roll always yields 11–20); must spend before the GM announces the outcome.
- Edit Scene: add or change a scene detail with GM approval; cannot undo events that already occurred.
- Heroic Feat: gain one rank of an advantage the hero doesn't already have until end of next turn; fortune advantages excluded; prerequisites must be met.
- Inspiration: receive a hint, clue, or direction from the GM.
- Instant Counter: attempt to counter an effect used against the hero, as a reaction.
- Recover: immediately remove dazed, fatigued, or stunned; convert exhausted to fatigued.
- Heroes earn additional hero points during play from complications, acts of heroism, and roleplaying.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_019.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_020.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_021.md`

### extra effort

- Extra effort is a free action, declared by the player, limited to once per turn.
- Benefits (choose one): additional standard action; +2 circumstance bonus on one check (or upgrade existing bonus to +5); +1 rank to a power effect until start of next turn; power stunt (temporary Alternate Effect lasting until end of scene); additional resistance check against an ongoing effect; retry a failed effect; +1 speed rank until start of next turn; +1 Strength rank until start of next turn.
- Extra effort benefits are not limited by power level.
- Cost: at the start of the turn after using extra effort, the hero becomes fatigued; fatigued → exhausted; exhausted → incapacitated.
- Spending a hero point removes the fatigue cost of extra effort.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_019.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_020.md`

### power stunt

- A power stunt uses extra effort to temporarily gain an Alternate Effect of an existing power.
- The stunt lasts until end of scene or its duration expires, whichever comes first.
- Permanent effects cannot be used for power stunts.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_019.md`

### condition

- A condition is shorthand for a set of game modifiers imposed by effects, injuries, or fatigue.
- If multiple conditions apply, use all of their effects; some conditions supersede lesser ones.
- Each basic condition describes a single game modifier; they are the building blocks of the condition system.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_017.md`

### combined condition

- A combined condition bundles basic conditions under one name; individual constituents can be resolved or superseded independently.
- Example: if an effect removes the dazed part of staggered (dazed + hindered), the character is only hindered.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_018.md`

### dazed

- Limited to free actions and one standard action per turn (player's choice); superseded by Stunned.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_017.md`

### stunned

- Cannot take any actions, including free actions.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_017.md`

### staggered

- Combined condition: dazed + hindered.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_018.md`

### incapacitated

- Combined condition: defenseless + stunned + unaware; generally fall prone.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_018.md`

### dying

- Combined condition: incapacitated + near death; Fortitude DC 15 each round — two degrees of success stabilizes, three total degrees of failure means death; another character can stabilize with Treatment DC 15 or Healing.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_018.md`

### vulnerable

- Active defenses halved (round up); superseded by Defenseless.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_017.md`

### defenseless

- Active defense bonuses become 0; attackers may use routine checks; forgoing routine makes any hit a critical hit.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_017.md`

### impaired

- −2 circumstance penalty on checks (may be scoped); superseded by Disabled for the same trait.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_017.md`

### disabled

- −5 circumstance penalty on checks (may be scoped); superseded by Debilitated for the same trait.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_017.md`

### weakened

- Temporary power point loss in a trait; superseded by Debilitated.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_017.md`

### exhausted

- Combined condition: impaired + hindered; recovers after one hour of comfortable rest.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_018.md`

### fatigued

- The character is hindered; recovers after one hour of rest.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_017.md`

### compelled

- Limited to free actions and one standard action per turn, both chosen by the controller; superseded by Controlled.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_017.md`

### controlled

- All actions each turn are dictated by another character.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_017.md`

### debilitated

- One or more abilities lowered below −5.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_017.md`

### hindered

- Half normal speed (−1 speed rank); superseded by Immobile.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_017.md`

### immobile

- No movement speed; still capable of actions unless another condition prevents it.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_017.md`

### normal

- Unharmed, unaffected, acting normally.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_017.md`

### transformed

- Some or all traits altered by an outside agency; power point total cannot increase but can effectively decrease.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_017.md`

### unaware

- Completely unaware of surroundings; cannot make interaction or Perception checks (may be scoped to specific senses).
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_017.md`

### asleep

- Combined condition: defenseless + stunned + unaware; hearing Perception check (3+ degrees of success) or shaking wakes the character.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_018.md`

### blind

- Combined condition: hindered + visually unaware + vulnerable; may also be impaired or disabled for vision-dependent activities.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_018.md`

### bound

- Combined condition: defenseless + immobile + impaired.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_018.md`

### deaf

- Auditory concealment from the character; may allow surprise attacks.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_018.md`

### entranced

- Combined condition: stunned; any obvious threat breaks the trance; an ally can free with interaction skill check (DC 10 + effect rank).
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_018.md`

### paralyzed

- Combined condition: defenseless + immobile + physically stunned; still aware; can take purely mental actions.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_018.md`

### prone

- −5 close attack penalty for the prone character; opponents get +5 close / −5 ranged attack modifier; character is hindered; standing up is a move action.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_018.md`

### restrained

- Combined condition: hindered + vulnerable; if anchored to an immobile object, immobile instead of hindered.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_018.md`

### surprised

- Combined condition: stunned + vulnerable.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_018.md`

### reaction

- A reaction is a response to something else happening during the round, possibly not on the character's turn.
- Reactions take no significant time and do not count against the character's normal action allotment.
- A character can react as often as circumstances dictate, but only when they dictate.
- Spending a hero point is a reaction.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_016.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_017.md`

### Gamemaster (GM)

- The GM creates adventures, portrays villains and supporting characters, describes the world, and decides the outcome of actions based on die rolls and rules.
- The GM sets the DC for checks based on circumstances.
- The GM decides when a routine check is allowed and how many characters can help in a team check.
- The GM approves Edit Scene hero point spends and provides Inspiration hints.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_006.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_010.md`

### player character (PC)

- A player controls a superhero they have created; they interact with other PCs and with the world and stories created by the GM.
- Players declare extra effort, spend hero points, and choose which actions their heroes take each turn.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_004.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_006.md`

### non-player character (NPC)

- NPCs include villains, supporting cast, thugs, cops — any character controlled by the GM rather than a player.
- Active defenses in combat against NPCs are generally routine opposition (DC 10 + defense).
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_004.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_006.md`

*Boundary Domain* — Terms this module uses but other modules own: the power effect a character resists, the character that holds traits and conditions, power points, complications, advantages and the action round.

### Effect / power effect

- Owned by: Power
- An effect is the basic building block of a power; it describes what a power does in game terms.
- Resistance check DC is typically 10 + effect rank — the effect's rank is what the character resists against.
- Conditions are imposed by power effects (as well as by injuries, fatigue, and environmental hazards).
- Extra effort can increase a power effect by +1 rank; power stunts temporarily create an Alternate Effect.
- Instant Counter (hero point spend) attempts to counter an effect used against the character.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_016.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_019.md`

### Character / hero

- Owned by: Character Construction
- A character is the entity that possesses traits, makes checks, and has conditions applied to it.
- Every rule in this module acts on or through a character — there is no check without a character making it.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_006.md`

### Power points

- Owned by: Character Construction
- A character's power point total is referenced by conditions: Transformed cannot increase it; Weakened temporarily removes power points from a trait.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_017.md`

### Complication

- Owned by: Character Construction
- Heroes earn hero points during play from complications; the complication triggers a setback, the GM awards a hero point in return.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_021.md`

### Advantage

- Owned by: Advantage
- Heroic Feat (hero point spend) grants one rank of an advantage the hero does not already have until end of next turn; fortune advantages are excluded; prerequisites must be met.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_006.md`, `.context/sources/rules/HeroesHandbook-rules__chunk_020.md`

### Action round structure

- Owned by: Combat
- A round is 6 seconds; each character gets one turn per round.
- On a turn: one standard action + one move action (or two move actions) + any free actions + reactions as triggered.
- Standard action: acting upon something (attack, use a power); limited to one per round.
- Move action: movement, drawing weapons, standing up, manipulating objects; taken before or after the standard action but not split around it.
- Free action: minor actions (talking, dropping something, ending or maintaining powers); as many as the GM considers reasonable.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_016.md`
