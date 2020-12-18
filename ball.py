from turtle import Turtle
import random


class Ball(Turtle):
    """A Ball for the Pong game."""
    def __init__(self):
        """Initialize a ball."""
        super(Ball, self).__init__("circle")
        self.penup()
        self.color("white")
        # Pick a random side to start
        self.side = random.choice(["A", "B"])
        self.start_side(self.side)

    def start_side(self, side):
        """Reset the ball back to the center and set the heading of the ball to move at a random angle depending on
        the side parameter."""
        self.home()
        angle = random.randint(-70, 70) if side == "A" else random.randint(120, 240)
        self.setheading(angle)

    def move(self):
        """Move the ball forward at the preset heading."""
        self.forward(4)

    def offset(self):
        """Return a random int between [-15, 15] to offset the angle of the bounce."""
        return random.randint(-15, 15)

    def bounce_off_wall(self):
        """Change the angle of the ball's movement and adding an offset to simulate the ball bouncing off the wall."""
        angle = self.heading()
        # Manually change the angle if the ball's heading is too close to vertical.
        if 75 <= angle < 90:
            angle = 65
        elif 90 <= angle <= 105:
            angle = 115
        elif 255 <= angle < 270:
            angle = 215
        elif 270 <= angle < 285:
            angle = 295
        self.setheading(-angle + self.offset())
        self.move()

    def bounce_off_paddle(self):
        """Change the angle of tbe ball's movement and adding an offset when the ball hits a paddle."""
        angle = self.heading()
        self.setheading(-angle + 180 + self.offset())
        self.move()
