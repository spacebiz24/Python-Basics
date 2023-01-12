# Write a program to create a class by name "Points" with two properties 'x' and 'y' coordinates and perform scalar multiplication using operator overloading concept.

class Points:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def displayPoints(self):
        print(self.x, self.y)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Points(self.x * other, self.y * other)
        elif isinstance(other, Points):
            return Points(self.x * other.x, self.y * other.y)

P1 = Points(1, 3)
P2 = P1 * 4
P2.displayPoints()