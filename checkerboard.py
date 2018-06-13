import turtle

t = turtle.Turtle()
t.shape("turtle")
d = ['red', 'green', 'yellow', 'blue']
"""
t.getscreen()

screenWidth = t.window_width()
screenHeight = t.window_height()

t.write(screenWidth)
t.goto(30,0)
t.write(screenHeight)
"""
t.speed(0)

count = 0
y_position = 0

while count < 8:

  x=0
  
  while x < 8:
    t.pu()
    t.goto(75*x,y_position)
    t.pd()
    x=x+1
    for c in d:
      t.color(c)
      t.forward(75)
      t.left(90)
      t.write(c)
  t.pu()
  y_position += 75

  count += 1 
