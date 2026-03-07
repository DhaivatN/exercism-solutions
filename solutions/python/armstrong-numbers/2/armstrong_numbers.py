"Program to check if number is armstrong number"
def is_armstrong_number(number):
    """
    check armstrong function
    """
    number_of_digits = len(str(number))
    total = 0
    number_slicing = number
    for _ in range(number_of_digits):
        current_digit = number_slicing % 10
        total += current_digit ** number_of_digits
        number_slicing //= 10
    return total == number    