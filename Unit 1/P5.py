# Design and implement a python program that accepts an integer n and computes the value of n+nn+nnn

n = int(input("Enter a variable: "))
x = int(input("Enter the number of iterations: "))
sum = 0
for i in range(1, x + 1):
    sum += n ** i
print("Sum is: ", sum)