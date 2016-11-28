"""

Circle Lab

"""

from math import pi


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        print('%s(%r)' % (self.__class__, self.radius))

    def __repr__(self):
        return repr(self.radius)

    @property  # computes on the fly as opposed to storing init value
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, val):
        self.radius = val / 2

    @property
    def area(self):
        return self.radius ** 2 * pi

    @classmethod
    def from_diameter(cls, diameter=None):
        return diameter
