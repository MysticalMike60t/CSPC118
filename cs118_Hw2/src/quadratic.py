from lib import calc, display


def find_roots() -> int:
    display.quadratic_formula()  # Added this for the coolness factor :3
    display.quadratic_equation()
    # ax² – bx – c = 0
    quadratic_eq_result = calc.quadratic(2, 8, 24)
    print(
        f"\nThe roots are: \x1b[1;34m{quadratic_eq_result['1']}\x1b[0m and \x1b[1;34m{quadratic_eq_result['2']}\x1b[0m"
    )
    return 0
