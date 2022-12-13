# a) Design and implement a python class named circle constructed by a radius and two methods which will compute the area and the perimeter of the circle.
# b) Implement a class called country, which represents a country with a name, a population, and an area. Define country with a constructor that has four parameters: country, name, population and its area.

class circle:
    def __init__(self, radius):
        self.radius = radius
        self.pi = 3.14159265
    def computeArea(self):
        return self.pi * self.radius ** 2
    def computeParameter(self):
        return 2 * self.pi * self.radius

c = circle(10)
area = c.computeArea()
perimeter = c.computeParameter()
print("Area is: ", area)
print("Perimeter is: ", perimeter)

class country:
    def __init__(self, name, pop, area):
        self.name = name
        self.population = pop
        self.area = area

india = country("India", 69420, 420)
print("Country name: ", india.name)
print("Country population: ", india.population)
print("Country area: ", india.area)