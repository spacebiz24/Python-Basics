# Write a program that reads a file and writes out a new file with the lines in reversed order (i.e. the first line in the old file becomes the last one in the new file.)

file = open("Unit 3/P10.txt", 'w')
num = int(input("Enter the number of lines to enter: "))
for i in range(num):
    file.write(input("Enter a line: "))
    file.write("\n")
file.close()

file = open("Unit 3/P10.txt", 'r')
lines = file.readlines()
file.close()

file = open("Unit 3/P10_New.txt", 'w')
for i in range(len(lines)):
    file.write(lines[len(lines) - i - 1])
file.close()
