#! /usr/bin/env python3

# A module for getting the smallest prime factor of an integer.

import sys


# This chunk of code is examining the user input to make sure a) a number is provided and b) that it is not zero or negative

# when you define functions, it should be done right after importing any modules and before any other code
# None is a built in python value that returns a null value. This is not the same as returning a zero

# functions should be placed after the modules are imported, but before the rest of the code down below

# a script for getting the smallest prime factor from an integer
def get_smallest_prime_factor(n):
    '''
    Returns the smallest integer that is a factor of 'n'.

    If 'n' is a prime number 'None' is returned

    Parameters
    ----------
    n : int 
        The integer to be factored
    
    Returns
    -------
    int or None
        The smallest integer that is a factor of 'n'
        or None if 'n is a prime.

    Example
    -------
    >>> get_smallest_prime_factor(7)
    >>> get_smallest_prime_factor(8)
    2
    >>> get_smallest_prime_factor(9)
    3
    
    '''
    for i in range(2, n):
        if (n % i) == 0:
            return i
    return None


# use the below if __name__ = '__main__' to parse the command line interface (CLI) from the functions above. Everything below this conditional is considered to be part of the command line and not part of the defined functions
# Be sure to fix indentation

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(sys.argv[0] + ": Expecting one command line argument -- the integer for which to get the smallest factor")
    n = int(sys.argv[1])
    if n < 1:
        sys.exit(sys.argv[0] + ": Expecting a positive integer")

    smallest_prime_factor = get_smallest_prime_factor(n)

    if smallest_prime_factor is None:
        print(n)
    else:
        print(smallest_prime_factor)
