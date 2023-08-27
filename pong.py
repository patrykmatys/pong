import turtle

# Set up the game window
window = turtle.Screen()
window.title("Pong Game")
window.bgcolor("black")
window.setup(width=800, height=600)

# Create the left paddle
left_paddle = turtle.Turtle()
left_paddle.speed(0)
left_paddle.shape("square")
left_paddle.color("white")
left_paddle.shapesize(stretch_wid=6, stretch_len=1)
left_paddle.penup()
left_paddle.goto(-350, 0)

# Create the right paddle
right_paddle = turtle.Turtle()
right_paddle.speed(0)
right_paddle.shape("square")
right_paddle.color("white")
right_paddle.shapesize(stretch_wid=6, stretch_len=1)
right_paddle.penup()
right_paddle.goto(350, 0)

# Create the ball
ball = turtle.Turtle()
ball.speed(40)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2  # Ball's horizontal speed
ball.dy = -2  # Ball's vertical speed

# Move the left paddle
def move_left_paddle_up():
    y = left_paddle.ycor()
    if y < 250:
        y += 20
    left_paddle.sety(y)

def move_left_paddle_down():
    y = left_paddle.ycor()
    if y > -240:
        y -= 20
    left_paddle.sety(y)

# Move the right paddle
def move_right_paddle_up():
    y = right_paddle.ycor()
    if y < 250:
        y += 20
    right_paddle.sety(y)

def move_right_paddle_down():
    y = right_paddle.ycor()
    if y > -240:
        y -= 20
    right_paddle.sety(y)

# Keyboard bindings
window.listen()
window.onkeypress(move_left_paddle_up, "w")
window.onkeypress(move_left_paddle_down, "s")
window.onkeypress(move_right_paddle_up, "Up")
window.onkeypress(move_right_paddle_down, "Down")

# Initialize scores
score_left = 0
score_right = 0

# Create the score display
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Left: {}  Right: {}".format(score_left, score_right), align="center", font=("Courier", 24, "normal"))

# ... (Previous code)

# Main game loop
while True:
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_left += 1
        score_display.clear()
        score_display.write("Left: {}  Right: {}".format(score_left, score_right), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_right += 1
        score_display.clear()
        score_display.write("Left: {}  Right: {}".format(score_left, score_right), align="center", font=("Courier", 24, "normal"))

    # Paddle and ball collisions
    if (350 > ball.xcor() > 340) and (right_paddle.ycor() + 50 > ball.ycor() > right_paddle.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1

    if (-350 < ball.xcor() < -340) and (left_paddle.ycor() + 50 > ball.ycor() > left_paddle.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1

# Close the game window when clicking the close button
window.bye()