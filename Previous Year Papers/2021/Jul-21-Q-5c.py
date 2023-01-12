# Write Python Program to Reverse Each Word in “secrets.txt” file.

file = open("Python/secrets.txt", "r")
x = ""
for i in file.readlines():
    for j in i.split(" "):
        x += j[::-1] + " "
print(x)

file.close()
