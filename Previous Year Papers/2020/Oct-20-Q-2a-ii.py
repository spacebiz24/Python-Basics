# Write a python program to print the following pattern using nested for loop.
#     1
#    2 3
#   4 5 6
#  7 8 9 10
# 11 12 13 14

s = int(input("Enter number of rows: "))
m = (2 * s) - 2
num = 1
for i in range(0, s):
    for j in range(0, m):
        print(end=" ")
    m = m - 1
    for j in range(0, i + 1):
        print(num, end=" ")
        num += 1
    print()
