import time
from food import Food
from snake import Snake
from turtle import Screen
from score_board import ScoreBoard

game_is_on = True

screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.setup(width=600, height=600)


def turn_off_game():
    global game_is_on
    game_is_on = False


food = Food()
snake = Snake()
score_board = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(turn_off_game, "Escape")

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score_board.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score_board.reset()
        snake.reset()

    # Detect collision with wall
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score_board.reset()
            snake.reset()

screen.exitonclick()