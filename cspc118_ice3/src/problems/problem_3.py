from lib.classes import ExitCode


def handle_operation(operation_type: str, num_1: float, num_2: float):
    match operation_type:
        case "a":
            return num_1 + num_2
        case "s":
            return num_1 - num_2
        case "m":
            return num_1 * num_2
        case "d":
            return num_1 / num_2
        case _:
            return float(0)  # To make it not return with a Literal type.


def run() -> int:
    num_1: float = float(input("Enter first numeric value: "))
    num_2: float = float(input("Enter second numeric value: "))
    operation_type: str = input("Enter operation type [a|s|m|d]: ")
    while operation_type not in ("a", "s", "m", "d"):
        operation_type: str = input("Invalid, enter [a|s|m|d]: ")
    operation_result: float = handle_operation(operation_type, num_1, num_2)
    print(rf"Result: {operation_result}")
    return ExitCode.OK
