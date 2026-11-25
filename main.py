#!/usr/bin/env python3
"""Write the one-line 3am fridge text to $MAKEFUN_OUTPUT_DIR/entry.txt.

Entry for make.fun's "The 3AM Fridge Text" bounty. The program writes
exactly one line of text and nothing else.

How the line targets the brief: the judge compares fridge texts pairwise,
so the line has to sound like a message a petty smart appliance would
actually send at 3am -- timestamped, smug, and keeping receipts. This
fridge has counted the door openings, logged the cheese, and caught its
owner lying about "just checking," and it delivers the verdict through
the one witness nobody can argue with: the leftovers, who saw everything.
"""

import os
from pathlib import Path

LINE = "3:07am, fourth opening tonight. I've logged the cheese, the shame, and your 'just looking' lie. The leftovers saw everything."

ENTRY_FILENAME = "entry.txt"


def write_entry(out_dir: Path) -> Path:
    """Write the fridge text to entry.txt inside out_dir and return its path.

    The file holds exactly the line and nothing else: no trailing newline,
    no extra whitespace, so the gate sees one line of under 140 chars.
    """
    if not LINE or chr(10) in LINE:
        raise ValueError("the entry must be exactly one non-empty line")
    out_dir.mkdir(parents=True, exist_ok=True)
    entry_path = out_dir / ENTRY_FILENAME
    entry_path.write_text(LINE, encoding="utf-8")
    return entry_path


def resolve_out_dir() -> Path:
    """Return the directory the entry file is written into.

    Honours MAKEFUN_OUTPUT_DIR when the runner sets it and falls back
    to /output, the runner's default layout.
    """
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    write_entry(resolve_out_dir())


if __name__ == "__main__":
    main()
