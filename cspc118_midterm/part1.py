# /// script
# requires-python = ">=3.14"
# dependencies = []
# ///


def convert_to_kelvin(f: float) -> float:
    return (f + 459.67) * (5 / 9)


def main() -> None:
    temp_fahrenheit: float = float(
        input("What temperature is it in Fahrenheit? \x1b[36m")
    )
    temp_kelvin: float = convert_to_kelvin(temp_fahrenheit)

    print(f"Temperature in Kelvin: {int(temp_kelvin)} K")

    if temp_kelvin < 250.0:
        print("\x1b[0mBrrrrrrr")
    elif temp_kelvin > 290.0:
        print("\x1b[0mWarm")


if __name__ == "__main__":
    main()
