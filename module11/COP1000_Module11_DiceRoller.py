"""
Module 11
Project: Custom Dice Roller Engine
Program: COP1000_Module11_DiceRoller.py
Author: Richard Anderson
"""
import importlib
import dice_tools

importlib.reload(dice_tools)

# print(dice_tools.roll_die(6))

def input_int(message: str):
  while True:
    try:
      return int(input(message).strip())
    except ValueError:
      print("Please enter an integer.")

def input_sides(message: str):
  while True:
    sides = input_int(message)
    if sides > 0:
      return sides
    else:
      print("Number of sides must be greater than zero.")

def main():
  print("Custom Dice Roller\n")

  num_sides = input_sides("How many sides should each die have? ")
  num_rolls = input_int("How many dice should be rolled? ")

  print("")

  total = 0
  for roll in range(1, num_rolls + 1):
    result = dice_tools.roll_die(num_sides)
    print(f"Roll {roll}: {result}")
    total += result
  print(f"\nTotal: {total}")

def main_loop():
  while True:
    main()
    print("")
    choice = input("run again? [y/n]: ").strip()
    if choice.casefold() != "y":
      return
    print("")

main_loop()
