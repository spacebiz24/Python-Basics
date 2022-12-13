# Write a Python class to implement pow(x, n).

class power:
    def __init__(self, x, n):
        self.x = x
        self.n = n
    def pow(self):
        return self.x ** self.n

pow = power(420, 69)
res = pow.pow()
print("Result is: ", res)