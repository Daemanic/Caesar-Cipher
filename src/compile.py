def caesar_cipher(text: str, shift: int) -> str:
    result = []
    shift = shift % 26

    for char in text:
        if "A" <= char <= "Z":
            position = ord(char) - ord("A")
            new_position = (position + shift) % 26
            result.append(chr(new_position + ord("A")))
        elif "a" <= char <= "z":
            position = ord(char) - ord("a")
            new_position = (position + shift) % 26
            result.append(chr(new_position + ord("a")))
        else:
            result.append(char)
    return "".join(result)

def encrypt(text: str, shift: int) -> str:
    return caesar_cipher(text, shift)

def decrypt(text: str, shift: int) -> str:
    return caesar_cipher(text, -shift)