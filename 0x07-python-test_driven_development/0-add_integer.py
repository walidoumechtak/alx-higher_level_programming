#!/usr/bin/python3

"""calc the sum of two integer"""


def add_integer(a, b=98):
    """the body of sum
    Returns:
        addition of a and b
    """
    sum = 0
    boolb1 = isinstance(b, int)
    boolb2 = isinstance(b, float)
    boola1 = isinstance(a, int)
    boola2 = isinstance(a, float)
    if (boola1 or boola2) and (boolb1 or boolb2):
        sum = int(a) + int(b)
    else:
        if boola1 is False:
            raise TypeError("a must be an integer")
        elif not boolb1:
            raise TypeError("b must be an integer")
    return sum
