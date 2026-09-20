from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
screen=Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake=Snake()
food=Food()
scoreboard=ScoreBoard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")



game_on=True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase()

    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()<-280 or snake.head.ycor()>280:
        game_on=False
        scoreboard.over()

    for i in snake.seg[1:]:
        if snake.head.distance(i)<10:
            game_on=False
            scoreboard.over()



screen.exitonclick()






















#
# for i in range(3):
#     tim=Turtle()
#     tim.color("white")
#     tim.shape("square")
#     tim.goto(i*20,0)

# tim = Turtle()
# tim.color("white")
# tim.shape("square")
# tim.penup()
#
# tom=Turtle()
# tom.forward(20)
# tom.color("white")
# tom.shape("square")
# tom.penup()
#
# tam=Turtle()
# tam.forward(40)
# tam.color("white")
# tam.shape("square")
# tam.penup()