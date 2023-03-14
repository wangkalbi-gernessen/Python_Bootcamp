import random
from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("red")
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)

"""Draw square"""
# for _ in range(4):
#     timmy_the_turtle.color("blue")
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.left(90)

"""Draw dashed line"""
# for _ in range(15):
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.pendown()

# """Draw shape"""
# def draw_shape(num_slides):
#     angle = 360 / num_slides
#     for _ in range(num_slides):
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(angle)
#
# draw_shape(6)

"""Draw random walk"""


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


# directions = [0, 90, 180, 270]
# for _ in range(200):
#     timmy_the_turtle.color(random_color())
#     timmy_the_turtle.forward(30)
#     timmy_the_turtle.setheading(random.choice(directions))

"""Draw spirograph"""
timmy_the_turtle.speed("fastest")
timmy_the_turtle.color(random_color())
timmy_the_turtle.circle(100)
current_heading = timmy_the_turtle.heading()
timmy_the_turtle.setheading(current_heading + 10)
timmy_the_turtle.circle(100)

screen = Screen()
screen.exitonclick()
