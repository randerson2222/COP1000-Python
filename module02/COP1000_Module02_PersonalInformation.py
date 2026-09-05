# Module 2
# Project: Personal Information Form
"""
Program: COP1000_Module02_PersonalInformation.py
Author: Richard Anderson
Project: Personal Information Form
"""
print("== Personal Information Form ==")
# input
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")
career_interest = input("Enter your career interest: ")
# calculations
age_next_year = age + 1
# output
print("== Personal Information Summary ==")
print(f"Name: {first_name} {last_name}")
print(f"Age: {age}")
print(f"Age Next Year: {age_next_year}")
print(f"City: {city}")
print(f"Career Interest: {career_interest}")