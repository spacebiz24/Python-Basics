# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters. 
# Sample String : 'The quick Brown Fox'
# Expected Output : 
# No. of Upper case characters : 3
# No. of Lower case Characters : 13

def UpLowCount():
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
UpLowCount()