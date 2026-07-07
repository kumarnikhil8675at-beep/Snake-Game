import turtle
import time
import snake 
import food
import scoreboard

snake=snake.Snake()
food=food.Food()
score=scoreboard.score()


screeen=turtle.Screen()
screeen.listen()
screeen.setup(width=600, height=700)
screeen.tracer(0)

line=turtle.Turtle()
line.hideturtle()
line.penup()
line.goto(-300,290)
line.pendown()
line.forward(600)
line.speed(10)


while snake.lose(score,290):
    screeen.update()
    time.sleep(0.3)
    
    snake.move()
        
    screeen.onkey(fun=snake.up,key='w')
    screeen.onkey(fun=snake.down,key='s')
    screeen.onkey(fun=snake.right,key='d')
    screeen.onkey(fun=snake.left,key='a')
    
    if snake.snakedoby_check(score)== False: break 
 
    if snake.segment.distance(food)<15:
        snake.new_snake_add()
        score.scoreupdate()
        food.foodpositonchange()

turtle.done()