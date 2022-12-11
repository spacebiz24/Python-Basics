# Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.  
# Sample String : 'restart'
# Expected Result : 'resta$t'

str = input("Enter a string: ")
nstr = str[0]
for i in str[1:]:
    if(i == nstr[0]):
        nstr += "$"
    else:
        nstr += i
print("Edited String is: " + nstr)