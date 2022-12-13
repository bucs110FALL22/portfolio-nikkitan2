import pygame
pygame.init()
w = 250
h = 250
display = pygame.display.set_mode(size=(w, h))
font = pygame.font.Font(None, 25)
font_color = "pink"
font_pos = (15, 15)
line_color = "pink"

upper_limit = 20
iters = {}
max_so_far = 0
max_val = 0
scale = 5

new_display = pygame.transform.flip(display, False, True)

num = []

stop = upper_limit + 1
start = 2

coords = []
iters_c = {}

def print_3n_plus_1_sequence(n):
 count = 0
 while True:
   if n == 1:
     break
   if n % 2 == abs(1):
     n = 3 * n + 1
     num.append(n)
     
     count +=1
   
   elif n % 2 == 0:
     n = n/2

     num.append(n)
     count +=1
 return count

for i in range(start, stop):
  count = print_3n_plus_1_sequence(i)
  iters[i] = count
  iters_c[i * scale] = h - count * scale
  coords = list(iters_c.items())

  if count > max_so_far:
    max_so_far = count
    max_val = str(max_so_far)
    display.blit(new_display, (0,0))
    msg = font.render("the max value is " + max_val, True, font_color)
    display.blit(msg, font_pos)
    pygame.display.flip()
   
  if i > start+1:
   pygame.draw.lines(display, line_color, False, coords)
   pygame.display.flip()

  pygame.time.wait(500)
max_val = max_so_far 
print("iters:", iters)

pygame.time.wait(5000)