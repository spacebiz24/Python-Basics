# Write Python program to replace comma-separated words with hyphens and print hyphen-separated words in ascending order.

x = input("Put it in:\n")
l = x.split(',')
l = sorted(l)
for i in range(len(l) - 1):
    print(l[i], end='-')
print(l[-1])
