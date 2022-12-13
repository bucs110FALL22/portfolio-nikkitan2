# Import the Pygame library and initialize the game engine
import pygame
pygame.init()

# Set the upper limit and initialize the dictionary and maximum value
upper_limit = 20
iters = {}
max_so_far = 0

# Iterate over all positive integers from 2 to upper_limit
for start in range(2, upper_limit+1):
  # Initialize the counter to 0 and the starting value
  count = 0
  n = start

  # Keep generating new terms in the 3n+1 sequence until n reaches 1
  while n != 1:
    # If n is even, divide it by 2 to get the next term in the sequence
    if n % 2 == 0:
      n = n // 2
    # If n is odd, multiply it by 3 and add 1 to get the next term in the sequence
    else:
      n = 3 * n + 1

    # Increment the counter to keep track of the number of iterations
    count += 1

  # Store the number of iterations in the dictionary and update the maximum value if necessary
  iters[start] = count
  if count > max_so_far:
    max_so_far = count

# Set the screen dimensions and create the screen object
screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the background color to white and clear the screen
bg_color = (255, 255, 255)
screen.fill(bg_color)
