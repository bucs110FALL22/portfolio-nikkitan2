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

x = random.randrange(0,10)
print(x)
#Race 1
michelangelo.speed(1)
leonardo.speed(1)
michelangelo.forward(50)
leonardo.forward(50)
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)
#Race 2
for i in range(10):
  michelangelo.speed(1)
  leonardo.speed(1)
  michelangelo.forward(x)
  leonardo.forward(x)

michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

michelangelo.clear()
leonardo.clear()

# PART B - complete part B here
import pygame
import math
pygame.init()

window = pygame.display.set_mode()
window.fill('ghostwhite')
pygame.display.flip()

coords = []

#equilateral triangle
num_sides = 3
side_length = 50
offset = 100

for i in range(num_sides):
  theta = (2.0 * math.pi * (i)) / num_sides
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords.append([x,y])

window.fill('ghostwhite')
pygame.display.flip()

pygame.draw.polygon(window,"blue",coords)
pygame.display.flip()
pygame.time.wait(2000)

window.fill("ghostwhite")
pygame.display.flip()


#square
coords = []
num_sides = 4

for i in range(num_sides):
  theta = (2.0 * math.pi * (i)) / num_sides
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords.append([x,y])

pygame.draw.polygon(window,"blue",coords)
pygame.display.flip()
pygame.time.wait(2000)

window.fill("ghostwhite")
pygame.display.flip()

#hexagon
coords = []
num_sides = 6

for i in range(num_sides):
  theta = (2.0 * math.pi * (i)) / num_sides
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords.append([x,y])

pygame.draw.polygon(window,"blue",coords)
pygame.display.flip()
pygame.time.wait(2000)

window.fill("ghostwhite")
pygame.display.flip()

#nonagon
coords = []
num_sides = 9

for i in range(num_sides):
  theta = (2.0 * math.pi * (i)) / num_sides
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords.append([x,y])

pygame.draw.polygon(window,"blue",coords)
pygame.display.flip()
pygame.time.wait(2000)

#circle-ish
coords = []
num_sides = 360

for i in range(num_sides):
  theta = (2.0 * math.pi * (i)) / num_sides
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords.append([x,y])

pygame.draw.polygon(window,"blue",coords)
pygame.display.flip()
pygame.time.wait(2000)

window.fill("ghostwhite")
pygame.display.flip()




