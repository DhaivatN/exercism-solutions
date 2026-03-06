def equilateral(sides):
    if check_sides(sides):
        side1, side2, side3 = sides
        return side1 == side2 == side3
    return False


def isosceles(sides):
    if check_sides(sides):
        side1, side2, side3 = sides
        return side1 == side2 or side2 == side3 or side1 == side3
    return False

def scalene(sides):
    if check_sides(sides):
        side1, side2, side3 = sides
        return side1 != side2 and side2 != side3 and side1 != side3
    return False
    
def check_sides(sides):
    a, b, c = sides
    return min(a, b, c) > 0 and (a + b) > c and (b + c) > a and (a + c) > b