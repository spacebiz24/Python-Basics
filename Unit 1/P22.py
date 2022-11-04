print("Conversion between Fahrenheit and Celsius:")
print("Conversion from Celsius to Fahrenheit: 'F'")
print("Conversion from Fahrenheit to Celsius: 'C'")
choice = input("Enter the choice: ")
val = float(input("Enter the value to convert: "))
choice = choice.lower()
if choice == "c":
    C = (val - 32) * (5 / 9)
    print("Temperature in Celsius: ", C)
elif choice == "f":
    F = ((9 / 5) * val) + 32
    print("Temperature in Fahrenheit: ", F)
else:
    print("Invalid choice")