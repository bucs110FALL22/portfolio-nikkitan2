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
