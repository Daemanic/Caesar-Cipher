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

## [2] Expected letter frequencies

An expected frequency is an estimate of how often a letter appears in typical english writing.

The exact frequencies vary according to the text. A novel, a technical document, a short message, and a piece of source code may have different distributions.

| Letter | Approximate frequency |
|---|---:|
| E | 12.70% |
| T | 9.06% |
| A | 8.17% |
| O | 7.51% |
| I | 6.97% |
| N | 6.75% |
| S | 6.33% |
| H | 6.09% |
| R | 5.99% |
| D | 4.25% |


The projects `FREQ` dictionary stores the expected percentage for each english letter. The scoring function uses these values to compare a candidate against the references distribution.

---