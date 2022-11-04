x = int(input("Enter the number of numbers you want to give: "))
sum = 0
while (x > 0):
    a = int(input("Enter the number: "))
    if a <= 100:
        sum += a
    x -= 1
print("Sum is: ", sum)