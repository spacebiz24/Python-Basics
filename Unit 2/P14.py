str = input("Enter a string: ")
dict = {}
for i in str:
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] += 1
for i in dict:
    print(i, ",", dict[i], end="\n")