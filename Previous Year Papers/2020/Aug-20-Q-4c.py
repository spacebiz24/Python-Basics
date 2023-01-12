# Write a python program to create a dictionary with key as first character and value as list of words starting with that character.
# Input : hi hello how are you
# Output :
# h : ['hi', 'hello', 'how']
# a : ['are']
# y : ['you']

s = 'hi hello how are you'
l = s.split(' ')
d = {}

for i in l:
    d[i[0]] = d.get(i[0], [])
    d[i[0]].append(i)

print(d)
