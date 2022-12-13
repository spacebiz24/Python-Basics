# Write an interactive program to compute the square root of a number. The input values must be tested for validity. If it is negative the user defined method MySqrt() should raise an exception.

class NegError(Exception):
    pass

def MySqrt():
    num = input("Enter a number: ")
    try:
        num = int(num)
        if num < 0:
            raise NegError
        res = num ** 0.5
        print("Square root is: ", res)
    except ValueError:
        print("Enter a number!")
    except NegError:
        print("Enter a positive number!")

MySqrt()