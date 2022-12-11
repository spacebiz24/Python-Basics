#  Design and implement a python program to get a new string from a give string where ‘is’ has been added to the front. If the string already begins with “is” the return the string unchanged.

str = input("Enter a string: ")
if str[:2] != "is":
    print("is" + str)
else:
    print(str)