import pygame
pygame.init()
pygame.font.Font(None, 20)

display = pygame.display.set_mode()

def seq3np1(n):
 # Start with the given integer
  n = 101

# Keep generating new terms in the sequence until n reaches 1
  while n != 1:
  # If n is even, divide it by 2 to get the next term in the sequence
    if n % 2 == 0:
      n = n // 2
  # If n is odd, multiply it by 3 and add 1 to get the next term in the sequence
    else:
      n = 3 * n + 1
  
  # Print the current term in the sequence
    print(n)
