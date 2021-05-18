# Pong in Python3 with turtle from tutorial by @TokyoAdTech

import turtle

wn = turtle.Screen()
wn.title("Pong by @KingPipi")
wn.bgcolor("#fc034e")
wn.setup(width=800, height=600)
wn.tracer(0) #stop window from updating so update can be performed manually

# Define Score Keeper Variables
score_a = 0
score_b = 0


# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) #not speed for paddle on screen
paddle_a.shape("square") #default size 20px x 20px
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350, 0) #start position

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.5 # define ball movement
ball.dy = 0.5

# Score Writer
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f"Player A: {score_a} Player B: {score_b}", align="center", font=("Courier", 24, "normal"))


# Movement functions
def paddle_a_up():
    y = paddle_a.ycor() # use turtle method that returns y coordinate to determine position
    y += 50 # move up on the y axis
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 50 # move down on the y axis
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 50 # move up on the y axis. Same axis as before but different x position per setup in line 28
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 50 # move down on the y axis.
    paddle_b.sety(y)

# Keyboard binding to call movement functions
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

#Main game loop:
while True:
    wn.update()
    # move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    # border check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1 #Add a point to player 1 if player 2 misses the ball
        pen.clear()
        pen.write(f"Player A: {score_a} Player B: {score_b}", align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1 #Add a point to player 2 if player 1 misses the ball
        pen.clear()
        pen.write(f"Player A: {score_a} Player B: {score_b}", align="center", font=("Courier", 24, "normal"))

    #paddle collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
