# Write a Python program to add 'ing' at the end of a given string (length should be at least 3).If the given string already ends with 'ing' then add 'ly' instead. If the string length of the givenstring is less than 3, leave it unchanged
# Sample String : 'abc'
# Sample String : 'string'
# Expected Result : 'abcing'
# Expected Result : 'stringly'

x = input("Enter: ")
string = ""
if len(x) >= 3:
    if x[-3:] == "ing":
        string = x[:-3] + "ly"
    else:
        string = x[:-3] + "ing"
else:
    string = x

print(string)
