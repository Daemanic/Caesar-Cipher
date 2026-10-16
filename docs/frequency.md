# Letter Frequency Analysis

## [0] Introduction

Frequency analysis is a technique used to study how often letters appear in a piece of text.

In english, letters do not appear equally often. E.g: `E`, `T`, and `A` are generally more common than `Z`, `Q`, and `X`.

A caesar cipher preserves the number of occurrences of each letter, but changes which letters those occurences belong to. This means letter frequency patterns cab help identify a likely decryption.

In this project, frequency analysis is used to rank possible plaintext candidates when cracking a caesar cipher using [scoring](../src/scoring.py).

---

## [1] Frequency importance

```text
THE CAT IS IN THE GARDEN
```

The letter `T` appear more than once, and so does `E`. Other letters appear less frequently.

If the sentence is encrypted using a caesar cipher, every occurence of a particular letter is shifted to the same new letter.

The original frequencies are not lost, Instead, thye are associated with different letters.

By comparing a decrypted candidate with typical english letter frequencies, the program can estimate whether that candidate is plausible english text.

---