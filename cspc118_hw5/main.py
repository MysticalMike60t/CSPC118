# /// script
# requires-python = ">=3.14"
# dependencies = []
# ///

# Caden Finkelstein
# CSPC118

# I decided to make my code much simpler, since I kinda got bored of making it WAY too complex, lol.
# P.S. - Its also because I'm doing this at 5am on a Thursday night :)

import random
import sys


def prob_sep(num: int) -> None:
    print(f"***************Problem{num}*****************************")


# I just made first parameter a boolean cause I don't want to write a whole class or type for it
def num_expand_step(even: bool, start: int, stop: int) -> list[int]:
    _: int = 2 if even else 1
    return list(range(start, stop + _, 2))


def main() -> int:
    # Part 1
    prob_sep(1)
    for _ in num_expand_step(False, 2, 10):
        print(f"{_}")

    # Part 2
    prob_sep(2)
    for _ in num_expand_step(False, 1, 99):
        print(f"{_}")

    # Part 3
    prob_sep(3)
    _min: int = 2
    _max: int = 10
    _i: int = _min
    while _i < (_max + 2):
        print(_i) if (_i >= _min and not _i % 2) or (
            _i <= _max and not _i % 2
        ) else next
        _i += 1

    # Part 4
    prob_sep(4)
    _min: int = 5
    _max: int = 11
    _i: int = _min
    while _i < (_max + 2):
        print(_i) if (_i >= _min and _i % 2) or (_i <= _max and _i % 2) else next
        _i += 1

    # Part 5
    prob_sep(5)
    for _ in reversed(range(1, (10 + 1), 1)):
        print(_)

    # Part 6
    prob_sep(6)
    _i: int = 100
    while _i >= 0:
        print(_i)
        _i -= 25

    # Part 7
    prob_sep(7)
    groceries = ["milk", "cookies", "bread", "soup"]
    for _ in groceries:
        print(_)

    # Part 8
    prob_sep(8)
    threats = ("DDoS", "Phishing", "Malware", "Virus")
    for _ in threats:
        print(_)

    # Part 9
    prob_sep(9)
    _input: str = input("Enter a word: ").strip()
    for _ in _input:
        print(_)

    # Part 10
    prob_sep(10)
    _input: int = int(input("Enter the step amount: ").strip())
    for _ in range(1, (10 + 1), _input):
        print(_)

    # Part 11
    prob_sep(11)
    _low: int = int(input("Enter the low number: ").strip())
    _high: int = int(input("Enter the high number: ").strip())
    for _ in range(_low, (_high + 1)):
        print(_)

    # Part 12
    prob_sep(12)
    while input("Guess the secret word: ").strip() != "python":
        print("No. Try again. (Hint: a snake and programming language.)")
    print("You guessed the secret word.")

    # Part 13
    prob_sep(13)
    while input("Guess the secret word: ").strip().lower() != "python":
        print("No. Try again. (Hint: a snake and programming language.)")
    print("You guessed the secret word.")

    # Part 14
    prob_sep(14)
    while int(input("Guess the number: ").strip()) != int(random.randrange(1, 10)):
        print("Try again.")
    print("You guessed the number.")

    # Part 15
    prob_sep(15)
    _val = 0
    while _val <= 100:
        _ = int(input("Enter a number: "))
        _val += _
    print(f"Total = {_val}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
