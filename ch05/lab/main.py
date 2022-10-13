def seq3np1(n):
  while n!= 1 and n > 0:
    print(n)
    if (n % 2) == 0:
      n = n // 2
    else:
      n = 3 * n + 1
  print(n)
  
seq3np1(3)
