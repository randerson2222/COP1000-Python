# Module 4
# Project: Guess the Number Game
"""
Program: COP1000_Module04_GuessTheNumber.py
Author: Richard Anderson
Project: Guess the Number Game
"""

import random

# range of random integer (min, max)
randint_min = 1
randint_max = 20

secret_number = random.randint(randint_min, randint_max)

print("Welcome to Guess the Number!\n")
print(f"I am thinking of a number from {randint_min} to {randint_max}.\n")

guess_counter = 0
while True:
  user_input = input("Enter your guess: ")
  try:
    user_number = int(user_input)
    guess_counter += 1
    if user_number == secret_number:
      print(f"\nCorrect!")
      print(f"You guessed the number in {guess_counter} attempts.")
      break
    elif user_number > secret_number:
      print("Too high. Try again.")
    elif user_number < secret_number:
      print("Too low. Try again.")
  except ValueError:
    print("Please enter a whole number. (input cannot be converted to integer)")