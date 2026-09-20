from turtle import Turtle
STARTING=[(0,0), (-20,0), (-40,0)]
MOVE_DIS=20
UP=90
DOWN=270
RIGHT=0
LEFT=180
class Snake:
    def __init__(self):
        self.seg=[]
        self.create_snake()
        self.head=self.seg[0]

    def create_snake(self):
        for i in STARTING:
            self.add(i)

    def add(self, i):
        tim = Turtle("square")
        tim.color("white")
        tim.penup()
        tim.goto(i)
        self.seg.append(tim)

    def extend(self):
        self.add(self.seg[-1].position())

    def move(self):
        for i in range(len(self.seg) - 1, 0, -1):
            newx = self.seg[i - 1].xcor()
            newy = self.seg[i - 1].ycor()
            self.seg[i].goto(newx, newy)
        self.head.forward(MOVE_DIS)


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)







