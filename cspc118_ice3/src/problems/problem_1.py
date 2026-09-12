from lib.classes import ExitCode


def run() -> int:
    # I use float type 2 times, because the first indicates
    #   that the variable can only be a float, and the
    #   second is to convert the input to a float. It just
    #   helps with understanding the code, and minimizing
    #   potential development issues/misunderstandings.
    float_1: float = float(input("Please enter float #1: "))
    float_2: float = float(input("Please enter float #2: "))

    match float_1:
        case float(f) if float_1 >= float_2:
            print(rf"The first number ( {f} ) you entered is larger")
        case float(f) if float_1 <= float_2:
            print(rf"The first number ( {f} ) you entered is smaller")
        case _:
            print(
                rf"What happened??????\nYour input: ( Float #1 = {float_1}, Float #2 = {float_2} )"
            )
            return ExitCode.ERR

    return ExitCode.OK
