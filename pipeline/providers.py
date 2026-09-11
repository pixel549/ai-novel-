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
    provider = role_cfg.get("provider", "stub")

    if provider == "stub":
        return _stub(role_cfg)
    if provider == "gemini":
        return _gemini(system, user, role_cfg.get("model", "gemini-2.0-flash"), max_tokens)
    if provider == "openai_compatible":
        return _openai_compatible(role_cfg, system, user, max_tokens)
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


def _gemini(system, user, model, max_tokens, retries=4):
    key = os.environ.get("GEMINI_API_KEY")
    if not key:
        raise ModelError("GEMINI_API_KEY not set")

    url = (
        f"https://generativelanguage.googleapis.com/v1beta/models/"
        f"{model}:generateContent?key={key}"
    )

    # Gemini 2.5/3.x "thinking" models count invisible reasoning tokens
    # against maxOutputTokens with no separate budget or validation - a call
    # can burn most of its budget thinking and return a chapter truncated
    # mid-sentence with finishReason MAX_TOKENS, which looks like ordinary
    # (short) text if you don't check for it. Caught live: unify given a
    # healthy 3413-word draft returned 265 words that stopped mid-scene, and
    # the editor read the incompleteness as the chapter diverging from the
    # skeleton. Detect it and retry with a larger budget instead of quietly
    # accepting a fragment as a finished pass.
    for attempt in range(retries):
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
            with urllib.request.urlopen(req, timeout=180) as resp:
                data = json.loads(resp.read())
            candidate = data["candidates"][0]
            finish = candidate.get("finishReason")
            parts = candidate.get("content", {}).get("parts", [])
            text = parts[0]["text"] if parts else ""
            if finish == "MAX_TOKENS" and attempt < retries - 1:
                max_tokens = int(max_tokens * 1.6)
                print(f"             (gemini hit MAX_TOKENS with {len(text.split())} "
                      f"words visible - retrying with maxOutputTokens={max_tokens})")
                continue
            if not text:
                raise ModelError(f"gemini returned no usable text (finishReason={finish})")
            return text
        except urllib.error.HTTPError as e:
            if e.code in (429, 503) and attempt < retries - 1:
                time.sleep(30 * (attempt + 1))
                continue
            raise ModelError(f"gemini {e.code}: {e.read()[:300]}")
        except (KeyError, IndexError) as e:
            raise ModelError(f"gemini returned no usable text: {e}")
    raise ModelError("gemini: retries exhausted")


# --------------------------------------------------------------------------
# openai-compatible: Groq, OpenRouter, Cerebras, Mistral, local
# --------------------------------------------------------------------------


def _openai_compatible(role_cfg, system, user, max_tokens, retries=4):
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

    for attempt in range(retries):
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
            with urllib.request.urlopen(req, timeout=180) as resp:
                data = json.loads(resp.read())
            return data["choices"][0]["message"]["content"]
        except urllib.error.HTTPError as e:
            if e.code in (429, 503) and attempt < retries - 1:
                time.sleep(30 * (attempt + 1))
                continue
            raise ModelError(f"{role_cfg.get('role')} {e.code}: {e.read()[:300]}")
    raise ModelError("retries exhausted")
