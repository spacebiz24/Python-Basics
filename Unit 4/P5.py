# Design and implement a program that accepts two numbers separated by comma and performs a division of two numbers. Include exceptions for the necessary conditions with finally clause.

x, y = input("Enter two numbers seperated by a comma: ").split(',')
try:
    x = int(x)
    y = int(y)
    res = x / y
    print("Quotient is: ", res)
except ValueError:
    print("Enter a number!")
except ZeroDivisionError:
    print("Y must not be equal to zero")