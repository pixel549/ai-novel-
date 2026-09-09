#!/usr/bin/env python3
"""Draft one chapter.

    python run_chapter.py 1
    python run_chapter.py 1 --force        rerun passes already on disk
    python run_chapter.py 1 --stop unify   stop after a given pass

Every pass is written to workspace/NN/ the moment it finishes. A rate limit
costs you one pass, not the chapter — run the same command again.
"""

import argparse
import json
import sys

from pipeline import passes, state

ORDER = ["action", "character", "atmosphere", "unify"]
MAX_REVISIONS = 3
MIN_LENGTH, MAX_LENGTH = 1800, 3200

# character and atmosphere are bounded edits that add to the draft - they
# should never shrink it drastically. This catches content loss (a pass
# gutting the draft instead of layering onto it) without the false positives
# the old text-similarity BUDGET check produced on legitimate first-person
# rewrites, which touch almost every sentence by nature.
MIN_RETENTION = {"character": 0.85, "atmosphere": 0.85}

# action has no previous draft to compare against - it's the first pass - so
# it needs an absolute floor instead of a retention ratio. Caught live: action
# wrote 190 words for a 12-event chapter, which no later pass could recover
# from (character/atmosphere only add to what's there; unify only cuts).
MIN_ACTION_WORDS = 1200


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("chapter", type=int)
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--stop", choices=ORDER + ["skeleton"])
    args = ap.parse_args()

    n = args.chapter
    roles = state.load_roles()
    canon = state.canon()
    beats = state.chapter_beats(n)
    act, pov = state.act_of(n)
    prev = state.last_chapters(n)
    motifs = state.load_motifs()
    motif_snapshot = state.motif_brief(n, motifs)

    print(f"\n=== Chapter {n}: {beats['title']} (Act {act}, POV {pov}) ===")

    # ---- skeleton -------------------------------------------------------
    if state.pass_done(n, "skeleton") and not args.force:
        skel = json.loads(state.load_pass(n, "skeleton"))
        print("  [skeleton] loaded")
    else:
        print("  [skeleton] running")
        skel = passes.skeleton(roles, n, beats, act, pov, canon, prev)
        state.save_pass(n, "skeleton", json.dumps(skel, indent=2))
    state.save_ends_on(n, skel["ends_on"])
    print(f"             {len(skel['events'])} events")
    if args.stop == "skeleton":
        return

    # ---- prose passes ---------------------------------------------------
    draft = None
    for name in ORDER:
        if state.pass_done(n, name) and not args.force:
            draft = state.load_pass(n, name)
            print(f"  [{name}] loaded ({len(draft.split())} words)")
            if args.stop == name:
                return
            continue

        print(f"  [{name}] running")
        if name == "action":
            new = passes.action(roles, n, beats, act, pov, canon, prev, skel, motifs)
            if len(new.split()) < MIN_ACTION_WORDS:
                print(f"             {len(new.split())} words — under floor, retrying once")
                new = passes.action(roles, n, beats, act, pov, canon, prev, skel, motifs)
        elif name == "character":
            new = passes.character(roles, n, act, pov, canon, skel, draft, motifs)
        elif name == "atmosphere":
            new = passes.atmosphere(roles, n, act, pov, canon, skel, draft, motifs)
        else:
            new = passes.unify(roles, n, act, pov, canon, skel, draft)

        if draft and name in MIN_RETENTION:
            old_words, new_words = len(draft.split()), len(new.split())
            if new_words < MIN_RETENTION[name] * old_words:
                print(f"             cut {old_words}->{new_words} words "
                      f"({new_words / old_words:.0%}) — discarding, keeping previous pass")
                new = draft

        draft = new
        state.save_pass(n, name, draft)
        print(f"             {len(draft.split())} words")
        if args.stop == name:
            return

    # ---- editor ---------------------------------------------------------
    for attempt in range(1, MAX_REVISIONS + 1):
        print(f"  [editor] attempt {attempt}")
        verdict = passes.editor(roles, n, act, pov, canon, skel, draft, prev, motif_snapshot)

        # The editor LLM is unreliable at actually counting words - verified
        # live (it passed a 393-word chapter against an 1800-3200 requirement).
        # Word count is cheap to check in code, so don't trust the model's
        # self-report for it.
        word_count = len(draft.split())
        if verdict["verdict"] == "PASS" and not (MIN_LENGTH <= word_count <= MAX_LENGTH):
            verdict = {
                "verdict": "REVISE",
                "failures": [{
                    "check": 8,
                    "problem": f"Chapter is {word_count} words, outside the required "
                               f"{MIN_LENGTH}-{MAX_LENGTH} range.",
                    "where": "(whole chapter)",
                    "fix": f"{'Expand' if word_count < MIN_LENGTH else 'Trim'} to land "
                           f"within {MIN_LENGTH}-{MAX_LENGTH} words.",
                }],
                "notes": "length override — code-checked, not the editor's own count",
            }

        state.log_editor(n, attempt, verdict)
        print(f"           {verdict['verdict']}: {len(verdict.get('failures', []))} failures")
        for f in verdict.get("failures", []):
            print(f"           - check {f.get('check')}: {f.get('problem','')[:90]}")

        if verdict["verdict"] == "PASS":
            break
        if attempt == MAX_REVISIONS:
            # Don't ship this as if it were finished - a chapter still
            # failing after MAX_REVISIONS attempts (caught live: the revise
            # loop oscillated 259->1285->268 words, regressing rather than
            # converging) is a real failure, not a "close enough, flag it."
            # Shipping it would let the next run move on to the chapter
            # after this one, permanently leaving broken prose behind.
            # Clear this chapter's passes so the next attempt regenerates
            # from action instead of reloading the same bad drafts, and
            # exit nonzero so the workflow shows red instead of a
            # deceptive green checkmark.
            print("           MAX REVISIONS — discarding, not shipping")
            state.save_pass(n, "FLAGGED", json.dumps(verdict, indent=2))
            for name in ORDER:
                state.clear_pass(n, name)
            for i in range(1, MAX_REVISIONS):
                state.clear_pass(n, f"revision_{i}")
            return 1

        draft = passes.revise(roles, n, act, pov, canon, skel, draft, verdict)
        state.save_pass(n, f"revision_{attempt}", draft)

    # ---- ship -----------------------------------------------------------
    state.clear_pass(n, "FLAGGED")  # stale from an earlier failed attempt, if any
    state.save_chapter(n, beats["title"], draft)
    summary = passes.summarise(roles, n, canon, draft)
    state.save_summary(n, summary)

    print(f"\n  chapters/{n:02d}.md — {len(draft.split())} words")
    print(f"  summary: {summary.strip()[:160]}\n")


if __name__ == "__main__":
    sys.exit(main())
