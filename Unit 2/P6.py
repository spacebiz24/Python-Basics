# Design and implement a program to count the number of vowels present in a given list of strings using ‘in’ or ‘not in’ operator.

list = ["apple", "orange", "banana", "kiwi", "pear", "cherry"]
dict = {
    "a":0,
    "e":0,
    "i":0,
    "o":0,
    "u":0
}
for i in list:
    for j in i:
        if j in dict:
            dict[j] += 1
print("The number of vowels are:")
print(dict)