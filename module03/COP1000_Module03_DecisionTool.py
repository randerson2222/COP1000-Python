# Module 3
# Project: Decision-Making Tool
"""
Program: COP1000_Module03_DecisionTool.py
Author: Richard Anderson
Project: Decision-Making Tool
"""

rain_rec = "Consider reading a book indoors."
cool_rec = "Consider roasting marshmallows."
outdoor_rec = "Consider going hiking in a state park."
hot_rec = "Consider going swimming."

outdoor_thres = 60
hot_thres = 85

def input_float(message: str) -> float:
  input_good = False
  while(input_good == False):
    user_input = input(message)
    try:
      user_float = float(user_input)
      input_good = True
    except ValueError:
      print("Please enter a number.")
      input_good = False
  return user_float

def input_yesno(message: str) -> bool:
  input_good = False
  while(input_good == False):
    user_input = input(message)
    if user_input.casefold() == "yes":
      user_bool = True
      input_good = True
    elif user_input.casefold() == "no":
      user_bool = False
      input_good = True
    else:
      print("Please enter yes or no.")
      input_good = False
  return user_bool

temperature = input_float("What is the current temperature (Fahrenheit)? ")
is_raining = input_yesno("Is it raining (yes/no)? ")

# print(f"current temperature: {temperature}")
# print(f"is_raining: {is_raining}")

print("\nRecommendation: ", end="")

if is_raining == True:
  print(rain_rec)
elif temperature < outdoor_thres:
  print(cool_rec)
elif temperature >= outdoor_thres and temperature < hot_thres:
  print(outdoor_rec)
else:
  print(hot_rec)