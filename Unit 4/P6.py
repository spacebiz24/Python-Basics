# Write a Python class to find the three elements that sum to zero from a set of n real numbers.

class Zero:
    def __init__(self, list):
        self.list = list
    def zerocheck(self):
        for i in self.list:
            for j in self.list:
                for k in self.list:
                    if i + j + k == 0 and i != j != k:
                        print("The numbers which sum to zero: ", i, j, k)

list = [1, 2, 3, 4, 5, -1, 0]
zero = Zero(list)
zero.zerocheck()