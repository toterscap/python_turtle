import math
import turtle

screen = turtle.Screen()
screen.bgcolor("pink")
turtle.pencolor("white")

t = turtle.Turtle()
t.speed(0)

start = t.position()

def draw_rectangle(width,length,color,pen_color):
  t.fillcolor(color)
  t.begin_fill()
  t.pencolor(pen_color)
  t.forward(width)
  t.right(90)
  t.forward(length)
  t.right(90)
  t.forward(width)
  t.right(90)
  t.forward(length)
  t.right(90)
  t.end_fill()

def draw_triange(leg,color):
  t.fillcolor(color)
  t.begin_fill()
  t.left(60)
  t.forward(leg)
  t.right(120)
  t.forward(leg)
  t.right(120)
  t.forward(leg)
  t.end_fill()



draw_rectangle(100,100,"black","white")
draw_triange(100,"yellow")

t.penup()
t.left(90)
t.forward(100)
t.left(90)
t.forward(50)
t.pendown()

draw_rectangle(25,-50,"white","white")
