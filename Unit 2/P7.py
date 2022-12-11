# Write a function char_freq() that takes a string and builds a frequency listing of the characters contained in it. Represent the frequency listing as a python dictionary.

def char_freq(str):
    dict = {}
    for i in str:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    print(dict)
char_freq("Apple")