import random

num = random.randrange(1.11)
num_guesses = 1

for i in range(3):
  guess_num = int(input("Please enter a guess"))
  #num_guesses = num_guesses +1
  num_guesses += 1
  if guess_num > num:
    print("Your guess is too high")
  elif guess_num < num:
    print("Your guess is too low")
  else:
    print("Correct!")

print("it took you", num_guesses, "to get it right.")