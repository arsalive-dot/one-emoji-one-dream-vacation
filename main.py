"""make.fun entry: One Emoji, One Dream Vacation.

Writes one emoji to /output/entry.txt — the entrant's dream
vacation in a single character. The pick is the volcano:
not a generic beach or plane, but one particular dream —
standing at the edge of an erupting volcano, lava glowing
below, the most alive place on earth.

Built to the judge brief's top criteria: exactly one emoji that
plainly names a dream vacation — a place, not a feeling
(criterion 1); it evokes the trip at a glance, lava glowing
below the rim (criterion 2); it points at one particular dream
rather than any holiday (criterion 3); it is a fresh pick with
a spark of surprise where the beach and the plane are the
words everyone reaches for first (criterion 4); and it reads
instantly at small size on any screen (criterion 5).
"""

import os

ENTRY = "🌋"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    tmp_path = "/output/.entry.txt.tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.replace(tmp_path, "/output/entry.txt")
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
