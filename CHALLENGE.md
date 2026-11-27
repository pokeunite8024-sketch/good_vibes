# THREE LOCKS (v2, hard mode)

Three locks, one flag: `FLAG{24 hex characters}`.
No hints. No partial credit. Guessing is useless.

## Files
- `stage1_keystream.txt`: 320 output bits of a generator
- `stage2.bin`: sealed data
- `final.bin`: the encrypted flag

## Lock 1: the generator
Three Fibonacci LFSRs (all seeds non-zero, seed = initial state as an integer):

| name | length | taps (1-indexed) |
|------|--------|------------------|
| A    | 28     | 28, 3            |
| B    | 30     | 30, 6, 4, 1      |
| C    | 32     | 32, 22, 2, 1     |

Each step: output = lowest bit of state;
feedback = XOR of state bit (t-1) for each tap t;
state = (state >> 1) | (feedback << (length-1)).

Combiner per time step: `z = B if A == 1 else C`.
`stage1_keystream.txt` holds z for the first 320 steps.

`K1 = SHA256( seedA(4 bytes BE) || seedB(4 bytes BE) || seedC(4 bytes BE) )`

## Lock 2: the seal
`stage2.bin` is XORed with the stream
`SHA256(K1 || i)` for i = 0, 1, 2, ... (i is an 8-byte big-endian counter, blocks concatenated).
Decrypted, it is JSON. What you do with it is up to you.
The secret you are after is a 128-bit integer.

## Lock 3: the flag
`K2` = that 128-bit integer as 16 bytes, big-endian.
`final.bin` is XORed with the same SHA256-counter stream, keyed by
`SHA256( K1 || K2 || "final" )`.

## Rules
Any tools are allowed, including AI. A correct flag is the only proof.
