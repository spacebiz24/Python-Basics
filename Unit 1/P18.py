print("Binary to Decimal converter: ")
digit0 = int(input("Enter the leftmost digit: "))
digit1 = int(input("Enter the next digit: "))
digit2 = int(input("Enter the next digit: "))
digit3 = int(input("Enter the rightmost digit: "))
val = digit0 * 1 + digit1 * 2 + digit2 * 4 + digit3 * 8
print("The value is: ", val)