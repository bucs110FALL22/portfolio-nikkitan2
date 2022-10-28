import turtle
import pygame

t = turtle.Turtle()
window = turtle.Screen()
window.bgcolor("black")
t.color("white")
t.speed(15)
t.pensize(10)

def draw(r):
  for i in range(2):
    t.circle(r,90)      
    t.circle(r//2,90)
t.seth(-45)

t.fillcolor("white")
t.begin_fill()
draw(100)
t.end_fill()

t.begin_fill()
t.penup()
t.goto(20,100)
t.pendown()
draw(20)
t.end_fill()

t.begin_fill()
t.penup()
t.goto(50,110)
t.pendown()
draw(25)
t.end_fill()

t.begin_fill()
t.penup()
t.goto(90,100)
t.pendown()
draw(20)
t.end_fill()

pygame.time.wait(2000)

t.color("black")
t.penup()
t.goto(90,50)
t.pendown()
t.goto(100,50)

t.penup()
t.goto(40,50)
t.pendown()
t.goto(50,50)
