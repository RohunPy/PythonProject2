import random
from idlelib.configdialog import FontPage
from turtle import Turtle, Screen
ALIGN = "right"
FONT = ("Courier" , 28, "bold")

screen = Screen()
screen.setup(width=800, height=600)
screen.bgpic('road.gif')

y_positions = [-260, -172, -85, 2, 85, 172, 260 ]
colors = [ "white", "red", "orange", "pink", "tomato", "dodger blue", "yellow"]
all_turtle = []

for index in range(0, 7):
    new_tur = Turtle(shape="turtle")
    new_tur.shapesize(2)
    new_tur.speed('fastest')
    new_tur.penup()
    new_tur.goto(x=-350, y=y_positions[index])
    new_tur.color(colors[index])
    all_turtle.append(new_tur)

user_bet = input("Which turtle will win the race? Enter a color: ")

is_on = True

while is_on:
    for turtle in all_turtle:
        if turtle.xcor() > 330:
            is_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                turtle.write(f'Winner! The {winner} is winner' , font=FONT, align=ALIGN)
            else:
                turtle.write(f'Lost! The {winner} is winner', font=FONT, align=ALIGN)

        random_pace = random.randint(0, 7)
        turtle.forward(random_pace)






screen.exitonclick()


















