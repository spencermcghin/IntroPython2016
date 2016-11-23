"""

Tests for Circle Classes

"""

from Circle import Circle


def test_radius():
    c = Circle(4)
    assert c.radius == 4