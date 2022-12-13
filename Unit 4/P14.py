# Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle.

class Rectangle:
    def __init__(self, length, breadth):
        self.x = length
        self.y = breadth
    def computeArea(self):
        print("Area of rectangle: ", self.x * self.y)

rect = Rectangle(10, 10)
rect.computeArea()