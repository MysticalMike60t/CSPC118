# Named this differently because of the instructions grammar, and doesn't really follow my uses of "print".


def quadratic_formula() -> None:
    # ± :   U+00B1  \u00b1
    # √ :   U+221A  \u221a
    # ² :   U+00B2  \u00b2
    # ─ :   U+2500  \u2500
    print("""
         -b ± √(b² - 4ac)
    x = ──────────────────
                2a
    """)


def quadratic_equation() -> None:
    print("ax² – bx – c = 0")
