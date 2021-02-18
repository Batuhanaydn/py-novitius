# Simple Pong Games
# if you are using mac or linux:
# import os
# os.system("bounce.wav&")

import turtle
import winsound



win = turtle.Screen()
win.title("Pong Game @beyaydinn")
win.bgcolor("blue")
win.setup(width=800, height=600)
win.tracer(0)


# Score
score_a = 0
score_b = 0


# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("red")
paddle_a.shapesize(stretch_wid=4.8, stretch_len=1)

paddle_a.penup()
paddle_a.goto(-350, 0)



# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("red")
paddle_b.shapesize(stretch_wid=4.8, stretch_len=1)

paddle_b.penup()
paddle_b.goto(350, 0)


# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("green")

ball.penup()
ball.goto(0, 0)
# Ball Move
ball.dx = 0.2
ball.dy = -0.2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.pensize(width=5)
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0 ", align="center", font=("Courier", 24, "bold"))




# Function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 10
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Keyboardb Binding
win.listen()
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")

# Main Game Loop

while True:

    win.update()
    # Move Ball 
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    # border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)


    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)


    if ball.xcor() > 390:
        ball.goto(180,0)
        ball.dx *=-1
        score_a += 1
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "bold"))
    
    if ball.xcor() < -390:
        ball.goto(-180,0)
        ball.dx *=-1
        score_b += 1
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "bold"))

    # Paddle and Ball Collisions
    if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40 ):
        ball.setx(340)
        ball.dx *= -1      
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)



    if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40 ):
        ball.setx(-340)
        ball.dx *= -1      
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
