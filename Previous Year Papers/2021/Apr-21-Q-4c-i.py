# Write Python code to create a function called most_frequent that takes a string and prints the letters in decreasing order of frequency. Use dictionaries.

def most_frequent(s):
    d = {}
    l = []
    for i in s:
        d[i] = d.get(i, 0) + 1
    l = list(d.items())
    for i in range(len(l)):
        for j in range(i - 1):
            if (l[j][1] < l[j + 1][1]):
                temp = l[j]
                l[j] = l[j + 1]
                l[j + 1] = temp
            else:
                continue
    d = {}
    for i in range(len(l)):
        d[l[i][0]] = l[i][1]
    return d

s = 'jokermancrybabypythonprogramminglifeisbutadream'

print(most_frequent(s))
