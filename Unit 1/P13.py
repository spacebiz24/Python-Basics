m = int(input("Enter the number of rows: "))
n = int(input("Enter the number of columns: "))
matrix = [[0 for col in range(n)] for row in range(m)]
for j in range(n):
    for i in range(m):
        matrix[i][j] = i * j
print(matrix)