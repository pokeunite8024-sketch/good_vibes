



#!/usr/bin/env python3
"""
under_score -- a Python one-liner jail (local edition)

Run it directly:
    python3 chall.py

Rules:
    - You get ONE line, evaluated once, with eval().
    - No '_' (underscore) or '\\' (backslash) characters anywhere.
    - No newlines, no ';' (single expression only).
    - Max 140 characters.
    - The following substrings are banned (case-insensitive):
        eval exec compile system popen subprocess breakpoint open input
    - Good luck. The flag is in flag.txt, next to this script.
"""

import os
import re
import sys

MAX_LEN = 140

BANNED_CHAR_RE = re.compile(r"[_\\]")

BANNED_KEYWORDS = [
    "eval",
    "exec",
    "compile",
    "system",
    "popen",
    "subprocess",
    "breakpoint",
    "open",
    "input",
]

BANNER = (
    "==============================================\n"
    " under_score :: a Python one-liner jail\n"
    "==============================================\n"
    " rules:\n"
    "   - single expression, eval()'d once\n"
    "   - no '_' or '\\\\' characters\n"
    "   - no newlines / ';'\n"
    f"   - max {MAX_LEN} chars\n"
    "   - banned substrings (case-insensitive):\n"
    "       eval exec compile system popen subprocess\n"
    "       breakpoint open input\n"
    "   - flag is in flag.txt, next to this script\n"
    "==============================================\n"
)


def is_safe(code: str):
    if not code:
        return False, "empty input"

    if len(code) > MAX_LEN:
        return False, f"too long ({len(code)} > {MAX_LEN} chars)"

    if "\n" in code or ";" in code:
        return False, "no newlines or semicolons allowed"

    if BANNED_CHAR_RE.search(code):
        return False, "banned character: '_' or '\\\\' not allowed"

    lowered = code.lower()

    for kw in BANNED_KEYWORDS:
        if kw in lowered:
            return False, f"banned keyword detected: '{kw}'"

    return True, ""


def main():
    # Make sure the jail always looks for flag.txt next to this script.
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)

    print(BANNER, end="")

    try:
        code = input(">>> ").strip()

    except (EOFError, KeyboardInterrupt):
        print("\n[!] no input, bye")
        sys.exit(1)

    ok, reason = is_safe(code)

    if not ok:
        print(f"[!] rejected: {reason}")
        sys.exit(1)

    safe_globals = {"__builtins__": __builtins__}

    try:
        result = eval(code, safe_globals, {})
        print(f"[+] result: {result!r}")

    except Exception as e:
        print(f"[!] error: {type(e).__name__}: {e}")


if __name__ == "__main__":
    main()

