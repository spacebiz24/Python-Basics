# Write a Python program to construct the following pattern, using a nested loop number
# Expected Output:
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777

x = int(input("Enter a arange of series: "))
for i in range(1, x + 1):
    for j in range(1, i + 1):
        print(i, end = "")
    print(end = "\n")