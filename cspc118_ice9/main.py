# /// script
# requires-python = ">=3.14"
# dependencies = []
# ///


import sys
import turtle
from time import sleep

the_turtle = turtle.Turtle()


def draw_stair(passed_turtle: turtle.Turtle) -> None:
    passed_turtle.forward(50)
    passed_turtle.right(90)
    passed_turtle.forward(25)
    passed_turtle.left(90)


def draw_circle(passed_turtle: turtle.Turtle, color: str, radius: int) -> None:
    passed_turtle.pencolor(color)
    passed_turtle.circle(radius)


def draw_smiley_face(passed_turtle: turtle.Turtle) -> None:
    passed_turtle.hideturtle()
    passed_turtle.speed(1)
    passed_turtle.color("brown", "yellow")
    passed_turtle.begin_fill()
    passed_turtle.width(2)
    passed_turtle.circle(100)
    passed_turtle.end_fill()

    # Eye
    passed_turtle.penup()
    passed_turtle.setpos(0, 0)
    passed_turtle.color("black")
    passed_turtle.setpos(-35, 110)
    passed_turtle.pendown()
    passed_turtle.begin_fill()
    passed_turtle.circle(15)
    passed_turtle.end_fill()

    # Eye
    passed_turtle.penup()
    passed_turtle.setpos(0, 0)
    passed_turtle.color("black")
    passed_turtle.setpos(35, 110)
    passed_turtle.pendown()
    passed_turtle.begin_fill()
    passed_turtle.circle(15)
    passed_turtle.end_fill()

    # Mouth
    passed_turtle.penup()
    passed_turtle.setpos(0, 0)
    passed_turtle.color("brown")
    passed_turtle.setpos(-50, 75)
    passed_turtle.pendown()
    passed_turtle.right(90)
    passed_turtle.circle(50, 180)

    _ = input("Press any ket to exit...")


def main() -> int:
    _n: int = int(input("How many stairs? "))
    for _ in range(_n):
        draw_stair(the_turtle)

    _c: str = input("Enter color: ")
    _r: int = int(input("Enter Radius: "))
    _i: int = 0
    while _i < 10:
        if _i != 0:
            sleep(1)
        draw_circle(the_turtle, _c, _r)
        the_turtle.forward(20)
        _i += 1

    the_turtle.reset()

    draw_smiley_face(the_turtle)

    return 0


if __name__ == "__main__":
    sys.exit(main())
