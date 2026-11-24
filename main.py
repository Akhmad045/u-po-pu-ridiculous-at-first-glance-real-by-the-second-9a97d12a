#!/usr/bin/env python3
"""Write one bizarre-but-sound startup pitch to /output/entry.txt.

The pitch is a single sentence (at most 200 characters) for the
make.fun bounty "Ridiculous at First Glance, Real by the Second".
Standard library only; no network access.

Usage: python3 main.py
"""

import os

ENTRY = (
    "HotBeds rents one bed to two strangers working opposite shifts: "
    "a night nurse sleeps by day, a barista by night, so each pays half "
    "the rent and landlords earn double from a single mattress."
)

OUTPUT_PATH = "/output/entry.txt"


def validate(line):
    """Check the pitch against the gate: 1-200 chars, one clean line."""
    if not line:
        raise ValueError("entry is empty")
    if len(line) > 200:
        raise ValueError(f"entry is {len(line)} chars, over the 200 limit")
    if line != line.strip():
        raise ValueError("entry has leading or trailing whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if any(ord(ch) < 32 or ord(ch) == 127 for ch in line):
        raise ValueError("entry contains control characters")
    if not line.strip():
        raise ValueError("entry is only whitespace")
    return line


def main():
    line = validate(ENTRY)
    data = line.encode("utf-8")
    if data.decode("utf-8") != line:
        raise SystemExit("entry does not survive a UTF-8 round-trip")

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "wb") as fh:
        fh.write(data)

    with open(OUTPUT_PATH, "rb") as fh:
        back = fh.read()
    if back != data:
        raise SystemExit("written file does not round-trip exactly")

    print(f"wrote {len(line)} chars ({len(data)} bytes) to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
