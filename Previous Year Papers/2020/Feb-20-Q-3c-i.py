# Write a Python function rotatelist(ls,k) that takes a list ls and a positive integer k and returnsthe list ls after k rotations. If k is not positive, your function should return ls unchanged. Notethat your function should not change ls itself, and should return the rotated list.

def rotatelist(ls, k):
    lst = ls
    m = 0
    while m < k:
        temp = lst[len(lst) - 1]
        for i in range(len(lst) - 1, 0, -1):
            lst[i] = lst[i - 1]
        lst[0] = temp
        m += 1
    return lst

print(rotatelist([1, 2, 3, 4, 5], 2))
