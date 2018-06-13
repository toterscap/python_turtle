import turtle

t = turtle.Turtle()

radius = 100
count = 10

while count > 1:
  if count % 2 == 0:
    t.color("blue")
  else:
    t.color("green")
  t.begin_fill()
  t.circle(radius)
  t.pu()
  t.left(90)
  t.forward(10)
  t.right(90)
  t.pd()
  radius -= 10
  t.end_fill()
  count -= 1
