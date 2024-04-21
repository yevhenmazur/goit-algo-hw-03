"""Module providing a function for choosing random samples."""

import random

def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    """The function select certain number of random numbers from a given range"""
    if not isinstance(min, int) or not isinstance(max, int) or not isinstance(quantity, int):
        print("At least one of the arguments is not an integer. Check the input data is correct.")
        result = None
    elif min < 0 or max < 0 or quantity < 0:
        print("All arguments must be positive integers. Check the input data is correct.")
        result = None
    elif max <= min or quantity > max - min:
        print("The arguments have a false correlation. Check that max > min and quantity < (max - min)")
        result = None
    else:
        seq = tuple(range(min, max))
        result = random.sample(seq, quantity)
        result.sort()
    print(result)
    return result

### Uncomment section below to check the function
'''
INPUT_MIN = 1
INPUT_MAX = 20
INPUT_QUANTITY = 3

get_numbers_ticket(INPUT_MIN, INPUT_MAX, INPUT_QUANTITY)
'''