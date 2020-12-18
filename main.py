from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=700, height=400)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

win_number = int(screen.textinput(title="Number of Wins", prompt="How many wins for a game?"))

paddle_A = Paddle(player="A")
paddle_B = Paddle(player="B")
ball = Ball()
scoreboard = Scoreboard()

# Set the listeners
screen.listen()
screen.onkeypress(paddle_A.up, "w")
screen.onkeypress(paddle_A.up, "a")
screen.onkeypress(paddle_A.down, "s")
screen.onkeypress(paddle_A.down, "d")
screen.onkeypress(paddle_B.up, "Up")
screen.onkeypress(paddle_B.up, "Left")
screen.onkeypress(paddle_B.down, "Down")
screen.onkeypress(paddle_B.down, "Right")


def is_winner(player):
    """If the player has win_number of wins, show the game over screen. Otherwise, countdown to the next round."""
    if scoreboard.score[player] == win_number:
        scoreboard.game_over(player)
        return False
    else:
        scoreboard.countdown()
        return True


# Play the game
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.01)

    ball.move()

    # If the ball passes through the left side, right side wins
    if ball.xcor() < -350:
        scoreboard.increase_score("B")
        ball.start_side("A")
        game_is_on = is_winner("B")
    # If the ball passes through the right side, left side wins
    if ball.xcor() > 340:
        scoreboard.increase_score("A")
        ball.start_side("B")
        game_is_on = is_winner("A")

    # If the ball hits a horizontal wall, the ball will bounce off the wall
    if ball.ycor() < -180 or ball.ycor() > 190:
        ball.bounce_off_wall()

    # Determine if the ball will bounce off of the paddle
    if ball.distance(paddle_A) < 50 and ball.xcor() < -290 or ball.distance(paddle_B) < 50 and ball.xcor() > 280:
        ball.bounce_off_paddle()

screen.exitonclick()
