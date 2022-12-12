# Write a Python program to print a string five times, delay three seconds using the time module.

import time
str = input("Enter a string: ")
for i in range(5):
    time.sleep(3)
    print(str)