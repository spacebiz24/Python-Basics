# Write a program to create a class called Point with two attributes x and y. Write following functions and demonstrate the working of these functions by creating suitable objects.
# i. To read attribute values
# ii. To display point as an ordered pair
# iii. To find distance between two points

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def readXY():
        x = int(input("Enter x: "))
        y = int(input("Enter y: "))
        return Point(x, y)

    def displayXY(self):
        return self.x, self.y

    def distance(self, other):
        d = ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
        print("Distance is ", d)

P1 = Point(3, 4)
P2 = Point.readXY()
P1.displayXY()
P2.displayXY()
P2.distance(P1)
