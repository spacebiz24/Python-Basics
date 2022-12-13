# Write a Python class which has two methods get_String and print_String. get_String accept a string from the user and print_String print the string in upper case.

class String:
    def __init__(self):
        self.str = ""
    def get_String(self):
        self.str = input("Enter a string: ")
    def print_String(self):
        self.str = (self.str).capitalize()
        print("Modified String is:")
        print(self.str)

str = String()
str.get_String()
str.print_String()