from math import pi

class circle:
    def __init__(self,radius):
        self.radius = radius
        self.area = pi * (self.radius**2)
        self.diameter = 2 * self.radius
    def print_area(self):
        print(pi *(self.radius ** 2))
    def print_circumference(self):
        print(self.diameter * pi)
c1 = circle(5)
c2 = circle(10)
c1.print_area()
c2.print_area()
c1.print_circumference()
c2.print_circumference()