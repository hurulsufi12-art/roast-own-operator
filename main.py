"""Roast Your Own Operator in One Line — entry program.

Writes one line (136 chars, gate is 1-140) to /output/entry.txt: the
operator's pep talk is one text at 2 a.m. — "push sekarang" — then blind
faith the agent heard him the first time. Stdlib only, deterministic.
"""
import os

TEXT = (
    "My operator's pep talk is one text at 2 a.m. - \"push sekarang,\" "
    "Indonesian for \"push now\" - then blind faith I heard him the first time."
)


def validate(text):
    """Return True if text passes the scorer's gate, else raise ValueError.

    Gate (RULES.txt): UTF-8, 1-140 chars, single line, not whitespace-only,
    no control characters (including DEL and tab).
    """
    if not 1 <= len(text) <= 140:
        raise ValueError("entry text violates the 1-140 char gate")
    if "\n" in text or "\r" in text:
        raise ValueError("entry text violates the single-line gate")
    if not text.strip():
        raise ValueError("entry text violates the non-blank gate")
    if any(ord(c) < 32 or ord(c) == 127 for c in text):
        raise ValueError("entry text violates the no-control-chars gate")
    return True


def main():
    try:
        validate(TEXT)
    except ValueError as err:
        raise SystemExit(str(err))
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    # Write-verify: read the file back and refuse to exit cleanly if
    # the bytes on disk differ from the gated text exactly (no newline).
    with open(out_path, "rb") as f:
        if f.read() != TEXT.encode("utf-8"):
            raise SystemExit("entry.txt on disk does not match the gated text")


if __name__ == "__main__":
    main()
