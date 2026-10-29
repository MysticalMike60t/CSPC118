# /// script
# requires-python = ">=3.14"
# dependencies = []
# ///

# Caden Finkelstein
# CSPC118

import random
import sys

DATA_STORE = {
    "user": {"score": 0},
    "computer": {"score": 0},
    "total": {"ties": 0, "rounds": 1},
}


def check_choice(choices: list[str], user_input: str) -> int:
    for choice in choices:
        if user_input == choice:
            return choices.index(choice)
    return -1


def get_winner(user_choice: int, computer_choice: int) -> int:
    match user_choice:
        case c if c == computer_choice:
            return 0
        case c if c == computer_choice + 1 or c == computer_choice - 2:
            return 1
        case c if c == computer_choice - 1 or c == computer_choice + 2:
            return 2
        case _:
            return 0


def display_leaderboard() -> None:
    print(
        f"Score -> You: \x1b[35m{DATA_STORE['user']['score']}\x1b[0m | Computer: \x1b[35m{DATA_STORE['computer']['score']}\x1b[0m | Ties: \x1b[35m{DATA_STORE['total']['ties']}\x1b[0m"
    )


def main() -> None:
    #                       0        1         2
    choices: list[str] = ["rock", "paper", "scissors"]
    play: bool = True
    while play:
        print(f"\nRound \x1b[35m{DATA_STORE['total']['rounds']}\x1b[0m")
        user_input: str = input(
            "\x1b[36mPick rock\x1b[0m, \x1b[36mpaper\x1b[0m, or \x1b[36mscissors\x1b[0m (or \x1b[36m'q'\x1b[0m to quit): \x1b[34m"
        ).lower()
        print("\x1b[0m")
        if user_input.lower() == "q":
            print("\x1b[92mThanks for playing!\x1b[0m")
            play = False
        else:
            validation: int = check_choice(choices, user_input)
            computer_choice: int = random.randint(0, len(choices) - 1)

            if validation != -1:
                print(f"Computer choice: \x1b[36m{choices[computer_choice]}\x1b[0m")
            else:
                print("\x1b[31mInvalid choice. Please try again.\x1b[0m")
                continue

            winner: int = get_winner(validation, computer_choice)
            match winner:
                case 1:
                    DATA_STORE["user"]["score"] += 1
                    print("\x1b[32mYou win this round!\x1b[0m")
                case 2:
                    DATA_STORE["computer"]["score"] += 1
                    print("\x1b[31mComputer wins this round!\x1b[0m")
                case _:
                    DATA_STORE["total"]["ties"] += 1
                    print("\x1b[35mTie!\x1b[0m")

        display_leaderboard()

        DATA_STORE["total"]["rounds"] += 1


if __name__ == "__main__":
    sys.exit(main())
