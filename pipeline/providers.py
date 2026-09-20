"""Single entry point for all model calls.

Roles map to providers in roles.json, so the unify pass can sit on your best
model and the mechanical passes on whatever free tier is going, without any
other file knowing about it.
"""

import json
import os
import time
import urllib.error
import urllib.request


class ModelError(Exception):
    pass


def call_model(role_cfg, system, user, max_tokens=4000):
    """role_cfg is normally one {provider, model, ...} dict. It can also be a
    LIST of them - a fallback chain, tried in preference order. Each
    candidate already retries internally (_gemini/_openai_compatible only
    raise ModelError once their own retry budget is exhausted), so falling
    back here means "this whole provider is down right now," not "one
    request failed." Added after three straight days where a single
    provider (gemini-3.6-flash, under sustained demand) had no fallback at
    all - once its own retries ran out, the entire chapter failed outright.
    A plain dict behaves exactly as before (a one-candidate chain)."""
    chain = role_cfg if isinstance(role_cfg, list) else [role_cfg]
    for i, cfg in enumerate(chain):
        try:
            return _dispatch(cfg, system, user, max_tokens)
        except ModelError as e:
            if i == len(chain) - 1:
                raise
            next_cfg = chain[i + 1]
            print(f"             ({cfg.get('provider')}/{cfg.get('model')} exhausted its "
                  f"retries ({e}) - falling back to "
                  f"{next_cfg.get('provider')}/{next_cfg.get('model')})")


def _dispatch(cfg, system, user, max_tokens):
    provider = cfg.get("provider", "stub")
    if provider == "stub":
        return _stub(cfg)
    if provider == "gemini":
        return _gemini(system, user, cfg.get("model", "gemini-2.0-flash"), max_tokens)
    if provider == "openai_compatible":
        return _openai_compatible(cfg, system, user, max_tokens)
    raise ModelError(f"unknown provider: {provider}")


# --------------------------------------------------------------------------
# stub — no network. Shakes out the pipeline for free before you spend quota.
# --------------------------------------------------------------------------

_LOREM = (
    "The corridor smelled of salt and old iron. She counted the doors as she "
    "passed them, because counting was the only thing down here that stayed the "
    "same twice. Lloyd stopped at the fourth one and put his hand flat against "
    "it and did not say what he was looking at. Behind them the water moved "
    "without anything moving it. "
)


def _stub(role_cfg):
    role = role_cfg.get("role", "?")
    if role == "skeleton":
        return json.dumps(
            {
                "pov": "stub",
                "events": [
                    {"n": 1, "event": "stub event one"},
                    {"n": 2, "event": "stub event two"},
                    {"n": 3, "event": "stub event three"},
                ],
                "learned": [],
                "ends_on": "stub closing image",
            }
        )
    if role == "editor":
        return json.dumps({"verdict": "PASS", "failures": [], "notes": "stub editor"})
    if role == "summariser":
        return "Stub three-sentence summary of the chapter."
    return (_LOREM * 12).strip()


# --------------------------------------------------------------------------
# gemini
# --------------------------------------------------------------------------


def _gemini(system, user, model, max_tokens, error_retries=9, truncation_retries=3):
    key = os.environ.get("GEMINI_API_KEY")
    if not key:
        raise ModelError("GEMINI_API_KEY not set")

    url = (
        f"https://generativelanguage.googleapis.com/v1beta/models/"
        f"{model}:generateContent?key={key}"
    )

    # Two independent retry budgets, not one shared counter. They used to be
    # the same loop counter, which meant a call that truncated (below) burned
    # through the same attempts reserved for genuine transient errors - caught
    # live when action needed 3 truncation-retries to land a usable draft,
    # leaving character's own call almost no room before a real Gemini 503
    # ("high demand") exhausted what was left and crashed the run. Truncation
    # and transient errors are unrelated failure modes and now each get their
    # own full allowance.
    #
    # error_retries raised 6 -> 9 (30s/60s/.../270s, ~22.5 min total) after
    # three straight days of 503 storms outlasting the old 10.5-minute
    # budget entirely, on every pass, not just the expensive ones - a job
    # taking longer is free on GitHub Actions; a job failing outright isn't.
    # The real fix for that pattern is the roles.json model swap (moving
    # off gemini-3.6-flash, which is under sustained load, onto the
    # higher-throughput 3.5-flash-lite tier); this is the secondary margin.
    truncations = 0
    errors = 0
    while True:
        body = {
            "systemInstruction": {"parts": [{"text": system}]},
            "contents": [{"role": "user", "parts": [{"text": user}]}],
            "generationConfig": {"temperature": 1.0, "maxOutputTokens": max_tokens},
        }
        try:
            req = urllib.request.Request(
                url,
                data=json.dumps(body).encode(),
                headers={
                    "Content-Type": "application/json",
                    "User-Agent": "ai-novel-pipeline/1.0",
                },
            )
            # 300s, not 180s: raised max_tokens ceilings (unify/revise can now
            # ask for 24576+ after repeated truncation-retries) mean a genuine
            # completion can legitimately take longer to generate.
            with urllib.request.urlopen(req, timeout=300) as resp:
                data = json.loads(resp.read())
            candidate = data["candidates"][0]
            finish = candidate.get("finishReason")
            parts = candidate.get("content", {}).get("parts", [])
            text = parts[0]["text"] if parts else ""
            # Gemini 2.5/3.x "thinking" models count invisible reasoning
            # tokens against maxOutputTokens with no separate budget or
            # validation - a call can burn most of its budget thinking and
            # return a chapter truncated mid-sentence with finishReason
            # MAX_TOKENS, which looks like ordinary (short) text if you don't
            # check for it. Caught live: unify given a healthy 3413-word
            # draft returned 265 words that stopped mid-scene, and the editor
            # read the incompleteness as the chapter diverging from the
            # skeleton. Detect it and retry with a larger budget instead of
            # quietly accepting a fragment as a finished pass.
            if finish == "MAX_TOKENS" and truncations < truncation_retries:
                truncations += 1
                max_tokens = int(max_tokens * 1.6)
                print(f"             (gemini hit MAX_TOKENS with {len(text.split())} "
                      f"words visible - retrying with maxOutputTokens={max_tokens})")
                continue
            if not text:
                raise ModelError(f"gemini returned no usable text (finishReason={finish})")
            return text
        except urllib.error.HTTPError as e:
            if e.code in (429, 503) and errors < error_retries:
                errors += 1
                wait = 30 * errors
                print(f"             (gemini {e.code} - retrying in {wait}s, "
                      f"attempt {errors}/{error_retries})")
                time.sleep(wait)
                continue
            raise ModelError(f"gemini {e.code}: {e.read()[:300]}")
        except OSError as e:
            # Catches urllib.error.URLError, socket.timeout/TimeoutError, and
            # - the gap found live on chapter 6 - raw connection failures
            # like http.client.RemoteDisconnected that urllib does NOT wrap
            # in URLError. do_open() only wraps OSError from h.request();
            # an OSError raised later from h.getresponse() (a dropped
            # connection, reset, etc.) propagates unwrapped, so the
            # previous (socket.timeout, TimeoutError, URLError) tuple missed
            # it entirely and crashed the run uncaught. Every one of these
            # is OSError under the hood (RemoteDisconnected is a
            # ConnectionResetError is a ConnectionError is an OSError), and
            # HTTPError - also technically an OSError subclass - is already
            # caught by the more specific except above it, so broadening
            # this to plain OSError is strictly more coverage, not less
            # precision.
            if errors < error_retries:
                errors += 1
                wait = 30 * errors
                print(f"             (gemini request error ({e}) - retrying "
                      f"in {wait}s, attempt {errors}/{error_retries})")
                time.sleep(wait)
                continue
            raise ModelError(f"gemini request failed after retries: {e}")
        except (KeyError, IndexError) as e:
            raise ModelError(f"gemini returned no usable text: {e}")


# --------------------------------------------------------------------------
# openai-compatible: Groq, OpenRouter, Cerebras, Mistral, local
# --------------------------------------------------------------------------


def _openai_compatible(role_cfg, system, user, max_tokens, error_retries=6):
    key = os.environ.get(role_cfg.get("api_key_env", ""))
    base = role_cfg.get("base_url")
    if not key or not base:
        raise ModelError(f"missing base_url or key env for role {role_cfg.get('role')}")

    body = {
        "model": role_cfg["model"],
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
        "temperature": 1.0,
        "max_tokens": max_tokens,
    }
    # Optional, per-role: a reasoning model (Groq's qwen roles) can emit its
    # whole chain-of-thought as literal <think>...</think> text sharing the
    # same max_tokens budget as the real answer - caught live on the
    # summariser, where it burned 2000 tokens on reasoning and never reached
    # the actual summary. Only set on roles.json entries that need it, so
    # this can't affect a role that doesn't recognize these fields.
    if "reasoning_effort" in role_cfg:
        body["reasoning_effort"] = role_cfg["reasoning_effort"]
    if "reasoning_format" in role_cfg:
        body["reasoning_format"] = role_cfg["reasoning_format"]

    errors = 0
    while True:
        try:
            req = urllib.request.Request(
                base.rstrip("/") + "/chat/completions",
                data=json.dumps(body).encode(),
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {key}",
                    "User-Agent": "ai-novel-pipeline/1.0",
                },
            )
            with urllib.request.urlopen(req, timeout=300) as resp:
                data = json.loads(resp.read())
            return data["choices"][0]["message"]["content"]
        except urllib.error.HTTPError as e:
            if e.code in (429, 503) and errors < error_retries:
                errors += 1
                time.sleep(30 * errors)
                continue
            raise ModelError(f"{role_cfg.get('role')} {e.code}: {e.read()[:300]}")
        except OSError as e:
            # Same broadening as _gemini() - see its comment. Covers
            # URLError/timeouts and raw connection drops (RemoteDisconnected
            # etc.) that urllib doesn't wrap, without swallowing HTTPError
            # (already handled above, and matched first regardless).
            if errors < error_retries:
                errors += 1
                time.sleep(30 * errors)
                continue
            raise ModelError(f"{role_cfg.get('role')} request failed after retries: {e}")
