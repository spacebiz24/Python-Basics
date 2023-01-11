# Write a Python class to get all possible unique subsets from a set of distinct integers.

def get_subsets(array):
    subsets = [[]]
    for x in array:
        new_subsets = []
        for subset in subsets:
            new_subsets.append(subset + [x])
        subsets += new_subsets
    return subsets

s = [1, 2, 3]
subsets = get_subsets(s)
print(subsets)