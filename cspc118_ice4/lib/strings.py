import re


def check_has_special_chars(string: str) -> bool:
    return bool(re.search(r"[^a-zA-Z0-9]", string))


def has_vowel(string: str) -> bool:
    vowels = "aeiouAEIOU"
    for char in string:
        for vowel in vowels:
            if char.find(vowel) >= 0:
                return True
    return False


def has_char(string: str, char: str) -> bool:
    match string.find(char):
        case int(n) if n >= 0:
            return True
        case _:
            return False
