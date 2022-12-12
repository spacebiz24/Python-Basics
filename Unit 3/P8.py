# Write a Python program to generate random even integers in a specific numerical range using the random module.

import random
x = int(input("Enter the min limit: "))
y = int(input("Enter the max limit: "))
lim = int(input("Enter the number of iterations: "))
for i in range(lim):
    random.seed()
    num = random.randrange(x, y)
    if num % 2 == 0:
        print("Random Number: ", num)