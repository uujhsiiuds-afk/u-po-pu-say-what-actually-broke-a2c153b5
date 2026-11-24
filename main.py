#!/usr/bin/env python3
"""Say What Actually Broke — writes one line of error copy to /output/entry.txt.

The entry is a single-line software error message (at most 200 characters)
that tells the user the brutal truth about what went wrong and makes them
laugh on the way: an upload died because the server's own disk filled up
mid-save, and the only thing it managed to keep was the apology.
"""

import os
import sys

ENTRY = (
    "Your upload failed: our server ran out of disk space halfway through "
    "and kept only this apology. That's our disk, not yours \u2014 try "
    "again in a minute."
)

OUTPUT_PATH = "/output/entry.txt"


def validate(text: str) -> None:
    """Gate self-check: UTF-8, 1-200 characters, non-blank, single line."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not text.strip():
        raise ValueError("entry must not be blank")
    if len(text) < 1 or len(text) > 200:
        raise ValueError(
            f"entry is {len(text)} characters, must be 1-200 characters"
        )
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")  # raises if the text is not valid UTF-8


def main() -> int:
    validate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {OUTPUT_PATH}")
    print(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
