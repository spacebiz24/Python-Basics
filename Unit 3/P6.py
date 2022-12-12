# Write a Python program to count the number of lines in a text file.

file = open("Unit 3/P6.txt", "w")
num = int(input("Enter the number of lines: "))
for i in range(num):
    file.write(input("Enter the line: "))
    file.write("\n")
file.close()

file = open("Unit 3/P6.txt", "r")
lines = file.readlines()
print ("Number of lines:", len(lines))
file.close()