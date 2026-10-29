# /// script
# requires-python = ">=3.14"
# dependencies = []
# ///


def main() -> None:
    grade_midterm: float = float(
        input("What grade did you get on the midterm? \x1b[36m")
    )
    grade_final: float = float(
        input("\x1b[0mWhat grade did you get on the final? \x1b[36m")
    )
    grades: list[float] = [grade_midterm, grade_final]
    passing_grade: float = 70.0
    final_grade: float = (grade_midterm + grade_final) / len(grades)

    if final_grade >= passing_grade:
        print(
            f"\x1b[0m\x1b[32mCongrats, you passed the course with: {final_grade}\x1b[0m"
        )
    else:
        print(f"\x1b[31mSorry, you failed the course with: {final_grade}\x1b[0m")


if __name__ == "__main__":
    main()
