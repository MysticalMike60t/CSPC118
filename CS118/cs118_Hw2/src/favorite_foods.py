from dataclasses import dataclass, field

from lib.strings import check_has_special_chars
from lib.types import FavList

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


def favorite_foods() -> FavoriteFoods:
    state: InitState = init_state()
    while True:
        state.input.tmp = input("Enter your favorite food:")
        state.input.tmp_len = len(state.input.tmp)
        state.input.list.append(state.input.tmp)
        if state.input.tmp_len <= 0 or not check_has_special_chars(state.input.tmp):
            print(rf"Input '{state.input.tmp}' is invalid.")
            print("Stupid...")
            break
        if state.input.tmp:
            break
    return 0
