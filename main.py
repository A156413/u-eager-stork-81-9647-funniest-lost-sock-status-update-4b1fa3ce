#!/usr/bin/env python3
"""Funniest Lost Sock Status Update — make.fun entry.

Writes one status update, in the voice of a lost sock, to /output/entry.txt
and prints the same line to stdout.
"""

import os

STATUS = (
    "Day 47 behind the dryer: the lint is friendly, the static is strong, "
    "and I have started a new life with a single glove."
)

MAX_CHARS = 120


def main() -> None:
    assert len(STATUS) <= MAX_CHARS, (
        f"status update is {len(STATUS)} chars, over the {MAX_CHARS} limit"
    )
    os.makedirs("/output", exist_ok=True)
    # The grader collects outputs as another user: everything under
    # /output must be world-readable.
    os.chmod("/output", 0o755)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(STATUS + "\n")
    os.chmod("/output/entry.txt", 0o644)
    with open("/output/entry.txt", encoding="utf-8") as f:
        assert f.read().strip() == STATUS, "entry.txt does not match STATUS"
    print(STATUS)


if __name__ == "__main__":
    main()
