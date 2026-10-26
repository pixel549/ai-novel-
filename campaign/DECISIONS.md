# DECISIONS

Project-management file. Not loaded at the table.

## Defaults chosen (Jake can overturn any of these)

- **D-1 Timeframe.** The campaign opens roughly a year after chapter 25.
  Crane is dead and blamed on the Church; the works-water schedule has been
  brought forward and wells are being capped; Ferrick's sub-panel has momentum;
  the Church's Sanctum at Carrowgate is untouched and Vantry's Ascension House
  is a burned shell.
- **D-2 Player characters.** New characters, unconnected to Lloyd, Maria and
  Edie. The three can appear as NPCs under rules set in I1. Canon limits
  (e.g. Lloyd's second arm is never confirmed; Maria never learns of the five
  weeks) still bind.
- **D-3 Scope.** Five Parts (levels 1–100) are planned, but written
  playable-first: a vertical slice (brief, surface adaptation, a base, Part I)
  before depth. Part boundaries follow regions and arcs, not depth tiers.
- **D-4 Antagonist.** The Church of the Mercies and the Fourth Mercy remain
  the main pressure. Per canon stance, the institution is outlasted or
  escaped, not defeated or redeemed.
- **D-5 Tone.** Surface follows the novel's stance; the Salts, when they
  surface, follow Bloodborne dream-logic. See PLAN.md.
- **D-6 Bases.** The campaign has no single hub. Stillwell Hydro (where the
  novel opens) is one location among several bases. The reception clerk is
  never statted.
- **D-7 Insight.** Mechanically true in-game; socially disbelieved on the
  surface.
- **D-8 Format.** Built for an AI DM or small table, matching the ruleset's
  own assumptions.
- **D-9 Salts role (Jake, 2026-10-21).** The campaign is set in the real
  world after the novel, not in repeated Salts runs. The Salts are background:
  they explain part of the world's Arcana (chalice-granted powers such as
  Lloyd's) but not all of it (Maria's native Arcana stays unexplained, per
  canon). They appear in the campaign as lore and as a few short "thin site"
  incursions (T1–T3), not as the engine.
- **D-10 Surface rules.** Salts-loop rules (anchor chalice, hub banking,
  Abandon-All, Token economy, no fast travel) do not apply on the surface
  as written. S1 proposes replacements, tagged `(untested)`: crowns and
  favours for Tokens, safehouses for the hub, real travel, and a
  flight/capture/recovery rule in place of bail-out. Jake decides what sticks.

- **D-11 Carrowgate geography and the hydros network (session default,
  2026-10-26, for C1).** Two calls made to write the Gazetteer: (1) the road
  and rail between the Larrow Valley and Vantry pass within a half-day of
  Carrowgate's outskirts, close enough for the undramatized ch.12/13 stop
  (R-4) to be a station changeover rather than a detour — consistent with
  everything on the page (nothing rules it out) and with Lloyd's own nine
  years working in Carrowgate before the book opens; (2) Stillwell is not
  the Commonwealth's only hydro — canon §5's "the Church has been using
  [the Salts] industrially for years" implies a supply chain the novel
  never maps, so C1 assumes a small handful of further hydros exist
  elsewhere, unnamed and unplaced until a Part needs one. Neither call
  touches chapter text or contradicts canon; both are logged here per
  RUNBOOK's Phase 2 instructions rather than re-litigated in C1 itself. See
  `campaign/C1-gazetteer.md` → "The Map" and "The Hydros".

## Open questions for Jake

- **Q-1** The ruleset (v7), design bible (v2.5), dev log, character sheet and
  monster manual live in your Claude chats/project, not in this repo. Please
  add them to `campaign/system/`. Until then, numbers are `(SYS?)`.
- **Q-2** Is the novel's *Salts* identical to the game's, or a quieter
  corner of the same thing? Default: identical (the hydro, recipes, chalices
  and the anchor all line up already).
- **Q-4** Should the PCs be able to take the salts at all? Default: yes, but
  only at thin sites and at a price, so the option exists without becoming the
  loop.
- **Q-5** Which parts of the ruleset should stay untouched on the surface
  (combat, limb targeting, status effects, parry) versus be adapted? Default:
  combat and condition rules untouched; economy, recovery and travel adapted.
- **Q-3** Does the campaign want a canonical ending, or a set of possible
  endings? Default: several, ordered by cost, none clean.

## Blocked

(none)

## Review findings

First Saturday QA pass (2026-10-23), covering everything written for the
campaign phase so far: `campaign/PLAN.md`, `RUNBOOK.md`, `DECISIONS.md`,
`STATUS.md`, `system/README.md`, and `novel/readthrough/batch-1.md`–
`batch-4.md` (read-through notes for ch. 1–20), checked against
`novel/canon.md`, each other, and (for the two flagged chapter-text issues
below) the chapters themselves. No `campaign/system/` ruleset exists yet, so
nothing to check campaign files against on that front — none exist yet
either. One small fix made (`novel/outline.md`'s stale Cast-section line
still describing Lloyd's injury as his left arm, "regrown wrong," predating
canon.md's resolution — corrected to match canon.md Section 2; this was
flagged twice in batch-1/2 as a documentation-sync item and never itself a
chapter problem). Four larger items carried up from the batch notes, none
fixed, because each needs a judgment call rather than a mechanical
correction:

- **R-1 (ch. 7) — the ethereal arm lifts a solid object.** Canon Section 2 is
  explicit that Lloyd's ethereal second arm "cannot lift, carry, throw, or
  apply force to ordinary matter while ethereal" and "grants no strength
  beyond his own," reserving ambiguity only for combat against things seen by
  Insight. In ch. 7 the ethereal arm reaches into a stud bay and draws an
  ordinary three-foot iron rod bodily through solid lath into Lloyd's other
  hand, "solid" and weighted. The chapter itself lampshades the tension
  ("shouldn't be a thing that arm is allowed to touch... a weight to it that
  a thing made only of my own seeing has no business having") but doesn't
  resolve it. Batch-3's comparison point (ch. 15's ethereal-arm combat use,
  squarely inside the stated limit) strengthens the case that ch. 7 is the
  outlier. Needs a decision: ground it (the rod stays intangible to anyone
  but Lloyd, or he can't keep it) or accept it as an early, currently-
  unflagged expansion of what the arm can do, well ahead of the "clumsy
  early, fluent late" curve canon promises for later in the book.
- **R-2 (ch. 9) — Lloyd breaks the fourth wall.** Closing the chapter, Lloyd
  explicitly names the act of narrating and the existence of "a page in
  whatever this is." Canon Section 1's "Never" list for Lloyd is explicit
  ("Never articulate, never wry, never self-analysing out loud") and Section
  7 adds, book-wide, "No character ever names their own arc, growth, or
  psychology aloud." The line does not recur anywhere in ch. 10–25 — the rest
  of the book, confirmed clean as of the Phase 1 read-through's completion —
  which settles the question raised when this was first logged: it reads now
  as a one-off slip rather than an intended device. Needs a decision: let it
  stand as a single deliberate overreach (striking on its own terms), or walk
  it back to match Lloyd's established voice.
- **R-3 (ch. 16 vs. ch. 13) — three nights or four days.** Ch. 16 (Lloyd,
  delirious) narrates the Ascension House tank room as one he'd described to
  the others "from outside a barred window three nights running." Ch. 13's
  own text gives this as four days, twice over ("I counted that cart on both
  its days for four days running"; "On the fourth evening I came back from
  the chapel wall with the same report"). Ch. 16 is built around deliberately
  unreliable numbers elsewhere (the knot-cord counts ninety-one instead of
  nineteen, by outline mandate), so this could be the same conceit extending
  one step further into background detail, or it could be a plain slip — and
  unlike the cord, nothing marks this specific number as intentionally wrong.
  Needs a decision: leave it (read as delirium bleeding into a fact Lloyd
  should have straight) or correct "three" to "four" in ch. 16.
- **R-4 (ch. 12, ch. 13) — a Carrowgate stop that isn't on the page.** Two
  separate lines imply the trio passed through or connected to Carrowgate
  between ch. 6 and ch. 12, which isn't dramatized anywhere in the on-page
  route: ch. 12's "the bonesetter in Carrowgate had sworn it would settle"
  (of Lloyd's arm) and ch. 13's "her bundle still tied the same knot it had
  been since Carrowgate" (of Maria's). Not a confirmed contradiction — there's
  room for an off-page stop — but worth a call only if it matters for the
  Gazetteer's geography (C1); otherwise it can stand as unresolved backstory.

Second Saturday-adjacent finding, added same session after P1.5 (read-through
ch. 21–25) — see `novel/readthrough/batch-5.md`:

- **R-5 (ch. 23) — the Still Mind registers a dropped tray.** Canon Section 2
  is explicit: Edie's ability "covers violence only. Not lies, not
  intentions, not danger in general. A collapsing floor does not register. A
  man deciding to hit her does." In ch. 23, her Still Mind flinches a
  half-second ahead of a tray dropping elsewhere in Ferrick's house — an
  accident with no person's violent intent behind it, the same category of
  event canon's own example rules out. This is not a drafting slip:
  `novel/outline.md` (line 552–555) specifies the beat deliberately ("The
  Still Mind catches once in the chapter, uselessly, on nothing worse than a
  dropped tray... the smallest possible rehearsal of the gap she's lived in
  since the tunnel"), so the contradiction sits between the outline and
  canon.md's hard limit, not between the chapter and its outline. Needs a
  decision: loosen the hard limit to cover sudden/startling accidents
  generally, or re-ground the scene so what she senses is a person's sharp,
  violence-adjacent reflex near the tray (someone lunging to catch it, say)
  rather than the tray's fall itself.

None of R-1–R-5 were touched in chapter text this pass, per RUNBOOK (Phase 1
is read-only on chapters; anything beyond a one-line slip gets logged, not
rewritten). All five are also cross-referenced in the relevant batch's "Open
threads" / "Structural issues" sections for SYNTHESIS (P1.6) to weigh. The
Phase 1 read-through (all 25 chapters, batches 1–5) is now complete.
