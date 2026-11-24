#!/usr/bin/env python3
"""Write one bizarre-but-sound startup pitch to /output/entry.txt.

The pitch is a single sentence (at most 200 characters) for the
make.fun bounty "Ridiculous at First Glance, Real by the Second".
Standard library only; no network access.

Usage: python3 main.py
"""

import os

ENTRY = (
    "HotBeds rents one bed to two strangers on opposite shifts \u2014 "
    "a night nurse sleeps by day, a barista by night \u2014 so each pays "
    "half the rent and the landlord earns twice from one mattress."
)

OUTPUT_PATH = "/output/entry.txt"


def main():
    line = ENTRY
    if not (1 <= len(line) <= 200):
        raise SystemExit(f"entry is {len(line)} chars, must be 1-200")
    if line != line.strip():
        raise SystemExit("entry has leading or trailing whitespace")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be a single line")
    if any(ord(ch) < 32 for ch in line):
        raise SystemExit("entry contains control characters")

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as fh:
        fh.write(line)

    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as fh:
        back = fh.read()
    if back != line:
        raise SystemExit("written file does not round-trip exactly")

    print(f"wrote {len(line)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
