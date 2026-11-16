"""
Module 8
Project: Persistent Data Logger
Program: COP1000_Module08_DataLogger.py
Data File: activity_log.csv
Author: Richard Anderson
"""
import csv

def input_int(message: str) -> int:
  while True:
    try:
      return int(input(message).strip())
    except ValueError:
      print("Please enter an integer.")

print("Activity Data Logger\n")

header = ["Activity", "TimeInMinutes"]

with open("activity_log.csv", mode="w", newline="", encoding="utf-8") as file:
  writer = csv.writer(file)
  writer.writerow(header)
  for i in range(1,4):
    activity = input(f"Enter activity {i}: ").strip()
    time_in_minutes = input_int("Minutes: ")
    row = [activity, time_in_minutes]
    writer.writerow(row)
    print("")

print("Data saved successfully.\n")

print("--- Saved Activity Log ---\n")

with open("activity_log.csv", mode="r", newline="", encoding="utf-8") as file:
  reader = csv.reader(file)

  # Skip the header row, return None if file empty
  next(reader, None)

  for row in reader:
    print(f"Activity: {row[0]} | Minutes: {row[1]}")