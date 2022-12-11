# Design and implement a python program to count the number 4 in a given list.

list = [4,4,4,1,2,85,2,4,65,4]
count = 0
for i in list:
    if i == 4:
        count += 1
print("Number of 4's is: ", count)