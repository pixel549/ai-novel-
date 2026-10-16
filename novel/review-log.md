# Review log

Weekly consistency-review pass. Unlike nightly drafting sessions (summaries
only), this pass reads every drafted chapter in full against `canon.md` and
`outline.md`. Entries are dated, newest first.

---

## 2026-10-16 — Review of chapters 1–25 (book complete)

Backup tag `backup-pre-review-2026-10-16` created locally before any changes.
Tag push to origin was refused with a 403, same as every prior review —
carrying on per standing instructions; the commit history is the rollback.

The novel finished since the last review: chapters 23, 24, and 25 (the Ferrick
house visit, the Crane killing, and the "Year Seven" epilogue) have landed,
taking the book to its full 25 chapters and closing Act III. All 25 chapters
were reread in full this pass — not just the three new ones — specifically
because a book that's just gone to a close is exactly where an early-chapter
promise and a late-chapter payoff are most likely to have quietly drifted
apart.

### Needs your attention

**The clearest finding this week is a timeline inconsistency around Edie's
confession in ch. 24, baked into the outline itself rather than introduced by
the draft.** Canon and outline both fix the Attrition as ending nineteen
months before ch. 1, and the outline places Colonel Reyne's tunnel collapse
"in the last year of the war" — so the collapse, and Edie's killing of Reyne
eleven weeks later, happened roughly 1.5–2.5 years before ch. 1, not more.
Ch. 24 happens well under a year after ch. 1 by the book's own internal
clock (ch. 24 itself says "in four months" of Edie visiting them in
Carrowgate, measured from their arrival there in ch. 20, which checks out
against everything in between). That puts Edie's confession at something
like two to three years after she killed Reyne — but the text has her say,
twice, "Nine years ago I served under a colonel..." and "I've... spent nine
years insisting on a line." Nine is nowhere close to two or three. I don't
think this is a drafting slip so much as a pre-existing tension in the
reference documents: outline.md's own ch. 24 notes call for "nine years,"
likely because it was written to echo Lloyd's own nine years away from
Callow Ford (a deliberate parallel between the two characters' long-held
secrets, and a nice one), without being checked against "ended nineteen
months before ch. 1" + "last year of the war" elsewhere in the same document.
I haven't touched the text, because which fact is the one that's "wrong" is
a judgment call, not a mechanical fix: either the Attrition-recency numbers
move, which would ripple into the Reconstruction-hasn't-reached-the-valleys
theme threaded through chapters 8, 9, and 21–22, or Edie's "nine years"
becomes something smaller (and loses the Lloyd echo), or it's left exactly as
drafted on the theory that a devastated, traumatized woman's "nine years" is
emotionally true rather than a number she'd actually be able to audit, and
nobody's going to do this arithmetic while reading. I'd lean toward the last
of those three myself, but it's your call, not mine.

**Softer and not a contradiction, just under-explained:** ch. 24 has Edie
produce her own private security floor plan of Ferrick's townhouse — "kept in
a drawer at the townhouse, marked up by my own hand and nobody else's, for
two years" — with three crosses on it that are Lloyd's. But the floor plan
Maria found in Lloyd's coat back in ch. 20 reads, by every detail around it
(a "chief clerk," a "west stair... shut Tuesdays, carpet men in," a numbered
central chamber), like a plan of the Indemnity Office or some other
government building, not a private family townhouse. Nothing on the page
ever shows Lloyd getting into Edie's own locked drawer at Ferrick's house to
mark up that specific document — his established recon (ch. 20–22) was all
in government offices and chop-houses, and the one time we see him physically
inside the townhouse (ch. 24 itself) is explicitly his first time there,
arranged "last week" by Edie for that day's killing. It's not unreasonable
that he scouted the townhouse too, off-page, sometime after learning Maria
had been inside it (ch. 23) — he's established as exactly the kind of patient,
quiet infiltrator who'd do that without telling anyone — but the text doesn't
say so, and the mechanism by which Edie's discovery works (her own, long-kept,
private plan, marked by a hand that wasn't hers) is the engine of the whole
chapter. Worth a read with this in mind; I'd call it elidable rather than
broken, but it's close enough to the chapter's load-bearing beam that I didn't
want to decide that for you silently.

**Much smaller, mentioned only because I found it while checking the above:**
ch. 25's opening paragraph attributes "ringed in red on his own wall" to "the
sub-panel's old figures" (the water-safety report), but ch. 23 establishes
the red ring specifically on the calendar date for the Church/Vantry hearing,
a different document entirely — and ch. 25's own later scene (the Ferrick
house visit) correctly calls back to "the spring hearing's date ringed twice
in red." Likely just a loose reuse of the image rather than a real confusion,
and arguably reads fine as "everything on his wall that mattered sat in red
ink and went nowhere" — I left it alone, but flagging it in case you read it
differently. In the same paragraph, "the schedule came forward eleven years"
for the water-remediation timeline sits next to "beat that arithmetic by six
years and some months" for the Indemnity payout a few lines later; these are
two different schedules (remediation timeline vs. the seven-year payout) and
don't contradict each other once you track which is which, but a reader
moving quickly could conflate them. Not fixed, just noted.

### Fixed directly (small, mechanical)

- **`chapters/24.md`** — Ferrick's townhouse was described as having "its
  brass plate" (implying a plate announcing it as a government building),
  directly contradicting ch. 23's established and thematically pointed detail
  that the house has "no plate on the door... the absence was the guard, not
  the lack of one." Reworded to drop the brass plate and echo the "no plate"
  detail instead, so the two chapters describe the same house consistently.
- **`chapters/25.md`** — the planted evidence at Crane's death was introduced
  in ch. 24 as "a torn scrap of vestment thread," then referred back to in
  ch. 25 as "a scrap of altar-cloth" — two different objects standing in for
  the same single prop. Standardized ch. 25 to "vestment thread," matching
  ch. 24 and `motifs.json`'s `vestment-thread-frame` entry.

No other canon contradictions, timeline/geography inconsistencies beyond the
one flagged above, dropped-and-contradicted plot threads, characterization
drift, or POV violations found anywhere in chapters 1–25. Specifically
checked and confirmed clean on this pass: the who-knows-what table (Lloyd's
second arm and the ch.-3-regrowth truth never told to Maria or Edie; Maria's
theft and Lloyd's five weeks in Carrowgate never leak into Maria's or Edie's
own narration respectively; Edie's killing of Reyne reaches Lloyd and Maria
only in ch. 24, on schedule); Vail's hard prose rules across all four of her
on-page appearances (ch. 12, 13, 15, 18 letter) — no lowered voice, no
threat, no banned staging cue anywhere, including a line-by-line check for
"cold," "flat," "chill," "seemed," and doorway-lingering around every Vail
scene; the Insight ambiguity, specifically including Crane's death in ch. 24,
which stages the killing (no mark, nothing a coroner could name, "something
moved across his face that had nothing to do with pain yet") in a way that
never actually confirms Lloyd's ability caused it rather than a convenient
natural collapse — the hard limit that the ethereal arm "cannot apply force
to ordinary matter" is never shown being broken on the page, because the
book never commits to saying what happened at all. That's a deliberate and
well-handled use of the ambiguity rule at the highest-stakes possible moment,
not a hard-limit violation, and worth calling out as something that worked
rather than just something I checked.

### Change requests

None opened. The timeline item above doesn't need `outline.md` to change in
the sense `change_requests.md` is built for — there's no future drafting left
to protect, and both ways of resolving it (adjust the Attrition's recency, or
adjust Edie's "nine years") are small, contained copy-level decisions once
you've picked one, not outline amendments. Left for your call in "Needs your
attention" above. `change_requests.md` itself is unchanged (still no open
requests).

### Motif ledger (`novel/motifs.json`)

Current and in excellent shape. Spot-checked every motif introduced or paid
off in chapters 20–25 against the actual text (`crane-floor-plan`,
`stone-dust-boot`, `coin-stacking`, `ferrick-letters-hall`,
`locked-cabinet-nursery`, `ferrick-red-ring-calendar`, `edie-four-person-
detail`, `edie-own-floor-plan-crosses`, `vestment-thread-frame`,
`home-roof-gap`, `crooked-arm`) and every one matches what's on the page,
including the payoffs ch. 25 was written to deliver and the handful of
already-logged, deliberate minor cooldown breaches (`edie-four-person-detail`
at two chapters early, `coin-stacking` at three chapters early against its
own `min_gap`) — both already correctly annotated as intentional rather than
missed. No stale `last_used` values found, no new breaches. Nothing needed
updating.

### Prose-habit counts (`novel/voice_ledger.json`)

Recounted the two exact-substring constructs — `the-way-simile` and
`a-thing-abstraction` — across all 25 chapters with a fresh script, hand-
checking every hit against its sentence the same way the 2026-10-09 review
did, specifically to catch anything the chapter-by-chapter nightly passes
might have missed by only ever seeing their own chapter. Every single count
matched what's already on file, chapter for chapter, with no corrections
needed — both constructs are exactly as rested/retired as the ledger already
says. Spot-checked the 40+-word-sentence counts with a script of my own; my
naive automated sentence-splitter disagreed with the filed numbers by one or
two sentences in a handful of chapters (mostly around scene-break markers and
quoted dialogue, which a script without hand-checking handles worse than a
human reader does), never by more than three, and never in a way that changed
which band a chapter falls in. Given the existing counts were explicitly
hand-verified chapter by chapter already, I'm treating the filed numbers as
the real ones rather than overwriting good manual work with a cruder script's
output. The aphorism, same-as, clerical-metaphor, negation-doubling, which-
appositive, as-if, and both i-have/i-did-not anaphora entries were checked
against the actual prose in every chapter they cite (including rereading the
specific quoted examples in context) and all of them matched the text
exactly, including the fine distinctions the notes already draw (e.g. ch.
25's "I have learned not to answer that one quickly" correctly logged under
`i-have-had-anaphora` rather than the aphorism entry, which I confirmed reads
as a flat personal habit rather than a stated general rule, same call the
ledger already made). No new recurring construction, gesture, or closer
found beyond what's tracked. The ledger's own "final entry" markers on most
constructs are accurate — the book is done, and the ledger reflects that.

**Quality beyond the counts:** reread chapters 23–25 specifically for
sentence-shape or paragraph-ending sameness the counts wouldn't catch, since
those are the three chapters a prior full-book review hasn't seen yet. Ch.
23 and 24 each end on a bare physical object (a locked front door against
unbuttoned weather; bread and three crosses facing up at nobody), and ch. 25
ends on a held hand and a repeated line of dialogue rather than a third
object-close in a row — the ledger's own `narrator-explains-the-scene` entry
already tracks this rotation and nothing here contradicts it. No new
sameness found.

### Anything else worth noting

The book is complete at 25 chapters, roughly 59,500 words, inside the
pipeline's stated band in every chapter (1,848–3,197 words). Twenty-five
chapters in, canon's hard limits on all three abilities, the Insight
ambiguity, Vail's writing rules, the authorial stance in canon §8 (the cost
test, Edie never getting a heroic clean save, Maria keeping her humor even at
the worst of it, the ending landing on "something person-sized surviving, at
a real price, with the rot substantially unhealed" rather than either triumph
or total grinding-down), and the who-knows-what table all hold up under a
full reread of the finished book, not just a chapter-by-chapter one. The two
mechanical fixes above are the only things that needed a line edit anywhere
in the full 25 chapters. `README.md`'s "Known gaps" section is now stale — it
still frames ch. 16 as an open risk to watch and tells a future session to
"check `change_requests.md` before drafting Act II," both of which were
settled chapters ago and the second of which no longer applies at all now
that the book is finished. I haven't touched it, since it's outside this
review's scope (`chapters/` and `novel/`), but it's worth a pass whenever
you're next in the repo, if only so nobody reads it as current guidance.

---

## 2026-10-09 — Review of chapters 1–22

Backup tag `backup-pre-review-2026-10-09` created locally before any changes.
Tag push to origin was refused with a 403, same as the 2026-10-02 review —
carrying on per standing instructions; the commit history is the rollback.

Ten chapters have landed since the last full review (13–22), taking the book
from the end of Act I's aftermath through to the end of ch. 22 — the whole of
the Fourth Mercy raid, Lloyd's delirium, and five Act III (Maria) chapters
covering the recovery, the Vantry fallout, and the discovery and confession of
the Crane plan. All 22 drafted chapters were reread in full this pass, not
just the new ones, since a contradiction between an early and a late chapter
is exactly the kind of thing a summary-only nightly session can't catch.

### Needs your attention

Nothing structural. No canon contradictions, timeline or geography
inconsistencies, dropped-and-contradicted plot threads, characterization
drift, or POV violations found anywhere in chapters 13–22, and the fixes from
the 2026-10-02 review (chapter 1's ending, chapter 2's ability framing,
chapter 6's tense problem, the arm-regrowth canon note) are all still holding
correctly in 13–22's references back to them. The who-knows-what table is
being respected exactly: Lloyd's second arm and the ch.-3-regrowth truth are
still never told to Maria or Edie; Maria's theft and the five weeks in
Carrowgate stay where they were; Maria learns of the Crane plan in ch. 20 and
Lloyd confesses it in ch. 21, on schedule; Edie's "charge" stays unnamed to
Lloyd and Maria throughout (the broadsheet prints "Ferrick" in ch. 18 as a
public byline, but nothing on the page connects that name to Edie for either
of them yet). Vail's three on-page appearances (ch. 13's imbuing scene, ch.
15's yard confrontation, ch. 18's letter) all stay inside canon §3's hard
rules — no lowered voice, no threat, no banned staging cue, menace carried
entirely in what she says. Maria's and Edie's ability limits hold throughout
the siege (ch. 15): two lightning bolts, hated both times; the sustained-light
use introduced as the deliberately undramatic one; Edie foreseeing a blow and
still taking it on the ribs, no heroic clean save.

One gap worth flagging even though it isn't a contradiction: outline ch. 5
specifies a chalice cost for Edie ("Edie gives up sleeping without waking
twice") alongside Lloyd's memory cost, which ch. 5 does dramatize on the page.
Edie's cost never appears anywhere in chapters 1–22 — not in ch. 1–5 itself
(the extraction happens same-day, so there's no "next night" inside Act I to
show it), and not in any later chapter, because Edie has had no POV chapter
since and the detail is invisible from outside unless someone notices her
waking at night, which nobody has yet had cause to narrate. This may simply
be a cost the book never puts on the page — it doesn't block anything — but
it's been quietly undramatized for 22 chapters running and seemed worth
surfacing rather than letting it go unmentioned indefinitely. Not opening a
change request for it, since no outline content needs to change; just flagging
it as something you may want a nightly session to work in as incidental color
(Lloyd or Maria noticing her awake at an odd hour) if a convenient scene comes
up, or to consciously decide is fine left as implicit.

### Fixed directly (small, mechanical)

No chapter text needed fixing this week — chapters 13–22 came out clean
against canon and the outline, and chapters 1–12 are unchanged since the
2026-10-02 fixes. This week's direct fixes are all to the reference ledgers:

- **`novel/motifs.json`** — `wrist-healing-ridge` (the badly-knit wrist ridge
  from Lloyd's ch.-15 arm, healed in ch. 17) breached its own 10-chapter
  cooldown: ch. 20 reuses the exact image twice in one chapter ("a man
  rebuilding a body that still caught at the wrist when he closed his fist too
  fast"; "the newer scar, the wrist that still caught"), only three chapters
  after ch. 17 introduced it. Not a factual error — the detail is still true
  of him — but it was spent twice as passing texture rather than on a scene
  where the catch means something, which is how it burned through the
  cooldown this fast and went unnoticed (nightly sessions only see their own
  chapter against the ledger's `last_used`, which was already wrong by the
  time ch. 20 drafted). `last_used` corrected to 20 with a note to spend it on
  a beat next time, not a description.
- **`novel/motifs.json`** — `shawl-wrap`'s `last_used` was stale at 10 in all
  three lists (action/character/atmosphere); the real last appearance is ch.
  11 ("Maria pulled her shawl up over her nose..."), still well inside every
  list's own cooldown so not a breach, just an uncorrected count. Updated to
  11; it's been dormant for eleven chapters since and is fine to use again
  whenever a cold or dirty scene wants it.

### Change requests

None opened. Nothing found this week rises to an outline amendment — see
"Needs your attention" above for the one open item, which doesn't need
`outline.md` or `canon.md` to change.

### Motif ledger (`novel/motifs.json`)

Beyond the two `last_used` corrections above, the ledger is current. The
chapter-20-onward entries (`crane-floor-plan`, `stone-dust-boot`,
`coin-stacking`, `vail-letter-floorboard`) are all accurately tracked and
their notes match what's actually on the page. The deliberately-unresolved
items (`the-kept-thing` from the siege, the Insight ambiguity generally) are
correctly still open and correctly not nudged toward resolution by anything
in 17-22.

### Prose-habit counts (`novel/voice_ledger.json`)

Recounted all four tracked constructs for every drafted chapter with a fresh
script (exact substring search for "the way" and "a thing", a word-tokenizing
sentence splitter for the 40-word threshold, each chapter's hits hand-checked
rather than trusted to a fixed idiom blocklist, since a blanket filter was
itself causing errors — see below). Corrected counts, against what was filed
before this review:

| Chapter | "the way" (was → now) | "a thing" | aphorism | 40+-word sentences (was → now) |
|---|---|---|---|---|
| 01 | 0 | 1 (new) | 0 | 1 → 7 |
| 02 | 0 | 0 | 0 | 0 → 1 |
| 06 | 5 → 6 | 0 | 0 | 14 |
| 07 | 14 → 15 | 6 | 0 | 26 |
| 08 | 17 → 18 | 7 | 3 | 23 |
| 09 | 18 | 2 | 1 | 21 |
| 21 | 0 | 0 | 0 → 1 | 16 |

Everything not listed above checked out unchanged. Three distinct causes for
the corrections, all now noted in `voice_ledger.json` itself:

- **Stale pre-rewrite counts.** Chapters 1 and 2 were both substantively
  rewritten in the 2026-10-02 addendum (ch. 1 completed with a new ending,
  ch. 2's fight rewritten to fix the ability-creep finding) but neither
  chapter's prose-habit counts were retaken afterward. The new material in
  both carries habit instances that were never on file. General note added to
  the ledger: a chapter's counts need retaking whenever it's substantively
  rewritten later, not just logged once at first draft.
- **An idiom filter that was itself too blunt.** The "the way" undercounts in
  ch. 6-8 all trace to the same mechanical error: a blanket exclusion for
  idiomatic phrases like "in the way" or "way off" was also catching genuine
  manner-clause uses that happen to share a few words with an unrelated idiom
  nearby in the same sentence ("in the way I knew thin", "the way men read
  something" sitting close to an unrelated "way off shift"). Fixed by hand-
  checking every hit against its actual sentence rather than trusting the
  filter; this is a one-time correction, not a sign the underlying habit is
  worse than tracked.
- **A quiet instance nightly review missed.** Ch. 21's aphorism count was
  filed as a clean twelfth chapter in the streak, but "There are rooms in him
  I have learned not to knock on" is the pattern exactly as defined (compare
  the ledger's own example), delivered quietly rather than as a flagged
  aside, which is presumably why it read as clean on a single-chapter nightly
  pass. Corrected to 1.

**New construction noticed:** `i-did-not-anaphora` — sentence-initial "I did
not [verb]," often arriving in short runs, distinct from the already-tracked
`i-have-had-anaphora` (present/past-perfect openers) and `negation-doubling`
(a clause negated against itself within one sentence). Counts: ch. 17: 3,
ch. 18: 3, ch. 19: 5, ch. 20: 6, ch. 21: 0, ch. 22: 2. Never flagged before
because no single chapter's count looked alarming in isolation — it only
shows up reading Act III's chapters together, which is exactly what this
weekly pass is for and a nightly pass can't be. Ch. 19's five-in-a-row is a
deliberate, well-earned rhetorical list (everything Maria kept from the
others, named explicitly as a list); ch. 20's six are scattered rather than
massed and read closer to a default tic than a device. Added to the ledger
with a recommendation that nightly sessions let a short deliberate list stand
but watch for ch. 20's scattered-six shape recurring.

**Quality beyond the counts:** no new chapter-ending or paragraph-shape
sameness found beyond what the ledger already tracks (the closers entries are
current through ch. 22 and match what's actually on the page). The one real
finding in this category is the `i-did-not-anaphora` pattern above — Maria's
Act III voice has a genuine, growing habit of listing what she withheld
rather than stating what she did, and ch. 20 is where it starts to read as
reflex rather than craft.

### Anything else worth noting

Twenty-two chapters in, the book is in good shape. The Insight ambiguity, the
Vail writing rules, the who-knows-what table, and the authorial stance in
canon §8 (the cost test, Edie never getting a heroic clean save, Maria
keeping her humor even at the worst of it) are all holding up under a full
reread, not just a chapter-by-chapter one. The only thing worth watching
going forward isn't a correctness issue: ch. 21 and ch. 22 ran noticeably
shorter and more dialogue-dense than the chapters around them (1,922 and
1,904 words against a 1,800-3,200 band that's mostly running 2,100-2,400
lately), which tracks with both chapters being built mostly from direct
confrontation rather than description — not a problem on its own, but worth
knowing if the back half of Act III starts feeling thin the way the README
already flags ch. 16 as a risk chapter.

---

## 2026-10-02 (addendum) — Follow-up fixes on Jake's direction

Jake reviewed the findings below and asked for all four open items to be
resolved rather than left as flags, and supplied the key that unlocks the
first one: the ch. 3 "regrowth" isn't fully Maria's healing — it's the Salts
doing it, the same source the second, ethereal arm comes from at the chalice,
and that's worth a horror beat in Lloyd's own POV rather than a silent fix.
All four are now done:

- **Canon contradiction (Maria's healing vs. ch. 3 regrowth) — resolved, not
  just patched.** Added a note to `canon.md` §2 (Lloyd's ability section)
  making it canon: Maria's healing in ch. 3 really did close the wound, set
  the bone, stop the bleeding — all within her stated limits — but the
  forearm, wrist, and fingers that filled in beneath her hands came from
  whatever the Salts already had waiting there, the same source the second
  arm manifests from at the chalice. She believes she regrew it. She didn't,
  and never finds out she didn't. Added a row to the §6 who-knows-what table
  ("The ch. 3 regrowth wasn't Maria's doing" — Lloyd only, ch. 6, never told).
  The passage itself lives in the rewritten ch. 6 (below) rather than as a
  change to ch. 3's already-committed, Edie-POV text — Edie has no Insight
  and genuinely has no way to perceive anything beyond an ordinary, if
  remarkable, healing, so nothing in ch. 3 needed to change for this to hold
  together.
- **Chapter 1, completed.** Wrote the missing ending — the rest of the steam
  room beat, the timer sounding, stepping into the cold corridor, towels,
  Lloyd wiping his forearm, Maria's shawl, Edie pocketing the token — landing
  on the doorway image the frozen skeleton's `ends_on` already specified.
  Chapter is now 2,824 words (was 2,247 and incomplete), within the pipeline's
  1,800–3,200 word band. Caught myself reaching for Lloyd's "the way [clause]"
  tic twice while drafting this in Edie's voice and rewrote both — that
  construction has a clean 0 count across all of Act I and should stay that
  way; it's specifically a Lloyd habit. Updated `chapters/01.summary.txt`
  again to cover the now-complete chapter.
- **Chapter 2's ability-creep, fixed.** Rewrote Maria's second use of Arcana
  in the wire-creature fight: it no longer delivers a "concussive pulse" that
  physically slams and pins the creature to the wall (a kinetic-force effect
  canon doesn't give her). It's now an overexposure of light with no force
  behind it, and the creature's reaction is a flinch/recoil rather than being
  physically thrown — giving Lloyd a still target to land his second strike
  on, same plot function, without the ability reading as a weapon. Updated
  the one downstream reference ("Maria's pinned pulse" in the paragraph where
  the creature finally breaks) to match. Her first use of light in the same
  fight (locking Lloyd's strike line steady) was left alone — that one reads
  fine as an intensified, combat-pressure version of her canon Steadying
  knack rather than a new force ability.
- **Chapter 6, fully rewritten.** Fixed the present/past tense defect
  end to end (it traced to the unify pass pasting the frozen skeleton's
  present-tense event lines in verbatim as paragraph openers — confirmed by
  comparing the committed text against `workspace/06/skeleton.txt`) and cut
  the doubled-up beats that came with it. All twelve skeleton events are
  preserved, the chapter still ends on the frozen `ends_on` line exactly, and
  this is where the Maria's-healing reveal above now lives: a private,
  guarded passage right after Lloyd checks his arm's balance on stepping
  outside, where he admits to himself (and only to us) that what came back
  under Maria's hands didn't feel grown, it felt delivered — the same way the
  second arm later arrives already whole — and that he's never going to ask
  her whether she can tell the difference between what she did and what she
  thinks she did. New chapter is 1,853 words (was 1,950), still inside the
  1,800–3,200 band. Recounted its prose-habit stats afterward and updated
  `voice_ledger.json`: "the way" went from 4 to 5 true uses (trimmed down once
  from a first-pass 7, specifically so fixing one problem didn't create a
  second one), 40+-word sentences recount to 14. The ch. 6/7/8 "patient
  inevitability" closer note from the main review still applies unchanged —
  ch. 6's closing line wasn't touched.

Nothing here required touching `change_requests.md` — all four were either a
pipeline-output bug (ch. 1), a now-resolved canon clarification (the arm), or
in-chapter execution fixes (ch. 2, ch. 6), not outline amendments.

---

## 2026-10-02 — Review of chapters 1–12

Backup tag `backup-pre-review-2026-10-02` created locally before any changes
(tag push to origin was refused with a 403, as has happened before on this
repo — carrying on per standing instructions; the commit history is the
rollback).

### Needs your attention — most important item first

*All four items below were resolved the same day — see the addendum above
this entry for what changed. Left in place as the record of what was found.*

**Chapter 1 is incomplete.** `chapters/01.md` cuts off mid-sentence
("...the far wall vanished behind a wall of grey-white") and never reaches the
end of its own frozen skeleton. The skeleton for ch. 1 specifies 10 beats; the
committed text stops partway through beat 9 (entering the steam room) and is
missing all of beat 10 (the timer sounding, towels, Lloyd wiping his forearm,
Maria wrapping her shawl, Edie pocketing the token) and the chapter's own
`ends_on` line ("I stand in the doorway of the hydro, steam still curling,
the iodine-stained sign flickering above the entrance").

This is a drafting-pipeline bug, not a canon problem: `workspace/01/editor.log`
shows the editor correctly rejected an earlier attempt for this exact reason
("cuts off mid-sentence and fails to include events 2 through 10"), but then
passed a *later* attempt (`revision_2.txt`) that has the identical truncation
problem, just padded up to a passable word count. The editor's length check
apparently doesn't also verify the chapter reaches its final skeleton beat.
I did not attempt to write the missing ending myself — finishing it means
drafting new prose in Edie's voice to hit specific remaining beats, which is
real drafting work, not a mechanical fix, and this review's brief is to flag
structural gaps rather than act on them. Recommend re-running chapter 1
through the pipeline (`--force`, possibly `--stop` after unify to inspect
before spending an editor pass) or hand-finishing the last ~300–400 words.

Related, smaller bug I *did* fix: `chapters/01.summary.txt` contained a leaked
`<think>` reasoning block from the summariser model and was itself truncated
mid-sentence — the exact bug fixed two chapters later in commit `bff46fb`
("Strip leaked `<think>` reasoning from summariser output"), just never
re-run for chapter 1. I replaced it with a clean four-sentence summary of what
chapter 1 actually contains (not what it's missing), so nightly sessions
drafting future chapters get usable context. This is cosmetic housekeeping,
not a fix for the chapter's missing content.

**Maria's healing of Lloyd's severed arm (ch. 3) conflicts with canon's hard
limit on her healing (canon.md §2).** Canon states her healing "does not
regrow" and "costs her hours and leaves her useless afterwards." Chapter 3
has her regrow his entire severed forearm, including a new hand and five
fingers, in what reads as a single continuous scene with no hours-long cost
shown. This is not a drafting slip, though — `outline.md`'s own ch. 3 beat
explicitly calls for it ("Maria talks him through the regrowth like she's
done it before, because she has. It comes back wrong."), and the regrowth is
load-bearing: ch. 5's chalice scene needs Lloyd to already have a normal-
looking right arm for the Second Right ability to attach to. So this is a
contradiction between the two frozen reference documents themselves, present
since before any of this was drafted, not something introduced by a chapter
going off-script. I haven't touched `canon.md` or the chapter — that's your
call, not a change-request-against-the-outline situation (canon.md has no
amendment process of its own). The cleanest fix is probably a one-line carve-
out in canon.md's healing limit, something like "the one exception is the
ch. 3 regrowth, which is why it is singular and extraordinarily costly — it
is not a repeatable capability," so future chapters don't accidentally cite
ch. 3 as precedent for cheaper healing later in the book.

**Maria's combat ability in chapter 2 reads as more than "Light."** Canon
lists her Light ability as "reliable, cheap, sustained. The most useful thing
she does" — essentially illumination. In ch. 2's fight with the wire creature,
what she casts behaves as a concussive, directional force: it locks Lloyd's
arm into a strike line, then slams the creature flat against a granite wall
with "a heavy, hollow thud" and pins it there. That's closer to a kinetic
weapon than canon's stated utility ability, and sits in some tension with
§2's explicit instruction that "she is a dangerous individual, not a weapon,
and every fight should make that distinction obvious." Flagging for your
awareness rather than touching it — it's the chapter's central set-piece, so
any fix is a rewrite, not a line edit.

**Chapter 6 has a chapter-wide prose defect, not just habit drift.** Nearly
every paragraph in ch. 6 opens with a present-tense topic sentence and then
continues in past tense — e.g. "I step out of Stillwell onto the cobbled
street... My boots hit the wet stone," or "Edie opens a ledger, tallies the
cost of the journey east... She pulled a bound book..." This happens
roughly once per paragraph for the entire chapter and reads like an
unconverted skeleton beat line left at the top of each paragraph rather than
folded into the prose — it violates canon §7's flat "first person, past
tense" rule, and it also makes the chapter noticeably more repetitive and
weaker than the chapters on either side of it (several beats are stated twice:
once as a present-tense label, once as the past-tense scene). This is too
pervasive to be a one-line mechanical fix, and it's not a canon-fact
contradiction either, so it doesn't fit cleanly into a change request — it's
a craft problem with the chapter as drafted. I'm flagging it the way the
README already flags ch. 16: chapter 6 reads like a strong candidate for a
hand revision or a re-run, at your discretion. I did fix the two small
continuity slips inside it (below) since those were one-line and unrelated
to the tense problem.

### Fixed directly (small, mechanical)

- **`chapters/06.md`** — "She's still in *Carrow Ford*?" corrected to
  "*Callow Ford*" (Lloyd's home village; "Carrow Ford" isn't a place in this
  book and reads as a slip toward "Carrowgate," the capital).
- **`chapters/06.md`** — "the elbow had been broken and put back together
  *twice*" corrected to "...put back together *wrong*." Lloyd's right elbow
  has only been broken and reset once at this point in the story (ch. 3);
  canon's "broken ... twice" detail belongs to his *nose*, not this arm.
- **`chapters/01.md`** and **`chapters/05.md`** — Edie's deafening camouflet
  is named three different ways across the drafted chapters ("the camouflet
  at the third sap" in ch. 1, "a camouflet at the Red Redoubt" in ch. 3, "the
  camouflet at the fourth sap" in ch. 5). Canon doesn't specify which is
  correct, so I standardized ch. 1 and ch. 5 to ch. 3's "Red Redoubt," the
  only one that names an actual place rather than a sap number.
- **`chapters/01.summary.txt`** — replaced the corrupted (leaked-reasoning,
  truncated) summary with a clean one describing what the chapter actually
  contains (see above).

No other canon contradictions, timeline/geography inconsistencies, dropped
plot threads, characterization drift, or POV violations found across
chapters 1–12. The who-knows-what table in canon §6 is being respected
exactly (Ferrick's name stays unspoken to Lloyd/Maria through ch. 9, Maria's
theft and Lloyd's five weeks in Carrowgate land on schedule in ch. 12 and
stay privileged to the right people, nothing about the second arm or Anse
Duley leaks early).

### Change requests

None opened this week. Nothing found rises to an outline amendment — the
issues above are either pipeline bugs (ch. 1), a canon/outline document
contradiction (ch. 3 healing), or in-chapter execution quality (ch. 2's
ability framing, ch. 6's prose), not places where the outline itself needs to
change. `change_requests.md` is unchanged (still no open requests).

### Motif ledger (`novel/motifs.json`)

Mostly current. One real staleness found: the knot-cord / ledger props
(`brass-ferrule-cord`, `knot-cord-hitch`, `oilcloth-ledger`) were logged as
`last_used: 11` but all recur in ch. 12 — including the chapter's closing
line ("I watched the cord go still in her hands, finished for the night,
forty-one knots or none"). That's a second cooldown override back to back
(ch. 11 was already an explicit override of a 4-chapter gap). The reuse is
thematically justified — ch. 12 is literally about counting and tallies, and
the closing line ties the cord directly to the forty-one-crowns reveal — but
it means the prop hasn't actually rested since ch. 9. Updated `last_used` to
12 on all three entries and added notes recommending it hold off until at
least ch. 16 rather than treating ch. 12 as a fresh clock start. The
Stillwell-specific hardware motifs (valve, gauge, gas lamp, steam-room door,
etc.) still show `last_used: 6` — that's correct, not stale; the party left
Stillwell at ch. 6 and those fixtures have had no reason to reappear.

### Prose-habit counts (`novel/voice_ledger.json`)

Counted fresh with shell scripts (sentence-split on terminal punctuation,
word-tokenize, pattern-match with manual filtering of idiomatic false
positives) rather than trusting the numbers already on file, since several of
the pre-ch.-9 baseline figures turned out to be inaccurate.

| Chapter | "the way" simile (true uses only) | "a thing" | 40+-word sentences |
|---|---|---|---|
| 01 | 0 | 0 | 1 |
| 02 | 0 | 0 | 0 |
| 03 | 0 | 0 | 0 |
| 04 | 0 | 1 | 0 |
| 05 | 0 | 0 | 0 |
| 06 | 4 | 0 | 15 |
| 07 | 14 | 6 | 26 |
| 08 | 17 | 7 | 23 |
| 09 | 18 | 2 | 21 |
| 10 | 0 | 0 | 23 |
| 11 | 0 | 0 | 20 |
| 12 | 1 | 0 | 23 |

Two corrections to the numbers already on file:

- **"The way" simile**: the ch. 01–05 baseline and ch. 07/08's prior counts
  included idiomatic, non-simile uses ("all the way," "in the way of," "the
  way back/to") as false positives. Ch. 05's prior count of 1 was *entirely*
  one such false positive. Corrected counts are in `voice_ledger.json`.
- **Long sentences (40+ words)**: the ch. 01–05 baseline (10, 12, 10, 6, 12)
  significantly overstated this. A fresh, scripted recount finds almost none
  in Act I — Edie's chapters are dense but syntactically contained. The habit
  genuinely starts at ch. 06 with the switch to Lloyd's POV (consistent with
  his canon voice, "runs long, then breaks") and has held a stable low-to-
  mid-20s rate ever since rather than still "developing." Ch. 10–12's figures
  were already accurate and are unchanged by this correction.

"A thing" and the aphorism/same-as/clerical-metaphor/negation-doubling/
which-appositive entries already on file checked out as accurate on manual
re-read and are left as-is (one addition: a single early "same as" instance
surfaced in ch. 09, predating the ch. 10 cluster that first got it flagged —
added to that entry's history).

**New prose-quality finding (counts wouldn't have caught this):** chapters
6, 7, and 8 each end their chapter on the same move — an indifferent or
inanimate thing personified as "patient," waiting out time without hurry.
Ch. 6: the guard's shadow "stretching ahead of us like a dark omen." Ch. 7:
the floodwater "patient, working at the dark... given enough time and no one
to tell it to stop." Ch. 8: the water's sweetness "patient, the way a thing
sits when it isn't in any hurry to be noticed." Three chapters running on
the identical closing image, never flagged night-to-night because each
session only sees its own chapter's ending. It stopped on its own at ch.
9–12 (which close on action or dialogue instead), so no text needed fixing,
but I've added it to the ledger's `closers` section as spent, so "patient"
doesn't get reached for again as a chapter-ending word.

### Anything else worth noting

- Chapter 6 is also the weakest-written of the twelve on a pure craft level,
  independent of the tense problem above — several beats are described twice
  per paragraph (once in summary, once in scene), which reads like leftover
  skeleton structure. Mentioned above under "needs your attention"; not
  repeating the fix recommendation twice here, just flagging that it's worth
  reading yourself before deciding whether to let it stand.
- Everything else held up well. Twelve chapters in, the who-knows-what table,
  the ability hard-limits (outside the two ch. 2/ch. 3 items above), Vail's
  writing rules (not yet on-page directly, but Maria's retelling of her in
  ch. 12 keeps clear of every banned staging cue), and the outline's beat-by-
  beat plan are all being followed closely. No dropped plot threads.
