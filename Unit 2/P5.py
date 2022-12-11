# Design and implement a python program to find the list of words that are no longer than n from a given list of words.

words = ["apple", "orange", "banana", "kiwi", "pear", "cherry"]
num = int(input("Enter the limit on length of the string: "))
new_words = []
for i in words:
    if(len(i) <= num):
        new_words.append(i)
print(new_words)