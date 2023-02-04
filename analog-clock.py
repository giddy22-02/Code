import turtle
clock=turtle.Screen()
clock.bgcolor("skyblue")
clock.setup(width=600, height=600)
clock.title("Analog clock")

#...............creating a drawing pen
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0) #speed is 1 move per second and can be changed
pen.pensize(3)


# ............Creating a function
def draw_clock(pen):
    #...drawing the clock face
    pen.up()
    pen.goto(0, 210)
    pen.setheading(180)
    pen.color("blue")
    pen.pendown()
    pen.circle(210)
    #...drawing hour lines
    pen.up()
    pen.goto(0,0)
    pen.setheading(90)

    for _ in range(12):
        pen.fd(190)
        pen.pendown()
        pen.fd(20)
        pen.penup()
        pen.goto(0,0)
        pen.rt(30)
draw_clock(pen)


#..............loop to keep the clock displayed without disappearing
clock.mainloop()
