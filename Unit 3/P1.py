# Design and implement a program to create and read the contents of a file that resembles a phone book with names and phone numbers. Now alphabetically sort the phonebook.

file = open("Unit 3/P1.txt", 'w')
num = int(input("Enter the number of contacts to enter: "))
for i in range(num):
    file.write(input("Enter the name: "))
    file.write(", ")
    file.write(input("Enter the number: "))
    file.write("\n")
file.close()
file = open("Unit 3/P1.txt", "r")
names = list(file.readlines())
names = sorted(names)
file.close()
file = open("Unit 3/P1.txt", "w")
for i in range(len(names)):
    file.write(names[i])
file.close()