# under_score (local edition)

**Category:** Misc / PyJail
**Difficulty:** Hard

## Description

> One underscore. That's all I'm asking you not to use.

This is a local challenge — no server, no network. Just run:

```
python3 chall.py
```

It prints a banner, then prompts you with `>>>` for a single line of
Python. That line is run through `eval()`. That's the whole attack surface.

## Rules enforced by the script

- Exactly one line of input, evaluated once as a single Python expression.
- No `_` (underscore) or `\` (backslash) characters, anywhere in your input.
- No newlines or `;` — it must be one expression, not a sequence of statements.
- Max 140 characters.
- The following substrings are banned, case-insensitive, wherever they occur:
  `eval exec compile system popen subprocess breakpoint open input`

If your input violates a rule, you're told which one, and the script exits.
Otherwise your expression is evaluated and the `repr()` of the result (or
the exception) is printed.

## Goal

Make the script read `flag.txt`, which sits right next to `chall.py`.

## Files provided

- `chall.py` — the whole challenge, run it with `python3 chall.py`
- `flag.txt` — replace the placeholder with your real flag before handing
  this out

## Hints (progressive — open only if stuck)

<details>
<summary>Hint 1</summary>

You can't type `__class__`, `__import__`, `__builtins__`, or any other dunder
directly — they all contain the banned character. But you *can* compute the
underscore character at runtime. What function turns a number into a
character?
</details>

<details>
<summary>Hint 2</summary>

`chr(95)` gives you `'_'` without ever typing it. String concatenation and
multiplication (`chr(95)*2 + 'class' + chr(95)*2`) let you build any dunder
name you need, and `getattr(obj, name_string)` lets you fetch attributes by
a computed string instead of literal dot-syntax.
</details>

<details>
<summary>Hint 3</summary>

`globals()['__builtins__']` isn't banned by name — but you can't write the
string `'__builtins__'` literally either (it has underscores). Build that
string the same way you built `'__class__'`. From there you can reach
`__import__` the same way, without ever typing the banned words — check
which literal words are *actually* on the ban list before deciding what
needs obfuscating.
</details>

<details>
<summary>Hint 4</summary>

`open` is explicitly banned as a substring, so the obvious `open('flag.txt')`
is out, even if you build it with `getattr`. You need another way to turn a
path into bytes. Look at what `io.FileIO` gives you.
</details>

## Flag format

`flag{...}`
