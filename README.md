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



If your input violates a rule, you're told which one, and the script exits.
Otherwise your expression is evaluated and the `repr()` of the result (or
the exception) is printed.

## Goal

Make the script read `flag.txt`, which sits right next to `chall.py`.

## Files provided

- `chall.py` — the whole challenge, run it with `python3 chall.py`
- `flag.txt` — replace the placeholder with your real flag before handing
  this out



## Flag format

`flag{...}`
