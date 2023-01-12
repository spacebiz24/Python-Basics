# Consider the string "Mississippi". Write Python code that implements and returns the functionality of histogram using dictionaries for the given string. Also, write the function print_hist() to print the keys and their values in alphabetical order from the values returned by the histogram function.

x = input("Enter a string: ")

def print_hist(diction):
    keys = list(diction.keys())
    keys.sort()
    sorted_dict = {i: diction[i] for i in keys}
    print(sorted_dict)

dict = {}
for i in x:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1

print_hist(dict)
