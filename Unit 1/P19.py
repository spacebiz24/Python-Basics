# Write a Python program to check the validity of password input by users. Go to the editor 
# Validation :
# At least 1 letter between [a-z] and 1 letter between [A-Z].
# At least 1 number between [0-9].
# At least 1 character from [$#@].
# Minimum length 6 characters.
# Maximum length 16 characters

password = input("Enter the password: ")
slcount = 0
clcount = 0
ncount = 0
scount = 0
if len(password) <= 16 and len(password) >= 6:
    for i in password:
        if i.isupper():
            clcount += 1
        if i.islower():
            slcount += 1
        if i.isdigit():
            ncount += 1
        if i.isalnum() != 1:
            scount += 1
    if clcount > 0 and slcount > 0 and ncount > 0 and scount > 0:
        print("Password is valid")
    else:
        print("Password is invalid")