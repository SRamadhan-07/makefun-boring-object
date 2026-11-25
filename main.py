"""Write a deadpan one-line review of a flat-pack spare screw.

The review goes exactly, with no extra output, to /output/entry.txt.
"""

import os

ENTRY_TEXT = (
    "Flat-pack spare screw: not needed, not thrown away, "
    "now legally the most permanent fixture in the home."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as out:
        out.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
