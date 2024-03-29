from turtle import *
#setting up screen
screen = Screen()
screen.bgcolor("Pink")
screen.title("Simple house on Python...")
screen.setworldcoordinates(-2, -4, 15, 15)
#creating a turtle
pen = Turtle()
pen.color("brown")
#creating front outline
height = 4
length = 9
pen.begin_fill()
pen.fillcolor("NavajoWhite")
for i in range(2):
   
    pen.forward(length)
    pen.left(90)
    pen.forward(height)
    pen.left(90)
pen.end_fill()
#creating right side face of house
pen.penup()
pen.goto(9,4)
pen.pendown()
pen.begin_fill()
pen.fillcolor("NavajoWhite")
pen.setheading(45)
pen.penup()
pen.forward(length/2)
pen.pendown()
pen.setheading(270)
pen.forward(height)
pen.goto(9,0)
pen.seth(90)
pen.forward(height)
pen.end_fill()
#creating top right roof of the house
pen.begin_fill()
pen.fillcolor("NavajoWhite")
pen.setheading(45)
pen.penup()
pen.forward(length/2)
pen.pendown()
pen.goto(10.6,8)
pen.goto(9,4)
pen.end_fill()
#creating roof of the house
pen.begin_fill()
pen.fillcolor("darkblue")
pen.goto(10.6,8)
pen.seth(181)
pen.forward(length-1)
pen.goto(0,4)
pen.seth(0)
pen.forward(length)
pen.end_fill()
# creating door
pen.penup()
pen.goto(4,0)
pen.begin_fill()
pen.fillcolor("dark red")
for i in range(2):
    pen.forward(1)
    pen.left(90)
    pen.forward(2)
    pen.left(90)
pen.end_fill()
pen.hideturtle()

screen.exitonclick()