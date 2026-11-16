import importlib
import calculations
import messages

importlib.reload(calculations)
importlib.reload(messages)

messages.show_title()
print("")

a = 10
b = 5

ops = {
  "+": calculations.add,
  "-": calculations.subtract,
  "*": calculations.multiply,
  "/": calculations.divide
}

print("== Testing Section ==\n")

for string, function in ops.items():
  print(f"{a} {string} {b} = {function(a, b)}")

print("")

def input_float(message: str) -> float:
  while True:
    try:
      return float(input(message))
    except ValueError:
      print("Please enter a number.")

print("== User Input Section ==\n")

first = input_float("Enter the first number: ")
second = input_float("Enter the second number: ")

ops_2 = {
  "Sum": calculations.add,
  "Difference": calculations.subtract,
  "Product": calculations.multiply,
  "Quotient": calculations.divide
}

print("")

for string, function in ops_2.items():
  print(f"{string}: {function(first, second)}")

print("")

print("== Protect Division by Zero (Exercise 5 Section) ==\n")

print(f"{1} / {0} = {calculations.divide(1, 0)}")

print("")
messages.show_goodbye()
