import turtle

t = turtle.Turtle()
s = turtle.Screen()

def draw_circle(color, radius):
    t.penup()
    t.goto(0, -radius)  # Move turtle to the bottom of the circle
    t.pendown()
    t.color("black", color)  # Black outline, filled with color
    t.begin_fill()
    t.circle(radius)
    t.end_fill()



draw_circle("red", 100)
draw_circle("white", 70)
draw_circle("red", 40)

s.exitonclick()
