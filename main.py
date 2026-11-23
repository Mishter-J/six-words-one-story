#!/usr/bin/env python3
"""Six Words, One Story — make.fun entry (program/v1).

Writes the chosen six-word story to /output/entry.txt.

The story: "The letter arrived after her funeral."
A letter posted in hope reaches its reader one day too late —
the sender's words survive, the person they were meant for does not.
Six words, one turn, and the letter's contents left unsaid.

The gate requires UTF-8 text of 1-60 characters, exactly six words,
so the program validates the story against the gate before writing it.
"""

import os

STORY = "The letter arrived after her funeral."

OUT_PATH = "/output/entry.txt"


def validate(story: str) -> None:
    """Fail loudly rather than write an entry the gate would refuse."""
    text = story.encode("utf-8").decode("utf-8")  # must be valid UTF-8
    if not 1 <= len(text) <= 60:
        raise ValueError(f"story is {len(text)} chars, gate allows 1-60")
    if len(text.split()) != 6:
        raise ValueError(f"story is {len(text.split())} words, gate needs 6")
    if not text.strip():
        raise ValueError("story must not be only whitespace")


def main() -> None:
    validate(STORY)
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(STORY)


if __name__ == "__main__":
    main()
