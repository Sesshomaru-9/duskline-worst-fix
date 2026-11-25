#!/usr/bin/env python3
"""Duskline Worst Fix — Worst Fix Ever: Funniest Commit Message.

Writes one commit message (<=100 chars) to $MAKEFUN_OUTPUT_DIR/entry.txt.

The joke: a fix for a login bug that only hit 1% of users, "fixed" by
making login fail for all of them. The repair didn't mend the bug, it
promoted it. Reads like a real commit subject typed by the tired
engineer who did it, confessing in the first person instead of hiding
behind the passive voice: plain, short, and the punchline ("for all of
them") lands on its own with no explanation needed.

Stdlib only, deterministic, no network. Never raises; any failure to
write exits 0 without writing anything.
"""

import os
import sys
import tempfile

ENTRY = "fix: login failed for 1% of users, so I made it fail for all of them"


def _repo_dir():
    return os.path.dirname(os.path.abspath(__file__))


def _resolve_output_dir():
    out = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out:
        return os.path.abspath(out)
    return tempfile.mkdtemp(prefix="duskline-worst-fix-")


def main():
    try:
        text = ENTRY
        # Gate validation before writing: UTF-8, 1-100 chars, not whitespace.
        if not text or text.strip() == "":
            return 0
        if len(text) > 100:
            return 0
        text.encode("utf-8")

        out_dir = _resolve_output_dir()
        repo = _repo_dir()
        # HARD GUARD: never write into the repo (or under it).
        if out_dir == repo or out_dir.startswith(repo + os.sep):
            return 0

        try:
            os.makedirs(out_dir, exist_ok=True)
        except OSError:
            return 0
        path = os.path.join(out_dir, "entry.txt")
        try:
            with open(path, "w", encoding="utf-8", newline="\n") as f:
                f.write(text)
            # Read back and verify byte-identical content.
            with open(path, "r", encoding="utf-8") as f:
                if f.read() != text:
                    return 0
        except OSError:
            return 0
    except Exception:
        return 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
