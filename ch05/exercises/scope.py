def multiplication(x, y):
  value = 0
  for i in range(x):
    value = value + y
  return value

def exponent(a, b):
  value = 1
  for i in range(a):
    value = value * b
  return value

def sqaure(num):
  return multiplication(num, num)

def main():
  value1 =  multiplication(x=5, y=6)
  print(value1)
  value2 = exponent(a=5, b=6)
  print(value2)
  value3 = sqaure(5)
  print(value3)

main()
