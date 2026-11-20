# /// script
# requires-python = ">=3.14"
# dependencies = []
# ///

# Write a function for the turtle that will draw a square.
# The input to the function should accept 1 input
# argument that is the length of 1 side of the square.
#
# Challenge #1 – Make the function above recursive.

import turtle as t

TURTLE: t.Turtle = t.Turtle("classic", visible=True)
SCREEN = t.Screen()
SQUARE_SIZE: int = 100


def write_square(iter: int):
    if iter == 0:
        return
    TURTLE.seth(TURTLE.heading() + 90)
    TURTLE.fd(SQUARE_SIZE)
    iter -= 1
    write_square(iter)


def main() -> None:
    # Configure Mr. Tortle
    TURTLE.pen(fillcolor="black", pencolor="red", pensize=10)

    # Configure Mr. Tortle's home
    SCREEN.setup(364, 480)
    SCREEN.bgpic("cat.gif")
    SCREEN.bgcolor("purple")

    # Tell Mr. Tortle where to sit and wait
    TURTLE.home()

    # Show Mr. Tortle to the world
    TURTLE.showturtle()

    # Make Mr. Tortle draw a square
    write_square(4)

    TURTLE.pu()
    TURTLE.goto(0, -128)
    TURTLE.pd()
    TURTLE.write("Meow Meow Meow", align="center", font=("Arial", 24, "normal"))
    TURTLE.hideturtle()
    # 364x480
    # Stare at Mr. Tortle infinitely

    r = print("Meow")
    print(r)
    t.done()


if __name__ == "__main__":
    main()
