str = input("Enter a string: ")
nstr = str[0]
for i in str[1:]:
    if(i == nstr[0]):
        nstr += "$"
    else:
        nstr += i
print("Edited String is: " + nstr)