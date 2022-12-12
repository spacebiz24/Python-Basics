# Write a Python program to get a single random element from a specified string.

import random
str = input("Enter a string: ")
num = int(input("Number of iterations: "))
for i in range(num):
    random.seed()
    print(random.choice(str))
