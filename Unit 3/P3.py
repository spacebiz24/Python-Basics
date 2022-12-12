# Design and implement a program to open a file and count the occurrences of each letter in the file.

file = open("Unit 3/P3.txt", 'w')
file.write(input("Enter a string: "))
file.close()

file = open("Unit 3/P3.txt", 'r')
diction ={}
for i in file.read():
    if i.lower().isalpha():
        if i in diction:
            diction[i] += 1
        else:
            diction[i] = 1
print(diction)
file.close()