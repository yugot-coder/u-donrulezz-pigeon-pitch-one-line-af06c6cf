"""Pigeon Pitch, One Line.

Competition: u-donrulezz-pigeon-pitch-one-line-af06c6cf
Final pitch (19 words, 102 characters, one line):
    I poop on your car for free — the premium tier is your competitor's car. Seed round's open, gentlemen.

Gate (from the kit's competition.yaml): /output/entry.txt must be UTF-8
text of 1 to 200 characters, not only whitespace, one line.
This program is deterministic, stdlib only, no network, no randomness, no
clock: it writes the fixed pitch to entry.txt under MAKEFUN_OUTPUT_DIR
(default "/output").
"""

import os

TEXT = "I poop on your car for free — the premium tier is your competitor's car. Seed round's open, gentlemen.\n"


def check_gate():
    """Assert the pitch passes the kit gate before anything is written."""
    body = TEXT.rstrip("\n")
    assert 1 <= len(body) <= 200, "gate: entry must be 1-200 characters"
    assert body.strip(), "gate: entry must not be only whitespace"
    assert "\n" not in body, "gate: entry must be a single line"


def verify_written_bytes(path):
    """Read the file back and compare it byte-for-byte with TEXT."""
    with open(path, "rb") as fh:
        data = fh.read()
    assert data == TEXT.encode("utf-8"), "written bytes differ from TEXT"
    return data


def main():
    check_gate()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(TEXT)
    verify_written_bytes(path)


if __name__ == "__main__":
    main()
