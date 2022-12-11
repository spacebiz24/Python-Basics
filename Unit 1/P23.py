# Write a Python program to count the number of even and odd numbers from a series of numbers.

list = [1,4,56,23,132,67,92,345]
for i in list:
    if i % 2 == 0:
        print(i, " is even")
    else:
        print(i, " is odd")