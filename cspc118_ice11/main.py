# /// script
# requires-python = ">=3.14"
# dependencies = []
# ///

# Caden Finkelstein
# CSPC118

import sys


def main() -> int:
    word: str = input("Enter a string: \x1b[35m")
    if word == word[::-1]:
        print("\x1b[0mThis word is a palindrome.")
        return 0
    else:
        print("\x1b[0mThis word is not a palindrome")
        return 1


if __name__ == "__main__":
    sys.exit(main())
