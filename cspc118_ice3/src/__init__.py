# I did not include much input validation to save time, since it would take a LOT longer.

import sys

from lib.classes import ExitCode
from problems import problem_1, problem_2, problem_3, problem_4


def main() -> int:

    match problem_1.run():
        case ExitCode.OK:
            print("Problem #1 complete!")
        case _:
            print("Problem #1 failed...")

    match problem_2.run():
        case ExitCode.OK:
            print("Problem #2 complete!")
        case _:
            print("Problem #2 failed...")

    match problem_3.run():
        case ExitCode.OK:
            print("Problem #3 complete!")
        case _:
            print("Problem #3 failed...")

    match problem_4.run():
        case ExitCode.OK:
            print("Problem #4 complete!")
        case _:
            print("Problem #4 failed...")

    return ExitCode.OK


if __name__ == "__main__":
    sys.exit(main())
