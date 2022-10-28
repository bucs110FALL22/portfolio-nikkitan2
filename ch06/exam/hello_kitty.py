import turtle
import pygame

my_turtle = turtle.Turtle()
window = turtle.Screen()
window.bgcolor("pink")
my_turtle.color("green")
my_turtle.speed(1)


def draw(head):
  for i in range(2):    
    turtle.circle(head, 90)
    turtle.circle(head//2, 90)
turtle.seth(-45)
draw(100)
pygame.time.wait(2000)
