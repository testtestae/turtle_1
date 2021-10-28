import turtle
import time
t = turtle.Turtle()
t.speed(10)
t.fillcolor("black")
t.pencolor("black")
t.shape("turtle")
a = 0.1
b = 0.1
c = 0.1
t.turtlesize(a,b,c)
while True:
    a = a + 1
    b = b + 1
    c = c + 1
    t.turtlesize(a,b,c)
    time.sleep(0.1)