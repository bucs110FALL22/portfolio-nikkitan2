import random
import turtle

def isinscreen(window, turt):
  turtleX = t.xcor()
  turtleY = t.ycor()
 
  x_range = wn.window_width()/2
  y_range = wn.window_height()/2

  if abs(turtleX) > x_range or abs(turtleY) > y_range:
    return False
  return True

t = turtle.Turtle()
wn = turtle.Screen()
t.shape('turtle')
t.speed(0)

distance = 10
angle = 90
is_in_screen = True

colors = ["green", "blue", "purple"]

while is_in_screen:
  coin = random.randrange(0,2)
  if coin == 0:
    t.left(angle)
  else:
    t.right(angle)
  t.forward(distance)
  
  t.color(colors[0])
  colors.append(colors.pop(0))
  

wn.bgcolor("yellow")
wn.exitonclick
