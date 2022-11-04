str = input("Enter a string: ")
if(len(str) <= 2):
    nstr = ""
else:
    nstr = str[:2] + str[len(str)-2:]
print("New String is: ", nstr)