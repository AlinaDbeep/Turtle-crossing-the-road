from turtle import Turtle

start_pos = (0, -280)
move_dist = 10
y_line_end = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("pink")
        self.penup()
        self.go_to_start()
        self.setheading(90)

    def go_up(self):
        self.forward(move_dist)

    def go_to_start(self):
        self.goto(start_pos)

    def is_at_finish_line(self):
        if self.ycor() > y_line_end:
            return True
        else:
            return False