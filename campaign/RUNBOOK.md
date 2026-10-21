# RUNBOOK — scheduled sessions

Read this first. It tells a scheduled session what to do. It overrides the
older novel-drafting instructions. **The novel is finished; do not draft
chapters.** Work autonomously; no one is watching. Jake can edit this file to
change what future sessions do.

## Setup

1. Clone/register the repo as your task prompt says.
2. Read `campaign/STATUS.md` (the work queue) and `campaign/PLAN.md`.
3. Read `campaign/DECISIONS.md` so you honour what is already decided.
4. `git pull --rebase` before you start and again before you push. If a push
   is rejected, rebase and retry once; never force-push.
5. Tag pushes return 403 in this repo. Skip tags. Commit history is the
   rollback.

## Pick the work

- Take the **first row in STATUS.md with status `todo`** whose dependencies
  are all `done`. Set it `in-progress` in the same commit you finish it in
  (do not push a half-state).
- If every runnable row is blocked, write why in `campaign/DECISIONS.md`
  under "Blocked", and stop. Do not guess your way around a missing input.
- If nothing is left, do nothing and say so.

Slot differences:
- **Weeknight** (Mon–Fri, midnight and noon Perth): take the next item.
- **Saturday**: do the **QA pass first** (below), then take the next item if
  you have room.
- **Sunday**: take the next item, preferring items marked `creative` (set
  pieces, bosses, NPC voice). Skip to the next runnable if none.

## Phase 1: read-through (rows P1.1–P1.6)

Goal: a full, attentive read of the finished book, to judge it and to mine it
for the campaign.

Batch rows (P1.1–P1.5): read every chapter in the batch **in full**, plus
`novel/canon.md`. For P1.2–P1.5 also read the previous batch's notes. Write
`novel/readthrough/batch-N.md` with, per chapter:

1. **What happens** (3 lines).
2. **Craft verdict**: strong / fine / weak, with one or two specific lines or
   passages quoted as evidence. Name sentence-shape sameness, repeated
   closers, tics. Read for quality, not only counts.
3. **Continuity flags** against canon.md and earlier chapters.

Then, once for the batch:

4. **Lore ledger**: every named place, organisation, person, object, rule and
   number the book established or implied, one line each, with the chapter.
5. **Open threads**: questions the book raised and left, things the ending
   leaves unresolved, anything an RPG could pick up.
6. **Small fixes**: name slips, one-line contradictions: fix directly in the
   chapter file. Anything structural: list it, do not rewrite it.

Do not rewrite chapters in this phase.

P1.6 synthesis, after all five batches, write three files:
- `novel/readthrough/SYNTHESIS.md`: honest book-level verdict, ranked list of
  the real problems (e.g. long-sentence rate since ch. 6, ch. 6 craft), and
  which chapters, if any, deserve a hand revision. Short. No flattery.
- `campaign/source-bible.md`: the consolidated lore ledger, organised by
  place / faction / person / object / rule. This is what every campaign file
  cites.
- `campaign/hooks.md`: the open threads ranked by campaign usefulness, each
  with a one-line "what the table could do with this".

Mark P1.6 `done`, then continue to Phase 2 next session.

## Phase 2: campaign components

For a campaign row: read `PLAN.md` (template and conventions), `source-bible.md`,
`hooks.md`, every file the row depends on, and `novel/canon.md` sections 4–9.
Read `campaign/system/` if it has files; it is the binding ruleset. Then write
the file `campaign/<ID>-<slug>.md` to the target size and definition of done:

- Follows the template/conventions in PLAN.md.
- Consistent with canon.md, the chapter-25 ending state, and earlier campaign
  files.
- Table-time voice. No design rationale in the file.
- Nothing that needs a ruleset number is invented; mark `(SYS?)` instead.

Decisions that are Jake's to make (tone merges, who survives, big reveals):
pick the most defensible default, write it into the file, and add a line to
`campaign/DECISIONS.md` under "Defaults chosen" so he can overturn it. Do not
stop for them.

Also update `campaign/STATUS.md`: set the row `done`, add the date and a
one-line note of what exists and what is thin.

## Saturday QA pass

Read every file added or changed since the last QA. Check against canon.md,
the ruleset (if present), and each other. Fix small contradictions directly.
Log larger ones in `campaign/DECISIONS.md` under "Review findings". Write a
**Digest** at the top of STATUS.md (5 lines max: what exists, what is next,
anything Jake must decide, anything blocked). Replace the previous digest.

## Commit

Commit the files you touched with a message saying which row and what changed.
Push to main. If you had to skip something, say so in the commit message.
