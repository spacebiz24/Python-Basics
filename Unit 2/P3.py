# Design and implement a python program to generate and print list except the first 5 elements, where the values are square of numbers between 1 and 30(both included).

list = []
for i in range(1, 30 + 1):
    list.append(i ** 2)
print(list[6:])