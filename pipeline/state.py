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


# ------------------------------------------------------------------ motifs


MOTIF_ROLES = ("action", "character", "atmosphere")


def load_motifs():
    p = NOVEL / "motifs.json"
    if not p.exists():
        return {role: [] for role in MOTIF_ROLES}
    data = json.loads(p.read_text())
    for role in MOTIF_ROLES:
        data.setdefault(role, [])
    return data


def save_motifs(motifs):
    (NOVEL / "motifs.json").write_text(json.dumps(motifs, indent=2))


def motif_brief(n, motifs):
    """Every logged detail across all three descriptive passes, so atmosphere
    knows what character already spent and vice versa. Cooldown is advisory —
    the prompt tells the model it can override for plot-load-bearing detail."""
    rows = []
    for role in MOTIF_ROLES:
        for m in motifs.get(role, []):
            since = n - m["last_used"]
            gap = m.get("min_gap", 1)
            if since < gap:
                status = f"ON COOLDOWN — free again ch. {m['last_used'] + gap} unless this chapter's events need it now"
            else:
                status = "free to reuse"
            subj = f"{m['subject']} — " if m.get("subject") else ""
            rows.append(
                f"- [{role}] {subj}\"{m['detail']}\" (id: {m['id']}) — "
                f"last used ch. {m['last_used']}, {status}"
            )
    return "\n".join(rows) if rows else "(no recurring details logged yet)"


def merge_motifs(motifs, role, n, entries):
    log = motifs.setdefault(role, [])
    by_id = {m["id"]: m for m in log}
    for e in entries:
        mid = e.get("id")
        if not mid:
            continue
        gap = e.get("min_gap")
        gap = gap if isinstance(gap, int) and gap > 0 else 3
        if mid in by_id:
            by_id[mid]["last_used"] = n
            by_id[mid]["min_gap"] = gap
        else:
            rec = {
                "id": mid,
                "subject": e.get("subject", ""),
                "detail": e.get("detail", ""),
                "min_gap": gap,
                "last_used": n,
            }
            log.append(rec)
            by_id[mid] = rec
    save_motifs(motifs)


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


def save_ends_on(n, text):
    """The skeleton's closing image, persisted the moment skeleton completes.
    Every later pass is instructed to preserve it, so it's a reliable record
    of how the chapter actually ends — used to bridge into the next one."""
    CHAPTERS.mkdir(parents=True, exist_ok=True)
    (CHAPTERS / f"{n:02d}.ends_on.txt").write_text(text.strip())


def previous_ending(n):
    p = CHAPTERS / f"{n - 1:02d}.ends_on.txt"
    return p.read_text().strip() if p.exists() else "(this is the first chapter)"


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


def clear_pass(n, name):
    (ws(n) / f"{name}.txt").unlink(missing_ok=True)


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
