
def seq3np1(n):
  n = 101
  count = 0
  while n > 1:
    print(n)
    if (n % 2) == 0:
      n = n // 2 
    else:
      n = 3 * n + 1
    count = count + 1
      
    print(n)
    print(count)
  
  
seq3np1(3)
