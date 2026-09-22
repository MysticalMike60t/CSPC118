# /// script
# requires-python = ">=3.14"
# dependencies = []
# ///


import sys


def part1() -> None:
    _n: int = int(input("Enter a number: "))
    _i: int = 1
    while _i <= _n:
        print("Howdy!!!")
        _i += 1


def part2() -> None:
    days = (
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    )
    for _ in days:
        print(f"{_[:3]}")


def part3() -> None:
    _n: int = int(input("Enter a number: "))

    _f: int = 1
    for _i in range(1, _n + 1):
        _f *= _i

    print(f"The factorial of {_n} is {_f}")


def main() -> int:
    part1()
    part2()
    part3()
    return 0


if __name__ == "__main__":
    sys.exit(main())
