# Define a class called TIME with instance variables hour, minute and seconds. Define constructor for initializing instance variables, method to convert integer value to time form(hour, minute, second), method to convert from time form to integer form. Overload the appropriate operators to perform the following operations and to display the objects.
# T3 = T1+T2
# T4 = T1+75
# T5 = 130+T1

class TIME:

    def __init__(self, h, m, s):
        self.h = h
        self.m = m
        self.s = s

    def t2i(self):
        return ((self.h * 3600) + (self.m * 60) + self.s)

    def i2t(x):
        return x // 3600, (x % 3600) // 60, (x % 60)

    def __add__(a, b):
        x = a.t2i()
        try:
            y = b.t2i()
        except:
            y = b
        (q1, q2, q3) = TIME.i2t(x + y)
        return TIME(q1, q2, q3)

T1 = TIME(2, 30, 10)
T2 = TIME(1, 20, 20)

print(T1.t2i())
print(TIME.i2t(9085))
T3 = T1 + T2
print(T3.h, T3.m, T3.s)
T4 = T1 + 75
print(T4.h, T4.m, T4.s)
# ERROR
# T5=130+T1
# print(T5)
