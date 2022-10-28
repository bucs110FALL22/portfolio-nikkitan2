import turtle
import pygame

t = turtle.Turtle()
window = turtle.Screen()
window.bgcolor("black")
t.hideturtle()
t.color("white")
t.speed(15)
t.pensize(10)
t.fillcolor("white")

def draw(r):
  for i in range(2):
    t.circle(r,90)      
    t.circle(r//2,90)
t.seth(-45)


t.begin_fill()
draw(100)
t.end_fill()

def move(x, y):
  t.begin_fill()
  t.penup()
  t.goto(x,y)
  t.pendown()
  draw(23)
  t.end_fill()

move(20, 100)
move(55, 110)
move(90,100)

t.pensize(5)
t.color("black")
t.penup()
t.goto(90,50)
t.pendown()
t.goto(100,50)

t.penup()
t.goto(40,50)
t.pendown()
t.goto(50,50)
pygame.time.wait(2000)