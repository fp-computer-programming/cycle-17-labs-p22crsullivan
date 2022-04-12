# Author: CRS 04/11/22
import math
class Circle():
    def get_area(radius):
        area = math.pi * (radius ** 2)
        return area

Circle1 = Circle()
Circle1.get_area(3)
print(Circle1)
