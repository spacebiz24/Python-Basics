# If n is odd, then n = 3n + 1, else if n is even, then n = n / 2. This goes on until n is not equal to 1.


def Collatz(n):
    while n != 1:
        print(n, end="\t")
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
    print(n, end="\t")


x = int(input("Enter a number: "))
Collatz(x)
