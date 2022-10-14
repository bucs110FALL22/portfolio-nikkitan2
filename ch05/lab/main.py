import pygame
pygame.init()
pygame.font.Font(None, 20)

display = pygame.display.set_mode()

def seq3np1(n):
  n = 101
  
  upper_limit = 20
  iters = {}
  max_so_far = 
  for i in range(2, upper_limit + 1):
    count = 0
  while n > 1:
    print(n)
    if (n % 2) == 0:
      n = n // 2     
    else:
      n = 3 * n + 1
    count = count + 1
    iters[n] = (count)
      
    print(n)
    print(count)
    print(iters)
  
  
seq3np1(3)
