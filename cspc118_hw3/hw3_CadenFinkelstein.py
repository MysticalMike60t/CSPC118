# /// script
# requires-python = ">=3.14"
# dependencies = []
# ///

# Caden Finkelstein
# CSPC118

import math
import sys


def sep(n: int) -> None:
    print(f"=================Problem {n!s} ===============")


def main() -> int:
    # Part 1
    sep(1)
    donor: str = input("Enter donor blood type (O, A, B, AB): ")
    patient: str = input("Enter recipient blood type (O, A, B, AB): ")
    match donor.upper():
        case "O":
            print("The match works.")
        case _ if patient == "AB":
            print("The match works.")
        case b if b == patient:
            print("The match works.")
        case _:
            print("The match doesn't work.")

    # Part 2
    sep(2)
    health: int = int(input("What is your current health level? "))
    damage: int = int(input("How much damage did the monster do? "))
    if (health - damage) > 0:
        print(f"Your character is still alive with a health of {health}.")
    else:
        print("Game Over")

    # Part 3
    sep(3)
    web_vis = [25, 60, 10, 15, 16, 34, 50]
    print(f"The website has been online {len(web_vis)} days.")
    print(f"There were {min(web_vis)} visitors on our slowest day.")
    print(f"There were {max(web_vis)} visitors on our busiest day.")

    # Part 4
    sep(4)
    print(f"The ladder reaches height of {5 * math.sin(45 * math.pi / 180)} feet.")

    # Extra Credit
    print("================= EXTRA CREDIT ===============")
    x: int = int(input("Enter the x coordinate:"))
    y: int = int(input("Enter the y coordinate:"))
    if math.sqrt(x**2 + y**2) <= 10:
        print("The dart hits the board")
    else:
        print("The dart misses the board")

    return 0


if __name__ == "__main__":
    sys.exit(main())
