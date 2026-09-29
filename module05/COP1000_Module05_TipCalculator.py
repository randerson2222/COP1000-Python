# Module 5
# Project: Tip Calculator Utility
"""
Program: COP1000_Module05_TipCalculator.py
Author: Richard Anderson
Project: Tip Calculator Utility
"""

def input_float(message: str) -> float:
  while True:
    try:
      return float(input(message))
    except ValueError:
      print("Please enter a number.")

def calculate_tip(bill: float, tip_percent: float) -> float:
  tip_rate = tip_percent / 100
  return bill * tip_rate

def calculate_total(bill: float, tip: float) -> float:
  return bill + tip

# get user input
print("=== Tip Calculator ===")
bill = input_float("Enter the bill amount:   $")
tip_percent = input_float("Enter the tip percentage: ")
print("")

# calculate
tip = calculate_tip(bill, tip_percent)
total = calculate_total(bill, tip)

# display
print(f"Bill:  ${bill:.2f}")
print(f"Tip:   ${tip:.2f}")
print(f"Total: ${total:.2f}")