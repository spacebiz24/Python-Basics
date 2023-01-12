# Write a Python program to replace last value of tuples in a list.
# Sample input:[(10, 20, 40), (40, 50, 60), (70, 80, 90)]
# Output:[(10, 20, 100), (40, 50, 100), (70, 80, 100)]

l = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
l_elem = []

for i in range(len(l)):
    l_elem.append(list(l[i]))

for i in range(len(l_elem)):
    l_elem[i][2] = 100

l_new = []

for i in range(len(l_elem)):
    l_new.append(tuple(l_elem[i]))

print(l_new)
