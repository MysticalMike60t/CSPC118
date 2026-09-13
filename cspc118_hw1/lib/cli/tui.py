import os


def separator() -> None:
    print("\x1b[90m-\x1b[0m" * int(os.get_terminal_size().columns))
