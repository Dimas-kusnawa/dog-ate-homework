#!/usr/bin/env python3
"""The Dog Ate My Homework: Funniest Excuse.

Writes one line to /output/entry.txt: the excuse a dog gives after
being caught eating the homework, in the dog's own voice.
"""

import os

# The line: the worksheet said "show your work", so the dog took the
# instruction literally and showed it to his stomach. A dog who
# believes he has done nothing wrong - he followed the instructions.
# Why it lands: the twist is dog logic applied to a real school phrase.
# It is not a stock line about the cat, the taste of paper, or being
# a good boy; the dog is proud, not embarrassed, and the joke needs
# no setup beyond the homework already being gone.
LINE = "It said 'show your work'. I showed it to my stomach, and I have never been prouder of a maths problem."


def main():
    # The gate wants 1 to 200 UTF-8 characters, not only white space.
    # This line is 102 characters, one line, no trailing newline.
    assert 1 <= len(LINE) <= 200, "line must fit the 200-char cap"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
