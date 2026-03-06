def equilateral(sides):
    if check_sides(sides):
        a, b, c = sides
        return a == b == c
    return False


def isosceles(sides):
    if check_sides(sides):
        a, b, c = sides
        return a == b or b == c or a == c
    return False

def scalene(sides):
    if check_sides(sides):
        a, b, c = sides
        return a != b and b != c and a != c
    return False
    
def check_sides(sides):
    a, b, c = sides
    return min(a, b, c) > 0 and (a + b) > c and (b + c) > a and (a + c) > b