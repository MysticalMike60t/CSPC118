# /// script
# requires-python = ">=3.14"
# dependencies = []
# ///

import matplotlib.pyplot as plt


def main() -> None:

    storm = [0.2, 0.5, 1.2, 2.5, 2.7, 1.7]
    x = [0, 1, 2, 3, 4, 5]
    plt.bar(x, storm, align="center")
    plt.ylabel("Rainfall (inches)")
    plt.title("Rainfall during a Storm")
    plt.show()


if __name__ == "__main__":
    main()
