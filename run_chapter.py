#!/usr/bin/env python3
"""Draft one chapter.

    python run_chapter.py 1
    python run_chapter.py 1 --force        rerun passes already on disk
    python run_chapter.py 1 --stop unify   stop after a given pass

Every pass is written to workspace/NN/ the moment it finishes. A rate limit
costs you one pass, not the chapter — run the same command again.
"""

import argparse
import difflib
import json
import sys

from pipeline import passes, state

ORDER = ["action", "character", "atmosphere", "unify"]
MAX_REVISIONS = 3


def drift(a, b):
    return 1.0 - difflib.SequenceMatcher(None, a, b).ratio()


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
        elif name == "character":
            new = passes.character(roles, n, act, pov, canon, skel, draft, motifs)
        elif name == "atmosphere":
            new = passes.atmosphere(roles, n, act, pov, canon, skel, draft, motifs)
        else:
            new = passes.unify(roles, n, act, pov, canon, skel, draft)

        # Change budget: stop a later pass quietly undoing an earlier one.
        if draft and name in passes.BUDGET:
            d = drift(draft, new)
            print(f"             drift {d:.0%} (budget {passes.BUDGET[name]:.0%})")
            if d > passes.BUDGET[name]:
                print(f"             OVER BUDGET — retrying once, tighter")
                new = passes.character(roles, n, act, pov, canon, skel, draft, motifs) \
                    if name == "character" else \
                    passes.atmosphere(roles, n, act, pov, canon, skel, draft, motifs)
                d = drift(draft, new)
                print(f"             drift {d:.0%}")
                if d > passes.BUDGET[name]:
                    print(f"             STILL OVER — keeping previous pass")
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
        state.log_editor(n, attempt, verdict)
        print(f"           {verdict['verdict']}: {len(verdict.get('failures', []))} failures")
        for f in verdict.get("failures", []):
            print(f"           - check {f.get('check')}: {f.get('problem','')[:90]}")

        if verdict["verdict"] == "PASS":
            break
        if attempt == MAX_REVISIONS:
            print("           MAX REVISIONS — shipping flagged")
            state.save_pass(n, "FLAGGED", json.dumps(verdict, indent=2))
            break

        draft = passes.revise(roles, n, act, pov, canon, skel, draft, verdict)
        state.save_pass(n, f"revision_{attempt}", draft)

    # ---- ship -----------------------------------------------------------
    state.save_chapter(n, beats["title"], draft)
    summary = passes.summarise(roles, n, canon, draft)
    state.save_summary(n, summary)

    print(f"\n  chapters/{n:02d}.md — {len(draft.split())} words")
    print(f"  summary: {summary.strip()[:160]}\n")


if __name__ == "__main__":
    sys.exit(main())
