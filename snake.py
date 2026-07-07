import turtle

TTposition=[(0,0),(-20,0),(-40,0)]
Move_distance=20

class Snake:
    def __init__(self):
        self.TTlist=[]
        self.create_snake()
        self.segment=self.TTlist[0]
 
    
    def create_snake(self):
        for position in TTposition:
            self.addsnake(position)
            
    def addsnake(self,position):
        tur=turtle.Turtle(shape="square")
        tur.penup()
        tur.goto(position)
        tur.color('red')
        self.TTlist.append(tur)
    
    def move(self):
        for a in range(len(self.TTlist)-1,0,-1):
            new_x=self.TTlist[a-1].xcor()
            new_y=self.TTlist[a-1].ycor()
            self.TTlist[a].goto(new_x,new_y)
        self.TTlist[0].forward(Move_distance)
    
    def up(self):
        self.segment.setheading(90)
    
    def down(self):
        self.segment.setheading(270)
    
    def right(self):
        self.segment.setheading(0)
    
    def left(self):
        self.segment.setheading(180)
        
    def lose(self,text,value):
        new=True
        new_x=self.segment.xcor()
        new_y=self.segment.ycor()
        if(round(new_x)>value or round(new_x)<-value or round(new_y)>value or round(new_y)<-value):
            text.gameover()
            return False
        else:
            return True
        
    def snakedoby_check(self,text):
        for part in self.TTlist[1:]:
            if(self.segment.distance(part)<15):
                text.gameover()
                return False
        return True
    
    def new_snake_add(self):
        self.addsnake(self.TTlist[-1].position())
    