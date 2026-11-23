#!/usr/bin/env python3
"""One Line, Zero Use: The Useless Superpower Sprint.

Writes a single original line (at most 200 characters) describing a
hilariously useless superpower to /output/entry.txt.

No network, no model calls, no randomness: the same line every run, so
the replay matches the live run exactly.
"""

import os

LINE = "I can teleport anywhere in the universe, but only to the exact spot where I'm already standing."
# The joke pays off in the last few words: the grandest power imaginable,
# cancelled by a destination the hero never leaves.


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
