#!/usr/bin/env python3
"""Weirdest Job Title entry — program/v1.

Writes a single job title, the weirdest one we could think of, to
/output/entry.txt. The title is a real-sounding job with one hilariously
specific twist: a senior, credentialed-sounding role whose entire purpose
is chaperoning penguins on Antarctic cruise ships.

Deterministic: the same title is written on every run.

The file holds exactly the title bytes and nothing else — no trailing
newline — because the bounty asks for a single job title and nothing else.
"""

import os

TITLE = "Senior Penguin Chaperone for Antarctic Cruise Ships"
OUTPUT_PATH = "/output/entry.txt"
MAX_TITLE_CHARS = 60


def main() -> None:
    assert len(TITLE) <= MAX_TITLE_CHARS, (
        f"title is {len(TITLE)} chars, over the {MAX_TITLE_CHARS} limit"
    )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(TITLE)


if __name__ == "__main__":
    main()
