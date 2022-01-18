# Turtle documentation @ https://docs.python.org/3/library/turtle.html

import random
import turtle as t
import colorgram
colors = colorgram.extract('image.jpg', 30)

rgb_colors =[]

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    all_colors = (r, g, b)
    rgb_colors.append(all_colors)


tim = t.Turtle()
tim.hideturtle()
tim.speed("fastest")
t.colormode(255)
tim.penup()

def position_selector():
    """ Defines the starting position of each row. Provides rules for drawing and movement """
    x_pos = -225
    y_pos = -225
    for i in range (10):
        tim.setposition(x_pos, y_pos)
        draw_row()
        y_pos += 50


def draw_row():
    """ Draws 10 dots of random colors in a row """
    for i in range(10):
        tim.dot(20, random.choice(rgb_colors))
        tim.forward(50)


position_selector()

screen = t.Screen()
screen.exitonclick()


