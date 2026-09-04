# Caden Finkelstein
#
# This uses some 256-bit colors.

import sys
from html import escape

# I namespaced these for readability since direct calls were too generic.
import favorite_foods
import hacking_attempts
import quadratic
import time_estimate


def print_problem_seperator(number: int) -> None:
    # 48;5;234 (nice background color)
    bg_color = ""

    def escape_colors(value: str) -> str:
        if len(bg_color) >= 1:
            has_bg = True
        else:
            has_bg = False
        return f"{value}{';' if has_bg else ''}{bg_color}"

    line_color = escape_colors("38;5;38")
    title_color = escape_colors("38;5;33")
    value_color = escape_colors("38;5;177")
    print(
        f"\x1b[{line_color}m****************\x1b[0m\x1b[{line_color}m \x1b[0m\x1b[{title_color}mProblem\x1b[0m\x1b[{line_color}m \x1b[0m\x1b[{value_color}m{number}\x1b[0m\x1b[{line_color}m \x1b[0m\x1b[{line_color}m****************\x1b[0m"
    )


def main() -> int:
    print("\x1b[1;38;5;8mMade by: \x1b[0m\x1b[3;38;5;218mCaden Finkelstein\x1b[0m")

    def print_error(origin: str, exit_code: int) -> None:
        print(f"\x1b[1;31mError from '{origin}' with code {exit_code!s}.\x1b[0m")

    print_problem_seperator(1)

    fav_food_ask_exit_code: int = favorite_foods.ask()
    if fav_food_ask_exit_code >= 1:
        print_error("ask()", fav_food_ask_exit_code)  # ooooooooo prettyyyy
        return 1

    print_problem_seperator(2)

    hack_attempt_stats_exit_code: int = hacking_attempts.stats()
    if hack_attempt_stats_exit_code >= 1:
        print_error("stats()", hack_attempt_stats_exit_code)  # ooooooooo prettyyyy
        return 1

    print_problem_seperator(3)

    study_ask_hours_exit_code: int = time_estimate.ask_hours()
    if study_ask_hours_exit_code >= 1:
        print_error("ask_hours()", study_ask_hours_exit_code)  # ooooooooo prettyyyy
        return 1

    print_problem_seperator(4)

    quadratic_find_roots_exit_code: int = quadratic.find_roots()
    if quadratic_find_roots_exit_code >= 1:
        print_error(
            "find_roots()", quadratic_find_roots_exit_code
        )  # ooooooooo prettyyyy
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
