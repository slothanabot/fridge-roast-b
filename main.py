#!/usr/bin/env python3
"""Fridge Roast: One Line, Biggest Laugh (make.fun entry).

Writes a single original one-line roast of a smart fridge to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output). Standard library only,
deterministic, no network, no model calls.
"""

import os
import sys

LINE = "My smart fridge's touchscreen froze mid-update — the first time anything in it has ever actually been frozen."


def main() -> int:
    text = LINE.strip()
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"line is {len(text)} characters, must be 1-200")
    if "\n" in text or text != LINE:
        raise SystemExit("line must be a single line with no extra whitespace")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = text.encode("utf-8")
    with open(path, "wb") as handle:
        handle.write(data)
    os.chmod(path, 0o644)
    print(f"Wrote {len(text)} characters ({len(data)} bytes) to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
