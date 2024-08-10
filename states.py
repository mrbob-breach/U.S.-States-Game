from turtle import Turtle


class State(Turtle):

    def __init__(self, text, x, y):
        super().__init__()
        self.penup()
        self.ht()
        self.text = text
        self.x = x
        self.y = y
        self.teleport(self.x, self.y)
        self.write(self.text)





