"""One Word, First Thought — make.fun bounty u-0xkianno-one-word-first-thought-106abaf8.

Writes exactly one word to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
The word is "nudiustertian": relating to the day before yesterday.
A whole word for a day English normally needs a whole phrase for —
surprising, specific, and quietly witty.
"""

import os

WORD = "nudiustertian"


def main() -> None:
    # The entry must be exactly one word: fail loudly rather than ever
    # writing two words, a blank, or a trailing newline.
    if not WORD or any(ch.isspace() for ch in WORD):
        raise ValueError(f"Entry must be exactly one word, got {WORD!r}")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
