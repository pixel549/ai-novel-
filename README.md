# ai-novel

A pipeline that drafts a novel one chapter per run, using several models with
different jobs and an editor that can reject.

The premise: long-form AI fiction fails because each chapter is generated from
the previous chapter, so it drifts. Here the outline is written first and
frozen, and the drafter never continues from prose — it is handed one chapter's
beats and told to hit them. Coherence is enforced by the pipeline rather than
remembered by the models.

## Run it

    python run_chapter.py 1

Stdlib only, no dependencies. Out of the box every role is on the `stub`
provider — no API calls, canned text. Debug the harness for free, then swap in
real models.

    python run_chapter.py 3 --force          rerun passes already on disk
    python run_chapter.py 3 --stop skeleton  stop after one pass

## The passes

| pass | job |
|---|---|
| **skeleton** | Turns the chapter's beats into a structured event list. **Frozen** — every later pass is checked against it. |
| **action** | Blocking, movement, spatial logic. Complete, not good. |
| **character** | Interiority and dialogue. Bounded edit. |
| **atmosphere** | Sensory texture. Bounded edit. |
| **unify** | Rewrites the accumulated material as one continuous piece of prose. Cuts hard. **This is the pass that writes the book.** |
| **editor** | Eight checks against the skeleton and canon. Can reject, up to three times. |
| **summariser** | Four sentences. All that later chapters ever see of this one. |

The first three passes are researchers handing notes to the fourth. Only unify
is asked to write well — prose quality is cross-cutting and doesn't live in any
of the content dimensions.

## Why it holds together

- **The outline is locked.** Amendments go through `novel/change_requests.md`
  and need approval. The drafter cannot invent plot.
- **Context stays flat.** A chapter sees its own beats, the canon, and
  summaries — never text — of the last three chapters. Chapter 25 costs the
  same as chapter 2.
- **The editor has fail conditions, not taste.** Ask a model if a chapter is
  good and it says yes. Ask whether every skeleton event occurs, whether the
  POV knows what it narrates, whether Lloyd's Insight got resolved — and you
  get real rejections.
- **Every pass writes to disk immediately.** A rate limit costs one pass, not
  the chapter. Run the same command again.
- **Motifs are logged, not remembered.** `action`, `character` and
  `atmosphere` share one ledger (`novel/motifs.json`) of small recurring
  details — a scar, a gesture, a smell — each with a suggested cooldown
  before it should reappear. It's a nudge: the skeleton can always override
  it when a detail is genuinely load-bearing this chapter. This is how a
  character's bright blue eyes don't get mentioned every single chapter
  without the pipeline having to re-read any previous chapter's prose.

## Going live

Copy `roles.example.json` over `roles.json` and set the API keys in the
environment. Two rules:

- **Put your best model on `unify`.** It does the writing that matters.
- **The editor must be a different model from unify**, or it approves its own
  work.

Roles are mapped to providers individually, so you can split across free tiers
(Gemini, Groq, Mistral, Cerebras) without any other file knowing.

## Layout

    novel/outline.md           25 chapters of beats. Frozen.
    novel/canon.md             Characters, abilities, world, who-knows-what.
    novel/change_requests.md   Proposed outline amendments, pending approval.
    novel/motifs.json          Recurring detail ledger, shared by action/character/atmosphere.
    roles.json                 Which model does which job.
    chapters/NN.md             Finished chapters.
    chapters/NN.summary.txt    What later chapters see.
    workspace/NN/              Every intermediate pass, plus editor.log.

**Keep `workspace/`.** When a chapter comes out badly you need to see whether
atmosphere drowned it or unify flattened it, and you can't diagnose that from
the finished text. `editor.log` — the rejection history — is frankly the most
interesting output in the repo.

## Scheduling

`.github/workflows/draft.yml` runs one chapter a day and commits the result.
Get three chapters working locally first; debugging this through Actions logs
is miserable.

## Status

The book is complete: 25/25 chapters drafted, roughly 59,500 words. There is
no more nightly drafting left to do and `novel/change_requests.md` has no
open requests. What's left is upkeep: a Saturday consistency-review session
rereads the whole book against `novel/canon.md` and `novel/outline.md` and
logs findings to `novel/review-log.md` (read that file for anything open),
and a weekly creative session either revises a chapter, expands
`novel/canon.md` / `novel/motifs.json`, or — no longer applicable now that
every chapter is drafted — fleshes out thin outline beats, logging what it
picked and why at the bottom of `novel/outline.md`.

Ch. 16 (Lloyd delirious, deliberately unreliable) was the chapter this README
used to flag as most likely to come out as mush. It didn't: see the
2026-10-03 entry at the bottom of `novel/outline.md` and the 2026-10-16 entry
in `novel/review-log.md`, both of which checked it against the finished text
and found it concrete and well-built. No chapter is currently flagged as a
hand-revision candidate.
