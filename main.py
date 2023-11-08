#This is a small program to imitate the Hirst's dot paintings using turtle module:
from turtle import Turtle,Screen
import random

color_list = [(233, 242, 236), (208, 158, 96), (234, 213, 101), (41, 104, 144), (149, 78, 57), (130, 168, 194), (202, 137, 162)]
tim = Turtle()
# tim.hideturtle()
#Penup for the turtle:

tim.penup()
tim.shape('turtle')

#Set the initial position of the turtle to (-200,-200):

tim.setx(-200)
tim.sety(-200)
tim.pensize(20)
screen = Screen()
screen.colormode(255)
for i in range(0, 10):
    tim.sety(-200 + 50*i)
    tim.setx(-200)
    for j in range(0,10):
        tim.pencolor(random.choice(color_list))
#To change the dot size:
        tim.dot(20)
        tim.forward(50)


screen.exitonclick()



