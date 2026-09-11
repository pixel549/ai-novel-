#!/usr/bin/env python3
"""Test one pass against an already-checkpointed draft, with no pipeline run.

    python test_pass.py 2 unify        rerun unify on workspace/02/atmosphere.txt
    python test_pass.py 2 character    rerun character on workspace/02/action.txt
    python test_pass.py 2 action       rerun action from the chapter's beats

Reads the same files run_chapter.py checkpoints and calls that one pass
function directly. Prints the result to stdout and its word count to
stderr. Nothing is saved to workspace/ or chapters/ - this is for iterating
on a prompt or a provider fix against a known-good upstream draft without
paying for the whole pipeline (skeleton through editor/revise) on every
attempt.
"""

import json
import sys

from pipeline import passes, state

UPSTREAM = {"character": "action", "atmosphere": "character", "unify": "atmosphere"}


def main():
    if len(sys.argv) != 3 or sys.argv[2] not in ("action", "character", "atmosphere", "unify"):
        sys.exit(f"usage: {sys.argv[0]} <chapter> <action|character|atmosphere|unify>")
    n, name = int(sys.argv[1]), sys.argv[2]

    roles = state.load_roles()
    canon = state.canon()
    act, pov = state.act_of(n)
    skel = json.loads(state.load_pass(n, "skeleton"))
    motifs = state.load_motifs()

    if name == "action":
        beats = state.chapter_beats(n)
        prev = state.last_chapters(n)
        result = passes.action(roles, n, beats, act, pov, canon, prev, skel, motifs)
    else:
        draft = state.load_pass(n, UPSTREAM[name])
        if name == "character":
            result = passes.character(roles, n, act, pov, canon, skel, draft, motifs)
        elif name == "atmosphere":
            result = passes.atmosphere(roles, n, act, pov, canon, skel, draft, motifs)
        else:
            result = passes.unify(roles, n, act, pov, canon, skel, draft)

    print(result)
    print(f"\n--- {len(result.split())} words ---", file=sys.stderr)


if __name__ == "__main__":
    main()
