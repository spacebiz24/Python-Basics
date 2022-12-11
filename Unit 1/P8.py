# Write a python program that asks the user how many coins of various types they have, and then print the total amount of money in rupees.

print("Standard coin notations available:")
print("1, 2, 5 Rupees")
c1 = int(input("Enter the number of Ru.1 coins you have: "))
c2 = int(input("Enter the number of Ru.2 coins you have: "))
c5 = int(input("Enter the number of Ru.5 coins you have: "))
sum = c1 * 1 + c2 * 2 + c5 * 5
print("Total amount: ", sum)