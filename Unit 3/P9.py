# Write a function that takes a list of integers, and returns the number of primes in the list.

def isPrime(num):
    i = num
    count = 0
    while i > 0:
        if num % i == 0:
            count += 1
        i -= 1
    if count == 2:
        return True

def primeList(list):
    nlist = []
    for i in list:
        if isPrime(i):
            nlist.append(i)
    print("Prime List:")
    print(nlist)

lst = [1,3,4,5,2,1,8,9]
primeList(lst)