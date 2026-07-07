from turtle import Turtle
Font="Arial"
Size=20
FontSize="bold"
Aligment="center"

class score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-80,300)
        self.scores=0
        self.writes()
    
    def writes(self):
        self.write(f"your score {self.scores}",font=(Font, Size, FontSize))
    
    def gameover(self):
        self.goto(0,0)
        self.write("you lose",align=Aligment,font=(Font, Size, FontSize))
        
    def scoreupdate(self):
        self.scores+=1
        self.clear()
        self.writes()
        