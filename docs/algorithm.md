# Caesar Cipher Algorithm

## 0. Overview

A caesar cipher is a simple substitution copher that encrypts text by shifting each english letter by a fixed number of positions in the alphabet.

For example, with a shift of `three`:
- `A` becomes `D`
- `B` becomes `E`
- `C` becomes `F`

This project supports three operations:
- Encrypt: shifts letters forward.
- Decrypt: shifts letters backward using the known key.
- Crack: tries all possible shifts and rank the results candidates using letter-frequency analysis.

The core cipher implementation is in: [`src/compile.py`](../src/compile.py), while the CLI workflow is handled by [`src/cli.py`](../src/cli.py)

---

## 1. Alphabet Representation

The english alphabet contains 26 letters. To perform calculatons, each letter is represented by a number from `0` to `25`.

| Letter | Value |
|---|---:|
| A | 0 |
| B | 1 |
| C | 2 |
| ... | ... |
| X | 23 |
| Y | 24 |
| Z | 25 |

Using zero-based positions make it easier to calculate shifts.

For example, `H = 7` and with a shfit of `3`, its new position is `10` which corresponds to `K`.

---
