"""The passes.

    skeleton    events only, structured, FROZEN after this point
    action      blocking and spatial logic. Complete, not good.
    character   interiority and dialogue.
    atmosphere  sensory texture.
    unify       rewrites the accumulated material as one continuous piece of
                prose. This is the pass that actually writes the book. It may
                cut freely and may not add events.
    editor      checks against the skeleton and canon. Can reject.

The first three passes are researchers handing notes to the fourth. Only the
unify pass is asked to write well.
"""

import json
import re

from . import state
from .providers import call_model


def _sys(role, canon, act, pov):
    return f"""You are one stage of a multi-stage novel drafting pipeline. You are the {role}.

The book is THE SWEETWATER YEARS: grimdark Victorian fantasy, first person,
past tense. This chapter is in Act {act} and is narrated by {pov} — always
"I", never third person, never any other POV. Never break POV. If {pov} does
not know a thing, the chapter cannot say it. {pov}'s narrative voice (sentence
shape, rhythm, how they handle their own feelings) is specified in canon and
is as binding as anything else here — the prose should read as unmistakably
{pov}'s even without the name attached.

The canon below is binding. Where your instinct and the canon disagree, the
canon is right.

=== CANON ===
{canon}
=== END CANON ===

Output only the requested text. No preamble, no commentary, no headings, no
notes about what you did."""


# ------------------------------------------------------------------ motifs


def _motif_section(n, motifs):
    """Appended to action/character/atmosphere prompts. All three passes
    share one ledger (novel/motifs.json) so none of them repeats a detail
    another already spent, without needing the full previous chapters."""
    return f"""

RECURRING DETAILS ALREADY ESTABLISHED (logged by every descriptive pass —
action, character, atmosphere — across earlier chapters):
{state.motif_brief(n, motifs)}

A cooldown is a nudge, not a rule. If this chapter's skeleton or dialogue
genuinely needs a detail marked ON COOLDOWN — it's the subject of a beat, a
plot point, something a character is actively discussing — use it anyway.
Otherwise reach for something new, or a detail marked free to reuse.

When you finish the chapter, on its own new line write the marker @@MOTIFS@@
followed by a JSON array logging any small, distinctive recurring detail you
introduced or reused this chapter (a scar, a phrase, a signature gesture, a
recurring smell — not generic prose). Format:
[{{"id": "kebab-case-id", "subject": "who or where it belongs to, or \"\"",
"detail": "the detail, a few words", "min_gap": N, "status": "new" or
"reused"}}]
Reuse an existing id exactly when referencing a logged detail. min_gap is how
many chapters should normally pass before it reappears unless the plot needs
it sooner — use 1 for a trait that's simply always true of the character and
will come up often (a fighter's hands, a limp), 4-8 for a distinctive one-off
(a scar, a specific memory, an unusual object). If nothing here is worth
tracking, output an empty array."""


def _log_motifs(raw, role, n, motifs):
    marker = "@@MOTIFS@@"
    if marker not in raw:
        return raw.rstrip()
    draft, _, tail = raw.partition(marker)
    m = re.search(r"\[.*\]", tail, re.DOTALL)
    if m:
        try:
            state.merge_motifs(motifs, role, n, json.loads(m.group(0)))
        except (json.JSONDecodeError, TypeError):
            pass
    return draft.rstrip()


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

THE PREVIOUS CHAPTER ENDED ON: {state.previous_ending(n)}
Your first event should either continue directly from that image (pick it up
a beat later, same scene) or make a deliberate, legible cut away from it (new
scene, new time, new place) — never open as if the previous chapter didn't
just happen. If this is the first chapter of a new Act with a new POV, a
clean cut is expected; make it a considered choice, not a default.

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


def action(roles, n, beats, act, pov, canon, prev, skel, motifs):
    cfg = roles["action"]
    raw = call_model(
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
prose.

This must run at least 2,000 words. If you're unsure whether you've covered
enough, you haven't — render every event as a full beat with real blocking,
not a one-line summary of what happened. A short pass here is a failure no
later pass can recover from.{_motif_section(n, motifs)}""",
        max_tokens=6000,
    )
    return _log_motifs(raw, "action", n, motifs)


# --------------------------------------------------------------- character


def character(roles, n, act, pov, canon, skel, draft, motifs):
    cfg = roles["character"]
    raw = call_model(
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

This is not a polish pass — the action draft is deliberately thin, and most of
this chapter's real weight is supposed to come from here. Extend reactions
into full paragraphs. Let exchanges run as long as the beat supports. Give
{pov} room to actually feel something instead of a single sentence naming
that they felt it. Expect this pass to add substantially to the draft's
length, not just retouch its sentences.

You may not change what happens or the order it happens in — you're filling
the space around the skeleton, not moving through it faster or slower. Return
the full chapter.{_motif_section(n, motifs)}""",
        max_tokens=6000,
    )
    return _log_motifs(raw, "character", n, motifs)


# -------------------------------------------------------------- atmosphere


def atmosphere(roles, n, act, pov, canon, skel, draft, motifs):
    cfg = roles["atmosphere"]
    raw = call_model(
        cfg,
        _sys("atmosphere pass", canon, act, pov),
        f"""Here is a draft with structure and people. Add the world around them.

THE FROZEN EVENT SKELETON — unchanged and unchangeable:
{json.dumps(skel['events'], indent=2)}

DRAFT:
{draft}

Your job: sensory specificity. Light, smell, damp, cold, noise, texture, the
particular grime of this place. Grimdark Victorian: industrial, wet, tired.

Precision, not sparseness, is the skill here. Two precise details beat six
vague ones — but a scene with none is bare, not restrained, and this draft
runs bare more often than it runs overwritten. Do not decorate a scene that's
already doing its job, but ground every scene that isn't yet. Never add a
metaphor that {pov} would not think of.

Do not change what happens. Return the full chapter.{_motif_section(n, motifs)}""",
        max_tokens=6000,
    )
    return _log_motifs(raw, "atmosphere", n, motifs)


# ------------------------------------------------------------------ unify


def unify(roles, n, act, pov, canon, skel, draft):
    """The pass that actually writes the book."""
    cfg = roles["unify"]
    words = len(draft.split())
    floor, ceiling = int(words * 0.75), int(words * 0.85)
    return call_model(
        cfg,
        _sys("final prose pass", canon, act, pov),
        f"""Three separate passes have built this chapter: one laid the events,
one added the people, one added the world. It is complete and it reads like
three people wrote it, because three did.

Rewrite it as one continuous piece of prose by a single author.

THE FROZEN EVENT SKELETON — every event must survive. You may not add events:
{json.dumps(skel['events'], indent=2)}

DRAFT ({words} words):
{draft}

Your mandate:
- One voice throughout. Vary sentence rhythm — the accumulated draft will have
  fallen into a uniform sentence length; break it.
- CUT. Anything doing a job that is already done elsewhere. Any detail added
  for its own sake. Any sentence that restates the previous sentence with
  different words.
- Target length: {floor}-{ceiling} words. That's a real floor, not a
  suggestion of scale — coming in under {floor} words means you cut content,
  not fat, and that's a failure even where the remaining prose reads well.
- End scenes one beat earlier than the draft does.
- Keep every event. Keep the closing image: {skel['ends_on']}

You are the only pass being asked to write well. Return the full chapter.""",
        # Raised from 8000 after unify truncated mid-sentence on a healthy
        # 3413-word input - thinking tokens on this model count against this
        # budget, so headroom matters more here than the word count alone
        # would suggest. providers._gemini also now detects and retries a
        # MAX_TOKENS cutoff, but starting higher means it shouldn't need to.
        max_tokens=12000,
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
8. LENGTH: is the chapter between 1,800 and 3,200 words?
9. MOTIF COOLDOWN: cross-reference RECURRING DETAILS below. Does the chapter
   reuse a detail marked ON COOLDOWN in a way that ISN'T plot-load-bearing —
   not the subject of a beat, not something a character is actively
   discussing, just reached for out of habit? A cooldown detail that's
   genuinely doing work this chapter is not a failure; one that's decorative
   repetition is."""


def editor(roles, n, act, pov, canon, skel, draft, prev, motif_brief):
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

RECURRING DETAILS (as logged before this chapter ran — action, character and
atmosphere may have used some of these while drafting):
{motif_brief}

FROZEN SKELETON:
{json.dumps(skel, indent=2)}

CHAPTER:
{draft}

{EDITOR_CHECKS}

Output JSON only:
{{
  "verdict": "PASS" or "REVISE",
  "failures": [
    {{"check": 1-9, "problem": "what is wrong", "where": "the offending line or passage", "fix": "what to do instead"}}
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
    # Caught live: handed a too-short chapter and a check-8 "expand" failure,
    # this pass shrank it further two rounds running (859 -> ~330 words)
    # instead of growing it - "fix only what's named, don't touch the rest"
    # reads to the model as license to trim rather than add. Spell out the
    # expand case explicitly so cutting isn't the safe-looking move.
    expand = next(
        (f for f in verdict["failures"]
         if f.get("check") == 8 and "expand" in f.get("fix", "").lower()),
        None,
    )
    expansion_note = ""
    if expand:
        expansion_note = f"""

This chapter is {len(draft.split())} words and must reach at least 1,800. The
fix is to ADD - more interiority, more dialogue, more sensory detail, beats
played out in full rather than summarized. Do not cut, condense or tighten
anything to compensate; a chapter that comes out of this pass shorter than it
went in is a failure regardless of anything else it gets right. Add to the
scenes and beats already in the frozen skeleton below - do not introduce a
new scene, encounter or character to pad the length. Where an event feels
rushed, that is exactly where to slow down and add page."""
    return call_model(
        cfg,
        _sys("revision pass", canon, act, pov),
        f"""The editor has rejected this chapter. Fix ONLY the listed failures.
Everything not named below stays exactly as it is — do not take the
opportunity to rewrite anything else.{expansion_note}

FAILURES:
{json.dumps(verdict['failures'], indent=2)}

FROZEN SKELETON — every one of these events must still be clearly present in
your output; do not drop, merge, replace or add to them:
{json.dumps(skel['events'], indent=2)}

CHAPTER:
{draft}

Return the full corrected chapter.""",
        max_tokens=12000,  # see unify() - same truncation risk, same headroom
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
