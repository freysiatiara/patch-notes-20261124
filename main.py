"""Real-Life Patch Notes: The Comedy Changelog.

The program writes one patch-note line to /output/entry.txt: a terse
software release note for a bug in real life / human biology. The joke
is a specific, recognisable memory bug: the brain keeps every song
lyric from 2009 yet forgets why you walked into the kitchen.
"""

import os

ENTRY = (
    "v2.4.0: fixed a bug where the brain remembered every song lyric "
    "from 2009 but forgot why you opened the fridge."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 160 characters.
    assert 1 <= len(ENTRY) <= 160, len(ENTRY)
    assert "\n" not in ENTRY
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
