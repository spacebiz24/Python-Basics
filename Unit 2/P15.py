y = (1,2,3,4,5,6,7,8,9)
x = []
for i in y:
    if i % 2 == 0:
        x.append(i)
print("Edited Tuple is: ")
print(tuple(x))