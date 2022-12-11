# 2) Design and implement a program to count the number of individual characters in a string.
# Sample string:”yahoo.com”
# Result: {‘0’:3,’y’:1,’.’:1,’a’:1,’h’:1,’m’:1,’c’:1}

x = input("Enter a string: ")
dict = {}
for i in x:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1
print(dict)