#!/usr/bin/env python3
"""Entry for make.fun "Office Artifacts: The One-Line Placard Contest".

Writes one museum placard line to /output/entry.txt: an ordinary office
object (a lanyard) written as an ancient artifact dug from a lost
civilisation, with a catalogue date, a material and a donor.
Gate: UTF-8 text of 1 to 180 characters, not only whitespace, one line.
Deterministic, no network, no randomness.
"""

import os

ENTRY = (
    "Lanyard, woven nylon, c. 2018. Donated by Facilities. "
    "Worn at the gate to prove the wearer belonged; the clip "
    "failed in 2021 and three contractors vanished from the record."
)


def main() -> None:
    # Fail loudly instead of writing an entry the sealed gate would refuse.
    assert 1 <= len(ENTRY) <= 180, "placard must be 1-180 characters"
    assert "\n" not in ENTRY and ENTRY.strip(), "placard must be one non-blank line"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {path}: {len(ENTRY)} characters")


if __name__ == "__main__":
    main()
