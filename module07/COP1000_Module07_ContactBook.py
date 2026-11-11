"""
Module 7
Project: Contact Book Application
Program: COP1000_Module07_ContactBook.py
Author: Richard Anderson
"""
contact_book = {
    "Joe": {
        "phone": "555-5555",
        "email": "example@example.com"
    },
    "Alex": {
        "phone": "555-1234",
        "email": ""
    },
    "Jordan": {
        "phone": "555-5678",
        "email": ""
    },
}
def present_contact_record(record):
  try:
    print(f"\tPhone: {record["phone"]}")
  except KeyError:
    print("phone key missing")
  try:
    print(f"\tEmail: {record["email"]}")
  except KeyError:
    print("email key missing")
def find_byname(contact_book):
  # print("find")
  name_str = input("enter name: ").strip()
  try:
    record = contact_book[name_str]
  except KeyError:
    print("no contact exists with this name")
    return False
  present_contact_record(record)
  return True
def add_contact(contact_book):
  # print("add")
  print("== Add a new contact (will replace existing contacts) ==")
  name_str = name_str = input("enter name: ").strip()
  while not name_str:
    print("name can't be empty")
    name_str = input("enter name: ").strip()
  phone_str = input("enter phone: ").strip()
  email_str = input("enter email: ").strip()
  contact_book[name_str] = {
      "phone": phone_str,
      "email": email_str
  }
  print(f"{name_str}")
  present_contact_record(contact_book[name_str])
  print("added.")
def del_byname(contact_book):
  # print("del")
  name_str = input("enter name: ").strip()
  try:
    del contact_book[name_str]
  except KeyError:
    print("no contact exists with this name")
    return False
  print(f"{name_str} deleted.")
  return True
def present_names(contact_book):
  for name in contact_book:
    print(name)
def present_contacts(contact_book):
  for name, record in contact_book.items():
    print(f"{name}")
    present_contact_record(record)
def print_dict(contact_book):
  print(contact_book)
menu_dict = {
    "f": {
        "title": "Find a Contact by Name",
        "func_name": find_byname
    },
    "a": {
        "title": "Add a Contact",
        "func_name": add_contact
    },
    "d": {
        "title": "Delete a Contact",
        "func_name": del_byname
    },
    "s": {
        "title": "Show All Contacts (names only)",
        "func_name": present_names
    },
    "ss": {
        "title": "Show All Contacts (complete)",
        "func_name": present_contacts
    },
    "pd": {
       "title": "Print Dict (for debugging)",
       "func_name": print_dict
    }
}
def present_menu(contact_book, menu_dict):
  for key, value in menu_dict.items():
        print(f"{key}. {value["title"]}")
def validate_q(str):
  if str.strip() == "q":
    return True
  else:
    return False
def menu_loop(contact_book, menu_dict):
  while True:
    print("== Menu ==")
    present_menu(contact_book, menu_dict)
    print("q. Quit")
    input_str = input("input: ").strip()
    if validate_q(input_str):
      return
    try:
      menu_dict[input_str]["func_name"](contact_book)
    except KeyError:
      print("menu item does not exist")
menu_loop(contact_book, menu_dict)