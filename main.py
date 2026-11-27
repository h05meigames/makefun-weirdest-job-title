#!/usr/bin/env python3
"""Weirdest Job Title entry — program/v2 (blind round 2).

Writes a single job title, the weirdest one we could think of, to
/output/entry.txt. The title is a real-sounding job with one hilariously
specific twist: a professional mourner — a genuinely real profession —
whose clients are complete strangers holding funerals for their goldfish.
Solemn, credentialed-sounding work applied to the tiniest, most trivial
subject imaginable.

Deterministic: the same title is written on every run.

The file holds exactly the title bytes and nothing else — no trailing
newline — because the bounty asks for a single job title and nothing else.
"""

import os

TITLE = "Professional Mourner for Strangers' Goldfish Funerals"
OUTPUT_PATH = "/output/entry.txt"
MAX_TITLE_CHARS = 60


def main() -> None:
    assert len(TITLE) <= MAX_TITLE_CHARS, (
        f"title is {len(TITLE)} chars, over the {MAX_TITLE_CHARS} limit"
    )
    assert TITLE == TITLE.strip() and "\n" not in TITLE, (
        "title must be a single line with no leading/trailing whitespace"
    )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(TITLE)
    # Verify the write: a silent partial write must never ship.
    with open(OUTPUT_PATH, "rb") as f:
        assert f.read().decode("utf-8") == TITLE, (
            "written file does not hold exactly the title"
        )


if __name__ == "__main__":
    main()
