# Write a Python program to count the frequency of words in a file.

def dictionCreate(list):
    dict = {}
    for i in list:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    print(dict)

file = open("Unit 3/P16.txt", 'w')
num = int(input("Enter the number of words: "))
for i in range(num):
    file.write(input("Enter a word: "))
    file.write(" ")
file.close()

file = open("Unit 3/P16.txt", 'r')
words = file.read()
word_list = words.split(" ")
dictionCreate(word_list)
file.close()