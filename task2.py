import argparse
import turtle

arguments = argparse.ArgumentParser(
    prog="snowflake",
    description="Малює сніжинку Коха із заданою глибиною рекурсії.",
)

arguments.add_argument(
    "-d", "--depth", type=int, default=3, help="Рекурсивна глибина(default: %(default)s)"
)

def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)


def draw_koch_curve(order, size=300):
    window = turtle.Screen()
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-size / 3, 0)
    t.pendown()

    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

    window.mainloop()


if __name__ == "__main__":
    args = arguments.parse_args()
    draw_koch_curve(args.depth)