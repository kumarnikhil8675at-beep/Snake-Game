from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.goto(random.randrange(-220,220,20),random.randrange(-180,180,20))
        self.speed("fastest")
       
        
    def foodpositonchange(self):
        self.goto(random.randrange(-220,220,20),random.randrange(-180,180,20))
        
        
        