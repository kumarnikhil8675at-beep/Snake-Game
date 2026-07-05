import turtle
import random
import time

TTlist=[]
TTposition=[(0,0),(-20,0),(-40,0)]
score=0

for a in range(3):
    tur=turtle.Turtle(shape="square")
    tur.penup()
    tur.goto(TTposition[a])
    tur.color('red')
    TTlist.append(tur)
    
doot=turtle.Turtle(shape="circle")

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

def right():
    TTlist[0].right(90)

def left():
    TTlist[0].left(90)

def dot():
    doot.penup()
    doot.goto(random.randrange(-220,220,20),random.randrange(-180,180,20))
 
def snakedoby_check():
    for a in range(3,len(TTlist)):
        if (round(TTlist[0].xcor()) == round(TTlist[a].xcor()) and round(TTlist[0].ycor()) == round(TTlist[a].ycor())):
            # print("You lose")
            text.clear()
            text.write(f"You lose",font=("Arial", 20, "bold"))
            return False
    return True
  
def food():
    tt=turtle.Turtle(shape='square')
    tt.hideturtle()
    new_x=TTlist[len(TTlist)-1].xcor()
    new_y=TTlist[len(TTlist)-1].ycor()
    TTlist.append(tt)
    tt.penup()
    tt.goto(new_x,new_y)
    tt.showturtle()
    global score
    score += 1
    dot()


def lose():
    a=TTlist[0].position()
    if(round(a[0])>290 or round(a[0])<-290 or round(a[1])>290 or round(a[1])<-290):
        # print("you lose first")
        text.clear()
        text.write(f"You lose",font=("Arial", 20, "bold"))
        return False
    else:
        return True

text=turtle.Turtle()
text.hideturtle()
text.penup()
text.goto(-80,300)

dot()
while lose():
    screeen.update()
    time.sleep(0.3)
    
    for a in range(len(TTlist)-1,0,-1):
        new_x=TTlist[a-1].xcor()
        new_y=TTlist[a-1].ycor()
        TTlist[a].goto(new_x,new_y)
        
    screeen.onkey(fun=right,key='d')
    screeen.onkey(fun=left,key='a')
    
    if(snakedoby_check()== False): break 
    elif(round(TTlist[0].xcor()) == round(doot.xcor()) and round(TTlist[0].ycor()) == round(doot.ycor())):food()        
                   
    text.clear()
    text.write(f"your scor {score}",font=("Arial", 20, "bold"))
    TTlist[0].forward(20)
    
    
turtle.done()