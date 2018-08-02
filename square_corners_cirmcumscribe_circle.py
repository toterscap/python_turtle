import turtle
import math

t = turtle.Turtle()

color = input('what color')

length = int(input('what length?'))

t.color (color)


#draw square
corner_A = t.pos()
t.fd(length)
t.right(90)
corner_B = t.pos()
t.fd(length)
t.right(90)
corner_C = t.pos()
t.fd(length)
corner_D = t.pos()
t.right(90)
t.fd(length)

def drawCorners(corner1,corner2,corner3,corner4):
  t.pu()
  t.right(135)
  t.pd()
  t.goto(corner3)
  t.pu()
  t.goto(corner2)
  t.right(180)
  t.pd()
  t.goto(corner4)  
  
  
  

drawCorners(corner_A,corner_B,corner_C,corner_D)

#inscribe circle
t.home()
t.pu()
t.goto(corner_D)
t.fd(length/2)
t.pd()
t.circle(length/2,360)

#circumscribe circle
t.pu()
t.home()
t.right(135)
t.pd()


t.circle(math.sin(math.radians(45))*100)



print color
