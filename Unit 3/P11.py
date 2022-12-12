# Write a Python program to generate a series of unique random numbers using the random module.

import random
lst = []
lim = int(input("Enter limit of series: "))
for i in range(lim):
    random.seed()
    if i not in lst:
        lst.append(random.randrange(0, 100))
print(lst)