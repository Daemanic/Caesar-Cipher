# Caesar Cipher Algorithm

## [0] Introduction

A caesar cipher is a simple substitution copher that encrypts text by shifting each english letter by a fixed number of positions in the alphabet.

For example, with a shift of `3`:
- `A` becomes `D`
- `B` becomes `E`
- `C` becomes `F`

This project supports three operations:
- Encrypt: shifts letters forward.
- Decrypt: shifts letters backward using the known key.
- Crack: tries all possible shifts and rank the results candidates using letter-frequency analysis.

The core cipher implementation is in: [`src/compile.py`](../src/compile.py), while the CLI workflow is handled by [`src/cli.py`](../src/cli.py)

---

## [1] Alphabet Representation

The english alphabet contains `26` letters. To perform calculatons, each letter is represented by a number from `0` to `25`.

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

## [2] Encryption

Encryption shifts each uppercase or lowercase letter forward by the specified key.

Used formulation:

\[
    E(x) = (x + k) \bmod 26
]

- `k`: the shift requested.
- `x`: the original letters position.
- `E(x)`: the encrypted letters position.
- `26`: the total number of letters in the alphabet.

The modulo operation (`%`) makes sure that the positions wrap around when they reach the end of the alphabet.

For example, if `X = 23` is shifted by `5` then it goes off the `26` letter alphabet limit, so just like a clock (where 1 comes after 12 instead of 13), the new position will be `2` which corresponds to `C`.

### [~] Process Implemented

1. Receive the input text and shift key.
2. Normalize the key using modulo (`%26`).
3. Process the text one character at a time.
4. If the character is an uppercase letter, calculate its position relative to `A`.
5. If it is a lowercase letter, calculate its position relative to `a`.
6. Add the shift key and apply module (`%26`).
7. Conver the new position back into a character.
8. Leave characters outside `A-Z` and `a-z` unchanged.
9. Join the resulting characters and return the ciphertext.

> Note: the spaces, comma, and exclamation mark remain unchanged.

---

## [3] Decryption

It basically reverses the encryption shift (opposite of above).

Used Formulation:

\[
    D(x) = (x - k) \bmod 26
]

- `k`: original encryption key.
- `x`: the cipher letters position.
- `D(x)`: decrypted letters position.

### [~] -ve Shift Reason

The project reuses the same core function for encryption and decryption. Instead of creating a separate letter-shifting algorithm, the decryption function passes the negative of the key to the core function.

```python
def encrypt(text, shift):
    return caesar_cipher(text, shift)

def decrypt(text, shift):
    return caesar_cipher(text, -shift)
```

> Note: this makes the code simpler by repetitive logic.

---

## [4] Cracking Cipher

The attempt to recover the original plaintext without being given the encryption key. A caesar cipher has only `26` distinct shifts, so the program can test every possible key.

### [~] Process Implemented

1. Receive the ciphertext.
2. Generate a candidate by trying a possible decryption shift.
3. Repeat for shifts `0` through `25`.
4. Calculate a frequency score for each candidate.
5. Sort candidates by score, from lowest to highest.
6. Display the requested number of top-ranked candidates.

> Note: the program does not automatically know what is the correct answer, so it uses [`frequency analysis`](./frequency.md) to estimate which candidates look most like english text.

---

## [5] Workflow

```text
    user runs a command
            |
            v
    parse command-line args
            |
            v
    validate requested operation
            |
            v
    read text provided (arg, file, or input)
            |
            v
    choose the operation (encrypt, decrypt, or crack)
            |
            v
    according to the operation, perform task
            |
            v
    output result or store in file
```