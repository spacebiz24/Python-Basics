# Write a Python program that allows the user to enter a four-digit binary number and displays its value in base 10. Each binary digit should be entered one per line, starting with the leftmost digit , as shown below.
# Enter leftmost digit: 1
# Enter the next digit: 0
# Enter the next digit: 0
# Enter the next digit: 1      
# The value is 9

print("Binary to Decimal converter: ")
digit0 = int(input("Enter the leftmost digit: "))
digit1 = int(input("Enter the next digit: "))
digit2 = int(input("Enter the next digit: "))
digit3 = int(input("Enter the rightmost digit: "))
val = digit0 * 1 + digit1 * 2 + digit2 * 4 + digit3 * 8
print("The value is: ", val)