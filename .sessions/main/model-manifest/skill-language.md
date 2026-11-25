## Language

*Skill* — The Skill abstraction is the core mechanical concept of the module — it defines what a skill is, how it is acquired, and how it is resolved. A skill is a learned ability combining training (ranks) and natural talent (ability modifier); its check is the single resolution path for all skill-based actions: roll d20, add the skill rank, add the ability modifier, add any circumstance modifiers, and compare to a DC. The Skill KA owns the rank economy (1 PP per 2 ranks, split freely across skills), the check formula, the Trained Only gate, and the circumstance modifier concept as it applies within skill use. Skill Mastery is included here because it is a direct enhancement to the skill check resolution — it removes the roll requirement for a nominated skill, granting the routine check result unconditionally. The Skill abstraction is the foundation upon which every named skill (Acrobatics, Deception, etc.) is built; no individual skill makes sense without this mechanical foundation.

### skill rank

- A skill rank is the number of points a character has invested in a skill; it serves as a numerical bonus added to the d20 roll on skill checks.
- Characters with at least one rank in a skill are considered trained in that skill.
- Skills cost 1 power point per 2 ranks; ranks may be split across multiple skills.
- A character with rank 0 in a skill is untrained; some skills may still be used untrained, others cannot.
- Skill rank benchmarks: +5 allows routine DC 15; +10 allows routine DC 20; +15 allows routine DC 25; +30 allows routine DC 40.
- Contributes its numeric value as a direct bonus to the d20 roll on every check for its associated skill.
- Establishes trained status on the skill when its value is 1 or greater.
- Accumulates at a fixed rate of 2 ranks per power point, split freely across any skills at the player's discretion.
- **Invariant:** rank 0 is a valid state representing an untrained skill, not an absent one; the ability modifier still applies when rank is 0.
- **Invariant:** the maximum reachable rank is bounded by the skill modifier limit set at character construction.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_041.md`

### skill check

- A skill check resolves skill use: roll d20 + skill rank + ability modifier + miscellaneous modifiers and compare to the Difficulty Class (DC).
- A result equal to or exceeding the DC is a success; higher totals produce better outcomes (degrees of success).
- Rolling a natural 20 scores a critical success: resolve degrees normally, then increase the result by one degree.
- When used untrained, skill rank is 0 but the ability modifier and other modifiers still apply.
- Attempts to use a Trained Only skill untrained automatically fail without a roll.
- Combines d20 roll, skill rank, ability modifier, and circumstance modifiers into a single total for comparison against the task DC.
- Increases the degree result by one when the d20 shows a natural 20, after calculating the normal degree.
- Produces automatic failure without a roll when a Trained Only skill is attempted with rank 0.
- Returns the ability modifier plus any applicable circumstance modifiers as the total when rank is 0 and the skill is not Trained Only.
- **Invariant:** the ability modifier component must always be included in the total, even when rank is 0.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_041.md`

### skill modifier

- The skill modifier is the total bonus added to the d20 roll: skill rank + ability modifier + miscellaneous modifiers.
- Each skill has an associated ability whose rank adds as the ability modifier to all checks for that skill, even when used untrained.
- Miscellaneous modifiers include circumstance modifiers, bonuses from advantages, and bonuses from powers.
- The higher the total skill modifier, the more consistent and favorable the skill check outcomes.
- Aggregates skill rank, ability modifier, and circumstance modifiers into a single numeric total.
- Serves as the effective bonus in routine check calculations: routine result equals modifier plus 10.
- Cannot exceed power level plus 10 at character construction or advancement time.
- **Invariant:** the ability modifier component always contributes, whether the character is trained or untrained in the skill.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_041.md`

### trained only

- Skills marked Trained Only require at least 1 rank to use; untrained attempts automatically fail.
- Some skills have both trained-only and untrained aspects; a character without ranks may use only the untrained aspects.
- Skills without the Trained Only marker may be attempted by any character using only the ability modifier.
- The Trained Only designation appears in the skill description and the Skills table Untrained column.
- Gates skill use by checking rank before any roll or DC comparison occurs.
- Permits use when rank is 1 or greater; produces automatic failure when rank is 0.
- Allows untrained characters to use only the explicitly untrained aspects of skills that have both trained and untrained uses.
- **Invariant:** the gate fires before any die roll is made; no partial result is produced for a blocked untrained attempt.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_042.md`

*Interaction Skill* — Interaction Skill is a named source category of skills whose purpose is social influence — changing the attitudes, beliefs, and actions of other characters through conversation, persuasion, trickery, or threat. The category owns its own requirements: subjects must be aware of and able to understand the user; unintelligent subjects impose a penalty; subjects lacking mental abilities cannot be targeted; the Immunity power effect can render a character wholly immune. These requirements belong to the category KA, not to individual skills. The four skills within this KA are Deception (lying, bluffing, disguise, feinting, innuendo, tricking), Intimidation (coercing, demoralizing, mass-intimidating minions), Persuasion (improving NPC attitudes step by step), and Insight (reading intentions, detecting illusions and influences, resisting social manipulation). Insight is the defensive counterpart to the three offensive interaction skills.

### interaction skill

- Interaction skills are a category used for social influence: changing others attitudes and gaining their cooperation.
- Require the subject to be aware of and able to understand the user; inability to hear or understand imposes a -5 circumstance penalty.
- Subjects with Intellect rank -5 impose a -5 circumstance penalty; subjects lacking any mental abilities cannot be targeted.
- The Immunity power effect can render a character completely immune to interaction skills.
- May be used on groups, but only to achieve the same result for every member; mindless subjects are unaffected.
- The interaction skills in this module are Deception, Intimidation, and Persuasion; Insight resists them.
- Evaluates three pre-conditions before resolving any interaction check: subject awareness and comprehension, subject minimum Intellect, and absence of Immunity effect.
- Reduces the check total by 5 when the subject cannot hear or understand; reduces by 5 when the subject's Intellect is rank -5.
- Blocks the check entirely when the subject lacks mental abilities or the Immunity effect is active against the user.
- Applies the same result uniformly to all members of a group when the check targets a group; cannot differentiate between individual members.
- **Invariant:** all three pre-conditions must resolve before the skill check proceeds; a blocked check produces no effect.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_042.md`

*Manipulation Skill* — Manipulation Skill is a named source category of skills requiring fine physical manipulation — the user must have prehensile limbs and a Strength rank, or a suitable Precise power effect. Physical impairment constrains use via circumstance penalties; characters without physical capability can still contribute via team check oversight. All four individual manipulation skills are Trained Only. Sleight of Hand (legerdemain, concealment, escape, theft) covers covert manual tasks. Technology (operating, building, repairing, sabotaging; requires tools) covers technical device work. Treatment (diagnosing, caring for, reviving, stabilizing, treating illness/poison; requires tools) covers medical work. Vehicles (operating any vehicle under stress) covers dramatic operation.

### manipulation skill

- Manipulation skills require fine physical manipulation; the user must have prehensile limbs and a Strength rank, or a suitable Precise power effect.
- Physical impairment causes the GM to impose a circumstance penalty scaled to severity.
- A character lacking physical manipulation capability may still hold ranks and use them to oversee or assist others via team checks.
- The manipulation skills in this module are Sleight of Hand, Technology, Treatment, and Vehicles.
- Requires physical manipulation capability (prehensile limbs plus Strength rank, or Precise power effect) as a prerequisite for primary use.
- Scales the circumstance penalty applied when physical manipulation is impaired according to the severity of the impairment.
- Permits use for oversight and assistance via team checks when the character lacks physical manipulation capability entirely.
- **Invariant:** lacking required tools for a Requires Tools manipulation skill always imposes a -5 circumstance penalty, regardless of other circumstances.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_043.md`

### Skill Mastery

- Skill Mastery is an advantage that allows the character to use a routine check result (bonus + 10) on a nominated skill even under stress, without rolling.
- A character with Skill Mastery can always achieve their routine result for that skill regardless of pressure.
- Source example: character has Skill Mastery for Stealth and does not need to roll.
- Grants the routine check result (bonus plus 10) for the nominated skill without requiring a die roll.
- Applies even under conditions that would normally compel a roll, such as combat or stress.
- **Invariant:** Skill Mastery must be assigned to a specific named skill; the routine result is always exactly bonus plus 10 for that skill.
- **Invariant:** the skill modifier limit still applies to the routine result; Skill Mastery does not bypass the PL cap.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_043.md`

### circumstance modifier

- A circumstance modifier is a bonus or penalty applied to a skill check that reflects the specific conditions under which it is made.
- Circumstance modifiers stack with the base skill modifier; favorable circumstances add bonuses, unfavorable circumstances impose penalties.
- Common penalties: lacking tools for a Requires Tools skill (-5); subject cannot hear/understand during interaction (-5); moving faster than speed rank minus 1 during Stealth (-5).
- Specific skill descriptions list the standard circumstance modifiers for each skill use.
- Adds a bonus or penalty to the skill modifier total based on the specific conditions present during skill use.
- Stacks additively with skill rank and ability modifier; multiple circumstance modifiers from different sources all contribute.
- Applies a standard -5 penalty when required tools are absent for a Requires Tools skill.
- Applies a standard -5 penalty when a subject cannot hear or understand during an interaction skill use.
- **Invariant:** circumstance modifiers are transient and situational; they do not permanently alter the skill rank or ability modifier.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_041.md`

*Physical Skill* — Physical Skill groups three skills grounded in bodily performance and environmental navigation: Acrobatics (balance, tumbling, falling, rising from prone — Agility, Trained Only), Athletics (climbing, jumping, running, swimming, falling — Strength, untrained allowed), and Stealth (hiding, tailing, moving without detection — Agility, untrained allowed). All three involve dynamic circumstance modifiers based on speed, surface conditions, and environmental factors, and all three have reactive interactions with other checks — Acrobatics reacts to failed resistance checks while balancing; Athletics reacts to failed resistance checks while climbing; Stealth reacts to Deception/Intimidation distraction checks.

### Acrobatics

- Acrobatics is a Trained Only skill based on Agility covering balance, acrobatic maneuvers, rising from prone, and reducing fall damage.
- Balancing: a successful check allows movement at ground speed minus 1 rank; one degree of failure equals no movement; two or more degrees means falling; the character is vulnerable while balancing unless DC is increased by +5.
- Maneuvering: checks for acrobatic stunts (flips, vaults, tumbling); GM sets the DC; two or more degrees of failure typically leaves the character prone.
- Standing: DC 20 check as a free action to rise from prone instead of a move action; failure leaves the character prone.
- Tumbling: DC 5 check reduces fall damage by 1 per degree of success; fall reduced to rank 0 deals no damage and character rises as a free action.
- Failing a resistance check while balancing triggers an immediate Acrobatics check against the original DC to avoid falling.
- Resolves balance checks against surface-specific DCs; one degree of failure means no movement; two or more degrees means a fall.
- Applies the vulnerable condition to the balancing character unless the DC is voluntarily increased by +5.
- Requires an immediate reactive check against the original balancing DC when the character fails a resistance check while balancing.
- Reduces fall damage by one point per degree of success on a DC 5 tumbling check; a fall reduced to rank 0 deals no damage.
- Produces a free-action standing result when a DC 20 check succeeds while the character is prone.
- **Invariant:** Acrobatics is Trained Only; untrained characters automatically fail all Acrobatics checks.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_044.md`

### Athletics

- Athletics is a skill based on Strength; it may be used untrained; it covers climbing, falling, jumping, running, and swimming.
- Climbing: a successful check allows climbing at ground speed rank minus 2; failure equals no progress; two or more degrees means falling; the character is vulnerable while climbing unless DC is increased by +5.
- Falling: a fall inflicts damage rank 4 plus twice the distance rank fallen (maximum rank 16); falls of rank 0 or less deal no damage; the character is prone at end of fall; Acrobatics can lessen fall damage.
- Jumping: Athletics check result equals running long-jump distance in feet; standing long-jump divides by 2; running vertical jump divides by 5; standing vertical jump divides by 10.
- Running: DC 15 check as a free action increases ground speed rank by +1 for one round.
- Swimming: DC 10 check allows swimming at ground speed rank minus 2; failure equals no progress; two or more degrees means going under.
- Resolves climbing movement at ground speed rank minus 2; two or more degrees of failure triggers a fall from current height.
- Applies the vulnerable condition while climbing unless the DC is voluntarily increased by +5.
- Calculates jump distance from the check result: running long-jump equals check result in feet; divide by 2 for standing, by 5 for running vertical, by 10 for standing vertical.
- Increases ground speed rank by +1 for one round when a DC 15 running check is made as a free action.
- Resolves swimming at ground speed rank minus 2; two or more degrees of failure causes the character to go under.
- **Invariant:** Athletics is untrained-allowed; fall damage is a system calculation (rank 4 + 2 x distance rank, max rank 16), not an Athletics check result.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_047.md`

*Combat Skill* — Combat Skill groups two skills that add directly to attack checks for specific weapons or powers: Close Combat (based on Fighting) and Ranged Combat (based on Dexterity). Both follow the same pattern: each is specific to a single named weapon or power, adds its rank to attack checks for that weapon/power only, and explicitly does not add to defense. Both can be used untrained. An array of powers may be treated as a single power at the GM’s discretion.

### Close Combat

- Close Combat is a skill based on Fighting; it may be used untrained; each Close Combat skill is specific to a single weapon or power.
- The skill rank adds to attack checks for that specific weapon or power only; it does not apply to defense.
- Close Combat: Unarmed covers punches and kicks but not grabbing or tripping maneuvers.
- An array of powers may be treated as one power for Close Combat purposes at the GMs discretion.
- For a broader bonus across all close attacks, see the Close Attack advantage.
- Adds its rank as a bonus to attack checks made with the specific weapon or power the skill names.
- Restricts its bonus exclusively to attack checks; contributes nothing to any defense value.
- Accepts a single weapon or power as its scope; the scope cannot expand to cover a broader category.
- Treats an array of powers as one power when the GM grants discretion.
- **Invariant:** every Close Combat instance is specific to exactly one weapon or power; the bonus never transfers to a different attack.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_048.md`

### Deception

- Deception is an interaction skill based on Presence; it covers lying, bluffing, disguise, feinting, innuendo, and tricking.
- Bluffing: Deception check opposed by targets Deception or Insight; circumstance modifiers from -5 (target wants to believe) to +20 (outrageous claim); standard action, or move action at -5.
- Disguise: Deception check result becomes the DC of observers Perception checks; GM rolls secretly; associates of the impersonated person get Perception bonuses (+2 regular, +5 friend, +10 intimate).
- Feinting: standard action Deception check opposed by targets Deception or Insight; success makes target vulnerable against the users next attack until end of users next round.
- Innuendo: DC 10 basic / DC 15 complex / DC 20 new information; recipient uses Insight at the same DC to understand; more than one degree of failure on either side misinterprets the message.
- Tricking: Deception check opposed by Deception or Insight to mislead into a dangerous action; more than one degree of failure on the users check leaves the user vulnerable.
- Resolves bluff checks against the target's Deception or Insight, applying believability and risk circumstance modifiers before comparing.
- Sets the disguise detection DC equal to its check result, which observers must exceed with Perception to see through.
- Applies the vulnerable condition to the target until end of the user's next round when a feint check succeeds.
- Transmits covert innuendo messages at DCs 10, 15, and 20 for basic, complex, and new-information messages respectively.
- Applies the vulnerable condition to the user until start of user's next round when a tricking check fails by more than one degree.
- **Invariant:** Deception is an interaction skill (all pre-conditions apply); uses Presence as its ability modifier; standard action in combat, move action at -5.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_049.md`

*Knowledge & Awareness Skill* — Knowledge & Awareness Skill groups three skills that derive value from accumulated knowledge, active research, and attentiveness: Expertise (professional and scholarly knowledge in a named field — Intellect, Trained Only), Investigation (searching, evidence analysis, information gathering, surveillance — Intellect, Trained Only), and Perception (noticing things across all sense types, detecting disguises and concealed objects — Awareness, untrained allowed). All three are information-gathering mechanisms: Expertise retrieves stored knowledge, Investigation actively searches and analyzes, and Perception passively or reactively notices the environment.

### Expertise

- Expertise is a Trained Only skill based on Intellect representing specialized professional or scholarly knowledge; each area is a separate skill.
- A trained character can practice and make a living at it: use tools of the trade, perform daily tasks, supervise helpers, handle common problems.
- Expertise checks answer knowledge questions: easy DC 10, basic DC 15, difficult DC 20+; most job-related checks are routine.
- The ability modifier is typically Intellect, but the GM may require a different ability based on the specific check.
- Some Expertise areas can be used untrained for general knowledge, but untrained checks cannot be routine (DC 10-15 only).
- Expertise covers professional knowledge not captured by other skills; professionals often need complementary skills (Investigation for detectives, Technology for scientists, Treatment for doctors).
- The GM may allow defaulting to a related Expertise at a circumstance penalty (-2 related, -5 loosely related).
- Answers knowledge questions within the named field at DC 10 for easy, DC 15 for basic, and DC 20 or higher for difficult questions.
- Permits professional tasks at routine check level when trained.
- Restricts untrained use to non-routine checks and DC 10-15 questions only.
- Defaults to a related Expertise area at the GM's discretion, at -2 (related) or -5 (loosely related) circumstance penalty.
- Assumes professional licensing and certification when the character is trained, handling licensing complications as character complications.
- **Invariant:** each Expertise is a separate skill with its own rank slot; a single character may hold multiple Expertise skills; the ability modifier is typically Intellect but may vary by task.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_051.md`

### Insight

- Insight is a skill based on Awareness; it may be used untrained; it covers reading intentions, detecting influence, evaluating trustworthiness, picking up innuendo, and resisting social manipulation.
- Detect Illusion: GM makes a secret Insight check (DC 10 + Illusion rank) to sense an illusions true nature.
- Detect Influence: Insight check (DC 10 + rank of the affecting effect or skill) to notice a subject acting under outside influence; three or more degrees give a general idea of the source.
- Evaluate: Insight check opposed by Deception to assess trustworthiness; DC 20 to evaluate a social situations mood; two or more degrees of failure causes misinterpretation.
- Innuendo: Insight is used to pick up on hidden Deception messages at the same DC as the sending check.
- Resist Influence: Insight check resists effects of interaction skills (Deception, Intimidation); if Insight result exceeds the opponents skill result, the character is unaffected.
- Insight checks are generally free actions; may be used as reactions against incoming interaction skill use.
- Resists incoming interaction skill effects when its check result exceeds the incoming skill check result.
- Detects illusion flaws when a GM-made secret check exceeds DC 10 plus the Illusion effect's rank.
- Identifies a subject acting under outside influence when its check exceeds DC 10 plus the rank of the influencing effect or skill.
- Assesses trustworthiness when opposed by the target's Deception check; evaluates social situations at DC 20.
- Interprets hidden Deception innuendo at the same DC as the sender's check.
- **Invariant:** Insight uses Awareness; it is untrained-allowed; the GM may make detect-illusion and evaluate checks secretly.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_052.md`

### Intimidation

- Intimidation is an interaction skill based on Presence; it covers using threats to coerce compliance or demoralize opponents.
- Coercing: Intimidation check opposed by targets Insight or Will defense (whichever is higher); success treats target as friendly for actions in the users presence only; targets true attitude becomes hostile after the attempt; more than one degree of failure causes the opposite effect.
- Demoralizing: standard action check in combat; success imposes the impaired condition (-2 penalty on checks) until end of users next round; four or more degrees imposes disabled (-5 penalty) until end of users next round.
- Intimidating Minions: a single check against a whole group that can see and hear the user; compared to a single GM resistance check for the group; the effect must be the same for all members.
- An imposing action before the check grants a circumstance bonus; a clearly superior target position imposes a circumstance penalty.
- Uses in action rounds are standard actions; may be attempted as a move action at -5 penalty.
- Coerces a target into acting friendly in the user's presence when its check exceeds the target's Insight or Will defense.
- Causes the target's true attitude to shift hostile after the attempt, regardless of whether coercion succeeded.
- Imposes the impaired condition (-2 on checks) until end of user's next round when a demoralizing check succeeds in combat.
- Imposes the disabled condition (-5 on checks) instead when the demoralizing check succeeds by four or more degrees.
- Compares a single check against a single group resistance roll to apply uniform coercion or demoralization to a group of visible, audible minions.
- **Invariant:** Intimidation is an interaction skill (all pre-conditions apply); uses Presence; the target's true attitude always becomes hostile after an attempt.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_053.md`

### Investigation

- Investigation is a Trained Only skill based on Intellect covering searching for clues, gathering information, interviewing contacts, surveillance, and forensic analysis.
- Search: an Investigation check picks up on area details with effort; DC scales from low (ransacking a room) to 25+ (extremely obscure clues); concealed objects DC opposed by hiders Stealth or Sleight of Hand.
- Gather Evidence: DC 15 to collect evidence; failure allows analysis at -5; more than one degree of failure ruins evidence; two or more degrees of success grant +2 to later analysis.
- Analyze Evidence: DC 15 to extract useful information; DC modified by time elapsed and scene disturbance; does not create clues where none exist.
- Gather Information: DC 10+ taking at least one hour; degree of success determines information type (general / specific / restricted / protected); more than one degree of failure may alert those being investigated.
- Surveillance: a stationary Investigation check result becomes the DC of a subjects Stealth check to evade detection.
- The GM may make Investigation checks secretly.
- Detects hidden details, clues, and objects in an area when its check meets or exceeds the target DC.
- Collects evidence for analysis when a DC 15 check succeeds; ruins evidence entirely on two or more degrees of failure.
- Extracts information from collected evidence when a DC 15 analysis check succeeds; time elapsed and scene disturbance increase the DC.
- Gathers information from contacts and rumors after at least one hour when a DC 10 or higher check succeeds; degree of success determines information classification (general, specific, restricted, protected).
- Establishes a surveillance DC equal to its check result that subjects must exceed with Stealth to evade detection.
- **Invariant:** Investigation is Trained Only; the GM may make Investigation checks secretly; investigation does not create evidence that does not exist.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_054.md`

### Perception

- Perception is a skill based on Awareness; it may be used untrained; it covers noticing and picking up on things in the environment across all sense types.
- Distance penalty: -1 circumstance penalty for every 10 feet between the character and what they try to perceive.
- Hearing: DC based on loudness (normal conversation DC 0, soft noise DC 10); through a door adds +5, through a solid wall +15; waking from sleep adds +10.
- Seeing: DC based on visibility (plain sight DC 0, subtle DC 5-10+); used to detect disguises (opposed by Deception) and concealed objects (opposed by Sleight of Hand).
- Discerning fine details requires at least three degrees of success.
- The GM usually makes Perception checks secretly.
- A character may retry a previously failed Perception check as a move action.
- Perception applies to all sense types defined in the Powers chapter.
- Detects stimuli across any sense type when its check meets or exceeds the stimulus DC.
- Applies a -1 circumstance penalty per 10 feet of distance before comparing the check total to the DC.
- Requires at least three degrees of success to discern fine sensory details.
- Contests a Deception check to detect a disguise; contests a Sleight of Hand check to detect a concealed object.
- Allows a retry of a previously failed check as a move action when a new opportunity to notice arises.
- **Invariant:** Perception is untrained-allowed; the GM routinely makes Perception checks secretly; a -10 to the DC is applied when the character is asleep.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_057.md`

### Persuasion

- Persuasion is an interaction skill based on Presence covering social graces, etiquette, negotiation, and winning others over.
- Improving attitudes: DC 15 check improves an NPCs attitude by one step; each two additional degrees improve by one more step; failure equals no change; more than one degree of failure worsens attitude by one step.
- NPC attitudes form a five-step scale: Hostile to Unfavorable to Indifferent to Favorable to Helpful.
- In negotiations, all participants roll Persuasion and compare results; opposed checks resolve competing advocacy before a third party.
- A successful Persuasion check takes at least a standard action and usually longer; the GM may forbid persuasion once combat begins.
- Each argument can only be attempted once per scene; retrying after failure requires a changed situation.
- Improves an NPC's attitude by one step when a DC 15 check succeeds; improves by one additional step per two degrees of success beyond the first.
- Worsens an NPC's attitude by one step when the check fails by more than one degree; a hostile attitude worsening may provoke an attack.
- Compares all participants' check results to determine negotiation advantage when multiple parties are competing.
- Restricts each distinct argument to one attempt per scene; further attempts after failure require a changed situation.
- Resets the resistance baseline to the NPC's initial (pre-persuasion) attitude for each additional attempt.
- **Invariant:** Persuasion is an interaction skill (all pre-conditions apply); uses Presence; attitude cannot exceed Helpful regardless of degrees of success.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_058.md`

### Ranged Combat

- Ranged Combat is a skill based on Dexterity; it may be used untrained; each Ranged Combat skill is specific to a single weapon or power.
- The skill rank adds to attack checks for that specific weapon or power only; it does not apply to defense.
- Ranged Combat: Throwing covers thrown weapons and thrown objects.
- An array of powers may be treated as one power for Ranged Combat purposes at the GMs discretion.
- For a broader bonus across all ranged attacks, see the Ranged Attack advantage.
- Adds its rank as a bonus to attack checks made with the specific weapon or power the skill names.
- Restricts its bonus exclusively to attack checks; contributes nothing to any defense value.
- Accepts a single weapon or power as its scope (Ranged Combat: Throwing covers thrown weapons and thrown objects).
- Treats an array of powers as one power when the GM grants discretion.
- **Invariant:** every Ranged Combat instance is specific to exactly one weapon or power; the bonus never transfers to a different attack.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_059.md`

### Sleight of Hand

- Sleight of Hand is a Trained Only manipulation skill based on Dexterity covering legerdemain, pickpocketing, concealment, contortion, and escape.
- Concealing: Sleight of Hand check result becomes the DC for Investigation or Perception checks to find the concealed item.
- Contorting: DC 30 to fit through a tight space wide enough for the head but not shoulders.
- Escaping: check to slip out of restraints; takes at least one minute per check; DC varies by restraint type.
- Legerdemain: minor feats have DC 10 unless an observer is focused; under observation, opposed by the observers Perception.
- Planting objects: requires a check result of 20 or higher to successfully plant; target notices the attempt if their Perception beats the users check.
- Stealing: DC 20 to take something covertly from a person; opposed by targets Perception.
- Sets the discovery DC for a concealed item equal to its check result for subsequent Investigation or Perception checks.
- Requires a minimum check result of 20 to successfully plant a small object on a person, regardless of the target's Perception result.
- Extracts the character from restraints when its check meets or exceeds the restraint's resistance DC (minimum one minute per attempt).
- Produces a covert theft when its check result exceeds DC 20 and the target's Perception check does not beat it.
- Fits the character through a tight space (wide enough for head, not shoulders) when a DC 30 check succeeds.
- **Invariant:** Sleight of Hand is Trained Only and a manipulation skill; physical manipulation capability is required.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_059.md`

### Stealth

- Stealth is a skill based on Agility; it may be used untrained; it covers hiding from observers and tailing subjects without detection.
- Hiding: requires cover or concealment; Stealth check opposed by observers Perception; cannot hide when others are already aware unless a Deception or Intimidation check first creates a distraction (Stealth at -5); cannot hide in plain sight.
- Tailing: Stealth check to follow a subject at normal speed using available cover; a worried subject makes opposed Perception checks each time they change course; an unsuspecting subject gets only one check per scene.
- Speed: movement at speed rank minus 1 incurs no Stealth penalty; moving up to full speed imposes -5 circumstance penalty.
- When using Deception or Intimidation to create a distraction for hiding, cover must be within 1 foot per Stealth rank.
- Hides the character from observer detection when its check result exceeds the observer's Perception check, provided cover or concealment exists.
- Enables movement at speed rank minus 1 without penalty; imposes a -5 circumstance penalty when moving at full speed.
- Allows tailing a subject at normal speed using cover; produces opposed Perception checks from a worried subject each time they change course.
- Permits a Stealth check attempt after a successful Deception or Intimidation distraction, but at -5 penalty; the character must be within 1 foot per Stealth rank of cover.
- **Invariant:** the character cannot use Stealth to remain hidden when observers are already actively aware of their presence; cover or concealment is always a prerequisite.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_060.md`

### Technology

- Technology is a Trained Only manipulation skill based on Intellect that requires tools; it covers operating, building, repairing, and sabotaging technological devices.
- Operating: routine operations do not require a check; unfamiliar devices require a check (DC 10 simple to DC 25+ highly advanced); lacking tools imposes -5.
- Building: DC and time based on complexity (Simple DC 15 / 2 hours through Advanced DC 25 / 4 days); failure wastes time and materials; time can be reduced 1 rank at -5 to the check.
- Repairing: DC is 5 lower and time rank 2 lower than building the same item.
- Jury-Rigging: DC is 10 lower than building, check is a standard action, but fixes only one problem and lasts until end of scene; must be fully repaired before it can be jury-rigged again.
- Demolitions: careful placement (at least one minute, DC 10) maximizes damage; two full degrees of success each add +5 damage to the structure.
- Security: disarms or sabotages locks, traps, and sensors; DC based on security level (simple DC 10 to super-max DC 40+); more than one degree of failure sets off the security device.
- Inventing: with the Inventor advantage, Technology can create temporary invention devices.
- Resolves unfamiliar device operation against a complexity DC (DC 10 simple to DC 25 or higher for highly advanced).
- Produces a built item when its check meets the complexity DC after the required time; failure wastes time and materials.
- Repairs items at DC 5 lower and time 2 ranks faster than building the same item.
- Performs jury-rig repairs at DC 10 lower than building, in a standard action; the fix expires at scene end and cannot repeat until full repair completes.
- Places demolitions charges that add +5 structure damage per two full degrees of success; detonates prematurely on two or more degrees of failure.
- Defeats security devices when its check meets the security DC; triggers the device on more than one degree of failure.
- **Invariant:** Technology is Trained Only, requires tools (-5 penalty without tools), and is a manipulation skill; the Inventor advantage is required for the inventing use.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_061.md`

### Treatment

- Treatment is a Trained Only manipulation skill based on Intellect that requires tools; it covers diagnosing, caring for, reviving, stabilizing, and treating injured or ill characters.
- Diagnosis: takes at least one minute; at GMs discretion, success grants +2 to subsequent Treatment checks.
- Provide Care: treating a patient for a day or more reduces recovery time rank by 1; a character can treat up to their Treatment rank in patients at once.
- Revive: standard action to remove the dazed or stunned condition; cannot revive a dying character without first stabilizing.
- Stabilize: standard action Treatment check stabilizes a dying character.
- Treat Disease or Poison: each time the patient makes a resistance check against an ailment, the treating character also makes a Treatment check; one degree of success grants +2 to the patients resistance check; three or more degrees grants +5.
- Lacking appropriate medical equipment imposes -5; treating a subject with unusual biology may impose an additional penalty; treating oneself imposes -5 and is limited to diagnosis, care, or treating disease/poison.
- Identifies injuries and ailments after at least one minute when its diagnosis check succeeds; the GM may grant +2 to subsequent Treatment checks.
- Reduces a patient's recovery time rank by 1 when a long-term care check succeeds over one or more days.
- Removes the dazed or stunned condition from a subject in a standard action when its revive check succeeds; other conditions on the patient remain.
- Stabilizes a dying character when its standard-action stabilize check succeeds.
- Provides a +2 bonus to a patient's concurrent resistance check against disease or poison when its treatment check succeeds; provides +5 when three or more degrees of success are achieved.
- **Invariant:** Treatment is Trained Only, requires tools (-5 without tools), and is a manipulation skill; a dying character cannot be revived without first being stabilized; self-treatment imposes -5 and excludes revive use.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_063.md`

### Vehicles

- Vehicles is a Trained Only manipulation skill based on Dexterity covering operation of ground vehicles, boats, aircraft, and spacecraft in dramatic or stressful situations.
- Routine vehicle operations do not require a check and may be done untrained for common vehicles.
- Vehicle maneuver DCs range from Easy DC 10 (low-speed turn) to Formidable DC 25 (high-speed maneuvers around obstacles).
- Vehicles does not cover riding animal mounts; for animal mounts, use Expertise: Riding (based on Agility).
- Resolves vehicle maneuvers in dramatic or stressful situations against DCs from 10 (easy low-speed turn) to 25 (formidable high-speed maneuvers).
- Does not require a check for routine operation of a familiar vehicle; allows untrained use for common vehicles in routine situations.
- Excludes animal mount riding from its scope; Expertise: Riding (based on Agility) handles mounts instead.
- **Invariant:** Vehicles is Trained Only and a manipulation skill; the physical manipulation prerequisite applies to vehicle operation.
- Sources: `.context/sources/rules/HeroesHandbook-rules__chunk_064.md`
