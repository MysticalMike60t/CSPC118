# /// script
# requires-python = ">=3.14"
# dependencies = []
# ///


def main() -> None:
    bill: int = int(input("Enter the restaurant bill: \x1b[32m$"))
    rating: int = int(
        input(
            "\x1b[0mEnter the service rating (1 = Poor, 2 = Good, 3 = Great): \x1b[36m"
        )
    )
    tip_percentages: list[int] = [10, 15, 20]

    tip_cost: float = bill * (tip_percentages[rating - 1] / 100)
    total_bill: float = bill + tip_cost

    print(f"\x1b[0mTip: \x1b[32m${tip_cost}0\x1b[0m")
    print(f"Total bill: \x1b[32m${total_bill}0\x1b[0m")


if __name__ == "__main__":
    main()
