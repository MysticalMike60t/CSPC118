import sys

import matplotlib.pyplot as plt


def main() -> int:
    _, ax = plt.subplots()
    ax.set_title("Average Temperature in Prescott January-December")
    ax.set_xlabel("Month")
    ax.set_ylabel("Temperature °F")
    ax.plot(
        [
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May",
            "Jun",
            "Jul",
            "Aug",
            "Sep",
            "Oct",
            "Nov",
            "Dec",
        ],
        [51, 54, 61, 68, 76, 88, 90, 87, 83, 72, 61, 52],
    )
    plt.show()
    return 0


if __name__ == "__main__":
    sys.exit(main())
