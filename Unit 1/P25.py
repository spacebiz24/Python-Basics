# Write a Python program to calculate the difference between the squared sum of first n natural numbers and the sum of squared first n natural numbers.

n = int(input("Enter the limit of natural numbers: "))
sqsum = 0
sum = 0
for i in range(1, n + 1):
    sqsum += i ** 2
    sum += i
diff = abs(sqsum - (sum ** 2))
print("Difference is: ", diff)