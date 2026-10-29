# /// script
# requires-python = ">=3.14"
# dependencies = []
# ///


def main() -> None:
    with open("art.txt", "r") as ascii_art:
        line_count = 0
        for line in ascii_art:
            line_count += 1
            print(line, end="")
        print(f"Total number of lines: {line_count}")


if __name__ == "__main__":
    main()
