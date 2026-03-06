def equilateral(sides):
    if check_sides(sides):
        a, b, c = sides[0], sides[1], sides[2]
        return a == b == c
    return False


def isosceles(sides):
    if check_sides(sides):
        a, b, c = sides[0], sides[1], sides[2]
        return a == b or b == c or a == c
    return False

def scalene(sides):
    if check_sides(sides):
        a, b, c = sides[0], sides[1], sides[2]
        return a != b and b != c and a != c
    return False
    
def check_sides(sides):
    a, b, c = sides[0], sides[1], sides[2]
    if min(a, b, c) > 0:
        return (a + b) >= c and (b + c) >= a and (a + c) >= b
    return False