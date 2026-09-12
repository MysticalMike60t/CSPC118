import sys


def main() -> int:
    # Part 1
    mult: int = int(input("Enter a number: "))
    for _ in range(mult):
        print("Howdy Partner!")
    # Part 2
    for n in range(1000):
        if not (n / 2).is_integer():
            print(n)
    # Part 3 / Challenge
    for h in range(24):
        h = h + 1  # To fix range starting at 0
        print(f"Hour {h} - {pow(2, h - 1):,} bacteria")
    return 0


if __name__ == "__main__":
    sys.exit(main())
