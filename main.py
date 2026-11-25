#!/usr/bin/env python3
"""make.fun entry: Monday Morning Punchlines
(u-gentle-badger-68-monday-morning-punchlines-709645dc).

Writes one joke about Monday mornings to /output/entry.txt. No network, no
randomness, no input: the output is byte-identical on every run.
"""

ENTRY = "My alarm clock requested weekends off — it says waking me on Monday counts as workplace harassment."
# The single submitted joke; keep byte-identical, do not reword.


def write_entry(path: str) -> None:
    """Write the joke to ``path`` as UTF-8 with no trailing newline."""
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


def main() -> None:
    write_entry("/output/entry.txt")


if __name__ == "__main__":
    main()
