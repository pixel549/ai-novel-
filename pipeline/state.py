"""Loading, parsing and persistence.

Every pass writes to workspace/NN/ as it completes, so a rate limit costs one
pass rather than the whole chapter. Rerun the same command to pick up.
"""

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NOVEL = ROOT / "novel"
WORKSPACE = ROOT / "workspace"
CHAPTERS = ROOT / "chapters"


def load_roles():
    with open(ROOT / "roles.json") as f:
        return json.load(f)


def canon():
    return (NOVEL / "canon.md").read_text()


# ------------------------------------------------------------------ outline


def chapter_beats(n):
    """Pull one chapter's section out of outline.md.

    Sections are headed '## Ch. N — Title'. Everything until the next '## ' or
    '# ' heading belongs to that chapter.
    """
    text = (NOVEL / "outline.md").read_text()
    pattern = rf"^## Ch\. {n} — (.+?)$"
    m = re.search(pattern, text, re.MULTILINE)
    if not m:
        raise SystemExit(f"no beats for chapter {n} in outline.md")

    start = m.end()
    rest = text[start:]
    nxt = re.search(r"^#{1,2} ", rest, re.MULTILINE)
    body = rest[: nxt.start()] if nxt else rest
    return {"number": n, "title": m.group(1).strip(), "beats": body.strip()}


def act_of(n):
    if n <= 5:
        return 1, "Edie"
    if n <= 16:
        return 2, "Lloyd"
    return 3, "Maria"


def last_chapters(n, k=3):
    """Summaries, not text. The drafter never sees a previous chapter whole —
    that is what stops context growing and what stops it continuing from prose
    instead of hitting the beat."""
    out = []
    for i in range(max(1, n - k), n):
        p = CHAPTERS / f"{i:02d}.summary.txt"
        if p.exists():
            out.append(f"Chapter {i}: {p.read_text().strip()}")
    return "\n\n".join(out) if out else "(this is the first chapter)"


# ---------------------------------------------------------------- workspace


def ws(n):
    d = WORKSPACE / f"{n:02d}"
    d.mkdir(parents=True, exist_ok=True)
    return d


def pass_done(n, name):
    return (ws(n) / f"{name}.txt").exists()


def save_pass(n, name, text):
    (ws(n) / f"{name}.txt").write_text(text)


def load_pass(n, name):
    return (ws(n) / f"{name}.txt").read_text()


def save_chapter(n, title, text):
    CHAPTERS.mkdir(parents=True, exist_ok=True)
    (CHAPTERS / f"{n:02d}.md").write_text(f"# {n}. {title}\n\n{text}\n")


def save_summary(n, text):
    CHAPTERS.mkdir(parents=True, exist_ok=True)
    (CHAPTERS / f"{n:02d}.summary.txt").write_text(text.strip())


def log_editor(n, attempt, verdict):
    """The rejection log. Frankly the most interesting output of the whole
    pipeline — keep it."""
    p = ws(n) / "editor.log"
    with open(p, "a") as f:
        f.write(f"--- attempt {attempt} ---\n{json.dumps(verdict, indent=2)}\n\n")
