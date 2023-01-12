# Write Python Program to get the File Name from user and find the longest Word in a File.

file = open("words.txt", "r")
longest = ""
for i in (file.read()).split():
    if len(longest) < len(i):
        longest = i
print(longest)
file.close()
