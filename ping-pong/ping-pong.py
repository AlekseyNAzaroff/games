import turtle
from random import choice, randint

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
border.setheading(270)  # 0-east; 90-north; 180-west; 270-south
for i in range(25):
    if i % 2 == 0:
        border.forward(24)
    else:
        border.up()
        border.forward(24)
        border.down()
border.hideturtle()

rocket_a = turtle.Turtle()
rocket_a.color('white')
rocket_a.shape('square')
rocket_a.shapesize(stretch_wid=5, stretch_len=1)
rocket_a.penup()
rocket_a.goto(-450, 0)

rocket_b = turtle.Turtle()
rocket_b.color('white')
rocket_b.shape('square')
rocket_b.shapesize(stretch_wid=5, stretch_len=1)
rocket_b.penup()
rocket_b.goto(450, 0)


def move_up_a():
    y = rocket_a.ycor() + 10
    if y > 250:
        y = 250
    rocket_a.sety(y)


def move_down_a():
    y = rocket_a.ycor() - 10
    if y < -250:
        y = -250
    rocket_a.sety(y)


def move_up_b():
    y = rocket_b.ycor() + 10
    if y > 250:
        y = 250
    rocket_b.sety(y)


def move_down_b():
    y = rocket_b.ycor() - 10
    if y < -250:
        y = -250
    rocket_b.sety(y)


ball = turtle.Turtle()
ball.shape('circle')
ball.color('red')
ball.speed(0)
ball.dx = 3
ball.dy = -3
ball.penup()

window.listen()
window.onkeypress(move_up_a, 'w')
window.onkeypress(move_down_a, 's')
window.onkeypress(move_up_b, 'Up')
window.onkeypress(move_down_b, 'Down')

while True:
    window.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() >= 290:
        ball.dy = -ball.dy

    if ball.ycor() <= -290:
        ball.dy = -ball.dy

    if ball.xcor() >= 490:
        ball.goto(0, randint(-150, 150))
        ball.dx = choice([-4, -3, -2, 2, 3, 4])
        ball.dy = choice([-4, -3, -2, 2, 3, 4])

    if ball.xcor() <= -490:
        ball.goto(0, randint(-250, 250))
        ball.dx = choice([-4, -3, -2, 2, 3, 4])
        ball.dy = choice([-4, -3, -2, 2, 3, 4])

window.mainloop()
