#!/usr/bin/env python3
# Entry for "Pigeon Pitch, One Line" (make.fun).
"""Pigeon Pitch, One Line — entry program.

Writes the one-line pitch to /output/entry.txt.
"""

import os


def build_pitch():
    speaker = "Investors, I'm a pigeon"
    offer = "my startup sells landlords pigeon-proofing, then sells pigeons maps of the gaps"
    twist = "both sides pay"
    close = "the spikes were never the moat—we were"
    return f"{speaker}: {offer}; {twist}, and {close}."


def main():
    pitch = build_pitch()
    assert "\n" not in pitch
    assert pitch.strip()
    assert len(pitch) <= 200
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(pitch)


if __name__ == "__main__":
    main()
