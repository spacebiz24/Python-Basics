# Write a program which count and print the numbers of each character in a string input by console.
# Example:
# If the following string is given as input to the program:
# abcdeabc
# Then, the output of the program should be:
# a,2   c,2   b,2   e,1   d,1

str = input("Enter a string: ")
dict = {}
for i in str:
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] += 1
for i in dict:
    print(i, ",", dict[i], end="\n")