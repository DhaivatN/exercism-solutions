"Program to count number of steps it takes to reach 1 according to the rules of the Collatz Conjecture. "
def steps(number):
    """Function to count number of steps"""
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    counter = 0
    while number != 1:
        # print("entered loop")
        if number % 2 == 0:
            # number is even
            number /= 2
            # continue
        else:
            number = 3 * number + 1
        counter += 1
    return counter