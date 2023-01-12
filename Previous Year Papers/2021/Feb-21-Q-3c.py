# Write a Python program to combine two dictionary adding values for common keys. Consider d1 = {'a': 100, 'b': 200, 'c':300} and d2 = {'a': 300, 'b': 200, 'd':400}, Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})

d = {}
d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}
l = list(d1.keys())
l.extend(list(d2.keys()))
for i in l:
    d[i] = d.get(i, 0) + d1.get(i, 0) + d2.get(i, 0)

print(d)
