import cmath
import math


def quadratic(a: int, b: int, c: int) -> dict[str, float]:
    def calc_pos(sqrt_d: complex) -> complex:
        return (-b + sqrt_d) / (2 * a)

    def calc_neg(sqrt_d: complex) -> complex:
        return (-b - sqrt_d) / (2 * a)

    d: int = b**2 - 4 * a * c
    sqrt_d: complex = math.sqrt(d) if d >= 0 else cmath.sqrt(d)
    roots: dict[
        str, float
    ] = {  # I set keys to strings just because they need to be 1 & 2 and not 0 & 1, but also for readability/understanding
        "1": round(float(calc_pos(sqrt_d).real), 1),
        "2": round(float(calc_neg(sqrt_d).real), 1),
    }
    return roots
