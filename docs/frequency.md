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

## [3] Counting occurrences

Pythons `collections.Counter` counts how many times each item appears in the iterable.

```python
from collections import Counter

text = 'banana'
counts = Counter(text)

print(counts)
```

```python
output:
{
    'b': 1,
    'a': 3,
    'n': 2
}
```

This is useful because the scoring algorithm needs to observe count of each letter in a candidate.

Before counting, the project filters out characters that are not english letters and converts uppercase letters to lowercase.

**Conceptually:**
```python
text = 'hello, world!'

letters = [
    char.lower()
    for char in text
    if 'a' <= char.lower() <= 'z'
]
```

The resulting list contains only the english letters, in lowercase. Extra stuffs; spaces, digits, and punctuations do not contribute to the frequency score.

---

## [4] Observing Expected Counts

The score function compares two quantities:

- Observed count: how many times a letter actually appears in the candidate.
- Expected count: how many times that letter would be expected to appear according to the reference frequencies.

The expected count calculation:

\[
    E_i = /frac{N /times p_i}{100}
]

- \(E_i\): the expected count for letter \(i\).
- \(p_i\): expected frequency percentage for that letter.
- \(N\): the total number of english letters in the candidate.

If the expected frequency of `E` is `12.70%` in a candidate containing `100` english letters:
```text
Expected E count = 100 x 12.70 / 100
                 = 12.7
```

So, if the candidate contains `13` instances of `E`, its observed count is close to the expected count.

If it contains no instances of `E`, the observed count differs more substantially from the expected count.

One letter alone is not enough to judge a candidate, so the program compares all `26` letters.

---
