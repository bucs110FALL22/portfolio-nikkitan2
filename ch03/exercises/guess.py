import random

num = random.randrange(1,11)
num_guesses = 0
correct_guess = False

for i in range(5):
  if not correct_guess: #flag variable
    guess_num = int(input("Please enter a guess"))
    #num_guesses = num_guesses + 1
    num_guesses += 1
    if guess_num > num:
      print("Your guess is too high")
    elif guess_num < num:
      print("Your guess is too low")
    else:
      print("Correct!")
      correct_guess = True

print("it took you", num_guesses, "to get it right.")