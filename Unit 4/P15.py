# Write a Python class to find a pair of elements (indices of the two numbers) from a given array whose sum equals a specific target number
# Input: numbers= [10,20,10,40,50,60,70], target=50
# Output: 3, 4

class pairnum:
    def __init__(self, list, target):
        self.target = target
        self.array = list
    def pairnum(self):
        for i in range(len(self.array)):
            for j in range(len(self.array)):
                if self.array[i] + self.array[j] == self.target and self.array[i] != self.array[j]:
                    print("Indices of pair of numbers are: ", i, j)

list = [1,2,5,3,74,2,4]
num = pairnum(list, 75)
num.pairnum()