# from turtle import Turtle, Screen
# tim = Turtle()
# screen = Screen()

# def move_forwards():
#     tim.forward(100)
    
# def move_backwards():
#     tim.backward(100)
    
# def move_up():
#     tim.up(100)
    
# def move_down():
#     tim.down(100)


# screen.listen()
# screen.onkey(key='d', fun=move_forwards)
# screen.onkey(key='a', fun=move_backwards)
# screen.onkey(key='w', fun=move_up)
# screen.onkey(key='s', fun=move_down)

# screen.exitonclick()

# # -------------------------------------------------------


from turtle import Turtle, Screen
import random
import time
is_race_on =False

screen =Screen()
screen.setup(width=500,height=400)
screen.colormode(255)
user_bet = screen.textinput(title="Ready to race?", prompt ="yeah?")

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color

all_turtles = []
y_pos = 150
for turtle_index in range(0,10):

    tim = Turtle(shape="turtle")
    tim.penup()
    
    tim.color(random_color())
    tim.goto(x=-230, y=y_pos)    
    all_turtles.append(tim)
    y_pos -=30
    
    
if user_bet:
    is_race_on =True
    
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            
            is_race_on = False
        rand_distance = random.randint(0,5)
        turtle.forward(rand_distance)
        #time.sleep(.5)





screen.exitonclick()