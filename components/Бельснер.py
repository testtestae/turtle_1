import turtle

t = turtle.Turtle()

def draw_circle1():
    for _ in range(360):
        t.forward(1)
        t.left(1)
turtle.mainloop()