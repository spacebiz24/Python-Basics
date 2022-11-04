str = input("Enter a string: ")
lcount = 0
dcount = 0
for i in str:
    if i.isalpha():
        lcount += 1
    if i.isdigit():
        dcount += 1
print("Letters ", lcount)
print("Digits ", dcount)