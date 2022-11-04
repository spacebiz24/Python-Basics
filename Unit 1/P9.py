t1 = 0
t2 = 1
print(t1, end = ", ")
print(t2, end = ", ")
i = 0
while (i < 50):
    t3 = t1 + t2
    print(t3, end = ", ")
    t1 = t2
    t2 = t3
    i += 1