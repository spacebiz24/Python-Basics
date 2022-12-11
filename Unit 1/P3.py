# Design and implement a program that evaluates the value of the quadratic equation ax2+bx+c by prompting the user to enter the values of a,b,c and x.

print("Quadratic Equation Solver:")
print("General form of a quadratic equation is 'ax^2 + bx + c'")
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
d = b ** 2 - 4 * a * c
sqrt_val = (abs(d)) ** 0.5
if d < 0:
    print("Imaginary roots exist:")
    print(- b / (2 * a), " +i", sqrt_val)
    print(- b / (2 * a), " -i", sqrt_val)
elif d > 0:
    print("Real and distinct roots exist:")
    print((- b + sqrt_val) / (2 * a))
    print((- b + sqrt_val) / (2 * a))
else:
    print("Real and equal roots exist:")
    print(-b / (2 * a))