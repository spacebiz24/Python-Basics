# Write a Python class to get all possible unique subsets from a set of distinct integers.

class Subsets:
    def __init__(self, array):
        self.array = array
    def get_subsets(self):
        subsets = [[]]
        for x in self.array:
            new_subsets = []
            for subset in subsets:
                new_subsets.append(subset + [x])
            subsets += new_subsets
        return subsets

s = [1, 2, 3]
S1 = Subsets(s)
subsets = S1.get_subsets()
print(subsets)