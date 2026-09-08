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
- **Change budgets.** Later passes are capped on how much they may alter
  (`passes.BUDGET`), because models never no-op: tell one to improve
  atmosphere and it will add atmosphere whether or not the scene needed any.
  Over budget retries once, then keeps the earlier pass.
- **The editor has fail conditions, not taste.** Ask a model if a chapter is
  good and it says yes. Ask whether every skeleton event occurs, whether the
  POV knows what it narrates, whether Lloyd's Insight got resolved — and you
  get real rejections.
- **Every pass writes to disk immediately.** A rate limit costs one pass, not
  the chapter. Run the same command again.

## Going live

Copy `roles.example.json` over `roles.json` and set the API keys in the
environment. Two rules:

- **Put your best model on `unify`.** It does the writing that matters.
- **The editor must be a different model from unify**, or it approves its own
  work.

Roles are mapped to providers individually, so you can split across free tiers
(Gemini, Groq, Mistral, OpenRouter) without any other file knowing.

## Layout

    novel/outline.md           25 chapters of beats. Frozen.
    novel/canon.md             Characters, abilities, world, who-knows-what.
    novel/change_requests.md   Proposed outline amendments, pending approval.
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

## Known gaps

- Ch. 16 (Lloyd delirious, deliberately unreliable) is the chapter most likely
  to come out as mush. Candidate for writing by hand.
- `novel/change_requests.md` has no open requests right now — check it before
  drafting Act II in case that's changed.
