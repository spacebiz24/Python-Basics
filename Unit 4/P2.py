# Design and implement a python program that describes the class rocket with its attributes as x and y values. Create a fleet of 5 rockets and display its x and y positions using suitable methods inside the class.

class rocket:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def getXYPosition(self):
        print("X coordinate is: ", self.x)
        print("Y coordinate is: ", self.y)
        print("\n")
r1 = rocket(1, 2)
r2 = rocket(2, 4)
r3 = rocket(3, 6)
r4 = rocket(4, 8)
r5 = rocket(5, 10)

r1.getXYPosition()
r2.getXYPosition()
r3.getXYPosition()
r4.getXYPosition()
r5.getXYPosition()