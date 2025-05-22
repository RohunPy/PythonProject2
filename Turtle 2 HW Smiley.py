import turtle
t = turtle.Turtle()
s = turtle.Screen()
t.width(1)
#outside circle
t.color("black" , "yellow")
t.begin_fill()
t.circle(100)
t.end_fill()
#first eye
t.penup()
t.goto(-40,100)
t.pendown()
t.color("black" , "white")
t.begin_fill()
t.circle(20)
t.end_fill()
#second eye
t.penup()
t.goto(40,100)
t.pendown()
t.color("black" , "white")
t.begin_fill()
t.circle(20)
t.end_fill()
#nose
t.penup()
t.goto(0,75)
t.pendown()
t.color("black")
t.begin_fill()
t.circle(10)
t.end_fill()
#draw smile
t.penup()
t.goto(-40,75)
t.pendown()
t.right(45)
t.circle(60, 100)
#tounge
t.penup()
t.goto(-10, 58)
t.right(135)
t.color("black", "red")
t.pendown()
t.begin_fill()
t.circle(10, 180)
t.end_fill()
#pupil
t.penup()
t.goto(-30, 110)
t.pendown()
t.color("black")
t.begin_fill()
t.circle(5)
t.end_fill()

# second pupil
t.penup()
t.goto(37, 110)
t.pendown()
t.color("black")
t.begin_fill()
t.circle(5)
t.end_fill()
t.penup()

t.goto(-200,200)




















s.exitonclick()