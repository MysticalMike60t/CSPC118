from dataclasses import dataclass

from data import hackingAttemptsPerDay


@dataclass
class Analysis:
    smallest: int = min(hackingAttemptsPerDay)
    largest: int = max(hackingAttemptsPerDay)
    sum: int = sum(hackingAttemptsPerDay)


def stats() -> int:
    print(
        f"There were \x1b[1;34m{Analysis.smallest!s}\x1b[0m hacking attempts on the \x1b[1;35mbest day\x1b[0m"
    )
    print(
        f"There were \x1b[1;34m{Analysis.largest!s}\x1b[0m hacking attempts on the \x1b[1;35mworst day\x1b[0m"
    )
    print(
        f"There were \x1b[1;34m{Analysis.sum!s}\x1b[0m hacking attempts \x1b[1;35moverall\x1b[0m"
    )
    return 0
