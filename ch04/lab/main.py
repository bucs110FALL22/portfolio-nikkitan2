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

while True:
  red_button = pygame.draw.rect(window, red, [0, 0, 100, 200],)
  blue_button = pygame.draw.rect(window, blue, [0, 100, 100, 200],)
  pygame.display.flip()
  mouse_x, mouse_y = pygame.mouse.get_pos()
  for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONDOWN:
      if blue_button.collidepoint(mouse_x, mouse_y):
        team = "blue"
      else:
        team = "red"

team = input("pick player red or blue:")