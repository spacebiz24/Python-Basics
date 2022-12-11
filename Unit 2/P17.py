# Write a Python program to generate and print a list except for the first 5 elements, where the values are square of numbers between 1 and 30 (both included)

list = []
for i in range(1, 30 + 1):
    list.append(i ** 2)
print("List is:")
print(list[5:])