# SPDX-License-Identifier: MIT
"""Write a dying phone's last text at 1% battery to /output/entry.txt.

Deterministic, offline, stdlib-only: the text is a fixed string, so every
run writes byte-identical output.
"""

import os

TEXT = (
    "At 1% I finally say it: tell my charger I loved it, tell my photos "
    "I tried to save them, and if I die mid-reply, I was typing something "
    "profound - trust me."
)
# The text is a single line well inside the 200-character cap.

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
