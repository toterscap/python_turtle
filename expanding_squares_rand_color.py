import turtle
import random

t = turtle.Turtle()

def draw_square(t,size):
  for i in range(4):
    t.forward(size)
    t.right(90)

leg = 10
r= leg*234/255
g = leg*3/255
b = leg*50/255

count = 0
while count < 50:
  t.pu()
  t.goto((leg*-1)/2,leg/2)
  t.pd()
  
  r = random.randrange(0,255,1)
  g = random.randrange(0,255,1)
  b = random.randrange(0,255,1)
  t.pencolor((r,g,b))
  
  draw_square(t,leg)
  leg += 10
  count += 10

