"""The passes.

    skeleton    events only, structured, FROZEN after this point
    action      blocking and spatial logic. Complete, not good.
    character   interiority and dialogue. Bounded edit.
    atmosphere  sensory texture. Bounded edit.
    unify       rewrites the accumulated material as one continuous piece of
                prose. This is the pass that actually writes the book. It may
                cut freely and may not add events.
    editor      checks against the skeleton and canon. Can reject.

The first three passes are researchers handing notes to the fourth. Only the
unify pass is asked to write well.
"""

import difflib
import json
import re

from . import state
from .providers import call_model

# Change budgets. Without these a later pass quietly undoes an earlier one.
BUDGET = {"character": 0.45, "atmosphere": 0.35}


def _sys(role, canon, act, pov):
    return f"""You are one stage of a multi-stage novel drafting pipeline. You are the {role}.

The book is THE SWEETWATER YEARS: grimdark Victorian fantasy, third person
limited, past tense. This chapter is in Act {act} and the point of view
character is {pov}. Never break POV. If {pov} does not know a thing, the
chapter cannot say it.

The canon below is binding. Where your instinct and the canon disagree, the
canon is right.

=== CANON ===
{canon}
=== END CANON ===

Output only the requested text. No preamble, no commentary, no headings, no
notes about what you did."""


def _drift(a, b):
    return 1.0 - difflib.SequenceMatcher(None, a, b).ratio()


# ---------------------------------------------------------------- skeleton


def skeleton(roles, n, beats, act, pov, canon, prev):
    cfg = roles["skeleton"]
    raw = call_model(
        cfg,
        _sys("event architect", canon, act, pov)
        + "\n\nYou output JSON only. No prose.",
        f"""Chapter {n}: {beats['title']}

WHAT HAPPENED IN THE LAST FEW CHAPTERS:
{prev}

THIS CHAPTER'S BEATS (from the locked outline — you may not add, remove or
reorder anything):
{beats['beats']}

Produce the event skeleton as JSON:
{{
  "pov": "{pov}",
  "events": [{{"n": 1, "event": "one sentence, physical, what actually happens"}}],
  "learned": ["facts a character knows at the end of this chapter that they did not know at the start"],
  "ends_on": "the closing image or line, one sentence"
}}

Between 6 and 14 events. Events are things that happen, not feelings, themes
or descriptions. This skeleton is frozen: every later pass is checked against
it, so put nothing in it that the beats do not support.""",
        max_tokens=2000,
    )
    m = re.search(r"\{.*\}", raw, re.DOTALL)
    if not m:
        raise SystemExit(f"skeleton pass returned no JSON:\n{raw[:400]}")
    return json.loads(m.group(0))


# ------------------------------------------------------------------ action


def action(roles, n, beats, act, pov, canon, prev, skel):
    cfg = roles["action"]
    return call_model(
        cfg,
        _sys("action and spatial logic pass", canon, act, pov),
        f"""Chapter {n}: {beats['title']}

RECENT CHAPTERS:
{prev}

THE FROZEN EVENT SKELETON — hit every one of these, in this order:
{json.dumps(skel['events'], indent=2)}

Ends on: {skel['ends_on']}

Write the chapter as continuous prose covering every event. Your job is
COMPLETENESS AND PHYSICAL COHERENCE, not quality. Specifically:

- Who is where, in what order, at what distance from what.
- Movement that a reader could draw. Doors, stairs, light, ground, weather.
- Action and violence that obeys physics and the ability limits in canon.
- Dialogue only where the plot requires words to be said. Keep it plain.

Do NOT reach for style. Do NOT add interiority, metaphor or sensory texture —
later passes add those and will fight you for the space. Plain declarative
prose. Around 2,000 words.""",
        max_tokens=6000,
    )


# --------------------------------------------------------------- character


def character(roles, n, act, pov, canon, skel, draft):
    cfg = roles["character"]
    out = call_model(
        cfg,
        _sys("character and dialogue pass", canon, act, pov),
        f"""Here is a structurally complete but flat draft. Add the people to it.

THE FROZEN EVENT SKELETON — you may not change, add, remove or reorder any of
these events. If your revision alters what happens, it is wrong:
{json.dumps(skel['events'], indent=2)}

DRAFT:
{draft}

Your job:
- {pov}'s interiority, in {pov}'s idiom as specified in canon. Never analytical
  about their own psychology.
- Dialogue that sounds like the specific people in canon, not like everyone.
- Reaction, hesitation, what someone does with their hands.
- Cut any line where a character explains their own arc.

Rewrite sentences. Do not rewrite the story. Return the full chapter.""",
        max_tokens=6000,
    )
    return out


# -------------------------------------------------------------- atmosphere


def atmosphere(roles, n, act, pov, canon, skel, draft):
    cfg = roles["atmosphere"]
    return call_model(
        cfg,
        _sys("atmosphere pass", canon, act, pov),
        f"""Here is a draft with structure and people. Add the world around them.

THE FROZEN EVENT SKELETON — unchanged and unchangeable:
{json.dumps(skel['events'], indent=2)}

DRAFT:
{draft}

Your job: sensory specificity. Light, smell, damp, cold, noise, texture, the
particular grime of this place. Grimdark Victorian: industrial, wet, tired.

Restraint is the whole skill here. Add texture where a scene is bare. Do not
decorate scenes that are already working, and do not put weather in every
paragraph. Two precise details beat six vague ones. Never add a metaphor that
{pov} would not think of.

Rewrite sentences. Do not rewrite the story. Return the full chapter.""",
        max_tokens=6000,
    )


# ------------------------------------------------------------------ unify


def unify(roles, n, act, pov, canon, skel, draft):
    """The pass that actually writes the book."""
    cfg = roles["unify"]
    return call_model(
        cfg,
        _sys("final prose pass", canon, act, pov),
        f"""Three separate passes have built this chapter: one laid the events,
one added the people, one added the world. It is complete and it reads like
three people wrote it, because three did.

Rewrite it as one continuous piece of prose by a single author.

THE FROZEN EVENT SKELETON — every event must survive. You may not add events:
{json.dumps(skel['events'], indent=2)}

DRAFT:
{draft}

Your mandate:
- One voice throughout. Vary sentence rhythm — the accumulated draft will have
  fallen into a uniform sentence length; break it.
- CUT. Anything doing a job that is already done elsewhere. Any detail added
  for its own sake. Any sentence that restates the previous sentence with
  different words. Expect to remove 15-25% of the words.
- End scenes one beat earlier than the draft does.
- Keep every event. Keep the closing image: {skel['ends_on']}

You are the only pass being asked to write well. Return the full chapter.""",
        max_tokens=8000,
    )


# ----------------------------------------------------------------- editor


EDITOR_CHECKS = """Answer each check with a pass or a failure. A failure needs
the specific line or passage at fault.

1. STRUCTURE: does every event in the frozen skeleton occur, in order?
2. ADDITIONS: does the chapter contain a significant event NOT in the skeleton?
3. POV: is anything narrated that the POV character cannot see, hear or know?
4. CANON: does anything contradict the canon file — a fact, a relationship,
   a timeline, an ability used beyond its stated limits?
5. INSIGHT AMBIGUITY: does the chapter confirm or deny whether Lloyd's
   perceptions are real? It must do neither. Both readings must survive.
6. CHARACTER: does anyone act against their canon behavioural rules? Check
   Vail's rules especially — no ominous staging, no menace in her delivery,
   no cold eyes, no pauses before answering.
7. SELF-ANALYSIS: does any character name their own arc, growth or psychology
   aloud?
8. LENGTH: is the chapter between 1,800 and 3,200 words?"""


def editor(roles, n, act, pov, canon, skel, draft, prev):
    cfg = roles["editor"]
    raw = call_model(
        cfg,
        _sys("editor", canon, act, pov)
        + "\n\nYou are a checker, not a writer. You output JSON only. Your job "
        "is to find failures, not to praise. A chapter with no failures is "
        "unusual and you should be confident before saying so.",
        f"""Chapter {n}.

RECENT CHAPTERS:
{prev}

FROZEN SKELETON:
{json.dumps(skel, indent=2)}

CHAPTER:
{draft}

{EDITOR_CHECKS}

Output JSON only:
{{
  "verdict": "PASS" or "REVISE",
  "failures": [
    {{"check": 1-8, "problem": "what is wrong", "where": "the offending line or passage", "fix": "what to do instead"}}
  ],
  "notes": "one sentence"
}}""",
        max_tokens=3000,
    )
    m = re.search(r"\{.*\}", raw, re.DOTALL)
    if not m:
        return {"verdict": "PASS", "failures": [], "notes": "editor returned no JSON"}
    try:
        return json.loads(m.group(0))
    except json.JSONDecodeError:
        return {"verdict": "PASS", "failures": [], "notes": "editor JSON malformed"}


def revise(roles, n, act, pov, canon, skel, draft, verdict):
    cfg = roles["unify"]
    return call_model(
        cfg,
        _sys("revision pass", canon, act, pov),
        f"""The editor has rejected this chapter. Fix ONLY the listed failures.
Everything not named below stays exactly as it is — do not take the
opportunity to rewrite anything else.

FAILURES:
{json.dumps(verdict['failures'], indent=2)}

FROZEN SKELETON:
{json.dumps(skel['events'], indent=2)}

CHAPTER:
{draft}

Return the full corrected chapter.""",
        max_tokens=8000,
    )


# --------------------------------------------------------------- summariser


def summarise(roles, n, canon, draft):
    cfg = roles["summariser"]
    return call_model(
        cfg,
        "You summarise novel chapters for a drafting pipeline. Plain, factual, "
        "no style. Output the summary only.",
        f"""Summarise this chapter in four sentences or fewer. Cover only: what
happened, what changed between characters, and what anyone learned. This
summary is all that later chapters will see of this one, so omit nothing
load-bearing and include no atmosphere.

{draft}""",
        max_tokens=500,
    )
