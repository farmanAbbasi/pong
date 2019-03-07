import turtle
import time
import random
import winsound


win_score=5
speed=0.2# for dx and dy of ball
#userInput=False
wn=turtle.Screen()
wn.title('Classic Pong')
wn.bgcolor('black')
wn.setup(width=800,height=600)
wn.tracer(0)

#Paddle A
paddle_a=turtle.Turtle()
paddle_a.shape('square')
paddle_a.color('red')
paddle_a.speed(0)
paddle_a.turtlesize(stretch_wid=4,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

#Paddle B
paddle_b=turtle.Turtle()
paddle_b.shape('square')
paddle_b.color('blue')
paddle_b.speed(0)
paddle_b.turtlesize(stretch_wid=4,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

#Ball
ball=turtle.Turtle()
ball.shape('circle')
ball.color('white')
ball.speed(0)
ball.penup()
ball.goto(0,0)
ball.dx=speed
ball.dy=speed
ball.direction="stop"

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("P1: 0  P2: 0", align="center", font=("Courier", 20, "normal"))

pen2 = turtle.Turtle()
pen2.speed(0)
pen2.color("white")
pen2.hideturtle()
pen2.penup()
pen2.goto(0,40)
pen2.write('Click c to start',align="center", font=("Courier", 16, "normal"))

#Functions
def paddle_a_up():
    if paddle_a.ycor() <260:# to avoid going out of screen
        paddle_a.sety(paddle_a.ycor()+20)
def paddle_a_down():
    if paddle_a.ycor() >-260:
        paddle_a.sety(paddle_a.ycor()-20)
def paddle_b_up():
    if paddle_b.ycor() <260:
        paddle_b.sety(paddle_b.ycor()+20)
def paddle_b_down():
    if paddle_b.ycor() >-260:
        paddle_b.sety(paddle_b.ycor()-20)
def continueOrNot():
    #continue wali line hata do
    pen2.clear()
    ball.direction='start'
    #ooper player x wins hata do
    pen.clear()
    pen.write("P1: 0  P2: 0", align="center", font=("Courier", 20, "normal"))

       
class MoveBallClass():
    def __init__(self,p1_score,p2_score):
        self.p1_score=p1_score
        self.p2_score=p2_score
    def move_ball(self):
        if ball.direction!='stop':
            x=ball.xcor()
            y=ball.ycor()
            ball.goto(x+ball.dx,y+ball.dy)
            if ball.ycor()>290:
                winsound.PlaySound("bounce.wav", winsound.SND_ASYNC | winsound.SND_FILENAME)
                ball.sety(290)
                ball.dy*=-1
            if ball.ycor()<-280:
                winsound.PlaySound("bounce.wav", winsound.SND_ASYNC | winsound.SND_FILENAME)
                ball.sety(-280)
                ball.dy*=-1
                
            if ball.xcor()>380:
                #increase score of p1
                self.p1_score+=1
                if self.p1_score==win_score:
                    pen.clear()
                    pen.write("P1 wins!!!",align="center", font=("Courier", 20, "normal"))
                    ball.goto(0,0)
                    ball.direction='stop'
                    self.p1_score=0
                    self.p2_score=0
                    pen2.penup()
                    pen2.goto(0,60)
                    pen2.write("Press c to continue...",align="center", font=("Courier", 16, "normal")) 
                else:
                    pen.clear()
                    pen.write("P1: {}  P2: {}".format(self.p1_score,self.p2_score), align="center", font=("Courier", 20, "normal"))
                ball.goto(0,0)
               #getting the sign for the current 
                if ball.dx>0:
                    sign_dx=+1
                else:
                    sign_dx=-1
                    
                if ball.dy>0:
                    sign_dy=+1
                else:
                    sign_dy=-1
                
                ball.dx=speed*sign_dx
                ball.dy=speed*sign_dy

                #reverse direction
                ball.dx*=-1
            
            if ball.xcor()<-390:
                #increase score of p2
                self.p2_score+=1
                if self.p2_score==win_score:
                    pen.clear()
                    pen.write("P2 wins!!!",align="center", font=("Courier", 20, "normal"))
                    ball.goto(0,0)
                    self.p1_score=0
                    self.p2_score=0
                    ball.direction='stop'
                    pen2.penup()
                    pen2.goto(0,40)
                    pen2.write("Press c to continue...",align="center", font=("Courier", 20, "normal"))
                else:
                    pen.clear()
                    pen.write("P1: {}  P2: {}".format(self.p1_score,self.p2_score), align="center", font=("Courier", 20, "normal"))
                
                ball.goto(0,0)
                #increase or decrease speed
                #getting the sign for the current 
                if ball.dx>0:
                    sign_dx=+1
                else:
                    sign_dx=-1
                    
                if ball.dy>0:
                    sign_dy=+1
                else:
                    sign_dy=-1
                
                ball.dx=speed*sign_dx
                ball.dy=speed*sign_dy
                #reverse direction
                ball.dx*=-1
        
        
def paddle_collision():
    if ball.xcor() > 340 and ball.xcor()<350 and (ball.ycor() < paddle_b.ycor()+40 and ball.ycor()> paddle_b.ycor()-40):
        #ball.xcor()<350 is for no glitch as while return it can cause
        #as length of paddle is 4*20 so the ball must hit b/w so that is the 2 and condition
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC | winsound.SND_FILENAME)
        ball.setx(340)
        #increase speed
        ball.dx+=0.1
        ball.dy+=0.08
        #reverse direction
        ball.dx*=-1
    if ball.xcor() <- 340 and ball.xcor()>-350 and (ball.ycor() < paddle_a.ycor()+40 and ball.ycor()> paddle_a.ycor()-40):
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC | winsound.SND_FILENAME)
        ball.setx(-340)
        #increase speed
        ball.dx-=0.08
        ball.dy-=0.1
        #reverse direction
        ball.dx*=-1    
               
#Listen to key press
wn.listen()
wn.onkeypress(paddle_a_up,'w')
wn.onkeypress(paddle_a_down,'s')
wn.onkeypress(paddle_b_up,'Up')
wn.onkeypress(paddle_b_down,'Down')
wn.onkeypress(continueOrNot,'c')


obj1=MoveBallClass(0,0)
while True:
    wn.update()
    obj1.move_ball()
    paddle_collision()


wn.mainloop()
