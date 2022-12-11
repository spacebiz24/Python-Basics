# Design and implement a python program to get a string made of the first 2 and the last 2 chars from a given string. If the string length is less than 2 return instead the empty string.

str = input("Enter a string: ")
if(len(str) <= 2):
    nstr = ""
else:
    nstr = str[:2] + str[len(str)-2:]
print("New String is: ", nstr)