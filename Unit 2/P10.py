str = input("Enter a string: ")
ucount = 0
lcount = 0
for i in str:
    if i.isupper():
        ucount += 1
    elif i.islower():
        lcount += 1
print("Number of Upper Case Characters: ", ucount)
print("Number of Lower Case Characters: ", lcount)