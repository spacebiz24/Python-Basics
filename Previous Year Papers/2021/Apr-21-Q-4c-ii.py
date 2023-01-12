# Write a Python program to convert a tuple to a dictionary.
# Sample Input: ((2, "w"),(3, "r"))
# Sample Output:{'w': 2, 'r': 3}

tup = ((2, "w"), (3, "r"))
l = list(tup)
d = {}

for i in range(len(l)):
    d[l[i][1]] = l[i][0]

print(d)
