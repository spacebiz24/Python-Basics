# Write a Python program which takes two digits m (row) and n (column) as input and generates a two-dimensional array. The element value in the i-th row and j-th column of the array should be i*j. 
# Test Data : Rows = 3, Columns = 4 
# Expected Result : [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]]

m = int(input("Enter the number of rows: "))
n = int(input("Enter the number of columns: "))
matrix = [[0 for col in range(n)] for row in range(m)]
for j in range(n):
    for i in range(m):
        matrix[i][j] = i * j
print(matrix)