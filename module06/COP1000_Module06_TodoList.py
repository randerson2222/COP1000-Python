# Module 6
# Project: To-Do List Manager
"""
Program: COP1000_Module06_TodoList.py
Author: Richard Anderson
Project: To-Do List Manager
Notes: Can only enter 3 to-do list items.
"""

NUMBER_OF_TASKS = 3

def display_list_numbered(my_list: list) -> None:
  for index, item in enumerate(my_list):
    print(f"{index + 1}. {item}")

def display_todo_list(task_list: list) -> None:
  print("--- My To-Do List ---\n")
  display_list_numbered(task_list)
  print(f"\nTotal Tasks: {len(task_list)}")

def collect_tasks(length: int) -> list:
  """Collect length number of tasks from the user"""
  task_list = []
  print(f"Enter {length} tasks.\n")

  while len(task_list) < length:
    current_slot = len(task_list) + 1
    user_input = input(f"Enter task {current_slot}: ").strip()

    if user_input:  # prevents adding empty tasks
      task_list.append(user_input)
    else:
      print(f"Task {current_slot} is empty. Try again.")

  return task_list

def manage_completion(task_list: list) -> None:
  """User interaction for completing/removing tasks"""
  print("--- Task Completion Manager ---")
  while task_list:  # while task_list is not empty
    print("")
    display_todo_list(task_list)
    user_input = input("\nEnter the number of the task you completed or quit with 'q': ").strip()
    if user_input.casefold() == "q":
      return
    try:
      choice = int(user_input)
      if 1 <= choice <= len(task_list):
        del task_list[choice - 1]
      else:
        print(f"Task number {choice} does not exist.")
    except ValueError:
      print("Invalid input. Please enter a number or 'q'.")
  print("\nAll items marked completed!")

def main():
  num_tasks = NUMBER_OF_TASKS

  print("=== To-Do List Manager ===\n")
  task_list = collect_tasks(num_tasks)

  if task_list:  # only run manage completion if the list is not empty
    print("")
    display_todo_list(task_list)
    print("")
    manage_completion(task_list)
  else:
    print("\nThere are no tasks.")

  print("\nBye.")

main()