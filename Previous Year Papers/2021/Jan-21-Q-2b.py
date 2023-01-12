# Given an input string with the combination of the lower and upper case letters, arrange characters in such a way that they are sorted and all lowercase letters should come first followed by uppercase letters.
# Given: str1 = PyNaTive
# Expected Output: aeivyNPT

str = sorted(input("Enter a string containing lower and upper case characters: "))
strL = ""
strU = ""
for i in str:
    if i.islower():
        strL += i
    elif i.isupper():
        strU += i
strF = strL + strU
print(strF)
