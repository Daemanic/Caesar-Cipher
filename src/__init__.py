from __future__ import annotations

def _shift_text(text: str, shift: int) -> str:
    shift %= 26
    result = []
    for char in text:
        if "a" <= char <= "z":
            result.append(chr((ord(char) - ord("a") + shift) % 26 + ord("a")))
        elif "A" <= char <= "Z":
            result.append(chr((ord(char) - ord("A") + shift) % 26 + ord("A")))
        else:
            result.append(char)
    return "".join(result)

def encrypt(text: str, shift: int) -> str:
    return _shift_text(text, shift)

def decrypt(text: str, shift: int) -> str:
    return _shift_text(text, -shift)
