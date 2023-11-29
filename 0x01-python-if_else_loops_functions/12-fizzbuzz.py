#!/usr/bin/python3

def fizzbuzz():
    """Print the numbers from 1 to 100 separated by a space.
    print Fizz instead of the number for multspls of 3
    print Buzz instead of the number for multpls of five
    print FizzBuzz instead of the number for mltpls of 3 n 5.
    """
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz ", end="")
        elif number % 3 == 0:
            print("Fizz ", end="")
        elif number % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(number), end="")
