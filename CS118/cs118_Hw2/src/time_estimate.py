from dataclasses import dataclass, field

from lib import question


@dataclass
class InputState:
    study: int = 0
    sleep: int = 0
    eat: int = 0


@dataclass
class InitState:
    hours_in_day: int = 24  # Obviously
    input: InputState = field(default_factory=InputState)
    hours_to_play: int = hours_in_day - (
        InputState.study + InputState.sleep + InputState.eat
    )


def init_state() -> InitState:
    return InitState()


def ask_hours() -> int:
    state: InitState = init_state()
    state.input.study = (
        int(input(f"{question.delimiter}How many hours do you plan to study? : ")) or 0
    )
    state.input.sleep = (
        int(input(f"{question.delimiter}How many hours do you plan to sleep? : ")) or 0
    )
    state.input.eat = (
        int(input(f"{question.delimiter}How many hours do you plan to eat? : ")) or 0
    )
    print(f"You have \x1b[1;34m{state.hours_to_play!s}\x1b[0m hours left to play")
    return 0
