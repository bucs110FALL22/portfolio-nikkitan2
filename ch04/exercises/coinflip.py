import turtle
import random

my_turtle = turtle.Turtle()
window = turtle.Screen()
window.bgcolor("white")
my_turtle.shape("turtle")
my_turtle.color("pink")


def cointoss():
  return random.choice(["heads","tails"])
  side = random.randint("heads","tails")
  if (side = "heads"):
    my_turtule