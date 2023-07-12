import turtle

window = turtle.Screen()
window.title("Ping-Pong")
window.setup(width=0.8, height=0.8)
window.bgcolor('black')


border = turtle.Turtle()
border.speed(0)
border.color('green')
border.begin_fill()
border.goto(-500, 300)
border.goto(500, 300)
border.goto(500, -300)
border.goto(-500, -300)
border.goto(-500, 300)
border.end_fill()

border.goto(0, 300)
border.color('white')
border.setheading(270) #0-east; 90-north; 180-west; 270-south
for i in range(25):
    if i % 2 == 0:
        border.forward(24)
    else:
        border.up()
        border.forward(24)
        border.down()

border.hideturtle()


window.mainloop()