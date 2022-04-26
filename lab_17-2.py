# Author: CRS 04/11/22
import math
# Create circle class
class Circle:
    # Define functions
    def __init__(self):
        self.radius = 3
    def get_diameter(self):
        return self.radius * 2
    def get_area(self):
        return math.pi * self.radius **2
    def get_perimeter(self):
        return 2 * math.pi * self.radius
# Test
my_circle = Circle()
print(my_circle.get_perimeter())