# THE DEEP SALTS — CAMPAIGN PLAN

A tabletop campaign set in the world of the novel (*The Deep Salts* / *The
Sweetwater Years*), played with Jake's Deep Salts ruleset (d20 base, six
attributes, Token economy, limb targeting, mutation, Insight, stopwatch parry).
It is a follow-up, not a second novel: the output is playable reference
material, not prose fiction.

## Structure: what we borrow from D&D books, and what changes

D&D splits a campaign across several books with different readers. We keep the
split and adapt each part to how Deep Salts actually plays (brew a recipe →
wake in a biome → reach the anchor chalice → wake at the hub; no fast travel;
monster numbers generated live from archetype bands).

| D&D book / part | TDS equivalent | Reader |
|---|---|---|
| Adventure intro, "Running the Adventure" | **A. Campaign Brief + DM's Guide** | DM / AI DM |
| Player's Handbook primer, Session Zero | **B. Player's Primer** | players |
| Campaign setting guide / gazetteer | **C. Gazetteer + Factions & Clocks** | DM |
| Hub town chapter | **D. Stillwell Hydro** (hub book) | DM |
| Numbered adventure chapters, by level band | **E. Delves**, one per depth tier (I–V), the spine of the campaign | DM |
| Between-chapter downtime / side quests | **F. Surface Interludes** (the Commonwealth above ground) | DM |
| Monster Manual appendix | **G. Bestiary Additions** (archetype, tells, behaviour; numbers live per ruleset) | DM |
| Magic items appendix | **H. Compendium**: chalices, recipes, weapons, items | DM / players |
| NPC appendix | **I. Dramatis Personae** | DM |
| Handouts, random tables | **J. Tables & Handouts** | DM |
| DM screen / campaign tracker | **K. Campaign Log & Continuity Index** (live-state files) | DM |

Two TDS-specific changes:

1. **The delve is the unit, not the dungeon.** Each delve module follows one
   template (below) so any of them can be run cold by an AI DM from one file.
2. **Table-time vs project files stay separate.** Reference files the DM loads
   mid-session are short and functional. Design rationale, open questions and
   history live in `campaign/DECISIONS.md` and the dev log, never in the
   table-time files. (This is Jake's standing rule for the ruleset; it applies
   here too.)

## Delve template (every Tier module uses this)

1. **Premise card** — tier, level band, one-line hook, what the Church or the
   surface wants from it.
2. **Entry** — the recipe, who sells it, the salts room, the cost.
3. **Biome overview** — look, sound, smell, what drifts (geometry and NPCs may
   drift; the hub does not).
4. **Anchor** — where the clean chalice is, what guards it, what the route
   back costs.
5. **Area keys** — numbered areas, each: purpose, sensory tells, encounter
   (archetype + tier, never fixed numbers), secrets, loot, exits.
6. **Encounter tables** — wandering, escalation by Insight tier.
7. **Set piece + boss** — gimmick, telegraphed tells (promises the DM must
   honour exactly), what defeat and retreat look like.
8. **Rewards and consequences** — Tokens, Insight, mutations offered, what the
   surface notices afterwards.
9. **DM notes** — failure states, bail-out ("Abandon-All") consequences, what
   to withhold.

## Tone contract (inherited, with one adaptation)

- **Underground (the Salts):** Bloodborne / Lovecraftian dream-logic. Withhold
  lore, describe don't signpost, unreliable sources.
- **Surface (the Commonwealth):** the novel's stance governs. Clear-eyed, not
  cynical. Institutions rot, individual costly choices are real, nothing
  structural gets fixed by a hero. Offer neglect over spectacle. Apply the cost
  test to every scene: what does this cost, and who pays.
- **Church menace** lives in the content of what is said, delivered warmly. No
  ominous staging (see canon.md Section 3 for the exact banned cues).
- **Insight:** in-game it is mechanically true (PCs perceive what is there).
  Surface NPCs still treat it as unreliable. The theme inherited from the
  novel: what it costs to be disbelieved while correct.
- **The reception clerk** is a narrative fixture, never statted, never a
  combat encounter.

## Work items

IDs are stable. Order is by dependency and **playable-first**: the first goal
is a *vertical slice* (brief, hub, Tier I delve, minimum DM guidance) so
the campaign can be tried at a table before the deeper tiers are written.
Sizes are targets for one scheduled session; split an item (a/b) if it would
run over.

| ID | Item | Depends on | Target |
|---|---|---|---|
| P1.1–P1.5 | Read-through batches (ch. 1–5, 6–10, 11–15, 16–20, 21–25) | none | notes per batch |
| P1.6 | Read-through synthesis + source bible + hooks | P1.1–P1.5 | 3 files |
| **A1** | Campaign Brief: premise, timeline anchor, pillars, relationship to novel, what PCs are | P1.6 | 1.5–2.5k w |
| **C1** | Gazetteer: Commonwealth after the novel, Carrowgate, Vantry ruins, Larrow Valley, the hydro network | A1 | 3–4k w |
| **C2** | Factions & Clocks: Church, Ferrick's sub-panel, hydro operators, the Crane works, Salts-dwellers; 5–6 clocks with triggers | A1, C1 | 2–3k w |
| **C3** | The Salts: cosmology, tier map (I Shallows → V Source), what depth does, link to the Fourth Mercy, Insight tiers as story | A1, C2 | 2–3k w |
| **D1** | Stillwell Hydro hub: layout, staff, services, rules of the house, the clerk, Purse/Vault, rumours | C1, C3 + system docs | 3–4k w |
| **E1a/b** | Delve I (Shallows, lv 1–28): overview, then area keys + boss | C3, D1 | 4–6k w |
| **A2** | DM's Guide: running order, tone contract, AI-DM standing instructions addendum, session zero, lines and veils | A1, E1 | 2–3k w |
| **B1** | Player's Primer: what the PCs know, character hooks, why they take the salts | A1, D1 | 1.5–2k w |
| **G1** | Bestiary additions for Tier I (archetype, tells, behaviour) | E1 | 1.5–2.5k w |
| **H1** | Compendium: Tier I chalices, recipes, items | E1 | 1.5–2.5k w |
| *Vertical slice complete — flag to Jake before continuing* | | | |
| **E2a/b** | Delve II | C3, E1 | 4–6k w |
| **E3a/b** | Delve III | E2 | 4–6k w |
| **E4a/b** | Delve IV | E3 | 4–6k w |
| **E5a/b** | Delve V (the Source) + finale and endings | E4 | 5–7k w |
| **F1–F3** | Surface Interludes, one per gap between delves (investigations built on the novel's open threads) | C2, E-tier before it | 2–3k w each |
| **I1** | Dramatis Personae, incl. Lloyd, Maria, Edie as cameo NPCs with the rules for using them | A1, C2 | 3–4k w |
| **G2–G5** | Bestiary additions, Tiers II–V | matching E | 1.5–2.5k w each |
| **H2–H5** | Compendium, Tiers II–V | matching E | 1.5–2.5k w each |
| **J1** | Rumour tables, wandering tables, handouts | C2, E1 | 2–3k w |
| **K1** | Campaign log and continuity index templates (live-state files) | D1 | 1–1.5k w |
| **Z1** | Integration pass: contradictions across all files, index/TOC, final DM checklist | all | review log |

## Conventions for every campaign file

- Plain markdown in `campaign/`. Filename: `<ID>-<slug>.md`.
- Table-time voice: tight, concrete, no design-rationale prose.
- Mechanics: use the real ruleset if `campaign/system/` has it. If it does
  not, write archetype and tier only and mark anything that needs a number
  `(SYS?)`. Never invent attribute numbers, thresholds or costs that the
  ruleset defines. Monster numbers are generated live at the table.
- Everything must be consistent with `novel/canon.md` and with chapter 25's
  ending state. Where it cannot be, log it in `campaign/DECISIONS.md`.
- No lyrics, no quotes from published games, no copying D&D text. We borrow
  structure only.
