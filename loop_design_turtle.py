import turtle

t = turtle.Turtle()

t.speed(0)
turtle_spot = []

length = 200
angle = 170

times_around = 25


full_count = (360*times_around)/170


t.color("red","yellow")
t.begin_fill()

count = 0

while count < full_count:
  t.forward(length)
  t.left(angle)
  count += 1

t.end_fill()





