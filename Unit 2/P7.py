def char_freq(str):
    dict = {}
    for i in str:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    print(dict)
char_freq("Apple")