#!/usr/bin/python3

def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a (int or float): The first integer or float.
        b (int or float, optional): The second integer or float. Defaults to 98.

    Returns:
        int: The sum of a and b as an integer.

    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if not (isinstance(a,(int, float))) and (isinstance(b,(int, float))):
        raise TypeError("a must be an integer" or "b must be an integer")

    if (isinstance(a,(int,float))) and (isinstance(b,(int,float))):
    a = int (a)
    b = int (b)

    return (a+b)

