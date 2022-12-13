
#part a
def print_3n_plus_1_sequence(n: int) -> None:
  count = 0
  while n > 1:
    count += 1
    print(n)
    if n % 2 == 0:
      n = n // 2
    else:
      n = 3 * n + 1
  print(1)
  print("The number of iterations was: ", count)


print_3n_plus_1_sequence(101)
#part b
def calculate_3n_plus_1_iterations(upper_limit: int) -> None:
  iters = {}
  for start in range(2, upper_limit + 1):
    n = start
    count = 0
    while n > 1:
      count += 1
      if n % 2 == 0:
        n = n // 2
      else:
        n = 3 * n + 1
    iters[start] = count
  print(iters)

calculate_3n_plus_1_iterations(10)
#part c

def graph():
  import pygame
  pygame.init()
  window = pygame.display.set_mode((500,500))
  pygame.draw.rect(window, (225,225,225), (0,0,500,500))
  upper_limit = 20
  iters = {}
  max_so_far = 0
  max_val = 100
  scale = 5

  for i in range(2,upper_limit):
    count = 0
    n = i
    while n > 1:
        if n % 2==0:
            n = n/2
        else:
            n = n * 3 + 1
        count = count + 1
        iters[n] = count

    iters.items()
    print(iters[n])

  pygame.draw.line(window,(0,0,0),[0,250],[500,250],2)
  pygame.draw.line(window,(0,0,0),[250,0],[250,500],2)
  pygame.draw.line(window,(0,0,0),[123,123],[123,123],2)
  pygame.draw.line(window,(0,0,0),[123,123],[123,123],2)
  pygame.display.update()
  pygame.time.wait(5000)
  newWindow = pygame.transform.flip(window,False,True)
  window.blit(newWindow,(0,0))
  pygame.display.update()
  pygame.time.wait(5000)
  font = pygame.font.Font(None,20)
  msg = font.render("maximum number of iteration:" + str(max_so_far), True, (225,225,225))
  window.blit(msg,(10,10))
  pygame.display.update()
  pygame.time.wait(5000)
graph()