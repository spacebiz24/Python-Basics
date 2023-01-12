# Write a Python code to add two matrices using nested loops and also perform transpose of the resultant matrix
import copy

lst1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
lst2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

lst3 = [[0 for row in range(3)] for column in range(3)]
lst4 = copy.deepcopy(lst3)

for i in range(len(lst1)):
    for j in range(len(lst1[i])):
        lst3[i][j] = lst1[i][j] + lst2[i][j]  # Addition
        lst4[j][i] = lst3[i][j]  # Transpose

print(lst3)
print(lst4)
