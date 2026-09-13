# I did not put much work into the function and variable names, so they may be a little weird.

import sys

from lib.cli import tui


def box(x: int, y: int, z: int) -> int:
    v: int = x * z * y
    s: int = 2 * ((x * z) + (x * y) + (z * y))
    print(
        f"\x1b[1;95m1.\x1b[0m \x1b[1;34mBox Dimensions\x1b[0m: \x1b[35ml\x1b[0m=\x1b[36m{x}\x1b[0m \x1b[35mw\x1b[0m=\x1b[36m{z}\x1b[0m \x1b[35mh\x1b[0m=\x1b[36m{y}\x1b[0m"
    )
    print(f"\x1b[35m>\x1b[0m\tVolume: \x1b[36m{v}\x1b[0m")
    print(f"\x1b[35m>\x1b[0m\tSurface Area: \x1b[36m{s}\x1b[0m")
    return 0


def calc_max_cap(m_cap: float, f_s: float) -> int:
    return int((m_cap / f_s).real)


def temp_conv(f: float) -> float:
    return (f - 32) * 5 / 9


def temp_tui() -> int:
    f: float = float(
        input(
            "\x1b[1;95m4.\x1b[0m Please enter a temperature in \x1b[35mFahrenheit\x1b[0m to convert to \x1b[35mCelsius\x1b[0m: \x1b[96m"
        )
    )
    print(
        f"\x1b[35m>\x1b[0m\t\x1b[96m{int(f)}\x1b[0m°\x1b[35mF\x1b[0m \x1b[33m==\x1b[0m \x1b[36m{round(temp_conv(f))}\x1b[0m°\x1b[35mC\x1b[0m"
    )
    return 0


def main() -> int:
    usb_cap_gb: float = 8
    usb_cap_mb: float = 8000

    print("\n")
    match box(3, 5, 8):
        case 0:
            pass
        case _:
            print("\x1b[31mFailed to run box calculations.\x1b[0m")
    tui.separator()
    # For all size calculations, I only used base10. Since you didn't ask for binary too.
    print(
        f"\x1b[1;95m2.\x1b[0m You have room for \x1b[36m{calc_max_cap(usb_cap_gb, 1.5)}\x1b[0m movies."
    )
    tui.separator()
    print(
        f"\x1b[1;95m2.\x1b[0m You have room for \x1b[36m{calc_max_cap(usb_cap_mb, 4)}\x1b[0m songs."
    )
    tui.separator()
    match temp_tui():
        case 0:
            pass
        case _:
            print("\x1b[31mFailed to run temperature conversion.\x1b[0m")
    tui.separator()
    print("\x1b[1;32mDone.\x1b[0m\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
