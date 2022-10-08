import pygame
import random
import math

#part a
pygame.init()
screen = pygame.display.set_mode()

size = pygame.display.get_window_size()

screen_width = 250
screen_height = 250
screen = pygame.display.set_mode([screen_width, screen_height])

screen.fill('blue')
pygame.draw.circle(screen, ('orange'), (125,125), 125)
pygame.draw.line(screen, ('black'), (125,0), (125,250), width=2)
pygame.draw.line(screen, ('black'), (0,125), (250,125), width=2)
pygame.display.flip()

#part b
for i in range(10):
  x = random.randrange (0,251)
  y = random.randrange (0,251)
  coords = (x,y)
  
  distance_from_center = math.hypot(x-125, y-125)
  is_in_circle = distance_from_center <= 250/2

  pygame.time.wait(500)
  if is_in_circle == True:
    pygame.draw.circle(screen, ('yellow'), coords, 5, 0)
  if is_in_circle == False:
    pygame.draw.circle(screen, ('pink'), coords, 5, 0)
    
  pygame.display.flip()
  
#part c
window = pygame.display.set_mode()
playerChoice = ""
leftRect = pygame.Rect(0, 0, x/2, y)
rightRect = pygame.Rect(x/2, 0, x/2, y)
redBTn = pygame.draw.rect(window, "red", leftRect)
blueBTn = pygame.draw.rect(window, "blue", rightRect)
pygame.display.flip()
print("who do you think will win?")
print("red or blue?")
awaitingGuess = True
while awaitingGuess == True:
  for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONDOWN:
      if event.pos[0] < x/2:
        playerChoice = "red"
        awaitingGuess = False
      elif event.pos[0] > x/2:
        playerChoice = "blue"
        awaitingGuess = False
print("you chose", playerChoice)
pygame.display.flip()
pygame.time.wait(500)
