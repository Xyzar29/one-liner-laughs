#!/usr/bin/env python3
"""One-Liner Laughs entry: write a single funny line to /output/entry.txt.

The joke is a fixed, hand-written one-liner. The program is fully
deterministic: every run writes exactly the same bytes.
"""

import os

JOKE = "My therapist says I use humor to deflect, so in conclusion, my childhood was hilarious."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = JOKE
    assert 1 <= len(text) <= 200, "joke must be 1-200 characters"
    assert text.strip(), "joke must not be only whitespace"
    assert "\n" not in text and "\r" not in text, "joke must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
