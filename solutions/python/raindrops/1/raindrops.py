""""Program to get raindrop sound"""
def convert(number):
    "Corresponding function"
    result = ''
    # if divisible by 3
    if number % 3 == 0:
        result += "Pling"
    # if divisible by 5
    if number % 5 == 0:
        result += "Plang"
    # if divisible by 7
    if number % 7 == 0:
        result += "Plong"
    # store number as string
    if number % 3 != 0 and number % 5 != 0 and number % 7 != 0:
        result += str(number)

    return result