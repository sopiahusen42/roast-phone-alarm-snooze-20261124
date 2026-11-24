"""Write the entry line for the make.fun bounty "One-Line Roast".

The program is deterministic: it holds one fixed line, validates it, and
writes it as UTF-8 plus a trailing newline to <output>/entry.txt. It never
reads the clock, touches the network, or generates anything random, so every
run produces byte-identical output. Pass MAKEFUN_OUTPUT_DIR to redirect the
output directory; it defaults to /output.
"""

import os
import sys

LINE = "My phone's snooze button is exactly the size of my thumb asleep. That is not a feature, that is a co-conspirator."

OUTPUT_DIR_DEFAULT = "/output"
FILENAME = "entry.txt"


def validate_entry(text):
    """Return an error string if `text` is not a valid entry line, else None."""
    if not isinstance(text, str):
        return "entry must be a str"
    if not text.strip():
        return "entry is blank"
    if len(text) > 200:
        return "entry is %d code points, limit is 200" % len(text)
    if "\n" in text or "\r" in text:
        return "entry must be a single line"
    if text != text.strip():
        return "entry has surrounding whitespace"
    return None


def main():
    text = LINE

    problem = validate_entry(text)
    if problem is not None:
        sys.stderr.write(problem + "\n")
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", OUTPUT_DIR_DEFAULT)
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, FILENAME)
    payload = (text + "\n").encode("utf-8")

    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text + "\n")

    with open(path, "rb") as handle:
        on_disk = handle.read()

    if on_disk != payload:
        sys.stderr.write("read-back mismatch at %s\n" % path)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
