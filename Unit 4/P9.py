# Write a Python class to find a pair of elements (indices of the two numbers) from a given array whose sum equals a specific target number.

class pairnum:
    def __init__(self, list, target):
        self.target = target
        self.array = list
    def pairnum(self):
        for i in self.array:
            for j in self.array:
                if i + j == self.target and i != j:
                    print("Pair of numbers are: ", i, j)

list = [1,2,5,3,74,2,4]
num = pairnum(list, 75)
num.pairnum()