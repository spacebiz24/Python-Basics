# Write a program that reads a file and prints only those lines that contain the substring snake.

file = open("Unit 3/P13.txt", 'w')
numLines = int(input("Enter the number of lines: "))
for i in range(numLines):
    file.write(input("Enter a line: "))
    file.write("\n")
file.close()

file = open("Unit 3/P13.txt", 'r')
lst = file.readlines()
print("Lines which contain 'snake':")
for i in lst:
    if "snake" in i:
        print(i)
file.close()