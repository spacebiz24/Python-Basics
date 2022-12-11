# Write a Python program to check a string represent an integer or not.  
# Expected Output:
# Input a string: Python                                                  
# The string is not an integer.

str = input("Enter a string: ")
count = 0
for i in str:
    if i.isdigit():
        count += 1
if(count == len(str)):
    print("The entered string is an integer")
else:
    print("The entered string is not an integer")