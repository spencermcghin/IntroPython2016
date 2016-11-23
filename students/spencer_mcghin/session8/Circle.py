"""

Circle Lab

"""

from math import pi


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property  # computes on the fly as opposed to storing init value
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, val):
        self.radius = val / 2

    @property
    def area(self):
        return self.radius ** 2 * math.pi
