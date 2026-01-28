from turtle import Turtle

x_position = [0, -20, -40]
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0

class Snake():
    def __init__(self):
        self.all_snake = []
        self.snake()
        self.head = self.all_snake[0]

    def snake(self):
        for position in x_position:
            self.create_snake((position, 0))


    def create_snake(self, position):           
            timmy = Turtle("square")
            timmy.penup()
            timmy.goto(position)
            self.all_snake.append(timmy)
    
    def extend(self):
        last_position = self.all_snake[-1].position()
        self.create_snake(last_position)

    def snake_forward(self):
        for snake_pos in range(len(self.all_snake) - 1, 0, -1):
            new_x = self.all_snake[snake_pos-1].xcor()
            new_y = self.all_snake[snake_pos-1].ycor()
            self.all_snake[snake_pos].goto(new_x, new_y)
        self.head.forward(20)    

    def forward(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def backward(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def upward(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def downward(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)        

    def reset(self):
        for segment in self.all_snake:
            segment.goto(1000, 1000) 
        self.all_snake.clear()
        self.snake()
        self.head = self.all_snake[0]