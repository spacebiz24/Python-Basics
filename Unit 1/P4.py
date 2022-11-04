print("Triangle Type Definition")
print("  /|")
print("c/ |a")
print("/__|")
print("  b")
a = int(input("Enter side 'a' of the triangle: "))
b = int(input("Enter side 'b' of the triangle: "))
c = int(input("Enter side 'c' of the triangle: "))
if (a == b == c):
    print("Triangle is Equilateral")
elif (a == b or b == c or c == a):
    print("Triangle is Isosceles")
else:
    print("Triangle is Scalene")