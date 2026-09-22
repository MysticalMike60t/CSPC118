# /// script
# requires-python = ">=3.14"
# dependencies = []
# ///

# Caden Finkelstein
# CSPC118

import sys

cadenClasses = ("CPSC118", "CISE120", "COMM122", "GSIS185", "MATH111", "UNIV101")
print(len(cadenClasses))
# cadenClasses.add()
#   AttributeError: 'tuple' object has no attribute 'add'
# cadenClasses.remove()
#   AttributeError: 'tuple' object has no attribute 'remove'


def main() -> int:
    nums: set[str] = set()
    for _ in range(5):
        nums.add(input("Name a lucky number: "))
    print(f"Your lucky numbers are: {nums}")
    print(f"You entered {len(nums)} different numbers.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
