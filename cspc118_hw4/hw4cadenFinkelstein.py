# /// script
# requires-python = ">=3.14"
# dependencies = []
# ///


# Caden Finkelstein
# CSPC118

import sys


def main() -> int:
    # Part 1
    start = 6
    stop = 20
    for _n in range(start, (stop + 2), 2):
        print(_n)

    # Part 2
    init_infected: int = 1
    mult: int = 3
    track_hrs: int = int(
        input("How many hours do you want to track the computer virus?: ")
    )

    for _n in range(track_hrs):
        print(
            f"Hour {_n + 1} - {init_infected * (pow(mult, _n))} computers infected"
        )  # Power of 4:30am 'genius' math

    # Part 3
    max: int = 50
    exp: int = 2
    for _n in range(max):
        print(f"{_n} squared = {pow(_n, exp)}")

    # Part 4
    temperature: int = int(
        input("What is the temperature (°F)?: ")
    )  # Named full word since "temp" could be perceived as a non-important var, lol
    match temperature:
        case _t if _t <= 30:
            print("You may need to deice the plane")
        case _t if _t >= 110:
            print("Too hot to take off")
        case _:
            print("Ready for take off")

    return 0


if __name__ == "__main__":
    sys.exit(main())
