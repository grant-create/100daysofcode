
# made in jupyter notebook
# doesnt seem to work in vscode


import turtle as t
from turtle import Screen
screen = Screen()
screen.screensize(200,150)

# Setting the screen color-mode
t.colormode(255)

import random

tim = t.Turtle()
tim.shape('turtle')

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color

direction = [0, 90, 180, 270]
tim.pensize(15)
tim.speed('fastest')
for _ in range(2000):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(direction))




my_screen = Screen()

print(my_screen.canvheight)
my_screen.exitonclick()
