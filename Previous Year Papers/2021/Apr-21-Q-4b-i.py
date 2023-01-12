#  Write a Python program to sort a list of tuples by second Item.

l = [(12, 34, 3), (3, 4, 5), (45, 65, 23), (22, 54, 6), (34, 223, 21)]

for i in range(len(l)):
    for j in range(i - 1):
        if (l[j][1] > l[j + 1][1]):
            temp = l[j]
            l[j] = l[j + 1]
            l[j + 1] = temp
        else:
            continue

print(l)
