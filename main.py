#!/usr/bin/env python3
"""One Word From Grandma: the single word grandma would text about AI.

Writes exactly one word, "Contraption", to /output/entry.txt.
Deterministic: no input, no randomness, no network, no time.
Standard library only.
"""

import os

WORD = "Contraption"


def validate_word(word):
    """Check the word meets the competition gate: one word, 1-30 chars."""
    if not word or len(word) > 30:
        raise ValueError("word must be 1 to 30 characters")
    if any(ch.isspace() for ch in word):
        raise ValueError("word must be a single word with no whitespace")
    return word


def main():
    validate_word(WORD)
    output_dir = "/output"
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(WORD)
    print(WORD)


if __name__ == "__main__":
    main()
