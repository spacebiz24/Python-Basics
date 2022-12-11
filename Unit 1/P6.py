# Design and implement a python program to test whether a number is within 100 of 1000 0r 2000.

x = int(input("Enter a number: "))
if (abs(x - 1000) <= 100 or abs(x - 2000) <= 100):
    print("Number passes the test!")
else:
    print("Number fails the test!")