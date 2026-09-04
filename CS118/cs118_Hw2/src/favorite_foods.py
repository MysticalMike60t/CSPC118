from dataclasses import dataclass, field

from data import favorite_foods
from lib import question

# Just type declarations because why not, lol
type FavoriteFoods = int


# I love complicating things :3
@dataclass
class InputState:
    tmp: str = ""
    tmp_len: int = 0
    list: list[str] = field(default_factory=list)


@dataclass
class InitState:
    input: InputState = field(default_factory=InputState)


def init_state() -> InitState:
    return InitState()


def ask() -> FavoriteFoods:
    state: InitState = init_state()  # Cosplaying React fr
    while True:
        state.input.tmp = str(
            input(f"{question.delimiter}What is your favorite food? ")
        )
        state.input.tmp_len = len(state.input.tmp)
        state.input.list.append(state.input.tmp)
        if state.input.tmp_len <= 0:
            print(f"\x1b[1;31mInput '{state.input.tmp}' is invalid.\x1b[0m")
            print("Stupid...")  # Necessary user discipline
            break
        if state.input.tmp:
            break
        # I could have made the modification of the list better, but it is unnecessary for this.
        favorite_foods[1] = "steak"
        print(f"{favorite_foods!s}")
    return 0
