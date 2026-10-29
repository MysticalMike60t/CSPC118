# /// script
# requires-python = ">=3.14"
# dependencies = []
# ///

# Caden Finkelstein

import sys


def main() -> int:
    age: int = int(input("How old are you? "))
    if age < 18:
        print("You are too young to vote.")
    elif 55 <= age:
        print("You are eligible to receive the senior citizen discount.")
    elif age >= 21:
        print("You are old enough to drink.")
    elif age >= 18:
        print("You are old enough to vote.")

    # Challenge
    day: int = int(input("Enter the day: "))
    month: int = int(input("Enter the month: "))
    year: int = int(input("Enter the 2-digit year: "))

    if day * month == year:
        print("This date is MAGIC :)")
    else:
        print("This date is not MAGIC :(")

    return 0


if __name__ == "__main__":
    sys.exit(main())
