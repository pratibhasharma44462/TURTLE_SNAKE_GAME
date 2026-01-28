from turtle import Screen
import time
from snake_move import Snake
from scoreboard_food import Food, Scoreboard



screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("lightgreen")
screen.title("SNAKE GAME")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()


screen.listen()
screen.onkey(snake.upward, "Up")
screen.onkey(snake.downward, "Down")
screen.onkey(snake.backward, "Left")
screen.onkey(snake.forward, "Right")
 

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.snake_forward()
    if snake.head.distance(food) < 15:
        food.relocate()
        snake.extend()
        score.score_board()
        
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        retry = screen.textinput("Game Over!!", "Retry? (yes/no): ")

        if retry and retry.lower() == "yes":
            snake.reset()
            score.reset_game()
            screen.listen()
        elif retry and retry.lower() == "no":    
                score.game_over() 
                game_is_on = False
                exit()
        else:
            screen.bye()
            game_is_on = False
        

    for tail in snake.all_snake[1:]:
        if snake.head.distance(tail) < 10:
            retry = screen.textinput("Game Over!!", "Retry? (yes/no): ")

            if retry and retry.lower() == "yes":
                snake.reset()
                score.reset_game()
                screen.listen()  
            elif retry and retry.lower() == "no":    
                score.game_over()
                game_is_on = False
                exit()
            else:
                screen.bye()
                game_is_on = False







screen.exitonclick()
