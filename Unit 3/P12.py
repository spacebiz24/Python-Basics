# Write a Python program to read a file line by line and store it into a list.
# Write a python program to find the longest words.

file = open("Unit 3/P12.txt", 'w')
numLines = int(input("Enter the number of lines: "))
for i in range(numLines):
    file.write(input("Enter a line: "))
    file.write("\n")
file.close()

file = open("Unit 3/P12.txt", 'r')
lst = []
lst = file.readlines()
maxLen = len(lst[0])
for i in lst:
    if len(i) > maxLen:
        maxLen = len(i)
        lstr = i
print("List is:")
print(lst)
print("Biggest String is: " + lstr)
file.close()