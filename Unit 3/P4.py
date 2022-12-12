# Design and implement a program that reads a file and outputs a new file with the lines in a sorted order.

file = open("Unit 3/P4.txt", 'w')
numLines = int(input("Enter number of lines: "))
for i in range(numLines):
    file.write(input("Enter line: "))
    file.write("\n")
file.close()

file =open("Unit 3/P4.txt", 'r')
list = file.readlines()
list = sorted(list)
file.close()

file = open("Unit 3/P4_New.txt", 'w')
for i in range(numLines):
    file.write(list[i])
file.close()