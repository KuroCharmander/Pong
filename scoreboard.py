from turtle import Turtle
import time

LEFT = "left"
RIGHT = "right"
CENTER = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    """The scoreboard of the Pong game."""
    def __init__(self):
        """Initialize the scoreboard."""
        super(Scoreboard, self).__init__()
        # Dictionary containing the scores of player A and B
        self.score = {"A": 0, "B": 0}
        self.color("white")
        self.hideturtle()
        self.width(5)
        self.penup()
        self.countdown()

    def countdown(self):
        """3 second countdown before the game starts."""
        self.home()
        self.clear()
        for sec in range(3, 0, -1):
            self.write(f"{sec}", align=CENTER, font=FONT)
            time.sleep(1)
            self.clear()
        self.update_scoreboard()

    def increase_score(self, player):
        """Increase the player's score."""
        self.clear()
        self.score[player] += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        """Updates the scoreboard to the current scores."""
        self.clear()
        self.draw_line()
        self.penup()
        self.goto(-40, 140)
        self.write(f"{self.score['A']}", align=RIGHT, font=FONT)
        self.goto(40, 140)
        self.write(f"{self.score['B']}", align=LEFT, font=FONT)

    def draw_line(self):
        """Draw the line that divides the players' side."""
        self.goto(0, -165)
        self.setheading(90)
        for _ in range(6):
            self.pendown()
            self.forward(40)
            self.penup()
            self.forward(20)

    def game_over(self, winner):
        """Displays 'GAME OVER' in the center of the screen and announces the winner."""
        self.home()
        self.write("GAME OVER", align=CENTER, font=FONT)
        self.goto(0, -40)
        self.write(f" Player {winner} wins!", align=CENTER, font=FONT)
