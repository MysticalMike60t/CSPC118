delimiter = "\x1b[38;5;218m>\x1b[0m  "


def ask(question: str) -> None:
    print(f"{delimiter}{question}")
