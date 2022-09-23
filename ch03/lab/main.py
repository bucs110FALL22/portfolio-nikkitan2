import turtle #1. import modules
import random

#Part A
window = turtle.Screen() # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle() # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up() # 4. Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. Your PART A code goes here
x = random.randrange(1,10)
print(x)
#Race 1
michelangelo.forward(50)
leonardo.forward(50)
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)
#Race 2
for i in range(10):
  michelangelo.forward(x)
  leonardo.forward(x)

michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

# PART B - complete part B here
import pygame
import math

cords = [(x1,y1),(x2,y2),(x3,y3)]
num_sides = 3
side_length = 20
offset =

for i in range():
  theta = (2.0 * math.pi * (loop increment variable))) / num_sides
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(thetha) + offset

pygame.draw.polygon(cords)

pygame.init()
window = pygame.display.set_mode()

window.exitonclick()