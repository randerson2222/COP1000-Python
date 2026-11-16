"""
Module 9
Project: Bulletproof Calculator
Program: COP1000_Module09_BulletproofCalculator.py
Author: Richard Anderson
"""
def input_float(message):
  try:
    return float(input(message).strip())
  except ValueError:
    print("Invalid input. Please enter numeric values.")
    return None

def add(a, b):
  return a + b
def subtract(a, b):
  return a - b
def multiply(a, b):
  return a * b

def divide(a, b):
  try:
    return a / b
  except ZeroDivisionError:
    print("Error: You cannot divide by zero.")
    return None

supported_ops = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

"""
def test_op(op_str):
  input = "+"
  if input in supported_ops:
    print("supported")
    return True
  else:
    print("unsupported")
    return False
"""

def main():
  print("Bulletproof Calculator\n")
  first = input_float("Enter the first number: ")
  if first == None:
    return
  try:
    operation = supported_ops[input("Enter an operation (+, -, *, /): ").strip()]
    # print(operation)
    # print(type(operation))
  except KeyError:
    print("Invalid operation.")
    return
  second = input_float("Enter the second number: ")
  if second == None:
    return
  # if operation.__name__ == "divide":
  #   print("Division")
  #### how to implement one function having a different signature #######
  # if operation.__name__ == "three_args":
  #   result = operation(a, b, c)
  # else:
  #   result = operation(a, b)
  ########################################################################
  result = operation(first, second)
  # breakpoint()
  # print(result) # debugging
  if result != None:
    print(f"Result: {result}")

def main_loop():
  while True:
    main()
    print("")
    choice = input("run again? [y/n]: ").strip()
    if choice.casefold() != "y":
      return
    print("")

# test_op("+")
# main()
main_loop()