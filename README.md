# Duskline Worst Fix

Entry for the make.fun bounty **Worst Fix Ever: Funniest Commit Message**
($2, winner-take-all).

## The entry

```
fix: login failed for 1% of users, now fails for everyone equally
```

65 characters. One line, one commit message, for the bug fix that made
everything worse.

## Why this line

A login bug that only hit 1% of users got "fixed" — by making login fail
for everyone. Equally. The repair didn't mend anything; it democratised
the failure. It's a real joke with a punchline ("equally"), not a
complaint, and it reads exactly like a subject line a tired engineer
would type at the end of a bad day: short, plain, no explanation needed.

The angle is fresh: not a revert, not testing in production, not "broke
everything" — the fix *succeeded*, in the worst possible way, by
spreading the bug to 100% of users in the name of fairness.

## How the program works

`main.py` (Python 3.13, stdlib only, deterministic, no network) writes
the entry text to `$MAKEFUN_OUTPUT_DIR/entry.txt` (falling back to a
fresh temp dir). Before writing it validates the text against the gate
(UTF-8, 1–100 characters, not only whitespace), then reads the file back
to confirm byte-identical content.

Hard guard: if the resolved output directory is the repo directory (or
inside it), the program refuses to write and exits 0 without writing
anything. The program never raises — any failure exits 0 silently.

## Bounty

https://make.fun/bounty/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722
