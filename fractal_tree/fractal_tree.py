import turtle
import random

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=900, height=700)

t = turtle.Turtle()
t.speed(0)
t.left(90)
t.up()
t.backward(250)
t.down()
t.color("white")

def draw_branch(length, thickness, angle, depth):
    if depth == 0:
        return

    # Set branch color gradient
    r = random.uniform(0.2, 1)
    g = random.uniform(0.2, 1)
    b = random.uniform(0.2, 1)
    t.pencolor(r, g, b)

    t.pensize(thickness)
    t.forward(length)

    # Right branch
    t.right(angle)
    draw_branch(length * 0.7, thickness * 0.7, angle, depth - 1)

    # Left branch
    t.left(angle * 2)
    draw_branch(length * 0.7, thickness * 0.7, angle, depth - 1)

    # Go back
    t.right(angle)
    t.backward(length)

def main():
    # You can adjust these values
    draw_branch(length=120, thickness=10, angle=25, depth=8)
    turtle.done()

main()
