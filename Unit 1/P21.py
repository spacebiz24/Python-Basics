#  Write a Python program that accepts a string and calculate the number of digits and letters.
# Sample Data : Python 3.2
# Expected Output :
# Letters 6 
# Digits 2

str = input("Enter a string: ")
lcount = 0
dcount = 0
for i in str:
    if i.isalpha():
        lcount += 1
    if i.isdigit():
        dcount += 1
print("Letters ", lcount)
print("Digits ", dcount)