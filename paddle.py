from turtle import Turtle

STARTING_Y_POSITION = [30, 20, 0, -20, -30]
UP = 90
DOWN = 270


class Paddle(Turtle):
    """Paddle for the Pong game."""
    def __init__(self, player):
        """Initialize a paddle for player 'A' or 'B'."""
        super().__init__("square")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.color("white")
        x = -310 if player == "A" else 300
        self.goto(x, 0)

    def up(self):
        """Move the paddle up if it's within the screen."""
        if self.ycor() < 150:
            self.sety(self.ycor() + 20)

    def down(self):
        """Move the paddle down if it's within the screen."""
        if self.ycor() > -150:
            self.sety(self.ycor() - 20)
