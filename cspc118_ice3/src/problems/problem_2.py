from lib.classes import ExitCode


def calc_max(f1: float, f2: float, f3: float):
    arr: list[float] = [f1, f2, f3]

    match float(max(arr)):
        case float(f) if f == f1:
            return "first"
        case float(f) if f == f2:
            return "second"
        case float(f) if f == f3:
            return "third"
        case _:
            print("Invalid input, failed to calculate.")
            return "float"


def run() -> int:

    # I use float type 2 times, because the first indicates
    #   that the variable can only be a float, and the
    #   second is to convert the input to a float. It just
    #   helps with understanding the code, and minimizing
    #   potential development issues/misunderstandings.
    float_1: float = float(input("Please enter float #1: "))
    float_2: float = float(input("Please enter float #2: "))
    float_3: float = float(input("Please enter float #3: "))

    print(
        rf"The {calc_max(float_1, float_2, float_3)} number you entered is the largest."
    )

    return ExitCode.OK
