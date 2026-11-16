"""
Module 10
Project: Library Management System
Program: COP1000_Module10_LibrarySystem.py
Author: Richard Anderson
"""
class Book:
  def __init__(self, title, author, availability=True):
    self.title = title
    self.author = author
    self.availability = availability
  def display_info_basic(self):
    print(f"Title: {self.title}")
    print(f"\tAuthor: {self.author}")
    print(f"\tAvailable: {self.availability}")
  def display_info(self):
    print(f"{self.title} by {self.author} - ", end="")
    if self.availability == True:
      print("Available")
    else:
      print("Checked Out")
  def check_out(self):
    self.availability = False

books = [Book("Python Fundamentals", "A. Smith"),
         Book("Learning to Code", "J. Taylor"),
         Book("Programming Logic", "M. Jones")]

def display_books(books):
  for index, book in enumerate(books, start=1):
    print(f"{index}. ", end="")
    book.display_info()

print("Library Catalog\n")
display_books(books)
print("")

books[1].check_out()

print("Updated Library Catalog\n")
display_books(books)