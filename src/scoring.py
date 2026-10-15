from collections import Counter

FREQ = {
    "a": 8.17, "b": 1.49, "c": 2.78, "d": 4.25, "e": 12.70,
    "f": 2.23, "g": 2.02, "h": 6.09, "i": 6.97, "j": 0.15,
    "k": 0.77, "l": 4.03, "m": 2.41, "n": 6.75, "o": 7.51,
    "p": 1.93, "q": 0.10, "r": 5.99, "s": 6.33, "t": 9.06,
    "u": 2.76, "v": 0.98, "w": 2.36, "x": 0.15, "y": 1.97,
    "z": 0.07,
}

def frequency_score(text: str) -> float:
    letters = [c.lower() for c in text if "a" <= c.lower() <= "z"]
    if not letters:
        return float("inf")
    counts = Counter(letters)
    total = len(letters)
    score = 0.0
    for letter, percent in FREQ.items():
        expected = total * percent / 100
        score += (counts.get(letter, 0) - expected) ** 2 / expected
    return score