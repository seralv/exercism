def _valid_triangle(sides):
    a, b, c = sides
    return (
        len(sides) == 3 and
        all(side > 0 for side in sides) and
        a + b >= c and
        a + c >= b and
        b + c >= a
    )

def equilateral(sides):
    """Returns True if the triangle is equilateral (all sides equal)."""  
    return _valid_triangle(sides) and len(set(sides)) == 1

def isosceles(sides):
    """Returns True if the triangle is isosceles (at least two sides equals)."""
    return _valid_triangle(sides) and len(set(sides)) <= 2

def scalene(sides):
    """Returns True if the triangle is scalene (all sides are different)."""
    return _valid_triangle(sides) and len(set(sides)) == 3
