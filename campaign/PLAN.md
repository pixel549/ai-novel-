# THE DEEP SALTS — CAMPAIGN PLAN

A tabletop campaign set in the world of the novel (*The Deep Salts* / *The
Sweetwater Years*), **in the real world, after the novel**. The player
characters live, travel, investigate, fight and bargain in the Aventine
Commonwealth. The Salts are background: they explain part of the world's
Arcana, they are why the Church does what it does, and they surface now and
then as a place the characters can be pulled into. They are not the campaign's
engine. (Meta: the novel and the solo Salts runs were the testbed where the
rules got worked out; the campaign proper is the world above them.)

The output is playable reference material, not prose fiction. Rules come from
Jake's Deep Salts ruleset (d20 base, six attributes, limb targeting, status
effects, mutation, Insight, stopwatch parry). Parts of that ruleset assume
the Salts loop (anchor chalice, hub, bail-out, Tokens, no fast travel), so
the surface needs an adaptation layer (item S1).

## Structure: what we borrow from D&D books, and what changes

D&D splits a campaign across books for different readers. We keep the split
and swap the dungeon-crawl spine for a **region-and-investigation spine**.

| D&D book / part | TDS equivalent | Reader |
|---|---|---|
| Adventure intro, "Running the Adventure" | **A. Campaign Brief + DM's Guide** | DM / AI DM |
| Player's Handbook primer, Session Zero | **B. Player's Primer** | players |
| Campaign setting guide / gazetteer | **C. Gazetteer, Factions & Clocks, the Salts as background** | DM |
| Rules supplement | **S. Surface Adaptation** of the ruleset (proposals) | DM, Jake |
| Home base / hub town | **D. Bases & Safehouses** | DM |
| Numbered adventure chapters, by level band | **R. Parts**: one per region or arc, the spine | DM |
| Optional dungeon chapters | **T. Thin Sites**: short Salts incursions (mini-delves) | DM |
| Travel / downtime sections | **F. Travel & Downtime** | DM |
| Monster Manual appendix | **G. Bestiary Additions** (archetype, tells, behaviour; numbers live per ruleset) | DM |
| Magic items appendix | **H. Compendium**: Arcana, chalice-gifts, items, weapons | DM / players |
| NPC appendix | **I. Dramatis Personae** | DM |
| Handouts, random tables | **J. Tables & Handouts** | DM |
| DM screen / campaign tracker | **K. Campaign Log & Continuity Index** | DM |

Table-time vs project files stay separate. Reference files the DM loads
mid-session are short and functional. Design rationale, open questions and
history live in `campaign/DECISIONS.md`, never in the table-time files.

## Part template (every R module uses this)

1. **Premise card**: region/arc, level band, one-line hook, what the surface
   wants, what the Church wants.
2. **Situation**: the state of the region when the PCs arrive; who holds what;
   which clocks are running and how they advance.
3. **Locations**: keyed sites (towns, works, houses, roads, rail stops), each
   with purpose, NPCs, sensory tells, secrets, exits.
4. **Lead web**: the investigation as nodes and clues. Every essential reveal
   is reachable at least three ways; no single missed roll stalls the table.
5. **Encounters**: social, pursuit, Arcana, Church operatives, pest-class
   horrors (undead where the war killed enough people), Fourth Mercy
   products, and the occasional Salts leak. Archetype + tier, never fixed
   numbers.
6. **Set pieces and antagonist**: gimmick, telegraphed tells (promises the DM
   must honour exactly), what defeat, flight and capture look like.
7. **Salts thread (optional)**: if this Part has a thin site (T module), where
   it is and why the story might send the PCs there.
8. **Consequences**: what changes on the map and on the clocks, what the
   Commonwealth notices, what it costs and who pays.
9. **DM notes**: failure states, what to withhold, how the novel's three
   survive or appear.

## Tone contract (inherited, with one adaptation)

- **The surface** is where the novel's stance governs. Clear-eyed, not
  cynical. Institutions rot, costly individual choices are real, nothing
  structural gets fixed by a hero. Offer neglect over spectacle. Apply the
  cost test to every scene: what does this cost, and who pays.
- **The Salts** (when they surface) are Bloodborne / Lovecraftian dream-logic.
  Withhold lore, describe don't signpost, unreliable sources.
- **Church menace** lives in the content of what is said, delivered warmly.
  No ominous staging (see canon.md Section 3 for the exact banned cues).
- **Insight**: in-game it is mechanically true (PCs perceive what is there).
  Surface NPCs still treat it as unreliable. Inherited theme: what it costs to
  be disbelieved while correct.
- **The reception clerk** at Stillwell Hydro is a narrative fixture, never
  statted, never a combat encounter.

## Work items

IDs are stable. Order is dependency plus **playable-first**: the first goal is
a *vertical slice* (brief, surface adaptation, a base, Part I, minimum DM
guidance) so the campaign can be tried at a table before the later Parts are
written. Sizes are per scheduled session; split an item (a/b) if it would run
over. Level bands for Parts II–V are `(SYS?)` until the ruleset's tier
bands are in `campaign/system/`.

| ID | Item | Depends on | Target |
|---|---|---|---|
| P1.1–P1.5 | Read-through batches (ch. 1–5, 6–10, 11–15, 16–20, 21–25) | none | notes per batch |
| P1.6 | Read-through synthesis + source bible + hooks | P1.1–P1.5 | 3 files |
| **A1** | Campaign Brief: premise, timeline anchor, pillars, relationship to the novel, what the PCs are, how the Salts fit | P1.6 | 1.5–2.5k w |
| **C1** | Gazetteer: the Commonwealth after the novel; regions as Part candidates (Larrow Valley, Vantry, Carrowgate, the rail, the hydros, anywhere else the novel implies) | A1 | 3–4k w |
| **C2** | Factions & Clocks: Church, Ferrick's sub-panel, the Crane works and what replaced it, hydro operators, the dead and their pests, Arcana practitioners; 5–6 clocks | A1, C1 | 2–3k w |
| **C3** | The Salts as background: what they are, what chalices do, which Arcana they explain and which they don't, how they leak into the surface, the Fourth Mercy's use of them. Lore and DM rules, not a tier ladder | A1, C2 | 2–3k w |
| **S1** | Surface adaptation of the ruleset: what carries over, what is replaced, what is new. Proposals tagged `(untested)` | A1 + system docs | 2–3k w |
| **D1** | Bases & Safehouses: the starting base, 2–3 alternates, Stillwell Hydro as a location (and its clerk), upkeep, how the PCs recover | C1, S1 | 3–4k w |
| **R1a/b** | Part I, first region (default: Larrow Valley): overview + locations, then lead web + set pieces + antagonist | C2, C3, D1 | 5–7k w |
| **A2** | DM's Guide: running order, tone contract, AI-DM standing instructions addendum, session zero, lines and veils | A1, R1b | 2–3k w |
| **B1** | Player's Primer: what PCs know, character hooks, why they stay | A1, D1 | 1.5–2k w |
| **G1** | Bestiary additions for Part I | R1b | 1.5–2.5k w |
| **H1** | Compendium for Part I (Arcana, items, weapons) | R1b | 1.5–2.5k w |
| *Vertical slice complete: flag to Jake before continuing* | | | |
| **R2a/b** | Part II (default: Vantry and the rail) | R1b | 5–7k w |
| **R3a/b** | Part III (default: Carrowgate and the Senate) | R2b | 5–7k w |
| **R4a/b** | Part IV (the Fourth Mercy's wider network) | R3b | 5–7k w |
| **R5a/b** | Part V: finale and endings (several, ordered by cost, none clean) | R4b | 5–7k w |
| **T1–T3** | Thin Sites: three short Salts incursions placed across Parts, each a compact delve using the ruleset's Salts loop | C3, R1b | 2–4k w each |
| **F1** | Travel & Downtime: rail, roads, recovery, Arcana healing, heat and notoriety, favours | S1, C1 | 2–3k w |
| **I1** | Dramatis Personae, incl. Lloyd, Maria, Edie as cameo NPCs with the rules for using them | A1, C2 | 3–4k w |
| **G2–G5** | Bestiary additions, Parts II–V | matching R | 1.5–2.5k w each |
| **H2–H5** | Compendium, Parts II–V | matching R | 1.5–2.5k w each |
| **J1** | Rumour and encounter tables, handouts | C2, R1b | 2–3k w |
| **K1** | Campaign log and continuity index templates | D1 | 1–1.5k w |
| **Z1** | Integration pass: contradictions across all files, index/TOC, final DM checklist | all | review log |

## Conventions for every campaign file

- Plain markdown in `campaign/`. Filename: `<ID>-<slug>.md`.
- Table-time voice: tight, concrete, no design-rationale prose.
- Mechanics: use the real ruleset if `campaign/system/` has it. If it does
  not, write archetype and tier only and mark anything that needs a number
  `(SYS?)`. Never invent attribute numbers, thresholds or costs that the
  ruleset defines. Monster numbers are generated live at the table. Any new
  surface rule goes in S1 tagged `(untested)`; other files cite S1 rather
  than inventing rules.
- Everything must be consistent with `novel/canon.md` and with chapter 25's
  ending state. Where it cannot be, log it in `campaign/DECISIONS.md`.
- No lyrics, no quotes from published games, no copying D&D text. Structure
  only.
