# Author: CRS 04/11/22
import math
class Circle():
    def get_area(self, radius = 3):
        return math.pi * (radius ** 2)

Circle1 = Circle()
print(Circle1.get_area())
