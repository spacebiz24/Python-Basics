# Write a function named readposint that uses the input dialog to prompt the user for a positive integer and then checks the input to confirm that it meets the requirements. It should be able to handle inputs that cannot be converted to int, as well as negative ints.

class NegError(Exception):
    pass
def readposint():
    try:
        num = int(input("Enter a number: "))
        if num < 0:
            raise NegError
    except ValueError:
        print("String not allowed")
    except NegError:
        print("Negative number not allowed")

readposint()