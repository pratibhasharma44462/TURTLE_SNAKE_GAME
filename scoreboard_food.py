from turtle import Turtle
import random
ALIGNMENT = "Center"
FONT = ("Courier" , 15 ,"normal ")


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5,0.5)
        self.color("coral")
        self.speed("fastest")
        self.relocate()

    def relocate(self):
        x_rand = random.randint(-270,270)
        y_rand = random.randint(-270,270)
        self.goto(x_rand, y_rand)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 270)
        self.write(f"Score : {self.score}" , align=ALIGNMENT , font= FONT)
        self.hideturtle()

    def score_board(self):
        self.score += 1
        self.clear()
        self.write(f"Score : {self.score}" , align=ALIGNMENT , font= FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!!" , align=ALIGNMENT , font= FONT)
        
    def reset_game(self):
        self.score = 0
        self.clear()
        self.goto(0, 270)
        self.write(f"Score : {self.score}", align=ALIGNMENT, font=FONT)

