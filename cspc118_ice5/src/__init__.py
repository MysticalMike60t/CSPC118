# I did not include much input validation to save time, since it would take a LOT longer.

import sys

from lib.classes import ExitCode
from lib.strings import has_char, has_vowel


def main() -> int:
    phrase: str = input("Input a phrase: ")
    print(rf"Capitalized: {phrase.capitalize()}")
    print(rf"Uppercase: {phrase.upper()}")
    print(rf"Lowercase: {phrase.lower()}")
    if has_char(phrase.lower(), "z"):
        print("Your phrase contains the letter z.")
    else:
        print("Your phrase does not contain the letter z.")
    if has_vowel(phrase):
        print(r"Your phrase contains a vowel.")
    else:
        print(r"Your phrase does not contain a vowel.")
    return ExitCode.OK


if __name__ == "__main__":
    sys.exit(main())
