# Letter Frequency Analysis

## [0] Introduction

Frequency analysis is a technique used to study how often letters appear in a piece of text.
In english, letters do not appear equally often. E.g: `E`, `T`, and `A` are generally more common than `Z`, `Q`, and `X`.

A caesar cipher preserves the number of occurrences of each letter, but changes which letters those occurences belong to. This means letter frequency patterns cab help identify a likely decryption.

In this project, frequency analysis is used to rank possible plaintext candidates when cracking a caesar cipher using [scoring](../src/scoring.py).

---

## [1] Frequency importance

```text
THE HELLO WORLD TEXT
```

The letter `T` appear more than once, and so does `E`. Other letters appear less frequently.
If the sentence is encrypted using a caesar cipher, every occurence of a particular letter is shifted to the same new letter.
The original frequencies are not lost, Instead, thye are associated with different letters.

By comparing a decrypted candidate with typical english letter frequencies, the program can estimate whether that candidate is plausible english text.

---

## [2] Expected letter frequencies

An expected frequency is an estimate of how often a letter appears in typical english writing.

The exact frequencies vary according to the text. A novel, a technical document, a short message, and a piece of source code may have different distributions.

| Letter | Frequency (Aprox.) |
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

Pythons `collections.Counter` function counts how many times each item appears in the iterable.

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
\]

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

## [5] Frequency Mechanism

The project uses a `chi-square-style` score to measure the difference between observed and expected letter counts.

Contribution per letter:

\[
\frac{(0_i - E_i)^2{E_i}}
\]

Sum of contribution:

\[
\chi^2 = \sum_{i=1}^{26}
\frac{(0_i - E_i)^2}{E_i}
\]

- \(0_i\): the observed count of letter.
- \(E_i\): its expected count.
- The sum covers all `26` english letters.

The score measures how far the observed distribution differs from the expected distrbution.

**Interpretation:**
For this implementation, a lower score generally indicates that the candidates letter counts are closer to the reference frequencies.
Whereas, a higher score indicates a greater difference.

The score is a ranking heuristic, not a percentage probability that the candidate is correct.

**Simplified Example:**
```python
observed = 13
expected = 12.7

difference = observed - expected
contribution = difference ** 2 / expected
print(contribution)
```
The result is a small contribution because the observed and expected counts are close.
The complete scoring function repeats this calculation for every letter and adds the contributions together.

---

## [6] Candidates Ranking

The cracking workflow generates one candidate for every possible decryption shift and calcualtes its frequency score.

**Conceptually:**
```python
candidates = []

for shift in range(26):
    candidate = decrypt(ciphertext, shift)
    score = frequency_score(candidate)

    candidates.append((score, shift, candidate))

candidates.sort(key=lambda item: item[0])
```

1. Its frequency score.
2. The decryption shift used.
3. The resulting candidate text.

The candidates are sorted by score in ascending order, placing the lowest-scoring candidates first

According to the users request, the program then displays the top candidates. For example: if five candidates was requested, the program displays the first five entries after sorting.

This process is called ranking, not guaranteed decryption. The program estimates which result is most plausible rather than proving which result is the original message.

---

## [7] Possible Scenario

**What if there are no letters?**

Punctuation-only text, digits, or any empty string do not privde useful letter-frequency information.
So, the projects scoring function returns positive infinity in this such situation:

```python
if not letters:
    return float("inf")
```

Positive infinity is used as a very poor score. When candidates are sorted in ascending order, a candidate with this score will normally appear after candidates with finite scores.

This prevents text with no english letters from receiving an artificially good score.

---

## [8] Summarization

1. Receive a candidate plaintext.
2. Keep english letters and convert them to lowercase.
3. Count the occurences of each letter using `Counter()`.
4. Calculate expected counts from the reference frequencies.
5. Compare observed and expected counts using a `chi-squared` formula.
6. Return the total score.
7. Use the score to rank candidate decryptions.

The frequency score helps the cracking algorithm choose promising results, but it does not guarantee that the highest-ranked result is correct.
