# Write a Python program to count the number of even and odd numbers from a series of numbers.

list = [1,4,56,23,132,67,92,345]
ecount = ocount = 0
for i in list:
    if i % 2 == 0:
        ecount += 1
    else:
        ocount += 1
print("Even Count: ", ecount)
print("Odd Count: ", ocount)
