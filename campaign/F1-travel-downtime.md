# F1 — TRAVEL & DOWNTIME

*Reader: DM. Builds on `S1-surface-adaptation.md` (Crowns and Favours, the
Hub → Safehouses rule, Flight/Capture/Recovery, "no fast travel") and
`C1-gazetteer.md` (the Map, the Hydros) — read both first; this file does
not restate either. Cites `C2-factions-clocks.md`'s six clocks throughout,
`D1-bases-safehouses.md` for the Region I model this file generalises past
Region I, `H1-compendium-part-1.md` (the quartermaster's ledger convention
this file fills in), and `R1a`–`R5a`'s own §4 "Travel Summary" sections,
which already fixed every leg's duration — this file does not re-derive
distances, only prices them and says what happens along the way. No
`campaign/system/` ruleset exists yet (Q-1); every crown figure below is a
proposed shape, `(SYS?)` for the exact number, same as `S1` and `D1`.*

## How to use this file

`S1` set three rules this file has to make concrete: travel takes the time
`C1` says it takes and something happens during it; recovery is never
instant or free; a favour costs the relationship, not a resource tick.
`D1` built all three for Region I's four named bases. Regions II–V have no
equivalent base file queued (`PLAN.md`'s work-item table; `R2a`/`R3a` both
note the gap directly when inventing their own lightly-detailed footholds),
so this file's job is to give the DM something that works everywhere a
`D1`-style file doesn't exist, while still deferring to `D1` wherever it
already answered the question for Region I specifically.

## 1. Travel — The Commonwealth by Leg

Every leg below is fixed already, cited to where it was set; this file adds
a cost and nothing else to the geography.

| Leg | Mode | Duration (fixed by) | Crown cost |
|---|---|---|---|
| Stillwell ↔ the valley's northern edge | foot | under a day (`R1a`§4) | free |
| Valley's edge ↔ Hessel Bight | road, overland | 4 days (`C1`, the one hard-given distance) | free on foot; a cart hire, `(SYS?)` |
| Ammet Ford's rail halt → the trunk line | rail, company service | — | no fare; a favour owed to the Valley Trust the moment a party boards (`D1`) |
| Hessel Bight ↔ Vantry | road | 5–6 days, via Tannery Reach, Sennet, the Selwick turning (`R1a`§4) | free on foot; see Waypoint Lodging below |
| Hessel Bight ↔ Vantry | rail | under a day (`R2a`§4) | a fare, `(SYS?)` — moderate, the trunk line's ordinary ticket price |
| Vantry ↔ Carrowgate | rail | a day (`R2a`/`R3a`§4) | a fare, `(SYS?)` — moderate |
| Vantry ↔ Carrowgate | road | 3–4 days (`R2a`/`R3a`§4) | free on foot; see Waypoint Lodging |
| Valley–Vantry road/rail ↔ Carrowgate | changeover, undramatized | half a day (`DECISIONS.md` D-11) | a short second fare if by rail; otherwise nothing — it is a station, not a stop |
| Vantry ↔ Oldbridge | rail | half a day, last rail stop in the campaign (`R4a`§4) | a fare, `(SYS?)` — cheap, a short branch line |
| Oldbridge ↔ Lissom Fen | cart track | half a day (`R4a`§4) | a cart hire, `(SYS?)` — or free if the party walks it |
| Lissom Fen ↔ the House of Quiet Rest | foot | about an hour (`R4a`§4) | free |
| The House ↔ Greymere Hydro | service track | same afternoon (`R4a`§4) | free |
| Greymere ↔ Hollowmere | cart road, poorly kept | the better part of a day (`R5a`§4) | free on foot; no cart for hire out here — Rede's own wagon, or none |
| Hollowmere ↔ Fallow Head | coast path | under 2 hours at low tide; impassable at high tide (`R5a`§4) | free, tide-gated rather than priced |

**Rail fares, shaped not numbered.** Third-class rail is the ordinary
ticket a working party can afford without the trip itself being a plot
point — cheap enough that a DM should let the party take it without
accounting for every shilling, same as nobody in the novel ever budgets a
coach fare on the page. A faster or more private arrangement (a first-class
compartment, a chartered coach, the Valley Trust's own carriage) costs
noticeably more and reads as conspicuous exactly where the ordinary ticket
doesn't — visible wealth or visible company affiliation, either one worth
an NPC's second look. `(SYS?)` for the actual shilling figures; the shape
above is what a DM can run today.

**Foot and cart.** Walking a road leg is always free and always slower;
hiring a cart or coach is always faster and always costs crowns per day,
`(SYS?)` for the figure, and always means a driver who sees where the party
goes and who they travel with. A party with something to hide should feel
that trade every time, not just when the DM remembers to mention it.

## 2. What Happens on the Road

Per `S1`'s "no fast travel" rule, a leg with a fixed duration is never a
cut between scenes — this file sets what actually happens during one.

**One check per leg-day on anything over a day.** A short leg (under a day:
Stillwell to the valley's edge, Lissom Fen to the House) gets one check at
most, often none — these are errands, not journeys. A multi-day leg (the
four days to Hessel Bight, the five or six to Vantry, the three or four
road-days to Carrowgate) gets one check per day travelled, drawn from
whichever of the two tables below fits where the party is.

**Pest or social — the DM picks which table, not a die roll between them.**
Every region has a live Pest Pressure Clock instance (`C2` Clock 5); a
check in a region currently running hot (recent mining, construction, or a
thin site cracked open nearby) should draw from a worse pest-encounter tier
`(SYS?)` than a quiet one, same as `C2` already says. A check anywhere else
— which is most of them, because this is a campaign about institutions and
neglect, not a monster-of-the-week crawl — is a social or faction encounter
instead: a Mercy brother on the road (`hooks.md` #9's construct candidate,
reusable here without resolving it), a capping-schedule testing team
running late (the Capping Clock, `C2` Clock 1), a Valley Trust rider asking
too-casual questions, a broadsheet stringer chasing a stale lead. The
waypoint towns `C1` names for exactly this purpose — Tannery Reach, Sennet,
the Selwick turning — are where a social check should land rather than a
pest one, by design; `C1` built them as texture, not as dungeon rooms.

**Rail skips the check, and that's the trade.** Taking the trunk line
instead of the road removes the day-by-day checks entirely — a day on a
train is a day with nothing keyed to it, which is exactly why the fare
matters and exactly why a party that always rails past the Northern Road
never meets Brother Aldous, never sees Tannery Reach's parish dispute,
never has a reason to learn Selwick's own discrepancy firsthand. Speed and
story are the same trade `S1` already names for safehouses and favours;
this is its travel-table version.

**Waypoint lodging.** A multi-day road leg needs somewhere to sleep that
isn't a cold camp. Tannery Reach, Sennet, and the Selwick almshouse (per
`C1`) all take an ordinary lodger for an ordinary fare — cheap, no
favour owed, no tab kept, the ordinary-traveller version of Stillwell's own
no-strings model (`D1`). A party that skips lodging and camps instead saves
the fare and pays for it on the next day's check, drawn from whichever
table is worse for that stretch of road.

## 3. Recovery

`D1` built four bases' worth of recovery for Region I. Regions II–V have no
equivalent file, so this section gives the DM a tier system that works
anywhere, per `S1`'s rule that recovery is never instant or free:

- **Rough** (a cold camp, the road itself, nowhere with a roof a party has
  any standing at). Slowest, free, and risky — no one is helping, and
  whatever hurt the party stays exactly as hurt until somewhere better is
  reached. `(SYS?)` for the time band; the shape is "worse than anywhere
  else in this list."
- **Ordinary** (a paid room at any town with an inn, a Mercy House, or
  waypoint lodging per §2 above). Costs crowns, `(SYS?)` for the nightly
  rate, no favour owed, no one watching especially closely — the surface
  equivalent of Stillwell's own clerk-neutral model (`D1`).
- **Standing** (a safehouse the party has actual standing at — one of `D1`'s
  four in Region I, or whatever a DM has let the party build the same way
  in a later region, per `S1`'s rule that a safehouse is wherever the party
  has standing, not a fixed address). Cheapest in crowns, most expensive in
  attention: whoever runs the place will know exactly what state the party
  came back in and will remember it, same as Nessa Beddoe does (`D1`).
- **Specialist** (a hydro's hydropathic side, a Mercy House's actual
  infirmary, a company surgeon per the Ammet Ford model). Fastest, costs
  crowns or a favour depending which faction runs the place, and comes
  watched — per `D1`'s own Ammet Ford note, whatever hurt the party and
  whatever they say about it reaches that faction whether they mean it to
  or not.

A DM running a Part without a `D1`-style file should name, in one line,
which tier the party's current lodging falls into rather than inventing a
fifth category — the four above are meant to cover every later region the
same way they cover Region I, with the specific names supplied on the fly
(`R2a`'s Ress Tannery, `R3a`'s Caddock Lowe, `R4a`'s Rufus Pledge are all
already-named Standing-tier options; Greymere and the House of Quiet Rest
both plausibly double as Specialist-tier if a table's standing with Rede
or Anstey allows it).

## 4. Arcana Healing

Distinct from the recovery tiers above, and from the Salts' own injury
rules (which stay thin-site-only, per `C3`/`S1`). A party that finds or
befriends a native Arcana practitioner — rare, unregulated, mostly weak
(canon §5; `C2`'s Arcana practitioners entry) — can seek healing from them
as a downtime option, and that healing follows Maria's own hard limits
exactly (canon §2), never a cleaner version built for party convenience:
slow, effortful, no regrowth, no cure for the Sweetwater or anything like
it, no raising the dead, and the healer is left genuinely useless for some
time afterward, not inconvenienced. A healer who can do this more than
once in a day doesn't exist in this campaign; if a table wants faster
Arcana healing than that, the answer is "there isn't any," the same answer
the novel gives.

**The cost is visibility, not crowns.** `C2`'s Arcana practitioners entry
already states the risk plainly: an unusually capable practitioner draws
exactly the attention the Fourth Mercy's stud book exists to collect.
Every time a party uses the same Arcana healer twice, that healer's name
is one step closer to being worth recruiting, dressed as charity, or
simply disappearing into absolution's intake — a DM should let that cost
accrue quietly and cash it in later (an NPC healer who goes missing, a
PC with native Arcana who gets a second, too-interested visit from a
Mercy brother) rather than announcing it at the table as a meter filling
up.

## 5. Heat and Notoriety *(new — untested)*

Nothing before this file names a mechanic for what a region remembers
about the party. `PLAN.md` asks F1 for one ("heat and notoriety"); this
session proposes the shape, tagged `(untested)` like every other S1/F1
mechanic, logged as a new default rather than decided silently.

**Heat** is how dangerous or suspicious the party reads to one specific
faction, right now, in one specific region. It rises sharply with a scene
that faction would notice (a theft from the Valley Trust, a fight near
Church property, a name on a wanted notice) and decays on its own with
time and distance — a party that leaves a region for another Part mostly
leaves its heat behind, the same way `S1` already says a safehouse's
standing lapses once play moves on. High heat with the Church specifically
feeds the Press Cycle (`C2` Clock 3) if it crosses into something public;
high heat with the Valley Trust feeds the Consolidation Clock (`C2` Clock
6) instead. Heat is the fast, local, forgettable one.

**Notoriety** is slower and sticks: what ordinary people in a region have
heard, true or not, and keep repeating after the party has moved on. It
rises from word of mouth rather than institutional notice — a rumour at
Beddoe's slate, a line in the broadsheet that didn't name them but
obviously meant them, a name a capping-camp worker mentions to the next
village over. It can be good (the party that got the testing team through
Pellick on schedule) or bad, and unlike heat it doesn't decay just because
the party left — it waits for them to come back.

**Where this touches the rest of the file.** High heat with a faction
makes that faction's favours cost more to call in and its Capture outcome
(`S1`) harsher — the Church's crisis-PR instinct processes a low-heat
stranger gently and a known troublemaker as a liability to be contained
properly. High notoriety in a region changes what an NPC assumes about the
party on sight, before any roll: Nessa's slate, a hydro's clerk, a
Mercy brother on the road will all react to notoriety the party earned
three sessions ago whether or not anyone present today witnessed it
directly. `(SYS?)` for any hard threshold; until the real ruleset supplies
one, a DM tracking two or three words per faction per region ("Valley
Trust: hot," "Vantry: a name, not a face") is the whole mechanic.

## 6. Favours in Practice

`S1` sets the rule (a favour costs the relationship, not a resource tick);
this section gives the DM the concrete version `H1`'s quartermaster's
ledger already asked for.

**The ledger.** Keep one list per faction or named NPC, DM-visible only,
exactly in the shape Nessa's slate already models (`D1`/`H1`): a line per
favour owed in either direction, specific and short, never a number on a
character sheet. "Owes the broadsheet editor a story" or "the capping camp
owes the party an escort, unpaid" are both single lines; a favour with no
specific content attached isn't a favour yet, it's a vague promise, and
shouldn't be spent as one.

**A price list, shaped not numbered.** For whoever reconciles this against
the real ruleset (Q-1), the relative scale this file assumes:

- **Cheap** (a shilling or two): a meal, a night at waypoint lodging, a
  short rail fare, a rumour bought at a tavern.
- **Moderate** (several crowns): a multi-day rail fare, a cart hire by the
  day, an ordinary doctor's visit, a basic resupply of kit.
- **Dear** (tens of crowns, the kind of sum Edie's ledger itemises rather
  than rounds off): a bribe that actually moves someone, a surgeon's fee
  for something serious, a first-class or chartered arrangement.
- **Not for sale at any price**: the things this campaign's six factions
  actually want kept — the buried survey, the stud book, the Sanctum's
  cooperation. These only move for a favour, evidence, or leverage, never
  for crowns, and a DM should say so plainly if a party tries to buy one.

**Calling one in.** Per `S1`: using a favour can strain the relationship,
close it, or — rarely — turn an NPC into something closer to a standing
ally, DM's call scene to scene based on what was actually asked for and
how it was asked. A favour called in carelessly should cost more than one
called in with the specific, itemised care Edie's own ledger models
(`source-bible.md`); that difference in care, not a die roll, is the real
mechanic here.

## DM Notes

**This file prices geography and behaviour; it does not reopen any of
it.** Every distance above was fixed by `C1` or a Part's own §4 before this
file existed — if a number here seems to disagree with one of those, the
Part file is right and this file has a typo to fix, not a new decision to
make.

**Don't let crowns become the point.** Per `S1`'s own warning against the
surface economy quietly becoming a Token economy: the price list above
exists so a DM has an answer when asked, not so a table starts optimising
travel routes for fare efficiency. If a session's actual content is the
spreadsheet rather than the two waypoint towns the road passes through,
something has gone sideways.

**Heat and Notoriety are the one genuinely new mechanic in this file.**
Everything else here assembles what earlier files already decided;
treat §5 with the same "first draft, break it at the table" caution `S1`
asks for its own four replacements, more than the rest of this file.

## Cross-references

- `S1-surface-adaptation.md` — Crowns and Favours, Hub → Safehouses, Flight/
  Capture/Recovery, "no fast travel"; this file is the detail table `S1`
  itself deferred here.
- `C1-gazetteer.md` — the Map; every leg in §1 is cited to here or to a
  Part's own §4, which in turn cites `C1`.
- `D1-bases-safehouses.md` — the Region I recovery model §3 generalises;
  Nessa's slate as the favour-ledger model for §6.
- `C2-factions-clocks.md` — all six clocks; Clock 1 (Capping), Clock 3
  (Press Cycle), Clock 5 (Pest Pressure), and Clock 6 (Consolidation) are
  each cited directly against travel checks or Heat in §§2/5.
- `H1-compendium-part-1.md` — the quartermaster's ledger, whose price list
  this file supplies.
- `R1a`–`R5a` §4 ("Travel Summary" in each) — the fixed durations this file
  prices rather than re-derives.
- `novel/canon.md` §2 (Arcana's hard limits, applied to Arcana healing) and
  §5 (World, the Attrition's pest problem).
- `DECISIONS.md` — D-32 (Heat and Notoriety invented; the recovery-tier
  generalisation; the price-list shape), added this session. Jake can
  overturn any of it.
- `G2`–`H5`, `J1`, and `K1` remain; none depend on this file directly, but
  `J1` (rumour and encounter tables) should use §2's pest/social split when
  it's written.
